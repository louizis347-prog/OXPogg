"""Bloco de verbos e expressões da aula 47: comprar um cartão de transporte."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('top up', '➕', 'recarregar', ('top up', 'I top up my card.', 'Eu recarrego meu cartão.'), ('tops up', 'She tops up her card.', 'Ela recarrega o cartão.'), ('topped up', 'He topped up twenty.', 'Ele recarregou vinte.'), ('topping up', 'I am topping up now.', 'Estou recarregando agora.'), 'Top up: o p dobra em topped/topping.'),
  vb('swipe', '💳', 'passar (cartão)', ('swipe', 'I swipe my card.', 'Eu passo meu cartão.'), ('swipes', 'He swipes the card.', 'Ele passa o cartão.'), ('swiped', 'She swiped twice.', 'Ela passou duas vezes.'), ('swiping', 'I am swiping it.', 'Estou passando o cartão.'), 'Swipe perde o e: swiping.'),
  vb('scan', '📷', 'escanear', ('scan', 'I scan the code.', 'Eu escaneio o código.'), ('scans', 'She scans the QR code.', 'Ela escaneia o QR code.'), ('scanned', 'He scanned his phone.', 'Ele escaneou o celular.'), ('scanning', 'I am scanning it.', 'Estou escaneando.'), 'Scan dobra o n: scanned, scanning.'),
  vb('tap', '👆', 'encostar / aproximar', ('tap', 'I tap my card.', 'Eu encosto meu cartão.'), ('taps', 'She taps the reader.', 'Ela encosta no leitor.'), ('tapped', 'He tapped the gate.', 'Ele encostou na catraca.'), ('tapping', 'I am tapping now.', 'Estou encostando agora.'), 'Tap = encostar de leve no leitor. Dobra o p: tapped.'),
  vb('use', '🔄', 'usar', ('use', 'I use the card every day.', 'Eu uso o cartão todo dia.'), ('uses', 'Sam uses the reader.', 'O Sam usa o leitor.'), ('used', 'We used the machine.', 'Nós usamos a máquina.'), ('using', 'I am using cash.', 'Estou usando dinheiro.'), 'Use é regular: used, using.')],
 verb_game=[
  dict(scene='Você quer recarregar o cartão.', en='I want to ___ my card.', opts=['top up', 'tops up', 'topped up'], ans=0, pt='Quero recarregar meu cartão.', why='Depois de “want to”, usa-se a forma base: top up.'),
  dict(scene='Ontem você passou o cartão duas vezes.', en='I ___ my card twice yesterday.', opts=['swipe', 'swiped', 'swiping'], ans=1, pt='Eu passei meu cartão duas vezes ontem.', why='“Yesterday” pede passado: swiped.'),
  dict(scene='A Ana encosta o cartão no leitor.', en='Ana ___ the reader.', opts=['tap', 'taps', 'tapping'], ans=1, pt='A Ana encosta no leitor.', why='Ana (ela) leva -s: taps.'),
  dict(scene='Agora você está escaneando o código.', en='I am ___ the code.', opts=['scan', 'scans', 'scanning'], ans=2, pt='Estou escaneando o código.', why='“am” + -ing: scanning (o n dobra).')],
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
