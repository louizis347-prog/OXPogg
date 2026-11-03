"""Bloco de verbos e expressões da aula 087: piquenique no parque."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('bring', '🎒', 'trazer / levar', ('bring', 'I bring a blanket.', 'Eu trago um cobertor.'), ('brings', 'Ravi brings cookies.', 'O Ravi traz biscoitos.'), ('brought', 'We brought sandwiches.', 'Nós trouxemos sanduíches.'), ('bringing', 'I am bringing juice.', 'Estou trazendo suco.'), 'Bring é irregular: brought no passado. Depois de did, volta para bring.'),
  vb('sit', '🪑', 'sentar', ('sit', 'We sit on the grass.', 'Nós sentamos na grama.'), ('sits', 'Lena sits under the tree.', 'A Lena senta debaixo da árvore.'), ('sat', 'They sat in the shade.', 'Eles sentaram na sombra.'), ('sitting', 'I am sitting on the blanket.', 'Estou sentado no cobertor.'), 'Sit é irregular: sat no passado. Dobra o t no -ing: sitting.'),
  vb('eat', '🥪', 'comer', ('eat', 'We eat lunch outside.', 'Nós almoçamos ao ar livre.'), ('eats', 'Ravi eats the chips.', 'O Ravi come os salgadinhos.'), ('ate', 'I ate a sandwich.', 'Eu comi um sanduíche.'), ('eating', 'Lena is eating fruit.', 'A Lena está comendo fruta.'), 'Eat é irregular: ate no passado.'),
  vb('pass', '🤲', 'passar (algo a alguém)', ('pass', 'Please pass the chips.', 'Por favor, passe os salgadinhos.'), ('passes', 'Lena passes the juice.', 'A Lena passa o suco.'), ('passed', 'He passed the cookies.', 'Ele passou os biscoitos.'), ('passing', 'I am passing the fruit.', 'Estou passando a fruta.'), 'Pass the… é o pedido simples à mesa: Pass the chips, please.'),
  vb('play', '⚽', 'brincar / jogar', ('play', 'Kids play on the grass.', 'As crianças brincam na grama.'), ('plays', 'The dog plays with a ball.', 'O cachorro brinca com uma bola.'), ('played', 'We played a game.', 'Nós jogamos um jogo.'), ('playing', 'They are playing catch.', 'Eles estão brincando de pegar a bola.'), 'Play serve para brincar e jogar. Passado regular: played.')],
 verb_game=[
  dict(scene='Hoje o Ravi trouxe biscoitos.', en='Ravi ___ cookies to the park.', opts=['bring', 'brings', 'brought'], ans=1, pt='O Ravi traz biscoitos para o parque.', why='Com “Ravi” (ele), o presente leva -s: brings.'),
  dict(scene='Ontem vocês trouxeram um cobertor.', en='Yesterday we ___ a blanket.', opts=['bring', 'brought', 'bringing'], ans=1, pt='Ontem nós trouxemos um cobertor.', why='“Yesterday” pede passado: brought.'),
  dict(scene='Agora a Lena está sentada na sombra.', en='Lena is ___ in the shade.', opts=['sit', 'sits', 'sitting'], ans=2, pt='A Lena está sentada na sombra.', why='“is” + verbo termina em -ing: sitting.'),
  dict(scene='Vocês comem o lanche no parque.', en='We ___ lunch in the park.', opts=['eat', 'eats', 'ate'], ans=0, pt='Nós almoçamos no parque.', why='Com “we”, o presente fica na forma base: eat.')],
 expressions=[
  dict(en='What’s in your bag?', pt='O que tem na sua bolsa?', ex='What’s in your bag? I’m hungry.', exp='Para perguntar o que alguém trouxe.', c='a'),
  dict(en='Did you bring…?', pt='Você trouxe…?', ex='Did you bring water?', exp='Para saber se alguém trouxe algo.', c='b'),
  dict(en='Let’s sit under that tree.', pt='Vamos sentar debaixo daquela árvore.', ex='It’s hot. Let’s sit under that tree.', exp='Para sugerir um lugar.', c='c'),
  dict(en='It’s shady.', pt='Tem sombra.', ex='Good idea. It’s shady here.', exp='Para dizer que o lugar tem sombra.', c='d'),
  dict(en='Pass the…, please.', pt='Passe o…, por favor.', ex='Pass the chips, please.', exp='Para pedir algo à mesa de forma educada.', c='a'),
  dict(en='Let’s eat!', pt='Vamos comer!', ex='Everything is ready. Let’s eat!', exp='Para convidar todos a começar a comer.', c='b')],
 expr_game=[
  dict(cue='Você quer saber se o amigo trouxe um cobertor.', opts=['Did you bring a blanket?', 'It’s shady.', 'Let’s eat!'], ans=0, why='Did you bring…? pergunta se trouxeram algo.'),
  dict(cue='O sol está forte e você quer outro lugar.', opts=['Pass the chips, please.', 'What’s in your bag?', 'Let’s sit under that tree.'], ans=2, why='Let’s sit… sugere onde sentar.'),
  dict(cue='Você quer os salgadinhos que estão longe de você.', opts=['Pass the chips, please.', 'Did you bring a blanket?', 'It’s shady.'], ans=0, why='Pass the…, please pede algo à mesa.')])
