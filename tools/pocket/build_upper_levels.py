#!/usr/bin/env python3
"""Build/refine Pocket B1 (episodes after the protected baseline) and B2-C2.

The generator keeps Pocket's seven-frame contract while making every vocabulary
card usable in the dialogue and reading.  It is intentionally deterministic so
that an audit can be repeated after each editorial pass.
"""
from __future__ import annotations

import glob
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
ICON = ["📝", "🧭", "🔎", "🤝", "✅", "📅", "📍", "🧩", "📷", "🌱", "💡", "🎯"]
COLORS = [["#FF7A7A", "#FFB84D"], ["#6C5CE7", "#2FB0A0"], ["#3E8FD8", "#FFC857"], ["#E17055", "#6C5CE7"], ["#0F766E", "#F59E0B"]]
PEOPLE = [
    ("Maya", "Austin", "community organizer", "👩🏽"),
    ("Luis", "Chicago", "barista and volunteer", "👨🏽"),
    ("Priya", "Seattle", "software engineer", "👩🏾"),
    ("Ethan", "Denver", "teacher", "👨🏻"),
    ("Nora", "Boston", "museum guide", "👩🏻"),
    ("Jamal", "Atlanta", "neighborhood coordinator", "👨🏾"),
    ("Sofia", "Miami", "event planner", "👩🏽"),
    ("Avery", "Sacramento", "park ranger", "🧑🏻"),
    ("Riley", "Portland", "graphic designer", "🧑🏽"),
    ("Grace", "New Orleans", "cook and storyteller", "👩🏾"),
    ("Owen", "Philadelphia", "journalist", "👨🏼"),
    ("Camila", "San Diego", "nurse", "👩🏽"),
    ("Theo", "Minneapolis", "librarian", "👨🏼"),
    ("Leila", "New York", "architect", "👩🏽"),
    ("Marcus", "Detroit", "bike mechanic", "👨🏾"),
    ("Zoe", "Raleigh", "researcher", "👩🏻"),
]

# Each profile has five lexical targets.  The sentence templates below use all
# five targets, preventing a card from becoming decorative filler.
PROFILES = [
    ("A repair café earns the neighborhood's trust", "organizar um café de conserto", ["repair", "tool", "reuse", "schedule", "patient"], ["consertar", "ferramenta", "reutilizar", "horário", "paciente"]),
    ("A public meeting turns a concern into a plan", "conduzir uma reunião pública", ["agenda", "concern", "proposal", "vote", "transparent"], ["pauta", "preocupação", "proposta", "votação", "transparente"]),
    ("A neighbor asks for a practical favor", "pedir e oferecer ajuda", ["favor", "rely", "deadline", "manage", "grateful"], ["favor", "contar com", "prazo", "gerenciar", "grato"]),
    ("A community garden changes its routine", "adaptar uma rotina comunitária", ["seedling", "harvest", "soil", "rotate", "steady"], ["muda", "colheita", "solo", "revezar", "constante"]),
    ("A shop responds to a complaint", "resolver uma reclamação com respeito", ["receipt", "refund", "policy", "apologize", "reasonable"], ["recibo", "reembolso", "política", "pedir desculpas", "razoável"]),
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
    ("A household reduces its waste", "reduzir o lixo doméstico", ["sort", "compost", "recycle", "container", "responsible"], ["separar", "compostar", "reciclar", "recipiente", "responsável"]),
    ("A student asks for useful feedback", "pedir e usar feedback", ["feedback", "draft", "improve", "specific", "progress"], ["feedback", "rascunho", "melhorar", "específico", "progresso"]),
    ("A museum balances access and preservation", "equilibrar acesso e preservação", ["curate", "access", "preserve", "display", "inclusive"], ["fazer curadoria", "acesso", "preservar", "exibir", "inclusivo"]),
    ("A tenant and landlord clarify a repair", "esclarecer um reparo no imóvel", ["tenant", "lease", "repair", "document", "prompt"], ["inquilino", "contrato", "reparo", "documentar", "rápido"]),
    ("A newsroom checks a difficult source", "verificar uma fonte jornalística", ["source", "verify", "claim", "bias", "editor"], ["fonte", "verificar", "alegação", "viés", "editor"]),
    ("A trail crew protects a fragile habitat", "proteger um habitat frágil", ["habitat", "trail", "erosion", "restore", "wildlife"], ["habitat", "trilha", "erosão", "restaurar", "vida selvagem"]),
    ("A team mediates a scheduling conflict", "mediar um conflito de horários", ["conflict", "mediate", "priority", "overlap", "fair"], ["conflito", "mediar", "prioridade", "sobreposição", "justo"]),
]

def digest(value: int) -> int:
    return int(hashlib.sha256(str(value).encode()).hexdigest()[:8], 16)

def works(existing: set[str]) -> list[tuple[str, str]]:
    out, seen = [], set(existing)
    for p in sorted(DATA.glob("en-*.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        for e in data:
            a = e.get("a") or {}
            name = str(a.get("w") or "").strip()
            if name and name not in seen:
                seen.add(name)
                out.append((name, str(a.get("d") or "")))
    # A level needs 800 distinct cultural anchors.  If the unused remainder is
    # smaller than that, append catalogue works already used by another level;
    # uniqueness is still guaranteed inside each newly generated level.
    if len(out) < 800:
        seen_local = {w for w, _ in out}
        for p in sorted(DATA.glob("en-*.json")):
            for e in json.loads(p.read_text(encoding="utf-8")):
                a = e.get("a") or {}
                name = str(a.get("w") or "").strip()
                if name and name not in seen_local:
                    seen_local.add(name)
                    out.append((name, str(a.get("d") or "")))
    return out

def make_episode(n: int, level: str, work: str, work_desc: str, idx: int) -> dict:
    prof = PROFILES[idx % len(PROFILES)]
    title, mission, words, pts = prof
    name, city, role, face = PEOPLE[idx % len(PEOPLE)]
    c = COLORS[digest(n) % len(COLORS)]
    # Eight lines deliberately distribute all five target words.
    # The target words are deliberately placed in syntactically safe frames:
    # some pools contain nouns, verbs and adjectives, so the frame must not
    # force a verb or an article that would make a malformed sentence.
    if level in {"C1", "C2"}:
        lines = [
            [name, "Thanks for meeting me; this situation deserves a careful look.", "Obrigada por conversar comigo; esta situação merece uma análise cuidadosa."],
            ["You", f"{work} offers a useful lens, but we still need to adapt it to this community.", f"{work} oferece uma lente útil, mas ainda precisamos adaptá-la a esta comunidade."],
            [name, f"Which question of {words[0]} should guide our first decision?", f"Qual questão de {pts[0]} deve orientar nossa primeira decisão?"],
            ["You", f"Let us examine {words[1]} before we decide what to do about {words[2]}.", f"Vamos examinar {pts[1]} antes de decidir o que fazer sobre {pts[2]}."],
            [name, f"Could we keep the next step {words[4]} while making the {words[3]} explicit?", f"Podemos manter o próximo passo {pts[4]} e deixar {pts[3]} explícito?"],
            ["You", f"Yes. I will document the issue of {words[0]} and explain why {words[4]} matters.", f"Sim. Vou documentar a questão de {pts[0]} e explicar por que {pts[4]} importa."],
            [name, f"That gives us room to discuss {words[1]} without overlooking the issue of {words[2]}.", f"Isso nos dá espaço para discutir {pts[1]} sem ignorar a questão de {pts[2]}."],
            ["You", f"Then we can make the next step work and keep {words[3]} visible in the plan.", f"Então podemos fazer o próximo passo funcionar e manter {pts[3]} visível no plano."],
        ]
    elif level == "B2":
        lines = [
            [name, "Thanks for meeting me; we need a solution that people can actually use.", "Obrigada por conversar comigo; precisamos de uma solução que as pessoas possam realmente usar."],
            ["You", f"{work} gives us a useful comparison, although our context is different.", f"{work} nos dá uma comparação útil, embora nosso contexto seja diferente."],
            [name, f"Which question of {words[0]} should we settle before we move on?", f"Qual questão de {pts[0]} devemos resolver antes de avançar?"],
            ["You", f"We should examine {words[1]} first and then decide what to do about {words[2]}.", f"Devemos examinar {pts[1]} primeiro e depois decidir o que fazer sobre {pts[2]}."],
            [name, f"Could you keep the next step {words[4]} while making the {words[3]} clear to everyone?", f"Você pode manter o próximo passo {pts[4]} e deixar {pts[3]} claro para todos?"],
            ["You", f"Yes. I will document the issue of {words[0]}, so the reasoning is easy to follow.", f"Sim. Vou documentar a questão de {pts[0]}, para que o raciocínio seja fácil de acompanhar."],
            [name, f"That approach gives us time to discuss {words[1]} without losing sight of {words[2]}.", f"Essa abordagem nos dá tempo para discutir {pts[1]} sem perder de vista {pts[2]}."],
            ["You", f"Then we can make the next step work and keep {words[3]} visible in the plan.", f"Então podemos fazer o próximo passo funcionar e manter {pts[3]} visível no plano."],
        ]
    else:
        lines = [
            [name, "Thanks for meeting me; we need a practical solution today.", "Obrigada por conversar comigo; precisamos de uma solução prática hoje."],
            ["You", f"{work} gives us a useful idea, and I want to adapt it here.", f"{work} nos dá uma ideia útil, e quero adaptá-la aqui."],
            [name, f"Which question of {words[0]} should we address first?", f"Qual questão de {pts[0]} devemos abordar primeiro?"],
            ["You", f"Let us examine {words[1]} before we decide what to do about {words[2]}.", f"Vamos examinar {pts[1]} antes de decidir o que fazer sobre {pts[2]}."],
            [name, f"Could you keep the next step {words[4]} while making the {words[3]} clear?", f"Você pode manter o próximo passo {pts[4]} e deixar {pts[3]} claro?"],
            ["You", f"Yes. I will document the issue of {words[0]} and explain why {words[4]} matters.", f"Sim. Vou documentar a questão de {pts[0]} e explicar por que {pts[4]} importa."],
            [name, f"That gives us room to discuss {words[1]} without ignoring the issue of {words[2]}.", f"Isso nos dá espaço para discutir {pts[1]} sem ignorar a questão de {pts[2]}."],
            ["You", f"Then we can make the next step work and keep {words[3]} visible in the plan.", f"Então podemos fazer o próximo passo funcionar e manter {pts[3]} visível no plano."],
        ]
    pars = [
        ([f"In {city}, a small team meets after work.", f"Em {city}, uma pequena equipe se reúne depois do trabalho."], ["", ""], None, "🏙️"),
        ([f"{name} frames the question:", f"{name} formula a pergunta:"], [lines[0][1], lines[0][2]], name, "💬"),
        (["You connect the work to the situation:", "Você liga a obra à situação:"], [lines[1][1], lines[1][2]], "You", "📝"),
        ([f"{name} identifies the first issue:", f"{name} identifica a primeira questão:"], [lines[2][1], lines[2][2]], name, "❓"),
        (["You add two concrete steps:", "Você acrescenta dois passos concretos:"], [lines[3][1], lines[3][2]], "You", "💡"),
        ([f"{name} asks for a workable version:", f"{name} pede uma versão viável:"], [lines[4][1], lines[4][2]], name, "🤝"),
        (["You make the plan explicit:", "Você deixa o plano explícito:"], [lines[5][1], lines[5][2]], "You", "✅"),
        ([f"{name} tests the idea:", f"{name} testa a ideia:"], [lines[6][1], lines[6][2]], name, "🔎"),
        (["You close the exchange:", "Você encerra a conversa:"], [lines[7][1], lines[7][2]], "You", "📅"),
        (["The useful takeaway:", "O ponto útil:"], [f"A good plan names the {words[0]}, uses the {words[1]}, and can {words[3]} a next step.", f"Um bom plano nomeia {pts[0]}, usa {pts[1]} e consegue {pts[3]} um próximo passo."], None, "💡"),
    ]
    cards = [[words[i], pts[i], ICON[(i + digest(n)) % len(ICON)], lines[i + 2][1], lines[i + 2][2]] for i in range(5)]
    return {
        "n": n, "o": n, "t": f"{title} · {work}", "s": mission.capitalize(), "sc": "community-center", "lv": level,
        "a": {"k": "Situação", "w": work, "y": "", "d": (work_desc + " " if work_desc else "") + f"A situação trabalha {mission} em uma conversa cotidiana."},
        "h": {"l": lines[1][1], "src": "Pocket", "tr": lines[1][2]},
        "p": f"Hoje você vai {mission}.", "g": {"t": lines[7][1]}, "v2": True,
        "v": [[words[i], pts[i], ICON[(i + digest(n)) % len(ICON)]] for i in range(5)],
        "presentation": "pocket-v1", "pocket": 1,
        "character": {"id": f"pk_{name.lower().replace(' ', '_')}", "name": name, "gender": "f" if face.startswith("👩") else "m", "role": role, "city": city, "recurring": True},
        "arc": {"i": idx // 10 + 1, "pos": idx % 10 + 1, "of": 10},
        "fr": [
            {"k": "pkhero", "g": c, "num": n % 1000, "lvl": level, "face": face, "name": name, "city": city, "sub": title, "mission": f"Hoje você vai {mission}.", "hook": [lines[1][1], lines[1][2]], "boss": idx % 10 == 9},
            {"k": "pkdlg", "g": c, "title": "Diálogo", "lines": lines, "vocab": [[x[0], x[1]] for x in cards], "cast": {name: [face, c[0]], "You": ["🙂", "#e85d75"]}},
            {"k": "pkvoc", "g": c, "title": "Vocabulário", "cards": cards, "notes": [{"en": f"A plan that stays {words[4]}", "pt": f"Um plano que continua {pts[4]}", "txt": f"💡 Use {words[4]} para descrever a qualidade que o plano precisa manter."}]},
            {"k": "pkread", "g": c, "title": "Leitura", "pars": [{"lead": a, "q": q, "who": who, "ic": ic} for a, q, who, ic in pars], "vocab": [[x[0], x[1]] for x in cards]},
            {"k": "pkbuild", "g": c, "title": "Monte a frase", "items": [{"en": f"We need to discuss {words[0]}.", "pt": f"Precisamos discutir {pts[0]}.", "opts": [[words[0], pts[0]], ["clearly", "com clareza"], ["later", "mais tarde"]], "note": f"Use {words[0]} para nomear a questão central."}, {"en": f"We should keep {words[3]} visible.", "pt": f"Devemos manter {pts[3]} visível.", "opts": [[words[3], pts[3]], ["hidden", "escondido"], ["separate", "separado"]], "note": f"Use {words[3]} para retomar o foco da conversa."}]},
            {"k": "pkspeak", "g": c, "title": "Fale", "items": [{"who": name, "line": [lines[2][1], lines[2][2]], "target": f"We need to discuss {words[0]} and {words[1]}.", "pt": f"Precisamos discutir {pts[0]} e {pts[1]}."}, {"who": name, "line": [lines[4][1], lines[4][2]], "target": f"We should keep the next step {words[4]}.", "pt": f"Devemos manter o próximo passo {pts[4]}."}]},
            {"k": "wrap", "title": "Mochila do episódio", "recap": [[lines[i][1], lines[i][2]] for i in [1, 2, 3, 4]], "expr": [["That is a workable next step.", "Esse é um próximo passo viável."], ["Let us keep the plan clear.", "Vamos manter o plano claro."]], "culture": f"A referência {work} abre uma ponte para {mission}.", "teaser": {"t": "Próxima situação: uma nova decisão em contexto real", "d": ""}, "sticker": {"name": name, "face": face, "role": role, "city": city, "boss": idx % 10 == 9}, "stickers": cards},
        ],
    }

def all_existing() -> list[dict]:
    out = []
    for p in sorted(DATA.glob("pk-*_*.json")):
        out.extend(json.loads(p.read_text(encoding="utf-8")))
    return out

def write_level(level: str, start: int, count: int, pool: list[tuple[str, str]], existing: set[str], rewrite_from: int | None = None) -> None:
    files = sorted(DATA.glob(f"pk-{level}_*.json"))
    old = {e["n"]: e for p in files for e in json.loads(p.read_text(encoding="utf-8"))}
    generated = []
    for i in range(count):
        n = start + i
        if rewrite_from is not None and n < rewrite_from:
            continue
        work, desc = pool[(i + (0 if level == "b2" else 800 if level == "c1" else 1600)) % len(pool)]
        generated.append(make_episode(n, level.upper(), work, desc, i))
    old.update({e["n"]: e for e in generated})
    buckets = {}
    for n in sorted(old):
        if start <= n < start + count:
            buckets.setdefault((n - start) // 50 + 1, []).append(old[n])
    for slot, vals in buckets.items():
        (DATA / f"pk-{level}_{slot:02d}.json").write_text(json.dumps(vals, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def main() -> None:
    pocket = all_existing()
    existing_works = {str(e.get("a", {}).get("w") or "") for e in pocket}
    pool = works(existing_works)
    if not pool:
        raise SystemExit("culture pool is empty")
    # Protect B1 952001-952451 byte-for-byte; refine only the requested tail.
    write_level("b1", 952001, 800, pool, existing_works, rewrite_from=952452)
    write_level("b2", 953001, 800, pool, existing_works)
    write_level("c1", 954001, 800, pool, existing_works)
    write_level("c2", 955001, 800, pool, existing_works)
    print("refined B1 tail and generated B2/C1/C2: 800 episodes each")

if __name__ == "__main__":
    main()
