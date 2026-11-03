"""Bloco de verbos e expressões da aula 115: material escolar."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('carry', '🎒', 'carregar, levar', ('carry', 'I carry my backpack.', 'Eu carrego minha mochila.'), ('carries', 'Tom carries a big bag.', 'O Tom carrega uma sacola grande.'), ('carried', 'She carried two notebooks.', 'Ela carregou dois cadernos.'), ('carrying', 'I am carrying my books.', 'Estou carregando meus livros.'), 'Carry muda o y: carries, carried.'),
  vb('pick', '👆', 'escolher', ('pick', 'We pick two notebooks.', 'Nós escolhemos dois cadernos.'), ('picks', 'Lily picks a blue backpack.', 'A Lily escolhe uma mochila azul.'), ('picked', 'I picked a calculator.', 'Eu escolhi uma calculadora.'), ('picking', 'I am picking a color.', 'Estou escolhendo uma cor.'), 'Pick = escolher. Passado regular: picked.'),
  vb('count', '🔢', 'contar', ('count', 'I count ten pencils.', 'Eu conto dez lápis.'), ('counts', 'Rosa counts the packs.', 'A Rosa conta os pacotes.'), ('counted', 'He counted two erasers.', 'Ele contou duas borrachas.'), ('counting', 'I am counting my money.', 'Estou contando meu dinheiro.'), 'Count serve para números e para dinheiro.'),
  vb('draw', '🖍️', 'desenhar', ('draw', 'I draw a line with a ruler.', 'Eu desenho uma linha com uma régua.'), ('draws', 'Lily draws a cat.', 'A Lily desenha um gato.'), ('drew', 'He drew a house.', 'Ele desenhou uma casa.'), ('drawing', 'She is drawing a map.', 'Ela está desenhando um mapa.'), 'Irregular: draw vira drew no passado.'),
  vb('write', '✍️', 'escrever', ('write', 'We write our names.', 'Nós escrevemos nossos nomes.'), ('writes', 'Tom writes a list.', 'O Tom escreve uma lista.'), ('wrote', 'I wrote a note.', 'Eu escrevi um bilhete.'), ('writing', 'I am writing now.', 'Estou escrevendo agora.'), 'Irregular: write vira wrote. Cuidado com o -ing: writing.')],
 verb_game=[
  dict(scene='O Tom leva a mochila para a escola todo dia.', en='Tom ___ his backpack every day.', opts=['carry', 'carries', 'carried'], ans=1, pt='O Tom leva a mochila todo dia.', why='Com “Tom” (ele), carry vira carries.'),
  dict(scene='Ontem a Lily desenhou um gato.', en='Yesterday Lily ___ a cat.', opts=['draw', 'drew', 'drawing'], ans=1, pt='Ontem a Lily desenhou um gato.', why='“Yesterday” pede passado; draw vira drew.'),
  dict(scene='Agora você escolhe a cor da mochila.', en='I am ___ a color now.', opts=['pick', 'picks', 'picking'], ans=2, pt='Estou escolhendo uma cor agora.', why='“am” + verbo termina em -ing: picking.'),
  dict(scene='Vocês escrevem a lista de material.', en='We ___ the list together.', opts=['write', 'writes', 'wrote'], ans=0, pt='Nós escrevemos a lista juntos.', why='Com “we”, o presente fica na forma base: write.')],
 expressions=[
  dict(en='I need…', pt='Eu preciso de…', ex='I need two notebooks.', exp='Para dizer o que você quer comprar.', c='a'),
  dict(en='Where are the…?', pt='Onde ficam os…?', ex='Where are the rulers?', exp='Para achar algo na loja.', c='b'),
  dict(en='How much is it?', pt='Quanto custa?', ex='How much is this backpack?', exp='Para saber o preço.', c='c'),
  dict(en='I’ll take it.', pt='Eu levo.', ex='I like it. I’ll take it.', exp='Para decidir a compra.', c='d'),
  dict(en='a pack of', pt='um pacote de', ex='I want a pack of pencils.', exp='Para pedir itens vendidos juntos.', c='a'),
  dict(en='on sale', pt='em promoção', ex='These notebooks are on sale.', exp='Quando o preço está reduzido.', c='b')],
 expr_game=[
  dict(cue='Você não encontra as réguas.', opts=['Where are the rulers?', 'I’ll take it.', 'On sale.'], ans=0, why='Where are the…? pergunta o lugar.'),
  dict(cue='Você gostou da mochila azul e vai comprá-la.', opts=['How much is it?', 'I’ll take it.', 'Where are the…?'], ans=1, why='I’ll take it decide a compra.'),
  dict(cue='Você quer saber o valor do caderno.', opts=['A pack of ten.', 'How much is it?', 'I need two.'], ans=1, why='How much is it? pergunta o preço.')])
