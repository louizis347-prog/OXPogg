"""Bloco de verbos e expressões da aula 47: comprar um cartão de transporte."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('add', '➕', 'adicionar / recarregar', ('add', 'I add twenty dollars.', 'Eu adiciono vinte dólares.'), ('adds', 'She adds ten dollars.', 'Ela adiciona dez dólares.'), ('added', 'He added thirty dollars.', 'Ele adicionou trinta dólares.'), ('adding', 'I am adding money.', 'Estou adicionando dinheiro.'), 'Add money = pôr crédito no cartão.'),
  vb('buy', '🛍️', 'comprar', ('buy', 'I buy a transit card.', 'Eu compro um cartão.'), ('buys', 'Tom buys a one-way ticket.', 'O Tom compra uma passagem.'), ('bought', 'We bought two tickets.', 'Nós compramos duas passagens.'), ('buying', 'I am buying a card.', 'Estou comprando um cartão.'), 'Irregular: buy vira bought.'),
  vb('pay', '💳', 'pagar', ('pay', 'I pay in cash.', 'Eu pago em dinheiro.'), ('pays', 'Ana pays by card.', 'A Ana paga no cartão.'), ('paid', 'He paid twenty dollars.', 'Ele pagou vinte dólares.'), ('paying', 'I am paying now.', 'Estou pagando agora.'), 'Irregular: pay vira paid.'),
  vb('tap', '👆', 'encostar / aproximar', ('tap', 'I tap my card.', 'Eu encosto meu cartão.'), ('taps', 'She taps the reader.', 'Ela encosta no leitor.'), ('tapped', 'He tapped the gate.', 'Ele encostou na catraca.'), ('tapping', 'I am tapping now.', 'Estou encostando agora.'), 'Tap = encostar de leve no leitor. Dobra o p: tapped.'),
  vb('use', '🔄', 'usar', ('use', 'I use the card every day.', 'Eu uso o cartão todo dia.'), ('uses', 'Sam uses the reader.', 'O Sam usa o leitor.'), ('used', 'We used the machine.', 'Nós usamos a máquina.'), ('using', 'I am using cash.', 'Estou usando dinheiro.'), 'Use é regular: used, using.')],
 verb_game=[
  dict(scene='Você quer pôr vinte dólares no cartão.', en='I want to ___ twenty dollars.', opts=['add', 'adds', 'added'], ans=0, pt='Quero adicionar vinte dólares.', why='Depois de “want to”, usa-se a forma base: add.'),
  dict(scene='Ontem você comprou dois bilhetes.', en='I ___ two tickets yesterday.', opts=['buy', 'bought', 'buying'], ans=1, pt='Eu comprei dois bilhetes ontem.', why='“Yesterday” pede passado: bought.'),
  dict(scene='A Ana encosta o cartão no leitor.', en='Ana ___ the reader.', opts=['tap', 'taps', 'tapping'], ans=1, pt='A Ana encosta no leitor.', why='Ana (ela) leva -s: taps.'),
  dict(scene='Agora você está pagando em dinheiro.', en='I am ___ in cash.', opts=['pay', 'pays', 'paying'], ans=2, pt='Estou pagando em dinheiro.', why='“am” + -ing: paying.')],
 expressions=[
  dict(en='I need a transit card.', pt='Preciso de um cartão de transporte.', ex='Hi! I need a transit card.', exp='Para pedir o cartão no guichê.', c='a'),
  dict(en='How much do you want to add?', pt='Quanto você quer adicionar?', ex='Sure. How much do you want to add?', exp='O atendente pergunta o valor da recarga.', c='b'),
  dict(en='Cash or card?', pt='Dinheiro ou cartão?', ex='Cash or card? — Card, please.', exp='Pergunta sobre a forma de pagamento.', c='c'),
  dict(en='Here you go.', pt='Aqui está.', ex='Cash? Here you go.', exp='Ao entregar algo a alguém.', c='d'),
  dict(en='Here’s your change.', pt='Aqui está seu troco.', ex='Here’s your change and your receipt.', exp='O atendente devolve o troco.', c='a'),
  dict(en='Tap it on the reader.', pt='Encoste no leitor.', ex='Tap it on the reader at the gate.', exp='Instrução para usar o cartão na catraca.', c='b')],
 expr_game=[
  dict(cue='O atendente pergunta como você vai pagar.', opts=['Cash or card?', 'Here’s your change.', 'Tap it on the reader.'], ans=0, why='Cash or card? pergunta a forma de pagamento.'),
  dict(cue='Você quer um cartão de transporte.', opts=['I need a transit card.', 'Here you go.', 'Have a nice day!'], ans=0, why='I need… pede o que você quer.'),
  dict(cue='Você entrega o dinheiro ao atendente.', opts=['Here you go.', 'How much?', 'Tap it.'], ans=0, why='Here you go acompanha a entrega.')])
