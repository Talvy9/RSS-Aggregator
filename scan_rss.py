import feedparser

with open("RSS.txt", "r") as f:
    feeds = [line.strip() for line in f if line.strip()]

for feed_url in feeds:
    print("=" * 80)
    print(f"Feed: {feed_url}")

    feed = feedparser.parse(feed_url)

    for entry in feed.entries[:5]:
        print(f"- {entry.get('title', 'No title')}")
        print(f"  {entry.get('link', '')}")
