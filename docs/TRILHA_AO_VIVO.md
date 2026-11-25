# Trilha da aula ao vivo no PoggloDict: como manter as duas alinhadas

Regra de trabalho: **a ordem da aula ao vivo (Painel) manda.** Para cada grupo de aulas ao vivo:
1. Listar o que a aula ensina (vocabulário, estruturas, funções) e conferir se o PoggloDict já tem lições que cobrem isso (`tools/pd_links_build.py`, mapa `LINKS`).
2. O que faltar vira **lição nova no PoggloDict**, no formato das lições autorais do A1 (5 frases de leitura, 8 falas de diálogo, pronúncia, exercício, 4–5 palavras; mini-história nas lições múltiplas de 10).
3. Ligar a aula às lições (antes, aquecimento, depois) com o script e testar no navegador.

## Onde as lições novas entram
O PoggloDict A1 tem 350 posições fixas, todas já ocupadas. As lições novas **substituem lições do bloco A1 301–339** (autorais minhas, sem ligação com a sequência ao vivo), sempre em ordem e fora das posições múltiplas de 10 que carregam mini-história (a revisão do bloco fica na posição 10 de cada bloco).
- Usadas: **301–310** (bloco “Conhecendo pessoas”, aulas ao vivo 1–10).
- Livres para os próximos blocos: 311–319 (+320 revisão), 321–329 (+330), 331–339 (+340). Depois disso será preciso decidir de onde tirar mais posições (por exemplo, partes de 181–300).
- Fonte das lições: `poglodict/fontes/a1-181-350/NNN.json`; depois rode `python3 tools/poglodict_build_a1.py`.
- Vocabulário de base (cumprimentos, números, família…) pode e deve repetir o de outras lições; o que importa é a sequência.

## Limites conhecidos
- O conteúdo antigo das posições 301–310 (tarefas da casa) foi substituído; ele continua no histórico do git. Se for preciso, recriamos esse conteúdo quando uma aula ao vivo pedir.
- O PoggloDict standalone (quem não faz aula ao vivo) vê o bloco 301–310 no fim do A1; para essas pessoas o caminho recomendado é a ordem do “antes da aula”.
- Ainda não há código da turma nem progresso sincronizado: o professor não vê quem fez a prévia.
