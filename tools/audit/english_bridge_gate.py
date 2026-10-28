#!/usr/bin/env python3
"""Trava editorial da ponte cultural do inglês regular (A1–C2)."""
from __future__ import annotations

import glob
import json
import re
from collections import Counter
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bridge_rules import bridge_failures  # noqa: E402

COURSES = ("en-a1", "en-a2", "en-b1", "en-b2", "en-c1", "en-c2")
MARKER = re.compile(
    r"\b(a aula|a referência|a cena|a obra|a pintura|o filme|o livro|a série|a canção|o poema|"
    r"o contexto da obra|o contexto de|o episódio parte|a relação entre obra e foco|a relação com|o elo com|conversa diretamente|"
    r"ponto de partida|serve de ponte|the scene|the reference|connect)\b",
    re.I,
)


def walk(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, list):
        for y in x:
            yield from walk(y)
    elif isinstance(x, dict):
        for y in x.values():
            yield from walk(y)


def main():
    failures = []
    totals = Counter()
    cultural_works = {"en-c1": set(), "en-c2": set()}
    for course in COURSES:
        for path in sorted(glob.glob(f"data/{course}_*.json")):
            for e in json.load(open(path, encoding="utf-8")):
                totals[course] += 1
                work = str((e.get("a") or {}).get("w") or "").strip()
                desc = str((e.get("a") or {}).get("d") or "")
                if not work or not MARKER.search(desc):
                    failures.append(f"{course}:{e.get('n')}: descrição sem ponte obra–foco")
                bridges = [x for x in e.get("fr", []) if x.get("k") == "bridge"]
                if course in ("en-c1", "en-c2"):
                    if work in cultural_works[course]:
                        failures.append(f"{course}:{e.get('n')}: obra cultural repetida")
                    cultural_works[course].add(work)
                    if len(e.get("fr", [])) not in (18, 19):
                        failures.append(f"{course}:{e.get('n')}: quantidade de quadros diferente de 18/19")
                    if e.get("presentation") != "regular-pilot-v1":
                        failures.append(f"{course}:{e.get('n')}: C1/C2 fora do modelo regular-pilot-v1")
                    old_culture = {"cultob", "cultx", "cultcena", "cultgame"} & {x.get("k") for x in e.get("fr", [])}
                    if old_culture:
                        failures.append(f"{course}:{e.get('n')}: quadros culturais antigos ainda presentes")
                    for message in bridge_failures(e):
                        failures.append(f"{course}:{e.get('n')}: {message}")
                    words = next((x for x in e.get("fr", []) if x.get("k") == "words"), None)
                    verbs = next((x for x in e.get("fr", []) if x.get("k") == "verbs"), None)
                    if words is not None and len(words.get("items", [])) != 6:
                        failures.append(f"{course}:{e.get('n')}: vocabulário ativo não tem seis itens")
                    if verbs is not None and len(verbs.get("items", [])) != 4:
                        failures.append(f"{course}:{e.get('n')}: quadro de verbos não tem quatro itens")
                    tdlg = next((x for x in e.get("fr", []) if x.get("k") == "tdlg"), None)
                    if tdlg is not None:
                        for turn in tdlg.get("turns", []):
                            if len(turn.get("o", [])) != 3 or not 0 <= turn.get("a", -1) < len(turn.get("o", [])):
                                failures.append(f"{course}:{e.get('n')}: alternativa inválida no diálogo")
                    dquiz = next((x for x in e.get("fr", []) if x.get("k") == "dquiz"), None)
                    if dquiz is not None:
                        for item in dquiz.get("items", []):
                            if isinstance(item, dict) and not 0 <= item.get("a", -1) < len(item.get("opts", [])):
                                failures.append(f"{course}:{e.get('n')}: gabarito inválido no quiz")
    print("episódios:", dict(totals), "falhas:", len(failures))
    for failure in failures[:100]:
        print("FALHA", failure)
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
