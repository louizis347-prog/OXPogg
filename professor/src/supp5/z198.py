"""Bloco de verbos e expressões da aula 198: pedir carona."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('drive', '🚗', 'dirigir', ('drive', 'I drive to work.', 'Eu dirijo até o trabalho.'), ('drives', 'Leo drives a blue car.', 'O Leo dirige um carro azul.'), ('drove', 'He drove for an hour.', 'Ele dirigiu por uma hora.'), ('driving', 'I am driving now.', 'Estou dirigindo agora.'), 'Drive vira drove no passado. Com a pessoa que dirige: “Leo drives”.'),
  vb('arrive', '📍', 'chegar', ('arrive', 'We arrive at nine.', 'Nós chegamos às nove.'), ('arrives', 'Leo arrives at work.', 'O Leo chega ao trabalho.'), ('arrived', 'She arrived at noon.', 'Ela chegou ao meio-dia.'), ('arriving', 'I am arriving now.', 'Estou chegando agora.'), 'Arrive + at (lugar pequeno) ou in (cidade): arrive at work, arrive in Denver.'),
  vb('give', '🎁', 'dar', ('give', 'I give him five dollars.', 'Eu dou cinco dólares a ele.'), ('gives', 'Sam gives money for gas.', 'O Sam dá dinheiro pela gasolina.'), ('gave', 'He gave me a ride.', 'Ele me deu uma carona.'), ('giving', 'She is giving a ride.', 'Ela está dando uma carona.'), 'Give vira gave no passado. Give someone a ride = dar carona a alguém.'),
  vb('park', '🅿️', 'estacionar', ('park', 'We park in front.', 'Nós estacionamos na frente.'), ('parks', 'Leo parks the car.', 'O Leo estaciona o carro.'), ('parked', 'I parked near the bank.', 'Eu estacionei perto do banco.'), ('parking', 'He is parking now.', 'Ele está estacionando agora.'), 'Park é regular. Park the car = estacionar o carro.'),
  vb('share', '🤝', 'dividir', ('share', 'We share the gas.', 'Nós dividimos a gasolina.'), ('shares', 'Sam shares the cost.', 'O Sam divide o custo.'), ('shared', 'They shared a ride.', 'Eles dividiram uma carona.'), ('sharing', 'We are sharing a car.', 'Estamos dividindo um carro.'), 'Share termina em e: o passado leva só -d (shared).')],
 verb_game=[
  dict(scene='O Leo chega ao trabalho às nove.', en='Leo ___ at work at nine.', opts=['arrive', 'arrives', 'arrived'], ans=1, pt='O Leo chega ao trabalho às nove.', why='Com Leo (ele) no presente: arrives.'),
  dict(scene='Ontem ele te deu uma carona.', en='Yesterday he ___ me a ride.', opts=['give', 'gives', 'gave'], ans=2, pt='Ontem ele me deu uma carona.', why='Yesterday pede passado: gave.'),
  dict(scene='O Leo está ao volante agora.', en='Leo is ___ to work now.', opts=['drive', 'drives', 'driving'], ans=2, pt='O Leo está dirigindo para o trabalho agora.', why='Is + verbo termina em -ing: driving.'),
  dict(scene='Vocês dividem a gasolina.', en='We ___ the gas.', opts=['share', 'shares', 'shared'], ans=0, pt='Nós dividimos a gasolina.', why='Com we no presente: share.')],
 expressions=[
  dict(en='Can I get a ride?', pt='Posso pegar carona?', ex='My car is in the shop. Can I get a ride?', exp='Para pedir carona com educação.', c='a'),
  dict(en='in the shop', pt='na oficina', ex='My car is in the shop.', exp='Quando o carro está no conserto.', c='b'),
  dict(en='Where should I meet you?', pt='Onde devo te encontrar?', ex='Thanks! Where should I meet you?', exp='Para combinar o ponto de encontro.', c='c'),
  dict(en='How long is the drive?', pt='Quanto dura o trajeto?', ex='How long is the drive to work?', exp='Para saber o tempo da viagem de carro.', c='d'),
  dict(en='chip in', pt='contribuir com dinheiro', ex='Can I chip in for gas?', exp='Para oferecer ajuda a pagar algo.', c='a'),
  dict(en='See you around!', pt='A gente se vê por aí!', ex='Thanks for the favor. See you around!', exp='Despedida informal e simpática.', c='b')],
 expr_game=[
  dict(cue='Você quer saber o lugar para encontrar o motorista.', opts=['How long is the drive?', 'Where should I meet you?', 'See you around!'], ans=1, why='Where should I meet you? pergunta o lugar.'),
  dict(cue='Você quer oferecer dinheiro pela gasolina.', opts=['Can I chip in for gas?', 'My car is in the shop.', 'Can I get a ride?'], ans=0, why='Chip in for gas oferece ajuda para pagar.'),
  dict(cue='Seu carro está no conserto e você precisa de ajuda para ir ao trabalho.', opts=['See you around!', 'How long is the drive?', 'Can I get a ride?'], ans=2, why='Can I get a ride? pede carona.')])
