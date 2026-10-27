#!/usr/bin/env python3
"""Confere as obras do lote C do A1 (zzc1_*): nenhuma em obras_em_uso, nenhuma repetida entre os alvos, nenhuma igual a obra de outro lote A1 (obras_new_a1_*.json)
nem de A2/B1 (aviso). Uso (da raiz): python3 tools/v3/chk_obras_zz_c.py <a1_targets_c.json>"""
import json, sys, re, unicodedata, glob, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
norm = lambda s: re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s.lower()).encode('ascii', 'ignore').decode())
d = json.load(open(sys.argv[1]))
use = {norm(x) for x in d['obras_em_uso']}
mine = json.load(open(os.path.join(HERE, 'obras_new_a1_zz_c.json'), encoding='utf-8'))
T = {str(t['n']) for t in d['targets']}
bad = 0
print('alvos:', len(T), 'obras no JSON:', len(mine))
for n in sorted(T - set(mine)): print('SEM OBRA', n); bad += 1
seen = {}
for n, w in mine.items():
    k = norm(w['name'])
    if n not in T: print('FORA DOS ALVOS', n); bad += 1
    if k in use: print('EM USO', n, w['name']); bad += 1
    if k in seen: print('REPETIDA entre alvos', n, seen[k], w['name']); bad += 1
    seen[k] = n
other = collections.defaultdict(list)
for f in glob.glob(os.path.join(HERE, 'obras_new_a1_*.json')):
    if f.endswith('obras_new_a1_zz_c.json'): continue
    for n, w in json.load(open(f, encoding='utf-8')).items():
        if isinstance(w, dict) and w.get('name'): other[norm(w['name'])].append((os.path.basename(f), n))
for k, n in seen.items():
    if k in other: print('COLIDE com outro lote A1', n, other[k]); bad += 1
warn = collections.defaultdict(list)
for f in glob.glob(os.path.join(HERE, 'obras_*.json')):
    b = os.path.basename(f)
    if b.startswith('obras_new_a1_'): continue
    for n, w in json.load(open(f, encoding='utf-8')).items():
        if isinstance(w, dict):
            nm = w.get('name') or (w.get('a') or {}).get('w') or w.get('work')
            if nm: warn[norm(nm)].append(b + ':' + n)
for k, n in seen.items():
    if k in warn: print('aviso (A2/B1/outros níveis):', n, mine[n]['name'], warn[k][:2])
print('problemas:', bad)
sys.exit(1 if bad else 0)
