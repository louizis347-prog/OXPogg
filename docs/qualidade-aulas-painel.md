# Qualidade das aulas ao vivo do Painel do Professor

Gerado por `professor/src/quality_report.py`. É uma fila de revisão automática: aponta onde olhar, não substitui a revisão humana.

## Quest (1700 aulas)

- Esqueleto de telas: 81% das aulas têm exatamente a mesma sequência (10 sequências distintas).
- Obras culturais distintas: 1425; repetidas em mais de uma aula: 125.
- Títulos de tela repetidos em ≥50% das aulas: me → “Sobre você · começo” (1700×); review → “Mochila · expressões” (1700×); work → “A obra e a situação” (1700×); story → “Cena da obra” (1700×); facts → “A situação em contexto” (1699×); compare → “Brasil e Estados Unidos” (1700×); quiz → “Entenda a ideia” (1700×); dialog → “Conversa · começo” (1699×); choice → “Sua resposta · 1/5” (1697×); vocab → “Palavras em ação · 1/2” (1700×); verbs → “Verbos em ação · 1/2” (1700×); verbplay → “Aplique os verbos” (1700×); exprs → “Expressões comuns” (1700×); exprplay → “Qual expressão usar?” (1700×); soundlab → “Laboratório de sons · o som” (1700×); role → “Missão ao vivo” (1700×); writing → “Escreva a sua versão” (1699×); exit → “Mostre o que aprendeu” (1700×); finish → “Missão concluída” (1700×); bridge → “Ponte · português → inglês” (1699×).

Aulas com mais avisos (primeiras 15):

- **Quest 131** · I need help! — falas curtas (média < 5 palavras) | muitas falas com até 3 palavras | obra repetida em 2 aulas | obra com ligação fraca com o tema (heurística)
- **Quest 32** · Water, please — falas curtas (média < 5 palavras) | muitas falas com até 3 palavras | obra repetida em 2 aulas
- **Quest 36** · Burger combo — falas curtas (média < 5 palavras) | obra repetida em 4 aulas | obra com ligação fraca com o tema (heurística)
- **Quest 53** · Airport check-in — falas curtas (média < 5 palavras) | muitas falas com até 3 palavras | obra repetida em 3 aulas
- **Quest 54** · Security and the gate — falas curtas (média < 5 palavras) | obra repetida em 2 aulas | obra com ligação fraca com o tema (heurística)
- **Quest 57** · I'm lost — falas curtas (média < 5 palavras) | obra repetida em 2 aulas | obra com ligação fraca com o tema (heurística)
- **Quest 90** · At the museum — falas curtas (média < 5 palavras) | obra repetida em 3 aulas | obra com ligação fraca com o tema (heurística)
- **Quest 1001** · A sandwich at the deli — falas curtas (média < 5 palavras) | muitas falas com até 3 palavras | obra repetida em 2 aulas
- **Quest 1007** · A birthday cake — falas curtas (média < 5 palavras) | muitas falas com até 3 palavras | obra repetida em 9 aulas
- **Quest 1236** · Hiking trail — estrutura “the hill trail” em 4 de 11 falas | obra repetida em 2 aulas | obra com ligação fraca com o tema (heurística)
- **Quest 1245** · Theme park rides — estrutura “you have to” em 4 de 11 falas | obra repetida em 2 aulas | obra com ligação fraca com o tema (heurística)
- **Quest 133** · Where is the ATM? — falas curtas (média < 5 palavras) | obra repetida em 2 aulas | obra com ligação fraca com o tema (heurística)
- **Quest 139** · Wash my car — falas curtas (média < 5 palavras) | muitas falas com até 3 palavras | obra repetida em 2 aulas
- **Quest 171** · Booking a table — falas curtas (média < 5 palavras) | obra repetida em 9 aulas | obra com ligação fraca com o tema (heurística)
- **Quest 173** · At the drive-thru — falas curtas (média < 5 palavras) | muitas falas com até 3 palavras | obra repetida em 3 aulas

Resumo dos avisos:

- obra repetida em N aulas: 400 aulas
- obra com ligação fraca com o tema (heurística): 238 aulas
- obra sem ano: 225 aulas
- estrutura “…” em N de N falas: 117 aulas
- falas curtas (média < N palavras): 112 aulas
- muitas falas com até N palavras: 21 aulas
