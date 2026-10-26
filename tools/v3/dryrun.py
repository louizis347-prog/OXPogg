#!/usr/bin/env python3
"""Monta em memória (SEM gravar nada) os episódios de um arquivo tools/v3/b1_*.py e roda as checagens do modelo piloto.
Uso (da raiz do repositório): COURSE=en-b1 python3 tools/v3/dryrun.py b1_331_340"""
import glob, importlib, json, os, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, 'v3'))
import model_v2 as M
from v3 import lib
import model_v3 as MV
from v3.check import check
COURSE = os.environ.get('COURSE', 'en-b1')
mod = importlib.import_module('v3.' + sys.argv[1])
chunks, where = {}, {}
for f in sorted(glob.glob(os.path.join(ROOT, 'data', COURSE + '_*.json'))):
    d = json.load(open(f, encoding='utf-8')); chunks[f] = d
    for i, e in enumerate(d): where[e['n']] = (f, i)
order = sorted(where, key=lambda n: chunks[where[n][0]][where[n][1]]['o'])
eps = sorted(mod.EPS, key=lambda e: order.index(e['n']))
bad = 0; gs = []; built_all = []
for k, E in enumerate(eps):
    f, i = where[E['n']]; old = chunks[f][i]
    P = eps[k - 1] if k else None
    if P and order.index(P['n']) == order.index(E['n']) - 1:
        prev = (P['v2'], P['extra'], P['verbs'])
    else:
        pf, pj = where[order[order.index(E['n']) - 1]]; pit = chunks[pf][pj]
        prev = MV.prev_from_pilot(pit) if any(x['k'] == 'pgrule' for x in pit['fr']) else MV.prev_from_old(pit)
    M.HOTPT.update(lib.SAYPT)
    built = M.build(old, E['v2'], E['extra'], E['verbs'], prev, E['more'])
    pr = check(built)
    print(('OK ' if not pr else 'XX '), E['n'], built['t'], len(built['fr']), 'quadros', '| gs:', built.get('gs'))
    for q in pr: print('    -', q)
    bad += len(pr); gs.append(built.get('gs')); built_all.append(built)
print('problemas:', bad, '| rótulos gs:', len(gs), 'únicos:', len(set(gs)))

# --- cada episódio tem conteúdo próprio: palavras, verbos, laboratório de sons e obra não podem repetir entre episódios vizinhos ---
def _sets(e):
    F = {}
    for f in e['fr']: F.setdefault(f['k'], []).append(f)
    return dict(vocab={w[0].lower() for w in (e.get('v') or [])}, verbos={v['v'].lower() for v in F.get('verbs', [{}])[0].get('items', [])},
                lab={x[0].lower() for x in F.get('pglab', [{}])[0].get('ex', [])}, obra={(e.get('a') or {}).get('w', '')})
rep = 0
for a, b in zip(built_all, built_all[1:]):
    A, B = _sets(a), _sets(b)
    for k in A:
        com = A[k] & B[k]
        if com:
            rep += 1; print('REPETIDO entre', a['n'], 'e', b['n'], k, sorted(com))
print('repetições entre episódios vizinhos:', rep)
