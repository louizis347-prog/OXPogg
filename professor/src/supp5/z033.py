"""Bloco de verbos e expressões da aula 033: na padaria."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('pick', '👆', 'escolher / pegar', ('pick', 'I pick two croissants.', 'Eu escolho dois croissants.'), ('picks', 'She picks a cookie.', 'Ela escolhe um cookie.'), ('picked', 'He picked a small cake.', 'Ele escolheu um bolo pequeno.'), ('picking', 'I am picking a loaf.', 'Estou escolhendo um pão.'), 'Pick é escolher com a mão; passado regular: picked.'),
  vb('cut', '🔪', 'cortar', ('cut', 'We cut the bread.', 'Nós cortamos o pão.'), ('cuts', 'The baker cuts a loaf.', 'O padeiro corta um pão.'), ('cut', 'I cut the cake.', 'Eu cortei o bolo.'), ('cutting', 'He is cutting the bread.', 'Ele está cortando o pão.'), 'Cut não muda no passado: cut, cut, cut.'),
  vb('sell', '🏷️', 'vender', ('sell', 'We sell fresh bread.', 'Nós vendemos pão fresco.'), ('sells', 'The shop sells cookies.', 'A padaria vende cookies.'), ('sold', 'He sold the last loaf.', 'Ele vendeu o último pão.'), ('selling', 'They are selling cupcakes.', 'Estão vendendo cupcakes.'), 'Irregular: sell vira sold.'),
  vb('carry', '🛍️', 'carregar / levar', ('carry', 'I carry the bread home.', 'Eu levo o pão para casa.'), ('carries', 'She carries a big bag.', 'Ela leva uma sacola grande.'), ('carried', 'He carried the cake.', 'Ele levou o bolo.'), ('carrying', 'I am carrying two bags.', 'Estou levando duas sacolas.'), 'Carry vira carries e carried (y vira ies/ied).'),
  vb('bake', '🥖', 'assar', ('bake', 'We bake bread every day.', 'Nós assamos pão todo dia.'), ('bakes', 'The baker bakes cakes.', 'O padeiro assa bolos.'), ('baked', 'He baked a cake.', 'Ele assou um bolo.'), ('baking', 'I am baking bread.', 'Estou assando pão.'), 'Bake perde o e antes de -ing: baking.'),
 verb_game=[
  dict(scene='Ontem você escolheu um pão.', en='Yesterday I ___ a loaf of bread.', opts=['pick', 'picked', 'picking'], ans=1, pt='Ontem eu escolhi um pão.', why='Passado regular de pick: picked.'),
  dict(scene='A padaria vende bolo.', en='The bakery ___ cake.', opts=['sell', 'sells', 'sold'], ans=1, pt='A padaria vende bolo.', why='“The bakery” (ele/ela/coisa) leva -s: sells.'),
  dict(scene='Você pede para cortar o pão.', en='Can you ___ the bread, please?', opts=['cut', 'cuts', 'cutting'], ans=0, pt='Pode cortar o pão, por favor?', why='Depois de “can you” vem a forma base: cut.'),
  dict(scene='O padeiro leva um pedido agora.', en='The baker is ___ an order.', opts=['carry', 'carrying', 'carries'], ans=1, pt='O padeiro está levando um pedido.', why='“is” + -ing: carrying.')],
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
