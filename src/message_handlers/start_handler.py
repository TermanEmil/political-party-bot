from telegram import Update
from telegram.ext import ContextTypes


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = '\n'.join([
        f'Acest bot ofera informatii despre partidul politic MAN',
        f'Pentru a schimba limba acceseaza /limba',
        f'Чтобы изменить язык, выберите /limba',
    ])

    await update.message.reply_text(text)