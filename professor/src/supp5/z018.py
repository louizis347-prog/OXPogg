"""Bloco de verbos e expressões da aula 018."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('play', '⚽', 'jogar / tocar', ('play', 'I play soccer.', 'Eu jogo futebol.'), ('plays', 'Raj plays guitar.', 'O Raj toca violão.'), ('played', 'We played tennis.', 'Nós jogamos tênis.'), ('playing', 'I am playing cards.', 'Estou jogando cartas.'), 'Play serve para esporte, jogo e instrumento.'),
  vb('read', '📖', 'ler', ('read', 'I read books.', 'Eu leio livros.'), ('reads', 'Mia reads comics.', 'A Mia lê quadrinhos.'), ('read', 'I read a book last week.', 'Eu li um livro semana passada.'), ('reading', 'I am reading now.', 'Estou lendo agora.'), 'Escreve igual no passado, mas lê-se “red”.'),
  vb('watch', '🎬', 'assistir', ('watch', 'I watch movies.', 'Eu assisto filmes.'), ('watches', 'Sam watches TV.', 'O Sam assiste TV.'), ('watched', 'We watched a film.', 'Nós assistimos a um filme.'), ('watching', 'I am watching a game.', 'Estou assistindo a um jogo.'), 'Com he/she: watches (-es).'),
  vb('swim', '🏊', 'nadar', ('swim', 'I swim on Saturday.', 'Eu nado no sábado.'), ('swims', 'Raj swims fast.', 'O Raj nada rápido.'), ('swam', 'We swam yesterday.', 'Nós nadamos ontem.'), ('swimming', 'I am swimming now.', 'Estou nadando agora.'), 'Passado irregular: swim vira swam; -ing duplica o m.'),
  vb('draw', '✏️', 'desenhar', ('draw', 'I draw in the park.', 'Eu desenho no parque.'), ('draws', 'Mia draws comics.', 'A Mia desenha quadrinhos.'), ('drew', 'We drew a map.', 'Nós desenhamos um mapa.'), ('drawing', 'I am drawing a cat.', 'Estou desenhando um gato.'), 'Irregular: draw, drew.')],
 verb_game=[
  dict(scene='O Raj toca violão.', en='Raj ___ guitar.', opts=['play', 'plays', 'played'], ans=1, pt='O Raj toca violão.', why='Com “Raj”: plays.'),
  dict(scene='Ontem vocês assistiram a um filme.', en='We ___ a movie yesterday.', opts=['watch', 'watches', 'watched'], ans=2, pt='Nós assistimos a um filme ontem.', why='Passado: watched.'),
  dict(scene='Agora você está lendo.', en='I am ___ a book.', opts=['read', 'reads', 'reading'], ans=2, pt='Estou lendo um livro.', why='“am” + -ing: reading.'),
  dict(scene='Vocês desenham no parque às dez.', en='We ___ in the park at ten.', opts=['draw', 'draws', 'drew'], ans=0, pt='Nós desenhamos no parque às dez.', why='Presente com “we”: draw.')],
 expressions=[
  dict(en='What do you do in your free time?', pt='O que você faz no tempo livre?', ex='What do you do in your free time?', exp='Perguntar sobre hobbies.', c='a'),
  dict(en='I play soccer.', pt='Eu jogo futebol.', ex='I play soccer and read books.', exp='Dizer o que você pratica.', c='b'),
  dict(en='for fun', pt='por diversão', ex='I play at home, just for fun.', exp='Dizer que é hobby.', c='c'),
  dict(en='Do you want to play?', pt='Quer jogar?', ex='Do you want to play soccer on Saturday?', exp='Convidar para jogar.', c='d'),
  dict(en='What time?', pt='A que horas?', ex='Sure! What time?', exp='Perguntar o horário.', c='a'),
  dict(en='in the park', pt='no parque', ex='At ten, in the park.', exp='Dizer o lugar.', c='b')],
 expr_game=[
  dict(cue='Você quer saber o que o amigo faz no tempo livre.', opts=['What do you do in your free time?', 'What time?', 'For fun.'], ans=0, why='Free time = tempo livre.'),
  dict(cue='Você convida alguém para jogar sábado.', opts=['I play soccer.', 'Do you want to play on Saturday?', 'In the park.'], ans=1, why='Do you want to…? convida.'),
  dict(cue='Aceitaram o convite e você quer saber a hora.', opts=['What time?', 'For fun.', 'In the park.'], ans=0, why='What time? pergunta a hora.')])
