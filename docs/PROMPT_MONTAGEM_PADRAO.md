# Roteiro-padrão de montagem de episódio (cursos regulares)

Modelo exato: os quatro episódios de referência do inglês A1 — **n=7009801** (Alice no País das Maravilhas), **n=70001** (O Mágico de Oz), **n=7070001** (Peter Pan) e **n=30001** (Toy Story). Tudo o que está aqui foi lido desses episódios (`data/en-a1_*.json`) e do contrato `tools/audit/regular_pilot_contract.py`. Vale para todos os cursos regulares (inglês, espanhol, francês, alemão, italiano, japonês, coreano, português, chinês…), nunca para o Neighbors.

Como usar: copie o **PROMPT-MESTRE** (seção 11) e preencha os campos `{…}` com a ficha do episódio em `plano/<curso>.json`. As seções 1–10 são a especificação que o prompt cita.

---

## 1. Princípios (não negociáveis)

1. **Cada episódio é novo.** Par ou ímpar, continuação ou não: tem a sua obra, o seu padrão (`gs`), as suas 6 palavras, 4 verbos, 4 expressões, 3 sons, os seus objetos da cena, as suas falas e perguntas. **A única coisa que retoma o episódio anterior é a mochila de revisão** (quadro 2).
2. **Obra cultural única.** Uma referência real e conhecida (livro, filme, série, peça, poema, música, quadro, jogo, desenho, lenda…), **que não se repete em nenhum outro episódio do curso**. A cena é autoral: fala *como* os personagens da obra, não copia nem cita trechos protegidos.
3. **Densidade fixa.** 19 quadros, nessa ordem, com essas contagens (seção 3). O contrato automático reprova o que fugir.
4. **O padrão do dia é o centro.** Título, capa, regra, molde, cenas, perguntas, missões e fechamento ensinam o mesmo padrão (`gs`) e nada do episódio vizinho.
5. **Fatos só se verdadeiros.** Ano, autor, enredo da obra: só o que você tem certeza. Sem número inventado.
6. **Língua natural.** Idioma-alvo correto e falado de verdade; português do Brasil natural; tradução fiel.

## 2. Entradas do episódio (vêm do plano)

| Campo | Descrição |
|---|---|
| `n`, `pos` | identificador e posição no curso |
| `foco` | uma frase: o que o episódio ensina (único no curso) |
| `gs` | rótulo curto e **único** do padrão (ex.: “He's · She's”) |
| `obra` | nome, tipo, criador, ano (se certo) — única no curso |
| `verbos` | 4 verbos distintos (nunca 2+ iguais aos do episódio anterior) |
| `expressoes` | 4 expressões/gírias/colocações reais, **únicas no curso** |
| `quadros` | os 19 quadros formatados e vazios (seção 3) |

## 3. Os 19 quadros, na ordem e com as contagens exatas

Todo quadro tem `k` (tipo). A maioria leva também `rs` (cenário), `chars` (personagens na cena, `[id, x%, olha(0/1), escala]`), `say` (fala curta do guia que abre o quadro) e, nos de prática, `bubble`/`avatar` (o personagem “fala” a pergunta).

1. **`cover` — Capa.** `art` (cenário `s`, 3–5 emojis de ambiente `[emoji,x,y,tamanho,"bob"]`, `seed`), `sub` = “*<padrão>*: **em 10 minutos você** *<ação concreta>* como *<personagem da obra>*”, `badge` (nível), `snd` (som de abertura), `say` (2 frases: o contexto e a pergunta-gancho), `gancho` = `[personagem, fala na língua-alvo, tradução]` (a 1ª fala da cena), `obra` (“Nome: subtítulo · ano”), `stage` (cenário + 2–3 personagens). *O primeiro episódio de um curso não tem mochila (quadro 2).*
2. **`review` — Mochila de revisão (única retomada).** `prev` (título do episódio anterior), `work` (obra do anterior), `recap` (4 pares frase/tradução do anterior), `bag` (**5 bolsos**: Padrão, Palavras, Verbos, Expressões, Sons — itens do episódio anterior), `lead`, `next` (“Hoje: **<gs>**”), `say`, `rs`, `chars`. É gerada do episódio anterior (`tools/audit/fix_mechanical.py`); nunca escrita à mão.
3. **`hotscene` — Explore a cena.** `rs` + `chars` (2–3 personagens da obra) e **5 objetos** clicáveis `hot[]`: `{e (emoji), x, y (% na cena), en, pt, say (frase com o padrão), sayPt}`. Os 5 objetos existem no cenário escolhido e **não repetem os do episódio vizinho**.
4. **`pgscene` — Cena 1.** `cast` (2 personagens: ícone + cor) e **8 falas** `[personagem, língua-alvo, tradução]` que usam o padrão várias vezes de forma natural; `speakers` liga nome → id da arte.
5. **`pgsheet` “Você entendeu?”** — **3** perguntas de compreensão da cena: `ask`, `speak`, `pt`, 3 opções `[emoji, texto]`, `a` (índice certo), `why` (cita a fala).
6. **`pgrule` — Regra do padrão.** `rule`: `who`, `head` (o `gs`), `sub`, `say[2]`, `formula[]` (de → para, com `say` e `note`), `uses[4]` (ícone, tag, frase, tradução), `rules[2]`, `tips[1]`; mais **1 pergunta** `q` de 3 opções.
7. **`pgmold` — Molde de frases.** **3 páginas** (`label`, `slots` com `cat` e `opts`, `end`) para montar frases trocando peças.
8. **`pgsheet` “Palavras da cena”** (`layout: grid`) — **exatamente 6 palavras**: `fig` (emoji), `say`, `ask`, 3 `opts`, `a`, `ptWord`, `why` com “**palavra** = tradução. Soa como “…”.” (a pronúncia é escrita para brasileiro ler).
9. **`verbs` — Verbos do episódio.** `title`, `tip` (“Quatro verbos: a, b, c e d.”), **4 itens** `{v, ic, pt, f (duas formas: eu/ele-ela com a terminação em negrito), ex[2], note}`, e `quiz` com **4** perguntas.
10. **`vplay` — Missão dos verbos.** os mesmos 4 verbos em modo jogo: `items[4]` e `plan` (**7 passos**), `say`, `bubble`, `avatar`.
11. **`pgexp` — Expressões e gírias.** **4 itens** `{ic, en, tag (Gíria/Expressão/Phrasal verb/Colocação), pt, use (quando usar, com negrito), ex[2]}` e `quiz` com **4** perguntas.
12. **`pgscene` — Cena 2 “Na conversa de verdade”.** diálogo com **as 4 expressões em uso, destacadas em `**negrito**`**; mínimo **6 falas** no A1/A2 e **8 falas** do B1 em diante; sem fala de enchimento (“Good.”, “Coffee?”, “Please.”, “Here.”).
13. **`pgsheet` “Complete as falas”** — **6** lacunas `text` com `___`, 3 `opts`, `a`, `why`, `say`.
14. **`pgsheet` “Qual está certa?”** — **4** itens: 3 frases, 1 certa; os erros são os que brasileiros realmente cometem.
15. **`pglab` — Laboratório de sons.** `short`, `title`, `say`, `intro {what, how, pt}`, **3 sons** (`ex`: palavra, pronúncia, tradução, dica), **3 pares mínimos** (`pairs`), `tip`, `phrase[2]`, **3 desafios** (`rounds`: `fig 🎧`, `say`, `ask`, `opts`, `a`, `why`). O som é **difícil para brasileiros**, ligado às palavras do episódio, e **diferente do som do episódio anterior**.
16. **`pgsheet` “Caça-sons”** — **5** itens de escuta (`fig 🎧`): ouvir e tocar a palavra ou a figura (`pic`).
17. **`pgspeak` — Sua vez de falar.** **5 frases** `[língua-alvo, tradução]` crescentes (1ª curta, 5ª combina duas), `who`, `say`.
18. **`pgmission` — Missão: sua vez!** **3 missões**: a **primeira se chama “Cena da obra”** (fala como os personagens), as outras duas são situações reais do aluno. Cada uma tem `data`: `prompt` (com a tarefa em negrito), `ph`, `chips`, `model` (resposta-modelo), `check[3]`, `kw[3]` (**regex que casam com o `model`** e não deixam passar qualquer frase), `tips[3]`, `ok[3]`, `reply[2]`.
19. **`wrap` — Para levar.** `recap` (4 pares), `teaser {t (título do PRÓXIMO episódio), d (“Próximo padrão: …”)}`, `sticker {title, sub (“Obra · ano”), rs, chars}`, `rs`, `chars`.

**Campos de topo do episódio:** `n`, `t` (título), `s` (subtítulo curto), `sc` (cenário base), `a` (obra: `k` “🎬 Filme”, `w` nome, `y` ano, `d` descrição de 1–2 frases em português), `h` (`l` fala-gancho, `src` obra, `tr` tradução), `p` (“Hoje você aprende…”), `v` (**6** palavras `[palavra, tradução, “Soa como…”]`), `g {t}` e `gs` (o padrão), `presentation: "regular-pilot-v1"`, `stage`.

## 4. Visual: cenários e personagens

- **Cenários (`rs`)**: variedade obrigatória. Os quadros de um mesmo episódio não repetem o cenário em sequência, e o `rs` principal difere do dos episódios vizinhos. Preferir cenários novos (`beach zoo farm playground busstop bakery supermarket bookshop postoffice bank pharmacy restaurant hotelroom mountain forest snow stage library museum castlehall garden fair pool stadium harbor chefkitchen musicroom traincar soccerfield fishing artroom nightcity meetingroom christmas`) além dos clássicos (`cafe living market airport lobby station subway park pier lake nyc cafe2 airport2 lobby1 lobby2 cafe3 diner home1 yard park2 school shop office clinic kitchen bedroom bath counter gym hall street`). Os objetos de `hotscene` têm de existir no cenário escolhido.
- **Personagens**: sempre os **personagens da obra do episódio**, com o nome da obra (nunca “Woman”/“Man”/“Girl”/“Boy”). Arte: usar um id existente em `js/chars*.js` só se for exatamente aquele personagem (ex.: `dorothy`, `scarecrow`, `lion`, `wendy`, `peter`, `cowboy`, `ranger`; `chars5`: `glinda`, `harry`, `gandalf`…). Senão, desenhar o personagem com ficha própria (figurino, adereço, cor) para que o aluno **reconheça a obra**. Variar rostos, idades e cores entre episódios.
- **Posição na cena**: `chars` = `[id, x (0–100), olha (0 esquerda/1 direita), escala]`; dois personagens em lados opostos, olhando para o centro; `hot` com `x,y` espalhados sem sobrepor os personagens.
- **Layout**: cabe sem rolar, com respiro; o guia (`say`, `bubble`, `avatar`) abre cada quadro; capa e figurinha (`sticker`) mostram a obra com identidade visual própria.

## 5. Vocabulário e criação de conteúdo

- **6 palavras da cena**: concretas, ligadas à obra e ao padrão, **nenhuma repetida do episódio vizinho**. Cada uma com tradução e “Soa como…” para brasileiro.
- **4 verbos**: do padrão/foco; formas “eu” e “ele/ela” (ou o equivalente do idioma) mostrando a terminação em negrito; exemplo na cena do episódio.
- **4 expressões**: reais e comuns, **uma por vez em contexto na cena 2**; `tag` correta; **únicas no curso** e nunca invenção solta.
- **Nível (CEFR)**: A1 frases curtas e concretas; A2 rotina e passado simples; B1 opiniões e planos; B2 nuance e debate; C1 registro, hedging, inversão; C2 estilo, retórica, dialeto, ironia. O foco do plano manda.
- **Perguntas**: **uma única resposta defensável**; distratores são erros plausíveis de brasileiros; a posição da resposta certa varia; `why` curto e correto.
- **Traduções**: a mesma frase tem sempre a mesma tradução em todo o curso.
- **Pronúncia**: “Soa como…” escrito com letras do português (ex.: *witch* → “UÍTCH”).

## 6. Adaptação por idioma e por nível

- O **idioma-alvo** muda (inglês, espanhol…); as traduções e explicações são sempre **português do Brasil**. Verbos e expressões são do idioma-alvo; o laboratório escolhe o som difícil *daquele idioma para brasileiros* (inglês: *sh*, *th*, *-ed*; espanhol: *j*, *rr*, *ñ*, *z/c*; etc.).
- **A1/A2**: cena 2 com 6+ falas; **B1 em diante**: cena 2 com 8+ falas.
- **Espanhol**: incluir armadilhas de brasileiros (falsos amigos, “portuñol”).
- O padrão (`gs`) e a obra vêm do plano; nunca mudar sem atualizar o plano.

## 7. Contrato automático (o que reprova)

`tools/audit/regular_pilot_contract.py`: 19 quadros na ordem; `presentation` presente; 6 palavras; 4 verbos; 4 expressões; laboratório 3+3; duas cenas (1ª ≥ 8 falas, 2ª ≥ 6 ou 8 conforme o nível); 3 missões; mochila no quadro 2; obra presente e sem repetir no curso. A **trava** (`tools/audit/regular_gate.py`, workflow `regular-quality-gate.yml`) roda isso em todo PR, exige obra única entre episódios prontos, exige que cursos fechados estejam 100% no padrão e exige **aderência ao plano** (obra, 4 verbos e 4 expressões iguais ao mapeado).

## 8. Montagem (comandos)

1. Escrever o episódio no módulo do curso (`tools/v3/<prefixo>_NNN_MMM.py`, construtores `S`/`E`/`EP`), com `from v3.<…> import *`.
2. Verificar sem gravar: `COURSE=<curso> python3 tools/v3/dryrun.py <módulo>` (0 problemas, 0 repetições com vizinhos, 0 enchimento).
3. Gravar: `COURSE=<curso> python3 tools/model_v3.py <n…>`; marcar: `COURSE=<curso> python3 tools/v3/mark_pilot2.py`; consertar mochila/teaser: `python3 tools/audit/fix_mechanical.py <curso>`.
4. Conferir: `python3 tools/audit/regular_pilot_contract.py --course <curso>`, `python3 tools/audit/regular_gate.py`, `python3 tools/plan/check_plan.py <curso> --estrito`.
5. Subir cache (`sw.js`, `app.html`), PR, merge.

## 9. Erros que já aconteceram (evitar)

- Continuação (episódio par) herdando obra, palavras, verbos ou sons do ímpar.
- Falas de enchimento na cena 2.
- Obra repetida em episódios distantes do mesmo curso; título de obra com “:”; obra de outro país/idioma sem relação.
- Texto do episódio ainda citando a obra antiga depois da troca (gaps, regra, molde, missões, expressões).
- Elenco genérico (“Woman e Man”) ou o mesmo boneco em episódios diferentes.
- `cover.sub` sem “em 10 minutos”; `teaser` que não aponta para o próximo episódio; mochila de outro episódio.
- Resposta com duas opções defensáveis; tradução diferente para a mesma frase.
- Fatos de obra de memória sem avisar; anos inventados.

## 10. Lista de conferência de um episódio (antes de entregar)

- [ ] 19 quadros na ordem; 6 palavras, 4 verbos, 4 expressões, 3 sons + 3 desafios, 3 missões (1ª “Cena da obra”).
- [ ] Obra, `gs`, 4 verbos e 4 expressões **iguais ao plano**.
- [ ] Obra única no curso; fatos conferidos; sem “:” no título.
- [ ] Cenas: 8 falas + (6 ou 8) com as expressões em negrito; sem enchimento.
- [ ] Nada repete o episódio vizinho (palavras, verbos, sons, objetos), exceto a mochila.
- [ ] Cenários variados; personagens da obra; `kw` das missões testados contra o `model`.
- [ ] `teaser` aponta o próximo episódio; `cover.sub` com “em 10 minutos”.
- [ ] Contrato, trava e dry-run sem falhas.

## 11. PROMPT-MESTRE (copiar e preencher)

> Você é autor de episódios do curso regular **{curso}** (idioma-alvo: **{idioma}**, nível **{nível CEFR}**, aluno brasileiro). Escreva o episódio **n={n}** (posição {pos}) no modelo **regular-pilot-v1**, idêntico em estrutura e densidade aos episódios de referência 7009801, 70001, 7070001 e 30001 do inglês A1 (leia-os em `data/en-a1_*.json` antes de começar) e conforme `docs/PROMPT_MONTAGEM_PADRAO.md`.
>
> **Ficha do episódio (do plano):** foco = {foco}; padrão (`gs`) = {gs}; obra = {obra nome} ({tipo}, {criador}, {ano}); verbos = {4 verbos}; expressões = {4 expressões}. Episódio anterior: {título, obra, palavras, verbos, som do laboratório} (só a mochila pode retomá-lo); próximo episódio: {título}.
>
> **Entregue** os 19 quadros, na ordem e com as contagens do contrato: capa com “em 10 minutos você …”; mochila gerada do anterior; cena clicável com 5 objetos; cena 1 com 8 falas; 3 perguntas de compreensão; regra com fórmula, usos, regras e pergunta; molde de 3 páginas; 6 palavras (com “Soa como…”); 4 verbos com formas e quiz de 4; missão dos verbos com plano de 7 passos; 4 expressões com quiz de 4; cena 2 ({6 ou 8}+ falas) encenando as 4 expressões em negrito, sem fala de enchimento; 6 lacunas; 4 “qual está certa”; laboratório com 1 som difícil para brasileiros (3 palavras, 3 pares mínimos, 3 desafios, diferente do anterior); 5 caça-sons; 5 frases para falar; 3 missões (a 1ª “Cena da obra”, `kw` que casam com o `model`); fechamento com recap de 4, teaser do próximo e figurinha da obra.
>
> **Regras:** conteúdo 100% próprio deste episódio; nada repetido do vizinho exceto a mochila; personagens = personagens da obra (arte existente só se for exatamente aquele personagem; senão ficha própria); cenários variados e diferentes dos vizinhos; tradução para português do Brasil natural e consistente; só fatos que você tem certeza; uma única resposta defensável por pergunta; distratores = erros reais de brasileiros.
>
> **Antes de entregar** rode `dryrun.py` do módulo (0 problemas), grave com `model_v3.py` + `mark_pilot2.py` + `fix_mechanical.py` e confira `regular_pilot_contract.py` e `regular_gate.py`. Relate em português o que verificou e o que veio de memória sem checagem.
