import os
import requests
import feedparser
from config import KEYWORDS, RSS_FEEDS
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]




news = []

for feed in RSS_FEEDS:
    try:
        d = feedparser.parse(feed)
        for entry in d.entries:
            title = entry.title
            link = entry.link
            if any(k.lower() in title.lower() for k in KEYWORDS):
                news.append(f"📰 {title}\n{link}")
    except:
        pass

response = requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True
    }
)
response = requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": text}
)

print(response.status_code)
print(response.text)
