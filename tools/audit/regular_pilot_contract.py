#!/usr/bin/env python3
"""Quality contract shared by every regular course (never Neighbors)."""
import argparse
import json
import os
import sys
from collections import Counter
import re

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bridge_rules import bridge_failures  # noqa: E402

EXPECTED = [
    'cover', 'review', 'hotscene', 'pgscene', 'pgsheet', 'pgrule',
    'pgmold', 'pgsheet', 'verbs', 'vplay', 'pgexp', 'pgscene',
    'pgsheet', 'pgsheet', 'pglab', 'pgsheet', 'pgspeak', 'pgmission', 'wrap',
]

# A generic coaching verb is useful once in a lesson, but it cannot make up
# most of an advanced lesson's verb set.  These are the fallbacks that the old
# C1/C2 generator appended when it could not find authored verbs.
GENERIC_VERBS = {'explain', 'notice', 'connect', 'rephrase', 'use', 'make', 'show', 'read'}
SUBJECT_STARTERS = {
    'i', 'you', 'he', 'she', 'it', 'we', 'they', 'this', 'that', 'these',
    'those', 'there', 'what', 'who', 'which', 'where', 'when', 'why',
}
IDIOM_PARTICLES = {
    'about', 'after', 'against', 'around', 'at', 'away', 'back', 'by', 'down',
    'for', 'from', 'in', 'into', 'off', 'on', 'out', 'over', 'through', 'to',
    'under', 'up', 'with', 'without',
}


def _text(item):
    """Return the learner-facing English text for a verb/expression item."""
    if not isinstance(item, dict):
        return ''
    return str(item.get('en') or item.get('x') or item.get('v') or '').strip()


def _norm_phrase(value):
    value = str(value or '').replace('’', "'").replace('‘', "'").replace('`', "'").lower()
    value = re.sub(r"[^a-z0-9']+", ' ', value)
    return re.sub(r'\s+', ' ', value).strip()


def _looks_like_sentence(value):
    """Reject sentence-shaped fillers while allowing short phrasal verbs.

    The authored contract expects reusable chunks (``come to terms with``,
    ``dawn on someone``), not a complete proposition with a capitalized subject
    and final punctuation.  A short chunk with a particle/preposition remains
    valid even when it starts with a pronoun (e.g. ``dawn on someone``).
    """
    raw = str(value or '').strip()
    if not raw:
        return True
    if raw.endswith(('.', '?', '!')):
        return True
    tokens = _norm_phrase(raw).split()
    if len(tokens) < 3 or tokens[0] not in SUBJECT_STARTERS:
        return False
    # A pronoun-led chunk is acceptable only when it is clearly an idiomatic
    # prepositional/phrasal unit; otherwise it is a sentence in disguise.
    return not any(token in IDIOM_PARTICLES for token in tokens[1:])


def _content_failures(course, episode, verbs, expressions):
    """Content-level checks added after the structural pilot contract."""
    failures = []
    level = course.rsplit('-', 1)[-1]
    # The stricter semantic checks target the advanced courses whose old data
    # passed merely because it had four placeholder objects.
    if level not in ('c1', 'c2'):
        return failures
    verb_values = [_norm_phrase(item.get('v')) for item in verbs.get('items', []) if isinstance(item, dict)]
    generic = [v for v in verb_values if v in GENERIC_VERBS]
    if len(generic) >= 2:
        failures.append('verbos genéricos demais: ' + ', '.join(generic))
    if len(set(verb_values)) != len(verb_values):
        failures.append('verbos repetidos dentro do episódio')
    expr_values = [_norm_phrase(_text(item)) for item in expressions.get('items', [])]
    if len(set(expr_values)) != len(expr_values):
        failures.append('expressões repetidas dentro do episódio')
    sentence_like = [_text(item) for item in expressions.get('items', []) if _looks_like_sentence(_text(item))]
    if sentence_like:
        failures.append('expressões em formato de frase: ' + ' | '.join(sentence_like))
    if any(v.startswith('the point is ') for v in expr_values):
        failures.append('expressão-modelo genérica: The point is …')
    return failures


def load_course(manifest, course):
    episodes = []
    for filename in manifest[course]:
        path = os.path.join('data', filename)
        for episode in json.load(open(path, encoding='utf-8')):
            episodes.append((path, episode))
    return episodes


def audit(course, episodes, ponte=True):
    """ponte=True inclui as regras da ponte obra↔episódio (bridge_rules.py) nos episódios marcados regular-pilot-v1."""
    failures = []
    works = Counter()
    for ordinal, (path, episode) in enumerate(episodes, 1):
        label = f'{course} {ordinal} ({episode.get("n")}, {path})'
        frames = episode.get('fr', [])
        kinds = ['pgsheet' if frame.get('k') == 'pgfind' else frame.get('k') for frame in frames]
        if episode.get('presentation') != 'regular-pilot-v1':
            failures.append(f'{label}: presentation ausente')
        with_reading = EXPECTED[:3] + ['rdg'] + EXPECTED[3:]
        # versão final: leitura + diálogo (depois dos verbos) no lugar do último quadro de sons
        full = list(with_reading)
        full.insert(full.index('vplay') + 1, 'pgdlg')
        full.pop(full.index('pglab') + 1)
        if ordinal != 1 and kinds not in (EXPECTED, with_reading, full):
            failures.append(f'{label}: sequência de 19 quadros inválida')
        if len(episode.get('v') or []) != 6:
            failures.append(f'{label}: vocabulário deve ter exatamente 6 itens')
        scenes = [frame for frame in frames if frame.get('k') == 'pgscene']
        level = course.rsplit('-', 1)[-1]
        minimum_second_scene = 6 if level in ('a1', 'a2') else 8
        if (len(scenes) != 2 or len(scenes[0].get('lines', [])) < 8
                or len(scenes[1].get('lines', [])) < minimum_second_scene):
            failures.append(f'{label}: cenas precisam de 8 e {minimum_second_scene}+ falas')
        # The opening lesson has no previous episode to put in the backpack.
        if ordinal != 1 and (len(frames) < 2 or frames[1].get('k') != 'review'):
            failures.append(f'{label}: mochila de revisão ausente')
        verbs = next((frame for frame in frames if frame.get('k') == 'verbs'), {})
        if len(verbs.get('items', [])) != 4:
            failures.append(f'{label}: precisa de exatamente 4 verbos')
        expressions = next((frame for frame in frames if frame.get('k') == 'pgexp'), {})
        if len(expressions.get('items', [])) != 4:
            failures.append(f'{label}: precisa de exatamente 4 expressões')
        for issue in _content_failures(course, episode, verbs, expressions):
            failures.append(f'{label}: {issue}')
        lab = next((frame for frame in frames if frame.get('k') == 'pglab'), {})
        if len(lab.get('ex', [])) != 3 or len(lab.get('rounds', [])) != 3:
            failures.append(f'{label}: laboratório precisa de 3 sons e 3 desafios')
        mission = next((frame for frame in frames if frame.get('k') == 'pgmission'), {})
        if len(mission.get('missions', [])) != 3:
            failures.append(f'{label}: precisa de exatamente 3 missões')
        if ponte:
            for msg in bridge_failures(episode):
                failures.append(f'{label}: {msg}')
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
