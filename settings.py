import json
import os

SETTINGS_FILE = "settings.json"


DEFAULT_SETTINGS = {
    "bot_token": "",
    "chat_id": "",

    "interval": 20,
    "delivery_only": True,

    "price_limits": {
        "iphone 12": 8000,
        "iphone 12 pro": 12000,
        "iphone 12 pro max": 15000,

        "iphone 13": 16000,
        "iphone 13 pro": 18000,
        "iphone 13 pro max": 21000,

        "iphone 14": 17000,
        "iphone 14 plus": 25000,
        "iphone 14 pro": 25000,
        "iphone 14 pro max": 28000,

        "iphone 15": 28000,
        "iphone 15 plus": 32000,
        "iphone 15 pro": 38000,
        "iphone 15 pro max": 45000
    },

    "bad_words": [
        "копия",
        "реплика",
        "восстановленный",
        "реф",
        "ref",
        "icloud",
        "заблок",
        "не работает",
        "разбит",
        "трещина",
        "скол",
        "донор",
        "на запчасти",
        "ремонт",
        "после ремонта",
        "без face id",
        "face id не работает",
        "нет true tone",
        "true tone отсутствует",
        "не включается",
        "аккаунт",
        "mdm"
    ]
}


def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS.copy()

    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_settings(settings):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(
            settings,
            f,
            ensure_ascii=False,
            indent=4
        )


settings = load_settings()