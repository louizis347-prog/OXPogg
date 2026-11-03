"""Bloco de verbos e expressões da aula 040: pedido de pizza por telefone."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('call', '📞', 'ligar', ('call', 'I call the pizza place.', 'Eu ligo para a pizzaria.'), ('calls', 'She calls Joe’s Pizza.', 'Ela liga para a pizzaria do Joe.'), ('called', 'He called at six.', 'Ele ligou às seis.'), ('calling', 'I am calling to order.', 'Estou ligando para pedir.'), 'Call + lugar/pessoa. I’m calling to order = estou ligando para fazer um pedido.'),
  vb('order', '🍕', 'pedir', ('order', 'We order a large pizza.', 'Nós pedimos uma pizza grande.'), ('orders', 'Sam orders pepperoni.', 'O Sam pede pepperoni.'), ('ordered', 'I ordered a medium pizza.', 'Eu pedi uma pizza média.'), ('ordering', 'I am ordering takeout.', 'Estou pedindo para viagem.'), 'Passado regular: ordered.'),
  vb('pick up', '🛍️', 'retirar', ('pick up', 'I pick up the pizza at six.', 'Eu retiro a pizza às seis.'), ('picks up', 'He picks up the order.', 'Ele retira o pedido.'), ('picked up', 'She picked up the pizza.', 'Ela retirou a pizza.'), ('picking up', 'I am picking up my order.', 'Estou retirando meu pedido.'), 'Verbo frasal: pick up. Só o pick muda: picks up, picked up.'),
  vb('take', '⏱️', 'levar (tempo)', ('take', 'Pizzas take twenty minutes.', 'Pizzas levam vinte minutos.'), ('takes', 'It takes thirty minutes.', 'Leva trinta minutos.'), ('took', 'It took fifteen minutes.', 'Levou quinze minutos.'), ('taking', 'It is taking a long time.', 'Está demorando bastante.'), 'Irregular: take vira took. It takes… minutes = leva… minutos.'),
  vb('want', '🙋', 'querer', ('want', 'I want half cheese.', 'Eu quero metade queijo.'), ('wants', 'Sam wants a soda.', 'O Sam quer um refrigerante.'), ('wanted', 'I wanted a large pizza.', 'Eu queria uma pizza grande.'), ('wanting', 'I am wanting mushrooms.', 'Estou querendo cogumelos.'), 'No telefone, I’d like… soa mais educado que I want…')],
 verb_game=[
  dict(scene='Você liga para a pizzaria.', en='Hi, I am ___ to order a pizza.', opts=['call', 'calls', 'calling'], ans=2, pt='Oi, estou ligando para pedir uma pizza.', why='“am” + -ing: calling.'),
  dict(scene='A pizza demora vinte minutos.', en='It ___ twenty minutes.', opts=['take', 'takes', 'took'], ans=1, pt='Leva vinte minutos.', why='“It” (ele/ela) leva -s: takes.'),
  dict(scene='Ontem você pediu uma pizza média.', en='Yesterday I ___ a medium pizza.', opts=['order', 'orders', 'ordered'], ans=2, pt='Ontem eu pedi uma pizza média.', why='“Yesterday” pede passado: ordered.'),
  dict(scene='O Sam vai buscar a pizza às seis.', en='Sam ___ up the pizza at six.', opts=['pick', 'picks', 'picked'], ans=1, pt='O Sam retira a pizza às seis.', why='Presente com “Sam” leva -s: picks up.')],
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
