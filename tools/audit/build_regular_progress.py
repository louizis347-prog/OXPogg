#!/usr/bin/env python3
"""Painel de acompanhamento do inglês regular: estrutura (contrato) e ponte obra↔episódio (bridge_rules)."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import regular_pilot_contract as contract
from bridge_rules import bridge_failures

manifest = json.load(open('data/manifest.json', encoding='utf-8'))
levels = ['en-a1', 'en-a2', 'en-b1', 'en-b2', 'en-c1', 'en-c2']
rows = []
for level in levels:
    episodes = contract.load_course(manifest, level)
    failures = contract.audit(level, episodes, ponte=False)
    failing = set()
    for failure in failures:
        marker = f'{level} '
        if failure.startswith(marker):
            token = failure[len(marker):].split(' ', 1)[0]
            if token.isdigit():
                failing.add(int(token))
    complete = len(episodes) - len(failing)
    ponte_ok = sum(1 for _, e in episodes if e.get('presentation') == 'regular-pilot-v1' and not bridge_failures(e))
    rows.append((level.upper(), len(episodes), complete, len(failing), ponte_ok))

lines = [
    '# Acompanhamento — Inglês regular',
    '',
    '> Atualizado pelo contrato de qualidade (estrutura e densidade dos episódios 2–5) e pelas regras da ponte obra↔episódio (`tools/audit/bridge_rules.py`).',
    '',
    '| Nível | Episódios | Estrutura conforme | A reescrever | Progresso | Ponte completa |',
    '| --- | ---: | ---: | ---: | ---: | ---: |',
]
for level, total, complete, pending, ponte in rows:
    lines.append(f'| {level} | {total} | {complete} | {pending} | {complete / total:.0%} | {ponte} ({ponte / total:.0%}) |')
lines += [
    '',
    '## Critério para considerar um episódio concluído',
    '',
    '**Estrutura e densidade** (`tools/audit/regular_pilot_contract.py`):',
    '- 19 quadros do modelo `regular-pilot-v1`;',
    '- 6 itens de vocabulário, 4 verbos, 4 expressões;',
    '- laboratório com 3 sons e 3 desafios;',
    '- duas cenas densas e 3 missões;',
    '- mochila como única retomada do episódio anterior;',
    '- obra cultural própria, sem repetição dentro do curso.',
    '',
    '**Ponte obra↔episódio** (`tools/audit/bridge_rules.py`, padrão em `docs/PADRAO_PONTE_OBRA.md`):',
    '- pelo menos uma fala das cenas cita a obra ou um personagem dela;',
    '- a 1ª missão se chama “Cena da obra” e cita a obra ou um personagem;',
    '- gancho da capa e figurinha do fechamento são da obra do episódio; descrição da obra com 90+ caracteres;',
    '- elenco sem nomes genéricos (Woman, Man, Girl, Boy…); mesmo cenário nunca em 3 quadros seguidos.',
    '',
    '## Trava',
    '',
    'Todo episódio marcado `regular-pilot-v1`, em qualquer curso regular, precisa passar o contrato e a ponte (`tools/audit/regular_gate.py`, workflow `regular-quality-gate.yml`). Falhas antigas ficam no baseline (`tools/audit/gate_baseline.json`); falha nova reprova. Os 4 episódios de referência (7009801, 70001, 7070001, 30001) são o modelo e ficam fora das regras da ponte.',
    '',
    'Para atualizar: `python3 tools/audit/build_regular_progress.py`.',
]
os.makedirs('docs', exist_ok=True)
open('docs/ACOMPANHAMENTO_INGLES_REGULAR.md', 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
