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
  vb('give', '🦴', 'dar', ('give', 'I give my dog water.', 'Eu dou água ao meu cachorro.'), ('gives', 'Ana gives her cat a treat.', 'A Ana dá um petisco ao gato.'), ('gave', 'She gave the dog food.', 'Ela deu comida ao cachorro.'), ('giving', 'I am giving him a treat.', 'Estou dando um petisco a ele.'), 'Passado irregular: give vira gave.'),
  vb('play', '🎾', 'brincar', ('play', 'We play with the ball.', 'Nós brincamos com a bola.'), ('plays', 'Max plays in the garden.', 'O Max brinca no jardim.'), ('played', 'He played all day.', 'Ele brincou o dia todo.'), ('playing', 'Max is playing now.', 'O Max está brincando agora.'), 'Play with + algo.'),
  vb('wash', '🛁', 'lavar', ('wash', 'I wash my dog on Sunday.', 'Eu lavo meu cachorro no domingo.'), ('washes', 'Ana washes her dog.', 'A Ana lava o cachorro dela.'), ('washed', 'He washed the dog.', 'Ele lavou o cachorro.'), ('washing', 'I am washing my dog.', 'Estou lavando meu cachorro.'), 'Com he/she/it, wash vira washes (-es).')],
 verb_game=[
  dict(scene='A Ana lava o cachorro todo domingo.', en='Ana ___ her dog every Sunday.', opts=['wash', 'washes', 'washed'], ans=1, pt='A Ana lava o cachorro dela todo domingo.', why='Com “Ana” (ela): washes (-es).'),
  dict(scene='Ontem ela deu comida ao cachorro.', en='She ___ the dog food yesterday.', opts=['give', 'gives', 'gave'], ans=2, pt='Ela deu comida ao cachorro ontem.', why='Passado de give: gave.'),
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
