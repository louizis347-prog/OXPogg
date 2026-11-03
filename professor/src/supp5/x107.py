X = dict(
 key=dict(big="I'd love to!", label="Aceitar o convite de almoço", sub="Aceite um convite de colegas, pergunte o que é bom e faça o seu pedido."),
 mini=[
  dict(who="Cole", en="Do you want to {have lunch|get coffee|take a walk} with us?", pt="Quer {almoçar|tomar um café|dar uma volta} com a gente?"),
  dict(who="You", en="Yes, I'd love to! Where are we {going|eating|meeting}?", pt="Quero sim! Onde vamos {ir|comer|nos encontrar}?"),
  dict(who="Cole", en="To the {deli|café|park} on the corner.", pt="{À delicatessen|Ao café|Ao parque} da esquina."),
  dict(who="You", en="I'll have a {turkey|tuna|chicken} sandwich.", pt="Vou querer um sanduíche de {peru|atum|frango}."),
 ],
 dlg=[
  dict(who="Cole", en="Alex, do you want to have {lunch|coffee} with us?", pt="Alex, quer {almoçar|tomar um café} com a gente?"),
  dict(who="You", en="Yes, I'd love to! Where are we {going?|eating?}", pt="Quero sim! {Aonde vamos?|Onde vamos comer?}"),
  dict(who="Cole", en="To the {deli|café} on the corner.", pt="{À delicatessen|Ao café} da esquina."),
  dict(who="You", en="Great. What's {good|best} there?", pt="Ótimo. O que é {bom|melhor} lá?"),
  dict(who="Cole", en="The {sandwiches|salads} are great.", pt="{Os sanduíches|As saladas} são ótimos."),
  dict(who="You", en="I'll have a {turkey|tuna|chicken} sandwich.", pt="Vou querer um sanduíche de {peru|atum|frango}."),
  dict(who="Cole", en="Me too. And a {salad.|soup.}", pt="Eu também. E {uma salada.|uma sopa.}"),
  dict(who="You", en="Let's go before it's {crowded.|full.}", pt="Vamos antes de ficar {cheio.|lotado.}"),
  dict(who="Cole", en="Do you bring {lunch|food} from home?", pt="Você traz {almoço|comida} de casa?"),
 ],
 vocab=[
  dict(w="deli", pt="delicatessen", e="🥪", ex=["The deli is on the corner.", "We eat at the deli."]),
  dict(w="lunchbox", pt="marmita", e="🍱", ex=["My lunchbox is blue.", "I bring a lunchbox from home."]),
  dict(w="mustard", pt="mostarda", e="🌭", ex=["I like mustard.", "Put mustard on the sandwich."]),
  dict(w="tuna", pt="atum", e="🐟", ex=["I'll have a tuna sandwich.", "The tuna is fresh."]),
  dict(w="crowded", pt="cheio de gente", e="👥", ex=["The deli is crowded.", "It is not crowded now."]),
  dict(w="break", pt="intervalo", e="⏸️", ex=["My lunch break is one hour.", "Take a break."]),
 ],
 molds=[
  dict(title="Convidar", frame="Do you want to {verb} with us?", slots=[dict(key="verb", opts=["have lunch", "get coffee", "take a break"])], model="Do you want to have lunch with us?", note="Do you want to + verbo base. Depois de 'to', o verbo não muda."),
  dict(title="Pedir comida", frame="I'll have a {food} sandwich and a {side}.", slots=[dict(key="food", opts=["turkey", "tuna", "chicken"]), dict(key="side", opts=["salad", "soup", "cookie"])], model="I'll have a turkey sandwich and a salad.", note="I'll have... é o jeito natural de pedir. Use a antes de uma coisa só."),
  dict(title="Escrever convite", frame="Hi {name}! Lunch at {time}? Let's go to the {place}.", slots=[dict(key="name", opts=["Cole", "Sam", "Ana"]), dict(key="time", opts=["noon", "12:30", "one o'clock"]), dict(key="place", opts=["deli", "café", "park"])], model="Hi Cole! Lunch at noon? Let's go to the deli.", note="Let's + verbo = sugestão. Em mensagens curtas, a gente corta palavras."),
 ],
 sounds=[
  dict(say="Do you want to have lunch?", tag="ligação: want to / have lunch", tip="Una 'want to' (soa 'wanna') e 'have lunch'. Diga tudo num fôlego só."),
  dict(say="I'd love to!", tag="ligação: love to", tip="O v de 'love' encosta no 'to': 'luv-too'. A força vai em LOVE."),
  dict(say="I'll have a turkey sandwich.", tag="ligação: have a", tip="'have a' soa 'ha-vuh'. Acentue TUR e SAND."),
 ],
 role=dict(turns=[
  dict(npc="Do you want to have lunch with us?", opts=[
   dict(en="Yes, I'd love to!", pt="Quero sim!", reply="Great! We go to the deli."),
   dict(en="Sure, thanks! Where are we going?", pt="Claro, obrigado! Aonde vamos?", reply="To the deli on the corner."),
   dict(en="Yes, I'd love to! Where are we going?", pt="Quero sim! Aonde vamos?", reply="To the deli on the corner.")]),
  dict(npc="To the deli on the corner.", opts=[
   dict(en="Great. What's good there?", pt="Ótimo. O que é bom lá?", reply="The sandwiches are great."),
   dict(en="Nice. Is it far?", pt="Legal. É longe?", reply="No, it's two minutes from here."),
   dict(en="Cool. What do they have?", pt="Legal. O que eles têm?", reply="Sandwiches and salads.")]),
  dict(npc="So, what do you want to eat?", opts=[
   dict(en="I'll have a turkey sandwich.", pt="Vou querer um sanduíche de peru.", reply="Me too. And a salad."),
   dict(en="I'll have a tuna sandwich.", pt="Vou querer um sanduíche de atum.", reply="Good choice! I like tuna too."),
   dict(en="I'll have a chicken sandwich.", pt="Vou querer um sanduíche de frango.", reply="Nice. I'll get the turkey.")]),
  dict(npc="Look, the line is getting long.", opts=[
   dict(en="Let's go before it's crowded.", pt="Vamos antes de ficar cheio.", reply="Good idea. Let's go."),
   dict(en="Let's sit by the window.", pt="Vamos sentar perto da janela.", reply="Okay. I see a table."),
   dict(en="Let's order now.", pt="Vamos pedir agora.", reply="Yes, I'm hungry!")]),
 ], change=["Cole não gosta de peru: peça outra opção e pergunte o que ele quer.", "O deli está fechado: sugira outro lugar.", "Você traz o almoço de casa hoje: diga isso e pergunte se pode se sentar com eles."]),
 writing=dict(task="Escreva 2 ou 3 frases convidando um colega para almoçar: diga o horário, o lugar e o que vai pedir.", model="Hi Cole! Lunch at noon? Let's go to the deli. I'll have a tuna sandwich.", kw=["lunch", "deli", "sandwich", "noon"], checks=["Convidou o colega para almoçar.", "Disse o horário ou o lugar.", "Disse o que vai pedir."]),
 scenes=dict(pool=["cafe", "office", "counter", "street"], npc=dict(g="m", role="coworker"), you=dict(g="m")),
 convo=dict(npc=dict(name="Cole"), story="Você é novo no trabalho. Cole, um colega, convida você para almoçar.", turns=[
  dict(npc="Alex, do you want to have lunch with us?", pt="Alex, quer almoçar com a gente?", opts=[
   dict(en="I'll have a turkey sandwich.", pt="Vou querer um sanduíche de peru.", ok=False, fb="Cedo demais: ainda não estão no deli."),
   dict(en="Yes, I'd love to! Where are we going?", pt="Quero sim! Aonde vamos?", ok=True, fb="Aceite e pergunte o lugar."),
   dict(en="Me too.", pt="Eu também.", ok=False, fb="Não é uma resposta a um convite.")]),
  dict(npc="To the deli on the corner.", pt="À delicatessen da esquina.", opts=[
   dict(en="Do you bring lunch from home?", pt="Você traz almoço de casa?", ok=False, fb="É uma pergunta que o Cole faz depois."),
   dict(en="Yes, I'd love to!", pt="Quero sim!", ok=False, fb="Você já aceitou."),
   dict(en="Great. What's good there?", pt="Ótimo. O que é bom lá?", ok=True, fb="Pedir uma dica sobre o lugar.")]),
  dict(npc="The sandwiches are great.", pt="Os sanduíches são ótimos.", opts=[
   dict(en="I'll have a turkey sandwich.", pt="Vou querer um sanduíche de peru.", ok=True, fb="Fez o pedido com I'll have."),
   dict(en="To the deli on the corner.", pt="À delicatessen da esquina.", ok=False, fb="Essa é a fala dele."),
   dict(en="Let's go before it's crowded.", pt="Vamos antes de ficar cheio.", ok=False, fb="Ainda falta escolher o pedido.")]),
  dict(npc="Me too. And a salad.", pt="Eu também. E uma salada.", opts=[
   dict(en="Do you want to have lunch?", pt="Quer almoçar?", ok=False, fb="Vocês já estão indo."),
   dict(en="Let's go before it's crowded.", pt="Vamos antes de ficar cheio.", ok=True, fb="Boa sugestão para a hora do almoço."),
   dict(en="What's good there?", pt="O que é bom lá?", ok=False, fb="Já perguntou e ele respondeu.")]),
  dict(npc="Do you bring lunch from home?", pt="Você traz almoço de casa?", opts=[
   dict(en="Sometimes, but today I like the deli.", pt="Às vezes, mas hoje gosto do deli.", ok=True, fb="Resposta real e simples."),
   dict(en="I'll have a turkey sandwich.", pt="Vou querer um sanduíche de peru.", ok=False, fb="Não responde à pergunta."),
   dict(en="Yes, I'd love to!", pt="Quero sim!", ok=False, fb="Isso responde a um convite, não a essa pergunta.")]),
 ]),
)
