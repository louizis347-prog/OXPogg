#!/usr/bin/env python3
"""Repeatable structural/content audit for Pocket B1 tail and B2-C2."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"

def load(level: str):
    out = []
    for p in sorted(DATA.glob(f"pk-{level}_*.json")):
        out.extend(json.loads(p.read_text(encoding="utf-8")))
    return out

def check(level: str, start: int, count: int, tail_only: bool = False):
    episodes = load(level)
    target = [e for e in episodes if (not tail_only or e["n"] >= 952452)]
    errors = []
    ids = [e.get("n") for e in episodes]
    if len(episodes) != count or len(set(ids)) != count or ids != sorted(ids):
        errors.append(f"contagem/ordenação: {len(episodes)} episódios")
    if ids and (min(ids) != start or max(ids) != start + count - 1):
        errors.append("intervalo de IDs incorreto")
    if len({e.get("a", {}).get("w") for e in episodes}) != count:
        errors.append("obra cultural repetida dentro do nível")
    for e in target:
        fr = {x.get("k"): x for x in e.get("fr", [])}
        for key, field, expected in (("pkdlg", "lines", 8), ("pkvoc", "cards", 5), ("pkread", "pars", 10), ("pkbuild", "items", 2), ("pkspeak", "items", 2), ("wrap", "recap", 4)):
            if key not in fr or len(fr[key].get(field, [])) != expected:
                errors.append(f"{e['n']}: {key} não tem {expected} itens")
        if "pkvoc" not in fr or "pkdlg" not in fr or "pkread" not in fr:
            continue
        text = " ".join(str(x) for x in fr["pkdlg"]["lines"] + fr["pkread"]["pars"]).lower()
        words = [c[0].strip().lower() for c in fr["pkvoc"].get("cards", [])]
        if len(words) != len(set(words)):
            errors.append(f"{e['n']}: vocabulário duplicado")
        for word in words:
            if word and word not in text:
                errors.append(f"{e['n']}: vocabulário não usado: {word}")
        for c in fr["pkvoc"].get("cards", []):
            if len(c) < 5 or any(not str(v).strip() for v in c[:5]):
                errors.append(f"{e['n']}: cartão de vocabulário incompleto")
    return errors

def main():
    errors = []
    for _ in range(8):
        errors.extend(check("b1", 952001, 800, tail_only=True))
        for level, start in (("b2", 953001), ("c1", 954001), ("c2", 955001)):
            errors.extend(check(level, start, 800))
    if errors:
        print("FALHAS", len(errors))
        print("\n".join(errors[:20]))
        return 1
    print("8 auditorias completas: B1 (episódios 452–800), B2, C1 e C2 sem falhas estruturais ou de alinhamento lexical")
    return 0

if __name__ == "__main__":
    sys.exit(main())
