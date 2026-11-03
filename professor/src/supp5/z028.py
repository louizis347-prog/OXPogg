"""Bloco de verbos e expressões da aula 28: fome e sede com um amigo."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('feel', '😋', 'sentir-se', ('feel', 'I feel hungry at noon.', 'Eu me sinto com fome ao meio-dia.'), ('feels', 'She feels thirsty.', 'Ela se sente com sede.'), ('felt', 'We felt tired.', 'Nós nos sentimos cansados.'), ('feeling', 'I am feeling hungry.', 'Estou me sentindo com fome.'), 'Passado irregular: feel vira felt.'),
  vb('drink', '🥤', 'beber', ('drink', 'I drink water after class.', 'Eu bebo água depois da aula.'), ('drinks', 'Leo drinks juice.', 'O Leo bebe suco.'), ('drank', 'She drank a cold soda.', 'Ela bebeu um refrigerante gelado.'), ('drinking', 'I am drinking water.', 'Estou bebendo água.'), 'Passado irregular: drink vira drank.'),
  vb('walk', '🛒', 'andar / ir a pé', ('walk', 'I walk to the store.', 'Eu vou a pé até a loja.'), ('walks', 'Mia walks to the snack aisle.', 'A Mia vai a pé até o corredor de lanches.'), ('walked', 'We walked to the market.', 'Nós fomos a pé até o mercado.'), ('walking', 'I am walking to the store.', 'Estou indo a pé até a loja.'), 'Walk to + lugar: walk to the store.'),
  vb('cook', '🍲', 'cozinhar', ('cook', 'I cook soup at home.', 'Eu faço sopa em casa.'), ('cooks', 'Mia cooks rice.', 'A Mia cozinha arroz.'), ('cooked', 'She cooked some soup.', 'Ela cozinhou uma sopa.'), ('cooking', 'I am cooking dinner.', 'Estou cozinhando o jantar.'), 'Cook serve para cozinhar e para fazer uma refeição.'),
  vb('share', '🤝', 'dividir', ('share', 'We share a snack.', 'Nós dividimos um lanche.'), ('shares', 'Mia shares her apple.', 'A Mia divide a maçã dela.'), ('shared', 'We shared a sandwich.', 'Nós dividimos um sanduíche.'), ('sharing', 'We are sharing a juice.', 'Estamos dividindo um suco.'), 'Termina em -e: shared, sharing.')],
 verb_game=[
  dict(scene='Você está com fome.', en='I ___ hungry.', opts=['am', 'is', 'are'], ans=0, pt='Eu estou com fome.', why='Com “I” usamos am.'),
  dict(scene='O Leo está com sede.', en='Leo ___ thirsty.', opts=['am', 'is', 'are'], ans=1, pt='O Leo está com sede.', why='Com “Leo” (ele) usamos is.'),
  dict(scene='Ontem a Mia cozinhou uma sopa.', en='Mia ___ some soup yesterday.', opts=['cooks', 'cooked', 'cooking'], ans=1, pt='A Mia cozinhou uma sopa ontem.', why='“Yesterday” pede passado: cooked.'),
  dict(scene='Você bebe água porque está com sede.', en='I ___ my water.', opts=['drink', 'drinks', 'drank'], ans=0, pt='Eu bebo minha água.', why='Com “I” no presente: drink.')],
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
