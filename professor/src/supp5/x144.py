X = dict(
 key=dict(big="Where are the dinosaurs?", label="Visitar um museu", sub="Peça a entrada, confira se é de graça, pegue o mapa, pergunte onde fica uma sala e se pode fotografar."),
 mini=[
  dict(who="Ethan", en="Welcome to the {museum|gallery|exhibit}! How many?", pt="Bem-vindos ao {museu|salão|espaço de exposição}! Quantos?"),
  dict(who="You", en="{Two|Three|Four} adults, please.", pt="{Dois|Três|Quatro} adultos, por favor."),
  dict(who="Ethan", en="It's {free|ten dollars|open} today.", pt="Hoje é {de graça|dez dólares|aberto}."),
  dict(who="You", en="Where are the {dinosaurs?|paintings?|statues?}", pt="Onde ficam {os dinossauros?|os quadros?|as estátuas?}"),
 ],
 dlg=[
  dict(who="Ethan", en="Welcome to the {museum!|gallery!} How many?", pt="Bem-vindos ao {museu!|salão!} Quantos?"),
  dict(who="You", en="{Two|Three} adults, please.", pt="{Dois|Três} adultos, por favor."),
  dict(who="Ethan", en="It's {free|open} today.", pt="Hoje é {de graça.|aberto.}"),
  dict(who="You", en="Really? That's {great!|nice!}", pt="Sério? Que {ótimo!|legal!}"),
  dict(who="Ethan", en="Here's a {map.|guide.}", pt="Aqui está um {mapa.|guia.}"),
  dict(who="You", en="Where are the {dinosaurs?|paintings?}", pt="Onde ficam {os dinossauros?|os quadros?}"),
  dict(who="Ethan", en="On the first {floor,|level,} to the left.", pt="No primeiro {andar,|nível,} à esquerda."),
  dict(who="You", en="Can we take {photos?|pictures?}", pt="Podemos tirar {fotos?|fotos?}"),
  dict(who="Ethan", en="Yes, but no {flash.|video.}", pt="Sim, mas sem {flash.|vídeo.}"),
 ],
 vocab=[
  dict(w="dinosaur", pt="dinossauro", e="🦖", ex=["The dinosaur is huge.", "Leo loves dinosaurs."]),
  dict(w="giant", pt="gigante", e="🦣", ex=["The dinosaur is giant.", "I see a giant bone."]),
  dict(w="admission", pt="entrada (preço)", e="🎟️", ex=["Admission is free today.", "How much is admission?"]),
  dict(w="guard", pt="segurança", e="💂", ex=["Ask the guard, please.", "The guard is at the door."]),
  dict(w="gallery", pt="sala de exposição", e="🖼️", ex=["The gallery is on the second floor.", "This gallery is quiet."]),
  dict(w="animal", pt="animal", e="🐾", ex=["I like animals.", "This animal is big."]),
 ],
 molds=[
  dict(title="Pedir a entrada", frame="{n} adults, please.", slots=[dict(key="n", opts=["Two", "Three", "Four"])], model="Two adults, please.", note="Depois do número, use o plural: adults."),
  dict(title="Perguntar onde fica", frame="Where are the {thing}? On the {floor} floor, to the {side}.", slots=[dict(key="thing", opts=["dinosaurs", "paintings", "statues"]), dict(key="floor", opts=["first", "second", "third"]), dict(key="side", opts=["left", "right", "back"])], model="Where are the dinosaurs? On the first floor, to the left.", note="Plural pede are. Floor é andar."),
  dict(title="Escrever a visita", frame="Hi. {n} adults, please. Where are the {thing}? Can we take photos?", slots=[dict(key="n", opts=["Two", "Three", "Four"]), dict(key="thing", opts=["dinosaurs", "paintings", "bones"])], model="Hi. Two adults, please. Where are the dinosaurs? Can we take photos?", note="Can we take photos? é a pergunta comum em museus."),
 ],
 sounds=[
  dict(say="Where are the dinosaurs?", tag="acento: DI-no-saurs", tip="Acentue a primeira sílaba: DAI-no-sors. O 'saurs' final é curto."),
  dict(say="Yes, but no flash.", tag="acento: NO FLASH", tip="Acentue NO e FLASH. 'But' fica fraco e rápido."),
  dict(say="It's free today.", tag="acento: FREE to-DAY", tip="Acentue FREE e a última sílaba de 'today': 'tu-DEI'."),
 ],
 role=dict(turns=[
  dict(npc="Welcome to the museum! How many?", opts=[
   dict(en="Two adults, please.", pt="Dois adultos, por favor.", reply="It's free today."),
   dict(en="Two adults and one child, please.", pt="Dois adultos e uma criança, por favor.", reply="It's free today. Kids too."),
   dict(en="Just one adult, please.", pt="Só um adulto, por favor.", reply="It's free today.")]),
  dict(npc="It's free today.", opts=[
   dict(en="Really? That's great!", pt="Sério? Que ótimo!", reply="Here's a map."),
   dict(en="Wow, thank you!", pt="Uau, obrigado!", reply="You're welcome. Here's a map."),
   dict(en="Is it free every day?", pt="É de graça todo dia?", reply="Yes, it is. Here's a map.")]),
  dict(npc="Here's a map.", opts=[
   dict(en="Where are the dinosaurs?", pt="Onde ficam os dinossauros?", reply="On the first floor, to the left."),
   dict(en="Where are the paintings?", pt="Onde ficam os quadros?", reply="On the second floor, to the right."),
   dict(en="Where is the cafe?", pt="Onde fica o café?", reply="On the second floor, next to the stairs.")]),
  dict(npc="Anything else?", opts=[
   dict(en="Can we take photos?", pt="Podemos tirar fotos?", reply="Yes, but no flash."),
   dict(en="Can we touch the bones?", pt="Podemos tocar nos ossos?", reply="Sorry, please don't touch."),
   dict(en="Is there a gift shop?", pt="Tem loja de lembranças?", reply="Yes, on the first floor, to the right.")]),
 ], change=["Os dinossauros estão fechados hoje: peça outra sala para visitar.", "Você quer usar flash: pergunte se pode.", "Um amigo quer tirar uma foto sua: peça ajuda ao segurança."]),
 writing=dict(task="Você chega a um museu em Washington. Escreva 2 ou 3 frases: peça a entrada, pergunte onde ficam os dinossauros e se pode fotografar.", model="Hi. Two adults, please. Where are the dinosaurs? Can we take photos? Thank you very much.", kw=["adults", "where", "dinosaurs", "photos"], checks=["Pediu a entrada.", "Perguntou onde fica uma sala.", "Perguntou sobre fotos."]),
 scenes=dict(pool=["museum", "artroom", "lobby", "hall", "street"], npc=dict(g="m", role="staff"), you=dict(g="f")),
 convo=dict(npc=dict(name="Ethan"), story="Você chega a um museu em Washington. Ethan trabalha na entrada.", turns=[
  dict(npc="Welcome to the museum! How many?", pt="Bem-vindos ao museu! Quantos?", opts=[
   dict(en="Here's a map.", pt="Aqui está um mapa.", ok=False, fb="Quem entrega o mapa é ele."),
   dict(en="Two adults, please.", pt="Dois adultos, por favor.", ok=True, fb="Responde quantas pessoas são."),
   dict(en="Yes, but no flash.", pt="Sim, mas sem flash.", ok=False, fb="Não responde à pergunta.")]),
  dict(npc="It's free today.", pt="Hoje é de graça.", opts=[
   dict(en="Really? That's great!", pt="Sério? Que ótimo!", ok=True, fb="Reage à boa notícia."),
   dict(en="On the first floor, to the left.", pt="No primeiro andar, à esquerda.", ok=False, fb="Ninguém perguntou onde fica algo."),
   dict(en="Two adults, please.", pt="Dois adultos, por favor.", ok=False, fb="Você já disse isso.")]),
  dict(npc="Here's a map.", pt="Aqui está um mapa.", opts=[
   dict(en="Where are the dinosaurs?", pt="Onde ficam os dinossauros?", ok=True, fb="Pede uma localização."),
   dict(en="It's free today.", pt="Hoje é de graça.", ok=False, fb="Quem informa isso é ele."),
   dict(en="Yes, but no flash.", pt="Sim, mas sem flash.", ok=False, fb="Ninguém perguntou sobre fotos ainda.")]),
  dict(npc="On the first floor, to the left.", pt="No primeiro andar, à esquerda.", opts=[
   dict(en="Welcome to the museum!", pt="Bem-vindo ao museu!", ok=False, fb="Esse é o cumprimento dele."),
   dict(en="Two adults, please.", pt="Dois adultos, por favor.", ok=False, fb="Você já comprou a entrada."),
   dict(en="Can we take photos?", pt="Podemos tirar fotos?", ok=True, fb="Pergunta útil em um museu.")]),
  dict(npc="Yes, but no flash.", pt="Sim, mas sem flash.", opts=[
   dict(en="Really? That's great!", pt="Sério? Que ótimo!", ok=False, fb="Não é uma notícia surpreendente."),
   dict(en="Where are the dinosaurs?", pt="Onde ficam os dinossauros?", ok=False, fb="Você já perguntou."),
   dict(en="No flash, no problem. Thanks!", pt="Sem flash, sem problema. Obrigado!", ok=True, fb="Aceita a regra com educação.")]),
 ]),
)
