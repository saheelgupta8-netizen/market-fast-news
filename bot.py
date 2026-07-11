import os
import requests
import feedparser
from config import KEYWORDS
from sources import RSS_FEEDS
from filters import is_high_impact
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

    if is_high_impact(title):
        news.append(
            f"🚨 HIGH IMPACT\n"
            f"📰 {title}\n"
            f"🔗 {link}"
        )
    else:
        news.append(
            f"📰 {title}\n"
            f"🔗 {link}"
        )
    except Exception as e:
        print(e)

if news:
    text = (
        "🚨 *MARKET FAST NEWS*\n"
        "━━━━━━━━━━━━━━\n\n"
        + "\n\n".join(news[:10])
    )
else:
    text = "No new Solar/Defence news found."

response = requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
)

print(response.status_code)
print(response.text)
