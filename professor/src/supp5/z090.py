"""Bloco de verbos e expressões da aula 090: no museu."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('visit', '🏛️', 'visitar', ('visit', 'We visit the museum today.', 'Nós visitamos o museu hoje.'), ('visits', 'Gina visits a gallery.', 'A Gina visita uma galeria.'), ('visited', 'I visited an art museum.', 'Eu visitei um museu de arte.'), ('visiting', 'We are visiting Los Angeles.', 'Estamos visitando Los Angeles.'), 'Visit é verbo direto: visit the museum (sem preposição).'),
  vb('learn', '📚', 'aprender', ('learn', 'I learn about art here.', 'Eu aprendo sobre arte aqui.'), ('learns', 'Marco learns two names.', 'O Marco aprende dois nomes.'), ('learned', 'We learned a lot.', 'Nós aprendemos muito.'), ('learning', 'I am learning about painters.', 'Estou aprendendo sobre pintores.'), 'Learn about = aprender sobre algo.'),
  vb('paint', '🖌️', 'pintar', ('paint', 'Artists paint every day.', 'Artistas pintam todo dia.'), ('paints', 'Gina paints at home.', 'A Gina pinta em casa.'), ('painted', 'Van Gogh painted the sky.', 'Van Gogh pintou o céu.'), ('painting', 'She is painting a tree.', 'Ela está pintando uma árvore.'), 'Painting também é o substantivo “quadro, pintura”.'),
  vb('buy', '🎟️', 'comprar', ('buy', 'We buy two tickets.', 'Nós compramos dois ingressos.'), ('buys', 'Marco buys a map.', 'O Marco compra um mapa.'), ('bought', 'Gina bought a card.', 'A Gina comprou um cartão.'), ('buying', 'I am buying tickets.', 'Estou comprando ingressos.'), 'Buy é irregular: bought no passado.'),
  vb('walk', '🚶', 'andar / caminhar', ('walk', 'We walk slowly.', 'Nós andamos devagar.'), ('walks', 'Marco walks to the gift shop.', 'O Marco anda até a lojinha.'), ('walked', 'They walked to the second floor.', 'Eles caminharam até o segundo andar.'), ('walking', 'I am walking in the museum.', 'Estou andando pelo museu.'), 'Walk to = andar até um lugar. Passado regular: walked.')],
 verb_game=[
  dict(scene='A Gina compra um cartão na lojinha.', en='Gina ___ a card at the shop.', opts=['buy', 'buys', 'bought'], ans=1, pt='A Gina compra um cartão na lojinha.', why='Com “Gina” (ela), o presente leva -s: buys.'),
  dict(scene='Ontem vocês visitaram um museu.', en='Yesterday we ___ a museum.', opts=['visit', 'visited', 'visiting'], ans=1, pt='Ontem nós visitamos um museu.', why='“Yesterday” pede passado: visited.'),
  dict(scene='Agora o Marco está aprendendo sobre arte.', en='Marco is ___ about art.', opts=['learn', 'learns', 'learning'], ans=2, pt='O Marco está aprendendo sobre arte.', why='“is” + verbo termina em -ing: learning.'),
  dict(scene='Vocês andam devagar entre os quadros.', en='We ___ slowly in the museum.', opts=['walk', 'walks', 'walked'], ans=0, pt='Nós andamos devagar no museu.', why='Com “we”, o presente fica na forma base: walk.')],
 expressions=[
  dict(en='Two tickets, please.', pt='Dois ingressos, por favor.', ex='Hi! Two tickets, please.', exp='Para pedir ingressos na bilheteria.', c='a'),
  dict(en='Students get a discount.', pt='Estudantes têm desconto.', ex='Students get a discount here.', exp='Para falar do preço especial de estudante.', c='b'),
  dict(en='I have a student card.', pt='Tenho carteirinha de estudante.', ex='I have a student card. Here it is.', exp='Para pedir o desconto de estudante.', c='c'),
  dict(en='What time does it close?', pt='Que horas fecha?', ex='What time does the museum close?', exp='Para saber o horário de fechamento.', c='d'),
  dict(en='Can I take photos?', pt='Posso tirar fotos?', ex='Excuse me, can I take photos?', exp='Para pedir permissão antes de fotografar.', c='a'),
  dict(en='No flash.', pt='Sem flash.', ex='Yes, but no flash, please.', exp='Para dizer ou entender a regra da luz da câmera.', c='b')],
 expr_game=[
  dict(cue='Você quer saber até que horas pode ficar no museu.', opts=['What time does it close?', 'No flash.', 'Two tickets, please.'], ans=0, why='What time does it close? pergunta o fechamento.'),
  dict(cue='Você quer pedir o preço de estudante.', opts=['Can I take photos?', 'I have a student card.', 'No flash.'], ans=1, why='I have a student card diz que você pode ter o desconto.'),
  dict(cue='Você quer fotografar um quadro e precisa de permissão.', opts=['Two tickets, please.', 'Can I take photos?', 'What time does it close?'], ans=1, why='Can I…? pede permissão.')])
