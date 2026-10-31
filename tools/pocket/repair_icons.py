#!/usr/bin/env python3
"""Fill and normalize Pocket vocabulary art while preserving SVG identity.

Pocket stores a vocabulary card as [English, Portuguese, icon, example, pt].
The icon value is an emoji key in data/pk-icons.json; pocket.js replaces that
key with the matching inline SVG.  This tool handles the final data pass after
human/agent edits: it fills empty values, replaces emoji that are not in the
catalogue, and mirrors the result into the wrap sticker cards.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEVELS = ("a1", "a2", "b1")

# The catalogue contains many more keys; these are deliberately common,
# recognizable SVGs for lexical families that occur throughout Pocket.
FALLBACK = ["💬", "📚", "📝", "💡", "⭐", "🔑", "🎯", "🧠", "🤝", "👀", "👂", "🗣️", "📍", "🌎", "🏠", "💼", "📅", "🛒", "🚗", "✈️", "🚌", "🍽️", "💰", "🎵", "🎨", "🧩"]
RULES = [
    (("airport", "flight", "plane", "travel", "trip", "luggage", "passport", "boarding"), "✈️"),
    (("bus", "train", "subway", "station", "ticket", "traffic", "drive", "car", "road", "street"), "🚌"),
    (("food", "meal", "breakfast", "lunch", "dinner", "cook", "kitchen", "restaurant", "coffee", "tea", "bread"), "🍽️"),
    (("money", "price", "cost", "pay", "cash", "bank", "budget", "cheap", "expensive", "dollar", "bill"), "💰"),
    (("school", "class", "study", "learn", "lesson", "teacher", "student", "exam", "homework", "course"), "📚"),
    (("work", "job", "office", "career", "meeting", "project", "email", "report", "manager", "apply"), "💼"),
    (("health", "doctor", "hospital", "medicine", "pain", "sick", "care", "body", "stomach", "sleep"), "🩺"),
    (("home", "house", "room", "bed", "door", "kitchen", "garden", "clean", "move"), "🏠"),
    (("music", "song", "sing", "sound", "voice", "listen", "dance", "movie", "film", "art", "paint"), "🎵"),
    (("book", "read", "write", "word", "letter", "story", "page", "text", "language", "say"), "📖"),
    (("family", "friend", "people", "together", "neighbor", "community", "welcome", "meet", "help"), "🤝"),
    (("weather", "rain", "sun", "cold", "hot", "snow", "wind", "summer", "winter", "spring"), "☀️"),
    (("place", "city", "country", "map", "near", "far", "direction", "corner", "address"), "📍"),
    (("phone", "mobile", "computer", "online", "website", "internet", "message", "call", "screen"), "📱"),
    (("game", "play", "sport", "ball", "team", "win", "run", "walk", "swim"), "🎯"),
]
BAD = {"🩷": "❤️", "🛞": "🚗", "🫘": "🍽️", "🫙": "🧺", "🛟": "🆘", "🪼": "🐟", "🪸": "🌊", "🪪": "🪪", "🫃": "🩺", "🪽": "🕊️", "🩶": "⚪", "🪹": "🌳", "🫳": "✋", "🛝": "🎠", "🫧": "💧", "🩻": "🩺"}

def choose(word: str, pt: str, example: str, catalog: set[str], seed: str) -> str:
    raw = " ".join((word, pt, example)).lower()
    if word in BAD and BAD[word] in catalog:
        return BAD[word]
    for terms, icon in RULES:
        if icon in catalog and any(re.search(r"\b" + re.escape(term) + r"\b", raw) for term in terms):
            return icon
    pool = [x for x in FALLBACK if x in catalog]
    h = int(hashlib.sha256(seed.encode("utf-8")).hexdigest()[:8], 16)
    return pool[h % len(pool)] if pool else next(iter(catalog))

def main() -> None:
    catalog = set(json.loads((ROOT / "data/pk-icons.json").read_text(encoding="utf-8")))
    stats = {lv: [0, 0] for lv in LEVELS}
    for lv in LEVELS:
        for path in sorted((ROOT / "data").glob(f"pk-{lv}_*.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            for episode in data:
                vocab_icons: dict[str, str] = {}
                for frame in episode.get("fr", []):
                    if frame.get("k") != "pkvoc":
                        continue
                    for i, card in enumerate(frame.get("cards", [])):
                        if len(card) < 5:
                            continue
                        word, pt, old = str(card[0]), str(card[1]), str(card[2]).strip()
                        icon = old if old in catalog else choose(word, pt, str(card[3]), catalog, f"{episode.get('n')}:{word}")
                        if not old or old not in catalog:
                            card[2] = icon
                        vocab_icons[word.lower()] = icon
                        stats[lv][0] += 1
                        stats[lv][1] += int(bool(card[2]))
                # Sticker cards mirror vocabulary cards. Keep the same SVG key.
                for frame in episode.get("fr", []):
                    if frame.get("k") == "pkread":
                        for i, part in enumerate(frame.get("pars", [])):
                            icon = str(part.get("ic", "")).strip()
                            if icon and icon not in catalog:
                                text = " ".join(str(x) for x in (part.get("lead", []) + part.get("q", [])))
                                part["ic"] = choose(icon, "", text, catalog, f"{episode.get('n')}:read:{i}")
                    if frame.get("k") != "wrap":
                        continue
                    for card in frame.get("stickers", []):
                        if len(card) >= 3:
                            icon = vocab_icons.get(str(card[0]).lower())
                            if icon:
                                card[2] = icon
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for lv, (total, filled) in stats.items():
        print(f"{lv}: {filled}/{total}")

if __name__ == "__main__":
    main()
