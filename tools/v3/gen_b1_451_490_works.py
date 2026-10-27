#!/usr/bin/env python3
"""Grava tools/v3/obras_new_b1_451_490.json a partir das especificações dos módulos b1_451_455 … b1_486_490 (uma obra por episódio).
Uso (da raiz do repositório): python3 tools/v3/gen_b1_451_490_works.py"""
import importlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, HERE)
from v3 import b1x_lib as L
for m in ('b1_451_455', 'b1_456_460', 'b1_461_465', 'b1_466_470', 'b1_471_475', 'b1_476_480', 'b1_481_485', 'b1_486_490'):
    importlib.import_module('v3.' + m)
out = {}
for n in L.ORDER:
    s = L.SPECS[n]
    w = L.work(n, s['ob'])
    w['line'] = [s['lines'][0][0], s['lines'][0][1] + ' (frase autoral da aula)']
    out[str(n)] = w
open(os.path.join(HERE, 'obras_new_b1_451_490.json'), 'w', encoding='utf-8').write('{\n' + ',\n'.join('%s: %s' % (json.dumps(k), json.dumps(v, ensure_ascii=False)) for k, v in out.items()) + '\n}\n')
print(len(out), 'obras gravadas')
