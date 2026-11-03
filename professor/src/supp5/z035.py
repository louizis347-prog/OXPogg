"""Bloco de verbos e expressões da aula 035: frutas por libra."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('pick', '🍎', 'escolher / pegar', ('pick', 'I pick the best apples.', 'Eu escolho as melhores maçãs.'), ('picks', 'Ana picks a ripe avocado.', 'A Ana escolhe um abacate maduro.'), ('picked', 'He picked three pears.', 'Ele escolheu três peras.'), ('picking', 'I am picking grapes.', 'Estou escolhendo uvas.'), 'Pick = escolher com a mão. Passado regular: picked.'),
  vb('buy', '🛍️', 'comprar', ('buy', 'I buy two pounds of grapes.', 'Eu compro duas libras de uvas.'), ('buys', 'She buys a melon.', 'Ela compra um melão.'), ('bought', 'He bought some bananas.', 'Ele comprou algumas bananas.'), ('buying', 'I am buying peaches.', 'Estou comprando pêssegos.'), 'Buy vira bought no passado (irregular).'),
  vb('put', '🧺', 'colocar / pôr', ('put', 'I put the fruit in a bag.', 'Eu coloco a fruta num saco.'), ('puts', 'Ana puts apples on the scale.', 'A Ana põe maçãs na balança.'), ('put', 'He put the pears in the cart.', 'Ele pôs as peras no carrinho.'), ('putting', 'I am putting grapes in a bag.', 'Estou colocando uvas num saco.'), 'Put não muda no passado: put, put. Dobra o t no -ing.'),
  vb('pay', '💳', 'pagar', ('pay', 'I pay by card.', 'Eu pago no cartão.'), ('pays', 'She pays at the register.', 'Ela paga no caixa.'), ('paid', 'He paid five dollars.', 'Ele pagou cinco dólares.'), ('paying', 'I am paying now.', 'Estou pagando agora.'), 'Pay vira paid (não “payed”) no passado.'),
  vb('wash', '🚿', 'lavar', ('wash', 'I wash the grapes.', 'Eu lavo as uvas.'), ('washes', 'Ana washes the apples.', 'A Ana lava as maçãs.'), ('washed', 'He washed the pears.', 'Ele lavou as peras.'), ('washing', 'I am washing the berries.', 'Estou lavando as frutinhas.'), 'Com he/she, wash vira washes (-es).'),],
 verb_game=[
  dict(scene='Você escolhe um abacate.', en='I ___ a ripe avocado.', opts=['pick', 'picks', 'picking'], ans=0, pt='Eu escolho um abacate maduro.', why='Com “I” o presente fica na forma base: pick.'),
  dict(scene='A Ana lava as uvas.', en='Ana ___ the grapes in the sink.', opts=['wash', 'washes', 'washed'], ans=1, pt='A Ana lava as uvas na pia.', why='Com “Ana” (ela) o presente leva -es: washes.'),
  dict(scene='Ontem a Ana pagou no caixa.', en='Yesterday Ana ___ at the register.', opts=['pay', 'pays', 'paid'], ans=2, pt='Ontem a Ana pagou no caixa.', why='“Yesterday” pede passado: paid.'),
  dict(scene='Você põe as maçãs no saco.', en='I ___ three apples in the bag.', opts=['put', 'puts', 'putting'], ans=0, pt='Eu coloco três maçãs no saco.', why='Com “I” o presente fica na forma base: put.')],
 expressions=[
  dict(en='two dollars a pound', pt='dois dólares a libra', ex='Apples are two dollars a pound.', exp='Forma comum de dizer o preço por peso.', c='a'),
  dict(en='I’ll take three pounds.', pt='Vou levar três libras.', ex='I’ll take three pounds, please.', exp='Para dizer a quantidade que você quer.', c='b'),
  dict(en='a box of…', pt='uma caixa de…', ex='A box of strawberries, please.', exp='Para pedir frutas vendidas em caixa.', c='c'),
  dict(en='They look fresh.', pt='Elas parecem frescas.', ex='These grapes look fresh.', exp='Para elogiar a qualidade da fruta.', c='d'),
  dict(en='Is that all?', pt='É só isso?', ex='Okay. Is that all?', exp='O vendedor pergunta antes de fechar a conta.', c='a'),
  dict(en='That’s twelve dollars.', pt='Dá doze dólares.', ex='Two boxes? That’s twelve dollars.', exp='O vendedor diz o total.', c='b')],
 expr_game=[
  dict(cue='Você quer saber se eles têm morangos.', opts=['Do you have strawberries?', 'Is that all?', 'Two dollars a pound.'], ans=0, why='Do you have…? pergunta se existe.'),
  dict(cue='Você quer três libras de laranja.', opts=['A box of oranges.', 'I’ll take three pounds.', 'They look fresh.'], ans=1, why='I’ll take… diz o que você leva.'),
  dict(cue='O vendedor diz o total.', opts=['That’s twelve dollars.', 'Do you have grapes?', 'I’ll take two.'], ans=0, why='That’s… dollars informa o total.')])
