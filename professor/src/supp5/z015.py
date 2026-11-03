"""Bloco de verbos e expressões da aula 015."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('meet', '🤝', 'encontrar', ('meet', 'We meet at seven.', 'Nós nos encontramos às sete.'), ('meets', 'Mia meets us there.', 'A Mia nos encontra lá.'), ('met', 'We met at Joe’s.', 'Nós nos encontramos no Joe’s.'), ('meeting', 'I am meeting Sam.', 'Estou encontrando o Sam.'), 'Irregular: meet, met.'),
  vb('text', '💬', 'mandar mensagem', ('text', 'I text my friends.', 'Eu mando mensagem para meus amigos.'), ('texts', 'Mia texts me.', 'A Mia me manda mensagem.'), ('texted', 'I texted Sam.', 'Eu mandei mensagem ao Sam.'), ('texting', 'I am texting Mia.', 'Estou mandando mensagem à Mia.'), 'Text também é verbo nos EUA.'),
  vb('decide', '🤔', 'decidir', ('decide', 'We decide at six.', 'Nós decidimos às seis.'), ('decides', 'Raj decides the place.', 'O Raj decide o lugar.'), ('decided', 'We decided on pizza.', 'Nós decidimos por pizza.'), ('deciding', 'I am deciding now.', 'Estou decidindo agora.'), 'Decide + -d no passado; decide on = escolher/decidir por.'),
  vb('want', '🙋', 'querer', ('want', 'I want pizza.', 'Eu quero pizza.'), ('wants', 'Sam wants to come.', 'O Sam quer vir.'), ('wanted', 'I wanted to go.', 'Eu queria ir.'), ('wanting', 'I am wanting pizza.', 'Estou querendo pizza.'), 'Want + to + verbo. Quase não se usa com -ing.'),
  vb('bring', '🎁', 'trazer', ('bring', 'I bring snacks.', 'Eu trago lanches.'), ('brings', 'Mia brings a game.', 'A Mia traz um jogo.'), ('brought', 'He brought drinks.', 'Ele trouxe bebidas.'), ('bringing', 'I am bringing a friend.', 'Estou trazendo um amigo.'), 'Irregular: bring, brought.')],
 verb_game=[
  dict(scene='Ontem vocês decidiram ir ao Joe’s.', en='We ___ to go to Joe’s yesterday.', opts=['decide', 'decides', 'decided'], ans=2, pt='Nós decidimos ir ao Joe’s ontem.', why='“Yesterday” pede passado: decided.'),
  dict(scene='A Mia sempre traz um jogo.', en='Mia ___ a game.', opts=['bring', 'brings', 'brought'], ans=1, pt='A Mia traz um jogo.', why='Com “Mia” (ela): brings.'),
  dict(scene='Você manda mensagem ao Sam agora.', en='I am ___ Sam now.', opts=['text', 'texts', 'texting'], ans=2, pt='Estou mandando mensagem ao Sam agora.', why='“am” + -ing: texting.'),
  dict(scene='Vocês se encontram às sete.', en='We ___ at seven.', opts=['meet', 'meets', 'met'], ans=0, pt='Nós nos encontramos às sete.', why='Com “we” o presente fica na base: meet.')],
 expressions=[
  dict(en='Are you free tonight?', pt='Você está livre hoje à noite?', ex='Hey! Are you free tonight?', exp='Para convidar alguém.', c='a'),
  dict(en='What’s up?', pt='E aí? / O que foi?', ex='Yes! What’s up?', exp='Pergunta informal.', c='b'),
  dict(en='Let’s…', pt='Vamos…', ex='Let’s get pizza.', exp='Para sugerir um plano.', c='c'),
  dict(en='Sounds great!', pt='Parece ótimo!', ex='Sounds great! Where?', exp='Para aceitar um plano.', c='d'),
  dict(en='See you at seven!', pt='A gente se vê às sete!', ex='Sure. See you at seven!', exp='Para confirmar a hora.', c='a'),
  dict(en='I think so.', pt='Acho que sim.', ex='I think so. Why?', exp='Resposta suave quando não tem certeza.', c='b')],
 expr_game=[
  dict(cue='Você quer saber se o amigo pode sair hoje à noite.', opts=['Are you free tonight?', 'See you at seven!', 'Sounds great!'], ans=0, why='Are you free…? checa a agenda.'),
  dict(cue='Um amigo propôs pizza e você aceita.', opts=['I think so.', 'Sounds great!', 'What’s up?'], ans=1, why='Sounds great! aceita.'),
  dict(cue='Você propõe comer pizza.', opts=['Let’s get pizza.', 'Are you free?', 'See you then.'], ans=0, why='Let’s… sugere um plano.')])
