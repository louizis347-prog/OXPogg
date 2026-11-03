"""Bloco de verbos e expressões da aula 036: combo de hambúrguer."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('get', '🍔', 'pegar / pedir', ('get', 'I get a cheeseburger.', 'Eu peço um cheeseburger.'), ('gets', 'She gets fries.', 'Ela pede batata frita.'), ('got', 'He got a cola.', 'Ele pediu uma cola.'), ('getting', 'I am getting a combo.', 'Estou pedindo um combo.'), 'What can I get you? é a pergunta do caixa. Passado: got.'),
  vb('want', '🙋', 'querer', ('want', 'I want a combo.', 'Eu quero um combo.'), ('wants', 'He wants ketchup.', 'Ele quer ketchup.'), ('wanted', 'She wanted lemonade.', 'Ela queria limonada.'), ('wanting', 'I am wanting fries.', 'Estou querendo batata frita.'), 'Do you want…? é a pergunta para escolher.'),
  vb('come', '🍟', 'vir / acompanhar', ('come', 'Fries come with the burger.', 'A batata frita vem com o hambúrguer.'), ('comes', 'A cola comes with the combo.', 'Uma cola vem com o combo.'), ('came', 'The burger came with fries.', 'O hambúrguer veio com batata.'), ('coming', 'Your order is coming now.', 'Seu pedido está chegando agora.'), 'Irregular: come vira came. Comes with = vem com.'),
  vb('add', '➕', 'adicionar', ('add', 'I add ketchup.', 'Eu adiciono ketchup.'), ('adds', 'He adds cheese.', 'Ele adiciona queijo.'), ('added', 'She added a cola.', 'Ela adicionou uma cola.'), ('adding', 'I am adding fries.', 'Estou adicionando batata frita.'), 'Add é útil para mudar o pedido: add fries.'),
  vb('eat', '😋', 'comer', ('eat', 'We eat here.', 'Nós comemos aqui.'), ('eats', 'She eats a burger.', 'Ela come um hambúrguer.'), ('ate', 'I ate fries.', 'Eu comi batata frita.'), ('eating', 'I am eating lunch.', 'Estou almoçando.'), 'Irregular: eat vira ate.')],
 verb_game=[
  dict(scene='O combo vem com batata e bebida.', en='The combo ___ with fries and a drink.', opts=['come', 'comes', 'came'], ans=1, pt='O combo vem com batata e bebida.', why='“The combo” (ele/ela) leva -s: comes.'),
  dict(scene='Ontem você comeu um hambúrguer.', en='Yesterday I ___ a burger.', opts=['eat', 'ate', 'eating'], ans=1, pt='Ontem eu comi um hambúrguer.', why='Passado irregular de eat: ate.'),
  dict(scene='Você quer um combo.', en='I ___ a combo, please.', opts=['want', 'wants', 'wanted'], ans=0, pt='Eu quero um combo, por favor.', why='Com “I” o presente fica na forma base: want.'),
  dict(scene='Ela está pedindo agora.', en='She is ___ a cheeseburger.', opts=['get', 'gets', 'getting'], ans=2, pt='Ela está pedindo um cheeseburger.', why='“is” + -ing: getting.')],
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
