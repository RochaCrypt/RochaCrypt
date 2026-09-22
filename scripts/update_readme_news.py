#!/usr/bin/env python3
"""
update_readme_news.py — inject latest cybersecurity headlines into the profile README.

Fetches RSS feeds and rewrites the block between the CYBER-NEWS markers with a
clean list of: title (linked), a short summary and the source.
Author: Alexandre Rocha (github.com/RochaCrypt)
"""
import html
import re
import time
from datetime import datetime, timezone

import feedparser

FEEDS = [
    ("The Hacker News", "https://feeds.feedburner.com/TheHackersNews"),
    ("BleepingComputer", "https://www.bleepingcomputer.com/feed/"),
    ("Krebs on Security", "https://krebsonsecurity.com/feed/"),
    ("Dark Reading", "https://www.darkreading.com/rss.xml"),
    ("SecurityWeek", "https://www.securityweek.com/feed/"),
    ("The Record", "https://therecord.media/feed/"),
    ("CISA Advisories", "https://www.cisa.gov/cybersecurity-advisories/all.xml"),
]
MAX_ITEMS = 8
SUMMARY_LEN = 150
README = "README.md"
START = "<!-- CYBER-NEWS:START -->"
END = "<!-- CYBER-NEWS:END -->"

TAGS = re.compile(r"<[^>]+>")
WS = re.compile(r"\s+")


def clean_summary(text):
    if not text:
        return ""
    text = html.unescape(TAGS.sub(" ", text))
    text = WS.sub(" ", text).strip()
    if len(text) > SUMMARY_LEN:
        cut = text[:SUMMARY_LEN].rsplit(" ", 1)[0]
        text = cut.rstrip(".,;:") + "…"
    return text


def clean_title(text):
    text = WS.sub(" ", html.unescape(text or "")).strip()
    return text.replace("[", "(").replace("]", ")")


def date_of(entry):
    for key in ("published_parsed", "updated_parsed"):
        t = entry.get(key)
        if t:
            return datetime.fromtimestamp(time.mktime(t), tz=timezone.utc)
    return None


def collect():
    items = []
    for source, url in FEEDS:
        try:
            feed = feedparser.parse(url)
        except Exception as exc:  # noqa: BLE001
            print(f"[!] {source}: {exc}")
            continue
        for e in feed.entries[:12]:
            title = clean_title(e.get("title"))
            link = (e.get("link") or "").strip()
            if not title or not link:
                continue
            items.append({
                "title": title,
                "url": link,
                "source": source,
                "summary": clean_summary(e.get("summary") or e.get("description")),
                "date": date_of(e),
            })
        print(f"[+] {source}: ok")
    items.sort(key=lambda x: x["date"] or datetime.min.replace(tzinfo=timezone.utc),
               reverse=True)
    return items[:MAX_ITEMS]


def build_block(items):
    lines = []
    for it in items:
        lines.append(f"**[{it['title']}]({it['url']})**  ")
        if it["summary"]:
            lines.append(f"{it['summary']}  ")
        lines.append(f"<sub>`{it['source']}`</sub>")
        lines.append("")
    return "\n".join(lines).rstrip()


def main():
    items = collect()
    if not items:
        print("[!] No items fetched; leaving README unchanged.")
        return
    block = build_block(items)

    with open(README, encoding="utf-8") as fh:
        content = fh.read()

    if START not in content or END not in content:
        print(f"[!] Markers not found in {README}.")
        return

    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    replacement = f"{START}\n\n{block}\n\n{END}"
    new = pattern.sub(replacement, content)

    if new == content:
        print("[=] No change.")
        return
    with open(README, "w", encoding="utf-8") as fh:
        fh.write(new)
    print(f"[+] Updated README with {len(items)} headlines.")


if __name__ == "__main__":
    main()
