# Pocket A1 · Mapa de 800 episódios

Objetivo do A1: vocabulário amplo + conversar sobre muitos assuntos, sem repetir padrões de fala.

## Regra ímpar / par
- **Ímpar (1, 3, 5…)**: situação do dia a dia (os 210 atuais + 190 novos = 400).
- **Par (2, 4, 6…)**: "continuação" do ímpar. Mesmo cenário ou personagem como ponte, mas com **outro tema, outro vocabulário e outro padrão** (filmes, séries, bichos, espaço, música, esporte, ciência, arte, mitos, jogos, mundo do trabalho, natureza…). 400 episódios novos.
- Cada par = 1 padrão novo no ímpar + 1 padrão novo no par. Nenhum padrão novo se repete como "novo".

## Limite de nível (CEFR A1) — regra rígida
Permitido: *to be*, *have*, *can*, imperativo, *there is/are*, presente simples, presente contínuo básico, *like/want/need*, *this/that*, plurais, preposições simples, números, horas, cores, perguntas wh- simples.
Blocos prontos aceitos (sem ensinar a gramática): *I would like…*, *Can/Could you…?*, *May I…?*, *Let us…*.
**Proibido no A1**: futuro (*will*, *going to*), passado (*was/were*, *did*, verbos no passado), *should*, *have to*, *used to*, presente perfeito, comparativos longos, condicionais.
Passado e futuro ficam para o A2 (reserva em `tools/pocket/reserva_a2/`). Porta automática: `tools/pocket/audit_nivel.py`.

## Estágios (80 episódios cada = 40 pares)
| # | Episódios | Padrões novos |
|---|-----------|---------------|
| 1 | 1–80 | I am / you are, my name is, where are you from, this/that, cumprimentos, please/thanks, números 1–20, Can I have… |
| 2 | 81–160 | have/has, possessivos, família, horas, dias, a/an, plural, what is this, cores |
| 3 | 161–240 | wh-perguntas, there is/are, how much/many, preposições de lugar, direções simples, Do you have… |
| 4 | 241–320 | presente simples (I/you/we/they), he/she (-s), do/does, advérbios de frequência, rotina |
| 5 | 321–400 | can/can't, like/love/want/need + substantivo e + to, comida, pedidos, I would like |
| 6 | 401–480 | presente contínuo (agora), clima, roupas, descrever pessoas e lugares, adjetivos |
| 7 | 481–560 | some/any, contáveis/incontáveis, compras, dinheiro, lugares da cidade, transporte |
| 8 | 561–640 | imperativo, instruções, regras e placas, saúde e corpo, casa e objetos |
| 9 | 641–720 | pronomes (me/him/her…), and/but/or/because simples, gostos, opiniões curtas, convites com Let us |
| 10 | 721–800 | revisão por temas, mini-diálogos mistos, grande final do A1 |

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
Cada episódio atual é etiquetado por estágio (pelo padrão em K) e assume uma vaga ímpar do estágio. Os arcos 17 (passado) e 18 (futuro) foram para a reserva do A2. Dos demais, cerca de 94 episódios ainda têm will/passado/should/have to espalhados e serão reescritos antes de entrar no mapa.

## Ordem de trabalho
1. Gerar o mapa/CSV com a etiquetagem manual dos 210. 
2. Escrever o estágio 1 completo (80) como piloto: ver o tom dos pares.
3. Seguir estágio a estágio, validando padrões e vocabulário.


## Ordem pedagógica atual (revisada)
`tools/pocket/ordenar.py`:
1. **Trilha curada à mão** (≈110 episódios): primeiros contatos → pedir o básico → eu e as pessoas → lugares, casa e cidade.
2. **Resto por blocos de assunto**, cada bloco mantendo a sequência interna em que foi escrito. A ordem dos blocos é definida à mão (`ORD_DIA`, `ORD_TEMA`), do mais simples ao mais rico. Ímpar = dia a dia, par = tema, intercalados em proporção.
3. Revisões finais ("Everything you know", "Look how much you know", "A full day") no fim.
Mapa auditável: `tools/pocket/mapa_a1.csv`. Para novos episódios: escreva o arco e acrescente o número em `ORD_DIA` ou `ORD_TEMA`.
