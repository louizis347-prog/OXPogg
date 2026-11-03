"""Bloco de verbos e expressões da aula 11."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('arrive', '🚌', 'chegar', ('arrive', 'We arrive at three.', 'Nós chegamos às três.'), ('arrives', 'The bus arrives at four.', 'O ônibus chega às quatro.'), ('arrived', 'The train arrived early.', 'O trem chegou cedo.'), ('arriving', 'The bus is arriving now.', 'O ônibus está chegando agora.'), 'Arrive at + hora ou lugar pequeno. Passado só com -d: arrived.'),
  vb('leave', '🚪', 'sair / partir', ('leave', 'We leave at five.', 'Nós saímos às cinco.'), ('leaves', 'The train leaves at four.', 'O trem sai às quatro.'), ('left', 'The bus left at three.', 'O ônibus saiu às três.'), ('leaving', 'I am leaving now.', 'Estou saindo agora.'), 'Irregular: leave vira left.'),
  vb('start', '🎬', 'começar', ('start', 'We start at four.', 'Nós começamos às quatro.'), ('starts', 'The movie starts at five.', 'O filme começa às cinco.'), ('started', 'Class started at three.', 'A aula começou às três.'), ('starting', 'The class is starting now.', 'A aula está começando agora.'), 'Com coisas no singular, starts: the movie starts.'),
  vb('wait', '⏳', 'esperar', ('wait', 'We wait here.', 'Nós esperamos aqui.'), ('waits', 'She waits for the bus.', 'Ela espera o ônibus.'), ('waited', 'I waited ten minutes.', 'Eu esperei dez minutos.'), ('waiting', 'I am waiting for the train.', 'Estou esperando o trem.'), 'Wait for + algo ou alguém: wait for the bus.'),
  vb('catch', '🏃', 'pegar (transporte)', ('catch', 'I catch the bus at three.', 'Eu pego o ônibus às três.'), ('catches', 'He catches the train.', 'Ele pega o trem.'), ('caught', 'We caught the bus.', 'Nós pegamos o ônibus.'), ('catching', 'I am catching the train.', 'Estou pegando o trem.'), 'Catch the bus = pegar o ônibus. Irregular: caught.')],
 verb_game=[
  dict(scene='O ônibus chega às quatro.', en='The bus ___ at four o’clock.', opts=['arrive', 'arrives', 'arrived'], ans=1, pt='O ônibus chega às quatro horas.', why='“The bus” é singular: arrives.'),
  dict(scene='Vocês saem às cinco.', en='We ___ at five o’clock.', opts=['leave', 'leaves', 'left'], ans=0, pt='Nós saímos às cinco horas.', why='Com “we” o presente fica na forma base: leave.'),
  dict(scene='Ontem você pegou o trem.', en='Yesterday I ___ the train.', opts=['catch', 'catching', 'caught'], ans=2, pt='Ontem eu peguei o trem.', why='“Yesterday” pede passado irregular: caught.'),
  dict(scene='Agora você espera o ônibus.', en='I am ___ for the bus.', opts=['waiting', 'wait', 'waits'], ans=0, pt='Estou esperando o ônibus.', why='“am” + verbo termina em -ing: waiting.')],
 expressions=[
  dict(en='What time is it?', pt='Que horas são?', ex='Excuse me, what time is it?', exp='Para perguntar as horas.', c='a'),
  dict(en='It’s three o’clock.', pt='São três horas.', ex='It’s three o’clock.', exp='Para dizer a hora exata.', c='b'),
  dict(en='What time is the…?', pt='A que horas é o…?', ex='What time is the bus?', exp='Para perguntar o horário de algo.', c='c'),
  dict(en='half past / thirty', pt='e meia', ex='It’s two thirty.', exp='Para dizer a hora com 30 minutos.', c='d'),
  dict(en='Excuse me', pt='Com licença', ex='Excuse me, what time is it?', exp='Para chamar a atenção de um desconhecido.', c='a'),
  dict(en='We have ten minutes.', pt='Temos dez minutos.', ex='Oh good. We have ten minutes.', exp='Para dizer quanto tempo falta.', c='b')],
 expr_game=[
  dict(cue='Você quer saber as horas a um desconhecido.', opts=['Excuse me, what time is it?', 'It’s three o’clock.', 'We have ten minutes.'], ans=0, why='Excuse me chama a atenção; what time is it? pergunta as horas.'),
  dict(cue='Você quer saber o horário do trem.', opts=['What time is the train?', 'What time is it?', 'It’s at four.'], ans=0, why='What time is the…? pergunta o horário de algo.'),
  dict(cue='São exatamente três horas.', opts=['It’s three o’clock.', 'It’s at three.', 'We have three.'], ans=0, why='It’s + hora + o’clock diz a hora exata.')])
