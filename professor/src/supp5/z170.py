"""Bloco de verbos e expressões da aula 170: chamar uma corrida."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('book', '📱', 'reservar, pedir (corrida)', ('book', 'I book a ride.', 'Eu peço uma corrida.'), ('books', 'Leo books a ride.', 'O Leo pede uma corrida.'), ('booked', 'I booked a ride last night.', 'Eu pedi uma corrida ontem à noite.'), ('booking', 'I am booking a ride.', 'Estou pedindo uma corrida.'), 'Passado regular: booked.'),
  vb('buckle', '🪢', 'afivelar, colocar o cinto', ('buckle', 'I buckle my seatbelt.', 'Eu coloco o cinto.'), ('buckles', 'Leo buckles up.', 'O Leo coloca o cinto.'), ('buckled', 'He buckled up.', 'Ele colocou o cinto.'), ('buckling', 'I am buckling my seatbelt.', 'Estou colocando o cinto.'), 'A expressão comum é buckle up.'),
  vb('put', '🧳', 'pôr, colocar', ('put', 'I put my bag in the trunk.', 'Eu ponho a mala no porta-malas.'), ('puts', 'Marco puts the bag in the trunk.', 'O Marco põe a mala no porta-malas.'), ('put', 'He put my bag in the trunk.', 'Ele pôs minha mala no porta-malas.'), ('putting', 'He is putting the bag in the trunk.', 'Ele está pondo a mala no porta-malas.'), 'Put é igual no presente e no passado. Dobra o t no -ing.'),
  vb('drive', '🚗', 'dirigir', ('drive', 'I drive to work.', 'Eu dirijo até o trabalho.'), ('drives', 'Marco drives to the airport.', 'O Marco dirige até o aeroporto.'), ('drove', 'He drove me to the hotel.', 'Ele me levou de carro ao hotel.'), ('driving', 'Marco is driving fast.', 'O Marco está dirigindo rápido.'), 'Drive é irregular: drove.'),
  vb('check', '✅', 'conferir, checar', ('check', 'I check the app.', 'Eu confiro o aplicativo.'), ('checks', 'Leo checks the car.', 'O Leo confere o carro.'), ('checked', 'I checked the name.', 'Eu conferi o nome.'), ('checking', 'I am checking the map.', 'Estou conferindo o mapa.'), 'Passado regular: checked.')],
 verb_game=[
  dict(scene='O Marco está dirigindo agora.', en='Marco is ___ to the airport.', opts=['drive', 'driving', 'drove'], ans=1, pt='O Marco está dirigindo para o aeroporto.', why='Is + -ing: driving.'),
  dict(scene='O Marco põe a mala no porta-malas.', en='Marco ___ the bag in the trunk.', opts=['put', 'puts', 'putting'], ans=1, pt='O Marco põe a mala no porta-malas.', why='Ele (3ª pessoa) leva -s: puts.'),
  dict(scene='Você vai pedir uma corrida.', en='I want to ___ a ride.', opts=['book', 'books', 'booked'], ans=0, pt='Quero pedir uma corrida.', why='Depois de to, use o verbo base: book.'),
  dict(scene='Ontem você conferiu o nome do motorista.', en='Yesterday I ___ the driver’s name.', opts=['check', 'checked', 'checking'], ans=1, pt='Ontem eu conferi o nome do motorista.', why='Yesterday pede passado: checked.')],
 expressions=[
  dict(en='Are you Leo?', pt='Você é o Leo?', ex='Hi! Are you Leo?', exp='Para confirmar quem é o passageiro.', c='a'),
  dict(en='You’re my driver, right?', pt='Você é meu motorista, né?', ex='Hi! You’re my driver, right?', exp='Para confirmar a pessoa antes de entrar.', c='b'),
  dict(en='Going to the airport?', pt='Vai para o aeroporto?', ex='Going to the airport?', exp='Para confirmar o destino.', c='c'),
  dict(en='Buckle up.', pt='Coloque o cinto.', ex='Sure, buckle up.', exp='Para lembrar de colocar o cinto.', c='d'),
  dict(en='How long will it take?', pt='Quanto tempo vai demorar?', ex='How long will it take to the airport?', exp='Para perguntar a duração.', c='a'),
  dict(en='About twenty minutes.', pt='Uns vinte minutos.', ex='It’s about twenty minutes.', exp='Para dizer um tempo aproximado.', c='b')],
 expr_game=[
  dict(cue='Você quer saber a duração da corrida.', opts=['Buckle up.', 'How long will it take?', 'Going to the airport?'], ans=1, why='How long will it take? pergunta o tempo.'),
  dict(cue='O motorista lembra de colocar o cinto.', opts=['Buckle up.', 'About twenty minutes.', 'Are you Leo?'], ans=0, why='Buckle up = coloque o cinto.'),
  dict(cue='Você confirma que ele é seu motorista.', opts=['Going to the airport?', 'You’re my driver, right?', 'About twenty minutes.'], ans=1, why='Right? no fim pede confirmação.')])
