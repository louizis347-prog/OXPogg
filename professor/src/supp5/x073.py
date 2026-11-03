X = dict(
 key=dict(big="What size are you?", label="Qual é o seu tamanho?", sub="A pergunta básica numa loja de roupas. Responda com I'm a + tamanho (small, medium, large); o número pode variar conforme a marca."),
 mini=[
  dict(who="Marco", en="Hi! Can I help you?", pt="Oi! Posso ajudar?"),
  dict(who="You", en="Yes, I'm looking for a {T-shirt|jacket|dress}.", pt="Sim, estou procurando {uma camiseta|uma jaqueta|um vestido}."),
  dict(who="Marco", en="What size are you?", pt="Qual é seu tamanho?"),
  dict(who="You", en="I'm a {medium|small|large}. Do you have it in {blue|black|gray}?", pt="Eu sou {M|P|G}. Tem em {azul|preto|cinza}?"),
 ],
 dlg=[
  dict(who="Marco", en="Hi! Can I {help you?|help?}", pt="Oi! Posso {ajudar?|ajudar?}"),
  dict(who="You", en="Yes, I'm looking for a {T-shirt.|jacket.|dress.}", pt="Sim, estou procurando {uma camiseta.|uma jaqueta.|um vestido.}"),
  dict(who="Marco", en="What {size|number} are you?", pt="Qual é seu {tamanho?|tamanho?}"),
  dict(who="You", en="I'm a {medium.|small.|large.}", pt="Eu sou {M.|P.|G.}"),
  dict(who="Marco", en="Here are some in {medium.|small.}", pt="Aqui estão algumas no {M.|P.}"),
  dict(who="You", en="Do you have it in {blue?|black?|gray?}", pt="Tem em {azul?|preto?|cinza?}"),
  dict(who="Marco", en="Yes, here {you go.|it is.}", pt="Tem, {aqui está.|aqui está.}"),
  dict(who="You", en="Where can I {try it on?|find a fitting room?}", pt="Onde posso {provar?|achar um provador?}"),
  dict(who="Marco", en="Thanks for {shopping|buying} with us!", pt="Obrigado por {comprar|comprar} conosco!"),
 ],
 vocab=[
  dict(w="jeans", pt="jeans", e="👖", ex=["I need a new pair of jeans.", "These jeans are too long."]),
  dict(w="dress", pt="vestido", e="👗", ex=["She wears a red dress.", "The dress is in the window."]),
  dict(w="jacket", pt="jaqueta", e="🧥", ex=["The jacket is warm.", "I like this black jacket."]),
  dict(w="shirt", pt="camisa", e="👔", ex=["The shirt is blue.", "Try this shirt on."]),
  dict(w="medium", pt="médio (M)", e="📏", ex=["I'm a medium.", "Do you have this in medium?"]),
  dict(w="fitting room", pt="provador", e="🚪", ex=["The fitting room is on the left.", "Take the shirts to the fitting room."]),
 ],
 molds=[
  dict(title="Dizer o que procura", frame="I'm looking for a {item}.", slots=[dict(key="item", opts=["T-shirt", "jacket", "dress", "shirt"])], model="I'm looking for a T-shirt.", note="Looking for = procurando. Para jeans (plural), diga: I'm looking for jeans, sem a."),
  dict(title="Dizer o tamanho e a cor", frame="I'm a {size}. Do you have it in {color}?", slots=[dict(key="size", opts=["medium", "small", "large"]), dict(key="color", opts=["blue", "black", "gray"])], model="I'm a medium. Do you have it in blue?", note="I'm a + tamanho. Do you have it in + cor? é a pergunta natural para outra cor."),
  dict(title="Escrever a sua compra", frame="I bought a {color} {item} in size {size}. It fits {how}!", slots=[dict(key="color", opts=["blue", "black", "gray"]), dict(key="item", opts=["shirt", "jacket", "dress"]), dict(key="size", opts=["medium", "small", "large"]), dict(key="how", opts=["me", "well", "perfectly"])], model="I bought a blue shirt in size medium. It fits me!", note="Bought é o passado de buy. It fits me = serve em mim."),
 ],
 sounds=[
  dict(say="Do you have it in blue?", tag="redução: do you", tip="Do you vira 'dyu'. Una have it: 'havit'. Acentue BLUE."),
  dict(say="What size are you?", tag="ligação: size are", tip="Size are soa 'saizar'. A voz sobe no final, como numa pergunta."),
  dict(say="Where can I try it on?", tag="ligação: try it on", tip="Try it on soa 'trai-ton'. Una as três palavras sem pausa."),
 ],
 role=dict(turns=[
  dict(npc="Hi! Can I help you?", opts=[
   dict(en="Yes, I'm looking for a T-shirt.", pt="Sim, estou procurando uma camiseta.", reply="Sure! What size are you?"),
   dict(en="Yes, I'm looking for a jacket.", pt="Sim, estou procurando uma jaqueta.", reply="Sure! What size are you?"),
   dict(en="Yes, I need a dress, please.", pt="Sim, preciso de um vestido, por favor.", reply="Sure! What size are you?")]),
  dict(npc="What size are you?", opts=[
   dict(en="I'm a medium.", pt="Eu sou M.", reply="Here are some in medium."),
   dict(en="I'm a small.", pt="Eu sou P.", reply="Here are some in small."),
   dict(en="I think I'm a large.", pt="Acho que sou G.", reply="Here are some in large.")]),
  dict(npc="Here are some in your size.", opts=[
   dict(en="Do you have it in blue?", pt="Tem em azul?", reply="Yes, here you go."),
   dict(en="Do you have it in black?", pt="Tem em preto?", reply="Yes, here you go."),
   dict(en="Do you have it in gray?", pt="Tem em cinza?", reply="Yes, here you go.")]),
  dict(npc="Yes, here you go.", opts=[
   dict(en="Where can I try it on?", pt="Onde posso provar?", reply="The fitting room is on the left. Thanks for shopping with us!"),
   dict(en="Can I try it on, please?", pt="Posso provar, por favor?", reply="Of course! The fitting room is over there. Thanks for shopping with us!"),
   dict(en="Is there a fitting room?", pt="Tem provador?", reply="Yes, it's on the left. Thanks for shopping with us!")]),
 ], change=["A camiseta ficou grande: peça um tamanho menor.", "A cor que você quer não tem: escolha outra cor.", "Você gostou, mas é caro: pergunte se está em promoção."]),
 writing=dict(task="Você está numa loja de roupas. Escreva 2 ou 3 frases: diga o que procura, o seu tamanho e peça outra cor.", model="Hi! I'm looking for a shirt. I'm a medium. Do you have it in blue, please?", kw=["looking", "medium", "blue", "shirt"], checks=["Disse o que procura.", "Disse o seu tamanho.", "Perguntou por outra cor."]),
 scenes=dict(pool=["shop", "counter", "street", "market"], npc=dict(g="m", role="clerk"), you=dict(g="f")),
 convo=dict(npc=dict(name="Marco"), story="Você está numa loja de roupas em Los Angeles. O Marco é o vendedor.", turns=[
  dict(npc="Hi! Can I help you?", pt="Oi! Posso ajudar?", opts=[
   dict(en="Thanks for shopping with us!", pt="Obrigado por comprar conosco!", ok=False, fb="Essa frase é do vendedor, no final."),
   dict(en="Yes, I'm looking for a T-shirt.", pt="Sim, estou procurando uma camiseta.", ok=True, fb="Diz o que você procura."),
   dict(en="I'm a medium.", pt="Eu sou M.", ok=False, fb="Ainda não perguntaram seu tamanho.")]),
  dict(npc="What size are you?", pt="Qual é seu tamanho?", opts=[
   dict(en="Yes, here you go.", pt="Tem, aqui está.", ok=False, fb="Essa fala é de quem entrega algo."),
   dict(en="I'm looking for a T-shirt.", pt="Estou procurando uma camiseta.", ok=False, fb="Você já disse isso; agora é o tamanho."),
   dict(en="I'm a medium.", pt="Eu sou M.", ok=True, fb="Responde o tamanho com I'm a...")]),
  dict(npc="Here are some in medium.", pt="Aqui estão algumas no M.", opts=[
   dict(en="Do you have it in blue?", pt="Tem em azul?", ok=True, fb="Pede outra cor com educação."),
   dict(en="What size are you?", pt="Qual é seu tamanho?", ok=False, fb="Essa pergunta é do vendedor."),
   dict(en="I'm a medium.", pt="Eu sou M.", ok=False, fb="O tamanho já foi dito.")]),
  dict(npc="Yes, here you go.", pt="Tem, aqui está.", opts=[
   dict(en="Where can I try it on?", pt="Onde posso provar?", ok=True, fb="Pergunta onde fica o provador."),
   dict(en="Hi! Can I help you?", pt="Oi! Posso ajudar?", ok=False, fb="Quem pergunta isso é o vendedor, no começo."),
   dict(en="I'm looking for a dress.", pt="Estou procurando um vestido.", ok=False, fb="Você já tem a camiseta na mão.")]),
  dict(npc="Thanks for shopping with us!", pt="Obrigado por comprar conosco!", opts=[
   dict(en="Where can I try it on?", pt="Onde posso provar?", ok=False, fb="Muito tarde; você está indo embora."),
   dict(en="Thank you! Bye!", pt="Obrigada! Tchau!", ok=True, fb="Despedida simples e educada."),
   dict(en="Do you have it in blue?", pt="Tem em azul?", ok=False, fb="Essa pergunta ficou para trás.")]),
 ]),
)
