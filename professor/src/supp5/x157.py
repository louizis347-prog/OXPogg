X = dict(
 key=dict(big="Do you need one more player?", label="Entrar num jogo", sub="Num jogo de rua, você aceita o convite, pergunta se faltam jogadores, descobre seu time, pega a camisa e acompanha a bola."),
 mini=[
  dict(who="Kai", en="Hey! Do you want to {play|join us|try}?", pt="Oi! Quer {jogar|se juntar a nós|tentar}?"),
  dict(who="You", en="Sure. Do you need one more {player|person}?", pt="Claro. Precisam de mais {um jogador|uma pessoa}?"),
  dict(who="Kai", en="Yes! You're with us. Take a {blue|red|white} shirt.", pt="Sim! Você está conosco. Pegue uma camisa {azul|vermelha|branca}."),
  dict(who="You", en="Thanks. Who has the {ball|towel|bottle}?", pt="Valeu. Quem está com {a bola|a toalha|a garrafa}?"),
 ],
 dlg=[
  dict(who="Kai", en="Hey! Do you want to {play?|join us?}", pt="Oi! Quer {jogar?|se juntar a nós?}"),
  dict(who="You", en="Sure. Do you need one more {player?|person?}", pt="Claro. Precisam de mais {um jogador?|uma pessoa?}"),
  dict(who="Kai", en="Yes, we're {three on three.|two on two.}", pt="Sim, somos {três contra três.|dois contra dois.}"),
  dict(who="You", en="Which {team|side} am I on?", pt="Em que {time|lado} estou?"),
  dict(who="Kai", en="You're with us. Take a {blue|red} shirt.", pt="Você está conosco. Pegue uma camisa {azul.|vermelha.}"),
  dict(who="You", en="Thanks. Who has the {ball?|water?}", pt="Valeu. Quem está com {a bola?|a água?}"),
  dict(who="Kai", en="I do. {Pass|Throw} it to me!", pt="Eu estou. {Passe|Jogue} para mim!"),
  dict(who="You", en="Here! {Shoot!|Jump!}", pt="Aqui! {Arremesse!|Pule!}"),
  dict(who="Kai", en="{Nice shot!|Great pass!}", pt="{Bela cesta!|Belo passe!}"),
 ],
 vocab=[
  dict(w="winner", pt="vencedor", e="🏆", ex=["Who is the winner?", "The blue team is the winner."]),
  dict(w="court", pt="quadra", e="🏟️", ex=["The court is in the park.", "We play on the court."]),
  dict(w="point", pt="ponto", e="☝️", ex=["We have ten points.", "One more point, please!"]),
  dict(w="shot", pt="arremesso / cesta", e="🎯", ex=["That is a nice shot.", "Take a shot!"]),
  dict(w="dribble", pt="quicar a bola", e="⛹️", ex=["I dribble with my right hand.", "Dribble, then shoot."]),
  dict(w="gym", pt="ginásio / academia", e="🏋️", ex=["The gym is big.", "We play in the gym."]),
 ],
 molds=[
  dict(title="Convidar alguém", frame="Do you want to play {game} with us?", slots=[dict(key="game", opts=["basketball", "a game", "three on three"])], model="Do you want to play basketball with us?", note="Play + o jogo, sem 'the'. Do you want to... é o convite normal."),
  dict(title="Pedir a bola", frame="{verb} the ball to {who}!", slots=[dict(key="verb", opts=["Pass", "Throw", "Give"]), dict(key="who", opts=["me", "him", "her", "them"])], model="Pass the ball to me!", note="Depois de to, use me, him, her, them (não I, he, she)."),
  dict(title="Escrever sobre seu time", frame="I play with the {color} team. We have {n} players. Our court is in the {place}.", slots=[dict(key="color", opts=["blue", "red", "white"]), dict(key="n", opts=["three", "four", "five"]), dict(key="place", opts=["park", "gym", "school"])], model="I play with the blue team. We have three players. Our court is in the park.", note="Players no plural depois de three, four, five."),
 ],
 sounds=[
  dict(say="Pass it to me!", tag="ligação: pass it", tip="Una pass e it: 'pá-sit'. Acentue PASS e ME."),
  dict(say="Take a blue shirt.", tag="ligação: take a", tip="Soa 'tay-ka'. A palavra 'a' é fraca; acentue TAKE e BLUE."),
  dict(say="Do you need one more player?", tag="ligação: need one", tip="Soa 'nee-dwun'. Una need e one sem pausa."),
 ],
 role=dict(turns=[
  dict(npc="Hey! Do you want to play?", opts=[
   dict(en="Sure. Do you need one more player?", pt="Claro. Precisam de mais um jogador?", reply="Yes, we're three on three."),
   dict(en="Yes! Can I join you?", pt="Sim! Posso entrar?", reply="Sure! We're three on three."),
   dict(en="Maybe. How many players do you have?", pt="Talvez. Quantos jogadores vocês têm?", reply="Five. We're three on three, so we need one more.")]),
  dict(npc="Yes, we're three on three.", opts=[
   dict(en="Which team am I on?", pt="Em que time estou?", reply="You're with us. Take a blue shirt."),
   dict(en="Great! Which shirt do I take?", pt="Ótimo! Qual camisa eu pego?", reply="Take a blue shirt. You're with us."),
   dict(en="Great! Who is on my team?", pt="Ótimo! Quem está no meu time?", reply="You're with us. Take a blue shirt.")]),
  dict(npc="You're with us. Take a blue shirt.", opts=[
   dict(en="Thanks. Who has the ball?", pt="Valeu. Quem está com a bola?", reply="I do. Pass it to me!"),
   dict(en="Thanks. Do we play to eleven?", pt="Valeu. Jogamos até onze?", reply="Yes. The first team to eleven wins. I have the ball. Pass it to me!"),
   dict(en="Thanks! Is the ball new?", pt="Valeu! A bola é nova?", reply="No, it's old, but it's good. I do have it. Pass it to me!")]),
  dict(npc="I do. Pass it to me!", opts=[
   dict(en="Here! Shoot!", pt="Aqui! Arremesse!", reply="Nice shot!"),
   dict(en="Here you go!", pt="Toma!", reply="Thanks! Nice pass!"),
   dict(en="Here! Jump!", pt="Aqui! Pule!", reply="Got it! Nice shot!")]),
 ], change=["O seu time está perdendo: diga 'Keep trying!' para animar.", "Você não tem camisa azul: peça outra cor.", "Está muito quente: pergunte se pode beber água."]),
 writing=dict(task="Você chega a uma quadra no parque. Escreva 2 ou 3 frases: pergunte se precisam de um jogador, em que time você está e quem está com a bola.", model="Hi! Do you need one more player? Which team am I on? Who has the ball?", kw=["player", "team", "ball", "need"], checks=["Perguntou se precisam de um jogador.", "Perguntou em que time está.", "Perguntou pela bola."]),
 scenes=dict(pool=["park", "park2", "playground", "gym"], npc=dict(g="m", role="friend"), you=dict(g="m")),
 convo=dict(npc=dict(name="Kai"), story="Você está num parque. O Kai convida você para um jogo de basquete.", turns=[
  dict(npc="Hey! Do you want to play?", pt="Oi! Quer jogar?", opts=[
   dict(en="Nice shot!", pt="Bela cesta!", ok=False, fb="Ainda não houve nenhum arremesso."),
   dict(en="Take a blue shirt.", pt="Pegue uma camisa azul.", ok=False, fb="Essa fala é do Kai."),
   dict(en="Sure. Do you need one more player?", pt="Claro. Precisam de mais um jogador?", ok=True, fb="Aceita e pergunta se faltam jogadores.")]),
  dict(npc="Yes, we're three on three.", pt="Sim, somos três contra três.", opts=[
   dict(en="Which team am I on?", pt="Em que time estou?", ok=True, fb="Próximo passo: descobrir seu time."),
   dict(en="Yes, I do. Pass it to me!", pt="Sim. Passe para mim!", ok=False, fb="Ainda ninguém tem a bola."),
   dict(en="Nice shot!", pt="Bela cesta!", ok=False, fb="O jogo ainda não começou.")]),
  dict(npc="You're with us. Take a blue shirt.", pt="Você está conosco. Pegue uma camisa azul.", opts=[
   dict(en="Sure. Do you need one more player?", pt="Claro. Precisam de mais um jogador?", ok=False, fb="Você já entrou no time."),
   dict(en="I do. Pass it to me!", pt="Estou com ela. Passe para mim!", ok=False, fb="Você ainda não tem a bola."),
   dict(en="Thanks. Who has the ball?", pt="Valeu. Quem está com a bola?", ok=True, fb="Agradece e pergunta pela bola.")]),
  dict(npc="I do. Pass it to me!", pt="Eu estou. Passe para mim!", opts=[
   dict(en="Thanks. Who has the ball?", pt="Valeu. Quem está com a bola?", ok=False, fb="Ele acabou de dizer: I do."),
   dict(en="You're with us.", pt="Você está conosco.", ok=False, fb="Quem fala isso é o Kai."),
   dict(en="Here! Shoot!", pt="Aqui! Arremesse!", ok=True, fb="Resposta rápida, como num jogo.")]),
  dict(npc="Nice shot!", pt="Bela cesta!", opts=[
   dict(en="Which team am I on?", pt="Em que time estou?", ok=False, fb="Você já sabe seu time."),
   dict(en="Thanks! Good game.", pt="Valeu! Bom jogo.", ok=True, fb="Agradece o elogio com simpatia."),
   dict(en="Here! Shoot!", pt="Aqui! Arremesse!", ok=False, fb="O arremesso já aconteceu.")]),
 ]),
)
