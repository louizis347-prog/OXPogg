#!/usr/bin/env python3
"""Rebuilds C2 verb/expression practice from each episode's own focus.

The previous conversion guaranteed four item slots but could copy generic verbs and
sentence-sized ``cexp`` material.  This tool creates short, teachable lexical
chunks from the episode focus and its six active words.  It is deliberately
content-only: it does not change frames, cultural references or progress IDs.
"""
from __future__ import annotations

import glob
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSE = "en-c2"
ICONS = ["🧩", "🎚️", "💡", "🧭"]

# Glosses are kept explicit so the practice cards remain useful to a Portuguese-speaking learner.
GLOSS = {
    "foreground": "colocar em primeiro plano", "reorder": "reordenar", "front": "antepor", "defer": "adiar",
    "punctuate": "pontuar", "compress": "comprimir", "juxtapose": "justapor", "balance": "equilibrar",
    "suspend": "suspender", "accumulate": "acumular", "qualify": "qualificar", "unpack": "desdobrar",
    "resolve": "resolver", "layer": "sobrepor", "withhold": "reter", "bracket": "isolar entre parênteses",
    "digress": "divagar", "interrupt": "interromper", "insert": "inserir", "sidetrack": "desviar",
    "resume": "retomar", "embed": "encaixar", "subordinate": "subordinar", "concede": "conceder",
    "condition": "condicionar", "nest": "anidar", "coordinate": "coordenar", "repeat": "repetir",
    "echo": "ecoar", "parallel": "paralelizar", "align": "alinhar", "reinforce": "reforçar",
    "unify": "unificar", "pattern": "padronizar", "invert": "inverter", "oppose": "opor",
    "reverse": "reverter", "mirror": "espelhar", "contrast": "contrastar", "sharpen": "aguçar",
    "represent": "representar", "associate": "associar", "invoke": "invocar", "substitute": "substituir",
    "condense": "condensar", "index": "indicar", "evoke": "evocar", "contradict": "contradizer",
    "reconcile": "conciliar", "provoke": "provocar", "complicate": "complicar", "expose": "expor",
    "trace": "rastrear", "infer": "inferir", "deduce": "deduzir", "scrutinize": "examinar",
    "corroborate": "corroborar", "challenge": "questionar", "hedge": "atenuar", "qualify": "qualificar",
    "stake": "apostar", "frame": "enquadrar", "signal": "sinalizar", "nuance": "nuançar",
    "negotiate": "negociar", "concede": "conceder", "counter": "contrapor", "rebut": "refutar",
    "underscore": "sublinhar", "broach": "abordar", "delineate": "delinear", "differentiate": "diferenciar",
}

PROFILES = [
    (r"syntax|style|word order|fronting|inversion|clause", [
        "foreground", "reorder", "front", "defer", "punctuate", "compress", "juxtapose", "balance",
        "frame", "signal", "sharpen", "underscore", "delineate", "differentiate", "qualify", "echo",
    ], ["foreground the clause", "defer the main point", "front the key phrase", "mark a contrast", "compress the syntax", "balance two clauses", "signal the register", "sharpen the emphasis"]),
    (r"periodic|cumulative|suspense|modifier|trailing", [
        "suspend", "accumulate", "qualify", "unpack", "defer", "resolve", "layer", "withhold",
        "compress", "foreground", "punctuate", "balance", "frame", "signal", "echo", "underscore",
    ], ["suspend the payoff", "layer a modifier", "delay the main clause", "accumulate detail", "resolve the period", "withhold the predicate", "balance the cadence", "mark the release"]),
    (r"parenthes|digression|aside|dash|interruption", [
        "bracket", "digress", "interrupt", "insert", "qualify", "sidetrack", "resume", "punctuate",
        "frame", "withhold", "layer", "compress", "signal", "foreground", "echo", "balance",
    ], ["bracket an aside", "insert a qualification", "interrupt the flow", "resume the thread", "mark a digression", "layer a comment", "frame the aside", "punctuate the break"]),
    (r"subordinat|embedded|relative|concession|condition|complex", [
        "embed", "subordinate", "concede", "condition", "nest", "coordinate", "qualify", "foreground",
        "defer", "balance", "frame", "signal", "differentiate", "layer", "resolve", "compress",
    ], ["embed a clause", "concede a point", "condition the claim", "nest a relative", "qualify the statement", "coordinate two ideas", "defer the result", "balance the hierarchy"]),
    (r"anaphora|parallel|repetition|series|unity", [
        "repeat", "echo", "parallel", "align", "reinforce", "unify", "pattern", "balance",
        "foreground", "mirror", "frame", "signal", "underscore", "compress", "differentiate", "sharpen",
    ], ["echo the opening", "parallel the clauses", "repeat the cadence", "align the series", "reinforce the pattern", "unify the voice", "balance the refrain", "sharpen the parallel"]),
    (r"chiasm|antithesis|opposite|reverse|contrast", [
        "invert", "oppose", "reverse", "mirror", "contrast", "balance", "frame", "sharpen",
        "juxtapose", "counter", "rebut", "differentiate", "foreground", "signal", "echo", "underscore",
    ], ["invert the order", "mirror the contrast", "oppose two claims", "reverse the emphasis", "balance the antithesis", "frame the counterpoint", "sharpen the opposition", "signal the reversal"]),
    (r"metonym|synecdoche|represent|association|crown|whole", [
        "represent", "associate", "invoke", "substitute", "condense", "index", "evoke", "frame",
        "foreground", "signal", "differentiate", "trace", "underscore", "compress", "mirror", "balance",
    ], ["stand for the whole", "invoke an association", "substitute the part", "condense the image", "index a power", "evoke the institution", "frame the symbol", "trace the reference"]),
    (r"oxymoron|paradox|contradiction|tension", [
        "juxtapose", "contradict", "reconcile", "provoke", "resolve", "complicate", "expose", "balance",
        "frame", "counter", "qualify", "foreground", "mirror", "sharpen", "signal", "differentiate",
    ], ["juxtapose two terms", "hold a contradiction", "reconcile the tension", "provoke a paradox", "resolve the opposition", "complicate the claim", "expose the premise", "frame the ambiguity"]),
    (r"idiom|phrasal|collocation|slang|register|rhetoric|discourse", [
        "frame", "signal", "nuance", "hedge", "stake", "negotiate", "concede", "counter",
        "rebut", "broach", "differentiate", "underscore", "qualify", "challenge", "scrutinize", "delineate",
    ], ["signal a register", "hedge a claim", "stake a position", "negotiate a nuance", "concede a point", "counter an objection", "broach a topic", "mark a collocation"]),
]
DEFAULT_VERBS = ["trace", "infer", "deduce", "scrutinize", "corroborate", "challenge", "frame", "signal", "nuance", "negotiate", "counter", "rebut", "underscore", "broach", "delineate", "differentiate"]
DEFAULT_EXP = ["trace the implication", "infer the subtext", "scrutinize the wording", "frame the response", "signal the register", "nuance the claim", "negotiate the ambiguity", "challenge the premise"]
ALL_VERBS = list(dict.fromkeys(v for _, verbs, _ in PROFILES for v in verbs))


def frames(e):
    return {q.get("k"): q for q in e.get("fr", [])}


def words(e):
    out=[]
    for item in e.get("v") or []:
        if isinstance(item,list) and item and re.fullmatch(r"[A-Za-z][A-Za-z' -]*", str(item[0])):
            out.append(str(item[0]).lower().strip())
    return out or ["syntax", "register", "context", "meaning", "voice", "choice"]


def choose_profile(focus):
    low=(focus or "").lower()
    for pattern, verbs, expr in PROFILES:
        if re.search(pattern, low): return verbs,expr
    return DEFAULT_VERBS,DEFAULT_EXP


def seed(e):
    return int(hashlib.sha1(str(e.get("n")).encode()).hexdigest()[:8],16)


def third(verb):
    parts=verb.split(); last=parts[-1]
    if last.endswith("y") and len(last)>1 and last[-2] not in "aeiou": last=last[:-1]+"ies"
    elif last.endswith(("s","x","z","ch","sh","o")): last += "es"
    else: last += "s"
    return " ".join(parts[:-1]+[last])


def make_verbs(e, candidates):
    v=words(e); offset=seed(e)%len(candidates); chosen=[]
    used = repair_episode.used_verbs
    pool = list(dict.fromkeys(candidates))
    for step in range(1, len(pool)):
        for shift in range(len(pool)):
            candidate=[pool[(offset+shift+i*step)%len(pool)] for i in range(4)]
            key=tuple(sorted(candidate))
            if len(set(candidate))==4 and key not in used:
                chosen=candidate; used.add(key); break
        if chosen: break
    if not chosen:
        # A profile can exhaust its finite combinations over 510 episodes.
        # Fall back to the full advanced C2 lexicon while preserving global
        # tuple uniqueness.
        for step in range(1, len(ALL_VERBS)):
            for shift in range(len(ALL_VERBS)):
                candidate=[ALL_VERBS[(offset+shift+i*step)%len(ALL_VERBS)] for i in range(4)]
                key=tuple(sorted(candidate))
                if len(set(candidate))==4 and key not in used:
                    chosen=candidate; used.add(key); break
            if chosen: break
    if not chosen: chosen=[ALL_VERBS[(offset+i)%len(ALL_VERBS)] for i in range(4)]
    focus=e.get("s") or e.get("t") or "this focus"
    out=[]
    for i,verb in enumerate(chosen):
        pt=GLOSS.get(verb,verb)
        obj=v[i%len(v)]
        out.append({"v":verb,"ic":ICONS[i],"pt":pt,
            "f":[["I",f"I {verb} the {obj}."],["she",f"She {third(verb)} the {obj}."]],
            "ex":[f"In this episode, we {verb} the {obj} to discuss {focus}.",f"Neste episódio, nós {pt} {obj} para discutir {focus}."],
            "note":f"**{verb}** = {pt}; use-o para falar de {focus}."})
    return out


def make_expressions(e, templates, used=None):
    v=words(e); offset=seed(e)%len(templates); focus=e.get("s") or e.get("t") or "the focus"
    used = used if used is not None else set()
    out=[]; seen=set()
    for i in range(4):
        base=templates[(offset+i)%len(templates)]
        phrase = None; key = None
        for j, prep in enumerate(("around", "in", "on", "through")):
            noun=v[(i+j)%len(v)]
            candidate=f"{base} {prep} {noun}"
            candidate_key=re.sub(r"[^a-z0-9']+"," ",candidate.lower()).strip()
            if len(candidate_key.split()) <= 6 and candidate_key not in seen and candidate_key not in used:
                phrase, key = candidate, candidate_key
                break
        if phrase is None:
            noun=v[(i+offset)%len(v)]
            phrase=f"{base} {noun}"
            key=re.sub(r"[^a-z0-9']+"," ",phrase.lower()).strip()
        seen.add(key); used.add(key)
        pt=f"bloco para {focus.lower()} ({noun})"
        out.append({"x":phrase,"en":phrase,"pt":pt,"ic":ICONS[len(out)%4],"use":f"Bloco curto para falar de {focus}.","ex":[phrase,f"Bloco ligado a {focus}."]})
        if len(out)==4: break
    return out


def repair_episode(e):
    fs=frames(e); focus=e.get("s") or e.get("t") or "the focus"
    candidates,templates=choose_profile(focus)
    if fs.get("verbs"): fs["verbs"]["items"]=make_verbs(e,candidates)
    if fs.get("pgexp"): fs["pgexp"]["items"]=make_expressions(e,templates,repair_episode.used)
    return e


def main():
    total=0
    repair_episode.used=set()
    repair_episode.used_verbs=set()
    for path in sorted((ROOT/"data").glob(f"{COURSE}_*.json")):
        data=json.loads(path.read_text(encoding="utf-8"))
        for e in data:
            if e.get("presentation")=="regular-pilot-v1": repair_episode(e); total+=1
        path.write_text(json.dumps(data,ensure_ascii=False,separators=(",",":")),encoding="utf-8")
    print(f"{COURSE}: {total} episódios reescritos")

if __name__=="__main__": main()
