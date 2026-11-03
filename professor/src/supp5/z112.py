"""Bloco de verbos e expressões da aula 112: a carteirinha da biblioteca."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('borrow', '🤝', 'pegar emprestado', ('borrow', 'I borrow two books.', 'Eu pego dois livros emprestados.'), ('borrows', 'Ana borrows a movie.', 'A Ana pega um filme emprestado.'), ('borrowed', 'He borrowed a novel.', 'Ele pegou um romance emprestado.'), ('borrowing', 'I am borrowing a book.', 'Estou pegando um livro emprestado.'), 'Borrow = pegar emprestado; lend = emprestar. Não confunda.'),
  vb('renew', '🔄', 'renovar', ('renew', 'We renew books online.', 'Nós renovamos livros on-line.'), ('renews', 'She renews her card.', 'Ela renova a carteirinha.'), ('renewed', 'I renewed the book.', 'Eu renovei o livro.'), ('renewing', 'I am renewing it now.', 'Estou renovando agora.'), 'Renew se escreve como o português “renovar”; passado com -ed.'),
  vb('return', '↩️', 'devolver', ('return', 'I return books on Friday.', 'Eu devolvo livros na sexta.'), ('returns', 'Sam returns the movie.', 'O Sam devolve o filme.'), ('returned', 'She returned the book.', 'Ela devolveu o livro.'), ('returning', 'I am returning this book.', 'Estou devolvendo este livro.'), 'Return = devolver ou voltar. Passado regular: returned.'),
  vb('find', '🔍', 'encontrar', ('find', 'I find the book fast.', 'Eu encontro o livro rápido.'), ('finds', 'Ana finds her seat.', 'A Ana encontra seu lugar.'), ('found', 'He found the movie.', 'Ele encontrou o filme.'), ('finding', 'I am finding a good book.', 'Estou encontrando um bom livro.'), 'Find é irregular: passado found.'),
  vb('check out', '🧾', 'retirar (emprestar)', ('check out', 'We check out three books.', 'Nós retiramos três livros.'), ('checks out', 'She checks out a movie.', 'Ela retira um filme.'), ('checked out', 'I checked out two books.', 'Eu retirei dois livros.'), ('checking out', 'I am checking out now.', 'Estou retirando agora.'), 'Check out é o termo comum no balcão para levar um livro emprestado.')],
 verb_game=[
  dict(scene='A Ana pega livros emprestados toda semana.', en='Ana ___ books every week.', opts=['borrow', 'borrows', 'borrowed'], ans=1, pt='A Ana pega livros emprestados toda semana.', why='Com “Ana” (ela), o presente leva -s: borrows.'),
  dict(scene='Ontem você achou o livro que queria.', en='Yesterday I ___ the book.', opts=['find', 'found', 'finding'], ans=1, pt='Ontem eu encontrei o livro.', why='“Yesterday” pede passado; find vira found.'),
  dict(scene='Agora você devolve o livro no balcão.', en='I am ___ this book now.', opts=['return', 'returns', 'returning'], ans=2, pt='Estou devolvendo este livro agora.', why='“am” + verbo termina em -ing: returning.'),
  dict(scene='Vocês renovam os livros pela internet.', en='We ___ our books online.', opts=['renew', 'renews', 'renewed'], ans=0, pt='Nós renovamos nossos livros on-line.', why='Com “we”, o presente fica na forma base: renew.')],
 expressions=[
  dict(en='I’d like a library card.', pt='Eu gostaria de uma carteirinha.', ex='Hi! I’d like a library card, please.', exp='Para pedir a carteirinha no balcão.', c='a'),
  dict(en='Is it free?', pt='É grátis?', ex='Is the card free?', exp='Para perguntar se há custo.', c='b'),
  dict(en='What’s the due date?', pt='Qual é a data de devolução?', ex='What’s the due date for this book?', exp='Para saber até quando ficar com o livro.', c='c'),
  dict(en='Keep your voice down.', pt='Fale baixo.', ex='Please keep your voice down here.', exp='Pedido comum em bibliotecas.', c='d'),
  dict(en='check out', pt='retirar (emprestar)', ex='I’d like to check out these books.', exp='Verbo frasal para levar livros emprestados.', c='a'),
  dict(en='page-turner', pt='livro de prender a leitura', ex='This book is a real page-turner.', exp='Elogio informal a um livro emocionante.', c='b')],
 expr_game=[
  dict(cue='Você quer pegar três livros emprestados.', opts=['I’d like to check out these books.', 'Is it free?', 'Keep your voice down.'], ans=0, why='Check out é o verbo para retirar livros.'),
  dict(cue='Você quer saber se a carteirinha custa algo.', opts=['What’s the due date?', 'Is the card free?', 'It’s a page-turner.'], ans=1, why='Is… free? pergunta sobre o preço.'),
  dict(cue='Você quer saber até quando pode ficar com o livro.', opts=['What’s the due date?', 'Is it free?', 'I’d like a library card.'], ans=0, why='Due date é a data de devolução.')])
