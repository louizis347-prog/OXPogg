"""Bloco de verbos e expressões da aula 231: pausa para o café."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('stir', '🥄', 'mexer', ('stir', 'I stir my coffee.', 'Eu mexo meu café.'), ('stirs', 'Mei stirs her tea.', 'A Mei mexe o chá dela.'), ('stirred', 'He stirred the sugar.', 'Ele mexeu o açúcar.'), ('stirring', 'I am stirring my cup.', 'Estou mexendo minha xícara.'), 'Stir dobra o r no passado: stirred.'),
  vb('offer', '🤝', 'oferecer', ('offer', 'I offer her a donut.', 'Eu ofereço um donut a ela.'), ('offers', 'Sam offers some milk.', 'O Sam oferece um pouco de leite.'), ('offered', 'She offered me a cookie.', 'Ela me ofereceu um biscoito.'), ('offering', 'He is offering sugar.', 'Ele está oferecendo açúcar.'), 'Offer something to someone ou offer someone something.'),
  vb('like', '👍', 'gostar', ('like', 'I like strong coffee.', 'Eu gosto de café forte.'), ('likes', 'Mei likes two sugars.', 'A Mei gosta de dois açúcares.'), ('liked', 'We liked the donuts.', 'Nós gostamos dos donuts.'), ('liking', 'I am liking this break.', 'Estou gostando desta pausa.'), 'Like é verbo de estado: prefira “I like”, não “I am liking”.'),
  vb('have', '☕', 'tomar / ter', ('have', 'I have tea at three.', 'Eu tomo chá às três.'), ('has', 'Sam has a donut.', 'O Sam come um donut.'), ('had', 'We had coffee at ten.', 'Nós tomamos café às dez.'), ('having', 'I am having a break.', 'Estou fazendo uma pausa.'), 'Have também quer dizer comer ou beber. Passado irregular: had.'),
  vb('need', '🛎️', 'precisar', ('need', 'I need a break.', 'Eu preciso de uma pausa.'), ('needs', 'Sam needs a coffee.', 'O Sam precisa de um café.'), ('needed', 'I needed it yesterday.', 'Eu precisei disso ontem.'), ('needing', 'She is needing sugar.', 'Ela está precisando de açúcar.'), 'Need é verbo de estado: no dia a dia, diga “I need”.')],
 verb_game=[
  dict(scene='A Mei sempre põe dois açúcares.', en='Mei ___ two sugars in her coffee.', opts=['like', 'likes', 'liked'], ans=1, pt='A Mei gosta de dois açúcares no café.', why='Com “Mei” (ela), o presente leva -s: likes.'),
  dict(scene='Ontem vocês tomaram café às dez.', en='Yesterday we ___ coffee at ten.', opts=['have', 'has', 'had'], ans=2, pt='Ontem nós tomamos café às dez.', why='“Yesterday” pede passado: had.'),
  dict(scene='Você mexe o açúcar agora.', en='I am ___ my coffee now.', opts=['stir', 'stirs', 'stirring'], ans=2, pt='Estou mexendo meu café agora.', why='“am” + verbo termina em -ing: stirring.'),
  dict(scene='O Sam quer dar um donut à Mei.', en='Sam ___ Mei a donut.', opts=['offer', 'offers', 'offered'], ans=1, pt='O Sam oferece um donut à Mei.', why='Presente com ele/ela: offers.')],
 expressions=[
  dict(en='Time for a break?', pt='Hora de uma pausa?', ex='Time for a break? I need a coffee.', exp='Para chamar alguém para descansar um pouco.', c='a'),
  dict(en='How do you take your coffee?', pt='Como você toma seu café?', ex='How do you take your coffee, Sam?', exp='Para saber se a pessoa quer puro, com leite ou açúcar.', c='b'),
  dict(en='Here you go.', pt='Aqui está.', ex='Here you go. Careful, it’s hot.', exp='Quando você entrega algo a alguém.', c='c'),
  dict(en='Careful, it’s hot.', pt='Cuidado, está quente.', ex='Careful, it’s hot! Take a small sip.', exp='Para avisar que a bebida queima.', c='d'),
  dict(en='black', pt='puro, sem leite', ex='I take my coffee black.', exp='Café sem leite e sem açúcar.', c='a'),
  dict(en='a long morning', pt='uma manhã longa', ex='It’s been a long morning.', exp='Para dizer que você está cansado do trabalho.', c='b')],
 expr_game=[
  dict(cue='Você entrega o café quente para a colega.', opts=['Here you go. Careful, it’s hot.', 'How do you take your coffee?', 'It’s been a long morning.'], ans=0, why='Here you go entrega e Careful avisa.'),
  dict(cue='Você quer saber se ela toma o café com leite.', opts=['Time for a break?', 'How do you take your coffee?', 'Chocolate, please.'], ans=1, why='How do you take…? pergunta o jeito de tomar.'),
  dict(cue='Você está cansado e quer descansar.', opts=['It’s been a long morning.', 'Which flavor?', 'Here you go.'], ans=0, why='A long morning explica o cansaço.')])
