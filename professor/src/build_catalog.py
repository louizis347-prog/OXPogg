#!/usr/bin/env python3
"""Catálogo do painel (data/v4/curriculum.json) com todas as aulas Quest que já têm dados em data/v4."""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(HERE, '..', 'data', 'v4')
out = []
for n in range(1, 400):
    f = os.path.join(D, '%03d.json' % n)
    if not os.path.exists(f): continue
    L = json.load(open(f, encoding='utf-8'))
    goal = next((p.get('goal', '') for p in L['pages'] if p.get('kind') == 'cover'), '') or L.get('pt', '')
    pt = re.split(r'(?<=[.!?])\s', goal.strip())[0][:90]
    k = (n - 1) // 8 + 1
    out.append(dict(n=n, unit=dict(n=k, k=(n - 1) % 8 + 1, of=8, name=''), level='A1', title=L['title'], pt=pt, scene=L.get('scene') or 'street', cast=L.get('cast') or []))
for u in {x['unit']['n'] for x in out}:
    g = [x for x in out if x['unit']['n'] == u]
    nm = 'Quest %d · %s → %s' % (u, g[0]['title'], g[-1]['title'])
    for x in g: x['unit']['name'] = nm; x['unit']['of'] = len(g)
json.dump(out, open(os.path.join(D, 'curriculum.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('ok', len(out))
