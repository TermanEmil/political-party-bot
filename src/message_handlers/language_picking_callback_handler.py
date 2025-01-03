from telegram import Update
from telegram.ext import ContextTypes


async def language_picking_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query

    if not query:
        return

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    if query.data == 'language-ro':
        text = 'Ați ales limba română'
    else:
        text = 'Вы выбрали русский язык'

    await query.from_user.send_message(text=text)
