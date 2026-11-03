"""Bloco de verbos e expressões da aula 75: no shopping."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('shop', '🛍️', 'fazer compras', ('shop', 'We shop at the mall.', 'Nós fazemos compras no shopping.'), ('shops', 'Rosa shops on Saturday.', 'A Rosa faz compras no sábado.'), ('shopped', 'I shopped all day.', 'Eu fiz compras o dia todo.'), ('shopping', 'They are shopping now.', 'Eles estão fazendo compras agora.'), 'O -ing e o passado dobram o p: shopping, shopped. Go shopping = ir às compras.'),
  vb('spend', '💸', 'gastar', ('spend', 'I spend twenty dollars.', 'Eu gasto vinte dólares.'), ('spends', 'She spends a lot.', 'Ela gasta muito.'), ('spent', 'We spent a little.', 'Nós gastamos pouco.'), ('spending', 'He is spending too much.', 'Ele está gastando demais.'), 'Passado irregular: spend, spent.'),
  vb('save', '🐷', 'economizar / guardar', ('save', 'I save money.', 'Eu economizo dinheiro.'), ('saves', 'The sale saves ten dollars.', 'A promoção economiza dez dólares.'), ('saved', 'We saved fifteen dollars.', 'Nós economizamos quinze dólares.'), ('saving', 'I am saving for a jacket.', 'Estou juntando dinheiro para uma jaqueta.'), 'Save termina em e: saving, saved. Save money = economizar.'),
  vb('buy', '🛒', 'comprar', ('buy', 'I buy a bag.', 'Eu compro uma bolsa.'), ('buys', 'Rosa buys a red bag.', 'A Rosa compra uma bolsa vermelha.'), ('bought', 'She bought it on sale.', 'Ela a comprou em promoção.'), ('buying', 'I am buying a gift.', 'Estou comprando um presente.'), 'Passado irregular: buy, bought.'),
  vb('return', '↩️', 'devolver', ('return', 'You return the bag with a receipt.', 'Você devolve a bolsa com o recibo.'), ('returns', 'He returns the shoes.', 'Ele devolve os sapatos.'), ('returned', 'I returned the jacket.', 'Eu devolvi a jaqueta.'), ('returning', 'She is returning a bag.', 'Ela está devolvendo uma bolsa.'), 'Return também é “voltar”; na loja, é devolver a mercadoria.')],
 verb_game=[
  dict(scene='A Rosa comprou a bolsa em promoção ontem.', en='Yesterday Rosa ___ the bag on sale.', opts=['buy', 'buys', 'bought'], ans=2, pt='Ontem a Rosa comprou a bolsa em promoção.', why='“Yesterday” pede passado: bought (irregular).'),
  dict(scene='Nós gastamos pouco hoje.', en='Today we ___ only twenty dollars.', opts=['spend', 'spent', 'spending'], ans=1, pt='Hoje nós gastamos só vinte dólares.', why='A ação já terminou: spent (passado de spend).'),
  dict(scene='Agora elas estão fazendo compras.', en='They are ___ at the mall.', opts=['shop', 'shops', 'shopping'], ans=2, pt='Elas estão fazendo compras no shopping.', why='“are” + verbo termina em -ing: shopping (dobra o p).'),
  dict(scene='Ela sempre economiza dinheiro.', en='She always ___ money.', opts=['save', 'saves', 'saved'], ans=1, pt='Ela sempre economiza dinheiro.', why='Com “she” o presente leva -s: saves.')],
 expressions=[
  dict(en='How much is it?', pt='Quanto custa?', ex='How much is this bag?', exp='Para perguntar o preço.', c='a'),
  dict(en='Is it on sale?', pt='Está em promoção?', ex='Is the jacket on sale?', exp='Para saber se há desconto.', c='b'),
  dict(en='percent off', pt='por cento de desconto', ex='It is thirty percent off.', exp='Para dizer quanto é o desconto.', c='c'),
  dict(en='That\'s a good price.', pt='É um bom preço.', ex='Thirty-five dollars? That\'s a good price.', exp='Para elogiar um preço bom.', c='d'),
  dict(en='Cash or card?', pt='Dinheiro ou cartão?', ex='Cash or card? — Card, please.', exp='Pergunta do caixa sobre como pagar.', c='a'),
  dict(en='Maybe later.', pt='Talvez mais tarde.', ex='It\'s expensive. Maybe later.', exp='Para dizer, com educação, que você não compra agora.', c='b')],
 expr_game=[
  dict(cue='Você quer saber o preço da bolsa.', opts=['How much is it?', 'Cash or card?', 'Maybe later.'], ans=0, why='How much...? pergunta o preço.'),
  dict(cue='Você quer saber se a bolsa tem desconto.', opts=['Is it on sale?', 'That\'s a good price.', 'I\'ll take it.'], ans=0, why='On sale = em promoção.'),
  dict(cue='Está caro e você não quer comprar agora.', opts=['Maybe later.', 'Cash or card?', 'It\'s thirty percent off.'], ans=0, why='Maybe later é uma recusa educada.')])
