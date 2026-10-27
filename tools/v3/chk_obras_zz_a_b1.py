#!/usr/bin/env python3
"""Colisões de obra do lote B1 ZZ-A (36 episódios). Uso: python3 tools/v3/chk_obras_zz_a_b1.py <targets.json>"""
import json, glob, os, re, sys, unicodedata
H = os.path.dirname(os.path.abspath(__file__))
def N(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9 ]", "", s.replace("'", "").replace("’", "")); return re.sub(r'^the ', '', re.sub(r'\s+', ' ', s).strip())
mine = json.load(open(os.path.join(H, 'obras_new_b1_zz_a.json')))
d = json.load(open(sys.argv[1])); uso = {N(x) for x in d['obras_em_uso']}
tg = {str(t['n']) for t in d['targets']}
bad = 0
names = {k: N(v['name']) for k, v in mine.items()}
assert set(names) == tg, set(names) ^ tg
if len(set(names.values())) != len(names): print('REPETIDA entre alvos'); bad += 1
for k, nm in names.items():
    if nm in uso: print('em uso', k, mine[k]['name']); bad += 1
for f in glob.glob(os.path.join(H, 'obras_new_*.json')):
    if f.endswith('obras_new_b1_zz_a.json'): continue
    for k, v in json.load(open(f)).items():
        if N(v['name']) in names.values() and not (f.endswith(('_zz_c.json','_zz_b.json')) and False):
            print('colide', os.path.basename(f), k, v['name']); bad += 1
for k, v in mine.items():
    if ':' in v['name']: print('dois-pontos', k); bad += 1
for f in glob.glob(os.path.join(H, '..', '..', 'data', 'en-b1_*.json')):
    for e in json.load(open(f, encoding='utf-8')):
        m = re.search(r'"sticker": ?\{[^}]*?"sub": "([^"]*?) · ', json.dumps(e, ensure_ascii=False))
        if m and N(m.group(1)) in names.values() and str(e['n']) not in mine:
            print('colide data', e['n'], m.group(1)); bad += 1
print('alvos', len(mine), 'problemas', bad)
