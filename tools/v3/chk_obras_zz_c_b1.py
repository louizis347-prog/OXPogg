#!/usr/bin/env python3
"""Confere as obras do lote C do B1: nenhuma em obras_em_uso, nenhuma repetida entre os alvos, nenhuma igual a obra de outros lotes (obras_new_*.json, obras_old*.json).
Uso (da raiz): python3 tools/v3/chk_obras_zz_c_b1.py <b1_targets_c.json>"""
import json, sys, re, unicodedata, glob, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
norm = lambda s: re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s.lower()).encode('ascii', 'ignore').decode())
d = json.load(open(sys.argv[1]))
use = {norm(x) for x in d['obras_em_uso']}
mine = json.load(open(os.path.join(HERE, 'obras_new_b1_zz_c.json'), encoding='utf-8'))
T = {str(t['n']) for t in d['targets']}
bad = 0
print('alvos:', len(T), 'obras no JSON:', len(mine))
for n in sorted(T - set(mine), key=int): print('SEM OBRA', n)
seen = {}
for n, w in mine.items():
    k = norm(w['name'])
    if n not in T: print('FORA DOS ALVOS', n); bad += 1
    if k in use: print('EM USO', n, w['name']); bad += 1
    if k in seen: print('REPETIDA entre alvos', n, seen[k], w['name']); bad += 1
    seen[k] = n
    if ':' in w['name']: print('DOIS PONTOS', n, w['name']); bad += 1
other = collections.defaultdict(list)
for f in glob.glob(os.path.join(HERE, 'obras_*.json')):
    b = os.path.basename(f)
    if b == 'obras_new_b1_zz_c.json': continue
    for n, w in json.load(open(f, encoding='utf-8')).items():
        if isinstance(w, dict):
            nm = w.get('name') or (w.get('a') or {}).get('w') or w.get('work')
            if nm: other[norm(nm)].append(b + ':' + n)
for k, n in seen.items():
    if k in other: print('COLIDE com outra camada', n, mine[n]['name'], other[k][:3]); bad += 1
print('problemas:', bad)
sys.exit(1 if bad else 0)
