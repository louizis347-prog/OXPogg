X = dict(
 key=dict(big="I'd like to rent a car", label="Alugar um carro", sub="Diga que quer alugar, mostre a carteira, informe os dias e pergunte se a gasolina está incluída."),
 mini=[
  dict(who="Claire", en="Hi! I'd like to {rent|book|get} a car.", pt="Oi! Eu gostaria de {alugar|reservar|pegar} um carro."),
  dict(who="You", en="Sure. Do you have a {driver's license|credit card|passport}?", pt="Claro. Você tem {carteira de motorista|cartão de crédito|passaporte}?"),
  dict(who="Claire", en="Yes. For {three|two|five} days.", pt="Sim. Por {três|dois|cinco} dias."),
  dict(who="You", en="A {small|big|automatic} car is fifty dollars a day.", pt="Um carro {pequeno|grande|automático} custa cinquenta dólares por dia."),
 ],
 dlg=[
  dict(who="Claire", en="Hi! I'd like to {rent|book} a car.", pt="Oi! Eu gostaria de {alugar|reservar} um carro."),
  dict(who="You", en="Sure. Do you have a {driver's license?|license?}", pt="Claro. Você tem {carteira de motorista?|carteira?}"),
  dict(who="Claire", en="Yes, {here it is.|here you go.}", pt="Sim, {aqui está.|tome.}"),
  dict(who="You", en="For how many {days?|weeks?}", pt="Por quantos {dias?|semanas?}"),
  dict(who="Claire", en="{Three|Two|Five} days.", pt="{Três|Dois|Cinco} dias."),
  dict(who="You", en="A {small|big} car is fifty dollars a day.", pt="Um carro {pequeno|grande} custa cinquenta dólares por dia."),
  dict(who="Claire", en="That's fine. Is {gas|insurance} included?", pt="Tudo bem. {A gasolina|O seguro} está incluído?"),
  dict(who="You", en="No, it {isn't.|is not.}", pt="Não, {não está.|não está.}"),
  dict(who="Claire", en="Have a {safe|good} trip!", pt="Boa {viagem!|viagem!}"),
 ],
 vocab=[
  dict(w="license", pt="carteira de motorista", e="🪪", ex=["Do you have a license?", "Show your license, please."]),
  dict(w="automatic", pt="automático", e="⚙️", ex=["I want an automatic car.", "This car is automatic."]),
  dict(w="seatbelt", pt="cinto de segurança", e="🪢", ex=["Put on your seatbelt.", "The seatbelt is blue."]),
  dict(w="highway", pt="rodovia", e="🛣️", ex=["The highway is long.", "We drive on the highway."]),
  dict(w="rental", pt="aluguel (de carro)", e="🚙", ex=["This is a rental car.", "The rental office is open."]),
  dict(w="trunk", pt="porta-malas", e="🧳", ex=["The trunk is big.", "Put the bag in the trunk."]),
 ],
 molds=[
  dict(title="Pedir um carro", frame="I'd like to rent a {type} car.", slots=[dict(key="type", opts=["small", "big", "automatic"])], model="I'd like to rent a small car.", note="I'd like to... é educado. Rent a car = alugar um carro."),
  dict(title="Dizer o preço", frame="A {type} car is {price} dollars a day.", slots=[dict(key="type", opts=["small", "big", "cheap"]), dict(key="price", opts=["fifty", "sixty", "eighty"])], model="A small car is fifty dollars a day.", note="A day = por dia. Não use 'by day' aqui."),
  dict(title="Escrever o pedido", frame="Hi! I'd like to rent a car for {days} days. Is {thing} included?", slots=[dict(key="days", opts=["two", "three", "five"]), dict(key="thing", opts=["gas", "insurance", "the seatbelt"])], model="Hi! I'd like to rent a car for two days. Is gas included?", note="Is... included? pergunta se algo já está no preço."),
 ],
 sounds=[
  dict(say="I'd like to rent a car.", tag="ligação: rent a", tip="Una rent e a: 'renta'. Acentue RENT e CAR."),
  dict(say="Here it is.", tag="ligação: here it is", tip="Soa 'hirit-iz'. Una as três palavras sem parar."),
  dict(say="Have a safe trip!", tag="ritmo: HAVE a SAFE TRIP", tip="Acentue HAVE, SAFE e TRIP; 'a' fica fraco, quase 'uh'."),
 ],
 role=dict(turns=[
  dict(npc="Hi! I'd like to rent a car.", opts=[
   dict(en="Sure. Do you have a driver's license?", pt="Claro. Você tem carteira de motorista?", reply="Yes, here it is."),
   dict(en="Of course. May I see your license?", pt="Claro. Posso ver sua carteira?", reply="Yes, here it is."),
   dict(en="Sure. License, please.", pt="Claro. A carteira, por favor.", reply="Yes, here you go.")]),
  dict(npc="Yes, here it is.", opts=[
   dict(en="For how many days?", pt="Por quantos dias?", reply="Three days."),
   dict(en="Thanks. How many days?", pt="Obrigado. Quantos dias?", reply="Three days."),
   dict(en="Great. For how long?", pt="Ótimo. Por quanto tempo?", reply="Three days.")]),
  dict(npc="Three days. What do you have?", opts=[
   dict(en="A small car is fifty dollars a day.", pt="Um carro pequeno custa cinquenta dólares por dia.", reply="That's fine. Is gas included?"),
   dict(en="A big car is eighty dollars a day.", pt="Um carro grande custa oitenta dólares por dia.", reply="Hmm, that's a lot. Is gas included?"),
   dict(en="An automatic car is sixty dollars a day.", pt="Um carro automático custa sessenta dólares por dia.", reply="Okay. Is gas included?")]),
  dict(npc="Is gas included?", opts=[
   dict(en="No, it isn't.", pt="Não, não está.", reply="Okay. Thank you!"),
   dict(en="No, you pay for gas.", pt="Não, você paga a gasolina.", reply="Okay. Thank you!"),
   dict(en="No, but return it with a full tank.", pt="Não, mas devolva com o tanque cheio.", reply="Okay. Thank you!")]),
 ], change=["O carro pequeno acabou: ofereça um maior e diga o preço.", "Claire esqueceu a carteira: explique que precisa dela para alugar.", "Claire quer o carro por mais um dia: diga o novo total."]),
 writing=dict(task="Você quer alugar um carro. Escreva 2 ou 3 frases: diga que quer alugar, por quantos dias e pergunte se a gasolina está incluída.", model="Hi! I'd like to rent a small car for three days. Is gas included?", kw=["rent", "car", "days", "gas"], checks=["Disse que quer alugar um carro.", "Disse por quantos dias.", "Perguntou sobre a gasolina."]),
 scenes=dict(pool=["street", "airport", "lobby", "counter"], npc=dict(g="f", role="customer"), you=dict(g="m")),
 convo=dict(npc=dict(name="Claire"), story="Você trabalha em uma locadora de carros. Claire quer alugar um carro.", turns=[
  dict(npc="Hi! I'd like to rent a car.", pt="Oi! Eu gostaria de alugar um carro.", opts=[
   dict(en="Have a safe trip!", pt="Boa viagem!", ok=False, fb="Cedo demais: é a despedida."),
   dict(en="Sure. Do you have a driver's license?", pt="Claro. Você tem carteira de motorista?", ok=True, fb="Primeiro passo: pedir a carteira."),
   dict(en="No, it isn't.", pt="Não, não está.", ok=False, fb="Não responde ao pedido dela.")]),
  dict(npc="Yes, here it is.", pt="Sim, aqui está.", opts=[
   dict(en="For how many days?", pt="Por quantos dias?", ok=True, fb="Próximo passo: o tempo do aluguel."),
   dict(en="Is gas included?", pt="A gasolina está incluída?", ok=False, fb="Quem pergunta isso é ela."),
   dict(en="Three days.", pt="Três dias.", ok=False, fb="Essa resposta é dela, não sua.")]),
  dict(npc="Three days.", pt="Três dias.", opts=[
   dict(en="Do you have a driver's license?", pt="Você tem carteira de motorista?", ok=False, fb="Ela já mostrou a carteira."),
   dict(en="I'd like to rent a car.", pt="Eu gostaria de alugar um carro.", ok=False, fb="Esse é o pedido dela."),
   dict(en="A small car is fifty dollars a day.", pt="Um carro pequeno custa cinquenta dólares por dia.", ok=True, fb="Diz o preço por dia.")]),
  dict(npc="That's fine. Is gas included?", pt="Tudo bem. A gasolina está incluída?", opts=[
   dict(en="No, it isn't.", pt="Não, não está.", ok=True, fb="Resposta curta e clara."),
   dict(en="For how many days?", pt="Por quantos dias?", ok=False, fb="Ela já disse: três dias."),
   dict(en="Yes, here it is.", pt="Sim, aqui está.", ok=False, fb="Não responde sobre a gasolina.")]),
  dict(npc="Okay. Thank you!", pt="Certo. Obrigada!", opts=[
   dict(en="Have a safe trip!", pt="Boa viagem!", ok=True, fb="Despedida natural."),
   dict(en="Do you have a license?", pt="Você tem carteira?", ok=False, fb="Já foi feito."),
   dict(en="A small car, please.", pt="Um carro pequeno, por favor.", ok=False, fb="Quem escolhe o carro é a cliente.")]),
 ]),
)
