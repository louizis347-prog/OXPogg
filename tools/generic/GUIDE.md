# Guia — trocar a obra de aulas GENÉRICAS (só título/referência + capa nova), sem mexer no conteúdo da aula

**Contexto.** Estes episódios do inglês regular têm aula que **não é sobre uma obra específica** (a obra do título é só um rótulo: cenas-modelo do tipo “I noticed X in the program notes”). Decisão do dono do produto: **não reescrever a aula** — trocar a obra por uma que **combine de verdade com o tema/situação da aula**, mantendo **uma obra única em todo o curso**, e fazer uma **capa nova (ficha, arte à mão)** ligada à obra e ao conteúdo.

## Entrega (por agente)
Um arquivo `tools/generic/out/<LOTE>.json`:
```
{ "<n>": { "obra": {"nome": "...", "tipo": "Livro|Filme|Série|Canção|Pintura|Peça|Poema|Jogo|Lugar|Tradição|Personagem|…", "ano": "1999"},
           "desc": "2–3 frases em português do Brasil: fatos VERDADEIROS e conhecidos sobre a obra + a frase de ponte “A referência <nome> combina com <foco da aula em poucas palavras>.”",
           "ficha": { ... ficha da capa ... } }, ... }
```
Não edite `data/`, não faça commit. Valide com `python3 tools/generic/check.py <LOTE>` até `problemas: 0`.

## Como escolher a obra (o que importa)
1. Leia o brief `tools/generic/lotes/<LOTE>.json` (`alvo`: `titulo`, `gramatica`, `foco`, `vocab`, `falas`, `cenario`, `obra_atual`). Para ver a aula inteira: `data/en-<nivel>_NN.json` (procure o `n`). **A obra nova precisa ter relação real com a situação e o vocabulário da aula** (ex.: aula de comida no mercado → um filme/livro/lugar ligado a mercado ou comida), não com a gramática.
2. **Única em todo o inglês regular (A1–C2, 3.000 episódios) e nesta entrega**: nenhuma obra que já seja a obra de outro episódio — nem com grafia/idioma diferente, nem da mesma franquia (“Peter Pan” = “Peter and Wendy”; “The Lego Movie” ≈ “Lego”). O `check.py` confere; confira você mesmo também (`grep` em `data/en-*.json`).
3. **Real e conhecida**; título em inglês (ou nome próprio consagrado). Fatos corretos — nada inventado. Sem pessoas reais com falas inventadas.
4. **Adequada ao nível**: A1/A2 = obras acessíveis (infantis, filmes/séries populares, canções, lugares, tradições); B1/B2 = obras adultas conhecidas; C1/C2 = obras culturalmente densas (literatura, cinema autoral, arte, instituições, debates), em inglês.
5. Varie: não escolha 18 filmes; misture livros, canções, quadros, lugares, tradições, jogos, séries.
6. `desc`: português do Brasil natural, 2–3 frases, fatos verdadeiros, **inclui obrigatoriamente** a frase `A referência <nome> combina com <foco>.` (o gate de ponte exige “A referência…”).

## Ficha da capa (arte nova, à mão)
Formato e vocabulário válidos: `tools/ficha/vocab.json`; exemplos: `tools/ficha/work/en-a2_fix_01.json`, `tools/ficha/exemplos.json`. `{ "t": <nome da obra>, "scene": …, "tod": …, "cast": [1–4: pessoa "p" OU bicho "a"], "prop": {id, at, s}, "decor": […] }` — desenhe **a cena que todo mundo reconhece da obra** (personagens com roupa/cabelo/chapéu certos, objeto-símbolo, cenário e hora do dia), coerente com o conteúdo da aula (`cenario`/`falas`). **Nenhuma ficha pode repetir elenco+objeto+cenário de outra** (o `check.py` compara com TODAS as fichas existentes e com os outros lotes): varie cenário, objeto e roupas.
- Veja o resultado: `node tools/ficha/render_sheet.js <seu-json-só-com-as-fichas> /tmp/<LOTE>.png 4` (monte um JSON `{n: ficha}` temporário) e abra o PNG com Read; refaça o que ficar genérico. Se faltar peça na biblioteca, use a mais próxima e anote `"falta": ["..."]`.

## Antes de entregar
`python3 tools/generic/check.py <LOTE>` com `problemas: 0`; fichas conferidas no PNG. Responda com um resumo curto (n → obra) e ressalvas.
