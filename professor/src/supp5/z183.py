"""Bloco de verbos e expressões da aula 183: celular perdido."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('lose', '😟', 'perder', ('lose', 'I lose things a lot.', 'Eu perco coisas com frequência.'), ('loses', 'Dee loses her keys.', 'A Dee perde as chaves.'), ('lost', 'I lost my phone.', 'Perdi meu celular.'), ('losing', 'I am losing my pen.', 'Estou perdendo minha caneta.'), 'Passado irregular: lose vira lost.'),
  vb('remember', '🧠', 'lembrar', ('remember', 'I remember the train.', 'Eu me lembro do trem.'), ('remembers', 'She remembers the seat.', 'Ela se lembra do assento.'), ('remembered', 'He remembered the color.', 'Ele lembrou a cor.'), ('remembering', 'I am remembering now.', 'Estou me lembrando agora.'), 'Remember não leva “me”: I remember.'),
  vb('search', '🔎', 'procurar', ('search', 'We search the bag.', 'Nós procuramos na bolsa.'), ('searches', 'Evan searches the desk.', 'O Evan procura na mesa.'), ('searched', 'I searched my pockets.', 'Procurei nos bolsos.'), ('searching', 'She is searching now.', 'Ela está procurando agora.'), 'Search = procurar com cuidado em um lugar.'),
  vb('look', '👀', 'olhar, parecer', ('look', 'I look at the clock.', 'Eu olho o relógio.'), ('looks', 'It looks new.', 'Parece novo.'), ('looked', 'We looked everywhere.', 'Procuramos em todo lugar.'), ('looking', 'I am looking for my phone.', 'Estou procurando meu celular.'), 'Look at = olhar; look for = procurar; look like = parecer com.'),
  vb('leave', '🚪', 'deixar, sair', ('leave', 'I leave at five.', 'Eu saio às cinco.'), ('leaves', 'The train leaves now.', 'O trem sai agora.'), ('left', 'I left it on the seat.', 'Deixei no assento.'), ('leaving', 'We are leaving soon.', 'Estamos saindo logo.'), 'Passado irregular: leave vira left. Também significa deixar algo para trás.')],
 verb_game=[
  dict(scene='Ontem você perdeu o celular.', en='Yesterday I ___ my phone.', opts=['lose', 'lost', 'losing'], ans=1, pt='Ontem eu perdi meu celular.', why='Yesterday pede passado: lost.'),
  dict(scene='O Evan procura na mesa agora.', en='Evan ___ the desk.', opts=['search', 'searches', 'searched'], ans=1, pt='O Evan procura na mesa.', why='Com Evan (ele), o presente leva -s: searches.'),
  dict(scene='Você está procurando o celular.', en='I am ___ for my phone.', opts=['look', 'looks', 'looking'], ans=2, pt='Estou procurando meu celular.', why='Am + verbo termina em -ing: looking.'),
  dict(scene='Você deixou o celular no trem.', en='I ___ it on the train.', opts=['leave', 'left', 'leaving'], ans=1, pt='Eu o deixei no trem.', why='O passado de leave é left.')],
 expressions=[
  dict(en='I lost my phone!', pt='Perdi meu celular!', ex='Excuse me, I lost my phone!', exp='Para pedir ajuda com um objeto perdido.', c='a'),
  dict(en='What does it look like?', pt='Como ele é?', ex='What does it look like? — It’s black.', exp='Para pedir uma descrição.', c='b'),
  dict(en='lost and found', pt='achados e perdidos', ex='Let me call the lost and found.', exp='O lugar onde ficam objetos achados.', c='c'),
  dict(en='Thank goodness!', pt='Graças a Deus!', ex='They have it? Thank goodness!', exp='Para mostrar alívio.', c='d'),
  dict(en='Keep an eye on it.', pt='Fique de olho nisso.', ex='Keep an eye on your phone.', exp='Cuidar para não perder.', c='a'),
  dict(en='keep in touch', pt='manter contato', ex='Let’s keep in touch.', exp='Para dizer que vão continuar se falando.', c='b')],
 expr_game=[
  dict(cue='Você quer saber como é o objeto.', opts=['What does it look like?', 'Thank goodness!', 'Keep in touch.'], ans=0, why='What does it look like? pede descrição.'),
  dict(cue='Eles acharam seu celular e você sente alívio.', opts=['Thank goodness!', 'I lost my phone!', 'Lost and found.'], ans=0, why='Thank goodness! mostra alívio.'),
  dict(cue='Você precisa dizer que perdeu algo.', opts=['Keep an eye on it.', 'I lost my phone!', 'What does it look like?'], ans=1, why='I lost… diz que algo foi perdido.')])
