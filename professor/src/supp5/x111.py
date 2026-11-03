X = dict(
 key=dict(big="Can I speak to…?", label="Pedir uma pessoa ao telefone", sub="No trabalho, diga bom dia, peça para falar com a pessoa, espere e, se ela não estiver, deixe um recado com seu número."),
 mini=[
  dict(who="Omar", en="Good morning, {Austin Print|Lee Office|Star Shop}. Tessa speaking.", pt="Bom dia, {Austin Print|Escritório Lee|Loja Star}. Tessa falando."),
  dict(who="You", en="Hello. Can I speak to {Mr. Lee|Ms. Rose|Dr. Hill}, please?", pt="Olá. Posso falar com {o Sr. Lee|a Sra. Rose|o Dr. Hill}, por favor?"),
  dict(who="Omar", en="I'm sorry, he's not here. Can I {take a message?|help you?|call you back?}", pt="Sinto muito, ele não está. Posso {anotar um recado?|ajudar?|retornar sua ligação?}"),
  dict(who="You", en="Yes. Please tell him {Sam|Ana|Tom} called.", pt="Sim. Diga que {o Sam|a Ana|o Tom} ligou."),
 ],
 dlg=[
  dict(who="Omar", en="Good morning, {Austin Print.|Star Shop.} Tessa speaking.", pt="Bom dia, {Austin Print.|Loja Star.} Tessa falando."),
  dict(who="You", en="Hello. Can I {speak|talk} to Mr. Lee, please?", pt="Olá. Posso {falar|conversar} com o Sr. Lee, por favor?"),
  dict(who="Omar", en="One {moment.|minute.} I'll {transfer|connect} you.", pt="Um {momento.|minuto.} Vou {transferir|conectar} você."),
  dict(who="You", en="{Thank you.|Thanks.}", pt="{Obrigado.|Valeu.}"),
  dict(who="Omar", en="I'm sorry, he's not {here.|in.}", pt="Sinto muito, ele não {está.|está.}"),
  dict(who="You", en="Can I take a {message?|note?}", pt="Posso anotar um {recado?|bilhete?}"),
  dict(who="Omar", en="Yes. Please {tell|say to} him Alex called.", pt="Sim. {Diga|Fale} que o Alex ligou."),
  dict(who="You", en="What's your phone {number?|line?}", pt="Qual é seu {telefone?|número?}"),
  dict(who="Omar", en="It's five five five, zero one nine {nine.|nine.}", pt="É cinco cinco cinco, zero um nove {nove.|nove.}"),
 ],
 vocab=[
  dict(w="extension", pt="ramal", e="☎️", ex=["What is your extension?", "Dial extension twelve."]),
  dict(w="voicemail", pt="caixa postal", e="📼", ex=["Leave a voicemail.", "I have one voicemail."]),
  dict(w="receptionist", pt="recepcionista", e="🧑‍💼", ex=["The receptionist is nice.", "Ask the receptionist."]),
  dict(w="busy", pt="ocupado", e="🔴", ex=["The line is busy.", "He is busy now."]),
  dict(w="hang up", pt="desligar", e="📴", ex=["Please do not hang up.", "I hang up at five."]),
  dict(w="caller", pt="quem liga", e="📲", ex=["The caller is Sam.", "Who is the caller?"]),
 ],
 molds=[
  dict(title="Pedir uma pessoa", frame="Hello. Can I speak to {person}, please?", slots=[dict(key="person", opts=["Mr. Lee", "Ms. Rose", "Dr. Hill", "the manager"])], model="Hello. Can I speak to Mr. Lee, please?", note="Can I speak to…? é o jeito educado de pedir alguém. Use Mr., Ms. ou Dr. com o sobrenome."),
  dict(title="Deixar um recado", frame="Please tell {who} {name} called.", slots=[dict(key="who", opts=["him", "her", "them"]), dict(key="name", opts=["Sam", "Ana", "Tom"])], model="Please tell him Sam called.", note="Tell him/her + nome + called. O passado called mostra que a ligação já aconteceu."),
  dict(title="Escrever um recado", frame="Hi {name}, {person} called at {time}. Please call back.", slots=[dict(key="name", opts=["Tessa", "Omar", "Rosa"]), dict(key="person", opts=["Sam", "Ana", "Mr. Lee"]), dict(key="time", opts=["nine", "ten", "two"])], model="Hi Tessa, Sam called at nine. Please call back.", note="Recado curto: quem ligou, a hora e o pedido. Please call back = ligue de volta."),
 ],
 sounds=[
  dict(say="Can I speak to Mr. Lee?", tag="ligação: Can I", tip="Una Can e I: 'kenai'. Acentue SPEAK e LEE; Can fica fraco."),
  dict(say="One moment, please.", tag="acento: MO-ment", tip="Acentue a primeira sílaba de moment: MO-ment. O 'o' soa como 'ou'."),
  dict(say="I'll transfer you.", tag="ligação: transfer you", tip="Transfer you soa 'transfer-chu'. T e Y se juntam num som de 'tch'."),
 ],
 role=dict(turns=[
  dict(npc="Good morning, Austin Print. Tessa speaking.", opts=[
   dict(en="Hello. Can I speak to Mr. Lee, please?", pt="Olá. Posso falar com o Sr. Lee, por favor?", reply="One moment. I'll transfer you."),
   dict(en="Good morning. Is Mr. Lee there, please?", pt="Bom dia. O Sr. Lee está, por favor?", reply="One moment. I'll check."),
   dict(en="Hi. May I speak to Mr. Lee?", pt="Oi. Posso falar com o Sr. Lee?", reply="Sure. One moment.")]),
  dict(npc="One moment. I'll transfer you.", opts=[
   dict(en="Thank you.", pt="Obrigado.", reply="You're welcome."),
   dict(en="Thanks a lot.", pt="Muito obrigado.", reply="No problem."),
   dict(en="OK, I'll wait.", pt="Ok, eu espero.", reply="Thank you.")]),
  dict(npc="I'm sorry, he's not here.", opts=[
   dict(en="Can I leave a message?", pt="Posso deixar um recado?", reply="Yes, of course."),
   dict(en="When will he be back?", pt="Quando ele volta?", reply="Maybe at two o'clock."),
   dict(en="OK. I'll call again later.", pt="Ok. Ligo de novo mais tarde.", reply="Okay. Thank you for calling.")]),
  dict(npc="Please tell me your name and phone number.", opts=[
   dict(en="It's Sam. Five five five, zero one nine nine.", pt="É o Sam. Cinco cinco cinco, zero um nove nove.", reply="Got it. I'll tell him."),
   dict(en="My name is Ana. My number is five five five, zero one nine nine.", pt="Meu nome é Ana. Meu número é cinco cinco cinco, zero um nove nove.", reply="Thanks, Ana. I'll tell him."),
   dict(en="This is Tom. It's five five five, zero one nine nine.", pt="Aqui é o Tom. É cinco cinco cinco, zero um nove nove.", reply="Thanks, Tom. Goodbye.")]),
 ], change=["A linha está ocupada: diga que vai esperar ou ligar mais tarde.", "A recepcionista não entende o número: repita devagar, um a um.", "Você ligou para o lugar errado: peça desculpas e desligue com educação."]),
 writing=dict(task="Escreva um recado de 2 ou 3 frases para um colega: diga quem ligou, a hora e peça para ligar de volta.", model="Hi Omar, Sam called at ten. Please call back. His number is five five five, zero one nine nine.", kw=["called", "please", "call", "number"], checks=["Disse quem ligou.", "Disse a hora ou o número.", "Pediu para ligar de volta."]),
 scenes=dict(pool=["lobby", "counter", "office", "meetingroom"], npc=dict(g="f", role="receptionist"), you=dict(g="m")),
 convo=dict(npc=dict(name="Tessa"), story="Você liga para a empresa Austin Print e quer falar com o Sr. Lee. A Tessa atende.", turns=[
  dict(npc="Good morning, Austin Print. Tessa speaking.", pt="Bom dia, Austin Print. Tessa falando.", opts=[
   dict(en="Hello. Can I speak to Mr. Lee, please?", pt="Olá. Posso falar com o Sr. Lee, por favor?", ok=True, fb="Primeiro passo: pedir a pessoa."),
   dict(en="Good morning. Can I take a message?", pt="Bom dia. Posso anotar um recado?", ok=False, fb="Quem anota o recado é ela, e ainda é cedo."),
   dict(en="I'm sorry, he's not here.", pt="Sinto muito, ele não está.", ok=False, fb="Essa fala é de quem atende.")]),
  dict(npc="One moment. I'll transfer you.", pt="Um momento. Vou transferir.", opts=[
   dict(en="It's five five five, zero one nine nine.", pt="É cinco cinco cinco, zero um nove nove.", ok=False, fb="Ninguém pediu o número ainda."),
   dict(en="Good morning, Austin Print.", pt="Bom dia, Austin Print.", ok=False, fb="Quem atende diz isso, não você."),
   dict(en="Thank you.", pt="Obrigado.", ok=True, fb="Agradecer é natural.")]),
  dict(npc="I'm sorry, he's not here. Can I take a message?", pt="Sinto muito, ele não está. Posso anotar um recado?", opts=[
   dict(en="Yes, please. Tell him Sam called.", pt="Sim, por favor. Diga que o Sam ligou.", ok=True, fb="Aceita e diz o recado."),
   dict(en="Yes, you can speak to Mr. Lee.", pt="Sim, você pode falar com o Sr. Lee.", ok=False, fb="Ela disse que ele não está."),
   dict(en="One moment, please.", pt="Um momento, por favor.", ok=False, fb="Quem pede um momento é quem atende.")]),
  dict(npc="What's your phone number?", pt="Qual é o seu telefone?", opts=[
   dict(en="It's five five five, zero one nine nine.", pt="É cinco cinco cinco, zero um nove nove.", ok=True, fb="Responde com o número, um a um."),
   dict(en="Can I take a message?", pt="Posso anotar um recado?", ok=False, fb="Você é quem deixa o recado."),
   dict(en="He's not here.", pt="Ele não está.", ok=False, fb="Essa informação já foi dada.")]),
  dict(npc="Thanks, I'll tell him.", pt="Obrigada, vou avisar.", opts=[
   dict(en="Good morning, Austin Print.", pt="Bom dia, Austin Print.", ok=False, fb="Já houve a saudação."),
   dict(en="Thank you. Have a good day!", pt="Obrigado. Tenha um bom dia!", ok=True, fb="Despedida educada."),
   dict(en="What's your number?", pt="Qual é o seu número?", ok=False, fb="Você já deu o seu; não precisa do dela.")]),
 ]),
)
