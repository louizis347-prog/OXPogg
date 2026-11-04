X = dict(
 key=dict(big="It's a snow day!", label="Dia de neve em casa", sub="Fale da neve, confirme se a escola fechou e se prepare: casaco, botas e luvas antes de sair."),
 mini=[
  dict(who="Sabrina", en="Look outside! It snowed all {night.|morning.|day.}", pt="Olha lá fora! Nevou a {noite toda.|manhã toda.|dia todo.}"),
  dict(who="You", en="Wow! Is school {closed|open|cancelled} today?", pt="Nossa! A escola está {fechada|aberta|cancelada} hoje?"),
  dict(who="Sabrina", en="Yes, it's a snow day! Put on your {coat|hat|boots} first.", pt="Sim, é dia de neve! Primeiro ponha {o casaco|o gorro|as botas}."),
  dict(who="You", en="Where are my {gloves?|boots?|mittens?}", pt="Onde estão {minhas luvas?|minhas botas?|minhas mitenes?}"),
 ],
 dlg=[
  dict(who="Sabrina", en="Look outside! It snowed all {night.|day.}", pt="Olha lá fora! Nevou {a noite toda.|o dia todo.}"),
  dict(who="You", en="Wow! How much {snow|ice} is there?", pt="Nossa! Quanta {neve|gelo} tem?"),
  dict(who="Sabrina", en="About {ten|twelve} inches.", pt="Uns {vinte e cinco|trinta} centímetros."),
  dict(who="You", en="Is school {closed|open} today?", pt="A escola está {fechada|aberta} hoje?"),
  dict(who="Sabrina", en="Yes, it's a {snow day!|cold day!}", pt="Sim, é um {dia de neve!|dia frio!}"),
  dict(who="You", en="Great! Let's build a {snowman.|sled.}", pt="Ótimo! Vamos fazer um {boneco de neve.|trenó.}"),
  dict(who="Sabrina", en="First, put on your {coat|hat} and boots.", pt="Primeiro, ponha {casaco|gorro} e botas."),
  dict(who="You", en="Where are my {gloves?|boots?}", pt="Onde estão {minhas luvas?|minhas botas?}"),
  dict(who="Sabrina", en="They're by the {door.|window.}", pt="Estão perto da {porta.|janela.}"),
 ],
 vocab=[
  dict(w="snowman", pt="boneco de neve", e="⛄", ex=["We build a snowman.", "The snowman has a hat."]),
  dict(w="sled", pt="trenó", e="🛷", ex=["I ride the sled.", "The sled is red."]),
  dict(w="coat", pt="casaco", e="🧥", ex=["Put on your coat.", "My coat is warm."]),
  dict(w="freezing", pt="congelando, gelado", e="🥶", ex=["It's freezing outside.", "My hands are freezing."]),
  dict(w="icy", pt="com gelo, gelado", e="🧊", ex=["The road is icy.", "Be careful, it's icy."]),
  dict(w="cozy", pt="aconchegante", e="🛋️", ex=["The house is cozy.", "I like a cozy room."]),
 ],
 molds=[
  dict(title="Perguntar sobre a escola", frame="Is school {state} {time}?", slots=[dict(key="state", opts=["closed", "open", "cancelled"]), dict(key="time", opts=["today", "tomorrow", "on Monday"])], model="Is school closed today?", note="Is school + closed/open + quando. Pergunta de sim ou não."),
  dict(title="Perguntar onde estão as roupas", frame="Where are my {thing}?", slots=[dict(key="thing", opts=["gloves", "boots", "socks", "hats"])], model="Where are my gloves?", note="Coisas no plural pedem are: Where are my…?"),
  dict(title="Escrever o que vai vestir", frame="It's {weather}. I put on my {thing1} and my {thing2}.", slots=[dict(key="weather", opts=["freezing", "icy", "very cold"]), dict(key="thing1", opts=["coat", "hat", "boots"]), dict(key="thing2", opts=["gloves", "scarf", "boots"])], model="It's freezing. I put on my coat and my gloves.", note="Put on é vestir. My + roupa. Pode usar freezing para muito frio."),
 ],
 sounds=[
  dict(say="They're by the door.", tag="o th de they: com voz", tip="Língua entre os dentes e a garganta vibra. Não diga 'dei'."),
  dict(say="It snowed all night.", tag="-ed: snowed = /d/", tip="Depois de som com voz, o -ed soa /d/ e não vira sílaba: 'snowd'."),
  dict(say="Let's build a snowman.", tag="ritmo: LET'S BUILD a SNOWman", tip="Acentue LET'S, BUILD e SNOW. O a fica fraquinho."),
 ],
 role=dict(turns=[
  dict(npc="Look outside! It snowed all night.", opts=[
   dict(en="Wow! How much snow is there?", pt="Nossa! Quanta neve tem?", reply="About ten inches."),
   dict(en="Wow! It's so white!", pt="Nossa! Está tão branco!", reply="Yes! About ten inches."),
   dict(en="Wow! Is it cold?", pt="Nossa! Está frio?", reply="Yes, it's freezing. About ten inches of snow.")]),
  dict(npc="About ten inches.", opts=[
   dict(en="Is school closed today?", pt="A escola está fechada hoje?", reply="Yes, it's a snow day!"),
   dict(en="Are the roads icy?", pt="As ruas estão com gelo?", reply="Yes, a little. And school is closed. It's a snow day!"),
   dict(en="Is school open?", pt="A escola está aberta?", reply="No, it's a snow day!")]),
  dict(npc="It's a snow day!", opts=[
   dict(en="Great! Let's build a snowman.", pt="Ótimo! Vamos fazer um boneco de neve.", reply="First, put on your coat and boots."),
   dict(en="Great! Let's use the sled.", pt="Ótimo! Vamos usar o trenó.", reply="First, put on your coat and boots."),
   dict(en="Great! Let's make hot tea.", pt="Ótimo! Vamos fazer chá quente.", reply="Good idea. But first, coat and boots.")]),
  dict(npc="Put on your coat and boots.", opts=[
   dict(en="Where are my gloves?", pt="Onde estão minhas luvas?", reply="They're by the door."),
   dict(en="Where is my hat?", pt="Onde está meu gorro?", reply="It's by the door."),
   dict(en="Where are my boots?", pt="Onde estão minhas botas?", reply="They're by the door.")]),
 ], change=["As luvas estão molhadas: peça um par seco.", "Seu irmão não quer sair porque está frio: convença com um chocolate quente.", "A rua está com gelo: avise para andar com cuidado."]),
 writing=dict(task="Escreva 2 ou 3 frases sobre um dia de neve: diga que a escola está fechada, o que você veste e o que vai fazer.", model="It's a snow day! School is closed. I put on my coat and boots, and I build a snowman.", kw=["snow", "closed", "coat", "snowman"], checks=["Disse que é dia de neve.", "Disse o que veste.", "Disse o que vai fazer."]),
 scenes=dict(pool=["snow", "home1", "living", "kitchen"], npc=dict(g="f", role="mom"), you=dict(g="m")),
 convo=dict(npc=dict(name="Sabrina"), story="Você acorda e vê muita neve. A Sabrina está em casa com você e fala do dia de neve.", turns=[
  dict(npc="Look outside! It snowed all night.", pt="Olha lá fora! Nevou a noite toda.", opts=[
   dict(en="Wow! How much snow is there?", pt="Nossa! Quanta neve tem?", ok=True, fb="Reage e pergunta a quantidade."),
   dict(en="About ten inches.", pt="Uns vinte e cinco centímetros.", ok=False, fb="Quem responde isso é a Sabrina."),
   dict(en="They're by the door.", pt="Estão perto da porta.", ok=False, fb="Ninguém perguntou das luvas.")]),
  dict(npc="About ten inches.", pt="Uns vinte e cinco centímetros.", opts=[
   dict(en="Yes, it's a snow day!", pt="Sim, é dia de neve!", ok=False, fb="Quem diz isso é a Sabrina."),
   dict(en="Is school closed today?", pt="A escola está fechada hoje?", ok=True, fb="Pergunta natural depois de muita neve."),
   dict(en="Where are my gloves?", pt="Onde estão minhas luvas?", ok=False, fb="Ainda é cedo para essa pergunta.")]),
  dict(npc="Yes, it's a snow day!", pt="Sim, é dia de neve!", opts=[
   dict(en="Is school closed today?", pt="A escola está fechada hoje?", ok=False, fb="Você já perguntou, e ela respondeu."),
   dict(en="First, put on your coat and boots.", pt="Primeiro, ponha casaco e botas.", ok=False, fb="Quem diz isso é a Sabrina."),
   dict(en="Great! Let's build a snowman.", pt="Ótimo! Vamos fazer um boneco de neve.", ok=True, fb="Sugere uma brincadeira.")]),
  dict(npc="First, put on your coat and boots.", pt="Primeiro, ponha casaco e botas.", opts=[
   dict(en="Where are my gloves?", pt="Onde estão minhas luvas?", ok=True, fb="Pergunta o que falta."),
   dict(en="How much snow is there?", pt="Quanta neve tem?", ok=False, fb="Você já perguntou isso."),
   dict(en="Great! Let's build a snowman.", pt="Ótimo! Vamos fazer um boneco de neve.", ok=False, fb="Você já disse isso.")]),
  dict(npc="They're by the door.", pt="Estão perto da porta.", opts=[
   dict(en="Where are my gloves?", pt="Onde estão minhas luvas?", ok=False, fb="Ela acabou de responder."),
   dict(en="Is school closed today?", pt="A escola está fechada hoje?", ok=False, fb="Já foi respondido."),
   dict(en="Thanks! I'm ready.", pt="Valeu! Estou pronto.", ok=True, fb="Agradece e fecha a conversa.")]),
 ]),
)
