K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('open', '🚪', 'abrir', ('open', 'I open the drawer.', 'Eu abro a gaveta.'), ('opens', 'Jonah opens the cabinet.', 'O Jonah abre o armário.'), ('opened', 'She opened the oven.', 'Ela abriu o forno.'), ('opening', 'I am opening the fridge.', 'Estou abrindo a geladeira.'), 'Regular: open, opened, opening.'),
  vb('stir', '🥄', 'mexer', ('stir', 'I stir the soup.', 'Eu mexo a sopa.'), ('stirs', 'Tara stirs the pasta.', 'A Tara mexe o macarrão.'), ('stirred', 'He stirred the rice.', 'Ele mexeu o arroz.'), ('stirring', 'I am stirring the sauce.', 'Estou mexendo o molho.'), 'No -ed e no -ing, dobre o r: stirred, stirring.'),
  vb('boil', '♨️', 'ferver', ('boil', 'We boil water for tea.', 'Nós fervemos água para o chá.'), ('boils', 'The kettle boils fast.', 'A chaleira ferve rápido.'), ('boiled', 'I boiled two eggs.', 'Eu fervi dois ovos.'), ('boiling', 'The water is boiling.', 'A água está fervendo.'), 'Boil serve para água, ovos e macarrão.'),
  vb('heat', '🔥', 'esquentar', ('heat', 'I heat the pan.', 'Eu esquento a panela.'), ('heats', 'Tara heats the milk.', 'A Tara esquenta o leite.'), ('heated', 'He heated the soup.', 'Ele esquentou a sopa.'), ('heating', 'I am heating the oven.', 'Estou esquentando o forno.'), 'Heat up = esquentar algo que estava frio.'),
  vb('pour', '🫗', 'despejar / servir', ('pour', 'I pour water in the pan.', 'Eu despejo água na panela.'), ('pours', 'Jonah pours the tea.', 'O Jonah serve o chá.'), ('poured', 'She poured the milk.', 'Ela serviu o leite.'), ('pouring', 'I am pouring the juice.', 'Estou servindo o suco.'), 'Pour é para líquidos: água, chá, leite.')],
 verb_game=[
  dict(scene='Tara põe o macarrão na água quente e mexe.', en='Tara ___ the pasta.', opts=['stir', 'stirs', 'stirring'], ans=1, pt='A Tara mexe o macarrão.', why='Com “Tara” (ela), o presente leva -s: stirs.'),
  dict(scene='Agora o Jonah está abrindo a gaveta.', en='Jonah is ___ the drawer.', opts=['open', 'opens', 'opening'], ans=2, pt='O Jonah está abrindo a gaveta.', why='“is” + verbo termina em -ing: opening.'),
  dict(scene='Ontem você ferveu dois ovos.', en='Yesterday I ___ two eggs.', opts=['boil', 'boiled', 'boiling'], ans=1, pt='Ontem eu fervi dois ovos.', why='“Yesterday” pede passado: boiled.'),
  dict(scene='Vocês esquentam a panela todo dia.', en='We ___ the pan every day.', opts=['heat', 'heats', 'heated'], ans=0, pt='Nós esquentamos a panela todo dia.', why='Com “we” o presente fica na forma base: heat.')],
 expressions=[
  dict(en='Can I help you?', pt='Posso ajudar você?', ex='Can I help you in the kitchen?', exp='Para oferecer ajuda a um amigo.', c='a'),
  dict(en='Where is…? / Where are…?', pt='Onde está…? / Onde ficam…?', ex='Where are the forks?', exp='Is para uma coisa, are para várias.', c='b'),
  dict(en='Make yourself at home.', pt='Fique à vontade.', ex='Come in! Make yourself at home.', exp='O anfitrião diz isso ao receber alguém.', c='c'),
  dict(en='Help yourself.', pt='Sirva-se.', ex='Help yourself to some bread.', exp='Para oferecer comida ou bebida.', c='d'),
  dict(en='get… from', pt='pegar… em', ex='Get a plate from the cabinet.', exp='Para pedir que alguém pegue algo de um lugar.', c='a'),
  dict(en='You\'re too kind.', pt='Você é gentil demais.', ex='Thanks, you\'re too kind.', exp='Resposta educada a um elogio ou favor.', c='b')],
 expr_game=[
  dict(cue='Você quer saber onde estão as colheres.', opts=['Where are the spoons?', 'Make yourself at home.', 'Help yourself.'], ans=0, why='Where are… pergunta onde ficam várias coisas.'),
  dict(cue='Você chega e o amigo quer que você relaxe.', opts=['Where is the salt?', 'Make yourself at home.', 'Get a plate.'], ans=1, why='Make yourself at home é o convite para ficar à vontade.'),
  dict(cue='Você quer oferecer ajuda na cozinha.', opts=['Can I help you?', 'It\'s under the stove.', 'You\'re too kind.'], ans=0, why='Can I help you? oferece ajuda.')])
