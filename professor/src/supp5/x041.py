X = dict(
 key=dict(big="Cut the onions, please", label="Pedir ajuda na cozinha", sub="Na receita, usamos o imperativo: Cut, Add, Stir. Com please e um tom simples, o pedido soa educado."),
 mini=[
  dict(who="Aaron", en="What are you {making|cooking|making for dinner}?", pt="O que você está {fazendo|cozinhando|fazendo para o jantar}?"),
  dict(who="You", en="{Pasta|Soup|Rice} with tomato sauce.", pt="{Massa|Sopa|Arroz} com molho de tomate."),
  dict(who="Aaron", en="Can I help? {Sure.|Yes.|Of course.}", pt="Posso ajudar? {Claro.|Sim.|Com certeza.}"),
  dict(who="You", en="{Cut|Wash|Chop} the onions, please.", pt="{Corte|Lave|Pique} as cebolas, por favor."),
 ],
 dlg=[
  dict(who="Aaron", en="What are you {making|cooking}?", pt="O que você está {fazendo|cozinhando}?"),
  dict(who="You", en="{Pasta|Soup} with tomato sauce.", pt="{Massa|Sopa} com molho de tomate."),
  dict(who="Aaron", en="Can I {help?|do something?}", pt="Posso {ajudar?|fazer algo?}"),
  dict(who="You", en="Sure. {Cut|Wash} the onions, please.", pt="Claro. {Corte|Lave} as cebolas, por favor."),
  dict(who="Aaron", en="How {many?|many onions?}", pt="{Quantas?|Quantas cebolas?}"),
  dict(who="You", en="Just {one|two}. Then add the {tomatoes|carrots}.", pt="Só {uma|duas}. Depois adicione os {tomates|cenouras}."),
  dict(who="Aaron", en="OK. Is it {hot?|ready?}", pt="Ok. Está {quente?|pronto?}"),
  dict(who="You", en="Careful! The {pan|pot} is hot.", pt="Cuidado! A {panela|panela} está quente."),
  dict(who="Aaron", en="Dinner is served!", pt="O jantar está servido!"),
 ],
 vocab=[
  dict(w="cook", pt="cozinhar", e="👩‍🍳", ex=["I like to cook at home.", "Can you cook pasta?"]),
  dict(w="salt", pt="sal", e="🧂", ex=["Add a little salt.", "Pass the salt, please."]),
  dict(w="pan", pt="panela, frigideira", e="🍳", ex=["The pan is hot.", "Put the onions in the pan."]),
  dict(w="onion", pt="cebola", e="🧅", ex=["Cut the onion, please.", "One onion is enough."]),
  dict(w="knife", pt="faca", e="🔪", ex=["Be careful with the knife.", "The knife is sharp."]),
  dict(w="tomato", pt="tomate", e="🍅", ex=["Add the tomato to the sauce.", "This tomato is red and fresh."]),
 ],
 molds=[
  dict(title="Pedir uma tarefa", frame="{verb} the {food}, please.", slots=[dict(key="verb", opts=["Cut", "Wash", "Chop"]), dict(key="food", opts=["onions", "tomatoes", "carrots"])], model="Cut the onions, please.", note="Verbo no imperativo + the + ingrediente + please. Cut, wash e chop funcionam com legumes."),
  dict(title="Dar o próximo passo", frame="Then add the {food} to the {tool}.", slots=[dict(key="food", opts=["tomatoes", "onions", "salt"]), dict(key="tool", opts=["pan", "pot", "bowl"])], model="Then add the tomatoes to the pan.", note="Then = depois. Add ... to ... = adicione ... a ..."),
  dict(title="Escrever um aviso", frame="Careful! The {thing} is {adj}.", slots=[dict(key="thing", opts=["pan", "pot", "knife"]), dict(key="adj", opts=["hot", "very hot", "sharp"])], model="Careful! The pan is hot.", note="Careful! chama atenção para o perigo. Hot = quente; sharp = afiado."),
 ],
 sounds=[
  dict(say="What are you making?", tag="redução: what are you", tip="What are you vira 'wha-dr-ya': 'Whaddaya making?'. Acentue MAK-ing."),
  dict(say="Cut the onions, please.", tag="ritmo: cut / onions", tip="Acentue CUT, ON-ions e PLEASE. The fica curtinho."),
  dict(say="Careful! The pan is hot.", tag="acento: CARE-ful", tip="O acento de careful é na primeira sílaba: 'CARE-ful'. Hot recebe força."),
 ],
 role=dict(turns=[
  dict(npc="What are you making?", opts=[
   dict(en="Pasta with tomato sauce.", pt="Massa com molho de tomate.", reply="Mmm, that sounds good."),
   dict(en="Soup with vegetables.", pt="Sopa com legumes.", reply="Nice! I love soup."),
   dict(en="Rice with tomato sauce.", pt="Arroz com molho de tomate.", reply="Great! I'm hungry.")]),
  dict(npc="Can I help?", opts=[
   dict(en="Sure. Cut the onions, please.", pt="Claro. Corte as cebolas, por favor.", reply="Sure. How many?"),
   dict(en="Yes! Wash the tomatoes, please.", pt="Sim! Lave os tomates, por favor.", reply="Okay. How many?"),
   dict(en="Of course. Chop the carrots, please.", pt="Com certeza. Pique as cenouras, por favor.", reply="Okay. How many?")]),
  dict(npc="How many?", opts=[
   dict(en="Just one. Then add the tomatoes.", pt="Só uma. Depois adicione os tomates.", reply="OK. Is it hot?"),
   dict(en="Two, please. Then add them to the pan.", pt="Duas, por favor. Depois ponha na panela.", reply="OK. Is the pan hot?"),
   dict(en="Just one is enough.", pt="Só uma basta.", reply="OK. Is it hot?")]),
  dict(npc="OK. Is it hot?", opts=[
   dict(en="Careful! The pan is hot.", pt="Cuidado! A panela está quente.", reply="Thanks! I'll be careful."),
   dict(en="Yes, it is. Be careful!", pt="Sim, está. Cuidado!", reply="Okay. I'll use a towel."),
   dict(en="Yes! Careful with the pan.", pt="Sim! Cuidado com a panela.", reply="Got it. Dinner smells great!")]),
 ], change=["Falta sal: peça para ele passar o sal.", "Você corta o dedo de leve: peça um curativo.", "O molho está muito forte: pergunte se ele quer experimentar."]),
 writing=dict(task="Você ensina uma receita simples a um amigo. Escreva 2 ou 3 frases com ordens: corte um ingrediente, adicione outro e avise que a panela está quente.", model="Cut the onions, please. Then add the tomatoes to the pan. Careful! The pan is hot.", kw=["cut", "onions", "add", "pan"], checks=["Usou um verbo de ordem (cut, add...).", "Citou ingredientes.", "Avisou do perigo com Careful."]),
 scenes=dict(pool=["kitchen", "home1", "living", "chefkitchen"], npc=dict(g="m", role="friend"), you=dict(g="f")),
 convo=dict(npc=dict(name="Aaron"), story="Você está cozinhando em casa e um amigo quer ajudar.", turns=[
  dict(npc="What are you making?", pt="O que você está fazendo?", opts=[
   dict(en="Pasta with tomato sauce.", pt="Massa com molho de tomate.", ok=True, fb="Diz o prato com clareza."),
   dict(en="I'm making now.", pt="Estou fazendo agora.", ok=False, fb="Falta dizer o que está fazendo."),
   dict(en="Dinner is served!", pt="O jantar está servido!", ok=False, fb="Só se diz quando a comida está pronta.")]),
  dict(npc="Can I help?", pt="Posso ajudar?", opts=[
   dict(en="Careful! The pan is hot.", pt="Cuidado! A panela está quente.", ok=False, fb="É um aviso útil, mas ele ofereceu ajuda: dê uma tarefa."),
   dict(en="Yes, you are my friend.", pt="Sim, você é meu amigo.", ok=False, fb="Não responde ao pedido de ajuda."),
   dict(en="Sure. Cut the onions, please.", pt="Claro. Corte as cebolas, por favor.", ok=True, fb="Aceita e pede uma tarefa com educação.")]),
  dict(npc="How many?", pt="Quantas?", opts=[
   dict(en="Just one. Then add the tomatoes.", pt="Só uma. Depois adicione os tomates.", ok=True, fb="Diz a quantidade e o passo seguinte."),
   dict(en="Cut the onions, please.", pt="Corte as cebolas, por favor.", ok=False, fb="Você já pediu isso; ele quer saber a quantidade."),
   dict(en="Pasta with tomato sauce.", pt="Massa com molho de tomate.", ok=False, fb="Isso já foi dito; responda a quantidade.")]),
  dict(npc="OK. Is it hot?", pt="Ok. Está quente?", opts=[
   dict(en="No, it's a knife.", pt="Não, é uma faca.", ok=False, fb="Ele pergunta da panela; sua frase não faz sentido."),
   dict(en="How many?", pt="Quantas?", ok=False, fb="Esta pergunta é dele, e já foi respondida."),
   dict(en="Careful! The pan is hot.", pt="Cuidado! A panela está quente.", ok=True, fb="Responde e avisa do perigo.")]),
  dict(npc="Dinner is served!", pt="O jantar está servido!", opts=[
   dict(en="Thanks, Aaron! Let's eat.", pt="Obrigada, Aaron! Vamos comer.", ok=True, fb="Resposta natural à refeição pronta."),
   dict(en="What are you making?", pt="O que você está fazendo?", ok=False, fb="O jantar já está pronto; a pergunta ficou para trás."),
   dict(en="Cut the onions, please.", pt="Corte as cebolas, por favor.", ok=False, fb="O cozimento acabou.")]),
 ]),
)
