# Prompt — referência cultural única e capa própria por episódio (curso regular)

Você vai criar/revisar episódios do curso regular de inglês do Pogglot (modelo `regular-pilot-v1`, padrão dos episódios 2–5 do A1).

## Referência cultural (`a.w`, `a.y`, `a.k`, `h.src`)
1. Cada episódio tem **uma obra real, própria e única nos 3.000 episódios** (livro, filme, série, canção, pintura, peça, poema, jogo, lugar/tradição).
2. Unicidade pela normalização forte: minúsculas, sem acento, sem parênteses, **sem subtítulo depois de “:”**, sem artigo inicial (the/a/an/el/la/le/o/os). “Rear Window: Whodunit” e “Rear Window” são a mesma obra; “Peter Pan” e “Peter and Wendy”, também.
3. Mesma franquia ≠ obra nova só por mudar o número (evite “Paddington” duas vezes).
4. Título **em inglês** (ou nome próprio consagrado: Sagrada Família, Amélie). Obra hispânica/lusófona só se a política do curso permitir; nesse caso nunca repita entre níveis.
5. Tipo (`a.k`) e ano (`a.y`) corretos para a obra. Nada de “Cultural anchor”, “(siglo XX)” ou descrição genérica copiada.
6. A obra aparece na ponte: `h.src`, `cover.gancho`, cena 1/2, missão “Cena da obra”, figurinha.
7. Ao trocar uma obra, troque **tudo** (título, tipo, ano, ponte) e atualize `tools/plan/map/en-*.json`. Use `python3 tools/audit/fix_dup_works.py`.

## Capa (gerador `js/obra-art.js`)
1. A capa é determinística pela obra: paleta HSL derivada do hash do título (harmonia análoga/complementar/tríade), **nunca** uma das 6 paletas fixas.
2. Cena por palavra-chave (água, floresta, palco, lab, biblioteca, museu, cozinha) ou, sem palavra-chave, **por hash** entre 10 cenas (nunca “city” por padrão). Máx. 25% dos episódios na mesma cena.
3. Dois personagens **diferentes** (cabelo, acessório, cor); objeto-símbolo ligado à obra ou escolhido por hash.
4. Obras de referência (10 primeiros do A1) podem ter arte desenhada à mão como camada premium por cima do gerador.
5. Nenhuma capa pode ser visualmente idêntica a outra.
6. **Nível de detalhe = capas desenhadas à mão** (medido nas 10 referências): ≥110 elementos SVG, ≥18 cores de preenchimento, ≥30 paths, ≥2 gradientes (céu e chão), 3 figuras com rosto (2 crianças com cabelo, roupa, blush e olhos com brilho + 1 bichinho), ≥6 itens de cenário (flores gigantes, cogumelos, brilhos, borboleta, balão, tufos de grama), traço de nanquim e SVG XML válido.
7. Os recortes usados dentro do episódio (`sticker`, `strip` da faixa “Obra em foco”, `face`) vêm do mesmo SVG e precisam mostrar os rostos (≥2 em cover/sticker/strip, ≥1 em face).

## Trava (obrigatória antes de publicar)
```
python3 -m http.server 8123 &
node tools/audit/trava_referencias_capas.js      # 3.000 obras e capas distintas, cena dominante ≤ 25%, ≥ 600 paletas, detalhe mínimo e rostos visíveis em cada recorte
python3 tools/audit/regular_gate.py && python3 tools/audit/english_bridge_gate.py && python3 tools/build_data_index.py --check
```
Falhou = não publica. A mesma trava roda no GitHub Actions (`regular-quality-gate.yml`).
