import asyncio
import os

import uvicorn
from dotenv import load_dotenv
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Route

from src.setup_webhook import setup_webhook
from src.update_handler import handle_bot_request

# Take environment variables from .env
load_dotenv()


async def main() -> None:
    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    url = os.environ.get("NGROK_WEBSERVER_URL")
    await setup_webhook(bot_token=bot_token, url=f"{url}/telegram")

    async def telegram_endpoint(request: Request) -> Response:
        message = await request.json()
        await handle_bot_request(bot_token, message)
        return Response()

    # noinspection PyTypeChecker
    starlette_app = Starlette(
        routes=[
            Route("/telegram", telegram_endpoint, methods=["POST"]),
        ],
        middleware=[
            Middleware(CORSMiddleware, allow_origins=['*'])
        ],
    )

    webserver = uvicorn.Server(
        config=uvicorn.Config(
            port=5000,
            use_colors=False,
            host="127.0.0.1",
            app=starlette_app,
        )
    )

    # Run application and webserver together
    await webserver.serve()


if __name__ == "__main__":
    asyncio.run(main())