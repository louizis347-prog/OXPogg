"""Bloco de verbos e expressões da aula 036: combo de hambúrguer."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('stand', '🧍', 'ficar de pé', ('stand', 'I stand in line.', 'Eu fico na fila.'), ('stands', 'She stands at the counter.', 'Ela fica no balcão.'), ('stood', 'He stood in line.', 'Ele ficou na fila.'), ('standing', 'We are standing in line.', 'Estamos na fila.'), 'Irregular: stand vira stood. Stand in line = ficar na fila.'),
  vb('order', '🧾', 'pedir', ('order', 'We order a burger combo.', 'Nós pedimos um combo de hambúrguer.'), ('orders', 'Evan orders a cheeseburger.', 'O Evan pede um cheeseburger.'), ('ordered', 'I ordered a large Coke.', 'Eu pedi uma Coca grande.'), ('ordering', 'She is ordering now.', 'Ela está pedindo agora.'), 'Order serve para pedir comida; o passado só acrescenta -ed.'),
  vb('eat', '🍔', 'comer', ('eat', 'We eat burgers here.', 'Nós comemos hambúrguer aqui.'), ('eats', 'Evan eats his fries.', 'O Evan come a batata dele.'), ('ate', 'I ate a big burger.', 'Eu comi um hambúrguer grande.'), ('eating', 'I am eating lunch.', 'Estou almoçando.'), 'Eat vira ate no passado (irregular).'),
  vb('get', '🥤', 'pegar / pedir', ('get', 'I get a large drink.', 'Eu pego uma bebida grande.'), ('gets', 'She gets a milkshake.', 'Ela pega um milkshake.'), ('got', 'He got extra fries.', 'Ele pegou batata extra.'), ('getting', 'I am getting a shake.', 'Estou pegando um milkshake.'), 'Can I get…? é o jeito comum de pedir. Passado: got.'),
  vb('add', '➕', 'adicionar / acrescentar', ('add', 'I add a drink to the combo.', 'Eu acrescento uma bebida ao combo.'), ('adds', 'Evan adds cheese.', 'O Evan acrescenta queijo.'), ('added', 'She added a cookie.', 'Ela acrescentou um cookie.'), ('adding', 'I am adding fries.', 'Estou acrescentando batata.'), 'Add pode ser usado para pedir mais algo: Add a cookie, please.'),],
 verb_game=[
  dict(scene='Você fica na fila do caixa.', en='I ___ in line at the register.', opts=['stand', 'stands', 'stood'], ans=0, pt='Eu fico na fila do caixa.', why='Com “I” o presente fica na forma base: stand.'),
  dict(scene='Ontem você ficou na fila.', en='Yesterday I ___ in line.', opts=['stand', 'stood', 'standing'], ans=1, pt='Ontem eu fiquei na fila.', why='Passado irregular de stand: stood.'),
  dict(scene='O Evan pede um combo.', en='Evan ___ a burger combo.', opts=['order', 'orders', 'ordered'], ans=1, pt='O Evan pede um combo de hambúrguer.', why='Com “Evan” (ele) o presente leva -s: orders.'),
  dict(scene='Ela está pegando um milkshake agora.', en='She is ___ a milkshake.', opts=['get', 'gets', 'getting'], ans=2, pt='Ela está pegando um milkshake.', why='“is” + -ing: getting (o t dobra).')],
 expressions=[
  dict(en='What can I get you?', pt='O que posso trazer para você?', ex='Welcome! What can I get you?', exp='A pergunta do caixa.', c='a'),
  dict(en='Do you want a combo?', pt='Quer um combo?', ex='A burger? Do you want a combo?', exp='O caixa oferece burger + batata + bebida.', c='b'),
  dict(en='What comes with it?', pt='O que vem junto?', ex='What comes with the burger?', exp='Para saber o que o pedido inclui.', c='c'),
  dict(en='A cola, please.', pt='Uma cola, por favor.', ex='A combo and a cola, please.', exp='Para escolher a bebida.', c='d'),
  dict(en='for here or to go', pt='para comer aqui ou levar', ex='For here, please.', exp='Para dizer se você come aqui ou leva.', c='a'),
  dict(en='That’s it.', pt='É só isso.', ex='No, thanks. That’s it.', exp='Para encerrar o pedido.', c='b')],
 expr_game=[
  dict(cue='Você quer saber o que vem com o hambúrguer.', opts=['What comes with it?', 'That’s it.', 'A cola, please.'], ans=0, why='What comes with it? = o que vem junto?'),
  dict(cue='O caixa pergunta se quer mais alguma coisa; você não quer.', opts=['A cola, please.', 'No, thanks. That’s it.', 'Do you want a combo?'], ans=1, why='That’s it encerra o pedido.'),
  dict(cue='Você escolhe a bebida do combo.', opts=['A cola, please.', 'For here.', 'What can I get you?'], ans=0, why='Diga a bebida + please.')])
