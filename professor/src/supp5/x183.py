X = dict(
 key=dict(big="I lost my phone", label="Perdi o celular", sub="Diga o que perdeu, onde viu pela última vez e como ele é. Cor e capa ajudam muito a achar o aparelho."),
 mini=[
  dict(who="You", en="Excuse me, I lost my {phone!|bag!|wallet!}", pt="Com licença, perdi {meu celular!|minha bolsa!|minha carteira!}"),
  dict(who="Evan", en="Where did you last {see it?|have it?}", pt="Onde você {viu pela última vez?|teve pela última vez?}"),
  dict(who="You", en="{On the train,|At the station,|On the bus,} I think.", pt="{No trem,|Na estação,|No ônibus,} acho."),
  dict(who="Evan", en="Thank you. Let me call the {lost and found.|station office.}", pt="Obrigado. Vou ligar para {achados e perdidos.|o escritório da estação.}"),
 ],
 dlg=[
  dict(who="Evan", en="Excuse me, I lost my {phone!|bag!}", pt="Com licença, perdi {meu celular!|minha bolsa!}"),
  dict(who="You", en="Oh no. Where did you last {see it?|have it?}", pt="Ai, não. Onde {viu pela última vez?|teve pela última vez?}"),
  dict(who="Evan", en="On the {train,|bus,} I think.", pt="No {trem,|ônibus,} acho."),
  dict(who="You", en="What does it look {like?|like, please?}", pt="Como ele {é?|é, por favor?}"),
  dict(who="Evan", en="It's {black,|silver,} with a blue {case.|cover.}", pt="É {preto,|prateado,} com {capa azul.|capa azul.}"),
  dict(who="You", en="Let me call the lost and {found.|found desk.}", pt="Vou ligar para achados e {perdidos.|perdidos.}"),
  dict(who="Evan", en="Thank you {so much.|very much.}", pt="Muito {obrigado.|obrigado.}"),
  dict(who="You", en="Hello, did someone find a {phone?|black phone?}", pt="Alô, alguém achou {um celular?|um celular preto?}"),
  dict(who="Evan", en="What color is {it?|the case?}", pt="Que cor é {ele?|a capa?}"),
 ],
 vocab=[
  dict(w="case", pt="capa (de celular)", e="📲", ex=["My phone has a blue case.", "The case is old."]),
  dict(w="station", pt="estação", e="🚉", ex=["I am at the station.", "The station is big."]),
  dict(w="owner", pt="dono", e="🙋", ex=["I am the owner.", "Who is the owner?"]),
  dict(w="silver", pt="prateado", e="🪙", ex=["My phone is silver.", "I like the silver one."]),
  dict(w="picture", pt="foto, imagem", e="🖼️", ex=["I have a picture of my phone.", "The picture is on my screen."]),
  dict(w="hand", pt="mão", e="✋", ex=["The phone is in my hand.", "Give me your hand."]),
 ],
 molds=[
  dict(title="Dizer o que perdeu", frame="Excuse me, I lost my {thing}!", slots=[dict(key="thing", opts=["phone", "bag", "wallet"])], model="Excuse me, I lost my phone!", note="Lost é o passado de lose. Use my + objeto."),
  dict(title="Dizer onde foi", frame="{place}, I think.", slots=[dict(key="place", opts=["On the train", "At the station", "On the bus"])], model="On the train, I think.", note="On the train/bus; at the station. I think suaviza a certeza."),
  dict(title="Descrever por escrito", frame="It's {color}, with a {color2} {part}.", slots=[dict(key="color", opts=["black", "silver", "white"]), dict(key="color2", opts=["blue", "red", "green"]), dict(key="part", opts=["case", "sticker", "strap"])], model="It's black, with a blue case.", note="A cor vem antes do nome: a blue case, não a case blue."),
 ],
 sounds=[
  dict(say="I lost my phone!", tag="acento: PHONE", tip="Phone tem o som f, não p. Junte os lábios de leve com os dentes: foun."),
  dict(say="Where did you last see it?", tag="redução: did you", tip="Did you soa “didja”. Una as duas palavras sem pausa."),
  dict(say="It's black, with a blue case.", tag="ritmo: BLACK / BLUE CASE", tip="Acentue black, blue e case. As palavras pequenas ficam leves."),
 ],
 role=dict(turns=[
  dict(npc="Hi. How can I help you?", opts=[
   dict(en="Excuse me, I lost my phone!", pt="Com licença, perdi meu celular!", reply="Oh no. Where did you last see it?"),
   dict(en="Hi. I think I lost my phone.", pt="Oi. Acho que perdi meu celular.", reply="Oh no. Where did you last see it?"),
   dict(en="Hello. I can't find my phone.", pt="Olá. Não acho meu celular.", reply="Oh no. Where did you last see it?")]),
  dict(npc="Where did you last see it?", opts=[
   dict(en="On the train, I think.", pt="No trem, acho.", reply="What does it look like?"),
   dict(en="At the station, I think.", pt="Na estação, acho.", reply="What does it look like?"),
   dict(en="In my pocket, on the bus.", pt="No meu bolso, no ônibus.", reply="What does it look like?")]),
  dict(npc="What does it look like?", opts=[
   dict(en="It's black, with a blue case.", pt="É preto, com capa azul.", reply="Let me call the lost and found."),
   dict(en="It's silver, with a red case.", pt="É prateado, com capa vermelha.", reply="Let me call the lost and found."),
   dict(en="It's white, with a sticker.", pt="É branco, com um adesivo.", reply="Let me call the lost and found.")]),
  dict(npc="Let me call the lost and found.", opts=[
   dict(en="Thank you so much.", pt="Muito obrigada.", reply="Good news. They have it."),
   dict(en="Thanks. I appreciate it.", pt="Valeu. Agradeço.", reply="Good news. They have it."),
   dict(en="Thank you. I'll wait here.", pt="Obrigada. Espero aqui.", reply="Sure. It'll take a minute.")]),
 ], change=["O achados e perdidos pede a cor e a marca: responda em inglês.", "Você precisa deixar seu contato: diga seu nome e número.", "Eles não acharam o celular: peça para ligar de novo amanhã."]),
 writing=dict(task="Escreva 2 ou 3 frases para o achados e perdidos: diga que perdeu o celular, onde foi e como ele é.", model="Hello, I lost my phone on the train. It's black, with a blue case. Did someone find it?", kw=["lost", "phone", "black", "case"], checks=["Disse que perdeu o celular.", "Disse onde foi.", "Descreveu o celular."]),
 scenes=dict(pool=["station", "subway", "traincar", "counter"], npc=dict(g="m", role="station worker"), you=dict(g="f")),
 convo=dict(npc=dict(name="Evan"), story="Você perdeu o celular em uma estação de trem em Chicago. O Evan trabalha no balcão de ajuda.", turns=[
  dict(npc="Hi. How can I help you?", pt="Oi. Como posso ajudar?", opts=[
   dict(en="Excuse me, I lost my phone!", pt="Com licença, perdi meu celular!", ok=True, fb="Diz o problema de forma clara."),
   dict(en="Thank you so much.", pt="Muito obrigada.", ok=False, fb="Ainda não há o que agradecer."),
   dict(en="What does it look like?", pt="Como ele é?", ok=False, fb="Quem pergunta isso é o Evan.")]),
  dict(npc="Oh no. Where did you last see it?", pt="Ai, não. Onde viu pela última vez?", opts=[
   dict(en="It's black, with a blue case.", pt="É preto, com capa azul.", ok=False, fb="Ele perguntou onde, não como é."),
   dict(en="On the train, I think.", pt="No trem, acho.", ok=True, fb="Responde com o lugar."),
   dict(en="Let me call the lost and found.", pt="Vou ligar para achados e perdidos.", ok=False, fb="Quem diz isso é o Evan.")]),
  dict(npc="What does it look like?", pt="Como ele é?", opts=[
   dict(en="It's black, with a blue case.", pt="É preto, com capa azul.", ok=True, fb="Dá cor e capa."),
   dict(en="On the train, I think.", pt="No trem, acho.", ok=False, fb="Você já disse onde."),
   dict(en="Good news. They have it.", pt="Boa notícia. Eles estão com ele.", ok=False, fb="Essa fala é do Evan.")]),
  dict(npc="Let me call the lost and found.", pt="Vou ligar para achados e perdidos.", opts=[
   dict(en="I lost my phone!", pt="Perdi meu celular!", ok=False, fb="Ele já sabe disso."),
   dict(en="Where did you last see it?", pt="Onde você viu pela última vez?", ok=False, fb="Essa pergunta é do Evan."),
   dict(en="Thank you so much.", pt="Muito obrigada.", ok=True, fb="Agradece a ajuda.")]),
  dict(npc="Good news. They have it.", pt="Boa notícia. Eles estão com ele.", opts=[
   dict(en="Thank goodness!", pt="Graças a Deus!", ok=True, fb="Mostra alívio."),
   dict(en="What does it look like?", pt="Como ele é?", ok=False, fb="Pergunta do Evan, e já foi respondida."),
   dict(en="I lost my phone!", pt="Perdi meu celular!", ok=False, fb="Já foi achado.")]),
 ]),
)
