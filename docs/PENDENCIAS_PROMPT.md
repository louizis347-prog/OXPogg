# Pendências do curso regular de inglês — prompt para a próxima sessão

Contexto: Pogglot (repo louizis347-prog/OXPogg), curso regular de inglês A1–C2, 3.000 episódios em `data/en-<nível>_NN.json`.
A obra de cada episódio está em `a.w` (título), `a.d` (descrição); a aula em `t`, `p`, `s`, `v`, falas.
Regra do projeto: cada obra aparece **uma só vez** no curso; título/descrição/capa têm de combinar com a aula. Não alterar a aula nem os emojis. Publicar por PR + merge no `main`; subir `sw.js` (`pogglot-shell-vNNN`).

## 1. Obras repetidas (trava `node tools/audit/trava_referencias_capas.js` falha: 2.992 ≠ 3.000)
Cada par abaixo é a mesma obra em dois episódios. Em um deles, trocar a obra (título `a.w`, ano `a.y`, tipo `a.k`, descrição `a.d`, ficha em `tools/ficha/work/*_zzscenes.json`) por uma obra livre que combine com a aula, e rodar `python3 tools/scenes/apply.py` + `tools/ficha/validate.py`.
- 70052 (A1) × 7083286 (B2) — Cafe Terrace at Night
- 80312 (A1) × 81158 (A2) — The Three Billy Goats Gruff
- 81288 (A2) × 82231 (B1) — Anthony Bourdain (Parts Unknown × No Reservations; tratar como a mesma obra)
- 7082004 (B1) × 7960121 (C2) — The Help × Help! (conferir se a trava os considera iguais)
- 930059 (B1) × 85119 (C2) — Wall Street × Wall Street: Money Never Sleeps
- + mais 3 pares: rodar a trava com a lista completa (`R.dups`, hoje só imprime 5).

## 2. Título que não bate com a descrição (corrigido pelo agente de cenários só na capa)
- 83105 (B2) "Their Eyes Were Watching God" — a sinopse é de *Wuthering Heights* (Lockwood, Nelly Dean, Earnshaw).
- 7083135 (B2) "The Diving Bell and the Butterfly" — a descrição é de "green with envy" (cita Moby-Dick).
- 83071 (B2) "The Erie Canal" — a descrição fala de O Apanhador no Campo de Centeio ("The Man Standing There").
Ação: reescrever título/ano/tipo/descrição para uma obra que combine com `t` e a aula (sem mexer na aula) e revisar a capa.

## 3. Ficha com defeito
- 82273 (B1): `check_render.js` → "face: sem olhos". Corrigir a ficha.

## 4. Já resolvido (não refazer)
Os 46 episódios "ERRADO" de `docs/REVISAO_TITULO_AULA.csv` (20 de outra obra + 26 genéricos) já têm título/descrição novos e não repetem obra, inclusive 950013, 85070 e 960061.

## 5. Opcional (não pedido)
- 34 casos "FRACO" no CSV (ligação frouxa, defensável) — revisar se quiser.
- Capas por associação livre (ex.: Scarface em hotel, Hubble em laboratory, "1776" em throne) — conferir visualmente.
- `tools/generic/out`: ondas não aplicadas; não aplicar sem revisão.
- Restyle de 4 fichas (Moomins etc.) e a troca da Beavis.

## Verificação ao final
`node tools/audit/trava_referencias_capas.js`, `python3 tools/ficha/validate.py --curso en-<nível>`, `node tools/ficha/check_render.js en-<nível>`, `python3 tools/build_data_index.py --check`.
