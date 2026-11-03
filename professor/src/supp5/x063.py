X = dict(
 key=dict(big="Is there a kitchen?", label="Conhecer um apartamento", sub="Em uma visita, pergunte se há cada cômodo e onde fica, com Is there...? e next to."),
 mini=[
  dict(who="Kai", en="Welcome! Let me show you the {apartment|house|room}.", pt="Bem-vindo! Deixe-me mostrar {o apartamento|a casa|o quarto}."),
  dict(who="You", en="Thanks. It looks {nice|big|bright}.", pt="Valeu. Parece {bonito|grande|claro}."),
  dict(who="Kai", en="This is the {living room|kitchen|bedroom}. It has a big window.", pt="Esta é {a sala|a cozinha|o quarto}. Tem uma janela grande."),
  dict(who="You", en="I like it. Is there a {kitchen|balcony|closet}?", pt="Gostei. Tem {cozinha|varanda|armário}?"),
 ],
 dlg=[
  dict(who="Kai", en="Welcome! Let me show you the {apartment.|place.}", pt="Bem-vindo! Deixe-me mostrar {o apartamento.|o lugar.}"),
  dict(who="You", en="Thanks. It looks {nice.|big.}", pt="Valeu. Parece {bonito.|grande.}"),
  dict(who="Kai", en="This is the {living room.|bedroom.} It has a big {window.|balcony.}", pt="Esta é {a sala.|o quarto.} Tem {uma janela grande.|uma varanda grande.}"),
  dict(who="You", en="I like it. Is there a {kitchen?|closet?}", pt="Gostei. Tem {cozinha?|armário?}"),
  dict(who="Kai", en="Yes, it's here. It has a new {stove.|fridge.}", pt="Tem, é aqui. Tem {um fogão novo.|uma geladeira nova.}"),
  dict(who="You", en="And the {bedroom?|bathroom?}", pt="E {o quarto?|o banheiro?}"),
  dict(who="Kai", en="It's down the hall, next to the {bathroom.|kitchen.}", pt="Fica no corredor, ao lado {do banheiro.|da cozinha.}"),
  dict(who="You", en="Perfect. How many {rooms|bedrooms} are there?", pt="Perfeito. Quantos {cômodos|quartos} tem?"),
  dict(who="Kai", en="Come back anytime. It's {yours!|ready!}", pt="Volte quando quiser. É {seu!|seu!}"),
 ],
 vocab=[
  dict(w="kitchen", pt="cozinha", e="🍳", ex=["The kitchen is small.", "Is there a kitchen?"]),
  dict(w="bedroom", pt="quarto", e="🛏️", ex=["The bedroom is quiet.", "I have one bedroom."]),
  dict(w="fridge", pt="geladeira", e="🧊", ex=["The fridge is new.", "The milk is in the fridge."]),
  dict(w="balcony", pt="varanda", e="🌇", ex=["The balcony is nice.", "There is a balcony."]),
  dict(w="stove", pt="fogão", e="🔥", ex=["The stove is new.", "I cook on the stove."]),
  dict(w="closet", pt="armário embutido", e="🚪", ex=["The closet is big.", "My shoes are in the closet."]),
 ],
 molds=[
  dict(title="Perguntar se existe", frame="Is there a {room}?", slots=[dict(key="room", opts=["kitchen", "balcony", "closet", "bedroom"])], model="Is there a kitchen?", note="Is there a...? pergunta se algo existe no lugar."),
  dict(title="Descrever o cômodo", frame="This is the {room}. It has a {thing}.", slots=[dict(key="room", opts=["kitchen", "bedroom", "bathroom"]), dict(key="thing", opts=["big window", "small window", "new door"])], model="This is the kitchen. It has a big window.", note="It has a... descreve o que o cômodo tem."),
  dict(title="Escrever sobre o apartamento", frame="The {room} is {where}.", slots=[dict(key="room", opts=["bedroom", "kitchen", "bathroom"]), dict(key="where", opts=["next to the hall", "down the hall", "next to the kitchen"])], model="The bedroom is next to the hall.", note="Next to = ao lado de. Down the hall = no corredor."),
 ],
 sounds=[
  dict(say="It looks nice.", tag="ritmo: it LOOKS NICE", tip="Acentue LOOKS e NICE; it fica curto e fraco."),
  dict(say="Is there a kitchen?", tag="ligação: is there a", tip="Is there a soa 'izdera'. Acentue KIT-chen."),
  dict(say="Next to the bathroom.", tag="ligação: next to", tip="Next to soa 'nekstu'. Una e acentue BATH."),
 ],
 role=dict(turns=[
  dict(npc="Welcome! Let me show you the apartment.", opts=[
   dict(en="Thanks. It looks nice.", pt="Valeu. Parece bonito.", reply="This is the living room. It has a big window."),
   dict(en="Thank you. It looks big.", pt="Obrigado. Parece grande.", reply="This is the living room. It has a big window."),
   dict(en="Thanks! I'm excited.", pt="Obrigado! Estou animado.", reply="Great! This is the living room. It has a big window.")]),
  dict(npc="This is the living room. It has a big window.", opts=[
   dict(en="I like it. Is there a kitchen?", pt="Gostei. Tem cozinha?", reply="Yes, it's here. It has a new stove."),
   dict(en="Nice. Is there a balcony?", pt="Bonito. Tem varanda?", reply="Yes, it's small, but it's nice."),
   dict(en="I love the window. Where's the kitchen?", pt="Adoro a janela. Onde fica a cozinha?", reply="It's here. It has a new stove.")]),
  dict(npc="Do you want to see the bedroom?", opts=[
   dict(en="Yes. And the bedroom?", pt="Sim. E o quarto?", reply="It's down the hall, next to the bathroom."),
   dict(en="Yes, where is it?", pt="Sim, onde fica?", reply="It's down the hall, next to the bathroom."),
   dict(en="Sure. And the bathroom?", pt="Claro. E o banheiro?", reply="It's down the hall, next to the bedroom.")]),
  dict(npc="That's all. Any questions?", opts=[
   dict(en="Perfect. How many rooms are there?", pt="Perfeito. Quantos cômodos tem?", reply="Four rooms. Come back anytime. It's yours!"),
   dict(en="Great. How many bedrooms are there?", pt="Ótimo. Quantos quartos tem?", reply="Two bedrooms. Come back anytime!"),
   dict(en="No, thanks. I love it!", pt="Não, obrigado. Adorei!", reply="Great! Come back anytime. It's yours!")]),
 ], change=["O apartamento não tem varanda: pergunte se há outra área aberta.", "O quarto é muito pequeno: diga isso com educação e pergunte por outro.", "Você quer ver o prédio de novo: combine um horário."]),
 writing=dict(task="Você visitou um apartamento. Escreva 2 ou 3 frases para um amigo: diga como é a sala, a cozinha e o quarto.", model="The apartment is nice. The living room has a big window. The kitchen has a new stove, and the bedroom is next to the bathroom.", kw=["apartment", "kitchen", "bedroom", "window"], checks=["Falou da sala ou da janela.", "Falou da cozinha.", "Falou do quarto."]),
 scenes=dict(pool=["living", "kitchen", "bedroom", "hall", "home1"], npc=dict(g="m", role="agent"), you=dict(g="f")),
 convo=dict(npc=dict(name="Kai"), story="Você visita um apartamento para alugar. Kai mostra cada cômodo.", turns=[
  dict(npc="Welcome! Let me show you the apartment.", pt="Bem-vindo! Deixe-me mostrar o apartamento.", opts=[
   dict(en="Thanks. It looks nice.", pt="Valeu. Parece bonito.", ok=True, fb="Agradece e elogia."),
   dict(en="Come back anytime.", pt="Volte quando quiser.", ok=False, fb="É a fala de despedida do Kai."),
   dict(en="Yes, it's here.", pt="Tem, é aqui.", ok=False, fb="Você ainda não perguntou nada.")]),
  dict(npc="This is the living room. It has a big window.", pt="Esta é a sala. Tem uma janela grande.", opts=[
   dict(en="It has a new stove.", pt="Tem um fogão novo.", ok=False, fb="Essa é uma fala de Kai sobre a cozinha."),
   dict(en="I like it. Is there a kitchen?", pt="Gostei. Tem cozinha?", ok=True, fb="Elogia e pergunta pelo próximo cômodo."),
   dict(en="Welcome! Let me show you.", pt="Bem-vindo! Deixe-me mostrar.", ok=False, fb="Quem mostra é Kai.")]),
  dict(npc="Yes, it's here. It has a new stove.", pt="Tem, é aqui. Tem um fogão novo.", opts=[
   dict(en="And the bedroom?", pt="E o quarto?", ok=True, fb="Pede para ver o próximo cômodo."),
   dict(en="It's down the hall.", pt="Fica no corredor.", ok=False, fb="Quem informa o lugar é Kai."),
   dict(en="Is there a kitchen?", pt="Tem cozinha?", ok=False, fb="Você acabou de ver a cozinha.")]),
  dict(npc="It's down the hall, next to the bathroom.", pt="Fica no corredor, ao lado do banheiro.", opts=[
   dict(en="Perfect. How many rooms are there?", pt="Perfeito. Quantos cômodos tem?", ok=True, fb="Boa pergunta para fechar a visita."),
   dict(en="Is there a balcony?", pt="Tem varanda?", ok=False, fb="Plausível, mas não encaixa agora; ele só falou do quarto."),
   dict(en="Let me show you the apartment.", pt="Deixe-me mostrar o apartamento.", ok=False, fb="Quem mostra é Kai.")]),
  dict(npc="Come back anytime. It's yours!", pt="Volte quando quiser. É seu!", opts=[
   dict(en="Thanks! I want it.", pt="Valeu! Eu quero.", ok=True, fb="Responde com alegria."),
   dict(en="It looks nice.", pt="Parece bonito.", ok=False, fb="Já foi dito no início."),
   dict(en="And the bedroom?", pt="E o quarto?", ok=False, fb="Você já viu o quarto.")]),
 ]),
)
