# Guia para escrever aulas B1 (ficha g30NN.py) — LEIA INTEIRO

## Tarefa
Escrever fichas `/tmp/gen/g30NN.py` (NN = número da aula: 3001…3070) do seu lote. Use SEMPRE `from mk import *` e `B1(k, d)` com **k = NN − 3000** (ex.: g3017 → `B1(17, d)`).
Modelos validados para copiar a ESTRUTURA exata (troque todo o conteúdo e use `B1(k,d)` no lugar de `A2(...)`): `/tmp/gen/g2051.py`, `/tmp/gen/g2300.py` (e qualquer g2051–g2500). Leia 1 modelo inteiro antes de começar.
Tema, cidade, personagem (npc), "you" e cenário vêm do plano `/tmp/b1/planb1.py` (lista P; índice k−1). NÃO mude título/cidade/personagens. A coluna "estrutura" é o foco gramatical: ela precisa aparecer MUITAS vezes no diálogo e nos exemplos.

## Como validar (OBRIGATÓRIO, uma aula por vez)
`cd /tmp/gen && ./chk.sh 30NN` → deve imprimir exatamente `30NN ok`. Se aparecer FAIL ou linhas `SWAP?`, `GLOSS?`, `VOCABEX?`, `MOLD?`, `CEFR?`, `GRAMMAR?`, `REPEAT?`, `OBRA?`, conserte e rode de novo (para ver os avisos: `cd /home/user/OXPogg/professor/src && python3 /tmp/gen/g30NN.py`).
NÃO rode run2.sh, build_v5.py, enrich_v6.py, finish.sh, git, nem edite mk.py/compact.py/dsl.py/common.py. Outros agentes trabalham em paralelo. Só crie/edite os SEUS arquivos g30NN.py.

## Regras de nível CEFR — B1 (o usuário é rígido: só entra o que de fato é B1; nada de B2 e nada de A1 infantil)
Referência: CEFR-J Vocabulary/Grammar Profile (docs/NIVEIS_CEFR.md). **Vocabulário** do diálogo: palavras A1, A2 ou B1 do CEFR-J; uma palavra B2+ só se a aula a ENSINAR (vocabulário `gl`, verbos `vb`, expressões `ex`). O `mk.py` imprime `CEFR?` com as palavras fora da regra: troque por palavras mais simples ou ensine-as. Máx. 2 palavras B2+ por aula. Nomes próprios são livres. O vocabulário ensinado (`gl`, 6 primeiras) deve ser de nível B1 (ou A2 tardio) e ÚTIL: substantivos, adjetivos, phrasal verbs comuns, colocações — não repita palavras já ensinadas em aulas B1 anteriores (`REPEAT?`) nem palavras básicas do A1.
**Gramática PERMITIDA no B1:** tudo do A2 (present simple/continuous, passado simples, past progressive, going to, will afirmativo, should, have to, comparativos/superlativos, 1º condicional, passivo presente, there is/are, quantificadores…) MAIS: present perfect (ever/never/already/yet/just/for/since/How long, been/gone), could (pedido e habilidade passada), must/mustn't, don't have to / had to / Do I have to, may/might (possibilidade), used to (afirmativo, negativo e pergunta), passivo no presente e no passado (was built, is made, by + agente), orações relativas definidas (who/that/which e relativa sem pronome), 2º condicional simples (If I had…, I would… / If I were you), will/won't (previsão, promessa), discurso indireto de afirmações (said/told me + that + passado), perguntas indiretas simples (Do you know where…? Could you tell me…? I wonder if…), gerúndio/infinitivo depois de verbos comuns, too/enough, as…as, pronomes reflexivos, conectores (while, as soon as, so that só se necessário… mas veja abaixo).
**PROIBIDO no B1 (é B2+; o `mk.py` acusa `GRAMMAR?` em diálogo e expressões):** past perfect (had + particípio), present perfect contínuo (have been -ing), wish, modais perfeitos (should have / could have / must have / might have), 3º condicional (would have), would rather, had better, be/get used to, unless, futuro contínuo/perfeito, perguntas reportadas (asked if…), inversões (not only, hardly), passivo contínuo/perfeito (is being fixed, has been made), whom/whose, so that, in order to. Na dúvida, escolha a frase mais simples.
**VOCÊ precisa vigiar** todos os campos da ficha (cartões, quiz, erros, tarefas, cultura, exemplos de vocabulário): o mk.py só confere diálogo e expressões. Nenhum campo pode conter estrutura B2 (lista acima).

## Qualidade (padrão de excelência — não é A2 com palavras maiores)
- Diálogo próprio de 11 falas, naturais e específicas do tema, com a estrutura da aula bem visível; falas de 6–16 palavras, com situação real (problema, decisão, opinião, história). Nada de falas genéricas reaproveitadas.
- `O` (abertura) e `C` (fecho): 6 pares EN/PT cada, mais elaborados que no A2 (já podem usar a estrutura da aula).
- PT-BR natural. `err`: 4 erros reais de brasileiros com a estrutura (ex.: “I have went”, “I am agree”, “He told me that…” sem backshift).
- Verbos `vb`: 5, cada um com passado diferente da base (evite read, put, cut, hit, set, cost); inclua phrasal verbs úteis quando fizer sentido; 8 campos separados por | (veja os modelos).
- `sw` (trocas): ≥ 6 entradas; chave = índice 0-based da fala; EN e PT são **substrings exatas** da fala do índice; um índice por entrada, índices diferentes.
- `gl`: 9 itens (6 com emoji+exemplos, 3 só palavra/PT); cada palavra de `gl` aparece no texto (diálogo, abertura ou fecho); o exemplo longo (5º campo) contém a palavra.
- Moldes `mo`: o modelo (4º campo) = frame preenchido com a PRIMEIRA opção de cada slot. `lab`: 3 pares com palavras diferentes (a≠b). `real`, `so`, `chg`, `wt`, `cu` (hook, 5 V/F, 2 wild, compare, 3 quiz), `cards` (4, 20–60 palavras em PT) — siga os modelos.
- `cu` e a cultura: informação correta e verificável; nada de estatística inventada.

## Referência cultural própria ("Cena da obra") — OBRIGATÓRIO e NOVA
Acrescente em `d` a chave `obra=('Título','ANO','Nota em português')`. Nunca repita obra usada em qualquer aula do projeto (o registro avisa `OBRA?`). Escolha obras REAIS e conhecidas (filme, livro, música, série, pintura, arquitetura, festival, tradição, evento esportivo, invenção, lugar) ligadas ao tema; varie tipos e épocas. **Só afirme o que sabe com certeza**: resuma em termos gerais, cite o ano só se tiver certeza (senão `''`), não invente detalhes, números, falas nem prêmios. Nota PT-BR de 150 a ~330 caracteres; pode incluir UMA frase curta em inglês do próprio diálogo (gramática B1). Não escreva "reproduz a obra": o registro acrescenta a frase final.

## Entrega
Quando todas as suas aulas estiverem `ok` sem avisos, responda com UMA linha: `lote 30XX–30YY ok` (e, se algo ficou com ressalva — por exemplo, estrutura do plano adaptada —, diga qual aula e por quê). Escreva e valide em lotes pequenos (3–4 fichas por comando) e não releia arquivos grandes sem necessidade.
