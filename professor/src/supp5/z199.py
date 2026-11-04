"""Bloco de verbos e expressões da aula 199: estou atrasado."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('wake', '☀️', 'acordar', ('wake', 'I wake at six.', 'Eu acordo às seis.'), ('wakes', 'Cole wakes Tom up.', 'O Cole acorda o Tom.'), ('woke', 'He woke late today.', 'Ele acordou tarde hoje.'), ('waking', 'I am waking him now.', 'Estou acordando ele agora.'), 'Wake up é o verbo frasal mais comum. Passado irregular: woke.'),
  vb('hurry', '💨', 'apressar-se', ('hurry', 'We hurry to class.', 'Nós nos apressamos para a aula.'), ('hurries', 'Tom hurries to the bus.', 'O Tom se apressa para o ônibus.'), ('hurried', 'I hurried out the door.', 'Eu saí correndo pela porta.'), ('hurrying', 'I am hurrying now.', 'Estou me apressando agora.'), 'Hurry troca o y por i: hurries e hurried. Hurry up! = Anda logo!'),
  vb('run', '🏃', 'correr', ('run', 'I run to the bus stop.', 'Eu corro até o ponto.'), ('runs', 'Tom runs fast.', 'O Tom corre rápido.'), ('ran', 'He ran to class.', 'Ele correu para a aula.'), ('running', 'I am running late.', 'Estou chegando atrasado.'), 'Run vira ran no passado. “I’m running late” quer dizer “vou me atrasar”.'),
  vb('brush', '🪥', 'escovar', ('brush', 'I brush my teeth.', 'Eu escovo os dentes.'), ('brushes', 'Tom brushes his teeth.', 'O Tom escova os dentes.'), ('brushed', 'She brushed her hair.', 'Ela escovou o cabelo.'), ('brushing', 'I am brushing my teeth.', 'Estou escovando os dentes.'), 'Brush termina em sh: com ele ou ela, acrescente -es (brushes).'),
  vb('grab', '🍌', 'pegar rápido', ('grab', 'I grab a banana.', 'Eu pego uma banana.'), ('grabs', 'Tom grabs his keys.', 'O Tom pega as chaves.'), ('grabbed', 'He grabbed his bag.', 'Ele pegou a mochila.'), ('grabbing', 'I am grabbing my coat.', 'Estou pegando meu casaco.'), 'Grab é pegar rápido. Dobra o b: grabbed, grabbing.')],
 verb_game=[
  dict(scene='O Cole acorda o Tom agora.', en='Cole ___ Tom up.', opts=['wake', 'wakes', 'woke'], ans=1, pt='O Cole acorda o Tom.', why='Com Cole (ele) no presente: wakes.'),
  dict(scene='Ontem o Tom correu até o ônibus.', en='Yesterday Tom ___ to the bus.', opts=['run', 'runs', 'ran'], ans=2, pt='Ontem o Tom correu até o ônibus.', why='Yesterday pede passado: ran.'),
  dict(scene='Agora você escova os dentes.', en='I am ___ my teeth.', opts=['brush', 'brushes', 'brushing'], ans=2, pt='Estou escovando os dentes.', why='Am + verbo termina em -ing: brushing.'),
  dict(scene='Vocês sempre se apressam de manhã.', en='We always ___ in the morning.', opts=['hurry', 'hurries', 'hurried'], ans=0, pt='Nós sempre nos apressamos de manhã.', why='Com we no presente: hurry.')],
 expressions=[
  dict(en='Wake up!', pt='Acorde!', ex='Wake up! It’s seven thirty!', exp='Para acordar alguém.', c='a'),
  dict(en='I’m so late.', pt='Estou tão atrasado.', ex='Oh no, I’m so late.', exp='Quando você percebe o atraso.', c='b'),
  dict(en='on time', pt='na hora', ex='I want to be on time.', exp='Para dizer que você chega sem atraso.', c='c'),
  dict(en='set an alarm', pt='programar um alarme', ex='I set an alarm for seven.', exp='Para falar do despertador.', c='d'),
  dict(en='Hurry up!', pt='Anda logo!', ex='Hurry up! The bus is here.', exp='Para pedir pressa a alguém.', c='a'),
  dict(en='I’m running late.', pt='Estou me atrasando.', ex='Sorry, I’m running late.', exp='Para avisar que vai chegar tarde.', c='b')],
 expr_game=[
  dict(cue='Seu colega ainda está dormindo.', opts=['Wake up!', 'on time', 'set an alarm'], ans=0, why='Wake up! acorda a pessoa.'),
  dict(cue='Você manda mensagem avisando que vai atrasar.', opts=['I’m running late.', 'Wake up!', 'Hurry up!'], ans=0, why='I’m running late avisa o atraso.'),
  dict(cue='Seu amigo está lento e o ônibus já chegou.', opts=['on time', 'Hurry up!', 'I’m so late.'], ans=1, why='Hurry up! pede pressa.')])
