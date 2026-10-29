#!/usr/bin/env python3
"""Aplica os lotes de cenários (tools/scenes/out/*.json): grava fichas completas em tools/ficha/work/en-<nivel>_zzscenes.json
(o build.py usa o último arquivo por ordem alfabética, então estas fichas substituem as antigas) e reconstrói js/fichas-en-*.js.
Uso: python3 tools/scenes/apply.py [lote ...]   (sem argumentos: todos os lotes de tools/scenes/out)"""
import glob, json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
base = {}
for fn in sorted(glob.glob(os.path.join(ROOT, 'tools/ficha/work/*_*.json'))):
    if '_zzscenes' in fn: continue
    for n, f in json.load(open(fn, encoding='utf-8')).items():
        if not f.get('conflito'): base[int(n)] = f
lotes = sys.argv[1:] or [os.path.basename(f)[:-5] for f in sorted(glob.glob(os.path.join(ROOT, 'tools/scenes/out/*.json')))]
by = {}
for l in lotes:
    out = json.load(open(os.path.join(ROOT, 'tools/scenes/out', l + '.json'), encoding='utf-8'))
    lv = 'en-' + l.split('_')[0]
    for n, x in out.items():
        f = dict(base[int(n)]); f['scene'] = x['scene']; f['tod'] = x['tod']; f['decor'] = list(x.get('decor') or [])
        by.setdefault(lv, {})[n] = f
for lv, d in by.items():
    fn = os.path.join(ROOT, 'tools/ficha/work/%s_zzscenes.json' % lv)
    old = json.load(open(fn, encoding='utf-8')) if os.path.exists(fn) else {}
    old.update(d); json.dump(old, open(fn, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    subprocess.run([sys.executable, os.path.join(ROOT, 'tools/ficha/build.py'), lv], cwd=ROOT, check=True)
print('cenários aplicados:', {lv: len(d) for lv, d in by.items()})
