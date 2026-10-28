#!/usr/bin/env python3
"""Refina os quadros linguísticos repetidos do C1 e C2.

O trabalho aproveita a cena autoral de cada episódio para reconstruir as
atividades de vocabulário, frases, verbos, transferência e conversa. Assim,
o conteúdo reaproveitado continua alinhado ao foco do episódio, mas deixa de
ser apenas uma variação superficial de um pool fixo.
"""
from __future__ import annotations

import glob
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSES = ("en-c1", "en-c2")


def frame(e, kind):
    return next((x for x in e.get("fr", []) if x.get("k") == kind), None)


def scene_lines(e):
    fr = frame(e, "scene")
    lines = fr.get("lines", []) if fr else []
    return [x for x in lines if isinstance(x, list) and len(x) >= 3 and x[1] and x[2]]


def focus(e):
    return str(e.get("s") or e.get("t") or "a missão").strip()


def update_wsent(e, lines):
    fr = frame(e, "wsent")
    words = frame(e, "words")
    if not fr or not words or not lines:
        return False
    items = fr.get("items") or []
    glosses = {
        str(item[0]): str(item[2])
        for item in (words.get("items") or [])
        if isinstance(item, list) and len(item) >= 3
    }
    changed = False
    templates = [
        ("The word {word} sharpens this moment: {en}", "A palavra {word} dá precisão a este momento: {pt}"),
        ("This scene detail carries the idea of {word}: {en}", "Este detalhe da cena carrega a ideia de {word}: {pt}"),
        ("Read the line through the lens of {word}: {en}", "Leia a fala pela lente de {word}: {pt}"),
        ("The choice becomes clearer with {word}: {en}", "A escolha fica mais clara com {word}: {pt}"),
        ("Notice how {word} helps us read the scene: {en}", "Observe como {word} ajuda a ler a cena: {pt}"),
        ("In this context, {word} names a useful distinction: {en}", "Neste contexto, {word} nomeia uma distinção útil: {pt}"),
    ]
    for i, item in enumerate(items[:6]):
        if not isinstance(item, dict):
            continue
        word = str(item.get("w") or "the term")
        gloss = glosses.get(word, word)
        en_line = lines[i % len(lines)][1]
        pt_line = lines[i % len(lines)][2]
        en_t, pt_t = templates[i % len(templates)]
        item["en"] = en_t.format(word=word.lower(), en=en_line)
        item["pt"] = pt_t.format(word=gloss, pt=pt_line)
        changed = True
    return changed


def update_verbs(e, lines):
    verbs = frame(e, "verbs")
    vplay = frame(e, "vplay")
    if not verbs or not vplay or not lines:
        return False
    changed = False
    for idx, item in enumerate(verbs.get("items") or []):
        if not isinstance(item, dict):
            continue
        verb = str(item.get("v") or "use")
        pt = str(item.get("pt") or verb)
        en_line = lines[(idx + 1) % len(lines)][1]
        pt_line = lines[(idx + 1) % len(lines)][2]
        item["ex"] = [
            f"The scene lets us {verb} the choice in: {en_line}",
            f"A cena nos ajuda a {pt} a escolha em: {pt_line}",
        ]
        changed = True
    # vplay is the same repertoire, but receives fresh practice sentences too.
    vitems = vplay.get("items") or []
    for idx, item in enumerate(vitems):
        if not isinstance(item, dict):
            continue
        verb = str(item.get("v") or "use")
        pt = str(item.get("pt") or verb)
        en_line = lines[(idx + 3) % len(lines)][1]
        pt_line = lines[(idx + 3) % len(lines)][2]
        item["ex"] = [
            f"Use {verb} to interpret this turn: {en_line}",
            f"Use {pt} para interpretar esta fala: {pt_line}",
        ]
        changed = True
    return changed


def update_tdlg(e, lines, seed):
    fr = frame(e, "tdlg")
    if not fr or len(lines) < 8:
        return False
    response_indices = [1, 3, 5, 7]
    turns = []
    for turn_idx, prompt_idx in enumerate([0, 2, 4, 6]):
        prompt = lines[prompt_idx]
        correct_idx = response_indices[turn_idx]
        choices = [lines[correct_idx]] + [lines[i] for i in response_indices if i != correct_idx][:2]
        rotation = (seed + turn_idx) % 3
        choices = choices[rotation:] + choices[:rotation]
        turns.append({
            "n": [prompt[1], prompt[2]],
            "o": [[choice[1], choice[2]] for choice in choices],
            "a": rotation,
        })
    fr["turns"] = turns
    fr["intro"] = "Você responde à cena. Ouça a fala, escolha a continuação que mantém a intenção e complete a conversa."
    return True


def update_ctxv(e, lines, seed):
    fr = frame(e, "ctxv")
    if not fr or not lines:
        return False
    items = fr.get("items") or []
    for idx, item in enumerate(items):
        if not isinstance(item, dict):
            continue
        first = lines[(2 * idx) % len(lines)]
        second = lines[(2 * idx + 1) % len(lines)]
        item["place"] = f"Cena {idx + 1} · {e.get('sc') or 'contexto'}"
        item["lines"] = [[first[0], first[1]], [second[0], second[1]]]
        item["pt"] = f"{first[0]}: {first[2]} {second[0]}: {second[2]}"
        item["why"] = f"A fala de {first[0]} prepara a resposta de {second[0]} no foco {focus(e)}."
        item["ic"] = (item.get("art") or ["🎧"])[0]
    fr["say"] = "Escute duas falas da cena e transfira a intenção para outro contexto."
    return True


def update_produce(e, lines):
    fr = frame(e, "produce")
    if not fr or not lines:
        return False
    quote = lines[-1]
    fr["prompt"] = f"{fr.get('prompt', 'Produza uma resposta avançada.')} Retome este detalhe da cena: “{quote[1]}” e explique sua escolha."
    fr["model"] = f"{fr.get('model', '').strip()} {quote[1]}".strip()
    fr["check"] = list(fr.get("check") or [])[:2] + [f"Conectei minha resposta ao detalhe: {quote[1]}"]
    return True


def process(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    changed = 0
    for e in data:
        lines = scene_lines(e)
        seed = int(e.get("n") or 0)
        if update_wsent(e, lines): changed += 1
        if update_verbs(e, lines): changed += 1
        if update_tdlg(e, lines, seed): changed += 1
        if update_ctxv(e, lines, seed): changed += 1
        if update_produce(e, lines): changed += 1
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    os.replace(tmp, path)
    return len(data), changed


def main():
    total = 0
    for course in COURSES:
        for name in sorted(glob.glob(str(ROOT / "data" / f"{course}_*.json"))):
            count, changed = process(Path(name))
            total += count
            print(Path(name).name, count, "episódios; blocos refeitos", changed)
    print("TOTAL", total)


if __name__ == "__main__":
    main()
