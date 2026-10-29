# Guia — reescrever 29 aulas do A2 de inglês para obras NOVAS e ÚNICAS (modelo regular-pilot-v1)

**Contexto.** Cada aula abaixo ensina hoje o vocabulário de uma obra que já é o tema de outro episódio do inglês regular (ex.: aula de Dom Quixote no A2 e Dom Quixote no A1). Decisão do dono do produto: **cada obra aparece UMA vez em todo o curso**. Então cada episódio do seu lote ganha uma **obra nova** (campo `obra_nova` do brief — já verificada como livre) e a aula é **reescrita por inteiro em torno dela**, mantendo a gramática do dia. Além do módulo da aula, você escreve a **ficha da capa** (arte nova, escrita à mão, como no A1).

## Entrega (por agente)
1. `tools/v3/a2_fix_<LOTE>.py` — um módulo com um episódio por `add(dict(...), EPS)`; mesmo `n` do brief (o episódio substitui o atual).
   Cabeçalho: `from v3.b2lib import *` e `EPS = []` (a função `add` e os helpers `work/mission` estão em `tools/v3/b2lib.py`).
2. `tools/ficha/work/en-a2_fix_<LOTE>.json` — `{ "<n>": {ficha}, ... }` com a ficha da capa de cada episódio.
3. Não edite `data/`, não rode `tools/model_v3.py`, não faça commit. Eu aplico depois que você passar na validação.

## Referências obrigatórias (leia antes de escrever)
- Formato completo dos campos: `tools/v3/b2_001_005.py` (leia pelo menos dois `add(dict(...))` inteiros) e `tools/v3/b2lib.py`. O guia `tools/b2gen/GUIDE.md` explica cada regra de qualidade (cenas de 8 falas, laboratório de sons, missões com `kw`, personagens `ids`, cenários `rs`, `obra.pa`, `teaser`) — **vale tudo o que está lá**, com as adaptações abaixo para o A2.
- Briefs: `tools/a2fix/briefs.json` → `alvo` (os seus episódios: `titulo`, `gramatica`, `porque`, `sub`, `anterior`, `proximo`, `obra_nova`, `vocab_atual` — só para você NÃO repetir o vocabulário da obra antiga).
- Validação (obrigatória, sem gravar): `python3 tools/a2fix/try.py a2_fix_<LOTE>` até `problemas: 0`.

## Regras (todas obrigatórias)
1. **Nível A2 (CEFR) real**: frases curtas, vocabulário concreto, situações do dia a dia. O foco gramatical é o do brief (`gramatica` / `porque`): mantenha o **mesmo título** do episódio e ensine **exatamente esse padrão** — só a situação, as personagens e o vocabulário mudam para a obra nova.
2. **A obra nova é o assunto da aula**: use `obra_nova.nome/tipo/ano` exatamente como no brief (`work(...)`, nome sem subtítulo). Os fatos sobre a obra devem ser **verdadeiros e conhecidos** (nada inventado). A obra aparece DENTRO da aula: uma fala da cena principal e a primeira missão (“Cena da obra”) citam a obra ou um personagem/elemento real dela; o elenco **não** pode ser genérico (nada de Alex/Jordan/Woman/Man): use personagens ou figuras da obra (para lugares, tradições, canções: pessoas e situações reais ligadas a ela — ex.: um guia no Tower Bridge, a família na Thanksgiving).
3. **Todo conteúdo é do episódio**: 6 vocabulário, 4 verbos, 4 expressões, sons do laboratório, falas, quizzes, lacunas, armadilhas, missões — ligados ao padrão e à obra. Vocabulário/verbos/`hot`/som **diferentes** dos episódios vizinhos (`anterior`/`proximo`) e **sem palavras da obra antiga** (`vocab_atual`).
4. **Expressões únicas no A2**: nenhuma expressão de `exps` pode ser ensinada em outro episódio do A2 (o validador confere). Prefira expressões do tema da obra.
5. **Inglês natural e correto; português do Brasil natural**; traduções fiéis; cada `why` curto e certo; nenhuma pergunta com duas respostas defensáveis; a posição da resposta certa varia entre as perguntas.
6. **Cenas**: 8 falas na principal; a segunda cena = `exps` + `scene2extra` (4 falas) com pequeno conflito ou surpresa, diálogo **novo**.
7. **Missões**: 3 checagens cada; os regex `kw` precisam casar com o `model` e não podem deixar passar qualquer frase.
8. **Cenários (`rs`)**: variados, combinando com o texto, existentes na lista do validador. Personagens `ids`: nomeados existentes só se forem exatamente o personagem; senão `p:...` (veja a regra 9 do guia B2).
9. **A obra e o episódio seguinte**: `teaser` = título do `proximo` do brief, sem prometer o que ele não ensina.

## Ficha da capa (arte nova, à mão)
Formato e vocabulário válidos: `tools/ficha/vocab.json`; exemplos prontos: `tools/ficha/work/en-a2_001_040.json` e `tools/ficha/exemplos.json`. Cada ficha: `{"t": <título da obra>, "scene": …, "tod": …, "cast": [1–4 personagens: pessoa "p" OU bicho "a"], "prop": {id, at, s}, "decor": […]}` — desenhe **a cena que todo mundo reconhece da obra nova** (personagens com roupa/chapéu/cabelo certos, objeto-símbolo, cenário e hora do dia). Nada de genérico: duas fichas nunca repetem elenco+objeto+cenário (`validate.py` confere contra todos os cursos).
- Valide: `python3 tools/ficha/validate.py --curso en-a2 --meu tools/ficha/work/en-a2_fix_<LOTE>.json tools/ficha/work/en-a2_fix_<LOTE>.json` e olhe o resultado: `node tools/ficha/render_sheet.js tools/ficha/work/en-a2_fix_<LOTE>.json /tmp/<LOTE>.png 3` (abra o PNG com Read e confira se cada capa lembra a obra; refaça o que estiver genérico).
- Se faltar uma peça (ex.: um prop) na biblioteca, escolha a mais próxima e anote em `"falta": ["..."]` na ficha.

## Antes de entregar
`try.py` com `problemas: 0`; fichas sem ERRO e conferidas no PNG; releia: nenhuma obra repetida, fatos corretos, tradução natural, resposta única, cenários variados. Responda com a lista dos episódios entregues e qualquer ressalva.
