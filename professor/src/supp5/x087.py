"""Bloco extra da aula 87: piquenique no parque."""
X = dict(
 key=dict(big="Let's sit under that tree", label="Propor um lugar", sub="Diga o que você trouxe, sugira onde sentar e convide para comer. Let's + verbo é o jeito simples de convidar."),
 mini=[
  dict(who="Ravi", en="Did you bring a {blanket|cooler|bag}?", pt="Você trouxe {um cobertor|uma caixa térmica|uma bolsa}?"),
  dict(who="You", en="Yes. I have {sandwiches|fruit|water}.", pt="Sim. Tenho {sanduíches|frutas|água}."),
  dict(who="Ravi", en="Let's sit {under that tree|on the grass|near the lake}.", pt="Vamos sentar {debaixo daquela árvore|na grama|perto do lago}."),
  dict(who="You", en="Good idea. It's {shady|quiet|nice} there.", pt="Boa ideia. Lá é {com sombra|tranquilo|agradável}."),
 ],
 dlg=[
  dict(who="Ravi", en="It's a beautiful day for a {picnic!|walk!}", pt="É um lindo dia para um {piquenique!|passeio!}"),
  dict(who="You", en="Yes! Did you bring a {blanket?|cooler?}", pt="Sim! Você trouxe {cobertor?|uma caixa térmica?}"),
  dict(who="Ravi", en="I did. And you, what's in your {bag?|cooler?}", pt="Trouxe. E você, o que tem na sua {bolsa?|caixa térmica?}"),
  dict(who="You", en="{Sandwiches,|Cheese,} fruit and juice.", pt="{Sanduíches,|Queijo,} frutas e suco."),
  dict(who="Ravi", en="Great! I have {chips|crackers} and cookies.", pt="Ótimo! Tenho {salgadinhos|biscoitos salgados} e biscoitos."),
  dict(who="You", en="Let's sit under that {tree.|bench.}", pt="Vamos sentar debaixo daquela {árvore.|daquele banco.}"),
  dict(who="Ravi", en="Good idea. It's {shady.|cool.}", pt="Boa ideia. Tem {sombra.|fresquinho.}"),
  dict(who="You", en="Let's {eat!|start!}", pt="Vamos {comer!|começar!}"),
  dict(who="Ravi", en="Have a great {picnic!|day!}", pt="Tenha um ótimo {piquenique!|dia!}"),
 ],
 vocab=[
  dict(w="picnic", pt="piquenique", e="🧺", ex=["We have a picnic on Saturday.", "The picnic is by the lake."]),
  dict(w="grass", pt="grama", e="🌱", ex=["The grass is soft.", "We sit on the grass."]),
  dict(w="chips", pt="salgadinhos", e="🥔", ex=["I have chips and cookies.", "These chips are salty."]),
  dict(w="shade", pt="sombra", e="🌳", ex=["There is shade here.", "Let's sit in the shade."]),
  dict(w="fruit", pt="fruta", e="🍓", ex=["I have fruit in my bag.", "The fruit is fresh."]),
  dict(w="cooler", pt="caixa térmica", e="🧊", ex=["The cooler is cold.", "My juice is in the cooler."]),
 ],
 molds=[
  dict(title="Dizer o que você trouxe", frame="I have {food} and {drink}.", slots=[dict(key="food", opts=["sandwiches", "fruit", "chips"]), dict(key="drink", opts=["juice", "water", "lemonade"])], model="I have sandwiches and juice.", note="I have + comida and bebida. Para mais de um item, use and."),
  dict(title="Sugerir um lugar", frame="Let's sit {place}.", slots=[dict(key="place", opts=["under that tree", "on the grass", "near the lake", "in the shade"])], model="Let's sit under that tree.", note="Let's + verbo base, sem to. Sit = sentar."),
  dict(title="Escrever um convite", frame="Hi! Let's have a picnic on {day}. I have {food}. Can you bring {thing}?", slots=[dict(key="day", opts=["Saturday", "Sunday", "Friday"]), dict(key="food", opts=["sandwiches", "fruit", "cookies"]), dict(key="thing", opts=["juice", "chips", "a blanket"])], model="Hi! Let's have a picnic on Saturday. I have sandwiches. Can you bring juice?", note="On + dia da semana. Can you bring…? pede para trazer algo."),
 ],
 sounds=[
  dict(say="Did you bring a blanket?", tag="redução: did you", tip="Em fala rápida, 'did you' vira 'didju'. Acentue BRING e BLAN."),
  dict(say="Let's sit under that tree.", tag="ligação: sit under", tip="Una sit e under: 'sidunder'. O t entre vogais soa quase como d."),
  dict(say="Sandwiches, fruit and juice.", tag="ritmo: lista em três", tip="Acentue SAND, FRUIT e JUICE; 'and' fica fraco, quase 'n'."),
 ],
 role=dict(turns=[
  dict(npc="It's a beautiful day for a picnic!", opts=[
   dict(en="Yes! Did you bring a blanket?", pt="Sim! Você trouxe cobertor?", reply="I did. And you, what's in your bag?"),
   dict(en="Yes! Did you bring a cooler?", pt="Sim! Você trouxe uma caixa térmica?", reply="I did. And you, what's in your bag?"),
   dict(en="It sure is! Is the blanket in your bag?", pt="Com certeza! O cobertor está na sua bolsa?", reply="I did. And you, what's in your bag?")]),
  dict(npc="And you, what's in your bag?", opts=[
   dict(en="Sandwiches, fruit and juice.", pt="Sanduíches, frutas e suco.", reply="Great! I have chips and cookies."),
   dict(en="Cheese, fruit and water.", pt="Queijo, frutas e água.", reply="Great! I have chips and cookies."),
   dict(en="Just sandwiches and lemonade.", pt="Só sanduíches e limonada.", reply="Great! I have chips and cookies.")]),
  dict(npc="I have chips and cookies.", opts=[
   dict(en="Let's sit under that tree.", pt="Vamos sentar debaixo daquela árvore.", reply="Good idea. It's shady."),
   dict(en="Let's sit on the grass.", pt="Vamos sentar na grama.", reply="OK. The grass is soft."),
   dict(en="Let's sit near the lake.", pt="Vamos sentar perto do lago.", reply="Good idea. It's nice there.")]),
  dict(npc="Good idea. Are you ready?", opts=[
   dict(en="Yes. Let's eat!", pt="Sim. Vamos comer!", reply="Have a great picnic!"),
   dict(en="Yes. Let's share the food!", pt="Sim. Vamos dividir a comida!", reply="Have a great picnic!"),
   dict(en="Yes. Chips first, please!", pt="Sim. Salgadinhos primeiro, por favor!", reply="Have a great picnic!")]),
 ], change=["O lugar sob a árvore está ocupado: sugira outro lugar.", "Ravi esqueceu o cobertor: diga que dá para sentar na grama.", "Começa a ventar muito: sugira ir para um lugar com sombra."]),
 writing=dict(task="Escreva 2 ou 3 frases para um amigo: convide para um piquenique no sábado, diga o que você tem e peça que ele traga uma bebida.", model="Hi! Let's have a picnic on Saturday. I have sandwiches. Can you bring juice?", kw=["picnic", "saturday", "have", "bring"], checks=["Convidou para o piquenique.", "Disse o que tem.", "Pediu que ele trouxesse algo."]),
 scenes=dict(pool=["park", "park2", "playground", "lake"], npc=dict(g="m", role="friend"), you=dict(g="f")),
 convo=dict(npc=dict(name="Ravi"), story="Você e seu amigo Ravi estão no parque para um piquenique.", turns=[
  dict(npc="It's a beautiful day for a picnic!", pt="É um lindo dia para um piquenique!", opts=[
   dict(en="Have a great picnic!", pt="Tenha um ótimo piquenique!", ok=False, fb="É uma despedida; ainda é cedo."),
   dict(en="Let's eat!", pt="Vamos comer!", ok=False, fb="Vocês ainda nem sentaram."),
   dict(en="Yes! Did you bring a blanket?", pt="Sim! Você trouxe cobertor?", ok=True, fb="Concorda e pergunta algo útil.")]),
  dict(npc="I did. And you, what's in your bag?", pt="Trouxe. E você, o que tem na sua bolsa?", opts=[
   dict(en="Sandwiches, fruit and juice.", pt="Sanduíches, frutas e suco.", ok=True, fb="Lista curta e clara."),
   dict(en="I did.", pt="Trouxe.", ok=False, fb="Essa resposta é dele."),
   dict(en="It's shady.", pt="Tem sombra.", ok=False, fb="Não responde sobre a bolsa.")]),
  dict(npc="Great! I have chips and cookies.", pt="Ótimo! Tenho salgadinhos e biscoitos.", opts=[
   dict(en="Did you bring a blanket?", pt="Você trouxe cobertor?", ok=False, fb="Ele já respondeu."),
   dict(en="Let's sit under that tree.", pt="Vamos sentar debaixo daquela árvore.", ok=True, fb="Propõe o próximo passo."),
   dict(en="Sandwiches, fruit and juice.", pt="Sanduíches, frutas e suco.", ok=False, fb="Você já disse isso.")]),
  dict(npc="Good idea. It's shady.", pt="Boa ideia. Tem sombra.", opts=[
   dict(en="Let's eat!", pt="Vamos comer!", ok=True, fb="Convida a começar."),
   dict(en="Let's sit under that tree.", pt="Vamos sentar debaixo daquela árvore.", ok=False, fb="Ele já concordou."),
   dict(en="Have a great picnic!", pt="Tenha um ótimo piquenique!", ok=False, fb="É fala de despedida dele.")]),
  dict(npc="Have a great picnic!", pt="Tenha um ótimo piquenique!", opts=[
   dict(en="Did you bring a blanket?", pt="Você trouxe cobertor?", ok=False, fb="Fora de contexto."),
   dict(en="It's a beautiful day.", pt="É um lindo dia.", ok=False, fb="Não responde ao desejo dele."),
   dict(en="Thanks! You too!", pt="Obrigado! Você também!", ok=True, fb="Resposta natural.")]),
 ]),
)
