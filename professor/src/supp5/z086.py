"""Bloco de verbos e expressões da aula 086: noite de cinema."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('watch', '📺', 'assistir / ver', ('watch', 'We watch a comedy.', 'Nós assistimos a uma comédia.'), ('watches', 'Sam watches action films.', 'O Sam assiste a filmes de ação.'), ('watched', 'I watched a cartoon.', 'Eu assisti a um desenho.'), ('watching', 'I am watching the trailer.', 'Estou vendo o trailer.'), 'Watch = assistir algo que se mexe (filme, jogo). Passado: watched.'),
  vb('laugh', '😂', 'rir', ('laugh', 'We laugh a lot.', 'Nós rimos muito.'), ('laughs', 'Mia laughs at the actor.', 'A Mia ri do ator.'), ('laughed', 'Everybody laughed.', 'Todos riram.'), ('laughing', 'Sam is laughing now.', 'O Sam está rindo agora.'), 'Laugh at = rir de algo ou alguém.'),
  vb('start', '▶️', 'começar', ('start', 'Films start at eight.', 'Os filmes começam às oito.'), ('starts', 'The film starts now.', 'O filme começa agora.'), ('started', 'The trailer started.', 'O trailer começou.'), ('starting', 'It is starting!', 'Está começando!'), 'Em perguntas com does, use start sem -s: What time does it start?'),
  vb('enjoy', '🎉', 'aproveitar / curtir', ('enjoy', 'I enjoy comedies.', 'Eu curto comédias.'), ('enjoys', 'Cole enjoys the film.', 'O Cole curte o filme.'), ('enjoyed', 'We enjoyed the night.', 'Nós curtimos a noite.'), ('enjoying', 'I am enjoying the movie.', 'Estou curtindo o filme.'), 'Enjoy já traz o “aproveitar”: não use “enjoy of”.'),
  vb('share', '🤝', 'dividir', ('share', 'We share the popcorn.', 'Nós dividimos a pipoca.'), ('shares', 'Mia shares her candy.', 'A Mia divide seus doces.'), ('shared', 'Sam shared a large popcorn.', 'O Sam dividiu uma pipoca grande.'), ('sharing', 'We are sharing a seat map.', 'Estamos compartilhando o mapa de assentos.'), 'Share = dividir ou compartilhar.')],
 verb_game=[
  dict(scene='Toda sexta a Mia vê um filme.', en='Mia ___ a film every Friday.', opts=['watch', 'watches', 'watched'], ans=1, pt='A Mia assiste a um filme toda sexta.', why='Com “Mia” (ela), o presente leva -es: watches.'),
  dict(scene='Você pergunta o horário do filme.', en='What time does it ___?', opts=['start', 'starts', 'started'], ans=0, pt='Que horas ele começa?', why='Depois de does, o verbo fica na forma base: start.'),
  dict(scene='Ontem todo mundo riu do ator.', en='Everybody ___ at the actor.', opts=['laugh', 'laughs', 'laughed'], ans=2, pt='Todos riram do ator.', why='“Ontem” pede passado: laughed.'),
  dict(scene='Os amigos estão dividindo a pipoca agora.', en='We are ___ the popcorn.', opts=['share', 'shares', 'sharing'], ans=2, pt='Estamos dividindo a pipoca.', why='“are” + verbo termina em -ing: sharing.')],
 expressions=[
  dict(en='How about…?', pt='Que tal…?', ex='How about a comedy tonight?', exp='Para sugerir uma ideia a um amigo.', c='a'),
  dict(en='What time does it start?', pt='Que horas começa?', ex='What time does the film start?', exp='Para perguntar o horário de um filme ou evento.', c='b'),
  dict(en='Let’s buy tickets online.', pt='Vamos comprar ingressos online.', ex='Let’s buy tickets online now.', exp='Para propor um plano com alguém.', c='c'),
  dict(en='a large one', pt='um grande', ex='A large one, please.', exp='Para escolher o tamanho sem repetir o nome da coisa.', c='d'),
  dict(en='Enjoy the movie!', pt='Aproveite o filme!', ex='Thanks! Enjoy the movie!', exp='Despedida simpática antes de o filme começar.', c='a'),
  dict(en='That was awesome!', pt='Foi incrível!', ex='That was awesome! I loved it.', exp='Para elogiar um filme depois que acaba.', c='b')],
 expr_game=[
  dict(cue='Você quer saber a hora em que o filme começa.', opts=['What time does it start?', 'Do you want popcorn?', 'Enjoy the movie!'], ans=0, why='What time…? pergunta o horário.'),
  dict(cue='Você quer sugerir uma comédia para o seu amigo.', opts=['That was awesome!', 'How about a comedy?', 'A large one, please.'], ans=1, why='How about…? é para sugerir.'),
  dict(cue='O filme acabou e você adorou.', opts=['Let’s buy tickets online.', 'What time does it start?', 'That was awesome!'], ans=2, why='That was awesome! elogia algo que já aconteceu.')])
