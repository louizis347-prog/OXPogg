#!/usr/bin/env python3
"""Grava tools/v3/obras_new_a1_zz_a.json (obras do lote A do A1). Rodar da raiz: python3 tools/v3/zz1_works.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, HERE)
from v3 import zz1_lib as Z
Z.load()
new = {}
for n in sorted(Z.SPECS):
    s = Z.SPECS[n]
    name, kind, text, theme, emojis = Z.work(s)
    new[str(n)] = dict(name=name, kind=kind, text=text, line=['', ''], pa=dict(t=theme, e=list(emojis), v=0))
json.dump(new, open(os.path.join(HERE, 'obras_new_a1_zz_a.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(new), 'obras')
