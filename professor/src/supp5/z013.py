"""Bloco de verbos e expressões da aula 013."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('lose', '😟', 'perder', ('lose', 'I lose my keys a lot.', 'Eu perco minhas chaves muito.'), ('loses', 'Tom loses his bag.', 'O Tom perde a mochila.'), ('lost', 'I lost my phone.', 'Eu perdi meu celular.'), ('losing', 'I am losing my bag!', 'Estou perdendo minha bolsa!'), 'Irregular: lose, lost.'),
  vb('find', '🔍', 'achar / encontrar', ('find', 'I find my bag.', 'Eu acho minha bolsa.'), ('finds', 'She finds a red jacket.', 'Ela acha uma jaqueta vermelha.'), ('found', 'I found your phone.', 'Eu achei seu celular.'), ('finding', 'I am finding my seat.', 'Estou achando meu lugar.'), 'Irregular: find, found.'),
  vb('leave', '🪑', 'deixar / esquecer', ('leave', 'I leave my bag here.', 'Eu deixo minha bolsa aqui.'), ('leaves', 'He leaves his jacket.', 'Ele deixa a jaqueta.'), ('left', 'I left it on the chair.', 'Eu deixei na cadeira.'), ('leaving', 'I am leaving now.', 'Estou saindo agora.'), 'Irregular: leave, left. Também significa “sair”.'),
  vb('belong', '🏷️', 'pertencer', ('belong', 'These keys belong to me.', 'Estas chaves são minhas.'), ('belongs', 'This bag belongs to Ana.', 'Esta bolsa é da Ana.'), ('belonged', 'It belonged to my dad.', 'Era do meu pai.'), ('belonging', 'Is it belonging to you?', 'Pertence a você?'), 'Belong to = ser de alguém. Quase nunca se usa com -ing.'),
  vb('take', '🎒', 'pegar / levar', ('take', 'I take my bag.', 'Eu levo minha bolsa.'), ('takes', 'Sam takes the red one.', 'O Sam pega a vermelha.'), ('took', 'She took my jacket.', 'Ela pegou minha jaqueta.'), ('taking', 'I am taking this one.', 'Estou levando este.'), 'Irregular: take, took.')],
 verb_game=[
  dict(scene='Você deixou o celular na cadeira.', en='I ___ my phone on the chair.', opts=['leave', 'left', 'leaving'], ans=1, pt='Eu deixei meu celular na cadeira.', why='Passado de leave: left.'),
  dict(scene='Uma pessoa achou a sua jaqueta.', en='She ___ my jacket by the door.', opts=['find', 'finds', 'found'], ans=2, pt='Ela achou minha jaqueta perto da porta.', why='Ação já feita: found.'),
  dict(scene='A bolsa azul é da Ana.', en='The blue bag ___ to Ana.', opts=['belong', 'belongs', 'belonging'], ans=1, pt='A bolsa azul é da Ana.', why='Com “bag” (it), o presente leva -s.'),
  dict(scene='Você está levando a bolsa vermelha.', en='I am ___ the red bag.', opts=['take', 'took', 'taking'], ans=2, pt='Estou levando a bolsa vermelha.', why='“am” + -ing: taking.')],
 expressions=[
  dict(en='Is this your bag?', pt='Esta é a sua bolsa?', ex='Excuse me, is this your bag?', exp='Para perguntar a um desconhecido.', c='a'),
  dict(en='Mine is blue.', pt='A minha é azul.', ex='No, mine is blue.', exp='Para dizer qual é a sua.', c='b'),
  dict(en='This one / That one', pt='Este / Aquele', ex='This one is red. That one is black.', exp='Perto = this; longe = that.', c='c'),
  dict(en='over there', pt='ali / lá', ex='My bag is over there.', exp='Para mostrar algo longe.', c='d'),
  dict(en='Excuse me', pt='Com licença', ex='Excuse me, is this seat free?', exp='Para chamar a atenção com educação.', c='a'),
  dict(en='Thank you so much!', pt='Muito obrigado!', ex='Yes, that’s mine. Thank you so much!', exp='Para agradecer de verdade.', c='b')],
 expr_game=[
  dict(cue='Você quer perguntar se a mochila é da pessoa.', opts=['Is this your bag?', 'Mine is blue.', 'Thank you so much!'], ans=0, why='Is this your…? pergunta de quem é.'),
  dict(cue='Você mostra qual é a sua bolsa, azul.', opts=['That one is far.', 'Mine is blue.', 'Is that yours?'], ans=1, why='Mine is… diz qual é a sua.'),
  dict(cue='Alguém achou seu celular e você agradece.', opts=['Excuse me.', 'Over there.', 'Thank you so much!'], ans=2, why='Thank you so much! agradece com ênfase.')])
