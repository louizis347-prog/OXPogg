K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('borrow', '🤝', 'pegar emprestado', ('borrow', 'I borrow sugar.', 'Eu pego açúcar emprestado.'), ('borrows', 'Miles borrows a cup.', 'O Miles pega uma xícara emprestada.'), ('borrowed', 'He borrowed a ladder.', 'Ele pegou uma escada emprestada.'), ('borrowing', 'I am borrowing a book.', 'Estou pegando um livro emprestado.'), 'Borrow = pegar emprestado de alguém. Lend = emprestar a alguém.'),
  vb('lend', '🤲', 'emprestar', ('lend', 'I lend my ladder.', 'Eu empresto minha escada.'), ('lends', 'Pearl lends him sugar.', 'A Pearl empresta açúcar a ele.'), ('lent', 'She lent me a cup.', 'Ela me emprestou uma xícara.'), ('lending', 'I am lending a pen.', 'Estou emprestando uma caneta.'), 'Irregular: lend, lent.'),
  vb('bake', '🎂', 'assar', ('bake', 'I bake a cake.', 'Eu asso um bolo.'), ('bakes', 'Miles bakes on Saturday.', 'O Miles assa no sábado.'), ('baked', 'She baked cookies.', 'Ela assou biscoitos.'), ('baking', 'I am baking a pie.', 'Estou assando uma torta.'), 'Bake perde o e antes de -ing: baking.'),
  vb('return', '↩️', 'devolver', ('return', 'I return the ladder.', 'Eu devolvo a escada.'), ('returns', 'Miles returns the cup.', 'O Miles devolve a xícara.'), ('returned', 'He returned the book.', 'Ele devolveu o livro.'), ('returning', 'I am returning the tools.', 'Estou devolvendo as ferramentas.'), 'Return = devolver; também significa voltar.'),
  vb('save', '🍰', 'guardar / salvar', ('save', 'I save a slice for you.', 'Eu guardo uma fatia para você.'), ('saves', 'Pearl saves a piece.', 'A Pearl guarda um pedaço.'), ('saved', 'He saved me a seat.', 'Ele guardou um lugar para mim.'), ('saving', 'I am saving some cake.', 'Estou guardando um pouco de bolo.'), 'Save me a slice = guarde uma fatia para mim.')],
 verb_game=[
  dict(scene='O Miles precisa de açúcar e pede à vizinha.', en='Miles ___ sugar from Pearl.', opts=['borrow', 'borrows', 'lends'], ans=1, pt='O Miles pega açúcar emprestado da Pearl.', why='Com “Miles” (ele), use borrows. Lend é o oposto.'),
  dict(scene='Ontem a Pearl emprestou uma xícara de açúcar.', en='Yesterday Pearl ___ him a cup of sugar.', opts=['lend', 'lent', 'lending'], ans=1, pt='Ontem a Pearl emprestou a ele uma xícara de açúcar.', why='“Yesterday” pede passado: lent.'),
  dict(scene='Agora o Miles está assando um bolo.', en='Miles is ___ a cake.', opts=['bake', 'bakes', 'baking'], ans=2, pt='O Miles está assando um bolo.', why='“is” + verbo termina em -ing: baking.'),
  dict(scene='Você promete devolver a escada amanhã.', en='I ___ the ladder tomorrow.', opts=['return', 'returns', 'returned'], ans=0, pt='Eu devolvo a escada amanhã.', why='Com “I” o presente fica na forma base: return.')],
 expressions=[
  dict(en='Can I ask you a favor?', pt='Posso pedir um favor?', ex='Hi, Pearl! Can I ask you a favor?', exp='Para começar um pedido com educação.', c='a'),
  dict(en='Can I borrow…?', pt='Posso pegar… emprestado?', ex='Can I borrow some sugar?', exp='Para pedir algo emprestado.', c='b'),
  dict(en='Here you go.', pt='Aqui está.', ex='Here you go. One cup of sugar.', exp='Ao entregar algo a alguém.', c='c'),
  dict(en='You\'re a lifesaver!', pt='Você me salvou!', ex='Thanks again. You\'re a lifesaver!', exp='Agradecimento caloroso e informal.', c='d'),
  dict(en='No big deal.', pt='Não foi nada.', ex='Don\'t worry. It\'s no big deal.', exp='Resposta para dizer que o favor foi fácil.', c='a'),
  dict(en='I owe you one.', pt='Fico te devendo uma.', ex='Thanks! I owe you one.', exp='Para dizer que vai retribuir o favor.', c='b')],
 expr_game=[
  dict(cue='Você quer pedir um pouco de farinha emprestada.', opts=['Can I borrow some flour?', 'Here you go.', 'No big deal.'], ans=0, why='Can I borrow…? pede algo emprestado.'),
  dict(cue='Alguém te agradece por um favor pequeno e você quer diminuir.', opts=['I owe you one.', 'No big deal.', 'Can I ask you a favor?'], ans=1, why='No big deal diz que foi fácil.'),
  dict(cue='Você acaba de ganhar ajuda e quer agradecer muito.', opts=['Here you go.', 'You\'re a lifesaver!', 'How much do you need?'], ans=1, why='You\'re a lifesaver! é um agradecimento forte e simpático.')])
