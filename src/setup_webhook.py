from telegram.ext import Application


async def setup_webhook(bot_token: str, url: str):
    application = Application.builder().token(bot_token).build()
    await application.bot.set_webhook(url=url)