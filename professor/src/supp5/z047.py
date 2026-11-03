"""Bloco de verbos e expressões da aula 47: comprar um cartão de transporte."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('buy', '🛒', 'comprar', ('buy', 'I buy a card.', 'Eu compro um cartão.'), ('buys', 'She buys a ticket.', 'Ela compra um bilhete.'), ('bought', 'He bought a card.', 'Ele comprou um cartão.'), ('buying', 'I am buying a card.', 'Estou comprando um cartão.'), 'Passado irregular: bought.'),
  vb('pay', '💳', 'pagar', ('pay', 'I pay at the machine.', 'Eu pago na máquina.'), ('pays', 'She pays with cash.', 'Ela paga em dinheiro.'), ('paid', 'He paid five dollars.', 'Ele pagou cinco dólares.'), ('paying', 'I am paying now.', 'Estou pagando agora.'), 'Atenção: pay vira paid (não “payed”).'),
  vb('read', '📖', 'ler', ('read', 'I read the sign.', 'Eu leio a placa.'), ('reads', 'She reads the price.', 'Ela lê o preço.'), ('read', 'He read the map.', 'Ele leu o mapa.'), ('reading', 'I am reading the sign.', 'Estou lendo a placa.'), 'No passado, read se escreve igual, mas se fala “red”.'),
  vb('put', '👆', 'colocar / pôr', ('put', 'I put the card on the reader.', 'Eu coloco o cartão no leitor.'), ('puts', 'She puts money on it.', 'Ela coloca dinheiro nele.'), ('put', 'He put the card away.', 'Ele guardou o cartão.'), ('putting', 'I am putting the card away.', 'Estou guardando o cartão.'), 'Put não muda no passado: put, put.'),
  vb('use', '🔄', 'usar', ('use', 'I use the card every day.', 'Eu uso o cartão todo dia.'), ('uses', 'Sam uses the reader.', 'O Sam usa o leitor.'), ('used', 'We used the machine.', 'Nós usamos a máquina.'), ('using', 'I am using cash.', 'Estou usando dinheiro.'), 'Use é regular: used, using.')],
 verb_game=[
 dict(scene='Você quer comprar um cartão.', en='I want to ___ a card.', opts=['buy', 'buys', 'bought'], ans=0, pt='Quero comprar um cartão.', why='Depois de “want to”, usa-se a forma base: buy.'),
 dict(scene='Ontem você pagou na máquina.', en='I ___ at the machine yesterday.', opts=['pay', 'paid', 'paying'], ans=1, pt='Eu paguei na máquina ontem.', why='“Yesterday” pede passado irregular: paid.'),
 dict(scene='A Ana coloca o cartão no leitor.', en='Ana ___ the card on the reader.', opts=['put', 'puts', 'putting'], ans=1, pt='A Ana coloca o cartão no leitor.', why='Ana (ela) leva -s: puts.'),
 dict(scene='Agora você está lendo a placa.', en='I am ___ the sign.', opts=['read', 'reads', 'reading'], ans=2, pt='Estou lendo a placa.', why='“am” + -ing: reading.')],
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
