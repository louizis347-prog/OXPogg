#!/usr/bin/env python3
"""Grava as obras novas das camadas ova2_*.py em tools/v3/obras_new_a2_001_240_<faixa>.json (uma por arquivo ova2_<faixa>.py). Rodar da raiz."""
import glob, importlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, HERE)
from v3 import ova2
for f in sorted(glob.glob(os.path.join(HERE, 'ova2_*.py'))):
    name = os.path.basename(f)[:-3]
    before = set(ova2.WORKS)
    importlib.import_module('v3.' + name)
    new = {k: ova2.WORKS[k] for k in ova2.WORKS if k not in before}
    out = os.path.join(HERE, 'obras_new_a2_001_240_%s.json' % name[len('ova2_'):])
    json.dump(new, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(name, len(new), 'obras')
