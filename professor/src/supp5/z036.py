"""Bloco de verbos e expressões da aula 036: combo de hambúrguer."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('stand', '🧍', 'ficar de pé', ('stand', 'I stand in line.', 'Eu fico na fila.'), ('stands', 'She stands at the counter.', 'Ela fica no balcão.'), ('stood', 'He stood in line.', 'Ele ficou na fila.'), ('standing', 'We are standing in line.', 'Estamos na fila.'), 'Irregular: stand vira stood. Stand in line = ficar na fila.'),
  vb('swap', '🔁', 'trocar', ('swap', 'I swap the fries for a salad.', 'Eu troco a batata por uma salada.'), ('swaps', 'He swaps the cola for water.', 'Ele troca a cola por água.'), ('swapped', 'She swapped the bun.', 'Ela trocou o pão.'), ('swapping', 'I am swapping my drink.', 'Estou trocando minha bebida.'), 'Swap A for B: trocar A por B. Dobra o p: swapped.'),
  vb('stack', '🍔', 'empilhar', ('stack', 'We stack the burgers.', 'Nós empilhamos os hambúrgueres.'), ('stacks', 'Malik stacks the tray.', 'O Malik arruma a bandeja.'), ('stacked', 'He stacked the boxes.', 'Ele empilhou as caixas.'), ('stacking', 'She is stacking the cups.', 'Ela está empilhando os copos.'), 'Stack é empilhar; passado regular: stacked.'),
  vb('supersize', '🍟', 'aumentar o tamanho', ('supersize', 'I supersize my fries.', 'Eu aumento minha batata para o maior tamanho.'), ('supersizes', 'He supersizes his drink.', 'Ele aumenta o tamanho da bebida.'), ('supersized', 'She supersized her combo.', 'Ela aumentou o tamanho do combo.'), ('supersizing', 'I am supersizing my cola.', 'Estou aumentando o tamanho da cola.'), 'Supersize é pedir o tamanho maior do combo; regular.'),
  vb('munch', '😋', 'mastigar / petiscar', ('munch', 'We munch on fries.', 'Nós petiscamos batata frita.'), ('munches', 'She munches on a burger.', 'Ela mastiga um hambúrguer.'), ('munched', 'I munched on nuggets.', 'Eu petisquei nuggets.'), ('munching', 'He is munching on fries.', 'Ele está petiscando batata frita.'), 'Munch on = comer algo com gosto e aos poucos. Munches leva -es.')],
 verb_game=[
  dict(scene='Você fica na fila do caixa.', en='I ___ in line at the register.', opts=['stand', 'stands', 'stood'], ans=0, pt='Eu fico na fila do caixa.', why='Com “I” o presente fica na forma base: stand.'),
  dict(scene='Ontem você ficou na fila.', en='Yesterday I ___ in line.', opts=['stand', 'stood', 'standing'], ans=1, pt='Ontem eu fiquei na fila.', why='Passado irregular de stand: stood.'),
  dict(scene='O Evan troca a batata por salada.', en='Evan ___ the fries for a salad.', opts=['swap', 'swaps', 'swapped'], ans=1, pt='O Evan troca a batata por salada.', why='Com “Evan” (ele) o presente leva -s: swaps.'),
  dict(scene='Ela está aumentando o tamanho agora.', en='She is ___ her combo.', opts=['supersize', 'supersizes', 'supersizing'], ans=2, pt='Ela está aumentando o tamanho do combo.', why='“is” + -ing: supersizing.')],
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
