#!/usr/bin/env python3
"""Trava editorial da ponte cultural do inglês regular (A1–C2)."""
from __future__ import annotations

import glob
import json
import re
from collections import Counter

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
                    if len(bridges) != 1:
                        failures.append(f"{course}:{e.get('n')}: quadro bridge ausente/duplicado")
                        continue
                    b = bridges[0]
                    text = " ".join(str(b.get(k) or "") for k in ("text", "coach", "topic"))
                    if work.lower() not in text.lower():
                        failures.append(f"{course}:{e.get('n')}: bridge sem obra")
                    topic = str(b.get("topic") or "").strip()
                    if not topic or topic.lower() not in text.lower():
                        failures.append(f"{course}:{e.get('n')}: bridge sem foco")
                    if str(b.get("text") or "").startswith("Connect ") and "today’s goal" in str(b.get("text")):
                        failures.append(f"{course}:{e.get('n')}: bridge genérica")
                    cult = next((x for x in e.get("fr", []) if x.get("k") == "cultcena"), None)
                    link = str((cult or {}).get("link") or "")
                    if work.lower() not in link.lower() or (topic and topic.lower() not in link.lower()):
                        failures.append(f"{course}:{e.get('n')}: cultcena sem ponte completa")
    print("episódios:", dict(totals), "falhas:", len(failures))
    for failure in failures[:100]:
        print("FALHA", failure)
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
