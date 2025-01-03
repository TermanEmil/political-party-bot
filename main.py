import asyncio
import os
import functions_framework

from src.update_handler import handle_bot_request


async def _handle_async(request_json):
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    await handle_bot_request(bot_token, request_json)
    return {"statusCode": 200}


@functions_framework.http
def telegram_bot_message_handler(request):
    request_json = request.get_json(silent=True)
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError as e:
        if str(e).startswith('There is no current event loop in thread'):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        else:
            raise

    return loop.run_until_complete(_handle_async(request_json))