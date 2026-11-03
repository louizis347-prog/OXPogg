# Aulas Quest v5 — junção enxuta (curso regular + Neighbors)

Cada aula 1–50 do Painel do Professor (`professor/aula4.html?n=N`) junta **um episódio do Neighbors inglês A1 (`nb-a1`, aula N)** com **um episódio do curso regular `en-a1` casado pelo TEMA**. O montador `professor/src/build_v5.py` pega do material existente: diálogo, expressões, regra, troca de palavras, sons, vocabulário, ditado, missão, cenas/personagens, figurinha. O suplemento `professor/src/supp5/sNNN.py` traz só o que é novo.

## O que você escreve (um arquivo por aula, `SUPP = dict(...)`)
- `reg`: número R do episódio regular mais próximo do tema do Neighbors (lista em `src/supp5/_titles.txt`, linhas `R<n> | título | obra`). Prefira não repetir o mesmo R em aulas diferentes. Veja o que o episódio tem com `python3 src/show_v5.py N R`.
- `culture` (inglês, curto; pode mencionar o Brasil em `compare`): `hook` (≥15 palavras), `mythfact` ≥4 `{s, ans:bool, why}` (misture verdadeiros e falsos), `wild` 2 `{kind, lines[], decode:{q,opts[3],ans,why}}` (cardápio, aviso, mensagem… reais), `compare {br, us, tip, ask}`, `quiz` 3 `{q,opts[3],ans,why}`, `polite` (opcional). **Só fatos verdadeiros e verificáveis**; sem estatística inventada.
- `reading`: texto ORIGINAL de 170–320 palavras, 4+ parágrafos, inglês simples do nível A1 (frases curtas), ligado à cena do Neighbors e à obra do episódio regular, com as expressões-alvo em **negrito**. Campos: `genre, title, text[], glossary[≥8 {w,pt}]` (cada `w` aparece no texto), `fast {q,opts[3],ans,why}`, `scan[3 {q, ans, alt[]}]`, `tf[≥4 {s,ans:bool,why}]` (mistos), `order[5]` (eventos na ordem correta), `ctx[3 {sent,w,opts[3],ans,why}]` (`w` está em `sent`), `chunkHunt[]`, `think`.
- `convo`: `{npc:{name}, story, turns:[≥4 {npc, pt, opts:[3 {en,pt,ok,fb}]}]}` seguindo o diálogo do Neighbors (o `npc` diz a fala; a opção `ok:true` é a resposta natural; as 2 erradas são erros plausíveis de brasileiros ou respostas fora de contexto; `fb` curto em inglês; **exatamente uma `ok`; varie a posição da correta**).
- `errors`: ≥4 `{wrong, fix, alt, why}` (frase errada típica de brasileiro, a correta, um segundo erro, motivo).
- `homework` (1 frase) e `homework_items` (4 itens). Opcional: `complications` (3), `badge {icon,name,desc}`, `sticker`.
- Texto da aula em **inglês** (A1), `pt` apenas nos campos `pt`/glossário. Não copie os textos de outras aulas nem das aulas antigas (`data/v3`, `supp/`). Modelo: `src/supp5/s001.py`.

## Passos
1. `python3 src/show_v5.py N` (lê o Neighbors), escolha `reg`, `python3 src/show_v5.py N R`.
2. Escreva `src/supp5/sNNN.py`. 3. `python3 src/validate_v5.py N` até `ok`. 4. Não faça commit/push; não edite outros arquivos.
