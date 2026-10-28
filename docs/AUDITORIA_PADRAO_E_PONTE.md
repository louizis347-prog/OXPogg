# Auditoria de padrão e ponte obra↔episódio — inglês regular A1–B2 (do episódio 6 em diante)

Régua: os episódios de referência 2–5 do A1 (n 7009801, 70001, 7070001, 30001) e o contrato `tools/audit/regular_pilot_contract.py`. Ferramenta: `tools/audit/regular_bridge_audit.py` (resultado em `tools/audit/regular_bridge_audit.json`). Mede só o que dá para medir por script; qualidade de língua, fatos e arte continuam pedindo olho humano.

## 1. Estrutura e densidade (contrato)
Os 1.980 episódios de A1, A2, B1 e B2 passam no contrato sem nenhuma falha: 19 quadros na ordem, 6 palavras, 4 verbos, 4 expressões, laboratório 3+3, duas cenas, 3 missões, mochila, obra própria e única no curso. A trava (`regular_gate.py`) confirma 0 falhas nesses quatro níveis. Também medidos aqui: 5 objetos clicáveis em posições distintas (100%), mochila é do episódio anterior (100%), `say` em todos os quadros de prática (100%), cenário nunca repetido 3 vezes seguidas (95–99%).

## 2. Ponte entre a obra e o episódio (o que ainda falta)
A ponte = a obra aparece DENTRO da aula, como nos episódios de referência (elenco, cena e figurinha da obra) e mais: uma fala da cena ligada à obra (palavra do título/descrição ou personagem da obra) e a 1ª missão (“Cena da obra”) ligada ao enredo/personagem. Taxa de episódios (do 6º em diante) que passam, **depois do piloto** e com a régua final da trava (a missão conta só pelo enunciado e pelo modelo da 1ª missão; a primeira versão da auditoria contava a missão inteira, com regex e dicas, e superestimava):

| Nível | Elenco da obra (P1) | Obra nas cenas (P2) | Missão ligada à obra (P3) | P2 e P3 juntos | Elenco genérico |
|---|---:|---:|---:|---:|---:|
| A1 (461) | 80% | 76% | 35% | 156 (33%) | 20% |
| A2 (469) | 57% | 67% | 27% | 116 (24%) | 43% |
| B1 (525) | 68% | 52% | 16% | 75 (14%) | 32% |
| B2 (505) | 99% | 69% | 19% | 97 (19%) | 0% |

Total: **444 de 1960 episódios (22%)** cumprem cena e missão. O gargalo é a **missão (P3)**. No B2 só o final (406–505) está no nível pedido: 6–105: P2 54%, P3 11%; 106–305: P2 51%, P3 3%; 306–405: P2 90%, P3 26%; 406–505: P2 100%, P3 54%. Em A1, A2 e B1 a regra nunca foi aplicada.

Calibração: os episódios de referência passam tudo, exceto P3 em 70001 e 7070001 (a missão “Cena da obra” deles é genérica): por isso eles são o modelo e ficam fora das regras da ponte; a ponte na missão é um requisito NOVO, além da referência.

Observações: “P1” mede se o elenco é da obra; “Elenco genérico” mede nomes como Woman, Man, Girl… D4 (teaser) é só um indicador grosseiro: no B2 o teaser descreve o foco do próximo em português.

## 3. Conclusão
- **Padrão estrutural/densidade: adequado** (contrato e trava limpos nos quatro níveis).
- **Ponte obra↔episódio: NÃO está no padrão desejado.** Só 444 dos 1960 episódios (22%, do 6º em diante) cumprem as duas pontes (cena e missão); o B2 final (406–505) é o único trecho no nível pedido.
- **Elenco genérico:** 19% (A1), 43% (A2), 31% (B1) dos episódios ainda usam nomes genéricos.

## 4. Correção proposta
Aplicar uma camada de “ponte” por episódio em `tools/audit/bridge_patches/`: (a) uma fala da cena 1 (ou 2) reescrita para falar da obra usando o padrão do dia; (b) a missão “Cena da obra” reescrita para ligar o padrão ao enredo/personagem; (c) elenco com os personagens da obra quando faltar. Os patches são reaplicáveis por script depois de qualquer reconstrução dos dados.

## 5. Piloto (20 episódios, 5 por nível)
Aplicado e publicado: `tools/audit/bridge_patches/pilot_en-*.json` (resultado lado a lado em `docs/PILOTO_PONTE_ANTES_DEPOIS.md`). Os 20 do piloto passam em cena e missão. Contrato continua com 0 falhas em A1, A2, B1 e B2.
Defeitos achados nos próprios episódios durante o piloto (não são de ponte, ficam para a reconstrução): cena 2 com falantes trocados (7910029, 7080309), elenco fora da obra ou genérico (70065, 82106, 82177, 81086, 81228), cena 2 que repete a cena 1 (7081146, 7081310), campo da obra/tipo errado (7081030 badge A1 em A2; 82177 “Livro” para filme; 940029 título em português), padrão registrado que não bate (7940007), `gs` vazio (7083089).
