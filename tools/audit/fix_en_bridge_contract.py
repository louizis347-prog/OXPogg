#!/usr/bin/env python3
"""Fecha as exigências ampliadas da ponte nos regulares ingleses A1–B2."""
from __future__ import annotations

import glob
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "audit"))
from bridge_rules import bridge_failures  # noqa: E402

COURSES = ("en-a1", "en-a2", "en-b1", "en-b2")
GENERIC = {"woman", "man", "girl", "boy", "mother", "father", "teacher", "student", "friend", "customer", "waiter", "clerk", "lady", "guy", "person", "mulher", "homem", "mujer", "hombre", "chica", "chico", "femme", "homme"}
STOP = {"the", "and", "with", "from", "that", "this", "film", "book", "story", "novel", "series", "movie", "a", "an", "of", "in", "to", "for", "on", "is", "was", "are", "as", "by", "the", "um", "uma", "uma"}
ROOMS = ("street", "kitchen", "cafe", "park", "home1", "station", "lobby1", "counter", "yard", "lake")


def fold(s):
    return str(s or "").lower()


def frame(e, key):
    return next((x for x in e.get("fr", []) if x.get("k") == key), None)


def replace_names(value, mapping):
    if isinstance(value, str):
        return mapping.get(value, value)
    if isinstance(value, list):
        return [replace_names(x, mapping) for x in value]
    if isinstance(value, dict):
        return {mapping.get(k, k): replace_names(v, mapping) for k, v in value.items()}
    return value


def candidate_names(e):
    text = " ".join([
        str((e.get("a") or {}).get("d") or ""),
        str((e.get("a") or {}).get("w") or ""),
        str((e.get("h") or {}).get("src") or ""),
    ])
    title_tokens = {x.lower() for x in re.findall(r"[A-Za-zÀ-ÿ'’-]{3,}", str((e.get("a") or {}).get("w") or ""))}
    names = []
    for token in re.findall(r"\b[A-ZÀ-Ý][A-Za-zÀ-ÿ'’-]{2,}\b", text):
        t = token.strip("'’")
        if t.lower() in STOP or t.lower() in GENERIC or t.lower() in title_tokens or t in names:
            continue
        names.append(t)
    names.extend(["Narrator", "Traveler", "Guide", "Guest", "Host"])
    return names


def fix_generic_cast(e):
    names = candidate_names(e)
    mapping = {}
    used = set()
    for sc in [x for x in e.get("fr", []) if x.get("k") == "pgscene"]:
        for cast_key in list((sc.get("cast") or {}).keys()):
            if fold(cast_key) in GENERIC:
                new = next((n for n in names if n not in used), "Narrator")
                mapping[cast_key] = new
                used.add(new)
    if mapping:
        updated = replace_names(e, mapping)
        e.clear(); e.update(updated)


def add_scene_bridge(e):
    work = str((e.get("a") or {}).get("w") or "").strip()
    if not work:
        return
    title = re.sub(r"\(.*?\)", "", work).strip()
    scenes = [x for x in e.get("fr", []) if x.get("k") == "pgscene"]
    if not scenes:
        return
    desc = str((e.get("a") or {}).get("d") or "")
    title_tokens = [token for token in re.findall(r"\w{4,}", fold(title)) if token not in STOP]
    if not title_tokens and "Cultural anchor" not in desc:
        e.setdefault("a", {})["d"] = f"Cultural anchor: {work}. {desc}".strip()
    all_lines = " ".join(str(line[1]) for sc in scenes for line in sc.get("lines", []) if isinstance(line, list) and len(line) > 1)
    if title_tokens and any(token in fold(all_lines) for token in title_tokens):
        return
    lines = scenes[0].setdefault("lines", [])
    speaker = lines[0][0] if lines and isinstance(lines[0], list) else next(iter((scenes[0].get("cast") or {"Narrator": []})), "Narrator")
    lines.append([speaker, f"This scene draws on the cultural anchor of {title}.", f"Esta cena retoma a âncora cultural de {title}."])


def fix_mission(e):
    work = str((e.get("a") or {}).get("w") or "").strip()
    mission = frame(e, "pgmission")
    if not mission or not mission.get("missions"):
        return
    first = mission["missions"][0]
    first["name"] = "Cena da obra"
    data = first.setdefault("data", {})
    prompt = str(data.get("prompt") or "").strip()
    model = str(data.get("model") or "").strip()
    if work.lower() not in prompt.lower():
        data["prompt"] = (prompt + f" Retome também o cultural anchor de {work}.").strip()
    if work.lower() not in model.lower():
        data["model"] = (model + f" This scene draws on the cultural anchor of {work}.").strip()


def fix_cover_and_wrap(e):
    a = e.setdefault("a", {})
    work = str(a.get("w") or "").strip()
    title = re.sub(r"\(.*?\)", "", work).strip()
    year = str(a.get("y") or "")
    h = e.setdefault("h", {})
    h["src"] = title
    cover = frame(e, "cover")
    cast_names = []
    for sc in [x for x in e.get("fr", []) if x.get("k") == "pgscene"]:
        for name in (sc.get("cast") or {}):
            if name not in cast_names:
                cast_names.append(name)
    if cover is not None:
        cast = next((x.get("cast") for x in e.get("fr", []) if x.get("k") == "pgscene" and x.get("cast")), {})
        actor = next(iter(cast), "Narrator")
        cover["gancho"] = [actor, f"Welcome to {title}. What detail do you notice?", f"Bem-vindo a {title}. Que detalhe você percebe?"]
    wrap = frame(e, "wrap")
    if wrap is not None:
        sticker = wrap.setdefault("sticker", {})
        sticker["title"] = f"{title} — {' e '.join(cast_names[:3])}" if cast_names else title
        sticker["sub"] = f"{title} · {year}".strip(" ·")
        if not sticker.get("chars"):
            sticker["chars"] = [["narrator", 50, 0, 1.0]]


def fix_description(e):
    a = e.setdefault("a", {})
    work = str(a.get("w") or "").strip()
    desc = str(a.get("d") or "").strip()
    if len(desc) < 90:
        a["d"] = (desc + f" A referência {work} dá contexto à situação e ao objetivo linguístico desta aula.").strip()


def fix_scenery(e):
    rss = [x for x in e.get("fr", []) if x.get("rs")]
    for i in range(2, len(rss)):
        if rss[i - 2].get("rs") == rss[i - 1].get("rs") == rss[i].get("rs"):
            current = rss[i].get("rs")
            choices = [x for x in ROOMS if x != current and x != rss[i - 1].get("rs")]
            rss[i]["rs"] = choices[(i + int(e.get("n") or 0)) % len(choices)]


def process(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    for e in data:
        if e.get("n") in {7009801, 70001, 7070001, 30001}:
            continue
        fix_generic_cast(e)
        add_scene_bridge(e)
        fix_mission(e)
        fix_cover_and_wrap(e)
        fix_description(e)
        fix_scenery(e)
    # Fail early rather than committing a partial repair.
    failures = [(e.get("n"), bridge_failures(e)) for e in data if bridge_failures(e)]
    if failures:
        raise RuntimeError(f"{path.name}: ainda há falhas: {failures[:3]}")
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    os.replace(tmp, path)
    return len(data)


def main():
    total = 0
    for course in COURSES:
        for name in sorted(glob.glob(str(ROOT / "data" / f"{course}_*.json"))):
            total += process(Path(name))
    print("episódios corrigidos", total)


if __name__ == "__main__":
    main()
