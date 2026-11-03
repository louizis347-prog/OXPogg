"""Bloco de verbos e expressões da aula 016."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('love', '❤️', 'amar / adorar', ('love', 'I love dogs.', 'Eu adoro cachorros.'), ('loves', 'Max loves people.', 'O Max adora gente.'), ('loved', 'He loved the park.', 'Ele adorou o parque.'), ('loving', 'He is loving the park!', 'Ele está adorando o parque!'), 'Love é mais forte que like.'),
  vb('walk', '🦮', 'passear / andar', ('walk', 'I walk my dog.', 'Eu passeio com meu cachorro.'), ('walks', 'Ana walks Rex.', 'A Ana passeia com o Rex.'), ('walked', 'We walked in the park.', 'Nós passeamos no parque.'), ('walking', 'I am walking Max.', 'Estou passeando com o Max.'), 'Walk the dog = passear com o cachorro.'),
  vb('feed', '🥣', 'alimentar', ('feed', 'I feed my cat.', 'Eu dou comida ao meu gato.'), ('feeds', 'Tom feeds the fish.', 'O Tom alimenta os peixes.'), ('fed', 'She fed the dog.', 'Ela deu comida ao cachorro.'), ('feeding', 'I am feeding Luna.', 'Estou dando comida à Luna.'), 'Irregular: feed, fed.'),
  vb('play', '🎾', 'brincar', ('play', 'We play with the ball.', 'Nós brincamos com a bola.'), ('plays', 'Max plays in the garden.', 'O Max brinca no jardim.'), ('played', 'He played all day.', 'Ele brincou o dia todo.'), ('playing', 'Max is playing now.', 'O Max está brincando agora.'), 'Play with + algo.'),
  vb('brush', '🪮', 'escovar', ('brush', 'I brush my dog.', 'Eu escovo meu cachorro.'), ('brushes', 'Ana brushes Rex every day.', 'A Ana escova o Rex todo dia.'), ('brushed', 'He brushed the cat.', 'Ele escovou o gato.'), ('brushing', 'I am brushing Luna now.', 'Estou escovando a Luna agora.'), 'Com he/she: brushes (-es).')],
 verb_game=[
  dict(scene='A Ana escova o cachorro todo dia.', en='Ana ___ her dog every day.', opts=['brush', 'brushes', 'brushed'], ans=1, pt='A Ana escova o cachorro dela todo dia.', why='Com “Ana” (ela): brushes (-es).'),
  dict(scene='Ontem ela deu comida ao cachorro.', en='She ___ the dog yesterday.', opts=['feed', 'feeds', 'fed'], ans=2, pt='Ela deu comida ao cachorro ontem.', why='Passado de feed: fed.'),
  dict(scene='O Max está brincando agora.', en='Max is ___ now.', opts=['play', 'plays', 'playing'], ans=2, pt='O Max está brincando agora.', why='“is” + -ing: playing.'),
  dict(scene='Você passeia com o cachorro todo dia.', en='I ___ my dog every day.', opts=['walk', 'walks', 'walked'], ans=0, pt='Eu passeio com meu cachorro todo dia.', why='Com “I”, forma base: walk.')],
 expressions=[
  dict(en='What a cute dog!', pt='Que cachorro fofo!', ex='Look! What a cute dog!', exp='Elogio simpático.', c='a'),
  dict(en='What’s his name?', pt='Qual é o nome dele?', ex='What’s his name? — Max.', exp='Perguntar o nome do bicho.', c='b'),
  dict(en='How old is he?', pt='Quantos anos ele tem?', ex='How old is he? — He is five.', exp='Idade usa be, não have.', c='c'),
  dict(en='Does he like kids?', pt='Ele gosta de crianças?', ex='Does he like kids?', exp='Pergunta no presente com does.', c='d'),
  dict(en='Do you have a pet?', pt='Você tem um bicho de estimação?', ex='Do you have a pet?', exp='Puxar assunto.', c='a'),
  dict(en='He is very friendly.', pt='Ele é muito amigável.', ex='Yes, he is very friendly.', exp='Descrever o jeito do bicho.', c='b')],
 expr_game=[
  dict(cue='Você quer saber o nome do cachorro.', opts=['How old is he?', 'What’s his name?', 'What a cute dog!'], ans=1, why='What’s his name? pergunta o nome.'),
  dict(cue='Você elogia o cachorro.', opts=['What a cute dog!', 'Do you have a pet?', 'How old is he?'], ans=0, why='What a… elogia.'),
  dict(cue='Você quer saber a idade dele.', opts=['Does he like kids?', 'How old is he?', 'He is friendly.'], ans=1, why='How old…? pergunta a idade.')])
