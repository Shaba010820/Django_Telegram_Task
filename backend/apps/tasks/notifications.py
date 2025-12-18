import httpx
from django.conf import settings


def send_telegram_message(telegram_id: int, text: str) -> None:
    if not settings.BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is not set")

    url = f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": telegram_id,
        "text": text,
    }

    httpx.post(url, json=payload, timeout=10)