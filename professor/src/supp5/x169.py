X = dict(
 key=dict(big="Where is baggage claim?", label="Esteira de bagagem", sub="Pergunte onde fica a esteira, qual é a do seu voo e descreva sua mala se não a encontrar."),
 mini=[
  dict(who="You", en="Excuse me, where is {baggage claim?|the exit?|the bathroom?}", pt="Com licença, onde fica {a esteira de bagagem?|a saída?|o banheiro?}"),
  dict(who="Chloe", en="Follow the signs. It's {downstairs.|upstairs.|on the left.}", pt="Siga as placas. Fica {lá embaixo.|lá em cima.|à esquerda.}"),
  dict(who="You", en="Which belt is for my {flight?|bags?|plane?}", pt="Qual esteira é do meu {voo?|bagagem?|avião?}"),
  dict(who="Chloe", en="Belt number {four.|two.|six.}", pt="Esteira número {quatro.|dois.|seis.}"),
 ],
 dlg=[
  dict(who="Chloe", en="Excuse me, where is {baggage claim?|the exit?}", pt="Com licença, onde fica {a esteira de bagagem?|a saída?}"),
  dict(who="You", en="Follow the signs. It's {downstairs.|upstairs.}", pt="Siga as placas. Fica {lá embaixo.|lá em cima.}"),
  dict(who="Chloe", en="Thanks. Which {belt|gate} is for my flight?", pt="Valeu. Qual {esteira|portão} é do meu voo?"),
  dict(who="You", en="{Belt|Gate} number {four.|two.}", pt="{Esteira|Portão} número {quatro.|dois.}"),
  dict(who="Chloe", en="I can't find my {suitcase.|bag.}", pt="Não encontro minha {mala.|bolsa.}"),
  dict(who="You", en="What does it {look like?|look like, please?}", pt="Como ela {é?|é, por favor?}"),
  dict(who="Chloe", en="It's {big,|small,} blue, with a red ribbon.", pt="É {grande,|pequena,} azul, com uma fita vermelha."),
  dict(who="You", en="Let's check the {other|next} belts.", pt="Vamos ver nas {outras|próximas} esteiras."),
  dict(who="Chloe", en="It's not here. Where can I {ask?|go?}", pt="Não está aqui. Onde posso {perguntar?|ir?}"),
 ],
 vocab=[
  dict(w="baggage", pt="bagagem", e="🧳", ex=["My baggage is heavy.", "Where is baggage claim?"]),
  dict(w="worker", pt="funcionário(a)", e="👷", ex=["The worker helps me.", "A worker is near the belt."]),
  dict(w="small", pt="pequeno(a)", e="🤏", ex=["My bag is small.", "I have a small suitcase."]),
  dict(w="hall", pt="saguão", e="🏛️", ex=["The hall is big.", "Baggage claim is in the hall."]),
  dict(w="cart", pt="carrinho", e="🛒", ex=["I need a cart.", "Put the bags on the cart."]),
  dict(w="arrival", pt="chegada", e="🛬", ex=["The arrival hall is big.", "Our arrival is at noon."]),
 ],
 molds=[
  dict(title="Perguntar o lugar", frame="Excuse me, where is {place}?", slots=[dict(key="place", opts=["baggage claim", "the exit", "the bathroom", "the taxi stop"])], model="Excuse me, where is baggage claim?", note="Excuse me abre o pedido com educação. Where is + lugar."),
  dict(title="Descrever a mala", frame="It's {size}, {color}, with {thing}.", slots=[dict(key="size", opts=["big", "small", "heavy"]), dict(key="color", opts=["blue", "black", "green"]), dict(key="thing", opts=["a red ribbon", "four wheels", "a long handle"])], model="It's big, blue, with a red ribbon.", note="Tamanho, cor e um detalhe: assim o funcionário reconhece a mala."),
  dict(title="Escrever um aviso", frame="Hello! I can't find my {thing}. My flight is {num}.", slots=[dict(key="thing", opts=["suitcase", "blue bag", "small bag"]), dict(key="num", opts=["number twelve", "number forty", "number eighty"])], model="Hello! I can't find my suitcase. My flight is number twelve.", note="I can't find = não consigo encontrar."),
 ],
 sounds=[
  dict(say="Excuse me, where is baggage claim?", tag="ritmo: exCUSE me, WHERE is BAGgage CLAIM", tip="Acentue CUSE, WHERE, BAG e CLAIM; 'is' fica fraco."),
  dict(say="I can't find my suitcase.", tag="can't: som de a aberto", tip="Em 'can't' o a é longo (americano: 'quént'); o t final fica suave. Não diga 'can'."),
  dict(say="It's big, blue, with a red ribbon.", tag="ligação: with a", tip="Una with e a: 'wi-tha'. Acentue BIG, BLUE e RED."),
 ],
 role=dict(turns=[
  dict(npc="Hello! Can I help you?", opts=[
   dict(en="Excuse me, where is baggage claim?", pt="Com licença, onde fica a esteira de bagagem?", reply="Follow the signs. It's downstairs."),
   dict(en="Hi! Where is baggage claim, please?", pt="Oi! Onde fica a esteira, por favor?", reply="Follow the signs. It's downstairs."),
   dict(en="Yes, please. Where are the bags?", pt="Sim, por favor. Onde ficam as malas?", reply="Follow the signs. It's downstairs.")]),
  dict(npc="Follow the signs. It's downstairs.", opts=[
   dict(en="Thanks. Which belt is for my flight?", pt="Valeu. Qual esteira é do meu voo?", reply="Belt number four."),
   dict(en="Thank you. Which belt is it?", pt="Obrigada. Qual esteira é?", reply="Belt number four."),
   dict(en="Great. Where is my flight's belt?", pt="Ótimo. Onde é a esteira do meu voo?", reply="Belt number four.")]),
  dict(npc="Belt number four. Is everything okay?", opts=[
   dict(en="I can't find my suitcase.", pt="Não encontro minha mala.", reply="What does it look like?"),
   dict(en="My suitcase isn't here.", pt="Minha mala não está aqui.", reply="What does it look like?"),
   dict(en="I don't see my bag.", pt="Não vejo minha mala.", reply="What does it look like?")]),
  dict(npc="What does it look like?", opts=[
   dict(en="It's big, blue, with a red ribbon.", pt="É grande, azul, com uma fita vermelha.", reply="Let's check the other belts."),
   dict(en="It's small and black, with wheels.", pt="É pequena e preta, com rodas.", reply="Let's check the other belts."),
   dict(en="It's heavy and green.", pt="É pesada e verde.", reply="Let's check the other belts.")]),
 ], change=["A mala não aparece em nenhuma esteira: pergunte onde preencher um formulário.", "Você não entendeu a placa: peça ao funcionário para mostrar o caminho.", "O funcionário pergunta o número do voo: diga um número e agradeça."]),
 writing=dict(task="Sua mala não chegou. Escreva 2 ou 3 frases para o funcionário: diga que não encontra, descreva a mala e pergunte onde pedir ajuda.", model="I can't find my suitcase. It's big and blue, with a red ribbon. Where can I ask?", kw=["find", "suitcase", "blue", "ask"], checks=["Disse que não encontra a mala.", "Descreveu a mala.", "Perguntou onde pedir ajuda."]),
 scenes=dict(pool=["airport", "airport2", "hall", "counter"], npc=dict(g="f", role="worker"), you=dict(g="m")),
 convo=dict(npc=dict(name="Chloe"), story="Você chegou a Newark. A Chloe trabalha no aeroporto e vai ajudar você.", turns=[
  dict(npc="Hello! Can I help you?", pt="Olá! Posso ajudar?", opts=[
   dict(en="Excuse me, where is baggage claim?", pt="Com licença, onde fica a esteira de bagagem?", ok=True, fb="Pedido educado e claro."),
   dict(en="Belt number four.", pt="Esteira número quatro.", ok=False, fb="Você ainda não sabe a esteira."),
   dict(en="What does it look like?", pt="Como ela é?", ok=False, fb="Quem pergunta isso é ela.")]),
  dict(npc="Follow the signs. It's downstairs.", pt="Siga as placas. Fica lá embaixo.", opts=[
   dict(en="Thanks. Which belt is for my flight?", pt="Valeu. Qual esteira é do meu voo?", ok=True, fb="Próximo passo: achar a esteira."),
   dict(en="It's big, blue, with a red ribbon.", pt="É grande, azul, com uma fita vermelha.", ok=False, fb="Ninguém perguntou da mala ainda."),
   dict(en="I can't find my suitcase.", pt="Não encontro minha mala.", ok=False, fb="Ainda é cedo: você nem chegou à esteira.")]),
  dict(npc="Belt number four.", pt="Esteira número quatro.", opts=[
   dict(en="Follow the signs.", pt="Siga as placas.", ok=False, fb="Essa fala é dela."),
   dict(en="Thank you. I can't find my suitcase.", pt="Obrigada. Não encontro minha mala.", ok=True, fb="Explica o problema."),
   dict(en="Where is the exit?", pt="Onde fica a saída?", ok=False, fb="Ela já respondeu; diga qual é o seu problema.")]),
  dict(npc="What does it look like?", pt="Como ela é?", opts=[
   dict(en="It's not here.", pt="Não está aqui.", ok=False, fb="Não descreve a mala."),
   dict(en="Which belt is it?", pt="Qual esteira é?", ok=False, fb="Ela já disse: quatro."),
   dict(en="It's big, blue, with a red ribbon.", pt="É grande, azul, com uma fita vermelha.", ok=True, fb="Descreve a mala.")]),
  dict(npc="Let's check the other belts.", pt="Vamos ver nas outras esteiras.", opts=[
   dict(en="It's not here. Where can I ask?", pt="Não está aqui. Onde posso perguntar?", ok=True, fb="Pede onde reportar."),
   dict(en="Where is baggage claim?", pt="Onde fica a esteira?", ok=False, fb="Você já está lá."),
   dict(en="It's big, blue, with a red ribbon.", pt="É grande, azul, com uma fita vermelha.", ok=False, fb="Já descreveu.")]),
 ]),
)
