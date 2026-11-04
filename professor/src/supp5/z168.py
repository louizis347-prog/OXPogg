"""Bloco de verbos e expressões da aula 168: controle de passaportes."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('answer', '💬', 'responder', ('answer', 'I answer the questions.', 'Eu respondo às perguntas.'), ('answers', 'Lia answers the officer.', 'A Lia responde ao oficial.'), ('answered', 'I answered in English.', 'Eu respondi em inglês.'), ('answering', 'I am answering the officer.', 'Estou respondendo ao oficial.'), 'Answer a pessoa: answer the officer. Passado regular: answered.'),
  vb('stay', '🛏️', 'ficar, hospedar-se', ('stay', 'I stay at a hotel.', 'Eu fico em um hotel.'), ('stays', 'Lia stays in Midtown.', 'A Lia fica em Midtown.'), ('stayed', 'We stayed for a week.', 'Nós ficamos uma semana.'), ('staying', 'I am staying at a hotel.', 'Estou hospedada em um hotel.'), 'Stay at + hotel; stay for + tempo.'),
  vb('arrive', '🛬', 'chegar', ('arrive', 'We arrive in Atlanta at noon.', 'Nós chegamos a Atlanta ao meio-dia.'), ('arrives', 'The flight arrives at six.', 'O voo chega às seis.'), ('arrived', 'I arrived this morning.', 'Eu cheguei hoje de manhã.'), ('arriving', 'We are arriving now.', 'Estamos chegando agora.'), 'Arrive in + cidade; arrive at + lugar pequeno.'),
  vb('fly', '✈️', 'voar', ('fly', 'I fly to Atlanta.', 'Eu voo para Atlanta.'), ('flies', 'She flies on Friday.', 'Ela voa na sexta.'), ('flew', 'We flew all night.', 'Nós voamos a noite toda.'), ('flying', 'I am flying to the USA.', 'Estou voando para os EUA.'), 'Fly é irregular: flew. A 3ª pessoa é flies.'),
  vb('visit', '📍', 'visitar', ('visit', 'I visit a friend.', 'Eu visito um amigo.'), ('visits', 'Lia visits Atlanta.', 'A Lia visita Atlanta.'), ('visited', 'We visited a museum.', 'Nós visitamos um museu.'), ('visiting', 'I am visiting the USA.', 'Estou visitando os EUA.'), 'Visit serve para lugares e pessoas.')],
 verb_game=[
  dict(scene='Você está viajando para os EUA agora.', en='I am ___ to Atlanta.', opts=['fly', 'flew', 'flying'], ans=2, pt='Estou voando para Atlanta.', why='Am + -ing: flying.'),
  dict(scene='A Lia responde ao oficial.', en='Lia ___ the questions.', opts=['answer', 'answers', 'answering'], ans=1, pt='A Lia responde às perguntas.', why='Ela (3ª pessoa) leva -s: answers.'),
  dict(scene='Você diz onde vai ficar duas semanas.', en='I will ___ at a hotel.', opts=['stay', 'stays', 'stayed'], ans=0, pt='Vou ficar em um hotel.', why='Depois de will, use o verbo base: stay.'),
  dict(scene='Seu voo chegou hoje de manhã.', en='We ___ this morning.', opts=['arrive', 'arrived', 'arriving'], ans=1, pt='Nós chegamos hoje de manhã.', why='This morning (já passou) pede passado: arrived.')],
 expressions=[
  dict(en='Here you go.', pt='Aqui está.', ex='Passport? — Here you go.', exp='Para entregar um documento.', c='a'),
  dict(en='I’m here on vacation.', pt='Estou aqui de férias.', ex='Tourism. I’m here on vacation.', exp='Para dizer o motivo da viagem.', c='b'),
  dict(en='How long will you stay?', pt='Quanto tempo vai ficar?', ex='How long will you stay? — Two weeks.', exp='Pergunta sobre a duração da estadia.', c='c'),
  dict(en='for two weeks', pt='por duas semanas', ex='I’ll stay for two weeks.', exp='Para dizer a duração.', c='d'),
  dict(en='a return ticket', pt='uma passagem de volta', ex='I have a return ticket.', exp='Para falar da passagem de volta.', c='a'),
  dict(en='Welcome to the USA!', pt='Bem-vindo aos EUA!', ex='Welcome to the USA! Enjoy your trip.', exp='Saudação ao entrar no país.', c='b')],
 expr_game=[
  dict(cue='O oficial pede o passaporte.', opts=['Here you go.', 'Two weeks.', 'At a hotel.'], ans=0, why='Here you go = aqui está.'),
  dict(cue='Você explica que viaja de férias.', opts=['Welcome to the USA!', 'I’m here on vacation.', 'a return ticket'], ans=1, why='I’m here on vacation diz o motivo.'),
  dict(cue='Você quer dizer a duração da viagem.', opts=['for two weeks', 'Here you go.', 'a return ticket'], ans=0, why='For + tempo diz por quanto tempo.')])
