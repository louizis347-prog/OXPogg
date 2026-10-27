#!/usr/bin/env python3
"""Require one non-repeated cultural reference for each regular-course episode."""
import argparse
import json
import os
import sys
from collections import defaultdict


def load(manifest, course):
    result = []
    for filename in manifest[course]:
        result.extend(json.load(open(os.path.join('data', filename), encoding='utf-8')))
    return result


def audit(course, episodes):
    references = defaultdict(list)
    errors = []
    for ordinal, episode in enumerate(episodes, 1):
        work = (episode.get('a') or {}).get('w', '').strip()
        if not work:
            errors.append(f'{course} {ordinal} ({episode.get("n")}): referência cultural ausente')
        else:
            references[work.casefold()].append((ordinal, episode.get('n'), work))
    for entries in references.values():
        if len(entries) > 1:
            work = entries[0][2]
            ids = ', '.join(f'{ordinal}/{episode_id}' for ordinal, episode_id, _ in entries)
            errors.append(f'{course}: obra repetida “{work}” em {ids}')
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--course', action='append')
    parser.add_argument('--report')
    args = parser.parse_args()
    manifest = json.load(open('data/manifest.json', encoding='utf-8'))
    regular = [course for course in manifest if not course.startswith('nb')]
    courses = args.course or regular
    invalid = set(courses) - set(regular)
    if invalid:
        raise SystemExit('Cursos inválidos ou Neighbors: ' + ', '.join(sorted(invalid)))
    report = {}
    failed = False
    for course in courses:
        episodes = load(manifest, course)
        errors = audit(course, episodes)
        report[course] = {'episodes': len(episodes), 'errors': errors}
        print(f'{course}: {len(episodes)} episódios; {len(errors)} falhas culturais')
        failed |= bool(errors)
    if args.report:
        with open(args.report, 'w', encoding='utf-8') as target:
            json.dump(report, target, ensure_ascii=False, indent=2)
    raise SystemExit(failed)


if __name__ == '__main__':
    main()
