X = dict(
 key=dict(big="How is she in class?", label="Perguntar à professora", sub="Cumprimente a professora, pergunte como seu filho vai na aula e se há algo de que ele precisa."),
 mini=[
  dict(who="Serena", en="Hi! Please {sit down|come in|take a seat}.", pt="Oi! Por favor, {sente-se|entre|sente-se}."),
  dict(who="You", en="Thank you. How is {Leo|Anna|my son} in class?", pt="Obrigado. Como {o Leo|a Anna|meu filho} vai na aula?"),
  dict(who="Serena", en="He is a {good|great|happy} student.", pt="Ele é um aluno {bom|ótimo|feliz}."),
  dict(who="You", en="Does he do his {homework|reading|work} every day?", pt="Ele faz {a lição de casa|a leitura|o trabalho} todo dia?"),
 ],
 dlg=[
  dict(who="Serena", en="Hello, I'm Anna's {mother|aunt}. Can we {talk?|meet?}", pt="Olá, sou {a mãe|a tia} da Anna. Podemos {conversar?|nos reunir?}"),
  dict(who="You", en="Of course. Please {sit down.|come in.}", pt="Claro. Por favor, {sente-se.|entre.}"),
  dict(who="Serena", en="How is Anna in {class?|school?}", pt="Como a Anna está {na aula?|na escola?}"),
  dict(who="You", en="She is a {good|great} student.", pt="Ela é uma {boa|ótima} aluna."),
  dict(who="Serena", en="Does she do her {homework?|reading?}", pt="Ela faz {a lição de casa?|a leitura?}"),
  dict(who="You", en="Yes, {every day.|every night.}", pt="Sim, {todo dia.|toda noite.}"),
  dict(who="Serena", en="Does she have {friends?|books?}", pt="Ela tem {amigos?|livros?}"),
  dict(who="You", en="Yes, she is very {friendly.|kind.}", pt="Sim, ela é muito {simpática.|gentil.}"),
  dict(who="Serena", en="Is there anything she {needs?|wants?}", pt="Ela {precisa|quer} de algo?"),
 ],
 vocab=[
  dict(w="grade", pt="nota", e="💯", ex=["She has a good grade.", "What is his grade?"]),
  dict(w="report card", pt="boletim", e="📄", ex=["Here is her report card.", "The report card is good."]),
  dict(w="principal", pt="diretor(a) da escola", e="🧑‍💼", ex=["The principal is nice.", "I want to meet the principal."]),
  dict(w="recess", pt="recreio", e="🛝", ex=["Kids play at recess.", "Recess is at ten."]),
  dict(w="classmate", pt="colega de classe", e="🧒", ex=["Anna is my classmate.", "Her classmate is friendly."]),
  dict(w="test", pt="prova", e="📝", ex=["The test is on Friday.", "She has a math test."]),
 ],
 molds=[
  dict(title="Perguntar da aula", frame="How is {name} in {place}?", slots=[dict(key="name", opts=["Leo", "Anna", "my son"]), dict(key="place", opts=["class", "school", "math"])], model="How is Leo in class?", note="How is...? pergunta como alguém está indo. Use in class, não on class."),
  dict(title="Perguntar da lição", frame="Does {who} do {thing} every day?", slots=[dict(key="who", opts=["he", "she", "Anna"]), dict(key="thing", opts=["homework", "reading", "the work"])], model="Does he do homework every day?", note="Depois de Does, o verbo fica na forma base: do."),
  dict(title="Escrever à professora", frame="Hello, Ms. Lane. {name} is a {adj} student. Is there anything {who} needs?", slots=[dict(key="name", opts=["Leo", "Anna", "My son"]), dict(key="adj", opts=["good", "happy", "new"]), dict(key="who", opts=["he", "she", "they"])], model="Hello, Ms. Lane. Leo is a good student. Is there anything he needs?", note="Is there anything... needs? pergunta se falta algo."),
 ],
 sounds=[
  dict(say="Does she do her homework?", tag="ritmo: DOES she DO her HOMEwork", tip="Acentue DOES, DO e HOME. 'she' e 'her' ficam fracos, quase 'shi' e 'er'."),
  dict(say="Please sit down.", tag="ligação: sit down", tip="Una a última consoante com a próxima palavra: 'sidown'."),
  dict(say="Is there anything she needs?", tag="redução: anything", tip="Diga 'ENNY-thing', com o acento no começo. O th é suave."),
 ],
 role=dict(turns=[
  dict(npc="Hello! Please sit down.", opts=[
   dict(en="Thank you. How is my son in class?", pt="Obrigado. Como meu filho vai na aula?", reply="He is doing very well."),
   dict(en="Thanks. How is Leo in school?", pt="Obrigado. Como o Leo vai na escola?", reply="He is doing very well."),
   dict(en="Thank you. Is Anna OK in class?", pt="Obrigado. A Anna está bem na aula?", reply="She is doing very well.")]),
  dict(npc="He is a good student.", opts=[
   dict(en="That's great. Does he do his homework?", pt="Que ótimo. Ele faz a lição de casa?", reply="Yes, every day."),
   dict(en="Good. Does he read at home?", pt="Bom. Ele lê em casa?", reply="Yes, a little every night."),
   dict(en="I'm happy. Does he do his work?", pt="Fico feliz. Ele faz o trabalho dele?", reply="Yes, every day.")]),
  dict(npc="Yes, every day.", opts=[
   dict(en="Does he have friends?", pt="Ele tem amigos?", reply="Yes, he is very friendly."),
   dict(en="Does he play at recess?", pt="Ele brinca no recreio?", reply="Yes, with three boys."),
   dict(en="Is he happy in class?", pt="Ele está feliz na aula?", reply="Yes, he smiles a lot.")]),
  dict(npc="He is very friendly.", opts=[
   dict(en="Is there anything he needs?", pt="Ele precisa de algo?", reply="Just a new notebook."),
   dict(en="Does he need help?", pt="Ele precisa de ajuda?", reply="No, he is fine."),
   dict(en="Can I see his report card?", pt="Posso ver o boletim dele?", reply="Of course. Here it is.")]),
 ], change=["A professora diz que o aluno precisa de ajuda na leitura: pergunte como ajudar em casa.", "A professora pergunta se você quer falar com o diretor: diga que sim, por favor.", "Você esqueceu o nome da professora: pergunte de novo, com educação."]),
 writing=dict(task="Você é pai ou mãe. Escreva 2 ou 3 frases para a professora: pergunte como seu filho vai na aula e se ele faz a lição de casa.", model="Hello, Ms. Lane. How is my son in class? Does he do his homework?", kw=["how", "class", "does", "homework"], checks=["Cumprimentou a professora.", "Perguntou como a criança vai na aula.", "Perguntou sobre a lição de casa."]),
 scenes=dict(pool=["school", "hall", "office", "library"], npc=dict(g="f", role="teacher"), you=dict(g="f")),
 convo=dict(npc=dict(name="Ms. Lane"), story="Você é pai ou mãe na escola do seu filho. Ms. Lane é a professora.", turns=[
  dict(npc="Hello! Please sit down.", pt="Olá! Sente-se, por favor.", opts=[
   dict(en="Thank you. How is my son in class?", pt="Obrigado. Como meu filho vai na aula?", ok=True, fb="Agradeça e pergunte da aula."),
   dict(en="Please sit down.", pt="Sente-se, por favor.", ok=False, fb="Quem convida é a professora."),
   dict(en="He is a good student.", pt="Ele é um bom aluno.", ok=False, fb="Essa é a resposta dela.")]),
  dict(npc="He is a good student.", pt="Ele é um bom aluno.", opts=[
   dict(en="Yes, every day.", pt="Sim, todo dia.", ok=False, fb="Ainda não perguntou nada."),
   dict(en="That's great. Does he do his homework?", pt="Que ótimo. Ele faz a lição de casa?", ok=True, fb="Reaja e pergunte."),
   dict(en="I am a good student.", pt="Eu sou um bom aluno.", ok=False, fb="Fala de você, não do filho.")]),
  dict(npc="Yes, every day.", pt="Sim, todo dia.", opts=[
   dict(en="He is very friendly.", pt="Ele é muito simpático.", ok=False, fb="Quem diz isso é ela."),
   dict(en="Does he have friends?", pt="Ele tem amigos?", ok=True, fb="Próxima pergunta natural."),
   dict(en="Please sit down.", pt="Sente-se, por favor.", ok=False, fb="Já estão sentados.")]),
  dict(npc="Yes, he is very friendly.", pt="Sim, ele é muito simpático.", opts=[
   dict(en="Is there anything he needs?", pt="Ele precisa de algo?", ok=True, fb="Fecha a conversa de forma útil."),
   dict(en="Yes, every day.", pt="Sim, todo dia.", ok=False, fb="Não responde nada."),
   dict(en="Hello, I'm his mother.", pt="Olá, sou a mãe dele.", ok=False, fb="Vocês já se apresentaram.")]),
  dict(npc="Just a new notebook. Thanks for coming!", pt="Só um caderno novo. Obrigada por vir!", opts=[
   dict(en="Hello! Nice to meet you.", pt="Olá! Prazer.", ok=False, fb="É hora de se despedir."),
   dict(en="I will buy one today. Thank you!", pt="Vou comprar um hoje. Obrigado!", ok=True, fb="Prometa e agradeça."),
   dict(en="He needs me.", pt="Ele precisa de mim.", ok=False, fb="Não combina com a fala.")]),
 ]),
)
