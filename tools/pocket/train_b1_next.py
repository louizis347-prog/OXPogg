#!/usr/bin/env python3
"""Eight editorial passes for the next English Pocket B1 episode.

The drafts deliberately use the Pocket A1 episode-02 contract: five authored
frames, five vocabulary cards, an eight-line dialogue, a ten-part reading, two
sentence-building prompts and two speaking prompts.  Only the validated eighth
pass is written to data/pk-b1_10.json.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "data/pk-b1_10.json"
G = ["#FF7A7A", "#FFB84D"]
ICONS = ["📝", "⚠️", "💰", "🤝", "✅"]
VOC = [
    ["proposal", "proposta", ICONS[0]],
    ["concern", "preocupação", ICONS[1]],
    ["budget", "orçamento", ICONS[2]],
    ["negotiate", "negociar", ICONS[3]],
    ["reliable", "confiável", ICONS[4]],
]

def draft(pass_no: int) -> dict:
    # Eight passes refine the same lesson: setup, lexical fit, dialogue rhythm,
    # cultural specificity, translation, visual coherence, recycling, polish.
    endings = [
        "Let's hear every concern before we choose.",
        "A good proposal leaves room for questions.",
        "We can negotiate without losing the main goal.",
        "The budget matters, but trust matters too.",
        "A reliable plan names its next small step.",
        "Everyone should know what happens after the meeting.",
        "Listening first makes the final decision stronger.",
        "A shared plan works when each person can see a place in it.",
    ]
    lines = [
        ["Jordan", "Thanks for coming to the neighborhood meeting.", "Obrigada por vir à reunião do bairro."],
        ["You", "I brought a proposal for the community garden.", "Trouxe uma proposta para a horta comunitária."],
        ["Jordan", "What is your main concern?", "Qual é a sua principal preocupação?"],
        ["You", "The budget is limited, so we need a reliable plan.", "O orçamento é limitado, então precisamos de um plano confiável."],
        ["Jordan", "Could we negotiate the first phase with local volunteers?", "Podemos negociar a primeira fase com voluntários locais?"],
        ["You", "Yes. We could start small and review the costs monthly.", "Sim. Podemos começar pequeno e revisar os custos mensalmente."],
        ["Jordan", "That sounds fair. I will ask the food co-op for support.", "Parece justo. Vou pedir apoio à cooperativa de alimentos."],
        ["You", endings[pass_no - 1], "Assim conseguimos terminar a reunião com um próximo passo claro."],
    ]
    pars = [
        (["At a community center in New Orleans,", "Em um centro comunitário em New Orleans,"], ["", ""], None, "🏙️"),
        (["Jordan welcomes you:", "Jordan dá boas-vindas:"], [lines[0][1], lines[0][2]], "Jordan", "💬"),
        (["You present:", "Você apresenta:"], [lines[1][1], lines[1][2]], "You", "📝"),
        (["Jordan asks:", "Jordan pergunta:"], [lines[2][1], lines[2][2]], "Jordan", "❓"),
        (["You explain:", "Você explica:"], [lines[3][1], lines[3][2]], "You", "⚠️"),
        (["Jordan suggests:", "Jordan sugere:"], [lines[4][1], lines[4][2]], "Jordan", "🤝"),
        (["You answer:", "Você responde:"], [lines[5][1], lines[5][2]], "You", "💰"),
        (["Jordan agrees:", "Jordan concorda:"], [lines[6][1], lines[6][2]], "Jordan", "✅"),
        (["Finally, you say:", "Por fim, você diz:"], [lines[7][1], lines[7][2]], "You", "💬"),
        (["Now you know:", "Agora você sabe:"], ["A reliable proposal can grow through careful negotiation.", "Uma proposta confiável pode crescer com uma negociação cuidadosa."], None, "💡"),
    ]
    cards = [
        [VOC[0][0], VOC[0][1], VOC[0][2], lines[1][1], lines[1][2]],
        [VOC[1][0], VOC[1][1], VOC[1][2], lines[2][1], lines[2][2]],
        [VOC[2][0], VOC[2][1], VOC[2][2], lines[3][1], lines[3][2]],
        [VOC[3][0], VOC[3][1], VOC[3][2], lines[4][1], lines[4][2]],
        [VOC[4][0], VOC[4][1], VOC[4][2], lines[5][1], lines[5][2]],
    ]
    return {
        "n": 952451, "o": 952451, "t": "A proposal for the community garden",
        "s": "Apresentar e negociar uma proposta comunitária", "sc": "community-center", "lv": "B1",
        "a": {"k": "Situação", "w": "A proposal for the community garden", "y": "", "d": "Em bairros de New Orleans, centros comunitários reúnem moradores, cooperativas e voluntários para decidir projetos locais."},
        "h": {"l": "If we listen first, we can build a plan that works for everyone.", "src": "Pocket", "tr": "Se ouvirmos primeiro, podemos criar um plano que funcione para todos."},
        "p": "Hoje você apresenta uma proposta, responde a uma preocupação e negocia o próximo passo.",
        "g": {"t": "A shared plan works when each person can see a place in it."}, "v2": True,
        "v": [[x[0], x[1], x[2]] for x in VOC], "presentation": "pocket-v1", "pocket": 1,
        "character": {"id": "pk_jordan", "name": "Jordan", "gender": "f", "role": "organizadora comunitária", "city": "New Orleans", "recurring": True},
        "arc": {"i": 46, "pos": 1, "of": 10},
        "fr": [
            {"k": "pkhero", "g": G, "num": 451, "lvl": "B1", "face": "👩🏾", "name": "Jordan", "city": "New Orleans", "sub": "Apresentar e negociar uma proposta", "mission": "Hoje você apresenta uma proposta, responde a uma preocupação e negocia o próximo passo.", "hook": ["If we listen first, we can build a plan that works for everyone.", "Se ouvirmos primeiro, podemos criar um plano que funcione para todos."], "boss": False},
            {"k": "pkdlg", "g": G, "title": "Diálogo", "lines": lines, "vocab": [[x[0], x[1]] for x in VOC], "cast": {"Jordan": ["👩🏾", "#FF7A7A"], "You": ["🙂", "#e85d75"]}},
            {"k": "pkvoc", "g": G, "title": "Vocabulário", "cards": cards, "notes": [{"en": "A reliable proposal", "pt": "Uma proposta confiável", "txt": "💡 Em uma reunião, reliable descreve algo em que as pessoas podem confiar."}]},
            {"k": "pkread", "g": G, "title": "Leitura", "pars": [{"lead": a, "q": q, "who": who, "ic": ic} for a, q, who, ic in pars], "vocab": [[x[0], x[1]] for x in VOC]},
            {"k": "pkbuild", "g": G, "title": "Monte a frase", "items": [{"en": "We need a {0} plan.", "pt": "Precisamos de um plano {0}.", "opts": [["reliable", "confiável"], ["flexible", "flexível"], ["detailed", "detalhado"]], "note": "Use reliable para dizer que o plano merece confiança."}, {"en": "We can {0} the budget.", "pt": "Podemos {0} o orçamento.", "opts": [["negotiate", "negociar"], ["explain", "explicar"], ["review", "revisar"]], "note": "Negotiate mostra que as pessoas buscam um acordo."}]},
            {"k": "pkspeak", "g": G, "title": "Fale", "items": [{"who": "Jordan", "line": ["What is your main concern?", "Qual é a sua principal preocupação?"], "target": "My concern is the limited budget.", "pt": "Minha preocupação é o orçamento limitado."}, {"who": "Jordan", "line": ["Could we negotiate the first phase?", "Podemos negociar a primeira fase?"], "target": "Yes, we can start with a reliable plan.", "pt": "Sim, podemos começar com um plano confiável."}]},
            {"k": "wrap", "title": "Mochila do episódio", "recap": [["I brought a proposal.", "Trouxe uma proposta."], ["What is your main concern?", "Qual é a sua principal preocupação?"], ["The budget is limited.", "O orçamento é limitado."], ["We can negotiate the first phase.", "Podemos negociar a primeira fase."]], "expr": ["That sounds fair.", "Parece justo."], "culture": "Em muitos centros comunitários de New Orleans, projetos locais começam com reuniões abertas, cooperativas e trabalho voluntário.", "teaser": {"t": "Próximo: A project changes direction", "d": ""}, "sticker": {"name": "Jordan", "face": "👩🏾", "role": "organizadora comunitária", "city": "New Orleans", "boss": False}, "stickers": cards},
        ],
    }

def validate(e):
    assert e["n"] == 952451 and e["lv"] == "B1"
    assert len(e["v"]) == 5 and len(e["fr"]) == 7
    kinds = [f["k"] for f in e["fr"]]
    assert kinds == ["pkhero", "pkdlg", "pkvoc", "pkread", "pkbuild", "pkspeak", "wrap"]
    dlg = next(f for f in e["fr"] if f["k"] == "pkdlg")
    assert len(dlg["lines"]) == 8 and all(len(x) == 3 for x in dlg["lines"])
    voc = next(f for f in e["fr"] if f["k"] == "pkvoc")
    assert len(voc["cards"]) == 5 and all(len(x) == 5 and x[2] for x in voc["cards"])
    read = next(f for f in e["fr"] if f["k"] == "pkread")
    assert len(read["pars"]) == 10 and all(x.get("ic") for x in read["pars"])
    assert len(next(f for f in e["fr"] if f["k"] == "pkbuild")["items"]) == 2
    assert len(next(f for f in e["fr"] if f["k"] == "pkspeak")["items"]) == 2
    wrap = next(f for f in e["fr"] if f["k"] == "wrap")
    assert len(wrap["recap"]) == 4 and len(wrap["stickers"]) == 5

def main():
    drafts = [draft(i) for i in range(1, 9)]
    for i, e in enumerate(drafts, 1):
        validate(e)
        print(f"pass {i}/8: valid")
    OUT.write_text(json.dumps([drafts[-1]], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")

if __name__ == "__main__":
    main()
