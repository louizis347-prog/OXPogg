#!/usr/bin/env python3
"""Diversifica a aprendiz do Painel: troca o nome "Mia" (que aparece em quase todas as aulas) por um nome
sorteado, fixo por aula, de um conjunto de personagens com aparência própria (pele, cabelo, penteado, roupa).
- Troca o nome em TODO o texto da aula (falas, vocativos, capa, roteiro) e no currículo, sem tocar em "Mamma Mia".
- Aulas em que o texto trata a aprendiz por "ela"/"she" só recebem nomes femininos.
- Os nomes novos entram em data/elenco.json (aparência) e a escolha fica registrada em data/learner_names.json,
  então rodar de novo mantém tudo igual (idempotente) e aulas novas com "Mia" recebem um nome ainda não usado ali.
IMPORTANTE: rodar DEPOIS de build/enrich/validate_x|y|z e de apply_live.py (os validadores reconstroem a aula e devolvem "Mia").
Uso: python3 tools/diversify_learner.py [N ...]   (sem argumentos: todas as aulas)"""
import glob, json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
D = os.path.join(ROOT, 'data'); V4 = os.path.join(D, 'v4')
REG = os.path.join(D, 'learner_names.json')

# nome, gênero, país, pele, cabelo, penteado, vestido?, cor da roupa
POOL = [
 ('Amara','f','Nigeria','dark','black','braids',0,'#e8a33d'),('Priya','f','India','brown','black','long',0,'#d9708f'),
 ('Sofia','f','Argentina','light','brown','curly',1,'#4a90d9'),('Leila','f','Morocco','tan','black','bun',0,'#2f9d63'),
 ('Chloe','f','Canada','pale','blond','ponytail',0,'#6b7fd6'),('Nia','f','Kenya','deep','black','afro',1,'#e0584a'),
 ('Camila','f','Colombia','tan','brown','long',1,'#d94f6a'),('Aisha','f','Egypt','tan','black','long',0,'#3a8f9c'),
 ('Hannah','f','Germany','pale','blond','bob',0,'#c58a2f'),('Zara','f','Pakistan','brown','black','bun',1,'#7a5fa8'),
 ('Isabel','f','Spain','light','brown','side',0,'#b5543c'),('Fatima','f','Turkey','tan','brown','bun',0,'#2f7f86'),
 ('Elsa','f','Sweden','pale','blond','braids',1,'#4d8f6b'),('Rina','f','Japan','light','black','bob',0,'#d94f6a'),
 ('Tamara','f','Georgia','light','brown','long',0,'#8a4f7d'),('Bianca','f','Italy','light','black','curly',1,'#e0584a'),
 ('Dalia','f','Lebanon','tan','black','long',0,'#3b6ea5'),('Esther','f','Ghana','dark','black','curly',0,'#c9702f'),
 ('Freya','f','Norway','pale','blond','long',0,'#2f9d63'),('Gita','f','Nepal','brown','black','ponytail',0,'#a8445a'),
 ('Imani','f','USA','deep','black','afro',0,'#e8a33d'),('Keisha','f','Jamaica','dark','black','braids',1,'#6b7fd6'),
 ('Lina','f','Syria','tan','brown','bun',0,'#5b8f3a'),('Marta','f','Poland','pale','brown','bob',0,'#4a5a8a'),
 ('Noor','f','Jordan','tan','black','long',1,'#2f7f86'),('Olivia','f','Australia','pale','brown','ponytail',0,'#d9708f'),
 ('Paloma','f','Mexico','brown','black','long',1,'#e8a33d'),('Selma','f','Bosnia','light','brown','side',0,'#7a5fa8'),
 ('Thais','f','Brazil','tan','black','curly',0,'#2f9d63'),('Uma','f','India','brown','black','long',1,'#c58a2f'),
 ('Vera','f','Russia','pale','blond','bob',0,'#3a8f9c'),('Wanda','f','Poland','light','blond','curly',1,'#b5543c'),
 ('Ximena','f','Mexico','tan','black','ponytail',0,'#4d8f6b'),('Yara','f','Brazil','brown','black','curly',0,'#e0584a'),
 ('Zainab','f','Somalia','dark','black','bun',1,'#6b7fd6'),('Ingrid','f','Denmark','pale','blond','braids',0,'#2f9d63'),
 ('Mina','f','Korea','light','black','side',0,'#d94f6a'),('Carmen','f','Spain','tan','black','bun',1,'#a8445a'),
 ('Tara','f','Ireland','pale','brown','curly',0,'#4a90d9'),('Sade','f','Nigeria','deep','black','braids',1,'#e8a33d'),
 ('Lucas','m','Brazil','tan','brown','side',0,'#3b6ea5'),('Kenji','m','Japan','light','black','side',0,'#e0584a'),
 ('Andre','m','Haiti','dark','black','curly',0,'#2f9d63'),('Mateo','m','Spain','light','brown','curly',0,'#c58a2f'),
 ('Samir','m','Lebanon','tan','black','side',0,'#4a5a8a'),('Noah','m','USA','pale','blond','side',0,'#6b7fd6'),
 ('Ravi','m','India','brown','black','side',0,'#e8a33d'),('Tomas','m','Czechia','pale','brown','side',0,'#8a4f7d'),
 ('Victor','m','Romania','light','black','side',0,'#2f7f86'),('Wei','m','China','light','black','side',0,'#d94f6a'),
 ('Yusuf','m','Turkey','tan','black','curly',0,'#b5543c'),('Zane','m','Canada','pale','blond','spiky',0,'#4d8f6b'),
 ('Amir','m','Iran','tan','black','side',0,'#c9702f'),('Bruno','m','Portugal','light','brown','side',0,'#3a8f9c'),
 ('Chen','m','China','light','black','side',0,'#e0584a'),('Dario','m','Italy','light','black','curly',0,'#5b8f3a'),
 ('Emeka','m','Nigeria','deep','black','afro',0,'#e8a33d'),('Felipe','m','Chile','tan','brown','side',0,'#4a90d9'),
 ('Gael','m','Mexico','brown','black','curly',0,'#7a5fa8'),('Hiro','m','Japan','light','black','spiky',0,'#2f9d63'),
 ('Idris','m','Sudan','dark','black','afro',0,'#d9708f'),('Jonas','m','Germany','pale','blond','side',0,'#3b6ea5'),
 ('Kwame','m','Ghana','deep','black','afro',0,'#c58a2f'),('Luca','m','Italy','light','brown','side',0,'#e0584a'),
 ('Mohamed','m','Egypt','tan','black','side',0,'#2f7f86'),('Nico','m','Greece','light','brown','curly',0,'#6b7fd6'),
 ('Oscar','m','Peru','tan','black','side',0,'#a8445a'),('Pedro','m','Portugal','tan','brown','side',0,'#4d8f6b'),
 ('Mia','f','Brazil','brown','black','pigtails',1,'#4a90d9'),
]
BAD = re.compile(r'(?<!Mamma )\bMia\b')
FEM = re.compile(r"\b(she|her|hers|herself|ela|dela|nela|girl|a menina)\b", re.I)

def walk(x, out):
    if isinstance(x, str): out.append(x)
    elif isinstance(x, list):
        for i in x: walk(i, out)
    elif isinstance(x, dict):
        for v in x.values(): walk(v, out)

def hsh(s):
    x = 2166136261
    for ch in str(s): x = ((x ^ ord(ch)) * 16777619) & 0xFFFFFFFF
    return x

def ensure_elenco():
    p = os.path.join(D, 'elenco.json'); el = json.load(open(p, encoding='utf-8')); have = {e['name'] for e in el}; add = 0
    for n, g, c, sk, hr, hs, dr, top in POOL:
        if n in have:
            for e in el:
                if e['name'] == n and 'g' not in e: e['g'] = g
            continue
        el.append({'name': n, 'g': g, 'country': c, 'job': 'student', 'look': {'hs': hs, 'outfit': 'dress' if dr else 'shirt', 'top': top, 'hair': hr, 'skin': sk}}); add += 1
    for e in el:
        if e['name'] == 'Mia' and 'g' not in e: e['g'] = 'f'
    json.dump(el, open(p, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    return add

def main(ns):
    added = ensure_elenco()
    reg = json.load(open(REG)) if os.path.exists(REG) else {}
    files = sorted(glob.glob(os.path.join(V4, '[0-9]*.json'))); changed = 0; femg = 0
    for f in files:
        n = int(re.search(r'(\d+)\.json$', f).group(1))
        if ns and n not in ns: continue
        raw = open(f, encoding='utf-8').read()
        if not BAD.search(raw): continue
        d = json.loads(raw); ss = []; walk(d, ss)
        near = [s for s in ss if re.search(r'\bMia\b', s)]
        fem = any(FEM.search(s) for s in near)
        key = str(n)
        name = reg.get(key)
        if not name:
            cands = [p for p in POOL if (p[1] == 'f' or not fem)]
            start = hsh('lesson%s' % n) % len(cands)
            for k in range(len(cands)):
                p = cands[(start + k) % len(cands)]
                if not re.search(r'\b%s\b' % re.escape(p[0]), raw): name = p[0]; break
            reg[key] = name
        if fem: femg += 1
        new = BAD.sub(name, raw)
        open(f, 'w', encoding='utf-8').write(new); changed += 1
    cp = os.path.join(V4, 'curriculum.json'); cur = json.load(open(cp, encoding='utf-8'))
    for x in cur:
        nm = reg.get(str(x['n']))
        if nm and 'cast' in x: x['cast'] = [nm if c == 'Mia' else c for c in x['cast']]
    json.dump(cur, open(cp, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    json.dump(reg, open(REG, 'w', encoding='utf-8'), ensure_ascii=False, indent=0, sort_keys=True)
    print('nomes novos no elenco:', added, '| aulas alteradas:', changed, '| aulas com aprendiz feminina:', femg)

if __name__ == '__main__':
    main({int(a) for a in sys.argv[1:]})
