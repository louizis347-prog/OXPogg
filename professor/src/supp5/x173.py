X = dict(
 key=dict(big="A cheeseburger meal, please", label="Pedir no drive-thru", sub="Peça com frases curtas e na ordem: o prato, o tamanho da bebida, o acompanhamento e, no final, se quer mais algo."),
 mini=[
  dict(who="Kai", en="Welcome! What can I {get|bring|give} you?", pt="Bem-vindo! O que posso {pegar|trazer|dar} para você?"),
  dict(who="You", en="A {cheeseburger|chicken|fish} meal, please.", pt="Um combo de {cheeseburger|frango|peixe}, por favor."),
  dict(who="Kai", en="What size {drink?|cola?|juice?}", pt="Que tamanho de {bebida?|cola?|suco?}"),
  dict(who="You", en="{Small|Medium|Large}, with {cola.|juice.|water.}", pt="{Pequeno|Médio|Grande}, com {cola.|suco.|água.}"),
 ],
 dlg=[
  dict(who="Kai", en="Welcome! What can I {get|give} you?", pt="Bem-vindo! O que posso {pegar|dar} para você?"),
  dict(who="You", en="Hi. A {cheeseburger|chicken} meal, please.", pt="Oi. Um combo de {cheeseburger|frango}, por favor."),
  dict(who="Kai", en="What size {drink?|cola?}", pt="Que tamanho de {bebida?|cola?}"),
  dict(who="You", en="{Medium,|Small,|Large,} with {cola.|juice.}", pt="{Médio,|Pequeno,|Grande,} com {cola.|suco.}"),
  dict(who="Kai", en="Any {sides?|extras?} Fries or salad?", pt="Algum {acompanhamento?|extra?} Fritas ou salada?"),
  dict(who="You", en="{Fries,|Salad,} please.", pt="{Fritas,|Salada,} por favor."),
  dict(who="Kai", en="Anything {else?|more?}", pt="Mais {alguma coisa?|alguma coisa?}"),
  dict(who="You", en="An apple {pie,|pie} too.", pt="Uma torta de maçã {também.|também.}"),
  dict(who="Kai", en="That's {nine fifty.|ten dollars.} Pull {forward.|ahead.}", pt="São {nove e cinquenta.|dez dólares.} Siga {em frente.|adiante.}"),
 ],
 vocab=[
  dict(w="meal", pt="combo, refeição", e="🍔", ex=["I want a burger meal.", "The meal is nine dollars."]),
  dict(w="speaker", pt="alto-falante", e="🔊", ex=["Talk to the speaker.", "The speaker is loud."]),
  dict(w="straw", pt="canudo", e="🥤", ex=["Can I have a straw?", "The straw is red."]),
  dict(w="nuggets", pt="nuggets (pedacinhos de frango)", e="🍗", ex=["I want six nuggets.", "The nuggets are hot."]),
  dict(w="extra", pt="extra, a mais", e="➕", ex=["I want extra ketchup.", "Extra cheese, please."]),
  dict(w="dessert", pt="sobremesa", e="🍰", ex=["I want a dessert.", "The dessert is sweet."]),
 ],
 molds=[
  dict(title="Pedir o combo", frame="A {food} meal, please.", slots=[dict(key="food", opts=["cheeseburger", "chicken", "fish"])], model="A cheeseburger meal, please.", note="A + prato + meal, please é o jeito mais simples e educado de pedir."),
  dict(title="Dizer tamanho e bebida", frame="{size}, with {drink}.", slots=[dict(key="size", opts=["Small", "Medium", "Large"]), dict(key="drink", opts=["cola", "juice", "water"])], model="Small, with cola.", note="Primeiro o tamanho, depois with + bebida."),
  dict(title="Escrever o pedido completo", frame="Hi. A {food} meal, {size}, with {side}. {extra}, please.", slots=[dict(key="food", opts=["cheeseburger", "chicken", "fish"]), dict(key="size", opts=["small", "medium", "large"]), dict(key="side", opts=["fries", "salad", "nuggets"]), dict(key="extra", opts=["Extra ketchup", "Extra sauce", "A straw"])], model="Hi. A cheeseburger meal, small, with fries. Extra ketchup, please.", note="Escreva o pedido em ordem. Please no final deixa tudo educado."),
 ],
 sounds=[
  dict(say="What can I get you?", tag="ligação: can I", tip="Una can e I: 'kenai'. Acentue WHAT e GET."),
  dict(say="Fries, please.", tag="som: z final", tip="Fries termina com z, não 's' seco. Faça a garganta vibrar."),
  dict(say="Medium, with cola.", tag="ritmo: MEdium WITH COla", tip="Acentue ME, WITH e CO; 'with' fica curto e firme."),
 ],
 role=dict(turns=[
  dict(npc="Welcome! What can I get you?", opts=[
   dict(en="Hi. A cheeseburger meal, please.", pt="Oi. Um combo de cheeseburger, por favor.", reply="What size drink?"),
   dict(en="Hi. A chicken meal, please.", pt="Oi. Um combo de frango, por favor.", reply="What size drink?"),
   dict(en="Hi. Six nuggets, please.", pt="Oi. Seis nuggets, por favor.", reply="What size drink?")]),
  dict(npc="What size drink?", opts=[
   dict(en="Medium, with cola.", pt="Médio, com cola.", reply="Any sides? Fries or salad?"),
   dict(en="Small, with water.", pt="Pequeno, com água.", reply="Any sides? Fries or salad?"),
   dict(en="Large, with juice.", pt="Grande, com suco.", reply="Any sides? Fries or salad?")]),
  dict(npc="Any sides? Fries or salad?", opts=[
   dict(en="Fries, please.", pt="Fritas, por favor.", reply="Anything else?"),
   dict(en="Salad, please.", pt="Salada, por favor.", reply="Anything else?"),
   dict(en="Fries, and extra ketchup.", pt="Fritas, e ketchup extra.", reply="Sure. Anything else?")]),
  dict(npc="Anything else?", opts=[
   dict(en="An apple pie, too.", pt="Uma torta de maçã também.", reply="That's nine fifty. Pull forward."),
   dict(en="A straw, please.", pt="Um canudo, por favor.", reply="Sure. That's nine dollars. Pull forward."),
   dict(en="No, that's all.", pt="Não, é só isso.", reply="That's eight fifty. Pull forward.")]),
 ], change=["O atendente não entendeu bem: repita seu pedido mais devagar.", "Acabou a cola: escolha outra bebida.", "Você pediu um item errado: peça para trocar."]),
 writing=dict(task="Escreva 2 ou 3 frases com seu pedido no drive-thru: o combo, o tamanho da bebida e o acompanhamento.", model="Hi. A chicken meal, please. A small drink, with water, and fries. Thank you.", kw=["meal", "please", "with", "fries"], checks=["Pediu um combo.", "Disse o tamanho e a bebida.", "Escolheu o acompanhamento."]),
 scenes=dict(pool=["street", "market", "counter", "cafe"], npc=dict(g="m", role="cashier"), you=dict(g="f")),
 convo=dict(npc=dict(name="Kai"), story="Você está de carro em um drive-thru em Phoenix. O Kai atende no alto-falante.", turns=[
  dict(npc="Welcome! What can I get you?", pt="Bem-vindo! O que vai querer?", opts=[
   dict(en="Anything else?", pt="Mais alguma coisa?", ok=False, fb="Quem pergunta isso é o atendente."),
   dict(en="Hi. A cheeseburger meal, please.", pt="Oi. Um combo de cheeseburger, por favor.", ok=True, fb="Pedido claro e educado."),
   dict(en="Pull forward.", pt="Siga em frente.", ok=False, fb="Essa fala é do atendente, no fim.")]),
  dict(npc="What size drink?", pt="Que tamanho de bebida?", opts=[
   dict(en="Medium, with cola.", pt="Médio, com cola.", ok=True, fb="Tamanho + bebida."),
   dict(en="Fries or salad?", pt="Fritas ou salada?", ok=False, fb="Quem pergunta isso é o atendente."),
   dict(en="A cheeseburger meal, please.", pt="Um combo de cheeseburger, por favor.", ok=False, fb="Você já pediu o combo.")]),
  dict(npc="Any sides? Fries or salad?", pt="Algum acompanhamento? Fritas ou salada?", opts=[
   dict(en="That's nine fifty.", pt="São nove e cinquenta.", ok=False, fb="O preço é dito por ele."),
   dict(en="Medium, with cola.", pt="Médio, com cola.", ok=False, fb="Você já escolheu a bebida."),
   dict(en="Fries, please.", pt="Fritas, por favor.", ok=True, fb="Escolhe o acompanhamento.")]),
  dict(npc="Anything else?", pt="Mais alguma coisa?", opts=[
   dict(en="Welcome to the drive-thru!", pt="Bem-vindo ao drive-thru!", ok=False, fb="Quem dá as boas-vindas é o atendente."),
   dict(en="Fries, please.", pt="Fritas, por favor.", ok=False, fb="Você já pediu as fritas."),
   dict(en="An apple pie, too.", pt="Uma torta de maçã também.", ok=True, fb="Acrescenta mais um item.")]),
  dict(npc="That's nine fifty. Pull forward.", pt="São nove e cinquenta. Siga em frente.", opts=[
   dict(en="Okay. Thank you!", pt="Certo. Obrigado!", ok=True, fb="Fecha o pedido com educação."),
   dict(en="What size drink?", pt="Que tamanho de bebida?", ok=False, fb="Quem pergunta isso é o atendente."),
   dict(en="Any sides?", pt="Algum acompanhamento?", ok=False, fb="Essa pergunta é dele e já foi respondida.")]),
 ]),
)
