from config import PRICE_LIMITS, BAD_WORDS


def normalize(text: str) -> str:
    return text.lower().replace("ё", "е").strip()


def check_card(title, price, text):

    title = normalize(title)
    text = normalize(text)

    full_text = f"{title}\n{text}"

    # Плохие слова
    for word in BAD_WORDS:
        if normalize(word) in full_text:
            return False, None, "Плохое слово"

    # Проверка моделей
    for model, limit in sorted(
        PRICE_LIMITS.items(),
        key=lambda x: len(x[0]),
        reverse=True
    ):

        if model in title:

            if price > limit:
                return False, model, "Дороже лимита"

            diff = limit - price

            if diff >= 7000:
                status = "💎 СУПЕР ЦЕНА"
            elif diff >= 3000:
                status = "🔥 Очень выгодно"
            elif diff >= 1000:
                status = "✅ Выгодно"
            else:
                status = "📱 Подходит"

            return True, model, status

    return False, None, "Модель не найдена"