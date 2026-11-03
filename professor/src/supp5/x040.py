X = dict(
 key=dict(big="I'd like a pizza for takeout", label="Pedir para viagem por telefone", sub="Takeout (ou to go) é comida para levar; ao telefone, diga o pedido, o nome e espere o tempo de preparo."),
 mini=[
  dict(who="Chloe", en="Joe's Pizza. How can I {help you|help you today|help}?", pt="Joe's Pizza. Como posso {ajudar|ajudar hoje|ajudar}?"),
  dict(who="You", en="Hi. I'd like a {large|medium|small} pizza for takeout.", pt="Oi. Eu gostaria de uma pizza {grande|média|pequena} para viagem."),
  dict(who="Chloe", en="What kind of pizza? We have {cheese|pepperoni|mushroom}.", pt="Que tipo de pizza? Temos {queijo|pepperoni|cogumelo}."),
  dict(who="You", en="Half cheese, half {pepperoni|mushroom|cheese}.", pt="Metade queijo, metade {pepperoni|cogumelo|queijo}."),
 ],
 dlg=[
  dict(who="Chloe", en="Joe's Pizza. How can I {help you|help you today}?", pt="Joe's Pizza. Como posso {ajudar|ajudar hoje}?"),
  dict(who="You", en="Hi. I'd like a {large|medium|small} pizza for takeout.", pt="Oi. Eu gostaria de uma pizza {grande|média|pequena} para viagem."),
  dict(who="Chloe", en="What {kind of pizza?|type of pizza?}", pt="Que {tipo de pizza?|tipo de pizza?}"),
  dict(who="You", en="Half {cheese|mushroom}, half pepperoni.", pt="Metade {queijo|cogumelo}, metade pepperoni."),
  dict(who="Chloe", en="Anything else?", pt="Mais alguma coisa?"),
  dict(who="You", en="A {bottle of soda|bottle of water}, please.", pt="Uma {garrafa de refrigerante|garrafa de água}, por favor."),
  dict(who="Chloe", en="It'll be {twenty|thirty|fifteen} minutes.", pt="Fica pronto em {vinte|trinta|quinze} minutos."),
  dict(who="You", en="Great. My name is {Sam.|Sam Lopez.}", pt="Ótimo. Meu nome é {Sam.|Sam Lopez.}"),
  dict(who="Chloe", en="Your order will be ready {soon!|in a few minutes!}", pt="Seu pedido ficará pronto {logo!|em poucos minutos!}"),
 ],
 vocab=[
  dict(w="order", pt="pedido", e="📝", ex=["I'd like to place an order.", "Your order is ready."]),
  dict(w="pickup", pt="retirada", e="🛍️", ex=["Pickup is at the counter.", "Is this for pickup or delivery?"]),
  dict(w="delivery", pt="entrega", e="🛵", ex=["Do you do delivery?", "The delivery is thirty minutes."]),
  dict(w="bottle", pt="garrafa", e="🍾", ex=["A bottle of water, please.", "The bottle is cold."]),
  dict(w="minute", pt="minuto", e="⏱️", ex=["It'll be ten minutes.", "Wait one minute, please."]),
  dict(w="pizza", pt="pizza", e="🍕", ex=["I'd like a large pizza.", "The pizza is hot."]),
 ],
 molds=[
  dict(title="Pedir a pizza", frame="I'd like a {size} pizza for takeout.", slots=[dict(key="size", opts=["large", "medium", "small"])], model="I'd like a large pizza for takeout.", note="For takeout = para levar. I'd like é educado, bom para telefone."),
  dict(title="Escolher os sabores", frame="Half cheese, half {b}.", slots=[dict(key="b", opts=["pepperoni", "mushroom", "sausage"])], model="Half cheese, half pepperoni.", note="Half... half... = metade... metade... Combine dois sabores na mesma pizza."),
  dict(title="Escrever o pedido", frame="Hi! I'd like {food} for {how}, please. My name is {name}.", slots=[dict(key="food", opts=["a large pizza", "a medium pizza", "two pizzas"]), dict(key="how", opts=["pickup", "takeout", "delivery"]), dict(key="name", opts=["Sam", "Ana", "Leo"])], model="Hi! I'd like a large pizza for pickup, please. My name is Sam.", note="Diga o pedido, retirada ou entrega, e o seu nome."),
 ],
 sounds=[
  dict(say="I'd like a large pizza.", tag="ligação: like a", tip="Like a soa 'laika'. Acentue LARGE e PIZ-za."),
  dict(say="What kind of pizza?", tag="ligação: kind of", tip="Kind of vira 'kaindev'. Una as palavras."),
  dict(say="It'll be twenty minutes.", tag="ligação: it'll be", tip="It'll be soa 'itlbi'. Acentue TWEN-ty MIN-utes."),
 ],
 role=dict(turns=[
  dict(npc="Joe's Pizza. How can I help you?", opts=[
   dict(en="Hi. I'd like a large pizza for takeout.", pt="Oi. Eu gostaria de uma pizza grande para viagem.", reply="Sure! What kind of pizza?"),
   dict(en="Hi. I'd like a medium pizza for pickup.", pt="Oi. Eu gostaria de uma pizza média para retirar.", reply="Sure! What kind of pizza?"),
   dict(en="Hello. Can I order a pizza for takeout?", pt="Olá. Posso pedir uma pizza para viagem?", reply="Of course. What kind of pizza?")]),
  dict(npc="What kind of pizza?", opts=[
   dict(en="Half cheese, half pepperoni.", pt="Metade queijo, metade pepperoni.", reply="Half cheese, half pepperoni. Anything else?"),
   dict(en="Cheese, please.", pt="Queijo, por favor.", reply="One cheese pizza. Anything else?"),
   dict(en="Half mushroom, half cheese.", pt="Metade cogumelo, metade queijo.", reply="Half mushroom, half cheese. Anything else?")]),
  dict(npc="Anything else?", opts=[
   dict(en="A bottle of soda, please.", pt="Uma garrafa de refrigerante, por favor.", reply="A bottle of soda. It'll be twenty minutes."),
   dict(en="A bottle of water, please.", pt="Uma garrafa de água, por favor.", reply="A bottle of water. It'll be twenty minutes."),
   dict(en="No, that's all.", pt="Não, é só isso.", reply="Okay. It'll be twenty minutes.")]),
  dict(npc="It'll be twenty minutes. Can I have a name for the order?", opts=[
   dict(en="Great. My name is Sam.", pt="Ótimo. Meu nome é Sam.", reply="Thanks, Sam. Your order will be ready soon!"),
   dict(en="Okay. It's Sam.", pt="Ok. É Sam.", reply="Thanks, Sam. Your order will be ready soon!"),
   dict(en="Perfect. The name is Sam.", pt="Perfeito. O nome é Sam.", reply="Got it, Sam. See you in twenty minutes!")]),
 ], change=["A pizzaria diz que vai demorar quarenta minutos: pergunte se pode ser mais rápido ou aceite.", "Você quer entrega, não retirada: peça delivery e dê o endereço.", "Não há pepperoni hoje: escolha outro sabor."]),
 writing=dict(task="Você liga para uma pizzaria. Escreva 2 ou 3 frases: peça uma pizza para viagem, diga os sabores e o seu nome.", model="Hi! I'd like a large pizza for takeout. Half cheese, half pepperoni, please. My name is Sam.", kw=["pizza", "takeout", "cheese", "name"], checks=["Pediu a pizza para takeout.", "Disse os sabores.", "Disse o seu nome."]),
 scenes=dict(pool=["diner", "restaurant", "counter", "street"], npc=dict(g="f", role="cashier"), you=dict(g="m")),
 convo=dict(npc=dict(name="Chloe"), story="Você liga para uma pizzaria para pedir comida para viagem.", turns=[
  dict(npc="Joe's Pizza. How can I help you?", pt="Joe's Pizza. Como posso ajudar?", opts=[
   dict(en="Hi. I'd like a large pizza for takeout.", pt="Oi. Eu gostaria de uma pizza grande para viagem.", ok=True, fb="Faz o pedido de forma clara e educada."),
   dict(en="Your order will be ready soon!", pt="Seu pedido ficará pronto logo!", ok=False, fb="Esta frase é da pizzaria, no fim."),
   dict(en="Goodbye. Have a nice day.", pt="Tchau. Tenha um bom dia.", ok=False, fb="Você acabou de ligar; ainda não fez o pedido.")]),
  dict(npc="What kind of pizza?", pt="Que tipo de pizza?", opts=[
   dict(en="A large one, please.", pt="Uma grande, por favor.", ok=False, fb="O tamanho já foi dito; ela quer saber o sabor."),
   dict(en="Half cheese, half pepperoni.", pt="Metade queijo, metade pepperoni.", ok=True, fb="Diz os sabores com a estrutura half... half..."),
   dict(en="My name is Sam.", pt="Meu nome é Sam.", ok=False, fb="O nome é pedido depois do pedido.")]),
  dict(npc="Anything else?", pt="Mais alguma coisa?", opts=[
   dict(en="A bottle of soda, please.", pt="Uma garrafa de refrigerante, por favor.", ok=True, fb="Acrescenta uma bebida."),
   dict(en="It'll be twenty minutes.", pt="Fica pronto em vinte minutos.", ok=False, fb="Essa frase é de quem atende."),
   dict(en="Yes, I'm a pizza.", pt="Sim, eu sou uma pizza.", ok=False, fb="Não faz sentido; peça um item extra ou diga que é só isso.")]),
  dict(npc="It'll be twenty minutes.", pt="Fica pronto em vinte minutos.", opts=[
   dict(en="Great. My name is Sam.", pt="Ótimo. Meu nome é Sam.", ok=True, fb="Aceita o tempo e dá o nome para o pedido."),
   dict(en="Anything else?", pt="Mais alguma coisa?", ok=False, fb="Quem pergunta isso é a atendente."),
   dict(en="What kind of pizza?", pt="Que tipo de pizza?", ok=False, fb="Esta pergunta é dela e já foi respondida.")]),
  dict(npc="Your order will be ready soon!", pt="Seu pedido ficará pronto logo!", opts=[
   dict(en="Thank you! Bye!", pt="Obrigado! Tchau!", ok=True, fb="Fecha a ligação com educação."),
   dict(en="Joe's Pizza. How can I help you?", pt="Joe's Pizza. Como posso ajudar?", ok=False, fb="Essa fala é de quem atende o telefone."),
   dict(en="Half cheese, half pepperoni.", pt="Metade queijo, metade pepperoni.", ok=False, fb="O pedido já foi feito.")]),
 ]),
)
