X = dict(
 key=dict(big="It's for my best friend", label="Presente para alguém", sub="Diga para quem é o presente e do que a pessoa gosta; o atendente sugere ideias e pergunta o orçamento."),
 mini=[
  dict(who="You", en="Hi! I need a {birthday|wedding|thank-you} gift.", pt="Oi! Preciso de um presente de {aniversário|casamento|agradecimento}."),
  dict(who="Leo", en="Who is it for?", pt="Para quem é?"),
  dict(who="You", en="It's for my {best friend.|sister.|teacher.} She loves {books|tea|music}.", pt="É para {minha melhor amiga.|minha irmã.|minha professora.} Ela adora {livros|chá|música}."),
  dict(who="Leo", en="How about a {mug?|puzzle?|bookmark?} It's only {six|eight|two} dollars.", pt="Que tal {uma caneca?|um quebra-cabeça?|um marcador?} Custa só {seis|oito|dois} dólares."),
 ],
 dlg=[
  dict(who="Leo", en="Hi! Can I help you find {something?|a gift?}", pt="Oi! Posso ajudar a achar {algo?|um presente?}"),
  dict(who="You", en="Yes, I need a {birthday|special} gift.", pt="Sim, preciso de um presente de {aniversário|especial}."),
  dict(who="Leo", en="Who is it {for?|from?}", pt="Para quem {é?|é?}"),
  dict(who="You", en="It's for my {best friend.|sister.}", pt="É para {minha melhor amiga.|minha irmã.}"),
  dict(who="Leo", en="What does she {like?|love?}", pt="Do que ela {gosta?|adora?}"),
  dict(who="You", en="She loves {books|puzzles} and tea.", pt="Ela adora {livros|quebra-cabeças} e chá."),
  dict(who="Leo", en="How about a {book|bookmark} and a mug?", pt="Que tal {um livro|um marcador} e uma caneca?"),
  dict(who="You", en="That's a {great|good} idea.", pt="É uma {ótima|boa} ideia."),
  dict(who="Leo", en="What's your {budget?|price?}", pt="Qual é seu {orçamento?|limite?}"),
 ],
 vocab=[
  dict(w="bookmark", pt="marcador de página", e="🔖", ex=["I put a bookmark in my book.", "The bookmark is blue."]),
  dict(w="puzzle", pt="quebra-cabeça", e="🧩", ex=["She likes puzzles.", "This puzzle has a hundred pieces."]),
  dict(w="buy", pt="comprar", e="🛍️", ex=["I want to buy a gift.", "Where can I buy it?"]),
  dict(w="special", pt="especial", e="⭐", ex=["It is a special day.", "I want something special."]),
  dict(w="budget", pt="orçamento", e="💰", ex=["My budget is twenty dollars.", "What's your budget?"]),
  dict(w="present", pt="presente", e="🎁", ex=["This present is for Tia.", "I have a present for you."]),
 ],
 molds=[
  dict(title="Dizer para quem é", frame="It's for my {person}.", slots=[dict(key="person", opts=["best friend", "sister", "teacher", "brother"])], model="It's for my best friend.", note="It's for + my + pessoa. Use for para quem recebe o presente."),
  dict(title="Dizer do que a pessoa gosta", frame="She {verb} {thing}.", slots=[dict(key="verb", opts=["loves", "likes", "enjoys"]), dict(key="thing", opts=["books", "tea", "music"])], model="She loves books.", note="Com she, o verbo leva -s: loves, likes. Sem -ing em verbos de gosto."),
  dict(title="Escrever o que quer comprar", frame="I need a {item} for my {person}. My budget is {price} dollars.", slots=[dict(key="item", opts=["book", "mug", "puzzle"]), dict(key="person", opts=["friend", "sister", "teacher"]), dict(key="price", opts=["ten", "twenty", "thirty"])], model="I need a book for my friend. My budget is ten dollars.", note="Need + a + coisa. Diga o orçamento com My budget is…"),
 ],
 sounds=[
  dict(say="She loves books and mugs.", tag="o -s final: /s/ e /z/", tip="Depois de k o -s é surdo: books. Depois de g vibra: mugs. Não ponha um 'i' no final."),
  dict(say="How about a book?", tag="ligação: how about", tip="Una how e about sem pausa: 'haw-a-BOUT'. O acento fica em BOOK."),
  dict(say="What's your budget?", tag="acento: BUDget", tip="Budget tem acento no começo: BUD-jet. O g soa como j."),
 ],
 role=dict(turns=[
  dict(npc="Hi! Can I help you find something?", opts=[
   dict(en="Yes, I need a birthday gift.", pt="Sim, preciso de um presente de aniversário.", reply="Sure. Who is it for?"),
   dict(en="Yes, I need a gift for a friend.", pt="Sim, preciso de um presente para uma amiga.", reply="Sure. Who is it for?"),
   dict(en="Yes, I want something special.", pt="Sim, quero algo especial.", reply="Of course. Who is it for?")]),
  dict(npc="Who is it for?", opts=[
   dict(en="It's for my best friend.", pt="É para minha melhor amiga.", reply="Nice! What does she like?"),
   dict(en="It's for my sister.", pt="É para minha irmã.", reply="Nice! What does she like?"),
   dict(en="It's for my teacher.", pt="É para minha professora.", reply="Nice! What does she like?")]),
  dict(npc="What does she like?", opts=[
   dict(en="She loves books and tea.", pt="Ela adora livros e chá.", reply="How about a book and a mug?"),
   dict(en="She likes puzzles.", pt="Ela gosta de quebra-cabeças.", reply="How about a puzzle and a card?"),
   dict(en="She loves music.", pt="Ela adora música.", reply="How about a music book and a bookmark?")]),
  dict(npc="How about a book and a mug?", opts=[
   dict(en="That's a great idea.", pt="Ótima ideia.", reply="What's your budget?"),
   dict(en="That sounds good.", pt="Parece bom.", reply="What's your budget?"),
   dict(en="Great! I'll take it.", pt="Ótimo! Vou levar.", reply="Perfect. What's your budget?")]),
 ], change=["O livro custa mais que seu orçamento: peça algo mais barato.", "Você quer embrulho: pergunte se há gift wrap.", "O atendente pergunta se é para uma criança: diga a idade."]),
 writing=dict(task="Escreva 2 ou 3 frases: diga que precisa de um presente, para quem é e do que a pessoa gosta.", model="Hi! I need a gift for my best friend. She loves books and tea. My budget is twenty dollars.", kw=["gift", "friend", "loves", "budget"], checks=["Disse que precisa de um presente.", "Disse para quem é.", "Disse do que a pessoa gosta ou o orçamento."]),
 scenes=dict(pool=["shop", "bookshop", "market", "counter"], npc=dict(g="m", role="clerk"), you=dict(g="f")),
 convo=dict(npc=dict(name="Leo"), story="Você está em uma lojinha de presentes. O Leo trabalha lá e ajuda você a escolher um presente de aniversário.", turns=[
  dict(npc="Hi! Can I help you find something?", pt="Oi! Posso ajudar a achar algo?", opts=[
   dict(en="Who is it for?", pt="Para quem é?", ok=False, fb="Quem pergunta isso é o atendente."),
   dict(en="Yes, I need a birthday gift.", pt="Sim, preciso de um presente de aniversário.", ok=True, fb="Diz o que você procura."),
   dict(en="What's your budget?", pt="Qual é seu orçamento?", ok=False, fb="Essa pergunta é do atendente.")]),
  dict(npc="Who is it for?", pt="Para quem é?", opts=[
   dict(en="It's for my best friend.", pt="É para minha melhor amiga.", ok=True, fb="Responde a pergunta."),
   dict(en="She loves books and tea.", pt="Ela adora livros e chá.", ok=False, fb="Primeiro diga quem é a pessoa."),
   dict(en="How about a mug?", pt="Que tal uma caneca?", ok=False, fb="Essa é a sugestão do atendente.")]),
  dict(npc="What does she like?", pt="Do que ela gosta?", opts=[
   dict(en="That's a great idea.", pt="Ótima ideia.", ok=False, fb="Ainda não há ideia para aceitar."),
   dict(en="It's for my best friend.", pt="É para minha melhor amiga.", ok=False, fb="Você já disse isso."),
   dict(en="She loves books and tea.", pt="Ela adora livros e chá.", ok=True, fb="Diz o gosto dela.")]),
  dict(npc="How about a book and a mug?", pt="Que tal um livro e uma caneca?", opts=[
   dict(en="Yes, I need a birthday gift.", pt="Sim, preciso de um presente de aniversário.", ok=False, fb="Você já disse isso no começo."),
   dict(en="What does she like?", pt="Do que ela gosta?", ok=False, fb="Quem pergunta isso é o atendente."),
   dict(en="That's a great idea.", pt="Ótima ideia.", ok=True, fb="Aceita a sugestão com simpatia.")]),
  dict(npc="What's your budget?", pt="Qual é seu orçamento?", opts=[
   dict(en="About twenty dollars.", pt="Uns vinte dólares.", ok=True, fb="Responde com um valor."),
   dict(en="She loves books and tea.", pt="Ela adora livros e chá.", ok=False, fb="Não responde ao orçamento."),
   dict(en="How about a book?", pt="Que tal um livro?", ok=False, fb="Quem sugere é o atendente.")]),
 ]),
)
