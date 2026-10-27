#!/usr/bin/env python3
"""Confere que as obras de tools/v3/ova2b_241_zz_b.py não colidem com obras_em_uso (arquivo JSON do escopo) nem entre si.
Uso: python3 tools/v3/chk_zz_b_obras.py <a2_targets_b.json>"""
import json, re, sys, unicodedata, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v3 import ova2b
import importlib
importlib.import_module('v3.ova2b_241_zz_b')
norm = lambda s: re.sub(r"[^a-z0-9]", "", unicodedata.normalize('NFD', s.lower()).encode('ascii', 'ignore').decode())
d = json.load(open(sys.argv[1], encoding='utf-8'))
alvos = {t['n'] for t in d['targets']}
uso = {norm(x) for x in d['obras_em_uso']}
mine = {n: ova2b.OVR[n]['ob']['name'] for n in alvos}
falt = [n for n in alvos if n not in ova2b.OVR or n not in ova2b.GX]
cont = {}
bad = 0
for n, nm in mine.items():
    cont.setdefault(norm(nm), []).append(n)
    if norm(nm) in uso: bad += 1; print('COLIDE com obras_em_uso:', n, nm)
for k, v in cont.items():
    if len(v) > 1: bad += 1; print('REPETIDA entre alvos:', v)
for n in falt: bad += 1; print('SEM override completo:', n)
print('alvos:', len(alvos), '| obras distintas:', len(cont), '| problemas:', bad)
