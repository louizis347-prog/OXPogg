# Qualidade automática das aulas (fila de revisão)

Gerado por `professor/tools/quality_report.py`. Os pontos somam alertas (mais pontos = aula que merece reescrita ou revisão primeiro): média de palavras por fala abaixo do esperado do nível (2), 3+ falas curtas (1), 3+ falas repetidas de outras aulas (2), estrutura-alvo em ≥85% das falas (2; só mede A2 em diante, onde o foco vem do plano). A ligação da obra cultural com o tema NÃO é medida (a nota está em português e o diálogo em inglês; qualquer comparação automática seria enganosa): esse ponto precisa de leitura humana. **É um filtro automático; não substitui revisão humana.**

## Resumo por nível

| Nível | Aulas | Média de palavras/fala | Aulas com ≥3 pontos | Aulas com ≥5 pontos |
|---|---|---|---|---|
| A1 | 500 | 6.2 | 117 (23%) | 11 |
| A2 | 500 | 8.9 | 3 (1%) | 0 |
| B1 | 500 | 12.0 | 0 (0%) | 0 |
| B2 | 200 | 18.1 | 0 (0%) | 0 |

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
| 2120 | Spell it, please | 3 | 6.1 | 3 | 0 | 0.0 |
| 2011 | The wrong train | 3 | 8.4 | 3 | 11 | 0.0 |
| 2411 | A city bus tour | 3 | 8.4 | 3 | 11 | 0.0 |
| 2113 | Something to drink | 2 | 7.6 | 0 | 0 | 0.91 |
| 2317 | A walk in the forest | 2 | 8.2 | 1 | 0 | 1.0 |
| 2073 | The tallest building | 2 | 8.4 | 0 | 0 | 1.0 |
| 2021 | There was a problem | 2 | 8.7 | 0 | 11 | 0 |
| 2421 | A clean beach | 2 | 8.7 | 0 | 11 | 0.0 |
| 2053 | It’s going to rain | 2 | 8.9 | 0 | 0 | 0.91 |
| 2061 | You should rest | 2 | 9.1 | 1 | 10 | 0 |
| 2361 | A text from a friend | 2 | 9.1 | 1 | 10 | 0.64 |
| 2381 | Halloween costumes | 2 | 9.1 | 0 | 6 | 0.64 |
| 2081 | How much is it? | 2 | 9.2 | 0 | 6 | 0.09 |
| 2410 | A bike path | 2 | 9.4 | 0 | 0 | 0.91 |
| 2346 | A short story | 1 | 7.8 | 3 | 1 | 0.27 |

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
| 3425 | Is it safe to take with milk? | 2 | 10.8 | 0 | 0 | 0.91 |
| 3077 | He has never been late | 2 | 11.0 | 0 | 0 | 0.91 |
| 3139 | Mom said dinner was ready | 2 | 11.2 | 0 | 0 | 0.91 |
| 3255 | The soup needs more salt | 2 | 11.2 | 0 | 0 | 1.0 |
| 3164 | I’m going to learn to swim | 2 | 11.3 | 0 | 0 | 1.0 |
| 3485 | She seems to be tired | 2 | 11.3 | 0 | 0 | 0.91 |
| 3181 | I think it’s a good idea | 2 | 11.4 | 0 | 0 | 1.0 |
| 3152 | She wants to learn Spanish | 2 | 11.6 | 0 | 0 | 0.91 |

## B2 — 15 aulas para rever primeiro

| Aula | Título | Pontos | Palavras/fala | Curtas | Repetidas | Densidade alvo |
|---|---|---|---|---|---|---|
| 4078 | The more you practise, the better you get | 2 | 15.5 | 0 | 0 | 0.91 |
| 4072 | The man whose car was stolen | 2 | 15.7 | 0 | 0 | 1.0 |
| 4164 | A painter whose work I admire | 2 | 16.1 | 0 | 0 | 1.0 |
| 4086 | You’d better hurry | 2 | 16.6 | 0 | 0 | 1.0 |
| 4059 | I’m getting my hair cut tomorrow | 2 | 18.0 | 0 | 0 | 0.91 |
| 4122 | I wish phones weren’t so addictive | 2 | 18.0 | 0 | 0 | 1.0 |
| 4081 | This time next week I’ll be flying | 2 | 18.1 | 0 | 0 | 1.0 |
| 4179 | I’m not used to writing so much | 2 | 18.5 | 0 | 0 | 1.0 |
| 4119 | I’d rather not take painkillers | 2 | 18.6 | 0 | 0 | 1.0 |
| 4149 | Whoever wins, nothing will change | 2 | 18.6 | 0 | 0 | 0.91 |
| 4085 | I’d rather stay home tonight | 2 | 18.7 | 0 | 0 | 1.0 |
| 4090 | Whether or not you agree | 2 | 18.9 | 0 | 0 | 1.0 |
| 4138 | Despite the delay, we enjoyed the trip | 2 | 19.7 | 0 | 0 | 1.0 |
| 4184 | I wish people would use bikes more | 2 | 19.7 | 0 | 0 | 0.91 |
| 4137 | She suggested we take the night train | 2 | 19.8 | 0 | 0 | 0.91 |
