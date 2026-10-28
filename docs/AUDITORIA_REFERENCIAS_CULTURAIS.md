# Auditoria #2 — referências culturais e capas (inglês regular, 3.000 episódios)

Base: `main` + merge 865b7232. Métricas calculadas sobre `data/en-*.json` e `PogObra.meta()`.
CSV com os episódios problemáticos: `docs/AUDITORIA_REFERENCIAS_CULTURAIS.csv`. Grade visual: `docs/auditoria_capas_grade.png`.

## 1. Referências culturais
| Métrica | Resultado |
|---|---|
| Episódios | 3.000 (A1 466, A2 474, B1 530, B2 510, C1 510, C2 510) — contagem por nível não é 500 |
| Obras distintas (normalizadas) | **2.975** (antes: 2.770) |
| Obras repetidas | 25 grupos / 50 episódios (ex.: Marianela, Niebla, Nada, Antipoemas) |
| Obras que atravessam níveis | 20 |
| Títulos provavelmente não ingleses | **394** (A1 10 · A2 46 · B1 49 · B2 84 · C1 116 · C2 89) |
| Resíduo de template ("Cultural anchor", "siglo") | 0 |

Os 10 primeiros A1 continuam coerentes com a referência (Paddington, Paisaje Cafetero, Oz, Peter Pan, Toy Story, Branca de Neve e Rosa Vermelha, 80 Dias, Kim, Mil e Uma Noites, Madeline).
Falta ainda: zerar as 25 repetições e decidir a política dos 394 títulos em outro idioma (obras hispânicas em inglês regular).

## 2. Capas
- **Bug corrigido nesta entrega:** em `js/obra-art.js` a função local `P()` escondia o estado global `P` do player; `has()` dava sempre falso e **nenhuma capa por obra aparecia no app**. Corrigido (`playerState()` via eval indireto); agora `svg.obra-art.obra-cover` é injetado.
- **Distinção visual é fraca.** Chave única existe nos 3.000 (por hash), mas visualmente:
  - só **6 paletas** em todo o curso;
  - **8 cenas**, sendo **64% "city"** (1.916/3.000);
  - 37 motivos; apenas **377 combinações** cena+motivo+paleta (as 2 mais comuns somam 385 episódios);
  - sempre os **mesmos dois personagens iguais**, só trocando cor de roupa.
- Contra a referência (10 capas desenhadas à mão, com personagens e cenário próprios da obra), a arte procedural é **genérica**: Alice/Oz/Peter Pan não são reconhecíveis. A arte à mão foi sobrescrita no merge da outra sessão e ainda está no histórico git.
- `landing-pro.js`, `home-new.js`, `figurinhas.js`, `obra-theme.js` e `pilot-reward.js` usam a API antiga (`PogObra.svg(id,'obra-cover')`, `face('alice')`); a landing mostra arte genérica.

## 3. Recomendações (aguardam decisão)
1. Restaurar as 10 capas à mão como camada "premium" sobre o gerador (`js/obra-art-hand.js`).
2. Ampliar o gerador: mais cenas (hoje 8), 20+ paletas, elenco variável por obra (ids de personagens), tirar o viés "city".
3. Adaptar landing, home, figurinhas e tema à API nova.
4. Substituir as 25 obras repetidas e definir política para os 394 títulos não ingleses.
5. Capas à mão para as próximas centenas de episódios por lote (ex.: 5 por nível).

## 4. Correções aplicadas (após esta auditoria)
- 25 obras repetidas trocadas + 9 colisões que a normalização com subtítulo revelou → **3.000 obras distintas** (`tools/audit/fix_dup_works.py`; plano `tools/plan/map` sincronizado).
- Gerador de capas reescrito: paleta por hash (3.000 distintas, antes 6), 10 cenas (cena dominante 17%, antes 64% “city”), skyline variável, personagens com visuais diferentes → **3.000 capas distintas**.
- Nova trava `tools/audit/trava_referencias_capas.js` (também no workflow). Prompt de replicação: `docs/PROMPT_REFERENCIAS_E_CAPAS.md`.
- **Os 394 “não ingleses” eram heurística** (acentos e artigos), com falsos positivos (Amélie, Sagrada Família, Teatro Colón são nomes próprios). Ainda é decisão de política; não foram alteradas.
- Pendente: restaurar os 10 desenhos à mão como camada premium; adaptar landing/home/figurinhas à API nova.
