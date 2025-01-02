from typing import Optional

from telegram import Update
from telegram.ext import Application, CommandHandler

from src.message_handlers.start_handler import start_handler
from src.utils.bot_utils import stringify
from src.utils.logger import logger
from src.utils.stopwatch import Stopwatch


def _extract_user_id(message_data: dict) -> Optional[int]:
    if 'message' in message_data:
        key = 'message'
    else:
        return None

    return message_data[key]['from']['id']


async def handle_bot_request(bot_token: str, message_data: dict):
    user_id = _extract_user_id(message_data)
    if user_id is None:
        return

    logger.info(f'Handling bot request for user {user_id}')

    application = Application.builder() \
        .token(bot_token) \
        .build()

    application.add_handler(CommandHandler("start", start_handler))

    on_finish = lambda delta: logger.info(f'User {user_id}: Request handling finished in {delta} seconds.')
    with Stopwatch(on_finish=on_finish):
        async with application:
            update = Update.de_json(data=message_data, bot=application.bot)
            readable_update = stringify(update)
            logger.info(f'User {user_id}: Processing request: {readable_update}.')
            await application.process_update(update)
