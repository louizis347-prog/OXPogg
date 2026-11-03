"""Bloco de verbos e expressões da aula 28: fome e sede com um amigo."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('growl', '🙋', 'roncar / rosnar', ('growl', 'My stomach growls at noon.', 'Meu estômago ronca ao meio-dia.'), ('growls', 'His stomach growls loudly.', 'O estômago dele ronca alto.'), ('growled', 'My stomach growled in class.', 'Meu estômago roncou na aula.'), ('growling', 'My stomach is growling.', 'Meu estômago está roncando.'), 'Stomach growls = barriga roncando de fome.'),
  vb('gulp', '🥤', 'engolir / beber rápido', ('gulp', 'I gulp my water.', 'Eu bebo a água rápido.'), ('gulps', 'Leo gulps his juice.', 'O Leo bebe o suco rápido.'), ('gulped', 'She gulped down some water.', 'Ela bebeu água de um gole só.'), ('gulping', 'I am gulping my water.', 'Estou bebendo água rápido.'), 'Gulp down = beber ou engolir de uma vez, com sede.'),
  vb('head', '🛒', 'ir em direção a', ('head', 'I head to the kitchen.', 'Eu vou para a cozinha.'), ('heads', 'Mia heads to the store.', 'A Mia vai para a loja.'), ('headed', 'We headed to the café.', 'Nós fomos para o café.'), ('heading', 'We are heading to lunch.', 'Estamos indo almoçar.'), 'Head to + lugar = ir para lá; muito comum no dia a dia.'),
  vb('microwave', '♨️', 'esquentar no micro-ondas', ('microwave', 'I microwave my lunch.', 'Eu esquento meu almoço no micro-ondas.'), ('microwaves', 'Cole microwaves a burrito.', 'O Cole esquenta um burrito no micro-ondas.'), ('microwaved', 'She microwaved some soup.', 'Ela esquentou uma sopa no micro-ondas.'), ('microwaving', 'I am microwaving leftovers.', 'Estou esquentando sobras no micro-ondas.'), 'Microwave também é verbo: microwave the soup.'),
  vb('share', '🤝', 'dividir', ('share', 'We share a snack.', 'Nós dividimos um lanche.'), ('shares', 'Mia shares her apple.', 'A Mia divide a maçã dela.'), ('shared', 'We shared a sandwich.', 'Nós dividimos um sanduíche.'), ('sharing', 'We are sharing a juice.', 'Estamos dividindo um suco.'), 'Termina em -e: shared, sharing.')],
 verb_game=[
  dict(scene='Você está com fome.', en='I ___ hungry.', opts=['am', 'is', 'are'], ans=0, pt='Eu estou com fome.', why='Com “I” usamos am.'),
  dict(scene='O Leo está com sede.', en='Leo ___ thirsty.', opts=['am', 'is', 'are'], ans=1, pt='O Leo está com sede.', why='Com “Leo” (ele) usamos is.'),
  dict(scene='Ontem a Mia esquentou uma sopa no micro-ondas.', en='Mia ___ some soup yesterday.', opts=['microwaves', 'microwaved', 'microwaving'], ans=1, pt='A Mia esquentou uma sopa ontem.', why='“Yesterday” pede passado: microwaved.'),
  dict(scene='Você bebe água rápido porque está com sede.', en='I ___ my water.', opts=['gulp', 'gulps', 'gulping'], ans=0, pt='Eu bebo minha água rápido.', why='Com “I” no presente: gulp.')],
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
