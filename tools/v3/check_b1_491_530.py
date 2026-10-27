#!/usr/bin/env python3
"""Confere B1 491-530 em memória: contrato (19 quadros, 6 vocab, 4 verbos, 4 expressões, lab 3+3, cenas >=8, 3 missões),
obras únicas (vs obras_em_uso fixas, entre si e vs obras_new_b1_* de outros) e rótulos gs únicos (vs data/ e módulos b1_*).
Uso: COURSE=en-b1 python3 tools/v3/check_b1_491_530.py"""
import glob, importlib, json, os, re, sys, unicodedata
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, 'v3'))
os.environ.setdefault('COURSE', 'en-b1')
import model_v2 as M, model_v3 as MV
from v3 import lib
sys.path.insert(0, os.path.join(ROOT, 'tools', 'audit'))
from regular_pilot_contract import EXPECTED
norm = lambda s: re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower())
mods = sorted(os.path.basename(f)[:-3] for f in glob.glob(os.path.join(HERE, 'v3', 'b1_4[9]*.py')) + glob.glob(os.path.join(HERE, 'v3', 'b1_5[0-3]*.py')))
mods = [m for m in mods if re.match(r'b1_(49[1-9]|50\d|51\d|52\d|530)', m) or m in ('b1_491_495',)]
EPS = []
for m in sorted(set(mods)):
    EPS += importlib.import_module('v3.' + m).EPS
chunks, where = {}, {}
for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'en-b1_*.json'))):
    d = json.load(open(f, encoding='utf-8')); chunks[f] = d
    for i, e in enumerate(d): where[e['n']] = (f, i)
order = sorted(where, key=lambda n: chunks[where[n][0]][where[n][1]]['o'])
EPS.sort(key=lambda e: order.index(e['n']))
bad = []; works = {}; gss = {}
for k, E in enumerate(EPS):
    f, i = where[E['n']]; old = chunks[f][i]
    P = EPS[k - 1] if k else None
    if P and order.index(P['n']) == order.index(E['n']) - 1: prev = (P['v2'], P['extra'], P['verbs'])
    else:
        pf, pj = where[order[order.index(E['n']) - 1]]; pit = chunks[pf][pj]
        prev = MV.prev_from_pilot(pit) if any(x['k'] == 'pgrule' for x in pit['fr']) else MV.prev_from_old(pit)
    M.HOTPT.update(lib.SAYPT)
    b = M.build(old, E['v2'], E['extra'], E['verbs'], prev, E['more'])
    fr = b['fr']; kinds = [x['k'] for x in fr]; lab = next(x for x in fr if x['k'] == 'pglab')
    sc = [x for x in fr if x['k'] == 'pgscene']
    ok = (b.get('presentation', 'regular-pilot-v1') and kinds == EXPECTED and len(b['v']) == 6 and len(next(x for x in fr if x['k'] == 'verbs')['items']) == 4
          and len(next(x for x in fr if x['k'] == 'pgexp')['items']) == 4 and len(lab['ex']) == 3 and len(lab['rounds']) == 3
          and len(sc) == 2 and len(sc[0]['lines']) >= 8 and len(sc[1]['lines']) >= 8 and len(next(x for x in fr if x['k'] == 'pgmission')['missions']) == 3
          and fr[1]['k'] == 'review')
    if not ok: bad.append(('contrato', E['n']))
    works[E['n']] = b['a']['w']; gss[E['n']] = b['pattern']
print('episódios construídos:', len(EPS))
used = set(norm(x) for x in json.load(open(os.path.join(HERE, 'v3', 'obras_em_uso.json')))) if os.path.exists(os.path.join(HERE, 'v3', 'obras_em_uso.json')) else set()
# obras em uso: dados do B1 já convertidos + obras_new de outros arquivos
for f in glob.glob(os.path.join(ROOT, 'data', 'en-b1_*.json')):
    for x in json.load(open(f, encoding='utf-8')):
        if x.get('presentation') == 'regular-pilot-v1' and x['n'] not in works: used.add(norm(x['a']['w']))
mine = os.path.join(HERE, 'v3', 'obras_new_b1_491_530.json')
for f in glob.glob(os.path.join(HERE, 'v3', 'obras_new_b1_*.json')):
    if f == mine: continue
    for n, v in json.load(open(f, encoding='utf-8')).items():
        if int(n) not in works: used.add(norm(v['name']))
seen = {}
for n, w in works.items():
    if norm(w) in used: bad.append(('obra já em uso', n, w))
    if norm(w) in seen: bad.append(('obra repetida', n, w, seen[norm(w)]))
    seen[norm(w)] = n
usedgs = {}
for f in glob.glob(os.path.join(ROOT, 'data', 'en-b1_*.json')):
    for x in json.load(open(f, encoding='utf-8')):
        if x.get('gs') and x.get('presentation') == 'regular-pilot-v1' and x['n'] not in works: usedgs[x['gs']] = x['n']
for f in glob.glob(os.path.join(HERE, 'v3', 'b1_*.py')):
    b = os.path.basename(f)[:-3]
    if b in mods: continue
    try:
        for E in importlib.import_module('v3.' + b).EPS: usedgs.setdefault(E['v2']['base']['pattern_label'], E['n'])
    except Exception as ex: print('aviso: não importou', b, ex)
for n, g in gss.items():
    if g in usedgs: bad.append(('gs já usado', n, g, usedgs[g]))
if len(set(gss.values())) != len(gss): bad.append(('gs repetido entre os meus',))
print('obras distintas:', len(set(map(norm, works.values()))), '| gs distintos:', len(set(gss.values())))
print('PROBLEMAS:', bad if bad else 0)
