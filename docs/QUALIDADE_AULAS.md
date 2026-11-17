# Qualidade automática das aulas (fila de revisão)

Gerado por `professor/tools/quality_report.py`. Os pontos somam alertas (mais pontos = aula que merece reescrita ou revisão primeiro): média de palavras por fala abaixo do esperado do nível (2), 3+ falas curtas (1), 3+ falas repetidas de outras aulas (2), estrutura-alvo em ≥85% das falas (2; só mede A2 em diante, onde o foco vem do plano). A ligação da obra cultural com o tema NÃO é medida (a nota está em português e o diálogo em inglês; qualquer comparação automática seria enganosa): esse ponto precisa de leitura humana. **É um filtro automático; não substitui revisão humana.**

## Resumo por nível

| Nível | Aulas | Média de palavras/fala | Aulas com ≥3 pontos | Aulas com ≥5 pontos |
|---|---|---|---|---|
| A1 | 500 | 6.2 | 117 (23%) | 11 |
| A2 | 500 | 8.4 | 6 (1%) | 1 |
| B1 | 500 | 11.8 | 0 (0%) | 0 |
| B2 | 200 | 17.6 | 0 (0%) | 0 |

## A1 — 15 aulas para rever primeiro

| Aula | Título | Pontos | Palavras/fala | Curtas | Repetidas | Densidade alvo |
|---|---|---|---|---|---|---|
| 48 | Taking a taxi | 5 | 3.2 | 8 | 4 | 0.0 |
| 205 | At the vet | 5 | 3.7 | 8 | 3 | 0.0 |
| 25 | Pizza by the slice | 5 | 3.9 | 6 | 4 | 0.11 |
| 53 | Airport check-in | 5 | 3.9 | 6 | 3 | 0.11 |
| 173 | At the drive-thru | 5 | 3.9 | 5 | 3 | 0.0 |
| 33 | At the bakery | 5 | 4.3 | 6 | 3 | 0.0 |
| 90 | At the museum | 5 | 4.4 | 6 | 3 | 0.0 |
| 46 | The bus stop | 5 | 4.7 | 3 | 4 | 0.0 |
| 47 | Buy a transit card | 5 | 4.9 | 4 | 3 | 0.0 |
| 68 | At the laundry room | 5 | 4.9 | 3 | 3 | 0.0 |
| 77 | Returning an item | 5 | 4.9 | 4 | 3 | 0.0 |
| 1001 | A sandwich at the deli | 3 | 3.4 | 8 | 1 | 0.0 |
| 82 | Garage sale | 3 | 3.7 | 6 | 0 | 0.11 |
| 159 | Surprise party | 3 | 3.7 | 7 | 0 | 0.0 |
| 204 | Packing a lunch | 3 | 3.7 | 6 | 1 | 0.0 |

## A2 — 15 aulas para rever primeiro

| Aula | Título | Pontos | Palavras/fala | Curtas | Repetidas | Densidade alvo |
|---|---|---|---|---|---|---|
| 2050 | Review: asking about the past | 5 | 6.4 | 3 | 3 | 0.0 |
| 2012 | Weekend trip to the lake | 4 | 6.5 | 2 | 3 | 0.09 |
| 2120 | Spell it, please | 3 | 6.1 | 3 | 0 | 0.0 |
| 2013 | A bad cold | 3 | 6.7 | 3 | 0 | 0.36 |
| 2011 | The wrong train | 3 | 8.4 | 3 | 11 | 0.0 |
| 2411 | A city bus tour | 3 | 8.4 | 3 | 11 | 0.0 |
| 2025 | Did you like it? | 2 | 6.2 | 2 | 2 | 0.0 |
| 2196 | Splitting the bill | 2 | 6.3 | 1 | 2 | 0.18 |
| 2045 | The garden party | 2 | 6.5 | 2 | 0 | 0.55 |
| 2067 | Maybe, maybe not | 2 | 6.5 | 1 | 0 | 0.55 |
| 2037 | How many people came? | 2 | 6.6 | 1 | 0 | 0.36 |
| 2135 | Online shopping | 2 | 6.6 | 1 | 1 | 0.0 |
| 2023 | The concert | 2 | 6.7 | 1 | 1 | 0.18 |
| 2016 | Moving day | 2 | 6.8 | 1 | 0 | 0.18 |
| 2155 | At the border | 2 | 6.8 | 1 | 2 | 0.09 |

## B1 — 15 aulas para rever primeiro

| Aula | Título | Pontos | Palavras/fala | Curtas | Repetidas | Densidade alvo |
|---|---|---|---|---|---|---|
| 3051 | Stop talking, start working | 2 | 9.1 | 0 | 0 | 0.91 |
| 3001 | Have you ever been here? | 2 | 9.5 | 0 | 11 | 0.09 |
| 3052 | It’s too cold to swim | 2 | 9.5 | 0 | 0 | 0.91 |
| 3053 | He’s old enough to drive | 2 | 9.5 | 0 | 0 | 1.0 |
| 3101 | Where is this made? | 2 | 9.5 | 0 | 11 | 0.82 |
| 3003 | Already done, not yet | 2 | 10.1 | 0 | 0 | 0.91 |
| 3140 | What did the doctor say? | 2 | 10.1 | 0 | 0 | 1.0 |
| 3044 | Do you know where it is? | 2 | 10.4 | 0 | 0 | 0.91 |
| 3425 | Is it safe to take with milk? | 2 | 10.8 | 0 | 0 | 0.91 |
| 3077 | He has never been late | 2 | 11.0 | 0 | 0 | 0.91 |
| 3139 | Mom said dinner was ready | 2 | 11.2 | 0 | 0 | 0.91 |
| 3255 | The soup needs more salt | 2 | 11.2 | 0 | 0 | 1.0 |
| 3164 | I’m going to learn to swim | 2 | 11.3 | 0 | 0 | 1.0 |
| 3485 | She seems to be tired | 2 | 11.3 | 0 | 0 | 0.91 |
| 3181 | I think it’s a good idea | 2 | 11.4 | 0 | 0 | 1.0 |

## B2 — 15 aulas para rever primeiro

| Aula | Título | Pontos | Palavras/fala | Curtas | Repetidas | Densidade alvo |
|---|---|---|---|---|---|---|
| 4078 | The more you practise, the better you get | 2 | 15.5 | 0 | 0 | 0.91 |
| 4072 | The man whose car was stolen | 2 | 15.7 | 0 | 0 | 1.0 |
| 4164 | A painter whose work I admire | 2 | 16.1 | 0 | 0 | 1.0 |
| 4086 | You’d better hurry | 2 | 16.6 | 0 | 0 | 1.0 |
| 4041 | He must have missed the bus | 2 | 17.5 | 0 | 0 | 1.0 |
| 4049 | She ought to have apologised | 2 | 17.8 | 0 | 0 | 1.0 |
| 4089 | Despite the rain, we went out | 2 | 17.8 | 0 | 0 | 1.0 |
| 4083 | I’m used to getting up early | 2 | 17.9 | 0 | 0 | 1.0 |
| 4059 | I’m getting my hair cut tomorrow | 2 | 18.0 | 0 | 0 | 0.91 |
| 4122 | I wish phones weren’t so addictive | 2 | 18.0 | 0 | 0 | 1.0 |
| 4157 | I’m looking forward to seeing you | 2 | 18.0 | 0 | 0 | 1.0 |
| 4081 | This time next week I’ll be flying | 2 | 18.1 | 0 | 0 | 1.0 |
| 4054 | The room is going to be painted | 2 | 18.5 | 0 | 0 | 1.0 |
| 4179 | I’m not used to writing so much | 2 | 18.5 | 0 | 0 | 1.0 |
| 4119 | I’d rather not take painkillers | 2 | 18.6 | 0 | 0 | 1.0 |
