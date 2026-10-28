# Trava de qualidade e plano por episódio (cursos regulares)

## Trava (`tools/audit/regular_gate.py`, workflow `.github/workflows/regular-quality-gate.yml`)
- Todo episódio marcado `regular-pilot-v1` em qualquer curso regular (nunca Neighbors) precisa passar `tools/audit/regular_pilot_contract.py`: 19 quadros, 6 palavras, 4 verbos, 4 expressões, laboratório 3+3, duas cenas densas, 3 missões, mochila, obra própria — a densidade dos episódios 2–5 do inglês.
- **Ponte obra↔episódio** (`tools/audit/bridge_rules.py`, `docs/PADRAO_PONTE_OBRA.md`): fala das cenas que cita a obra ou personagem dela; 1ª missão “Cena da obra” (enunciado e modelo) citando a obra ou personagem; gancho da capa e figurinha da obra; descrição da obra (90+ caracteres); elenco sem nomes genéricos; mesmo cenário nunca em 3 quadros seguidos. Os 4 episódios de referência do inglês A1 são o modelo e ficam fora da ponte.
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

## Atualização (28/10) — a trava passa a incluir a ponte
- `regular_pilot_contract.audit(..., ponte=True)` (padrão) soma as regras de `bridge_rules.py` a todo episódio marcado `regular-pilot-v1`; `try.py` do B2 e `regular_gate.py` usam isso, então episódio novo já nasce com a ponte.
- Baseline: as 4.622 falhas existentes (a ponte falta em ~80% dos episódios A1–B2 e nos cursos de outros idiomas já convertidos) ficam toleradas; só falha nova reprova. À medida que a ponte é aplicada (`apply_bridge_patches.py`), reduzir o baseline com `python3 tools/audit/regular_gate.py --shrink` (só remove o que foi corrigido; nunca adiciona).
- Autoteste: `python3 tools/audit/test_gate.py` (11 casos em memória: um episódio bom passa e cada defeito conhecido reprova).
- Painel `docs/ACOMPANHAMENTO_INGLES_REGULAR.md` agora mostra estrutura e ponte.

## Atualização — expressões únicas em todo curso regular
- Regra 6 da trava (`tools/audit/expr_rules.py`, usada por `regular_gate.py` e testada em `test_gate.py`): a expressão ensinada no quadro de expressões (`pgexp`) de um episódio não pode ser ensinada em outro episódio do mesmo curso, nem duas vezes no mesmo episódio. A comparação ignora caixa, pontuação e espaços (“Let’s go!” = “let's go”).
- Única repetição oficial: a **mochila de revisão** (quadro `review`), que retoma o conteúdo do episódio anterior. Ela não é lida por esta regra.
- Antes a regra valia só para o C1 e o C2; agora vale para todos os cursos regulares marcados `regular-pilot-v1`. As repetições que já existiam (4.885, a maioria no espanhol e no inglês A1/A2/B1) entram no baseline e saem dele com `regular_gate.py --shrink` conforme forem trocadas; repetição nova bloqueia.
