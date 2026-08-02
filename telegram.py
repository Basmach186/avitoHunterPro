import requests
from datetime import datetime
from config import BOT_TOKEN, CHAT_ID


API = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send(title, price, model, status, link):

    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    text = (
        f"🔥 <b>{status}</b>\n\n"
        f"📱 <b>{title}</b>\n\n"
        f"💰 <b>Цена:</b> {price:,} ₽\n"
        f"📲 <b>Модель:</b> {model.title()}\n"
        f"🚚 <b>Авито Доставка</b>\n"
        f"🕒 <b>Найдено:</b> {now}\n\n"
        f"<a href=\"{link}\">🔗 Открыть объявление</a>"
    )

    try:
        requests.post(
            f"{API}/sendMessage",
            data={
                "chat_id": CHAT_ID,
                "text": text,
                "parse_mode": "HTML",
                "disable_web_page_preview": False,
            },
            timeout=15,
        )
    except Exception as e:
        print("Telegram error:", e)


def send_text(text):

    try:
        requests.post(
            f"{API}/sendMessage",
            data={
                "chat_id": CHAT_ID,
                "text": text,
                "parse_mode": "HTML",
            },
            timeout=15,
        )
    except Exception as e:
        print("Telegram error:", e)