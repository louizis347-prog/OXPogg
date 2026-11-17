# Níveis CEFR do projeto: referência, regra e auditoria

## Referência usada

- **Vocabulário:** CEFR-J Vocabulary Profile v1.5 (Tono Laboratory, dados abertos, repositório `openlanguageprofiles/olp-en-cefrj`). Cópia: `professor/data/cefrj-vocab.json` (≈7 mil palavras, A1–B2).
- **Gramática:** CEFR-J Grammar Profile (2018), com colunas de Core Inventory, EGP e GSELO. Cópia: `professor/data/cefrj-grammar.csv`.
- Os níveis anteriores do projeto (tetos por faixa de aula) eram estimativas minhas e **não** vinham de nenhuma lista oficial.

## Regra do projeto

1. **Vocabulário:** nenhuma palavra do diálogo pode estar acima do nível da aula (A1 → A1; A2 → A1+A2), a menos que a aula a ensine (vocabulário, glossário, verbos ou expressões da própria aula). Nomes próprios são ignorados.
2. **Gramática:** só entra no nível o que a referência classifica nele (tabela abaixo).
3. A checagem roda em `tools/cefr_audit.py` e aparece como `CEFR n ok` no fim do `runbatch.sh`.

## Gramática por nível (CEFR-J)

| Estrutura | Nível CEFR-J | Decisão no A2 |
|---|---|---|
| was/were afirmativo | A1.3 | A2.1 |
| was/were negativo e passado simples (afirmativo) | A1.3 / A2.1 | A2.1 |
| passado simples negativo e perguntas (did/didn't) | A2.1 | A2.1 |
| should | A2.1 | A2.2 |
| present perfect afirmativo | A2.1 | A2.2 (ever/never/already; sem forma negativa) |
| if (condição) | A2.1 | A2.3 |
| passiva (is/was made) | A1.2–A2.1 | A2.3 |
| going to, will, have to, much (incontável), comparativo com more | A2.2 | A2.2 |
| **could, may, might, must** | **B1.1** | **fora do A2** (só como frases prontas) |
| **used to** | **B1.1** | **fora do A2** (trocado por passado com always/often) |
| present perfect negativo e com for/since | B1.1 | fora do A2 |
| segundo condicional | B1.2 | fora do A2 |
| which relativo, discurso indireto com tell | B1–B2 | fora do A2 |

## Resultado da auditoria (depois da correção completa)

- **Vocabulário:** 0 palavras fora da regra nas 550 aulas (A1 e A2). Toda palavra do diálogo acima do nível da aula é ensinada na própria aula, na tela extra "Palavras de apoio" (`professor/src/support_words.json`, 579 palavras em 315 aulas).
- **Gramática:** 0 ocorrências de *could, must/mustn't, may, might, used to, present perfect negativo* e *I've never* nos diálogos. Os pedidos educados viraram *Can I / Can you*, e *must* virou *have to* ou *Don't*. As trocas estão em `professor/src/overrides_a1.json` e são aplicadas em toda reconstrução.
- **Limite da checagem:** o vocabulário é conferido automaticamente (`tools/cefr_audit.py`); a gramática foi conferida por busca de padrões, e não por um analisador sintático.

## A2 (2001–2150) — conferência final

- Vocabulário: 0 palavras fora da regra nas 150 aulas (`tools/cefr_audit.py`).
- Gramática: 0 estruturas proibidas nos diálogos (`BAN` em `tools/gen/mk.py`, a mesma lista do guia dos agentes).
- Teste no navegador: as 150 aulas têm 44 quadros e nenhum erro.

## A2 extras (2151–2350) — conferência final

- Vocabulário: 0 palavras fora da regra nas 350 aulas A2 (`tools/cefr_audit.py`).
- Gramática: 0 estruturas proibidas nos diálogos (lista `BAN` em `tools/gen/mk.py`).
- Teste no navegador: as 350 aulas têm 44 quadros e nenhum erro.
- Aulas acima da 233 reaproveitam os episódios do curso regular de A2 a partir do 1 (o curso tem 237 episódios); a "Cena da obra" delas repete a de aulas anteriores.

## B1 (3001–3200) — conferência final

- **Numeração:** o B1 usa os ids 3001–3200 e aparece no painel como "B1 · 001" a "B1 · 200". Plano em `professor/tools/plan_b1.py`; gerador `professor/tools/gen/mk.py` (função `B1`) e guia `professor/tools/gen/AGENT_GUIDE_B1.md`.
- **Vocabulário:** 0 palavras fora da regra nos diálogos das 200 aulas (`tools/cefr_audit.py`, teto B1). Palavra B2 só entra se a própria aula a ensina.
- **Gramática permitida (CEFR-J, leitura conservadora):** tudo do A2 mais present perfect, could, must/mustn't, have to em todas as formas, may/might, used to, passivo presente e passado, relativas definidas (who/that/which, sem pronome), 2º condicional simples, will/won't, discurso indireto simples (said/told + passado), perguntas indiretas simples, gerúndio/infinitivo, too/enough, as…as, reflexivos.
- **Proibido (B2):** past perfect, present perfect contínuo, wish, modais perfeitos, 3º condicional, would rather, had better, be/get used to, unless, futuro contínuo/perfeito, perguntas reportadas, inversões, passivo contínuo/perfeito, whom/whose, so that, in order to (lista `BAN_B1` em `mk.py`).
- **Títulos:** três títulos do plano foram trocados por conterem estrutura B2 (passivo contínuo, past perfect, "whose").
- **Subtítulo da aula:** nas aulas do B1 o subtítulo é "Foco da aula" (vem do plano). Antes ele mostrava o resumo de gramática de outro episódio. O mesmo defeito existe nas aulas do A2 e ainda não foi corrigido.
- **Teste no navegador:** as 200 aulas têm 44 quadros e nenhum erro.
- **Obras culturais:** 200 títulos distintos, sem repetir nenhuma outra aula do projeto. Os fatos foram escritos pelo modelo e só uma amostra foi conferida; vários anos ficaram em branco por falta de certeza.
- **Limites:** a checagem de gramática é por padrões de texto e cobre diálogo e expressões; cartões, quiz e cultura dependem da revisão dos autores das fichas. Nenhum professor revisou o conteúdo.

## B1 (3201–3350) e correção do subtítulo do A2 — conferência final

- **B1 3201–3350 (150 aulas, blocos temáticos):** diálogos com 0 palavras fora da regra B1 (`tools/cefr_audit.py`) e sem estruturas B2. Duas aulas tiveram uma palavra B2 trocada (3285 "saving", 3312 "dyed"). 350 títulos de aula distintos no B1 e 350 obras distintas, sem coincidir com A1 nem A2.
- **Índice do episódio de apoio:** a partir da aula 3234 o índice recomeça do início (o conjunto de apoio tem 233 entradas válidas); isso só afeta a cena de apoio, a obra e o título de cada aula são próprios.
- **Subtítulo das aulas do A2 (2001–2500):** passou a ser "Foco da aula" (vem de `tools/plan_a2.py`). Antes mostrava o resumo de gramática de outro episódio. A mudança expôs 3 aulas A2 cujos diálogos tinham uma palavra B1 que só "passava" na auditoria por constar nesse subtítulo errado (2001 "sports", 2061 "charge", 2081 "pounds"). As três palavras agora são ensinadas na tela de apoio da própria aula (`src/support_words.json`).
- **Teste no navegador:** 500 aulas do A2 e 350 do B1, todas com 44 quadros e nenhum erro.
- **Limites:** checagem de gramática por padrões de texto (diálogo e expressões); cartões, quiz e cultura dependem da revisão dos autores das fichas. Fatos das obras só amostrados; vários anos em branco por falta de certeza. Nenhum professor revisou o conteúdo.

## B1 (3351–3500) — conferência final: B1 completo com 500 aulas

- **Aulas 3351–3500 (150 aulas, blocos temáticos):** redes sociais, festas, compras online, banco, transporte, hotel, restaurante, saúde, casa, hobbies, natureza, cidades, história, pessoas e revisões. Total do B1: 500 aulas (3001–3500), mostradas como "B1 · 001" a "B1 · 500".
- **Vocabulário:** 0 palavras fora da regra B1 nos diálogos das 150 aulas (`tools/cefr_audit.py`). Sem estruturas B2 nos diálogos (`BAN_B1`).
- **Teste no navegador:** as 150 aulas têm 44 quadros e nenhum erro.
- **Títulos e obras:** 500 títulos de aula e 500 obras distintos no B1, sem coincidir com A1 ou A2.
- **Índice do episódio de apoio:** `reg` recomeça a cada 233 (módulo), só para a cena de apoio; título e obra de cada aula são próprios.
- **Varredura de B2 fora do diálogo (cartões, quiz, cultura):** os achados restantes são exemplos ERRADOS propositais dos exercícios ("If I would have money…", "She said she was being hungry"), pergunta com *whose* (não é relativa) e frases em ordem embaralhada. "Wish you were here" (3367) e algumas notas culturais com *wish* como substantivo ficaram como informação cultural.
- **Limites:** checagem de gramática por padrões de texto; cartões, quiz e cultura dependem da revisão dos autores das fichas. Fatos das obras só amostrados; vários anos em branco por falta de certeza. Nenhum professor revisou o conteúdo.

## B2 (4001–4100) — primeiras 100 aulas

- **Numeração:** o B2 usa os ids 4001+ e aparece no painel como "B2 · 001"; plano em `professor/tools/plan_b2.py`, gerador `tools/gen/mk.py` (função `B2`) e guia `tools/gen/AGENT_GUIDE_B2.md`. O subtítulo da aula é "Foco da aula" (vem do plano).
- **Conteúdo (100 aulas):** present perfect contínuo, past perfect (simples e contínuo), 3º condicional e *wish*/*if only*, modais perfeitos (dedução e crítica), passivos avançados (contínuo, perfeito, futuro, modal, de relato), causativo, discurso indireto completo, relativas não definidoras, *whose*/*whom*, futuro contínuo e perfeito, *be/get used to*, *would rather*, *had better*, *unless*, *so that*, *despite* e revisões.
- **Gramática proibida (C1):** inversões (hardly/no sooner/not only/never have I), condicional invertido (Had I known…), *were to*, subjuntivo formal (suggest that he go), particípio perfeito (Having finished…), futuro perfeito contínuo, orações clivadas (What I need is… / It was X that…) — lista `BAN_B2` em `mk.py`.
- **Vocabulário:** 0 palavras fora da regra B2 nos diálogos (`tools/cefr_audit.py`, teto B2). Palavras fora da lista do CEFR-J só entram se a aula as ensina. A tabela de formas irregulares (`chosen`, `spoke`, `flown`…) passou a valer pelo verbo-base.
- **Teste no navegador:** as 100 aulas têm 44 quadros e nenhum erro.
- **Títulos e obras:** 100 títulos distintos; as obras não repetem nenhuma de A2/B1 (conferido também com títulos normalizados, sem "The" e com variações). Três obras repetidas foram trocadas (4010, 4036, 4046).
- **Varredura de C1 fora do diálogo:** os achados restantes são exemplos errados propositais, frases embaralhadas dos exercícios e definições ("get used to means to become accustomed to…").
- **Limites:** checagem de gramática por padrões de texto; cartões, quiz e cultura dependem da revisão dos autores das fichas. Fatos das obras só amostrados; vários anos em branco. Nenhum professor revisou o conteúdo.
