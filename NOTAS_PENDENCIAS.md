# Pogglot — balanço e pendências (19/10/2026)

## Feito
- Inglês regular A1–C2 (5.000 episódios): estrutura nova aplicada em todos (original + continuação enxuta, práticas alternadas, verbos 7+7, Monte a cena, cultura em quadros, ilustração em toda tela, textos cortados corrigidos).
- Leitura da regra (`rdg`): só en-a1 (388).
- Conversa jogável (`rdgplay`): só 10 pares do A1.
- Cultura escrita à mão: só 10 obras do A1; as demais usam texto-modelo.
- Neighbors: japonês 365, alemão 400, francês 400 (tools/nb/).

## Pendente (ordem sugerida)
1. Leitura da regra (`rdg`) para en-a2…c2 (2.111 continuações) — ver tools/rdg/ e tools/addrdg.py.
2. Cultura caprichada: 378 obras do A1 restantes em tools/rdg/cult_a1.py, depois `git checkout -- data` e rodar tools/culture2.py; depois A2–C2.
3. `rdgplay` além dos 10 pares (tools/rdg/play_a1.py, tools/applyplay.py).
4. Telas de conteúdo que ainda rolam; espanhol A2–C2 e Neighbors não reorganizados.
5. Futuro: gerador de roteiro de estudo (tempo disponível → tutor).

## Regras de trabalho
Commit + push em main e claude/nifty-mendel-y3nbxt a cada mudança; sem PR; uma coisa por vez; relatórios em português.
