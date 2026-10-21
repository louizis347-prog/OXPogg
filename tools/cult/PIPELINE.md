# Leitura rica (Cena da obra) — pipeline por curso (usado em en-a1, en-a2, en-b1; agora en-b2)

1. `python3 tools/cult/mk_chunks.py CURSO N` → `tools/cult/work/CURSO_chunkK.json` (obras distintas do curso: `work`, `chips` [tipo, ano, autor], `panel`, `eps`).
2. **Escrita com pesquisa** (um agente por bloco): para cada obra do bloco, pesquisar na web (WebSearch/WebFetch) e produzir
   - `tools/cult/kb/CURSO_K.json`: `{obra: {kind, by, y1, pd, blurb, cena:{mode, lines, hl, src?, ctx}, q?}}`
     * `kind`: filme | livro | série | poema | canção | peça | conto | fábula | mito | cartas | arte …; `y1` = ano da obra (confirmado); `pd` = domínio público (true só se confirmado); `blurb` = 1 frase em pt-BR.
     * `cena.mode`: `scene` (resumo da cena em `ctx`, sem falas — PADRÃO quando não for possível confirmar o texto literal), `page`/`quote` (só para obras em DOMÍNIO PÚBLICO com o trecho original confirmado em fonte; `lines` = [[inglês, português, falante]], `src` = referência, `hl` = palavras a destacar, `q` = pergunta de compreensão {q,o[3],a,why}).
     * NUNCA invente falas, citações ou fatos. Se não confirmar, use `scene` e escreva só o que se sabe com segurança.
   - `tools/cult/kb2/CURSO_K.json`: `{obra: {intro, leitura:[2 parágrafos], facts:[2]}}` — texto em pt-BR (inglês só em títulos/termos): `intro` 2–4 frases (o que é, quem fez, quando, contexto); `leitura` 2 parágrafos de ~60–90 palavras (bastidores, recepção, curiosidade verificada; sem repetir a intro; sem opinião inventada); `facts` 2 fatos curtos verificáveis.
   - Entradas de uma mesma franquia/obra com variações de título (ex.: «12 Angry Men: The Verdict») compartilham a base da obra mãe, mas `ctx` deve ser específico do episódio quando o título indicar cena diferente.
3. **Verificação independente** (outro agente, sem ver a base como verdade): `tools/cult/kb/verify2_CURSO_K.json` `{obra: {v: ok|fix|drop, why, y1?, by?, blurb?, lines?, ctx?, src?, kb2?:{intro,leitura,facts}}}` com fontes pesquisadas; `python3 tools/cult/apply_verify.py CURSO verify2` aplica.
4. `python3 tools/cult/inject.py CURSO` (cria o quadro `cultcena` e enriquece a linha do tempo) e `python3 tools/cult/inject2.py CURSO` (aplica a apresentação rica em cultob/cultcena/culttl). Quem integra é o coordenador (não rode estes dois nem edite data/ nos blocos de escrita/verificação).
