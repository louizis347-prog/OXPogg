# Qualidade das aulas ao vivo do Painel do Professor

Gerado por `professor/src/quality_report.py`. É uma fila de revisão automática: aponta onde olhar, não substitui a revisão humana.

## Quest (200 aulas)

- Esqueleto de telas: 97% das aulas têm exatamente a mesma sequência (4 sequências distintas).
- Obras culturais distintas: 200; repetidas em mais de uma aula: 0.
- Títulos de tela repetidos em ≥50% das aulas: review → “Mochila · expressões” (200×); reviewwords → “Mochila · palavras” (200×); quiz → “Mochila · desafio” (200×); reviewsay → “Mochila · fale” (200×); work → “A obra e a situação” (200×); facts → “A situação em contexto” (199×); compare → “Brasil e Estados Unidos” (200×); dialog → “Conversa · começo” (199×); choice → “Sua resposta · 1/5” (198×); vocab → “Palavras em ação · 1/2” (200×); verbs → “Verbos em ação · 1/2” (200×); verbplay → “Aplique os verbos” (200×); exprs → “Expressões comuns” (200×); exprplay → “Qual expressão usar?” (200×); soundlab → “Laboratório de sons · o som” (200×); role → “Missão ao vivo” (200×); writing → “Escreva a sua versão” (199×); exit → “Mostre o que aprendeu” (200×); finish → “Missão concluída” (200×).

Aulas com mais avisos (primeiras 15):

- **Quest 131** · I need help! — falas curtas (média < 5 palavras) | muitas falas com até 3 palavras | obra com ligação fraca com o tema (heurística)
- **Quest 10** · Days of the week — falas curtas (média < 5 palavras) | obra com ligação fraca com o tema (heurística)
- **Quest 22** · Party invitation — falas curtas (média < 5 palavras) | obra com ligação fraca com o tema (heurística)
- **Quest 25** · Pizza by the slice — falas curtas (média < 5 palavras) | muitas falas com até 3 palavras
- **Quest 26** · What's in this? — falas curtas (média < 5 palavras) | muitas falas com até 3 palavras
- **Quest 31** · Coffee, your way — falas curtas (média < 5 palavras) | muitas falas com até 3 palavras
- **Quest 32** · Water, please — falas curtas (média < 5 palavras) | muitas falas com até 3 palavras
- **Quest 33** · At the bakery — falas curtas (média < 5 palavras) | obra com ligação fraca com o tema (heurística)
- **Quest 35** · Fruit by the pound — falas curtas (média < 5 palavras) | muitas falas com até 3 palavras
- **Quest 36** · Burger combo — falas curtas (média < 5 palavras) | obra com ligação fraca com o tema (heurística)
- **Quest 48** · Taking a taxi — falas curtas (média < 5 palavras) | muitas falas com até 3 palavras
- **Quest 53** · Airport check-in — falas curtas (média < 5 palavras) | muitas falas com até 3 palavras
- **Quest 54** · Security and the gate — falas curtas (média < 5 palavras) | obra com ligação fraca com o tema (heurística)
- **Quest 57** · I'm lost — falas curtas (média < 5 palavras) | obra com ligação fraca com o tema (heurística)
- **Quest 58** · Buying tickets — falas curtas (média < 5 palavras) | muitas falas com até 3 palavras

Resumo dos avisos:

- falas curtas (média < N palavras): 95 aulas
- obra com ligação fraca com o tema (heurística): 33 aulas
- muitas falas com até N palavras: 14 aulas

## Real-Life (100 aulas)

- Esqueleto de telas: 100% das aulas têm exatamente a mesma sequência (1 sequências distintas).
- Obras culturais distintas: 0; repetidas em mais de uma aula: 0.
- Títulos de tela repetidos em ≥50% das aulas: nenhum.

Aulas com mais avisos (primeiras 15):

- **Real-Life 27** · Checking in at the airport — falas curtas (média < 5 palavras) | muitas falas com até 3 palavras
- **Real-Life 73** · Comparing Two Things Before You Buy — estrutura “the gray one” em 5 de 9 falas

Resumo dos avisos:

- falas curtas (média < N palavras): 1 aulas
- muitas falas com até N palavras: 1 aulas
- estrutura “…” em N de N falas: 1 aulas
