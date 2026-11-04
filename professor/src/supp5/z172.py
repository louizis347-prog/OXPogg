"""Bloco de verbos e expressões da aula 172: o pedido errado."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('change', '🔁', 'trocar', ('change', 'I change my order.', 'Eu troco meu pedido.'), ('changes', 'Jonah changes the plate.', 'O Jonah troca o prato.'), ('changed', 'They changed my soup.', 'Eles trocaram minha sopa.'), ('changing', 'He is changing my plate.', 'Ele está trocando meu prato.'), 'Change também é troco e mudança. Passado regular: changed.'),
  vb('heat', '🔥', 'esquentar', ('heat', 'We heat the soup.', 'Nós esquentamos a sopa.'), ('heats', 'The cook heats the plate.', 'O cozinheiro esquenta o prato.'), ('heated', 'He heated my soup.', 'Ele esquentou minha sopa.'), ('heating', 'She is heating my soup.', 'Ela está esquentando minha sopa.'), 'Heat up = esquentar algo que esfriou.'),
  vb('replace', '♻️', 'substituir', ('replace', 'I replace the fish with chicken.', 'Eu troco o peixe por frango.'), ('replaces', 'Jonah replaces the plate.', 'O Jonah substitui o prato.'), ('replaced', 'They replaced my order.', 'Eles substituíram meu pedido.'), ('replacing', 'He is replacing my fork.', 'Ele está substituindo meu garfo.'), 'Replace X with Y = trocar X por Y. Perde o e final antes do -ing.'),
  vb('forget', '🤔', 'esquecer', ('forget', 'I forget the sauce.', 'Eu esqueço o molho.'), ('forgets', 'Jonah forgets my drink.', 'O Jonah esquece minha bebida.'), ('forgot', 'They forgot my soup.', 'Eles esqueceram minha sopa.'), ('forgetting', 'I am forgetting something.', 'Estou esquecendo algo.'), 'Forget é irregular: forgot no passado.'),
  vb('serve', '🍽️', 'servir', ('serve', 'We serve fish and chicken.', 'Nós servimos peixe e frango.'), ('serves', 'Jonah serves the soup.', 'O Jonah serve a sopa.'), ('served', 'They served the wrong plate.', 'Eles serviram o prato errado.'), ('serving', 'He is serving lunch.', 'Ele está servindo o almoço.'), 'Serve = servir comida. Passado regular: served.')],
 verb_game=[
  dict(scene='Ontem o garçom esqueceu seu molho.', en='Yesterday Jonah ___ my sauce.', opts=['forget', 'forgot', 'forgetting'], ans=1, pt='Ontem o Jonah esqueceu meu molho.', why='“Yesterday” pede passado irregular: forgot.'),
  dict(scene='Agora o garçom está trocando seu prato.', en='Jonah is ___ my plate.', opts=['change', 'changes', 'changing'], ans=2, pt='O Jonah está trocando meu prato.', why='“is” + verbo termina em -ing: changing.'),
  dict(scene='O cozinheiro esquenta a sopa.', en='The cook ___ the soup.', opts=['heat', 'heats', 'heated'], ans=1, pt='O cozinheiro esquenta a sopa.', why='Com o cozinheiro (ele), o presente leva -s: heats.'),
  dict(scene='O restaurante serve peixe todo dia.', en='We ___ fish every day.', opts=['serve', 'serves', 'serving'], ans=0, pt='Nós servimos peixe todo dia.', why='Com “we”, o presente fica na forma base: serve.')],
 expressions=[
  dict(en='On the house', pt='Por conta da casa', ex='The dessert is on the house.', exp='Quando o restaurante oferece algo de graça.', c='a'),
  dict(en='My mistake.', pt='Foi erro meu.', ex='My mistake. I will fix it.', exp='Para assumir o erro de forma curta e simpática.', c='b'),
  dict(en='I appreciate it.', pt='Agradeço.', ex='Thanks, I appreciate it.', exp='Para agradecer com um pouco mais de peso que thanks.', c='c'),
  dict(en='Hold on a sec.', pt='Espere um segundinho.', ex='Hold on a sec, I will check.', exp='Pedido informal para esperar um instante.', c='d'),
  dict(en='It’s all good.', pt='Está tudo bem.', ex='It’s all good. No problem.', exp='Para dizer que não há problema depois de um pedido de desculpas.', c='a'),
  dict(en='I think there’s a mistake.', pt='Acho que há um erro.', ex='Excuse me, I think there’s a mistake.', exp='Para avisar educadamente que algo está errado.', c='b')],
 expr_game=[
  dict(cue='O garçom pede desculpas e você quer dizer que está tudo bem.', opts=['It’s all good.', 'On the house.', 'Hold on a sec.'], ans=0, why='It’s all good aceita o pedido de desculpas.'),
  dict(cue='Você é o garçom e quer assumir o erro.', opts=['I appreciate it.', 'My mistake.', 'It’s all good.'], ans=1, why='My mistake = foi erro meu.'),
  dict(cue='O restaurante oferece a sobremesa de graça.', opts=['The dessert is on the house.', 'Hold on a sec.', 'I think there’s a mistake.'], ans=0, why='On the house = grátis, por conta da casa.')])
