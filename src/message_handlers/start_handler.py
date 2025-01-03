from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = '\n'.join([
        f'Alegeti limba',
        f'Выбрать язык'
    ])

    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton('RO', callback_data='language-ro'),
        InlineKeyboardButton('РУ', callback_data='language-ru'),
    ]])
    await update.message.reply_text(text, reply_markup=keyboard)