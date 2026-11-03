X = dict(
 key=dict(big="Is it far from here?", label="Perguntar se é longe", sub="Pergunte se o lugar é longe e se dá para ir a pé. Quem responde costuma dizer o tempo em minutos."),
 mini=[
  dict(who="Evan", en="Excuse me, is the {lake|park|museum} far from here?", pt="Com licença, {o lago|o parque|o museu} fica longe daqui?"),
  dict(who="You", en="Not really. It's {ten|five|fifteen} minutes on foot.", pt="Nem tanto. São {dez|cinco|quinze} minutos a pé."),
  dict(who="Evan", en="Can I {walk|go|ride a bike} there?", pt="Posso {ir a pé|ir|ir de bicicleta} até lá?"),
  dict(who="You", en="Yes. Go straight and then turn {right.|left.}", pt="Sim. Siga em frente e vire à {direita.|esquerda.}"),
 ],
 dlg=[
  dict(who="Evan", en="Excuse me, is the {lake|park} far from here?", pt="Com licença, {o lago|o parque} fica longe daqui?"),
  dict(who="You", en="Not really. It's {ten|five} minutes on foot.", pt="Nem tanto. São {dez|cinco} minutos a pé."),
  dict(who="Evan", en="Can I {walk|go} there?", pt="Posso {ir a pé|ir} até lá?"),
  dict(who="You", en="Yes. Go straight and then turn {right.|left.}", pt="Sim. Siga em frente e vire à {direita.|esquerda.}"),
  dict(who="Evan", en="Is it a {nice|long} walk?", pt="É um passeio {bom?|longo?}"),
  dict(who="You", en="Yes, you'll see many {trees|birds} and bikes.", pt="Sim, você verá muitas {árvores|aves} e bicicletas."),
  dict(who="Evan", en="Should I take a {bus?|taxi?}", pt="Devo pegar um {ônibus?|táxi?}"),
  dict(who="You", en="No, {walking|riding a bike} is better.", pt="Não, {andar|andar de bicicleta} é melhor."),
  dict(who="Evan", en="Enjoy your {walk!|day!}", pt="Aproveite a {caminhada!|dia!}"),
 ],
 vocab=[
  dict(w="walk", pt="caminhada / andar", e="🚶", ex=["It's a nice walk.", "I walk to school."]),
  dict(w="mile", pt="milha", e="📏", ex=["It's one mile from here.", "The lake is two miles away."]),
  dict(w="tired", pt="cansado", e="😴", ex=["I'm tired.", "He is tired after the walk."]),
  dict(w="lake", pt="lago", e="🏞️", ex=["The lake is big.", "We walk to the lake."]),
  dict(w="tree", pt="árvore", e="🌳", ex=["There is a big tree.", "The park has many trees."]),
  dict(w="bike", pt="bicicleta", e="🚲", ex=["I ride my bike.", "There are many bikes."]),
 ],
 molds=[
  dict(title="Perguntar se é longe", frame="Is the {place} far from here?", slots=[dict(key="place", opts=["lake", "park", "station", "museum"])], model="Is the lake far from here?", note="Is the... far from here? = O... fica longe daqui? Far é para distância."),
  dict(title="Dizer o tempo a pé", frame="It's {time} minutes on foot.", slots=[dict(key="time", opts=["ten", "five", "fifteen", "twenty"])], model="It's ten minutes on foot.", note="On foot = a pé. Diga o número e minutes (plural)."),
  dict(title="Escrever a pergunta", frame="Excuse me, is the {place} far? Can I {way} there?", slots=[dict(key="place", opts=["lake", "park", "museum"]), dict(key="way", opts=["walk", "take a bus", "ride a bike"])], model="Excuse me, is the lake far? Can I walk there?", note="Comece com Excuse me e pergunte duas coisas: distância e como ir."),
 ],
 sounds=[
  dict(say="Is the lake far from here?", tag="palavra fraca: from", tip="From é fraco e soa 'frm'. Dê força a LAKE e FAR."),
  dict(say="Go straight and then turn right.", tag="palavra fraca: and", tip="And soa 'n': 'straight-n-then'. Dê força a STRAIGHT, TURN e RIGHT."),
  dict(say="Can I walk there?", tag="palavra fraca: can", tip="Can fraco soa 'kn'. O l de walk é mudo: 'uók'. Dê força a WALK."),
 ],
 role=dict(turns=[
  dict(npc="Excuse me, is the lake far from here?", opts=[
   dict(en="Not really. It's ten minutes on foot.", pt="Nem tanto. São dez minutos a pé.", reply="Can I walk there?"),
   dict(en="No, it's close. Five minutes on foot.", pt="Não, é perto. Cinco minutos a pé.", reply="Can I walk there?"),
   dict(en="A little far. Fifteen minutes on foot.", pt="Um pouco longe. Quinze minutos a pé.", reply="Can I walk there?")]),
  dict(npc="Can I walk there?", opts=[
   dict(en="Yes. Go straight and then turn right.", pt="Sim. Siga em frente e vire à direita.", reply="Is it a nice walk?"),
   dict(en="Yes. Go straight, then turn left.", pt="Sim. Siga em frente, depois vire à esquerda.", reply="Is it a nice walk?"),
   dict(en="Sure. It's straight, then on the right.", pt="Claro. É em frente, depois à direita.", reply="Is it a nice walk?")]),
  dict(npc="Is it a nice walk?", opts=[
   dict(en="Yes, you'll see many trees and bikes.", pt="Sim, você verá muitas árvores e bicicletas.", reply="Should I take a bus?"),
   dict(en="Yes, you'll see the lake.", pt="Sim, você verá o lago.", reply="Should I take a bus?"),
   dict(en="Yes, it's quiet and sunny.", pt="Sim, é tranquilo e ensolarado.", reply="Should I take a bus?")]),
  dict(npc="Should I take a bus?", opts=[
   dict(en="No, walking is better.", pt="Não, andar é melhor.", reply="Great. Enjoy your walk!"),
   dict(en="No, it's too short.", pt="Não, é curto demais.", reply="Okay. Enjoy your walk!"),
   dict(en="You can, but walking is nice.", pt="Pode, mas andar é agradável.", reply="Okay. Enjoy your walk!")]),
 ], change=["O visitante está cansado: sugira ônibus ou táxi e diga o tempo.", "O visitante tem uma mala pesada: diga que o lago fica a quinze minutos a pé.", "Começa a chover: diga que o ônibus é melhor hoje."]),
 writing=dict(task="Você explica o caminho a um visitante. Escreva 2 ou 3 frases: diga se é longe, o tempo a pé e como ir.", model="The lake is not far. It's ten minutes on foot. Go straight and then turn right. Walking is better.", kw=["lake", "minutes", "foot", "walking"], checks=["Disse se é longe ou perto.", "Disse o tempo a pé.", "Deu uma direção simples."]),
 scenes=dict(pool=["park", "park2", "lake", "street"], npc=dict(g="m", role="tourist"), you=dict(g="f")),
 convo=dict(npc=dict(name="Evan"), story="Você está numa praça em Chicago e um visitante pergunta sobre o lago.", turns=[
  dict(npc="Excuse me, is the lake far from here?", pt="Com licença, o lago fica longe daqui?", opts=[
   dict(en="Enjoy your walk!", pt="Aproveite a caminhada!", ok=False, fb="Isso se diz no fim."),
   dict(en="Not really. It's ten minutes on foot.", pt="Nem tanto. São dez minutos a pé.", ok=True, fb="Responde e dá o tempo."),
   dict(en="Should I take a bus?", pt="Devo pegar um ônibus?", ok=False, fb="Quem pergunta isso é o visitante.")]),
  dict(npc="Can I walk there?", pt="Posso ir a pé?", opts=[
   dict(en="It's ten minutes on foot.", pt="São dez minutos a pé.", ok=False, fb="Isso já foi dito e não responde à pergunta."),
   dict(en="Yes. Go straight and then turn right.", pt="Sim. Siga em frente e vire à direita.", ok=True, fb="Diz sim e dá a direção."),
   dict(en="Excuse me, is the lake far from here?", pt="Com licença, o lago fica longe daqui?", ok=False, fb="Essa pergunta é dele.")]),
  dict(npc="Is it a nice walk?", pt="É um bom passeio?", opts=[
   dict(en="Yes, you'll see many trees and bikes.", pt="Sim, você verá muitas árvores e bicicletas.", ok=True, fb="Descreve o caminho."),
   dict(en="Go straight and then turn right.", pt="Siga em frente e vire à direita.", ok=False, fb="A direção já foi dada."),
   dict(en="Should I take a bus?", pt="Devo pegar um ônibus?", ok=False, fb="Quem pergunta isso é ele.")]),
  dict(npc="Should I take a bus?", pt="Devo pegar um ônibus?", opts=[
   dict(en="Yes, you'll see many trees.", pt="Sim, você verá muitas árvores.", ok=False, fb="Não responde a pergunta."),
   dict(en="Can I walk there?", pt="Posso ir a pé?", ok=False, fb="Essa pergunta é dele e já foi respondida."),
   dict(en="No, walking is better.", pt="Não, andar é melhor.", ok=True, fb="Responde e dá uma razão curta.")]),
  dict(npc="Enjoy your walk!", pt="Aproveite a caminhada!", opts=[
   dict(en="Is the lake far from here?", pt="O lago fica longe daqui?", ok=False, fb="Essa pergunta abre a conversa."),
   dict(en="Thanks! Have a good day!", pt="Valeu! Tenha um bom dia!", ok=True, fb="Fecha com simpatia."),
   dict(en="Go straight and then turn right.", pt="Siga em frente e vire à direita.", ok=False, fb="Você já disse isso.")]),
 ]),
)
