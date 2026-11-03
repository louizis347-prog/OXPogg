"""Bloco de verbos e expressões da aula 29: pedir comida vegetariana."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('fry', '🍳', 'fritar', ('fry', 'I fry vegetables.', 'Eu frito legumes.'), ('fries', 'The chef fries onions.', 'O chef frita cebola.'), ('fried', 'He fried the beans.', 'Ele fritou o feijão.'), ('frying', 'I am frying potatoes.', 'Estou fritando batatas.'), 'Fry vira fries e fried (y vira ies/ied).'),
  vb('mix', '🥣', 'misturar', ('mix', 'We mix beans and rice.', 'Nós misturamos feijão e arroz.'), ('mixes', 'The chef mixes the beans.', 'O chef mistura o feijão.'), ('mixed', 'I mixed the sauce.', 'Eu misturei o molho.'), ('mixing', 'He is mixing the salad.', 'Ele está misturando a salada.'), 'Mix vira mixes na forma ele/ela.'),
  vb('use', '🔍', 'usar', ('use', 'We use no meat.', 'Nós não usamos carne.'), ('uses', 'This sauce uses milk.', 'Este molho usa leite.'), ('used', 'They used butter.', 'Eles usaram manteiga.'), ('using', 'I am using a fork.', 'Estou usando um garfo.'), 'Use perde o e antes de -ing: using.'),
  vb('choose', '👆', 'escolher', ('choose', 'I choose the pasta.', 'Eu escolho a massa.'), ('chooses', 'Eva chooses the salad.', 'A Eva escolhe a salada.'), ('chose', 'He chose the veggie burger.', 'Ele escolheu o hambúrguer vegetariano.'), ('choosing', 'I am choosing a soup.', 'Estou escolhendo uma sopa.'), 'Irregular: choose vira chose.'),
  vb('ask', '🙋', 'perguntar / pedir', ('ask', 'I ask for no meat.', 'Eu peço sem carne.'), ('asks', 'She asks about the sauce.', 'Ela pergunta sobre o molho.'), ('asked', 'He asked for beans.', 'Ele pediu feijão.'), ('asking', 'I am asking about the burger.', 'Estou perguntando sobre o hambúrguer.'), 'Ask about = perguntar sobre; ask for = pedir algo.'),
 verb_game=[
  dict(scene='O chef frita legumes para o jantar.', en='The chef ___ vegetables for dinner.', opts=['fry', 'fries', 'fried'], ans=1, pt='O chef frita legumes para o jantar.', why='“The chef” é ele/ela no presente: fries.'),
  dict(scene='O chef mistura feijão para o hambúrguer.', en='The chef ___ beans for the burger.', opts=['mix', 'mixes', 'mixing'], ans=1, pt='O chef mistura feijão para o hambúrguer.', why='“The chef” é ele/ela no presente: mixes.'),
  dict(scene='Ele escolheu o hambúrguer vegetariano.', en='He ___ the veggie burger.', opts=['chooses', 'chose', 'choosing'], ans=1, pt='Ele escolheu o hambúrguer vegetariano.', why='Passado irregular de choose: chose.'),
  dict(scene='Ela pergunta sobre o molho.', en='She ___ about the sauce.', opts=['ask', 'asks', 'asking'], ans=1, pt='Ela pergunta sobre o molho.', why='Com “she” o presente leva -s: asks.')],
 expressions=[
  dict(en='Do you have vegetarian dishes?', pt='Vocês têm pratos vegetarianos?', ex='Hi! Do you have vegetarian dishes?', exp='Para saber se há opção vegetariana.', c='a'),
  dict(en='Is there meat in it?', pt='Tem carne nisso?', ex='Is there meat in the soup?', exp='Para checar ingredientes.', c='b'),
  dict(en='I don’t eat meat or fish.', pt='Eu não como carne nem peixe.', ex='I don’t eat meat or fish.', exp='Explicar sua dieta.', c='c'),
  dict(en='No problem.', pt='Sem problema.', ex='No problem. We have a veggie burger too.', exp='Resposta simpática do atendente.', c='d'),
  dict(en='Just vegetables.', pt='Só legumes.', ex='No meat. Just vegetables.', exp='Dizer que só há legumes.', c='a'),
  dict(en='Good choice!', pt='Boa escolha!', ex='The pasta? Good choice!', exp='O atendente elogia seu pedido.', c='b')],
 expr_game=[
  dict(cue='Você quer saber se a sopa tem peixe.', opts=['Is there fish in it?', 'Good choice!', 'No problem.'], ans=0, why='Is there… in it? pergunta sobre ingredientes.'),
  dict(cue='Você explica que não come carne.', opts=['Just vegetables.', 'I don’t eat meat.', 'Good choice!'], ans=1, why='I don’t eat… explica sua dieta.'),
  dict(cue='Você quer saber se há opção vegetariana.', opts=['Do you have vegetarian dishes?', 'No problem.', 'Just vegetables.'], ans=0, why='Do you have…? pergunta por uma opção.')])
