X = dict(
 key=dict(big="My key doesn't work", label="Falar de um problema no hotel", sub="Frase curta e educada para pedir ajuda na recepção: diga o que não funciona e peça que alguém resolva."),
 mini=[
  dict(who="Cole", en="Hello, front desk. How can I {help|help you|help you today}?", pt="Olá, recepção. Como posso {ajudar|ajudar você|ajudar você hoje}?"),
  dict(who="You", en="My {key|shower|TV} doesn't work.", pt="Minha {chave|ducha|TV} não funciona."),
  dict(who="Cole", en="I'm sorry. I'll send {someone|a person|help}.", pt="Sinto muito. Vou mandar {alguém|uma pessoa|ajuda}."),
  dict(who="You", en="Thank you. Also, the {air conditioner|light|TV} is off.", pt="Obrigado. Além disso, {o ar-condicionado|a luz|a TV} está desligado."),
 ],
 dlg=[
  dict(who="Cole", en="Hello, front desk. How can I {help?|help you?}", pt="Olá, recepção. Como posso {ajudar?|ajudar você?}"),
  dict(who="You", en="My {key|card} doesn't work.", pt="Minha {chave|chave-cartão} não funciona."),
  dict(who="Cole", en="I'm sorry. I'll send {someone.|a person.}", pt="Sinto muito. Vou mandar {alguém.|uma pessoa.}"),
  dict(who="You", en="Thank you. Also, the {air conditioner|light} is off.", pt="Obrigado. Além disso, {o ar-condicionado|a luz} está desligado."),
  dict(who="Cole", en="Is it too {hot?|cold?}", pt="Está muito {quente?|frio?}"),
  dict(who="You", en="Yes, very {hot.|cold.}", pt="Sim, muito {quente.|frio.}"),
  dict(who="Cole", en="We'll fix it {right away.|very soon.}", pt="Vamos consertar {já.|logo.}"),
  dict(who="You", en="Thanks {a lot.|so much.}", pt="{Muito obrigado.|Obrigado mesmo.}"),
  dict(who="Cole", en="Sorry again for the {trouble!|problem!}", pt="Desculpe de novo pelo {problema!|transtorno!}"),
 ],
 vocab=[
  dict(w="towel", pt="toalha", e="🛁", ex=["Can I have a towel, please?", "The towel is on the bed."]),
  dict(w="broken", pt="quebrado", e="💔", ex=["The TV is broken.", "My phone is broken."]),
  dict(w="fix", pt="consertar", e="🔧", ex=["Can you fix the light?", "They fix it right away."]),
  dict(w="lobby", pt="saguão", e="🏨", ex=["I am in the lobby.", "The lobby is big."]),
  dict(w="elevator", pt="elevador", e="🛗", ex=["The elevator is on the left.", "I take the elevator."]),
  dict(w="front desk", pt="recepção", e="🛎️", ex=["Call the front desk.", "The front desk is open all night."]),
 ],
 molds=[
  dict(title="Dizer o que não funciona", frame="My {thing} doesn't work.", slots=[dict(key="thing", opts=["key", "TV", "shower", "air conditioner"])], model="My key doesn't work.", note="Doesn't work = não funciona. Com coisa no singular, use doesn't."),
  dict(title="Pedir para consertar", frame="Can you fix the {thing}, please?", slots=[dict(key="thing", opts=["light", "shower", "TV", "air conditioner"])], model="Can you fix the light, please?", note="Can you...? é um pedido educado. Depois vem o verbo base: fix."),
  dict(title="Escrever para a recepção", frame="Hello. The {item} is broken in room {room}. Can you {act}, please?", slots=[dict(key="item", opts=["TV", "shower", "light"]), dict(key="room", opts=["412", "208", "310"]), dict(key="act", opts=["send someone", "fix it", "help me"])], model="Hello. The TV is broken in room 412. Can you send someone, please?", note="Diga o problema, o número do quarto e peça ajuda."),
 ],
 sounds=[
  dict(say="I'll send someone.", tag="redução: I'll", tip="I'll soa quase como 'ail'. O som final é um L curto, sem vogal."),
  dict(say="We'll fix it right away.", tag="redução: we'll", tip="We'll soa 'uil'. Una a 'fix it': fi-xit. Acentue FIX e a-WAY."),
  dict(say="My key doesn't work.", tag="doesn't: 'dazent'", tip="Doesn't soa 'DAZ-nt'. Acentue KEY e WORK; as outras palavras são fracas."),
 ],
 role=dict(turns=[
  dict(npc="Hello, front desk. How can I help?", opts=[
   dict(en="My key doesn't work.", pt="Minha chave não funciona.", reply="I'm sorry. I'll send someone."),
   dict(en="My TV doesn't work.", pt="Minha TV não funciona.", reply="I'm sorry. I'll send someone."),
   dict(en="The shower is broken.", pt="A ducha está quebrada.", reply="I'm sorry. I'll send someone.")]),
  dict(npc="I'm sorry. I'll send someone. Anything else?", opts=[
   dict(en="Thank you. Also, the air conditioner is off.", pt="Obrigado. Além disso, o ar-condicionado está desligado.", reply="Is it too hot?"),
   dict(en="Yes. The light is off, too.", pt="Sim. A luz também está apagada.", reply="Is it dark in the room?"),
   dict(en="Yes. Can I have a towel?", pt="Sim. Posso ter uma toalha?", reply="Sure. I'll send one.")]),
  dict(npc="Is it too hot?", opts=[
   dict(en="Yes, very hot.", pt="Sim, muito quente.", reply="We'll fix it right away."),
   dict(en="Yes, it is too hot.", pt="Sim, está quente demais.", reply="We'll fix it right away."),
   dict(en="A little hot.", pt="Um pouco quente.", reply="We'll fix it very soon.")]),
  dict(npc="We'll fix it right away. Sorry for the trouble!", opts=[
   dict(en="Thanks a lot.", pt="Muito obrigado.", reply="You're welcome. Have a nice night!"),
   dict(en="No worries. Thank you!", pt="Sem problema. Obrigado!", reply="You're welcome. Have a nice night!"),
   dict(en="Thank you for your help.", pt="Obrigado pela ajuda.", reply="You're welcome. Have a nice night!")]),
 ], change=["A pessoa diz que o problema é no quarto 412: confirme o número do quarto.", "O ar-condicionado ainda não funciona: ligue de novo e diga com educação.", "Você precisa de uma toalha extra: peça no mesmo telefonema."]),
 writing=dict(task="Você está num hotel e há um problema no quarto. Escreva 2 ou 3 frases para a recepção: diga o que não funciona e peça ajuda.", model="Hello. My key doesn't work. Can you send someone to room 412, please? Also, the air conditioner is off.", kw=["key", "room", "please", "work"], checks=["Disse o que não funciona.", "Pediu ajuda com Can you…?", "Disse o número do quarto ou deu um segundo problema."]),
 scenes=dict(pool=["lobby", "lobby1", "lobby2", "hotelroom"], npc=dict(g="m", role="receptionist"), you=dict(g="f")),
 convo=dict(npc=dict(name="Cole"), story="Você está num hotel em Miami e fala com a recepção.", turns=[
  dict(npc="Hello, front desk. How can I help?", pt="Olá, recepção. Como posso ajudar?", opts=[
   dict(en="Sorry again for the trouble!", pt="Desculpe de novo pelo problema!", ok=False, fb="Esta frase é de quem trabalha na recepção, no fim."),
   dict(en="My key doesn't work.", pt="Minha chave não funciona.", ok=True, fb="Diz o problema de forma curta e clara."),
   dict(en="We'll fix it right away.", pt="Vamos consertar já.", ok=False, fb="Quem promete consertar é o hotel.")]),
  dict(npc="I'm sorry. I'll send someone.", pt="Sinto muito. Vou mandar alguém.", opts=[
   dict(en="Thank you. Also, the air conditioner is off.", pt="Obrigado. Além disso, o ar-condicionado está desligado.", ok=True, fb="Agradece e acrescenta um segundo problema."),
   dict(en="Hello, front desk. How can I help?", pt="Olá, recepção. Como posso ajudar?", ok=False, fb="Essa fala é de quem atende."),
   dict(en="Is it too hot?", pt="Está muito quente?", ok=False, fb="Quem pergunta isso é o atendente.")]),
  dict(npc="Is it too hot?", pt="Está muito quente?", opts=[
   dict(en="I'll send someone.", pt="Vou mandar alguém.", ok=False, fb="Essa frase é da recepção."),
   dict(en="Thanks a lot.", pt="Muito obrigado.", ok=False, fb="Ainda é cedo para agradecer; responda a pergunta."),
   dict(en="Yes, very hot.", pt="Sim, muito quente.", ok=True, fb="Responde à pergunta.")]),
  dict(npc="We'll fix it right away.", pt="Vamos consertar já.", opts=[
   dict(en="Thanks a lot.", pt="Muito obrigado.", ok=True, fb="Agradece pela ajuda."),
   dict(en="Is it too hot?", pt="Está muito quente?", ok=False, fb="Essa pergunta já foi feita e respondida."),
   dict(en="My key doesn't work.", pt="Minha chave não funciona.", ok=False, fb="Esse problema você já disse.")]),
  dict(npc="Sorry again for the trouble!", pt="Desculpe de novo pelo problema!", opts=[
   dict(en="No worries. Have a good night!", pt="Sem problema. Boa noite!", ok=True, fb="Responde com simpatia e se despede."),
   dict(en="Hello, front desk. How can I help?", pt="Olá, recepção. Como posso ajudar?", ok=False, fb="Essa fala abre a conversa e é da recepção."),
   dict(en="I'll send someone.", pt="Vou mandar alguém.", ok=False, fb="Quem manda alguém é o hotel.")]),
 ]),
)
