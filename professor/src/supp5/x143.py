X = dict(
 key=dict(big="It's so foggy today", label="Falar do tempo e da neblina", sub="Comente o tempo, pergunte se dá para ver a ponte, aceite um casaco e combine o passeio de bondinho."),
 mini=[
  dict(who="You", en="Good morning! It's so {foggy|cold|gray} today.", pt="Bom dia! Está tão {nublado|frio|cinza} hoje."),
  dict(who="Nina", en="Yes. It's always {foggy|cloudy|chilly} here.", pt="Sim. Aqui sempre está {com neblina|nublado|friozinho}."),
  dict(who="You", en="Can we see the {bridge|bay|hills}?", pt="Dá para ver {a ponte|a baía|as colinas}?"),
  dict(who="Nina", en="Not right now. Maybe at {noon|two|four}.", pt="Agora não. Talvez ao {meio-dia|às duas|às quatro}."),
 ],
 dlg=[
  dict(who="Nina", en="Good morning! It's so {foggy|cold} today.", pt="Bom dia! Está tão {nublado|frio} hoje."),
  dict(who="You", en="Yes. It's always {foggy|cloudy} here.", pt="Sim. Aqui sempre está {com neblina|nublado}."),
  dict(who="Nina", en="Can we see the {bridge?|bay?}", pt="Dá para ver {a ponte?|a baía?}"),
  dict(who="You", en="Not right now. Maybe at {noon.|two.}", pt="Agora não. Talvez {ao meio-dia.|às duas.}"),
  dict(who="Nina", en="It's {chilly|cold} too.", pt="Está {frio|gelado} também."),
  dict(who="You", en="Take my {jacket.|scarf.}", pt="Pegue meu {casaco.|cachecol.}"),
  dict(who="Nina", en="Thanks. You're {kind.|nice.}", pt="Obrigado. Você é {gentil.|legal.}"),
  dict(who="You", en="Do you want to ride the {cable car?|bus?}", pt="Quer andar de {bondinho?|ônibus?}"),
  dict(who="Nina", en="Yes! Where do we {catch|get} it?", pt="Sim! Onde nós {pegamos|pegamos} isso?"),
 ],
 vocab=[
  dict(w="fog", pt="neblina", e="🌫️", ex=["The fog is thick today.", "Fog hides the bridge."]),
  dict(w="hill", pt="ladeira, colina", e="⛰️", ex=["The street goes up a hill.", "San Francisco has many hills."]),
  dict(w="chilly", pt="friozinho", e="🥶", ex=["It's chilly this morning.", "I'm chilly. Do you have a jacket?"]),
  dict(w="cable car", pt="bondinho", e="🚋", ex=["We ride the cable car.", "The cable car goes up the hill."]),
  dict(w="bay", pt="baía", e="🌊", ex=["The bay is blue.", "We see boats in the bay."]),
  dict(w="breeze", pt="brisa", e="🍃", ex=["There is a cool breeze.", "The breeze feels nice."]),
 ],
 molds=[
  dict(title="Comentar o tempo", frame="It's so {weather} today.", slots=[dict(key="weather", opts=["foggy", "cold", "chilly", "gray"])], model="It's so foggy today.", note="It's so + adjetivo. Foggy é adjetivo; fog é substantivo."),
  dict(title="Perguntar se dá para ver", frame="Can we see the {thing}? Not right now. Maybe at {time}.", slots=[dict(key="thing", opts=["bridge", "bay", "hills"]), dict(key="time", opts=["noon", "two", "four"])], model="Can we see the bridge? Not right now. Maybe at noon.", note="Can we + verbo base. Maybe at + hora."),
  dict(title="Escrever o convite", frame="It's {weather} here. Take my {item}. Do you want to ride the {ride}?", slots=[dict(key="weather", opts=["chilly", "cold", "foggy"]), dict(key="item", opts=["jacket", "scarf", "sweater"]), dict(key="ride", opts=["cable car", "bus", "ferry"])], model="It's chilly here. Take my jacket. Do you want to ride the cable car?", note="Take my + objeto. Ride the + transporte."),
 ],
 sounds=[
  dict(say="Where do we catch it?", tag="ligação: catch it", tip="Una 'catch' e 'it': 'catchit'. O ch passa para a vogal seguinte."),
  dict(say="Take my jacket.", tag="ligação: take my", tip="Una 'take' e 'my': 'teik-mai'. Acentue TAKE e JAC-ket."),
  dict(say="Not right now.", tag="ligação: right now", tip="Una 'right' e 'now' sem pausa: 'rai-now'. O t de 'not' quase some."),
 ],
 role=dict(turns=[
  dict(npc="Good morning! Look outside.", opts=[
   dict(en="Good morning! It's so foggy today.", pt="Bom dia! Está tão nublado hoje.", reply="Yes. It's always foggy here."),
   dict(en="Wow. It's really foggy.", pt="Uau. Está mesmo com neblina.", reply="Yes. It's always foggy here."),
   dict(en="Good morning! It's gray outside.", pt="Bom dia! Está cinza lá fora.", reply="Yes. It's often gray here.")]),
  dict(npc="Yes. It's always foggy here.", opts=[
   dict(en="Can we see the bridge?", pt="Dá para ver a ponte?", reply="Not right now. Maybe at noon."),
   dict(en="Is the bridge there?", pt="A ponte está lá?", reply="Yes, but we can't see it. Maybe at noon."),
   dict(en="Can we see the bay?", pt="Dá para ver a baía?", reply="Not right now. Maybe at noon.")]),
  dict(npc="Not right now. Maybe at noon.", opts=[
   dict(en="It's chilly too.", pt="Está frio também.", reply="Take my jacket."),
   dict(en="I'm cold. Do you have a jacket?", pt="Estou com frio. Você tem um casaco?", reply="Sure. Take my jacket."),
   dict(en="It's a bit cold, too.", pt="Também está um pouco frio.", reply="Take my scarf.")]),
  dict(npc="Take my jacket.", opts=[
   dict(en="Thanks. You're kind.", pt="Obrigado. Você é gentil.", reply="Do you want to ride the cable car?"),
   dict(en="Thank you. That's nice.", pt="Obrigado. Que legal.", reply="Do you want to ride the cable car?"),
   dict(en="Thanks. It's warm.", pt="Obrigado. Está quentinho.", reply="Good! Do you want to ride the cable car?")]),
 ], change=["A neblina passou: comente que agora dá para ver a ponte.", "Você esqueceu o casaco: peça emprestado.", "O bondinho está cheio: pergunte quanto tempo é a fila."]),
 writing=dict(task="Você visita São Francisco num dia de neblina. Escreva 2 ou 3 frases: comente o tempo e pergunte se dá para ver a ponte.", model="It's so foggy today. It's chilly too. Can we see the bridge?", kw=["foggy", "chilly", "bridge", "can"], checks=["Comentou a neblina.", "Falou do frio.", "Perguntou se dá para ver a ponte."]),
 scenes=dict(pool=["park", "park2", "street", "pier", "harbor"], npc=dict(g="f", role="friend"), you=dict(g="m")),
 convo=dict(npc=dict(name="Nina"), story="Você visita São Francisco. Nina é sua amiga e mora lá. A manhã está com neblina.", turns=[
  dict(npc="Good morning! Look outside.", pt="Bom dia! Olhe lá fora.", opts=[
   dict(en="Good morning! It's so foggy today.", pt="Bom dia! Está tão nublado hoje.", ok=True, fb="Comenta o tempo."),
   dict(en="Take my jacket.", pt="Pegue meu casaco.", ok=False, fb="Ainda não é hora de oferecer casaco."),
   dict(en="Where do we catch it?", pt="Onde pegamos?", ok=False, fb="Ninguém falou de transporte.")]),
  dict(npc="Yes. It's always foggy here.", pt="Sim. Aqui sempre tem neblina.", opts=[
   dict(en="Thanks. You're kind.", pt="Obrigado. Você é gentil.", ok=False, fb="Ela não ofereceu nada."),
   dict(en="Can we see the bridge?", pt="Dá para ver a ponte?", ok=True, fb="Pergunta natural."),
   dict(en="Not right now. Maybe at noon.", pt="Agora não. Talvez ao meio-dia.", ok=False, fb="Essa resposta é da Nina.")]),
  dict(npc="Not right now. Maybe at noon.", pt="Agora não. Talvez ao meio-dia.", opts=[
   dict(en="It's chilly too.", pt="Está frio também.", ok=True, fb="Comenta o frio."),
   dict(en="Can we see the bridge?", pt="Dá para ver a ponte?", ok=False, fb="Você já perguntou."),
   dict(en="Do you want to ride the cable car?", pt="Quer andar no bondinho?", ok=False, fb="Cedo demais; falta resolver o frio.")]),
  dict(npc="Take my jacket.", pt="Pegue meu casaco.", opts=[
   dict(en="It's so foggy today.", pt="Está tão nublado hoje.", ok=False, fb="Não responde à oferta."),
   dict(en="Thanks. You're kind.", pt="Obrigado. Você é gentil.", ok=True, fb="Agradece com educação."),
   dict(en="Do you want my jacket?", pt="Você quer meu casaco?", ok=False, fb="A oferta é dela; você é quem recebe.")]),
  dict(npc="Do you want to ride the cable car?", pt="Quer andar no bondinho?", opts=[
   dict(en="Yes! Where do we catch it?", pt="Sim! Onde pegamos?", ok=True, fb="Aceita e pergunta onde."),
   dict(en="Not right now. Maybe at noon.", pt="Agora não. Talvez ao meio-dia.", ok=False, fb="Isso era sobre a ponte."),
   dict(en="It's chilly too.", pt="Está frio também.", ok=False, fb="Não responde ao convite.")]),
 ]),
)
