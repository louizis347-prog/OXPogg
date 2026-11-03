X = dict(
 key=dict(big="In a cup or a cone?", label="Copo ou casquinha", sub="Na sorveteria você escolhe o sabor (flavor), quantas bolas (scoops) e se vai no copo ou na casquinha."),
 mini=[
  dict(who="Tiana", en="Hi! What flavor do you {want|like|need}?", pt="Oi! Que sabor você {quer|gosta|prefere}?"),
  dict(who="You", en="{Chocolate|Vanilla|Strawberry}, please.", pt="{Chocolate|Baunilha|Morango}, por favor."),
  dict(who="Tiana", en="{One scoop or two?|Do you want one scoop or two?|One or two scoops?}", pt="{Uma bola ou duas?|Quer uma bola ou duas?|Uma ou duas bolas?}"),
  dict(who="You", en="{Two scoops|One scoop|Three scoops}, please.", pt="{Duas bolas|Uma bola|Três bolas}, por favor."),
 ],
 dlg=[
  dict(who="Tiana", en="Hi! What flavor do you {want|like}?", pt="Oi! Que sabor você {quer|prefere}?"),
  dict(who="You", en="{Chocolate|Vanilla|Strawberry}, please.", pt="{Chocolate|Baunilha|Morango}, por favor."),
  dict(who="Tiana", en="{One scoop or two?|One or two scoops?}", pt="{Uma bola ou duas?|Uma ou duas bolas?}"),
  dict(who="You", en="{Two scoops|One scoop}. And {strawberry|vanilla}.", pt="{Duas bolas|Uma bola}. E {morango|baunilha}."),
  dict(who="Tiana", en="In a {cup or a cone?|cone or a cup?}", pt="No {copo ou na casquinha?|casquinha ou no copo?}"),
  dict(who="You", en="A {cone|cup}, please.", pt="{Na casquinha|No copo}, por favor."),
  dict(who="Tiana", en="That's {four|five} dollars.", pt="São {quatro|cinco} dólares."),
  dict(who="You", en="Here you go. {Thanks!|Thank you!}", pt="Aqui está. {Valeu!|Obrigado!}"),
  dict(who="Tiana", en="Enjoy your ice cream!", pt="Aproveite o sorvete!"),
 ],
 vocab=[
  dict(w="flavor", pt="sabor", e="😋", ex=["What flavor do you want?", "My favorite flavor is vanilla."]),
  dict(w="chocolate", pt="chocolate", e="🍫", ex=["Chocolate, please.", "I love chocolate ice cream."]),
  dict(w="vanilla", pt="baunilha", e="🍨", ex=["One scoop of vanilla, please.", "Vanilla is a classic flavor."]),
  dict(w="cone", pt="casquinha", e="🍦", ex=["A cone, please.", "The cone is crunchy."]),
  dict(w="scoop", pt="bola (de sorvete)", e="🥄", ex=["One scoop of chocolate, please.", "Two scoops, please."]),
  dict(w="cup", pt="copo", e="🥤", ex=["In a cup, please.", "The cup is small."]),
 ],
 molds=[
  dict(title="Escolher o sabor", frame="{flavor}, please.", slots=[dict(key="flavor", opts=["Chocolate", "Vanilla", "Strawberry", "Mint"])], model="Chocolate, please.", note="Basta dizer o sabor e please. Mint = hortelã."),
  dict(title="Escolher bolas e recipiente", frame="{scoops}, in {container}, please.", slots=[dict(key="scoops", opts=["One scoop", "Two scoops", "Three scoops"]), dict(key="container", opts=["a cone", "a cup", "a waffle cone"])], model="One scoop, in a cone, please.", note="Scoop é a bola de sorvete. Uma bola = one scoop; mais de uma, scoops."),
  dict(title="Escrever o pedido", frame="Hi! I'd like {scoops} of {flavor}, in a cone, please.", slots=[dict(key="scoops", opts=["one scoop", "two scoops", "three scoops"]), dict(key="flavor", opts=["chocolate", "vanilla", "strawberry"])], model="Hi! I'd like one scoop of chocolate, in a cone, please.", note="I'd like... of... é um pedido completo e educado."),
 ],
 sounds=[
  dict(say="What flavor do you want?", tag="redução: do you", tip="Do you vira 'dyu' ou 'dja': 'What flavor djuwant'. Fale rápido e leve."),
  dict(say="One scoop or two?", tag="redução: or", tip="Or fica fraco, quase 'er'. Acentue one, scoop e two."),
  dict(say="In a cup or a cone?", tag="redução: or", tip="Or vira 'er' e a se liga a cup: 'in-a-cup-er-a-cone'."),
 ],
 role=dict(turns=[
  dict(npc="Hi! What flavor do you want?", opts=[
   dict(en="Chocolate, please.", pt="Chocolate, por favor.", reply="Chocolate. One scoop or two?"),
   dict(en="Vanilla, please.", pt="Baunilha, por favor.", reply="Vanilla. One scoop or two?"),
   dict(en="Strawberry, please.", pt="Morango, por favor.", reply="Strawberry. One scoop or two?")]),
  dict(npc="One scoop or two?", opts=[
   dict(en="Two scoops. And strawberry.", pt="Duas bolas. E morango.", reply="Chocolate and strawberry. Good mix!"),
   dict(en="One scoop, please.", pt="Uma bola, por favor.", reply="One scoop. Small and sweet."),
   dict(en="Two scoops of the same flavor, please.", pt="Duas bolas do mesmo sabor, por favor.", reply="Two scoops of the same flavor. Sure!")]),
  dict(npc="In a cup or a cone?", opts=[
   dict(en="A cone, please.", pt="Na casquinha, por favor.", reply="A cone. Here you go."),
   dict(en="In a cup, please.", pt="No copo, por favor.", reply="In a cup. Here is a spoon."),
   dict(en="A cone, thanks.", pt="Na casquinha, valeu.", reply="One cone, coming up.")]),
  dict(npc="That's four dollars.", opts=[
   dict(en="Here you go. Thanks!", pt="Aqui está. Valeu!", reply="Thank you! Enjoy your ice cream!"),
   dict(en="Can I pay by card?", pt="Posso pagar com cartão?", reply="Sure! Card is fine. Enjoy your ice cream!"),
   dict(en="Here's five dollars.", pt="Aqui estão cinco dólares.", reply="Thanks! Here's your change. Enjoy your ice cream!")]),
 ], change=["A sorveteria acabou o sabor que você quer: escolha outro.", "Seu amigo quer provar: peça para experimentar.", "Está calor e você quer um sorvete grande: peça o tamanho."]),
 writing=dict(task="Você está numa sorveteria no parque. Escreva 2 ou 3 frases: diga os sabores, o número de bolas e se quer copo ou casquinha.", model="Hi! Two scoops, please. Chocolate and strawberry. In a cone, please. Thank you!", kw=["scoops", "chocolate", "strawberry", "cone"], checks=["Disse o número de bolas.", "Disse os sabores.", "Escolheu copo ou casquinha."]),
 scenes=dict(pool=["park", "park2", "fair", "street", "playground"], npc=dict(g="f", role="vendor"), you=dict(g="m")),
 convo=dict(npc=dict(name="Tiana"), story="Você está numa sorveteria num parque. Escolha o sabor, as bolas e a casquinha.", turns=[
  dict(npc="Hi! What flavor do you want?", pt="Oi! Que sabor você quer?", opts=[
   dict(en="Chocolate, please.", pt="Chocolate, por favor.", ok=True, fb="Resposta direta: o sabor."),
   dict(en="I'm a scoop.", pt="Eu sou uma bola.", ok=False, fb="Sem sentido; diga o sabor desejado."),
   dict(en="A cone, please.", pt="Uma casquinha, por favor.", ok=False, fb="Ela perguntou o sabor; a casquinha vem depois.")]),
  dict(npc="One scoop or two?", pt="Uma bola ou duas?", opts=[
   dict(en="Yes, thank you.", pt="Sim, obrigado.", ok=False, fb="É pergunta de escolha: diga uma ou duas."),
   dict(en="Chocolate, please.", pt="Chocolate, por favor.", ok=False, fb="O sabor já foi dito; agora é o número de bolas."),
   dict(en="Two scoops. And strawberry.", pt="Duas bolas. E morango.", ok=True, fb="Responde o número e acrescenta o segundo sabor.")]),
  dict(npc="In a cup or a cone?", pt="No copo ou na casquinha?", opts=[
   dict(en="A cone, please.", pt="Na casquinha, por favor.", ok=True, fb="Escolhe a casquinha."),
   dict(en="Two scoops, please.", pt="Duas bolas, por favor.", ok=False, fb="O número de bolas já foi escolhido."),
   dict(en="Here you go.", pt="Aqui está.", ok=False, fb="Você diz isso ao pagar, não ao escolher.")]),
  dict(npc="That's four dollars.", pt="São quatro dólares.", opts=[
   dict(en="Enjoy your ice cream!", pt="Aproveite o sorvete!", ok=False, fb="Essa frase é dita pelo vendedor."),
   dict(en="Here you go. Thanks!", pt="Aqui está. Valeu!", ok=True, fb="Você paga e agradece."),
   dict(en="What flavor do you want?", pt="Que sabor você quer?", ok=False, fb="Já escolheu o sabor; agora é hora de pagar.")]),
  dict(npc="Enjoy your ice cream!", pt="Aproveite o sorvete!", opts=[
   dict(en="Thank you! Bye!", pt="Obrigado! Tchau!", ok=True, fb="Despedida simples e simpática."),
   dict(en="Chocolate, please.", pt="Chocolate, por favor.", ok=False, fb="O pedido já terminou."),
   dict(en="One scoop or two?", pt="Uma bola ou duas?", ok=False, fb="Essa pergunta é do vendedor.")]),
 ]),
)
