#!/usr/bin/env python3
"""Rebuild Pocket B2-C2 from the regular English editorial catalogue.

The regular catalogue supplies a distinct cultural anchor and lexical seed for
each episode.  The Pocket frames then turn that seed into a short, coherent
lesson instead of cycling through a small generic profile bank.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
ICONS = ["📝", "🧭", "🔎", "🤝", "✅", "📅", "📍", "🧩", "📷", "🌱", "💡", "🎯"]
COLORS = [["#FF7A7A", "#FFB84D"], ["#6C5CE7", "#2FB0A0"], ["#3E8FD8", "#FFC857"], ["#E17055", "#6C5CE7"], ["#0F766E", "#F59E0B"]]
PEOPLE = [
    ("Maya", "Austin", "community organizer", "👩🏽"), ("Luis", "Chicago", "barista and volunteer", "👨🏽"),
    ("Priya", "Seattle", "software engineer", "👩🏾"), ("Ethan", "Denver", "teacher", "👨🏻"),
    ("Nora", "Boston", "museum guide", "👩🏻"), ("Jamal", "Atlanta", "neighborhood coordinator", "👨🏾"),
    ("Sofia", "Miami", "event planner", "👩🏽"), ("Avery", "Sacramento", "park ranger", "🧑🏻"),
    ("Riley", "Portland", "graphic designer", "🧑🏽"), ("Grace", "New Orleans", "cook and storyteller", "👩🏾"),
    ("Owen", "Philadelphia", "journalist", "👨🏼"), ("Camila", "San Diego", "nurse", "👩🏽"),
    ("Theo", "Minneapolis", "librarian", "👨🏼"), ("Leila", "New York", "architect", "👩🏽"),
    ("Marcus", "Detroit", "bike mechanic", "👨🏾"), ("Zoe", "Raleigh", "researcher", "👩🏻"),
]

def read_regular():
    out = []
    for p in sorted(DATA.glob("en-*.json")):
        level = p.stem.split("-")[1].split("_")[0]
        for e in json.loads(p.read_text(encoding="utf-8")):
            if e.get("a", {}).get("w"):
                e = dict(e)
                e["_level"] = level
                out.append(e)
    return out

def unique_sources(priority: list[str], all_sources: list[dict], count: int) -> list[dict]:
    ordered = [e for level in priority for e in all_sources if e.get("_level") == level]
    ordered += [e for e in all_sources if e not in ordered]
    out, seen = [], set()
    for e in ordered:
        work = str(e.get("a", {}).get("w") or "").strip()
        if work and work not in seen:
            seen.add(work)
            out.append(e)
            if len(out) == count:
                break
    return out

def digest(n: int) -> int:
    return (n * 2654435761) & 0xFFFFFFFF

def lexical_seed(src: dict) -> list[tuple[str, str]]:
    vals = []
    for item in src.get("v", []):
        if isinstance(item, list) and len(item) >= 2 and str(item[0]).strip():
            pair = (str(item[0]).strip(), str(item[1]).strip())
            if pair[0].lower() not in {x[0].lower() for x in vals}:
                vals.append(pair)
    # The regular catalogue normally has six entries.  Keep five, adding a
    # contextual fallback only for malformed legacy records.
    if len(vals) < 5:
        extra = [("context", "contexto"), ("purpose", "propósito"), ("evidence", "evidência"), ("outcome", "resultado")]
        for pair in extra:
            if pair[0] not in {x[0] for x in vals}:
                vals.append(pair)
            if len(vals) == 5:
                break
    return vals[:5]

def make_episode(n: int, level: str, src: dict, idx: int) -> dict:
    work = str(src["a"]["w"])
    year = str(src.get("a", {}).get("y") or "").strip()
    source_title = str(src.get("t") or "").strip()
    words = lexical_seed(src)
    name, city, role, face = PEOPLE[idx % len(PEOPLE)]
    color = COLORS[digest(n) % len(COLORS)]
    w0, w1, w2, w3, w4 = [x[0] for x in words]
    p0, p1, p2, p3, p4 = [x[1] for x in words]
    context = str(src.get("a", {}).get("d") or "").split(".")[0].strip()
    if not context:
        context = f"A referência {work} oferece um contexto cultural para a situação."
    if level == "B2":
        mission = "analisar uma situação e defender uma decisão"
        mission_pt = "analisar uma situação e defender uma decisão"
        lines = [
            [name, f"Thanks for meeting me; the {work} example needs a decision people can act on.", f"Obrigada por conversar comigo; o exemplo de {work} exige uma decisão que as pessoas possam executar."],
            ["You", f"{work} gives us a useful comparison for this case.", f"{work} nos dá uma comparação útil para este caso."],
            [name, f"How should we interpret the term “{w0}” here?", f"Como devemos interpretar o termo “{w0}” aqui?"],
            ["You", f"First, we should place “{w1}” in context and clarify the role of “{w2}”.", f"Primeiro, devemos colocar “{w1}” em contexto e esclarecer o papel de “{w2}”."],
            [name, f"Could you explain how “{w3}” changes the practical choice?", f"Você pode explicar como “{w3}” muda a escolha prática?"],
            ["You", f"Yes. The evidence suggests that “{w4}” is the safer interpretation.", f"Sim. As evidências sugerem que “{w4}” é a interpretação mais segura."],
            [name, f"That distinction matters; the {work} example shows why the audience may read the message differently.", f"Essa distinção importa; o exemplo de {work} mostra por que o público pode interpretar a mensagem de outra forma."],
            ["You", f"Then we can state the decision clearly, as the {work} example suggests, and leave room for a later review.", f"Então podemos declarar a decisão com clareza, como sugere o exemplo de {work}, e deixar espaço para uma revisão posterior."],
        ]
    elif level == "C1":
        mission = "qualify an argument and anticipate its implications"
        mission_pt = "qualificar um argumento e antecipar suas implicações"
        lines = [
            [name, f"Thanks for meeting me; the {work} case deserves more than a quick answer.", f"Obrigada por conversar comigo; o caso de {work} merece mais do que uma resposta rápida."],
            ["You", f"{work} offers a revealing lens, although its assumptions need to be tested here.", f"{work} oferece uma lente reveladora, embora suas premissas precisem ser testadas aqui."],
            [name, f"What does “{w0}” imply once we place it in this institutional context?", f"O que “{w0}” implica quando o colocamos neste contexto institucional?"],
            ["You", f"The distinction between “{w1}” and “{w2}” is subtle but consequential.", f"A distinção entre “{w1}” e “{w2}” é sutil, mas tem consequências."],
            [name, f"Could the wording around “{w3}” invite a different inference?", f"A formulação em torno de “{w3}” poderia convidar a uma inferência diferente?"],
            ["You", f"It could. In this setting, “{w4}” functions as a qualification rather than a conclusion.", f"Poderia. Neste contexto, “{w4}” funciona como uma qualificação, não como uma conclusão."],
            [name, f"That nuance should appear in the explanation of {work}; otherwise the claim sounds stronger than it is.", f"Essa nuance deve aparecer na explicação de {work}; caso contrário, a afirmação parecerá mais forte do que é."],
            ["You", f"Agreed. I will state the limit in the {work} case, acknowledge the counterpoint and then propose a test.", f"Concordo. Vou declarar o limite no caso de {work}, reconhecer o contraponto e então propor um teste."],
        ]
    else:
        mission = "refine a position and negotiate its consequences"
        mission_pt = "refinar uma posição e negociar suas consequências"
        lines = [
            [name, f"Thanks for meeting me; the wording around {work} will shape how the decision is understood.", f"Obrigada por conversar comigo; a formulação em torno de {work} definirá como a decisão será entendida."],
            ["You", f"{work} gives us a productive starting point, provided that we question its assumptions.", f"{work} nos dá um ponto de partida produtivo, desde que questionemos suas premissas."],
            [name, f"How would you delimit the claim carried by “{w0}”?", f"Como você delimitaria a afirmação transmitida por “{w0}”?"],
            ["You", f"I would distinguish “{w1}” from “{w2}”, since the distinction changes the frame of the debate.", f"Eu distinguiria “{w1}” de “{w2}”, pois a distinção muda o enquadramento do debate."],
            [name, f"And what follows if we read “{w3}” as a premise rather than an outcome?", f"E o que se segue se lermos “{w3}” como premissa, e não como resultado?"],
            ["You", f"Then “{w4}” becomes a condition to be examined, not a conclusion to be assumed.", f"Então “{w4}” se torna uma condição a examinar, não uma conclusão a presumir."],
            [name, f"That formulation preserves the counterargument in the {work} debate without weakening the central point.", f"Essa formulação preserva o contraponto no debate sobre {work} sem enfraquecer o ponto central."],
            ["You", f"Exactly. I will make the inference explicit in the {work} discussion and invite a response to the strongest objection.", f"Exatamente. Vou tornar a inferência explícita na discussão sobre {work} e convidar uma resposta à objeção mais forte."],
        ]
    cards = [[w, pt, ICONS[(i + digest(n)) % len(ICONS)], lines[min(i + 2, 7)][1], lines[min(i + 2, 7)][2]] for i, (w, pt) in enumerate(words)]
    pars = [
        ([f"At a meeting in {city}, the group revisits a cultural reference.", f"Em uma reunião em {city}, o grupo retoma uma referência cultural."], ["", ""], None, "🏙️"),
        ([f"{name} frames the context:", f"{name} apresenta o contexto:"], [lines[0][1], lines[0][2]], name, "💬"),
        (["The cultural bridge:", "A ponte cultural:"], [lines[1][1], lines[1][2]], "You", "📖"),
        (["A key term:", "Um termo-chave:"], [lines[2][1], lines[2][2]], name, "🔎"),
        (["A distinction:", "Uma distinção:"], [lines[3][1], lines[3][2]], "You", "🧩"),
        (["A practical question:", "Uma pergunta prática:"], [lines[4][1], lines[4][2]], name, "❓"),
        (["A qualified answer:", "Uma resposta qualificada:"], [lines[5][1], lines[5][2]], "You", "💡"),
        (["The implication:", "A implicação:"], [lines[6][1], lines[6][2]], name, "⚖️"),
        (["The next move:", "O próximo passo:"], [lines[7][1], lines[7][2]], "You", "✅"),
        (["The takeaway:", "O que fica:"], [f"A careful reader distinguishes “{w1}” from “{w2}” before drawing a conclusion.", f"Um leitor cuidadoso distingue “{w1}” de “{w2}” antes de tirar uma conclusão."], None, "🎯"),
    ]
    return {
        "n": n, "o": n, "t": f"{source_title} · {work}", "s": mission_pt.capitalize(), "sc": "cultural-study", "lv": level,
        "a": {"k": "Situação", "w": work, "y": year, "d": f"{context}. A missão usa essa referência para {mission_pt}."},
        "h": {"l": lines[1][1], "src": "Pocket · catálogo regular", "tr": lines[1][2]}, "p": f"Hoje você vai {mission_pt}.", "g": {"t": lines[7][1]}, "v2": True,
        "v": [[w, pt, ICONS[(i + digest(n)) % len(ICONS)]] for i, (w, pt) in enumerate(words)], "presentation": "pocket-v1", "pocket": 1,
        "character": {"id": f"pk_{name.lower()}", "name": name, "gender": "f" if face.startswith("👩") else "m", "role": role, "city": city, "recurring": True},
        "arc": {"i": idx // 10 + 1, "pos": idx % 10 + 1, "of": 10},
        "fr": [
            {"k": "pkhero", "g": color, "num": n % 1000, "lvl": level, "face": face, "name": name, "city": city, "sub": source_title, "mission": f"Hoje você vai {mission_pt}.", "hook": [lines[1][1], lines[1][2]], "boss": idx % 10 == 9},
            {"k": "pkdlg", "g": color, "title": "Diálogo", "lines": lines, "vocab": [[w, pt] for w, pt in words], "cast": {name: [face, color[0]], "You": ["🙂", "#e85d75"]}},
            {"k": "pkvoc", "g": color, "title": "Vocabulário", "cards": cards, "notes": [{"en": f"The distinction between “{w1}” and “{w2}”", "pt": f"A distinção entre “{w1}” e “{w2}”", "txt": "💡 Observe como o contexto muda o sentido e o registro de cada termo."}]},
            {"k": "pkread", "g": color, "title": "Leitura", "pars": [{"lead": a, "q": q, "who": who, "ic": ic} for a, q, who, ic in pars], "vocab": [[w, pt] for w, pt in words]},
            {"k": "pkbuild", "g": color, "title": "Monte a frase", "items": [{"en": f"The distinction between “{w1}” and “{w2}” matters.", "pt": f"A distinção entre “{w1}” e “{w2}” importa.", "opts": [[w1, p1], [w2, p2], ["context", "contexto"]], "note": "Use a estrutura para comparar dois sentidos."}, {"en": f"We should examine “{w4}” before deciding.", "pt": f"Devemos examinar “{w4}” antes de decidir.", "opts": [[w4, p4], ["later", "mais tarde"], ["quickly", "rapidamente"]], "note": "Use before para indicar a ordem do raciocínio."}]},
            {"k": "pkspeak", "g": color, "title": "Fale", "items": [{"who": name, "line": [lines[2][1], lines[2][2]], "target": f"The term “{w0}” needs a clear context.", "pt": f"O termo “{w0}” precisa de um contexto claro."}, {"who": name, "line": [lines[4][1], lines[4][2]], "target": f"The meaning of “{w3}” depends on the frame.", "pt": f"O sentido de “{w3}” depende do enquadramento."}]},
            {"k": "wrap", "title": "Mochila do episódio", "recap": [[lines[i][1], lines[i][2]] for i in [1, 2, 3, 4]], "expr": [["The distinction matters.", "A distinção importa."], ["Let us qualify the claim.", "Vamos qualificar a afirmação."]], "culture": f"{work} oferece a ponte cultural para esta missão.", "teaser": {"t": "Próxima situação: outro argumento em contexto real", "d": ""}, "sticker": {"name": name, "face": face, "role": role, "city": city, "boss": idx % 10 == 9}, "stickers": cards},
        ],
    }

def main():
    all_sources = read_regular()
    plans = {"b2": (953001, ["b2", "b1", "c1", "a2"]), "c1": (954001, ["c1", "c2", "b2", "b1"]), "c2": (955001, ["c2", "c1", "b2", "b1"])}
    for level, (start, priority) in plans.items():
        chosen = unique_sources(priority, all_sources, 800)
        if len(chosen) != 800:
            raise SystemExit(f"{level}: apenas {len(chosen)} âncoras culturais")
        for slot in range(16):
            vals = [make_episode(start + slot * 50 + i, level.upper(), chosen[slot * 50 + i], slot * 50 + i) for i in range(50)]
            (DATA / f"pk-{level}_{slot + 1:02d}.json").write_text(json.dumps(vals, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("B2, C1 e C2 reconstruídos a partir do catálogo regular")

if __name__ == "__main__":
    main()
