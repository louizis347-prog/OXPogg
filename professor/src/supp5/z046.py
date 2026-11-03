"""Bloco de verbos e expressões da aula 46: andar de ônibus."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('show', '🎫', 'mostrar', ('show', 'I show my pass.', 'Eu mostro meu passe.'), ('shows', 'She shows her card.', 'Ela mostra o cartão.'), ('showed', 'He showed the driver.', 'Ele mostrou ao motorista.'), ('showing', 'I am showing my pass.', 'Estou mostrando meu passe.'), 'Show serve para mostrar passe ou cartão. Passado: showed.'),
  vb('sit', '💺', 'sentar', ('sit', 'I sit near the window.', 'Eu sento perto da janela.'), ('sits', 'Ana sits in the front.', 'A Ana senta na frente.'), ('sat', 'We sat in the back.', 'Nós sentamos atrás.'), ('sitting', 'I am sitting here.', 'Estou sentado aqui.'), 'Irregular: sit vira sat.'),
  vb('hold', '🤝', 'segurar', ('hold', 'I hold the pole.', 'Eu seguro o poste.'), ('holds', 'She holds the rail.', 'Ela segura o corrimão.'), ('held', 'He held my bag.', 'Ele segurou minha bolsa.'), ('holding', 'I am holding on.', 'Estou me segurando.'), 'Irregular: hold vira held.'),
  vb('come', '🚌', 'vir / chegar', ('come', 'The bus comes here.', 'O ônibus vem aqui.'), ('comes', 'It comes every ten minutes.', 'Ele vem a cada dez minutos.'), ('came', 'The bus came late.', 'O ônibus chegou tarde.'), ('coming', 'The bus is coming now.', 'O ônibus está chegando agora.'), 'Passado irregular: came.'),
  vb('stop', '🛑', 'parar', ('stop', 'I stop at the park.', 'Eu paro no parque.'), ('stops', 'The bus stops here.', 'O ônibus para aqui.'), ('stopped', 'It stopped at Main.', 'Ele parou em Main.'), ('stopping', 'The bus is stopping.', 'O ônibus está parando.'), 'Dobra o p: stopped, stopping.')],
 verb_game=[
  dict(scene='Você segura o poste com força.', en='Ana ___ the pole tightly.', opts=['hold', 'holds', 'held'], ans=1, pt='A Ana segura o poste com força.', why='Ana (ela) no presente leva -s: holds.'),
 dict(scene='Ontem você mostrou o passe.', en='I ___ my pass yesterday.', opts=['show', 'showed', 'showing'], ans=1, pt='Eu mostrei meu passe ontem.', why='“Yesterday” pede passado: showed.'),
 dict(scene='Agora o ônibus está chegando.', en='The bus is ___ now.', opts=['come', 'comes', 'coming'], ans=2, pt='O ônibus está chegando agora.', why='“is” + -ing: coming.'),
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
