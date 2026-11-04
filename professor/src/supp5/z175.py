"""Bloco de verbos e expressões da aula 175: autoatendimento."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('scan', '📟', 'escanear', ('scan', 'I scan each item.', 'Eu escaneio cada item.'), ('scans', 'Tom scans the bread.', 'O Tom escaneia o pão.'), ('scanned', 'She scanned the milk.', 'Ela escaneou o leite.'), ('scanning', 'I am scanning the cheese.', 'Estou escaneando o queijo.'), 'Scan dobra o n: scanned, scanning.'),
  vb('weigh', '⚖️', 'pesar', ('weigh', 'We weigh the apples.', 'Nós pesamos as maçãs.'), ('weighs', 'The scale weighs the lemons.', 'A balança pesa os limões.'), ('weighed', 'He weighed the bananas.', 'Ele pesou as bananas.'), ('weighing', 'I am weighing the apples.', 'Estou pesando as maçãs.'), 'Weigh tem o som de “wei”: igual a way. O gh é mudo.'),
  vb('press', '🔘', 'apertar', ('press', 'I press the blue button.', 'Eu aperto o botão azul.'), ('presses', 'Rosa presses the screen.', 'A Rosa aperta a tela.'), ('pressed', 'He pressed the wrong button.', 'Ele apertou o botão errado.'), ('pressing', 'I am pressing the button.', 'Estou apertando o botão.'), 'Press termina em -ss: com he/she vira presses.'),
  vb('lift', '🏋️', 'levantar, erguer', ('lift', 'I lift the heavy bag.', 'Eu levanto a sacola pesada.'), ('lifts', 'Tom lifts the box.', 'O Tom levanta a caixa.'), ('lifted', 'She lifted the cart.', 'Ela levantou o carrinho.'), ('lifting', 'I am lifting the bag.', 'Estou levantando a sacola.'), 'Lift = erguer algo do chão ou da mesa.'),
  vb('bag', '🛍️', 'ensacar', ('bag', 'I bag the lemons.', 'Eu coloco os limões na sacola.'), ('bags', 'Rosa bags the bread.', 'A Rosa coloca o pão na sacola.'), ('bagged', 'He bagged the apples.', 'Ele ensacou as maçãs.'), ('bagging', 'I am bagging the items.', 'Estou ensacando os itens.'), 'Bag também é substantivo (sacola). Como verbo, dobra o g.')],
 verb_game=[
  dict(scene='Agora o Tom está escaneando o pão.', en='Tom is ___ the bread.', opts=['scan', 'scans', 'scanning'], ans=2, pt='O Tom está escaneando o pão.', why='“is” + verbo termina em -ing: scanning.'),
  dict(scene='Ontem ele apertou o botão errado.', en='Yesterday he ___ the wrong button.', opts=['press', 'pressed', 'presses'], ans=1, pt='Ontem ele apertou o botão errado.', why='“Yesterday” pede passado: pressed.'),
  dict(scene='A Rosa coloca o pão na sacola.', en='Rosa ___ the bread.', opts=['bag', 'bags', 'bagged'], ans=1, pt='A Rosa coloca o pão na sacola.', why='Com Rosa (ela), o presente leva -s: bags.'),
  dict(scene='Vocês pesam as maçãs na tela.', en='We ___ the apples.', opts=['weigh', 'weighs', 'weighing'], ans=0, pt='Nós pesamos as maçãs.', why='Com “we”, o presente fica na forma base: weigh.')],
 expressions=[
  dict(en='Bag it.', pt='Ponha na sacola.', ex='Scan it and bag it.', exp='Instrução simples para ensacar um item.', c='a'),
  dict(en='Self-serve', pt='Autosserviço', ex='This is a self-serve line.', exp='Quando você mesmo faz o serviço, sem atendente.', c='b'),
  dict(en='Ring it up.', pt='Passe no caixa.', ex='Can you ring it up?', exp='Pedir a um caixa para registrar a compra.', c='c'),
  dict(en='Cash or card?', pt='Dinheiro ou cartão?', ex='Cash or card? — Card, please.', exp='Pergunta comum na hora de pagar.', c='d'),
  dict(en='How does this work?', pt='Como isso funciona?', ex='Excuse me, how does this work?', exp='Para pedir ajuda com uma máquina.', c='a'),
  dict(en='Unexpected item', pt='Item inesperado', ex='The screen says unexpected item.', exp='Aviso da máquina quando algo está fora do lugar.', c='b')],
 expr_game=[
  dict(cue='Você quer saber como a máquina funciona.', opts=['Ring it up.', 'How does this work?', 'Bag it.'], ans=1, why='How does this work? pede explicação.'),
  dict(cue='O caixa pergunta como você vai pagar.', opts=['Cash or card?', 'Bag it.', 'Self-serve.'], ans=0, why='Cash or card? é a pergunta de pagamento.'),
  dict(cue='Você quer pedir ao caixa que registre a compra.', opts=['Can you ring it up?', 'Unexpected item.', 'Self-serve.'], ans=0, why='Ring it up = registrar no caixa.')])
