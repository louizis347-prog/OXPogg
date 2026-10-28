#!/usr/bin/env python3
"""Troca a segunda ocorrência de cada obra repetida (normalização forte) do
inglês regular por uma obra real ainda não usada em nenhum curso.
Uso: fix_dup_works.py [--check]"""
import glob, json, re, sys, unicodedata
from collections import defaultdict
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]

def norm(s):
    s = unicodedata.normalize('NFKD', (s or '').split(':')[0].lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'\(.*?\)', '', s); s = re.sub(r'[^a-z0-9 ]', ' ', s)
    s = re.sub(r'^(the|a|an|el|la|le|o|os)\s+', '', s.strip())
    return ' '.join(s.split())

# (titulo, tipo, ano) — obras reais, título em inglês
POOL = [("The Remains of the Day","Livro","1989"),("Brooklyn","Filme","2015"),("The Secret Garden","Livro","1911"),
("Rear Window","Filme","1954"),("Moby-Dick","Livro","1851"),("The Great Gatsby","Livro","1925"),("Casablanca","Filme","1942"),
("Bohemian Rhapsody","Canção","1975"),("Hamlet","Peça","1603"),("Pride and Prejudice","Livro","1813"),("The Starry Night","Pintura","1889"),
("Abbey Road","Álbum","1969"),("Frankenstein","Livro","1818"),("Sherlock","Série","2010"),
("The Wind in the Willows","Livro","1908"),("Jane Eyre","Livro","1847"),("Great Expectations","Livro","1861"),("Notting Hill","Filme","1999"),
("The Crown","Série","2016"),("Wuthering Heights","Livro","1847"),("Dracula","Livro","1897"),
("Mary Poppins","Filme","1964"),("Matilda","Livro","1988"),("The Hobbit","Livro","1937"),("Little Women","Livro","1868"),
("To Kill a Mockingbird","Livro","1960"),("Gulliver's Travels","Livro","1726"),("The Picture of Dorian Gray","Livro","1890"),
("Four Weddings and a Funeral","Filme","1994"),("Billy Elliot","Filme","2000"),("The Full Monty","Filme","1997"),("Downton Abbey","Série","2010"),
("Peaky Blinders","Série","2013"),("A Christmas Carol","Livro","1843"),("Oliver Twist","Livro","1838"),("Robin Hood","Lenda","séc. XIV"),
("Treasure Island","Livro","1883"),("Alice's Adventures in Wonderland","Livro","1865"),
("The Go-Between","Livro","1953"),("Atonement","Livro","2001"),("Educating Rita","Filme","1983"),("Chariots of Fire","Filme","1981"),
("Local Hero","Filme","1983"),("The Italian Job","Filme","1969"),("Withnail and I","Filme","1987"),("Kes","Filme","1969"),("Trainspotting","Filme","1996"),
("The King's Speech","Filme","2010"),("Skyfall","Filme","2012"),("The Prestige","Filme","2006"),("Gosford Park","Filme","2001"),("Howards End","Livro","1910"),
("A Room with a View","Livro","1908"),("The Thirty-Nine Steps","Livro","1915"),("Rebecca","Livro","1938"),("Brideshead Revisited","Livro","1945"),
("Lord of the Flies","Livro","1954"),("Animal Farm","Livro","1945"),("Nineteen Eighty-Four","Livro","1949"),("Brave New World","Livro","1932"),
("The Catcher in the Rye","Livro","1951"),("Of Mice and Men","Livro","1937"),("The Grapes of Wrath","Livro","1939"),("Their Eyes Were Watching God","Livro","1937"),
("Beloved","Livro","1987"),("The Color Purple","Livro","1982"),("Middlemarch","Livro","1871"),("Tess of the d'Urbervilles","Livro","1891"),
("Vanity Fair","Livro","1848"),("David Copperfield","Livro","1850"),("Persuasion","Livro","1817"),("Northanger Abbey","Livro","1817"),
("Heart of Darkness","Livro","1899"),("The Importance of Being Earnest","Peça","1895"),("Pygmalion","Peça","1913"),("Macbeth","Peça","1606"),
("The Tempest","Peça","1611"),("Twelfth Night","Peça","1602"),("Romeo and Juliet","Peça","1597"),("Waiting for Godot","Peça","1953"),
("Death of a Salesman","Peça","1949"),("A Streetcar Named Desire","Peça","1947"),("Our Town","Peça","1938"),("Fawlty Towers","Série","1975"),
("Black Books","Série","2000"),("The Office","Série","2001"),("Friday Night Lights","Série","2006"),("Cheers","Série","1982"),("Frasier","Série","1993"),
("Parks and Recreation","Série","2009"),("Ted Lasso","Série","2020"),("Blackadder","Série","1983"),("Yes Minister","Série","1980"),("Hey Jude","Canção","1968"),
("Imagine","Canção","1971"),("Yesterday","Canção","1965"),("Wonderwall","Canção","1995"),("Respect","Canção","1967"),("Hallelujah","Canção","1984"),
("Mr. Brightside","Canção","2003"),("Rolling in the Deep","Canção","2010"),("Blackbird","Canção","1968"),("Penny Lane","Canção","1967"),
("American Gothic","Pintura","1930"),("Nighthawks","Pintura","1942"),("The Hay Wain","Pintura","1821"),("The Fighting Temeraire","Pintura","1839"),
("Whistler's Mother","Pintura","1871"),("The Physical Impossibility of Death in the Mind of Someone Living","Obra de arte","1991"),
("Where the Wild Things Are","Livro","1963"),("The Gruffalo","Livro","1999"),("The Very Hungry Caterpillar","Livro","1969"),("Charlotte's Web","Livro","1952"),
("The Tale of Peter Rabbit","Livro","1902"),("Winnie-the-Pooh","Livro","1926"),("The Lion, the Witch and the Wardrobe","Livro","1950"),
("Charlie and the Chocolate Factory","Livro","1964"),("Anne of Green Gables","Livro","1908"),("Black Beauty","Livro","1877"),("Heidi","Livro","1881"),
("The Railway Children","Livro","1906"),("Swallows and Amazons","Livro","1930"),("Watership Down","Livro","1972"),("The BFG","Livro","1982"),
("Harry Potter and the Philosopher's Stone","Livro","1997"),("Bridget Jones's Diary","Livro","1996"),("Four Quartets","Poema","1943"),
("The Waste Land","Poema","1922"),("Ozymandias","Poema","1818"),("Daffodils","Poema","1807"),("Ode to a Nightingale","Poema","1819"),
("Still I Rise","Poema","1978"),("The Road Not Taken","Poema","1916"),("Casino Royale","Livro","1953"),("Murder on the Orient Express","Livro","1934"),
("The Hound of the Baskervilles","Livro","1902"),("Cranford","Livro","1853"),("North and South","Livro","1855"),
("The Snow Goose","Livro","1941"),("Kidnapped","Livro","1886"),("The Time Machine","Livro","1895"),("The War of the Worlds","Livro","1898"),
("Mrs Dalloway","Livro","1925"),("To the Lighthouse","Livro","1927"),("Orlando","Livro","1928"),("The Handmaid's Tale","Livro","1985"),
("Never Let Me Go","Livro","2005"),("Wolf Hall","Livro","2009"),("Life of Pi","Livro","2001"),("The Kite Runner","Livro","2003"),
("Slumdog Millionaire","Filme","2008"),("The Snowman","Filme","1982"),("Love Actually","Filme","2003"),("Shaun of the Dead","Filme","2004"),
("Wallace & Gromit: The Wrong Trousers","Filme","1993"),("Shaun the Sheep","Série","2007"),("Doctor Who","Série","1963"),("Midsomer Murders","Série","1997"),
("The Vicar of Dibley","Série","1994"),("Only Fools and Horses","Série","1981"),("Strictly Come Dancing","Série","2004"),("The Great British Bake Off","Série","2010")]

def strs(v):
    if isinstance(v, str): yield v
    elif isinstance(v, dict):
        for x in v.values(): yield from strs(x)
    elif isinstance(v, list):
        for x in v: yield from strs(x)

def rep(v, old, new):
    if isinstance(v, dict): return {k: rep(x, old, new) for k, x in v.items()}
    if isinstance(v, list): return [rep(x, old, new) for x in v]
    return v.replace(old, new) if isinstance(v, str) else v

files = sorted(glob.glob(str(ROOT/'data'/'en-*_*.json')))
data = {f: json.loads(Path(f).read_text(encoding='utf-8')) for f in files}
used = set()
for fn in glob.glob(str(ROOT/'data'/'*.json')):
    try: d = json.loads(Path(fn).read_text(encoding='utf-8'))
    except Exception: continue
    if isinstance(d, list):
        for e in d:
            if isinstance(e, dict) and isinstance(e.get('a'), dict): used.add(norm(e['a'].get('w', '')))
seen = defaultdict(list)
for f in files:
    for e in data[f]: seen[norm(e['a']['w'])].append((f, e))
free = [p for p in POOL if norm(p[0]) not in used]
BLOCK = {'peter and wendy', 'paddington 2', 'paddington in peru'}  # mesma obra/franquia de outro episódio
dups = [v[1:] for v in seen.values() if len(v) > 1] + [v for k, v in seen.items() if k in BLOCK]
todo = [x for v in dups for x in v]
print('duplicatas:', len(todo), '| reserva livre:', len(free))
if '--check' in sys.argv: sys.exit(1 if todo else 0)
assert len(free) >= len(todo), 'reserva insuficiente'
for (f, e), (nt, nk, ny) in zip(todo, free):
    old = e['a']['w']; oy = e['a'].get('y', '')
    new = rep(e, f"{old} ({oy})", f"{nt} ({ny})")
    new = rep(new, old, nt); new = rep(new, old.split(' (')[0], nt)
    new['a']['w'] = nt; new['a']['y'] = ny; new['a']['k'] = nk; new['h']['src'] = nt
    e.clear(); e.update(new)
    print(f"  {Path(f).name} #{e['n']}: {old} -> {nt}")
for f in files: Path(f).write_text(json.dumps(data[f], ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
