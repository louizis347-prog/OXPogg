#!/usr/bin/env python3
"""Confere os 40 episódios B1 371–410 (literatura) em memória: contrato do piloto, obra única, gs único e traduções coerentes.
Uso: COURSE=en-b1 python3 tools/v3/check_lit_371_410.py"""
import glob, importlib, json, os, re, sys, unicodedata
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, 'v3'))
import model_v2 as M
from v3 import lib
import model_v3 as MV
sys.path.insert(0, os.path.join(ROOT, 'tools', 'audit'))
from regular_pilot_contract import EXPECTED
COURSE = 'en-b1'
def norm(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '', s)
mods = sorted(os.path.basename(f)[:-3] for f in glob.glob(os.path.join(HERE, 'v3', 'b1_[34][0-9][0-9]_[34][0-9][0-9].py')) if 371 <= int(os.path.basename(f)[3:6]) <= 406)
eps = []
for m in mods: eps += importlib.import_module('v3.' + m).EPS
chunks, where = {}, {}
for f in sorted(glob.glob(os.path.join(ROOT, 'data', COURSE + '_*.json'))):
    d = json.load(open(f, encoding='utf-8')); chunks[f] = d
    for i, e in enumerate(d): where[e['n']] = (f, i)
order = sorted(where, key=lambda n: chunks[where[n][0]][where[n][1]]['o'])
prob = []; built = []
for k, E in enumerate(eps):
    f, i = where[E['n']]; old = chunks[f][i]
    P = eps[k - 1] if k else None
    if P and order.index(P['n']) == order.index(E['n']) - 1: prev = (P['v2'], P['extra'], P['verbs'])
    else:
        pf, pj = where[order[order.index(E['n']) - 1]]; pit = chunks[pf][pj]
        prev = MV.prev_from_pilot(pit) if any(x['k'] == 'pgrule' for x in pit['fr']) else MV.prev_from_old(pit)
    M.HOTPT.update(lib.SAYPT)
    b = M.build(old, E['v2'], E['extra'], E['verbs'], prev, E['more']); b['_gs'] = E['v2']['base']['pattern_label']; built.append(b)
print('episódios:', len(built), '| n distintos:', len({b['n'] for b in built}))
exp_n = [n for n in order if 82243 <= 0 or True]
pos = [order.index(b['n']) for b in built]; print('posições', min(pos) + 1, '-', max(pos) + 1, 'contíguas:', sorted(pos) == list(range(min(pos), max(pos) + 1)))
for b in built:
    F = b['fr']; kinds = [x['k'] for x in F]; n = b['n']
    if kinds != EXPECTED: prob.append((n, 'quadros'))
    if len(b.get('v') or []) != 6: prob.append((n, 'vocab'))
    sc = [x for x in F if x['k'] == 'pgscene']
    if len(sc) != 2 or len(sc[0]['lines']) < 8 or len(sc[1]['lines']) < 8: prob.append((n, 'cenas'))
    if F[1]['k'] != 'review': prob.append((n, 'mochila'))
    if len(next(x for x in F if x['k'] == 'verbs')['items']) != 4: prob.append((n, 'verbos'))
    if len(next(x for x in F if x['k'] == 'pgexp')['items']) != 4: prob.append((n, 'expressoes'))
    lab = next(x for x in F if x['k'] == 'pglab')
    if not (len(lab['ex']) == len(lab['pairs']) == len(lab['rounds']) == 3): prob.append((n, 'lab'))
    mis = next(x for x in F if x['k'] == 'pgmission')
    if len(mis['missions']) != 3: prob.append((n, 'missoes'))
    if len(next(x for x in F if x['k'] == 'hotscene')['hot']) != 5: prob.append((n, 'hot'))
    if b.get('presentation') not in (None, 'regular-pilot-v1'): prob.append((n, 'pres'))
    for l in sc[1]['lines'][:4]:
        if '**' not in l[1]: prob.append((n, 'expressao sem destaque na fala: ' + l[1]))
# obras
used = [str(x) for x in json.load(open('/tmp/claude-0/-home-user-OXPogg/aa240b69-cc21-5263-8573-be2969435207/scratchpad/b1new_1.json'))['obras_em_uso']]
usedn = {norm(u) for u in used}; usedn |= {norm(u.split(':')[0]) for u in used}
mine = json.load(open(os.path.join(HERE, 'v3', 'obras_new_b1_371_410.json'), encoding='utf-8'))
names = [mine[str(b['n'])]['name'] for b in built]
nn = [norm(x) for x in names]
print('obras:', len(names), 'distintas:', len(set(nn)))
for x in names:
    if ':' in x: prob.append((x, 'dois pontos no título'))
    if norm(x) in usedn: prob.append((x, 'obra já em uso'))
others = {}
for f in glob.glob(os.path.join(HERE, 'v3', 'obras_new_b1_*.json')):
    if f.endswith('obras_new_b1_371_410.json'): continue
    for k, v in json.load(open(f, encoding='utf-8')).items(): others.setdefault(norm(v['name']), []).append(os.path.basename(f))
    for k, v in json.load(open(f, encoding='utf-8')).items(): others.setdefault(norm(v['name'].split(':')[0]), []).append(os.path.basename(f))
for x in names:
    if norm(x) in others: prob.append((x, 'obra repetida em ' + ','.join(others[norm(x)])))
for b in built:
    if (b.get('a') or {}).get('w') != mine[str(b['n'])]['name']: prob.append((b['n'], 'obra construída diferente'))
# gs
gs_all = {}
for f in sorted(glob.glob(os.path.join(ROOT, 'data/en-b1_*.json'))):
    for x in json.load(open(f, encoding='utf-8')):
        if x.get('gs') and x.get('presentation') == 'regular-pilot-v1': gs_all.setdefault(x['gs'], []).append(x['n'])
for g in glob.glob(os.path.join(HERE, 'v3', 'b1_*.py')):
    bn = os.path.basename(g)[:-3]
    if bn in mods: continue
    if not re.match(r'b1_\d{3}_\d{3}$', bn): continue
mg = [b['_gs'] for b in built]
print('gs distintos:', len(set(mg)), 'de', len(mg))
for g in mg:
    if g in gs_all: prob.append((g, 'gs já usado em ' + str(gs_all[g])))
# vizinhança com o último convertido (370)
last = chunks[where[order[370 - 1]][0]][where[order[370 - 1]][1]]
def sets(e):
    F = {}
    for f in e['fr']: F.setdefault(f['k'], []).append(f)
    return ({w[0].lower() for w in e['v']}, {v['v'].lower() for v in F['verbs'][0]['items']}, {x[0].lower() for x in F['pglab'][0]['ex']})
a, b0 = sets(last), sets(built[0] if order.index(built[0]['n']) == 370 else built[0])
print('vizinho 370 ->', last['n'], 'repete:', [a[i] & b0[i] for i in range(3)])
# traduções coerentes entre os meus episódios
tr = {}
for b in built:
    for f in b['fr']:
        if f['k'] == 'pgscene':
            for l in f['lines']: tr.setdefault(l[1], set()).add(l[2])
for k, v in tr.items():
    if len(v) > 1: prob.append((k, 'traduções diferentes ' + str(v)))
print('PROBLEMAS:', len(prob))
for p in prob: print('  -', p)
