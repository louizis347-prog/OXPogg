#!/usr/bin/env python3
"""Converte C1/C2 do desenho cultural antigo para regular-pilot-v1.

O conteúdo avançado é reaproveitado dentro da arquitetura dos episódios 2–5:
duas cenas, regra, molde, seis palavras, quatro verbos, quatro expressões,
laboratório, produção e uma ponte cultural incorporada à missão.
"""
from __future__ import annotations

import glob
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSES = ("en-c1", "en-c2")

ICONS = ["🧩", "🎚️", "💡", "🧭", "🎙️", "🪶"]
VERB_PT = {
    "adapt": "adaptar", "analyze": "analisar", "argue": "argumentar", "balance": "equilibrar",
    "build": "construir", "carry": "carregar", "challenge": "desafiar", "clarify": "esclarecer",
    "compare": "comparar", "convey": "transmitir", "create": "criar", "decide": "decidir",
    "defend": "defender", "describe": "descrever", "detect": "detectar", "distinguish": "distinguir",
    "emphasize": "enfatizar", "explain": "explicar", "frame": "enquadrar", "highlight": "destacar",
    "imply": "sugerir", "interpret": "interpretar", "justify": "justificar", "notice": "perceber",
    "observe": "observar", "outline": "delinear", "position": "posicionar", "present": "apresentar",
    "project": "projetar", "question": "questionar", "reframe": "reenquadrar", "reflect": "refletir",
    "relate": "relacionar", "rephrase": "reformular", "respond": "responder", "revise": "revisar",
    "shape": "moldar", "signal": "sinalizar", "soften": "suavizar", "stress": "enfatizar",
    "support": "sustentar", "trace": "rastrear", "transfer": "transferir", "vary": "variar",
    "weigh": "ponderar", "wonder": "perguntar-se", "write": "escrever", "read": "ler",
    "show": "mostrar", "make": "fazer", "use": "usar", "choose": "escolher", "connect": "conectar",
}
STOP = {"the", "and", "with", "from", "that", "this", "into", "when", "what", "which", "your", "have", "has", "been", "were", "will", "would", "could", "should", "about", "there", "their", "they", "them", "then", "than", "just", "only", "more", "most", "some", "very", "here", "does", "did", "not", "for", "are", "was", "you", "she", "her", "his", "our", "its", "can", "how", "why", "who", "all", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"}
GENERIC_CAST = {"woman", "man", "girl", "boy", "mother", "father", "teacher", "student", "friend", "customer", "waiter", "clerk", "lady", "guy", "person", "mulher", "homem"}


def old_frame(e, key):
    return next((x for x in e.get("fr", []) if x.get("k") == key), None)


def clone(value):
    return json.loads(json.dumps(value, ensure_ascii=False))


def scene_lines(e):
    fr = old_frame(e, "scene")
    if fr and fr.get("lines"):
        return clone(fr["lines"])
    return []


def ensure_eight(lines, e, start=0):
    lines = clone(lines)
    work = str((e.get("a") or {}).get("w") or "the work")
    topic = str(e.get("s") or e.get("t") or "the focus")
    cast = list((old_frame(e, "scene") or {}).get("cast", {}).keys()) or ["Zoe", "Grace"]
    while len(lines) < 8:
        i = len(lines)
        speaker = cast[i % len(cast)]
        if i % 2:
            en = f"That detail from {work} changes how we understand {topic}."
            pt = f"Esse detalhe de {work} muda como entendemos {topic}."
        else:
            en = f"I can explain why {topic} matters in this scene."
            pt = f"Consigo explicar por que {topic} importa nesta cena."
        lines.append([speaker, en, pt])
    # A ponte precisa aparecer dentro da fala, mesmo quando a cena original
    # já tinha oito linhas e não precisava de preenchimento estrutural.
    work_fold = work.lower()
    scene_text = " ".join(str(x[1]).lower() for x in lines if isinstance(x, list) and len(x) > 1)
    title_tokens = [x for x in re.findall(r"\w{4,}", work_fold) if x not in STOP]
    if not title_tokens or not any(token in scene_text for token in title_tokens):
        speaker = lines[0][0]
        lines.append([speaker, f"This scene returns to {work} while we practise {topic}.", f"Esta cena retoma {work} enquanto praticamos {topic}."])
    return lines[:]


def scene_cast(e, lines):
    old = old_frame(e, "scene") or {}
    cast = clone(old.get("cast") or {"Zoe": ["👧", "#0c7a78"], "Grace": ["👩", "#2b6cb0"]})
    names = ["Narrator", "Traveler", "Guide", "Guest", "Host"]
    mapping = {}
    used = set(cast)
    for name in list(cast):
        if name.lower() in GENERIC_CAST:
            new = next(n for n in names if n not in used)
            mapping[name] = new
            used.add(new)
    if mapping:
        cast = {mapping.get(k, k): v for k, v in cast.items()}
        for line in lines:
            if line and line[0] in mapping:
                line[0] = mapping[line[0]]
    return cast


def vocab_items(e):
    result = []
    for i, item in enumerate(e.get("v") or []):
        if isinstance(item, list) and len(item) >= 3:
            result.append([item[0], ICONS[i % len(ICONS)], item[1], item[2]])
    while len(result) < 6:
        n = len(result)
        result.append([f"term{n + 1}", ICONS[n % len(ICONS)], "termo em contexto", "pronúncia em contexto"])
    return result[:6]


def extract_verbs(e, lines, existing=None):
    verbs = []
    if existing:
        for item in existing.get("items", []):
            # Preserve the authored verb and its Portuguese gloss.  Restricting
            # this to the tiny fallback dictionary silently discarded valid C1/C2
            # verbs and replaced them with generic ``notice/explain`` items.
            if isinstance(item, dict) and item.get("v"):
                verbs.append(item)
    text = " ".join(str(line[1]).lower() for line in lines if isinstance(line, list) and len(line) > 1)
    for token in re.findall(r"\b[a-z]+\b", text):
        if token in VERB_PT and token not in {str(x.get("v", "")).lower() for x in verbs}:
            verbs.append({"v": token, "pt": VERB_PT[token]})
    fallbacks = ["notice", "explain", "connect", "rephrase"]
    for token in fallbacks:
        if token not in {str(x.get("v", "")).lower() for x in verbs}:
            verbs.append({"v": token, "pt": VERB_PT[token]})
        if len(verbs) >= 4:
            break
    out = []
    for i, item in enumerate(verbs[:4]):
        verb = str(item.get("v"))
        pt = str(item.get("pt") or VERB_PT.get(verb.lower(), "usar"))
        ex = item.get("ex") if isinstance(item, dict) else None
        if not (isinstance(ex, list) and len(ex) == 2 and all(isinstance(x, str) for x in ex)):
            line = lines[(i + 1) % len(lines)]
            ex = [f"The scene lets us {verb} this choice: {line[1]}", f"A cena nos ajuda a {pt} esta escolha: {line[2]}"]
        out.append({"v": verb, "ic": ICONS[i], "pt": pt, "f": [["I", f"I {verb} the point."], ["she", f"She {verb}s the point."]], "ex": ex, "note": f"**{verb}** = {pt}; escolha a forma conforme o sujeito."})
    return out


def expressions(e, lines, vocab):
    out = []
    # cexp stores complete, authored English blocks.  Read it first; xpr's
    # coloured ``b`` segments are a fallback and must be flattened to text.
    for key in ("cexp", "xpr"):
        fr = old_frame(e, key)
        if not fr:
            continue
        for item in fr.get("items", []):
            if isinstance(item, dict):
                phrase = item.get("pt") or item.get("x") or item.get("t")
                en = item.get("x") or item.get("w")
                if not en and isinstance(item.get("b"), list):
                    en = " ".join(str(part[0] if isinstance(part, (list, tuple)) else part)
                                   for part in item["b"])
                if isinstance(en, list): en = " ".join(str(x) for x in en)
                if en and phrase:
                    out.append({"x": str(en), "en": str(en), "pt": str(phrase), "ic": item.get("ic", "💬"), "use": item.get("note") or item.get("use") or "Use este bloco em contexto.", "ex": item.get("ex") or []})
    for i, item in enumerate(vocab):
        if len(out) >= 4: break
        out.append({"x": f"The point is {item[0]}.", "en": f"The point is {item[0]}.", "pt": f"O ponto é {item[2]}.", "ic": ICONS[i], "use": "Expressão em contexto.", "ex": []})
    return out[:4]


def sentence_rule(e, expressions, lines):
    focus = str(e.get("s") or e.get("t") or "Foco da missão")
    pat = old_frame(e, "pat")
    tip = pat.get("tip") if pat else None
    if not tip:
        tip = f"Em nível avançado, observe como {focus} altera a intenção e o registro."
    formula = []
    for i, ex in enumerate(expressions[:3]):
        formula.append({"from": [["subject", 0], ["pattern", 1]], "to": [["subject", 0], ["pattern", 1]], "say": ex["x"], "note": ex["pt"]})
    return {"who": "polly", "head": focus, "sub": "Forma, intenção e registro em contexto.", "say": [tip, f"Use {focus} para escolher uma formulação precisa."], "formula": formula}


def mold_pages(expressions, lines):
    pages = []
    for i, ex in enumerate(expressions[:3]):
        pages.append({"label": ["Estrutura", "Intenção", "Registro"][i], "slots": [[ex["x"], 0], ["in context", 1]], "end": [ex["x"]], "tip": ex["pt"]})
    return {"title": "Molde reutilizável", "say": "Troque uma peça e preserve a intenção.", "pages": pages}


def comprehension(e, lines):
    old = old_frame(e, "dquiz")
    items = []
    if old:
        for q in old.get("items", [])[:3]:
            if isinstance(q, dict):
                opts = q.get("opts") or []
                items.append({"ask": q.get("q", "What is the point?"), "speak": q.get("q", "What is the point?"), "pt": q.get("pt", "O que ficou claro?"), "opts": opts, "a": q.get("a", 0), "why": q.get("why", "A cena mostra essa resposta.")})
    while len(items) < 3:
        i = len(items) % len(lines); line = lines[i]
        items.append({"ask": f"What does {line[0]} say?", "speak": line[1], "pt": f"O que {line[0]} diz?", "opts": [[line[1], line[1]], ["That is another detail.", "Esse é outro detalhe."], ["We do not know.", "Não sabemos."]], "a": 0, "why": line[1]})
    return items


def lab(e, vocab):
    old = old_frame(e, "soundlab")
    if old:
        ex = old.get("ex", [])[:3]
        rounds = old.get("rounds", [])[:3]
    else:
        ex = [[v[0], v[3].replace("Soa como ", "").strip("“”"), v[2], "repare no ritmo"] for v in vocab[:3]]
        rounds = [{"q": "Qual palavra foi dita?", "say": v[0], "opts": [v[0], "another"], "a": 0, "why": f"A palavra é {v[0]}."} for v in vocab[:3]]
    while len(ex) < 3: ex.append([vocab[len(ex)][0], "som em contexto", vocab[len(ex)][2], "repare no ritmo"])
    while len(rounds) < 3: rounds.append({"q": "Qual palavra foi dita?", "say": vocab[len(rounds)][0], "opts": [vocab[len(rounds)][0], "another"], "a": 0, "why": "Confira o som."})
    return {"k": "pglab", "rs": "street", "chars": [["tom", 50, 0, 1.0]], "short": old.get("short", "ritmo e redução") if old else "ritmo e redução", "title": "Laboratório de sons", "say": "Ouça, compare e repita o som em contexto.", "intro": old.get("intro", {}) if old else {"what": "O ritmo muda o sentido.", "how": "Repita a sequência com atenção.", "pt": "Não leia cada palavra isoladamente."}, "ex": ex[:3], "pairs": old.get("pairs", [])[:3] if old else [], "tip": old.get("tip", "Repare no ritmo e na redução sonora.") if old else "Repare no ritmo e na redução sonora.", "phrase": [f"{vocab[0][0]} in context.", f"{vocab[0][2]} em contexto."], "rounds": rounds[:3], "avatar": 1}


def make_episode(e, prev):
    old = {x.get("k"): x for x in e.get("fr", [])}
    lines = ensure_eight(scene_lines(e), e)
    cast = scene_cast(e, lines)
    old_tdlg = old.get("tdlg") or {}
    second = []
    for turn in old_tdlg.get("turns", []):
        n = turn.get("n") or []
        opts = turn.get("o") or []
        answer = turn.get("a", 0)
        if len(n) >= 2 and opts and isinstance(opts[answer], list) and len(opts[answer]) >= 2:
            second.append([old_tdlg.get("cast", {}).get("npc", ["Zoe"])[-1], n[0], n[1]])
            second.append([old_tdlg.get("cast", {}).get("you", ["Grace"])[-1], opts[answer][0], opts[answer][1]])
    second = ensure_eight(second or lines, e, 1)
    vocab = vocab_items(e)
    verbs = extract_verbs(e, lines, old.get("verbs"))
    expr = expressions(e, lines, vocab)
    work = str((e.get("a") or {}).get("w") or "a cultural reference")
    focus = str(e.get("s") or e.get("t") or "the lesson focus")
    cover = clone(old.get("cover") or {"k": "cover"})
    cover["k"] = "cover"
    cover.setdefault("badge", e.get("th", "C1"))
    cover["sub"] = focus
    cover["gancho"] = [lines[0][0], f"This scene returns to {work}. What do you notice?", f"Esta cena retoma {work}. O que você percebe?"]
    cover["obra"] = f"{work} · {(e.get('a') or {}).get('y', '')}"
    cover["say"] = f"A obra {work} abre a missão de {focus}."
    review = clone(old.get("review")) if old.get("review") else {"k": "review", "prev": prev.get("t", "A missão anterior") if prev else "", "work": (prev.get("a") or {}).get("w", "") if prev else "", "recap": [], "bag": [], "lead": "Retome a missão anterior antes de avançar.", "next": f"Hoje: {focus}", "say": "Abra a mochila e recupere o fio da trilha.", "rs": "park", "chars": [["tom", 32, 0, 1.0], ["tommy", 68, 1, 1.0]]}
    if prev and not review.get("prev"): review["prev"] = prev.get("t", "A missão anterior")
    review["k"] = "review"
    hotscene = {"k": "hotscene", "title": "Entre na cena cultural", "hint": "Toque nas pistas e escute a referência.", "rs": e.get("sc", "street"), "chars": [["polly", 34, 0, 1.0], ["tommy", 68, 1, 1.0]], "hot": [{"e": "🎭", "x": 15, "y": 18, "en": work, "pt": "obra cultural", "say": f"This is {work}.", "sayPt": f"Esta é a obra {work}."}, {"e": "💡", "x": 38, "y": 18, "en": focus, "pt": "foco", "say": f"The focus is {focus}.", "sayPt": f"O foco é {focus}."}, {"e": "🎧", "x": 62, "y": 18, "en": "context", "pt": "contexto", "say": "Notice the context.", "sayPt": "Observe o contexto."}, {"e": "🗣️", "x": 84, "y": 18, "en": "voice", "pt": "voz", "say": "Listen to the voice.", "sayPt": "Ouça a voz."}, {"e": "🔎", "x": 50, "y": 82, "en": "detail", "pt": "detalhe", "say": "Find the detail.", "sayPt": "Encontre o detalhe."}], "say": "A obra entra na aula por uma situação concreta.", "obra": {"name": work, "kind": (e.get("a") or {}).get("k", "referência cultural"), "text": (e.get("a") or {}).get("d", "")}}
    pgsheet_comp = {"k": "pgsheet", "title": "Confira sua compreensão", "items": comprehension(e, lines), "rs": "street", "chars": [["tommy", 50, 0, 1.0]], "review": False, "bubble": [lines[1][0], "What stands out from the scene?", "Qual detalhe ficou na memória?"], "avatar": 1}
    pgrule = {"k": "pgrule", "rule": sentence_rule(e, expr, lines), "say": f"Descubra como {focus} organiza a intenção.", "rs": "cafe", "chars": [["polly", 50, 0, 1.0]], "bubble": [lines[0][0], "Notice the pattern.", "Observe o padrão."], "avatar": 1}
    pgmold = {"k": "pgmold", **mold_pages(expr, lines), "rs": "lobby1", "chars": [["tommy", 50, 0, 1.0]], "bubble": [lines[0][0], "Change one piece.", "Troque uma peça."], "avatar": 1}
    words_frame = {"k": "pgsheet", "title": "Vocabulário ativo", "items": [{"fig": vocab[i][1], "say": vocab[i][0], "ask": "Escute e selecione a palavra.", "opts": [vocab[i][0], "another", "different"], "a": 0, "why": f"{vocab[i][0]} = {vocab[i][2]}."} for i in range(6)], "rs": "park", "chars": [["tommy", 50, 0, 1.0]], "bubble": [lines[0][0], "Find the active words.", "Encontre as palavras ativas."], "avatar": 1}
    verbs_frame = {"k": "verbs", "title": "Verbos do episódio", "items": verbs, "tip": f"Quatro verbos úteis para {focus}.", "say": "Use os verbos em uma frase própria.", "coach": f"Relacione os verbos ao foco {focus}."}
    vplay = {"k": "vplay", "title": "Verbos em ação", "items": clone(verbs), "plan": [[0, 0], [1, 0], [2, 0], [3, 0], [0, 3], [1, 3], [2, 3]], "say": "Monte as frases e escolha a forma precisa.", "coach": f"Use os verbos para interpretar {focus}."}
    exp_frame = {"k": "pgexp", "title": "Expressões em contexto", "items": expr, "say": "Aprenda cada expressão como um bloco reutilizável.", "coach": f"Leve as expressões de {focus} para uma situação nova."}
    phrase_frame = {"k": "pgsheet", "title": "Palavras em frases reais", "items": [{"fig": vocab[i][1], "say": vocab[i][0], "ask": "Qual palavra completa a ideia?", "opts": [vocab[i][0], "another", "different"], "a": 0, "why": f"A frase retoma {vocab[i][0]} em contexto."} for i in range(6)], "rs": "cafe2", "chars": [["tommy", 50, 0, 1.0]], "bubble": [lines[1][0], "Read the context.", "Leia o contexto."], "avatar": 1}
    quiz_frame = {"k": "pgsheet", "title": "Escolha a formulação precisa", "items": [{"ask": f"Que formulação preserva {focus}?", "opts": [expr[i % 4]["x"], expr[(i + 1) % 4]["x"], expr[(i + 2) % 4]["x"]], "a": 0, "why": expr[i % 4]["pt"], "say": expr[i % 4]["x"]} for i in range(4)], "rs": "street", "chars": [["tommy", 50, 0, 1.0]], "bubble": [lines[0][0], "Choose the precise version.", "Escolha a versão precisa."], "avatar": 1}
    pglab = lab(e, vocab)
    speak = {"k": "pgspeak", "title": "Agora é com você", "items": [[line[1], line[2]] for line in second[:5]], "who": second[0][0], "say": "Ouça cada frase e repita com ritmo.", "rs": "park", "chars": [["tom", 32, 0, 1.0], ["tommy", 68, 1, 1.0]]}
    produce = old.get("produce") or {}
    model = str(produce.get("model") or second[0][1])
    mission_data = []
    for i, label in enumerate(["Cena da obra", "Transferência", "Produção avançada"]):
        prompt = str(produce.get("prompt") or f"Use {focus} em uma resposta própria.")
        if i == 0: prompt = f"Na referência {work}, {prompt}"
        elif i == 1: prompt = f"Leve {focus} para uma situação cotidiana: {prompt}"
        else: prompt = f"Defenda uma escolha de linguagem em {focus}: {prompt}"
        mission_data.append({"ic": ["🎬", "🧭", "🎤"][i], "name": label, "desc": "Produza uma resposta completa.", "data": {"prompt": prompt, "ph": "Escreva como você responderia…", "chips": [verbs[i]["v"]], "model": model, "check": [f"Usei {verbs[i]['v']}?", f"Liguei a resposta a {focus}?", "Mantive o registro adequado?"], "kw": [rf"\b{re.escape(verbs[i]['v'])}\b", rf"\b{re.escape(work.split()[0])}\b", rf"\b{re.escape(verbs[(i+1)%4]['v'])}\b"], "tips": [[[f"I {verbs[i]['v']} the point.", f"Eu {verbs[i]['pt']} o ponto."]], [[second[i][1], second[i][2]]], [[f"This choice reflects {focus}.", f"Essa escolha reflete {focus}."]]], "ok": ["Precisão! 🎯", "Contexto! 🎬", "Registro! 🗣️"], "reply": ["Good work.", "Bom trabalho."]}})
    mission = {"k": "pgmission", "title": "Missão de produção", "missions": mission_data, "rs": "counter", "chars": [["tom", 50, 0, 1.0]], "say": "Escolha uma missão e coloque o inglês em ação.", "bubble": [second[0][0], "Choose a mission and keep speaking!", "Escolha uma missão e continue falando!"], "avatar": 1}
    wrap_old = old.get("wrap") or {}
    wrap = clone(wrap_old)
    wrap.update({"k": "wrap", "title": "O que fica da aula", "recap": [[v[0], v[2]] for v in vocab[:4]], "rs": "bedroom", "chars": [["tom", 32, 0, 1.0], ["tommy", 68, 1, 1.0]], "sticker": {"title": work, "sub": f"{work} · {(e.get('a') or {}).get('y','')}", "rs": e.get("sc", "street"), "chars": [["tom", 34, 0, 1.0], ["tommy", 68, 1, 1.0]]}})
    frames = [cover]
    if prev is not None: frames.append(review)
    frames.extend([hotscene, {"k": "pgscene", "cast": cast, "lines": lines, "speakers": cast, "rs": e.get("sc", "street"), "chars": [["polly", 34, 0, 1.0], ["tommy", 68, 1, 1.0]], "say": "Escute a cena e acompanhe o contexto."}, pgsheet_comp, pgrule, pgmold, words_frame, verbs_frame, vplay, exp_frame, {"k": "pgscene", "title": "Uma segunda situação", "cast": cast, "lines": second, "speakers": cast, "rs": "kitchen", "chars": [["polly", 34, 0, 1.0], ["tommy", 68, 1, 1.0]], "say": "Transfira o foco para outra situação."}, phrase_frame, quiz_frame, pglab, {"k": "pgsheet", "title": "Escreva na tela", "items": [{"fig": "✍️", "say": v[0], "ask": "Trace e escreva de memória.", "opts": [v[0], "another"], "a": 0, "why": f"{v[0]} é uma palavra da missão."} for v in vocab[:4]], "rs": "desk", "chars": [["tommy", 50, 0, 1.0]], "bubble": [second[0][0], "Write it from memory.", "Escreva de memória."], "avatar": 1}, speak, mission, wrap])
    e["fr"] = frames
    e["presentation"] = "regular-pilot-v1"
    e["pilot"] = 1
    e["reorg"] = 1
    return e


def process_course(course):
    episodes = []
    paths = []
    for name in sorted(glob.glob(str(ROOT / "data" / f"{course}_*.json"))):
        path = Path(name); paths.append(path); episodes.extend(json.loads(path.read_text(encoding="utf-8")))
    episodes.sort(key=lambda e: int(e.get("n") or 0))
    prev = None
    for e in episodes:
        make_episode(e, prev)
        prev = e
    by_path = {}
    for path in paths: by_path[path] = []
    for e in episodes:
        for path in paths:
            # IDs are unique; recover the original shard by range/order.
            if any(x.get("n") == e.get("n") for x in json.loads(path.read_text(encoding="utf-8"))):
                by_path[path].append(e); break
    for path, data in by_path.items():
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        os.replace(tmp, path)
    return len(episodes)


def main():
    total = sum(process_course(c) for c in COURSES)
    print("episódios convertidos", total)


if __name__ == "__main__":
    main()
