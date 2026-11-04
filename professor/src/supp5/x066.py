X = dict(
 key=dict(big="I'm looking for a sofa", label="Procurar um móvel na loja", sub="Diga o que procura, pergunte o preço e o conforto, experimente e decida com I'll take it."),
 mini=[
  dict(who="Omar", en="Hi! I'm looking for a {sofa|table|bed}.", pt="Oi! Estou procurando {um sofá|uma mesa|uma cama}."),
  dict(who="You", en="We have many. What {color|size|style} do you like?", pt="Temos vários. Que {cor|tamanho|estilo} você prefere?"),
  dict(who="Omar", en="Is it {comfortable|big|heavy}?", pt="É {confortável|grande|pesado}?"),
  dict(who="You", en="It's {four|three|five} hundred dollars.", pt="São {quatrocentos|trezentos|quinhentos} dólares."),
 ],
 dlg=[
  dict(who="Omar", en="Hi! I'm looking for a {sofa|desk|bed}.", pt="Oi! Estou procurando {um sofá|uma escrivaninha|uma cama}."),
  dict(who="You", en="We have many. What {color|size} do you like?", pt="Temos vários. Que {cor|tamanho} você prefere?"),
  dict(who="Omar", en="{Gray|Blue|Black}. How much is this one?", pt="{Cinza|Azul|Preto}. Quanto custa este?"),
  dict(who="You", en="It's {four|three|five} hundred dollars.", pt="São {quatrocentos|trezentos|quinhentos} dólares."),
  dict(who="Omar", en="Is it {comfortable|soft|big}?", pt="É {confortável|macio|grande}?"),
  dict(who="You", en="Sit down and try it.", pt="Sente e experimente."),
  dict(who="Omar", en="Yes, it's very {comfy|soft}. I'll take it.", pt="Sim, é muito {confortável|macio}. Vou levar."),
  dict(who="You", en="Great. We deliver on {Friday|Monday|Saturday}.", pt="Ótimo. Entregamos na {sexta|segunda|sábado}."),
  dict(who="Omar", en="We deliver on Friday. Enjoy!", pt="Entregamos na sexta. Aproveite!"),
 ],
 vocab=[
  dict(w="desk", pt="escrivaninha", e="🖥️", ex=["I need a desk for my room.", "The desk is next to the window."]),
  dict(w="pillow", pt="almofada / travesseiro", e="🛌", ex=["The pillow is very soft.", "I'd like a blue pillow."]),
  dict(w='carpet', pt='carpete', e='🟫', ex=['The carpet is soft.', 'I like this carpet.']),
  dict(w='dresser', pt='cômoda', e='🗄️', ex=['My socks are in the dresser.', 'The dresser is old.']),
  dict(w="comfy", pt="confortável (informal)", e="😌", ex=["This chair is so comfy.", "My bed is very comfy."]),
  dict(w="sale", pt="promoção", e="🔖", ex=["There is a sale today.", "The sale ends on Sunday."]),
 ],
 molds=[
  dict(title="Dizer o que procura", frame="I'm looking for a {item}.", slots=[dict(key="item", opts=["sofa", "desk", "lamp", "bed"])], model="I'm looking for a sofa.", note="Look for = procurar. Looking for a… serve em qualquer loja."),
  dict(title="Perguntar sobre o móvel", frame="Is it {adj}?", slots=[dict(key="adj", opts=["comfortable", "soft", "big", "heavy"])], model="Is it comfortable?", note="Is it + adjetivo = É...? Sirva para perguntar sobre qualquer coisa."),
  dict(title="Escrever o pedido", frame="Hi! I'm looking for {item} in {color}. How much is it? I'll take it.", slots=[dict(key="item", opts=["a sofa", "a desk", "a table"]), dict(key="color", opts=["gray", "blue", "black", "white"])], model="Hi! I'm looking for a sofa in gray. How much is it? I'll take it.", note="Diga o que quer, a cor, pergunte o preço e decida."),
 ],
 sounds=[
  dict(say="I'm looking for a sofa.", tag="ligação: looking for", tip="Looking for soa 'lukin-for'. Acentue LOOK e SO-fa."),
  dict(say="How much is this one?", tag="ligação: much is", tip="Much is vira 'machiz'. Una as palavras e acentue MUCH."),
  dict(say="I'll take it.", tag="ligação: take it", tip="Take it soa 'tay-kit'. Diga rápido: ail-TAY-kit."),
 ],
 role=dict(turns=[
  dict(npc="Hi! Can I help you?", opts=[
   dict(en="I'm looking for a sofa.", pt="Estou procurando um sofá.", reply="We have many. What color do you like?"),
   dict(en="I'm looking for a desk.", pt="Estou procurando uma escrivaninha.", reply="We have many. What color do you like?"),
   dict(en="Hi! I'm looking for a bed.", pt="Oi! Estou procurando uma cama.", reply="We have many. What color do you like?")]),
  dict(npc="What color do you like?", opts=[
   dict(en="Gray, please.", pt="Cinza, por favor.", reply="Nice. This gray one is four hundred dollars."),
   dict(en="Blue. How much is this one?", pt="Azul. Quanto custa este?", reply="This blue one is four hundred dollars."),
   dict(en="Black, I think.", pt="Preto, acho.", reply="Nice. This black one is four hundred dollars.")]),
  dict(npc="This one is four hundred dollars.", opts=[
   dict(en="Is it comfortable?", pt="É confortável?", reply="Sit down and try it."),
   dict(en="Can I sit on it?", pt="Posso sentar nele?", reply="Of course. Sit down and try it."),
   dict(en="Is it soft?", pt="É macio?", reply="Sit down and try it.")]),
  dict(npc="Sit down and try it.", opts=[
   dict(en="It's very comfy. I'll take it.", pt="É muito confortável. Vou levar.", reply="Great. We deliver on Friday."),
   dict(en="It's nice, but a bit pricey.", pt="É bom, mas meio caro.", reply="Okay. Let's look around. We have more sofas."),
   dict(en="Yes, I like it. I'll take it.", pt="Sim, gostei. Vou levar.", reply="Great. We deliver on Friday.")]),
 ], change=["O sofá custa mais do que você pensava: diga que é caro e peça para ver outro.", "Você quer entrega no sábado, não na sexta: pergunte se é possível.", "O sofá cinza acabou: escolha outra cor."]),
 writing=dict(task="Você está numa loja de móveis. Escreva 2 ou 3 frases: diga o que procura, pergunte o preço e decida.", model="Hi! I'm looking for a gray sofa. How much is it? It's very comfy, so I'll take it.", kw=["looking", "sofa", "much", "take"], checks=["Disse o que procura.", "Perguntou o preço.", "Decidiu comprar."]),
 scenes=dict(pool=["shop", "living", "home1", "street"], npc=dict(g="f", role="seller"), you=dict(g="m")),
 convo=dict(npc=dict(name="Tess"), story="Você está numa loja de móveis e quer comprar um sofá.", turns=[
  dict(npc="Hi! Can I help you?", pt="Oi! Posso ajudar?", opts=[
   dict(en="Yes, I'm looking for a sofa.", pt="Sim, estou procurando um sofá.", ok=True, fb="Diz o que você procura."),
   dict(en="We deliver on Friday.", pt="Entregamos na sexta.", ok=False, fb="Essa frase é de quem vende."),
   dict(en="I'll take it.", pt="Vou levar.", ok=False, fb="Você ainda não viu nada para decidir.")]),
  dict(npc="We have many. What color do you like?", pt="Temos vários. Que cor você prefere?", opts=[
   dict(en="Sit down and try it.", pt="Sente e experimente.", ok=False, fb="Quem diz isso é o vendedor."),
   dict(en="Gray, please.", pt="Cinza, por favor.", ok=True, fb="Responde com a cor."),
   dict(en="Friday is good.", pt="Sexta está bom.", ok=False, fb="Ainda não falaram de entrega.")]),
  dict(npc="This one is four hundred dollars.", pt="Este custa quatrocentos dólares.", opts=[
   dict(en="Is it comfortable?", pt="É confortável?", ok=True, fb="Pergunta natural sobre um sofá."),
   dict(en="What color do you like?", pt="Que cor você prefere?", ok=False, fb="Essa pergunta é da vendedora."),
   dict(en="It's four hundred dollars.", pt="São quatrocentos dólares.", ok=False, fb="Ela acabou de dizer o preço.")]),
  dict(npc="Sit down and try it.", pt="Sente e experimente.", opts=[
   dict(en="It's very comfy. I'll take it.", pt="É muito confortável. Vou levar.", ok=True, fb="Experimentou e decidiu."),
   dict(en="Hi! I'm looking for a sofa.", pt="Oi! Estou procurando um sofá.", ok=False, fb="Você já disse isso no começo."),
   dict(en="We have many.", pt="Temos vários.", ok=False, fb="Frase de quem vende.")]),
  dict(npc="Great. We deliver on Friday.", pt="Ótimo. Entregamos na sexta.", opts=[
   dict(en="How much is this one?", pt="Quanto custa este?", ok=False, fb="O preço já foi dito."),
   dict(en="Friday is good. Thanks!", pt="Sexta está bom. Obrigado!", ok=True, fb="Aceita o dia e agradece."),
   dict(en="Sit down and try it.", pt="Sente e experimente.", ok=False, fb="Quem diz isso é o vendedor.")]),
 ]),
)
