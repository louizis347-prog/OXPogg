"""Bloco de verbos e expressões da aula 46: andar de ônibus."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('pay', '💵', 'pagar', ('pay', 'I pay the driver.', 'Eu pago ao motorista.'), ('pays', 'She pays with a card.', 'Ela paga com cartão.'), ('paid', 'He paid two dollars.', 'Ele pagou dois dólares.'), ('paying', 'I am paying now.', 'Estou pagando agora.'), 'Irregular: pay vira paid.'),
  vb('sit', '💺', 'sentar', ('sit', 'I sit near the window.', 'Eu sento perto da janela.'), ('sits', 'Ana sits in the front.', 'A Ana senta na frente.'), ('sat', 'We sat in the back.', 'Nós sentamos atrás.'), ('sitting', 'I am sitting here.', 'Estou sentado aqui.'), 'Irregular: sit vira sat.'),
  vb('go', '➡️', 'ir', ('go', 'This bus goes downtown.', 'Este ônibus vai ao centro.'), ('goes', 'The bus goes to the park.', 'O ônibus vai ao parque.'), ('went', 'We went to the airport.', 'Nós fomos ao aeroporto.'), ('going', 'I am going downtown.', 'Estou indo ao centro.'), 'Com ônibus (3ª pessoa): goes. Passado: went.'),
  vb('wait', '⏳', 'esperar', ('wait', 'We wait at the bus stop.', 'Nós esperamos no ponto.'), ('waits', 'He waits for the bus.', 'Ele espera o ônibus.'), ('waited', 'I waited ten minutes.', 'Eu esperei dez minutos.'), ('waiting', 'I am waiting for the bus.', 'Estou esperando o ônibus.'), 'Wait for the bus = esperar o ônibus.'),
  vb('stop', '🛑', 'parar', ('stop', 'I stop at the park.', 'Eu paro no parque.'), ('stops', 'The bus stops here.', 'O ônibus para aqui.'), ('stopped', 'It stopped at Main.', 'Ele parou em Main.'), ('stopping', 'The bus is stopping.', 'O ônibus está parando.'), 'Dobra o p: stopped, stopping.')],
 verb_game=[
  dict(scene='Você quer saber se o ônibus vai ao centro.', en='This bus ___ downtown.', opts=['go', 'goes', 'went'], ans=1, pt='Este ônibus vai ao centro.', why='“This bus” (it) no presente leva -es: goes.'),
  dict(scene='Você pagou ao motorista ontem.', en='I ___ the driver yesterday.', opts=['pay', 'paid', 'paying'], ans=1, pt='Eu paguei ao motorista ontem.', why='“Yesterday” pede passado: paid.'),
  dict(scene='Agora você está esperando no ponto.', en='I am ___ at the bus stop.', opts=['wait', 'waits', 'waiting'], ans=2, pt='Estou esperando no ponto.', why='“am” + -ing: waiting.'),
  dict(scene='Vocês sentaram no fundo do ônibus.', en='We ___ in the back.', opts=['sit', 'sits', 'sat'], ans=2, pt='Nós sentamos no fundo.', why='Passado de sit é sat.')],
 expressions=[
  dict(en='Does this bus go…?', pt='Este ônibus vai para…?', ex='Does this bus go downtown?', exp='Para confirmar o destino antes de subir.', c='a'),
  dict(en='How much is the fare?', pt='Quanto custa a passagem?', ex='How much is the fare?', exp='Para saber o preço da viagem.', c='b'),
  dict(en='How long does it take?', pt='Quanto tempo leva?', ex='How long does it take to the park?', exp='Para saber a duração da viagem.', c='c'),
  dict(en='bus stop', pt='ponto de ônibus', ex='I wait at the bus stop.', exp='O local onde você espera o ônibus.', c='d'),
  dict(en='Is this seat taken?', pt='Este lugar está ocupado?', ex='Excuse me, is this seat taken?', exp='Para sentar ao lado de alguém.', c='a'),
  dict(en='Enjoy your trip!', pt='Boa viagem!', ex='Thanks, enjoy your trip!', exp='Despedida simpática para quem viaja.', c='b')],
 expr_game=[
  dict(cue='Você quer saber o preço da passagem.', opts=['How much is the fare?', 'Does this bus go downtown?', 'Enjoy your trip!'], ans=0, why='How much…? pergunta o preço.'),
  dict(cue='Você quer sentar ao lado de alguém.', opts=['Is this seat taken?', 'How long does it take?', 'Bus stop.'], ans=0, why='Is this seat taken? pede o lugar vago.'),
  dict(cue='Você quer saber o tempo da viagem.', opts=['How long does it take?', 'How much is the fare?', 'Does this bus go…?'], ans=0, why='How long does it take? pergunta a duração.')])
