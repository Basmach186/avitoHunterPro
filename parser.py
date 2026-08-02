from playwright.sync_api import sync_playwright

SEARCHES = [
    "iPhone 12",
    "iPhone 12 Pro",
    "iPhone 12 Pro Max",
    "iPhone 13",
    "iPhone 13 Pro",
    "iPhone 13 Pro Max",
    "iPhone 14",
    "iPhone 14 Plus",
    "iPhone 14 Pro",
    "iPhone 14 Pro Max",
    "iPhone 15",
    "iPhone 15 Plus",
    "iPhone 15 Pro",
    "iPhone 15 Pro Max",
]


def get_cards():
    result = []

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--start-maximized"
            ]
        )

        page = browser.new_page()

        page.set_viewport_size({"width": 1400, "height": 900})

        print("\n====================================")
        print("🚀 AVITO HUNTER")
        print("====================================\n")

        for search in SEARCHES:

            url = f"https://www.avito.ru/rossiya/telefony?q={search.replace(' ', '+')}"

            print(f"🔎 Поиск: {search}")

            try:
                page.goto(
                    url,
                    wait_until="domcontentloaded",
                    timeout=30000
                )

                page.wait_for_selector(
                    'div[data-marker="item"]',
                    timeout=5000
                )

            except:
                print("❌ Страница не загрузилась")
                continue

            cards = page.locator('div[data-marker="item"]')

            count = cards.count()

            print(f"📦 Найдено: {count}")

            for i in range(count):

                card = cards.nth(i)

                try:
                    title = card.locator("h3").inner_text().strip()
                except:
                    continue

                try:
                    href = card.locator("a").first.get_attribute("href")
                except:
                    continue

                if not href:
                    continue

                if href.startswith("/"):
                    href = "https://www.avito.ru" + href

                try:
                    price_text = card.locator('[itemprop="price"]').inner_text()
                except:
                    continue

                digits = "".join(filter(str.isdigit, price_text))

                if digits == "":
                    continue

                price = int(digits)

                text = card.inner_text().lower()

# Пропускаем магазины
                if "магазин" in text:
                    continue

                if "компания" in text:
                    continue

                if "официальный продавец" in text:
                    continue

                if "доставка" not in text:
                    continue

# Только свежие объявления
                if "вчера" in text:
                    continue

                if "позавчера" in text:
                    continue

                # Переходим в объявление
try:
    detail = browser.new_page()
    detail.goto(href, wait_until="domcontentloaded", timeout=30000)
    detail.wait_for_timeout(1500)

    full_text = detail.locator("body").inner_text().lower()

    detail.close()

except:
    full_text = text

result.append({
    "title": title,
    "price": price,
    "text": full_text,
    "link": href
})

        browser.close()

    print(f"\n✅ Всего карточек после фильтра: {len(result)}\n") 

    print(f"✅ Подходит: {title} | {price:,} ₽")
    return result