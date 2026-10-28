#!/usr/bin/env python3
"""Gera o léxico editorial dos episódios C1.

O gerador trabalha a partir do foco, da obra e das cenas já escritas. Ele não
usa o conjunto genérico ``explain/notice/connect/rephrase`` e nunca trata uma
frase completa como expressão: expressões são blocos lexicais de 2--6 tokens,
sem sujeito, pontuação final ou oração independente.

Por padrão roda em modo de auditoria (não grava). Use ``--write`` somente após
revisar o relatório. A mesma rotina serve para C2 com ``--course en-c2``.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GENERIC = {"explain", "notice", "connect", "rephrase"}
STOP = {
    "the", "and", "with", "from", "that", "this", "into", "when", "what",
    "which", "your", "have", "has", "been", "were", "will", "would", "could",
    "should", "about", "there", "their", "they", "them", "then", "than", "just",
    "only", "more", "most", "some", "very", "here", "does", "did", "not", "for",
    "are", "was", "you", "she", "her", "his", "our", "its", "can", "how", "why",
    "who", "all", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "scene", "focus", "work", "lesson", "episode", "today",
}
ICONS = ["🧩", "🎚️", "💡", "🧭"]

# Each family maps to a teachable discourse purpose. The object is selected
# from the episode's focus/scene, so the resulting item belongs to that lesson.
FAMILIES = {
    "argument": {
        "keys": ("argument", "claim", "evidence", "debate", "reason", "position", "counter", "thesis"),
        "verbs": [("qualify", "qualificar"), ("substantiate", "fundamentar"), ("concede", "conceder"), ("counter", "contrapor"), ("frame", "enquadrar"), ("weigh", "ponderar"), ("interrogate", "questionar criticamente"), ("rebut", "refutar"), ("defend", "defender"), ("challenge", "desafiar"), ("corroborate", "corroborar"), ("refute", "refutar"), ("foreground", "trazer para o primeiro plano"), ("contextualize", "contextualizar"), ("differentiate", "diferenciar"), ("reframe", "reenquadrar"), ("synthesize", "sintetizar"), ("scrutinize", "examinar"), ("weigh", "ponderar"), ("position", "posicionar")],
        "expr": [("qualify", "a {obj}"), ("substantiate", "the {obj}"), ("concede", "a point"), ("counter", "the objection"), ("frame", "the {obj}"), ("weigh", "the evidence"), ("rebut", "the charge"), ("defend", "a position"), ("challenge", "the premise"), ("corroborate", "the account"), ("refute", "the claim"), ("contextualize", "the evidence"), ("differentiate", "the readings"), ("reframe", "the question"), ("synthesize", "the findings"), ("scrutinize", "the wording"), ("position", "the argument"), ("interrogate", "the assumption"), ("foreground", "a tension"), ("reconcile", "the strands")],
    },
    "narrative": {
        "keys": ("story", "narrative", "character", "plot", "voice", "style", "fiction", "film", "novel"),
        "verbs": [("portray", "retratar"), ("underscore", "ressaltar"), ("foreground", "trazer para o primeiro plano"), ("reframe", "reenquadrar"), ("trace", "rastrear"), ("evoke", "evocar"), ("dramatize", "dramatizar"), ("depict", "representar"), ("foreshadow", "antecipar"), ("narrate", "narrar"), ("allude", "aludir"), ("juxtapose", "justapor"), ("animate", "dar vida a"), ("inhabit", "habitar"), ("render", "representar"), ("disclose", "revelar"), ("stage", "encenar"), ("recast", "reformular"), ("echo", "ecoar"), ("frame", "enquadrar")],
        "expr": [("portray", "a {obj}"), ("underscore", "the {obj}"), ("foreground", "a tension"), ("reframe", "the {obj}"), ("trace", "a motive"), ("evoke", "a memory"), ("dramatize", "the conflict"), ("depict", "the setting"), ("foreshadow", "the turn"), ("narrate", "the episode"), ("allude", "to a memory"), ("juxtapose", "two images"), ("animate", "the silence"), ("inhabit", "a perspective"), ("render", "the atmosphere"), ("disclose", "the motive"), ("stage", "a confrontation"), ("recast", "the encounter"), ("echo", "the refrain"), ("frame", "the scene")],
    },
    "register": {
        "keys": ("register", "tone", "formal", "polite", "hedge", "stance", "modality", "certainty", "subjunctive"),
        "verbs": [("hedge", "atenuar"), ("signal", "sinalizar"), ("modulate", "modular"), ("soften", "suavizar"), ("imply", "sugerir"), ("qualify", "qualificar"), ("calibrate", "calibrar"), ("temper", "moderar"), ("reserve", "reservar"), ("formulate", "formular"), ("phrase", "formular"), ("attenuate", "atenuar"), ("distinguish", "distinguir"), ("voice", "expressar"), ("index", "indicar"), ("frame", "enquadrar"), ("nuance", "nuançar"), ("position", "posicionar"), ("concede", "conceder"), ("disclaim", "ressalvar")],
        "expr": [("hedge", "a claim"), ("signal", "a stance"), ("modulate", "the tone"), ("soften", "the request"), ("imply", "a reservation"), ("qualify", "the answer"), ("calibrate", "the register"), ("temper", "the criticism"), ("reserve", "a judgment"), ("formulate", "a reply"), ("attenuate", "the force"), ("distinguish", "the nuance"), ("voice", "a concern"), ("index", "a stance"), ("frame", "the courtesy"), ("nuance", "the refusal"), ("position", "the speaker"), ("concede", "a limitation"), ("disclaim", "an assumption"), ("signal", "the distance")],
    },
    "change": {
        "keys": ("change", "reform", "policy", "society", "global", "economy", "history", "future", "technology"),
        "verbs": [("reshape", "remodelar"), ("trigger", "desencadear"), ("mitigate", "atenuar"), ("exacerbate", "agravar"), ("anticipate", "antecipar"), ("sustain", "sustentar"), ("transform", "transformar"), ("entrench", "consolidar"), ("disrupt", "desestabilizar"), ("recalibrate", "recalibrar"), ("redirect", "redirecionar"), ("accelerate", "acelerar"), ("constrain", "restringir"), ("offset", "compensar"), ("catalyze", "catalisar"), ("consolidate", "consolidar"), ("reallocate", "realocar"), ("reconfigure", "reconfigurar"), ("decarbonize", "descarbonizar"), ("institutionalize", "institucionalizar")],
        "expr": [("reshape", "the {obj}"), ("trigger", "a shift"), ("mitigate", "the impact"), ("exacerbate", "the divide"), ("anticipate", "a shift"), ("sustain", "the momentum"), ("transform", "the system"), ("entrench", "the pattern"), ("disrupt", "the cycle"), ("recalibrate", "the policy"), ("redirect", "the resources"), ("accelerate", "the transition"), ("constrain", "the growth"), ("offset", "the cost"), ("catalyze", "the reform"), ("consolidate", "the gains"), ("reallocate", "the burden"), ("reconfigure", "the network"), ("decarbonize", "the economy"), ("institutionalize", "the change")],
    },
    "perception": {
        "keys": ("perception", "attention", "memory", "identity", "meaning", "interpret", "mind", "choice"),
        "verbs": [("infer", "inferir"), ("discern", "discernir"), ("reconcile", "conciliar"), ("distil", "destilar"), ("interrogate", "questionar criticamente"), ("recast", "reformular"), ("detect", "detectar"), ("apprehend", "apreender"), ("intuit", "intuir"), ("decode", "decodificar"), ("construe", "interpretar"), ("recognize", "reconhecer"), ("register", "registrar"), ("parse", "analisar"), ("map", "mapear"), ("decode", "decodificar"), ("uncover", "descobrir"), ("locate", "localizar"), ("differentiate", "diferenciar"), ("synthesize", "sintetizar")],
        "expr": [("infer", "a motive"), ("discern", "the {obj}"), ("reconcile", "two readings"), ("distil", "the {obj}"), ("interrogate", "the assumption"), ("recast", "the question"), ("detect", "a pattern"), ("apprehend", "the nuance"), ("intuit", "the motive"), ("decode", "the signal"), ("construe", "the gesture"), ("recognize", "the shift"), ("register", "the detail"), ("parse", "the wording"), ("map", "the relation"), ("uncover", "the premise"), ("locate", "the clue"), ("differentiate", "the readings"), ("synthesize", "the evidence"), ("trace", "the inference")],
    },
}
ALL_VERBS = list(dict.fromkeys((v, pt) for fam in FAMILIES.values() for v, pt in fam["verbs"]))


def fold(text: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", " ", (text or "").lower()).strip()


def episode_text(e: dict) -> str:
    bits = [e.get("t", ""), e.get("s", ""), e.get("gs", ""), (e.get("a") or {}).get("w", ""), (e.get("a") or {}).get("d", "")]
    for q in e.get("fr", []):
        if q.get("k") == "pgscene":
            bits.extend(str(line[1]) for line in q.get("lines", []) if isinstance(line, list) and len(line) > 1)
    return " ".join(bits)


def terms(e: dict) -> list[str]:
    # Prefer the authored English vocabulary and scene lines.  The focus and
    # description are Portuguese-facing metadata and must not leak words such
    # as ``sutis`` or ``avan`` into English lexical chunks.
    source = []
    for item in e.get("v") or []:
        if isinstance(item, list) and item:
            source.append(str(item[0]))
    for q in e.get("fr", []):
        if q.get("k") == "pgscene":
            source.extend(str(line[1]) for line in q.get("lines", []) if isinstance(line, list) and len(line) > 1)
    source.extend([(e.get("a") or {}).get("w", ""), e.get("t", "")])
    words = [w for w in re.findall(r"[A-Za-z][A-Za-z'-]{3,}", " ".join(source)) if w.lower() not in STOP]
    seen = []
    for word in words:
        key = word.lower()
        if key not in {x.lower() for x in seen}:
            seen.append(word)
    return seen[:12] or ["the focus"]


def family(e: dict) -> str:
    text = fold(episode_text(e))
    scores = {name: sum(1 for key in data["keys"] if key in text) for name, data in FAMILIES.items()}
    return max(scores, key=scores.get)


def present(verb: str, subject: str) -> str:
    if subject == "I":
        return verb
    if verb.endswith("y") and verb[-2:] not in ("ay", "ey", "iy", "oy", "uy"):
        return verb[:-1] + "ies"
    if verb.endswith(("s", "x", "z", "ch", "sh")):
        return verb + "es"
    return verb + "s"


def build_lexicon(e: dict, ordinal: int, used: set[str] | None = None, used_verbs: set[tuple[str, ...]] | None = None) -> tuple[list[dict], list[dict]]:
    fam = FAMILIES[family(e)]
    ts = terms(e)
    # The offset makes adjacent episodes use different lexical sets while the
    # object slot ties each expression to the current focus/scene.
    vo = ordinal % len(fam["verbs"])
    eo = (ordinal * 2) % len(fam["expr"])
    used_verbs = used_verbs if used_verbs is not None else set()
    verb_pool = list(dict.fromkeys(fam["verbs"]))
    chosen_v = None
    for step in range(1, len(verb_pool)):
        for shift in range(len(verb_pool)):
            candidate = [verb_pool[(vo + shift + i * step) % len(verb_pool)] for i in range(4)]
            key = tuple(sorted(x[0] for x in candidate))
            if len(set(key)) == 4 and key not in used_verbs:
                chosen_v = candidate; used_verbs.add(key); break
        if chosen_v is not None: break
    if chosen_v is None:
        for step in range(1, len(ALL_VERBS)):
            for shift in range(len(ALL_VERBS)):
                candidate=[ALL_VERBS[(vo+shift+i*step)%len(ALL_VERBS)] for i in range(4)]
                key=tuple(sorted(x[0] for x in candidate))
                if len(set(candidate))==4 and key not in used_verbs:
                    chosen_v=candidate; used_verbs.add(key); break
            if chosen_v is not None: break
    chosen_v = chosen_v or [verb_pool[(vo + i) % len(verb_pool)] for i in range(4)]
    chosen_x = [fam["expr"][(eo + i) % len(fam["expr"])] for i in range(4)]
    verbs = []
    for i, (v, pt) in enumerate(chosen_v):
        line = ts[i % len(ts)]
        verbs.append({
            "v": v, "ic": ICONS[i], "pt": pt,
            "f": [["I", f"I {v} the {line}."], ["she", f"She {present(v, 'she')} the {line}."]],
            "ex": [f"The scene lets us {v} the {line}.", f"A cena nos ajuda a {pt} {line}."],
            "note": f"**{v}** = {pt}; use-o para falar de {line}.",
        })
    expressions = []
    used = used if used is not None else set()
    for i, (verb, tail) in enumerate(chosen_x):
        obj = ts[(i + ordinal) % len(ts)]
        template = tail.format(obj=obj)
        # Every block must be tied to this episode.  Generic templates such as
        # ``evoke a memory`` receive a compact lexical complement rather than a
        # sentence-sized explanation.
        if "{obj}" not in tail:
            prep = "of" if verb in {"evoke", "trace", "portray"} else "about"
            template = f"{template} {prep} {obj}"
        phrase = f"{verb} {template}"
        # Avoid collisions across episodes while keeping each item a short
        # reusable chunk.  A second topic word is enough to disambiguate a
        # repeated base template without resorting to punctuation fillers.
        base_phrase = phrase
        accepted = False
        for j in range(len(ts) * 3):
            extra = ts[(i + ordinal + j + 1) % len(ts)]
            prep = ("in", "on", "through")[j % 3]
            candidate = base_phrase if j == 0 else f"{verb} {tail.format(obj=obj)} {prep} {extra}"
            key = fold(candidate)
            if key not in used and 2 <= len(key.split()) <= 6:
                phrase = candidate; used.add(key); accepted = True; break
        if not accepted:
            # The topic words themselves are unique enough to keep the block
            # lexical when a profile has exhausted its first choices.
            phrase = f"{verb} {obj}"
            used.add(fold(phrase))
        expressions.append({
            "x": phrase, "en": phrase, "pt": f"{verb}: {tail.format(obj=obj)}", "ic": ICONS[i],
            "use": f"Bloco lexical para discutir {obj}.",
            "ex": [f"We can {phrase}.", f"Podemos {verb} {tail.format(obj=obj)}."],
        })
    return verbs, expressions


def validate(verbs: list[dict], expressions: list[dict]) -> list[str]:
    errors = []
    vv = [fold(x.get("v")) for x in verbs]
    if len(verbs) != 4 or len(set(vv)) != 4: errors.append("four distinct verbs required")
    if set(vv) & GENERIC: errors.append("generic verb present")
    xx = [str(x.get("en") or x.get("x") or "").strip() for x in expressions]
    if len(expressions) != 4 or len(set(fold(x) for x in xx)) != 4: errors.append("four distinct expressions required")
    for x in xx:
        tok = x.split()
        if not 2 <= len(tok) <= 6 or re.search(r"[.!?;:]$", x): errors.append(f"not a lexical block: {x}")
    return errors


def load(course: str):
    for path in sorted(glob.glob(str(ROOT / "data" / f"{course}_*.json"))):
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        yield Path(path), data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", default="en-c1", choices=("en-c1", "en-c2"))
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    ordinal = 0; bad = 0; total = 0; used_expr: set[str] = set(); used_verbs: set[tuple[str, ...]] = set()
    for path, data in load(args.course):
        changed = False
        for e in data:
            ordinal += 1; total += 1
            verbs, expressions = build_lexicon(e, ordinal, used_expr, used_verbs)
            errors = validate(verbs, expressions)
            if errors: bad += 1; print(e.get("n"), errors)
            if args.write:
                for q in e.get("fr", []):
                    if q.get("k") == "verbs": q["items"] = verbs
                    if q.get("k") == "pgexp": q["items"] = expressions
                changed = True
        if changed: path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"{args.course}: {total} episódios; {bad} falhas lexicais; modo={'write' if args.write else 'audit'}")
    raise SystemExit(1 if bad else 0)


if __name__ == "__main__": main()
