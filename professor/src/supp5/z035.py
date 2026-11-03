"""Bloco de verbos e expressões da aula 035: frutas por libra."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('look', '👀', 'parecer / olhar', ('look', 'These apples look good.', 'Estas maçãs parecem boas.'), ('looks', 'The fruit looks fresh.', 'A fruta parece fresca.'), ('looked', 'The grapes looked sweet.', 'As uvas pareciam doces.'), ('looking', 'I am looking at the oranges.', 'Estou olhando as laranjas.'), 'Look + adjetivo = parecer: looks good, looks fresh.'),
  vb('weigh', '⚖️', 'pesar', ('weigh', 'We weigh the fruit.', 'Nós pesamos a fruta.'), ('weighs', 'The box weighs two pounds.', 'A caixa pesa duas libras.'), ('weighed', 'He weighed the apples.', 'Ele pesou as maçãs.'), ('weighing', 'She is weighing the grapes.', 'Ela está pesando as uvas.'), 'Weigh serve para o vendedor e para o peso da fruta.'),
  vb('take', '🍎', 'levar', ('take', 'I take three pounds.', 'Eu levo três libras.'), ('takes', 'She takes two boxes.', 'Ela leva duas caixas.'), ('took', 'He took four apples.', 'Ele levou quatro maçãs.'), ('taking', 'I am taking the strawberries.', 'Estou levando os morangos.'), 'Irregular: take vira took. I’ll take… = vou levar…'),
  vb('pay', '💵', 'pagar', ('pay', 'I pay with cash.', 'Eu pago em dinheiro.'), ('pays', 'He pays twelve dollars.', 'Ele paga doze dólares.'), ('paid', 'She paid for the grapes.', 'Ela pagou pelas uvas.'), ('paying', 'I am paying now.', 'Estou pagando agora.'), 'Pay vira paid (não “payed”).'),
  vb('cost', '💲', 'custar', ('cost', 'Apples cost two dollars.', 'Maçãs custam dois dólares.'), ('costs', 'A box costs five dollars.', 'Uma caixa custa cinco dólares.'), ('cost', 'The grapes cost four dollars.', 'As uvas custaram quatro dólares.'), ('costing', 'Fruit is costing more now.', 'A fruta está custando mais agora.'), 'Cost não muda no passado: cost.')],
 verb_game=[
  dict(scene='Você acha as maçãs bonitas.', en='These apples ___ good.', opts=['look', 'looks', 'looking'], ans=0, pt='Estas maçãs parecem boas.', why='“These apples” é plural: look, sem -s.'),
  dict(scene='A caixa de morangos custa cinco dólares.', en='A box of strawberries ___ five dollars.', opts=['cost', 'costs', 'costing'], ans=1, pt='Uma caixa de morangos custa cinco dólares.', why='Sujeito singular (uma caixa) leva -s: costs.'),
  dict(scene='Ontem a Ana pagou doze dólares.', en='Yesterday Ana ___ twelve dollars.', opts=['pay', 'pays', 'paid'], ans=2, pt='Ontem a Ana pagou doze dólares.', why='“Yesterday” pede passado: paid.'),
  dict(scene='Você leva três libras de maçãs.', en='I’ll ___ three pounds, please.', opts=['take', 'took', 'taking'], ans=0, pt='Vou levar três libras, por favor.', why='Depois de “I’ll”, forma base: take.')],
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
