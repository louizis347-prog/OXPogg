# Trava de qualidade e plano por episódio (cursos regulares)

## Trava (`tools/audit/regular_gate.py`, workflow `.github/workflows/regular-quality-gate.yml`)
- Todo episódio marcado `regular-pilot-v1` em qualquer curso regular (nunca Neighbors) precisa passar `tools/audit/regular_pilot_contract.py`: 19 quadros, 6 palavras, 4 verbos, 4 expressões, laboratório 3+3, duas cenas densas, 3 missões, mochila, obra própria — a densidade dos episódios 2–5 do inglês.
- Obra única entre os episódios marcados do mesmo curso. Cursos em `tools/audit/gate_enforced.json` precisam estar 100% no modelo.
- Episódio com mapeamento em `tools/plan/map/` e marcado precisa usar a obra, os 4 verbos e as 4 expressões do plano.
- Falhas antigas ficam em `tools/audit/gate_baseline.json` (toleradas); falha nova reprova a checagem. Para o merge ser bloqueado de fato, marque a checagem como obrigatória na regra da `main` (Settings > Branches).
- Atualizar o baseline só ao corrigir ou aceitar de propósito: `python3 tools/audit/regular_gate.py --update-baseline`.

## Plano (`plano/<curso>.json`, `tools/plan/`)
- Cada episódio ganha, ANTES do conteúdo: foco, padrão (`gs`), obra cultural, 4 verbos, 4 expressões e os 19 quadros já formatados e vazios.
- Autoria do mapeamento: `tools/plan/map/<curso>_<parte>.json`. Validar: `python3 tools/plan/check_map.py <arquivo> ...` e `python3 tools/plan/check_plan.py <cursos> [--estrito]`. Gerar o plano: `python3 tools/plan/build_plan.py <cursos>`.
- Regras: obra única no curso (e nos cursos mapeados juntos), expressão única, padrão único, 4 verbos/expressões distintos, vizinhos sem 2+ verbos em comum.
- Mapeados: en-c1 e en-c2 (510 cada). Revisão humana pendente: `plano/REVISAR_C1_C2.md`.
- Mapeado também: **es-a1** (495 episódios + 5 já prontos). Revisão humana pendente: `plano/REVISAR_ES_A1.md`. Os validadores comparam sem acento (espanhol).

## Atualização (28/10)
- A aderência ao plano só vale para cursos listados em `tools/audit/gate_plan_ativo.json` (hoje en-c1 e en-c2, cujo conteúdo ainda será escrito a partir do plano). O es-a1 foi convertido por outra frente sem seguir o plano de `tools/plan/map/es-a1_*.json`, que ficou apenas como registro.
- O nome da obra vem de `a.w` (mesmo campo do contrato); o rótulo `sticker.sub` varia entre cursos.
- Baseline atual (toleradas, a corrigir): es-a1 71132/71143/71152 e es-a2 212 com obra repetida.
