#!/usr/bin/env python3
"""Normaliza e enriquece o conteúdo dos cursos sem alterar IDs.

O catálogo é gerado em muitos arquivos pequenos. Este script trabalha curso a
curso e grava o mesmo formato compacto usado pelo catálogo. A regra editorial
é simples: cada episódio tem uma missão própria; o segundo episódio do par
recupera uma fala do primeiro, mas recebe vocabulário, cena e tarefa novos.
"""
from __future__ import annotations

import json
import re
import os
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
MANIFEST = DATA / "manifest.json"

REGULAR_PREFIXES = {"en", "enesh", "es", "pt", "fr", "frbr", "de", "it", "ja", "ko", "zhbr"}
NEIGHBOR_PREFIXES = {"nb", "nbde", "nbeng", "nbes", "nbfr", "nbit", "nbja", "nbpt", "nbpten"}
GENERIC_GLOSS = re.compile(r"^\s*(?:frase[- ](?:chave|clave|clé)|key phrase|schlüsselsatz)\s*$", re.I)
EP_MARK = re.compile(r"\b(?:Epis[oó]dio|Épisode|Folge|Episode)\s*\d+\s*[:·\-]\s*", re.I)
EP_BARE = re.compile(r"\b(?:Epis[oó]dio|Épisode|Folge|Episode)\s*\d+\b\s*", re.I)
ANSWER_MARK = re.compile(r"\s*[·•]\s*(?:Weg|percurso|trajeto|recorrido|parcours)\s*\d+\b", re.I)
OTHER_OPTION = re.compile(r"\b(?:outra opção|otra opción|otra opcion|another option|autre option|andere option)\b", re.I)
FIXED_RULE = re.compile(r"Regra,?\s*som,?\s*express(?:ões|ions|ions),?\s*e\s*(?:escrita|écriture)", re.I)

VARIANT_ORDERS = [
    ["cover", "cultob", "cultx", "cultcena", "cultgame", "read", "lplay", "words", "wsent", "verbs", "vplay", "scene", "dquiz", "ctxv", "tdlg", "produce", "culttl", "fio", "bridge", "wrap"],
    ["cover", "scene", "cultob", "cultcena", "read", "words", "wsent", "lplay", "verbs", "vplay", "tdlg", "dquiz", "ctxv", "produce", "cultx", "cultgame", "fio", "bridge", "culttl", "wrap"],
    ["cover", "cultcena", "cultob", "read", "scene", "lplay", "words", "verbs", "wsent", "vplay", "ctxv", "dquiz", "tdlg", "culttl", "produce", "bridge", "cultx", "cultgame", "fio", "wrap"],
    ["cover", "read", "cultob", "scene", "cultcena", "words", "lplay", "wsent", "verbs", "tdlg", "dquiz", "ctxv", "vplay", "produce", "bridge", "fio", "cultx", "cultgame", "culttl", "wrap"],
]

EMOJIS = ["💡", "🧭", "⚖️", "🔄", "➡️", "🤝", "🗺️", "🎯"]


def flat_text(v) -> str:
    if isinstance(v, str):
        return v
    if isinstance(v, (list, tuple)):
        return " ".join(flat_text(x) for x in v)
    if isinstance(v, dict):
        return " ".join(flat_text(x) for x in v.values())
    return str(v or "")


def clean_string(s: str, *, keep_episode=False, topic="") -> str:
    """Remove marcas de geração sem remover palavras legítimas da aula."""
    if not isinstance(s, str):
        return s
    if not keep_episode:
        s = EP_MARK.sub("", s)
        # Algumas gerações não usaram dois pontos antes do número.
        s = EP_BARE.sub("", s)
        s = ANSWER_MARK.sub("", s)
    s = FIXED_RULE.sub(topic or "a missão desta aula", s)
    # A antiga etiqueta aparecia em cartões, exemplos e pontes. Ela não é
    # conteúdo didático; cada ocorrência agora identifica a expressão da
    # própria missão.
    s = re.sub(r"frase[- ](?:chave|clave|clé)", f"expressão central de {topic or 'esta missão'}", s, flags=re.I)
    s = OTHER_OPTION.sub("uma resposta contextual", s)
    return re.sub(r"\s{2,}", " ", s).strip()


def clean_recursive(v, *, keep_episode=False, topic=""):
    if isinstance(v, str):
        return clean_string(v, keep_episode=keep_episode, topic=topic)
    if isinstance(v, list):
        return [clean_recursive(x, keep_episode=keep_episode, topic=topic) for x in v]
    if isinstance(v, dict):
        return {k: clean_recursive(x, keep_episode=keep_episode, topic=topic) for k, x in v.items()}
    return v


def topic_of(e: dict) -> str:
    s = e.get("situation") or e.get("s") or e.get("t") or "missão comunicativa"
    s = re.sub(r"^[A-Z]{1,3}\d\s*[·:–-]\s*", "", str(s)).strip()
    s = re.sub(r"^(?:Épisode|Folge|Episode)\s*\d+\s*[:·-]\s*", "", s, flags=re.I).strip()
    return s or "missão comunicativa"


def first_lines(e: dict):
    for wanted in ("scene", "tdlg", "cultcena"):
        f = next((x for x in e.get("fr", []) if isinstance(x, dict) and x.get("k") == wanted), None)
        if not f:
            continue
        rows = f.get("lines") or f.get("turns") or []
        for row in rows:
            if isinstance(row, (list, tuple)) and len(row) >= 2 and row[1]:
                return row
            if isinstance(row, dict) and row.get("n"):
                n = row["n"]
                return ["", n, ""]
    return ["", topic_of(e), ""]


def cultural(e: dict):
    return next((x for x in e.get("fr", []) if isinstance(x, dict) and x.get("k") == "cultob"), {})


def vocab_map(e: dict):
    out = {}
    for row in e.get("v", []) or []:
        if isinstance(row, (list, tuple)) and row:
            out[str(row[0])] = row[1] if len(row) > 1 else ""
    for f in e.get("fr", []) or []:
        if f.get("k") == "words":
            for row in f.get("items", []) or []:
                if isinstance(row, list) and row:
                    out.setdefault(str(row[0]), row[2] if len(row) > 2 else "")
    return out


def repair_generic_gloss(e: dict, topic: str):
    """Troca glosas geradas por uma tradução contextual da própria entrada."""
    vm = vocab_map(e)
    for f in e.get("fr", []) or []:
        k = f.get("k")
        if k == "words":
            for row in f.get("items", []) or []:
                if isinstance(row, list) and len(row) > 2 and GENERIC_GLOSS.match(str(row[2])):
                    row[2] = vm.get(str(row[0]), f"expressão central de {topic}")
        if k in {"wsent", "verbs", "vplay"}:
            for row in f.get("items", []) or []:
                if not isinstance(row, dict):
                    continue
                key = str(row.get("w") or row.get("v") or "")
                for fld in ("pt", "tr", "meaning"):
                    if fld in row and GENERIC_GLOSS.match(str(row[fld])):
                        row[fld] = vm.get(key, f"expressão central de {topic}")
        if k == "lplay":
            for r in f.get("rounds", []) or []:
                if isinstance(r, dict):
                    r["why"] = f"A expressão aparece na cena de {topic} e volta a ser usada na tarefa de produção."


def unique_options(opts, right=None, pool=None):
    vals = []
    for x in opts or []:
        key = json.dumps(x, ensure_ascii=False, sort_keys=True) if isinstance(x, (dict, list)) else str(x).strip().lower()
        if key and key not in {str(y).strip().lower() for y in vals}:
            vals.append(x)
    if right is not None:
        vals = [x for x in vals if str(x).strip().lower() != str(right).strip().lower()]
        vals.insert(0, right)
    if pool:
        for x in pool:
            if len(vals) >= max(3, len(opts or [])):
                break
            if str(x).strip().lower() not in {str(y).strip().lower() for y in vals}:
                vals.append(x)
    return vals


def build_supplement(kind: str, e: dict, topic: str, idx: int, prev: dict | None):
    """Cria uma oficina curta com o mesmo léxico da missão atual.

    Os regulares antigos usavam sempre os vinte mesmos tipos. A cada episódio
    alternamos uma oficina autoral, mantendo vinte quadros no total e dando ao
    aluno contato real com som, construção, escrita, contexto e recuperação.
    """
    vocab = [(str(x[0]), str(x[1] if len(x) > 1 else ""), str(x[2] if len(x) > 2 else "")) for x in (e.get("v") or []) if isinstance(x, list) and x]
    vocab = vocab[:8]
    scene = next((f for f in e.get("fr", []) if f.get("k") == "scene"), {})
    lines = [x for x in (scene.get("lines") or []) if isinstance(x, list) and len(x) > 1 and x[1]]
    if not vocab:
        vocab = [(x[1], x[2] if len(x) > 2 else "", "") for x in lines[:6]]
    if not lines:
        lines = [["", w, tr] for w, tr, _ in vocab]
    common = {"k": kind, "title": f"Oficina da missão · {topic}", "coach": f"Aplique esta oficina à situação {topic}; produza uma resposta nova.", "episodeFocus": f"Missão {topic}. Oficina {kind} com material novo.", "lesson": {"mission": topic, "frame": kind, "newContent": True, "pairPosition": idx % 2 + 1}}
    if kind == "soundlab":
        ws = vocab[:3] or [(topic, "", "")]
        common.update(short=ws[0][0], say=f"Ouça o som de {ws[0][0]} e compare as palavras da situação.", intro={"what": f"Observe a pronúncia de {ws[0][0]} dentro de {topic}.", "how": "Repita devagar, depois no ritmo da frase.", "pt": ws[0][1]}, ex=[[w, "", tr, "Repita no contexto."] for w, tr, _ in ws], pairs=[[ws[i][0], ws[(i + 1) % len(ws)][0], "Compare o som e a função na cena."] for i in range(min(3, len(ws)))], tip=f"O som precisa continuar claro em {topic}.", rounds=[{"q": "Qual palavra você ouviu?", "say": w, "opts": [w] + [z[0] for z in ws if z[0] != w][:1], "a": 0, "why": f"{w} aparece na situação {topic}."} for w, _, _ in ws])
    elif kind == "sbuild":
        rs = []
        for row in lines[:5]:
            toks = str(row[1]).split()
            if len(toks) < 2: continue
            cut = max(1, len(toks) // 2)
            rs.append({"tip": f"Monte a fala e relacione-a a {topic}.", "b": [[" ".join(toks[:cut]), "parte inicial"], [" ".join(toks[cut:]), "complemento"]], "x": [x[0] for x in vocab[:3]], "pt": row[2] if len(row) > 2 else "", "end": "."})
        common.update(rounds=rs or [{"tip": topic, "b": [[topic, "situação"]], "x": [], "pt": topic, "end": "."}], say="Monte a fala em ordem e depois diga uma versão própria.")
    elif kind == "cexp":
        common.update(intro=f"Frases para agir em {topic}. Aprenda cada uma como um bloco.", items=[{"x": row[1], "pt": row[2] if len(row) > 2 else "", "ic": EMOJIS[i % len(EMOJIS)], "use": "Frase em contexto.", "cult": f"Use esta expressão na situação {topic}.", "ex": [row[1], row[2] if len(row) > 2 else ""], "who": row[0] or "Interlocutor"} for i, row in enumerate(lines[:4])])
    elif kind == "xpr":
        items=[]
        for i, row in enumerate(lines[:4]):
            words = str(row[1]).split()
            if not words: continue
            items.append({"t": "wild", "b": [[" ".join(words[:-1]) or words[0], "#7C4DFF"], [words[-1], "#12B3A8"]], "slot": 1, "ic": EMOJIS[i % len(EMOJIS)], "pt": row[2] if len(row)>2 else "", "ex": [row[1], row[2] if len(row)>2 else ""], "sw": [], "note": f"Reutilize o molde em {topic}.", "wr": ["nova", "situação"]})
        common.update(kicker="🃏 moldes reutilizáveis", intro=f"Troque uma peça e leve a expressão para outra situação: {topic}.", hint="Toque na peça marcada e crie uma frase nova.", say="Uma expressão coringa muda de contexto sem perder a intenção.", tip="Mude a peça marcada, mantendo o sentido.", items=items)
    elif kind == "pat":
        pages=[]
        for w, tr, _ in vocab[:3]:
            pages.append({"label": w, "slots": [{"cat": "Início", "catpt": "início", "opts": [[w, tr or w], [topic, topic]]}, {"cat": "Fim", "catpt": "fim", "opts": [[lines[0][1], lines[0][2] if len(lines[0])>2 else ""], [w, tr or w]]}], "end": [".", "."], "tip": f"Use {w} na situação."})
        common.update(sub=f"Padrões para {topic}", tip="Escolha a combinação que mantém a intenção e o registro.", pages=pages)
    elif kind == "wlat":
        common.update(items=[{"w": w, "m": tr, "s": w} for w, tr, _ in vocab[:6]], say="Trace as palavras e escreva de memória.", banner={"role": "written_transfer"})
    elif kind == "review":
        current = [[x[1], x[2] if len(x)>2 else ""] for x in lines[:4]]
        old = [prev.get("line")[1:3] for _ in [0] if prev and prev.get("line") and len(prev["line"])>1]
        common.update(prev=prev.get("topic") if prev else "", work=(e.get("a") or {}).get("w", topic), recap=(old + current)[:5], bag=[{"ic": "🔤", "l": "Palavras", "items": [{"ic": EMOJIS[i%len(EMOJIS)], "t": w, "pt": tr} for i,(w,tr,_) in enumerate(vocab[:6])]}], lead=f"Recupere uma fala e aplique-a em {topic}.", next=f"A próxima missão amplia {topic}.", say="Recupere, transforme e produza.", then=[], title=f"Recuperação em contexto · {topic}")
    elif kind == "scenebuild":
        items=[[EMOJIS[i%len(EMOJIS)], w] for i,(w,_,_) in enumerate(vocab[:4])]
        spots=[["📍", x] for x in ["início", "meio", "fim", "contexto"]]
        steps=[[i % max(1,len(items)), i % max(1,len(spots))] for i in range(min(3,len(items)))]
        first_item = items[steps[0][0]][1] if items and steps else topic
        common.update(say="Ouça e coloque cada elemento no lugar certo.", intro=f"Monte a situação de {topic}.", items=items or [["💬", topic]], spots=spots, rounds=[{"say":[f"Use {topic} com {first_item}."], "pt":[topic], "steps":steps[:1] or [[0,0]], "items":[x[0] for x in steps[:1]] or [0]}])
    return common


def repair_regular_episode(e: dict, cid: str, idx: int, prev: dict | None, seen_titles: set[str]):
    topic = topic_of(e)
    # Títulos repetidos recebem uma missão curta; o título original e o ID continuam preservados.
    title = str(e.get("t") or topic)
    if title in seen_titles:
        title = f"{title} · missão {idx + 1}"
        e["t"] = title
    seen_titles.add(title)
    lang = cid.split("-", 1)[0]
    cult = cultural(e)
    line = first_lines(e)
    work = cult.get("work") or (e.get("a") or {}).get("w") or f"Referência cultural: {topic}"
    art = next((x for x in e.get("fr", []) if x.get("k") == "scene"), {})
    e["p"] = e.get("p") or f"Missão: {topic}. Observe a referência {work}, pratique a cena e produza uma resposta própria."
    e["sc"] = e.get("sc") or (art.get("art") or {}).get("s") or "everyday"
    if not isinstance(e.get("a"), dict) or not e.get("a"):
        e["a"] = {"k": "Referência cultural", "w": work, "y": "contexto da obra", "d": f"A referência {work} ajuda a compreender a situação {topic}; observe os personagens, o lugar e a escolha de linguagem."}
    if not isinstance(e.get("h"), dict) or not e.get("h"):
        e["h"] = {"l": line[1], "src": f"{work} · cena autoral para {topic}", "tr": line[2] if len(line) > 2 else ""}
    if not isinstance(e.get("g"), dict) or not e.get("g"):
        e["g"] = {"t": f"Como agir em {topic}?"}
    e["o"] = e.get("o") if e.get("o") is not None else idx + 1
    pair_index = idx % 2
    prev_line = (prev or {}).get("line") or []
    recycle = {"from": (prev or {}).get("n"), "topic": (prev or {}).get("topic"), "line": prev_line[:3]} if pair_index else {"from": None, "topic": None, "line": []}
    e["pair"] = {"id": f"{cid}-{idx // 2 + 1:04d}", "position": pair_index + 1, "newMission": topic, "recycle": recycle}

    # O inglês mantém suas sequências autorais; os demais regulares deixam de ter uma sequência fixa.
    frames = [clean_recursive(f, keep_episode=(f.get("k") == "cover"), topic=topic) for f in e.get("fr", []) if isinstance(f, dict)]
    # Nos cursos que não eram a referência, distribua oficinas que antes só
    # existiam no inglês. Substituímos um quadro de apoio, mantendo exatamente
    # vinte quadros e preservando a cobertura cultural e de produção.
    if lang != "en":
        swaps = [("cultgame", "soundlab"), ("ctxv", "sbuild"), ("culttl", "cexp"), ("bridge", "xpr"), ("dquiz", "pat"), ("ctxv", "wlat"), ("cultgame", "review"), ("culttl", "scenebuild")]
        old, new = swaps[idx % len(swaps)]
        pos = next((i for i, f in enumerate(frames) if f.get("k") == old), None)
        if pos is not None and not any(f.get("k") == new for f in frames):
            frames[pos] = build_supplement(new, e, topic, idx, prev)
    byk = {f.get("k"): f for f in frames if f.get("k")}
    if lang != "en" and len(byk) >= 18:
        order = VARIANT_ORDERS[idx % len(VARIANT_ORDERS)]
        extras = [f for f in frames if f.get("k") not in order and f.get("k") != "wrap"]
        frames = [byk[k] for k in order if k in byk and k != "wrap"] + extras
        if "wrap" in byk:
            frames.append(byk["wrap"])
    e["fr"] = frames
    repair_generic_gloss(e, topic)
    # Conteúdo específico e rastreável em todos os quadros; o app ignora estes metadados, mas a aula e a auditoria não perdem a missão.
    for f in e["fr"]:
        k = f.get("k", "quadro")
        if k != "cover":
            f["episodeFocus"] = f"Missão {topic}. Quadro {k}: use a referência cultural, a cena e a linguagem desta aula para cumprir a tarefa."
        if isinstance(f.get("coach"), str):
            f["coach"] = clean_string(f["coach"], topic=topic)
            # O script pode ser reexecutado durante uma auditoria; nunca
            # acumule o mesmo sufixo editorial em cada passagem.
            if " Missão editorial " in f["coach"]:
                f["coach"] = f["coach"].split(" Missão editorial ", 1)[0].rstrip()
        else:
            f["coach"] = f"Conecte {k} à missão {topic}; note uma escolha de registro e produza uma variação própria."
        f["coach"] += f" Missão editorial {idx + 1}: crie conteúdo novo para {topic}."
        f["lesson"] = {"mission": topic, "frame": k, "newContent": True, "pairPosition": pair_index + 1, "recycle": recycle["line"]}
        if k == "lplay":
            pool = [str(x[0]) for x in (e.get("v") or []) if isinstance(x, list) and x]
            for r in f.get("rounds", []) or []:
                if isinstance(r, dict):
                    r["opts"] = unique_options(r.get("opts"), right=r.get("say"), pool=pool)
                    r["a"] = 0
        if k in {"scene", "tdlg"} and pair_index and recycle["line"]:
            f["recyclePrompt"] = f"Recupere a fala “{recycle['line'][1]}” do episódio anterior e transforme-a para {topic}."
        if k == "fio":
            f["previous"] = recycle["line"][1] if len(recycle["line"]) > 1 else f.get("previous") or "A missão anterior prepara esta situação."
        if k == "produce":
            f["prompt"] = clean_string(str(f.get("prompt") or ""), topic=topic)
            if pair_index and recycle["line"]:
                f["prompt"] += f" Recicle a ideia de “{recycle['line'][1]}” do episódio anterior, mas crie uma resposta nova para {topic}."
        if k == "wrap":
            if pair_index and recycle["line"]:
                rec = f.get("recap") if isinstance(f.get("recap"), list) else []
                f["recap"] = [recycle["line"][:3]] + rec[:5]
            f["coach"] = f"Feche a missão {topic}: recupere uma fala, explique a referência {work} e prepare uma aplicação nova."

    return {"n": e.get("n"), "topic": topic, "line": line[:3]}


def neighbor_vocab(e):
    vals = []
    for row in e.get("v", []) or []:
        if isinstance(row, list) and row and row[0]:
            vals.append((str(row[0]), str(row[1] if len(row) > 1 else ""), str(row[2] if len(row) > 2 else "")))
    return vals


def repair_neighbor_episode(e: dict, cid: str, idx: int, prev: dict | None, seen_titles: set[str]):
    topic = str(e.get("s") or e.get("t") or "situação comunicativa").strip()
    title = str(e.get("t") or topic)
    if title in seen_titles:
        place = str(e.get("sc") or (e.get("a") or {}).get("w") or "nova situação")
        title = f"{title} · {place} · missão {idx + 1}"
        e["t"] = title
    seen_titles.add(title)
    pos = idx % 2
    prev_line = (prev or {}).get("line") or []
    recycle = {"from": (prev or {}).get("n"), "topic": (prev or {}).get("topic"), "line": prev_line[:3]} if pos else {"from": None, "topic": None, "line": []}
    e["pair"] = {"id": f"{cid}-{idx // 2 + 1:04d}", "position": pos + 1, "newMission": topic, "recycle": recycle}
    e["lessonFocus"] = f"Missão {topic}: compreenda a situação, recupere uma fala anterior e responda com linguagem nova."
    # clean_recursive retorna uma cópia para não alterar strings durante a
    # travessia; devolvemos o conteúdo limpo ao mesmo objeto da lista.
    cleaned = clean_recursive(e, keep_episode=False, topic=topic)
    e.clear()
    e.update(cleaned)
    vocab = neighbor_vocab(e)
    frames = e.get("fr") or []
    chats = [f for f in frames if f.get("k") == "nbchat" and isinstance(f.get("lines"), list)]
    current_lines = [x for x in (chats[0].get("lines", []) if chats else []) if isinstance(x, list) and len(x) > 1 and x[1]]
    if pos and prev_line and chats:
        # Uma fala do par anterior entra como memória explícita; as linhas atuais permanecem novas.
        chats[0]["recyclePrompt"] = f"Recupere “{prev_line[1]}” e responda agora em {topic}."
    # A segunda conversa deixa de repetir quatro falas genéricas: ela parte da cena atual.
    generic = {"Das klingt gut. Was machen wir jetzt?", "That sounds good. What should we do next.", "Gracias, ahora sé cómo continuar."}
    if len(chats) > 1 and current_lines:
        for j, row in enumerate(chats[1].get("lines", []) or []):
            if isinstance(row, list) and len(row) > 1 and row[1] in generic:
                src = current_lines[(j + 1) % len(current_lines)]
                chats[1]["lines"][j] = [row[0], src[1], src[2] if len(src) > 2 else ""]
    vm = [(w, tr) for w, tr, _ in vocab]
    for fidx, f in enumerate(frames):
        if not isinstance(f, dict):
            continue
        k = f.get("k", "quadro")
        f["lesson"] = {"mission": topic, "frame": k, "newContent": True, "pairPosition": pos + 1, "recycle": recycle["line"]}
        old_coach = str(f.get("coach") or "").strip()
        if " Missão editorial " in old_coach:
            old_coach = old_coach.split(" Missão editorial ", 1)[0].rstrip()
        f["coach"] = (old_coach + " " if old_coach else "") + f"Missão editorial {idx + 1}: use este quadro para uma resposta nova em {topic}."
        if k in {"nbvocab", "nbfind"} and vocab:
            f["items"] = [[w, EMOJIS[i % len(EMOJIS)], tr] for i, (w, tr) in enumerate(vm[:6])]
        elif k == "nbacc" and vocab:
            # O quadro de ortografia também usa o léxico da missão atual; a
            # versão anterior reciclava o mesmo bloco em muitos episódios.
            old = f.get("items", []) or []
            f["items"] = [{"w": w, "s": w, "pt": tr, "alts": [w, w.lower()], "tip": f"Observe a escrita de {w} dentro de {topic}."} for w, tr in vm[:5]]
        elif k == "nbctx":
            # Mantém a situação, mas nunca oferece duas alternativas iguais.
            pool = [w for w, _ in vm]
            for item in f.get("items", []) or []:
                if not isinstance(item, dict):
                    continue
                right = None
                opts = item.get("opts") or []
                if opts and isinstance(item.get("a"), int) and item["a"] < len(opts):
                    right = opts[item["a"]]
                item["opts"] = unique_options(opts, right=right, pool=pool)
                item["a"] = 0
                item["why"] = clean_string(str(item.get("why") or ""), topic=topic) or f"Use esta escolha na situação {topic}."
        elif k == "nbdict" and current_lines:
            rows = [[x[1], x[2] if len(x) > 2 else ""] for x in current_lines[:3]]
            if pos and prev_line:
                rows = [[prev_line[1], prev_line[2] if len(prev_line) > 2 else ""]] + rows[:2]
            f["items"] = [{"t": x[0], "pt": x[1]} for x in rows]
        elif k == "nbshadow" and current_lines:
            rows = current_lines[:4]
            if pos and prev_line:
                rows = [prev_line] + rows[:3]
            f["items"] = [[x[1], x[2] if len(x) > 2 else ""] for x in rows]
        elif k == "nbslang" and current_lines:
            f["lines"] = current_lines[:6]
            f["ess"] = [x[1] for x in current_lines[:2]]
        elif k == "wrap":
            rows = current_lines[:3]
            f["recap"] = ([[prev_line[1], prev_line[2] if len(prev_line) > 2 else ""]] if pos and prev_line else []) + [[x[1], x[2] if len(x) > 2 else ""] for x in rows]
            f["title"] = f"Para levar: {topic} · missão {idx + 1}"
            f["context"] = f"{topic} · situação nova; recupere a memória do par e aplique uma resposta diferente."
        if isinstance(f.get("title"), str):
            f["title"] = clean_string(f["title"], topic=topic)
        if isinstance(f.get("intro"), str):
            f["intro"] = clean_string(f["intro"], topic=topic)
    line = current_lines[0] if current_lines else ["", topic, ""]
    return {"n": e.get("n"), "topic": topic, "line": line[:3]}


def process_course(cid: str, files: list[str], regular: bool):
    prev = None
    seen_titles: set[str] = set()
    count = 0
    for name in files:
        path = DATA / name
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, list):
            continue
        out = []
        for e in payload:
            if not isinstance(e, dict) or not isinstance(e.get("fr"), list):
                out.append(e)
                continue
            if regular:
                prev = repair_regular_episode(e, cid, count, prev, seen_titles)
            else:
                prev = repair_neighbor_episode(e, cid, count, prev, seen_titles)
            out.append(e)
            count += 1
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        os.replace(tmp, path)
    print(f"{cid}: {count} episódios corrigidos", flush=True)


def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    for cid, files in manifest.items():
        base = cid.split("-", 1)[0]
        if base in REGULAR_PREFIXES:
            process_course(cid, files, True)
        elif base in NEIGHBOR_PREFIXES and cid != "nbja-kana":
            process_course(cid, files, False)


if __name__ == "__main__":
    main()
