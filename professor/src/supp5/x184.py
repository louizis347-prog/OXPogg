X = dict(
 key=dict(big="I have a flat tire", label="Pneu furado", sub="Ao pedir ajuda na estrada, diga o problema, se está seguro, onde está e que carro tem. Respostas curtas e claras bastam."),
 mini=[
  dict(who="You", en="Hi. I have a {flat tire.|flat wheel.|problem with my car.}", pt="Oi. Estou com {um pneu furado.|uma roda furada.|um problema no carro.}"),
  dict(who="Luis", en="Are you {safe|okay} right now?", pt="Você está {seguro|bem} agora?"),
  dict(who="You", en="Yes, I'm {on the side of the road.|near an exit.|in a parking lot.}", pt="Sim, estou {no acostamento.|perto de uma saída.|em um estacionamento.}"),
  dict(who="Luis", en="What kind of car do you {have?|drive?}", pt="Que carro você {tem?|dirige?}"),
 ],
 dlg=[
  dict(who="Luis", en="Hello, {roadside assistance.|road help.} How can I help?", pt="Olá, {assistência na estrada.|ajuda na estrada.} Como posso ajudar?"),
  dict(who="You", en="Hi. I have a {flat tire.|flat wheel.}", pt="Oi. Estou com {um pneu furado.|uma roda furada.}"),
  dict(who="Luis", en="Are you {safe|okay} right now?", pt="Você está {seguro|bem} agora?"),
  dict(who="You", en="Yes, I'm on the side of the {road.|highway.}", pt="Sim, estou no acostamento da {estrada.|rodovia.}"),
  dict(who="Luis", en="What's your {location?|address?}", pt="Qual é sua {localização?|localização?}"),
  dict(who="You", en="Highway ten, near exit {five.|six.}", pt="Rodovia dez, perto da saída {cinco.|seis.}"),
  dict(who="Luis", en="What kind of {car|vehicle} do you have?", pt="Que {carro|veículo} você tem?"),
  dict(who="You", en="A {white|black} Honda.", pt="Um Honda {branco.|preto.}"),
  dict(who="Luis", en="Do you have a {spare tire?|spare wheel?}", pt="Você tem {estepe?|roda reserva?}"),
 ],
 vocab=[
  dict(w="road", pt="estrada, rua", e="🛤️", ex=["The road is long.", "I am on the road."]),
  dict(w="wheel", pt="roda", e="🛞", ex=["The wheel is round.", "Check the wheel."]),
  dict(w="slow", pt="devagar, lento", e="🐢", ex=["Drive slow, please.", "The car is slow."]),
  dict(w="tool", pt="ferramenta", e="🔧", ex=["I need a tool.", "The tool is in the trunk."]),
  dict(w="flat", pt="furado, vazio", e="🫧", ex=["The tire is flat.", "I have a flat tire."]),
  dict(w="air", pt="ar", e="💨", ex=["The tire has no air.", "I need air for the tire."]),
 ],
 molds=[
  dict(title="Dizer o problema", frame="Hi. I have a {problem}.", slots=[dict(key="problem", opts=["flat tire", "problem with my car", "problem with the wheel"])], model="Hi. I have a flat tire.", note="I have a + problema. Flat tire = pneu furado."),
  dict(title="Dizer onde está", frame="I'm on {road}, near {place}.", slots=[dict(key="road", opts=["Highway ten", "Main Street", "Route five"]), dict(key="place", opts=["exit five", "the gas station", "the bridge"])], model="I'm on Highway ten, near exit five.", note="Near + lugar mostra onde você está. Não use of depois de near."),
  dict(title="Descrever o carro por escrito", frame="I have a {color} {brand}. It's in the {place}.", slots=[dict(key="color", opts=["white", "black", "red"]), dict(key="brand", opts=["Honda", "Ford", "Toyota"]), dict(key="place", opts=["right lane", "parking lot", "shade"])], model="I have a white Honda. It's in the right lane.", note="A cor vem antes da marca: a white Honda."),
 ],
 sounds=[
  dict(say="I have a flat tire.", tag="ritmo: FLAT TIRE", tip="Acentue flat e tire. Tire soa “taier”, com o ditongo ai."),
  dict(say="What's your location?", tag="acento: loCAtion", tip="O acento fica em CA: lo-CA-tion. O -tion soa “shun”."),
  dict(say="A white Honda.", tag="som: wh em white", tip="Wh soa como w: “uait”. Arredonde os lábios, sem soprar o ar."),
 ],
 role=dict(turns=[
  dict(npc="Hello, roadside assistance. How can I help?", opts=[
   dict(en="Hi. I have a flat tire.", pt="Oi. Estou com um pneu furado.", reply="Are you safe right now?"),
   dict(en="Hello. My tire is flat.", pt="Olá. Meu pneu está furado.", reply="Are you safe right now?"),
   dict(en="Hi. I need help with my car.", pt="Oi. Preciso de ajuda com meu carro.", reply="What's the problem?")]),
  dict(npc="Are you safe right now?", opts=[
   dict(en="Yes, I'm on the side of the road.", pt="Sim, estou no acostamento.", reply="Good. What's your location?"),
   dict(en="Yes, I'm in a parking lot.", pt="Sim, estou em um estacionamento.", reply="Good. What's your location?"),
   dict(en="Yes, I'm near an exit.", pt="Sim, estou perto de uma saída.", reply="Good. What's your location?")]),
  dict(npc="What's your location?", opts=[
   dict(en="Highway ten, near exit five.", pt="Rodovia dez, perto da saída cinco.", reply="What kind of car do you have?"),
   dict(en="Main Street, near the bridge.", pt="Rua Main, perto da ponte.", reply="What kind of car do you have?"),
   dict(en="Route five, near the gas station.", pt="Rota cinco, perto do posto.", reply="What kind of car do you have?")]),
  dict(npc="What kind of car do you have?", opts=[
   dict(en="A white Honda.", pt="Um Honda branco.", reply="Do you have a spare tire?"),
   dict(en="A black Toyota.", pt="Um Toyota preto.", reply="Do you have a spare tire?"),
   dict(en="A red Ford.", pt="Um Ford vermelho.", reply="Do you have a spare tire?")]),
 ], change=["Você não tem estepe: diga que não tem e peça reboque.", "Você não sabe a saída: diga a placa mais próxima que vê.", "Você está no meio da pista: peça ajuda e diga que vai para o acostamento."]),
 writing=dict(task="Escreva 2 ou 3 frases: diga que está com pneu furado, onde está e que carro tem.", model="I have a flat tire. I'm on Highway ten, near exit five. I have a white Honda.", kw=["flat", "tire", "highway", "honda"], checks=["Disse o problema.", "Disse onde está.", "Disse o carro."]),
 scenes=dict(pool=["street", "nyc", "nightcity", "pier"], npc=dict(g="m", role="operator"), you=dict(g="m")),
 convo=dict(npc=dict(name="Luis"), story="Você está de carro perto de Tulsa e o pneu furou. Você liga para a assistência na estrada e o Luis atende.", turns=[
  dict(npc="Hello, roadside assistance. How can I help?", pt="Olá, assistência na estrada. Como posso ajudar?", opts=[
   dict(en="Hi. I have a flat tire.", pt="Oi. Estou com um pneu furado.", ok=True, fb="Diz o problema com clareza."),
   dict(en="A white Honda.", pt="Um Honda branco.", ok=False, fb="Ainda não perguntaram o carro."),
   dict(en="Highway ten, near exit five.", pt="Rodovia dez, perto da saída cinco.", ok=False, fb="Primeiro diga o problema.")]),
  dict(npc="Are you safe right now?", pt="Você está seguro agora?", opts=[
   dict(en="A white Honda.", pt="Um Honda branco.", ok=False, fb="Não responde à pergunta."),
   dict(en="Yes, I'm on the side of the road.", pt="Sim, estou no acostamento.", ok=True, fb="Diz que está em lugar seguro."),
   dict(en="What's your location?", pt="Qual é sua localização?", ok=False, fb="Essa pergunta é do Luis.")]),
  dict(npc="What's your location?", pt="Qual é sua localização?", opts=[
   dict(en="Highway ten, near exit five.", pt="Rodovia dez, perto da saída cinco.", ok=True, fb="Dá o lugar com clareza."),
   dict(en="I have a flat tire.", pt="Estou com pneu furado.", ok=False, fb="Você já disse isso."),
   dict(en="Do you have a spare tire?", pt="Você tem estepe?", ok=False, fb="Essa pergunta é do Luis.")]),
  dict(npc="What kind of car do you have?", pt="Que carro você tem?", opts=[
   dict(en="Yes, I'm safe.", pt="Sim, estou seguro.", ok=False, fb="Isso já foi respondido."),
   dict(en="Highway ten.", pt="Rodovia dez.", ok=False, fb="Isso é o lugar, não o carro."),
   dict(en="A white Honda.", pt="Um Honda branco.", ok=True, fb="Cor e marca bastam.")]),
  dict(npc="Do you have a spare tire?", pt="Você tem estepe?", opts=[
   dict(en="Yes, I do. It's in the trunk.", pt="Sim, tenho. Está no porta-malas.", ok=True, fb="Responde e dá o lugar."),
   dict(en="Hello, roadside assistance.", pt="Olá, assistência na estrada.", ok=False, fb="Essa frase é do atendente."),
   dict(en="I have a flat tire.", pt="Estou com pneu furado.", ok=False, fb="Você já disse isso.")]),
 ]),
)
