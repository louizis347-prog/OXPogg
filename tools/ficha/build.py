#!/usr/bin/env python3
"""Junta as fichas (tools/ficha/work/<curso>_*.json) em js/fichas-<curso>.js (window.PogFichas). Uso: python3 tools/ficha/build.py [curso=en-a1]"""
import glob, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
curso = sys.argv[1] if len(sys.argv) > 1 else 'en-a1'
F = {}
for fn in sorted(glob.glob(os.path.join(HERE, 'work', curso + '_*.json'))):
    for n, f in json.load(open(fn, encoding='utf-8')).items():
        if f.get('conflito'): continue   # obra com título diferente da aula: fica de fora até o título ser corrigido
        f = {k: v for k, v in f.items() if k not in ('t', 'falta', 'conflito')}
        F[int(n)] = f
out = '/* Fichas das capas (gerado por tools/ficha/build.py a partir de tools/ficha/work/%s_*.json) */\nwindow.PogFichas=Object.assign(window.PogFichas||{},%s);\n' % (curso, json.dumps(F, ensure_ascii=False, separators=(',', ':'), sort_keys=True))
open(os.path.join(ROOT, 'js', 'fichas-%s.js' % curso), 'w', encoding='utf-8').write(out)
print('fichas-%s.js: %d fichas, %d KB' % (curso, len(F), len(out) // 1024))
