#!/usr/bin/env python3
"""Compare published Pocket episodes with their per-episode editorial scripts."""
import json
import re
from collections import Counter
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / 'data'
FORBIDDEN = ('thanks for meeting me', 'next step', 'useful comparison',
             'useful idea', 'useful lens', 'practical solution',
             'state the decision clearly', 'make the inference explicit',
             'strongest objection', 'the issue of ')

def read_level(level):
    return {e['n']:e for path in sorted(DATA.glob(f'pk-{level}_*.json'))
            for e in json.loads(path.read_text(encoding='utf-8'))}

def audit(level):
    plan = json.loads((DATA/'pk-roteiro'/f'pk-{level}.json').read_text(encoding='utf-8'))
    episodes = read_level(level)
    failures = Counter(); examples = {}
    for row in plan:
        n = row['n']; e = episodes.get(n)
        if not e:
            failures['missing'] += 1; continue
        fr = {f['k']:f for f in e.get('fr',[])}
        if not {'pkdlg','pkvoc','pkbuild','pkspeak','wrap'} <= fr.keys():
            failures['missing frame'] += 1; continue
        lines = fr['pkdlg']['lines']
        text = ' '.join(str(line[1]) for line in lines).lower()
        terms = [str(v[0]).lower() for v in row['vocabulario']]
        card_terms = [str(c[0]).lower() for c in fr['pkvoc']['cards']]
        if len(lines) < (10 if row.get('chefe') else 8):
            failures['dialogue too short'] += 1
        if not all(t in card_terms for t in terms):
            failures['script vocabulary absent'] += 1
            examples.setdefault('script vocabulary absent', n)
        if any(bad in text for bad in FORBIDDEN):
            failures['forbidden boilerplate'] += 1
            examples.setdefault('forbidden boilerplate', n)
        if row['titulo_en'].lower() not in e['t'].lower():
            failures['script title absent'] += 1
        if not all('{0}' in b.get('en','') and '{0}' in b.get('pt','') for b in fr['pkbuild']['items']):
            failures['broken build slots'] += 1
    return len(plan), failures, examples

if __name__ == '__main__':
    for level in ('b1','b2','c1','c2'):
        total, failures, examples = audit(level)
        print(level.upper(), total, 'roteiros', dict(failures), 'exemplos', examples)
