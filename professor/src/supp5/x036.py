X = dict(
 key=dict(big="Do you want a combo?", label="Combo ou item avulso", sub="Em lanchonetes dos EUA, combo costuma incluir sanduíche, batata frita e bebida; o conteúdo varia por lugar."),
 mini=[
  dict(who="Malik", en="Welcome! What can I {get you|get for you|get started for you}?", pt="Bem-vindo! O que {posso trazer|posso preparar|vai ser}?"),
  dict(who="You", en="A {cheeseburger|hamburger|chicken sandwich}, please.", pt="Um {cheeseburger|hambúrguer|sanduíche de frango}, por favor."),
  dict(who="Malik", en="Do you want a combo? It comes with {fries and a drink|fries and a soda|fries and a cola}.", pt="Quer o combo? Vem com {batata frita e uma bebida|batata frita e um refrigerante|batata frita e uma cola}."),
  dict(who="You", en="OK. A combo, and a {cola|lemonade|water}.", pt="Ok. Um combo e {uma cola|uma limonada|uma água}."),
 ],
 dlg=[
  dict(who="Malik", en="Welcome! What can I {get you|get for you}?", pt="Bem-vindo! O que {posso trazer|vai ser}?"),
  dict(who="You", en="A {cheeseburger|hamburger}, please.", pt="Um {cheeseburger|hambúrguer}, por favor."),
  dict(who="Malik", en="Do you want a {combo|meal deal}?", pt="Quer o {combo|menu completo}?"),
  dict(who="You", en="What {comes with it|is in it}?", pt="O que {vem nele|tem nele}?"),
  dict(who="Malik", en="{Fries and a drink.|Fries and a soda.}", pt="{Batata frita e uma bebida.|Batata frita e um refrigerante.}"),
  dict(who="You", en="OK. A combo, and a {cola|lemonade}.", pt="Ok. Um combo e {uma cola|uma limonada}."),
  dict(who="Malik", en="Anything else?", pt="Mais alguma coisa?"),
  dict(who="You", en="No, thanks. {That's all.|That's it.}", pt="Não, valeu. {É só isso.|Só isso.}"),
  dict(who="Malik", en="Enjoy your {burger|meal}!", pt="Bom apetite com seu {hambúrguer|lanche}!"),
 ],
 vocab=[
  dict(w="burger", pt="hambúrguer", e="🍔", ex=["I'd like a burger, please.", "The burger is hot."]),
  dict(w="combo", pt="combo", e="🍱", ex=["I'll have the combo.", "The combo comes with fries."]),
  dict(w="fries", pt="batata frita", e="🍟", ex=["Do you want fries?", "The fries are hot."]),
  dict(w="cola", pt="cola (refrigerante)", e="🥤", ex=["A cola, please.", "I'd like a small cola."]),
  dict(w="lemonade", pt="limonada", e="🍋", ex=["I'll have a lemonade.", "The lemonade is cold."]),
  dict(w="ketchup", pt="ketchup", e="🍅", ex=["Can I have ketchup?", "I like ketchup on my fries."]),
 ],
 molds=[
  dict(title="Pedir o lanche", frame="A {food}, please.", slots=[dict(key="food", opts=["cheeseburger", "hamburger", "chicken sandwich"])], model="A cheeseburger, please.", note="A + o item: simples e educado. Use please no final."),
  dict(title="Escolher o combo", frame="OK. A combo, and {drink}.", slots=[dict(key="drink", opts=["a cola", "a lemonade", "a water"])], model="OK. A combo, and a cola.", note="And + a bebida escolhida. Cada bebida leva a."),
  dict(title="Escrever o pedido", frame="Hi! I'd like {food} with {side}, please.", slots=[dict(key="food", opts=["a cheeseburger", "a hamburger", "a chicken sandwich"]), dict(key="side", opts=["fries", "a salad", "onion rings"])], model="Hi! I'd like a cheeseburger with fries, please.", note="I'd like... with... pede o lanche com um acompanhamento."),
 ],
 sounds=[
  dict(say="A cheeseburger, please.", tag="acento: CHEESEburger", tip="O acento está em CHEESE: 'CHIZ-bur-ger'. Please fica leve."),
  dict(say="What comes with it?", tag="ligação: comes with it", tip="Comes with it soa quase 'cumzwithit'. Una as palavras."),
  dict(say="Fries and a drink.", tag="ligação: and a", tip="And a vira 'enda'. Os acentos ficam em fries e drink."),
 ],
 role=dict(turns=[
  dict(npc="Welcome! What can I get you?", opts=[
   dict(en="A cheeseburger, please.", pt="Um cheeseburger, por favor.", reply="One cheeseburger. Do you want a combo?"),
   dict(en="A hamburger, please.", pt="Um hambúrguer, por favor.", reply="One hamburger. Do you want a combo?"),
   dict(en="A chicken sandwich, please.", pt="Um sanduíche de frango, por favor.", reply="One chicken sandwich. Do you want a combo?")]),
  dict(npc="Do you want a combo?", opts=[
   dict(en="What comes with it?", pt="O que vem nele?", reply="Fries and a drink."),
   dict(en="What is in the combo?", pt="O que tem no combo?", reply="Fries and a drink. It's a good deal."),
   dict(en="Does it come with a drink?", pt="Vem com bebida?", reply="Yes, fries and a drink.")]),
  dict(npc="Fries and a drink.", opts=[
   dict(en="OK. A combo, and a cola.", pt="Ok. Um combo e uma cola.", reply="One combo with a cola. Got it."),
   dict(en="OK. A combo, and a lemonade.", pt="Ok. Um combo e uma limonada.", reply="One combo with a lemonade. Good choice."),
   dict(en="Sure. A combo with water, please.", pt="Claro. Um combo com água, por favor.", reply="One combo with water. Sure.")]),
  dict(npc="Anything else?", opts=[
   dict(en="No, thanks. That's all.", pt="Não, valeu. É só isso.", reply="Great! Enjoy your burger!"),
   dict(en="Yes, ketchup, please.", pt="Sim, ketchup, por favor.", reply="Sure! Here's some ketchup. Enjoy your burger!"),
   dict(en="No, that's it. Thank you!", pt="Não, só isso. Obrigado!", reply="You're welcome. Enjoy your burger!")]),
 ], change=["Acabou a cola: escolha outra bebida.", "Você é vegetariano: pergunte se há opção sem carne.", "Você quer o combo para viagem: diga to go."]),
 writing=dict(task="Você está numa lanchonete. Escreva 2 ou 3 frases: peça um lanche, escolha o combo e diga a bebida.", model="Hi! A cheeseburger, please. I want the combo with fries and a cola. That's all, thanks!", kw=["cheeseburger", "combo", "fries", "cola"], checks=["Pediu um lanche com please.", "Escolheu o combo.", "Disse qual bebida quer."]),
 scenes=dict(pool=["diner", "restaurant", "counter", "street"], npc=dict(g="m", role="cashier"), you=dict(g="f")),
 convo=dict(npc=dict(name="Malik"), story="Você está numa lanchonete. Peça um hambúrguer e escolha o combo.", turns=[
  dict(npc="Welcome! What can I get you?", pt="Bem-vindo! O que vai ser?", opts=[
   dict(en="Welcome! How are you?", pt="Bem-vindo! Como vai?", ok=False, fb="Quem dá as boas-vindas é o atendente; você faz o pedido."),
   dict(en="Anything else?", pt="Mais alguma coisa?", ok=False, fb="Essa pergunta é do atendente."),
   dict(en="A cheeseburger, please.", pt="Um cheeseburger, por favor.", ok=True, fb="Pedido simples e educado.")]),
  dict(npc="Do you want a combo?", pt="Quer o combo?", opts=[
   dict(en="What comes with it?", pt="O que vem nele?", ok=True, fb="Pergunta o que o combo inclui antes de decidir."),
   dict(en="Yes, it is a burger.", pt="Sim, é um hambúrguer.", ok=False, fb="Não responde à pergunta; escolha sim ou pergunte."),
   dict(en="No, I'm a combo.", pt="Não, eu sou um combo.", ok=False, fb="Frase sem sentido; combo é o menu.")]),
  dict(npc="Fries and a drink.", pt="Batata frita e uma bebida.", opts=[
   dict(en="OK. A combo, and a cola.", pt="Ok. Um combo e uma cola.", ok=True, fb="Aceita o combo e escolhe a bebida."),
   dict(en="Fries and a drink, too.", pt="Batata frita e uma bebida também.", ok=False, fb="Repete o que ele disse, sem responder."),
   dict(en="Enjoy your burger!", pt="Bom apetite!", ok=False, fb="Quem diz isso é o atendente, no final.")]),
  dict(npc="Anything else?", pt="Mais alguma coisa?", opts=[
   dict(en="A cheeseburger, please.", pt="Um cheeseburger, por favor.", ok=False, fb="O hambúrguer já foi pedido."),
   dict(en="No, thanks. That's all.", pt="Não, valeu. É só isso.", ok=True, fb="Fecha o pedido com educação."),
   dict(en="What comes with it?", pt="O que vem nele?", ok=False, fb="Isso já foi explicado.")]),
  dict(npc="Enjoy your burger!", pt="Bom apetite!", opts=[
   dict(en="Thanks! You too.", pt="Obrigado! Igualmente.", ok=True, fb="Resposta simpática ao desejo de bom apetite."),
   dict(en="Welcome! What can I get you?", pt="Bem-vindo! O que vai ser?", ok=False, fb="Esta fala é de quem atende."),
   dict(en="Do you want a combo?", pt="Quer o combo?", ok=False, fb="Esta pergunta é do atendente e já foi feita.")]),
 ]),
)
