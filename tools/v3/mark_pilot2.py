#!/usr/bin/env python3
"""Marca os episódios escritos em tools/v3/ep_121_*.py … com a apresentação regular-pilot-v1 e o padrão gramatical do próprio episódio."""
import glob, importlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE))
PAT = {}
for f in sorted(glob.glob(os.path.join(HERE, 'ep_[01][0-9][0-9]_*.py'))):
    m = importlib.import_module('v3.' + os.path.basename(f)[:-3])
    for E in m.EPS:
        PAT[E['n']] = E['v2']['base']['pattern_label']
for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'en-a1_*.json'))):
    d = json.load(open(f, encoding='utf-8')); ch = False
    for x in d:
        if x['n'] in PAT:
            x['presentation'] = 'regular-pilot-v1'; x['g'] = {'t': PAT[x['n']]}; x['gs'] = PAT[x['n']]; ch = True
    if ch:
        open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
print('marcados:', len(PAT))
# Tira dos esqueletos, do roteiro (HTML) e dos docs os episódios que já foram remodelados.
import subprocess
subprocess.run([sys.executable, os.path.join(ROOT, 'tools/skel/build.py')], check=True, stdout=subprocess.DEVNULL)
subprocess.run([sys.executable, os.path.join(ROOT, 'tools/roteiro/build.py')], check=True, stdout=subprocess.DEVNULL)
print('esqueletos e roteiro atualizados')
