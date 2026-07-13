import os
import requests
import feedparser
from category import get_category
from config import KEYWORDS
from sources import RSS_FEEDS
from filters import is_high_impact

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

SENT_FILE = "sent_links.txt"

# Load sent links
if os.path.exists(SENT_FILE):
    with open(SENT_FILE, "r") as f:
        sent_links = set(line.strip() for line in f)
else:
    sent_links = set()

for feed in RSS_FEEDS:
    try:
        d = feedparser.parse(feed)

        for entry in d.entries:
            title = entry.title
            link = entry.link
            category = get_category(title)
            if link in sent_links:
                continue

            if any(k.lower() in title.lower() for k in KEYWORDS):

                if is_high_impact(title):
                    text = (
    "🚨 *MARKET FAST NEWS*\n\n"
    f"📂 {category}\n\n"
    "🚨 *HIGH IMPACT*\n\n"
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
                    }
                )

                print(response.status_code)

                sent_links.add(link)

    except Exception as e:
        print(e)

with open(SENT_FILE, "w") as f:
    for link in sent_links:
        f.write(link + "\n")
