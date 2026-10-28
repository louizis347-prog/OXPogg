# Pogglot — balanço e pendências (19/10/2026)

## Feito
- Inglês regular A1–C2 (5.000 episódios): estrutura nova aplicada em todos (original + continuação enxuta, práticas alternadas, verbos 7+7, Monte a cena, cultura em quadros, ilustração em toda tela, textos cortados corrigidos).
- Leitura da regra (`rdg`): en-a1 a en-c2 completos.
- Conversa jogável (`rdgplay`): só 10 pares do A1.
- Cultura escrita à mão: A1 completo (388 obras); A2–C2 ainda usam texto-modelo.
- Neighbors: japonês 365, alemão 400, francês 400 (tools/nb/).

## Pendente (ordem sugerida)
1. Cultura caprichada A2–C2: escrever como tools/rdg/cult_a1_NN.py (use tools/dumpcult.py <cid> para listar as obras) e rodar tools/culture2.py <cid>.
2. `rdgplay` além dos 10 pares (tools/rdg/play_a1.py, tools/applyplay.py).
3. Telas de conteúdo que ainda rolam; espanhol A2–C2 e Neighbors não reorganizados.
4. Futuro: gerador de roteiro de estudo (tempo disponível → tutor).

## Regras de trabalho
Commit + push em main e claude/nifty-mendel-y3nbxt a cada mudança; sem PR; uma coisa por vez; relatórios em português.

## Deploy
Cloudflare (Workers com arquivos estáticos, wrangler.jsonc) ligado ao GitHub (branch main); cada push em main publica automaticamente.

## Estrutura do site
- `index.html` = landing de venda (porta de entrada). `app.html` = o aplicativo. Links antigos com `?ref=` ou `#/` na raiz são redirecionados ao app.
- Planos e preços da landing vêm de `config.js` (checkoutUrl, checkoutUrlYear, priceMonth, priceYear). Pagamento previsto: Hotmart, liberando acesso por webhook.
- Scripts em tools/ que editavam index.html agora editam app.html.

## Visual e conteúdo (outubro/2026)
- Tokens de design: `css/tokens.css` (cor, fonte, raio, espaço, sombra). Variáveis antigas (--pg-, --p2-, --px-, --rw) apontam para ele. Fonte única Plus Jakarta Sans; Literata só no texto de leitura (`--t-font-read`).
- Home: `css/home2.css`. Comunidade: `css/community3.css`. Landing de venda: `index.html` + `css/landing.css`.
- Player no computador (>=1100px) e tablet: `css/desk.css`. Celular continua com cartões compactos.
- "Sua vez" v2: `js/suavez.js` + `css/suavez.css` (camada sobre rework/m2/talk/ai; mantém IA, voz, estrelas, XP).
- Cenários ilustrados refinados: `js/scn_fine.js` (biblioteca `window.SF` + lobby1/lobby2), `scn_fine2.js` (home1, school), `scn_fine3.js` (street, park2, yard), `scn_fine4.js` (shop, diner, cafe2, cafe3). Se um falhar, o cenário antigo é usado. Ainda no estilo antigo, pouco usados: kitchen, bedroom, bath, clinic, office, gym, hall, counter, tick, sub2, airport2, flags.
- Continuações do inglês: `tools/cont_a1.py` (SPECS escritos à mão; testa as palavras-chave; parte do arquivo original no git). 12 de 2.500 reescritas (A1, arquivo 01).
- Publicação em `main` foi bloqueada pelo ambiente (produção): precisa de pull request ou permissão do dono.

## Menu
Menu inferior virou botão flutuante lateral (css/sidenav.css, js/sidenav.js).

## Modelo piloto (18 quadros) no inglês A1
- Itens 1–5 (outra sessão) e 86–110 (esta sessão, tools/model_v3.py + tools/v3/ep_*.py + js/chars2.js com 25 personagens novos).
- Para refazer: `python3 tools/model_v3.py` e conferir com `python3 tools/v3/check.py`.
- Curso regular de inglês reduzido de 5.000 para 3.000 episódios (A1 466, A2 474, B1 530, B2 510, C1 510, C2 510), por pares, proporcional por arco, mantendo todos os arcos, os 30 episódios piloto e ≥70% do vocabulário único (ferramenta: tools/audit/en_reduce.py). Revisões do 'episódio anterior' refeitas pela cadeia original (18 do A1 ficaram sem quadro de revisão). Conversão ao modelo piloto vale só para os itens restantes (fora os 30 já feitos).

## Programa gramatical do inglês regular (3.000 episódios)
- Programa por nível em `tools/gram/syllabus.py` (A1 31 estruturas, A2 26, B1 26, B2 25, C1 22, C2 20), cada uma com janela de progressão e mínimo de pares.
- `tools/gram/assign.py --apply` reatribuiu g.t/gs/fn de pares sem estrutura (marcados `regram:1`: 488 itens) para cobrir as estruturas faltantes na ordem certa. Pilotos e abertura/fechamento de nível intactos; vocabulário e títulos preservados.
- Pendência: os quadros já assados dos itens `regram` ainda trazem o conteúdo antigo; ao converter ao modelo piloto, escrever a lição na nova estrutura (g.t).

## Esqueletos do inglês regular (episódios não piloto)
- `python3 tools/skel/build.py` gera `data/skel/en-<nível>.json` (o app não lê) e `docs/esqueletos/en-<nível>.md`: 2.924 episódios (A1 390 a partir do 77º; A2 474; B1 530; B2 510; C1 510; C2 510). Cada um traz título, tema, obra, cenário, gramática, vocabulário, frase-gancho e o plano dos 19 quadros do modelo piloto.
- Limite: o plano dos quadros é derivado dos dados do episódio, não escrito um a um. Nos itens `regram` (488) o tema do episódio nem sempre combina com a gramática nova: revisar tema/obra ao escrever a aula.

## Espanhol A1 no modelo piloto
- Episódios 1–5 (71001, 7071001, 71002, 7071002, 71003) reescritos no modelo/visual do inglês: `tools/es/ep_*.py` + `python3 tools/model_es.py` (usa `model_v2.LG` com textos em espanhol). Personagens novos em `js/chars3.js` (Tokio, Río, Dom Quixote, Sancho, Chavo, Dona Florinda). O visual `regular-pilot-v1` agora vale para en-a1 e es-a1. Vocabulário e títulos do esqueleto mantidos; obras trocadas por obras em espanhol coerentes com o tema.

## Francês A1 para brasileiros (frbr-a1) no modelo piloto
- Episódios 1–5 (1000000–1000004) refeitos: `tools/fr/ep_*.py` + `python3 tools/model_fr.py`. Obras do próprio esqueleto (Le Petit Prince, Astérix, Ratatouille), personagens novos em `js/chars3.js` (Pequeno Príncipe, piloto, Astérix, Obélix, Linguini, Rémy). Vocabulário mantido (4 palavras do esqueleto + 2) e títulos placeholder ("A1 · Épisode N…") trocados por títulos reais. O `regular-pilot-v1` vale também para frbr-a1.
- Atenção: nesse curso o pareamento xn/xof dos itens iniciais está bagunçado no esqueleto (ep. 1,3,5 principais; 2,4 continuações); não mexi.

## Português (ES→PT), Italiano e Alemão: 5 primeiros episódios no modelo piloto
- pt-a1 (810000–810004, interface em espanhol), it-a1 (950000–950004), de-a1 (940000–940004). Montadores: `tools/model_pt.py`, `model_it.py`, `model_de.py`; episódios em `tools/pt|it|de/ep_*.py`. Cada episódio tem cenários próprios do tema (escritório, bar, sala, estação, mercado, cozinha, lago…), personagens novos em `js/chars4.js` (28) e `PogPerson` exposto por `js/chars3.js`.
- `model_v2.build` agora traduz os rótulos fixos via `LG['ui']` (usado em pt-a1) e `js/es_pilot.js` traduz os rótulos dos renderizadores para cursos com interface em espanhol (FXES_MAP).
- Correção de estouro de margem: `.ps-hb` (chips do vocabulário), `.m2-bagrow`/`.m2-bt` (mochila), `.ps-pair`, `.ps-rt`, `.ps-hot-info` agora quebram linha em telas ≤ 360px. Teste: `node ovf.js <curso> <largura> <n…>` (em /tmp) varre os quadros e toca os objetos da cena.
- Os esqueletos de it-a1/de-a1 tinham só placeholders ("A1 · Episodio 1: salutare al lavoro", vocabulário genérico): temas mantidos, vocabulário e obras escritos agora. O pt-a1 manteve vocabulário e gramática do esqueleto (tudo×todo, apelido≠apellido, meu/minha) com 2 palavras novas por par.

## Esqueletos com escolhas identificadas (inglês regular)
- `python3 tools/skel/build.py` regenera `data/skel/en-*.json` e `docs/esqueletos/*.md` (tabelas + `SITUACAO.md`). Cada esqueleto agora registra: estrutura gramatical, vocabulário da cena (6 palavras), 4 verbos e até 4 expressões, tudo vindo dos dados do próprio episódio (nada foi escrito). Esses campos aparecem nos quadros: palavras da cena, verbos (e missão dos verbos), expressões (e cena de conversa).
- Ficam de fora (não mexidos): episódios prontos (1–5, 52–76, 116–120 do A1) e os de formato antigo 6–51 e 77–115. Total com esqueleto: 2.880.
- Limites: as «expressões» vêm do quadro cexp (frases-modelo do episódio), não são necessariamente idioms; 6 pares do A1/A2 têm só 3 expressões; ~30% dos pares ainda só têm tema (sem estrutura gramatical própria).

## Roteiro simples dos episódios de inglês (tarefa #31) — CONCLUÍDO
- Páginas: `roteiro/index.html` + `roteiro/en-a1.html` … `en-c2.html` (tabela simples: episódio, título, estrutura gramatical, vocabulário, 4 verbos, 4 expressões comuns, 2 gírias, obra).
- Cobertura: 1.440 pares (A1 173, A2 237, B1 265, B2 255, C1 255, C2 255). Fora: episódios prontos (pilotos 1–120).
- Fonte editável: `tools/roteiro/<nivel>_NN.txt` (linha `n|verbos|exp=pt;…|giria=pt;…`). Regerar: `python3 tools/roteiro/build.py`.
- IMPORTANTE: `tools/skel/build.py` sobrescreve o enriquecimento; sempre rodar `tools/roteiro/build.py` depois.
- Limites: ~30% dos pares ainda têm só um tema em "estrutura gramatical"; gírias do A1 são leves; 488 temas de regram divergentes não corrigidos.

## Roteiro por episódio (atualização)
- Não existe mais "episódio-continuação": cada episódio (3.000 por curso) tem roteiro próprio.
- Inglês: `tools/roteiro/<nivel>_NN.txt` (principais) e `<nivel>_x_NN.txt` (segundos) → `python3 tools/roteiro/build.py` (deve mostrar faltando 0 em todos os níveis). Rodar sempre depois de `tools/skel/build.py`.
- Demais cursos regulares: `tools/plan/<cid>/<nivel>_NN.txt` → `python3 tools/plan/build.py` → `data/plan/<cid>.json` (lido pela telinha pré-episódio). Só ja A1 eps 1–50 feito.
- PDFs: `python3 tools/pdfplan/build.py <cid>` → `docs/planos/<cid>.pdf`.

## Inglês A1: episódios 121–160 no modelo piloto
- Escritos em `tools/v3/ep_121_125.py` … `ep_156_160.py` (mesmo `ep()` de `tools/v3/lib.py`). Obra, cenário e capa vêm dos episódios antigos (`tools/v3/obras_old_121_160.json`, via `OB()`); título, vocabulário, verbos, expressões e gírias vêm do roteiro.
- Montar: `python3 tools/model_v3.py <n…>`; conferir: `python3 tools/v3/check.py`; marcar padrão/apresentação: `python3 tools/v3/mark_pilot2.py`.
- Em vários itens a gramática do roteiro antigo não casava com o título (itens `regram`); a estrutura escolhida está em `pattern` de cada episódio. Pilotos até o episódio 175 (30033). Próximo: 176 (`7030033`, "Dial 911").

## Cobertura gramatical do A1 (auditoria após o 175)
- Nos episódios 121–175 troquei algumas estruturas do roteiro antigo pelas que combinavam com título e vocabulário. Ficaram sem episódio dedicado: advérbios de frequência (planejado no 161), numerais (11–16, dezenas, números grandes, ordinais) e reforço de there is/are, preposições de lugar e conectores (and/but/because/so).
- Esses itens foram transferidos para episódios pendentes em `tools/gram/plan_a1.py` (lista de episódio → estrutura que PRECISA aparecer). Rodar `python3 tools/gram/plan_a1.py` ao fechar cada lote: mostra OK / FALTA / pendente.

## Inglês A1: remodelagem dos 85 episódios antigos (6–51 e 77–115)

- Todos os 175 primeiros episódios do A1 de inglês estão no modelo piloto (`presentation: regular-pilot-v1`): 19 quadros (o episódio 1 tem 18, sem revisão), sem `cultob`, `cultx`, `read`, `lplay` ou `tdlg`.
- Cada episódio tem rótulo de gramática próprio (`g.t`), sem repetição entre vizinhos nem no bloco inteiro (os episódios 1–4 também foram corrigidos).
- Fontes: `tools/v3/ep_006_010.py` … `ep_112_115.py` (escritos com `tools/v3/short.py`, que deriva do texto escrito à mão as perguntas de revisão, o caça-sons e as missões). A obra e o cenário de cada episódio vêm de `tools/v3/obras_old_006_115.json` (guardados do quadro `cultob` antigo).
- `tools/model_v3.py` agora ordena os episódios pela posição no curso, monta a revisão do episódio anterior (inclusive dos 5 primeiros) e só reescreve arquivos de dados que mudaram, para não pisar em outros fluxos (episódios 179+).
- Próximo: episódio 176 em diante (outro fluxo já refez 179–184 em `tools/editorial/browser_english_N.py`).

## Inglês A1 até o episódio 200

- Remodelados no modelo piloto: 181–191 e 196–200 (`tools/v3/ep_181_185.py`, `ep_186_191.py`, `ep_196_200.py`). Os episódios 176–180 e 192–195 já tinham sido refeitos por outro fluxo.
- Os 200 primeiros episódios estão no modelo piloto, com rótulos de gramática únicos (nenhum repetido nem vizinho igual).
- `tools/gram/check_unique.py` não quebra mais quando o episódio já saiu do esqueleto; `tools/model_v3.py` monta a revisão também a partir de episódios feitos por outro fluxo.
- Próximo: episódio 201 em diante.

## Inglês A1 até o episódio 230 (correções + 201–230)

- Segundos episódios dos pares que repetiam as mesmas 6 palavras do primeiro foram refeitos com vocabulário, cena e frases próprios: 54–76 e 118–120 em `tools/v3/ep_fix_a.py` … `ep_fix_d.py` (usam `tools/v3/oldn.py` só para reaproveitar elenco e obra). O episódio 52 (7030010), que repetia 5 das 6 palavras do 51, foi refeito em `ep_fix_g.py`.
- Falas seguidas do mesmo personagem corrigidas nos episódios 44 (7030008), 53 (70020) e 123 (910011). Varredura de todos os quadros de 1 a 230: 0 repetições.
- Episódios 176–180 e 192–195 (Maya e Luis, de outro fluxo) reconstruídos no modelo: `ep_fix_e.py` e `ep_fix_f.py`, com 5 objetos, só dois falantes (a voz do gerente, da bibliotecária e do balcão virou fala reportada), opções de escuta sem repetição e cenários padrão. A obra continua em `tools/v3/obras_redo.json`.
- Episódios 201–230 novos: `tools/v3/ep_201_205.py` … `ep_226_230.py`. Cada um com gramática A1 própria (embalagens, fatias, Can I, May I, Show me, pagar, easy/hard, very/really, família ampliada, older/younger, lembranças, How is, tempo, o que vestir, also/too, both, cartas, e-mail, elogios, caimento, gostos, love/hate/prefer, cozinha, quantidades de receita, refeições, for here/to go, a lot of/a few/a little, empty/full/enough, mesa para dois, recomendação). As obras vêm de `tools/v3/obras_old_201_230.json`.
- Todos os rótulos de gramática de 1 a 230 são únicos e nenhum par de vizinhos divide 3 ou mais palavras de vocabulário.
- `tools/gram/plan_a1.py` foi atualizado: estruturas que ficaram sem episódio dedicado foram reatribuídas a episódios pendentes (247–250, 239–240) e as já cobertas apontam para o episódio onde aparecem. Resultado: faltando 0.
- Próximo: episódio 231 em diante (ainda no formato antigo). Obs.: o 195 e o 196 repetem `weekday`/`weekend` (2 de 6 palavras); se incomodar, trocar no 195 por Friday e Sunday.

## Inglês A1 até o episódio 250

- Episódios 231–250 refeitos no modelo piloto: `tools/v3/ep_231_235.py` … `ep_246_250.py`. Obras em `tools/v3/obras_old_231_250.json` (lidas por `OB()`).
- Gramática (rótulos únicos): from … to, It takes, Do you speak, learn/study/practice, enjoy + -ing, want to, -s/-es/-ies, Does he…?, always/never, often/rarely, How often, once/twice/three times, wash/brush/comb, Please don’t, at home/school/work, partes do dia, -teen, minutos past/to, hundred/thousand/million, graus (30–100).
- `tools/gram/plan_a1.py` agora aponta as estruturas para os episódios onde de fato aparecem; faltando 0. Nenhum rótulo repetido de 1 a 250, nenhum par de vizinhos com 3 ou mais palavras iguais, nenhuma fala seguida do mesmo personagem.
- Próximo: episódio 251 em diante (ainda no formato antigo).

## Inglês A1 até o episódio 466 (fim do A1)

- Episódios 251–466 refeitos no modelo piloto (19 quadros cada): `tools/v3/ep_251_255.py` … `ep_461_466.py`. Obras dos episódios 351–466 em `tools/v3/obras_old_351_466.json` (lidas por `OB()`). `tools/v3/fixmold.py` remove opções de molde com um único elemento.
- O curso A1 tem 466 itens; o pedido “até o 500” não pôde ser cumprido: 467–500 exigiriam 34 itens novos (o `model_v3.py` só reescreve itens que já existem em `data/en-a1_NN.json`). Decidir se vira um bloco extra de revisão do A1 ou o início do A2.
- Rótulos de gramática únicos em todo o A1 (`tools/gram/check_unique.py`: 0 repetidos); `check.py`: 0 problemas.
- `plan_a1.py` ainda aponta 3 itens FALTA: ep 312 (because), ep 347 (so/but com too) e ep 440 (often/sometimes no jardim).

## Inglês A2 completo (474 episódios)
- Os 474 itens do A2 (`data/en-a2_*`) estão no modelo piloto (19 quadros, mesma identidade visual), cada um com seu rótulo de gramática próprio (`tools/gram/check_unique_a2.py`: 0 repetidos).
- A2 201–474: as obras faltavam em `obras_old_a2.json`; foram geradas a partir dos itens antigos (`a`), com arte padrão.
- Reaproveitado dos itens antigos: tema, obra/cena cultural, vocabulário e elenco; todo o resto foi reescrito no formato atual.
- Fontes: `tools/v3/a2_001_005.py` … `a2_091_093.py`; para refazer: `python3 tools/v3/fixmold.py <arq>`, `COURSE=en-a2 python3 tools/model_v3.py`, `COURSE=en-a2 python3 tools/v3/check.py`, `COURSE=en-a2 python3 tools/v3/mark_pilot2.py`.
- A2 completo. Falta apenas uma checagem de cobertura do plano A2 (não existe `plan_a2`). Teste no navegador 243→474 sem erros.
- Decisão pendente com o usuário: A1 tem só 466 itens; 467–500 viraria bloco extra de revisão ou início do A2.

## Inglês B1: primeiros 370 episódios
- Os 370 primeiros itens do B1 (`data/en-b1_*`, 530 no total) estão no modelo piloto (19 quadros, mesma identidade visual), cada um com seu rótulo de gramática próprio (`tools/gram/check_unique_b1.py`: 0 repetidos de 370).
- Fontes: `tools/v3/b1_001_005.py` … `b1_361_370.py` (de 101 em diante os arquivos usam o atalho `tools/v3/b1h.py`, função `S`, que gera R, lab, mold, produce, mission2 e exp_scene a partir de dados compactos). Obras dos itens 1–370 em `tools/v3/obras_old_b1.json` (para os itens 101+ rodar antes `python3 /tmp/obras_b1.py <lo> <hi>`; o script gera a partir dos itens antigos).
- Para refazer: `python3 tools/v3/fixmold.py`, `COURSE=en-b1 python3 tools/model_v3.py`, `COURSE=en-b1 python3 tools/v3/check.py`, `COURSE=en-b1 python3 tools/v3/mark_pilot2.py`.
- Faltam os itens 371–530 do B1 e a checagem de cobertura do plano B1.

- B1 331–370 (20 pares): escritos por tools/v3/b1_331_340.py … b1_361_370.py; montagem e checagens em um passo só (`COURSE=en-b1 python3 tools/model_v3.py`, `check.py`, `mark_pilot2.py`, `tools/gram/check_unique_b1.py`) e teste sem gravar com `COURSE=en-b1 python3 tools/v3/dryrun.py b1_NNN_MMM`. A frase 'I have jet lag.' ganhou tradução mais precisa no ep. 82168 (dicionário de falas compartilhado: frases iguais devem ter a mesma tradução em todos os episódios).

- REGRA DE CONTEÚDO (B1 331–370 e seguintes): cada episódio, inclusive a continuação do par, tem obra, 6 palavras, 4 verbos, 3 sons do laboratório, cena e falas PRÓPRIOS (como nos 5 primeiros do A1); só o quadro de revisão (mochila) retoma o episódio anterior. A segunda cena ('Na conversa de verdade') usa `fill=` com 4 falas específicas, nunca as falas-padrão. `COURSE=en-b1 python3 tools/v3/dryrun.py b1_NNN_MMM` acusa repetição entre episódios vizinhos e enchimento. Obras das continuações ficam em `tools/v3/obras_new_b1_*.json`.
- Atenção: os itens 1–330 do B1 (outra sessão) ainda compartilham palavras, verbos e laboratório dentro do par (100%); não foram refeitos.

## Auditoria do inglês regular contra o modelo dos episódios 2–5 do A1 (outubro/2026)
- Modelo de referência (definido pelo dono): A1 7009801, 70001, 7070001 e 30001. Cada episódio tem obra, elenco, palavras, verbos, laboratório de sons, cena e falas PRÓPRIOS; só a revisão (mochila) retoma o anterior.
- Ferramenta: `python3 tools/audit/regular_model_audit.py` (critérios K1–K12; relatório em `tools/audit/regular_model_audit.json`). Corrige o mecânico: `python3 tools/audit/fix_mechanical.py` (teaser do fechamento e revisão do anterior; rodar SEMPRE depois de `model_v3.py`, que recria o teaser dos arquivos-fonte).
- Resolvido: teasers que apontavam para episódios removidos na redução do curso (89) e 1 revisão fora de ordem.
- Pendente (precisa de escrita): continuações que repetem obra/palavras/verbos/sons/objetos do original (A1 ≈226, A2 ≈233, B1 ≈165), falas de enchimento (B1 259, A2 3) e elenco/arte genéricos em vez dos personagens da obra (A1 429, A2 474, B1 370).

## B1 itens 1–85 (módulos b1_001_005 … b1_081_085): continuações e enchimento refeitos (outubro/2026)
- Camada `tools/v3/b1fix.py` (E com sobrescritas por episódio) + dados em `tools/v3/b1fix_data_a/b/c.py`; as obras novas saem em `tools/v3/obras_new_b1_001_085.json` (gerado ao importar). Cada módulo importa `E` de `v3.b1fix`.
- 54 episódios: 42 continuações com obra própria (real, ano e autor/diretor conferidos de memória; sem números não verificados), elenco com personagens da obra (ids existentes; Hermione/Harry, Tin Man/Glinda, Sherlock, Mulan, Peter/Hook via chars5), capa nova; vocabulário/verbos novos onde repetiam; 12 originais (e várias continuações) com falas próprias na segunda cena (sem 'Good./Coffee?/Please./Here.').
- Reconstruir só estes: `COURSE=en-b1 python3 tools/model_v3.py <n…>` (lista de n = chaves de `FIX`), depois `python3 tools/audit/fix_mechanical.py`.
- Pendente: K3/K4 (elenco/arte genéricos) nos demais episódios; os itens 86+ estão em outra frente (`ovrb1*.py`). Elenco com arte genérica (polly/tom/tommy/misshoney) quando não há ficha da obra: só o nome mudou.
- Verificação: dryrun/check.py sem problemas, auditoria sem K8/K9 nos módulos 1–85; fatos das obras NÃO checados por fonte externa (sem acesso à web nesta sessão).

## Auditoria do modelo — B1 itens 1–172 (publicado)
- Continuações dos itens 1–172 com obra, palavras, verbos, sons e falas próprios (camadas `tools/v3/b1fix*.py` e `ovrb1*.py`). Fatos das obras vieram de memória: revisar `obras_new_b1_001_085.json` e `obras_new_b1_086_170_*.json`.
- Auditoria B1 depois do lote: obra repetida 165→79, enchimento 259→158. Falta itens 173–330 (e 371–530), A2 e A1; elenco/arte genéricos (K3/K4) seguem altos.
- Sempre rodar `fix_mechanical.py` depois de `model_v3.py`.

## Auditoria do modelo — B1 itens 173–330 (publicado)
- Continuações e originais dos itens 173–330 reescritos (camadas `ovrb1_*.py`, obras em `obras_new_b1_173_250_*.json` e `obras_new_b1_251_330_a.json`). B1 inteiro (370): K8 obra/vocab/verbos/lab e K9 enchimento zerados; sobra K8 hot 3.
- Fatos das obras vieram de memória: revisar (em especial Mil e Uma Noites, Romeu e Julieta, Cachinhos Dourados). Em 7082121, 7081271, 7082140, 7082141 e 7082196 algumas falas de objeto quente padrão não combinam totalmente com a obra nova. 7082016 e 7082021: troca de texto antigo não encontrada.
- Próximo: elenco/arte genéricos (K3 54%, K4 89%), A2, A1, B1 371–530.

## Inglês A2 — 15 episódios publicados no modelo (7081001, 7081006, 7081007, 7920001, 7081008, 7081009, 7081011, 7081012, 7920002, 7081015, 7081016, 7081018, 7081019, 7920003, 7081022)
- Cada um com obra própria (Peter Rabbit, Peter Pan, Matilda, O Senhor dos Anéis, Heidi, Mulan, Aladdin, Dom Quixote, Harry Potter, Pinóquio, Hansel e Gretel, Mulherzinhas, Robinson Crusoé, Toy Story, Assassinato no Expresso do Oriente), sem repetir obra no curso. A2: obra repetida em vizinhos 233→218.
- O resto do trabalho A2 (≈226 episódios 1–240 e 241–474) está nos módulos (`ova2*.py`, `ova2b*.py`) mas NÃO foi reconstruído em data/. Lista de obras do 241–474 que colidem com 1–240: ver relatório do agente (Hound of the Baskervilles, Mary Poppins, Singin' in the Rain, Forrest Gump etc.). Fatos das obras vêm de memória.
- `fix_mechanical.py` sem argumento falha em B1 82258+ (hotscene sem `hot`): rodar com `en-a2` ou corrigir. 

## Inglês A2 — mais 15 episódios publicados (lote 2)
7081025, 7081027, 7081028, 7920004, 7030032, 7081030, 7081033, 7081034, 7920005, 7081037, 7081038, 7081040, 7920006, 7081043, 7080207 — cada um com obra própria (Robin Hood, 20 Mil Léguas Submarinas, Chapeuzinho Vermelho, Viagens de Gulliver, Il Postino, Pocahontas, O Rei Leão, Um Conto de Natal, A Festa de Babette, Bonequinha de Luxo, My Fair Lady, Karatê Kid, De Volta para o Futuro, Arca de Noé, João e o Pé de Feijão). Deixados de fora por colidir com obra de outro episódio do curso: 7081024 (O Jardim Secreto), 7081041 (O Lorax), 7081045 (Frozen). A2: obra repetida em vizinhos 203.

## Inglês A2 — lote 3 publicado (30 episódios): 81043 7030040 7070080 7920007 7080270 7081052 7081053 7081054 7081055 7081056 7080213 7081060 7081061 7081062 7920009 7081064 7081066 7920010 7081071 7081072 7081073 7081079 7081081 7081083 7030038 7070076 7920012 7081086 7081087 7081091
Cada um com obra própria, sem colidir com obra de outro episódio do curso. Deixados de fora por colisão: 7081024, 7081041, 7081045, 7920008, 7081059, 7081076, 7920011, 7081082, 7920013, 7081093, 7920014 (trocar a obra deles antes de publicar). A2: obra repetida em vizinhos 174. Lotes de 30 a partir daqui (script em scratchpad: escolhe candidatos de ova2, reconstrói, filtra colisões).

## Inglês A2 — lote 4 publicado (30 episódios): 7081092 7081095 7081097 7081099 7081100 7081102 7081104 7920015 7081106 7081107 7081109 7081110 7081112 7081113 7081114 7081116 7920017 81121 7081121 7081123 7081124 7081125 7081126 7920018 7081127 7081131 7920019 7081134 7081135 7081137
Obra própria, sem colisão no curso. A2: obra repetida em vizinhos 145. Ainda de fora por colisão: 7081024, 7081041, 7081045, 7920008, 7081059, 7081076, 7920011, 7081082, 7920013, 7081093, 7920014, 7920016, 7081122, 7081128, 7081146.

## Inglês A2 — lote 5 publicado (15 episódios): 7081138 7920020 7081145 7920021 7081148 7081149 7081150 7081151 7081154 7920022 7081155 7081158 7081164 7920024 7081170
Fim dos candidatos sem colisão da camada ova2 (itens 1–240). Faltam 17 deles (colidem com obra de outro episódio: 7081024, 7081041, 7081045, 7920008, 7081059, 7081076, 7920011, 7081082, 7920013, 7081093, 7920014, 7920016, 7081122, 7081128, 7081146 e outros): trocar a obra. Próximo: camada ova2b (241–474, ~120 episódios; colisões listadas no relatório do agente). A2: obra repetida em vizinhos 132.

## Inglês A2 — lote 6 publicado (20 episódios da camada ova2b, itens 241+): 7081178 7081179 7081195 7081197 7081205 7081212 7081214 7081218 7081221 7081223 81224 7081224 7081228 7920033 7081235 7081240 7081242 7081244 7920035 7081251
Obra própria, sem colisão no curso. Dos 60 candidatos só 20 passaram no filtro de colisão (nome normalizado). Os demais precisam trocar de obra. A2: obra repetida em vizinhos 114.

## Inglês A2 — lote 7 publicado (60 episódios, troca de obras repetidas)
7081024 7081041 7081045 7920008 7081059 81060 81071 7081076 7920011 7081082 7920013 7081093 7920014 7920016 7081122 81126 7081128 7081146 7920023 81164 7081169 81170 7081172 7081175 7920025 7081176 81177 7081177 81178 7081181 920026 7920026 7081183 7081187 7081189 7920027 7081190 81191 7081191 81194 7081194 81195 81196 7081196 7920028 81197 81201 7081201 81202 7081202 7081203 7920029 7081204 81209 7081209 7920030 7081211 81216 7081216 7081217
Camadas: ova2_zz_a/ova2b_241_zz_a|b|c (novas obras de literatura, cinema, séries/teatro/jogos/mitos). A2: obra repetida em vizinhos 71; 386 obras distintas em 474 episódios (faltam lotes 2 e 3 de 148 trocas).

## Inglês A2 — fim da troca de obras repetidas (88 episódios, lotes 8–9)
Agora o A2 tem 474 obras distintas em 474 episódios (checagem com nome normalizado nos dados). Auditoria A2: K8 obra/vocab/lab/hot e K9 zerados; resta 1 repetição de verbos (7081241 com o vizinho). Falta: elenco/arte genéricos (K3/K4), revisão dos fatos das obras (memória), teste no navegador. Próximos: A1 (226 obras repetidas) e B1 371–530.

## Inglês A1 — troca de obras repetidas (263 episódios, publicado)
A1 passa a ter 466 obras distintas em 466 episódios (checagem com nome normalizado nos dados). Auditoria A1: K8 obra zerado; sobram repetições pontuais de hot (3), lab (1), verbos (3), vocab (4) entre vizinhos. Camadas: `ova1_zz_a/b/c`, dados `zz1_*`, `zz_b_*`, `zzc1_*`; 31 episódios dos módulos ep() longos trocados direto por `zz1_full`. Os 4 episódios de referência (2–5) intocados. Pendente: arte genérica (K4 94%), K12 (25), fatos das obras (memória), revisão no navegador. Obras que repetem com o A2 (ex.: The Martian, Tarzan) e outros níveis: ver relatórios dos agentes.

## Inglês B1 — troca de obras repetidas nos 370 episódios convertidos (107 trocas, publicado)
B1 (370 no modelo piloto): 370 obras distintas em 370 episódios (checagem com nome normalizado nos dados); K8 obra/vocab/verbos/lab e K9 zerados, sobram 3 repetições de objetos quentes. Camadas `ovrb1_zz_a/b/c` (literatura, cinema, séries/teatro/jogos/mitos). Pendente: B1 371–530 (160 episódios, formato antigo), elenco/arte genéricos (K3 41%, K4 92%), K12 (95), fatos das obras (memória), teste no navegador. Muitas obras do B1 também aparecem em outros níveis (regra aplicada só dentro de cada curso).

## Inglês B1 — 160 episódios restantes convertidos (371–530, publicado)
B1 completo: 530 episódios no modelo piloto, 530 obras distintas (contrato `tools/audit/regular_pilot_contract.py`: 0 falhas; `check.py`: 0 problemas; `check_unique_b1.py`: 0 repetidos de 530). Autoria por quatro agentes por categoria (literatura 371–410, cinema 411–450, séries/teatro/quadrinhos 451–490, jogos/músicas/pinturas/podcasts/mitos 491–530) com helpers `b1lit.py`, `b1cin.py`, `b1x_lib.py`, `n4h.py`. Pendente: arte/elenco genéricos (K4 92%), K12 (135), fatos das obras (memória), 3 repetições de objetos quentes, teste no navegador; obras também aparecem em outros níveis (regra só dentro do curso).

## Trava de qualidade + plano por episódio (inglês C1 e C2 mapeados)
Ver `docs/PLANO_E_TRAVA.md`. en-c1 e en-c2: 1.020 episódios mapeados (foco, gs, obra, 4 verbos, 4 expressões), validação conjunta 0 erros (obra única entre C1+C2 e fora das 1.360 já em uso no inglês; expressões e gs únicos). Pendente: revisar naturalidade das expressões, fatos/anos das obras (memória), ligação frouxa obra×foco (`plano/REVISAR_C1_C2.md`). Próximo: espanhol (es-a1…es-c2).

## Plano por episódio — espanhol A1 mapeado
es-a1: 495 episódios mapeados (foco, gs, obra do mundo hispânico, 4 verbos e 4 expressões em espanhol), validação conjunta 0 erros (obra, expressão e padrão únicos; vizinhos sem 2+ verbos iguais). 108 obras sem ano (memória). Detalhes em `plano/REVISAR_ES_A1.md`. Próximo: es-a2, es-b1, es-b2, es-c1, es-c2 (2.500 episódios).

## Inglês B2 — episódios 416–510 (95) no modelo piloto
B2: 510/510 no contrato (`regular_pilot_contract.py --course en-b2`: 0 falhas). Autoria por três agentes com letras de obra distintas, briefs com foco único em `tools/b2gen/briefs_416_447|448_479|480_510.json`, validação conjunta `try.py` 0 problemas. Pendente: refazer 940001 e 7083006 (obra do campo `a.w` diferente da capa/figurinha; módulo `b2_fix_05`), teaser do 447 ("Next Lesson") para o título real do 448, fatos das obras (memória), ligação frouxa obra×foco em alguns, resíduo de expressão trocada em falas isoladas (418, 421, 444). `mark_pilot2.py` agora aceita en-b2 (mas reescreve g/gs de episódios já prontos: usar só com cuidado).

## Inglês B2 — fechamento
940001 (The Winslow Boy) e 7083006 (The Conversation) refeitos em `tools/v3/b2_fix_05.py`; teaser do 447 corrigido. B2: 510 episódios, 510 obras distintas, contrato 0 falhas, trava sem falhas no en-b2. Pendente: fatos das obras (memória), ligação frouxa obra×foco, resíduo de expressão trocada em 418/421/444, arte genérica, teste no navegador.
