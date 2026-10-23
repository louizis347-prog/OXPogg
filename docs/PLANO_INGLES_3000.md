# Plano do curso regular de inglês: 5.000 → 3.000 episódios

Gerado por `tools/plan_en3000.py` (rode de novo para refazer; os dados já estão aplicados).

## Como foi decidido
- **Unidade = par**: cada padrão tinha um episódio *autoral* (cena + obra) e um episódio-*regra* (laboratório de sons, expressões coringa, molde). São 2.500 unidades.
- **Nenhum padrão gramatical e nenhum episódio autoral foi removido.** Para chegar a 3.000, o episódio-regra foi retirado de 2.000 unidades; o que ele tinha (expressões, laboratório de sons) foi para o `plan` do autoral.
- As 500 unidades restantes mantêm os dois episódios, escolhidas espaçadas ao longo do nível (as duas primeiras unidades do A1 estão entre elas).
- **Proporcional por nível** (60% de cada): A1 776→466, A2 792→475, B1 882→529, B2 850→510, C1 850→510, C2 850→510.
- Os **cinco primeiros** (9801, 7009801, 70001, 7070001, 30001) ficam como estão, sem `plan`.
- Os arcos (`ARCS`) ficam ancorados em episódios autorais, que foram todos preservados. A lista de removidos → substituto está em `docs/plano_en3000.json`.

## O que cada episódio ganhou (`plan` no JSON)
`pattern` (padrão do dia), `obra` (tipo, título, ano), `rs` (cena), `verbs` (até 4), `exps` (expressões e gírias, até 6), `sound` (laboratório de sons), `words` (vocabulário da cena), `ctx` (frases de contexto) e `todo` (o que ainda falta completar).

## Números por nível

| Nível | Antes | Depois | Unidades dobradas | Obras distintas | Planos com lacunas |
|---|---|---|---|---|---|
| A1 | 776 | 466 | 78 | 309 | 28 |
| A2 | 792 | 475 | 79 | 375 | 7 |
| B1 | 882 | 529 | 88 | 420 | 2 |
| B2 | 850 | 510 | 85 | 407 | 1 |
| C1 | 850 | 510 | 85 | 411 | 0 |
| C2 | 850 | 510 | 85 | 422 | 0 |

Total: 5000 → 3000 episódios.

## Limites honestos
- Existem só ~2.000 obras distintas no acervo; nos 3.000 episódios há **repetição de obra** (veja *Obras distintas*). Trocar a obra de cada repetido é parte do trabalho episódio a episódio.
- O `plan` reaproveita o conteúdo que já existia; onde faltou (coluna *lacunas*, campo `todo`) está marcado para completar.
- Quem já tinha concluído um episódio removido perde esse registro de progresso (o autoral correspondente continua).
