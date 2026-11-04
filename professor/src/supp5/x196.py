X = dict(
 key=dict(big="Can you hear me?", label="Checar som e imagem", sub="Na chamada de vídeo, confira primeiro se o outro lado vê e ouve. Frases curtas resolvem rápido."),
 mini=[
  dict(who="You", en="Hi, Ruth! Can you {see|hear} me?", pt="Oi, Ruth! Você {me vê|me ouve}?"),
  dict(who="Ruth", en="A little. Please {turn up|turn down} the volume.", pt="Um pouco. Por favor, {aumente|diminua} o volume."),
  dict(who="You", en="Okay. Is it {better|clear} now?", pt="Certo. Está {melhor|claro} agora?"),
  dict(who="Ruth", en="Yes! I {love|like} your {room.|screen.|place.}", pt="Sim! Eu {adoro|gosto d}{seu quarto.|a sua tela.|o seu lugar.}"),
 ],
 dlg=[
  dict(who="Ruth", en="Hi, {Mom!|Mama!} Can you {see|hear} me?", pt="Oi, {mãe!|mamãe!} Você {me vê?|me ouve?}"),
  dict(who="You", en="Hi, {honey!|dear!} Yes, I can {see|hear} you!", pt="Oi, {querida!|querida!} Sim, eu {vejo|ouço} você!"),
  dict(who="Ruth", en="Can you {hear|see} me?", pt="Você {me ouve?|me vê?}"),
  dict(who="You", en="A little. Turn {up|down} the {volume.|sound.}", pt="Um pouco. {Aumente|Diminua} o {volume.|som.}"),
  dict(who="Ruth", en="{Better|Good} now?", pt="{Melhor|Bom} agora?"),
  dict(who="You", en="Yes, {perfect.|great.} How are you?", pt="Sim, {perfeito.|ótimo.} Como você está?"),
  dict(who="Ruth", en="I'm great. I {love|like} my new place.", pt="Estou ótima. Eu {adoro|gosto d}o meu lugar novo."),
  dict(who="You", en="Show me your {apartment!|room!}", pt="Me mostre seu {apartamento!|quarto!}"),
  dict(who="Ruth", en="Okay. This is my {living room.|kitchen.}", pt="Ok. Esta é minha {sala.|cozinha.}"),
 ],
 vocab=[
  dict(w="video", pt="vídeo", e="📹", ex=["I make a video call.", "The video is clear."]),
  dict(w="volume", pt="volume", e="🔊", ex=["Turn up the volume.", "The volume is low."]),
  dict(w="winter", pt="inverno", e="❄️", ex=["It is cold in winter.", "I like winter."]),
  dict(w="miss", pt="sentir saudade", e="💛", ex=["I miss you.", "We miss our family."]),
  dict(w="mom", pt="mãe", e="👩", ex=["Hi, Mom!", "My mom calls me."]),
  dict(w="connection", pt="conexão", e="📶", ex=["The connection is bad.", "I have a good connection."]),
 ],
 molds=[
  dict(title="Checar se o outro ouve ou vê", frame="Can you {verb} me? {fix}.", slots=[dict(key="verb", opts=["see", "hear", "understand"]), dict(key="fix", opts=["Turn up the volume", "Please say it again", "Talk a little louder"])], model="Can you see me? Turn up the volume.", note="Can you + verbo base. A segunda frase é o pedido para resolver."),
  dict(title="Pedir para ver", frame="Show me your {thing}!", slots=[dict(key="thing", opts=["apartment", "room", "kitchen", "new bag"])], model="Show me your apartment!", note="Show me + your + algo. Serve para chamada de vídeo e para a vida real."),
  dict(title="Escrever uma mensagem de despedida", frame="I {feeling} you. {end}.", slots=[dict(key="feeling", opts=["miss", "love", "really miss"]), dict(key="end", opts=["Talk soon", "Call me later", "Bye for now"])], model="I miss you. Talk soon.", note="Miss e love são verbos de estado: sem -ing. Despedidas curtas e carinhosas."),
 ],
 sounds=[
  dict(say="Can you hear me?", tag="redução: can you", tip="Can you soa 'kenya'. Junte as duas palavras e acentue só HEAR."),
  dict(say="Turn up the volume.", tag="ligação: turn up", tip="Una turn + up: 'turnup'. A frase tem ritmo de TURN UP, VOLume."),
  dict(say="I miss you.", tag="ligação: miss you", tip="Miss you soa quase 'mi-shu'. Não pare entre as palavras."),
 ],
 role=dict(turns=[
  dict(npc="Hi! Can you see me?", opts=[
   dict(en="Yes, I can see you!", pt="Sim, eu vejo você!", reply="Great! Can you hear me?"),
   dict(en="Hi! Yes, I see you now.", pt="Oi! Sim, eu vejo você agora.", reply="Great! Can you hear me?"),
   dict(en="A little. The picture is small.", pt="Um pouco. A imagem está pequena.", reply="Let me move the camera. Can you hear me?")]),
  dict(npc="Can you hear me?", opts=[
   dict(en="A little. Turn up the volume.", pt="Um pouco. Aumente o volume.", reply="Okay. Better now?"),
   dict(en="No, I can't hear you.", pt="Não, não ouço você.", reply="Oh! Let me fix it. Better now?"),
   dict(en="Yes, I can hear you.", pt="Sim, eu ouço você.", reply="Perfect! Better now?")]),
  dict(npc="Better now?", opts=[
   dict(en="Yes, perfect. How are you?", pt="Sim, perfeito. Como você está?", reply="I'm great. I love my new place."),
   dict(en="Yes, now it's clear. How are you?", pt="Sim, agora está claro. Como você está?", reply="I'm great. I love my new place."),
   dict(en="Yes, great. How is your day?", pt="Sim, ótimo. Como está seu dia?", reply="It's good. I love my new place.")]),
  dict(npc="I love my new place.", opts=[
   dict(en="Show me your apartment!", pt="Me mostre seu apartamento!", reply="Okay. This is my living room."),
   dict(en="Show me your kitchen!", pt="Me mostre sua cozinha!", reply="Okay. This is my kitchen."),
   dict(en="Show me your room!", pt="Me mostre seu quarto!", reply="Okay. This is my room.")]),
 ], change=["A tela congela: diga que a conexão está ruim e peça para ligar de novo.", "A pessoa está no mudo: avise com 'You're on mute'.", "Já é tarde: diga 'I miss you' e 'Talk soon' para se despedir."]),
 writing=dict(task="Você está em uma chamada de vídeo com uma amiga. Escreva 2 ou 3 frases: pergunte se ela ouve, peça para aumentar o volume e peça para ver a casa dela.", model="Hi! Can you hear me? Turn up the volume, please. Show me your apartment!", kw=["hear", "volume", "show", "apartment"], checks=["Perguntou se ela ouve.", "Pediu para aumentar o volume.", "Pediu para ver a casa."]),
 scenes=dict(pool=["living", "home1", "bedroom", "kitchen"], npc=dict(g="f", role="friend"), you=dict(g="f")),
 convo=dict(npc=dict(name="Ruth"), story="Você liga em vídeo para a sua amiga Ruth, que acabou de mudar para um apartamento novo.", turns=[
  dict(npc="Hi! Can you see me?", pt="Oi! Você me vê?", opts=[
   dict(en="Yes, I can see you!", pt="Sim, eu vejo você!", ok=True, fb="Resposta natural com can."),
   dict(en="Turn up the volume.", pt="Aumente o volume.", ok=False, fb="A pergunta é sobre imagem, não som."),
   dict(en="This is my living room.", pt="Esta é minha sala.", ok=False, fb="Ainda é cedo para mostrar a casa.")]),
  dict(npc="Can you hear me?", pt="Você me ouve?", opts=[
   dict(en="Yes, I can see you!", pt="Sim, eu vejo você!", ok=False, fb="Ela perguntou sobre o som."),
   dict(en="A little. Turn up the volume.", pt="Um pouco. Aumente o volume.", ok=True, fb="Diz o problema e pede a solução."),
   dict(en="I love my new place.", pt="Adoro meu lugar novo.", ok=False, fb="Essa fala é da Ruth.")]),
  dict(npc="Better now?", pt="Melhor agora?", opts=[
   dict(en="Yes, perfect. How are you?", pt="Sim, perfeito. Como você está?", ok=True, fb="Responde e puxa conversa."),
   dict(en="Can you hear me?", pt="Você me ouve?", ok=False, fb="Você já testou o som."),
   dict(en="Okay. This is my living room.", pt="Ok. Esta é minha sala.", ok=False, fb="A sala é da Ruth, não sua.")]),
  dict(npc="I'm great. I love my new place.", pt="Estou ótima. Adoro meu lugar novo.", opts=[
   dict(en="A little. Turn up the volume.", pt="Um pouco. Aumente o volume.", ok=False, fb="O som já está bom."),
   dict(en="Show me your apartment!", pt="Me mostre seu apartamento!", ok=True, fb="Pedido natural para ver a casa nova."),
   dict(en="Better now?", pt="Melhor agora?", ok=False, fb="Já resolveram o som.")]),
  dict(npc="Okay. This is my living room.", pt="Ok. Esta é minha sala.", opts=[
   dict(en="Can you see me?", pt="Você me vê?", ok=False, fb="Agora você olha a sala dela."),
   dict(en="Nice! I miss you. Talk soon.", pt="Que legal! Sinto sua falta. Falamos logo.", ok=True, fb="Elogio e despedida carinhosa."),
   dict(en="Turn up the volume.", pt="Aumente o volume.", ok=False, fb="O som já está bom.")]),
 ]),
)
