X = dict(
 key=dict(big="Are you Leo?", label="Chamar uma corrida", sub="Confirme seu nome e o motorista, diga o destino e pergunte quanto tempo vai levar."),
 mini=[
  dict(who="Marco", en="Hi! Are you {Leo?|Anna?|Sam?}", pt="Oi! Você é {o Leo?|a Anna?|o Sam?}"),
  dict(who="You", en="Yes! You're my {driver,|ride,|driver} right? Going to the {airport.|hotel.|station.}", pt="Sim! Você é meu {motorista,|corrida,|motorista} né? Vou para {o aeroporto.|o hotel.|a estação.}"),
  dict(who="Marco", en="Sure, {buckle up.|sit down.|get in.}", pt="Claro, {coloque o cinto.|sente-se.|entre.}"),
  dict(who="You", en="How long will it take? — About {twenty|ten|thirty} minutes.", pt="Quanto tempo vai demorar? — Uns {vinte|dez|trinta} minutos."),
 ],
 dlg=[
  dict(who="Marco", en="Hi! Are you {Leo?|Sam?}", pt="Oi! Você é {o Leo?|o Sam?}"),
  dict(who="You", en="Yes! You're my {driver,|ride,} right?", pt="Sim! Você é meu {motorista,|motorista,} né?"),
  dict(who="Marco", en="That's right. Going to the {airport?|hotel?}", pt="Isso. Vai para {o aeroporto?|o hotel?}"),
  dict(who="You", en="Yes, please. {Terminal two.|Terminal one.}", pt="Sim, por favor. {Terminal dois.|Terminal um.}"),
  dict(who="Marco", en="Let me put your bag in the {trunk.|back.}", pt="Deixe-me pôr sua mala no {porta-malas.|banco de trás.}"),
  dict(who="You", en="Thanks. Can I sit in the {front?|back?}", pt="Valeu. Posso sentar {na frente?|atrás?}"),
  dict(who="Marco", en="Sure, {buckle up.|sit down.}", pt="Claro, {coloque o cinto.|sente-se.}"),
  dict(who="You", en="How long will it {take?|be?}", pt="Quanto tempo vai {demorar?|ser?}"),
  dict(who="Marco", en="About {twenty|thirty} minutes.", pt="Uns {vinte|trinta} minutos."),
 ],
 vocab=[
  dict(w="ride", pt="corrida, carona", e="🚘", ex=["I need a ride.", "The ride is short."]),
  dict(w="car", pt="carro", e="🚗", ex=["The car is blue.", "Is this your car?"]),
  dict(w="speed", pt="velocidade", e="💨", ex=["The speed is slow.", "Marco drives at a safe speed."]),
  dict(w="front", pt="frente", e="⬆️", ex=["I sit in the front.", "The front seat is free."]),
  dict(w="route", pt="trajeto, rota", e="🗺️", ex=["The route is short.", "This route is fast."]),
  dict(w="destination", pt="destino", e="📍", ex=["My destination is the airport.", "Type your destination."]),
 ],
 molds=[
  dict(title="Confirmar o motorista", frame="Yes! You're my {who}, right?", slots=[dict(key="who", opts=["driver", "ride", "Marco"])], model="Yes! You're my driver, right?", note="Right? no fim confirma algo. Dá para dizer isso com um sorriso."),
  dict(title="Dizer o destino", frame="Yes, please. {place}.", slots=[dict(key="place", opts=["Terminal two", "The airport", "Main Street", "The hotel"])], model="Yes, please. Terminal two.", note="Please deixa o pedido educado. Fale só o lugar."),
  dict(title="Escrever ao motorista", frame="Hi! I'm at the {place}. I'm wearing a {color} jacket.", slots=[dict(key="place", opts=["main door", "front door", "red door"]), dict(key="color", opts=["blue", "black", "green"])], model="Hi! I'm at the main door. I'm wearing a blue jacket.", note="Uma mensagem curta ajuda o motorista a achar você."),
 ],
 sounds=[
  dict(say="Are you Leo?", tag="ligação: are you", tip="Una are e you: 'arió'. Acentue LE-o."),
  dict(say="Can I sit in the front?", tag="ligação: sit in", tip="Una sit e in: 'sitin'. O i de sit é curto, não 'sít' comprido."),
  dict(say="How long will it take?", tag="ritmo: HOW LONG will it TAKE", tip="Acentue HOW, LONG e TAKE; 'will it' fica rápido: 'wilit'."),
 ],
 role=dict(turns=[
  dict(npc="Hi! Are you Leo?", opts=[
   dict(en="Yes! You're my driver, right?", pt="Sim! Você é meu motorista, né?", reply="That's right. Going to the airport?"),
   dict(en="Yes, I'm Leo. Are you Marco?", pt="Sim, sou o Leo. Você é o Marco?", reply="That's right. Going to the airport?"),
   dict(en="Hi! Yes, that's me.", pt="Oi! Sim, sou eu.", reply="That's right. Going to the airport?")]),
  dict(npc="Going to the airport?", opts=[
   dict(en="Yes, please. Terminal two.", pt="Sim, por favor. Terminal dois.", reply="Okay. Let me put your bag in the trunk."),
   dict(en="Yes. Terminal one, please.", pt="Sim. Terminal um, por favor.", reply="Okay. Let me put your bag in the trunk."),
   dict(en="Yes, to the airport, please.", pt="Sim, para o aeroporto, por favor.", reply="Okay. Let me put your bag in the trunk.")]),
  dict(npc="Let me put your bag in the trunk.", opts=[
   dict(en="Thanks. Can I sit in the front?", pt="Valeu. Posso sentar na frente?", reply="Sure, buckle up."),
   dict(en="Thank you. Can I sit in the back?", pt="Obrigado. Posso sentar atrás?", reply="Sure, buckle up."),
   dict(en="Thanks a lot! Can I open the door?", pt="Muito obrigado! Posso abrir a porta?", reply="Sure, buckle up.")]),
  dict(npc="Sure, buckle up.", opts=[
   dict(en="How long will it take?", pt="Quanto tempo vai demorar?", reply="About twenty minutes."),
   dict(en="Okay. How long is the ride?", pt="Ok. Quanto tempo dura a corrida?", reply="About twenty minutes."),
   dict(en="Done! Is it far?", pt="Pronto! É longe?", reply="About twenty minutes.")]),
 ], change=["O motorista pergunta o nome e é outro: diga que não é você e confira o app.", "Você esqueceu a mala no porta-malas: avise o motorista antes de sair.", "O trânsito está ruim: pergunte se vai demorar mais."]),
 writing=dict(task="Escreva 2 ou 3 frases para o motorista: diga seu nome, o destino e pergunte quanto tempo vai levar.", model="Hi! I'm Leo. I'm going to the airport, terminal two. How long will it take?", kw=["airport", "terminal", "long", "take"], checks=["Disse seu nome.", "Disse o destino.", "Perguntou quanto tempo vai levar."]),
 scenes=dict(pool=["street", "airport", "airport2", "park"], npc=dict(g="m", role="driver"), you=dict(g="m")),
 convo=dict(npc=dict(name="Marco"), story="Você pediu uma corrida em Los Angeles. O Marco é o motorista.", turns=[
  dict(npc="Hi! Are you Leo?", pt="Oi! Você é o Leo?", opts=[
   dict(en="Yes! You're my driver, right?", pt="Sim! Você é meu motorista, né?", ok=True, fb="Confirma e checa o motorista."),
   dict(en="Terminal two.", pt="Terminal dois.", ok=False, fb="Ele ainda não perguntou o destino."),
   dict(en="How long will it take?", pt="Quanto tempo vai demorar?", ok=False, fb="Cedo demais: confirme primeiro.")]),
  dict(npc="That's right. Going to the airport?", pt="Isso. Vai para o aeroporto?", opts=[
   dict(en="Sure, buckle up.", pt="Claro, coloque o cinto.", ok=False, fb="Essa fala é do motorista."),
   dict(en="Yes, please. Terminal two.", pt="Sim, por favor. Terminal dois.", ok=True, fb="Confirma o destino."),
   dict(en="Can I sit in the front?", pt="Posso sentar na frente?", ok=False, fb="Primeiro responda a pergunta.")]),
  dict(npc="Let me put your bag in the trunk.", pt="Deixe-me pôr sua mala no porta-malas.", opts=[
   dict(en="Thanks. Can I sit in the front?", pt="Valeu. Posso sentar na frente?", ok=True, fb="Agradece e pede o banco."),
   dict(en="About twenty minutes.", pt="Uns vinte minutos.", ok=False, fb="Essa é a fala dele."),
   dict(en="Yes! You're my driver, right?", pt="Sim! Você é meu motorista, né?", ok=False, fb="Já foi confirmado.")]),
  dict(npc="Sure, buckle up.", pt="Claro, coloque o cinto.", opts=[
   dict(en="Are you Leo?", pt="Você é o Leo?", ok=False, fb="O Leo é você."),
   dict(en="Terminal two.", pt="Terminal dois.", ok=False, fb="Já disse o terminal."),
   dict(en="How long will it take?", pt="Quanto tempo vai demorar?", ok=True, fb="Próxima pergunta natural.")]),
  dict(npc="About twenty minutes.", pt="Uns vinte minutos.", opts=[
   dict(en="Great, thank you!", pt="Ótimo, obrigado!", ok=True, fb="Resposta curta e simpática."),
   dict(en="Let me put your bag in the trunk.", pt="Deixe-me pôr sua mala no porta-malas.", ok=False, fb="Essa fala é do motorista."),
   dict(en="Going to the airport?", pt="Vai para o aeroporto?", ok=False, fb="Já foi respondido.")]),
 ]),
)
