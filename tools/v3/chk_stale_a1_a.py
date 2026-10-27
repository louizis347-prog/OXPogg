#!/usr/bin/env python3
"""Procura, no texto de cada episódio reconstruído (módulos A1), o nome da obra antiga (obra_atual do alvo). Uso: COURSE=en-a1 python3 tools/v3/chk_stale_a1_a.py <a1_targets_a.json>"""
import sys, os, json, glob, importlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, HERE)
d = json.load(open(sys.argv[1], encoding='utf-8')); old = {t['n']: t['obra_atual'] for t in d['targets']}
bad = 0; seen = set()
for f in sorted(glob.glob(os.path.join(HERE, 'ep_*.py'))):
    m = importlib.import_module('v3.' + os.path.basename(f)[:-3])
    for e in m.EPS:
        n = e['n']
        if n not in old: continue
        seen.add(n)
        txt = json.dumps(e, ensure_ascii=False).lower()
        o = old[n].lower().replace('’', "'")
        if o in txt.replace('’', "'"): bad += 1; print('cita a obra antiga:', n, old[n], '(módulo %s)' % m.__name__)
print('episódios vistos:', len(seen), '| citações da obra antiga:', bad)
