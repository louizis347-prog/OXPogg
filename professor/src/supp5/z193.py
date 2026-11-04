"""Bloco de verbos e expressões da aula 193: pedir uma escada emprestada."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('borrow', '🙏', 'pegar emprestado', ('borrow', 'I borrow a ladder.', 'Eu pego uma escada emprestada.'), ('borrows', 'Sam borrows a hammer.', 'O Sam pega um martelo emprestado.'), ('borrowed', 'We borrowed a tool.', 'Nós pegamos uma ferramenta emprestada.'), ('borrowing', 'I am borrowing a bike.', 'Estou pegando uma bicicleta emprestada.'), 'Borrow é pegar emprestado; quem dá é quem lend. Passado regular: borrowed.'),
  vb('lend', '🤲', 'emprestar', ('lend', 'I lend my tools.', 'Eu empresto minhas ferramentas.'), ('lends', 'Jordan lends the ladder.', 'O Jordan empresta a escada.'), ('lent', 'She lent me a hammer.', 'Ela me emprestou um martelo.'), ('lending', 'He is lending his bike.', 'Ele está emprestando a bicicleta.'), 'Lend é irregular: lent. Lend = dar emprestado; borrow = pegar emprestado.'),
  vb('climb', '🧗', 'subir', ('climb', 'I climb the ladder.', 'Eu subo na escada.'), ('climbs', 'Sam climbs up.', 'O Sam sobe.'), ('climbed', 'We climbed the stairs.', 'Nós subimos a escada.'), ('climbing', 'He is climbing slowly.', 'Ele está subindo devagar.'), 'No climb, o b é mudo: soa “claim”.'),
  vb('paint', '🎨', 'pintar', ('paint', 'We paint the door.', 'Nós pintamos a porta.'), ('paints', 'Jordan paints the wall.', 'O Jordan pinta a parede.'), ('painted', 'I painted the hallway.', 'Eu pintei o corredor.'), ('painting', 'She is painting a shelf.', 'Ela está pintando uma prateleira.'), 'Paint é tinta e também pintar. Passado regular: painted.'),
  vb('knock', '🚪', 'bater (à porta)', ('knock', 'I knock on the door.', 'Eu bato à porta.'), ('knocks', 'Sam knocks twice.', 'O Sam bate duas vezes.'), ('knocked', 'He knocked softly.', 'Ele bateu de leve.'), ('knocking', 'Someone is knocking.', 'Alguém está batendo.'), 'No knock, o k é mudo: soa “nock”.')],
 verb_game=[
  dict(scene='Ontem a Ana te emprestou uma escada.', en='Yesterday Ana ___ me a ladder.', opts=['lend', 'lent', 'lending'], ans=1, pt='Ontem a Ana me emprestou uma escada.', why='“Yesterday” pede passado irregular: lent.'),
  dict(scene='Agora o Sam está subindo na escada.', en='Sam is ___ the ladder.', opts=['climb', 'climbs', 'climbing'], ans=2, pt='O Sam está subindo na escada.', why='“is” + verbo termina em -ing: climbing.'),
  dict(scene='O Jordan sempre empresta suas ferramentas.', en='Jordan ___ his tools.', opts=['lend', 'lends', 'lent'], ans=1, pt='O Jordan empresta suas ferramentas.', why='Com “Jordan” (ele), o presente leva -s: lends.'),
  dict(scene='Nós pegamos emprestado um martelo.', en='We ___ a hammer from Jordan.', opts=['borrow', 'borrows', 'borrowing'], ans=0, pt='Nós pegamos um martelo emprestado do Jordan.', why='Com “we”, o presente fica na forma base: borrow.')],
 expressions=[
  dict(en='Do you have a minute?', pt='Tem um minutinho?', ex='Hi! Do you have a minute?', exp='Para pedir a atenção de alguém antes de um favor.', c='a'),
  dict(en='Could I borrow…?', pt='Posso pegar emprestado…?', ex='Could I borrow your ladder?', exp='Para pedir uma coisa emprestada com educação.', c='b'),
  dict(en='What for?', pt='Para quê?', ex='A ladder? What for?', exp='Para perguntar a razão de um pedido.', c='c'),
  dict(en='bring it back', pt='devolver (trazer de volta)', ex='I’ll bring it back soon.', exp='Para prometer devolver o que pegou.', c='d'),
  dict(en='No worries!', pt='Sem problema!', ex='No worries! Take your time.', exp='Para tranquilizar alguém.', c='a'),
  dict(en='Anytime!', pt='Quando quiser!', ex='Thanks! — Anytime!', exp='Resposta simpática a um agradecimento.', c='b')],
 expr_game=[
  dict(cue='Você quer pedir a escada do vizinho.', opts=['Could I borrow your ladder?', 'What for?', 'Anytime!'], ans=0, why='Could I borrow…? pede algo emprestado.'),
  dict(cue='Você promete devolver a escada.', opts=['No worries!', 'I’ll bring it back soon.', 'What for?'], ans=1, why='Bring it back = devolver.'),
  dict(cue='Alguém pede desculpas e você quer tranquilizar.', opts=['No worries!', 'Do you have a minute?', 'Could I borrow…?'], ans=0, why='No worries! tranquiliza.')])
