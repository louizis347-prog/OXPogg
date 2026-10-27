#!/usr/bin/env python3
"""Confere as obras do lote B do A1 (cinema): uso: python3 tools/v3/chk_obras_a1_b.py <pasta com a1_targets_b.json>
Prova: (1) nenhuma colide com obras_em_uso; (2) sem repetição entre si; (3) sem colisão com obras de outras camadas (JSON obras_*);
(4) nenhum texto montado cita a obra antiga do episódio."""
import json, sys, re, unicodedata, glob, os, importlib
sys.path.insert(0, 'tools'); sys.path.insert(0, 'tools/v3')
import v3.short as sh
d = json.load(open('%s/a1_targets_b.json' % sys.argv[1]))
norm = lambda s: re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s.lower()).encode('ascii', 'ignore').decode())
use = {norm(x) for x in d['obras_em_uso']}
T = {t['n']: t for t in d['targets']}
from v3 import zz_b_lib as Z
import v3.ova1_zz_b  # noqa
from v3 import ova2
bad = 0
mine = {}
for n in T:
    w = ova2.WORKS.get(str(n))
    if not w:
        print('SEM OBRA', n); bad += 1; continue
    k = norm(w['name'])
    if k in use: print('EM USO', n, w['name']); bad += 1
    if k in mine: print('REPETIDA', n, w['name'], mine[k]); bad += 1
    mine[k] = n
    if n not in Z.SPECS: print('SEM SPEC', n); bad += 1
# outras camadas (JSON de obras, exceto o meu)
others = {}
here = 'tools/v3'
for f in glob.glob(here + '/obras_*.json'):
    if f.endswith('obras_new_a1_zz_b.json'): continue
    for key, v in json.load(open(f)).items():
        if isinstance(v, dict) and 'name' in v and key not in {str(n) for n in T}:
            others.setdefault(norm(v['name']), []).append((os.path.basename(f), key))
for k, n in mine.items():
    if k in others:
        print('COLIDE (JSON de outra camada)', n, others[k][:3]); bad += 1
# texto montado não cita a obra antiga
orig = sh.E; rec = {}
def E(**k):
    r = orig(**k)
    if k['n'] in T: rec[k['n']] = r
    return r
sh.E = E
for f in sorted(glob.glob(here + '/ep_*.py')):
    try: importlib.import_module('v3.' + os.path.basename(f)[:-3])
    except Exception as e: print('ERRO', f, e)
for n, r in rec.items():
    old = T[n]['obra_atual']
    txt = json.dumps(r, ensure_ascii=False, default=str)
    if re.search(r'(?<![\w])' + re.escape(old) + r'(?![\w])', txt):  # sensível a maiúsculas: evita falso positivo (Rain / rain)
        print('CITA OBRA ANTIGA', n, old); bad += 1
print('alvos:', len(T), 'com obra nova:', len(mine), 'texto montado:', len(rec), 'problemas:', bad)
