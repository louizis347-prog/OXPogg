"""Bloco de verbos e expressões da aula 174: ingressos de cinema."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('laugh', '😂', 'rir', ('laugh', 'We laugh at the comedy.', 'Nós rimos da comédia.'), ('laughs', 'Cory laughs a lot.', 'O Cory ri muito.'), ('laughed', 'We laughed all night.', 'Nós rimos a noite toda.'), ('laughing', 'They are laughing now.', 'Eles estão rindo agora.'), 'Laugh = rir. Laugh at = rir de algo.'),
  vb('watch', '📺', 'assistir', ('watch', 'I watch a movie on Friday.', 'Eu assisto a um filme na sexta.'), ('watches', 'She watches the screen.', 'Ela olha a tela.'), ('watched', 'We watched a comedy.', 'Nós assistimos a uma comédia.'), ('watching', 'I am watching the trailer.', 'Estou assistindo ao trailer.'), 'Watch + filme: sem preposição. Com he/she: watches.'),
  vb('enjoy', '😊', 'curtir, gostar de', ('enjoy', 'I enjoy the movie.', 'Eu curto o filme.'), ('enjoys', 'Cory enjoys comedies.', 'O Cory curte comédias.'), ('enjoyed', 'We enjoyed the show.', 'Nós curtimos a sessão.'), ('enjoying', 'I am enjoying the movie.', 'Estou curtindo o filme.'), 'Enjoy sempre pede um objeto: enjoy the movie.'),
  vb('start', '▶️', 'começar', ('start', 'The movies start at seven.', 'Os filmes começam às sete.'), ('starts', 'The movie starts now.', 'O filme começa agora.'), ('started', 'The trailer started.', 'O trailer começou.'), ('starting', 'The movie is starting.', 'O filme está começando.'), 'Start = começar. Passado regular: started.'),
  vb('sell', '🎫', 'vender', ('sell', 'They sell popcorn here.', 'Eles vendem pipoca aqui.'), ('sells', 'Carlos sells tickets.', 'O Carlos vende ingressos.'), ('sold', 'He sold two tickets.', 'Ele vendeu dois ingressos.'), ('selling', 'She is selling popcorn.', 'Ela está vendendo pipoca.'), 'Sell é irregular: sold. Sold out = esgotado.')],
 verb_game=[
  dict(scene='O Carlos vende ingressos todo dia.', en='Carlos ___ tickets every day.', opts=['sell', 'sells', 'sold'], ans=1, pt='O Carlos vende ingressos todo dia.', why='Com Carlos (ele), o presente leva -s: sells.'),
  dict(scene='O filme está começando agora.', en='The movie is ___ now.', opts=['start', 'starts', 'starting'], ans=2, pt='O filme está começando agora.', why='“is” + verbo termina em -ing: starting.'),
  dict(scene='Ontem vocês riram muito.', en='Yesterday we ___ a lot.', opts=['laugh', 'laughed', 'laughing'], ans=1, pt='Ontem nós rimos muito.', why='“Yesterday” pede passado: laughed.'),
  dict(scene='Você quer assistir a uma comédia.', en='I want to ___ the new comedy.', opts=['watch', 'watches', 'watched'], ans=0, pt='Quero assistir à nova comédia.', why='Depois de to, use o verbo base: watch.')],
 expressions=[
  dict(en='Sold out', pt='Esgotado', ex='The seven o’clock show is sold out.', exp='Quando não há mais ingressos.', c='a'),
  dict(en='Coming soon', pt='Em breve', ex='The sign says coming soon.', exp='Aviso de filme que vai estrear em breve.', c='b'),
  dict(en='No spoilers!', pt='Sem spoilers!', ex='Please, no spoilers!', exp='Para pedir que não contem o final.', c='c'),
  dict(en='Blockbuster', pt='Grande sucesso de bilheteria', ex='This is a big blockbuster.', exp='Filme muito popular e caro de fazer.', c='d'),
  dict(en='Front row seats', pt='Lugares na primeira fileira', ex='I have front row seats.', exp='Assentos mais perto da tela.', c='a'),
  dict(en='Here’s my card.', pt='Aqui está meu cartão.', ex='Here’s my card. Thank you.', exp='Para entregar o cartão ao pagar.', c='b')],
 expr_game=[
  dict(cue='Você quer pedir que não contem o final do filme.', opts=['No spoilers!', 'Sold out.', 'Coming soon.'], ans=0, why='No spoilers! pede para não revelar a história.'),
  dict(cue='O vendedor diz que não restam ingressos.', opts=['Blockbuster.', 'Sold out.', 'Front row seats.'], ans=1, why='Sold out = esgotado.'),
  dict(cue='Você quer entregar o cartão para pagar.', opts=['Here’s my card.', 'Coming soon.', 'No spoilers!'], ans=0, why='Here’s my card é a forma natural.')])
