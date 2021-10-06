from fastapi import FastAPI, Request

from .validations import MessageBodyModel, ResponseToMessage

app = FastAPI()

# webhook_security = OnlyTelegramNetworkWithSecret(real_secret="your-secret-from-config-or-env")
# TODO: possible upgrades
#  - move {secret} to path
#  - use OnlyTelegramNetworkWithSecret as dependency:
secret = ""  # your secret
chat_id = 8611260527  # you can define a constant chat_id
group_chat_id = -4859830032  # or you can define a constant group_chat_id


@app.post('/webhook/{secret}')
async def post_process_telegram_update(message: MessageBodyModel, request: Request):
    # print(await request.json())
    # print(message)
    return ResponseToMessage(**{
        "text": "Copy paste:\n\n" + message.message.text,
        "chat_id": message.message.chat.id,
    })
