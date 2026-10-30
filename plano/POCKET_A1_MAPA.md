# Pocket A1 · Mapa de 800 episódios

Objetivo do A1: vocabulário amplo + conversar sobre muitos assuntos, sem repetir padrões de fala.

## Regra ímpar / par
- **Ímpar (1, 3, 5…)**: situação do dia a dia (os 210 atuais + 190 novos = 400).
- **Par (2, 4, 6…)**: "continuação" do ímpar. Mesmo cenário ou personagem como ponte, mas com **outro tema, outro vocabulário e outro padrão** (filmes, séries, bichos, espaço, música, esporte, ciência, arte, mitos, jogos, mundo do trabalho, natureza…). 400 episódios novos.
- Cada par = 1 padrão novo no ímpar + 1 padrão novo no par. Nenhum padrão novo se repete como "novo".

## Estágios (80 episódios cada = 40 pares)
| # | Episódios | Padrões novos (ordem de entrada) |
|---|-----------|----------------------------------|
| 1 | 1–80 | I am / you are, this/that, cumprimentos, números, please/thanks, Can I have…, my name is, where are you from |
| 2 | 81–160 | have/has, possessivos, like/love, família, horas, dias, a/an, plural, what's this |
| 3 | 161–240 | wh-perguntas, there is/are, how much/many, preposições de lugar, direções, I would like, do you have |
| 4 | 241–320 | presente simples I/you/we/they, he/she (-s), do/does, advérbios de frequência, can/can't, rotina |
| 5 | 321–400 | presente contínuo, tempo/clima, roupas, descrever pessoas/coisas, adjetivos, cores |
| 6 | 401–480 | want/need/like + to/ing, some/any, contáveis, compras, comida, pedidos |
| 7 | 481–560 | was/were, passado regular, expressões de tempo (ago, last, yesterday) |
| 8 | 561–640 | passado irregular, perguntas/negativas no passado, contar histórias |
| 9 | 641–720 | going to, will, should, have to, may/could, convites, planos |
| 10 | 721–800 | comparativos/superlativos, because/so/but, imperativo, conectores, revisão geral, grande final |

## Domínios de vocabulário (distribuídos entre os pares; cada um aparece em ≥3 estágios)
Cotidiano: casa, cidade, transporte, compras, comida, saúde, trabalho, escola, tecnologia, dinheiro.
Variados (pares): animais, natureza, espaço, mar, clima extremo, música, instrumentos, cinema (set de filmagem), séries (sitcom, médica, policial), sci-fi, fantasia, super-heróis, aventura, mistério, esportes, jogos, arte, museu, moda, história leve, mitos, ciência e laboratório, circo, parque de diversões, fazenda, floresta, deserto, polo, ilha, vulcão, festas do mundo, profissões diferentes, reality de culinária, show de talentos, viagem no tempo, detetive, robôs.
Regra: personagens e cenas de gênero são **originais**, nunca obras reais.

## Anti-repetição
1. Cada episódio tem 1 padrão-chave (campo K) e 1 campo de padrão de fala/escrita; o validador falha se o K repetir.
2. Padrões só podem usar gramática de estágios ≤ atual (nada de passado antes do estágio 7; os atuais arcos 16–20 serão realocados).
3. Vocabulário: cada palavra é "nova" uma vez; revisitas contam como reforço (≥3 episódios depois).
4. Mapa auditável: `tools/pocket/mapa_a1.csv` (ordem, estágio, ímpar/par, K, domínio, palavras novas) é gerado e checado a cada build.

## Como encaixar os 210 atuais
Cada episódio atual é etiquetado por estágio (pelo padrão em K) e assume uma vaga ímpar do estágio. Estimativa grosseira por regra automática: ~90 em estágios 1–2, ~30 em 3, ~26 em 4, ~13 em 5, ~15 em 7, ~22 em 9, ~5 em 10. Lacunas (estágios 2, 6, 8, 10 e o resto do 5/7/9) são preenchidas por ímpares novos. Ids passam a seguir a ordem final (950001…950800).

## Ordem de trabalho
1. Gerar o mapa/CSV com a etiquetagem manual dos 210. 
2. Escrever o estágio 1 completo (80) como piloto: ver o tom dos pares.
3. Seguir estágio a estágio, validando padrões e vocabulário.
