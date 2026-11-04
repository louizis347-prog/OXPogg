X = dict(
 key=dict(big="Surprise!", label="Festa surpresa", sub="Você avisa que ela está chegando, ajuda a esconder todo mundo, apaga as luzes, fica em silêncio e grita Surprise! na hora certa."),
 mini=[
  dict(who="Rosa", en="Shh! She's coming. Hide {behind the door|under the table|in the kitchen}!", pt="Shh! Ela está chegando. Escondam-se {atrás da porta|embaixo da mesa|na cozinha}!"),
  dict(who="You", en="Okay! Is the {cake|food|gift} on the table?", pt="Ok! {O bolo|A comida|O presente} está na mesa?"),
  dict(who="Rosa", en="Yes. Turn off the {lights|music|TV}.", pt="Sim. Desligue {as luzes|a música|a TV}."),
  dict(who="You", en="Quiet, quiet… {Surprise!|Hello!|Happy birthday!}", pt="Silêncio, silêncio… {Surpresa!|Olá!|Feliz aniversário!}"),
 ],
 dlg=[
  dict(who="Rosa", en="Shh! She's {coming.|here.}", pt="Shh! Ela está {chegando.|aqui.}"),
  dict(who="You", en="Everyone {hide!|wait!}", pt="Todos {se escondam!|esperem!}"),
  dict(who="Rosa", en="Is the {cake ready?|food ready?}", pt="{O bolo está pronto?|A comida está pronta?}"),
  dict(who="You", en="Yes, it's on the {table.|counter.}", pt="Sim, está {na mesa.|no balcão.}"),
  dict(who="Rosa", en="Turn off the {lights.|music.}", pt="Apague {as luzes.|a música.}"),
  dict(who="You", en="{Quiet, quiet…|Shh, shh…}", pt="{Silêncio, silêncio…|Psiu, psiu…}"),
  dict(who="Rosa", en="Surprise! {Happy birthday!|Happy birthday, Mia!}", pt="Surpresa! {Feliz aniversário!|Feliz aniversário, Mia!}"),
  dict(who="You", en="Oh my {gosh!|goodness!} I can't believe it!", pt="Meu {Deus!|nossa!} Não acredito!"),
  dict(who="Rosa", en="You {didn't|did not} know?", pt="Você {não sabia?|não sabia mesmo?}"),
 ],
 vocab=[
  dict(w="candle", pt="vela", e="🕯️", ex=["Blow out the candle.", "There are ten candles."]),
  dict(w="surprise", pt="surpresa", e="🎊", ex=["It is a surprise party.", "Surprise! Happy birthday!"]),
  dict(w="secret", pt="segredo", e="🤫", ex=["Keep it a secret.", "The party is a secret."]),
  dict(w="dark", pt="escuro", e="🌑", ex=["The room is dark.", "It is dark outside."]),
  dict(w="quiet", pt="silencioso / quieto", e="🤐", ex=["Be quiet, please.", "The house is quiet."]),
  dict(w="door", pt="porta", e="🚪", ex=["Hide behind the door.", "The door is open."]),
 ],
 molds=[
  dict(title="Mandar todos se esconderem", frame="Everyone, hide {place}!", slots=[dict(key="place", opts=["behind the door", "behind the sofa", "in the kitchen", "under the table"])], model="Everyone, hide behind the door!", note="Hide + lugar. Ordem sem 'to'."),
  dict(title="Pedir para desligar", frame="Turn off the {thing}.", slots=[dict(key="thing", opts=["lights", "music", "TV", "phone"])], model="Turn off the lights.", note="Turn off = desligar/apagar. O oposto é turn on."),
  dict(title="Escrever um cartão", frame="Happy birthday, {name}! This {item} is for you. Make a wish!", slots=[dict(key="name", opts=["Mia", "Tom", "Rosa"]), dict(key="item", opts=["card", "cake", "book"])], model="Happy birthday, Mia! This card is for you. Make a wish!", note="This ... is for you = isto é para você. Make a wish = faça um pedido."),
 ],
 sounds=[
  dict(say="Surprise!", tag="acento: sur-PRISE", tip="A força cai na 2ª sílaba: 'sur-PRAIZ'. Alongue o PRISE."),
  dict(say="Happy birthday!", tag="acento: HAP-py BIRTH-day", tip="Acentue HAP e BIRTH; 'py' e 'day' ficam mais fracas e curtas."),
  dict(say="Quiet, quiet…", tag="acento: QUI-et", tip="Duas sílabas, força na primeira: 'QUAI-et'. Fale baixinho."),
 ],
 role=dict(turns=[
  dict(npc="Shh! She's coming.", opts=[
   dict(en="Everyone hide!", pt="Todos se escondam!", reply="Behind the sofa! Quick!"),
   dict(en="Okay! Hide behind the door!", pt="Ok! Escondam-se atrás da porta!", reply="Good idea! Quick!"),
   dict(en="Quiet, everyone! Hide!", pt="Silêncio, pessoal! Escondam-se!", reply="Yes! Behind the curtain!")]),
  dict(npc="Is the cake ready?", opts=[
   dict(en="Yes, it's on the table.", pt="Sim, está na mesa.", reply="Great. Turn off the lights."),
   dict(en="Yes, and the candles are ready.", pt="Sim, e as velas estão prontas.", reply="Perfect. Turn off the lights."),
   dict(en="Yes, it's in the kitchen.", pt="Sim, está na cozinha.", reply="Bring it out! Then turn off the lights.")]),
  dict(npc="Turn off the lights.", opts=[
   dict(en="Quiet, quiet…", pt="Silêncio, silêncio…", reply="Here she comes. Ready?"),
   dict(en="Okay. Shh, everyone!", pt="Ok. Shh, pessoal!", reply="Here she comes. Ready?"),
   dict(en="Done. It's very dark.", pt="Pronto. Está muito escuro.", reply="Good. Here she comes. Ready?")]),
  dict(npc="Here she comes. Ready?", opts=[
   dict(en="Surprise! Happy birthday!", pt="Surpresa! Feliz aniversário!", reply="Look at her face! She didn't know."),
   dict(en="Surprise! Make a wish!", pt="Surpresa! Faça um pedido!", reply="She is so happy! She didn't know."),
   dict(en="Surprise! We love you!", pt="Surpresa! Amamos você!", reply="Aww! She didn't know.")]),
 ], change=["A aniversariante chega mais cedo: diga 'Shh! Hide!' e peça para todos se esconderem.", "O bolo não está na mesa: diga onde ele está.", "Alguém liga a TV alto: peça para desligar."]),
 writing=dict(task="Você escreve um cartão para uma amiga em uma festa surpresa. Escreva 2 ou 3 frases: Feliz aniversário, o nome dela, e um desejo.", model="Happy birthday, Mia! Surprise! Make a wish and blow out the candles.", kw=["happy", "birthday", "surprise", "wish"], checks=["Desejou feliz aniversário.", "Usou o nome da amiga.", "Falou de um desejo."]),
 scenes=dict(pool=["living", "home1", "kitchen", "garden"], npc=dict(g="f", role="friend"), you=dict(g="m")),
 convo=dict(npc=dict(name="Rosa"), story="Você está na festa surpresa da Mia. Ajude a Rosa a se preparar.", turns=[
  dict(npc="Shh! She's coming.", pt="Shh! Ela está chegando.", opts=[
   dict(en="Happy birthday to you!", pt="Feliz aniversário!", ok=False, fb="Cedo demais: ela ainda não chegou."),
   dict(en="Everyone hide!", pt="Todos se escondam!", ok=True, fb="Reação certa: esconder todo mundo."),
   dict(en="Is the cake ready?", pt="O bolo está pronto?", ok=False, fb="Essa pergunta é da Rosa.")]),
  dict(npc="Is the cake ready?", pt="O bolo está pronto?", opts=[
   dict(en="Yes, it's on the table.", pt="Sim, está na mesa.", ok=True, fb="Responde sim e diz onde está."),
   dict(en="Shh! She's coming.", pt="Shh! Ela está chegando.", ok=False, fb="Não responde à pergunta."),
   dict(en="Turn off the lights.", pt="Apague as luzes.", ok=False, fb="Essa ordem é da Rosa.")]),
  dict(npc="Turn off the lights.", pt="Apague as luzes.", opts=[
   dict(en="Is the cake ready?", pt="O bolo está pronto?", ok=False, fb="Você já respondeu isso."),
   dict(en="Surprise! Happy birthday!", pt="Surpresa! Feliz aniversário!", ok=False, fb="Cedo demais: ainda não é a hora."),
   dict(en="Okay. Quiet, quiet…", pt="Ok. Silêncio, silêncio…", ok=True, fb="Concorda e pede silêncio.")]),
  dict(npc="Here she comes! Ready?", pt="Lá vem ela! Prontos?", opts=[
   dict(en="Surprise! Happy birthday!", pt="Surpresa! Feliz aniversário!", ok=True, fb="O grito tradicional."),
   dict(en="Everyone hide!", pt="Todos se escondam!", ok=False, fb="Todos já estão escondidos."),
   dict(en="Turn off the lights.", pt="Apague as luzes.", ok=False, fb="As luzes já estão apagadas.")]),
  dict(npc="Look at her face! She didn't know.", pt="Olhe a cara dela! Ela não sabia.", opts=[
   dict(en="Shh! She's coming.", pt="Shh! Ela está chegando.", ok=False, fb="Ela já chegou."),
   dict(en="Is the cake ready?", pt="O bolo está pronto?", ok=False, fb="O bolo já está pronto."),
   dict(en="Yes! It's a great surprise.", pt="Sim! É uma ótima surpresa.", ok=True, fb="Reação feliz e natural.")]),
 ]),
)
