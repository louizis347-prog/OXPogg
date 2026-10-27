#!/usr/bin/env python3
"""Grava tools/v3/obras_new_b1_zz_a.json a partir de zz_b1a_d*.py. Rodar da raiz: python3 tools/v3/gen_zz_b1a_works.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, HERE)
from v3 import zz_b1a_lib as Z
from v3 import zz_b1a_d1, zz_b1a_d2, zz_b1a_d3, zz_b1a_d4
new = {str(n): Z.work(Z.SPECS[n]) for n in sorted(Z.SPECS)}
json.dump(new, open(os.path.join(HERE, 'obras_new_b1_zz_a.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(new), 'obras')
