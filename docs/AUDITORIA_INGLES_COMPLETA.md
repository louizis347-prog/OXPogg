# Auditoria completa do curso regular de inglês (A1–C2)

Gerada em 28/10/2026 sobre o `main` (3.000 episódios) por `tools/audit/auditoria_completa_en.py` (números brutos em `docs/AUDITORIA_INGLES_COMPLETA.json`). As checagens são estruturais e heurísticas: nenhuma substitui a leitura humana dos episódios.

## Resumo

| Critério combinado | Resultado | Situação |
|---|---|---|
| 3.000 episódios no modelo de 19 quadros | 3.000 de 3.000 | OK |
| Densidade (6 palavras, 4 verbos, 4 expressões, 3 missões, laboratório, fala) | A1–B2 uniforme; C1/C2 abaixo | Parcial |
| 3.000 referências culturais distintas | 2.770 obras distintas; 0 títulos idênticos | Não atendido |
| Obras no idioma e no contexto do curso | ≈569 títulos em espanhol e ≈42 em alemão, francês ou italiano | Problema |
| Conteúdo próprio por episódio (sem pares) | C1/C2 ainda com cenas copiadas entre vizinhos | Não atendido em C1/C2 e parcial em B1/B2 |
| Ponte da obra | Capa, gancho e figurinha citam a obra em 100%; missão cita em 36% (A1) a 100% (C1/C2) | Parcial |
| Capas refinadas | Arte própria **não aparece no app** (bug abaixo) | Quebrado |
| Trava de qualidade (contrato do piloto) | 0 falhas no A1; 116 / 238 / 175 / 397 / 378 episódios com falha de A2 a C2 | Parcial |

## 1. Padrão estrutural

- Os 3.000 episódios têm a sequência de 19 quadros (ou 18, sem o quadro de revisão, no primeiro) e a etiqueta `regular-pilot-v1`.
- Contrato do piloto (`regular_pilot_contract.py`): A1 0 falhas; A2 116; B1 238; B2 175; C1 397; C2 378 episódios.
- Alertas do `regular_model_audit.py` por nível, em % dos episódios:
  - K10 (capa sem "Em 10 minutos"): A2 22%, B1 42%, B2 46%, C1 100%, C2 100%.
  - K7 (revisão não é do episódio anterior): A2 24%, B1 42%, B2 33%, C1 100%, C2 100%.
  - K6 (teaser não aponta para o próximo): C1 79%, C2 80%.
  - K8 (repete hot, vocabulário ou verbos do vizinho): B1 20% de hot; C1 41% de hot e 50% de vocabulário; C2 32% de hot e 50% de vocabulário.
  - K4 (arte de personagem genérica, usada em 4 ou mais obras): A1 94%, A2 91%, B1 97%, B2 34%, C1 e C2 100%.

## 2. Referências culturais

- 2.770 obras distintas (normalizadas) em 3.000 episódios; 187 obras aparecem em mais de um episódio (417 episódios). Não há título idêntico: a unicidade literal foi obtida com subtítulos (ex.: "The Great Gatsby: The Party"), então a mesma obra continua sendo usada em até 6 episódios (Rear Window, The Wizard of Oz, Charlotte's Web, The Great Gatsby, It's a Wonderful Life…).
- Repetições por nível: A1 62, A2 98, B1 108, B2 41, C1 43, C2 65 episódios. Há repetição entre níveis (ex.: The Wizard of Oz no A1, B1 e duas vezes no C2).
- Língua e contexto: ≈569 obras têm título em espanhol (A2 49, B1 114, B2 143, C1 175, C2 85), como "Verano azul", "El señor presidente" e "Los fusilamientos del 3 de mayo", e ≈42 em alemão, francês ou italiano. O padrão sugere que parte das referências veio do curso de espanhol. Precisa de decisão editorial: obra estrangeira só se o episódio de fato a ensinar em inglês (ex.: filme traduzido).
- 174 episódios têm como "obra" uma cidade, tradição, lugar, instituição ou empresa, e não uma obra cultural.
- Texto de modelo vazando para o aluno: 11 (A1), 12 (A2), 3 (B1), 2 (B2), 150 (C1) e 174 (C2) descrições começam com "Cultural anchor:"; outras repetem o esqueleto "{obra} (20th century / siglo XX) é a referência cultural principal desta aula…" (100 episódios, em 7 esqueletos).
- Categoria incoerente: ex. C2 "The Death and Life of Great American Cities" aparece como "Canção". Em C1, 168 episódios têm categoria genérica "obra".

## 3. Conteúdo próprio por episódio

- Títulos repetidos: 31 títulos (63 episódios).
- Expressões: 12.000 ensinadas, 11.391 distintas; 543 expressões aparecem em mais de um episódio (ex.: "dig in" em 4; "well done", "oh no", "excuse me" em 3).
- Falas de cena iguais em outros episódios: o percentual médio das falas da cena 1 que reaparecem em outro episódio é A1 0,6%, A2 18,7%, B1 33,9%, B2 25,0%, **C1 54,8% e C2 50,3%**.
- Vizinhos com mais de 50% das falas da cena 1 iguais: A2 24, B1 104, B2 75, **C1 301, C2 287**. É o formato antigo de "pares" (episódio e continuação), exatamente o que foi descartado no A1, no A2 e no B2 reformulado.
- Títulos em português puro (formato de par): A1 28, A2 69, B1 134, B2 5, C1 192, C2 236 (heurística; no A1 o formato "português · padrão em inglês" é o do modelo).

## 4. Ponte da obra

Percentual de episódios em que o nome da obra aparece (heurística por palavras):

| Nível | Capa | Gancho | Cena | Missão | Cena e missão | Figurinha |
|---|---|---|---|---|---|---|
| A1 | 100% | 100% | 91% | 36% | 33% | 100% |
| A2 | 100% | 100% | 95% | 56% | 52% | 100% |
| B1 | 100% | 100% | 89% | 55% | 48% | 100% |
| B2 | 100% | 100% | 90% | 84% | 76% | 100% |
| C1 | 100% | 100% | 97% | 100% | 97% | 100% |
| C2 | 100% | 100% | 99% | 100% | 99% | 100% |

O nome aparecer não prova que a obra mude a aula. No C1/C2 a menção é mecânica (texto de modelo: "Em {obra}, …"). O A1, A2 e B1 têm a missão pouco conectada à obra.

## 5. Capas e identidade visual

- **Bug que desativa a arte por obra no app.** `js/obra-art.js` (`has()`) lê `window.P`, mas no `app.html` o player é declarado com `let P`, então `window.P` é sempre indefinido. Resultado: em 30 episódios amostrados (5 por nível) nenhum recebeu a arte por obra nem o tema de cor (`obraSvg=false`, sem classe `ot-*`). A capa mostrada continua sendo a cena genérica do modelo.
- A arte desenhada à mão que eu havia feito para os 10 primeiros episódios foi sobrescrita quando `js/obra-art.js` foi reescrito em paralelo (gerador procedural para os 3.000). A landing e a home usam `PogObra.svg(<número>)` e `PogObra.face(<id do personagem>)`, que não existem mais na nova API (`svg(e, modo)`), e hoje caem na arte genérica.
- Cenários distintos no modelo: 31; vizinhos com o mesmo cenário (`rs`): 1.546 pares; 722 personagens distintos, 21 deles usados em 4 ou mais obras (afeta 1.626 episódios).

## 6. Densidade

Mediana por nível: 6 palavras, 4 verbos, 4 expressões, cena 1 com 8 a 9 falas, cena 2 com 8, 3 missões, 3 pares no laboratório, 5 frases de fala, 19 quadros, em A1 a C2. Referência A1 (episódios 2 a 5): 6/4/4, cena 8/6, 24 perguntas nas folhas de prática.

- Perguntas nas folhas de prática: A1–B2 mediana 24; **C1 e C2 mediana 15 (-38%)**.
- Laboratório de sons com menos de 3 pares: 255 episódios do C1 e 255 do C2 (metade de cada nível).
- Texto em inglês por episódio (mediana, caracteres): A1 16.306; A2 16.650; B1 17.369; B2 19.392; C1 18.435; C2 19.382, sem episódios abaixo de 70% da mediana do nível.
- A uniformidade dos números não prova densidade real: onde as cenas são copiadas (C1/C2), o conteúdo efetivamente novo é menor.

## 7. O que não foi auditado

Fatos sobre as obras (datas, autores, enredos), qualidade e naturalidade do inglês e do português, adequação das traduções e a correção pedagógica das respostas. Nada disso é verificável por script.

## 8. Plano sugerido (do que mais pesa ao que mais custa)

1. Corrigir o bug de `window.P` em `js/obra-art.js` e religar a arte e o tema por obra. É uma linha. Depois reintegrar as 10 capas desenhadas à mão como arte "premium" por cima do gerador procedural.
2. Decidir a política de obras estrangeiras (espanhol, alemão, francês) e trocar as ≈610 que não devem ficar no curso de inglês.
3. Limpar o texto de modelo que vaza ("Cultural anchor:", "(siglo XX)", esqueletos repetidos) e corrigir as categorias.
4. Reescrever C1 e C2 como episódios independentes (cenas, vocabulário e hot próprios): hoje 301 e 287 pares com cena copiada. Fazer o mesmo, em menor escala, em B1 e B2.
5. Trocar as 417 repetições de obra por obras novas (primeiro as que se repetem entre níveis).
6. Levar C1/C2 ao modelo de densidade do A1 (24 perguntas, 3 pares de laboratório) e corrigir o teaser, o "Em 10 minutos" e a revisão em A2–C2.
7. Revisão humana por amostragem de fatos, traduções e respostas.
