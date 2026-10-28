#!/usr/bin/env python3
"""Give every English regular-pilot episode its own cultural reference.

The first occurrence of a reference is preserved. Later occurrences are
rebuilt around unused cultural references already present in the catalogue.
The rewrite updates the cultural bridge, scene, hotspots and comprehension
items together, so changing ``a.w`` alone can never leave an old work in the
episode's cultural frames.
"""
from __future__ import annotations

import copy
import glob
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def norm(value: object) -> str:
    value = unicodedata.normalize("NFKC", str(value or "")).casefold()
    return re.sub(r"\s+", " ", value).strip()


def episodes_in(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    return data if isinstance(data, list) else data.get("episodes", data.get("e", []))


def walk_replace(value, old: str, new: str):
    if isinstance(value, str):
        return value.replace(old, new)
    if isinstance(value, list):
        return [walk_replace(v, old, new) for v in value]
    if isinstance(value, dict):
        return {k: walk_replace(v, old, new) for k, v in value.items()}
    return value


def kind_label(kind: str) -> str:
    low = norm(kind)
    if any(x in low for x in ("filme", "film", "obra", "cinema")):
        return "film"
    if any(x in low for x in ("livro", "book", "romance", "novel", "poema", "poetry", "poem")):
        return "book or literary work"
    if any(x in low for x in ("canç", "cancion", "song", "music", "música")):
        return "song"
    if any(x in low for x in ("série", "serie", "program", "televis")):
        return "series"
    if any(x in low for x in ("pintura", "painting", "artist", "artista")):
        return "work of art"
    if any(x in low for x in ("teatro", "theatre", "play")):
        return "play"
    if any(x in low for x in ("tradi", "festa", "evento", "event", "document")):
        return "cultural tradition or event"
    return "cultural reference"


def cultural_candidates(used: set[str]):
    # Keep a first source record for each title. Exclude city/place-only cards;
    # they are useful as settings but are not a cultural work for this contract.
    records = {}
    allow = (
        "livro", "book", "romance", "novel", "poema", "poetry", "poem",
        "filme", "film", "obra", "série", "serie", "canç", "canción",
        "song", "pintura", "painting", "teatro", "theatre", "tradição",
        "tradition", "conto", "festa", "evento", "event", "música", "musica",
        "documento", "document", "programa", "program", "artista", "artist",
    )
    for filename in sorted(ROOT.glob("data/*.json")):
        try:
            data = json.loads(filename.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        eps = data if isinstance(data, list) else data.get("episodes", data.get("e", []))
        if not isinstance(eps, list):
            continue
        for episode in eps:
            if not isinstance(episode, dict):
                continue
            a = episode.get("a") or {}
            title = str(a.get("w") or "").strip()
            key = norm(title)
            kind = str(a.get("k") or "")
            if not title or key in used or key in records:
                continue
            if not any(token in norm(kind) for token in allow):
                continue
            records[key] = {
                "w": title,
                "k": kind or "Referência cultural",
                "y": str(a.get("y") or "").strip(),
                "source": copy.deepcopy(a),
            }
    return list(records.values())


def focus_text(episode: dict) -> str:
    text = str(episode.get("s") or episode.get("p") or "the communicative task")
    text = re.sub(r"^[^:]{0,80}:\s*", "", text)
    return text.rstrip(".")


def rebuild_cultural_frames(episode: dict, work: dict, old: str):
    title, year = work["w"], work["y"]
    label = kind_label(work["k"])
    focus = focus_text(episode)
    year_suffix = f" ({year})" if year else ""
    description = (
        f"{title}{year_suffix} é a referência cultural principal desta aula. "
        f"A obra funciona como uma lente para praticar {focus}, ligando contexto, intenção e uso natural do inglês."
    )
    # Remove old source mentions from every nested field before writing the
    # new cultural block. This catches subtitles, bridges and hidden metadata.
    replaced = walk_replace(episode, old, title)
    episode.clear()
    episode.update(replaced)
    a = episode.setdefault("a", {})
    a.update({"k": work["k"], "w": title, "y": year, "d": description})
    h = episode.setdefault("h", {})
    h["src"] = title
    h["tr"] = h.get("tr") or "Observe como o contexto ajuda a entender a cena."

    chars = [["tom", 42, 0, 1.0], ["polly", 68, 1, 1.0]]
    cultural_line = f"This lesson uses {title} as a cultural lens."
    cultural_pt = f"Esta aula usa {title} como lente cultural."
    frames = episode.setdefault("fr", [])
    for frame in frames:
        if not isinstance(frame, dict):
            continue
        k = frame.get("k")
        if k == "cover":
            frame["sub"] = f"{focus}: uma cena inspirada por {title}"
            frame["say"] = f"Observe um detalhe de {title} e conecte-o à missão: {focus}."
            frame["gancho"] = [
                "Pog",
                f"What detail from {title} helps you read this situation?",
                f"Que detalhe de {title} ajuda você a entender esta situação?",
            ]
            frame["obra"] = f"{title}{year_suffix}"
            frame["stage"] = {"rs": "cultural", "chars": chars}
        elif k == "hotscene":
            frame["rs"] = "cultural"
            frame["chars"] = chars
            frame["hot"] = [
                {"e": "📚", "x": 15, "y": 15, "en": title, "pt": "obra em foco", "say": cultural_line, "sayPt": cultural_pt},
                {"e": "🗓️", "x": 52, "y": 17, "en": year or "context", "pt": "contexto", "say": f"The context of {title} matters here.", "sayPt": f"O contexto de {title} importa aqui."},
                {"e": "🔎", "x": 86, "y": 15, "en": "detail", "pt": "detalhe", "say": "Look for one concrete detail.", "sayPt": "Procure um detalhe concreto."},
                {"e": "💬", "x": 14, "y": 82, "en": "intention", "pt": "intenção", "say": "The detail changes the intention.", "sayPt": "O detalhe muda a intenção."},
                {"e": "🧭", "x": 86, "y": 82, "en": "bridge", "pt": "ponte", "say": f"Now connect {title} to the task.", "sayPt": f"Agora ligue {title} à missão."},
            ]
            frame["say"] = "Explore os detalhes e faça a ponte com a missão."
            frame["obra"] = {"name": title, "kind": f"{work['k']} · {year}".strip(" ·"), "text": description, "line": [cultural_line, cultural_pt], "pa": {"t": "cultural", "e": ["📚", "🔎", "🧭"], "p": "b", "v": 0}}
        elif k == "pgscene":
            frame["rs"] = "cultural"
            frame["chars"] = chars
            frame["speakers"] = {"Alex": "tom", "Jordan": "polly"}
            frame["cast"] = {"Alex": ["👨", "#2b6cb0"], "Jordan": ["👩", "#c0392b"]}
            frame["lines"] = [
                ["Alex", f"I noticed {title} in the program notes.", f"Eu notei {title} nas notas do programa."],
                ["Jordan", "What detail should we keep in mind?", "Que detalhe devemos ter em mente?"],
                ["Alex", f"It is a {label}, so the context changes how we read the scene.", f"É uma referência cultural, então o contexto muda como lemos a cena."],
                ["Jordan", "That makes the intention clearer.", "Isso deixa a intenção mais clara."],
                ["Alex", f"Let us connect that detail to today’s task: {focus}.", f"Vamos ligar esse detalhe à missão de hoje: {focus}."],
                ["Jordan", "Good idea. I can say it in my own words.", "Boa ideia. Posso dizer isso com minhas próprias palavras."],
                ["Alex", "Exactly. Context first, then the natural expression.", "Exatamente. Primeiro o contexto, depois a expressão natural."],
                ["Jordan", "All right. I’m ready to try.", "Certo. Estou pronto para tentar."],
            ]
            frame["say"] = "Leia a cena e perceba como a referência muda a intenção."
        elif k == "pgsheet":
            frame["items"] = [
                {"ask": f"Which reference frames today’s lesson?", "speak": f"Which reference frames today’s lesson?", "pt": "Qual referência conduz a aula de hoje?", "opts": [["📚", title], ["🗺️", "A random place"], ["🎲", "An unrelated game"]], "a": 0, "why": f"The scene names {title} as its cultural reference."},
                {"ask": "What should the learners notice first?", "speak": "What should the learners notice first?", "pt": "O que os estudantes devem observar primeiro?", "opts": [["🔎", "A concrete cultural detail"], ["🔇", "Nothing in particular"], ["🏃", "Only the speed"]], "a": 0, "why": "A concrete detail creates the bridge to the language task."},
                {"ask": "What comes after the context?", "speak": "What comes after the context?", "pt": "O que vem depois do contexto?", "opts": [["💬", "The communicative task"], ["⏹️", "The end of the lesson"], ["❓", "A random answer" ]], "a": 0, "why": "The cultural bridge leads into the episode mission."},
            ]
            frame["rs"] = "cultural"
            frame["chars"] = [["polly", 50, 0, 1.0]]
            frame["bubble"] = ["Jordan", f"Which detail from {title} do you remember?", f"Que detalhe de {title} você lembra?"]
        elif isinstance(frame.get("obra"), str):
            frame["obra"] = f"{title}{year_suffix}"
        elif isinstance(frame.get("obra"), dict):
            frame["obra"].update({"name": title, "kind": f"{work['k']} · {year}".strip(" ·"), "text": description})


def main():
    paths = sorted(ROOT.glob("data/en-*.json"))
    episode_rows = []
    loaded = {}
    for path in paths:
        data = json.loads(path.read_text(encoding="utf-8"))
        loaded[path] = data
        eps = data if isinstance(data, list) else data.get("episodes", data.get("e", []))
        if not isinstance(eps, list):
            continue
        for episode in eps:
            if isinstance(episode, dict) and episode.get("presentation") == "regular-pilot-v1":
                episode_rows.append((path, episode))

    used = set()
    duplicates = []
    for path, episode in episode_rows:
        key = norm((episode.get("a") or {}).get("w"))
        if key in used:
            duplicates.append((path, episode))
        else:
            used.add(key)

    candidates = cultural_candidates(used)
    if len(candidates) < len(duplicates):
        raise SystemExit(f"not enough unused cultural references: {len(candidates)} for {len(duplicates)}")

    for (path, episode), work in zip(duplicates, candidates):
        old = str((episode.get("a") or {}).get("w") or "")
        rebuild_cultural_frames(episode, work, old)

    changed = {path for path, _ in duplicates}
    for path in changed:
        data = loaded[path]
        path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"episodes={len(episode_rows)} unique_before={len(used)} replaced={len(duplicates)} unique_after={len(used)+len(duplicates)} files_changed={len(changed)}")


if __name__ == "__main__":
    main()
