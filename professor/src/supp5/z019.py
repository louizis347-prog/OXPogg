"""Bloco de verbos e expressões da aula 019."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('listen', '🎧', 'ouvir', ('listen', 'I listen to pop.', 'Eu ouço pop.'), ('listens', 'Mia listens to jazz.', 'A Mia ouve jazz.'), ('listened', 'We listened to rock.', 'Nós ouvimos rock.'), ('listening', 'I am listening now.', 'Estou ouvindo agora.'), 'Listen to + música.'),
  vb('sing', '🎤', 'cantar', ('sing', 'I sing in the car.', 'Eu canto no carro.'), ('sings', 'Beyoncé sings well.', 'A Beyoncé canta bem.'), ('sang', 'She sang a song.', 'Ela cantou uma música.'), ('singing', 'I am singing!', 'Estou cantando!'), 'Irregular: sing, sang.'),
  vb('buy', '🎟️', 'comprar', ('buy', 'I buy tickets.', 'Eu compro ingressos.'), ('buys', 'Sam buys two tickets.', 'O Sam compra dois ingressos.'), ('bought', 'I bought tickets.', 'Eu comprei ingressos.'), ('buying', 'I am buying tickets now.', 'Estou comprando ingressos agora.'), 'Irregular: buy, bought.'),
  vb('sit', '💺', 'sentar', ('sit', 'We sit near the stage.', 'Nós sentamos perto do palco.'), ('sits', 'Mia sits in front.', 'A Mia senta na frente.'), ('sat', 'I sat in row five.', 'Eu sentei na fileira cinco.'), ('sitting', 'I am sitting here.', 'Estou sentado aqui.'), 'Passado irregular: sit vira sat; -ing duplica o t.'),
  vb('dance', '💃', 'dançar', ('dance', 'We dance at concerts.', 'Nós dançamos em shows.'), ('dances', 'Raj dances all night.', 'O Raj dança a noite toda.'), ('danced', 'We danced last night.', 'Nós dançamos ontem à noite.'), ('dancing', 'I am dancing to this song.', 'Estou dançando esta música.'), 'Dance + -d no passado: danced.')],
 verb_game=[
  dict(scene='A Mia ouve jazz.', en='Mia ___ to jazz.', opts=['listen', 'listens', 'listened'], ans=1, pt='A Mia ouve jazz.', why='Com “Mia”: listens.'),
  dict(scene='Ontem você comprou ingressos.', en='I ___ tickets yesterday.', opts=['buy', 'buys', 'bought'], ans=2, pt='Eu comprei ingressos ontem.', why='Passado de buy: bought.'),
  dict(scene='Você está cantando agora.', en='I am ___ my favorite song.', opts=['sing', 'sang', 'singing'], ans=2, pt='Estou cantando minha música favorita.', why='“am” + -ing: singing.'),
  dict(scene='Vocês dançam nos shows.', en='We ___ at concerts.', opts=['dance', 'dances', 'danced'], ans=0, pt='Nós dançamos nos shows.', why='Presente com “we”: dance.')],
 expressions=[
  dict(en='What music do you like?', pt='Que música você gosta?', ex='What music do you like?', exp='Perguntar o gosto musical.', c='a'),
  dict(en='Who is your favorite singer?', pt='Quem é seu cantor favorito?', ex='Who is your favorite singer?', exp='Perguntar o favorito.', c='b'),
  dict(en='I love…', pt='Eu adoro…', ex='I love Taylor Swift.', exp='Gosto forte.', c='c'),
  dict(en='Do you have tickets?', pt='Você tem ingressos?', ex='Do you have tickets?', exp='Perguntar sobre ingressos.', c='d'),
  dict(en='They are expensive.', pt='Estão caros.', ex='Not yet. They are expensive.', exp='Falar do preço.', c='a'),
  dict(en='Great idea!', pt='Boa ideia!', ex='Let’s go! — Great idea!', exp='Aceitar uma sugestão.', c='b')],
 expr_game=[
  dict(cue='Você quer saber o cantor favorito dele.', opts=['Who is your favorite singer?', 'Great idea!', 'They are expensive.'], ans=0, why='Favorite = favorito.'),
  dict(cue='Você quer saber se ele já comprou ingressos.', opts=['I love rock.', 'Do you have tickets?', 'Great idea!'], ans=1, why='Do you have…? pergunta posse.'),
  dict(cue='O amigo sugeriu ir ao show e você aceita.', opts=['Great idea!', 'Not yet.', 'What music?'], ans=0, why='Great idea! aceita.')])
