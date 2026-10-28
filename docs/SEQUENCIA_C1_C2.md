# Sequência de produção — inglês C1 e C2 (retomável a qualquer momento)

Estado: infraestrutura pronta e enviada (guia, briefs, validador, biblioteca). Os agentes foram pausados; o que já foi escrito fica em `tools/v3/c1_*.py` / `c2_*.py`.

## Passo 0 — ver onde parou
`python3 tools/seq/sequencia.py` (painel por lote) e `python3 tools/seq/sequencia.py --prompt` (prompt pronto do próximo lote pendente).

## Passo 1 — escrever (agentes, 1 por lote de 51)
- C1 primeiro (lotes 1–51 … 460–510), depois C2 (`briefs_c2_*`, guia `GUIDE_C2.md`, validador com `COURSE_GEN=en-c2`).
- Peça: “siga a sequência de docs/SEQUENCIA_C1_C2.md”. Para cada lote pendente, lançar um agente com o prompt de `--prompt`. Agentes só escrevem módulos; não tocam em `data/`, não commitam.

## Passo 2 — montar e validar (eu)
1. `COURSE=en-c1 python3 tools/model_v3.py` (ou `en-c2`), depois `python3 tools/audit/mark_pilot2.py` / `fix_mechanical.py en-c1` conforme o fluxo do B2.
2. `python3 tools/c1gen/try.py <todos os módulos>` (validação conjunta de obras/expressões), `python3 tools/plan/check_plan.py en-c1 --estrito`, `python3 tools/audit/regular_gate.py`, `python3 tools/audit/test_gate.py`.
3. Adicionar `en-c1` (e depois `en-c2`) a `tools/audit/gate_enforced.json` quando estiver 100%.
4. Subir `sw.js` / `app.html ?v=`, PR e merge.

## Regras (iguais às do B2 + ponte)
Plano é a lei (obra, 4 verbos, 4 expressões, foco); ponte obra↔episódio obrigatória; elenco da obra; fatos só se verdadeiros; nada de filler.
