"""Bloco de verbos e expressões da aula 061: balcão de turismo."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('visit', '🏛️', 'visitar', ('visit', 'We visit the museum.', 'Nós visitamos o museu.'), ('visits', 'Mia visits the bell.', 'A Mia visita o sino.'), ('visited', 'I visited the park.', 'Eu visitei o parque.'), ('visiting', 'I am visiting Philadelphia.', 'Estou visitando a Filadélfia.'), 'Passado regular: visited.'),
  vb('try', '😋', 'experimentar', ('try', 'I try a cheesesteak.', 'Eu experimento um cheesesteak.'), ('tries', 'She tries the soup.', 'Ela experimenta a sopa.'), ('tried', 'We tried the pie.', 'Nós experimentamos a torta.'), ('trying', 'I am trying a new food.', 'Estou experimentando uma comida nova.'), 'Try muda para tries e tried (y vira ie/i).'),
  vb('enjoy', '😊', 'aproveitar', ('enjoy', 'I enjoy the city.', 'Eu aproveito a cidade.'), ('enjoys', 'He enjoys the park.', 'Ele aproveita o parque.'), ('enjoyed', 'We enjoyed the day.', 'Nós aproveitamos o dia.'), ('enjoying', 'I am enjoying my trip.', 'Estou aproveitando minha viagem.'), 'Enjoy + algo: enjoy the day.'),
  vb('find', '🔎', 'encontrar', ('find', 'I find the museum.', 'Eu encontro o museu.'), ('finds', 'Leo finds a map.', 'O Leo acha um mapa.'), ('found', 'She found the bell.', 'Ela encontrou o sino.'), ('finding', 'I am finding the street.', 'Estou encontrando a rua.'), 'Find é irregular: found no passado.'),
  vb('show', '👉', 'mostrar', ('show', 'I show my ticket.', 'Eu mostro meu ingresso.'), ('shows', 'Leo shows the map.', 'O Leo mostra o mapa.'), ('showed', 'He showed me the way.', 'Ele me mostrou o caminho.'), ('showing', 'He is showing the map.', 'Ele está mostrando o mapa.'), 'Show me the map = mostre-me o mapa.')],
 verb_game=[
  dict(scene='A Mia está na cidade agora.', en='Mia is ___ the city today.', opts=['visit', 'visits', 'visiting'], ans=2, pt='A Mia está visitando a cidade hoje.', why='“is” + -ing: visiting.'),
  dict(scene='Ontem você achou o museu.', en='Yesterday I ___ the museum.', opts=['find', 'finds', 'found'], ans=2, pt='Ontem eu achei o museu.', why='Passado irregular de find: found.'),
  dict(scene='O Leo mostra o mapa.', en='Leo ___ the map to Mia.', opts=['show', 'shows', 'showed'], ans=1, pt='O Leo mostra o mapa para a Mia.', why='Ele (3ª pessoa) leva -s no presente: shows.'),
  dict(scene='Você quer provar a comida local.', en='I want to ___ a cheesesteak.', opts=['try', 'tries', 'tried'], ans=0, pt='Quero experimentar um cheesesteak.', why='Depois de to, use o verbo base: try.')],
 expressions=[
  dict(en='What can I see in one day?', pt='O que posso ver em um dia?', ex='Hi. What can I see in one day?', exp='Para pedir um roteiro curto.', c='a'),
  dict(en='Is it free?', pt='É de graça?', ex='Is it free? — Yes, it is.', exp='Para perguntar se há cobrança.', c='b'),
  dict(en='a local favorite', pt='o preferido de quem mora ali', ex='It is a local favorite.', exp='Para falar de um lugar ou prato querido pela região.', c='c'),
  dict(en='Do you have a map?', pt='Vocês têm mapa?', ex='Great idea. Do you have a map?', exp='Para pedir um mapa no balcão.', c='d'),
  dict(en='Enjoy your day!', pt='Aproveite o seu dia!', ex='Thanks! Enjoy your day!', exp='Despedida simpática.', c='a'),
  dict(en='a must-see', pt='imperdível', ex='This place is a must-see.', exp='Para dizer que um lugar vale muito a visita.', c='b')],
 expr_game=[
  dict(cue='Você quer saber se o ingresso tem custo.', opts=['Is it free?', 'Enjoy your day!', 'Do you have a map?'], ans=0, why='Is it free? pergunta sobre o preço.'),
  dict(cue='Você quer um mapa de papel.', opts=['Do you have a map?', 'What can I see in one day?', 'a local favorite'], ans=0, why='Do you have a...? pede um objeto.'),
  dict(cue='Você quer dizer que o lugar é imperdível.', opts=['It is a must-see.', 'Is it free?', 'Enjoy your day!'], ans=0, why='A must-see = imperdível.')])
