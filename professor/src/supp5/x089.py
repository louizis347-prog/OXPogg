"""Bloco extra da aula 89: acampar."""
X = dict(
 key=dict(big="Where should we put the tent?", label="Escolher o lugar", sub="Pergunte onde montar a barraca, diga o que falta e onde estão as coisas. Should serve para pedir uma sugestão."),
 mini=[
  dict(who="Jonah", en="Where should we put the {tent|fire|bags}?", pt="Onde devemos pôr {a barraca|a fogueira|as mochilas}?"),
  dict(who="You", en="{Over there|Near the trees|Next to the lake}.", pt="{Ali|Perto das árvores|Ao lado do lago}."),
  dict(who="Jonah", en="Is the ground {flat|dry|soft}?", pt="O chão é {plano|seco|macio}?"),
  dict(who="You", en="Yes. Let's {build a fire|cook dinner|put up the tent}.", pt="Sim. Vamos {fazer uma fogueira|preparar o jantar|montar a barraca}."),
 ],
 dlg=[
  dict(who="Jonah", en="Where should we put the {tent?|fire?}", pt="Onde devemos pôr {a barraca?|a fogueira?}"),
  dict(who="You", en="Over there, near the {trees.|lake.}", pt="Ali, perto {das árvores.|do lago.}"),
  dict(who="Jonah", en="Good. Is the ground {flat?|dry?}", pt="Bom. O chão é {plano?|seco?}"),
  dict(who="You", en="Yes. Let's build a {fire.|camp.}", pt="Sim. Vamos {fazer uma fogueira.|montar o acampamento.}"),
  dict(who="Jonah", en="We need {wood.|water.}", pt="Precisamos de {lenha.|água.}"),
  dict(who="You", en="I'll get some. Where is the {flashlight?|backpack?}", pt="Eu pego. Onde está {a lanterna?|a mochila?}"),
  dict(who="Jonah", en="It's in my {backpack.|bag.}", pt="Está na minha {mochila.|bolsa.}"),
  dict(who="You", en="Thanks. It's getting {dark.|cold.}", pt="Valeu. Está {escurecendo.|esfriando.}"),
  dict(who="Jonah", en="Sleep well in the {tent!|woods!}", pt="Durma bem na {barraca!|floresta!}"),
 ],
 vocab=[
  dict(w="tent", pt="barraca", e="⛺", ex=["The tent is small.", "We put up the tent here."]),
  dict(w="campfire", pt="fogueira", e="🔥", ex=["The campfire is warm.", "We cook on the campfire."]),
  dict(w="flashlight", pt="lanterna", e="🔦", ex=["Where is the flashlight?", "My flashlight is bright."]),
  dict(w="backpack", pt="mochila", e="🎒", ex=["It's in my backpack.", "The backpack is heavy."]),
  dict(w="firewood", pt="lenha", e="🪵", ex=["We need firewood.", "I carry the firewood."]),
  dict(w="sleeping bag", pt="saco de dormir", e="🛌", ex=["My sleeping bag is warm.", "Put the sleeping bag in the tent."]),
 ],
 molds=[
  dict(title="Perguntar onde pôr", frame="Where should we put the {thing}?", slots=[dict(key="thing", opts=["tent", "bags", "flashlight", "food"])], model="Where should we put the tent?", note="Where should we put…? pede uma sugestão. Should vem antes de we."),
  dict(title="Dizer onde está", frame="It's {place}.", slots=[dict(key="place", opts=["in my backpack", "near the trees", "under the tree", "next to the tent"])], model="It's in my backpack.", note="It's + lugar. Use in, near, under, next to."),
  dict(title="Escrever uma lista", frame="Pack a {thing1}, a {thing2} and {thing3}. We need them tonight.", slots=[dict(key="thing1", opts=["tent", "sleeping bag", "flashlight"]), dict(key="thing2", opts=["flashlight", "backpack", "jacket"]), dict(key="thing3", opts=["water", "food", "firewood"])], model="Pack a tent, a flashlight and water. We need them tonight.", note="Pack + coisas é uma lista curta. Them = eles/elas."),
 ],
 sounds=[
  dict(say="Where should we put the tent?", tag="ritmo: WHERE should we PUT the TENT", tip="Acentue WHERE, PUT e TENT. 'should we' fica fraco: 'shuh-wee'."),
  dict(say="I'll get some.", tag="ligação: get some", tip="Una get e some: 'getsom'. O t some quase todo."),
  dict(say="It's getting dark.", tag="t entre vogais: getting", tip="Em inglês americano, 'getting' soa como 'geding'. Acentue GET e DARK."),
 ],
 role=dict(turns=[
  dict(npc="Where should we put the tent?", opts=[
   dict(en="Over there, near the trees.", pt="Ali, perto das árvores.", reply="Good. Is the ground flat?"),
   dict(en="Next to the lake.", pt="Ao lado do lago.", reply="Good. Is the ground flat?"),
   dict(en="Under that big tree.", pt="Debaixo daquela árvore grande.", reply="Good. Is the ground flat?")]),
  dict(npc="Is the ground flat?", opts=[
   dict(en="Yes. Let's build a fire.", pt="Sim. Vamos fazer uma fogueira.", reply="We need wood."),
   dict(en="Yes, it's flat and dry.", pt="Sim, é plano e seco.", reply="Great. We need wood for the fire."),
   dict(en="Yes. Let's put up the tent.", pt="Sim. Vamos montar a barraca.", reply="OK. And we need wood.")]),
  dict(npc="We need wood.", opts=[
   dict(en="I'll get some. Where is the flashlight?", pt="Eu pego. Onde está a lanterna?", reply="It's in my backpack."),
   dict(en="I'll get some. Where is my jacket?", pt="Eu pego. Onde está meu casaco?", reply="It's in my backpack."),
   dict(en="I'll get some. Can I use the flashlight?", pt="Eu pego. Posso usar a lanterna?", reply="Sure. It's in my backpack.")]),
  dict(npc="It's in my backpack.", opts=[
   dict(en="Thanks. It's getting dark.", pt="Valeu. Está escurecendo.", reply="Sleep well in the tent!"),
   dict(en="Thanks. It's getting cold.", pt="Valeu. Está esfriando.", reply="Sleep well in the tent!"),
   dict(en="Thanks. Look at the stars!", pt="Valeu. Olha as estrelas!", reply="Wow! Sleep well in the tent!")]),
 ], change=["A barraca não fica em pé: peça ajuda ao Jonah.", "A lanterna não acende: diga que precisa de pilhas novas.", "Começa a chover: sugira entrar na barraca."]),
 writing=dict(task="Escreva 2 ou 3 frases para um amigo: diga o que levar para acampar (barraca, lanterna e água) e que vocês precisam deles à noite.", model="Hi Jonah! Pack a tent, a flashlight and water. We need them tonight.", kw=["pack", "tent", "flashlight", "need"], checks=["Listou o que levar.", "Usou Pack ou Bring.", "Disse que precisam à noite."]),
 scenes=dict(pool=["forest", "mountain", "lake", "park2"], npc=dict(g="m", role="friend"), you=dict(g="f")),
 convo=dict(npc=dict(name="Jonah"), story="Você chega a um camping com seu amigo Jonah.", turns=[
  dict(npc="Where should we put the tent?", pt="Onde devemos montar a barraca?", opts=[
   dict(en="Sleep well in the tent!", pt="Durma bem na barraca!", ok=False, fb="É despedida; vocês nem montaram a barraca."),
   dict(en="Over there, near the trees.", pt="Ali, perto das árvores.", ok=True, fb="Responde onde."),
   dict(en="It's in my backpack.", pt="Está na minha mochila.", ok=False, fb="Ele pergunta onde pôr a barraca, não onde algo está.")]),
  dict(npc="Good. Is the ground flat?", pt="Bom. O chão é plano?", opts=[
   dict(en="Yes. Let's build a fire.", pt="Sim. Vamos fazer uma fogueira.", ok=True, fb="Responde e dá o próximo passo."),
   dict(en="Where should we put the tent?", pt="Onde devemos montar a barraca?", ok=False, fb="Já foi resolvido."),
   dict(en="We need wood.", pt="Precisamos de lenha.", ok=False, fb="É a fala dele; primeiro responda.")]),
  dict(npc="We need wood.", pt="Precisamos de lenha.", opts=[
   dict(en="Is the ground flat?", pt="O chão é plano?", ok=False, fb="Ele já perguntou isso."),
   dict(en="I'll get some. Where is the flashlight?", pt="Eu pego. Onde está a lanterna?", ok=True, fb="Oferece ajuda e pergunta."),
   dict(en="Sleep well!", pt="Durma bem!", ok=False, fb="Ainda é cedo.")]),
  dict(npc="It's in my backpack.", pt="Está na minha mochila.", opts=[
   dict(en="We need wood.", pt="Precisamos de lenha.", ok=False, fb="Você já vai buscar."),
   dict(en="Over there, near the trees.", pt="Ali, perto das árvores.", ok=False, fb="Não é sobre onde pôr algo."),
   dict(en="Thanks. It's getting dark.", pt="Valeu. Está escurecendo.", ok=True, fb="Agradece e explica o motivo.")]),
  dict(npc="Sleep well in the tent!", pt="Durma bem na barraca!", opts=[
   dict(en="Thanks! You too!", pt="Obrigado! Você também!", ok=True, fb="Resposta natural."),
   dict(en="Where is the flashlight?", pt="Onde está a lanterna?", ok=False, fb="Já foi respondido."),
   dict(en="Let's build a fire.", pt="Vamos fazer uma fogueira.", ok=False, fb="Já é hora de dormir.")]),
 ]),
)
