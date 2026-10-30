#!/usr/bin/env python3
"""Build the authored reading and guided-dialogue frames for regular English B1-C2.

The player contract is deliberately small and testable: seven reading lines (about
90 English words) and six dialogue turns, each with three answer variations.  The
source episode remains authoritative for its cultural work, focus, vocabulary,
cast, banner and progression metadata; this script only replaces/inserts the two
frames so old skeletons cannot leak into the player.
"""
from __future__ import annotations

import copy
import glob
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
LEVELS = {"b1": "B1", "b2": "B2", "c1": "C1", "c2": "C2"}
WORD_RE = re.compile(r"[A-Za-z]+(?:['’-][A-Za-z]+)?")

READ_TEMPLATES = [
    "In {work}, {focus} becomes a practical question about what matters next.",
    "A detail from the work gives {focus} a human scale and invites careful attention.",
    "The episode follows that detail through a conversation shaped by timing and choice.",
    "Notice how {v0} and {v1} frame the scene while {v2} shifts perspective.",
    "The reference offers context, so the learner listens, infers, and responds with purpose.",
    "Then {v3}, {v4}, and {v5} help the speaker make a precise contribution.",
    "By the end, the idea is explained with nuance, evidence, and respectful intent.",
]

QUESTION_TEMPLATES = [
    "What does {v} reveal about the situation?",
    "How would you connect {v} to the work?",
    "Which response uses {v} most naturally here?",
    "What can the speaker clarify with {v}?",
    "Why is {v} the careful choice in this context?",
    "How would you close the exchange after using {v}?",
]

ANSWER_TEMPLATES = [
    ("It keeps the idea precise while respecting the context.", "Isso mantém a ideia precisa e respeita o contexto."),
    ("It connects the detail to the speaker's real intention.", "Isso conecta o detalhe à intenção real de quem fala."),
    ("It makes the meaning clear without sounding abrupt.", "Isso deixa o sentido claro sem soar brusco."),
    ("It gives enough evidence for the listener to follow.", "Isso oferece evidência suficiente para o ouvinte acompanhar."),
    ("It acknowledges the other person's point before adding a view.", "Isso reconhece o ponto da outra pessoa antes de acrescentar uma opinião."),
    ("It leaves the conversation open for a useful next step.", "Isso deixa a conversa aberta para um próximo passo útil."),
]

WRONG_TEMPLATES = [
    ("It ignores the detail and changes the subject immediately.", "Isso ignora o detalhe e muda de assunto imediatamente."),
    ("It sounds certain even though the evidence is missing.", "Isso soa certo embora falte evidência."),
    ("It repeats the word without explaining its role.", "Isso repete a palavra sem explicar sua função."),
    ("It would fit a different scene, not this one.", "Isso serviria para outra cena, não para esta."),
    ("It closes the exchange before the other speaker can answer.", "Isso encerra a conversa antes que a outra pessoa responda."),
    ("It turns a careful observation into an unsupported claim.", "Isso transforma uma observação cuidadosa em uma afirmação sem apoio."),
]

def digest(e):
    return int(hashlib.sha256(str(e.get("n", "")).encode()).hexdigest()[:8], 16)

def clean(text):
    text = str(text or "").strip()
    text = re.sub(r"\s+", " ", text)
    return text

def words(e):
    out = []
    for row in e.get("v", []):
        if isinstance(row, list) and row:
            x = clean(row[0])
            if x and x.lower() not in {z.lower() for z in out}:
                out.append(x)
    # Fall back to language-bearing words found in the authored scene.
    for f in e.get("fr", []):
        if f.get("k") in {"scene", "pgscene", "convo", "tdlg"}:
            for line in f.get("lines", []):
                if isinstance(line, list) and len(line) > 1:
                    for x in WORD_RE.findall(line[1]):
                        if len(x) > 3 and x.lower() not in {z.lower() for z in out}:
                            out.append(x)
    while len(out) < 6:
        out.append(["context", "evidence", "perspective", "nuance", "choice", "exchange"][len(out)])
    return out[:6]

def work_info(e):
    a = e.get("a") or {}
    work = clean(a.get("w") or e.get("t") or "the cultural work")
    focus = clean(e.get("s") or e.get("episodeFocus") or e.get("t") or "the episode mission")
    desc = clean(a.get("d") or "")
    return work, focus, desc

def compact_label(text, limit):
    """Keep long legacy focus strings from swamping the reading contract."""
    text = re.split(r"[.!?]", clean(text))[0]
    toks = text.split()
    return " ".join(toks[:limit]).rstrip(" ,;:") or "the lesson"

def banner_for(e):
    for f in e.get("fr", []):
        if isinstance(f.get("banner"), dict):
            return copy.deepcopy(f["banner"])
    # Keep the same shape consumed by fxKindBar when a legacy episode has no banner.
    colors = [["#2b1d3a", "#5b3b91", "#f0b35a", "#f7e5bf"], ["#123b4a", "#1f6f78", "#ef8354", "#f8f1e5"]][digest(e) % 2]
    return {"pa": {"t": "cultural-scene", "p": colors, "e": ["📖", "💬", "🎧"], "v": 0}, "role": "cultural-dialogue"}

def cast_for(e):
    for f in e.get("fr", []):
        c = f.get("cast")
        if isinstance(c, dict) and c.get("npc") and c.get("you"):
            return copy.deepcopy(c)
    # Scene cast is a map of name -> [emoji, colour].
    for f in e.get("fr", []):
        c = f.get("cast")
        if isinstance(c, dict) and c:
            names = list(c)
            if len(names) >= 2:
                def arr(name):
                    val = c[name] if isinstance(c[name], list) else ["🧑", "#2b6cb0"]
                    return [val[0], val[1], name]
                return {"npc": arr(names[0]), "you": arr(names[1])}
    return {"npc": ["🧑‍🏫", "#0c7a78", "Guide"], "you": ["🧑", "#e85d75", "Learner"]}

def reading(e):
    work, focus, desc = work_info(e)
    work_label = compact_label(work, 4)
    focus_label = compact_label(focus, 4)
    v = words(e)
    h = digest(e)
    lines = []
    for i, template in enumerate(READ_TEMPLATES):
        text = template.format(work=work_label, focus=focus_label, v0=v[0], v1=v[1], v2=v[2], v3=v[3], v4=v[4], v5=v[5])
        pt = [
            f"Em {work}, {focus.lower()} se torna uma questão prática quando as pessoas precisam decidir o próximo passo.",
            "Um detalhe da obra dá uma escala humana ao foco e convida a uma atenção cuidadosa à língua.",
            "O episódio acompanha esse detalhe numa conversa em que o sentido depende do momento e da escolha.",
            f"Observe como {v[0]} e {v[1]} enquadram a cena, enquanto {v[2]} muda a perspectiva de quem fala.",
            "A referência cultural oferece contexto sem substituir a tarefa: ouvir, inferir e responder.",
            f"À medida que a situação avança, {v[3]}, {v[4]} e {v[5]} ajudam o estudante a contribuir com precisão.",
            "No fim, a mesma ideia pode ser explicada com mais nuance, evidência e intenção respeitosa.",
        ][i]
        lines.append([text, pt])
    # Guard the contract against accidental future template edits.
    count = sum(len(WORD_RE.findall(x[0])) for x in lines)
    if count < 80:
        lines[-1][0] = lines[-1][0][:-1] + " with a clear reason and a constructive next step."
    elif count > 100:
        # Keep the seven-line contract while shortening the final two lines.
        lines[0][0] = f"In {work_label}, the focus becomes a practical question."
        lines[1][0] = "A detail from it invites careful attention."
        lines[-2][0] = f"Then {v[3]}, {v[4]}, and {v[5]} guide a precise response."
        lines[-1][0] = "The idea ends with nuance and respect."
    # Recount after any shortening and pad only with authored, useful context.
    count = sum(len(WORD_RE.findall(x[0])) for x in lines)
    if count < 80:
        lines[-1][0] = "The idea ends with nuance, evidence, and respect for the listener's next question."
    return {
        "k": "read", "title": f"Leitura cultural · {work}",
        "say": "Leia, ouça cada linha e conecte a referência cultural à missão da aula.",
        "s": lines, "banner": banner_for(e), "episodeId": str(e.get("n")),
        "episodeFocus": focus, "lessonRole": "cultural_reading", "pairId": e.get("pairId"),
        "missionType": e.get("missionType") or "cultural-bridge", "lesson": e.get("lesson") or e.get("t"),
    }

def dialogue(e):
    work, focus, _ = work_info(e)
    v = words(e)
    h = digest(e)
    turns = []
    for i in range(6):
        term = v[(i + h) % len(v)]
        q = QUESTION_TEMPLATES[i].format(v=term)
        q += f" In the context of {work}, what would you say next?"
        qpt = [
            f"O que {term} revela sobre a situação? No contexto de {work}, o que você diria em seguida?",
            f"Como você ligaria {term} à obra {work}?",
            f"Qual resposta usa {term} com naturalidade nesta situação?",
            f"O que o falante pode esclarecer com {term} enquanto trata de {focus.lower()}?",
            f"Por que {term} é uma escolha cuidadosa neste contexto de {work}?",
            f"Como você encerraria a troca depois de usar {term}?",
        ][i]
        good = ANSWER_TEMPLATES[(i + h) % len(ANSWER_TEMPLATES)]
        wrong1 = WRONG_TEMPLATES[(i + h + 1) % len(WRONG_TEMPLATES)]
        wrong2 = WRONG_TEMPLATES[(i + h + 3) % len(WRONG_TEMPLATES)]
        turns.append({
            "n": [q, qpt],
            "o": [[good[0] + f" I can mention {term} and keep the purpose clear.", good[1] + f" Posso mencionar {term} e manter o objetivo claro."], [wrong1[0], wrong1[1]], [wrong2[0], wrong2[1]]],
            "a": 0,
            "hint": f"Use **{term}** para ligar a resposta ao contexto.",
            "q": f"Responda usando {term} e mantenha a intenção da missão.",
        })
    return {
        "k": "tdlg", "title": f"Conversa guiada · {work}",
        "intro": "Ouça cada fala, escolha uma resposta e compare as três possibilidades. Toque no 🔊 quantas vezes quiser!",
        "cast": cast_for(e), "turns": turns,
        "coach": f"Use o vocabulário e as expressões de {focus} para conversar sobre {work} com precisão.",
        "episodeId": str(e.get("n")), "episodeFocus": focus, "levelProgression": e.get("levelProgression") or e.get("lesson"),
        "lessonRole": "communicative_transfer", "pairId": e.get("pairId"),
        "missionType": e.get("missionType") or "cultural-bridge", "banner": banner_for(e), "lesson": e.get("lesson") or e.get("t"),
    }

def replace_frame(fr, kind, frame):
    for i, old in enumerate(fr):
        if old.get("k") == kind:
            fr[i] = frame
            return
    # Read is placed before the first practice/review block; dialogue follows it.
    anchor = next((i for i, x in enumerate(fr) if x.get("k") in {"scene", "pgscene", "produce", "fio", "wrap"}), len(fr))
    fr.insert(anchor, frame)

def normalize_frame_count(fr):
    """Keep the regular-player contract at twenty visible stages.

    Some legacy episodes already contain a conversational/review placeholder;
    once `read` and `tdlg` are authored those placeholders are redundant.  In
    richer sequences we drop only optional enrichment stages, never the cover,
    cultural bridge, scene, production, story thread or the new frames.
    """
    removable = [
        "convo", "review", "pgdialogue", "pgreading", "mystery", "paraphrase",
        "chain", "voices", "scenebuild", "wlat", "ctxv", "lplay", "dquiz",
    ]
    while len(fr) > 20:
        removed = False
        for kind in removable:
            idx = next((i for i, f in enumerate(fr) if f.get("k") == kind), None)
            if idx is not None:
                fr.pop(idx); removed = True; break
        if not removed:
            # Deterministic last resort: remove the stage immediately before the
            # narrative close, retaining fio/wrap and every required frame.
            idx = next((i for i, f in enumerate(fr) if f.get("k") in {"fio", "wrap"}), len(fr)) - 1
            if fr[idx].get("k") in {"read", "tdlg", "cover", "scene"}:
                idx = max(0, idx - 1)
            fr.pop(idx)

def process(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    changed = 0
    for e in data:
        fr = e.get("fr")
        if not isinstance(fr, list):
            continue
        replace_frame(fr, "read", reading(e))
        replace_frame(fr, "tdlg", dialogue(e))
        normalize_frame_count(fr)
        e["advancedReadingDialogue"] = "v1"
        changed += 1
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return changed

def main():
    total = 0
    for prefix in LEVELS:
        for path in sorted(DATA.glob(f"en-{prefix}_*.json")):
            total += process(path)
    print(f"updated {total} episodes")

if __name__ == "__main__":
    main()
