from typing import Optional

from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

from src.message_handlers.about_handler import about_handler
from src.message_handlers.party_agenda_handler import party_agenda_handler
from src.message_handlers.pick_language_handler import pick_language_handler, pick_language_callback_handler
from src.message_handlers.start_handler import start_handler
from src.utils.bot_utils import stringify
from src.utils.logger import logger
from src.utils.stopwatch import Stopwatch


def _extract_user_id(message_data: dict) -> Optional[int]:
    if 'message' in message_data:
        key = 'message'
    elif 'inline_query' in message_data:
        key = 'inline_query'
    elif 'callback_query' in message_data:
        key = 'callback_query'
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
    application.add_handler(CommandHandler("limba", pick_language_handler))
    application.add_handler(CallbackQueryHandler(pick_language_callback_handler))

    application.add_handler(CommandHandler("about", about_handler))
    application.add_handler(CommandHandler("agenda", party_agenda_handler))


    on_finish = lambda delta: logger.info(f'User {user_id}: Request handling finished in {delta} seconds.')
    with Stopwatch(on_finish=on_finish):
        async with application:
            update = Update.de_json(data=message_data, bot=application.bot)
            readable_update = stringify(update)
            logger.info(f'User {user_id}: Processing request: {readable_update}.')
            await application.process_update(update)
