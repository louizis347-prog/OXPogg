X = dict(
 key=dict(big="Two dollars a pound", label="Preço por libra", sub="Nos EUA, frutas e legumes costumam ser vendidos por pound (cerca de 454 gramas) ou por caixa."),
 mini=[
  dict(who="Victor", en="Hi! These {apples|oranges|grapes} look good.", pt="Oi! {Essas maçãs|Essas laranjas|Essas uvas} estão boas."),
  dict(who="You", en="They're fresh today. {Two|Three|Four} dollars a pound.", pt="São frescas de hoje. {Dois|Três|Quatro} dólares a libra."),
  dict(who="Victor", en="I'll take {three|two|four} pounds.", pt="Vou levar {três|duas|quatro} libras."),
  dict(who="You", en="Okay. {Anything else?|Is that all?|Would you like anything else?}", pt="Certo. {Mais alguma coisa?|É só isso?|Quer mais alguma coisa?}"),
 ],
 dlg=[
  dict(who="Victor", en="Hi! These {apples|oranges} look good.", pt="Oi! {Essas maçãs|Essas laranjas} estão boas."),
  dict(who="You", en="They're fresh today. {Two|Three} dollars a pound.", pt="São frescas de hoje. {Dois|Três} dólares a libra."),
  dict(who="Victor", en="I'll take {three|two|four} pounds.", pt="Vou levar {três|duas|quatro} libras."),
  dict(who="You", en="Okay. {Anything else?|Is that all?}", pt="Certo. {Mais alguma coisa?|É só isso?}"),
  dict(who="Victor", en="Do you have {strawberries|grapes|oranges}?", pt="Vocês têm {morangos|uvas|laranjas}?"),
  dict(who="You", en="Yes. {Five|Four|Six} dollars a box.", pt="Temos. {Cinco|Quatro|Seis} dólares a caixa."),
  dict(who="Victor", en="{One box|Two boxes}, please.", pt="{Uma caixa|Duas caixas}, por favor."),
  dict(who="You", en="That's {eleven|twelve} dollars.", pt="São {onze|doze} dólares."),
  dict(who="Victor", en="Enjoy your fruit!", pt="Aproveite as frutas!"),
 ],
 vocab=[
  dict(w="apple", pt="maçã", e="🍎", ex=["These apples are sweet.", "I'll take one apple."]),
  dict(w="grapes", pt="uvas", e="🍇", ex=["The grapes are fresh.", "I'd like a pound of grapes."]),
  dict(w="orange", pt="laranja", e="🍊", ex=["An orange is a good snack.", "Do you have oranges today?"]),
  dict(w="strawberry", pt="morango", e="🍓", ex=["This strawberry is red and sweet.", "I like strawberry jam."]),
  dict(w="pound", pt="libra (peso)", e="⚖️", ex=["Two dollars a pound.", "I'll take three pounds."]),
  dict(w="box", pt="caixa", e="📦", ex=["One box of strawberries, please.", "The box is on the table."]),
 ],
 molds=[
  dict(title="Dizer o preço", frame="{fruit} are {price} a pound.", slots=[dict(key="fruit", opts=["Apples", "Oranges", "Grapes"]), dict(key="price", opts=["two dollars", "three dollars", "four dollars"])], model="Apples are two dollars a pound.", note="A pound = por libra. Fruta no plural leva are."),
  dict(title="Fazer o pedido", frame="I'll take {amount} of {fruit}.", slots=[dict(key="amount", opts=["three pounds", "two pounds", "one box"]), dict(key="fruit", opts=["apples", "oranges", "strawberries"])], model="I'll take three pounds of apples.", note="Amount of fruit: three pounds of apples. O of liga a quantidade ao produto."),
  dict(title="Escrever o pedido", frame="Hi! Do you have {fruit}? I'd like {amount}, please.", slots=[dict(key="fruit", opts=["strawberries", "grapes", "oranges"]), dict(key="amount", opts=["one box", "two pounds", "three pounds"])], model="Hi! Do you have strawberries? I'd like one box, please.", note="Do you have...? pergunta se tem. I'd like... pede com educação."),
 ],
 sounds=[
  dict(say="Two dollars a pound.", tag="ritmo: dollars a pound", tip="A fica fraco e ligado: 'dolars-a-pound'. Acentue dollars e pound."),
  dict(say="I'll take three pounds.", tag="ritmo: palavras fortes", tip="Acento em take, three e pounds. I'll é bem curto."),
  dict(say="That's eleven dollars.", tag="ritmo: eleven", tip="Eleven tem acento na segunda sílaba: 'i-LE-ven'. Dollars fecha a frase."),
 ],
 role=dict(turns=[
  dict(npc="Hi! These apples look good.", opts=[
   dict(en="They're fresh today. Two dollars a pound.", pt="São frescas de hoje. Dois dólares a libra.", reply="Great price. They look sweet."),
   dict(en="Yes, they're sweet. Three dollars a pound.", pt="Sim, são doces. Três dólares a libra.", reply="Okay. That's fair."),
   dict(en="Thanks! They're fresh. Two dollars a pound.", pt="Obrigado! São frescas. Dois dólares a libra.", reply="Perfect. I like fresh fruit.")]),
  dict(npc="I'll take three pounds.", opts=[
   dict(en="Okay. Anything else?", pt="Certo. Mais alguma coisa?", reply="Yes. Do you have strawberries?"),
   dict(en="Sure. Is that all?", pt="Claro. É só isso?", reply="Hmm, also strawberries. Do you have any?"),
   dict(en="Great. Would you like anything else?", pt="Ótimo. Quer mais alguma coisa?", reply="Yes, please. Do you have strawberries?")]),
  dict(npc="Do you have strawberries?", opts=[
   dict(en="Yes. Five dollars a box.", pt="Temos. Cinco dólares a caixa.", reply="Perfect. One box, please."),
   dict(en="Yes, they're fresh. Four dollars a box.", pt="Temos, são frescos. Quatro dólares a caixa.", reply="Good. One box, please."),
   dict(en="Yes. Six dollars a box.", pt="Temos. Seis dólares a caixa.", reply="Okay. One box, please.")]),
  dict(npc="One box, please.", opts=[
   dict(en="That's eleven dollars.", pt="São onze dólares.", reply="Here you go. Thanks!"),
   dict(en="Here you go. That's eleven dollars.", pt="Aqui está. São onze dólares.", reply="Thanks! Enjoy the day."),
   dict(en="Sure! Eleven dollars, please.", pt="Claro! Onze dólares, por favor.", reply="Here you go. Thanks!")]),
 ], change=["Os morangos acabaram: ofereça uvas.", "O cliente quer só meia libra: diga o preço.", "O cliente pergunta se a fruta é fresca: responda."]),
 writing=dict(task="Você vende frutas numa barraca. Escreva 2 ou 3 frases: diga o preço de uma fruta por libra e o preço de outra por caixa.", model="The apples are fresh today. They are two dollars a pound. The strawberries are five dollars a box.", kw=["apples", "fresh", "pound", "box"], checks=["Disse um preço por pound.", "Disse um preço por box.", "Usou are com frutas no plural."]),
 scenes=dict(pool=["market", "supermarket", "farm", "street"], npc=dict(g="m", role="customer"), you=dict(g="f")),
 convo=dict(npc=dict(name="Victor"), story="Você vende frutas numa feira nos EUA. Um cliente quer comprar maçãs e morangos.", turns=[
  dict(npc="Hi! These apples look good.", pt="Oi! Essas maçãs estão boas.", opts=[
   dict(en="They're fresh today. Two dollars a pound.", pt="São frescas de hoje. Dois dólares a libra.", ok=True, fb="Responde ao elogio e já informa o preço."),
   dict(en="I'll take three pounds.", pt="Vou levar três libras.", ok=False, fb="Quem compra é o cliente; você é o vendedor."),
   dict(en="Enjoy your fruit!", pt="Aproveite as frutas!", ok=False, fb="É uma despedida, usada no fim da compra.")]),
  dict(npc="I'll take three pounds.", pt="Vou levar três libras.", opts=[
   dict(en="Do you have apples?", pt="Vocês têm maçãs?", ok=False, fb="Você é o vendedor; essa pergunta é do cliente."),
   dict(en="No, thank you.", pt="Não, obrigado.", ok=False, fb="Ele fez um pedido, não uma pergunta de sim ou não."),
   dict(en="Okay. Anything else?", pt="Certo. Mais alguma coisa?", ok=True, fb="Confirma e oferece mais produtos.")]),
  dict(npc="Do you have strawberries?", pt="Vocês têm morangos?", opts=[
   dict(en="Yes. Five dollars a box.", pt="Temos. Cinco dólares a caixa.", ok=True, fb="Responde que tem e diz o preço."),
   dict(en="Strawberries are red.", pt="Morangos são vermelhos.", ok=False, fb="É verdade, mas não responde à pergunta."),
   dict(en="I'll take a box, please.", pt="Vou levar uma caixa, por favor.", ok=False, fb="Você é o vendedor, não o comprador.")]),
  dict(npc="One box, please.", pt="Uma caixa, por favor.", opts=[
   dict(en="Two dollars a pound.", pt="Dois dólares a libra.", ok=False, fb="Esse é o preço das maçãs; ele pediu morangos por caixa."),
   dict(en="Do you have strawberries?", pt="Vocês têm morangos?", ok=False, fb="Já foi respondido; agora diga o total."),
   dict(en="That's eleven dollars.", pt="São onze dólares.", ok=True, fb="Três libras de maçãs a dois dólares é seis, mais cinco: onze.")]),
  dict(npc="Enjoy your fruit!", pt="Aproveite as frutas!", opts=[
   dict(en="Thanks! Come again.", pt="Obrigado! Volte sempre.", ok=True, fb="Despedida típica de quem vende."),
   dict(en="Anything else?", pt="Mais alguma coisa?", ok=False, fb="Ele já está indo embora."),
   dict(en="Hi! Can I help you?", pt="Oi! Posso ajudar?", ok=False, fb="É uma saudação de início de conversa.")]),
 ]),
)
