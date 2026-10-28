#!/usr/bin/env python3
"""Replace repeated ``pgexp`` items in the regular English course.

Only the episode's expression frame is considered here.  Occurrences in a
scene or in the review backpack remain valid recycling.  A repeated item is
replaced by a short lexical block built from the episode's own active words and
level-appropriate collocation templates.
"""
from __future__ import annotations

import argparse
import glob
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COURSES = ("en-a1", "en-a2", "en-b1", "en-b2")

STOP = {
    "the", "and", "with", "from", "that", "this", "into", "when", "what",
    "which", "your", "have", "has", "been", "were", "will", "would", "could",
    "should", "about", "there", "their", "they", "them", "then", "than", "just",
    "only", "more", "most", "some", "very", "here", "does", "did", "not", "for",
    "are", "was", "you", "she", "her", "his", "our", "its", "can", "how", "why",
    "who", "all", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "scene", "episode", "today", "lesson", "focus", "while", "we",
}
BAD_OBJECT_HEADS = {
    "one", "two", "three", "four", "five", "six", "first", "then", "finally", "after",
    "go", "goes", "went", "come", "comes", "came", "ask", "talk", "look", "wait", "help",
    "check", "find", "bring", "share", "choose", "remember", "write", "take", "make", "get",
    "catch", "run", "figure", "deal", "keep", "sign", "settle", "fit", "pay", "try", "kick",
    "kicked", "score", "scored", "equalize", "equalized", "win", "won", "start", "break", "turn",
    "test", "heat", "boil", "freeze", "add", "bake", "mix", "stir", "use", "using", "be", "have",
    "was", "were", "is", "are", "been", "being", "built", "signed", "taken", "hidden", "discovered",
    "skim", "scan", "melt", "scored", "equalized", "kicked",
}

TEMPLATES = {
    "a1": [
        ("ask about {obj}", "perguntar sobre"), ("look at {obj}", "olhar para"),
        ("talk about {obj}", "falar sobre"), ("wait for {obj}", "esperar por"),
        ("help with {obj}", "ajudar com"), ("check {obj}", "conferir"),
        ("find {obj}", "encontrar"), ("bring {obj}", "trazer"),
        ("share {obj}", "compartilhar"), ("choose {obj}", "escolher"),
        ("remember {obj}", "lembrar de"), ("write down {obj}", "anotar"),
        ("look after {obj}", "cuidar de"), ("get ready for {obj}", "preparar-se para"),
        ("make room for {obj}", "abrir espaço para"), ("take care of {obj}", "cuidar de"),
        ("be ready for {obj}", "estar pronto para"), ("good at {obj}", "ser bom em"),
        ("new to {obj}", "ser novo em"), ("kind to {obj}", "ser gentil com"),
        ("free for {obj}", "estar livre para"), ("sure about {obj}", "ter certeza sobre"),
        ("open to {obj}", "estar aberto a"), ("close to {obj}", "estar perto de"),
        ("different from {obj}", "ser diferente de"), ("same as {obj}", "ser igual a"),
        ("far from {obj}", "estar longe de"), ("ready to use {obj}", "estar pronto para usar"),
        ("in time for {obj}", "chegar a tempo para"), ("right about {obj}", "estar certo sobre"),
        ("back to {obj}", "voltar a"), ("next to {obj}", "ficar ao lado de"),
    ],
    "a2": [
        ("catch up on {obj}", "se atualizar sobre"), ("look forward to {obj}", "aguardar com expectativa"),
        ("run into {obj}", "encontrar por acaso"), ("figure out {obj}", "descobrir"),
        ("deal with {obj}", "lidar com"), ("get along with {obj}", "dar-se bem com"),
        ("keep up with {obj}", "acompanhar"), ("take part in {obj}", "participar de"),
        ("make up for {obj}", "compensar"), ("put off {obj}", "adiar"),
        ("sort out {obj}", "resolver"), ("come across {obj}", "deparar-se com"),
        ("sign up for {obj}", "inscrever-se em"), ("check in for {obj}", "fazer check-in para"),
        ("settle into {obj}", "acomodar-se em"), ("fit in with {obj}", "encaixar-se em"),
        ("make sense of {obj}", "entender"), ("get used to {obj}", "acostumar-se com"),
        ("on the way to {obj}", "a caminho de"), ("in charge of {obj}", "responsável por"),
        ("at the end of {obj}", "no fim de"), ("for the sake of {obj}", "em nome de"),
        ("by the time of {obj}", "até o momento de"), ("in touch with {obj}", "em contato com"),
        ("on good terms with {obj}", "em bons termos com"), ("out of time for {obj}", "sem tempo para"),
        ("under pressure from {obj}", "sob pressão de"), ("in the middle of {obj}", "no meio de"),
        ("at short notice for {obj}", "com pouca antecedência para"), ("as a result of {obj}", "como resultado de"),
    ],
    "b1": [
        ("come to terms with {obj}", "aceitar e lidar com"), ("raise a question about {obj}", "levantar uma questão sobre"),
        ("draw attention to {obj}", "chamar atenção para"), ("keep tabs on {obj}", "acompanhar de perto"),
        ("rule out {obj}", "descartar"), ("follow up on {obj}", "dar continuidade a"),
        ("weigh up {obj}", "avaliar"), ("set out to {obj}", "propor-se a"),
        ("come down to {obj}", "reduzir-se a"), ("hinge on {obj}", "depender de"),
        ("take issue with {obj}", "contestar"), ("bear in mind {obj}", "ter em mente"),
        ("shed light on {obj}", "esclarecer"), ("make a case for {obj}", "defender"),
        ("strike a balance between {obj}", "equilibrar"), ("go hand in hand with {obj}", "andar junto com"),
        ("at odds with {obj}", "em conflito com"), ("in light of {obj}", "à luz de"),
        ("with regard to {obj}", "com relação a"), ("on behalf of {obj}", "em nome de"),
        ("in keeping with {obj}", "de acordo com"), ("in response to {obj}", "em resposta a"),
        ("in the course of {obj}", "no decorrer de"), ("at the heart of {obj}", "no centro de"),
        ("on the grounds of {obj}", "com base em"), ("in the wake of {obj}", "na esteira de"),
        ("under scrutiny for {obj}", "sob análise por"), ("by all accounts {obj}", "segundo todos os relatos"),
        ("in practical terms {obj}", "em termos práticos"), ("for the time being {obj}", "por enquanto"),
    ],
    "b2": [
        ("call into question {obj}", "colocar em dúvida"), ("draw a distinction between {obj}", "distinguir"),
        ("bear the brunt of {obj}", "sofrer o impacto maior de"), ("take precedence over {obj}", "ter precedência sobre"),
        ("come to grips with {obj}", "enfrentar e compreender"), ("give rise to {obj}", "dar origem a"),
        ("pave the way for {obj}", "abrir caminho para"), ("put {obj} into perspective", "colocar em perspectiva"),
        ("read between the lines of {obj}", "ler nas entrelinhas de"), ("take exception to {obj}", "se opor a"),
        ("hold sway over {obj}", "exercer influência sobre"), ("amount to {obj}", "equivaler a"),
        ("stem from {obj}", "derivar de"), ("run counter to {obj}", "contrariar"),
        ("in keeping with {obj}", "em consonância com"), ("by virtue of {obj}", "em virtude de"),
        ("at the expense of {obj}", "às custas de"), ("in the wake of {obj}", "na esteira de"),
        ("set the stage for {obj}", "preparar o terreno para"), ("take stock of {obj}", "avaliar a situação de"),
        ("bring to bear on {obj}", "aplicar sobre"), ("in the face of {obj}", "diante de"),
        ("on the cusp of {obj}", "à beira de"), ("underpin {obj}", "sustentar"),
        ("go against the grain of {obj}", "ir contra a corrente de"), ("leave no stone unturned for {obj}", "não deixar pedra sobre pedra por"),
        ("at the crux of {obj}", "no cerne de"), ("with a view to {obj}", "com vistas a"),
        ("insofar as {obj}", "na medida em que"), ("subject to {obj}", "sujeito a"),
    ],
}

# Safer collocation banks for replacement items.  Every template accepts a
# noun phrase from the episode's active vocabulary, so a replacement remains
# grammatical even when the original lesson is about an unusual object.
SAFE_TEMPLATES = {
    "a1": TEMPLATES["a1"],
    "a2": [
        ("learn about {obj}", "aprender sobre"), ("talk through {obj}", "conversar sobre"),
        ("think about {obj}", "pensar em"), ("find out about {obj}", "descobrir sobre"),
        ("look into {obj}", "investigar"), ("pay attention to {obj}", "prestar atenção a"),
        ("keep track of {obj}", "acompanhar"), ("make room for {obj}", "abrir espaço para"),
        ("take care of {obj}", "cuidar de"), ("get ready for {obj}", "preparar-se para"),
        ("look forward to {obj}", "aguardar com expectativa"), ("get used to {obj}", "acostumar-se com"),
        ("plan around {obj}", "planejar em torno de"), ("focus on {obj}", "concentrar-se em"),
        ("ask about {obj}", "perguntar sobre"), ("read about {obj}", "ler sobre"),
        ("write about {obj}", "escrever sobre"), ("work on {obj}", "trabalhar em"),
        ("prepare for {obj}", "preparar-se para"), ("check on {obj}", "verificar"),
        ("take part in {obj}", "participar de"), ("make sense of {obj}", "entender"),
        ("deal with {obj}", "lidar com"), ("fit in with {obj}", "encaixar-se em"),
        ("stay in touch with {obj}", "manter contato com"), ("be in charge of {obj}", "ser responsável por"),
        ("at the end of {obj}", "no fim de"), ("in the middle of {obj}", "no meio de"),
        ("as a result of {obj}", "como resultado de"), ("for the sake of {obj}", "em nome de"),
    ],
    "b1": [
        ("focus on {obj}", "concentrar-se em"), ("draw attention to {obj}", "chamar atenção para"),
        ("keep track of {obj}", "acompanhar de perto"), ("look into {obj}", "investigar"),
        ("follow up on {obj}", "dar continuidade a"), ("learn from {obj}", "aprender com"),
        ("reflect on {obj}", "refletir sobre"), ("build on {obj}", "desenvolver a partir de"),
        ("work through {obj}", "analisar passo a passo"), ("account for {obj}", "explicar"),
        ("plan around {obj}", "planejar em torno de"), ("respond to {obj}", "responder a"),
        ("prepare for {obj}", "preparar-se para"), ("argue for {obj}", "argumentar a favor de"),
        ("speak about {obj}", "falar sobre"), ("raise a question about {obj}", "levantar uma questão sobre"),
        ("shed light on {obj}", "esclarecer"), ("make a case for {obj}", "defender"),
        ("strike a balance with {obj}", "equilibrar com"), ("go hand in hand with {obj}", "andar junto com"),
        ("in light of {obj}", "à luz de"), ("with regard to {obj}", "com relação a"),
        ("on behalf of {obj}", "em nome de"), ("in response to {obj}", "em resposta a"),
        ("at the heart of {obj}", "no centro de"), ("in the wake of {obj}", "na esteira de"),
        ("under scrutiny for {obj}", "sob análise por"), ("in practical terms {obj}", "em termos práticos"),
    ],
    "b2": [
        ("call into question {obj}", "colocar em dúvida"), ("draw a distinction between {obj}", "distinguir"),
        ("bear the brunt of {obj}", "sofrer o impacto maior de"), ("take precedence over {obj}", "ter precedência sobre"),
        ("come to grips with {obj}", "enfrentar e compreender"), ("give rise to {obj}", "dar origem a"),
        ("pave the way for {obj}", "abrir caminho para"), ("put {obj} into perspective", "colocar em perspectiva"),
        ("read between the lines of {obj}", "ler nas entrelinhas de"), ("take exception to {obj}", "se opor a"),
        ("hold sway over {obj}", "exercer influência sobre"), ("stem from {obj}", "derivar de"),
        ("run counter to {obj}", "contrariar"), ("in keeping with {obj}", "em consonância com"),
        ("by virtue of {obj}", "em virtude de"), ("at the expense of {obj}", "às custas de"),
        ("in the wake of {obj}", "na esteira de"), ("set the stage for {obj}", "preparar o terreno para"),
        ("take stock of {obj}", "avaliar a situação de"), ("bring to bear on {obj}", "aplicar sobre"),
        ("in the face of {obj}", "diante de"), ("on the cusp of {obj}", "à beira de"),
        ("underpin {obj}", "sustentar"), ("at the crux of {obj}", "no cerne de"),
        ("with a view to {obj}", "com vistas a"), ("subject to {obj}", "sujeito a"),
    ],
}


def norm(value: str) -> str:
    value = str(value or "").replace("’", "'").replace("‘", "'").replace("`", "'")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9']+", " ", str(value or "").lower())).strip()


def theme_terms(e: dict) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for item in e.get("v") or []:
        if isinstance(item, list) and item:
            en = str(item[0]).strip()
            pt = str(item[1]).strip() if len(item) > 1 else en
            head = norm(en).split(" ", 1)[0] if norm(en) else ""
            if en and head not in BAD_OBJECT_HEADS and norm(en) not in {norm(x[0]) for x in out}:
                out.append((en.lower(), pt))
    # Add English title/work tokens only after the authored vocabulary.
    extra = " ".join([str(e.get("t") or ""), str((e.get("a") or {}).get("w") or "")])
    for token in re.findall(r"[A-Za-z][A-Za-z'-]{3,}", extra):
        if token.lower() not in STOP and token.lower() not in BAD_OBJECT_HEADS and norm(token) not in {norm(x[0]) for x in out}:
            out.append((token.lower(), token))
    return out or [("context", "contexto")]


def files(course: str):
    for path in sorted(glob.glob(str(ROOT / "data" / f"{course}_*.json"))):
        yield Path(path), json.loads(Path(path).read_text(encoding="utf-8"))


def replace_course(course: str, write: bool) -> tuple[int, int]:
    shards = list(files(course))
    episodes = [e for _, data in shards for e in data]
    episodes.sort(key=lambda e: e.get("o", e.get("n", 0)))
    level = course.rsplit("-", 1)[-1]
    templates = SAFE_TEMPLATES[level]
    canonical: set[str] = set()
    for e in episodes:
        q = next((q for q in e.get("fr", []) if q.get("k") == "pgexp"), None)
        if not q:
            continue
        for item in q.get("items", []):
            key = norm(item.get("en") or item.get("x"))
            if key:
                canonical.add(key)
    # Keep only the first occurrence; later occurrences are the ones to replace.
    seen: set[str] = set()
    replacements = 0
    used = set(canonical)
    for e in episodes:
        q = next((q for q in e.get("fr", []) if q.get("k") == "pgexp"), None)
        if not q:
            continue
        terms = theme_terms(e)
        topic = str(e.get("s") or e.get("t") or "the lesson focus")
        work = str((e.get("a") or {}).get("w") or "the cultural work")
        for idx, item in enumerate(q.get("items", [])):
            old = norm(item.get("en") or item.get("x"))
            if not old or old not in seen:
                if old:
                    seen.add(old)
                continue
            chosen = None
            for ti, (template, gloss) in enumerate(templates):
                for oi, (obj, obj_pt) in enumerate(terms):
                    template_use = template
                    if level in ("b1", "b2"):
                        template_use = template_use.replace("{obj}", "the {obj}")
                    phrase = template_use.format(obj=obj)
                    key = norm(phrase)
                    if key in used or key == old:
                        continue
                    # Keep blocks compact; a long authored term is shortened by
                    # trying the next term rather than creating a sentence.
                    if len(key.split()) > 8:
                        continue
                    chosen = (phrase, gloss, obj, obj_pt, key)
                    break
                if chosen:
                    break
            if not chosen:
                raise RuntimeError(f"sem expressão nova para {course} {e.get('n')}")
            phrase, gloss, obj, obj_pt, key = chosen
            used.add(key); seen.add(key); replacements += 1
            item["en"] = phrase
            item["x"] = phrase
            item["pt"] = f"{gloss} {obj_pt}"
            item["tag"] = "Expressão"
            item["use"] = f"Use este bloco para falar de {obj_pt} em uma situação ligada a {work}."
            item["ex"] = [f'Use "{phrase}" when you talk about {obj}.', f'Use "{phrase}" ao falar de {obj_pt}.']
        # Keep the quiz synchronized with the four visible expression cards.
        items = q.get("items", [])
        quiz = []
        for i, item in enumerate(items):
            opts = [items[i].get("en", ""), items[(i + 1) % len(items)].get("en", ""), items[(i + 2) % len(items)].get("en", "")]
            quiz.append({"ask": f"Qual bloco combina com {topic}?", "opts": opts, "a": 0, "why": f"**{items[i].get('en', '')}** = {items[i].get('pt', '')}."})
        q["quiz"] = quiz
    if write:
        by_n = {e.get("n"): e for e in episodes}
        for path, data in shards:
            path.write_text(json.dumps([by_n[e.get("n")] for e in data], ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    return len(episodes), replacements


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--course", action="append", choices=COURSES)
    args = ap.parse_args()
    for course in args.course or COURSES:
        total, replacements = replace_course(course, args.write)
        print(f"{course}: {total} episódios; {replacements} expressões substituídas; modo={'write' if args.write else 'audit'}")


if __name__ == "__main__":
    main()
