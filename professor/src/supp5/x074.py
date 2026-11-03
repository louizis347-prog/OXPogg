X = dict(
 key=dict(big="Can I try them on?", label="Posso experimentar?", sub="Frase útil em qualquer loja de sapatos. Depois de provar, o vendedor pergunta como os sapatos estão, e você responde com feel + adjetivo."),
 mini=[
  dict(who="Evan", en="Hi! I need {running shoes|boots|sneakers}.", pt="Oi! Preciso de {tênis de corrida|botas|tênis}."),
  dict(who="You", en="What size?", pt="Que número?"),
  dict(who="Evan", en="Size {ten|nine|eleven}. Can I try them on?", pt="Número {dez|nove|onze}. Posso experimentar?"),
  dict(who="You", en="Sure. How do they {feel|fit|look}?", pt="Claro. Como {estão|servem|ficaram}?"),
 ],
 dlg=[
  dict(who="Evan", en="Hi! I need {running shoes.|sneakers.|boots.}", pt="Oi! Preciso de {tênis de corrida.|tênis.|botas.}"),
  dict(who="You", en="What {size?|number?}", pt="Que {número?|número?}"),
  dict(who="Evan", en="Size {ten.|nine.|eleven.}", pt="Número {dez.|nove.|onze.}"),
  dict(who="You", en="Let me check. Here's a {pair.|box.}", pt="Vou ver. Aqui está {um par.|uma caixa.}"),
  dict(who="Evan", en="Can I try {them|these} on?", pt="Posso {experimentá-los?|experimentar estes?}"),
  dict(who="You", en="Sure. How do they {feel?|fit?}", pt="Claro. Como {estão?|servem?}"),
  dict(who="Evan", en="A little {tight.|big.|small.}", pt="Um pouco {apertados.|grandes.|pequenos.}"),
  dict(who="You", en="Try size {ten and a half.|nine and a half.}", pt="Experimente o {dez e meio.|nove e meio.}"),
  dict(who="Evan", en="Great choice. Enjoy your {shoes!|sneakers!}", pt="Ótima escolha. Aproveite {os sapatos!|os tênis!}"),
 ],
 vocab=[
  dict(w="laces", pt="cadarços", e="🪢", ex=["The laces are white.", "Tie your laces first."]),
  dict(w="boots", pt="botas", e="🥾", ex=["I need boots for the snow.", "The boots are brown."]),
  dict(w="socks", pt="meias", e="🧦", ex=["Put on your socks.", "These socks are white."]),
  dict(w="sneakers", pt="tênis", e="👟", ex=["I wear sneakers every day.", "The sneakers are comfortable."]),
  dict(w="pair", pt="par", e="👯", ex=["A pair of shoes, please.", "I have a new pair."]),
  dict(w="tight", pt="apertado", e="😣", ex=["The shoes are too tight.", "They feel a little tight."]),
 ],
 molds=[
  dict(title="Pedir o número", frame="I need {item} in size {size}.", slots=[dict(key="item", opts=["running shoes", "sneakers", "boots"]), dict(key="size", opts=["ten", "nine", "eight"])], model="I need running shoes in size ten.", note="Size + número. Shoes, sneakers e boots são plurais; não use a antes."),
  dict(title="Dizer como estão", frame="They feel {adj}.", slots=[dict(key="adj", opts=["tight", "big", "great", "comfortable"])], model="They feel tight.", note="Feel + adjetivo: they feel tight = estão apertados. Para um tênis só: it feels."),
  dict(title="Escrever sobre a compra", frame="I bought {item} in size {size}. They feel {adj}!", slots=[dict(key="item", opts=["sneakers", "boots", "running shoes"]), dict(key="size", opts=["ten", "nine", "eight"]), dict(key="adj", opts=["great", "comfortable", "perfect"])], model="I bought sneakers in size ten. They feel great!", note="Bought é o passado de buy. They feel great = eles estão ótimos."),
 ],
 sounds=[
  dict(say="Can I try them on?", tag="ligação: try them on", tip="Try them on soa 'trai-them-on'. Them fica fraco: 'dem'."),
  dict(say="How do they feel?", tag="ritmo: palavras fortes", tip="Bata HOW e FEEL. 'Do they' é rápido: 'dthey'."),
  dict(say="A little tight.", tag="som: t entre vogais", tip="Little soa 'lidl'. O tt vira um 'd' leve em inglês americano."),
 ],
 role=dict(turns=[
  dict(npc="Hi! I need running shoes.", opts=[
   dict(en="Sure. What size?", pt="Claro. Que número?", reply="Size ten."),
   dict(en="Hello! What size are you?", pt="Olá! Qual é o seu número?", reply="Size ten."),
   dict(en="Of course. What size?", pt="Claro. Que número?", reply="Size ten, please.")]),
  dict(npc="Size ten.", opts=[
   dict(en="Let me check. Here's a pair.", pt="Vou ver. Aqui está um par.", reply="Thanks! Can I try them on?"),
   dict(en="One moment. Here are some in ten.", pt="Um momento. Aqui estão alguns no dez.", reply="Thanks! Can I try them on?"),
   dict(en="Let me look. Here you go.", pt="Vou olhar. Aqui está.", reply="Thanks! Can I try them on?")]),
  dict(npc="Can I try them on?", opts=[
   dict(en="Sure. How do they feel?", pt="Claro. Como estão?", reply="A little tight."),
   dict(en="Of course. Are they comfortable?", pt="Claro. Estão confortáveis?", reply="A little tight, I think."),
   dict(en="Yes. How do they feel?", pt="Sim. Como estão?", reply="They feel a little tight.")]),
  dict(npc="A little tight.", opts=[
   dict(en="Try size ten and a half.", pt="Experimente o dez e meio.", reply="Great choice. Enjoy your shoes!"),
   dict(en="Let me get a bigger size.", pt="Vou buscar um número maior.", reply="Great choice. Enjoy your shoes!"),
   dict(en="Try the next size up.", pt="Experimente o número seguinte.", reply="Great choice. Enjoy your shoes!")]),
 ], change=["O cliente quer botas, não tênis: pergunte o número e a cor.", "Não há o número dez e meio: ofereça outro modelo.", "Os sapatos estão grandes: sugira um número menor ou meias mais grossas."]),
 writing=dict(task="Você compra sapatos. Escreva 2 ou 3 frases: diga o que precisa, o seu número e como os sapatos estão.", model="Hi! I need running shoes in size ten. I tried them on. They feel a little tight, so I need size ten and a half.", kw=["shoes", "size", "tight", "try"], checks=["Disse o que precisa.", "Disse o número.", "Disse como os sapatos estão."]),
 scenes=dict(pool=["shop", "counter", "street", "market"], npc=dict(g="m", role="clerk"), you=dict(g="m")),
 convo=dict(npc=dict(name="Evan"), story="Você trabalha numa sapataria em Detroit. O Evan é o cliente e procura tênis de corrida.", turns=[
  dict(npc="Hi! I need running shoes.", pt="Oi! Preciso de tênis de corrida.", opts=[
   dict(en="Great choice. Enjoy your shoes!", pt="Ótima escolha. Aproveite os sapatos!", ok=False, fb="Essa frase é para o final da compra."),
   dict(en="What size?", pt="Que número?", ok=True, fb="O vendedor pergunta o número primeiro."),
   dict(en="A little tight.", pt="Um pouco apertados.", ok=False, fb="Ele ainda não provou nada.")]),
  dict(npc="Size ten.", pt="Número dez.", opts=[
   dict(en="Let me check. Here's a pair.", pt="Vou ver. Aqui está um par.", ok=True, fb="Vai buscar e traz o par."),
   dict(en="What size?", pt="Que número?", ok=False, fb="Ele acabou de dizer: dez."),
   dict(en="Can I try them on?", pt="Posso experimentar?", ok=False, fb="Essa pergunta é do cliente.")]),
  dict(npc="Can I try them on?", pt="Posso experimentar?", opts=[
   dict(en="Try size ten and a half.", pt="Experimente o dez e meio.", ok=False, fb="Ainda não sabemos se está apertado."),
   dict(en="Sure. How do they feel?", pt="Claro. Como estão?", ok=True, fb="Permite e pergunta como estão."),
   dict(en="Size ten.", pt="Número dez.", ok=False, fb="O número já foi dito.")]),
  dict(npc="A little tight.", pt="Um pouco apertados.", opts=[
   dict(en="Try size ten and a half.", pt="Experimente o dez e meio.", ok=True, fb="Sugere o número maior."),
   dict(en="Sure. How do they feel?", pt="Claro. Como estão?", ok=False, fb="Ele já respondeu como estão."),
   dict(en="Hi! I need running shoes.", pt="Oi! Preciso de tênis de corrida.", ok=False, fb="Essa fala é do cliente, no começo.")]),
  dict(npc="Great choice. Enjoy your shoes!", pt="Ótima escolha. Aproveite os sapatos!", opts=[
   dict(en="Thank you! Come back soon.", pt="Obrigado! Volte sempre.", ok=True, fb="Agradece e comenta."),
   dict(en="What size?", pt="Que número?", ok=False, fb="A compra já terminou."),
   dict(en="Can I try them on?", pt="Posso experimentar?", ok=False, fb="Ele já provou e escolheu.")]),
 ]),
)
