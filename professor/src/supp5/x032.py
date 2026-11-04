X = dict(
 key=dict(big="Just water, please", label="Pedir só água", sub="Em muitos restaurantes dos EUA a água vem com gelo; se não quiser, diga No ice, please."),
 mini=[
  dict(who="Maya", en="Hi! Can I get you {something to drink|a drink|something cold}?", pt="Oi! Posso trazer {algo para beber|uma bebida|algo gelado}?"),
  dict(who="You", en="{Just water|Water|Lemonade}, please.", pt="{Só água|Água|Limonada}, por favor."),
  dict(who="Maya", en="{With ice?|Ice in your water?|Do you want ice?}", pt="{Com gelo?|Gelo na água?|Quer gelo?}"),
  dict(who="You", en="{No ice|Some ice|Just a little ice}, please.", pt="{Sem gelo|Com gelo|Só um pouco de gelo}, por favor."),
 ],
 dlg=[
  dict(who="Maya", en="Hi! Can I get you {something to drink|a drink|something cold}?", pt="Oi! Posso trazer {algo para beber|uma bebida|algo gelado}?"),
  dict(who="You", en="{Just water|Water|Lemonade}, please.", pt="{Só água|Água|Limonada}, por favor."),
  dict(who="Maya", en="{With ice?|Ice in your water?}", pt="{Com gelo?|Gelo na água?}"),
  dict(who="You", en="{No ice|Some ice}, please.", pt="{Sem gelo|Com gelo}, por favor."),
  dict(who="Maya", en="Here you go. {Ready to order?|Are you ready to order?}", pt="Aqui está. {Pronto para pedir?|Você já quer pedir?}"),
  dict(who="You", en="Not yet. {Five|Two|Ten} more minutes.", pt="Ainda não. Mais {cinco|dois|dez} minutos."),
  dict(who="Maya", en="No problem. {Take your time.|No rush.}", pt="Sem problema. {Fique à vontade.|Sem pressa.}"),
  dict(who="You", en="{Thank you!|Thanks a lot!}", pt="{Obrigado!|Muito obrigado!}"),
  dict(who="Maya", en="Enjoy your meal!", pt="Bom apetite!"),
 ],
 vocab=[
  dict(w="refill", pt="repor / completar o copo", e="🔄", ex=["Can I have a refill?", "A refill, please."]),
  dict(w="ice", pt="gelo", e="🧊", ex=["No ice, please.", "There is ice in my drink."]),
  dict(w="glass", pt="copo de vidro", e="🥛", ex=["Can I have a glass of water?", "My glass is empty."]),
  dict(w="napkin", pt="guardanapo", e="🧻", ex=["Can I have a napkin, please?", "The napkin is on the table."]),
  dict(w="fork", pt="garfo", e="🍴", ex=["I need a clean fork.", "The fork is next to the plate."]),
  dict(w="spoon", pt="colher", e="🥄", ex=["Can I have a spoon for the soup?", "The spoon is on the napkin."]),
 ],
 molds=[
  dict(title="Pedir a bebida", frame="Just {drink}, please. {ice}.", slots=[dict(key="drink", opts=["water", "lemonade", "iced tea"]), dict(key="ice", opts=["No ice", "Some ice", "Lots of ice"])], model="Just water, please. No ice.", note="Just = só. Diga o que você quer e depois a preferência sobre o gelo."),
  dict(title="Pedir mais tempo", frame="{opener}. {num} more minutes, please.", slots=[dict(key="opener", opts=["Not yet", "Not quite yet", "Sorry, not yet"]), dict(key="num", opts=["Five", "Two", "Ten"])], model="Not yet. Five more minutes, please.", note="Not yet = ainda não. Dá para pedir o tempo que você precisa sem pressa."),
  dict(title="Escrever um pedido", frame="Can I have {item} {extra}, please?", slots=[dict(key="item", opts=["a glass of water", "a lemonade", "an iced tea"]), dict(key="extra", opts=["with ice", "with no ice", "with extra ice"])], model="Can I have a glass of water with ice, please?", note="Can I have...? é um pedido educado. Coloque o complemento no fim da frase."),
 ],
 sounds=[
  dict(say="Can I get you something?", tag="ligação: can I", tip="Can e I se unem: soa como 'kenai'. Não pare entre as palavras."),
  dict(say="Take your time.", tag="ligação: take your", tip="O som do final de take liga com your: 'teik-yor'. Fale como uma frase só."),
  dict(say="Not yet. Five more minutes.", tag="ritmo: palavras fortes", tip="Dê força a not, yet, five e minutes; more fica curto e fraco."),
 ],
 role=dict(turns=[
  dict(npc="Hi! Can I get you something to drink?", opts=[
   dict(en="Just water, please.", pt="Só água, por favor.", reply="Sure! Water. With ice?"),
   dict(en="Water, please.", pt="Água, por favor.", reply="Okay, one water. With ice?"),
   dict(en="A lemonade, please.", pt="Uma limonada, por favor.", reply="Sure! One lemonade. With ice?")]),
  dict(npc="With ice?", opts=[
   dict(en="No ice, please.", pt="Sem gelo, por favor.", reply="No ice. Got it."),
   dict(en="Yes, with ice, please.", pt="Sim, com gelo, por favor.", reply="With ice. Coming right up."),
   dict(en="Just a little ice, please.", pt="Só um pouco de gelo, por favor.", reply="A little ice. No problem.")]),
  dict(npc="Here you go. Ready to order?", opts=[
   dict(en="Not yet. Five more minutes.", pt="Ainda não. Mais cinco minutos.", reply="No problem. Take your time."),
   dict(en="Not yet. Two more minutes, please.", pt="Ainda não. Mais dois minutos, por favor.", reply="Sure. I'll come back soon."),
   dict(en="Almost. Can I have a few minutes?", pt="Quase. Posso ter alguns minutos?", reply="Of course. No rush.")]),
  dict(npc="Enjoy your meal!", opts=[
   dict(en="Thank you!", pt="Obrigado!", reply="You're welcome!"),
   dict(en="Thanks a lot!", pt="Muito obrigado!", reply="My pleasure!"),
   dict(en="Thank you, you too!", pt="Obrigado, igualmente!", reply="Thanks! Let me know if you need anything.")]),
 ], change=["O restaurante não tem limonada: peça outra bebida.", "Você precisa de um garfo limpo: peça ao garçom.", "Seu amigo chega atrasado: peça mais dez minutos."]),
 writing=dict(task="Você está num restaurante. Escreva 2 ou 3 frases: peça uma bebida, diga como quer o gelo e peça mais tempo antes de pedir a comida.", model="Hi! Just water, please. No ice, please. We are not ready to order yet. Five more minutes, please.", kw=["water", "ice", "please", "minutes"], checks=["Pediu uma bebida com please.", "Disse como quer o gelo (ice).", "Pediu mais tempo (more minutes)."]),
 scenes=dict(pool=["diner", "restaurant", "cafe", "counter"], npc=dict(g="f", role="server"), you=dict(g="f")),
 convo=dict(npc=dict(name="Maya"), story="Você está num restaurante nos EUA. Peça a bebida e mais tempo.", turns=[
  dict(npc="Hi! Can I get you something to drink?", pt="Oi! Posso trazer algo para beber?", opts=[
   dict(en="Just water, please.", pt="Só água, por favor.", ok=True, fb="Resposta direta e educada ao pedido de bebida."),
   dict(en="Yes, I am ready to order.", pt="Sim, estou pronto para pedir.", ok=False, fb="Ela perguntou da bebida; o pedido da comida vem depois."),
   dict(en="Here you go.", pt="Aqui está.", ok=False, fb="Here you go é o que a garçonete diz ao entregar algo.")]),
  dict(npc="With ice?", pt="Com gelo?", opts=[
   dict(en="Yes, I like water.", pt="Sim, eu gosto de água.", ok=False, fb="Ela perguntou do gelo, não do seu gosto por água."),
   dict(en="No ice, please.", pt="Sem gelo, por favor.", ok=True, fb="Diz claramente que você não quer gelo."),
   dict(en="Water with a fork, please.", pt="Água com um garfo, por favor.", ok=False, fb="Responda sobre o gelo: com ou sem.")]),
  dict(npc="Here you go. Ready to order?", pt="Aqui está. Pronto para pedir?", opts=[
   dict(en="Not yet. Five more minutes.", pt="Ainda não. Mais cinco minutos.", ok=True, fb="Boa forma de pedir mais tempo."),
   dict(en="Enjoy your meal!", pt="Bom apetite!", ok=False, fb="Esta frase é dita por quem serve, e só quando a comida chega."),
   dict(en="The check, please.", pt="A conta, por favor.", ok=False, fb="Ainda nem pediu a comida; a conta vem no fim.")]),
  dict(npc="No problem. Take your time.", pt="Sem problema. Fique à vontade.", opts=[
   dict(en="Thank you!", pt="Obrigado!", ok=True, fb="Agradecer é a resposta natural."),
   dict(en="Yes, I'm ready now.", pt="Sim, estou pronto agora.", ok=False, fb="Você acabou de pedir mais tempo, então não faz sentido."),
   dict(en="With ice, please.", pt="Com gelo, por favor.", ok=False, fb="O assunto do gelo já foi resolvido.")]),
  dict(npc="Enjoy your meal!", pt="Bom apetite!", opts=[
   dict(en="No ice, please.", pt="Sem gelo, por favor.", ok=False, fb="O pedido já foi feito; agora responda com um agradecimento."),
   dict(en="Not yet. Five more minutes.", pt="Ainda não. Mais cinco minutos.", ok=False, fb="A comida já chegou; não há mais o que esperar."),
   dict(en="Thanks! You too.", pt="Obrigado! Para você também.", ok=True, fb="Resposta simpática e comum.")]),
 ]),
)
