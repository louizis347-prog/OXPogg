"""Bloco de verbos e expressões da aula 107: almoço com colegas."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('join', '🤝', 'juntar-se a', ('join', 'I join my team for lunch.', 'Eu me junto à equipe para almoçar.'), ('joins', 'Alex joins the group.', 'O Alex se junta ao grupo.'), ('joined', 'She joined us at noon.', 'Ela se juntou a nós ao meio-dia.'), ('joining', 'He is joining us today.', 'Ele está se juntando a nós hoje.'), 'Join não leva preposição: join us (não “join with us”).'),
  vb('meet', '👋', 'encontrar', ('meet', 'We meet in the lobby.', 'Nós nos encontramos no saguão.'), ('meets', 'Cole meets us at noon.', 'O Cole nos encontra ao meio-dia.'), ('met', 'I met Cole at the deli.', 'Eu encontrei o Cole na delicatessen.'), ('meeting', 'I am meeting my team.', 'Estou me encontrando com minha equipe.'), 'Passado irregular: meet vira met.'),
  vb('order', '🧾', 'pedir', ('order', 'I order a tuna sandwich.', 'Eu peço um sanduíche de atum.'), ('orders', 'Cole orders a salad.', 'O Cole pede uma salada.'), ('ordered', 'We ordered at the counter.', 'Nós pedimos no balcão.'), ('ordering', 'She is ordering soup.', 'Ela está pedindo sopa.'), 'Order serve para pedir comida num balcão ou mesa.'),
  vb('pick', '👆', 'escolher', ('pick', 'I pick the turkey.', 'Eu escolho o peru.'), ('picks', 'Alex picks a table.', 'O Alex escolhe uma mesa.'), ('picked', 'He picked tuna.', 'Ele escolheu atum.'), ('picking', 'I am picking a drink.', 'Estou escolhendo uma bebida.'), 'Pick é um jeito informal de dizer choose.'),
  vb('grab', '🥡', 'pegar rápido', ('grab', 'We grab lunch at noon.', 'Nós pegamos um almoço ao meio-dia.'), ('grabs', 'She grabs a napkin.', 'Ela pega um guardanapo.'), ('grabbed', 'I grabbed a sandwich.', 'Eu peguei um sanduíche.'), ('grabbing', 'He is grabbing a table.', 'Ele está pegando uma mesa.'), 'Grab lunch = comer algo rápido. Dobre o b: grabbed, grabbing.')],
 verb_game=[
  dict(scene='O Cole sempre encontra a equipe no saguão.', en='Cole ___ us in the lobby.', opts=['meet', 'meets', 'met'], ans=1, pt='O Cole nos encontra no saguão.', why='Com “Cole” (ele), o presente leva -s.'),
  dict(scene='Ontem você escolheu atum.', en='Yesterday I ___ tuna.', opts=['pick', 'picking', 'picked'], ans=2, pt='Ontem eu escolhi atum.', why='“Yesterday” pede passado: picked.'),
  dict(scene='Agora a Ana está pedindo sopa.', en='Ana is ___ soup.', opts=['order', 'orders', 'ordering'], ans=2, pt='A Ana está pedindo sopa.', why='“is” + verbo com -ing.'),
  dict(scene='Vocês se juntam ao grupo todo dia.', en='We ___ the team every day.', opts=['join', 'joins', 'joined'], ans=0, pt='Nós nos juntamos à equipe todo dia.', why='Com “we”, use a forma base: join.')],
 expressions=[
  dict(en='Do you want to…?', pt='Você quer…?', ex='Do you want to have lunch with us?', exp='Para convidar alguém.', c='a'),
  dict(en='I’d love to!', pt='Eu adoraria!', ex='Yes, I’d love to!', exp='Aceitar um convite com entusiasmo.', c='b'),
  dict(en='What’s good there?', pt='O que é bom lá?', ex='What’s good there? — The sandwiches.', exp='Pedir uma dica de comida.', c='c'),
  dict(en='I’ll have…', pt='Vou querer…', ex='I’ll have a turkey sandwich.', exp='Fazer o pedido.', c='d'),
  dict(en='Me too.', pt='Eu também.', ex='“I’ll have tuna.” — “Me too.”', exp='Dizer que você quer o mesmo.', c='a'),
  dict(en='before it’s crowded', pt='antes de ficar cheio', ex='Let’s go before it’s crowded.', exp='Sugerir sair cedo por causa da fila.', c='b')],
 expr_game=[
  dict(cue='Um colega convida você e você quer aceitar.', opts=['I’d love to!', 'Me too.', 'I’ll have tuna.'], ans=0, why='I’d love to! aceita um convite.'),
  dict(cue='Você quer decidir o seu prato no balcão.', opts=['What’s good there?', 'I’ll have a tuna sandwich.', 'Do you want to join us?'], ans=1, why='I’ll have… faz o pedido.'),
  dict(cue='Você quer sair antes da fila grande.', opts=['Let’s go before it’s crowded.', 'Me too.', 'What’s good there?'], ans=0, why='Sugestão para sair cedo.')])
