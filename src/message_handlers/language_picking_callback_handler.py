from telegram import Update
from telegram.ext import ContextTypes

from src.message_handlers import language


async def language_picking_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    if not query or query.data not in [language.ro, language.ru]:
        return

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    if query.data == language.ro:
        text = 'Ați ales limba română'
    else:
        text = 'Вы выбрали русский язык'

    await query.from_user.send_message(text=text)

    # Won't work as long as there isn't a db to save this
    context.user_data['language'] = query.data
