#!/usr/bin/env python3
"""Garante títulos únicos no escopo editorial inglês A1–B2."""
from __future__ import annotations

import glob
import json
import os
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def o_num(e):
    try:
        return float(e.get("o"))
    except (TypeError, ValueError):
        return None


for course in ("en-a1", "en-a2", "en-b1", "en-b2"):
    loaded = []
    groups = defaultdict(list)
    for name in sorted(glob.glob(str(ROOT / "data" / f"{course}_*.json"))):
        data = json.loads(Path(name).read_text(encoding="utf-8"))
        loaded.append((Path(name), data))
        for e in data:
            if o_num(e) is not None and o_num(e) >= 6:
                groups[str(e.get("t", ""))].append(e)
    changed = 0
    for title, records in groups.items():
        if len(records) < 2:
            continue
        for e in records[1:]:
            work = str(e.get("a", {}).get("w", "")).strip()
            suffix = work or f"episódio {int(o_num(e) or 0)}"
            candidate = f"{title} · {suffix}"
            # Em caso de uma obra já reutilizada, o identificador do episódio
            # continua tornando o título inequívoco.
            if any(x.get("t") == candidate for x in records):
                candidate = f"{candidate} · {int(o_num(e) or 0)}"
            e["t"] = candidate
            changed += 1
    for path, data in loaded:
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        os.replace(tmp, path)
    print(course, "títulos alterados:", changed)
