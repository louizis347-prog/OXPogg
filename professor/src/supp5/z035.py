"""Bloco de verbos e expressões da aula 035: frutas por libra."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('press', '👆', 'apertar', ('press', 'I press the avocado gently.', 'Eu aperto o abacate com cuidado.'), ('presses', 'She presses a peach.', 'Ela aperta um pêssego.'), ('pressed', 'He pressed the tomato.', 'Ele apertou o tomate.'), ('pressing', 'I am pressing the pear.', 'Estou apertando a pera.'), 'Press é apertar de leve para ver se a fruta está madura. Presses leva -es.'),
  vb('weigh', '⚖️', 'pesar', ('weigh', 'We weigh the fruit.', 'Nós pesamos a fruta.'), ('weighs', 'The box weighs two pounds.', 'A caixa pesa duas libras.'), ('weighed', 'He weighed the apples.', 'Ele pesou as maçãs.'), ('weighing', 'She is weighing the grapes.', 'Ela está pesando as uvas.'), 'Weigh serve para o vendedor e para o peso da fruta.'),
  vb('select', '✅', 'selecionar / escolher', ('select', 'I select the best apples.', 'Eu escolho as melhores maçãs.'), ('selects', 'She selects a few oranges.', 'Ela escolhe algumas laranjas.'), ('selected', 'He selected four pears.', 'Ele escolheu quatro peras.'), ('selecting', 'I am selecting grapes.', 'Estou escolhendo uvas.'), 'Select é um pouco mais formal que pick; passado regular.'),
  vb('swipe', '💳', 'passar o cartão', ('swipe', 'I swipe my card.', 'Eu passo meu cartão.'), ('swipes', 'He swipes his card.', 'Ele passa o cartão.'), ('swiped', 'She swiped her card.', 'Ela passou o cartão.'), ('swiping', 'I am swiping my card now.', 'Estou passando o cartão agora.'), 'Swipe your card = passe o cartão. Swipe perde o e no -ing.'),
  vb('rinse', '🚿', 'enxaguar', ('rinse', 'I rinse the grapes.', 'Eu enxáguo as uvas.'), ('rinses', 'She rinses the apples.', 'Ela enxágua as maçãs.'), ('rinsed', 'He rinsed the berries.', 'Ele enxaguou os morangos.'), ('rinsing', 'I am rinsing the pears.', 'Estou enxaguando as peras.'), 'Rinse é enxaguar rapidamente; regular, perde o e no -ing.')],
 verb_game=[
  dict(scene='Você aperta o abacate para ver se está maduro.', en='I ___ the avocado gently.', opts=['press', 'presses', 'pressing'], ans=0, pt='Eu aperto o abacate com cuidado.', why='Com “I” o presente fica na forma base: press.'),
  dict(scene='A Ana lava as uvas.', en='Ana ___ the grapes in the sink.', opts=['rinse', 'rinses', 'rinsed'], ans=1, pt='A Ana enxágua as uvas na pia.', why='Com “Ana” (ela) o presente leva -s: rinses.'),
  dict(scene='Ontem a Ana passou o cartão.', en='Yesterday Ana ___ her card.', opts=['swipe', 'swipes', 'swiped'], ans=2, pt='Ontem a Ana passou o cartão.', why='“Yesterday” pede passado: swiped.'),
  dict(scene='Você escolhe três libras de maçãs.', en='I ___ three pounds of apples.', opts=['select', 'selected', 'selecting'], ans=0, pt='Eu escolho três libras de maçãs.', why='Com “I” no presente: select.')],
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
