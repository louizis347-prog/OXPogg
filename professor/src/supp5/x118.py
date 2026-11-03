X = dict(
 key=dict(big="I lost my backpack", label="Achados e perdidos", sub="Diga o que perdeu, descreva a cor e o que tem dentro e confirme quando encontrarem."),
 mini=[
  dict(who="You", en="Excuse me, I lost my {backpack|wallet|umbrella}.", pt="Com licença, perdi {minha mochila|minha carteira|meu guarda-chuva}."),
  dict(who="Maya", en="What color is it?", pt="De que cor é?"),
  dict(who="You", en="It's {black|blue|gray} with a red {zipper.|strap.|tag.}", pt="É {preta|azul|cinza} com {zíper|alça|etiqueta} vermelho(a)."),
  dict(who="Maya", en="Where did you lose it? On the {bus?|train?|street?}", pt="Onde você perdeu? No {ônibus?|trem?|na rua?}"),
 ],
 dlg=[
  dict(who="Maya", en="Excuse me, I lost my {backpack.|wallet.|purse.}", pt="Com licença, perdi {minha mochila.|minha carteira.|minha bolsa.}"),
  dict(who="You", en="What color is it?", pt="De que cor é?"),
  dict(who="Maya", en="It's {black|blue} with a red zipper.", pt="É {preta|azul} com zíper vermelho."),
  dict(who="You", en="Where did you lose it?", pt="Onde você perdeu?"),
  dict(who="Maya", en="Maybe on the {bus.|train.}", pt="Talvez no {ônibus.|trem.}"),
  dict(who="You", en="What's inside?", pt="O que tem dentro?"),
  dict(who="Maya", en="A {notebook|charger} and a water bottle.", pt="Um {caderno|carregador} e uma garrafa de água."),
  dict(who="You", en="Let me check. Is this {it?|yours?}", pt="Vou ver. É {esta?|sua?}"),
  dict(who="Maya", en="Yes! That's mine. {Thank you!|Thanks a lot!}", pt="Sim! É minha. {Obrigado!|Muito obrigado!}"),
 ],
 vocab=[
  dict(w="wallet", pt="carteira (de dinheiro)", e="👛", ex=["My wallet is brown.", "I lost my wallet."]),
  dict(w="glasses", pt="óculos", e="👓", ex=["These are my glasses.", "She wears glasses."]),
  dict(w="watch", pt="relógio de pulso", e="⌚", ex=["I lost my watch.", "His watch is black."]),
  dict(w="purse", pt="bolsa", e="👜", ex=["Her purse is red.", "The purse is on the shelf."]),
  dict(w="charger", pt="carregador", e="🔌", ex=["I need a charger.", "This is my phone charger."]),
  dict(w="hat", pt="chapéu, boné", e="🧢", ex=["He has a black hat.", "Put on your hat."]),
 ],
 molds=[
  dict(title="Dizer o que perdeu", frame="Excuse me, I lost my {thing}.", slots=[dict(key="thing", opts=["wallet", "glasses", "purse", "hat"])], model="Excuse me, I lost my wallet.", note="I lost = eu perdi. Lost é o passado de lose."),
  dict(title="Descrever o item", frame="It's {color} with a {detail}.", slots=[dict(key="color", opts=["black", "blue", "brown"]), dict(key="detail", opts=["red zipper", "small pocket", "white tag"])], model="It's black with a red zipper.", note="With = com. Use para dar um detalhe do objeto."),
  dict(title="Escrever o aviso", frame="Hi! I lost my {thing} on the {place}. It's {color}. Inside: a {inside}.", slots=[dict(key="thing", opts=["backpack", "wallet", "purse"]), dict(key="place", opts=["bus", "train", "street"]), dict(key="color", opts=["black", "blue", "gray"]), dict(key="inside", opts=["notebook", "charger", "hat"])], model="Hi! I lost my backpack on the bus. It's black. Inside: a notebook.", note="On the bus/train. Inside: lista o que tem dentro."),
 ],
 sounds=[
  dict(say="Where did you lose it?", tag="redução: did you → didja", tip="Did + you soa 'didja'. Una as duas palavras sem pausa."),
  dict(say="Let me check.", tag="redução: let me → lemme", tip="Let me soa 'lemi'. O t quase desaparece."),
  dict(say="Is this it?", tag="ligação: is this it", tip="Soa 'is-thi-sit'. O s liga na vogal de it."),
 ],
 role=dict(turns=[
  dict(npc="Hello. Can I help you?", opts=[
   dict(en="Excuse me, I lost my backpack.", pt="Com licença, perdi minha mochila.", reply="What color is it?"),
   dict(en="Hi! I lost my wallet.", pt="Oi! Perdi minha carteira.", reply="What color is it?"),
   dict(en="Excuse me, I lost my glasses.", pt="Com licença, perdi meus óculos.", reply="What color are they?")]),
  dict(npc="What color is it?", opts=[
   dict(en="It's black with a red zipper.", pt="É preta com zíper vermelho.", reply="Where did you lose it?"),
   dict(en="It's blue and small.", pt="É azul e pequena.", reply="Where did you lose it?"),
   dict(en="It's brown with a white tag.", pt="É marrom com etiqueta branca.", reply="Where did you lose it?")]),
  dict(npc="Where did you lose it?", opts=[
   dict(en="Maybe on the bus.", pt="Talvez no ônibus.", reply="What's inside?"),
   dict(en="I think on the train.", pt="Acho que no trem.", reply="What's inside?"),
   dict(en="I'm not sure. Maybe at school.", pt="Não tenho certeza. Talvez na escola.", reply="What's inside?")]),
  dict(npc="What's inside?", opts=[
   dict(en="A notebook and a water bottle.", pt="Um caderno e uma garrafa de água.", reply="Let me check. Is this it?"),
   dict(en="My charger and a hat.", pt="Meu carregador e um boné.", reply="Let me check. Is this it?"),
   dict(en="A purse and my keys.", pt="Uma bolsa e minhas chaves.", reply="Let me check. Is this it?")]),
 ], change=["Não é a mochila certa: diga que a sua é de outra cor.", "O atendente pede seu nome e telefone: responda.", "Você não lembra onde perdeu: diga que não tem certeza."]),
 writing=dict(task="Escreva um bilhete para os achados e perdidos: diga o que perdeu, a cor e o que tem dentro.", model="Hi! I lost my backpack on the bus. It's black with a red zipper. Inside: a notebook.", kw=["lost", "backpack", "black", "inside"], checks=["Disse o que perdeu.", "Descreveu a cor ou um detalhe.", "Disse o que tem dentro."]),
 scenes=dict(pool=["lobby", "station", "busstop", "subway", "street"], npc=dict(g="f", role="clerk"), you=dict(g="m")),
 convo=dict(npc=dict(name="Maya"), story="Você perdeu sua mochila e vai ao balcão de achados e perdidos.", turns=[
  dict(npc="Hello. Can I help you?", pt="Olá. Posso ajudar?", opts=[
   dict(en="What color is it?", pt="De que cor é?", ok=False, fb="Quem pergunta isso é a atendente."),
   dict(en="Excuse me, I lost my backpack.", pt="Com licença, perdi minha mochila.", ok=True, fb="Diz o problema com educação."),
   dict(en="Yes! That's mine.", pt="Sim! É minha.", ok=False, fb="Ainda não mostraram nada.")]),
  dict(npc="What color is it?", pt="De que cor é?", opts=[
   dict(en="It's black with a red zipper.", pt="É preta com zíper vermelho.", ok=True, fb="Dá cor e um detalhe."),
   dict(en="Where did you lose it?", pt="Onde você perdeu?", ok=False, fb="Quem pergunta isso é a atendente."),
   dict(en="I lost my backpack.", pt="Perdi minha mochila.", ok=False, fb="Você já disse isso.")]),
  dict(npc="Where did you lose it?", pt="Onde você perdeu?", opts=[
   dict(en="A notebook and a water bottle.", pt="Um caderno e uma garrafa de água.", ok=False, fb="Ela perguntou onde, não o que tem dentro."),
   dict(en="Let me check.", pt="Vou ver.", ok=False, fb="Quem confere é a atendente."),
   dict(en="Maybe on the bus.", pt="Talvez no ônibus.", ok=True, fb="Responde o lugar, sem ter certeza.")]),
  dict(npc="What's inside?", pt="O que tem dentro?", opts=[
   dict(en="A notebook and a water bottle.", pt="Um caderno e uma garrafa de água.", ok=True, fb="Lista o que tem dentro."),
   dict(en="Maybe on the bus.", pt="Talvez no ônibus.", ok=False, fb="Você já disse o lugar."),
   dict(en="It's black.", pt="É preta.", ok=False, fb="Você já disse a cor.")]),
  dict(npc="Let me check. Is this it?", pt="Vou ver. É esta?", opts=[
   dict(en="Yes! That's mine. Thank you!", pt="Sim! É minha. Obrigado!", ok=True, fb="Confirma e agradece."),
   dict(en="What's inside?", pt="O que tem dentro?", ok=False, fb="Já foi respondido."),
   dict(en="Excuse me, I lost my backpack.", pt="Com licença, perdi minha mochila.", ok=False, fb="Ela já achou uma mochila.")]),
 ]),
)
