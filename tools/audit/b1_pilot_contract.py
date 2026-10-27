#!/usr/bin/env python3
"""Contract for B1 episodes 371–530 in the regular English pilot format."""
import glob
import json
import sys
from collections import Counter

EXPECTED = [
    'cover', 'review', 'hotscene', 'pgscene', 'pgsheet', 'pgrule',
    'pgmold', 'pgsheet', 'verbs', 'vplay', 'pgexp', 'pgscene',
    'pgsheet', 'pgsheet', 'pglab', 'pgsheet', 'pgspeak', 'pgmission', 'wrap',
]

episodes = []
for path in sorted(glob.glob('data/en-b1_*.json')):
    for episode in json.load(open(path, encoding='utf-8')):
        episodes.append((path, episode))

target = episodes[370:530]
works = Counter((episode.get('a') or {}).get('w', '').strip() for _, episode in target)
errors = []
for position, (path, episode) in enumerate(target, 371):
    frames = episode.get('fr', [])
    kinds = [frame.get('k') for frame in frames]
    label = f'B1 {position} ({episode.get("n")}, {path})'
    if episode.get('presentation') != 'regular-pilot-v1':
        errors.append(f'{label}: presentation ausente')
    if kinds != EXPECTED:
        errors.append(f'{label}: sequência inválida ({kinds})')
    scenes = [frame for frame in frames if frame.get('k') == 'pgscene']
    if len(scenes) != 2 or any(len(frame.get('lines', [])) < 8 for frame in scenes):
        errors.append(f'{label}: cenas precisam de 8+ falas cada')
    if len((episode.get('v') or [])) != 6:
        errors.append(f'{label}: vocabulário deve ter exatamente seis itens')
    verbs = next((frame for frame in frames if frame.get('k') == 'verbs'), {})
    if len(verbs.get('items', [])) != 4:
        errors.append(f'{label}: quadro de verbos deve ter exatamente quatro itens')
    expressions = next((frame for frame in frames if frame.get('k') == 'pgexp'), {})
    if len(expressions.get('items', [])) != 4:
        errors.append(f'{label}: quadro de expressões deve ter exatamente quatro itens')
    lab = next((frame for frame in frames if frame.get('k') == 'pglab'), {})
    if len(lab.get('ex', [])) != 3 or len(lab.get('rounds', [])) != 3:
        errors.append(f'{label}: laboratório precisa de três sons e três desafios')
    missions = next((frame for frame in frames if frame.get('k') == 'pgmission'), {})
    if len(missions.get('missions', [])) != 3:
        errors.append(f'{label}: produção precisa de exatamente três missões')
    if not (episode.get('a') or {}).get('w'):
        errors.append(f'{label}: obra cultural ausente')
    review = frames[1] if len(frames) > 1 else {}
    if review.get('k') != 'review':
        errors.append(f'{label}: mochila ausente')

for work, count in works.items():
    if work and count > 1:
        errors.append(f'obra repetida {count}×: {work}')

print(f'B1 371–530: {len(target)} episódios; {len(errors)} falhas')
for error in errors:
    print(error)
sys.exit(bool(errors))
