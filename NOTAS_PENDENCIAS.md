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
