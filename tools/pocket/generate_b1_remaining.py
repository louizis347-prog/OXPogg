#!/usr/bin/env python3
"""Complete Pocket B1 to the 800-episode plan with authored story frames.

The generator uses a large pool of unused cultural works from the regular
English catalogue, then combines each work with a rotating everyday mission.
Every episode keeps Pocket's seven-frame contract and receives its own title,
dialogue, reading, vocabulary and visual palette.
"""
from __future__ import annotations

import glob
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
TARGET_LAST = 952800  # 800 B1 episodes: 952001–952800
IC = ["📝", "⚠️", "💰", "🤝", "✅", "📅", "📍", "🧩", "📷", "🌱", "💡", "🎯"]
COLORS = [["#FF7A7A", "#FFB84D"], ["#6C5CE7", "#2FB0A0"], ["#3E8FD8", "#FFC857"], ["#E17055", "#6C5CE7"]]
PEOPLE = [
    ("Maya", "Austin", "community organizer", "👩🏽"), ("Luis", "Chicago", "barista", "👨🏽"),
    ("Priya", "Seattle", "engineer", "👩🏾"), ("Ethan", "Denver", "teacher", "👨🏻"),
    ("Nora", "Boston", "museum guide", "👩🏻"), ("Jamal", "Atlanta", "volunteer", "👨🏾"),
    ("Sofia", "Miami", "event planner", "👩🏽"), ("Avery", "Sacramento", "park ranger", "🧑🏻"),
    ("Riley", "Portland", "designer", "🧑🏽"), ("Grace", "New Orleans", "cook", "👩🏾"),
    ("Owen", "Philadelphia", "journalist", "👨🏼"), ("Camila", "San Diego", "nurse", "👩🏽"),
]
PROFILES = [
    ("A repair café takes shape", "organizar um café de conserto", ["repair", "tool", "schedule", "reuse", "patient"], ["consertar", "ferramenta", "horário", "reutilizar", "paciente"]),
    ("A public meeting needs a clear plan", "conduzir uma reunião pública", ["agenda", "proposal", "concern", "vote", "transparent"], ["pauta", "proposta", "preocupação", "votação", "transparente"]),
    ("A neighbor asks for a practical favor", "pedir e oferecer ajuda", ["favor", "rely", "deadline", "manage", "grateful"], ["favor", "contar com", "prazo", "gerenciar", "grato"]),
    ("A community garden changes its routine", "adaptar uma rotina comunitária", ["seedling", "harvest", "soil", "rotate", "steady"], ["muda", "colheita", "solo", "revezar", "constante"]),
    ("A local shop responds to a complaint", "resolver uma reclamação com respeito", ["receipt", "refund", "policy", "apologize", "reasonable"], ["recibo", "reembolso", "política", "pedir desculpas", "razoável"]),
    ("A volunteer shift needs a replacement", "trocar um turno de voluntariado", ["shift", "cover", "notice", "arrange", "available"], ["turno", "cobrir", "aviso", "organizar", "disponível"]),
    ("A small festival changes location", "avisar uma mudança de local", ["venue", "route", "sign", "update", "accessible"], ["local", "rota", "placa", "atualização", "acessível"]),
    ("A team compares two useful options", "comparar opções antes de decidir", ["option", "trade-off", "evidence", "prefer", "practical"], ["opção", "compensação", "evidência", "preferir", "prático"]),
    ("A friend returns something borrowed", "devolver algo emprestado", ["borrow", "return", "condition", "remind", "honest"], ["emprestar", "devolver", "estado", "lembrar", "honesto"]),
    ("A class prepares a cultural exchange", "preparar um intercâmbio cultural", ["custom", "introduce", "compare", "curious", "respectful"], ["costume", "apresentar", "comparar", "curioso", "respeitoso"]),
    ("A public library plans a late opening", "planejar um horário especial", ["library", "extend", "quiet", "notice", "convenient"], ["biblioteca", "estender", "silencioso", "aviso", "conveniente"]),
    ("A bus route is redesigned", "explicar uma mudança de transporte", ["route", "transfer", "fare", "delay", "efficient"], ["rota", "baldeação", "tarifa", "atraso", "eficiente"]),
    ("A workplace welcomes a new colleague", "acolher uma pessoa nova", ["onboard", "introduce", "team", "clarify", "supportive"], ["integrar", "apresentar", "equipe", "esclarecer", "prestativo"]),
    ("A family negotiates a weekend plan", "negociar um plano de fim de semana", ["suggest", "schedule", "compromise", "cancel", "flexible"], ["sugerir", "agenda", "compromisso", "cancelar", "flexível"]),
    ("A clinic explains a follow-up visit", "entender uma consulta de retorno", ["symptom", "referral", "follow-up", "prescription", "careful"], ["sintoma", "encaminhamento", "retorno", "receita", "cuidadoso"]),
    ("A team checks a safety procedure", "revisar um procedimento de segurança", ["checklist", "hazard", "report", "prevent", "alert"], ["lista de verificação", "perigo", "relatório", "prevenir", "alerta"]),
    ("A photographer asks for permission", "pedir autorização para fotografar", ["permission", "portrait", "frame", "publish", "sensitive"], ["permissão", "retrato", "enquadramento", "publicar", "sensível"]),
    ("A market stall solves a payment issue", "resolver um pagamento no mercado", ["vendor", "change", "card", "receipt", "secure"], ["vendedor", "troco", "cartão", "recibo", "seguro"]),
    ("A neighbor reduces household waste", "reduzir o lixo doméstico", ["sort", "compost", "recycle", "container", "responsible"], ["separar", "compostar", "reciclar", "recipiente", "responsável"]),
    ("A student asks for feedback", "pedir e usar feedback", ["feedback", "draft", "improve", "specific", "progress"], ["feedback", "rascunho", "melhorar", "específico", "progresso"]),
]

def digest(n: int) -> int:
    return int(hashlib.sha256(str(n).encode()).hexdigest()[:8], 16)

def culture_pool(existing: set[str]) -> list[tuple[str, str]]:
    pool = []
    seen = set(existing)
    for p in sorted(DATA.glob("en-*.json")):
        try: data = json.loads(p.read_text(encoding="utf-8"))
        except Exception: continue
        for e in data:
            a = e.get("a") or {}; w = str(a.get("w") or "").strip()
            if w and w not in seen:
                seen.add(w); pool.append((w, str(a.get("d") or "")))
    return pool

def episode(n: int, work: str, work_desc: str) -> dict:
    i = (n - 952001) // 10 + 1; pos = (n - 952001) % 10 + 1
    profile = PROFILES[(n - 952001) % len(PROFILES)]
    title, mission_pt, words, words_pt = profile
    person = PEOPLE[(n - 952001) % len(PEOPLE)]; name, city, role, face = person
    g = COLORS[digest(n) % len(COLORS)]
    v = [[words[j], words_pt[j], IC[(j + digest(n)) % len(IC)]] for j in range(5)]
    lines = [
        [name, f"Thanks for meeting me about {title.lower()}.", f"Obrigada por se encontrar comigo sobre {mission_pt}."],
        ["You", f"I brought a proposal inspired by {work}.", f"Trouxe uma proposta inspirada por {work}."],
        [name, f"What is your main concern about the plan?", "Qual é a sua principal preocupação com o plano?"],
        ["You", f"We need a practical way to use the {words[0]} without losing sight of the community.", f"Precisamos de uma forma prática de usar {words_pt[0]} sem perder de vista a comunidade."],
        [name, f"Could we {words[3]} the details before we publish the update?", f"Podemos {words_pt[3]} os detalhes antes de publicar a atualização?"],
        ["You", f"Yes. I can explain the evidence and keep the next step {words[4]}.", f"Sim. Posso explicar a evidência e manter o próximo passo {words_pt[4]}."],
        [name, f"That sounds fair. I will share the revised plan tomorrow.", "Parece justo. Vou compartilhar o plano revisado amanhã."],
        ["You", f"Great. If we listen carefully, the plan can work for everyone.", "Ótimo. Se ouvirmos com atenção, o plano pode funcionar para todos."],
    ]
    pars = [
        ([f"At a community space in {city},", f"Em um espaço comunitário em {city},"], ["", ""], None, "🏙️"),
        ([f"{name} explains:", f"{name} explica:"], [lines[0][1], lines[0][2]], name, "💬"),
        (["You present:", "Você apresenta:"], [lines[1][1], lines[1][2]], "You", "📝"),
        ([f"{name} asks:", f"{name} pergunta:"], [lines[2][1], lines[2][2]], name, "❓"),
        (["You clarify:", "Você esclarece:"], [lines[3][1], lines[3][2]], "You", "💡"),
        ([f"{name} suggests:", f"{name} sugere:"], [lines[4][1], lines[4][2]], name, "🤝"),
        (["You answer:", "Você responde:"], [lines[5][1], lines[5][2]], "You", "✅"),
        ([f"{name} agrees:", f"{name} concorda:"], [lines[6][1], lines[6][2]], name, "📅"),
        (["Finally, you say:", "Por fim, você diz:"], [lines[7][1], lines[7][2]], "You", "💬"),
        (["Now you know:", "Agora você sabe:"], [f"A {words[0]} can become useful when people negotiate with care.", f"{words_pt[0].capitalize()} pode se tornar útil quando as pessoas negociam com cuidado."], None, "💡"),
    ]
    cards = [[v[j][0], v[j][1], v[j][2], lines[j + 1][1], lines[j + 1][2]] for j in range(5)]
    return {
        "n": n, "o": n, "t": f"{title} · {work}", "s": mission_pt.capitalize(), "sc": "community-center", "lv": "B1",
        "a": {"k": "Situação", "w": work, "y": "", "d": (work_desc + " " if work_desc else "") + f"A situação trabalha {mission_pt} em uma conversa cotidiana."},
        "h": {"l": lines[1][1], "src": "Pocket", "tr": lines[1][2]}, "p": f"Hoje você vai {mission_pt}.", "g": {"t": lines[7][1]}, "v2": True,
        "v": [[x[0], x[1], x[2]] for x in v], "presentation": "pocket-v1", "pocket": 1,
        "character": {"id": f"pk_{name.lower().replace(' ', '_')}", "name": name, "gender": "f" if face.startswith("👩") else "m", "role": role, "city": city, "recurring": True},
        "arc": {"i": i, "pos": pos, "of": 10},
        "fr": [
            {"k": "pkhero", "g": g, "num": n - 952000, "lvl": "B1", "face": face, "name": name, "city": city, "sub": title, "mission": f"Hoje você vai {mission_pt}.", "hook": [lines[1][1], lines[1][2]], "boss": pos == 10},
            {"k": "pkdlg", "g": g, "title": "Diálogo", "lines": lines, "vocab": [[x[0], x[1]] for x in v], "cast": {name: [face, g[0]], "You": ["🙂", "#e85d75"]}},
            {"k": "pkvoc", "g": g, "title": "Vocabulário", "cards": cards, "notes": [{"en": f"A {words[4]} plan", "pt": f"Um plano {words_pt[4]}", "txt": f"💡 Use {words[4]} para avaliar se algo merece confiança na situação."}]},
            {"k": "pkread", "g": g, "title": "Leitura", "pars": [{"lead": a, "q": q, "who": who, "ic": ic} for a, q, who, ic in pars], "vocab": [[x[0], x[1]] for x in v]},
            {"k": "pkbuild", "g": g, "title": "Monte a frase", "items": [{"en": "We need a {0} plan.", "pt": "Precisamos de um plano {0}.", "opts": [[words[4], words_pt[4]], ["simple", "simples"], ["clear", "claro"]], "note": f"Use {words[4]} para mostrar confiança."}, {"en": "We can {0} the details.", "pt": "Podemos {0} os detalhes.", "opts": [[words[3], words_pt[3]], ["repeat", "repetir"], ["hide", "esconder"]], "note": f"Use {words[3]} para negociar com cuidado."}]},
            {"k": "pkspeak", "g": g, "title": "Fale", "items": [{"who": name, "line": [lines[2][1], lines[2][2]], "target": f"My main concern is the {words[0]}.", "pt": f"Minha principal preocupação é {words_pt[0]}."}, {"who": name, "line": [lines[4][1], lines[4][2]], "target": f"We can {words[3]} the details.", "pt": f"Podemos {words_pt[3]} os detalhes."}]},
            {"k": "wrap", "title": "Mochila do episódio", "recap": [[lines[1][1], lines[1][2]], [lines[2][1], lines[2][2]], [lines[3][1], lines[3][2]], [lines[4][1], lines[4][2]]], "expr": [["That sounds fair.", "Parece justo."], ["The next step is clear.", "O próximo passo está claro."]], "culture": f"A referência {work} oferece um ponto de partida para conversar sobre {mission_pt}.", "teaser": {"t": f"Próximo: {PROFILES[(n - 952001 + 1) % len(PROFILES)][0]}", "d": ""}, "sticker": {"name": name, "face": face, "role": role, "city": city, "boss": pos == 10}, "stickers": cards},
        ],
    }

def main():
    existing = []
    for p in sorted(DATA.glob("pk-b1_*.json")):
        existing += json.loads(p.read_text(encoding="utf-8"))
    seen_ids = {e["n"] for e in existing}; seen_works = {e.get("a", {}).get("w") for e in existing}
    pool = culture_pool(seen_works)
    need = [n for n in range(952458, TARGET_LAST + 1) if n not in seen_ids]
    if len(pool) < len(need): raise SystemExit(f"culture pool too short: {len(pool)} < {len(need)}")
    generated = [episode(n, pool[i][0], pool[i][1]) for i, n in enumerate(need)]
    buckets = {}
    for e in generated:
        slot = (e["n"] - 952001) // 50 + 1
        buckets.setdefault(slot, []).append(e)
    for slot, vals in buckets.items():
        path = DATA / f"pk-b1_{slot:02d}.json"
        old = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
        all_items = {e["n"]: e for e in old}
        all_items.update({e["n"]: e for e in vals})
        path.write_text(json.dumps([all_items[n] for n in sorted(all_items)], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"generated {len(generated)} episodes across {len(buckets)} files")

if __name__ == "__main__":
    main()
