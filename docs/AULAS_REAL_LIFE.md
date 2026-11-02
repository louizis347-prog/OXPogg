# Aulas Real-Life — método e guia de autoria (Painel do Professor)

As aulas ao vivo do Painel do Professor (`/professor/aula3.html?n=N`) seguem o método **Real-Life English**: cada encontro é uma experiência de comunicação, não uma aula de gramática com exercícios.

**Princípio central:** Situation → Language → Discovery → Practice → Interaction → Feedback → Real Life, integrando Speaking, Listening, Reading e Writing a gramática, vocabulário, pronúncia, cultura e situações autênticas.

**Regra pedagógica:** é melhor o estudante usar 5 expressões com naturalidade do que memorizar 20 palavras e não conseguir construir uma conversa.

## Os dois modelos (60 minutos)
| Estágio (`stage`) | Particular (1+1) | Grupo (4–6) |
|---|---|---|
| `warm` | Connection & warm-up · 5 min | Social warm-up · 6 min |
| `immersion` | Real-life immersion · 7 | Cultural immersion · 7 |
| `notice` | Notice the language · 8 | Language discovery · 8 |
| `gram` | Grammar & pronunciation · 10 | Grammar & pronunciation · 9 |
| `practice` | Controlled → guided practice · 9 | (dentro de `gram`, em pares) |
| `speak1` | Personalized roleplay · 11 | Communication lab · 11 (rodízio de pares + information gap) |
| `speak2` | — | Group mission · 11 |
| `write` | Writing & feedback · 7 | Writing & feedback · 5 |
| `exit` | Exit ticket & homework · 3 | Exit challenge · 3 |

A diferença mais importante: **a aula em grupo não é uma aula particular com mais gente assistindo.** Ela explora a interação entre os estudantes (rodízios, information gap, missões com papéis e restrições, responsabilidade individual).

## As telas (tipos `rl_*`)
Particular (14) e Grupo (15) — a mesma estrutura, com `rl_role` (só particular) no lugar de `rl_lab` + `rl_mission` (só grupo, `"for": "group"`):
`rl_open` → `rl_warm` → `rl_culture` → `rl_listen` → `rl_dialog` → `rl_chunks` → `rl_patterns` → `rl_pron` → `rl_challenge` → (`rl_role` | `rl_lab` + `rl_mission`) → `rl_write` → `rl_feedback` → `rl_exit` → `rl_levels`.

## Como escrever uma aula
1. Leia o **modelo completo**: `professor/src/lessons/l003.py` (aula 3, “Ordering at a café”). Copie a estrutura, os campos e a profundidade — **não o conteúdo**. Cada aula é original.
2. Crie `professor/src/lessons/lNNN.py` (NNN = número da aula, 3 dígitos) com `LESSON = dict(...)` e, no fim, `if __name__ == '__main__': print('ok', finish(LESSON))`. Importe `PLAN, teach, finish` de `rl_common` como em `l003.py`.
3. Dados do currículo da aula (título/tópico, situação, padrões principais, insight cultural, cenário e personagens sugeridos): `professor/data/v3/curriculum.json` (campo `n`).
4. Gere o JSON: `python3 professor/src/lessons/lNNN.py`. Valide: `python3 professor/src/validate_rl.py NNN` até **0 erros**.
5. Confira o visual: `NODE_PATH=$(npm root -g) node professor/tools/rl_shots.js NNN` (gera prints das telas em `/tmp/rl_NNN_*.png`; abra alguns com Read: nenhum texto cortado, nenhuma tela vazia).

## Regras de conteúdo (todas obrigatórias)
- **Situação real e concreta** (café, aeroporto, entrevista, farmácia…), com um **problema pequeno** que o estudante resolve. `situation.text`, `goal` (o que ele consegue fazer ao final) e 3–4 `canDo` + 4 critérios de sucesso.
- **Insight cultural dentro da língua** (não curiosidade solta): uma convenção social, diferença cultural ou jeito de interagir, ligado às próprias falas. **Só fatos verdadeiros**; sem estatísticas inventadas. Cartões `rl_culture` com `vis` (tokens abaixo), 3 perguntas em inglês com **resposta-modelo por nível** (A1, A2, B1, B2) e a comparação com o Brasil (`compare`).
- **Diálogo autêntico** de 8–10 falas (`dialog.lines`), com `pt` natural (português do Brasil), 4+ falas com os chunks marcados em `**negrito**`. Nível: A1 frases curtas (≤14 palavras), A2 até 20. Inglês americano natural.
- **Chunks** (`rl_chunks`): 5–8 expressões; **3–5 prioritárias** (`pri: true`) — as que serão usadas e repetidas; `alt` com equivalente formal/informal quando fizer sentido; `discover` (≥4 itens por função).
- **Gramática em contexto** (`rl_patterns`): 2–4 padrões que estão no diálogo (≥2 principais); **troca de palavras** (`swap`): `frame` com `{slots}`, ≥2 slots com ≥3 opções (`en` + `pt`), `tpt` com a tradução (mesmos `{slots}`); tabela spoken × written.
- **Pronúncia**: UM único fenômeno (ritmo, sons, entonação, redução ou ligação), `items` com `rhythm` (`o`=fraca, `O`=forte), `identify` (≥2 de “qual você ouve?”), e `own` (uso próprio).
- **Prática guiada** (`rl_challenge`): 2 níveis (“Controlled…”, “Guided…”), 8–10 itens, tipos `mcq` (3 opções), `gap` (`___`), `swap` (transformar), `reply` (resposta a uma fala); todo item com `why`.
- **Particular**: `rl_role` com `orders` (≥3), `complications` (≥3) e 3 `rounds` (com apoio → palavras-chave → sem roteiro). **Grupo**: `rl_lab` (≥4 rodadas; `infogap` com cartões A/B **complementares**: onde A sabe, B não sabe) e `rl_mission` (≥3 grupos, cada um com missão, restrição e frase inicial).
- **Writing**: tarefa curta ligada à situação, modelo, passos e checklist. **Feedback**: rubrica (flu/lan/pro/int), interpretações e 3 prompts. **Exit**: 3 competências com modelo; homework com 4 itens; `spaced` (next/week/unit). **Level up**: a mesma situação do A1 ao C2 (frases reais crescendo em complexidade) e `you`.
- **Roteiro do professor** (`teach`, em **português**) em ≥12 telas: `goal`; `solo` e/ou `group` (passos de condução); `answers`; `extra` (perguntas extras, ≥8 telas); `errors` (correções frequentes `{w, r}` de aprendizes brasileiros, ≥6 telas); `support` (alternativas para quem precisa de mais apoio, ≥6 telas); `stretch` (opcional).
- **Não repita** diálogo, expressão prioritária ou missão de outra aula. Retome conteúdo anterior só em `warm.recall` e `spaced`.
- Idioma da interface do aluno: inglês (instruções curtas) + `pt` onde há campo `pt`; roteiro do professor: português.

## Vocabulário permitido
- **`scene`**: use um destes (cenário da capa e do diálogo): `park cafe restaurant diner supermarket market bakery bookshop pharmacy hospital gym bank postoffice hotel airport station subway busstop road city plaza office classroom library livingroom bedroom kitchen corridor stage cinema concert stadium studio newsroom fairground rainystreet beach liberty` (e outros de `PogFicha.VOCAB.scene`).
- **`cast`/`speakers`/`sit.cast`**: nomes de `professor/data/elenco.json` (ex.: Mia, Ken, Luis, Omar, Sara, Raj, Ana, Tom…). Dois falantes no diálogo; ideal que a profissão combine com o papel.
- **`vis`** nos cartões culturais: `prop:<id>` (134 objetos ilustrados: cup, bag, coin, book, key, bus, train, airplane, pizza, sandwich, cake, ticket-like: envelope, map, compass, suitcase, camera, telephone, computer, mailbox, umbrella, clock, bed, bathtub, torch, …), `obj:<id>` (apple, bag, ball, book, clock, coin, cup, door, envelope, globe, key, lamp, phone, plane, suitcase, umbrella…), `flag:<cc>` (ar au br ca cn de eg es fr gb ie in it jp kr mx ng pt ru tr us), `tod:dawn|day|dusk|night`, `mood:<…>`.

## Níveis
A1: frases curtas e concretas, modelos, imagens. A2: rotina, passado simples, preferências. A mesma estrutura do método vale para todos; só muda a complexidade e a autonomia (a tela `rl_levels` mostra a progressão).

## Avaliação do estudante
Rubrica formativa de 1 a 5 (Fluency, Language use, Pronunciation, Interaction) — **ferramenta interna de acompanhamento, não certificação CEFR**. Ao final: *What you did well · What to improve · Your next challenge*.

## Revisão espaçada
Retomar o conteúdo na aula seguinte, depois de uma semana e na missão de encerramento da unidade (`rl_exit.spaced`).

## Unidade de 8 aulas
Situações 1–7 + **Real-Life Mission Day** (aula 8, missão integrada com várias situações encadeadas). Currículo completo: `professor/data/v3/curriculum.json` (100 aulas, A1 70 + A2 30).
