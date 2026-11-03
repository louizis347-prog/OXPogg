X = dict(
 key=dict(big="I'd like to enroll", label="Matricular-se em uma aula", sub="Diga que quer se matricular, peça o formulário, pergunte o horário e o preço, e veja se dá para pagar em partes."),
 mini=[
  dict(who="You", en="Hi! I'd like to enroll in an {English|art|music} class.", pt="Oi! Eu gostaria de me matricular em uma aula de {inglês|arte|música}."),
  dict(who="Kai", en="Sure. Do you have a {form?|photo ID?|phone number?}", pt="Claro. Você tem {um formulário?|um documento com foto?|um telefone?}"),
  dict(who="You", en="No. Can I {have one?|get one?|see one?}", pt="Não. Posso {pegar um?|conseguir um?|ver um?}"),
  dict(who="Kai", en="Here you go. {Fill it out,|Sign it,|Check it,} please.", pt="Aqui está. {Preencha,|Assine,|Confira,} por favor."),
 ],
 dlg=[
  dict(who="Kai", en="Hi! I'd like to {enroll|sign up} in an {English|art} class.", pt="Oi! Eu gostaria de me {matricular|inscrever} em uma aula de {inglês.|arte.}"),
  dict(who="You", en="Sure. Do you have a {form?|ID?}", pt="Claro. Você tem {um formulário?|um documento?}"),
  dict(who="Kai", en="No. Can I {have|get} one?", pt="Não. Posso {pegar|conseguir} um?"),
  dict(who="You", en="Here you go. {Fill it out,|Sign it,} please.", pt="Aqui está. {Preencha,|Assine,} por favor."),
  dict(who="Kai", en="What's the class {schedule?|level?}", pt="Qual é o {horário|nível} da aula?"),
  dict(who="You", en="{Monday|Tuesday} and {Wednesday,|Thursday,} from six to eight.", pt="{Segunda|Terça} e {quarta,|quinta,} das seis às oito."),
  dict(who="Kai", en="How {much|many} is the class?", pt="{Quanto custa|Quantos custam} a aula?"),
  dict(who="You", en="It's two {hundred|thousand} dollars.", pt="São {duzentos|dois mil} dólares."),
  dict(who="Kai", en="Can I pay in two {parts?|steps?}", pt="Posso pagar em duas {partes?|etapas?}"),
 ],
 vocab=[
  dict(w="enroll", pt="matricular-se", e="📝", ex=["I want to enroll today.", "She enrolls in a class."]),
  dict(w="tuition", pt="mensalidade, valor do curso", e="💵", ex=["The tuition is low.", "What is the tuition?"]),
  dict(w="semester", pt="semestre", e="🗓️", ex=["The semester starts in August.", "One semester is four months."]),
  dict(w="beginner", pt="iniciante", e="🌱", ex=["I am a beginner.", "This is a beginner class."]),
  dict(w="homework", pt="lição de casa", e="📚", ex=["I do my homework at night.", "Is there homework today?"]),
  dict(w="classroom", pt="sala de aula", e="🏫", ex=["The classroom is on the left.", "Our classroom is big."]),
 ],
 molds=[
  dict(title="Pedir a matrícula", frame="I'd like to enroll in {type} class.", slots=[dict(key="type", opts=["an English", "an art", "a music", "a computer"])], model="I'd like to enroll in an English class.", note="Enroll in = matricular-se em. Antes de vogal use an: an English class."),
  dict(title="Dizer o horário", frame="The class is on {days}, from {start} to {end}.", slots=[dict(key="days", opts=["Monday and Wednesday", "Tuesday and Thursday", "Saturday and Sunday"]), dict(key="start", opts=["six", "five", "seven"]), dict(key="end", opts=["eight", "nine", "ten"])], model="The class is on Monday and Wednesday, from six to eight.", note="From… to… indica o início e o fim. Os dias usam letra maiúscula."),
  dict(title="Escrever a pergunta", frame="Hi! How much is the {thing}? Can I pay in {n} parts?", slots=[dict(key="thing", opts=["class", "course", "semester"]), dict(key="n", opts=["two", "three", "four"])], model="Hi! How much is the class? Can I pay in two parts?", note="How much is…? pergunta o preço. Pay in two parts = pagar em duas partes."),
 ],
 sounds=[
  dict(say="Monday and Wednesday.", tag="ligação: Monday and", tip="Una Monday e and: 'Monday-n'. O d de Wednesday quase some: 'WENZ-day'."),
  dict(say="From six to eight.", tag="ritmo: FROM SIX to EIGHT", tip="Acentue SIX e EIGHT; 'from' e 'to' ficam fracos, quase 'frm' e 'tuh'."),
  dict(say="Fill it out.", tag="ligação: fill it out", tip="Soa 'fi-li-tout'. O l e o t se ligam às vogais seguintes."),
 ],
 role=dict(turns=[
  dict(npc="Hi! Can I help you?", opts=[
   dict(en="Yes. I'd like to enroll in an English class.", pt="Sim. Eu gostaria de me matricular em uma aula de inglês.", reply="Sure. Do you have a form?"),
   dict(en="Hi! How can I join a class?", pt="Oi! Como posso entrar em uma aula?", reply="You fill out a form. Here it is."),
   dict(en="Hello. I want to sign up for a class.", pt="Olá. Quero me inscrever em uma aula.", reply="Great. Fill out this form, please.")]),
  dict(npc="Here you go. Fill it out, please.", opts=[
   dict(en="Thanks. What's the class schedule?", pt="Obrigado. Qual é o horário da aula?", reply="Monday and Wednesday, from six to eight."),
   dict(en="Thank you. When does the class start?", pt="Obrigado. Quando a aula começa?", reply="It starts next Monday."),
   dict(en="OK. Is it a beginner class?", pt="Ok. É uma aula para iniciantes?", reply="Yes, it is.")]),
  dict(npc="Monday and Wednesday, from six to eight.", opts=[
   dict(en="Great. How much is the class?", pt="Ótimo. Quanto custa a aula?", reply="It's two hundred dollars."),
   dict(en="Hmm, I work on Monday. Is there another class?", pt="Hmm, eu trabalho na segunda. Tem outra turma?", reply="Yes. There is one on Tuesday and Thursday."),
   dict(en="Perfect. What's the price?", pt="Perfeito. Qual é o preço?", reply="It's two hundred dollars.")]),
  dict(npc="It's two hundred dollars.", opts=[
   dict(en="Can I pay in two parts?", pt="Posso pagar em duas partes?", reply="Yes, you can."),
   dict(en="Can I pay by card?", pt="Posso pagar no cartão?", reply="Yes, we take cards."),
   dict(en="OK. I'll pay today.", pt="Ok. Pago hoje.", reply="Great. Here is your receipt.")]),
 ], change=["O formulário está em outra língua: peça ajuda para preencher.", "A turma está cheia: pergunte se há lista de espera.", "O preço é alto demais: pergunte se há desconto."]),
 writing=dict(task="Escreva 2 ou 3 frases para a secretaria: diga que quer se matricular, pergunte o horário e o preço.", model="Hello! I'd like to enroll in an English class. What's the class schedule? How much is it?", kw=["enroll", "class", "schedule", "much"], checks=["Disse que quer se matricular.", "Perguntou o horário.", "Perguntou o preço."]),
 scenes=dict(pool=["school", "hall", "office", "lobby"], npc=dict(g="f", role="receptionist"), you=dict(g="m")),
 convo=dict(npc=dict(name="Kai"), story="Você está na secretaria de uma escola. A Kai trabalha lá e ajuda você a se matricular.", turns=[
  dict(npc="Hi! Can I help you?", pt="Oi! Posso ajudar?", opts=[
   dict(en="Hi! I'd like to enroll in an English class.", pt="Oi! Eu gostaria de me matricular em uma aula de inglês.", ok=True, fb="Diz o que você quer."),
   dict(en="Sure. Do you have a form?", pt="Claro. Você tem um formulário?", ok=False, fb="Quem pergunta isso é ela."),
   dict(en="It's two hundred dollars.", pt="São duzentos dólares.", ok=False, fb="Essa informação é dela.")]),
  dict(npc="Sure. Do you have a form?", pt="Claro. Você tem um formulário?", opts=[
   dict(en="Monday and Wednesday.", pt="Segunda e quarta.", ok=False, fb="Não responde à pergunta."),
   dict(en="Here you go. Fill it out, please.", pt="Aqui está. Preencha, por favor.", ok=False, fb="Quem entrega o formulário é ela."),
   dict(en="No. Can I have one?", pt="Não. Posso pegar um?", ok=True, fb="Responde e pede um.")]),
  dict(npc="Here you go. Fill it out, please.", pt="Aqui está. Preencha, por favor.", opts=[
   dict(en="Thanks. What's the class schedule?", pt="Obrigado. Qual é o horário da aula?", ok=True, fb="Pergunta o horário."),
   dict(en="Do you have a form?", pt="Você tem um formulário?", ok=False, fb="Ela acabou de dar o formulário."),
   dict(en="I'd like to enroll.", pt="Eu gostaria de me matricular.", ok=False, fb="Você já disse isso.")]),
  dict(npc="Monday and Wednesday, from six to eight.", pt="Segunda e quarta, das seis às oito.", opts=[
   dict(en="It's two hundred dollars.", pt="São duzentos dólares.", ok=False, fb="Quem informa o preço é ela."),
   dict(en="Monday and Wednesday, from six to eight.", pt="Segunda e quarta, das seis às oito.", ok=False, fb="Repete o que ela disse."),
   dict(en="How much is the class?", pt="Quanto custa a aula?", ok=True, fb="Próxima pergunta natural.")]),
  dict(npc="It's two hundred dollars.", pt="São duzentos dólares.", opts=[
   dict(en="Can I pay in two parts?", pt="Posso pagar em duas partes?", ok=True, fb="Pergunta sobre pagamento."),
   dict(en="What's the class schedule?", pt="Qual é o horário da aula?", ok=False, fb="Você já sabe o horário."),
   dict(en="Here you go.", pt="Aqui está.", ok=False, fb="Você ainda não entregou nada.")]),
 ]),
)
