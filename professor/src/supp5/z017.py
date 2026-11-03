"""Bloco de verbos e expressões da aula 017."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('like', '👍', 'gostar', ('like', 'I like coffee.', 'Eu gosto de café.'), ('likes', 'Mia likes tea.', 'A Mia gosta de chá.'), ('liked', 'I liked the eggs.', 'Eu gostei dos ovos.'), ('liking', 'I am liking this juice!', 'Estou gostando deste suco!'), 'Em perguntas: Do you like…? / Does she like…?'),
  vb('eat', '🍳', 'comer', ('eat', 'I eat eggs and toast.', 'Eu como ovos e torrada.'), ('eats', 'Sam eats fruit.', 'O Sam come fruta.'), ('ate', 'We ate at eight.', 'Nós comemos às oito.'), ('eating', 'I am eating cereal.', 'Estou comendo cereal.'), 'Irregular: eat, ate.'),
  vb('drink', '🥤', 'beber', ('drink', 'I drink tea.', 'Eu bebo chá.'), ('drinks', 'Ana drinks juice.', 'A Ana bebe suco.'), ('drank', 'I drank milk.', 'Eu bebi leite.'), ('drinking', 'I am drinking water.', 'Estou bebendo água.'), 'Irregular: drink, drank.'),
  vb('love', '😍', 'adorar', ('love', 'I love toast.', 'Eu adoro torrada.'), ('loves', 'Tom loves eggs.', 'O Tom adora ovos.'), ('loved', 'She loved the cake.', 'Ela adorou o bolo.'), ('loving', 'I am loving this tea!', 'Estou adorando este chá!'), 'Mais forte que like.'),
  vb('make', '🍽️', 'fazer / preparar', ('make', 'I make breakfast.', 'Eu preparo o café da manhã.'), ('makes', 'Dad makes eggs.', 'O pai faz ovos.'), ('made', 'She made toast.', 'Ela fez torrada.'), ('making', 'I am making coffee.', 'Estou fazendo café.'), 'Irregular: make, made.')],
 verb_game=[
  dict(scene='O Tom adora ovos.', en='Tom ___ eggs.', opts=['love', 'loves', 'loved'], ans=1, pt='O Tom adora ovos.', why='Com “Tom”: loves.'),
  dict(scene='Ontem você bebeu leite.', en='I ___ milk yesterday.', opts=['drink', 'drinks', 'drank'], ans=2, pt='Eu bebi leite ontem.', why='Passado de drink: drank.'),
  dict(scene='Agora você faz café.', en='I am ___ coffee.', opts=['make', 'made', 'making'], ans=2, pt='Estou fazendo café.', why='“am” + -ing: making.'),
  dict(scene='Vocês comem ovos toda manhã.', en='We ___ eggs every morning.', opts=['eat', 'eats', 'ate'], ans=0, pt='Nós comemos ovos toda manhã.', why='Com “we”, forma base: eat.')],
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
