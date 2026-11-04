X = dict(
 key=dict(big="Two for mini golf", label="Pedir os ingressos", sub="Fale primeiro o número de pessoas e depois a atividade. O preço costuma ser 'each' (por pessoa)."),
 mini=[
  dict(who="You", en="Hi! {Two|Three|Four} for mini golf, please.", pt="Oi! {Dois|Três|Quatro} para mini golfe, por favor."),
  dict(who="Claire", en="That's ten dollars {each.|a person.}", pt="São dez dólares {cada.|por pessoa.}"),
  dict(who="You", en="Here's {twenty.|forty.|thirty.} Keep the change.", pt="Aqui estão {vinte.|quarenta.|trinta.} Fique com o troco."),
  dict(who="Claire", en="Thanks. {Here are|Here come} your clubs and balls. Have {fun!|a good game!}", pt="Obrigada. {Aqui estão|Aí vêm} seus tacos e bolas. {Divirta-se!|Bom jogo!}"),
 ],
 dlg=[
  dict(who="Claire", en="Hi! {Two|Four} for mini golf, please.", pt="Oi! {Dois|Quatro} para mini golfe, por favor."),
  dict(who="You", en="That's {ten|twelve} dollars each.", pt="São {dez|doze} dólares cada."),
  dict(who="Claire", en="Here's {twenty.|forty.} Keep the change.", pt="Aqui estão {vinte.|quarenta.} Fique com o troco."),
  dict(who="You", en="Thanks. Here are your {clubs|sticks} and balls.", pt="Obrigado. Aqui estão {tacos|tacos} e bolas."),
  dict(who="Claire", en="Which {color|ball} do you want?", pt="Qual {cor|bola} você quer?"),
  dict(who="You", en="I'll take {red.|blue.} You take {yellow.|green.}", pt="Eu fico com {vermelha.|azul.} Você fica com {a amarela.|a verde.}"),
  dict(who="Claire", en="How does it {work?|go?}", pt="Como {funciona?|funciona?}"),
  dict(who="You", en="Hit the ball into the {hole.|cup.}", pt="Acerte a bola no {buraco.|buraco.}"),
  dict(who="Claire", en="How many {tries?|shots?}", pt="Quantas {tentativas?|tacadas?}"),
 ],
 vocab=[
  dict(w="hole", pt="buraco", e="🕳️", ex=["The ball is in the hole.", "Hole one is easy."]),
  dict(w="golf", pt="golfe", e="⛳", ex=["I like mini golf.", "Golf is a slow game."]),
  dict(w="club", pt="taco", e="🏌️", ex=["I have a red club.", "Take your club, please."]),
  dict(w="prize", pt="prêmio", e="🎁", ex=["The prize is ice cream.", "She wins a prize."]),
  dict(w="tunnel", pt="túnel", e="🚇", ex=["The ball goes in the tunnel.", "The tunnel is dark."]),
  dict(w="course", pt="campo, percurso", e="🌿", ex=["The course is green.", "This course is small."]),
 ],
 molds=[
  dict(title="Pedir ingressos", frame="Hi! {number} for {activity}, please.", slots=[dict(key="number", opts=["Two", "Three", "Four"]), dict(key="activity", opts=["mini golf", "the movie", "the museum"])], model="Hi! Two for mini golf, please.", note="Número + for + atividade + please. Funciona em quase qualquer bilheteria."),
  dict(title="Escolher a cor", frame="I'll take {mine}. You take {yours}.", slots=[dict(key="mine", opts=["red", "blue", "green"]), dict(key="yours", opts=["yellow", "white", "orange"])], model="I'll take red. You take yellow.", note="I'll take + cor é um jeito natural de escolher. Cores não levam artigo antes."),
  dict(title="Escrever uma regra do jogo", frame="{verb} the ball into the {place}. You have {number} tries.", slots=[dict(key="verb", opts=["Hit", "Push", "Roll"]), dict(key="place", opts=["hole", "box", "cup"]), dict(key="number", opts=["six", "five", "three"])], model="Hit the ball into the hole. You have six tries.", note="Use o verbo no começo para dar uma instrução. Tries = tentativas."),
 ],
 sounds=[
  dict(say="Keep the change.", tag="ritmo: KEEP the CHANGE", tip="Acentue KEEP e CHANGE. The fica fraco, quase 'dhe'."),
  dict(say="Here are your clubs and balls.", tag="ligação: clubs and", tip="Una clubs + and: 'clubzand'. O s liga com a vogal seguinte."),
  dict(say="How does it work?", tag="redução: does it", tip="Does it soa 'dazit'. Una as duas palavras e acentue WORK."),
 ],
 role=dict(turns=[
  dict(npc="Hi! How can I help you?", opts=[
   dict(en="Hi! Two for mini golf, please.", pt="Oi! Dois para mini golfe, por favor.", reply="That's ten dollars each."),
   dict(en="Hi! Three for mini golf, please.", pt="Oi! Três para mini golfe, por favor.", reply="That's thirty dollars. Ten each."),
   dict(en="Hello! Two tickets, please.", pt="Olá! Dois ingressos, por favor.", reply="That's ten dollars each.")]),
  dict(npc="That's ten dollars each.", opts=[
   dict(en="Here's twenty. Keep the change.", pt="Aqui estão vinte. Fique com o troco.", reply="Thanks! Here are your clubs and balls."),
   dict(en="Here's twenty. Do you take cards?", pt="Aqui estão vinte. Vocês aceitam cartão?", reply="Cash is fine. Thanks! Here are your clubs and balls."),
   dict(en="Here you go.", pt="Aqui está.", reply="Thanks! Here are your clubs and balls.")]),
  dict(npc="Which color do you want?", opts=[
   dict(en="I'll take red.", pt="Eu fico com a vermelha.", reply="Great. And your friend?"),
   dict(en="Blue, please.", pt="Azul, por favor.", reply="Great. And your friend?"),
   dict(en="Yellow for me.", pt="Amarela para mim.", reply="Great. And your friend?")]),
  dict(npc="Anything else?", opts=[
   dict(en="How does it work?", pt="Como funciona?", reply="Hit the ball into the hole. Six tries each."),
   dict(en="Where is hole one?", pt="Onde fica o buraco um?", reply="Go straight. It's on the left."),
   dict(en="No, thank you.", pt="Não, obrigado.", reply="Have fun!")]),
 ], change=["O atendente diz que o preço é doze dólares cada: pague de novo com o valor certo.", "Só sobrou uma cor: escolha outra cor.", "O jogo está cheio: pergunte quanto tempo vai esperar."]),
 writing=dict(task="Você está no balcão do mini golfe. Escreva 2 ou 3 frases: peça ingressos para duas pessoas, escolha uma cor e pergunte como funciona.", model="Hi! Two for mini golf, please. I'll take red. How does it work?", kw=["two", "golf", "take", "work"], checks=["Pediu dois ingressos.", "Escolheu uma cor.", "Perguntou como funciona."]),
 scenes=dict(pool=["park", "park2", "playground", "counter"], npc=dict(g="f", role="clerk"), you=dict(g="m")),
 convo=dict(npc=dict(name="Claire"), story="Você está em uma pista de mini golfe em um parque. A Claire trabalha no balcão.", turns=[
  dict(npc="Hi! How can I help you?", pt="Oi! Como posso ajudar?", opts=[
   dict(en="Hi! Two for mini golf, please.", pt="Oi! Dois para mini golfe, por favor.", ok=True, fb="Pedido claro e educado."),
   dict(en="That's ten dollars each.", pt="São dez dólares cada.", ok=False, fb="Quem fala o preço é a atendente."),
   dict(en="Hit the ball into the hole.", pt="Acerte a bola no buraco.", ok=False, fb="Isso é regra do jogo, vem depois.")]),
  dict(npc="That's ten dollars each.", pt="São dez dólares cada.", opts=[
   dict(en="Which color do you want?", pt="Qual cor você quer?", ok=False, fb="Quem pergunta isso é a atendente."),
   dict(en="Hi! Two for mini golf, please.", pt="Oi! Dois para mini golfe, por favor.", ok=False, fb="Você já pediu os ingressos."),
   dict(en="Here's twenty. Keep the change.", pt="Aqui estão vinte. Fique com o troco.", ok=True, fb="Dois ingressos de dez dão vinte.")]),
  dict(npc="Which color do you want?", pt="Qual cor você quer?", opts=[
   dict(en="I'll take red.", pt="Eu fico com a vermelha.", ok=True, fb="Escolhe a cor de forma natural."),
   dict(en="Here are your clubs and balls.", pt="Aqui estão tacos e bolas.", ok=False, fb="Essa fala é da atendente."),
   dict(en="How many tries?", pt="Quantas tentativas?", ok=False, fb="Não responde à pergunta da cor.")]),
  dict(npc="Here are your clubs and balls.", pt="Aqui estão tacos e bolas.", opts=[
   dict(en="That's ten dollars each.", pt="São dez dólares cada.", ok=False, fb="O preço já foi dito."),
   dict(en="How does it work?", pt="Como funciona?", ok=True, fb="Pergunta pelas regras."),
   dict(en="Keep the change.", pt="Fique com o troco.", ok=False, fb="Você já pagou antes.")]),
  dict(npc="Hit the ball into the hole.", pt="Acerte a bola no buraco.", opts=[
   dict(en="Two for mini golf, please.", pt="Dois para mini golfe, por favor.", ok=False, fb="Você já pagou."),
   dict(en="How many tries?", pt="Quantas tentativas?", ok=True, fb="Pergunta natural sobre a regra."),
   dict(en="I'll take red.", pt="Eu fico com a vermelha.", ok=False, fb="A cor já foi escolhida.")]),
 ]),
)
