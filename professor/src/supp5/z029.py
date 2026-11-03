"""Bloco de verbos e expressões da aula 29: pedir comida vegetariana."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('grill', '🥗', 'grelhar', ('grill', 'I grill veggies for dinner.', 'Eu grelho legumes no jantar.'), ('grills', 'The chef grills vegetables.', 'O chef grelha legumes.'), ('grilled', 'He grilled the corn.', 'Ele grelhou o milho.'), ('grilling', 'They are grilling mushrooms.', 'Estão grelhando cogumelos.'), 'Grilled vegetables = legumes grelhados; muito comum em cardápios.'),
  vb('mash', '🥔', 'amassar', ('mash', 'We mash chickpeas for the burger.', 'Nós amassamos grão-de-bico para o hambúrguer.'), ('mashes', 'The chef mashes beans.', 'O chef amassa feijão.'), ('mashed', 'He mashed the potatoes.', 'Ele amassou as batatas.'), ('mashing', 'She is mashing avocado.', 'Ela está amassando abacate.'), 'Com he/she/it, mash vira mashes (acrescenta -es).'),
  vb('hide', '🔍', 'esconder', ('hide', 'Some sauces hide meat.', 'Alguns molhos escondem carne.'), ('hides', 'This soup hides bacon.', 'Esta sopa esconde bacon.'), ('hid', 'They hid ham in the salad.', 'Eles esconderam presunto na salada.'), ('hiding', 'Is it hiding fish?', 'Está escondendo peixe?'), 'Irregular: hide, hid. Atenção ao ler os ingredientes.'),
  vb('choose', '👆', 'escolher', ('choose', 'I choose the pasta.', 'Eu escolho a massa.'), ('chooses', 'Eva chooses the salad.', 'A Eva escolhe a salada.'), ('chose', 'He chose the veggie burger.', 'Ele escolheu o hambúrguer vegetariano.'), ('choosing', 'I am choosing a soup.', 'Estou escolhendo uma sopa.'), 'Irregular: choose vira chose.'),
  vb('mean', '💬', 'significar / querer dizer', ('mean', 'I mean no fish.', 'Eu quero dizer sem peixe.'), ('means', 'Vegetarian means no meat.', 'Vegetariano significa sem carne.'), ('meant', 'She meant no eggs.', 'Ela quis dizer sem ovos.'), ('meaning', 'What are you meaning?', 'O que você quer dizer?'), 'Irregular: mean vira meant. What do you mean? esclarece uma dúvida.')],
 verb_game=[
  dict(scene='O chef grelha legumes para o jantar.', en='The chef ___ vegetables for dinner.', opts=['grill', 'grills', 'grilled'], ans=1, pt='O chef grelha legumes para o jantar.', why='“The chef” é ele/ela no presente: grills.'),
  dict(scene='O chef amassa feijão para o hambúrguer.', en='The chef ___ beans for the burger.', opts=['mash', 'mashes', 'mashing'], ans=1, pt='O chef amassa feijão para o hambúrguer.', why='“The chef” é ele/ela no presente: mashes.'),
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
