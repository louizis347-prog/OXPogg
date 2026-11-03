"""Bloco de verbos e expressões da aula 74: comprando sapatos."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('try', '🧪', 'experimentar / tentar', ('try', 'I try the shoes on.', 'Eu experimento os sapatos.'), ('tries', 'Evan tries a bigger size.', 'O Evan experimenta um número maior.'), ('tried', 'She tried the boots on.', 'Ela experimentou as botas.'), ('trying', 'He is trying a new pair.', 'Ele está experimentando um par novo.'), 'Try termina em y: tries, tried. Try on = provar.'),
  vb('tie', '🪢', 'amarrar', ('tie', 'I tie my shoes.', 'Eu amarro meus sapatos.'), ('ties', 'Evan ties the laces.', 'O Evan amarra os cadarços.'), ('tied', 'She tied her sneakers.', 'Ela amarrou os tênis.'), ('tying', 'He is tying his shoes.', 'Ele está amarrando os sapatos.'), 'Tie é especial: o -ing é tying (o ie vira y).'),
  vb('feel', '🤲', 'sentir / estar (sensação)', ('feel', 'The shoes feel great.', 'Os sapatos estão ótimos.'), ('feels', 'This pair feels tight.', 'Este par está apertado.'), ('felt', 'They felt small.', 'Eles pareciam pequenos.'), ('feeling', 'I am feeling good.', 'Estou me sentindo bem.'), 'Passado irregular: feel, felt. How do they feel? pergunta o conforto.'),
  vb('run', '🏃', 'correr', ('run', 'I run in the park.', 'Eu corro no parque.'), ('runs', 'Evan runs a few steps.', 'O Evan corre alguns passos.'), ('ran', 'We ran on Sunday.', 'Nós corremos no domingo.'), ('running', 'He is running in the store.', 'Ele está correndo na loja.'), 'Passado irregular: run, ran. O -ing dobra o n: running.'),
  vb('walk', '🚶', 'andar / caminhar', ('walk', 'You walk around the store.', 'Você anda pela loja.'), ('walks', 'Hank walks to the back.', 'O Hank vai até os fundos.'), ('walked', 'We walked to the shop.', 'Nós fomos a pé até a loja.'), ('walking', 'I am walking in new shoes.', 'Estou andando com sapatos novos.'), 'Walk around = andar de um lado para o outro (para testar).')],
 verb_game=[
  dict(scene='Agora o Evan está experimentando um par novo.', en='Evan is ___ a new pair.', opts=['try', 'trying', 'tries'], ans=1, pt='O Evan está experimentando um par novo.', why='“is” + verbo termina em -ing: trying.'),
  dict(scene='Ontem você correu no parque com os tênis.', en='Yesterday I ___ in the park.', opts=['run', 'runs', 'ran'], ans=2, pt='Ontem eu corri no parque.', why='“Yesterday” pede passado: ran (irregular).'),
  dict(scene='Este par aperta um pouco os pés.', en='This pair ___ a little tight.', opts=['feel', 'feels', 'felt'], ans=1, pt='Este par parece um pouco apertado.', why='“This pair” é singular: o presente leva -s: feels.'),
  dict(scene='Todo dia ela amarra os sapatos antes de sair.', en='She ___ her shoes before school.', opts=['tie', 'ties', 'tying'], ans=1, pt='Ela amarra os sapatos antes da escola.', why='Com “she” o presente leva -s: ties.')],
 expressions=[
  dict(en='What size?', pt='Que número?', ex='Hi! What size?', exp='Pergunta curta do vendedor sobre o tamanho.', c='a'),
  dict(en='Can I try them on?', pt='Posso experimentá-los?', ex='Can I try them on, please?', exp='Para pedir para provar os sapatos.', c='b'),
  dict(en='How do they feel?', pt='Como estão?', ex='How do they feel? Too tight?', exp='Para perguntar se os sapatos estão confortáveis.', c='c'),
  dict(en='A little tight', pt='um pouco apertado', ex='They are a little tight.', exp='Para dizer que o sapato aperta um pouco.', c='d'),
  dict(en='a pair of', pt='um par de', ex='I need a pair of boots.', exp='Para sapatos, meias e calças, que são pares.', c='a'),
  dict(en='Enjoy your shoes!', pt='Aproveite os sapatos!', ex='Great choice. Enjoy your shoes!', exp='Frase simpática do vendedor ao fim da compra.', c='b')],
 expr_game=[
  dict(cue='Você quer provar os sapatos.', opts=['Can I try them on?', 'What size?', 'Enjoy your shoes!'], ans=0, why='Try them on = provar os sapatos.'),
  dict(cue='Os sapatos estão apertando levemente.', opts=['A little tight.', 'How do they feel?', 'Size ten.'], ans=0, why='A little tight descreve o aperto leve.'),
  dict(cue='Você quer saber se os sapatos estão confortáveis.', opts=['How do they feel?', 'A pair of socks.', 'I need boots.'], ans=0, why='How do they feel? pergunta o conforto.')])
