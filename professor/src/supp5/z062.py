"""Bloco de verbos e expressões da aula 062: locadora de carros."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('rent', '🚗', 'alugar', ('rent', 'I rent a small car.', 'Eu alugo um carro pequeno.'), ('rents', 'Claire rents a car.', 'A Claire aluga um carro.'), ('rented', 'We rented a big car.', 'Nós alugamos um carro grande.'), ('renting', 'I am renting a car.', 'Estou alugando um carro.'), 'Passado regular: rented.'),
  vb('drive', '🛣️', 'dirigir', ('drive', 'I drive on the highway.', 'Eu dirijo na rodovia.'), ('drives', 'Ben drives to work.', 'O Ben dirige até o trabalho.'), ('drove', 'We drove three hours.', 'Nós dirigimos três horas.'), ('driving', 'I am driving to Austin.', 'Estou dirigindo para Austin.'), 'Drive é irregular: drove no passado.'),
  vb('start', '🔑', 'ligar (o carro)', ('start', 'I start the car.', 'Eu ligo o carro.'), ('starts', 'She starts the car.', 'Ela liga o carro.'), ('started', 'He started the engine.', 'Ele ligou o motor.'), ('starting', 'I am starting the car.', 'Estou ligando o carro.'), 'Start também significa começar.'),
  vb('park', '🅿️', 'estacionar', ('park', 'I park in the lot.', 'Eu estaciono no estacionamento.'), ('parks', 'Ben parks the car.', 'O Ben estaciona o carro.'), ('parked', 'We parked near the hotel.', 'Nós estacionamos perto do hotel.'), ('parking', 'I am parking now.', 'Estou estacionando agora.'), 'Park = estacionar; também é parque, o substantivo.'),
  vb('return', '↩️', 'devolver', ('return', 'I return the car on Friday.', 'Eu devolvo o carro na sexta.'), ('returns', 'Claire returns the key.', 'A Claire devolve a chave.'), ('returned', 'He returned the car late.', 'Ele devolveu o carro tarde.'), ('returning', 'I am returning the car.', 'Estou devolvendo o carro.'), 'Return = devolver ou voltar. Passado regular: returned.')],
 verb_game=[
  dict(scene='Você está dirigindo agora.', en='I am ___ to San Antonio.', opts=['drive', 'drove', 'driving'], ans=2, pt='Estou dirigindo para San Antonio.', why='“am” + -ing: driving.'),
  dict(scene='Ontem a Claire dirigiu três horas.', en='Yesterday Claire ___ for three hours.', opts=['drives', 'drove', 'drive'], ans=1, pt='Ontem a Claire dirigiu por três horas.', why='“Yesterday” pede passado irregular: drove.'),
  dict(scene='O Ben devolve a chave.', en='Ben ___ the key to the office.', opts=['return', 'returns', 'returned'], ans=1, pt='O Ben devolve a chave ao escritório.', why='Ele (3ª pessoa) leva -s: returns.'),
  dict(scene='Você aluga um carro hoje.', en='I want to ___ a small car.', opts=['rent', 'rents', 'rented'], ans=0, pt='Quero alugar um carro pequeno.', why='Depois de to, use o verbo base: rent.')],
 expressions=[
  dict(en='I’d like to rent a car.', pt='Eu gostaria de alugar um carro.', ex='Hi! I’d like to rent a car.', exp='Para abrir o pedido na locadora.', c='a'),
  dict(en='For how many days?', pt='Por quantos dias?', ex='For how many days? — Three.', exp='Para saber a duração do aluguel.', c='b'),
  dict(en='fifty dollars a day', pt='cinquenta dólares por dia', ex='It is fifty dollars a day.', exp='Para dizer o preço diário.', c='c'),
  dict(en='Is gas included?', pt='A gasolina está incluída?', ex='Is gas included in the price?', exp='Para saber se o combustível está no preço.', c='d'),
  dict(en='Here it is.', pt='Aqui está.', ex='My license? Here it is.', exp='Para entregar algo que pediram.', c='a'),
  dict(en='Have a safe trip!', pt='Boa viagem!', ex='Thanks. Have a safe trip!', exp='Despedida a quem vai viajar.', c='b')],
 expr_game=[
  dict(cue='Você quer saber se a gasolina está no preço.', opts=['Is gas included?', 'Have a safe trip!', 'Here it is.'], ans=0, why='Is... included? pergunta o que está no preço.'),
  dict(cue='Você entrega a carteira que o atendente pediu.', opts=['Here it is.', 'For how many days?', 'Is gas included?'], ans=0, why='Here it is = aqui está.'),
  dict(cue='Você se despede de quem vai viajar.', opts=['Have a safe trip!', 'Here it is.', 'For how many days?'], ans=0, why='Have a safe trip! deseja uma boa viagem.')])
