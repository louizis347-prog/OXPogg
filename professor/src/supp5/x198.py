X = dict(
 key=dict(big="Can I get a ride?", label="Pedir carona", sub="Explique o motivo, peça com educação e combine o lugar. Oferecer ajuda com a gasolina é um gesto simpático."),
 mini=[
  dict(who="You", en="Hey, are you going to {work?|school?|the mall?}", pt="Ei, você vai para {o trabalho?|a escola?|o shopping?}"),
  dict(who="Miles", en="Yes. {Why?|What's up?}", pt="Vou. {Por quê?|Que foi?}"),
  dict(who="You", en="My car is in the {shop.|garage.} Can I get a ride?", pt="Meu carro está na {oficina.|garagem.} Posso pegar carona?"),
  dict(who="Miles", en="Sure. I'm leaving in {ten|five|fifteen} minutes. {Meet me in front.|Wait outside.}", pt="Claro. Saio em {dez|cinco|quinze} minutos. {Me encontre na frente.|Espere do lado de fora.}"),
 ],
 dlg=[
  dict(who="Miles", en="Hey, are you going to {work?|school?}", pt="Ei, você vai para {o trabalho?|a escola?}"),
  dict(who="You", en="Yes. {Why?|What's up?}", pt="Vou. {Por quê?|Que foi?}"),
  dict(who="Miles", en="My car is in the {shop.|garage.} Can I get a ride?", pt="Meu carro está na {oficina.|garagem.} Posso pegar carona?"),
  dict(who="You", en="Sure. I'm leaving in {ten|five} minutes.", pt="Claro. Saio em {dez|cinco} minutos."),
  dict(who="Miles", en="Thank you {so much.|very much.} Where should I meet you?", pt="Muito {obrigado.|obrigado.} Onde devo te encontrar?"),
  dict(who="You", en="In front of the {building.|garage.}", pt="Na frente do {prédio.|estacionamento.}"),
  dict(who="Miles", en="Great. How long is the {drive?|trip?}", pt="Ótimo. Quanto dura o {trajeto?|trajeto?}"),
  dict(who="You", en="About {twenty-five|thirty} minutes.", pt="Uns {vinte e cinco|trinta} minutos."),
  dict(who="Miles", en="Can I chip in for {gas?|lunch?}", pt="Posso dividir {a gasolina?|o almoço?}"),
 ],
 vocab=[
  dict(w="mechanic", pt="mecânico", e="🔧", ex=["The mechanic fixes my car.", "I call the mechanic."]),
  dict(w="favor", pt="favor", e="🤝", ex=["Can you do me a favor?", "Thanks for the favor."]),
  dict(w="passenger", pt="passageiro", e="🧍", ex=["I am the passenger.", "The passenger sits in front."]),
  dict(w="work", pt="trabalho", e="💼", ex=["I go to work by car.", "Work starts at nine."]),
  dict(w="tank", pt="tanque", e="⛽", ex=["The tank is full.", "The tank is empty."]),
  dict(w="engine", pt="motor", e="⚙️", ex=["The engine is loud.", "The mechanic checks the engine."]),
 ],
 molds=[
  dict(title="Pedir carona", frame="My car is in the shop. Can I get a ride {where}?", slots=[dict(key="where", opts=["to work", "to school", "to the mall"])], model="My car is in the shop. Can I get a ride to work?", note="Can I get a ride + to + lugar. Explique o motivo antes de pedir."),
  dict(title="Combinar o encontro", frame="Where should I meet you? In front of the {place}.", slots=[dict(key="place", opts=["building", "garage", "bank", "store"])], model="Where should I meet you? In front of the building.", note="Where should I meet you? pergunta o lugar. In front of = na frente de."),
  dict(title="Escrever um agradecimento", frame="Thanks for the {thing}! Can I chip in for {cost}?", slots=[dict(key="thing", opts=["ride", "favor", "help"]), dict(key="cost", opts=["gas", "lunch", "coffee"])], model="Thanks for the ride! Can I chip in for gas?", note="Thanks for the + coisa. Chip in for = ajudar a pagar algo."),
 ],
 sounds=[
  dict(say="Can I get a ride?", tag="ligação: get a", tip="Una get + a: 'geta'. O t entre vogais soa quase como um d rápido, 'gedda'."),
  dict(say="Where should I meet you?", tag="redução: should I", tip="Should I soa 'shudai'. O l de should é mudo."),
  dict(say="About twenty-five minutes.", tag="acento: TWENty-FIVE", tip="Em twenty-five, os dois acentos ficam em TWEN e FIVE. O t de twenty costuma soar fraco."),
 ],
 role=dict(turns=[
  dict(npc="Hey, are you going to work?", opts=[
   dict(en="Yes. Can I get a ride?", pt="Vou. Posso pegar carona?", reply="Sure. I'm leaving in ten minutes."),
   dict(en="Yes. My car is in the shop. Can I get a ride?", pt="Vou. Meu carro está na oficina. Posso pegar carona?", reply="Sure. I'm leaving in ten minutes."),
   dict(en="Yes. Can I go with you?", pt="Vou. Posso ir com você?", reply="Sure. I'm leaving in ten minutes.")]),
  dict(npc="I'm leaving in ten minutes.", opts=[
   dict(en="Thank you so much. Where should I meet you?", pt="Muito obrigado. Onde devo te encontrar?", reply="In front of the building."),
   dict(en="Great! Where do we meet?", pt="Ótimo! Onde nos encontramos?", reply="In front of the building."),
   dict(en="Thanks! Where should I wait?", pt="Obrigado! Onde devo esperar?", reply="In front of the building.")]),
  dict(npc="In front of the building.", opts=[
   dict(en="Great. How long is the drive?", pt="Ótimo. Quanto dura o trajeto?", reply="About twenty-five minutes."),
   dict(en="Okay. Is it a long drive?", pt="Certo. É um trajeto longo?", reply="About twenty-five minutes."),
   dict(en="Great. How long is the trip?", pt="Ótimo. Quanto dura a viagem?", reply="About twenty-five minutes.")]),
  dict(npc="About twenty-five minutes.", opts=[
   dict(en="Can I chip in for gas?", pt="Posso dividir a gasolina?", reply="Sure, thanks! Five dollars is fine."),
   dict(en="Can I pay for the gas?", pt="Posso pagar a gasolina?", reply="No need. But thanks!"),
   dict(en="Thanks for the favor!", pt="Obrigado pelo favor!", reply="No problem. See you around!")]),
 ], change=["O motorista diz que sai em cinco minutos: diga que você está quase pronto.", "O motorista diz que o carro está cheio: pergunte se pode ir com outra pessoa.", "Ele não aceita dinheiro: agradeça e ofereça um café."]),
 writing=dict(task="Seu carro está na oficina. Escreva 2 ou 3 frases para um colega: peça carona, pergunte onde encontrar e ofereça dividir a gasolina.", model="My car is in the shop. Can I get a ride? Where should I meet you? I can chip in for gas.", kw=["car", "ride", "meet", "gas"], checks=["Explicou o motivo.", "Pediu carona.", "Ofereceu dividir a gasolina."]),
 scenes=dict(pool=["street", "yard", "home1", "park"], npc=dict(g="m", role="neighbor"), you=dict(g="f")),
 convo=dict(npc=dict(name="Miles"), story="Você é vizinho do Miles. Seu carro está na oficina e você o encontra na praça antes do trabalho.", turns=[
  dict(npc="Hey, are you going to work?", pt="Ei, você vai para o trabalho?", opts=[
   dict(en="Yes. My car is in the shop. Can I get a ride?", pt="Sim. Meu carro está na oficina. Posso pegar carona?", ok=True, fb="Dá o motivo e pede com educação."),
   dict(en="Sure. I'm leaving in ten minutes.", pt="Claro. Saio em dez minutos.", ok=False, fb="Quem oferece a carona é o Miles."),
   dict(en="About twenty-five minutes.", pt="Uns vinte e cinco minutos.", ok=False, fb="Isso responde outra pergunta.")]),
  dict(npc="Sure. I'm leaving in ten minutes.", pt="Claro. Saio em dez minutos.", opts=[
   dict(en="In front of the building.", pt="Na frente do prédio.", ok=False, fb="Primeiro agradeça e pergunte onde encontrar."),
   dict(en="Thank you so much. Where should I meet you?", pt="Muito obrigado. Onde devo te encontrar?", ok=True, fb="Agradece e pergunta o lugar."),
   dict(en="Can I chip in for gas?", pt="Posso dividir a gasolina?", ok=False, fb="Esta pergunta fica melhor no fim.")]),
  dict(npc="In front of the building.", pt="Na frente do prédio.", opts=[
   dict(en="Great. How long is the drive?", pt="Ótimo. Quanto dura o trajeto?", ok=True, fb="Pergunta natural sobre o tempo."),
   dict(en="Where should I meet you?", pt="Onde devo te encontrar?", ok=False, fb="Ele acabou de dizer o lugar."),
   dict(en="Yes. Why?", pt="Sim. Por quê?", ok=False, fb="Essa fala é de outro momento.")]),
  dict(npc="About twenty-five minutes.", pt="Uns vinte e cinco minutos.", opts=[
   dict(en="Sure. I'm leaving in ten minutes.", pt="Claro. Saio em dez minutos.", ok=False, fb="Quem sai é o Miles."),
   dict(en="Can I chip in for gas?", pt="Posso dividir a gasolina?", ok=True, fb="Oferta educada para ajudar a pagar."),
   dict(en="My car is in the shop.", pt="Meu carro está na oficina.", ok=False, fb="Ele já sabe disso.")]),
 ]),
)
