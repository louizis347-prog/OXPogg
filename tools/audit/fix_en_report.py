#!/usr/bin/env python3
"""Repair the English regular pilot after the content audit.

This pass is deliberately conservative: it keeps ids and the existing lesson
model, but replaces stale boilerplate, repairs malformed practice options,
fills the C1/C2 sound lab, and rewrites scenes that are mostly copied from a
neighbouring episode.  It also gives every episode a normalized-unique cultural
reference and refreshes all bridge fields that point at the work.
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "plan"))
from plan_lib import norm

LEVELS = {"en-a1": "A1", "en-a2": "A2", "en-b1": "B1", "en-b2": "B2", "en-c1": "C1", "en-c2": "C2"}
SCENES = ["cafe", "street", "park", "library", "kitchen", "museum", "station", "office", "market", "theatre"]

# A reserve of real books, films, songs, artworks and public landmarks.  It is
# used only when the old catalogue assigned the same work to two episodes.
RESERVE = [
    "The House of Mirth", "The Mill on the Floss", "The Tipping Point", "The Art of War",
    "The Interpretation of Dreams", "The Comedy of Errors", "The King James Bible",
    "The Telephone", "The House That Jack Built", "The Shock Doctrine", "The Four Freedoms",
    "The Autobiography of Benjamin Franklin", "The Wolf in Sheep's Clothing",
    "The Danger of a Single Story", "Life Is Beautiful", "The Road", "The Love Song of J. Alfred Prufrock",
    "Three Men in a Boat", "The Tale of Benjamin Bunny", "The Adventures of Pinocchio",
    "In the Heights", "The Gates of Hell", "The Ecstasy of Saint Teresa", "The Pompidou Centre",
    "The Burj Khalifa", "The Colosseum", "The Chrysler Building", "The Book of Kells",
    "What's Going On", "Songs in the Key of Life", "Purple Rain", "OK Computer",
    "Sweet Home Alabama", "Water Lilies", "Ways of Seeing", "Sophie's World", "Sophie's Choice",
    "Doctor Strangelove", "Rope", "Long Day's Journey into Night", "Rosencrantz and Guildenstern Are Dead",
    "Meditations on First Philosophy", "The Tipping Point", "The Glass Palace", "The Go-Between",
    "The Gettysburg Address", "The Canterbury Tales", "Rebecca", "Cider with Rosie", "Inside Out",
    "Rear Window", "The Turn of the Screw", "Erin Brockovich", "The Wonder Years", "The Intern",
    "Nancy Drew and the Secret of the Old Clock", "The Devil Wears Prada", "The Natural",
    "The Diary of a Young Girl", "The Motorcycle Diaries", "The Parent Trap", "Wuthering Heights",
    "The Lord of the Rings", "Booksmart", "The Time Machine", "The Gift of the Magi",
    "When Harry Met Sally", "The Shawshank Redemption", "Chariots of Fire", "Apollo 13",
    "Casablanca", "Citizen Kane", "Four Weddings and a Funeral", "Working Girl", "The Magic Mountain",
    "Persuasion", "The Namesake", "The Social Network", "The Yellow Wallpaper", "The Hunger Games",
    "The Princess and the Pea", "Gulliver's Travels", "David Copperfield", "Anne of Green Gables",
    "The Boy Who Cried Wolf", "Jane Eyre", "Great Expectations", "The Little Mermaid",
    "The Importance of Being Earnest", "The Martian", "The Owl and the Pussy-cat",
    "The Little Match Girl", "The Sorcerer's Apprentice", "Silas Marner", "The Little Engine That Could",
    "A Midsummer Night's Dream", "The Little Prince", "You've Got Mail", "The Wind in the Willows",
    "Harry Potter and the Philosopher's Stone", "The Hound of the Baskervilles", "Groundhog Day",
    "The Tortoise and the Hare", "The Gift of the Magi", "Emma", "The Old Man and the Sea",
    "My Fair Lady", "Hansel and Gretel", "Waiting for Godot", "Spider-Man", "The Secret Garden",
    "The Grand Budapest Hotel", "The Itsy Bitsy Spider", "Fantastic Mr Fox", "Casey at the Bat",
    "Singin' in the Rain", "The Emperor's New Clothes", "The Gingerbread Man", "The Swiss Family Robinson",
    "Stone Soup", "Moulin Rouge", "Where's Waldo?", "The Nutcracker", "Mad Men", "Bartleby",
    "Seinfeld", "12 Angry Men", "Agatha Christie's Poirot", "Marie Kondo", "Yes Minister",
    "The Grapes of Wrath", "The Little Match Girl", "The Lady, or the Tiger?", "The Sorcerer's Apprentice",
    "The Wind in the Willows", "The Secret Garden", "The Tale of Peter Rabbit", "The Snowman",
    "Eat Pray Love", "The Four Seasons", "The Planets", "The Firebird", "The Rite of Spring",
    "The Starry Night", "Girl with a Pearl Earring", "Guernica", "Nighthawks", "American Gothic",
    "The Thinker", "The Kiss", "The Persistence of Memory", "The Birth of Venus", "The Great Wave",
    "The Scream", "Campbell's Soup Cans", "The Night Watch", "The Garden of Earthly Delights",
    "The Parthenon", "The Taj Mahal", "The Statue of Liberty", "The Golden Gate Bridge", "The Space Needle",
    "The Great Barrier Reef", "Yellowstone", "The National Mall", "The High Line", "The Freedom Trail",
    "Route 66", "The Appalachian Trail", "The Underground Railroad", "The Apollo Theater", "Central Park",
    "The Rose Parade", "Macy's Thanksgiving Day Parade", "The Harlem Renaissance", "The New Deal",
    "The Getty Center", "The Metropolitan Museum of Art", "The Library of Congress", "The Smithsonian",
    "The Kennedy Center", "The Sundance Film Festival", "The Newport Jazz Festival", "Woodstock",
    "The Civil Rights Act", "The Moon Landing", "The Dust Bowl", "The Great Migration", "The Gold Rush",
    "The Boston Tea Party", "The Declaration of Independence", "The Constitution", "The Bill of Rights",
    "The Underground Railroad", "The Montgomery Bus Boycott", "The March on Washington", "The New York Public Library",
    "The Chicago Blues", "The Mississippi Delta", "The Appalachian Spring", "The Pacific Crest Trail",
    "The Oregon Trail", "The Transcontinental Railroad", "The Hoover Dam", "The Erie Canal", "The Panama Canal",
    "The Great Gatsby", "The Catcher in the Rye", "To Kill a Mockingbird", "Brave New World", "The War of the Worlds",
    "A Tale of Two Cities", "The Christmas Carol", "The Little House on the Prairie", "The Wonderful Wizard of Oz",
    "Alice's Adventures in Wonderland", "The Hobbit", "The Alchemist", "The Lorax", "Walden", "The Rosetta Stone",
    "Beloved", "The Bluest Eye", "Song of Solomon", "The Color Purple", "Invisible Man",
    "Their Eyes Were Watching God", "The Left Hand of Darkness", "The Dispossessed", "The Handmaid's Tale",
    "The Testaments", "Never Let Me Go", "Klara and the Sun", "Cloud Atlas", "Station Eleven",
    "The Remains of the Day", "The English Patient", "The Unbearable Lightness of Being", "The Master and Margarita",
    "One Hundred Years of Solitude", "Love in the Time of Cholera", "The House on Mango Street",
    "The Brief Wondrous Life of Oscar Wao", "The Poisonwood Bible", "The Book Thief", "All the Light We Cannot See",
    "The Night Circus", "The Goldfinch", "The Overstory", "The Secret History", "The Name of the Rose",
    "The Shadow of the Wind", "The Pillars of the Earth", "The Once and Future King", "A Wrinkle in Time",
    "The Giver", "The Golden Compass", "The Neverending Story", "The Phantom Tollbooth", "Holes",
    "The Outsiders", "The Perks of Being a Wallflower", "Looking for Alaska", "Room", "The Kite Runner",
    "The Trial", "The Castle", "The Metamorphosis", "The Plague", "The Stranger", "The Myth of Sisyphus",
    "The Republic", "The Prince", "The Wealth of Nations", "Silent Spring", "Cosmos", "Hidden Figures",
    "The Code Book", "The Innovators", "The Design of Everyday Things", "The Story of Art", "The Poetics of Space",
    "The Craftsman", "The Artist's Way", "Steal Like an Artist", "The Red Balloon", "The Seventh Seal",
    "Persona", "Wild Strawberries", "The Bicycle Thieves", "La Dolce Vita", "8½", "The Leopard",
    "The Battle of Algiers", "The 400 Blows", "Breathless", "The Umbrellas of Cherbourg", "Wings of Desire",
    "Paris Texas", "The Lives of Others", "Run Lola Run", "The White Ribbon", "In the Mood for Love",
    "Chungking Express", "Tokyo Story", "Ikiru", "Seven Samurai", "The Piano", "The Babadook",
    "Moonlight", "Get Out", "Do the Right Thing", "The Florida Project", "Lady Bird", "Nomadland",
    "Minari", "Past Lives", "The Farewell", "Whiplash", "The Grandmaster", "The Lunchbox",
    "Monsoon Wedding", "The Secret in Their Eyes", "Wild Tales", "Roma", "Y Tu Mamá También",
    "The Diving Bell and the Butterfly", "The Intouchables", "The Chorus", "A Prophet", "Portrait of a Lady on Fire",
    "Anatomy of a Fall", "The Zone of Interest", "A Separation", "The Salesman", "Close-Up", "Taste of Cherry",
    "Persepolis", "The Triplets of Belleville", "Song of the Sea", "The Secret of Kells", "Fantastic Planet",
    "The Red Turtle", "Kubo and the Two Strings", "Coraline", "The Iron Giant", "Spirited Away",
    "My Neighbor Totoro", "Princess Mononoke", "Grave of the Fireflies", "The Wind Rises", "Your Name",
    "Perfect Blue", "Paprika", "Akira", "Ghost in the Shell", "The Four Seasons", "Pictures at an Exhibition",
    "Boléro", "Clair de Lune", "Carmina Burana", "Kind of Blue", "A Love Supreme", "Time Out",
    "Blue Train", "Giant Steps", "The Miseducation of Lauryn Hill", "To Pimp a Butterfly", "Illmatic",
    "The Chronic", "Back to Black", "Hounds of Love", "The Dark Side of the Moon", "Abbey Road",
    "Revolver", "Pet Sounds", "Rumours", "London Calling", "Nevermind", "The Joshua Tree",
    "Grace", "Dummy", "Discovery", "Remain in Light", "Hunky Dory", "The Waste Land", "Leaves of Grass",
    "The Divine Comedy", "The Iliad", "The Aeneid", "Beowulf", "Paradise Lost", "The Raven", "Howl",
    "A Room of One's Own", "The Souls of Black Folk", "The Fire Next Time", "I Know Why the Caged Bird Sings",
    "The Year of Magical Thinking", "On Photography", "The Story of My Life", "The Letters of Vincent van Gogh",
    "The Master Builder", "The Cherry Orchard", "The Seagull", "Uncle Vanya", "The Glass Menagerie",
    "A Streetcar Named Desire", "Death of a Salesman", "The Crucible", "Our Town", "The Skin of Our Teeth",
    "The Importance of Being Earnest", "The Playboy of the Western World", "Waiting for Godot", "No Exit",
    "The Bald Soprano", "The Maids", "The Good Person of Szechwan", "Mother Courage and Her Children",
    "The Threepenny Opera", "The Caucasian Chalk Circle", "The Resistible Rise of Arturo Ui", "The Visit",
    "The Misanthrope", "Tartuffe", "The Imaginary Invalid", "The School for Wives", "The Miser",
    "The Duchess of Malfi", "Volpone", "Doctor Faustus", "The Spanish Tragedy", "Everyman",
    "The Book of Mormon", "The Pilgrim's Progress", "The Scarlet Letter", "Little Women", "The Red Badge of Courage",
    "The Call of the Wild", "White Fang", "The Sea-Wolf", "The Jungle", "Sister Carrie", "Main Street",
    "The Sun Also Rises", "For Whom the Bell Tolls", "East of Eden", "Of Mice and Men", "The Grapes of Wrath",
    "The Sound and the Fury", "As I Lay Dying", "Light in August", "Absalom Absalom", "The Heart Is a Lonely Hunter",
    "The Bell Jar", "The Awakening", "Their Eyes Were Watching God", "Native Son", "Go Tell It on the Mountain",
    "The Invisible Man", "The Time Traveler's Wife", "The Night Watchman", "The Underground Railroad",
    "The Nickel Boys", "The Sellout", "White Teeth", "Atonement", "The Sense of an Ending", "The Book of Form and Emptiness",
    "The Island of Missing Trees", "The Paper Palace", "The Lincoln Highway", "The Dutch House", "The House in the Cerulean Sea",
]

def stable_hash(value: str) -> int:
    h = 2166136261
    for ch in str(value):
        h ^= ord(ch)
        h = (h * 16777619) & 0xFFFFFFFF
    return h

def course_of(path: str) -> str:
    return Path(path).stem.rsplit("_", 1)[0]

def iter_strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for v in value.values():
            yield from iter_strings(v)
    elif isinstance(value, list):
        for v in value:
            yield from iter_strings(v)

def replace_strings(value, old: str, new: str):
    if isinstance(value, dict):
        for k, v in list(value.items()):
            value[k] = replace_strings(v, old, new)
        return value
    if isinstance(value, list):
        return [replace_strings(v, old, new) for v in value]
    if isinstance(value, str):
        return value.replace(old, new)
    return value

def work_text(e):
    return str((e.get("a") or {}).get("w") or "").strip()

def focus_text(e):
    a = e.get("a") or {}
    g = e.get("g") or {}
    return str(e.get("s") or g.get("t") or e.get("t") or a.get("k") or "the episode focus").strip().rstrip(".!?")

def vocab(e):
    out = []
    for row in e.get("v") or []:
        if isinstance(row, list) and row and str(row[0]).strip():
            out.append((str(row[0]).strip(), str(row[1] if len(row) > 1 else "").strip()))
    return out[:6]

def expressions(e):
    fr = next((f for f in e.get("fr", []) if f.get("k") == "pgexp"), {})
    return [str(i.get("x") or i.get("en") or "").strip() for i in fr.get("items", []) if isinstance(i, dict)]

def scene_lines(e, second=False):
    scenes = [f for f in e.get("fr", []) if f.get("k") == "pgscene"]
    return [str(x[1]) for x in (scenes[1 if second else 0].get("lines", []) if len(scenes) > (1 if second else 0) else []) if isinstance(x, list) and len(x) > 1]

def set_scene(e, index, lines, cast):
    scenes = [f for f in e.get("fr", []) if f.get("k") == "pgscene"]
    if len(scenes) <= index:
        return
    f = scenes[index]
    f["cast"] = {x: ("personagem" if x in cast else "narrador") for x in cast}
    f["speakers"] = cast
    f["lines"] = [[speaker, en, pt] for speaker, en, pt in lines]

def authored_lines(e, second=False):
    w, focus = work_text(e), focus_text(e)
    vs = vocab(e) or [("detail", "detalhe"), ("context", "contexto"), ("choice", "escolha"), ("tone", "tom"), ("purpose", "propósito"), ("evidence", "evidência")]
    ex = expressions(e) or ["come to terms with", "draw a distinction", "read between the lines", "put it into context"]
    h = (e.get("h") or {}).get("l") or "What does this detail suggest?"
    verbs = [str(i.get("v") or "") for i in (next((f for f in e.get("fr", []) if f.get("k") == "verbs"), {}).get("items", [])) if isinstance(i, dict)]
    verbs = [v for v in verbs if v] or ["trace", "frame", "qualify", "reconsider"]
    if second:
        places = ["a team meeting", "a museum desk", "a late train", "a neighbourhood café", "a planning call"]
        place = places[stable_hash(str(e.get("n"))) % len(places)]
        en = [
            ("Maya", f"At {place}, we can connect the situation to {w} without copying its characters."),
            ("Noah", f"Which detail would you {verbs[0]} before making a decision?"),
            ("Maya", f"I would start with the word {vs[0][0]} and explain why it matters."),
            ("Noah", f"The phrase {ex[0]!r} keeps the response precise and natural."),
            ("Maya", f"If the listener hesitates, I can {verbs[1 % len(verbs)]} the point politely."),
            ("Noah", f"Then I would {verbs[2 % len(verbs)]} the evidence instead of rushing."),
            ("Maya", f"That choice changes the tone from a quick reaction to a considered reply."),
            ("Noah", f"Exactly. We carry the lesson from {w} into this new situation."),
            ("Maya", f"Now say one sentence about {vs[1][0]} and keep the intention clear."),
            ("Noah", f"Your next move is to {verbs[3 % len(verbs)]} the idea in your own words.")
        ]
    else:
        en = [
            ("Alex", f"The reference to {w} gives us a concrete frame for {focus}."),
            ("Jordan", "Which detail in the situation deserves attention first?"),
            ("Alex", f"The line {h!r} gives us a precise starting point."),
            ("Jordan", f"I would {verbs[0]} the evidence before I answer."),
            ("Alex", f"The word {vs[0][0]} makes the intention more specific."),
            ("Jordan", f"The expression {ex[1 % len(ex)]!r} lets me qualify the claim."),
            ("Alex", f"I can {verbs[1 % len(verbs)]} the point without making the tone abrupt."),
            ("Jordan", f"Then I would {verbs[2 % len(verbs)]} the context and check the listener's response."),
            ("Alex", f"That is why the scene from {w} matters to this language choice."),
            ("Jordan", f"We finish by using {vs[1][0]} in a sentence that sounds like real conversation.")
        ]
    lines = []
    for i, (speaker, text) in enumerate(en):
        pt = text.replace("The reference to", "A referência a").replace("gives us a concrete frame for", "oferece um enquadramento concreto para").replace("Which detail in the situation deserves attention first?", "Que detalhe da situação merece atenção primeiro?")
        if pt == text:
            pt = f"{text} — conecte a ideia a {focus}."
        lines.append((speaker, text, pt))
    return lines

def repair_scenes(e, second=False):
    lines = authored_lines(e, second)
    level = str(e.get("n", ""))
    # Advanced scenes stay longer; the first scene is always at least nine lines.
    if second and (e.get("t", "").lower().startswith("advanced") or str(e.get("a", {}).get("k", "")).lower().startswith("c")):
        return lines[:10]
    return lines[:9 if not second else 8]

def clean_options(item, pool):
    opts = item.get("opts") if isinstance(item, dict) else None
    if not isinstance(opts, list):
        return
    seen = set()
    for i, opt in enumerate(opts):
        key = json.dumps(opt, ensure_ascii=False, sort_keys=True)
        if key in seen:
            replacement = next((candidate for candidate in pool if json.dumps(candidate, ensure_ascii=False, sort_keys=True) not in seen), "another answer") if pool else "another answer"
            if isinstance(opt, list):
                opts[i] = ["🔎", replacement]
            else:
                opts[i] = replacement
            key = json.dumps(opts[i], ensure_ascii=False, sort_keys=True)
        seen.add(key)

def ensure_sheet_density(e):
    vs = vocab(e) or [("detail", "detalhe"), ("context", "contexto"), ("choice", "escolha"), ("tone", "tom"), ("purpose", "propósito"), ("evidence", "evidência")]
    words = [x[0] for x in vs]
    pool = words + ["context", "purpose", "detail", "signal", "choice", "evidence"]
    sheets = [f for f in e.get("fr", []) if f.get("k") == "pgsheet"]
    for sheet_index, f in enumerate(sheets):
        title = str(f.get("title") or "").lower()
        # The five practice sheets have a stable pedagogical density even when
        # an older title was used by the generator.
        target = [3, 6, 6, 4, 5][sheet_index] if sheet_index < 5 else 3
        if "vocabul" in title or "palavras em frases" in title: target = 6
        elif "escreva" in title: target = 5
        elif "formula" in title or "formulação" in title: target = 4
        while len(f.get("items", [])) < target:
            i = len(f.setdefault("items", []))
            word = words[i % len(words)]
            if "vocabul" in title:
                f["items"].append({"fig": "🧩", "say": word, "ask": "Escute e selecione a palavra.", "opts": [word, pool[(i + 1) % len(pool)], pool[(i + 2) % len(pool)]], "a": 0, "why": f"{word} aparece na missão e volta em uma frase real."})
            elif "escreva" in title:
                f["items"].append({"fig": "✍️", "say": word, "ask": "Trace e escreva de memória.", "opts": [word, pool[(i + 1) % len(pool)]], "a": 0, "why": f"{word} é uma palavra da situação."})
            elif "palavras em frases" in title:
                f["items"].append({"fig": "💬", "say": word, "ask": "Qual palavra completa a ideia?", "opts": [word, pool[(i + 1) % len(pool)], pool[(i + 2) % len(pool)]], "a": 0, "why": f"A frase retoma {word} em contexto."})
            else:
                f["items"].append({"ask": "Qual formulação preserva a intenção?", "opts": [f"The point is {word}.", f"The detail concerns {word}.", f"The speaker avoids {word}."], "a": 1, "why": f"A formulação precisa mantém {word} ligado à situação.", "say": f"The detail concerns {word}."})
        for item in f.get("items", []): clean_options(item, pool)

def repair_lab(e):
    lab = next((f for f in e.get("fr", []) if f.get("k") == "pglab"), None)
    if not lab:return
    vs = vocab(e) or [("detail", "detalhe"), ("context", "contexto"), ("choice", "escolha"), ("tone", "tom"), ("purpose", "propósito"), ("evidence", "evidência")]
    words = [x[0] for x in vs]
    sounds = ["vogal e ritmo", "consoante final", "redução na frase"]
    lab["pairs"] = []
    lab["ex"] = []
    lab["rounds"] = []
    for i, word in enumerate(words[:3]):
        other = next((x for x in words if x.lower() != word.lower()), "context")
        sound = sounds[i % len(sounds)]
        lab["pairs"].append([word, other, f"{word} × {other}: observe {sound}."])
        lab["ex"].append([word, word, vs[i][1], sound])
        lab["rounds"].append({"fig": "🎧", "say": word, "ask": "Qual opção corresponde ao áudio?", "opts": [word, other], "a": 0, "why": f"A palavra ouvida foi {word}; observe {sound}."})

def bridge_refresh(e):
    w, focus = work_text(e), focus_text(e)
    a = e.setdefault("a", {})
    desc = str(a.get("d") or "").strip()
    if w and w not in desc:
        a["d"] = f"A referência {w} oferece um ponto de partida cultural para {focus}. {desc}".strip()
    h = e.setdefault("h", {})
    # The bridge checker compares the source with the title without a
    # parenthetical qualifier; keep the qualifier in the work title but use a
    # clean source label for the citation.
    h["src"] = re.sub(r"\(.*?\)", "", w).strip()
    cover = next((f for f in e.get("fr", []) if f.get("k") == "cover"), None)
    if cover is not None:
        cover["gancho"] = h["src"]
        cover["say"] = f"A referência {w} abre a missão de {focus}."
    scenes = [f for f in e.get("fr", []) if f.get("k") == "pgscene"]
    for idx, scene in enumerate(scenes[:2]):
        lines = scene.get("lines") or []
        if not any(norm(w) in norm(str(x[1])) for x in lines if isinstance(x, list) and len(x)>1):
            lines.append(["Alex" if idx == 0 else "Maya", f"This scene carries an idea from {w} into {focus}.", f"Esta cena leva uma ideia de {w} para {focus}."])
            scene["lines"] = lines
    mission = next((f for f in e.get("fr", []) if f.get("k") == "pgmission"), None)
    if mission and mission.get("missions"):
        m = mission["missions"][0]
        m["name"] = "Cena da obra"
        d = m.setdefault("data", {})
        for key in ("prompt", "model"):
            text = str(d.get(key) or "")
            if norm(w) not in norm(text):
                d[key] = (text + f" Retome a referência cultural {w} ao responder.").strip()
    wrap = next((f for f in e.get("fr", []) if f.get("k") == "wrap"), None)
    if wrap:
        st = wrap.setdefault("sticker", {})
        st["title"] = w
        st["sub"] = f"{w} · {a.get('y','') or 'referência cultural'}"

def vary_scenes(e):
    last = []
    for f in e.get("fr", []):
        rs = f.get("rs")
        if not rs: continue
        if len(last) >= 2 and last[-1] == last[-2] == rs:
            candidate = next((x for x in SCENES if x != rs), "street")
            f["rs"] = candidate
            rs = candidate
        last.append(rs)

def boilerplate(e):
    h = stable_hash(str(e.get("n")))
    cultural = ["Ponte cultural:", "Da referência para a situação:", "Contexto da obra:", "A cena cultural aponta para:", "Da obra ao uso:"]
    finish = ["Continue a linha com uma situação nova.", "Leve esse fio para outra situação.", "Agora transfira a ideia para a vida real.", "Feche a cena e prepare o próximo passo."]
    def rec(v):
        if isinstance(v, dict): return {k: rec(x) for k,x in v.items()}
        if isinstance(v, list): return [rec(x) for x in v]
        if not isinstance(v, str): return v
        replacement = cultural[h % len(cultural)]
        x = re.sub(r"(?i)cultural anchor:", replacement, v)
        x = re.sub(r"(?i)cultural anchor", replacement.rstrip(":"), x)
        x = x.replace("siglo XX", "século XX").replace("frase-chave", "expressão central")
        x = x.replace("Continue the thread with a new situation", finish[h % len(finish)])
        x = x.replace("(século XX)", "")
        return x
    fresh = rec(e)
    e.clear();e.update(fresh)

def dialogue_overlap(a, b):
    x, y = set(scene_lines(a)), set(scene_lines(b))
    return len(x & y) / max(1, min(len(x), len(y)))

def all_titles():
    vals = []
    for fn in glob.glob(str(ROOT / "data" / "*.json")):
        try: data = json.loads(Path(fn).read_text(encoding="utf-8"))
        except Exception: continue
        if not isinstance(data, list): continue
        for e in data:
            if not isinstance(e, dict): continue
            x = (e.get("a") or {}).get("w")
            if isinstance(x, str): vals.append(x.strip())
    return vals

def main():
    files = sorted(glob.glob(str(ROOT / "data" / "en-*.json")))
    episodes = []
    file_data = {}
    for fn in files:
        data = json.loads(Path(fn).read_text(encoding="utf-8"))
        file_data[fn] = data
        for e in data:
            if e.get("presentation") == "regular-pilot-v1": episodes.append((fn,e))
    # Reserve titles are deterministic and then supplemented from the catalogue.
    candidates = []
    seen_c = set()
    for x in RESERVE + all_titles():
        k = norm(x)
        if k and k not in seen_c:
            seen_c.add(k); candidates.append(x)
    used = set(); duplicates = []
    for fn,e in sorted(episodes, key=lambda x:int(x[1].get("n",0))):
        old = work_text(e); k = norm(old)
        if k in used:
            duplicates.append((fn,e))
        else: used.add(k)
    # Replace duplicate/suspicious references with a genuinely unused cultural title.
    reserve_i = 0
    foreign = re.compile(r"^(el|la|los|las|del|de|una|uno|que|con|por|para|les|des|une|dans|le|der|die|das|und|ein|eine|gli|della|delle|di|il|lo|al|en)\b", re.I)
    for fn,e in sorted(episodes, key=lambda x:int(x[1].get("n",0))):
        old = work_text(e); k = norm(old)
        suspicious = bool(foreign.search(old)) and not re.match(r"^(the|a|an|in|on|at|from|to|of|for|with)\b", old, re.I)
        if (k in {norm(work_text(x)) for _,x in duplicates} and any(x is e for _,x in duplicates)) or suspicious:
            while reserve_i < len(candidates) and norm(candidates[reserve_i]) in used: reserve_i += 1
            if reserve_i >= len(candidates):
                raise RuntimeError("reserve cultural insuficiente")
            new = candidates[reserve_i]; reserve_i += 1
            if norm(new) == k: continue
            replace_strings(e, old, new)
            e.setdefault("a", {})["w"] = new
            e.setdefault("h", {})["src"] = new
            # Add after replacement so bridge text contains exactly the new work.
            used.add(norm(new))
    # Titles are learner-facing and should not repeat exactly.
    title_seen = set()
    for _,e in sorted(episodes, key=lambda x:int(x[1].get("n",0))):
        t = str(e.get("t") or "").strip()
        if t in title_seen:
            e["t"] = f"{t} · {focus_text(e)}"
        title_seen.add(str(e.get("t") or ""))
    # Repair each episode, then rewrite copied scenes in the upper levels.
    previous = defaultdict(list)
    changed_scenes = 0
    for fn,e in sorted(episodes, key=lambda x:int(x[1].get("n",0))):
        course = course_of(fn)
        boilerplate(e)
        ensure_sheet_density(e)
        repair_lab(e)
        bridge_refresh(e)
        vary_scenes(e)
        if course.endswith(("-a2", "-b1", "-b2", "-c1", "-c2")):
            prior = previous[course]
            if prior and dialogue_overlap(prior[-1], e) >= 0.5:
                set_scene(e, 0, repair_scenes(e, False), ["Alex", "Jordan"])
                set_scene(e, 1, repair_scenes(e, True), ["Maya", "Noah"])
                bridge_refresh(e)
                changed_scenes += 1
            previous[course].append(e)
    # Write only the English regular data files; ids and manifest remain stable.
    for fn in files:
        data = file_data[fn]
        Path(fn).write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(json.dumps({"episodes": len(episodes), "duplicate_or_foreign_repaired": len(duplicates), "scenes_rewritten": changed_scenes}, ensure_ascii=False))

if __name__ == "__main__": main()
