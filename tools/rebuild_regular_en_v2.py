#!/usr/bin/env python3
"""Reorganize the regular English course without exposing odd/even episodes.

The data is already authored in 2,500 pairs (5,000 episodes).  This migration
keeps every episode id and every supported frame renderer, while giving each
episode one continuous lesson contract: mission, cultural anchor, scene,
language workshop, production and retrieval.  The former ``xof`` link is
replaced with internal pair metadata so it cannot leak into the learner UI.
"""

from __future__ import annotations

import copy
import glob
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

LEVELS = ("a1", "a2", "b1", "b2", "c1", "c2")
MISSIONS = (
    ("encontro", "Meet and connect", "meet someone and keep the exchange natural"),
    ("problema", "Solve the mix-up", "clarify a problem and reach a practical solution"),
    ("descoberta", "Read the world", "notice a cultural detail and explain what it means"),
    ("projeto", "Make a plan", "negotiate a next step and carry out a shared plan"),
)
LOCATIONS = {
    "cafe": "at the café", "diner": "at the diner", "subway": "on the subway",
    "subwaycar": "on the subway", "station": "at the station", "airport": "at the airport",
    "office": "at work", "studio": "in the studio", "classroom": "in class",
    "school": "at school", "library": "at the library", "museum": "at the museum",
    "market": "at the market", "shop": "at the shop", "park": "in the park",
    "beach": "at the beach", "kitchen": "in the kitchen", "living": "at home",
    "home": "at home", "restaurant": "at the restaurant", "hospital": "at the clinic",
    "clinic": "at the clinic", "hotel": "at the hotel", "lobby": "in the lobby",
    "street": "on the street", "city": "in the city", "museum-gallery": "at the museum",
}

# The renderer understands these keys.  Sorting by this contract unifies the
# former culture-first and grammar-first sequences without renaming a frame.
FRAME_ORDER = {
    "cover": 0,
    "cultob": 10, "cultx": 20, "cultcena": 30, "cultpg": 30,
    "culttl": 40, "cultgame": 50, "cult": 50, "review": 50,
    "bridge": 60, "pbridge": 60,
    "read": 70, "rdg": 70, "rdgplay": 75,
    "lplay": 80, "words": 90, "cwords": 90, "wsent": 100,
    "verbs": 110, "pat": 120, "sbuild": 125, "soundlab": 130,
    "vplay": 140, "cexp": 150, "xpr": 155, "ctxv": 160,
    "dquiz": 165, "tdlg": 170, "convo": 175, "scene": 180,
    "order": 185, "scenebuild": 190, "wlat": 195, "lexpack": 200,
    "produce": 210, "fio": 220, "cultq": 225, "wrap": 240,
}


def load_level(cid: str):
    rows = []
    paths = sorted(DATA.glob(f"{cid}_*.json"))
    for path in paths:
        with path.open(encoding="utf-8") as fh:
            data = json.load(fh)
        for pos, episode in enumerate(data):
            episode["_source"] = path.name
            episode["_source_pos"] = pos
            rows.append(episode)
    return rows, paths


def text_from(value):
    if isinstance(value, str):
        return re.sub(r"\s+", " ", value).strip()
    return ""


def first_frame(ep, *keys):
    for key in keys:
        for frame in ep.get("fr", []):
            if frame.get("k") == key:
                return frame
    return None


def first_line(ep):
    for frame in ep.get("fr", []):
        for key in ("lines", "full"):
            rows = frame.get(key)
            if isinstance(rows, list):
                for row in rows:
                    if isinstance(row, list) and row:
                        target = row[1] if len(row) > 1 and isinstance(row[1], str) else row[0]
                        if isinstance(target, str) and target.strip():
                            return target, row[2] if len(row) > 2 and isinstance(row[2], str) else ""
    return "", ""


def scene_art(ep):
    scene = first_frame(ep, "scene", "convo", "tdlg") or {}
    art = scene.get("art") or {}
    return text_from(art.get("s")) or text_from((first_frame(ep, "cover") or {}).get("art", {}).get("s"))


def work_info(ep):
    # ``cultob`` and the episode's source metadata identify the anchor chosen
    # for this episode.  Some older continuations carried ``cultx`` text from
    # the preceding episode, so those frames are deliberately lower priority.
    anchor = first_frame(ep, "cultob")
    if anchor and anchor.get("work"):
        return {
            "title": text_from(anchor.get("work")),
            "kind": text_from(anchor.get("kind") or anchor.get("tag") or "cultural work"),
            "year": anchor.get("year") or "",
        }
    source = ep.get("a") if isinstance(ep.get("a"), dict) else {}
    if source.get("w"):
        return {"title": text_from(source.get("w")), "kind": "cultural reference", "year": ""}
    for frame in ep.get("fr", []):
        work = frame.get("work")
        if work:
            return {
                "title": text_from(work),
                "kind": text_from(frame.get("kind") or frame.get("tag") or "cultural work"),
                "year": frame.get("year") or (frame.get("works") or [{}])[0].get("y"),
            }
    return {"title": "today's cultural reference", "kind": "cultural work", "year": ""}


def location(ep):
    raw = scene_art(ep).lower()
    for key, label in LOCATIONS.items():
        if key in raw:
            return label
    return "in a real-life situation"


def target_words(ep):
    frame = first_frame(ep, "words", "cwords")
    if not frame:
        return []
    out = []
    for item in frame.get("items", []):
        if isinstance(item, list) and item and isinstance(item[0], str):
            out.append(item[0])
        elif isinstance(item, dict) and item.get("w"):
            out.append(str(item["w"]))
    return out[:8]


def visual_seed(ep):
    for frame in ep.get("fr", []):
        pa = frame.get("pa")
        if isinstance(pa, dict) and pa.get("t"):
            return copy.deepcopy(pa)
        banner = frame.get("banner")
        if isinstance(banner, dict) and isinstance(banner.get("pa"), dict):
            return copy.deepcopy(banner["pa"])
    return {"t": "street", "p": ["#d9e9ff", "#fff7e1", "#4d6fa8"], "e": ["💬", "📚", "✨"], "v": 0}


def ensure_banner(frame, pa):
    if frame.get("k") in {"cover", "fio", "wrap"}:
        return
    if not isinstance(frame.get("banner"), dict):
        frame["banner"] = {"pa": copy.deepcopy(pa)}
    elif not isinstance(frame["banner"].get("pa"), dict):
        frame["banner"]["pa"] = copy.deepcopy(pa)


def role_icons(role):
    return {
        "cultural_anchor": ["🎬", "📖", "🌎"],
        "work_depth": ["🔎", "🧠", "🗺️"],
        "interpretive_scene": ["🎭", "👀", "💬"],
        "timeline": ["🕰️", "📍", "🧭"],
        "retrieval": ["🔁", "🧩", "⭐"],
        "focused_listening": ["🎧", "👂", "💬"],
        "listening_practice": ["🔊", "🎧", "🗣️"],
        "active_vocabulary": ["🧰", "🃏", "✨"],
        "words_in_context": ["🧩", "✍️", "💬"],
        "pattern_discovery": ["🧱", "🔧", "🧠"],
        "pronunciation": ["🎙️", "〰️", "👄"],
        "guided_practice": ["🎯", "🔁", "✅"],
        "meaning_and_intention": ["💡", "🗣️", "🤝"],
        "context_challenge": ["🧭", "❓", "🎯"],
        "comprehension": ["🔍", "✅", "📌"],
        "communicative_repair": ["🛠️", "💬", "🤝"],
        "daily_scene": ["📍", "👥", "💬"],
        "guided_production": ["🧩", "🗣️", "📝"],
        "written_transfer": ["✍️", "📝", "📨"],
        "lexical_transfer": ["🧰", "🔗", "💬"],
        "free_production": ["🎤", "🌟", "🚀"],
        "story_thread": ["🧵", "📍", "➡️"],
    }.get(role, ["💬", "✨", "🎯"])


def apply_frame_visual(frame, pa):
    role = frame.get("lessonRole") or _role(frame.get("k"))
    bpa = copy.deepcopy(pa)
    bpa["e"] = role_icons(role)
    frame["banner"] = {"pa": bpa, "role": role}


def dialogue_lines(ep):
    scene = first_frame(ep, "scene")
    if scene and isinstance(scene.get("lines"), list):
        return scene["lines"]
    convo = first_frame(ep, "convo")
    if convo and isinstance(convo.get("turns"), list):
        return convo["turns"]
    return []


def update_fio(ep, previous, mission, pair_id):
    fio = first_frame(ep, "fio")
    if not fio:
        return
    current_line, current_pt = first_line(ep)
    prev_line, prev_pt = first_line(previous) if previous else ("", "")
    fio["title"] = "Fio da história"
    fio["arc"] = ep.get("lesson", {}).get("arc") or ep.get("s") or "Prática comunicativa"
    fio["previous"] = previous.get("t") if previous else "A situação que abre esta sequência."
    fio["situation"] = ep.get("t") or mission[1]
    fio["nextLine"] = current_line or "Choose how you would respond next."
    fio["nextLinePt"] = current_pt
    fio["memory"] = prev_line or "Retome uma ideia da situação anterior."
    fio["pairId"] = pair_id
    # These are used by the remodelled renderer as contextual choices, not as
    # a separate lesson type.
    level = str(ep.get("lv") or ep.get("th") or "A1").upper()
    if level in {"A1", "A2"}:
        fio["tones"] = [
            ["natural", "Natural", f"Mantém a conversa fluida {location(ep)}."],
            ["clear", "Esclarecedora", "Explicita a informação de que o interlocutor precisa."],
            ["cautious", "Cuidadosa", "Confirma o contexto antes de avançar."],
        ]
    else:
        fio["tones"] = [
            ["natural", "Natural", "Mantém o ritmo e a relação sem excesso de explicação."],
            ["clear", "Esclarecedora", "Torna a intenção explícita e reduz a ambiguidade."],
            ["cautious", "Cuidadosa", "Ajusta o registro e deixa espaço para negociação."],
        ]
    fio["pragmatics"] = f"Nesta missão, observe clareza, relação entre os interlocutores, registro e consequência da resposta {location(ep)}."


def update_bridge(ep, previous, mission, work):
    bridge = first_frame(ep, "bridge", "pbridge")
    if not bridge:
        return
    bridge["title"] = "Da obra para a vida real"
    bridge["topic"] = ep.get("s") or mission[2]
    bridge["work"] = work["title"]
    bridge["kind"] = work["kind"]
    scene = first_frame(ep, "scene") or {}
    lines = scene.get("lines") or scene.get("full") or []
    if lines and isinstance(lines[0], list):
        bridge["from"] = [lines[0][1] if len(lines[0]) > 1 else lines[0][0], lines[0][2] if len(lines[0]) > 2 else ""]
    if previous:
        prev_line, prev_pt = first_line(previous)
        bridge["recycle"] = [prev_line, prev_pt]
    bridge["tail"] = f"A referência cultural ilumina o foco linguístico; agora leve a mesma intenção para {location(ep)}."


def update_wrap(ep, previous, mission, work):
    wrap = first_frame(ep, "wrap")
    if not wrap:
        return
    words = target_words(ep)
    recap = wrap.get("recap") if isinstance(wrap.get("recap"), list) else []
    if words:
        for word in words[:4]:
            if not any(isinstance(row, list) and row and row[0] == word for row in recap):
                recap.append([word, "Use it in a new sentence from today's mission."])
    if previous:
        prev_line, prev_pt = first_line(previous)
        if prev_line and not any(isinstance(row, list) and row and row[0] == prev_line for row in recap):
            recap.insert(0, [prev_line, prev_pt or "Carry this idea into the new situation."])
    wrap["recap"] = recap[:8]
    wrap["teaser"] = {"t": "Next mission", "d": f"Carry today's language into {mission[1].lower()} {location(ep)}."}
    wrap["title"] = "Recupere e leve adiante"
    wrap["work"] = work["title"]


def update_cover(ep, previous, mission, work, pair_id, pair_index):
    cover = first_frame(ep, "cover")
    if not cover:
        return
    old_sub = text_from(cover.get("sub")) or text_from(ep.get("s"))
    carry = first_line(previous)[0] if previous else ""
    cover["sub"] = mission[2].capitalize() + (f" {location(ep)}." if location(ep) not in mission[2] else ".")
    cover["mission"] = mission[2].capitalize() + "."
    cover["objective"] = f"{mission[2].capitalize()} using the language of this episode."
    cover["pairId"] = pair_id
    cover["pairIndex"] = pair_index
    cover["recycle"] = carry
    cover["say"] = f"Your mission: {mission[1].lower()} {location(ep)}."
    if carry:
        cover["handoff"] = f"Bring this idea forward: {carry}"
    # Keep the original hook when it is good; otherwise use the first target
    # line so every cover has a playable, episode-specific hook.
    if not cover.get("hook") or not cover["hook"][0]:
        line, tr = first_line(ep)
        if line:
            cover["hook"] = [line, tr]


def title_for(ep, mission, loc, seen):
    original = text_from(ep.get("t")) or mission[1]
    if original not in seen:
        seen.add(original)
        return original
    candidate = f"{original} · {loc.replace('at the ', 'at ').replace('on the ', 'on ')}"
    if candidate in seen:
        n = 2
        while f"{candidate} · {n}" in seen:
            n += 1
        candidate = f"{candidate} · {n}"
    seen.add(candidate)
    return candidate


def transform_level(cid):
    rows, paths = load_level(cid)
    by_n = {str(e.get("n")): e for e in rows}
    pairs = []
    for pos, e in enumerate(rows):
        if e.get("xof") is not None:
            continue
        x = by_n.get(str(e.get("n")))
        # xof lives on the continuation, so find it without relying on file
        # adjacency (the source files are chunked).
        continuation = next((q for q in rows if str(q.get("xof")) == str(e.get("n"))), None)
        if continuation is not None:
            pairs.append((e, continuation))
    if len(pairs) * 2 != len(rows):
        raise RuntimeError(f"{cid}: expected complete pairs, got {len(pairs)} pairs / {len(rows)} episodes")

    # Previous episode is the immediately preceding published episode in the
    # same level, regardless of whether it is the first or second member.
    ordered = [e for pair in pairs for e in pair]
    prev_map = {id(e): (ordered[i - 1] if i else None) for i, e in enumerate(ordered)}
    seen_titles = set()
    for pair_no, (base, follow) in enumerate(pairs, 1):
        pair_id = f"{cid}-{pair_no:04d}"
        mission = MISSIONS[(pair_no - 1) % len(MISSIONS)]
        for pair_index, ep in enumerate((base, follow), 1):
            previous = prev_map[id(ep)]
            work = work_info(ep)
            ep.pop("xof", None)
            ep.pop("_source", None)
            ep.pop("_source_pos", None)
            ep["reorg"] = 2
            ep["pairId"] = pair_id
            ep["pairIndex"] = pair_index
            ep["sequenceVersion"] = "regular-en-v2"
            ep["lesson"] = {
                "track": cid,
                "level": cid.split("-")[-1].upper(),
                "unit": pair_no,
                "missionType": mission[0],
                "mission": mission[2].capitalize(),
                "culturalAnchor": work,
                "orderVariant": (pair_no + pair_index) % 4,
                "recycleFrom": previous.get("n") if previous else None,
            }
            ep["t"] = title_for(ep, mission, location(ep), seen_titles)
            ep["s"] = mission[2].capitalize() + f" {location(ep)}."
            ep["p"] = f"Mission {pair_no}: {mission[2]} {location(ep)}, using {work['title']} as a cultural lens."
            ep["episodeFocus"] = ep["p"]
            ep["levelProgression"] = f"{cid.split('-')[-1].upper()}: {mission[2]}. Reuse one useful idea from the previous situation, then produce a new response."

            pa = visual_seed(base)
            for frame in ep.get("fr", []):
                frame["lessonRole"] = frame.get("lessonRole") or _role(frame.get("k"))
                frame["pairId"] = pair_id
                frame["missionType"] = mission[0]
                apply_frame_visual(frame, pa)
            # Stable pedagogical order; a four-way variant changes only the
            # middle practice order while keeping cover and closing fixed.
            ep["fr"] = sorted(enumerate(ep.get("fr", [])), key=lambda ix: (FRAME_ORDER.get(ix[1].get("k"), 205), ix[0]))
            ep["fr"] = [frame for _, frame in ep["fr"]]
            update_cover(ep, previous, mission, work, pair_id, pair_index)
            update_fio(ep, previous, mission, pair_id)
            update_bridge(ep, previous, mission, work)
            update_wrap(ep, previous, mission, work)
            # Make the recycling visible in the production prompt without
            # copying the former episode wholesale.
            prod = first_frame(ep, "produce")
            if prod and previous:
                carry = first_line(previous)[0]
                if carry:
                    prompt = text_from(prod.get("prompt"))
                    prod["prompt"] = f"{prompt} Reuse one idea from the previous situation, then adapt it: {carry}".strip()
                    prod["carryFromPrevious"] = carry
            # Keep the sequence available for audits and teacher materials.
            ep["sequence"] = [frame.get("k") for frame in ep.get("fr", [])]

    # Write only the original chunk files, preserving their episode order.
    by_source = defaultdict(list)
    for e in rows:
        by_source[e.get("_source", "")].append(e)
    # _source was removed during transformation; reconstruct by pair order and
    # path capacities from a fresh load.
    original_rows = []
    for path in paths:
        with path.open(encoding="utf-8") as fh:
            original_rows.extend(json.load(fh))
    transformed_by_n = {str(e.get("n")): e for e in rows}
    for path in paths:
        with path.open(encoding="utf-8") as fh:
            old = json.load(fh)
        out = [transformed_by_n[str(e.get("n"))] for e in old]
        tmp = path.with_suffix(path.suffix + ".tmp")
        with tmp.open("w", encoding="utf-8") as fh:
            json.dump(out, fh, ensure_ascii=False, separators=(",", ":"))
            fh.write("\n")
        os.replace(tmp, path)
    return len(rows), len(pairs)


def _role(key):
    return {
        "cover": "mission", "cultob": "cultural_anchor", "cultx": "work_depth",
        "cultcena": "interpretive_scene", "culttl": "timeline", "cultgame": "cultural_challenge",
        "review": "retrieval", "bridge": "cultural_language_bridge", "pbridge": "cultural_language_bridge",
        "read": "focused_listening", "rdg": "focused_listening", "lplay": "listening_practice",
        "words": "active_vocabulary", "wsent": "words_in_context", "verbs": "pattern_vocabulary",
        "pat": "pattern_discovery", "sbuild": "guided_transformation", "soundlab": "pronunciation",
        "vplay": "guided_practice", "cexp": "meaning_and_intention", "xpr": "meaning_and_intention",
        "ctxv": "context_challenge", "dquiz": "comprehension", "tdlg": "communicative_repair",
        "convo": "daily_scene", "scene": "daily_scene", "scenebuild": "guided_production",
        "wlat": "written_transfer", "lexpack": "lexical_transfer", "produce": "free_production",
        "fio": "story_thread", "wrap": "retrieval_and_next_mission",
    }.get(key, "practice")


def main():
    totals = []
    for level in LEVELS:
        count, pairs = transform_level(f"en-{level}")
        totals.append(count)
        print(f"en-{level}: {count} episódios reorganizados em {pairs} pares")
    print(f"total: {sum(totals)} episódios")


if __name__ == "__main__":
    main()
