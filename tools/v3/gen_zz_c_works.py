#!/usr/bin/env python3
"""Grava tools/v3/obras_new_b1_zz_c.json a partir de ovrb1_zz_c_d*.py. Rodar da raiz: python3 tools/v3/gen_zz_c_works.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, HERE)
from v3 import ovrb1_zz_c as Z
new = {str(n): Z.work(n) for n in sorted(Z.SPEC)}
json.dump(new, open(os.path.join(HERE, 'obras_new_b1_zz_c.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(new), 'obras')
