"""Bloco de verbos e expressões da aula 038: pedir a conta."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('pay', '💳', 'pagar', ('pay', 'I pay by card.', 'Eu pago no cartão.'), ('pays', 'He pays with cash.', 'Ele paga em dinheiro.'), ('paid', 'We paid together.', 'Nós pagamos juntos.'), ('paying', 'I am paying now.', 'Estou pagando agora.'), 'Pay vira paid (não “payed”).'),
  vb('bring', '🧾', 'trazer', ('bring', 'Please bring the check.', 'Por favor, traga a conta.'), ('brings', 'The waiter brings the check.', 'O garçom traz a conta.'), ('brought', 'She brought the bill.', 'Ela trouxe a conta.'), ('bringing', 'He is bringing my card.', 'Ele está trazendo meu cartão.'), 'Irregular: bring vira brought.'),
  vb('split', '✂️', 'dividir', ('split', 'We split the check.', 'Nós dividimos a conta.'), ('splits', 'She splits the bill.', 'Ela divide a conta.'), ('split', 'They split it yesterday.', 'Eles a dividiram ontem.'), ('splitting', 'We are splitting the check.', 'Estamos dividindo a conta.'), 'Split não muda no passado: split. Com ele/ela: splits.'),
  vb('give', '🤲', 'dar', ('give', 'I give him my card.', 'Eu dou meu cartão a ele.'), ('gives', 'She gives cash.', 'Ela dá dinheiro.'), ('gave', 'I gave him forty dollars.', 'Eu dei quarenta dólares a ele.'), ('giving', 'I am giving my card.', 'Estou dando meu cartão.'), 'Irregular: give vira gave.'),
  vb('need', '🙋', 'precisar', ('need', 'We need the check.', 'Nós precisamos da conta.'), ('needs', 'He needs change.', 'Ele precisa de troco.'), ('needed', 'I needed a receipt.', 'Eu precisei de um recibo.'), ('needing', 'We are needing the bill.', 'Estamos precisando da conta.'), 'I need… é direto; Can I have… soa mais educado.')],
 verb_game=[
  dict(scene='O garçom traz a conta agora.', en='The waiter ___ the check.', opts=['bring', 'brings', 'brought'], ans=1, pt='O garçom traz a conta.', why='Com “the waiter” (ele) o presente leva -s: brings.'),
  dict(scene='Ontem vocês pagaram juntos.', en='Yesterday we ___ together.', opts=['pay', 'paid', 'paying'], ans=1, pt='Ontem nós pagamos juntos.', why='“Yesterday” pede passado: paid.'),
  dict(scene='Vocês estão dividindo a conta.', en='We are ___ the check.', opts=['split', 'splits', 'splitting'], ans=2, pt='Estamos dividindo a conta.', why='“are” + -ing: splitting (o t dobra).'),
  dict(scene='Você deu seu cartão ao garçom.', en='I ___ him my card.', opts=['give', 'gave', 'gives'], ans=1, pt='Eu dei meu cartão a ele.', why='Passado irregular de give: gave.')],
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
