import time

from parser import get_cards
from filters import check_card
from telegram import send
from database import load_seen, save_seen
from config import CHECK_INTERVAL, PRICE_LIMITS

seen = load_seen()

print("=" * 60)
print("🚀 AVITO HUNTER 4.0")
print("=" * 60)

while True:

    try:

        print("\n🔍 Проверяю Авито...")

        cards = get_cards()

        print(f"📦 Получено объявлений: {len(cards)}")

        sent = 0
        skipped = 0

        for index, card in enumerate(cards, start=1):

            print("-" * 60)
            print(f"[{index}/{len(cards)}]")
            print(f"📱 {card['title']}")
            print(f"💰 {card['price']:,} ₽")

            link = card["link"]

            if link in seen:
                print("⏭ Уже было отправлено")
                skipped += 1
                continue

            ok, model = check_card(
                card["title"],
                card["price"],
                card["text"]
            )

            if not ok:
                print("❌ Не подходит")
                skipped += 1
                continue

            print("✅ Подходит!")

           limit = PRICE_LIMITS[model]
      profit = limit - card["price"]

message = f"""🔥 НАЙДЕН ВЫГОДНЫЙ IPHONE

📱 {card['title']}

💰 Цена: {card['price']:,} ₽

💵 Экономия: {profit:,} ₽

🏷 Модель: {model}

🚚 Авито Доставка

🔗 {card['link']}
"""

            send(message)

            seen.add(link)

            sent += 1

            print("📨 Отправлено в Telegram")

            time.sleep(1)

        save_seen(seen)

        print("\n" + "=" * 60)
        print(f"✅ Отправлено: {sent}")
        print(f"⏭ Пропущено: {skipped}")
        print("=" * 60)

    except Exception as e:
        print("❌ Ошибка:", e)

    print(f"\n⏳ Следующая проверка через {CHECK_INTERVAL} секунд...\n")

    time.sleep(CHECK_INTERVAL)