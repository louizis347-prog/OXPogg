X = dict(
 key=dict(big="A table for two, please", label="Pedir uma mesa", sub="Diga quantas pessoas são, escolha a pizza, aceite a espera e peça as bebidas."),
 mini=[
  dict(who="You", en="Hi. A table for {two|three|four}, please.", pt="Oi. Uma mesa para {dois|três|quatro}, por favor."),
  dict(who="Evan", en="Sure. Follow me. Would you like a {booth|table|seat} by the window?", pt="Claro. Siga-me. Querem {uma mesa de canto|uma mesa|um lugar} perto da janela?"),
  dict(who="You", en="We want a deep dish {pizza|sausage pizza|cheese pizza}.", pt="Queremos uma {pizza de massa grossa|pizza de massa grossa com linguiça|pizza de massa grossa com queijo}."),
  dict(who="Evan", en="It takes {forty|thirty|fifty} minutes.", pt="Leva {quarenta|trinta|cinquenta} minutos."),
 ],
 dlg=[
  dict(who="Evan", en="Hi. A table for {two|three}, please.", pt="Oi. Uma mesa para {dois|três}, por favor."),
  dict(who="You", en="Sure. {Follow me.|This way.}", pt="Claro. {Siga-me.|Por aqui.}"),
  dict(who="Evan", en="We want a deep dish {pizza.|sausage pizza.}", pt="Queremos uma {pizza de massa grossa.|pizza de massa grossa com linguiça.}"),
  dict(who="You", en="It takes {forty|thirty} minutes.", pt="Leva {quarenta|trinta} minutos."),
  dict(who="Evan", en="That's fine. We're not in a {hurry.|rush.}", pt="Tudo bem. Não temos {pressa.|pressa.}"),
  dict(who="You", en="Would you like something to {drink?|eat?}", pt="Querem algo para {beber?|comer?}"),
  dict(who="Evan", en="Two {sodas,|waters,} please.", pt="Dois {refrigerantes,|copos de água,} por favor."),
  dict(who="You", en="It's so {windy|cold} today!", pt="Está {ventando|frio} demais hoje!"),
  dict(who="Evan", en="That's why they call it the {Windy City.|Windy City, right?}", pt="Por isso chamam de {Cidade dos Ventos.|Cidade dos Ventos, certo?}"),
 ],
 vocab=[
  dict(w="crust", pt="massa, borda", e="🥖", ex=["The crust is thick.", "I like a thin crust."]),
  dict(w="sausage", pt="linguiça", e="🌭", ex=["We want sausage on the pizza.", "The sausage is hot."]),
  dict(w="topping", pt="cobertura (ingrediente extra)", e="🧅", ex=["Onions are my favorite topping.", "Choose one topping."]),
  dict(w="delicious", pt="delicioso", e="😋", ex=["The pizza is delicious.", "This cheese is delicious."]),
  dict(w="hurry", pt="pressa", e="⏱️", ex=["We are not in a hurry.", "Why are you in a hurry?"]),
  dict(w="host", pt="recepcionista do restaurante", e="🧑‍🍳", ex=["The host shows us a table.", "Ask the host, please."]),
 ],
 molds=[
  dict(title="Pedir a pizza", frame="We want a {kind} pizza with {top}.", slots=[dict(key="kind", opts=["deep dish", "thin crust", "large"]), dict(key="top", opts=["sausage", "onions", "extra cheese"])], model="We want a deep dish pizza with sausage.", note="Com + ingrediente = with. O adjetivo vem antes de pizza."),
  dict(title="Falar do tempo de espera", frame="It takes {time} minutes. {reply}", slots=[dict(key="time", opts=["thirty", "forty", "fifty"]), dict(key="reply", opts=["That's fine.", "That's okay.", "No problem."])], model="It takes thirty minutes. That's fine.", note="It takes + tempo mostra quanto algo demora."),
  dict(title="Escrever o pedido", frame="Hi. A table for {n}, please. We want a {kind} pizza and {drink}.", slots=[dict(key="n", opts=["two", "three", "four"]), dict(key="kind", opts=["deep dish", "large", "cheese"]), dict(key="drink", opts=["two sodas", "two waters", "a juice"])], model="Hi. A table for two, please. We want a deep dish pizza and two sodas.", note="A table for + número de pessoas. Use o plural em two sodas."),
 ],
 sounds=[
  dict(say="A table for two, please.", tag="ligação: table for", tip="Una 'table' e 'for': 'teibol-for'. Acentue TA-ble e TWO."),
  dict(say="It takes forty minutes.", tag="ligação: takes forty", tip="O s final de 'takes' passa para 'forty': 'teiks-forty'. Sem pausa."),
  dict(say="That's why they call it the Windy City.", tag="ligação: call it", tip="Soa 'colit'. Una 'call' e 'it' e acentue WIN-dy CI-ty."),
 ],
 role=dict(turns=[
  dict(npc="Hi! How many people?", opts=[
   dict(en="A table for two, please.", pt="Uma mesa para dois, por favor.", reply="Sure. Follow me."),
   dict(en="Two people, please.", pt="Duas pessoas, por favor.", reply="Sure. Follow me."),
   dict(en="Hi. Table for two.", pt="Oi. Mesa para dois.", reply="Okay. This way.")]),
  dict(npc="What would you like?", opts=[
   dict(en="We want a deep dish pizza.", pt="Queremos uma pizza de massa grossa.", reply="It takes forty minutes."),
   dict(en="A deep dish with sausage, please.", pt="Uma de massa grossa com linguiça, por favor.", reply="It takes forty minutes."),
   dict(en="A large cheese pizza, please.", pt="Uma pizza grande de queijo, por favor.", reply="That one is faster. Thirty minutes.")]),
  dict(npc="It takes a while. Is that okay?", opts=[
   dict(en="That's fine. We're not in a hurry.", pt="Tudo bem. Não temos pressa.", reply="Great. Would you like something to drink?"),
   dict(en="Okay. We have time.", pt="Certo. Temos tempo.", reply="Great. Would you like something to drink?"),
   dict(en="Hmm. Can we have a drink first?", pt="Hum. Podemos beber algo antes?", reply="Sure. What would you like?")]),
  dict(npc="Would you like something to drink?", opts=[
   dict(en="Two sodas, please.", pt="Dois refrigerantes, por favor.", reply="Coming right up. It's so windy today!"),
   dict(en="Two waters, please.", pt="Duas águas, por favor.", reply="Coming right up. It's so windy today!"),
   dict(en="One soda and one juice, please.", pt="Um refrigerante e um suco, por favor.", reply="Coming right up. It's so windy today!")]),
 ], change=["O restaurante está cheio: pergunte quanto tempo de espera.", "Seu amigo quer uma pizza sem queijo: peça isso ao anfitrião.", "A mesa perto da janela está livre: aceite e agradeça."]),
 writing=dict(task="Você está em uma pizzaria em Chicago. Escreva 2 ou 3 frases: peça uma mesa, a pizza e as bebidas.", model="Hi. A table for two, please. We want a deep dish pizza and two sodas.", kw=["table", "two", "pizza", "please"], checks=["Pediu uma mesa.", "Disse quantas pessoas.", "Pediu a pizza ou as bebidas."]),
 scenes=dict(pool=["restaurant", "diner", "street", "counter"], npc=dict(g="m", role="waiter"), you=dict(g="f")),
 convo=dict(npc=dict(name="Sam"), story="Você está em uma pizzaria em Chicago. Sam é o anfitrião.", turns=[
  dict(npc="Hi! How many people?", pt="Oi! Quantas pessoas?", opts=[
   dict(en="Two sodas, please.", pt="Dois refrigerantes, por favor.", ok=False, fb="Ainda não é hora de pedir bebida."),
   dict(en="Follow me.", pt="Siga-me.", ok=False, fb="Quem diz isso é o anfitrião."),
   dict(en="A table for two, please.", pt="Uma mesa para dois, por favor.", ok=True, fb="Diz quantas pessoas são.")]),
  dict(npc="Sure. Follow me. What would you like?", pt="Claro. Siga-me. O que vocês querem?", opts=[
   dict(en="We want a deep dish pizza.", pt="Queremos uma pizza de massa grossa.", ok=True, fb="Faz o pedido da comida."),
   dict(en="It takes forty minutes.", pt="Leva quarenta minutos.", ok=False, fb="Quem informa o tempo é o restaurante."),
   dict(en="A table for two, please.", pt="Uma mesa para dois, por favor.", ok=False, fb="Vocês já estão na mesa.")]),
  dict(npc="It takes forty minutes.", pt="Leva quarenta minutos.", opts=[
   dict(en="We want a deep dish pizza.", pt="Queremos uma pizza de massa grossa.", ok=False, fb="Vocês já pediram a pizza."),
   dict(en="That's fine. We're not in a hurry.", pt="Tudo bem. Não temos pressa.", ok=True, fb="Aceita a espera com educação."),
   dict(en="Would you like something to drink?", pt="Querem algo para beber?", ok=False, fb="Essa pergunta é do anfitrião.")]),
  dict(npc="Would you like something to drink?", pt="Querem algo para beber?", opts=[
   dict(en="Two sodas, please.", pt="Dois refrigerantes, por favor.", ok=True, fb="Pedido de bebida claro."),
   dict(en="It takes forty minutes.", pt="Leva quarenta minutos.", ok=False, fb="Não responde à pergunta."),
   dict(en="Follow me.", pt="Siga-me.", ok=False, fb="Não faz sentido aqui.")]),
  dict(npc="It's so windy today!", pt="Está ventando muito hoje!", opts=[
   dict(en="A table for two, please.", pt="Uma mesa para dois, por favor.", ok=False, fb="Vocês já têm mesa."),
   dict(en="Two sodas, please.", pt="Dois refrigerantes, por favor.", ok=False, fb="O assunto agora é o vento."),
   dict(en="That's why they call it the Windy City.", pt="Por isso chamam de Cidade dos Ventos.", ok=True, fb="Comentário natural sobre Chicago.")]),
 ]),
)
