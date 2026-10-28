#!/usr/bin/env python3
"""Confere B1 411-450 (cinema) em memória: contrato (19 quadros, 6/4/4, lab 3+3, cenas >=8, 3 missões), obra única e gs único.
Uso: COURSE=en-b1 python3 tools/v3/check_b1_411_450.py"""
import glob, importlib, json, os, re, sys, unicodedata
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, 'v3'))
import model_v2 as M
from v3 import lib
import model_v3 as MV
sys.path.insert(0, os.path.join(ROOT, 'tools', 'audit'))
from regular_pilot_contract import EXPECTED
nm = lambda s: re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower())
mods = ['b1_%d_%d' % (a, a + 4) for a in range(411, 450, 5)]
eps = []
for m in mods: eps += importlib.import_module('v3.' + m).EPS
chunks, where = {}, {}
for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'en-b1_*.json'))):
    d = json.load(open(f, encoding='utf-8')); chunks[f] = d
    for i, e in enumerate(d): where[e['n']] = (f, i)
order = sorted(where, key=lambda n: chunks[where[n][0]][where[n][1]]['o'])
eps.sort(key=lambda e: order.index(e['n']))
bad = []; built = []
for E in eps:
    f, i = where[E['n']]
    pf, pj = where[order[order.index(E['n']) - 1]]
    pit = chunks[pf][pj]
    prev = MV.prev_from_pilot(pit) if any(x['k'] == 'pgrule' for x in pit['fr']) else MV.prev_from_old(pit)
    M.HOTPT.update(lib.SAYPT)
    built.append(M.build(chunks[f][i], E['v2'], E['extra'], E['verbs'], prev, E['more']))
if len(built) != 40: bad.append('episódios: %d' % len(built))
for b in built:
    k = [x['k'] for x in b['fr']]; n = b['n']
    if k != EXPECTED: bad.append('%s quadros' % n)
    if len(b['v']) != 6: bad.append('%s vocab' % n)
    F = {}
    for x in b['fr']: F.setdefault(x['k'], []).append(x)
    if len(F['verbs'][0]['items']) != 4 or len(F['pgexp'][0]['items']) != 4: bad.append('%s verbos/exp' % n)
    if len(F['pglab'][0]['ex']) != 3 or len(F['pglab'][0]['rounds']) != 3: bad.append('%s lab' % n)
    sc = F['pgscene']
    if len(sc) != 2 or any(len(s['lines']) < 8 for s in sc): bad.append('%s cenas' % n)
    if len(F['pgmission'][0]['missions']) != 3: bad.append('%s missões' % n)
    if not (b.get('a') or {}).get('w'): bad.append('%s obra' % n)
    if F['review'][0].get('k') != 'review': bad.append('%s review' % n)
# obras
S = os.path.dirname(ROOT)
src = json.load(open('/tmp/claude-0/-home-user-OXPogg/aa240b69-cc21-5263-8573-be2969435207/scratchpad/b1new_2.json'))
em_uso = {nm(x) for x in src['obras_em_uso']}
mine = {}
for b in built: mine.setdefault(nm(b['a']['w']), []).append(b['n'])
for k, v in mine.items():
    if len(v) > 1: bad.append('obra repetida %s' % v)
    if k in em_uso: bad.append('obra em uso %s' % v)
mine_files = os.path.join(HERE, 'v3', 'obras_new_b1_411_450.json')
for f in glob.glob(os.path.join(HERE, 'v3', 'obras_new_b1_*.json')):
    if f == mine_files: continue
    for kk, v in json.load(open(f)).items():
        if nm(v['name']) in mine: bad.append('obra colide com %s: %s' % (os.path.basename(f), v['name']))
# gs: pattern entre os 40 e contra os 370 convertidos
used = set()
for f in glob.glob(os.path.join(ROOT, 'data', 'en-b1_*.json')):
    for x in json.load(open(f, encoding='utf-8')):
        if x.get('presentation') == 'regular-pilot-v1': used.add(x['gs'])
pats = [b['pattern'] for b in built]
if len(set(pats)) != 40: bad.append('patterns repetidos entre os 40')
for p in pats:
    if p in used: bad.append('gs já usado: ' + p)
print('episódios:', len(built), '| obras distintas:', len(mine), '| patterns distintos:', len(set(pats)))
print('PROBLEMAS:', len(bad)); [print(' -', x) for x in bad]
sys.exit(1 if bad else 0)
