#!/usr/bin/env python3
"""Normalize the six active vocabulary entries in non-English regular courses.

This is deliberately limited to the vocabulary layer. English regular data is
never touched. Existing lexical entries are preserved; malformed phrase entries
are replaced with the first usable lexical item from the same episode and the
corresponding translation/pronunciation metadata. The words and words-in-
sentences cards are kept in sync with the canonical ``episode['v']`` list.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
TOKEN = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿĀ-žА-Яа-я一-鿿ぁ-ゖァ-ヺ가-힣][A-Za-zÀ-ÖØ-öø-ÿĀ-žА-Яа-я一-鿿ぁ-ゖァ-ヺ가-힣'’\-]*")
STOP = {
    "a", "à", "ao", "as", "com", "da", "das", "de", "do", "dos", "e", "em", "en",
    "la", "las", "le", "les", "lo", "los", "na", "nas", "no", "nos", "o", "os", "para",
    "por", "que", "se", "um", "uma", "uns", "umas", "y", "el", "un", "una", "des", "du",
    "der", "die", "das", "ein", "eine", "und", "von", "zu", "il", "lo", "gli", "le", "un",
    "uno", "una", "di", "del", "della", "e", "の", "은", "는", "이", "가", "을", "를", "的",
}


def words(text):
    return [x for x in TOKEN.findall(str(text or "")) if x.lower() not in STOP and len(x) > 1]


def phrase_to_word(raw):
    """Return a lexical item, keeping CJK/Japanese/Korean entries intact."""
    raw = str(raw or "").strip()
    if not raw:
        return ""
    if not re.search(r"\s|/", raw):
        return raw
    candidates = words(raw)
    return candidates[0] if candidates else raw.split()[0]


def episode_candidates(ep):
    out = []
    for item in ep.get("v") or []:
        if isinstance(item, list) and item:
            out.append(item)
    for frame in ep.get("fr") or []:
        if frame.get("k") in {"words", "wsent"}:
            for item in frame.get("items") or []:
                if isinstance(item, list) and item:
                    out.append(item)
                elif isinstance(item, dict):
                    out.append([item.get("w") or item.get("en"), item.get("pt", ""), item.get("py", "")])
        if frame.get("k") in {"scene", "pgscene", "cultcena", "tdlg"}:
            for line in frame.get("lines") or []:
                if isinstance(line, list) and line:
                    out.extend([[token, "", ""] for token in words(line[0])])
        if frame.get("k") == "hotscene":
            for item in frame.get("hot") or []:
                out.append([item.get("en"), item.get("pt", ""), item.get("say", "")])
    return out


def normalize_episode(ep):
    candidates = episode_candidates(ep)
    chosen = []
    seen = set()
    for item in candidates:
        raw = item[0] if item else ""
        word = phrase_to_word(raw)
        key = word.casefold()
        if not word or key in seen:
            continue
        # Keep the item's translation and pronunciation, but make the entry's
        # first field a single lexical item. This avoids copying a sentence into
        # the active-vocabulary slot.
        pt = item[1] if len(item) > 1 else ""
        pron = item[2] if len(item) > 2 else ""
        chosen.append([word, pt, pron])
        seen.add(key)
        if len(chosen) == 6:
            break
    if len(chosen) < 6:
        # Chinese/Japanese/Korean episodes can have no whitespace at all. Use
        # short character chunks only as a last resort; the source sentence is
        # still retained in the scene, while the active card receives a stable
        # pronounceable unit instead of a full sentence.
        for item in candidates:
            raw = str(item[0] if item else "")
            chars = re.findall(r"[一-鿿ぁ-ゖァ-ヺ가-힣]{2,4}", raw)
            for chunk in chars:
                if chunk.casefold() in seen:
                    continue
                chosen.append([chunk, item[1] if len(item) > 1 else "", item[2] if len(item) > 2 else ""])
                seen.add(chunk.casefold())
                if len(chosen) == 6:
                    break
            if len(chosen) == 6:
                break
    if len(chosen) < 6:
        return False
    changed = chosen != ep.get("v")
    ep["v"] = chosen
    for frame in ep.get("fr") or []:
        if frame.get("k") == "words":
            old = frame.get("items") or []
            icons = [x[1] for x in old if isinstance(x, list) and len(x) > 1]
            frame["items"] = [[v[0], icons[i] if i < len(icons) else "🔤", v[1], v[2]] for i, v in enumerate(chosen)]
        elif frame.get("k") == "wsent":
            old = frame.get("items") or []
            icons = [x.get("ic", "🔤") for x in old if isinstance(x, dict)]
            frame["items"] = [{"w": v[0], "ic": icons[i] if i < len(icons) else "🔤", "en": v[0], "pt": v[1], "py": v[2]} for i, v in enumerate(chosen)]
    return changed


def main():
    manifest = json.loads((DATA / "manifest.json").read_text(encoding="utf-8"))
    touched = 0
    episodes = 0
    for course, files in manifest.items():
        if course.startswith("nb") or course.startswith("en-"):
            continue
        for rel in files:
            path = DATA / rel
            data = json.loads(path.read_text(encoding="utf-8"))
            dirty = False
            for ep in data:
                episodes += 1
                if normalize_episode(ep):
                    dirty = True
                    touched += 1
            if dirty:
                path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"episódios examinados: {episodes}; vocabulários corrigidos: {touched}")


if __name__ == "__main__":
    main()
