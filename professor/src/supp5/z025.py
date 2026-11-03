"""Bloco de verbos e expressões da aula 25: pedir fatias de pizza."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('grab', '🍕', 'pegar rápido', ('grab', 'I grab two slices.', 'Eu pego duas fatias.'), ('grabs', 'Jo grabs a napkin.', 'O Jo pega um guardanapo.'), ('grabbed', 'We grabbed a soda.', 'Nós pegamos um refrigerante.'), ('grabbing', 'I am grabbing a slice.', 'Estou pegando uma fatia.'), 'Grab é pegar algo rápido e informal. Dobra o b: grabbed, grabbing.'),
  vb('fold', '🛍️', 'dobrar', ('fold', 'I fold my slice in half.', 'Eu dobro minha fatia ao meio.'), ('folds', 'Jo folds her pizza.', 'A Jo dobra a pizza dela.'), ('folded', 'He folded the slice.', 'Ele dobrou a fatia.'), ('folding', 'I am folding my slice.', 'Estou dobrando minha fatia.'), 'Em NY, muita gente dobra a fatia para comer andando.'),
  vb('cost', '💲', 'custar', ('cost', 'Two slices cost eight dollars.', 'Duas fatias custam oito dólares.'), ('costs', 'A soda costs two dollars.', 'Um refrigerante custa dois dólares.'), ('cost', 'The pizza cost ten dollars.', 'A pizza custou dez dólares.'), ('costing', 'It is costing a lot.', 'Está custando muito.'), 'Irregular: cost é igual no passado (cost).'),
  vb('give', '🤝', 'dar', ('give', 'I give him ten dollars.', 'Eu dou dez dólares a ele.'), ('gives', 'He gives me the change.', 'Ele me dá o troco.'), ('gave', 'She gave me a napkin.', 'Ela me deu um guardanapo.'), ('giving', 'He is giving me a slice.', 'Ele está me dando uma fatia.'), 'Irregular: give vira gave.'),
  vb('pay', '💵', 'pagar', ('pay', 'I pay with cash.', 'Eu pago em dinheiro.'), ('pays', 'Jo pays first.', 'O Jo paga primeiro.'), ('paid', 'We paid ten dollars.', 'Nós pagamos dez dólares.'), ('paying', 'I am paying now.', 'Estou pagando agora.'), 'Passado: paid, não “payed”.')],
 verb_game=[
  dict(scene='Você pega duas fatias de pepperoni.', en='I ___ two slices of pepperoni.', opts=['grab', 'grabs', 'grabbed'], ans=0, pt='Eu pego duas fatias de pepperoni.', why='Com “I” o presente usa a forma base: grab.'),
  dict(scene='A soda grande custa dois dólares.', en='A large soda ___ two dollars.', opts=['cost', 'costs', 'costing'], ans=1, pt='Um refrigerante grande custa dois dólares.', why='“A soda” é ele/ela: costs.'),
  dict(scene='Ontem a Jo pagou dez dólares.', en='Jo ___ ten dollars yesterday.', opts=['pay', 'pays', 'paid'], ans=2, pt='A Jo pagou dez dólares ontem.', why='“Yesterday” pede passado: paid.'),
  dict(scene='O atendente está te dando o troco.', en='He is ___ me the change.', opts=['give', 'giving', 'gave'], ans=1, pt='Ele está me dando o troco.', why='“is” + -ing: giving.')],
 expressions=[
  dict(en='Two slices of pepperoni, please.', pt='Duas fatias de pepperoni, por favor.', ex='Two slices of pepperoni, please.', exp='Pedido direto na pizzaria.', c='a'),
  dict(en='Anything to drink?', pt='Algo para beber?', ex='Anything to drink? — A water, please.', exp='Pergunta do atendente sobre a bebida.', c='b'),
  dict(en='Small or large?', pt='Pequeno ou grande?', ex='Small or large? — Large.', exp='Pergunta sobre o tamanho.', c='c'),
  dict(en='How much is it?', pt='Quanto é?', ex='Large soda. How much is it?', exp='Para saber o preço.', c='d'),
  dict(en='Here you go.', pt='Aqui está.', ex='Here you go. Thanks!', exp='Ao entregar o dinheiro ou algo.', c='a'),
  dict(en='for here or to go', pt='para comer aqui ou levar', ex='One slice to go, please.', exp='Dizer se vai comer ali ou levar.', c='b')],
 expr_game=[
  dict(cue='Você quer saber o preço.', opts=['How much is it?', 'Small or large?', 'Here you go.'], ans=0, why='How much is it? pergunta o preço.'),
  dict(cue='Você entrega o dinheiro.', opts=['Anything to drink?', 'Here you go.', 'Large, please.'], ans=1, why='Here you go acompanha o que você entrega.'),
  dict(cue='Você quer uma água.', opts=['A water, please.', 'How much is it?', 'Two slices, please.'], ans=0, why='A water, please responde à pergunta da bebida.')])
