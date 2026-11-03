"""Bloco de verbos e expressões da aula 29: pedir comida vegetariana."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('eat', '🥗', 'comer', ('eat', 'I don’t eat meat.', 'Eu não como carne.'), ('eats', 'Ana eats vegetables.', 'A Ana come legumes.'), ('ate', 'We ate the pasta.', 'Nós comemos a massa.'), ('eating', 'I am eating soup.', 'Estou comendo sopa.'), 'Passado irregular: ate.'),
  vb('have', '🍝', 'ter', ('have', 'We have a veggie burger.', 'Nós temos um hambúrguer vegetariano.'), ('has', 'The soup has no meat.', 'A sopa não tem carne.'), ('had', 'I had the pasta.', 'Eu comi a massa.'), ('having', 'I am having the soup.', 'Vou comer a sopa.'), 'have vira has com ele/ela e had no passado.'),
  vb('contain', '🔍', 'conter / ter', ('contain', 'Some dishes contain fish.', 'Alguns pratos contêm peixe.'), ('contains', 'This soup contains cheese.', 'Esta sopa contém queijo.'), ('contained', 'It contained eggs.', 'Continha ovos.'), ('containing', 'Is it containing dairy?', 'Está contendo laticínios?'), 'Contain é mais formal; Is there… in it? é mais comum.'),
  vb('choose', '👆', 'escolher', ('choose', 'I choose the pasta.', 'Eu escolho a massa.'), ('chooses', 'Eva chooses the salad.', 'A Eva escolhe a salada.'), ('chose', 'He chose the veggie burger.', 'Ele escolheu o hambúrguer vegetariano.'), ('choosing', 'I am choosing a soup.', 'Estou escolhendo uma sopa.'), 'Irregular: choose vira chose.'),
  vb('mean', '💬', 'significar / querer dizer', ('mean', 'I mean no fish.', 'Eu quero dizer sem peixe.'), ('means', 'Vegetarian means no meat.', 'Vegetariano significa sem carne.'), ('meant', 'She meant no eggs.', 'Ela quis dizer sem ovos.'), ('meaning', 'What are you meaning?', 'O que você quer dizer?'), 'Irregular: mean vira meant. What do you mean? esclarece uma dúvida.')],
 verb_game=[
  dict(scene='Você não come carne nem peixe.', en='I don’t ___ meat or fish.', opts=['eat', 'eats', 'ate'], ans=0, pt='Eu não como carne nem peixe.', why='Depois de “don’t” usamos a forma base: eat.'),
  dict(scene='A sopa não leva carne.', en='The soup ___ no meat.', opts=['have', 'has', 'had'], ans=1, pt='A sopa não tem carne.', why='“The soup” é ele/ela: has.'),
  dict(scene='Ele escolheu o hambúrguer vegetariano.', en='He ___ the veggie burger.', opts=['chooses', 'chose', 'choosing'], ans=1, pt='Ele escolheu o hambúrguer vegetariano.', why='Passado irregular de choose: chose.'),
  dict(scene='Você explica o que quer dizer.', en='Vegetarian ___ no meat.', opts=['mean', 'means', 'meant'], ans=1, pt='Vegetariano significa sem carne.', why='“Vegetarian” é ele/ela no presente: means.')],
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
