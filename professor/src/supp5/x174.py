X = dict(
 key=dict(big="Two tickets, please", label="Comprar ingressos", sub="Diga quantos ingressos, qual filme e horário, escolha onde sentar e pague. Depois pergunte pela pipoca."),
 mini=[
  dict(who="You", en="Hi! {Two|Three|Four} tickets for the {seven|eight|nine} o'clock movie.", pt="Oi! {Dois|Três|Quatro} ingressos para o filme das {sete|oito|nove}."),
  dict(who="Carlos", en="Which {movie?|film?}", pt="Qual {filme?|filme?}"),
  dict(who="You", en="The new {comedy,|drama,|cartoon,} please.", pt="{A nova comédia,|O novo drama,|O novo desenho,} por favor."),
  dict(who="Carlos", en="Where do you want to sit? {Front,|Middle,|Back,} or...", pt="Onde quer sentar? {Na frente,|No meio,|Atrás,} ou..."),
 ],
 dlg=[
  dict(who="Carlos", en="Hi! {Two|Three} tickets for the seven o'clock {movie.|film.}", pt="Oi! {Dois|Três} ingressos para o {filme|filme} das sete."),
  dict(who="You", en="Which {movie?|film?}", pt="Qual {filme?|filme?}"),
  dict(who="Carlos", en="The new {comedy,|drama,} please.", pt="{A nova comédia,|O novo drama,} por favor."),
  dict(who="You", en="Okay. Where do you want to {sit?|stand?}", pt="Ok. Onde quer {sentar?|ficar?}"),
  dict(who="Carlos", en="In the {middle,|back,|front,} not too close.", pt="{No meio,|Atrás,|Na frente,} não muito perto."),
  dict(who="You", en="Those seats are {twelve|ten} dollars each.", pt="Esses lugares custam {doze|dez} dólares cada."),
  dict(who="Carlos", en="Here's my {card.|cash.}", pt="Aqui está meu {cartão.|dinheiro.}"),
  dict(who="You", en="Thanks. {Theater|Room} number five.", pt="Obrigado. {Sala|Sala} número cinco."),
  dict(who="Carlos", en="Where can I buy {popcorn?|snacks?}", pt="Onde posso comprar {pipoca?|lanches?}"),
 ],
 vocab=[
  dict(w="theater", pt="cinema, sala", e="🎭", ex=["The theater is big.", "We go to the theater."]),
  dict(w="showtime", pt="horário da sessão", e="🕖", ex=["The showtime is seven.", "What is the showtime?"]),
  dict(w="middle", pt="meio", e="🎯", ex=["I sit in the middle.", "The seat is in the middle."]),
  dict(w="front", pt="frente", e="⬆️", ex=["The front seats are close.", "I sit in the front."]),
  dict(w="back", pt="fundo, atrás", e="⬇️", ex=["The back seats are far.", "I sit in the back."]),
  dict(w="dark", pt="escuro", e="🌑", ex=["The theater is dark.", "It is dark at seven."]),
 ],
 molds=[
  dict(title="Pedir ingressos", frame="{number} tickets for the {time} o'clock movie, please.", slots=[dict(key="number", opts=["Two", "Three", "Four"]), dict(key="time", opts=["seven", "eight", "nine"])], model="Two tickets for the seven o'clock movie, please.", note="Número + tickets (plural). O'clock com hora cheia."),
  dict(title="Escolher o lugar", frame="I'd like to sit in the {place}, please.", slots=[dict(key="place", opts=["middle", "front", "back"])], model="I'd like to sit in the middle, please.", note="In the + lugar. Front, middle e back respondem 'Where do you want to sit?'."),
  dict(title="Escrever o pedido", frame="Hi! {number} tickets for the {movie} at {time}. In the {place}, please.", slots=[dict(key="number", opts=["Two", "Three", "Four"]), dict(key="movie", opts=["new comedy", "new drama", "cartoon"]), dict(key="time", opts=["seven", "eight", "nine"]), dict(key="place", opts=["middle", "front", "back"])], model="Hi! Two tickets for the new comedy at seven. In the middle, please.", note="Frase completa: quantidade, filme, hora e lugar."),
 ],
 sounds=[
  dict(say="Those seats are twelve dollars.", tag="som: ee de seats", tip="Seat tem o som longo 'ii', como 'ssiit' esticado. Sit é curto. Cuidado para não trocar."),
  dict(say="Two tickets, please.", tag="ritmo: TWO TICkets PLEASE", tip="Acentue TWO, TIC e PLEASE; 'tickets' tem o acento no começo."),
  dict(say="Where can I buy popcorn?", tag="ligação: can I", tip="Una can e I: 'kenai'. Acentue WHERE, BUY e POP."),
 ],
 role=dict(turns=[
  dict(npc="Hi! Can I help you?", opts=[
   dict(en="Hi! Two tickets for the seven o'clock movie.", pt="Oi! Dois ingressos para o filme das sete.", reply="Which movie?"),
   dict(en="Hello. Three tickets for eight o'clock, please.", pt="Olá. Três ingressos para as oito, por favor.", reply="Which movie?"),
   dict(en="Hi! Two tickets for tonight, please.", pt="Oi! Dois ingressos para hoje à noite, por favor.", reply="Which movie?")]),
  dict(npc="Which movie?", opts=[
   dict(en="The new comedy, please.", pt="A nova comédia, por favor.", reply="Okay. Where do you want to sit?"),
   dict(en="The cartoon, please.", pt="O desenho, por favor.", reply="Okay. Where do you want to sit?"),
   dict(en="The new drama, please.", pt="O novo drama, por favor.", reply="Okay. Where do you want to sit?")]),
  dict(npc="Where do you want to sit?", opts=[
   dict(en="In the middle, not too close.", pt="No meio, não muito perto.", reply="Those seats are twelve dollars each."),
   dict(en="In the back, please.", pt="Atrás, por favor.", reply="Those seats are ten dollars each."),
   dict(en="In the front, please.", pt="Na frente, por favor.", reply="Those seats are nine dollars each.")]),
  dict(npc="Those seats are twelve dollars each.", opts=[
   dict(en="Here's my card.", pt="Aqui está meu cartão.", reply="Thanks. Theater number five."),
   dict(en="Can I pay with cash?", pt="Posso pagar em dinheiro?", reply="Sure. Theater number five."),
   dict(en="That's fine. Here's my card.", pt="Tudo bem. Aqui está meu cartão.", reply="Thanks. Theater number five.")]),
 ], change=["A sessão das sete está lotada: escolha outro horário.", "Os lugares do meio acabaram: escolha frente ou fundo.", "Você quer um ingresso a mais: diga o novo número."]),
 writing=dict(task="Escreva 2 ou 3 frases para comprar ingressos: diga quantos, qual filme e horário e onde quer sentar.", model="Hi! Two tickets for the new comedy at seven o'clock, please. In the middle, not too close.", kw=["tickets", "comedy", "seven", "middle"], checks=["Disse quantos ingressos.", "Disse o filme e o horário.", "Pediu o lugar."]),
 scenes=dict(pool=["lobby", "lobby1", "counter", "street"], npc=dict(g="m", role="cashier"), you=dict(g="f")),
 convo=dict(npc=dict(name="Carlos"), story="Você está em um cinema em Portland. O Carlos trabalha na bilheteria.", turns=[
  dict(npc="Hi! Can I help you?", pt="Oi! Posso ajudar?", opts=[
   dict(en="Hi! Two tickets for the seven o'clock movie.", pt="Oi! Dois ingressos para o filme das sete.", ok=True, fb="Diz o que quer: número e horário."),
   dict(en="Those seats are twelve dollars each.", pt="Esses lugares custam doze dólares cada.", ok=False, fb="Quem diz o preço é o vendedor."),
   dict(en="Theater number five.", pt="Sala número cinco.", ok=False, fb="Essa fala vem depois da compra.")]),
  dict(npc="Which movie?", pt="Qual filme?", opts=[
   dict(en="Where can I buy popcorn?", pt="Onde posso comprar pipoca?", ok=False, fb="Ainda não é hora: primeiro o filme."),
   dict(en="The new comedy, please.", pt="A nova comédia, por favor.", ok=True, fb="Responde qual filme."),
   dict(en="In the middle, please.", pt="No meio, por favor.", ok=False, fb="Ele ainda não perguntou o lugar.")]),
  dict(npc="Okay. Where do you want to sit?", pt="Ok. Onde quer sentar?", opts=[
   dict(en="In the middle, not too close.", pt="No meio, não muito perto.", ok=True, fb="Diz o lugar."),
   dict(en="The new comedy, please.", pt="A nova comédia, por favor.", ok=False, fb="Você já escolheu o filme."),
   dict(en="Here's my card.", pt="Aqui está meu cartão.", ok=False, fb="O preço ainda não foi dito.")]),
  dict(npc="Those seats are twelve dollars each.", pt="Esses lugares custam doze dólares cada.", opts=[
   dict(en="Which movie?", pt="Qual filme?", ok=False, fb="Quem pergunta isso é o vendedor."),
   dict(en="Theater number five.", pt="Sala número cinco.", ok=False, fb="Essa fala é do vendedor."),
   dict(en="Here's my card.", pt="Aqui está meu cartão.", ok=True, fb="Forma natural de pagar.")]),
  dict(npc="Thanks. Theater number five.", pt="Obrigado. Sala número cinco.", opts=[
   dict(en="Where can I buy popcorn?", pt="Onde posso comprar pipoca?", ok=True, fb="Pergunta útil antes de entrar."),
   dict(en="Two tickets, please.", pt="Dois ingressos, por favor.", ok=False, fb="Você já comprou."),
   dict(en="Which movie?", pt="Qual filme?", ok=False, fb="Você já escolheu o filme.")]),
 ]),
)
