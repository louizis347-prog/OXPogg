#!/usr/bin/env python3
"""Garante uma referência cultural distinta em cada episódio C1/C2.

Quando a mesma obra aparecia em mais de um episódio, a primeira ocorrência é
preservada. As demais recebem uma obra não usada no catálogo regular inglês,
com os cartões culturais, a ponte e os metadados atualizados em conjunto.
"""
from __future__ import annotations

import glob
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TARGETS = ("en-c1", "en-c2")
DONOR_ORDER = ("en-b2", "en-b1", "en-a2", "en-a1")


def frames(e):
    return e.get("fr", [])


def frame(e, key):
    return next((x for x in frames(e) if x.get("k") == key), None)


def first_sentence(text):
    text = re.sub(r"\s+", " ", str(text or "")).strip()
    text = re.split(r"\s+A (?:cena cultural|referência cultural|aula)\b", text, maxsplit=1, flags=re.I)[0]
    if len(text) > 360:
        text = text[:360].rsplit(" ", 1)[0].rstrip(" ,;:—-")
    return text.rstrip(".") + "." if text else "Referência cultural selecionada para esta missão."


def replace_string(value, old, new):
    if isinstance(value, str):
        return value.replace(old, new)
    if isinstance(value, list):
        return [replace_string(x, old, new) for x in value]
    if isinstance(value, dict):
        return {k: replace_string(v, old, new) for k, v in value.items()}
    return value


def unique_pool(used):
    pool = []
    seen = set(used)
    for course in DONOR_ORDER:
        for path in sorted(glob.glob(str(ROOT / "data" / f"{course}_*.json"))):
            for e in json.loads(Path(path).read_text(encoding="utf-8")):
                a = e.get("a") or {}
                work = str(a.get("w") or "").strip()
                if not work or work in seen:
                    continue
                seen.add(work)
                pool.append({
                    "w": work,
                    "k": str(a.get("k") or "referência cultural"),
                    "y": str(a.get("y") or "período não informado"),
                    "d": first_sentence(a.get("d")),
                })
    return pool


def update_cultural_frames(e, donor):
    work, kind, year, desc = donor["w"], donor["k"], donor["y"], donor["d"]
    topic = str(e.get("s") or e.get("t") or "o foco da aula").strip()
    anchor = desc.rstrip(".")
    cultob = frame(e, "cultob")
    if cultob:
        cultob.update({
            "work": work,
            "kind": kind,
            "chips": [kind, year],
            "panels": [desc, f"Nesta aula, a referência ajuda a observar: {topic}."],
            "facts": [f"{kind}: {work}", f"Período: {year}"],
            "coach": f"Conecte {work} ao foco {topic} e diga qual detalhe cultural sustenta essa escolha.",
        })
    cultx = frame(e, "cultx")
    if cultx:
        cultx.update({
            "work": work,
            "tag": kind,
            "tiles": [
                {"ic": "💡", "l": "Um detalhe para levar", "t": f"{desc} A obra oferece uma lente para praticar {topic}."},
                {"ic": "🎯", "l": "Uma porta de entrada", "t": f"Procure um trecho ou registro sobre {work} e observe como ele ilumina {topic}."},
            ],
            "coach": f"Conecte {work} ao foco {topic} e diga qual detalhe cultural sustenta essa escolha.",
        })
    cultcena = frame(e, "cultcena")
    if cultcena:
        cultcena.update({
            "work": work,
            "tag": kind,
            "src": work,
            "ctx": desc,
            "leitura": [f"{desc} Aqui, a obra serve de ponto de partida para explorar {topic}.",
                        f"Para ampliar o contexto, procure uma fonte sobre {work} e anote um detalhe relevante."],
            "link": f"Na lição, {work} conversa diretamente com {topic}: {desc}",
            "coach": f"Interprete a situação de {topic}; depois explique como ela nasce do contexto de {work}.",
        })
    culttl = frame(e, "culttl")
    if culttl:
        culttl["fact"] = desc
        culttl["works"] = [{"n": work, "k": kind, "y": year, "d": desc, "t": "main work"}]
        culttl["coach"] = f"Conecte a referência cultural {work} a uma escolha linguística em {topic}."
    cultgame = frame(e, "cultgame")
    if cultgame:
        options = [kind, "documentário", "peça teatral"]
        while len(set(options)) < 3:
            options.append("registro cultural")
        cultgame.update({
            "work": work,
            "rounds": [{"t": "order", "items": [desc, f"A referência abre a missão de {topic}."]},
                       {"t": "mc", "q": f"“{work}” é apresentado aqui como…", "o": options[:3], "a": 0,
                        "why": f"“{work}” é apresentado aqui como {kind}."}],
            "coach": f"Conecte {work} ao foco {topic} e diga qual detalhe cultural sustenta essa escolha.",
        })
    bridge = frame(e, "bridge")
    if bridge:
        bridge.update({
            "work": work,
            "kind": kind,
            "text": f"A referência {work} oferece este contexto: {desc} A aula transforma essa situação em prática de {topic}.",
            "coach": f"Relacione a obra {work} ao foco {topic}; peça ao estudante que explique essa ligação.",
        })
    cover = frame(e, "cover")
    if cover and isinstance(cover.get("cw"), dict):
        cw = cover["cw"]
        cw.update({"work": work, "kind": kind, "year": year, "intro": f"Em **{work}**, {desc} Hoje, a obra abre a prática de **{topic}**.",
                   "fact": ["🎭", "Você sabia?", desc]})
        cw.pop("by", None)
    return e


def normalize_existing_culture(e):
    """Alinha metadados dos episódios que mantiveram a obra original."""
    work = str((e.get("a") or {}).get("w") or "").strip()
    kind = str((e.get("a") or {}).get("k") or "referência cultural")
    year = str((e.get("a") or {}).get("y") or "período não informado")
    if not work:
        return
    for key in ("cultob", "cultx", "cultcena", "cultgame", "bridge"):
        fr = frame(e, key)
        if fr is not None:
            fr["work"] = work
    cultcena = frame(e, "cultcena")
    if cultcena is not None:
        cultcena["src"] = work
    culttl = frame(e, "culttl")
    if culttl is not None and culttl.get("works"):
        first = culttl["works"][0]
        if isinstance(first, dict):
            first.update({"n": work, "k": kind, "y": year, "t": "main work"})
    cover = frame(e, "cover")
    if cover is not None and isinstance(cover.get("cw"), dict):
        cover["cw"].update({"work": work, "kind": kind, "year": year})


def process():
    paths = []
    episodes = []
    used = set()
    for course in TARGETS:
        for name in sorted(glob.glob(str(ROOT / "data" / f"{course}_*.json"))):
            path = Path(name); paths.append(path)
            data = json.loads(path.read_text(encoding="utf-8"))
            for e in data:
                episodes.append((path, e))
                used.add(str((e.get("a") or {}).get("w") or "").strip())
    pool = unique_pool(used)
    occurrences = defaultdict(int)
    replacements = []
    for path, e in sorted(episodes, key=lambda pe: int(pe[1].get("n") or 0)):
        a = e.setdefault("a", {})
        old = str(a.get("w") or "").strip()
        occurrences[old] += 1
        if occurrences[old] == 1:
            normalize_existing_culture(e)
            continue
        if not pool:
            raise RuntimeError("O catálogo de obras exclusivas acabou antes de concluir C1/C2")
        donor = pool.pop(0)
        # Referências ao trabalho antigo em review, wrap e metadados são
        # atualizadas antes de reescrever os cartões culturais detalhados.
        replaced = replace_string(e, old, donor["w"])
        e.clear(); e.update(replaced)
        e["a"].update({"w": donor["w"], "k": donor["k"], "y": donor["y"]})
        e["a"]["d"] = f"{donor['d']} A referência {donor['w']} conversa com o foco da aula: “{focus(e)}”."
        h = e.get("h")
        if isinstance(h, dict): h["src"] = donor["w"]
        update_cultural_frames(e, donor)
        replacements.append((e.get("n"), old, donor["w"]))
        normalize_existing_culture(e)
    by_path = defaultdict(list)
    for path, e in episodes: by_path[path].append(e)
    for path, data in by_path.items():
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        os.replace(tmp, path)
    print("episódios", len(episodes), "substituições", len(replacements), "obras disponíveis restantes", len(pool))
    for row in replacements[:12]: print(row)


def focus(e):
    return str(e.get("s") or e.get("t") or "o foco da aula").strip()


if __name__ == "__main__":
    process()
