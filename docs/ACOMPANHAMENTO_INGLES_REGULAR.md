# Acompanhamento — Inglês regular

> Atualizado pelo contrato de qualidade (estrutura e densidade dos episódios 2–5) e pelas regras da ponte obra↔episódio (`tools/audit/bridge_rules.py`).

| Nível | Episódios | Estrutura conforme | A reescrever | Progresso | Ponte completa |
| --- | ---: | ---: | ---: | ---: | ---: |
| EN-A1 | 466 | 466 | 0 | 100% | 131 (28%) |
| EN-A2 | 474 | 474 | 0 | 100% | 83 (18%) |
| EN-B1 | 530 | 530 | 0 | 100% | 40 (8%) |
| EN-B2 | 510 | 510 | 0 | 100% | 97 (19%) |
| EN-C1 | 510 | 0 | 510 | 0% | 0 (0%) |
| EN-C2 | 510 | 0 | 510 | 0% | 0 (0%) |

## Critério para considerar um episódio concluído

**Estrutura e densidade** (`tools/audit/regular_pilot_contract.py`):
- 19 quadros do modelo `regular-pilot-v1`;
- 6 itens de vocabulário, 4 verbos, 4 expressões;
- laboratório com 3 sons e 3 desafios;
- duas cenas densas e 3 missões;
- mochila como única retomada do episódio anterior;
- obra cultural própria, sem repetição dentro do curso.

**Ponte obra↔episódio** (`tools/audit/bridge_rules.py`, padrão em `docs/PADRAO_PONTE_OBRA.md`):
- pelo menos uma fala das cenas cita a obra ou um personagem dela;
- a 1ª missão se chama “Cena da obra” e cita a obra ou um personagem;
- gancho da capa e figurinha do fechamento são da obra do episódio; descrição da obra com 90+ caracteres;
- elenco sem nomes genéricos (Woman, Man, Girl, Boy…); mesmo cenário nunca em 3 quadros seguidos.

## Trava

Todo episódio marcado `regular-pilot-v1`, em qualquer curso regular, precisa passar o contrato e a ponte (`tools/audit/regular_gate.py`, workflow `regular-quality-gate.yml`). Falhas antigas ficam no baseline (`tools/audit/gate_baseline.json`); falha nova reprova. Os 4 episódios de referência (7009801, 70001, 7070001, 30001) são o modelo e ficam fora das regras da ponte.

Para atualizar: `python3 tools/audit/build_regular_progress.py`.
