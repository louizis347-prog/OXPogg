# Neighbors · Espanhol B2 · Bíblia da série «El Faro del Barrio»

300 episódios = 30 arcos × (9 episódios + 1 revisão automática). Esqueletos em `data/nbes-b2_NN.json` (campos `t`, `s`, `city`/`sc`, `pe` = personagem do episódio, `plan.learn`, `plan.sample`, `d`). Siga o `tools/nb/SPEC_GUIA.md` e use os arcos `tools/nb/specs/nbes-b1_a05.py` e `nbes-a2_a35.py` como modelo de qualidade e formato.

## Premissa
O aluno («Y», brasileiro/a) mora em Madrid há um ano e estagia no **El Faro del Barrio**, jornal local do bairro de Lavapiés, dirigido por Javier. Cada arco é uma «matéria» do jornal ligada ao tema gramatical/cultural do arco. A voz do aluno em `chat` é sempre «Y».

## Elenco fixo (use SEMPRE a personalidade e o nome do esqueleto `pe`)
- **Javier** (60, diretor do jornal; culto, cita Cervantes e García Márquez; guarda um segredo: o jornal está quebrado).
- **Lucía** (reportera estrella, ambiciosa; rival simpática do aluno).
- **Carmen** (administradora do prédio; rígida mas justa; sabe que o prédio vai ser vendido).
- **Valentina** (advogada do 2ºA; irônica; ajuda com contratos).
- **Pablo** (vizinho, fotógrafo freelance; brincalhão; apaixonado em segredo por Camila).
- **Santiago** (arquiteto; perfeccionista; dirige a reforma do prédio).
- **Camila** (doutoranda colombiana; melhor amiga e confidente do aluno).
- **Diego** (cozinheiro do bar «La Esquina»; fofoqueiro).
- Secundários por cidade: Ximena, Lupita, Memo (Cidade do México); Facundo, Julieta, Sofía, Mariana (Buenos Aires); Andrés, Matías, Cristóbal, Fernanda, Tomás (onde o esqueleto indicar).

## Três atos
- **Ato I (arcos 1–10)**: o aluno ganha seu lugar no jornal.
- **Ato II (arcos 11–20)**: corre o boato de que o prédio vai ser vendido e que o jornal fecha.
- **Ato III (arcos 21–30)**: cultura, comunidade e a luta para salvar o prédio e o jornal; o arco 30 fecha a série (a exposição final; o prédio e o jornal se salvam).

## Gancho de série (obrigatório)
1. **Todo episódio termina com um gancho**: a ÚLTIMA fala do `chat` (sempre do parceiro «P») deve plantar uma curiosidade, promessa ou pergunta que o episódio seguinte retoma (por exemplo: «Mañana te cuento lo de Santiago… pero no se lo digas a nadie.»). No `hook` do episódio seguinte, faça uma pequena retomada («callback») sem repetir frases literais.
2. **Ganchos de fronteira entre blocos de agentes** (o último episódio do arco indicado DEVE terminar assim, e o primeiro episódio do arco seguinte DEVE abrir retomando isso):
   - fim do arco 3 → «Javier quiere verte esta noche en la redacción. Dice que es importante.» → arco 4 ep.1: Javier oferece ao aluno a vaga fixa no jornal.
   - fim do arco 6 → «Lucía ha publicado tu reportaje con su firma.» → arco 7 ep.1: o aluno a confronta (com tom B2: queixa e reparação).
   - fim do arco 9 → «Javier se va dos semanas y te deja la redacción a tu cargo.» → arco 10 ep.1: o aluno assume.
   - fim do arco 12 → «Carmen te enseña un papel: el edificio tiene comprador.» → arco 13 ep.1: começa a investigação.
   - fim do arco 15 → «El comprador se llama Grupo Orión, y alguien del edificio lo sabía.» → arco 16 ep.1.
   - fim do arco 18 → «Alguien ha filtrado tu borrador a Grupo Orión.» → arco 19 ep.1.
   - fim do arco 21 → «Santiago confiesa que firmó un informe que no debía.» → arco 22 ep.1.
   - fim do arco 24 → «El Faro cierra el viernes si no consigue quinientos suscriptores.» → arco 25 ep.1.
   - fim do arco 27 → «La última oportunidad es la exposición del viernes. Y tú tienes que hablar.» → arco 28 ep.1.
   - arco 30: encerramento — exposição final, o prédio e o jornal se salvam; o último gancho é de despedida («Y mañana… ¿qué vamos a investigar?»).
3. Dentro do bloco, cada agente cria subtramas curtas (um mistério por arco), mantendo coerência com o elenco.

## Qualidade (produto pago)
- Espanhol 100% correto, natural, nível **B2 (DELE/SIELE B2)**: conectores, subjuntivo variado, registro formal e informal, ironia, expressões idiomáticas reais. Varie sotaque/vocabulário conforme a cidade (Madrid, Bogotá, CDMX, Buenos Aires).
- Português do Brasil claro; falsos amigos e dicas de pronúncia úteis para brasileiros.
- Reutilize vocabulário dos episódios anteriores do arco; nada de frases repetidas entre episódios; nenhum campo vazio; sem vulgaridade pesada nem política partidária; fatos culturais/históricos corretos (arcos 22–25: García Márquez, Guerra Civil, Gaudí, tango→reguetón: só afirme o que tem certeza).
- Valide cada arco com `python3 tools/nb/run_arc.py <SPEC.py> es nbes-b2 <ARCO> <BASE> <REVBASE> --dry` até passar. BASE = 91101 + 10*(ARCO-1); REVBASE = 94700 + ARCO. **Não grave em data/** (sem `--dry` é proibido: quem integra é o coordenador).
