# Local Telegram Bot With FastAPI & Ngrok

_By FarukOzderim_

## Description

An easy start for a telegram bot. This bot returns messages to the sender immediately.

## Configure

- Create your bot and get your bot_token from @BotFather in telegram.
- Add your bot_token to the code, main.py as your secret.
- Run ngrok in terminal and get your public https url.

```
ngrok http 9000
```

- Import build_telegram_bot.json with postman.
- Add your **token** and **url** from postman to Environments.
- Use telegram api setWebHookInfo to set your bot url.

## Run

```
uvicorn src.main:app --reload --port 9000
```

#
