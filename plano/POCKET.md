# Pocket · plano do curso (assinatura)

**Ideia:** episódios de 5 quadros e 3–4 minutos, situação do dia a dia, fala primeiro, jogo, som e personagens. Sem repetição de prática:
cada frase aparece 3 vezes (diálogo, montagem, fala) e volta no episódio seguinte por reciclagem natural.

## Meta: 5.000 episódios, por níveis do QECR/CEFR
| Nível | Episódios | Arcos de 10 | Horas guiadas (aprox.) | Foco |
|---|---|---|---|---|
| A1 | 800 | 80 | ~55 h | sobreviver: cumprimentar, pedir, perguntar, números, rotina |
| A2 | 1.000 | 100 | ~70 h | tarefas simples: compras, transporte, saúde, planos, passado simples |
| B1 | 1.200 | 120 | ~80 h | opinar, narrar, resolver problemas, trabalho, viagens |
| B2 | 1.100 | 110 | ~75 h | argumentar, negociar, registro formal/informal, mídia |
| C1 | 600 | 60 | ~40 h | nuance, humor, ironia, escrita profissional |
| C2 | 300 | 30 | ~20 h | precisão, estilo, cultura profunda |
| **Total** | **5.000** | **500** | ~340 h | |

(Cada episódio = ~4 min. As horas totais do QECR contam também estudo fora do app; o Pocket é a dose diária.)

## Quadros (sempre 5)
1. **Cena** – capa ilustrada, missão e frase-chave com som.
2. **Diálogo** – 6 a 8 falas em balões com avatares; toque na fala ou na palavra.
3. **Monte a frase** – troca de peças (reciclagem), 2 rodadas.
4. **Fale** – microfone, 2 respostas.
5. **Mochila** – frases, 1 expressão, 1 curiosidade cultural, figurinha do personagem.

## Estrutura de arco (10 episódios)
Episódios 1–9: situações; episódio 10: **mini-chefe** (conversa que junta as frases do arco) + figurinha rara.
Cada arco tem 1 personagem-guia fixo e 1 cenário principal diferente do arco anterior.

## Produção
- Conteúdo escrito à mão em lotes de 10 episódios (1 arco) por arquivo `tools/pocket/<nivel>_arcoNN.py`.
- `python3 tools/pocket/build.py` gera `data/pk-<nivel>_NN.json` e atualiza `data/manifest.json`.
- Auditoria: lint (EN/PT, 5 quadros, chips), layout (celular/PC), trava de duplicatas de frase-chave.
- Cobrança: o Pocket entra na mesma assinatura do app (primeiros episódios grátis por curso).
