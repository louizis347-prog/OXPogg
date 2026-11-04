X = dict(
 key=dict(big="Where is the salt?", label="Perguntar onde as coisas ficam", sub="Where is... para uma coisa, Where are... para várias; a resposta usa in, on ou under."),
 mini=[
  dict(who="Jonah", en="Can I help you in the {kitchen|garden|house}?", pt="Posso ajudar você na {cozinha|jardim|casa}?"),
  dict(who="You", en="Sure. Get a {plate|glass|bowl} from the cabinet.", pt="Claro. Pegue {um prato|um copo|uma tigela} no armário."),
  dict(who="Jonah", en="Where {are the forks|is the salt|are the spoons}?", pt="Onde {ficam os garfos|está o sal|ficam as colheres}?"),
  dict(who="You", en="It's {on the shelf|in the drawer|under the stove}.", pt="Está {na prateleira|na gaveta|embaixo do fogão}."),
 ],
 dlg=[
  dict(who="Jonah", en="Can I help you in the {kitchen|house}?", pt="Posso ajudar você na {cozinha|casa}?"),
  dict(who="You", en="Sure. Get a {plate|bowl|glass} from the cabinet.", pt="Claro. Pegue {um prato|uma tigela|um copo} no armário."),
  dict(who="Jonah", en="Where are the {forks|spoons|knives}?", pt="Onde ficam {os garfos|as colheres|as facas}?"),
  dict(who="You", en="In the {drawer|cabinet}, on the {left|right}.", pt="Na {gaveta|armário}, à {esquerda|direita}."),
  dict(who="Jonah", en="Do you have a {big|small} pan?", pt="Você tem uma panela {grande|pequena}?"),
  dict(who="You", en="Yes, it's {under|next to} the stove.", pt="Tenho, fica {embaixo do|ao lado do} fogão."),
  dict(who="Jonah", en="Thanks. Where is the {salt|sugar}?", pt="Valeu. Onde está o {sal|açúcar}?"),
  dict(who="You", en="It's on the {shelf|counter}.", pt="Está na {prateleira|bancada}."),
  dict(who="Jonah", en="Come back soon. Enjoy cooking!", pt="Volte logo. Bom cozinhar!"),
 ],
 vocab=[
  dict(w='jar', pt='pote', e='🫙', ex=['The jar is on the shelf.', 'This jar is empty.']),
  dict(w="microwave", pt="micro-ondas", e="📟", ex=["The microwave is on the counter.", "Use the microwave for the soup."]),
  dict(w="oven", pt="forno", e="♨️", ex=["The oven is hot.", "Put the bread in the oven."]),
  dict(w="sink", pt="pia", e="🚰", ex=["The glass is in the sink.", "Wash the pan in the sink."]),
  dict(w='stir', pt='mexer', e='🥄', ex=['Stir the soup.', 'I stir my tea.']),
  dict(w='freezer', pt='congelador', e='🧊', ex=['The ice is in the freezer.', 'The freezer is cold.']),
 ],
 molds=[
  dict(title="Perguntar onde fica", frame="Where is the {thing}?", slots=[dict(key="thing", opts=["salt", "pan", "kettle", "toaster"])], model="Where is the salt?", note="Where is... para uma coisa. Para várias: Where are the forks?"),
  dict(title="Dizer onde fica", frame="It's {place}.", slots=[dict(key="place", opts=["on the shelf", "in the drawer", "under the stove", "in the cabinet"])], model="It's on the shelf.", note="On = em cima, in = dentro, under = embaixo."),
  dict(title="Escrever sobre a cozinha", frame="In my kitchen, the {a} is {b}. The forks are {c}.", slots=[dict(key="a", opts=["pan", "kettle", "toaster"]), dict(key="b", opts=["on the stove", "on the counter", "under the sink"]), dict(key="c", opts=["in the drawer", "in the cabinet", "on the shelf"])], model="In my kitchen, the pan is on the stove. The forks are in the drawer.", note="Uma coisa: is. Várias coisas (forks): are. Depois diga onde ficam."),
 ],
 sounds=[
  dict(say="Where are the forks?", tag="redução: are", tip="Are fica fraco, quase 'er': whe-rer the FORKS."),
  dict(say="Can I help you?", tag="redução: can", tip="Can é fraco: kn-ai HELP you. Acentue HELP."),
  dict(say="It's on the shelf.", tag="redução: it's on", tip="It's on soa 'itson'. Acentue SHELF."),
 ],
 role=dict(turns=[
  dict(npc="Welcome! Make yourself at home.", opts=[
   dict(en="Thanks! Can I help you in the kitchen?", pt="Obrigado! Posso ajudar você na cozinha?", reply="Sure. Get a plate from the cabinet."),
   dict(en="Thank you. Your kitchen is cozy.", pt="Obrigado. Sua cozinha é aconchegante.", reply="Thanks! Can you get a plate from the cabinet?"),
   dict(en="Hi! Can I help you?", pt="Oi! Posso ajudar você?", reply="Sure. Get a plate from the cabinet.")]),
  dict(npc="Sure. Get a plate from the cabinet.", opts=[
   dict(en="Okay. Where are the forks?", pt="Certo. Onde ficam os garfos?", reply="In the drawer, on the left."),
   dict(en="Done. Where are the spoons?", pt="Pronto. Onde ficam as colheres?", reply="In the drawer, on the right."),
   dict(en="Got it. Where are the glasses?", pt="Entendi. Onde ficam os copos?", reply="In the cabinet, on the right.")]),
  dict(npc="Anything else you need?", opts=[
   dict(en="Do you have a big pan?", pt="Você tem uma panela grande?", reply="Yes, it's under the stove."),
   dict(en="Where is the kettle?", pt="Onde está a chaleira?", reply="It's on the stove."),
   dict(en="Where is the toaster?", pt="Onde está a torradeira?", reply="It's on the counter.")]),
  dict(npc="Here you go.", opts=[
   dict(en="Thanks. Where is the salt?", pt="Valeu. Onde está o sal?", reply="It's on the shelf. Enjoy cooking!"),
   dict(en="Thank you. Where is the sugar?", pt="Obrigado. Onde está o açúcar?", reply="It's on the shelf. Enjoy cooking!"),
   dict(en="Thanks! Can I use the sink?", pt="Valeu! Posso usar a pia?", reply="Sure! Enjoy cooking!")]),
 ], change=["Você não encontra o garfo na gaveta: pergunte onde mais pode estar.", "A panela grande está suja: peça uma pequena.", "Seu amigo diz que você pode relaxar: aceite e agradeça."]),
 writing=dict(task="Você ajuda um amigo na cozinha. Escreva 2 ou 3 frases: ofereça ajuda e pergunte onde fica uma coisa.", model="Can I help you in the kitchen? Where are the forks? Thanks, and where is the salt?", kw=["help", "kitchen", "where", "salt"], checks=["Ofereceu ajuda.", "Perguntou onde fica algo.", "Usou is ou are certo."]),
 scenes=dict(pool=["kitchen", "living", "home1", "chefkitchen"], npc=dict(g="f", role="friend"), you=dict(g="m")),
 convo=dict(npc=dict(name="Tara"), story="Você está na casa de uma amiga. Ela cozinha e você oferece ajuda.", turns=[
  dict(npc="Welcome! Make yourself at home.", pt="Bem-vindo! Fique à vontade.", opts=[
   dict(en="Thanks! Can I help you in the kitchen?", pt="Obrigado! Posso ajudar você na cozinha?", ok=True, fb="Agradece e oferece ajuda."),
   dict(en="It's on the shelf.", pt="Está na prateleira.", ok=False, fb="Ninguém perguntou onde algo fica."),
   dict(en="Come back soon.", pt="Volte logo.", ok=False, fb="Essa frase é de despedida.")]),
  dict(npc="Sure. Get a plate from the cabinet.", pt="Claro. Pegue um prato no armário.", opts=[
   dict(en="In the drawer, on the left.", pt="Na gaveta, à esquerda.", ok=False, fb="Quem responde onde fica é a anfitriã."),
   dict(en="Okay. Where are the forks?", pt="Certo. Onde ficam os garfos?", ok=True, fb="Pergunta onde ficam os próximos itens."),
   dict(en="Enjoy cooking!", pt="Bom cozinhar!", ok=False, fb="Ainda é cedo para esta frase.")]),
  dict(npc="In the drawer, on the left.", pt="Na gaveta, à esquerda.", opts=[
   dict(en="Do you have a big pan?", pt="Você tem uma panela grande?", ok=True, fb="Pede o próximo utensílio."),
   dict(en="Where are the forks?", pt="Onde ficam os garfos?", ok=False, fb="Ela acabou de responder isso."),
   dict(en="Yes, it's under the stove.", pt="Tenho, fica embaixo do fogão.", ok=False, fb="Quem responde é ela.")]),
  dict(npc="Yes, it's under the stove.", pt="Sim, fica embaixo do fogão.", opts=[
   dict(en="Thanks. Where is the salt?", pt="Valeu. Onde está o sal?", ok=True, fb="Agradece e pergunta o próximo item."),
   dict(en="Get a plate from the cabinet.", pt="Pegue um prato no armário.", ok=False, fb="Quem manda pegar o prato é ela."),
   dict(en="Can I help you?", pt="Posso ajudar?", ok=False, fb="Você já ofereceu ajuda.")]),
  dict(npc="It's on the shelf. Enjoy cooking!", pt="Está na prateleira. Bom cozinhar!", opts=[
   dict(en="Thank you. Your kitchen is cozy!", pt="Obrigado. Sua cozinha é aconchegante!", ok=True, fb="Agradece e elogia."),
   dict(en="Where is the salt?", pt="Onde está o sal?", ok=False, fb="Ela acabou de dizer."),
   dict(en="Do you have a big pan?", pt="Você tem uma panela grande?", ok=False, fb="Isso já foi respondido.")]),
 ]),
)
