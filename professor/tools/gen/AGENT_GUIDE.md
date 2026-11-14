# Guia para escrever aulas A2 (ficha gNNNN.py) — LEIA INTEIRO

## Tarefa
Escrever fichas `/tmp/gen/g20NN.py` (NN = número da aula, ex.: g2053.py) para as aulas do seu lote. Use SEMPRE `from mk import *` e `A2(k, d)` com k = NN − 2000 (ex.: `A2(53, d)`).
Modelos prontos e validados (copie a estrutura exata, troque o conteúdo): `/tmp/gen/g2051.py`, `/tmp/gen/g2036.py`, `/tmp/gen/g2020.py`.
O tema, cidade, personagem (npc), "you" e cena de cada aula vêm do plano `/tmp/a2/plan.py` (lista P; índice k−1). Não mude título/personagens. A estrutura gramatical da linha do plano é o foco da aula.

## Como validar (OBRIGATÓRIO, uma aula por vez)
`cd /tmp/gen && ./chk.sh 20NN`  → deve imprimir exatamente `20NN ok`.
Se aparecer FAIL ou qualquer linha começando por `SWAP?`, `GLOSS?`, `VOCABEX?`, `MOLD?`, `CEFR?`, `GRAMMAR?`, conserte e rode de novo. Para ver as linhas de aviso, rode `python3 -c "import sys;sys.path.insert(0,'/tmp/gen')" ` não é necessário: o chk.sh já mostra o final da saída; se ficar cortado, rode `cd /home/user/OXPogg/professor/src && python3 /tmp/gen/g20NN.py`.
NÃO rode runbatch.sh, build_v5.py, enrich_v6.py, finish.sh, git, nem edite mk.py/compact.py/dsl.py/common.py. Outros agentes trabalham em paralelo. Só crie/edite os SEUS arquivos g20NN.py.

## Regras de nível CEFR (o usuário é rígido: só entra o que de fato pertence ao nível A2)
Referência: CEFR-J Vocabulary/Grammar Profile (docs/NIVEIS_CEFR.md). Regra: **vocabulário** do diálogo só pode ser A1/A2 do CEFR-J, ou uma palavra mais difícil que a aula ENSINE (vocabulário `gl` 6 primeiras, verbos `vb`, expressões `ex`). O `mk.py` imprime `CEFR?` com as palavras fora da regra: troque por palavras simples (great, nice, good, big, small, happy…) ou, se for essencial, ensine-a em `gl`/`ex`. Máx. 2 palavras difíceis por aula. Nomes próprios (cidade, pessoas, ruas) são livres.
**Gramática PERMITIDA no A2 (só estas):** present simple e continuous (aff/neg/perguntas), frequência (always/usually/often/sometimes/never), there is/are, can/can't, imperativo afirmativo, would like/I'd like, Let's/How about, passado simples (was/were, regulares, irregulares, did/didn't, perguntas com did) com ago/last/yesterday/when, past progressive (was/were + -ing, com when), going to (afirmativo, negativo "am/is/are not going to", perguntas), will AFIRMATIVO (I'll help, It will be fun, I think it'll…), should AFIRMATIVO (You should rest), have to / has to AFIRMATIVO no presente (I have to work), comparativos (-er, more + adj, good/better, bad/worse) e superlativos (-est, most, best, worst), much/many/a lot of/a little/a few, too + adjetivo, how + adjetivo (how far/tall/old/long), if (1º condicional: If it rains, we’ll stay home) e when (When I get home, I’ll call you), passivo PRESENTE simples (It is made of wood / It is called… / It is sold here), perguntas com What/Where/When/Why/How/Who/Which (interrogativas), because/so/but/and/then.
**PROIBIDO (é B1+ ou duvidoso pela referência) — o mk.py acusa `GRAMMAR?`:** could, would (exceto would like), may, might, must/mustn't, used to, present perfect e past perfect (have/has + particípio, I've…, haven't), shouldn't, won't, "Will you…?/Will it…?" (pergunta com will), don't/doesn't/didn't have to, had to, "Should I…?", passivo no passado (was made/built), orações relativas (who/which/that + verbo), pronomes reflexivos (myself…), as…as, enough, perguntas indiretas (Do you know where…, Can you tell me where…), discurso indireto (told me, said that, asked me if), imperativo negativo (Don't + verbo; só "Don't worry" é aceito), segundo condicional (if I were/had… would).
Na dúvida, use a frase mais simples, com a estrutura permitida.

## Qualidade
- Diálogo próprio de 11 falas, naturais, nível A2, com a estrutura da aula bem visível (várias vezes); falas curtas.
- `O` (abertura) e `C` (fecho): 6 pares EN/PT cada, frases simples (presente/passado simples).
- PT-BR natural. Frases do diálogo sem estruturas proibidas. `err`: 4 erros comuns reais de brasileiros com a estrutura.
- Verbos `vb`: 5, cada um com forma passada DIFERENTE da base (evite read, put, cut, hit, set, cost) e 8 campos separados por | (veja os modelos).
- Cada `sw` (trocas): ≥ 6 entradas; a chave é o índice 0-based da fala; texto EN e PT devem ser **substrings exatas** (maiúsculas/minúsculas e contrações iguais) da fala daquele índice. Um índice por entrada; use índices de falas diferentes.
- `gl`: 9 itens (6 com emoji+exemplos, 3 só palavra/PT). Cada palavra de `gl` deve aparecer no texto (diálogo, abertura ou fecho). O exemplo longo (5º campo) deve conter a palavra.
- Moldes `mo`: o modelo (4º campo) tem de ser exatamente o frame preenchido com a PRIMEIRA opção de cada slot.
- Pares do soundlab `lab` (6º item): 3 pares com palavras diferentes entre si (a≠b).
- Exemplos `real`, `so` (3 sons), `chg` (3 mudanças em PT), `wt` (tarefa+modelo≥12 palavras+4 palavras-chave), `cu` (hook, 5 mf V/F, 2 wild, compare, 3 quiz), `cards` (4, texto PT de 20 a 60 palavras) — siga os modelos.
- Variedade de vocabulário: não repita o tema de aulas já feitas (g2001–g2052); varie verbos e substantivos.

## Entrega
Quando as suas aulas estiverem todas `ok` sem avisos, responda com UMA linha: `lote 20XX–20YY ok` (e, se algo ficou com ressalva, diga qual aula e por quê). Não faça mais nada.

## ADENDO (lote de 200 aulas extras, 2151–2350)
- As aulas 2151–2350 usam `A2(k, d)` com k = NN − 2000 (151…350); o plano está em `/tmp/a2/plan.py` (350 linhas). Modelos: g2051.py, g2036.py e qualquer g2053–g2150 já validada (veja a variedade de temas).
- **NÍVEL, com rigor máximo:** TODO texto em inglês da ficha (diálogo, abertura/fecho, exemplos de vocabulário, expressões, cartões, erros, quiz, tarefas) só pode usar a gramática PERMITIDA acima. Os avisos do mk.py cobrem só diálogo e expressões; o resto você precisa vigiar sozinho. Exemplos de coisas que NÃO podem aparecer em nenhum campo: could, would (exceto would like), may, might, must, used to, present perfect, orações relativas, passivo no passado, perguntas indiretas, discurso indireto, as…as, enough, Don't + verbo, if I were. Em cartões em português que citam exemplos em inglês, os exemplos também seguem a regra.
- O `mk.py` também imprime `REPEAT?` quando 3 ou mais das 6 palavras do vocabulário já foram ensinadas em aulas A2 anteriores: escolha outras palavras (temas e substantivos novos). Varie cenários, verbos e personagens.
- Se uma aula do plano pedir uma estrutura proibida, use a permitida mais próxima e registre na sua resposta final em uma frase.

## ADENDO 2 — referência cultural própria ("Cena da obra") e padrão de excelência
O usuário NÃO aceita "Cena da obra" repetida: cada aula precisa de uma referência cultural NOVA (nunca usada em outra aula do projeto), ligada ao tema da aula.
- Nas fichas das aulas 2351–2450, acrescente ao dicionário `d` a chave `obra=('Título da obra','ANO','Nota em português')`. O `mk.py` registra e valida (avisa `OBRA?` se faltar, se a obra já foi usada ou se a nota estiver fora de 150–420 caracteres). Para aulas já escritas, use o comando: `python3 /tmp/gen/obra.py NNNN "Título" ANO "Nota em português"`.
- Escolha obras REAIS e conhecidas que você conhece bem (filme, livro infantil ou clássico, música, série, pintura, obra de arquitetura, festival, tradição, evento esportivo, invenção, lugar famoso), em inglês ou do mundo, coerentes com o tema da aula. Varie os tipos e as épocas. **Só afirme o que você sabe com certeza**: resuma em termos gerais (do que trata), cite o ano só se tiver certeza (senão deixe `''`), não invente detalhes, números, falas nem prêmios.
- A nota (PT-BR, 150 a ~330 caracteres) diz o que é a obra e liga à situação da aula; pode incluir UMA frase curta em inglês tirada do próprio diálogo da aula (gramática A2). Não escreva "reproduz a obra": o registro acrescenta sozinho a frase final "A cena desta aula é original; não reproduz a obra.".
- Padrão de excelência: diálogos naturais e específicos (nada de falas genéricas repetidas entre aulas), conteúdo cultural em `cu` com informação correta e verificável (nada de estatísticas inventadas), vocabulário novo e útil, exemplos concretos.
