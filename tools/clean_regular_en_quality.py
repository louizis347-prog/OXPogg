#!/usr/bin/env python3
"""Remove generated boilerplate from the regular English course.

The v2 reorganisation gave the 5,000 lessons a stable, varied frame
architecture. This pass is deliberately data-only: it keeps episode IDs and
frame kinds intact while making the learner-facing copy specific to the
lesson, aligning cultural sources, and adding a contextual vocabulary bridge
to A2 (where the old bank was smaller than A1).
"""

from __future__ import annotations

import glob
import json
import os
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OLD_SUBJECT = "Regra, som, expressões e escrita"
MARKER = re.compile(r"\b(?:Episódio|Episode)\s*#?\s*\d+\s*[:·-]\s*", re.I)

PT_MISSION = {
    "encontro": "conhecer alguém e manter a conversa natural",
    "problema": "esclarecer um problema e chegar a uma solução prática",
    "descoberta": "observar um detalhe cultural e explicar o que ele significa",
    "projeto": "negociar o próximo passo e realizar um plano em conjunto",
}
PT_LOCATION = {
    "at the café": "na cafeteria", "at the diner": "na lanchonete", "on the subway": "no metrô",
    "at the station": "na estação", "at the airport": "no aeroporto", "at work": "no trabalho",
    "in the studio": "no estúdio", "in class": "na aula", "at school": "na escola",
    "at the library": "na biblioteca", "at the museum": "no museu", "at the market": "no mercado",
    "at the shop": "na loja", "in the park": "no parque", "at the beach": "na praia",
    "in the kitchen": "na cozinha", "at home": "em casa", "at the restaurant": "no restaurante",
    "at the clinic": "na clínica", "at the hotel": "no hotel", "in the lobby": "no saguão",
    "on the street": "na rua", "in the city": "na cidade", "in a real-life situation": "em uma situação real",
}
PT_LOCATION_CODE = {
    "cafe": "na cafeteria", "cafe2": "na cafeteria", "cafe3": "na cafeteria",
    "office": "no escritório", "outdoors": "ao ar livre", "home": "em casa",
    "city": "na cidade", "school": "na escola", "harbor": "no porto",
    "restaurant": "no restaurante", "party": "na festa", "park": "no parque",
    "airport": "no aeroporto", "ballroom": "no salão", "road": "na estrada",
    "hospital": "no hospital", "shop": "na loja", "gym": "na academia",
    "diner": "na lanchonete", "railway": "na ferrovia", "library": "na biblioteca",
    "fifth": "na Quinta Avenida", "lobby1": "no saguão", "lobby2": "no saguão",
    "home1": "em casa", "living": "na sala", "street": "na rua", "yard": "no quintal",
    "station": "na estação", "market": "no mercado", "nyc": "em Nova York",
    "park2": "no parque", "lake": "no lago", "sub2": "no metrô", "pier": "no píer",
    "airport2": "no aeroporto", "flags": "na praça", "tick": "no relógio",
}

COACHES = {
    "mission": [
        "Objetivo da cena: praticar {topic} enquanto você resolve {mission}. Prepare uma resposta própria.",
        "Comece pela situação: use {topic} para cumprir a missão de {mission} com clareza.",
    ],
    "cultural_anchor": [
        "Observe como {work} ilumina {topic}; depois ligue a referência à missão de {mission}.",
        "A obra {work} abre uma janela para {topic}. Repare no detalhe que ajuda a resolver {mission}.",
    ],
    "work_depth": [
        "Aprofunde {work} e encontre uma ideia que possa voltar na conversa sobre {topic}.",
        "Neste detalhe de {work}, procure a intenção que também aparece em {topic}.",
    ],
    "interpretive_scene": [
        "Interprete a cena de {work} e conecte sua decisão linguística a {topic}.",
        "Leia a cena como uma pista: o que {work} acrescenta à situação de {topic}?",
    ],
    "timeline": [
        "Use a linha do tempo de {work} para contextualizar {topic} antes de falar.",
        "Relacione o momento histórico de {work} à escolha de palavras em {topic}.",
    ],
    "cultural_challenge": [
        "Teste sua leitura de {work} e aplique a ideia à missão linguística {topic}.",
        "Resolva o desafio cultural: a resposta precisa combinar {work} e {topic}.",
    ],
    "cultural_language_bridge": [
        "Faça a ponte entre {work} e {topic}; explique como a mesma intenção funciona na vida real.",
        "Leve a referência de {work} para uma frase útil em {topic}.",
    ],
    "active_vocabulary": [
        "Ative este repertório em uma frase nova sobre {topic}; confira pronúncia e registro.",
        "Escolha duas palavras e use-as para avançar em {mission}; não apenas reconheça, produza.",
    ],
    "words_in_context": [
        "Veja cada palavra funcionando em uma situação de {topic}; depois crie uma frase sua.",
        "O contexto decide o sentido: use o repertório de {topic} em uma resposta completa.",
    ],
    "pattern_vocabulary": [
        "Observe os verbos em ação e escolha um para continuar a missão de {mission}.",
        "Conjugue estes verbos dentro de {topic}; a forma precisa acompanhar a intenção.",
    ],
    "daily_scene": [
        "Na cena cotidiana, faça {topic} soar natural; toda fala deve ter uma função.",
        "Entre na conversa e resolva {mission} usando o padrão de {topic}.",
    ],
    "listening_practice": [
        "Escute o ritmo de {topic}; identifique a palavra que muda a intenção da fala.",
        "Ouça até o fim antes de decidir: a pista sonora de {topic} está na redução e no acento.",
    ],
    "context_challenge": [
        "Transfira {topic} para dois contextos e escolha a forma que mantém a intenção.",
        "Mude a situação, não o sentido: aplique {topic} em uma resposta natural e outra cuidadosa.",
    ],
    "comprehension": [
        "Comprove que entendeu: explique por que a resposta combina com {topic}.",
        "Volte às pistas da cena e justifique sua escolha em {topic}.",
    ],
    "retrieval": [
        "Recupere a ideia anterior e relacione-a a {topic}; depois avance para a próxima missão.",
        "Reative uma frase do percurso e adapte-a à situação de {topic}.",
    ],
    "free_production": [
        "Produza uma resposta própria sobre {topic}; reutilize uma ideia anterior com nova intenção.",
        "Agora você conduz a conversa: resolva {mission} sem copiar o modelo.",
    ],
    "story_thread": [
        "Siga o fio: a situação anterior prepara {topic}; escolha a próxima fala com intenção.",
        "Continue a história levando {topic} para a próxima decisão comunicativa.",
    ],
    "retrieval_and_next_mission": [
        "Feche a missão retomando {topic} e leve uma frase sua para a próxima situação.",
        "Recupere o que funcionou em {topic}, transforme a frase e prepare o próximo passo.",
    ],
}


def load_rows():
    paths = sorted(Path(p) for p in glob.glob(str(DATA / "en-*.json")))
    rows_by_path = {}
    rows = []
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        rows_by_path[path] = [str(e.get("n")) for e in data]
        rows.extend(data)
    if len(rows) != 5000:
        raise SystemExit(f"esperava 5.000 episódios regulares de inglês, encontrei {len(rows)}")
    return rows, rows_by_path


def frame(ep, kind):
    return next((f for f in ep.get("fr", []) if f.get("k") == kind), None)


def work_name(ep):
    return str((ep.get("a") or {}).get("w") or "a referência cultural")


def target_words(ep):
    out = []
    for item in ep.get("v") or []:
        if isinstance(item, list) and item and item[0]:
            out.append(str(item[0]))
    return out


def mission_context(ep):
    lesson = ep.get("lesson") or {}
    mtype = str(lesson.get("missionType") or "encontro")
    mission = PT_MISSION.get(mtype, str(lesson.get("mission") or "comunicar com clareza")).lower()
    raw_loc = str(ep.get("rs") or ep.get("sc") or "")
    loc = PT_LOCATION.get(raw_loc, PT_LOCATION_CODE.get(raw_loc, "em uma situação real"))
    topic = str(ep.get("t") or "a situação de hoje").strip()
    return mission, loc, topic, mtype


def coach_text(ep, role, index):
    mission, _loc, topic, _mtype = mission_context(ep)
    templates = COACHES.get(role) or COACHES["context_challenge"]
    return templates[index % len(templates)].format(topic=topic, mission=mission, work=work_name(ep))


def replace_recursive(value, topic, strip_marker=True):
    if isinstance(value, dict):
        return {k: replace_recursive(v, topic, strip_marker) for k, v in value.items()}
    if isinstance(value, list):
        return [replace_recursive(v, topic, strip_marker) for v in value]
    if isinstance(value, str):
        text = value.replace(OLD_SUBJECT, topic)
        text = text.replace("reduces the risk of sounding abrupt or presumptuous", "keeps the request clear in this situation")
        text = text.replace("makes the intention explicit", "makes this intention explicit")
        text = text.replace("Continue the thread with a new situation", "Carry the idea into a new situation")
        return MARKER.sub("", text) if strip_marker else text
    return value


def canonical_source(ep):
    return f"{work_name(ep)} · referência cultural; cena adaptada didaticamente para esta missão."


def cultural_description(ep):
    work = work_name(ep)
    detail = str((ep.get("a") or {}).get("d") or "").strip()
    if len(detail) >= 100 and not detail.startswith("A cultural reference") and work.lower() in detail.lower():
        return detail
    return (
        f"{work} é a referência cultural desta aula. Ela oferece um ponto de vista para observar "
        f"como a linguagem de {ep.get('t') or 'hoje'} funciona em uma situação concreta."
    )


def repair_cultural_content(ep, fr, topic):
    """Do not leave a frame labelled with one work while describing another."""
    work = work_name(ep)
    blob_key = fr.get("k")
    if blob_key == "cultob":
        blob = json.dumps(fr.get("panels") or [], ensure_ascii=False)
        if work.lower() not in blob.lower():
            fr["panels"] = [cultural_description(ep),
                            f"Na missão, use essa referência para interpretar {topic} e formular uma resposta própria."]
    elif blob_key == "cultx":
        blob = json.dumps(fr.get("tiles") or [], ensure_ascii=False)
        if work.lower() not in blob.lower():
            fr["tiles"] = [
                {"ic": "💡", "l": "Contexto", "t": cultural_description(ep)},
                {"ic": "🎯", "l": "Ponte para a vida real",
                 "t": f"Retire uma ideia de {work} e aplique-a a {topic} em uma frase sua."},
            ]
    elif blob_key == "cultcena":
        blob = json.dumps({k: fr.get(k) for k in ("ctx", "leitura", "link", "lines")}, ensure_ascii=False)
        if work.lower() not in blob.lower():
            fr["mode"] = "scene"
            fr["lines"] = []
            fr["hl"] = []
            fr["ctx"] = f"A referência {work} oferece o contexto cultural para esta adaptação didática de {topic}."
            fr["leitura"] = [
                cultural_description(ep),
                f"Leia a situação como uma ponte: a ideia de {work} ajuda a escolher palavras e intenção em {topic}.",
            ]
            fr["link"] = f"{work} funciona como lente cultural; agora leve essa perspectiva para uma conversa sobre {topic}."
    elif blob_key == "cultgame":
        blob = json.dumps(fr.get("rounds") or [], ensure_ascii=False)
        if work.lower() not in blob.lower():
            kind = str((ep.get("a") or {}).get("k") or "referência cultural")
            fr["rounds"] = [
                {"t": "order", "items": [f"Referência cultural: {work}.",
                                            f"Foco da missão: {topic}."]},
                {"t": "mc", "q": f"“{work}” é a referência cultural desta missão?",
                 "o": [f"Sim — {kind}", "Não — é outra obra", "A pergunta não se aplica"],
                 "a": 0, "why": f"{work} é a referência escolhida para contextualizar {topic}."},
            ]


def add_a2_bridge(ep, bridge):
    """Add one meaningful, sourced lexical bridge without changing frame count."""
    if not bridge:
        return
    word, pt, pron = bridge[:3]
    existing = {str(x[0]) for x in (ep.get("v") or []) if isinstance(x, list) and x}
    if word in existing:
        return
    ep.setdefault("v", []).append([word, pt, pron])
    words = frame(ep, "words")
    if words is not None:
        words.setdefault("items", []).append([word, "🔎", pt, pron])
    wsent = frame(ep, "wsent")
    if wsent is not None:
        wsent.setdefault("items", []).append({"w": word, "ic": "🔎", "en": word, "pt": pt, "py": pron})
    lplay = frame(ep, "lplay")
    if lplay is not None:
        rounds = lplay.setdefault("rounds", [])
        if len(rounds) < 8:
            opts = [word]
            for x in (ep.get("v") or []):
                if isinstance(x, list) and x and str(x[0]) != word:
                    opts.append(str(x[0]))
                if len(opts) == 3:
                    break
            rounds.append({"t": "w", "say": word, "opts": opts, "a": 0,
                           "why": f"{word} aparece na situação de {ep.get('t')}; ouça e use-o em uma frase."})


def _sentence_candidates(ep):
    """Collect target-language sentences already present in this episode."""
    out = []
    for fr in ep.get("fr", []):
        if fr.get("k") not in {"scene", "convo", "dquiz", "cexp", "xpr", "verbs", "vplay", "pat", "sbuild", "soundlab", "tdlg"}:
            continue
        def visit(value):
            if isinstance(value, dict):
                for key, child in value.items():
                    if key in {"pt", "tr", "coach", "episodeFocus", "src", "title", "say", "intro", "tip", "note", "why", "hint", "lead"}:
                        continue
                    visit(child)
            elif isinstance(value, list):
                for child in value:
                    visit(child)
            elif isinstance(value, str):
                text = value.strip()
                if 8 <= len(text) <= 180 and text.count(" ") >= 2 and re.search(r"[A-Za-z]", text):
                    out.append(text.replace("{{", "").replace("}}", ""))
        visit(fr)
    return list(dict.fromkeys(out))


def repair_wsent(ep):
    """Make every 'Palavras em frases' card a real, audible sentence."""
    candidates = _sentence_candidates(ep)
    ws = frame(ep, "wsent")
    if not ws:
        return
    topic = str(ep.get("t") or "today's situation")
    for item in ws.get("items") or []:
        if not isinstance(item, dict):
            continue
        word = str(item.get("w") or "").strip()
        if not word:
            continue
        selected = None
        rx = re.compile(re.escape(word), re.I)
        for candidate in candidates:
            if rx.search(candidate):
                selected = candidate
                break
        if selected is None:
            selected = f"I can use '{word}' in this situation."
        selected = rx.sub(lambda m: "{{" + m.group(0) + "}}", selected, count=1)
        item["en"] = selected


def patch_episode(ep, bridge=None):
    mission, loc, topic, _mtype = mission_context(ep)
    work = work_name(ep)
    level = str((ep.get("lesson") or {}).get("level") or "A1")
    unit = (ep.get("lesson") or {}).get("unit") or ep.get("o") or ep.get("n")
    words = target_words(ep)
    lexical = ", ".join(words[:3]) if words else topic
    ep["s"] = f"{mission.capitalize()} {loc}: foco em {topic}."
    ep["p"] = f"Missão {unit}: {mission} {loc}. Foco linguístico: {topic}. Referência cultural: {work}."
    ep["episodeFocus"] = ep["p"]
    ep["levelProgression"] = (
        f"{level}: {topic}. Amplie {lexical} em uma situação de {mission}; "
        "recupere uma ideia anterior e produza uma resposta nova."
    )

    ep["fr"] = replace_recursive(ep.get("fr", []), topic)
    for i, fr in enumerate(ep.get("fr", [])):
        kind = fr.get("k")
        role = str(fr.get("lessonRole") or "context_challenge")
        repair_cultural_content(ep, fr, topic)
        fr["episodeFocus"] = ep["p"]
        if "levelProgression" in fr or kind in {"cover", "fio", "produce", "wrap"}:
            fr["levelProgression"] = ep["levelProgression"]
        if "coach" in fr or kind in {"cover", "fio", "wrap", "cexp", "xpr", "ctxv", "review"}:
            fr["coach"] = coach_text(ep, role, i)
        if kind == "cover":
            fr["sub"] = f"Missão: {mission} {loc}. Foco: {topic}."
            fr["say"] = f"Sua missão é {mission} {loc}; hoje você pratica {topic}."
            cw = fr.get("cw")
            if isinstance(cw, dict):
                old = str(cw.get("work") or "")
                cw["work"] = work
                cw["kind"] = (ep.get("a") or {}).get("k", cw.get("kind", "📖"))
                cw["year"] = (ep.get("a") or {}).get("y", cw.get("year", ""))
                if old and old != work:
                    cw["intro"] = f"A referência **{work}** abre a missão. Observe como **{topic}** transforma uma ideia cultural em linguagem útil."
                    cw["fact"] = ["📚", "Você sabia?", f"Nesta aula, {work} serve como ponte para praticar {topic} em uma situação cotidiana."]
        elif kind == "cultcena":
            fr["work"] = work
            fr["src"] = canonical_source(ep)
        elif kind in {"cultob", "cultx", "cultgame", "bridge"}:
            fr["work"] = work
        elif kind == "ctxv":
            variants = [
                "Ouça as situações de {topic} e complete cada lacuna com a palavra que mantém a intenção.",
                "Escute quatro contextos de {topic}; reconstrua as falas e compare as escolhas.",
                "Atenção ao som: complete cada situação de {topic} antes de olhar a explicação.",
                "Leve {topic} para novas situações: ouça, complete e diga a resposta em voz alta.",
            ]
            fr["title"] = f"Escuta em contexto · {topic}"
            fr["say"] = variants[i % len(variants)].format(topic=topic)
        elif kind == "cexp":
            fr["title"] = f"Expressões em contexto · {topic}"
        elif kind == "xpr":
            fr["title"] = f"Expressões coringa · {topic}"
        elif kind == "review":
            fr["title"] = f"Recuperação ativa · {topic}"
            fr["lead"] = f"Recupere uma ideia anterior e transfira-a para {topic}."
            fr["next"] = f"Agora: **{topic}** — use a lembrança anterior para resolver a missão de hoje."
            recap = fr.setdefault("recap", [])
            if not any(isinstance(row, list) and row and str(row[0]) == topic for row in recap):
                recap.append([topic, f"Use {topic} em uma frase nova."])
        elif kind == "wrap":
            fr["title"] = f"Recupere e leve adiante · {topic}"
            fr["teaser"] = {"t": "Próxima missão", "d": f"Leve {topic} para uma nova situação {loc}; transforme uma frase e use-a em outro contexto."}
        for key in ("rounds", "items"):
            seq = fr.get(key)
            if not isinstance(seq, list):
                continue
            for item in seq:
                if not isinstance(item, dict):
                    continue
                if item.get("why") == "A expressão aparece na cena e no vocabulário deste episódio.":
                    candidate = item.get("say") or item.get("w") or item.get("x") or topic
                    item["why"] = f"{candidate} reaparece na situação de {topic}; confirme o sentido pelo contexto e pelo som."

    if isinstance(ep.get("h"), dict):
        ep["h"]["src"] = canonical_source(ep)
    add_a2_bridge(ep, bridge if level == "A2" else None)
    repair_wsent(ep)


def build_a2_bank(rows):
    a1 = []
    a2_words = set()
    for ep in rows:
        level = str((ep.get("lesson") or {}).get("level") or "")
        for item in ep.get("v") or []:
            if not isinstance(item, list) or len(item) < 3 or not item[0]:
                continue
            word = str(item[0]).strip()
            if level == "A2":
                a2_words.add(word)
            elif level == "A1":
                a1.append(item[:3])
    out = []
    seen = set(a2_words)
    for item in a1:
        word = str(item[0]).strip()
        if word and word not in seen and re.search(r"[A-Za-z]", word):
            out.append(item)
            seen.add(word)
    return out


def write(rows, rows_by_path):
    by_id = {str(e.get("n")): e for e in rows}
    for path, ids in rows_by_path.items():
        old = json.loads(path.read_text(encoding="utf-8"))
        out = [by_id[str(e.get("n"))] for e in old]
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
        os.replace(tmp, path)


def main():
    rows, rows_by_path = load_rows()
    bank = build_a2_bank(rows)
    a2 = [e for e in rows if str((e.get("lesson") or {}).get("level") or "") == "A2"]
    needs = [e for e in a2 if len(e.get("v") or []) < 7]
    if len(bank) < len(needs):
        raise SystemExit(f"banco A1 insuficiente para a ponte A2: {len(bank)} < {len(needs)}")
    pending = iter(bank[:len(needs)])
    for ep in rows:
        bridge = next(pending, None) if ep in needs else None
        patch_episode(ep, bridge)
    write(rows, rows_by_path)
    print(f"atualizados {len(rows)} episódios; ponte lexical A2 já presente em {len(a2) - len(needs)} episódios; adicionada em {len(needs)}")


if __name__ == "__main__":
    main()
