# Guia para escrever um arco do Neighbors (9 episódios)

Cada arco = 9 episódios (o 10º, a revisão, é gerado automaticamente). Um arquivo `tools/nb/specs/<nome>.py` com `EPS = [dict(...), ... 9 vezes]`.
Exemplos reais: FR `tools/nb/f35.py` (EPS35), ES = mesma estrutura de FR (use f35.py como modelo), JA `tools/nb/j37.py` (tem a 3ª coluna de romaji).
Leia o primeiro episódio inteiro de um exemplo antes de escrever. Valide com:
`python3 tools/nb/run_arc.py ARQ.py LANG CID ARCO BASE REVBASE --dry` (NÃO grave: sem --dry ele escreve em data/; quem integra sou eu).

## Campos de cada episódio (todos obrigatórios)
- `n` id (do esqueleto), `t` título (o do esqueleto, na língua-alvo), `s` subtítulo em português SEM o prefixo «Em breve · » (frase de objetivo, ex. "Falar do que vai fazer com «aller + infinitivo»").
- `city` e `sc` (cena) do esqueleto; `rs` = cenário refinado coerente com `sc`; valores aceitos de `rs`: office shop living school cafe3 hall airport home1 station cafe2 counter gym street clinic park lake kitchen market flags bedroom yard park2 diner pier subway airport2 bath cafe station1.
- `desc` (pt, 2–3 frases): o ponto gramatical/cultural + «Dica:» curta para brasileiros (falso amigo, pronúncia, diferença do português).
- `name` + `face` = personagem do esqueleto (`pe`); `emo` = 4 emojis da cena; `mission` (pt, 1 frase, começa com "Hoje você …").
- `hook` = "frase na língua-alvo|tradução pt" (pergunta curta que abre a história); `goal` = frase-alvo curta que o aluno vai dizer.
- `v` = EXATAMENTE 6 tuplas (palavra, significado pt, dica de pronúncia pt entre “aspas” ex. Soa como “a-LÊ”., emoji). JA: dica "Lê-se «o-bo-e-ru».".
- `chat` = EXATAMENTE 11 falas alternando P (parceiro) e Y (aluno), formato "P: texto | tradução pt" (JA: "P: かな | pt | romaji"). Começa por P, termina por P. O diálogo conta uma pequena história com começo/meio/fim, naturalmente, sem listas artificiais, e usa o tema do esqueleto (`plan.learn`, `plan.sample`).
- `tap` = 3 itens (pergunta na língua-alvo, pt, [3 opções na língua-alvo], índice da correta (0..2, a certa SEMPRE no índice 0 está ok mas varie 0/1/2), índice da fala do `chat` que contém a resposta (0..10), "Y: “trecho exato”" ou "P: “trecho”").
- `swap` = (dica pt com «exemplo» e 🎓 nível do exame (DELE/SIELE ES, DELF FR, JLPT/JF JA), [2 páginas]); cada página = (rótulo, [3 pares (início, pt)], [3 pares (fim, pt)], pontuação final).
- `chat2` = EXATAMENTE 6 falas, começa por Y, mesma situação com outras palavras.
- `slang` = (nome do amigo, [emoji, "#AE3EC9"], [EXATAMENTE 6 falas "F:"/"Y:" alternando, com gírias/expressões idiomáticas reais e usadas hoje], {glossário expressão→pt, 5 itens; as 5 expressões DEVEM aparecer literalmente nas falas}, [2 expressões-chave que aparecem no glossário]).
- `real` = (forma "de livro", forma real falada, explicação pt) — as duas diferentes (ex. "Je ne vais pas manger" → "Je vais pas manger"). ES: contrações e elisões reais ("para" → "pa'"), JA: forma polida vs. casual.
- `recap_slang` = "expressão → tradução" (uma das do glossário).

## Qualidade (importante: é um produto pago)
- Língua-alvo 100% correta, natural e do nível do arco (A1/A2/B1 – CEFR). Português do Brasil, claro e curto. Nada de calques.
- Acentos/pontuação corretos (ES com ¿ ¡; FR com espaço antes de ? ! : ; JA em hiragana/kanji coerente com o nível, com romaji na 3ª coluna do chat/slang).
- Cada episódio ensina o ponto gramatical do esqueleto e reutiliza vocabulário dos anteriores do arco. Variar cenas, tom, humor. Personagens com personalidade.
- Gírias: reais, atuais, sem vulgaridade pesada; ES varia entre México/Espanha/Argentina/Chile conforme a cidade.
- Sem repetir textualmente frases entre episódios. Nenhum campo vazio.
- Rode a validação `--dry` até passar (ela confere as contagens, o glossário nas falas, índices do tap, swap 3×3 etc.).
