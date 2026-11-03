"""Bloco de verbos e expressões da aula 033: na padaria."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('buy', '🛍️', 'comprar', ('buy', 'I buy bread here.', 'Eu compro pão aqui.'), ('buys', 'She buys two croissants.', 'Ela compra dois croissants.'), ('bought', 'He bought a cake.', 'Ele comprou um bolo.'), ('buying', 'I am buying cookies.', 'Estou comprando cookies.'), 'Irregular: buy vira bought (não “buyed”).'),
  vb('take', '🥖', 'levar', ('take', 'I take two loaves.', 'Eu levo dois pães.'), ('takes', 'She takes a cookie.', 'Ela leva um cookie.'), ('took', 'We took three croissants.', 'Nós levamos três croissants.'), ('taking', 'I am taking the cake.', 'Estou levando o bolo.'), 'I’ll take… é o jeito de dizer “vou levar”. Passado: took.'),
  vb('cost', '💲', 'custar', ('cost', 'These cookies cost two dollars.', 'Estes cookies custam dois dólares.'), ('costs', 'The cake costs ten dollars.', 'O bolo custa dez dólares.'), ('cost', 'The cookie cost two dollars.', 'O cookie custou dois dólares.'), ('costing', 'The bread is costing more today.', 'O pão está custando mais hoje.'), 'Cost não muda no passado: cost. Com ele/ela/coisa singular: costs.'),
  vb('help', '🙂', 'ajudar', ('help', 'We help every customer.', 'Nós ajudamos cada cliente.'), ('helps', 'The baker helps me.', 'O padeiro me ajuda.'), ('helped', 'She helped me today.', 'Ela me ajudou hoje.'), ('helping', 'He is helping a customer.', 'Ele está ajudando um cliente.'), 'Can I help you? é a pergunta clássica do atendente.'),
  vb('want', '🍪', 'querer', ('want', 'I want two cookies.', 'Eu quero dois cookies.'), ('wants', 'He wants a loaf.', 'Ele quer um pão.'), ('wanted', 'I wanted a croissant.', 'Eu queria um croissant.'), ('wanting', 'I am wanting a cake.', 'Estou querendo um bolo.'), 'I’ll take… e I’d like… soam mais educados que I want…')],
 verb_game=[
  dict(scene='Ontem você comprou um pão.', en='Yesterday I ___ a loaf of bread.', opts=['buy', 'bought', 'buying'], ans=1, pt='Ontem eu comprei um pão.', why='Passado de buy: bought.'),
  dict(scene='O bolo custa dez dólares.', en='The cake ___ ten dollars.', opts=['cost', 'costs', 'costing'], ans=1, pt='O bolo custa dez dólares.', why='“The cake” (ele/ela/coisa) leva -s: costs.'),
  dict(scene='Você decide levar dois croissants.', en='I’ll ___ two croissants.', opts=['take', 'took', 'takes'], ans=0, pt='Vou levar dois croissants.', why='Depois de “I’ll” vem a forma base: take.'),
  dict(scene='O padeiro atende um cliente agora.', en='The baker is ___ a customer.', opts=['help', 'helping', 'helps'], ans=1, pt='O padeiro está ajudando um cliente.', why='“is” + -ing: helping.')],
 expressions=[
  dict(en='How much is it?', pt='Quanto custa?', ex='How much is the bread?', exp='Para perguntar o preço de algo.', c='a'),
  dict(en='I’ll take…', pt='Vou levar…', ex='I’ll take two cookies, please.', exp='Para decidir o que comprar.', c='b'),
  dict(en='Anything else?', pt='Mais alguma coisa?', ex='Anything else? The cookies are fresh.', exp='O atendente pergunta isso depois do pedido.', c='c'),
  dict(en='That’s six dollars.', pt='Dá seis dólares.', ex='Two cookies? That’s six dollars.', exp='O atendente diz o total a pagar.', c='d'),
  dict(en='each', pt='cada / a unidade', ex='Four dollars each.', exp='Preço por unidade.', c='a'),
  dict(en='fresh', pt='fresco / fresquinho', ex='The bread is fresh today.', exp='Para dizer que algo acabou de ser feito.', c='b')],
 expr_game=[
  dict(cue='Você quer saber o preço do croissant.', opts=['How much is the croissant?', 'I’ll take two.', 'Anything else?'], ans=0, why='How much is…? pergunta o preço.'),
  dict(cue='Você decidiu levar dois pães.', opts=['How much is it?', 'I’ll take two loaves.', 'It is fresh.'], ans=1, why='I’ll take… = vou levar…'),
  dict(cue='O atendente quer saber se você quer mais alguma coisa.', opts=['Anything else?', 'Four dollars each.', 'Here you go.'], ans=0, why='Anything else? = mais alguma coisa?')])
