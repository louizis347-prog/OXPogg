"""Bloco de verbos e expressões da aula 017."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('fry', '🍳', 'fritar', ('fry', 'I fry eggs.', 'Eu frito ovos.'), ('fries', 'Dad fries bacon.', 'O pai frita bacon.'), ('fried', 'She fried two eggs.', 'Ela fritou dois ovos.'), ('frying', 'I am frying eggs now.', 'Estou fritando ovos agora.'), 'Fry vira fries e fried (y vira i).'),
  vb('eat', '🍳', 'comer', ('eat', 'I eat eggs and toast.', 'Eu como ovos e torrada.'), ('eats', 'Sam eats fruit.', 'O Sam come fruta.'), ('ate', 'We ate at eight.', 'Nós comemos às oito.'), ('eating', 'I am eating cereal.', 'Estou comendo cereal.'), 'Irregular: eat, ate.'),
  vb('drink', '🥤', 'beber', ('drink', 'I drink tea.', 'Eu bebo chá.'), ('drinks', 'Ana drinks juice.', 'A Ana bebe suco.'), ('drank', 'I drank milk.', 'Eu bebi leite.'), ('drinking', 'I am drinking water.', 'Estou bebendo água.'), 'Irregular: drink, drank.'),
  vb('boil', '🥚', 'ferver', ('boil', 'I boil water for tea.', 'Eu fervo água para o chá.'), ('boils', 'Tom boils two eggs.', 'O Tom cozinha dois ovos.'), ('boiled', 'She boiled the eggs.', 'Ela cozinhou os ovos.'), ('boiling', 'I am boiling water.', 'Estou fervendo água.'), 'Boil an egg = cozinhar um ovo na água.'),
  vb('make', '🍽️', 'fazer / preparar', ('make', 'I make breakfast.', 'Eu preparo o café da manhã.'), ('makes', 'Dad makes eggs.', 'O pai faz ovos.'), ('made', 'She made toast.', 'Ela fez torrada.'), ('making', 'I am making coffee.', 'Estou fazendo café.'), 'Irregular: make, made.')],
 verb_game=[
  dict(scene='O Tom cozinha dois ovos na água.', en='Tom ___ two eggs.', opts=['boil', 'boils', 'boiled'], ans=1, pt='O Tom cozinha dois ovos.', why='Com “Tom”: boils.'),
  dict(scene='Ontem você bebeu leite.', en='I ___ milk yesterday.', opts=['drink', 'drinks', 'drank'], ans=2, pt='Eu bebi leite ontem.', why='Passado de drink: drank.'),
  dict(scene='Agora você faz café.', en='I am ___ coffee.', opts=['make', 'made', 'making'], ans=2, pt='Estou fazendo café.', why='“am” + -ing: making.'),
  dict(scene='Vocês fritam ovos toda manhã.', en='We ___ eggs every morning.', opts=['fry', 'fries', 'fried'], ans=0, pt='Nós fritamos ovos toda manhã.', why='Com “we”, forma base: fry.')],
 expressions=[
  dict(en='Do you like coffee?', pt='Você gosta de café?', ex='Do you like coffee?', exp='Para saber o gosto de alguém.', c='a'),
  dict(en='Yes, I do.', pt='Sim, gosto.', ex='Yes, I do. I like it with milk.', exp='Resposta curta afirmativa.', c='b'),
  dict(en='No, I don’t.', pt='Não, não gosto.', ex='No, I don’t. I like juice.', exp='Resposta curta negativa.', c='c'),
  dict(en='What do you like for breakfast?', pt='O que você gosta no café da manhã?', ex='What do you like for breakfast?', exp='Perguntar preferência de refeição.', c='d'),
  dict(en='Me too!', pt='Eu também!', ex='Me too! I love eggs.', exp='Para concordar.', c='a'),
  dict(en='with milk', pt='com leite', ex='I like it with milk.', exp='With + ingrediente.', c='b')],
 expr_game=[
  dict(cue='Você quer saber se a pessoa gosta de chá.', opts=['Do you like tea?', 'Yes, I do.', 'Me too!'], ans=0, why='Do you like…? pergunta o gosto.'),
  dict(cue='Você também ama ovos e concorda.', opts=['No, I don’t.', 'Me too!', 'With milk.'], ans=1, why='Me too! concorda.'),
  dict(cue='Você quer dizer que não gosta.', opts=['Yes, I do.', 'No, I don’t.', 'Do you like it?'], ans=1, why='No, I don’t. nega.')])
