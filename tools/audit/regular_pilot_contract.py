#!/usr/bin/env python3
"""Quality contract shared by every regular course (never Neighbors)."""
import argparse
import json
import os
import sys
from collections import Counter

EXPECTED = [
    'cover', 'review', 'hotscene', 'pgscene', 'pgsheet', 'pgrule',
    'pgmold', 'pgsheet', 'verbs', 'vplay', 'pgexp', 'pgscene',
    'pgsheet', 'pgsheet', 'pglab', 'pgsheet', 'pgspeak', 'pgmission', 'wrap',
]


def load_course(manifest, course):
    episodes = []
    for filename in manifest[course]:
        path = os.path.join('data', filename)
        for episode in json.load(open(path, encoding='utf-8')):
            episodes.append((path, episode))
    return episodes


def audit(course, episodes):
    failures = []
    works = Counter()
    for ordinal, (path, episode) in enumerate(episodes, 1):
        label = f'{course} {ordinal} ({episode.get("n")}, {path})'
        frames = episode.get('fr', [])
        kinds = [frame.get('k') for frame in frames]
        if episode.get('presentation') != 'regular-pilot-v1':
            failures.append(f'{label}: presentation ausente')
        if kinds != EXPECTED:
            failures.append(f'{label}: sequência de 19 quadros inválida')
        if len(episode.get('v') or []) != 6:
            failures.append(f'{label}: vocabulário deve ter exatamente 6 itens')
        scenes = [frame for frame in frames if frame.get('k') == 'pgscene']
        if len(scenes) != 2 or any(len(frame.get('lines', [])) < 8 for frame in scenes):
            failures.append(f'{label}: precisa de duas cenas com 8+ falas')
        if len(frames) < 2 or frames[1].get('k') != 'review':
            failures.append(f'{label}: mochila de revisão ausente')
        verbs = next((frame for frame in frames if frame.get('k') == 'verbs'), {})
        if len(verbs.get('items', [])) != 4:
            failures.append(f'{label}: precisa de exatamente 4 verbos')
        expressions = next((frame for frame in frames if frame.get('k') == 'pgexp'), {})
        if len(expressions.get('items', [])) != 4:
            failures.append(f'{label}: precisa de exatamente 4 expressões')
        lab = next((frame for frame in frames if frame.get('k') == 'pglab'), {})
        if len(lab.get('ex', [])) != 3 or len(lab.get('rounds', [])) != 3:
            failures.append(f'{label}: laboratório precisa de 3 sons e 3 desafios')
        mission = next((frame for frame in frames if frame.get('k') == 'pgmission'), {})
        if len(mission.get('missions', [])) != 3:
            failures.append(f'{label}: precisa de exatamente 3 missões')
        work = (episode.get('a') or {}).get('w', '').strip()
        if not work:
            failures.append(f'{label}: obra cultural ausente')
        else:
            works[work] += 1
    for work, amount in works.items():
        if amount > 1:
            failures.append(f'{course}: obra repetida {amount}×: {work}')
    return failures


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--course', action='append', help='course ID; repeat to audit selected courses')
    parser.add_argument('--report', help='optional JSON report path')
    args = parser.parse_args()
    manifest = json.load(open('data/manifest.json', encoding='utf-8'))
    regular = [course for course in manifest if not course.startswith('nb')]
    selected = args.course or regular
    unknown = set(selected) - set(regular)
    if unknown:
        raise SystemExit('Cursos inválidos ou Neighbors: ' + ', '.join(sorted(unknown)))
    report = {}
    for course in selected:
        episodes = load_course(manifest, course)
        failures = audit(course, episodes)
        report[course] = {'episodes': len(episodes), 'failures': failures}
        print(f'{course}: {len(episodes)} episódios; {len(failures)} falhas')
    if args.report:
        with open(args.report, 'w', encoding='utf-8') as target:
            json.dump(report, target, ensure_ascii=False, indent=2)
    raise SystemExit(any(data['failures'] for data in report.values()))


if __name__ == '__main__':
    main()
