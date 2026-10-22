#!/usr/bin/env python3
"""Finalize and audit the regular English v2 lesson contract.

This pass is intentionally separate from the first migration so it can be
rerun safely after a data bundle is regenerated.  It fixes episode-specific
cultural anchors, makes the four lesson variants visible in frame order, and
updates every frame's episode metadata without changing renderer keys.
"""

from __future__ import annotations

import copy
import glob
import json
import os
import re
from collections import defaultdict
from pathlib import Path

from rebuild_regular_en_v2 import (LEVELS, DATA, LOCATIONS, MISSIONS, _role,
                                   first_frame, first_line, location, target_words,
                                   visual_seed, work_info, update_bridge,
                                   update_cover, update_fio, update_wrap,
                                   apply_frame_visual)

PT_MISSION = {
    "encontro": "conhecer alguém e manter a conversa natural",
    "problema": "esclarecer um problema e chegar a uma solução prática",
    "descoberta": "observar um detalhe cultural e explicar o que ele significa",
    "projeto": "negociar o próximo passo e realizar um plano em conjunto",
}
PT_LOCATION = {
    "at the café": "na cafeteria", "at the diner": "na lanchonete", "on the subway": "no metrô",
    "at the station": "na estação", "at the airport": "no aeroporto", "at work": "no trabalho",
    "in the studio": "no estúdio", "in class": "na aula", "at school": "na escola",
    "at the library": "na biblioteca", "at the museum": "no museu", "at the market": "no mercado",
    "at the shop": "na loja", "in the park": "no parque", "at the beach": "na praia",
    "in the kitchen": "na cozinha", "at home": "em casa", "at the restaurant": "no restaurante",
    "at the clinic": "na clínica", "at the hotel": "no hotel", "in the lobby": "no saguão",
    "on the street": "na rua", "in the city": "na cidade", "in a real-life situation": "em uma situação real",
}


def variant_group(key):
    if key in {"cover"}: return "cover"
    if key in {"cultob", "cultx", "cultcena", "cultpg", "culttl", "cultgame", "cult"}: return "culture"
    if key in {"review"}: return "retrieve"
    if key in {"bridge", "pbridge"}: return "bridge"
    if key in {"read", "rdg", "rdgplay", "lplay"}: return "listen"
    if key in {"words", "cwords", "wsent", "verbs", "lexpack"}: return "vocab"
    if key in {"pat", "sbuild", "soundlab"}: return "pattern"
    if key in {"vplay", "cexp", "xpr", "ctxv", "dquiz"}: return "practice"
    if key in {"tdlg", "convo", "scene", "order"}: return "scene"
    if key in {"scenebuild", "wlat", "produce"}: return "production"
    if key == "fio": return "thread"
    if key == "wrap": return "wrap"
    return "practice"


VARIANT_ORDER = (
    ["cover", "culture", "bridge", "listen", "vocab", "pattern", "practice", "scene", "production", "thread", "wrap"],
    ["cover", "culture", "bridge", "scene", "listen", "pattern", "vocab", "practice", "production", "thread", "wrap"],
    ["cover", "culture", "bridge", "vocab", "scene", "practice", "pattern", "listen", "production", "thread", "wrap"],
    ["cover", "culture", "bridge", "pattern", "scene", "listen", "practice", "vocab", "production", "thread", "wrap"],
)


def load():
    rows = []
    by_path = {}
    for cid in (f"en-{x}" for x in LEVELS):
        for path in sorted(DATA.glob(f"{cid}_*.json")):
            with path.open(encoding="utf-8") as fh:
                data = json.load(fh)
            by_path[path] = [str(e.get("n")) for e in data]
            rows.extend(data)
    return rows, by_path


def title_unique(rows):
    seen = set()
    for ep in sorted(rows, key=lambda e: (str(e.get("pairId", "")), int(e.get("pairIndex", 0)))):
        title = str(ep.get("t") or "Episode")
        if title in seen:
            lv = str(ep.get("lesson", {}).get("level") or "EN")
            candidate = f"{title} · {lv}"
            if candidate in seen:
                candidate = f"{candidate} · {ep.get('pairId')}"
            title = candidate
        seen.add(title)
        ep["t"] = title


def refresh_threads(rows):
    ordered = sorted(rows, key=lambda e: (str(e.get("pairId", "")), int(e.get("pairIndex", 0))))
    for i, ep in enumerate(ordered):
        fio = first_frame(ep, "fio")
        if not fio:
            continue
        fio["situation"] = ep.get("t") or fio.get("situation")
        fio["previous"] = ordered[i - 1].get("t") if i else "A situação que abre esta sequência."


def rewrite(rows):
    by_pair = defaultdict(list)
    for ep in rows:
        by_pair[ep.get("pairId")].append(ep)
    ordered_pairs = sorted(by_pair.items(), key=lambda kv: kv[0])
    previous = None
    for pair_id, members in ordered_pairs:
        members.sort(key=lambda e: int(e.get("pairIndex", 0)))
        for ep in members:
            lesson = ep.setdefault("lesson", {})
            mission_no = max(1, int(lesson.get("unit") or 1))
            mission = MISSIONS[(mission_no - 1) % len(MISSIONS)]
            work = work_info(ep)
            pt_mission = PT_MISSION[mission[0]]
            pt_location = PT_LOCATION.get(location(ep), "em uma situação real")
            lesson["culturalAnchor"] = work
            lesson["missionType"] = mission[0]
            lesson["mission"] = pt_mission.capitalize()
            lesson["orderVariant"] = (mission_no + int(ep.get("pairIndex") or 1)) % 4
            ep["s"] = pt_mission.capitalize() + f" {pt_location}."
            ep["p"] = f"Missão {mission_no}: {pt_mission} {pt_location}, usando {work['title']} como lente cultural."
            ep["episodeFocus"] = ep["p"]
            ep["levelProgression"] = f"{lesson.get('level', 'A1')}: {pt_mission}. Retome uma ideia útil da situação anterior e produza uma resposta nova."
            pa = visual_seed(ep)
            # Four legacy A1 cultural-page records contained Portuguese prose
            # in the target-language column with an empty translation.  Turn
            # them into short adapted excerpts from the episode's real scene;
            # the target text now has an English line and a Brazilian
            # Portuguese gloss, so the audio and tap-to-translate actions agree.
            for frame in ep.get("fr", []):
                if frame.get("k") != "cultcena" or frame.get("mode") != "page":
                    continue
                lines = frame.get("lines") or []
                if not any(isinstance(row, list) and len(row) > 1 and str(row[1]).strip() == "" for row in lines):
                    continue
                scene = first_frame(ep, "scene") or {}
                adapted = []
                for row in scene.get("lines") or scene.get("full") or []:
                    if isinstance(row, list) and len(row) >= 3 and row[1] and row[2]:
                        adapted.append([row[1], row[2]])
                if adapted:
                    frame["lines"] = adapted[:6]
                    frame["form"] = "adapted"
                    frame["src"] = "Adapted scene for this lesson"
                    frame["about"] = "A short adapted scene connects the cultural reference to today's communicative mission."
            for frame in ep.get("fr", []):
                if frame.get("k") != "cultpg":
                    continue
                for row in frame.get("lines") or []:
                    if isinstance(row, list) and len(row) >= 3 and not str(row[0]).strip():
                        row[0] = "Narrator"
            for frame in ep.get("fr", []):
                role = _role(frame.get("k"))
                if frame.get("k") in {"cultob", "cultx", "cultcena", "cultpg", "cultgame", "cultq"}:
                    frame["work"] = work["title"]
                if frame.get("k") == "culttl" and isinstance(frame.get("works"), list):
                    for item in frame["works"]:
                        if isinstance(item, dict) and item.get("t") == "main work":
                            item["n"] = work["title"]
                frame["lessonRole"] = role
                frame["pairId"] = pair_id
                frame["missionType"] = mission[0]
                frame["episodeId"] = str(ep.get("n"))
                frame["episodeFocus"] = ep["p"]
                apply_frame_visual(frame, pa)
            variant = int(lesson.get("orderVariant") or 0) % 4
            order = {name: i for i, name in enumerate(VARIANT_ORDER[variant])}
            ep["fr"] = [x for _, x in sorted(enumerate(ep.get("fr", [])), key=lambda ix: (order.get(variant_group(ix[1].get("k")), 8), ix[0]))]
            ep["sequence"] = [f.get("k") for f in ep.get("fr", [])]
            update_cover(ep, previous, mission, work, pair_id, int(ep.get("pairIndex") or 1))
            cover = first_frame(ep, "cover")
            if cover:
                cover["sub"] = f"Missão: {pt_mission} {pt_location}."
                cover["mission"] = pt_mission.capitalize() + "."
                cover["objective"] = f"{pt_mission.capitalize()} usando o inglês deste episódio."
                cover["say"] = f"Sua missão é {pt_mission} {pt_location}."
            update_fio(ep, previous, mission, pair_id)
            update_bridge(ep, previous, mission, work)
            update_wrap(ep, previous, mission, work)
            wrap = first_frame(ep, "wrap")
            if wrap:
                wrap["teaser"] = {"t": "Próxima missão", "d": f"Leve o inglês de hoje para uma nova situação {pt_location}."}
            if previous:
                carry = first_line(previous)[0]
                if carry:
                    prod = first_frame(ep, "produce")
                    if prod:
                        prompt = str(prod.get("prompt") or "").strip()
                        prefix = "Retome uma ideia da situação anterior e adapte-a: "
                        prod["prompt"] = prompt if prefix in prompt else (f"{prompt} {prefix}{carry}").strip()
                        prod["carryFromPrevious"] = carry
            previous = ep
    title_unique(rows)
    refresh_threads(rows)


def write(rows, by_path):
    by_n = {str(ep.get("n")): ep for ep in rows}
    for path, ids in by_path.items():
        with path.open(encoding="utf-8") as fh:
            old = json.load(fh)
        out = [by_n[str(ep.get("n"))] for ep in old]
        tmp = path.with_suffix(path.suffix + ".tmp")
        with tmp.open("w", encoding="utf-8") as fh:
            json.dump(out, fh, ensure_ascii=False, separators=(",", ":"))
            fh.write("\n")
        os.replace(tmp, path)


def main():
    rows, by_path = load()
    if len(rows) != 5000:
        raise SystemExit(f"expected 5000 English regular episodes, got {len(rows)}")
    if any("xof" in e for e in rows):
        raise SystemExit("legacy xof link remains; run rebuild_regular_en_v2.py first")
    rewrite(rows)
    write(rows, by_path)
    print(f"finalized {len(rows)} English regular episodes")


if __name__ == "__main__":
    main()
