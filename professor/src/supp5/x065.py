X = dict(
 key=dict(big="Who do I call for problems?", label="Conhecer o proprietário", sub="No primeiro dia, receba a chave e pergunte onde ficam as coisas, o dia do lixo e a quem ligar."),
 mini=[
  dict(who="Evan", en="Hi! I'm your new {tenant|neighbor|roommate}.", pt="Oi! Sou seu novo {inquilino|vizinho|colega de casa}."),
  dict(who="You", en="Welcome! Here's your {key|number|keys}.", pt="Bem-vindo! Aqui está sua {chave|número|chaves}."),
  dict(who="Evan", en="Where is the {laundry room|basement|lobby}?", pt="Onde fica {a lavanderia|o porão|o saguão}?"),
  dict(who="You", en="It's in the {basement|lobby|hall}.", pt="Fica {no porão|no saguão|no corredor}."),
 ],
 dlg=[
  dict(who="Evan", en="Hi! I'm your new {tenant.|neighbor.}", pt="Oi! Sou seu novo {inquilino.|vizinho.}"),
  dict(who="You", en="Welcome! Here's your {key.|mail.}", pt="Bem-vindo! Aqui está sua {chave.|correspondência.}"),
  dict(who="Evan", en="Thank you. Where is the {laundry room?|basement?}", pt="Obrigado. Onde fica {a lavanderia?|o porão?}"),
  dict(who="You", en="It's in the {basement.|lobby.}", pt="Fica {no porão.|no saguão.}"),
  dict(who="Evan", en="What day is {trash day?|laundry day?}", pt="Que dia é {o dia do lixo?|o dia da lavanderia?}"),
  dict(who="You", en="It's every {Tuesday.|Friday.|Monday.}", pt="É toda {terça.|sexta.|segunda.}"),
  dict(who="Evan", en="Who do I {call|ask} for problems?", pt="Quem eu {chamo|procuro} se tiver problema?"),
  dict(who="You", en="Call me. My number is on the {door.|wall.}", pt="Me ligue. Meu telefone está {na porta.|na parede.}"),
  dict(who="Evan", en="Don't worry, I'll {fix it|clean it} today.", pt="Não se preocupe, eu {conserto|limpo} hoje."),
 ],
 vocab=[
  dict(w="landlord", pt="proprietário", e="🧑‍💼", ex=["The landlord is friendly.", "Call the landlord."]),
  dict(w='yard', pt='quintal', e='🌳', ex=['The yard is big.', 'The kids play in the yard.']),
  dict(w='roof', pt='telhado', e='🏠', ex=['The roof is red.', 'A cat is on the roof.']),
  dict(w="trash", pt="lixo", e="🗑️", ex=["Trash day is Tuesday.", "Put the trash outside."]),
  dict(w="laundry", pt="roupa suja, lavanderia", e="🧺", ex=["The laundry room is open.", "I do laundry on Sunday."]),
  dict(w="repair", pt="conserto", e="🔧", ex=["The repair is free.", "I need a repair."]),
 ],
 molds=[
  dict(title="Perguntar onde fica", frame="Where is the {place}?", slots=[dict(key="place", opts=["laundry room", "basement", "lobby", "trash room"])], model="Where is the laundry room?", note="Where is the...? pergunta o lugar de algo."),
  dict(title="Dizer o dia", frame="It's every {day}.", slots=[dict(key="day", opts=["Tuesday", "Friday", "Monday"])], model="It's every Tuesday.", note="Every + dia da semana = toda terça, toda sexta."),
  dict(title="Escrever ao proprietário", frame="Hi! I'm your new tenant. {question}", slots=[dict(key="question", opts=["Where is the laundry room?", "What day is trash day?", "Who do I call for problems?"])], model="Hi! I'm your new tenant. Where is the laundry room?", note="Apresente-se e faça uma pergunta curta."),
 ],
 sounds=[
  dict(say="Here's your key.", tag="ligação: here's your", tip="Here's your soa 'hirzyor'. Una e acentue KEY."),
  dict(say="It's in the basement.", tag="ligação: it's in", tip="It's in soa 'itsin'. Acentue BASE-ment."),
  dict(say="Don't worry, I'll fix it today.", tag="ritmo: DON'T WOR-ry, I'll FIX it toDAY", tip="Acentue DON'T, WOR, FIX e DAY; I'll e it ficam fracos."),
 ],
 role=dict(turns=[
  dict(npc="Hi! I'm your new tenant.", opts=[
   dict(en="Welcome! Here's your key.", pt="Bem-vindo! Aqui está sua chave.", reply="Thank you. Where is the laundry room?"),
   dict(en="Hi! Welcome! Here are your keys.", pt="Oi! Bem-vindo! Aqui estão suas chaves.", reply="Thank you. Where is the laundry room?"),
   dict(en="Nice to meet you! Here's your key.", pt="Prazer! Aqui está sua chave.", reply="Thanks! Where is the laundry room?")]),
  dict(npc="Where is the laundry room?", opts=[
   dict(en="It's in the basement.", pt="Fica no porão.", reply="Great. What day is trash day?"),
   dict(en="It's down the stairs, in the basement.", pt="Fica escada abaixo, no porão.", reply="Got it. What day is trash day?"),
   dict(en="It's in the basement, next to the stairs.", pt="Fica no porão, ao lado da escada.", reply="Thanks. What day is trash day?")]),
  dict(npc="What day is trash day?", opts=[
   dict(en="It's every Tuesday.", pt="É toda terça.", reply="Okay. Who do I call for problems?"),
   dict(en="It's every Friday.", pt="É toda sexta.", reply="Okay. Who do I call for problems?"),
   dict(en="It's every Monday morning.", pt="É toda segunda de manhã.", reply="Thanks. Who do I call for problems?")]),
  dict(npc="Who do I call for problems?", opts=[
   dict(en="Call me. My number is on the door.", pt="Me ligue. Meu telefone está na porta.", reply="Don't worry, I'll fix it today."),
   dict(en="Call me anytime. My number is in the lobby.", pt="Me ligue quando quiser. Meu telefone está no saguão.", reply="Great. Thanks!"),
   dict(en="Call the manager. The number is on the wall.", pt="Ligue para o gerente. O número está na parede.", reply="Okay, thanks!")]),
 ], change=["A lavanderia está quebrada hoje: diga quando será consertada.", "Evan perdeu a chave: explique o que fazer.", "O dia do lixo mudou para quarta: avise o inquilino."]),
 writing=dict(task="Você é o novo inquilino. Escreva 2 ou 3 frases ao proprietário: apresente-se e pergunte da lavanderia e do lixo.", model="Hi! I'm your new tenant. Where is the laundry room? What day is trash day?", kw=["tenant", "laundry", "trash", "day"], checks=["Disse que é o novo inquilino.", "Perguntou da lavanderia.", "Perguntou do dia do lixo."]),
 scenes=dict(pool=["lobby", "hall", "lobby1", "street"], npc=dict(g="f", role="customer"), you=dict(g="m")),
 convo=dict(npc=dict(name="Evan"), story="Você é o proprietário e conhece seu novo inquilino, Evan.", turns=[
  dict(npc="Hi! I'm your new tenant.", pt="Oi! Sou seu novo inquilino.", opts=[
   dict(en="Welcome! Here's your key.", pt="Bem-vindo! Aqui está sua chave.", ok=True, fb="Dá as boas-vindas e entrega a chave."),
   dict(en="Don't worry, I'll fix it today.", pt="Não se preocupe, eu conserto hoje.", ok=False, fb="Ainda não há problema algum."),
   dict(en="Where is the laundry room?", pt="Onde fica a lavanderia?", ok=False, fb="Quem pergunta isso é ele.")]),
  dict(npc="Thank you. Where is the laundry room?", pt="Obrigado. Onde fica a lavanderia?", opts=[
   dict(en="It's in the basement.", pt="Fica no porão.", ok=True, fb="Responde o lugar."),
   dict(en="It's every Tuesday.", pt="É toda terça.", ok=False, fb="Isso responde sobre o dia do lixo."),
   dict(en="My number is on the door.", pt="Meu telefone está na porta.", ok=False, fb="Isso responde quem chamar.")]),
  dict(npc="What day is trash day?", pt="Que dia é o dia do lixo?", opts=[
   dict(en="It's in the basement.", pt="Fica no porão.", ok=False, fb="Isso é um lugar, ele pergunta um dia."),
   dict(en="It's every Tuesday.", pt="É toda terça.", ok=True, fb="Responde o dia."),
   dict(en="Here's your key.", pt="Aqui está sua chave.", ok=False, fb="Já entregou a chave.")]),
  dict(npc="Who do I call for problems?", pt="Quem eu chamo se tiver problema?", opts=[
   dict(en="Call me. My number is on the door.", pt="Me ligue. Meu telefone está na porta.", ok=True, fb="Diz quem chamar e onde está o número."),
   dict(en="It's every Tuesday.", pt="É toda terça.", ok=False, fb="Responde outra pergunta."),
   dict(en="Hi! I'm your new tenant.", pt="Oi! Sou seu novo inquilino.", ok=False, fb="Essa fala é dele.")]),
  dict(npc="Don't worry, I'll fix it today.", pt="Não se preocupe, eu conserto hoje.", opts=[
   dict(en="Thank you. See you soon!", pt="Obrigado. Até logo!", ok=True, fb="Fecha a conversa com educação."),
   dict(en="Where is the laundry room?", pt="Onde fica a lavanderia?", ok=False, fb="Já respondeu isso."),
   dict(en="Welcome! Here's your key.", pt="Bem-vindo! Aqui está sua chave.", ok=False, fb="Você já disse isso no começo.")]),
 ]),
)
