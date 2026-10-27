#!/usr/bin/env python3
"""Grava tools/v3/obras_new_a1_zz_c.json (obras do lote C do A1). Rodar da raiz: python3 tools/v3/zzc1_works.py"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, HERE)
from v3 import ova2
import v3.ova1_zz_c
from v3 import zzc1_lib as Z
new = {str(n): ova2.WORKS[str(n)] for n in sorted(Z.SPECS) if str(n) in ova2.WORKS}
json.dump(new, open(os.path.join(HERE, 'obras_new_a1_zz_c.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(new), 'obras')
