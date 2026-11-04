X = dict(
 key=dict(big="What a cute dog!", label="Conversa no parque", sub="No parque de cães, elogie o cachorro, pergunte nome e idade e peça para os cães brincarem juntos. É um jeito fácil de puxar conversa."),
 mini=[
  dict(who="Jonah", en="Hi! What a {cute|nice|big} dog!", pt="Oi! Que cachorro {fofo!|bonito!|grande!}"),
  dict(who="You", en="Thank you! His name is {Max.|Rex.|Bobby.}", pt="Obrigado! O nome dele é {Max.|Rex.|Bobby.}"),
  dict(who="Jonah", en="How old is {he?|your dog?}", pt="Quantos anos {ele tem?|seu cachorro tem?}"),
  dict(who="You", en="He's {two|three|five} years old.", pt="Ele tem {dois|três|cinco} anos."),
 ],
 dlg=[
  dict(who="Jonah", en="Hi! What a {cute|nice} dog!", pt="Oi! Que cachorro {fofo!|bonito!}"),
  dict(who="You", en="Thank you! His name is {Max.|Rex.}", pt="Obrigado! O nome dele é {Max.|Rex.}"),
  dict(who="Jonah", en="How old is {he?|your dog?}", pt="Quantos anos {ele tem?|seu cachorro tem?}"),
  dict(who="You", en="He's {two|three} years old.", pt="Ele tem {dois|três} anos."),
  dict(who="Jonah", en="Is he {friendly?|shy?}", pt="Ele é {amigável?|tímido?}"),
  dict(who="You", en="Very! He loves to {play.|run.}", pt="Muito! Ele adora {brincar.|correr.}"),
  dict(who="Jonah", en="Can my dog {play|run} with him?", pt="Meu cachorro pode {brincar|correr} com ele?"),
  dict(who="You", en="Sure. What's your dog's {name?|age?}", pt="Claro. Qual é {o nome|a idade} do seu cachorro?"),
  dict(who="Jonah", en="Luna. She's {shy.|small.}", pt="Luna. Ela é {tímida.|pequena.}"),
 ],
 vocab=[
  dict(w="leash", pt="coleira (guia)", e="🦮", ex=["Take the leash, please.", "My dog has a red leash."]),
  dict(w="bone", pt="osso", e="🦴", ex=["The dog has a bone.", "Give him a bone."]),
  dict(w="bark", pt="latir, latido", e="🔊", ex=["I hear a bark.", "The dog can bark."]),
  dict(w="paw", pt="pata", e="🐾", ex=["Give me your paw.", "His paw is brown."]),
  dict(w="stick", pt="graveto", e="🪵", ex=["Throw the stick.", "He likes the stick."]),
  dict(w="big", pt="grande", e="🐕‍🦺", ex=["He is a big dog.", "That is a big park."]),
 ],
 molds=[
  dict(title="Elogiar o cachorro", frame="What a {adj} dog!", slots=[dict(key="adj", opts=["cute", "nice", "big"])], model="What a cute dog!", note="What a + adjetivo + substantivo mostra admiração. Dog fica no singular."),
  dict(title="Falar do seu cachorro", frame="His name is {name}. He's {age} years old.", slots=[dict(key="name", opts=["Max", "Rex", "Bobby"]), dict(key="age", opts=["two", "three", "five"])], model="His name is Max. He's two years old.", note="Para menina, use Her name e She's. A idade usa be: He's two."),
  dict(title="Escrever uma conversa", frame="Hi! {compliment} Is he {trait}? Can my dog {action} with him?", slots=[dict(key="compliment", opts=["What a cute dog!", "What a nice dog!", "What a big dog!"]), dict(key="trait", opts=["friendly", "shy", "kind"]), dict(key="action", opts=["play", "run", "walk"])], model="Hi! What a cute dog! Is he friendly? Can my dog play with him?", note="Can + verbo base pede permissão: Can my dog play?"),
 ],
 sounds=[
  dict(say="What a cute dog!", tag="ligação: what a", tip="What a soa “whata”: ligue o t ao a, sem pausa. Acentue CUTE."),
  dict(say="How old is he?", tag="redução: is he", tip="Is he soa quase “izzy”: o h fica fraco. Acentue OLD."),
  dict(say="He loves to play.", tag="ritmo: LOVES to PLAY", tip="To fica fraco: “ta”. Acentue loves e play. O s de loves soa z."),
 ],
 role=dict(turns=[
  dict(npc="Hi! What a cute dog!", opts=[
   dict(en="Thank you! His name is Max.", pt="Obrigado! O nome dele é Max.", reply="How old is he?"),
   dict(en="Thanks! He's a happy dog.", pt="Valeu! Ele é um cachorro feliz.", reply="What's his name?"),
   dict(en="Thank you! Her name is Daisy.", pt="Obrigada! O nome dela é Daisy.", reply="How old is she?")]),
  dict(npc="How old is he?", opts=[
   dict(en="He's two years old.", pt="Ele tem dois anos.", reply="Is he friendly?"),
   dict(en="He's three years old.", pt="Ele tem três anos.", reply="Is he friendly?"),
   dict(en="He's still a puppy. Six months.", pt="Ele ainda é filhote. Seis meses.", reply="Aw! Is he friendly?")]),
  dict(npc="Is he friendly?", opts=[
   dict(en="Very! He loves to play.", pt="Muito! Ele adora brincar.", reply="Can my dog play with him?"),
   dict(en="Yes! He loves to run.", pt="Sim! Ele adora correr.", reply="Can my dog play with him?"),
   dict(en="Yes, but he's a little shy.", pt="Sim, mas é um pouco tímido.", reply="Mine is shy, too. Can they play?")]),
  dict(npc="Can my dog play with him?", opts=[
   dict(en="Sure. What's your dog's name?", pt="Claro. Qual é o nome do seu cachorro?", reply="Luna. She's shy."),
   dict(en="Sure! Let's go to the grass.", pt="Claro! Vamos para a grama.", reply="Great! Her name is Luna."),
   dict(en="Sure, he'd love that.", pt="Claro, ele ia adorar.", reply="Thanks! Her name is Luna.")]),
 ], change=["O outro cachorro é grande e late muito: diga que o seu é pequeno e peça cuidado.", "Você esqueceu a guia: pergunte onde pode pegar uma.", "O cachorro do outro dono não gosta de brincar: diga que não tem problema."]),
 writing=dict(task="Escreva 2 ou 3 frases para um dono de cachorro no parque: elogie o cachorro, pergunte a idade e peça para os cães brincarem.", model="Hi! What a cute dog! How old is he? Can my dog play with him?", kw=["cute", "dog", "old", "play"], checks=["Elogiou o cachorro.", "Perguntou a idade.", "Pediu para brincarem."]),
 scenes=dict(pool=["park", "park2", "playground", "lake"], npc=dict(g="m", role="dog owner"), you=dict(g="f")),
 convo=dict(npc=dict(name="Jonah"), story="Você está no parque de cães, em Boulder, com o seu cachorro Max. O Jonah chega com a Luna e puxa conversa.", turns=[
  dict(npc="Hi! What a cute dog!", pt="Oi! Que cachorro fofo!", opts=[
   dict(en="Thank you! His name is Max.", pt="Obrigada! O nome dele é Max.", ok=True, fb="Agradece e diz o nome."),
   dict(en="Sure. What's your dog's name?", pt="Claro. Qual é o nome do seu cachorro?", ok=False, fb="Isso responde a um pedido, não a um elogio."),
   dict(en="Luna. She's shy.", pt="Luna. Ela é tímida.", ok=False, fb="Essa fala é do Jonah.")]),
  dict(npc="How old is he?", pt="Quantos anos ele tem?", opts=[
   dict(en="Very! He loves to play.", pt="Muito! Ele adora brincar.", ok=False, fb="Essa resposta é para 'Is he friendly?'."),
   dict(en="He's two years old.", pt="Ele tem dois anos.", ok=True, fb="Responde com a idade."),
   dict(en="Can my dog play with him?", pt="Meu cachorro pode brincar com ele?", ok=False, fb="Essa pergunta é do Jonah.")]),
  dict(npc="Is he friendly?", pt="Ele é amigável?", opts=[
   dict(en="He's two years old.", pt="Ele tem dois anos.", ok=False, fb="Você já disse a idade."),
   dict(en="Very! He loves to play.", pt="Muito! Ele adora brincar.", ok=True, fb="Responde e dá um motivo."),
   dict(en="Thank you! His name is Max.", pt="Obrigada! O nome dele é Max.", ok=False, fb="Você já disse o nome.")]),
  dict(npc="Can my dog play with him?", pt="Meu cachorro pode brincar com ele?", opts=[
   dict(en="Sure. What's your dog's name?", pt="Claro. Qual é o nome do seu cachorro?", ok=True, fb="Aceita e puxa conversa."),
   dict(en="How old is he?", pt="Quantos anos ele tem?", ok=False, fb="Essa pergunta é do Jonah."),
   dict(en="Hi! What a cute dog!", pt="Oi! Que cachorro fofo!", ok=False, fb="A conversa já começou.")]),
  dict(npc="Luna. She's shy.", pt="Luna. Ela é tímida.", opts=[
   dict(en="That's okay. Max is very kind.", pt="Tudo bem. O Max é muito gentil.", ok=True, fb="Tranquiliza o dono."),
   dict(en="He loves to play.", pt="Ele adora brincar.", ok=False, fb="Já foi dito, e o assunto agora é a Luna."),
   dict(en="Is he friendly?", pt="Ele é amigável?", ok=False, fb="Essa pergunta é do Jonah.")]),
 ]),
)
