X = dict(
 key=dict(big="Could I borrow…?", label="Pedir emprestado", sub="Peça com educação, diga para que precisa e prometa devolver logo. Pedir ao vizinho é comum."),
 mini=[
  dict(who="You", en="Hi, Jordan! Do you have a {minute?|moment?|second?}", pt="Oi, Jordan! Tem um {minutinho?|momento?|segundinho?}"),
  dict(who="Jordan", en="Sure. What do you need?", pt="Claro. Do que precisa?"),
  dict(who="You", en="Could I borrow your {ladder?|hammer?|screwdriver?} I need to change a {light bulb.|lamp.}", pt="Posso pegar {sua escada|seu martelo|sua chave de fenda} emprestada? Preciso trocar uma {lâmpada.|luminária.}"),
  dict(who="Jordan", en="Of course! It's in the {garage.|hallway.|basement.} No {worries!|problem!}", pt="Claro! Está na {garagem.|entrada.|porão.} Sem {problema!|problema!}"),
 ],
 dlg=[
  dict(who="Jordan", en="Hi, Mr. Wills! Do you have a {minute?|moment?}", pt="Oi, Sr. Wills! Tem um {minutinho?|momento?}"),
  dict(who="You", en="Sure. What do you {need?|want?}", pt="Claro. Do que {precisa?|quer?}"),
  dict(who="Jordan", en="Could I borrow your {ladder?|tool?}", pt="Posso pegar {sua escada|sua ferramenta} emprestada?"),
  dict(who="You", en="Of course. What {for?|else?}", pt="Claro. Para {quê?|que mais?}"),
  dict(who="Jordan", en="I need to change a light {bulb.|bulb, please.}", pt="Preciso trocar uma {lâmpada.|lâmpada, por favor.}"),
  dict(who="You", en="Is it {high?|far?}", pt="É {alto?|longe?}"),
  dict(who="Jordan", en="Yes, in the {hallway.|garage.}", pt="Sim, no {corredor.|garagem.}"),
  dict(who="You", en="The ladder is in the {garage.|basement.}", pt="A escada está na {garagem.|porão.}"),
  dict(who="Jordan", en="Thank you. I'll bring it back {soon.|tonight.}", pt="Obrigado. Devolvo {logo.|hoje à noite.}"),
 ],
 vocab=[
  dict(w="ladder", pt="escada de mão", e="🪜", ex=["The ladder is in the garage.", "I climb the ladder."]),
  dict(w="wood", pt="madeira", e="🪵", ex=["The shelf is made of wood.", "I need a piece of wood."]),
  dict(w="saw", pt="serra", e="🪚", ex=["Use the saw.", "The saw is sharp."]),
  dict(w="nail", pt="prego", e="📌", ex=["I need a nail.", "The nail is small."]),
  dict(w="drill", pt="furadeira", e="🔧", ex=["I need a drill.", "The drill is loud."]),
  dict(w="paint", pt="tinta, pintar", e="🎨", ex=["I need white paint.", "We paint the wall."]),
 ],
 molds=[
  dict(title="Pedir emprestado", frame="Could I borrow your {thing}?", slots=[dict(key="thing", opts=["ladder", "hammer", "screwdriver", "bike"])], model="Could I borrow your ladder?", note="Could I borrow + your + coisa é um pedido educado."),
  dict(title="Dizer para que precisa", frame="I need to {action} a {thing}.", slots=[dict(key="action", opts=["change", "fix", "paint"]), dict(key="thing", opts=["light bulb", "shelf", "door"])], model="I need to change a light bulb.", note="Need to + verbo base diz o que você vai fazer."),
  dict(title="Escrever um bilhete", frame="Hi! Could I borrow your {thing}? I'll bring it back {time}.", slots=[dict(key="thing", opts=["ladder", "hammer", "tool"]), dict(key="time", opts=["soon", "tonight", "tomorrow"])], model="Hi! Could I borrow your ladder? I'll bring it back soon.", note="Peça e prometa devolver. I'll = I will."),
 ],
 sounds=[
  dict(say="The ladder is in the hallway.", tag="acento: LADder, HALLway", tip="A 1ª sílaba é forte e a 2ª fraca: LAD-der, HALL-way. Não dê a mesma força às duas."),
  dict(say="Could I borrow it?", tag="ligação: could I", tip="Una could e I: 'cú-dai'. O d some quase por completo."),
  dict(say="I'll bring it back soon.", tag="ligação: bring it back", tip="Una bring-it: 'brin-git'. O -ing quase encosta no it."),
 ],
 role=dict(turns=[
  dict(npc="Hi! What's up?", opts=[
   dict(en="Hi! Do you have a minute?", pt="Oi! Tem um minutinho?", reply="Sure. What do you need?"),
   dict(en="Hi, Jordan! Do you have a moment?", pt="Oi, Jordan! Tem um momento?", reply="Of course. What do you need?"),
   dict(en="Hi! I need your help.", pt="Oi! Preciso da sua ajuda.", reply="Sure. What do you need?")]),
  dict(npc="What do you need?", opts=[
   dict(en="Could I borrow your ladder?", pt="Posso pegar sua escada emprestada?", reply="Of course. What for?"),
   dict(en="Could I borrow your hammer?", pt="Posso pegar seu martelo emprestado?", reply="Sure. What for?"),
   dict(en="Could I borrow a screwdriver?", pt="Posso pegar uma chave de fenda emprestada?", reply="Of course. What for?")]),
  dict(npc="What for?", opts=[
   dict(en="I need to change a light bulb.", pt="Preciso trocar uma lâmpada.", reply="Is it high?"),
   dict(en="I need to fix a shelf.", pt="Preciso consertar uma prateleira.", reply="Is it a big job?"),
   dict(en="I need to paint a door.", pt="Preciso pintar uma porta.", reply="Is it a big door?")]),
  dict(npc="Is it high?", opts=[
   dict(en="Yes, in the hallway.", pt="Sim, no corredor.", reply="The ladder is in the garage."),
   dict(en="Yes, it's very high.", pt="Sim, é bem alto.", reply="Okay. The ladder is in the garage."),
   dict(en="No, it's low.", pt="Não, é baixo.", reply="Then a small ladder is fine. It's in the garage.")]),
 ], change=["O vizinho diz que a escada é pesada: peça ajuda para carregar.", "Você quebrou algo da ferramenta: peça desculpas e ofereça consertar.", "Você precisa da escada por dois dias: peça mais tempo."]),
 writing=dict(task="Escreva 2 ou 3 frases para um vizinho: peça uma ferramenta emprestada, diga para que e prometa devolver.", model="Hi! Could I borrow your ladder? I need to change a light bulb. I'll bring it back soon.", kw=["borrow", "ladder", "need", "bring"], checks=["Pediu emprestado com educação.", "Disse para que precisa.", "Prometeu devolver."]),
 scenes=dict(pool=["yard", "home1", "street", "hall"], npc=dict(g="m", role="neighbor"), you=dict(g="f")),
 convo=dict(npc=dict(name="Jordan"), story="Você precisa de uma escada. Seu vizinho Jordan mora ao lado e pode ajudar.", turns=[
  dict(npc="Hi! What's up?", pt="Oi! E aí?", opts=[
   dict(en="Sure. What do you need?", pt="Claro. Do que precisa?", ok=False, fb="Quem pergunta isso é o vizinho."),
   dict(en="Hi! Do you have a minute?", pt="Oi! Tem um minutinho?", ok=True, fb="Abre o pedido com educação."),
   dict(en="I'll bring it back soon.", pt="Devolvo logo.", ok=False, fb="Ainda não pediu nada.")]),
  dict(npc="Sure. What do you need?", pt="Claro. Do que precisa?", opts=[
   dict(en="Could I borrow your ladder?", pt="Posso pegar sua escada emprestada?", ok=True, fb="Pedido educado com borrow."),
   dict(en="Of course. What for?", pt="Claro. Para quê?", ok=False, fb="Quem pergunta isso é o vizinho."),
   dict(en="The ladder is in the garage.", pt="A escada está na garagem.", ok=False, fb="Quem diz isso é o vizinho.")]),
  dict(npc="Of course. What for?", pt="Claro. Para quê?", opts=[
   dict(en="Could I borrow your ladder?", pt="Posso pegar sua escada emprestada?", ok=False, fb="Você já pediu."),
   dict(en="Is it high?", pt="É alto?", ok=False, fb="Quem pergunta isso é o vizinho."),
   dict(en="I need to change a light bulb.", pt="Preciso trocar uma lâmpada.", ok=True, fb="Dá o motivo.")]),
  dict(npc="Is it high?", pt="É alto?", opts=[
   dict(en="Yes, in the hallway.", pt="Sim, no corredor.", ok=True, fb="Responde sim e diz onde."),
   dict(en="I need to change a light bulb.", pt="Preciso trocar uma lâmpada.", ok=False, fb="Você já disse isso."),
   dict(en="Do you have a minute?", pt="Tem um minutinho?", ok=False, fb="Já passou do começo da conversa.")]),
  dict(npc="The ladder is in the garage.", pt="A escada está na garagem.", opts=[
   dict(en="Is it high?", pt="É alto?", ok=False, fb="Essa pergunta já foi feita."),
   dict(en="Thank you. I'll bring it back soon.", pt="Obrigado. Devolvo logo.", ok=True, fb="Agradece e promete devolver."),
   dict(en="Yes, in the hallway.", pt="Sim, no corredor.", ok=False, fb="Você já respondeu isso.")]),
 ]),
)
