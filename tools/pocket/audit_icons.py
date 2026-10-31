#!/usr/bin/env python3
"""Audit Pocket vocabulary-card visuals.

Each pkvoc card is [English, Portuguese, icon, example, example_pt].  The
renderer uses the third value as a key into data/pk-icons.json; an empty value
falls back to a first-letter tile.  This audit makes that fallback measurable.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", choices=["a1", "a2", "b1"], action="append")
    args = ap.parse_args()
    levels = args.level or ["a1", "a2", "b1"]
    icons = set(json.loads((ROOT / "data/pk-icons.json").read_text(encoding="utf-8")))
    bad = []
    for level in levels:
        total = filled = invalid = episodes = 0
        for path in sorted((ROOT / "data").glob(f"pk-{level}_*.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            episodes += len(data)
            for episode in data:
                for frame in episode.get("fr", []):
                    if frame.get("k") != "pkvoc":
                        continue
                    for idx, card in enumerate(frame.get("cards", [])):
                        total += 1
                        icon = str(card[2]).strip() if len(card) > 2 else ""
                        if icon:
                            filled += 1
                            if icon not in icons:
                                invalid += 1
                                bad.append((path.name, episode.get("n"), idx, icon))
        pct = (filled * 100 / total) if total else 0
        print(f"{level}: episodes={episodes} cards={total} icons={filled} coverage={pct:.1f}% invalid={invalid}")
    if bad:
        print("invalid examples:", bad[:10])
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
