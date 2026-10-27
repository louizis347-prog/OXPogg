#!/usr/bin/env python3
"""Grava tools/v3/obras_new_a2_001_240_zz_a.json (obras do lote A na camada ova2). Rodar da raiz: python3 tools/v3/zz_a_works.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, HERE)
from v3 import ova2
import v3.ova2_zz_a
from v3 import zz_a_lib as Z
new = {str(n): ova2.WORKS[str(n)] for n in sorted(Z.SPECS) if str(n) in ova2.WORKS}
json.dump(new, open(os.path.join(HERE, 'obras_new_a2_001_240_zz_a.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(new), 'obras')
