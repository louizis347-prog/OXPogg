"""Bloco extra da aula 90: no museu."""
X = dict(
 key=dict(big="Two tickets, please", label="Comprar ingressos", sub="Peça os ingressos, mostre a carteirinha, pergunte o horário e se pode tirar fotos. No diálogo original o aluno atende; aqui o treino é como visitante."),
 mini=[
  dict(who="You", en="Hi! {Two|Three|One} tickets, please.", pt="Oi! {Dois|Três|Um} ingresso(s), por favor."),
  dict(who="Marco", en="That's thirty dollars. {Students|Children|Seniors} get a discount.", pt="São trinta dólares. {Estudantes|Crianças|Idosos} têm desconto."),
  dict(who="You", en="I have a {student card|child ticket|senior card}.", pt="Tenho {carteirinha de estudante|ingresso infantil|carteira de idoso}."),
  dict(who="Marco", en="Then it's {twenty-four|twenty|twelve} dollars.", pt="Então são {vinte e quatro|vinte|doze} dólares."),
 ],
 dlg=[
  dict(who="Marco", en="Hi! {Two|Three} tickets, please.", pt="Oi! {Dois|Três} ingressos, por favor."),
  dict(who="You", en="That's thirty dollars. {Students|Children} get a discount.", pt="São trinta dólares. {Estudantes|Crianças} têm desconto."),
  dict(who="Marco", en="I have a {student card.|child ticket.}", pt="Tenho {carteirinha de estudante.|ingresso infantil.}"),
  dict(who="You", en="Then it's {twenty-four|twenty} dollars.", pt="Então são {vinte e quatro|vinte} dólares."),
  dict(who="Marco", en="What time does the museum {close?|open?}", pt="Que horas o museu {fecha?|abre?}"),
  dict(who="You", en="At {five|six} o'clock.", pt="Às {cinco.|seis.}"),
  dict(who="Marco", en="Can I take {photos?|pictures?}", pt="Posso tirar {fotos?|fotos?}"),
  dict(who="You", en="Yes, but no {flash.|video.}", pt="Sim, mas sem {flash.|vídeo.}"),
  dict(who="Marco", en="Enjoy the {museum!|show!}", pt="Aproveite o {museu!|show!}"),
 ],
 vocab=[
  dict(w="art", pt="arte", e="🎨", ex=["I like modern art.", "The art is on the second floor."]),
  dict(w="painting", pt="pintura, quadro", e="🖼️", ex=["This painting is beautiful.", "My favorite painting is blue."]),
  dict(w="floor", pt="andar", e="🏢", ex=["The paintings are on the second floor.", "Which floor is the cafe on?"]),
  dict(w="flash", pt="flash da câmera", e="⚡", ex=["No flash, please.", "Flash can hurt old paintings."]),
  dict(w="artist", pt="artista", e="🧑‍🎨", ex=["The artist is here.", "He is a famous artist."]),
  dict(w="gift shop", pt="lojinha de lembranças", e="🎁", ex=["The gift shop is near the door.", "I buy a card at the gift shop."]),
 ],
 molds=[
  dict(title="Pedir ingressos", frame="{number} tickets, please.", slots=[dict(key="number", opts=["Two", "Three", "Four"])], model="Two tickets, please.", note="Número + tickets, sempre no plural a partir de dois."),
  dict(title="Perguntar o horário", frame="What time does the {place} close?", slots=[dict(key="place", opts=["museum", "gift shop", "exhibit", "cafe"])], model="What time does the museum close?", note="Depois de does, o verbo fica sem -s: close."),
  dict(title="Escrever uma pergunta", frame="Hi! Can I {verb} {thing} here?", slots=[dict(key="verb", opts=["take", "see", "buy"]), dict(key="thing", opts=["photos", "a map", "tickets"])], model="Hi! Can I take photos here?", note="Can I + verbo base é o jeito educado de pedir permissão."),
 ],
 sounds=[
  dict(say="What time does the museum close?", tag="ritmo: WHAT time does the mu-SE-um CLOSE", tip="Acentue TIME, SE e CLOSE. 'does the' fica fraco: 'duz-thuh'."),
  dict(say="Can I take photos?", tag="ligação: can I", tip="Una can e I: 'kenai'. O can fica fraco: 'kn'."),
  dict(say="At five o'clock.", tag="ligação: at five o'clock", tip="Una as palavras sem pausa: 'atfaivaclók'. Acentue FIVE e CLOCK."),
 ],
 role=dict(turns=[
  dict(npc="Hello! Welcome to the museum. How can I help?", opts=[
   dict(en="Hi! Two tickets, please.", pt="Oi! Dois ingressos, por favor.", reply="That's thirty dollars. Students get a discount."),
   dict(en="Hi! Three tickets, please.", pt="Oi! Três ingressos, por favor.", reply="That's forty-five dollars. Students get a discount."),
   dict(en="Hello! One ticket, please.", pt="Olá! Um ingresso, por favor.", reply="That's fifteen dollars. Students get a discount.")]),
  dict(npc="Students get a discount.", opts=[
   dict(en="I have a student card.", pt="Tenho carteirinha de estudante.", reply="Then it's twenty-four dollars."),
   dict(en="Here is my student card.", pt="Aqui está minha carteirinha.", reply="Thanks. Then it's twenty-four dollars."),
   dict(en="Is there a discount for two?", pt="Tem desconto para dois?", reply="Yes, for students. Do you have a card?")]),
  dict(npc="Then it's twenty-four dollars.", opts=[
   dict(en="What time does the museum close?", pt="Que horas o museu fecha?", reply="At five o'clock."),
   dict(en="What time does it close today?", pt="Que horas fecha hoje?", reply="At five o'clock."),
   dict(en="Is the museum open late?", pt="O museu fica aberto até tarde?", reply="No, it closes at five o'clock.")]),
  dict(npc="At five o'clock.", opts=[
   dict(en="Can I take photos?", pt="Posso tirar fotos?", reply="Yes, but no flash. Enjoy the museum!"),
   dict(en="Can I take a photo of the painting?", pt="Posso fotografar o quadro?", reply="Yes, but no flash. Enjoy the museum!"),
   dict(en="Can I use my phone for photos?", pt="Posso usar o celular para fotos?", reply="Yes, but no flash. Enjoy the museum!")]),
 ], change=["Você esqueceu a carteirinha: pergunte se há outro desconto.", "O museu fecha mais cedo hoje: pergunte quanto tempo você tem.", "Fotos não são permitidas na sala nova: pergunte onde pode fotografar."]),
 writing=dict(task="Escreva 2 ou 3 frases na bilheteria: peça dois ingressos, diga que tem carteirinha de estudante e pergunte se pode tirar fotos.", model="Hi! Two tickets, please. I have a student card. Can I take photos?", kw=["tickets", "student", "card", "photos"], checks=["Pediu os ingressos.", "Disse que tem carteirinha.", "Perguntou sobre fotos."]),
 scenes=dict(pool=["museum", "artroom", "library", "counter"], npc=dict(g="m", role="clerk"), you=dict(g="f")),
 convo=dict(npc=dict(name="Marco"), story="Você está na bilheteria de um museu. Marco trabalha lá.", turns=[
  dict(npc="Hello! Welcome to the museum. How can I help?", pt="Olá! Bem-vindo ao museu. Como posso ajudar?", opts=[
   dict(en="Enjoy the museum!", pt="Aproveite o museu!", ok=False, fb="Essa é fala de quem atende, no fim."),
   dict(en="Hi! Two tickets, please.", pt="Oi! Dois ingressos, por favor.", ok=True, fb="Pedido claro e educado."),
   dict(en="At five o'clock.", pt="Às cinco.", ok=False, fb="Ninguém perguntou a hora.")]),
  dict(npc="That's thirty dollars. Students get a discount.", pt="São trinta dólares. Estudantes têm desconto.", opts=[
   dict(en="I have a student card.", pt="Tenho carteirinha de estudante.", ok=True, fb="Mostra que tem direito ao desconto."),
   dict(en="Can I take photos?", pt="Posso tirar fotos?", ok=False, fb="Primeiro o preço."),
   dict(en="Two tickets, please.", pt="Dois ingressos, por favor.", ok=False, fb="Você já pediu.")]),
  dict(npc="Then it's twenty-four dollars.", pt="Então são vinte e quatro dólares.", opts=[
   dict(en="I have a student card.", pt="Tenho carteirinha de estudante.", ok=False, fb="Já foi dito."),
   dict(en="What time does the museum close?", pt="Que horas o museu fecha?", ok=True, fb="Boa pergunta depois de pagar."),
   dict(en="Thirty dollars.", pt="Trinta dólares.", ok=False, fb="O preço mudou para vinte e quatro.")]),
  dict(npc="At five o'clock.", pt="Às cinco.", opts=[
   dict(en="Can I take photos?", pt="Posso tirar fotos?", ok=True, fb="Pede permissão com Can I."),
   dict(en="What time does the museum close?", pt="Que horas o museu fecha?", ok=False, fb="Ele acabou de responder."),
   dict(en="Enjoy the museum!", pt="Aproveite o museu!", ok=False, fb="Fala dele.")]),
  dict(npc="Yes, but no flash. Enjoy the museum!", pt="Sim, mas sem flash. Aproveite o museu!", opts=[
   dict(en="Thanks! Have a nice day!", pt="Obrigado! Tenha um bom dia!", ok=True, fb="Resposta natural."),
   dict(en="Two tickets, please.", pt="Dois ingressos, por favor.", ok=False, fb="Já está resolvido."),
   dict(en="I have a student card.", pt="Tenho carteirinha de estudante.", ok=False, fb="Já foi dito.")]),
 ]),
)
