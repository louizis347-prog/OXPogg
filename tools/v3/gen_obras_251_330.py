#!/usr/bin/env python3
"""Grava tools/v3/obras_new_b1_251_330_a.json a partir dos WORKS dos módulos ovrb1_251_*.py (obras próprias das continuações B1 251–330)."""
import glob, importlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, HERE)
W = {}
for f in sorted(glob.glob(os.path.join(HERE, 'ovrb1_2*.py')) + glob.glob(os.path.join(HERE, 'ovrb1_3*.py'))):
    W.update(getattr(importlib.import_module('v3.' + os.path.basename(f)[:-3]), 'WORKS', {}))
json.dump(W, open(os.path.join(HERE, 'obras_new_b1_251_330_a.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(W), 'obras')
