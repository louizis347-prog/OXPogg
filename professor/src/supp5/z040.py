"""Bloco de verbos e expressões da aula 040: pedido de pizza por telefone."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('dial', '☎️', 'discar', ('dial', 'I dial the pizza place.', 'Eu disco o número da pizzaria.'), ('dials', 'She dials Joe’s Pizza.', 'Ela disca para a pizzaria do Joe.'), ('dialed', 'He dialed at six.', 'Ele discou às seis.'), ('dialing', 'I am dialing the number.', 'Estou discando o número.'), 'Dial = discar. Em inglês americano: dialed, dialing.'),
  vb('order', '🍕', 'pedir', ('order', 'We order a large pizza.', 'Nós pedimos uma pizza grande.'), ('orders', 'Sam orders pepperoni.', 'O Sam pede pepperoni.'), ('ordered', 'I ordered a medium pizza.', 'Eu pedi uma pizza média.'), ('ordering', 'I am ordering takeout.', 'Estou pedindo para viagem.'), 'Passado regular: ordered.'),
  vb('pick up', '🛍️', 'retirar', ('pick up', 'I pick up the pizza at six.', 'Eu retiro a pizza às seis.'), ('picks up', 'He picks up the order.', 'Ele retira o pedido.'), ('picked up', 'She picked up the pizza.', 'Ela retirou a pizza.'), ('picking up', 'I am picking up my order.', 'Estou retirando meu pedido.'), 'Verbo frasal: pick up. Só o pick muda: picks up, picked up.'),
  vb('repeat', '🔁', 'repetir', ('repeat', 'I repeat my order.', 'Eu repito meu pedido.'), ('repeats', 'Chloe repeats the order.', 'A Chloe repete o pedido.'), ('repeated', 'She repeated my name.', 'Ela repetiu meu nome.'), ('repeating', 'I am repeating my number.', 'Estou repetindo meu número.'), 'Could you repeat that? = pode repetir?'),
  vb('confirm', '✅', 'confirmar', ('confirm', 'I confirm my order.', 'Eu confirmo meu pedido.'), ('confirms', 'Chloe confirms the total.', 'A Chloe confirma o total.'), ('confirmed', 'She confirmed my name.', 'Ela confirmou meu nome.'), ('confirming', 'I am confirming my number.', 'Estou confirmando meu número.'), 'Confirm é confirmar pedido, nome e telefone.')],
 verb_game=[
  dict(scene='Você disca para a pizzaria.', en='Hi, I am ___ to order a pizza.', opts=['dial', 'dials', 'dialing'], ans=2, pt='Oi, estou ligando para pedir uma pizza.', why='“am” + -ing: dialing (ou calling).'),
  dict(scene='A Chloe confirma o pedido.', en='Chloe ___ the order.', opts=['confirm', 'confirms', 'confirmed'], ans=1, pt='A Chloe confirma o pedido.', why='Com “Chloe” (ela) o presente leva -s: confirms.'),
  dict(scene='Ontem você pediu uma pizza média.', en='Yesterday I ___ a medium pizza.', opts=['order', 'orders', 'ordered'], ans=2, pt='Ontem eu pedi uma pizza média.', why='“Yesterday” pede passado: ordered.'),
  dict(scene='Ontem você repetiu seu número.', en='Yesterday I ___ my number.', opts=['repeat', 'repeats', 'repeated'], ans=2, pt='Ontem eu repeti meu número.', why='“Yesterday” pede passado: repeated.')],
 expressions=[
  dict(en='I’d like a pizza for takeout.', pt='Queria uma pizza para viagem.', ex='Hi. I’d like a large pizza for takeout.', exp='Para abrir o pedido por telefone.', c='a'),
  dict(en='What kind of pizza?', pt='Que tipo de pizza?', ex='What kind of pizza? — Pepperoni.', exp='O atendente pergunta o sabor.', c='b'),
  dict(en='half cheese, half pepperoni', pt='metade queijo, metade pepperoni', ex='Half cheese, half pepperoni, please.', exp='Para pedir uma pizza com dois sabores.', c='c'),
  dict(en='It’ll be thirty minutes.', pt='Vai levar trinta minutos.', ex='It’ll be thirty minutes.', exp='O atendente diz o tempo de espera.', c='d'),
  dict(en='My name is Sam.', pt='Meu nome é Sam.', ex='Great. My name is Sam.', exp='Para dar o nome do pedido.', c='a'),
  dict(en='pick up', pt='retirar', ex='I’ll pick up the pizza.', exp='Verbo frasal: buscar o pedido.', c='b')],
 expr_game=[
  dict(cue='Você quer pedir uma pizza grande para viagem.', opts=['I’d like a large pizza for takeout.', 'It’ll be thirty minutes.', 'My name is Sam.'], ans=0, why='I’d like… abre o pedido com educação.'),
  dict(cue='O atendente pergunta o nome para o pedido.', opts=['My name is Sam.', 'Half cheese, half pepperoni.', 'It’ll be thirty minutes.'], ans=0, why='My name is… dá o nome.'),
  dict(cue='Você quer metade queijo e metade pepperoni.', opts=['Half cheese, half pepperoni.', 'What kind of pizza?', 'I’ll pick up.'], ans=0, why='Half…, half… divide a pizza em dois sabores.')])
