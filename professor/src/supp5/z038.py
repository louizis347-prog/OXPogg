"""Bloco de verbos e expressões da aula 038: pedir a conta."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('sign', '✍️', 'assinar', ('sign', 'I sign the receipt.', 'Eu assino o recibo.'), ('signs', 'She signs the check.', 'Ela assina a conta.'), ('signed', 'We signed the slip.', 'Nós assinamos o comprovante.'), ('signing', 'I am signing the receipt.', 'Estou assinando o recibo.'), 'Sign the receipt: assinar o comprovante do cartão.'),
  vb('return', '↩️', 'devolver', ('return', 'I return the pen.', 'Eu devolvo a caneta.'), ('returns', 'He returns my card.', 'Ele devolve meu cartão.'), ('returned', 'She returned the receipt.', 'Ela devolveu o recibo.'), ('returning', 'He is returning my card.', 'Ele está devolvendo meu cartão.'), 'Return = devolver (ou voltar); passado regular: returned.'),
  vb('split', '✂️', 'dividir', ('split', 'We split the check.', 'Nós dividimos a conta.'), ('splits', 'She splits the bill.', 'Ela divide a conta.'), ('split', 'They split it yesterday.', 'Eles a dividiram ontem.'), ('splitting', 'We are splitting the check.', 'Estamos dividindo a conta.'), 'Split não muda no passado: split. Com ele/ela: splits.'),
  vb('hand', '🤲', 'entregar', ('hand', 'I hand him my card.', 'Eu entrego meu cartão a ele.'), ('hands', 'She hands over the cash.', 'Ela entrega o dinheiro.'), ('handed', 'He handed me the pen.', 'Ele me entregou a caneta.'), ('handing', 'I am handing him my card.', 'Estou entregando meu cartão a ele.'), 'Hand + pessoa + coisa: hand him the card. Hand over = entregar.'),
  vb('review', '🔍', 'conferir', ('review', 'We review the check.', 'Nós conferimos a conta.'), ('reviews', 'He reviews the total.', 'Ele confere o total.'), ('reviewed', 'I reviewed the bill.', 'Eu conferi a conta.'), ('reviewing', 'We are reviewing the check.', 'Estamos conferindo a conta.'), 'Review aqui é conferir os itens antes de pagar.')],
 verb_game=[
  dict(scene='Você assina o recibo agora.', en='I am ___ the receipt.', opts=['sign', 'signs', 'signing'], ans=2, pt='Estou assinando o recibo.', why='“am” + -ing: signing.'),
  dict(scene='O garçom devolve o cartão.', en='The waiter ___ my card.', opts=['return', 'returns', 'returned'], ans=1, pt='O garçom devolve meu cartão.', why='Com “the waiter” (ele) o presente leva -s: returns.'),
  dict(scene='Vocês estão dividindo a conta.', en='We are ___ the check.', opts=['split', 'splits', 'splitting'], ans=2, pt='Estamos dividindo a conta.', why='“are” + -ing: splitting (o t dobra).'),
  dict(scene='Você entregou seu cartão ao garçom.', en='I ___ him my card.', opts=['hand', 'handed', 'hands'], ans=1, pt='Eu entreguei meu cartão a ele.', why='Passado regular de hand: handed.')],
 expressions=[
  dict(en='The check, please.', pt='A conta, por favor.', ex='Excuse me. The check, please.', exp='Para pedir a conta ao garçom.', c='a'),
  dict(en='Together or separate?', pt='Junto ou separado?', ex='Together or separate? — Together.', exp='O garçom pergunta como dividir a conta.', c='b'),
  dict(en='Can I pay by card?', pt='Posso pagar no cartão?', ex='Can I pay by card?', exp='Para saber se aceitam cartão.', c='c'),
  dict(en='cash', pt='dinheiro em espécie', ex='I’ll pay in cash.', exp='Para dizer que paga em dinheiro.', c='d'),
  dict(en='Keep the change.', pt='Pode ficar com o troco.', ex='Here is fifty dollars. Keep the change.', exp='Para deixar o troco como gorjeta.', c='a'),
  dict(en='Have a nice day!', pt='Tenha um bom dia!', ex='Thank you. Have a nice day!', exp='Despedida educada.', c='b')],
 expr_game=[
  dict(cue='Você quer pedir a conta.', opts=['The check, please.', 'Together, please.', 'Have a nice day!'], ans=0, why='The check, please = a conta, por favor.'),
  dict(cue='O garçom pergunta junto ou separado; vocês pagam juntos.', opts=['Together, please.', 'By card.', 'Keep the change.'], ans=0, why='Together = junto.'),
  dict(cue='Você quer saber se pode pagar com cartão.', opts=['Can I pay by card?', 'Keep the change.', 'The check, please.'], ans=0, why='Can I pay by…? pergunta a forma de pagamento.')])
