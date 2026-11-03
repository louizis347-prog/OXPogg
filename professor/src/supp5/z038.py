"""Bloco de verbos e expressões da aula 038: pedir a conta."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('pay', '💳', 'pagar', ('pay', 'I pay the check.', 'Eu pago a conta.'), ('pays', 'Ana pays with a card.', 'A Ana paga com cartão.'), ('paid', 'He paid in cash.', 'Ele pagou em dinheiro.'), ('paying', 'I am paying now.', 'Estou pagando agora.'), 'Pay vira paid (não “payed”) no passado.'),
  vb('give', '🤲', 'dar / entregar', ('give', 'I give him my card.', 'Eu dou meu cartão a ele.'), ('gives', 'The waiter gives me the check.', 'O garçom me dá a conta.'), ('gave', 'She gave him cash.', 'Ela deu dinheiro a ele.'), ('giving', 'I am giving him a card.', 'Estou dando um cartão a ele.'), 'Give vira gave no passado (irregular).'),
  vb('split', '✂️', 'dividir', ('split', 'We split the check.', 'Nós dividimos a conta.'), ('splits', 'She splits the bill.', 'Ela divide a conta.'), ('split', 'They split it yesterday.', 'Eles a dividiram ontem.'), ('splitting', 'We are splitting the check.', 'Estamos dividindo a conta.'), 'Split não muda no passado: split. Com ele/ela: splits.'),
  vb('bring', '🧾', 'trazer', ('bring', 'Please bring the check.', 'Por favor, traga a conta.'), ('brings', 'The waiter brings the check.', 'O garçom traz a conta.'), ('brought', 'He brought the card back.', 'Ele trouxe o cartão de volta.'), ('bringing', 'She is bringing the check.', 'Ela está trazendo a conta.'), 'Bring vira brought no passado (irregular).'),
  vb('call', '🙋', 'chamar / ligar', ('call', 'I call the waiter.', 'Eu chamo o garçom.'), ('calls', 'Ana calls the waiter.', 'A Ana chama o garçom.'), ('called', 'He called the waiter.', 'Ele chamou o garçom.'), ('calling', 'I am calling the waiter.', 'Estou chamando o garçom.'), 'Call serve para chamar alguém ou ligar para alguém.'),],
 verb_game=[
  dict(scene='Você paga a conta agora.', en='I am ___ the check.', opts=['pay', 'pays', 'paying'], ans=2, pt='Estou pagando a conta.', why='“am” + -ing: paying.'),
  dict(scene='O garçom me dá a conta.', en='The waiter ___ me the check.', opts=['give', 'gives', 'gave'], ans=1, pt='O garçom me dá a conta.', why='Com “the waiter” (ele) o presente leva -s: gives.'),
  dict(scene='Vocês estão dividindo a conta.', en='We are ___ the check.', opts=['split', 'splits', 'splitting'], ans=2, pt='Estamos dividindo a conta.', why='“are” + -ing: splitting (o t dobra).'),
  dict(scene='Ontem o garçom trouxe a conta.', en='Yesterday the waiter ___ the check.', opts=['bring', 'brought', 'brings'], ans=1, pt='Ontem o garçom trouxe a conta.', why='Passado irregular de bring: brought.')],
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
