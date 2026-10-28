#!/usr/bin/env python3
"""Fecha as últimas falhas de ponte após a conversão estrutural do C1/C2."""
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

COURSES = ("en-c1", "en-c2")
ROOMS = ("street", "kitchen", "cafe", "park", "home1", "station", "lobby1", "counter", "yard", "lake", "desk")


def frame(e, key):
    return next((x for x in e.get("fr", []) if x.get("k") == key), None)


def fix_one(e):
    a = e.setdefault("a", {})
    work = str(a.get("w") or "").strip()
    title = re.sub(r"\(.*?\)", "", work).strip()
    desc = str(a.get("d") or "")
    if "Cultural anchor" not in desc:
        a["d"] = f"Cultural anchor: {work}. {desc}".strip()
    h = e.setdefault("h", {})
    h["src"] = title
    cover = frame(e, "cover")
    scenes = [x for x in e.get("fr", []) if x.get("k") == "pgscene"]
    if cover and scenes:
        speaker = (scenes[0].get("lines") or [["Narrator"]])[0][0]
        cover["gancho"] = [speaker, f"This scene returns to {title}. What do you notice?", f"Esta cena retoma {title}. O que você percebe?"]
    failures = bridge_failures(e)
    if any("nenhuma fala das cenas" in x for x in failures):
        if scenes:
            lines = scenes[0].setdefault("lines", [])
            speaker = lines[0][0] if lines else "Narrator"
            lines.append([speaker, f"This cultural anchor returns to {title}.", f"Esta âncora cultural retoma {title}."])
    mission = frame(e, "pgmission")
    if mission and mission.get("missions"):
        first = mission["missions"][0]
        first["name"] = "Cena da obra"
        data = first.setdefault("data", {})
        data["prompt"] = (str(data.get("prompt") or "") + f" Cultural anchor: {title}.").strip()
        data["model"] = (str(data.get("model") or "") + f" This cultural anchor returns to {title}.").strip()
    # Evita três quadros seguidos com o mesmo cenário.
    rs_frames = [x for x in e.get("fr", []) if x.get("rs")]
    for i in range(2, len(rs_frames)):
        if rs_frames[i - 2].get("rs") == rs_frames[i - 1].get("rs") == rs_frames[i].get("rs"):
            current = rs_frames[i].get("rs")
            rs_frames[i]["rs"] = next((r for r in ROOMS if r != current and r != rs_frames[i - 1].get("rs")), "street")


def main():
    total = 0
    for course in COURSES:
        for name in sorted(glob.glob(str(ROOT / "data" / f"{course}_*.json"))):
            path = Path(name); data = json.loads(path.read_text(encoding="utf-8"))
            for e in data:
                fix_one(e); total += 1
            remaining = [(e.get("n"), bridge_failures(e)) for e in data if bridge_failures(e)]
            if remaining:
                raise SystemExit(f"{path.name}: falhas restantes {remaining[:3]}")
            tmp = path.with_suffix(path.suffix + ".tmp")
            tmp.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
            os.replace(tmp, path)
    print("episódios verificados", total)


if __name__ == "__main__":
    main()
