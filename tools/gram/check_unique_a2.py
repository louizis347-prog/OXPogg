#!/usr/bin/env python3
"""Confere rótulos de gramática repetidos entre os episódios do A2 já remodelados (campo gs)."""
import glob, json, os, collections
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
c = collections.defaultdict(list)
for f in sorted(glob.glob(os.path.join(ROOT, 'data/en-a2_*.json'))):
    for x in json.load(open(f, encoding='utf-8')):
        if x.get('gs') and x.get('presentation') == 'regular-pilot-v1':
            c[x['gs']].append(x['n'])
rep = {k: v for k, v in c.items() if len(v) > 1}
for k, v in rep.items():
    print('REPETIDO', k, v)
print('repetidos:', len(rep), 'de', len(c))
