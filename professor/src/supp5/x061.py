X = dict(
 key=dict(big="What can I see in one day?", label="Pedir dicas de passeio", sub="No balcão de informações turísticas, pergunte o que ver, se é grátis e peça um mapa."),
 mini=[
  dict(who="Leo", en="Welcome! Can I {help you|help you today|help}?", pt="Bem-vindo! Posso {ajudar|ajudar hoje|ajudar}?"),
  dict(who="You", en="Yes, what can I {see|visit|do} in one day?", pt="Sim, o que posso {ver|visitar|fazer} em um dia?"),
  dict(who="Leo", en="Visit the {museum|park|market}. It's famous.", pt="Visite o {museu|parque|mercado}. É famoso."),
  dict(who="You", en="Great. Do you have a {map|guide|brochure}?", pt="Ótimo. Vocês têm {mapa|guia|folheto}?"),
 ],
 dlg=[
  dict(who="Leo", en="Welcome to Philadelphia! Can I {help you?|help you today?}", pt="Bem-vindo à Filadélfia! Posso {ajudar?|ajudar hoje?}"),
  dict(who="You", en="Yes, what can I {see|visit|do} in one day?", pt="Sim, o que posso {ver|visitar|fazer} em um dia?"),
  dict(who="Leo", en="Visit the Liberty Bell. It's {famous.|very famous.}", pt="Visite o Sino da Liberdade. É {famoso.|muito famoso.}"),
  dict(who="You", en="Is it {free?|open today?}", pt="É {de graça?|aberto hoje?}"),
  dict(who="Leo", en="Yes, it's {free.|open.}", pt="Sim, é {grátis.|aberto.}"),
  dict(who="You", en="Where can I {eat?|buy a ticket?}", pt="Onde posso {comer?|comprar um ingresso?}"),
  dict(who="Leo", en="Try a cheesesteak. It's a {local favorite.|good sandwich.}", pt="Experimente um cheesesteak. É {o preferido daqui.|um bom sanduíche.}"),
  dict(who="You", en="Great idea. Do you have a {map?|guide?}", pt="Ótima ideia. Vocês têm {mapa?|guia?}"),
  dict(who="Leo", en="Enjoy your {day!|stay!}", pt="Aproveite {o seu dia!|a sua estadia!}"),
 ],
 vocab=[
  dict(w="famous", pt="famoso", e="⭐", ex=["The Liberty Bell is famous.", "This is a famous street."]),
  dict(w="brochure", pt="folheto", e="📄", ex=["Do you have a brochure?", "The brochure is free."]),
  dict(w="landmark", pt="ponto turístico", e="📍", ex=["The bell is a landmark.", "This landmark is old."]),
  dict(w="statue", pt="estátua", e="🗽", ex=["The statue is tall.", "I take a photo of the statue."]),
  dict(w="souvenir", pt="lembrancinha", e="🎁", ex=["I want a souvenir.", "This souvenir is small."]),
  dict(w="guide", pt="guia", e="🧑‍🏫", ex=["The guide is friendly.", "We follow the guide."]),
 ],
 molds=[
  dict(title="Pedir dicas", frame="What can I {verb} in {time}?", slots=[dict(key="verb", opts=["see", "do", "visit"]), dict(key="time", opts=["one day", "two days", "the city"])], model="What can I see in one day?", note="What can I... ? = o que posso...? Troque o verbo e o tempo."),
  dict(title="Perguntar o preço", frame="Is the {place} free?", slots=[dict(key="place", opts=["museum", "park", "tour", "bus"])], model="Is the museum free?", note="Is the... free? Pergunta se não há cobrança."),
  dict(title="Pedir algo no balcão", frame="Hi! Do you have a {thing}? I'm a tourist.", slots=[dict(key="thing", opts=["map", "guide", "brochure"])], model="Hi! Do you have a map? I'm a tourist.", note="Do you have a...? é o jeito simples de pedir algo."),
 ],
 sounds=[
  dict(say="Visit the Liberty Bell.", tag="ligação: visit the", tip="Una a última consoante à próxima palavra e acentue LIB-er-ty."),
  dict(say="Is it free?", tag="ligação: is it", tip="Is it soa 'izit'. Acentue FREE."),
  dict(say="Where can I eat?", tag="ligação: can I", tip="Can I soa 'kenai'. Une as palavras, acentue EAT."),
 ],
 role=dict(turns=[
  dict(npc="Welcome to Philadelphia! Can I help you?", opts=[
   dict(en="Yes, what can I see in one day?", pt="Sim, o que posso ver em um dia?", reply="Visit the Liberty Bell. It's famous."),
   dict(en="Yes, what can I do today?", pt="Sim, o que posso fazer hoje?", reply="Visit the Liberty Bell. It's famous."),
   dict(en="Hi. I'm a tourist. Any tips?", pt="Oi. Sou turista. Alguma dica?", reply="Sure! Visit the Liberty Bell. It's famous.")]),
  dict(npc="Visit the Liberty Bell. It's famous.", opts=[
   dict(en="Is it free?", pt="É de graça?", reply="Yes, it's free."),
   dict(en="Is it open today?", pt="Está aberto hoje?", reply="Yes, it's open until five."),
   dict(en="Is it far from here?", pt="É longe daqui?", reply="No, it's close. Ten minutes on foot.")]),
  dict(npc="Do you need anything else?", opts=[
   dict(en="Where can I eat?", pt="Onde posso comer?", reply="Try a cheesesteak. It's a local favorite."),
   dict(en="Where can I buy a souvenir?", pt="Onde posso comprar uma lembrancinha?", reply="There is a small shop next door."),
   dict(en="Where is the museum?", pt="Onde fica o museu?", reply="It's on the next street.")]),
  dict(npc="Anything else?", opts=[
   dict(en="Great idea. Do you have a map?", pt="Ótima ideia. Vocês têm mapa?", reply="Yes, here you go. Enjoy your day!"),
   dict(en="Thanks! Can I have a map?", pt="Obrigado! Posso pegar um mapa?", reply="Of course. Enjoy your day!"),
   dict(en="That's all, thanks.", pt="É só isso, obrigado.", reply="You're welcome. Enjoy your day!")]),
 ], change=["O lugar famoso está fechado hoje: pergunte o que mais pode ver.", "Você só tem duas horas: diga isso e peça uma ideia rápida.", "O mapa é pago: pergunte se há um grátis ou decida se compra."]),
 writing=dict(task="Você está em uma cidade nova. Escreva 2 ou 3 frases para o balcão de turismo: pergunte o que ver, se é grátis e peça um mapa.", model="Hi! What can I see in one day? Is the museum free? Do you have a map, please?", kw=["see", "free", "map", "day"], checks=["Perguntou o que ver.", "Perguntou se é grátis.", "Pediu um mapa."]),
 scenes=dict(pool=["street", "museum", "park", "nyc"], npc=dict(g="m", role="guide"), you=dict(g="f")),
 convo=dict(npc=dict(name="Leo"), story="Você chega a uma cidade nova e vai ao balcão de informações turísticas.", turns=[
  dict(npc="Welcome to Philadelphia! Can I help you?", pt="Bem-vindo à Filadélfia! Posso ajudar?", opts=[
   dict(en="Yes, what can I see in one day?", pt="Sim, o que posso ver em um dia?", ok=True, fb="Pede dicas de forma clara."),
   dict(en="Enjoy your day!", pt="Aproveite o seu dia!", ok=False, fb="Essa fala é de quem atende, no fim."),
   dict(en="It's free.", pt="É grátis.", ok=False, fb="Você ainda não falou sobre preço.")]),
  dict(npc="Visit the Liberty Bell. It's famous.", pt="Visite o Sino da Liberdade. É famoso.", opts=[
   dict(en="Try a cheesesteak.", pt="Experimente um cheesesteak.", ok=False, fb="É uma dica de quem atende."),
   dict(en="Is it free?", pt="É de graça?", ok=True, fb="Pergunta sobre o preço."),
   dict(en="Welcome to Philadelphia!", pt="Bem-vindo à Filadélfia!", ok=False, fb="Quem dá boas-vindas é o atendente.")]),
  dict(npc="Yes, it's free.", pt="Sim, é grátis.", opts=[
   dict(en="Where can I eat?", pt="Onde posso comer?", ok=True, fb="Pede uma dica de comida."),
   dict(en="Yes, it's free.", pt="Sim, é grátis.", ok=False, fb="Você repetiria a resposta dele."),
   dict(en="Have a safe trip!", pt="Boa viagem!", ok=False, fb="Não combina com o momento.")]),
  dict(npc="Try a cheesesteak. It's a local favorite.", pt="Experimente um cheesesteak. É o preferido daqui.", opts=[
   dict(en="Can I help you?", pt="Posso ajudar?", ok=False, fb="Quem pergunta isso é o atendente."),
   dict(en="Is it free?", pt="É de graça?", ok=False, fb="Já respondeu isso; agora ele fala de comida."),
   dict(en="Great idea. Do you have a map?", pt="Ótima ideia. Vocês têm mapa?", ok=True, fb="Agradece a dica e pede um mapa.")]),
  dict(npc="Enjoy your day!", pt="Aproveite o seu dia!", opts=[
   dict(en="Thanks! You too!", pt="Obrigado! Você também!", ok=True, fb="Despedida natural."),
   dict(en="What can I see in one day?", pt="O que posso ver em um dia?", ok=False, fb="Você já perguntou isso no início."),
   dict(en="Where can I eat?", pt="Onde posso comer?", ok=False, fb="Já foi respondido.")]),
 ]),
)
