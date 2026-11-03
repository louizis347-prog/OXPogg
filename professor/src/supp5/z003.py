"""Bloco de verbos e expressões da aula 3."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('meet', '🤝', 'conhecer / encontrar', ('meet', 'I meet my neighbors.', 'Eu conheço meus vizinhos.'), ('meets', 'Maya meets Sam today.', 'A Maya encontra o Sam hoje.'), ('met', 'We met in the hall.', 'Nós nos encontramos no corredor.'), ('meeting', 'I am meeting Lena now.', 'Estou conhecendo a Lena agora.'), 'Irregular: meet vira met. Nice to meet you usa a forma base.'),
  vb('live', '🏠', 'morar', ('live', 'I live in 4B.', 'Eu moro no 4B.'), ('lives', 'Sam lives in 2A.', 'O Sam mora no 2A.'), ('lived', 'We lived in Texas.', 'Nós moramos no Texas.'), ('living', 'I am living here now.', 'Estou morando aqui agora.'), 'Live in + lugar: live in a building.'),
  vb('move', '📦', 'mudar-se', ('move', 'We move to Austin.', 'Nós nos mudamos para Austin.'), ('moves', 'Lena moves to 5C.', 'A Lena se muda para o 5C.'), ('moved', 'I moved here last week.', 'Eu me mudei para cá semana passada.'), ('moving', 'I am moving in today.', 'Estou me mudando hoje.'), 'Move in = mudar-se para uma casa; passado só com -d: moved.'),
  vb('like', '👍', 'gostar', ('like', 'I like this building.', 'Eu gosto deste prédio.'), ('likes', 'Sam likes tacos.', 'O Sam gosta de tacos.'), ('liked', 'She liked the neighborhood.', 'Ela gostou do bairro.'), ('liking', 'I am liking it here.', 'Estou gostando daqui.'), 'Like + algo, sem “of”: I like tacos.'),
  vb('see', '👀', 'ver', ('see', 'I see you in the hall.', 'Eu vejo você no corredor.'), ('sees', 'Maya sees Sam often.', 'A Maya vê o Sam com frequência.'), ('saw', 'I saw her yesterday.', 'Eu a vi ontem.'), ('seeing', 'I am seeing him later.', 'Vou ver ele mais tarde.'), 'Irregular: see vira saw. See you around! é despedida.')],
 verb_game=[
  dict(scene='Você diz onde mora.', en='I ___ in apartment 4B.', opts=['live', 'lives', 'lived'], ans=0, pt='Eu moro no apartamento 4B.', why='Com “I” o presente fica na forma base: live.'),
  dict(scene='O Sam mora no 2A.', en='Sam ___ in apartment 2A.', opts=['live', 'lives', 'living'], ans=1, pt='O Sam mora no apartamento 2A.', why='Com “Sam” (ele) o presente leva -s: lives.'),
  dict(scene='Você conheceu a Lena ontem.', en='I ___ Lena yesterday.', opts=['meet', 'meets', 'met'], ans=2, pt='Eu conheci a Lena ontem.', why='“Yesterday” pede passado: met.'),
  dict(scene='Você se mudou semana passada.', en='I ___ here last week.', opts=['moved', 'move', 'moving'], ans=0, pt='Eu me mudei para cá semana passada.', why='“Last week” pede passado: moved.')],
 expressions=[
  dict(en='Nice to meet you.', pt='Prazer em conhecer você.', ex='Hi, Maya! Nice to meet you.', exp='Ao conhecer alguém.', c='a'),
  dict(en='Nice to meet you too.', pt='Prazer também.', ex='Nice to meet you too!', exp='Resposta ao “Nice to meet you”.', c='b'),
  dict(en='Are you new here?', pt='Você é novo aqui?', ex='Are you new here?', exp='Para puxar conversa com um vizinho.', c='c'),
  dict(en='Welcome to the building!', pt='Bem-vindo ao prédio!', ex='Welcome to the building!', exp='Para receber um vizinho novo.', c='d'),
  dict(en='move in', pt='mudar-se (para dentro)', ex='I move in on Saturday.', exp='Verbo frasal: começar a morar num lugar.', c='a'),
  dict(en='See you around!', pt='A gente se vê por aí!', ex='Bye, Sam! See you around!', exp='Despedida simpática entre vizinhos.', c='b')],
 expr_game=[
  dict(cue='Alguém acabou de se apresentar para você.', opts=['Nice to meet you.', 'See you around!', 'Are you hungry?'], ans=0, why='Nice to meet you é o que se diz ao conhecer alguém.'),
  dict(cue='Você quer saber se a pessoa mudou há pouco.', opts=['Are you new here?', 'Welcome back!', 'Do you like tacos?'], ans=0, why='Are you new here? pergunta se a pessoa é nova no lugar.'),
  dict(cue='Você vai embora e quer se despedir do vizinho.', opts=['Nice to meet you.', 'See you around!', 'I live in 4B.'], ans=1, why='See you around! é uma despedida informal.')])
