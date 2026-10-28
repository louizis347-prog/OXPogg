# Auditoria de padrão e ponte obra↔episódio — inglês regular A1–B2 (do episódio 6 em diante)

Régua: os episódios de referência 2–5 do A1 (n 7009801, 70001, 7070001, 30001) e o contrato `tools/audit/regular_pilot_contract.py`. Ferramenta: `tools/audit/regular_bridge_audit.py` (resultado em `tools/audit/regular_bridge_audit.json`). Mede só o que dá para medir por script; qualidade de língua, fatos e arte continuam pedindo olho humano.

## 1. Estrutura e densidade (contrato)
Os 1.980 episódios de A1, A2, B1 e B2 passam no contrato sem nenhuma falha: 19 quadros na ordem, 6 palavras, 4 verbos, 4 expressões, laboratório 3+3, duas cenas, 3 missões, mochila, obra própria e única no curso. A trava (`regular_gate.py`) confirma 0 falhas nesses quatro níveis. Também medidos aqui: 5 objetos clicáveis em posições distintas (100%), mochila é do episódio anterior (100%), `say` em todos os quadros de prática (100%), cenário nunca repetido 3 vezes seguidas (95–99%).

## 2. Ponte entre a obra e o episódio (o que ainda falta)
A ponte = a obra aparece DENTRO da aula, como nos episódios de referência (elenco, cena e figurinha da obra) e mais: uma fala da cena ligada à obra e uma missão ligada ao enredo/personagem. Taxa de episódios (do 6º em diante) que passam:

| Nível | Elenco da obra (P1) | Obra nas cenas (P2) | Missão ligada à obra (P3) | P2 e P3 juntos | Elenco genérico (D6 falha) |
|---|---:|---:|---:|---:|---:|
| A1 (461) | 81% | 54% | 53% | 183 (40%) | 19% |
| A2 (469) | 57% | 51% | 41% | 135 (29%) | 43% |
| B1 (525) | 69% | 40% | 30% | 101 (19%) | 31% |
| B2 (505) | 100% | 57% | 36% | 166 (33%) | 0% |

Por faixa, o B2 melhora muito no fim (do 306 em diante, depois do guia “a obra dentro da aula”): episódios 406–505 chegam a 97% em P2 e 79% em P3; os 6–305 ficam em 31–47% (P2) e 11–23% (P3). A1/A2/B1 não receberam essa regra.

Calibração: os episódios de referência passam tudo, exceto P3 nos episódios 70001 e 7070001 (a missão “Cena da obra” deles é genérica). Ou seja, a ponte na missão é um requisito NOVO, além da referência.

Observações: P1 mede se o elenco é da obra (nomes aparecem na obra/descrição/figurinha); “D6” mede nomes genéricos (Woman, Man, Girl…). D4 (teaser com o próximo episódio) é só um indicador grosseiro: no B2 o teaser descreve o foco do próximo em português e não repete o título.

## 3. Conclusão
- **Padrão estrutural/densidade: adequado** (contrato e trava limpos nos quatro níveis).
- **Ponte obra↔episódio: NÃO está no padrão desejado.** Só 585 dos 1.960 episódios (do 6º em diante) cumprem as duas pontes; o B2 final (406–505) é o único trecho no nível pedido.
- **Elenco genérico:** 19% (A1), 43% (A2), 31% (B1) dos episódios ainda usam nomes genéricos.

## 4. Correção proposta
Aplicar uma camada de “ponte” por episódio em `tools/audit/bridge_patches/`: (a) uma fala da cena 1 (ou 2) reescrita para falar da obra usando o padrão do dia; (b) a missão “Cena da obra” reescrita para ligar o padrão ao enredo/personagem; (c) elenco com os personagens da obra quando faltar. Os patches são reaplicáveis por script depois de qualquer reconstrução dos dados.
