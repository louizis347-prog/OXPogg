"""Bloco de verbos e expressões da aula 28: fome e sede com um amigo."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('be', '🙋', 'ser / estar', ('am', 'I am hungry, and you are thirsty.', 'Eu estou com fome, e você está com sede.'), ('is', 'Leo is tired.', 'O Leo está cansado.'), ('was', 'I was hungry.', 'Eu estava com fome.'), ('being', 'I am being patient.', 'Estou sendo paciente.'), 'Em inglês fome e sede usam be: I am hungry. Com you/we/they: are. Passado: was / were.'),
  vb('need', '🆘', 'precisar', ('need', 'I need water.', 'Eu preciso de água.'), ('needs', 'Leo needs a snack.', 'O Leo precisa de um lanche.'), ('needed', 'We needed juice.', 'Nós precisávamos de suco.'), ('needing', 'I am needing a break.', 'Estou precisando de uma pausa.'), 'Need + coisa: I need water.'),
  vb('get', '🛒', 'pegar / buscar', ('get', 'I get the sandwiches.', 'Eu pego os sanduíches.'), ('gets', 'Mia gets the drinks.', 'A Mia pega as bebidas.'), ('got', 'We got an apple.', 'Nós pegamos uma maçã.'), ('getting', 'I am getting a juice.', 'Estou pegando um suco.'), 'I’ll get… oferece buscar algo. Passado: got.'),
  vb('buy', '💵', 'comprar', ('buy', 'I buy the sandwiches.', 'Eu compro os sanduíches.'), ('buys', 'Leo buys water.', 'O Leo compra água.'), ('bought', 'She bought two apples.', 'Ela comprou duas maçãs.'), ('buying', 'I am buying lunch.', 'Estou comprando o almoço.'), 'Irregular: buy vira bought.'),
  vb('share', '🤝', 'dividir', ('share', 'We share a snack.', 'Nós dividimos um lanche.'), ('shares', 'Mia shares her apple.', 'A Mia divide a maçã dela.'), ('shared', 'We shared a sandwich.', 'Nós dividimos um sanduíche.'), ('sharing', 'We are sharing a juice.', 'Estamos dividindo um suco.'), 'Termina em -e: shared, sharing.')],
 verb_game=[
  dict(scene='Você está com fome.', en='I ___ hungry.', opts=['am', 'is', 'are'], ans=0, pt='Eu estou com fome.', why='Com “I” usamos am.'),
  dict(scene='O Leo está com sede.', en='Leo ___ thirsty.', opts=['am', 'is', 'are'], ans=1, pt='O Leo está com sede.', why='Com “Leo” (ele) usamos is.'),
  dict(scene='Ontem a Mia comprou duas maçãs.', en='Mia ___ two apples yesterday.', opts=['buys', 'bought', 'buying'], ans=1, pt='A Mia comprou duas maçãs ontem.', why='Passado irregular de buy: bought.'),
  dict(scene='Você precisa de água.', en='I ___ water.', opts=['need', 'needs', 'needing'], ans=0, pt='Eu preciso de água.', why='Com “I” no presente: need.')],
 expressions=[
  dict(en='I’m hungry.', pt='Estou com fome.', ex='I’m hungry. Are you hungry?', exp='Dizer que está com fome.', c='a'),
  dict(en='I’m thirsty.', pt='Estou com sede.', ex='I’m so thirsty!', exp='Dizer que está com sede.', c='b'),
  dict(en='Let’s get a snack.', pt='Vamos pegar um lanche.', ex='Let’s get a snack.', exp='Sugerir comer algo juntos.', c='c'),
  dict(en='Do you want…?', pt='Você quer…?', ex='Do you want a sandwich?', exp='Oferecer algo.', c='d'),
  dict(en='I’ll get…', pt='Eu pego…', ex='I’ll get the sandwiches.', exp='Oferecer-se para buscar algo.', c='a'),
  dict(en='Good idea!', pt='Boa ideia!', ex='Good idea! Let’s go.', exp='Concordar com uma sugestão.', c='b')],
 expr_game=[
  dict(cue='Você sugere comer um lanche juntos.', opts=['Let’s get a snack.', 'I’m thirsty.', 'Good idea!'], ans=0, why='Let’s… sugere uma ação em grupo.'),
  dict(cue='Você se oferece para buscar os sanduíches.', opts=['I’ll get the sandwiches.', 'Do you want a sandwich?', 'I’m hungry.'], ans=0, why='I’ll get… é uma oferta.'),
  dict(cue='Seu amigo sugere almoçar e você concorda.', opts=['Let’s get lunch.', 'Good idea!', 'I’m thirsty.'], ans=1, why='Good idea! concorda com a sugestão.')])
