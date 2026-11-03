X = dict(
 key=dict(big="I have a question", label="Perguntar ao professor", sub="Levante a mão, diga “Excuse me”, pergunte o significado de uma palavra e peça para repetir com educação."),
 mini=[
  dict(who="You", en="Excuse me, {teacher|Ms. Lee|Mr. Brown}. I have a question.", pt="Com licença, {professora|Ms. Lee|Mr. Brown}. Tenho uma pergunta."),
  dict(who="Claire", en="Of course. What is it?", pt="Claro. Qual é?"),
  dict(who="You", en="What does \"{homework|lesson|clear}\" mean?", pt="O que quer dizer \"{homework|lesson|clear}\"?"),
  dict(who="Claire", en="It's a {work|task|page} you do at home. Can you repeat it, {please?|slowly?|again?}", pt="É um {trabalho|tarefa|página} que você faz em casa. Pode repetir, {por favor?|devagar?|de novo?}"),
 ],
 dlg=[
  dict(who="Claire", en="Excuse me, teacher. I have a {question.|doubt.}", pt="Com licença, professora. Tenho uma {pergunta.|dúvida.}"),
  dict(who="You", en="Of course. What is it?", pt="Claro. Qual é?"),
  dict(who="Claire", en="What does \"{homework|lesson}\" mean?", pt="O que quer dizer \"{homework|lesson}\"?"),
  dict(who="You", en="It's work you do at {home.|school.}", pt="É o trabalho que você faz em {casa.|escola.}"),
  dict(who="Claire", en="Ah, I see. Thank you.", pt="Ah, entendi. Obrigado."),
  dict(who="You", en="Do you have another {question?|doubt?}", pt="Você tem outra {pergunta?|dúvida?}"),
  dict(who="Claire", en="Yes. Can you {repeat,|say it again,} please?", pt="Tenho. Pode {repetir,|dizer de novo,} por favor?"),
  dict(who="You", en="Sure. {Slowly|Clearly} this time.", pt="Claro. {Devagar|Com clareza} desta vez."),
  dict(who="Claire", en="Now it's {clear.|better.}", pt="Agora está {claro.|melhor.}"),
 ],
 vocab=[
  dict(w="lesson", pt="aula, lição", e="📖", ex=["The lesson starts at nine.", "This lesson is easy."]),
  dict(w="meaning", pt="significado", e="💭", ex=["What is the meaning of this word?", "The meaning is easy."]),
  dict(w="repeat", pt="repetir", e="🔁", ex=["Please repeat the word.", "I repeat the sentence."]),
  dict(w="slowly", pt="devagar", e="🐢", ex=["Please speak slowly.", "She writes slowly."]),
  dict(w="sentence", pt="frase", e="💬", ex=["Read the sentence, please.", "This sentence is short."]),
  dict(w="clear", pt="claro", e="💡", ex=["Is it clear now?", "The answer is clear."]),
 ],
 molds=[
  dict(title="Pedir o significado", frame="What does \"{word}\" mean?", slots=[dict(key="word", opts=["lesson", "clear", "slowly", "repeat"])], model="What does \"lesson\" mean?", note="What does ... mean? pergunta o significado. Não diga 'What means'."),
  dict(title="Pedir para repetir", frame="Can you {verb} that, please?", slots=[dict(key="verb", opts=["repeat", "say", "write", "spell"])], model="Can you repeat that, please?", note="Can you...? é a forma educada de pedir. That = o que acabou de ser dito."),
  dict(title="Escrever ao professor", frame="Excuse me, {title}. I have a question about the {thing}.", slots=[dict(key="title", opts=["teacher", "Ms. Lee", "Mr. Brown"]), dict(key="thing", opts=["lesson", "homework", "word"])], model="Excuse me, teacher. I have a question about the lesson.", note="About = sobre. Serve para dizer o assunto da pergunta."),
 ],
 sounds=[
  dict(say="Can you repeat, please?", tag="ligação: repeat, please", tip="O t de repeat quase some antes do p: 'ripi-t pliz'. Una sem parar."),
  dict(say="What does it mean?", tag="redução: does it", tip="Does it soa 'dazit'. A pergunta sobe e desce no fim: mean."),
  dict(say="Slowly this time.", tag="ritmo: SLOW-ly THIS TIME", tip="Acentue SLOW, THIS e TIME. O -ly final é curto e fraco."),
 ],
 role=dict(turns=[
  dict(npc="Okay, class. Any questions?", opts=[
   dict(en="Excuse me. I have a question.", pt="Com licença. Tenho uma pergunta.", reply="Of course. What is it?"),
   dict(en="Yes, teacher. I have a question.", pt="Tenho, professora. Uma pergunta.", reply="Of course. What is it?"),
   dict(en="Teacher, can I ask something?", pt="Professora, posso perguntar algo?", reply="Of course. What is it?")]),
  dict(npc="Of course. What is it?", opts=[
   dict(en="What does \"homework\" mean?", pt="O que quer dizer \"homework\"?", reply="It's work you do at home."),
   dict(en="What does \"lesson\" mean?", pt="O que quer dizer \"lesson\"?", reply="It's a class or a part of a book."),
   dict(en="What does \"clear\" mean?", pt="O que quer dizer \"clear\"?", reply="It means easy to understand.")]),
  dict(npc="It's easy to understand. Okay?", opts=[
   dict(en="Can you repeat, please?", pt="Pode repetir, por favor?", reply="Sure. Slowly this time."),
   dict(en="Sorry, can you say it slowly?", pt="Desculpe, pode dizer devagar?", reply="Sure. Slowly this time."),
   dict(en="Can you say it again?", pt="Pode dizer de novo?", reply="Sure. Slowly this time.")]),
  dict(npc="Now it is clear?", opts=[
   dict(en="Yes, now it's clear. Thank you.", pt="Sim, agora está claro. Obrigado.", reply="Great. It gets easier."),
   dict(en="Ah, I see. Thank you, teacher.", pt="Ah, entendi. Obrigado, professora.", reply="Great. It gets easier."),
   dict(en="Yes! Thanks a lot.", pt="Sim! Muito obrigado.", reply="Great. It gets easier.")]),
 ], change=["A professora fala muito rápido: peça para falar mais devagar.", "Você não ouviu a palavra: peça para ela escrever no quadro.", "Você tem outra pergunta: pergunte sobre o dever de casa."]),
 writing=dict(task="Escreva um bilhete curto para sua professora: diga que tem uma pergunta, pergunte o significado de uma palavra e peça para repetir.", model="Excuse me, teacher. I have a question. What does \"lesson\" mean? Can you repeat, please?", kw=["question", "mean", "repeat", "please"], checks=["Disse que tem uma pergunta.", "Perguntou o significado de uma palavra.", "Pediu para repetir com educação."]),
 scenes=dict(pool=["school", "library", "hall", "musicroom"], npc=dict(g="f", role="teacher"), you=dict(g="m")),
 convo=dict(npc=dict(name="Ms. Lee"), story="Você é aluno em uma aula de inglês. A professora Ms. Lee explica a lição.", turns=[
  dict(npc="Okay, class. Any questions?", pt="Certo, turma. Alguma pergunta?", opts=[
   dict(en="Excuse me, teacher. I have a question.", pt="Com licença, professora. Tenho uma pergunta.", ok=True, fb="Boa forma de pedir a vez."),
   dict(en="Of course. What is it?", pt="Claro. Qual é?", ok=False, fb="Quem diz isso é a professora."),
   dict(en="Now it's clear.", pt="Agora está claro.", ok=False, fb="Você ainda não perguntou nada.")]),
  dict(npc="Of course. What is it?", pt="Claro. Qual é?", opts=[
   dict(en="It's work you do at home.", pt="É o trabalho que você faz em casa.", ok=False, fb="Isso é uma explicação, e quem pergunta é você."),
   dict(en="Thank you, teacher.", pt="Obrigado, professora.", ok=False, fb="Ainda falta fazer a pergunta."),
   dict(en="What does \"homework\" mean?", pt="O que quer dizer \"homework\"?", ok=True, fb="Pergunta o significado da palavra.")]),
  dict(npc="It's work you do at home.", pt="É o trabalho que você faz em casa.", opts=[
   dict(en="Ah, I see. Thank you.", pt="Ah, entendi. Obrigado.", ok=True, fb="Mostra que você entendeu."),
   dict(en="What does \"homework\" mean?", pt="O que quer dizer \"homework\"?", ok=False, fb="Ela acabou de explicar."),
   dict(en="Do you have another question?", pt="Você tem outra pergunta?", ok=False, fb="Quem pergunta isso é a professora.")]),
  dict(npc="Do you have another question?", pt="Você tem outra pergunta?", opts=[
   dict(en="No, I don't have a teacher.", pt="Não, eu não tenho professora.", ok=False, fb="Não faz sentido: ela é sua professora."),
   dict(en="Yes. Can you repeat, please?", pt="Tenho. Pode repetir, por favor?", ok=True, fb="Pede para ouvir de novo, com educação."),
   dict(en="Sure. Slowly this time.", pt="Claro. Devagar desta vez.", ok=False, fb="Essa é a fala da professora.")]),
  dict(npc="Sure. Slowly this time. It's work you do at home.", pt="Claro. Devagar desta vez. É o trabalho que você faz em casa.", opts=[
   dict(en="Can you repeat, please?", pt="Pode repetir, por favor?", ok=False, fb="Ela acabou de repetir."),
   dict(en="Excuse me, teacher.", pt="Com licença, professora.", ok=False, fb="Você já tem a atenção dela."),
   dict(en="Now it's clear. Thank you!", pt="Agora está claro. Obrigado!", ok=True, fb="Fecha a conversa de forma natural.")]),
 ]),
)
