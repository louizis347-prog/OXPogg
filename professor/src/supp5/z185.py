"""Bloco de verbos e expressões da aula 185: parque de cães."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('throw', '🎾', 'jogar, arremessar', ('throw', 'I throw the ball.', 'Eu jogo a bola.'), ('throws', 'Kim throws a stick.', 'A Kim joga um graveto.'), ('threw', 'He threw the ball far.', 'Ele jogou a bola longe.'), ('throwing', 'I am throwing the ball.', 'Estou jogando a bola.'), 'Passado irregular: throw vira threw.'),
  vb('pet', '🤚', 'fazer carinho', ('pet', 'I pet my dog.', 'Eu faço carinho no meu cachorro.'), ('pets', 'She pets Max.', 'Ela faz carinho no Max.'), ('petted', 'We petted the puppy.', 'Fizemos carinho no filhote.'), ('petting', 'He is petting Luna.', 'Ele está fazendo carinho na Luna.'), 'Pet dobra o t: petted, petting. Pergunte: Can I pet him?'),
  vb('feed', '🍖', 'alimentar', ('feed', 'We feed the dog.', 'Nós alimentamos o cachorro.'), ('feeds', 'Jonah feeds Luna.', 'O Jonah alimenta a Luna.'), ('fed', 'I fed him at six.', 'Eu o alimentei às seis.'), ('feeding', 'I am feeding him now.', 'Estou alimentando ele agora.'), 'Passado irregular: feed vira fed.'),
  vb('chase', '🏃', 'perseguir, correr atrás', ('chase', 'Dogs chase balls.', 'Cães correm atrás de bolas.'), ('chases', 'Max chases Luna.', 'O Max corre atrás da Luna.'), ('chased', 'He chased the ball.', 'Ele correu atrás da bola.'), ('chasing', 'They are chasing a stick.', 'Eles estão correndo atrás de um graveto.'), 'Chase termina em e: chased, chasing.'),
  vb('bark', '🔊', 'latir', ('bark', 'Small dogs bark a lot.', 'Cães pequenos latem muito.'), ('barks', 'Max barks at the ball.', 'O Max late para a bola.'), ('barked', 'He barked twice.', 'Ele latiu duas vezes.'), ('barking', 'Who is barking?', 'Quem está latindo?'), 'Bark é regular: barked, barking.')],
 verb_game=[
  dict(scene='A Kim joga o graveto agora.', en='Kim ___ a stick.', opts=['throw', 'throws', 'threw'], ans=1, pt='A Kim joga um graveto.', why='Com Kim (ela), o presente leva -s: throws.'),
  dict(scene='Ontem você alimentou o cachorro às seis.', en='Yesterday I ___ him at six.', opts=['feed', 'fed', 'feeding'], ans=1, pt='Ontem eu o alimentei às seis.', why='Yesterday pede passado: fed.'),
  dict(scene='O Max está correndo atrás da bola.', en='Max is ___ the ball.', opts=['chase', 'chases', 'chasing'], ans=2, pt='O Max está correndo atrás da bola.', why='Is + verbo termina em -ing: chasing.'),
  dict(scene='Cães pequenos latem muito.', en='Small dogs ___ a lot.', opts=['bark', 'barks', 'barked'], ans=0, pt='Cães pequenos latem muito.', why='Com dogs (plural), use a forma base: bark.')],
 expressions=[
  dict(en='What a cute dog!', pt='Que cachorro fofo!', ex='Hi! What a cute dog!', exp='Para elogiar um cachorro e puxar conversa.', c='a'),
  dict(en='How old is he?', pt='Quantos anos ele tem?', ex='How old is he? — He’s two.', exp='Pergunta natural sobre a idade.', c='b'),
  dict(en='Is he friendly?', pt='Ele é amigável?', ex='Is he friendly? — Very!', exp='Para saber se o cachorro é manso.', c='c'),
  dict(en='Good boy!', pt='Bom garoto!', ex='Good boy, Max!', exp='Elogio ao cachorro que se comporta bem.', c='d'),
  dict(en='walk the dog', pt='passear com o cachorro', ex='I walk the dog every morning.', exp='Rotina de quem tem cachorro.', c='a'),
  dict(en='Man’s best friend', pt='O melhor amigo do homem', ex='A dog is man’s best friend.', exp='Expressão comum para falar de cães.', c='b')],
 expr_game=[
  dict(cue='Você quer elogiar um cachorro.', opts=['What a cute dog!', 'How old is he?', 'Good boy!'], ans=0, why='What a cute dog! é o elogio.'),
  dict(cue='Você quer saber a idade do cachorro.', opts=['Is he friendly?', 'How old is he?', 'Walk the dog.'], ans=1, why='How old…? pergunta a idade.'),
  dict(cue='O cachorro obedeceu e você quer elogiar.', opts=['Good boy!', 'What a cute dog!', 'Is he friendly?'], ans=0, why='Good boy! elogia o comportamento.')])
