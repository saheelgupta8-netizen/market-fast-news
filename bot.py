import os
import requests
import feedparser

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

feeds = [
    "https://www.moneycontrol.com/rss/business.xml",
    "https://www.cnbctv18.com/commonfeeds/v1/eng/rss/market/rss.xml"
]

keywords = [
    "solar", "vikram", "waaree", "renewable",
    "defence", "bel", "bdl", "hal", "mazagon", "aequs"
]

news = []

for feed in feeds:
    try:
        d = feedparser.parse(feed)
        for entry in d.entries:
            title = entry.title
            link = entry.link
            if any(k.lower() in title.lower() for k in keywords):
                news.append(f"📰 {title}\n{link}")
    except:
        pass

if news:
    text = "\n\n".join(news[:10])
else:
    text = "❌ No new Solar/Defence news found."

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={"chat_id": CHAT_ID, "text": text}
)
