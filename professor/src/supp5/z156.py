"""Bloco de verbos e expressões da aula 156: clube do livro."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('talk', '💬', 'conversar / falar', ('talk', 'We talk about the book.', 'Nós conversamos sobre o livro.'), ('talks', 'Ava talks about the plot.', 'A Ava fala sobre o enredo.'), ('talked', 'We talked for an hour.', 'Nós conversamos por uma hora.'), ('talking', 'They are talking about the ending.', 'Eles estão conversando sobre o final.'), 'Talk about = conversar sobre. Talk to = falar com alguém.'),
  vb('finish', '🏁', 'terminar', ('finish', 'I finish the book on Friday.', 'Eu termino o livro na sexta.'), ('finishes', 'Lena finishes the chapter.', 'A Lena termina o capítulo.'), ('finished', 'I finished the novel last night.', 'Eu terminei o romance ontem à noite.'), ('finishing', 'I am finishing the last page.', 'Estou terminando a última página.'), 'Depois de did, volta ao normal: Did you finish? (não “finished”).'),
  vb('agree', '🤝', 'concordar', ('agree', 'We agree about the ending.', 'Nós concordamos sobre o final.'), ('agrees', 'Ava agrees with Lena.', 'A Ava concorda com a Lena.'), ('agreed', 'Everyone agreed.', 'Todos concordaram.'), ('agreeing', 'We are agreeing again.', 'Estamos concordando de novo.'), 'Nunca diga “I am agree”: é só I agree.'),
  vb('laugh', '😄', 'rir', ('laugh', 'We laugh at the grandmother.', 'Nós rimos da avó.'), ('laughs', 'Lena laughs a lot.', 'A Lena ri muito.'), ('laughed', 'Everyone laughed.', 'Todos riram.'), ('laughing', 'They are laughing now.', 'Eles estão rindo agora.'), 'Laugh at = rir de algo. Pronuncia-se “laf”.'),
  vb('borrow', '🤲', 'pegar emprestado', ('borrow', 'I borrow books from the library.', 'Eu pego livros emprestados na biblioteca.'), ('borrows', 'Ava borrows my novel.', 'A Ava pega meu romance emprestado.'), ('borrowed', 'I borrowed this book.', 'Eu peguei este livro emprestado.'), ('borrowing', 'She is borrowing a mystery.', 'Ela está pegando um mistério emprestado.'), 'Borrow = pegar emprestado; lend = emprestar a alguém.')],
 verb_game=[
  dict(scene='Toda semana a Ava fala do enredo.', en='Ava ___ about the plot every week.', opts=['talk', 'talks', 'talked'], ans=1, pt='A Ava fala sobre o enredo toda semana.', why='Com “Ava” (ela), o presente leva -s: talks.'),
  dict(scene='Ontem você terminou o livro.', en='Last night I ___ the book.', opts=['finish', 'finished', 'finishing'], ans=1, pt='Ontem à noite eu terminei o livro.', why='“Last night” pede passado: finished.'),
  dict(scene='Agora todos estão rindo da avó.', en='Everyone is ___ at the grandmother.', opts=['laugh', 'laughs', 'laughing'], ans=2, pt='Todos estão rindo da avó.', why='“is” + verbo termina em -ing: laughing.'),
  dict(scene='Você e a Ava têm a mesma opinião.', en='We ___ about the ending.', opts=['agree', 'agrees', 'agreed'], ans=0, pt='Nós concordamos sobre o final.', why='Com “we” o presente fica na forma base: agree.')],
 expressions=[
  dict(en='Thanks for having me.', pt='Obrigada por me receber.', ex='Thanks for having me. Your home is nice.', exp='Para agradecer ao anfitrião ao chegar.', c='a'),
  dict(en='Spoiler alert!', pt='Alerta de spoiler!', ex='Spoiler alert! I will tell the ending.', exp='Para avisar antes de contar uma surpresa da história.', c='b'),
  dict(en='It’s a page-turner.', pt='É um livro que prende.', ex='I love this book. It’s a page-turner.', exp='Para elogiar um livro difícil de largar.', c='c'),
  dict(en='I couldn’t put it down.', pt='Não consegui parar de ler.', ex='I couldn’t put it down. I read all night.', exp='Para dizer que o livro era tão bom que você leu sem parar.', c='d'),
  dict(en='I agree.', pt='Concordo.', ex='I agree. The grandmother is funny.', exp='Para mostrar que você pensa o mesmo.', c='a'),
  dict(en='Would you recommend it?', pt='Você recomendaria?', ex='Nice book! Would you recommend it?', exp='Para pedir a opinião final sobre um livro ou filme.', c='b')],
 expr_game=[
  dict(cue='Você vai contar o final e quer avisar os outros antes.', opts=['Thanks for having me.', 'Spoiler alert!', 'I agree.'], ans=1, why='Spoiler alert! avisa antes de contar o final.'),
  dict(cue='Você chega à casa da anfitriã e quer agradecer.', opts=['Thanks for having me.', 'Would you recommend it?', 'I couldn’t put it down.'], ans=0, why='Thanks for having me. agradece o convite.'),
  dict(cue='Você leu o livro inteiro sem parar, de tão bom.', opts=['It’s a page-turner.', 'I agree.', 'Spoiler alert!'], ans=0, why='Page-turner descreve um livro que prende.')])
