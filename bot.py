import os
import requests
import feedparser

from config import KEYWORDS
from sources import RSS_FEEDS
from filters import is_high_impact
from category import get_category

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

SENT_FILE = "sent_links.txt"

# Load already sent links
sent_links = set()

if os.path.exists(SENT_FILE):
    with open(SENT_FILE, "r", encoding="utf-8") as f:
        sent_links = set(line.strip() for line in f if line.strip())

for feed in RSS_FEEDS:
    try:
        d = feedparser.parse(feed)

        for entry in d.entries:

            title = entry.get("title", "").strip()
            link = entry.get("link", "").strip()

            if not title or not link:
                continue

            # Skip duplicate
            if link in sent_links:
                continue

            # Keyword filter
            if not any(k.lower() in title.lower() for k in KEYWORDS):
                continue

            category = get_category(title)

            if is_high_impact(title):
                text = (
                    "🚨 *MARKET FAST NEWS*\n\n"
                    "🔥 *HIGH IMPACT*\n\n"
                    f"📂 {category}\n\n"
                    f"📰 {title}\n\n"
                    f"🔗 {link}"
                )
            else:
                text = (
                    "🚨 *MARKET FAST NEWS*\n\n"
                    f"📂 {category}\n\n"
                    f"📰 {title}\n\n"
                    f"🔗 {link}"
                )

            response = requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={
                    "chat_id": CHAT_ID,
                    "text": text,
                    "parse_mode": "Markdown"
                },
                timeout=20
            )

            print(response.status_code)

            if response.status_code == 200:
                sent_links.add(link)

    except Exception as e:
        print(f"Feed Error: {e}")

# Save sent links
with open(SENT_FILE, "w", encoding="utf-8") as f:
    for link in sorted(sent_links):
        f.write(link + "\n")
