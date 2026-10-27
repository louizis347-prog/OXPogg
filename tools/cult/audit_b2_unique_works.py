#!/usr/bin/env python3
"""Check that the B2 cultural plan assigns one unique work to every episode."""
import glob
import json
import sys
from collections import Counter, defaultdict

manifest = json.load(open('data/manifest.json', encoding='utf-8'))['en-b2']
episodes = []
for filename in manifest:
    episodes.extend(json.load(open('data/' + filename, encoding='utf-8')))
titles = [episode['t'] for episode in episodes]

plans = []
for filename in glob.glob('tools/cult/work/en-b2_chunk*.json'):
    plans.extend(json.load(open(filename, encoding='utf-8')))

by_title = defaultdict(list)
for plan in plans:
    for title in plan.get('eps', []):
        by_title[title].append(plan['work'])

errors = []
assignment = {}
for title in titles:
    works = by_title[title]
    if len(works) != 1:
        errors.append(f'{title}: esperado 1 obra, encontrado {len(works)}')
    else:
        assignment[title] = works[0]
for work, amount in Counter(assignment.values()).items():
    if amount > 1:
        owners = [title for title, assigned in assignment.items() if assigned == work]
        errors.append(f'{work}: repetida em {owners}')

print(f'B2: {len(titles)} episódios; {len(assignment)} obras mapeadas; {len(errors)} falhas')
for error in errors:
    print(error)
sys.exit(bool(errors))
