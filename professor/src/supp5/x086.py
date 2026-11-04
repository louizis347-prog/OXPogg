"""Bloco extra da aula 86: noite de cinema."""
X = dict(
 key=dict(big="How about a comedy tonight?", label="Escolher um filme", sub="Diga o que você gosta, sugira um filme, pergunte o horário e peça pipoca. Os nomes dos tamanhos variam conforme o cinema."),
 mini=[
  dict(who="Cole", en="What do you want to {watch|see|choose} tonight?", pt="O que você quer {ver|assistir|escolher} hoje à noite?"),
  dict(who="You", en="I like {comedies|cartoons|horror films}. And you?", pt="Gosto de {comédias|desenhos|filmes de terror}. E você?"),
  dict(who="Cole", en="What time does it {start|end|open}?", pt="Que horas {começa|termina|abre}?"),
  dict(who="You", en="At {eight|seven|nine}. Let's buy tickets online.", pt="Às {oito|sete|nove}. Vamos comprar ingressos online."),
 ],
 dlg=[
  dict(who="Cole", en="What do you want to {watch|see} tonight?", pt="O que você quer {ver|assistir} hoje à noite?"),
  dict(who="You", en="I like {comedies.|cartoons.} And you?", pt="Gosto de {comédias.|desenhos.} E você?"),
  dict(who="Cole", en="I like {action|horror} movies.", pt="Gosto de filmes de {ação.|terror.}"),
  dict(who="You", en="How about a {comedy|cartoon} tonight?", pt="Que tal {uma comédia|um desenho} hoje?"),
  dict(who="Cole", en="OK. What time does it {start?|end?}", pt="Ok. Que horas {começa?|termina?}"),
  dict(who="You", en="At {eight.|seven.} Let's buy tickets online.", pt="Às {oito.|sete.} Vamos comprar ingressos online."),
  dict(who="Cole", en="Do you want {popcorn?|candy?}", pt="Quer {pipoca?|doces?}"),
  dict(who="You", en="Yes, a {large|small} one!", pt="Quero, {uma grande!|uma pequena!}"),
  dict(who="Cole", en="Enjoy the {movie!|show!}", pt="Aproveite o {filme!|show!}"),
 ],
 vocab=[
  dict(w="popcorn", pt="pipoca", e="🍿", ex=["I want a large popcorn.", "The popcorn is warm."]),
  dict(w="screen", pt="tela", e="📽️", ex=["The screen is very big.", "We sit near the screen."]),
  dict(w="comedy", pt="comédia", e="😂", ex=["This comedy is funny.", "I like a good comedy."]),
  dict(w="story", pt="história", e="📚", ex=["The story is funny.", "I like this story."]),
  dict(w="row", pt="fileira", e="🪑", ex=["We are in row F.", "Our row is in the middle."]),
  dict(w="actor", pt="ator", e="🎭", ex=["The actor is funny.", "My favorite actor is here."]),
 ],
 molds=[
  dict(title="Dizer do que você gosta", frame="I like {type} films.", slots=[dict(key="type", opts=["comedy", "action", "cartoon", "scary"])], model="I like comedy films.", note="Like + tipo de filme, sem -ing e sem 'the'."),
  dict(title="Sugerir um programa", frame="How about a {type} at {time}?", slots=[dict(key="type", opts=["comedy", "cartoon", "action film"]), dict(key="time", opts=["seven", "eight", "nine"])], model="How about a comedy at seven?", note="How about + coisa é um jeito simples de sugerir. At + hora."),
  dict(title="Escrever um plano", frame="Hi! Let's watch a {type} tonight. It starts at {time}. Do you want {snack}?", slots=[dict(key="type", opts=["comedy", "cartoon", "film"]), dict(key="time", opts=["seven", "eight", "nine"]), dict(key="snack", opts=["popcorn", "candy", "a drink"])], model="Hi! Let's watch a comedy tonight. It starts at seven. Do you want popcorn?", note="Let's + verbo convida. Do you want…? oferece algo."),
 ],
 sounds=[
  dict(say="What time does it start?", tag="ligação: what time", tip="Una what e time: 'uótaime'. O t de what quase some. Acentue TIME e START."),
  dict(say="Do you want popcorn?", tag="redução: do you", tip="Em fala rápida, 'do you' vira 'dju'. Acentue WANT e POP."),
  dict(say="Let's buy tickets online.", tag="ritmo: BUY TICK-ets ON-line", tip="Acentue BUY, TICK e ON; 'let's' e 'ets' ficam leves."),
 ],
 role=dict(turns=[
  dict(npc="What do you want to watch tonight?", opts=[
   dict(en="I like comedies. And you?", pt="Gosto de comédias. E você?", reply="I like action movies."),
   dict(en="I like cartoons. And you?", pt="Gosto de desenhos. E você?", reply="I like action movies."),
   dict(en="Let's see a comedy. And you?", pt="Vamos ver uma comédia. E você?", reply="I like action movies.")]),
  dict(npc="I like action movies.", opts=[
   dict(en="How about a comedy tonight?", pt="Que tal uma comédia hoje?", reply="OK. What time does it start?"),
   dict(en="How about a cartoon tonight?", pt="Que tal um desenho hoje?", reply="OK. What time does it start?"),
   dict(en="Let's see a comedy this time.", pt="Vamos ver uma comédia desta vez.", reply="OK. What time does it start?")]),
  dict(npc="OK. What time does it start?", opts=[
   dict(en="At eight. Let's buy tickets online.", pt="Às oito. Vamos comprar ingressos online.", reply="Good idea. Do you want popcorn?"),
   dict(en="At seven. Let's buy tickets online.", pt="Às sete. Vamos comprar ingressos online.", reply="Good idea. Do you want popcorn?"),
   dict(en="At nine. Let's get tickets on my phone.", pt="Às nove. Vamos pegar ingressos no meu celular.", reply="Good idea. Do you want popcorn?")]),
  dict(npc="Do you want popcorn?", opts=[
   dict(en="Yes, a large one!", pt="Quero, uma grande!", reply="Great! Enjoy the movie!"),
   dict(en="Yes, a small one, please.", pt="Quero, uma pequena, por favor.", reply="OK! Enjoy the movie!"),
   dict(en="No, thanks. I want candy.", pt="Não, obrigado. Quero doces.", reply="OK! Enjoy the movie!")]),
 ], change=["O filme que vocês querem já começou: sugira o próximo horário.", "Cole não gosta de comédia: sugira outro tipo de filme.", "A pipoca grande acabou: peça uma média."]),
 writing=dict(task="Escreva 2 ou 3 frases para um amigo: diga que filme você quer ver, a que horas começa e pergunte se ele quer pipoca.", model="Hi! Let's watch a comedy tonight. It starts at eight. Do you want popcorn?", kw=["watch", "comedy", "starts", "popcorn"], checks=["Disse qual filme quer ver.", "Disse o horário.", "Perguntou sobre a pipoca."]),
 scenes=dict(pool=["living", "home1", "stage", "counter"], npc=dict(g="m", role="friend"), you=dict(g="f")),
 convo=dict(npc=dict(name="Cole"), story="Você planeja uma noite de cinema com seu amigo Cole.", turns=[
  dict(npc="What do you want to watch tonight?", pt="O que você quer ver hoje à noite?", opts=[
   dict(en="Enjoy the movie!", pt="Aproveite o filme!", ok=False, fb="É uma despedida, ainda é cedo."),
   dict(en="Yes, a large one!", pt="Quero, uma grande!", ok=False, fb="Responde a outra pergunta (pipoca)."),
   dict(en="I like comedies. And you?", pt="Gosto de comédias. E você?", ok=True, fb="Diz o gosto e devolve a pergunta.")]),
  dict(npc="I like action movies.", pt="Gosto de filmes de ação.", opts=[
   dict(en="How about a comedy tonight?", pt="Que tal uma comédia hoje?", ok=True, fb="Sugere um meio-termo."),
   dict(en="What do you want to watch?", pt="O que você quer ver?", ok=False, fb="Ele acabou de responder."),
   dict(en="At eight.", pt="Às oito.", ok=False, fb="Ainda não perguntaram a hora.")]),
  dict(npc="OK. What time does it start?", pt="Ok. Que horas começa?", opts=[
   dict(en="I like action movies.", pt="Gosto de filmes de ação.", ok=False, fb="Essa fala é dele."),
   dict(en="Do you want popcorn?", pt="Quer pipoca?", ok=False, fb="Ele pediu o horário primeiro."),
   dict(en="At eight. Let's buy tickets online.", pt="Às oito. Vamos comprar ingressos online.", ok=True, fb="Responde a hora e propõe o próximo passo.")]),
  dict(npc="Do you want popcorn?", pt="Quer pipoca?", opts=[
   dict(en="At eight.", pt="Às oito.", ok=False, fb="Já falaram a hora."),
   dict(en="Yes, a large one!", pt="Quero, uma grande!", ok=True, fb="Resposta curta e natural."),
   dict(en="I like comedies.", pt="Gosto de comédias.", ok=False, fb="Não responde sobre pipoca.")]),
  dict(npc="Enjoy the movie!", pt="Aproveite o filme!", opts=[
   dict(en="Thanks! You too!", pt="Obrigado! Você também!", ok=True, fb="Resposta natural."),
   dict(en="What time does it start?", pt="Que horas começa?", ok=False, fb="Já foi respondido."),
   dict(en="How about a comedy?", pt="Que tal uma comédia?", ok=False, fb="A escolha já foi feita.")]),
 ]),
)
