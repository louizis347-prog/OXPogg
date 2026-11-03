"""Bloco de verbos e expressões da aula 143: San Francisco com neblina."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('ride', '🚋', 'andar (de bondinho, bicicleta)', ('ride', 'We ride the cable car.', 'Nós andamos de bondinho.'), ('rides', 'Mei rides a bike.', 'A Mei anda de bicicleta.'), ('rode', 'We rode up the hill.', 'Nós subimos a ladeira de bondinho.'), ('riding', 'We are riding now.', 'Estamos andando agora.'), 'Ride é irregular: rode no passado. Perde o e antes de -ing: riding.'),
  vb('catch', '🎯', 'pegar (um transporte)', ('catch', 'We catch the cable car here.', 'Nós pegamos o bondinho aqui.'), ('catches', 'Tom catches the bus.', 'O Tom pega o ônibus.'), ('caught', 'We caught the last one.', 'Nós pegamos o último.'), ('catching', 'We are catching the bus.', 'Estamos pegando o ônibus.'), 'Catch é irregular: caught. Em catches, o final é -es.'),
  vb('climb', '🧗', 'subir', ('climb', 'We climb the hill.', 'Nós subimos a ladeira.'), ('climbs', 'The street climbs fast.', 'A rua sobe rápido.'), ('climbed', 'We climbed the stairs.', 'Nós subimos as escadas.'), ('climbing', 'We are climbing now.', 'Estamos subindo agora.'), 'O b de climb é mudo: soa “claim”.'),
  vb('shiver', '🥶', 'tremer de frio', ('shiver', 'I shiver in the wind.', 'Eu tremo de frio no vento.'), ('shivers', 'Tom shivers a little.', 'O Tom treme um pouco de frio.'), ('shivered', 'He shivered all morning.', 'Ele tremeu de frio a manhã toda.'), ('shivering', 'I am shivering now.', 'Estou tremendo de frio agora.'), 'Use quando o frio é forte. Passado regular: shivered.'),
  vb('lend', '🧥', 'emprestar', ('lend', 'I lend you my jacket.', 'Eu empresto a você meu casaco.'), ('lends', 'Mei lends a jacket.', 'A Mei empresta um casaco.'), ('lent', 'She lent me her scarf.', 'Ela me emprestou o cachecol.'), ('lending', 'I am lending my pen.', 'Estou emprestando minha caneta.'), 'Lend é irregular: lent. Para pedir, diga: Can I borrow…?')],
 verb_game=[
  dict(scene='Agora vocês estão subindo a ladeira.', en='We are ___ the hill.', opts=['climb', 'climbing', 'climbed'], ans=1, pt='Estamos subindo a ladeira.', why='“are” + -ing: climbing.'),
  dict(scene='Ontem a Mei emprestou o casaco.', en='Yesterday Mei ___ me her jacket.', opts=['lends', 'lent', 'lending'], ans=1, pt='Ontem a Mei me emprestou o casaco.', why='Passado irregular: lent.'),
  dict(scene='O Tom pega o bondinho todo dia.', en='Tom ___ the cable car every day.', opts=['catch', 'catches', 'caught'], ans=1, pt='O Tom pega o bondinho todo dia.', why='Ele (3ª pessoa) leva -es: catches.'),
  dict(scene='Você quer andar de bondinho.', en='I want to ___ the cable car.', opts=['ride', 'rides', 'rode'], ans=0, pt='Quero andar de bondinho.', why='Depois de to, use o verbo base: ride.')],
 expressions=[
  dict(en='It’s so foggy today.', pt='Está tão nublado hoje.', ex='Good morning! It’s so foggy today.', exp='Para comentar a neblina.', c='a'),
  dict(en='It’s chilly.', pt='Está friozinho.', ex='It’s chilly. Do you have a jacket?', exp='Para falar de um frio leve.', c='b'),
  dict(en='Not right now.', pt='Agora não.', ex='Can we see the bridge? Not right now.', exp='Para dizer que ainda não dá.', c='c'),
  dict(en='Take my jacket.', pt='Pegue meu casaco.', ex='You’re cold? Take my jacket.', exp='Para emprestar roupa a alguém com frio.', c='d'),
  dict(en='You’re kind.', pt='Você é gentil.', ex='Thanks. You’re kind.', exp='Para agradecer um gesto de gentileza.', c='a'),
  dict(en='Look at that view!', pt='Olhe essa vista!', ex='Wow! Look at that view!', exp='Para admirar uma paisagem.', c='b')],
 expr_game=[
  dict(cue='Você quer emprestar seu casaco a um amigo com frio.', opts=['Take my jacket.', 'Not right now.', 'Look at that view!'], ans=0, why='Take my jacket oferece o casaco.'),
  dict(cue='Perguntam se dá para ver a ponte, e ainda não dá.', opts=['Not right now.', 'You’re kind.', 'It’s chilly.'], ans=0, why='Not right now = agora não.'),
  dict(cue='Alguém te emprestou um casaco e você agradece.', opts=['Thanks. You’re kind.', 'It’s so foggy today.', 'Not right now.'], ans=0, why='You’re kind agradece uma gentileza.')])
