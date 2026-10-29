#!/usr/bin/env python3
"""Aplica os módulos tools/v3/a2_fix_*.py nos dados do A2 (só os episódios de tools/a2fix/briefs.json) e garante a ponte obra–foco na descrição.
Uso: python3 tools/a2fix/apply.py   (depois: python3 tools/ficha/build.py en-a2 e as travas)"""
import glob, json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ns = [x['n'] for x in json.load(open(os.path.join(ROOT, 'tools/a2fix/briefs.json'), encoding='utf-8'))['alvo']]
env = dict(os.environ, COURSE='en-a2')
subprocess.run([sys.executable, os.path.join(ROOT, 'tools/model_v3.py')] + [str(n) for n in ns], env=env, cwd=ROOT, check=True)
MARKER = re.compile(r"\b(a aula|a referência|a cena|a obra|ponto de partida|serve de ponte|conversa diretamente|the scene|the reference|connect)\b", re.I)
for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'en-a2_*.json'))):
    d = json.load(open(f, encoding='utf-8')); dirty = False
    for e in d:
        if e['n'] in ns and not MARKER.search(e['a'].get('d', '')):
            sub = re.sub(r'\s*\(.*?\)\s*$', '', e.get('s') or '').strip()
            e['a']['d'] = e['a']['d'].rstrip() + f" A referência {e['a']['w']} combina com {sub}."; dirty = True
    if dirty:
        open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
print('a2fix aplicado:', len(ns), 'episódios')
