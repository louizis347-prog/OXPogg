"""Bloco de verbos e expressões da aula 041: cozinhando em casa."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('stir', '🥄', 'mexer', ('stir', 'I stir the soup.', 'Eu mexo a sopa.'), ('stirs', 'He stirs the sauce.', 'Ele mexe o molho.'), ('stirred', 'She stirred the rice.', 'Ela mexeu o arroz.'), ('stirring', 'I am stirring the pot.', 'Estou mexendo a panela.'), 'Stir dobra o r: stirred, stirring.'),
  vb('cut', '🔪', 'cortar', ('cut', 'I cut the onions.', 'Eu corto as cebolas.'), ('cuts', 'She cuts a tomato.', 'Ela corta um tomate.'), ('cut', 'He cut the carrots.', 'Ele cortou as cenouras.'), ('cutting', 'I am cutting onions.', 'Estou cortando cebolas.'), 'Cut não muda no passado: cut. Com ele/ela: cuts.'),
  vb('whisk', '🥚', 'bater (ovos)', ('whisk', 'I whisk the eggs.', 'Eu bato os ovos.'), ('whisks', 'She whisks the cream.', 'Ela bate o creme.'), ('whisked', 'He whisked two eggs.', 'Ele bateu dois ovos.'), ('whisking', 'I am whisking now.', 'Estou batendo agora.'), 'Whisk é regular: whisked.'),
  vb('wash', '🚿', 'lavar', ('wash', 'I wash the tomatoes.', 'Eu lavo os tomates.'), ('washes', 'She washes the carrots.', 'Ela lava as cenouras.'), ('washed', 'He washed the pan.', 'Ele lavou a panela.'), ('washing', 'I am washing the knife.', 'Estou lavando a faca.'), 'Wash vira washes com ele/ela.'),
  vb('wipe', '🧽', 'limpar / passar pano', ('wipe', 'I wipe the table.', 'Eu limpo a mesa.'), ('wipes', 'He wipes the counter.', 'Ele limpa a bancada.'), ('wiped', 'She wiped the knife.', 'Ela limpou a faca.'), ('wiping', 'I am wiping the pan.', 'Estou limpando a panela.'), 'Wipe perde o e: wiping.')],
 verb_game=[
  dict(scene='Agora você corta as cebolas.', en='I am ___ the onions.', opts=['cut', 'cuts', 'cutting'], ans=2, pt='Estou cortando as cebolas.', why='“am” + -ing: cutting (o t dobra).'),
  dict(scene='Ontem você fez o jantar.', en='Yesterday I ___ dinner.', opts=['make', 'made', 'makes'], ans=1, pt='Ontem eu fiz o jantar.', why='Passado irregular de make: made.'),
  dict(scene='O Evan lava os tomates.', en='Evan ___ the tomatoes.', opts=['wash', 'washes', 'washed'], ans=1, pt='O Evan lava os tomates.', why='Com “Evan” o presente leva -es: washes.'),
  dict(scene='Vocês mexem a sopa devagar.', en='We ___ the soup slowly.', opts=['stir', 'stirs', 'stirred'], ans=0, pt='Nós mexemos a sopa devagar.', why='Com “we” o presente fica na forma base: stir.')],
 expressions=[
  dict(en='What are you making?', pt='O que você está fazendo?', ex='What are you making? — Soup.', exp='Para perguntar o que alguém cozinha.', c='a'),
  dict(en='Can I help?', pt='Posso ajudar?', ex='Can I help? — Sure.', exp='Para oferecer ajuda na cozinha.', c='b'),
  dict(en='Cut the onions, please.', pt='Corte as cebolas, por favor.', ex='Cut the onions, please.', exp='Para pedir uma tarefa com educação.', c='c'),
  dict(en='Careful! It’s hot.', pt='Cuidado! Está quente.', ex='Careful! The pan is hot.', exp='Para avisar de algo quente.', c='d'),
  dict(en='add salt', pt='adicionar sal', ex='Add salt, please.', exp='Instrução comum em receitas.', c='a'),
  dict(en='Is it ready?', pt='Está pronto?', ex='Is it ready? I’m hungry.', exp='Para perguntar se a comida está pronta.', c='b')],
 expr_game=[
  dict(cue='Você quer oferecer ajuda na cozinha.', opts=['Can I help?', 'Careful! It’s hot.', 'Is it ready?'], ans=0, why='Can I help? oferece ajuda.'),
  dict(cue='Você avisa que a panela está quente.', opts=['Careful! The pan is hot.', 'What are you making?', 'Cut the onions.'], ans=0, why='Careful! avisa de perigo.'),
  dict(cue='Você quer saber o que ele está cozinhando.', opts=['What are you making?', 'Add salt, please.', 'Is it ready?'], ans=0, why='What are you making? pergunta o prato.')])
