# Trilha da aula ao vivo no PoggloDict: como manter as duas alinhadas

Regra de trabalho: **a ordem da aula ao vivo (Painel) manda, e o PoggloDict só ganha lições: nada é substituído nem removido por conta própria.** Depois, com o conjunto à vista, você decide o que sai, o que fica e o que muda de lugar.

Para cada grupo de aulas ao vivo:
1. Listar o que a aula ensina (vocabulário, estruturas, funções) e conferir o que o PoggloDict já cobre (`tools/pd_links_build.py`, mapa `LINKS`).
2. O que faltar vira **lição nova**, no formato das lições autorais do A1 (5 frases de leitura, 8 falas de diálogo, pronúncia, exercício, 4–5 palavras; mini-história nas lições múltiplas de 10).
3. Ligar a aula às lições (antes, aquecimento, depois) com o script e testar no navegador.

## Onde as lições novas entram
- **Acrescentadas ao final do A1 inglês**, depois da lição 350, em blocos de 10 na ordem das aulas ao vivo: **351–360** já existem (aulas ao vivo 1–10); o próximo bloco será **361–370**, e assim por diante. O PoggloDict inglês A1 passa a ter 360 lições (o app mostra “Lição N de 360” só no inglês A1; os demais idiomas e níveis continuam com 350).
- Cada bloco de 10 termina em uma revisão com mini-história (posição múltipla de 10).
- Fonte das lições: `poglodict/fontes/a1-181-360/NNN.json`; depois rode `python3 tools/poglodict_build_a1.py` e `python3 tools/pd_links_build.py`.
- O conteúdo antigo das lições 301–310 (casa e tarefas) foi mantido como estava.
- Vocabulário de base (cumprimentos, números, família…) pode repetir o de outras lições; o que importa é a sequência.

## Limites conhecidos
- Quem usa o PoggloDict sozinho vê o bloco da trilha ao vivo no fim do A1 (351+); para a turma, o caminho é o dos quadros “antes da aula”.
- A decisão de remover, reordenar ou mesclar lições fica para depois que houver mais blocos.
- Ainda não há código da turma nem progresso sincronizado: o professor não vê quem fez a prévia.
- Para outros níveis (A2, B1) a mesma lógica vale, mas o suporte a mais de 350 lições hoje só existe no inglês A1.
