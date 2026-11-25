# Guia — lições A1 181–300 do PoggloDict (inglês americano para brasileiros)

## O que você vai fazer
Escrever, para cada lição do seu lote, UM arquivo JSON em `poglodict/fontes/a1-181-350/NNN.json` (NNN = número da lição, 181…300), no MESMO padrão e na MESMA densidade das 50 primeiras lições do curso. Exemplos reais já convertidos para o formato: `/tmp/pd/exemplos/001.json`, `011.json`, `031.json`, `049.json` (leia os quatro antes de começar; o 049 mostra `story`). As 50 lições originais estão em `/home/user/OXPogg/poglodict/english-a1-plan.js` (título | foto | gramática | escopo | vocabulário) e `english-a1-content.js` (leitura, diálogo, pronúncia, exercício). Leia pelo menos 15 delas para absorver o tom.
Tema e objetivo gramatical de cada lição estão em `poglodict/fontes/a1-181-350/plano-gramatical.txt` (`NNN|tema do bloco|objetivo gramatical`): você escolhe o título concreto (PT-BR, uma cena específica), mas o objetivo gramatical é o da linha (pode refinar o texto, nunca trocar o tópico). Não existem imagens a produzir: só escolha arquivos de foto já existentes.

## Formato do JSON
```json
{"n":181,"title":"Acordando às seis","photo":"clock-1","art":"chat",
 "photos":["photo-clock-1.webp","photo-bag-1.webp"],
 "grammar":"Presente simples com I, you, we e they para rotinas",
 "goal":"Use a forma base do verbo depois de I, you, we e they para descrever o que você faz todo dia.",
 "words":[["wake up","acordar"],["alarm","despertador"],["get up","levantar-se"],["breakfast","café da manhã"]],
 "reading":[["Lia wakes up at six.","Lia acorda às seis."], ... 5 pares ...],
 "dialogue":[["What time do you wake up?","A que horas você acorda?"], ... 8 pares, pergunta/resposta alternadas ...],
 "pron":["Título do som, em PT","Dica de articulação em PT",["palavra","frase curta com a palavra"]],
 "gram":["I ___ at six.","wake up","wakes up","Eu acordo às seis.","Motivo curto em PT"],
 "pattern":"\\bwake(?:s)? up\\b",
 "extra":{"alarm":["The alarm rings at six.","O despertador toca às seis."]},   (opcional)
 "extra_names":["Mina"],                                                       (opcional: nomes próprios que você usou além de Lia, Ravi, Ben, Ava, Noah, Nico, Peg, June, Tina, Lou)
 "story":["Título PT",[["Frase 1.","Tradução 1."], ... 10 pares ...]]          (SÓ nas lições múltiplas de 10: 190, 200 … 300)
}
```
- `photo`: chave de foto EXISTENTE (sem `photo-` e sem `.webp`), a mais próxima do tema; `photos`: dois arquivos existentes (com `photo-…webp` ou `lesson-…webp`) que combinem com a cena (lista: `ls /home/user/OXPogg/poglodict/*.webp`). Como não há fotos novas, repita as mais próximas. `art`: um de cup, ticket, notebook, city, park, chat, map, health (o tema visual mais próximo).
- `words`: 4 ou 5 pares [termo EN, sentido em PT]. Os DOIS PRIMEIROS são o foco da lição: devem aparecer LITERALMENTE em frases da leitura/diálogo (o 2º pode vir de `extra`). Os termos devem vir do vocabulário do DICIONÁRIO (`/tmp/pd/dict_words.txt`, um verbete por linha — o validador confere palavra simples; frases como “wake up” valem se as palavras existirem). Escolha palavras úteis, concretas e de nível A1/A2 (o curso é baseado no vocabulário do dicionário do próprio PoggloDict). Nenhum termo-foco pode se repetir entre lições (o validador cruza todas) nem repetir os das 50 primeiras (veja `english-a1-plan.js`). Pode ensinar 1 termo composto (“check my email”).
- `reading`: 5 frases curtas (média 6–8 palavras, máx. 12), uma mini-cena com os personagens do curso (Lia, Ravi, Ben, Ava, Noah, Nico, Peg, June, Tina, Lou — pode misturar; evite repetir a mesma dupla em lições seguidas), com começo-meio-fim.
- `dialogue`: 8 falas que alternam pergunta e resposta (falante A pergunta, B responde), média 5–7 palavras (máx. 12). As falas 7 e 8 formam o “final da conversa” (pergunta + resposta que confirma informação); a fala 2 serve de resposta-modelo.
- `pron`: título curto do som/ritmo (“/θ/ em three e thanks”, “Acento em …”), dica clara em PT de como articular, e `[palavra, frase curta]` em inglês (a palavra deve aparecer nas frases do curso ou pelo menos ser A1).
- `gram`: exercício de escolha: prompt com `___`, resposta correta, resposta errada plausível (erro típico de brasileiro), tradução PT do prompt completo, motivo em PT (1 frase). A frase prompt com a correta deve ser inglês correto e mostrar o ponto gramatical da lição.
- `pattern`: expressão regular (sintaxe comum a JavaScript e Python, escape duplo de barras no JSON) que casa o ponto gramatical; o validador exige que ela case PELO MENOS 2 frases da leitura/diálogo. O app usa as 2 primeiras frases que casam como exemplos da regra gramatical, então elas precisam ilustrar bem a gramática.
- `story` (lições 190, 200, …, 300): mini-história de 10 frases (6–9 palavras cada, com começo, problema e fim) que revisa o bloco de 10 lições (vocabulário e gramática dos últimos dez dias), com personagem recorrente; título em PT.

## Regras de língua (rígidas — o usuário é exigente)
- **Nível A1 real** (o app usa CEFR-J): vocabulário A1; no máximo ~4 palavras A2 e 1–2 do vocabulário ensinado. Nada de B1. Frases simples e naturais (inglês americano; não “textbook-ese” artificial: fale como pessoas falam, com situações concretas, pequenas surpresas e detalhes — um preço, uma hora, um nome, um lugar).
- **Contrações**: no A1 só são permitidas as de be: I’m, you’re, he’s, she’s, it’s, we’re, they’re, there’s, what’s, where’s, who’s etc. PROIBIDO: don’t, doesn’t, isn’t, aren’t, can’t, won’t, I’ll, I’ve, I’d, let’s (use do not, does not, is not, are not, cannot, will not, I will, I have, I would, let us…). Use sempre o apóstrofo curvo ’.
- Tempos permitidos: o que o curso já viu + o ponto da lição. Lições 261–270 introduzem o passado simples; antes disso, nada de passado (exceto was/were em 261+). Lições 271–280 introduzem be going to; antes, sem futuro. Não use present perfect, condicionais, modais além de can/cannot/should/would like/have to/must, nem voz passiva.
- Cada lição ensina UM ponto gramatical (o da linha do skeleton) e o repete em várias frases do texto (pelo menos 3–4 das 13 frases o mostram). O resto da conversa usa gramática simples já vista (be, present simple, can, there is/are, this/that, want to…).
- PT-BR natural e fiel nas traduções (nada de tradução literal esquisita); a tradução do prompt e do motivo em PT são frases completas.
- Variedade REAL entre lições: lugares, objetos, horários, nomes, tipos de frase. NÃO reutilize frases entre lições nem estruturas de diálogo idênticas (o validador acusa frase idêntica em outra lição). Não repita o mesmo cenário duas vezes no bloco.
- Fatos: nada de informação duvidosa; preços e horários são fictícios e simples.
- Se o validador apontar palavra fora da lista: troque por palavra A1 equivalente ou, se for a palavra natural do tema, ENSINE-A em `words`.

## Validar
`python3 poglodict/fontes/validar.py 181 182 …` (só as suas). Deve imprimir `NNN ok` para cada. Ajuste até passar. No fim, rode de novo todas as suas. Os outros agentes escrevem em paralelo nos arquivos deles; não toque em arquivos de outros números, no validador ou em qualquer outro lugar. NÃO rode git, não edite o repositório: só crie `poglodict/fontes/a1-181-350/NNN.json`.
Se o validador acusar "vocabulário já usado em outra lição", troque o termo-foco da SUA lição.

## Entrega
Responda com UMA linha: `lote XXX–YYY ok` e, se alguma lição ficou com ressalva (palavra trocada, gramática adaptada), diga qual e por quê.
