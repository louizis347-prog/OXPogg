#!/usr/bin/env python3
"""Build the human-readable progress board for regular English."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import regular_pilot_contract as contract

manifest = json.load(open('data/manifest.json', encoding='utf-8'))
levels = ['en-a1', 'en-a2', 'en-b1', 'en-b2', 'en-c1', 'en-c2']
rows = []
for level in levels:
    episodes = contract.load_course(manifest, level)
    failures = contract.audit(level, episodes)
    failing_ordinals = set()
    for failure in failures:
        marker = f'{level} '
        if failure.startswith(marker):
            token = failure[len(marker):].split(' ', 1)[0]
            if token.isdigit():
                failing_ordinals.add(int(token))
    complete = len(episodes) - len(failing_ordinals)
    rows.append((level.upper(), len(episodes), complete, len(failing_ordinals)))

lines = [
    '# Acompanhamento — Inglês regular',
    '',
    '> Atualizado automaticamente pelo contrato de qualidade dos episódios 2–5.',
    '',
    '| Nível | Episódios | Conformes | A reescrever | Progresso |',
    '| --- | ---: | ---: | ---: | ---: |',
]
for level, total, complete, pending in rows:
    lines.append(f'| {level} | {total} | {complete} | {pending} | {complete / total:.0%} |')
lines += [
    '',
    '## Critério para considerar um episódio concluído',
    '',
    '- 19 quadros do modelo `regular-pilot-v1`;',
    '- 6 itens de vocabulário, 4 verbos, 4 expressões;',
    '- laboratório com 3 sons e 3 desafios;',
    '- duas cenas densas e 3 missões;',
    '- mochila como única retomada do episódio anterior;',
    '- obra cultural própria, sem repetição dentro do curso.',
    '',
    '## Fila atual',
    '',
    '- B1: pausado por solicitação do responsável.',
    '- B2: início da conversão para o piloto.',
    '- C1 e C2: entram após o B2.',
    '',
    'Para atualizar: `python3 tools/audit/build_regular_progress.py`.',
]
os.makedirs('docs', exist_ok=True)
open('docs/ACOMPANHAMENTO_INGLES_REGULAR.md', 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
