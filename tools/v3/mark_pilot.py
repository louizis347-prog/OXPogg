#!/usr/bin/env python3
"""Aplica a apresentação visual dos 5 primeiros (regular-pilot-v1) e o padrão do esqueleto aos episódios 116–120 do A1."""
import glob, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAT = {7910010: 'make + coisa (make tea, make a cake)', 70044: "Do you have…? · Yes, I do / No, I don't", 7070044: 'have · has · Here you are',
       10163: 'He is a… · She is a…', 7010163: 'What does he do? · Is she a…?'}
for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'en-a1_*.json'))):
    d = json.load(open(f, encoding='utf-8')); ch = False
    for x in d:
        if x['n'] in PAT:
            x['presentation'] = 'regular-pilot-v1'; x['g'] = {'t': PAT[x['n']]}; x['gs'] = PAT[x['n']]; ch = True
    if ch:
        open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
