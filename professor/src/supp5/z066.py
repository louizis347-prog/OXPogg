K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('try', '🪑', 'experimentar', ('try', 'I try the sofa.', 'Eu experimento o sofá.'), ('tries', 'Omar tries the chair.', 'O Omar experimenta a cadeira.'), ('tried', 'She tried the bed.', 'Ela experimentou a cama.'), ('trying', 'I am trying a new desk.', 'Estou experimentando uma escrivaninha nova.'), 'Try vira tries (y vira ies) e tried no passado.'),
  vb('sit', '🛋️', 'sentar', ('sit', 'We sit on the sofa.', 'Nós sentamos no sofá.'), ('sits', 'Omar sits down.', 'O Omar senta.'), ('sat', 'He sat for a minute.', 'Ele sentou por um minuto.'), ('sitting', 'I am sitting on a chair.', 'Estou sentado numa cadeira.'), 'Irregular: sit, sat. No -ing dobra o t: sitting.'),
  vb('look', '👀', 'olhar / procurar', ('look', 'We look at the lamps.', 'Nós olhamos os abajures.'), ('looks', 'She looks for a table.', 'Ela procura uma mesa.'), ('looked', 'I looked at the price.', 'Eu olhei o preço.'), ('looking', 'I am looking for a desk.', 'Estou procurando uma escrivaninha.'), 'Look at = olhar para. Look for = procurar.'),
  vb('deliver', '🚚', 'entregar', ('deliver', 'They deliver on Friday.', 'Eles entregam na sexta.'), ('delivers', 'The store delivers to my house.', 'A loja entrega na minha casa.'), ('delivered', 'They delivered the bed.', 'Eles entregaram a cama.'), ('delivering', 'The men are delivering the sofa.', 'Os homens estão entregando o sofá.'), 'Deliver é o verbo; delivery é o substantivo.'),
  vb('move', '📦', 'mover / mudar de lugar', ('move', 'We move the table.', 'Nós movemos a mesa.'), ('moves', 'He moves the lamp.', 'Ele move o abajur.'), ('moved', 'They moved the sofa.', 'Eles moveram o sofá.'), ('moving', 'I am moving a chair.', 'Estou movendo uma cadeira.'), 'Move perde o e antes de -ing: moving.')],
 verb_game=[
  dict(scene='Omar quer saber se o sofá é bom e senta nele.', en='Omar ___ on the sofa.', opts=['sit', 'sits', 'sat'], ans=1, pt='O Omar senta no sofá.', why='Com “Omar” (ele), o presente leva -s: sits.'),
  dict(scene='A loja entrega os móveis na sexta.', en='The store ___ on Friday.', opts=['deliver', 'delivers', 'delivering'], ans=1, pt='A loja entrega na sexta.', why='Com “the store” (ela), use delivers.'),
  dict(scene='Agora você procura uma mesa.', en='I am ___ for a table.', opts=['look', 'looks', 'looking'], ans=2, pt='Estou procurando uma mesa.', why='“am” + verbo termina em -ing: looking.'),
  dict(scene='Ontem ela experimentou uma cadeira.', en='Yesterday she ___ a chair.', opts=['try', 'tried', 'trying'], ans=1, pt='Ontem ela experimentou uma cadeira.', why='“Yesterday” pede passado: tried.')],
 expressions=[
  dict(en='I\'m looking for…', pt='Estou procurando…', ex='I\'m looking for a sofa.', exp='Para dizer ao vendedor o que você quer.', c='a'),
  dict(en='How much is this one?', pt='Quanto custa este?', ex='How much is this one? — It\'s four hundred dollars.', exp='Para perguntar o preço de algo que você está apontando.', c='b'),
  dict(en='so comfy', pt='tão confortável', ex='This sofa is so comfy.', exp='Jeito informal de elogiar um móvel ou uma cama.', c='c'),
  dict(en='a bit pricey', pt='meio caro', ex='It\'s a bit pricey.', exp='Para dizer, com educação, que o preço está alto.', c='d'),
  dict(en='look around', pt='dar uma olhada', ex='Let\'s look around first.', exp='Verbo frasal: ver a loja sem pressa antes de decidir.', c='a'),
  dict(en='I\'ll take it.', pt='Vou levar.', ex='It\'s perfect. I\'ll take it.', exp='Para decidir a compra na hora.', c='b')],
 expr_game=[
  dict(cue='Você acha o preço alto e quer ver outras opções.', opts=['I\'ll take it.', 'It\'s a bit pricey. Let\'s look around.', 'We deliver on Friday.'], ans=1, why='Dizer que está caro e que vai olhar mais é natural.'),
  dict(cue='Você já experimentou o sofá e quer comprar.', opts=['I\'m looking for a sofa.', 'How much is this one?', 'I\'ll take it.'], ans=2, why='I\'ll take it decide a compra.'),
  dict(cue='Você acabou de entrar e quer dizer o que procura.', opts=['I\'m looking for a desk.', 'It\'s so comfy.', 'Have a nice day.'], ans=0, why='I\'m looking for… começa a conversa.')])
