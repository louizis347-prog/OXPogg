"""Bloco de verbos e expressões da aula 48: pegar um táxi."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('call', '📱', 'chamar / ligar', ('call', 'I call a taxi.', 'Eu chamo um táxi.'), ('calls', 'She calls a car.', 'Ela chama um carro.'), ('called', 'We called a taxi.', 'Nós chamamos um táxi.'), ('calling', 'I am calling the driver.', 'Estou ligando ao motorista.'), 'Call a taxi = chamar um táxi.'),
  vb('take', '🚕', 'levar / pegar', ('take', 'I take a taxi to the airport.', 'Eu pego um táxi para o aeroporto.'), ('takes', 'The driver takes us downtown.', 'O motorista nos leva ao centro.'), ('took', 'It took thirty minutes.', 'Levou trinta minutos.'), ('taking', 'He is taking me to the hotel.', 'Ele está me levando ao hotel.'), 'Irregular: take vira took. It takes… = leva (tempo).'),
  vb('drive', '🚗', 'dirigir', ('drive', 'I drive to work.', 'Eu dirijo até o trabalho.'), ('drives', 'Sam drives carefully.', 'O Sam dirige com cuidado.'), ('drove', 'He drove fast.', 'Ele dirigiu rápido.'), ('driving', 'The driver is driving now.', 'O motorista está dirigindo agora.'), 'Irregular: drive vira drove.'),
  vb('arrive', '🏁', 'chegar', ('arrive', 'We arrive at noon.', 'Nós chegamos ao meio-dia.'), ('arrives', 'The taxi arrives soon.', 'O táxi chega logo.'), ('arrived', 'We arrived at the hotel.', 'Nós chegamos ao hotel.'), ('arriving', 'I am arriving at two.', 'Estou chegando às duas.'), 'Arrive at + lugar pequeno; arrive in + cidade.'),
  vb('tell', '💬', 'dizer / contar', ('tell', 'I tell the driver the address.', 'Eu digo o endereço ao motorista.'), ('tells', 'She tells him Oak Street.', 'Ela diz a ele Oak Street.'), ('told', 'We told him Terminal two.', 'Nós dissemos a ele Terminal dois.'), ('telling', 'I am telling him now.', 'Estou dizendo a ele agora.'), 'Irregular: tell vira told.')],
 verb_game=[
  dict(scene='Você chamou um táxi pelo app.', en='I ___ a taxi on the app.', opts=['call', 'called', 'calling'], ans=1, pt='Eu chamei um táxi pelo app.', why='O contexto passado pede called.'),
  dict(scene='O motorista leva você ao hotel.', en='The driver ___ me to the hotel.', opts=['take', 'takes', 'took'], ans=1, pt='O motorista me leva ao hotel.', why='Driver (ele) no presente leva -s: takes.'),
  dict(scene='Ontem vocês chegaram ao aeroporto.', en='We ___ at the airport yesterday.', opts=['arrive', 'arrives', 'arrived'], ans=2, pt='Nós chegamos ao aeroporto ontem.', why='“Yesterday” pede passado: arrived.'),
  dict(scene='Agora o motorista está dirigindo.', en='The driver is ___ now.', opts=['drive', 'drove', 'driving'], ans=2, pt='O motorista está dirigindo agora.', why='“is” + -ing: driving.')],
 expressions=[
  dict(en='Where to?', pt='Para onde?', ex='Hi! Where to? — To the airport, please.', exp='Pergunta do motorista ao receber você.', c='a'),
  dict(en='To the airport, please.', pt='Para o aeroporto, por favor.', ex='To the airport, please.', exp='Para dizer seu destino ao motorista.', c='b'),
  dict(en='How long does it take?', pt='Quanto tempo leva?', ex='How long does it take to the hotel?', exp='Para saber a duração.', c='c'),
  dict(en='How much is it?', pt='Quanto custa?', ex='How much is it to the airport?', exp='Para saber o preço da corrida.', c='d'),
  dict(en='Keep the change.', pt='Pode ficar com o troco.', ex='Here you go. Keep the change.', exp='Para dar o troco de gorjeta.', c='a'),
  dict(en='Safe travels!', pt='Boa viagem!', ex='Thanks! Safe travels!', exp='Despedida para quem viaja.', c='b')],
 expr_game=[
  dict(cue='O motorista quer saber seu destino.', opts=['To the airport, please.', 'Safe travels!', 'Keep the change.'], ans=0, why='To… please responde ao Where to?'),
  dict(cue='Você quer saber o preço da corrida.', opts=['How much is it?', 'Where to?', 'Safe travels!'], ans=0, why='How much is it? pergunta o preço.'),
  dict(cue='Você quer dar o troco de gorjeta.', opts=['Keep the change.', 'How long does it take?', 'Where to?'], ans=0, why='Keep the change = pode ficar com o troco.')])
