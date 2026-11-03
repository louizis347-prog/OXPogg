"""Bloco de verbos e expressões da aula 141: pizzaria em Chicago."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('follow', '👣', 'seguir', ('follow', 'We follow the host.', 'Nós seguimos o recepcionista.'), ('follows', 'Nora follows him.', 'A Nora o segue.'), ('followed', 'We followed him to the table.', 'Nós o seguimos até a mesa.'), ('following', 'I am following you.', 'Estou seguindo você.'), 'Passado regular: followed.'),
  vb('wait', '⏳', 'esperar', ('wait', 'We wait for the pizza.', 'Nós esperamos a pizza.'), ('waits', 'Evan waits at the table.', 'O Evan espera na mesa.'), ('waited', 'We waited forty minutes.', 'Nós esperamos quarenta minutos.'), ('waiting', 'We are waiting for a table.', 'Estamos esperando uma mesa.'), 'Wait for = esperar por alguém ou algo.'),
  vb('bake', '🔥', 'assar', ('bake', 'They bake the pizza here.', 'Eles assam a pizza aqui.'), ('bakes', 'The pizza bakes in a pan.', 'A pizza assa numa forma.'), ('baked', 'The cook baked it slowly.', 'O cozinheiro a assou devagar.'), ('baking', 'The pizza is baking now.', 'A pizza está assando agora.'), 'Bake perde o e antes de -ing: baking.'),
  vb('split', '✂️', 'dividir', ('split', 'We split the pizza.', 'Nós dividimos a pizza.'), ('splits', 'Nora splits the soda.', 'A Nora divide o refrigerante.'), ('split', 'We split the bill.', 'Nós dividimos a conta.'), ('splitting', 'We are splitting a pizza.', 'Estamos dividindo uma pizza.'), 'O passado é igual ao presente: split. Dobra o t em splitting.'),
  vb('order', '📝', 'pedir (comida)', ('order', 'We order two sodas.', 'Nós pedimos dois refrigerantes.'), ('orders', 'Evan orders a pizza.', 'O Evan pede uma pizza.'), ('ordered', 'We ordered cheese.', 'Nós pedimos queijo.'), ('ordering', 'I am ordering now.', 'Estou pedindo agora.'), 'Order = pedir comida ou bebida num restaurante.')],
 verb_game=[
  dict(scene='Vocês esperam a pizza agora.', en='We are ___ for the pizza.', opts=['wait', 'waiting', 'waited'], ans=1, pt='Estamos esperando a pizza.', why='“are” + -ing: waiting.'),
  dict(scene='Ontem vocês dividiram uma pizza.', en='Yesterday we ___ a pizza.', opts=['split', 'splits', 'splitting'], ans=0, pt='Ontem nós dividimos uma pizza.', why='O passado de split é split.'),
  dict(scene='O Evan pede bebidas.', en='Evan ___ two sodas.', opts=['order', 'orders', 'ordered'], ans=1, pt='O Evan pede dois refrigerantes.', why='Ele (3ª pessoa) leva -s: orders.'),
  dict(scene='O recepcionista leva vocês; vocês vão atrás.', en='Please ___ me.', opts=['follow', 'follows', 'following'], ans=0, pt='Por favor, siga-me.', why='Pedido com verbo base: follow.')],
 expressions=[
  dict(en='A table for two, please.', pt='Uma mesa para dois, por favor.', ex='Hi. A table for two, please.', exp='Para pedir mesa ao chegar.', c='a'),
  dict(en='Follow me.', pt='Siga-me.', ex='Sure. Follow me.', exp='O anfitrião leva você à mesa.', c='b'),
  dict(en='It takes forty minutes.', pt='Leva quarenta minutos.', ex='The pizza takes forty minutes.', exp='Para dizer quanto algo demora.', c='c'),
  dict(en='We’re not in a hurry.', pt='Não temos pressa.', ex='Take your time. We’re not in a hurry.', exp='Para mostrar que pode esperar.', c='d'),
  dict(en='Two sodas, please.', pt='Dois refrigerantes, por favor.', ex='Two sodas, please. Thanks.', exp='Para pedir bebidas de forma curta.', c='a'),
  dict(en='That’s why they call it…', pt='Por isso chamam de…', ex='That’s why they call it the Windy City.', exp='Para explicar a origem de um apelido.', c='b')],
 expr_game=[
  dict(cue='Você quer dizer que pode esperar, sem correria.', opts=['We’re not in a hurry.', 'Follow me.', 'Two sodas, please.'], ans=0, why='Not in a hurry = sem pressa.'),
  dict(cue='Você chega e quer uma mesa para duas pessoas.', opts=['A table for two, please.', 'It takes forty minutes.', 'Follow me.'], ans=0, why='Pedido de mesa ao entrar.'),
  dict(cue='Você explica por que Chicago tem esse apelido.', opts=['That’s why they call it the Windy City.', 'Two sodas, please.', 'It takes forty minutes.'], ans=0, why='That’s why they call it… explica um nome.')])
