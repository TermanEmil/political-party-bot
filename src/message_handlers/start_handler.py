from telegram import Update
from telegram.ext import ContextTypes


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = '\n'.join([
        f'Hello world',
        f'Meow Meow'
    ])

    await update.message.reply_text(text)