from os import environ
from sys import exit

from fastapi import FastAPI, Request
import asyncio
import uvicorn

from pyngrok import ngrok
from httpx import AsyncClient

from validations import MessageBodyModel, ResponseToMessage

app = FastAPI()

# webhook_security = OnlyTelegramNetworkWithSecret(real_secret="your-secret-from-config-or-env")
# TODO: possible upgrades
#  - move {secret} to path
#  - use OnlyTelegramNetworkWithSecret as dependency:
TOKEN = environ.get("TELEGRAM_TOKEN", "")
TELEGRAM_SEND_MESSAGE_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
TELEGRAM_SET_WEBHOOK_URL = f"https://api.telegram.org/bot{TOKEN}/setWebhook"
HOST_URL = None

if TOKEN == "":
    exit("No secret found, exiting now!")


@app.post("/webhook/{TOKEN}")
async def post_process_telegram_update(message: MessageBodyModel, request: Request):
    # print(await request.json())
    # print(message)
    return ResponseToMessage(
        **{
            "text": "Copy paste:\n\n" + message.message.text,
            "chat_id": message.message.chat.id,
        }
    )


async def request(url: str, payload: dict, debug: bool = False):
    async with AsyncClient() as client:
        request = await client.post(url, json=payload)
        if debug:
            print(request.json())
        return request


async def send_a_message_to_user(telegram_id: int, message: str) -> bool:
    message = ResponseToMessage(
        **{
            "text": message,
            "chat_id": telegram_id,
        }
    )
    req = await request(TELEGRAM_SEND_MESSAGE_URL, message.dict())
    return req.status_code == 200


async def set_telegram_webhook_url() -> bool:
    payload = {"url": f"{HOST_URL}/webhook/{TOKEN}"}
    req = await request(TELEGRAM_SET_WEBHOOK_URL, payload)
    return req.status_code == 200


if __name__ == "__main__":
    PORT = 8000
    http_tunnel = ngrok.connect(PORT, bind_tls=True)
    public_url = http_tunnel.public_url
    HOST_URL = public_url

    loop = asyncio.get_event_loop()
    success = loop.run_until_complete(set_telegram_webhook_url())
    if success:
        uvicorn.run("main:app", host="127.0.0.1", port=PORT, log_level="info")
    else:
        print("Fail, closing the app.")
