"""Bloco de verbos e expressões da aula 7."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('turn', '🎂', 'completar (idade)', ('turn', 'I turn thirty in June.', 'Eu faço trinta anos em junho.'), ('turns', 'Omar turns forty soon.', 'O Omar faz quarenta anos logo.'), ('turned', 'She turned twenty-nine.', 'Ela fez vinte e nove anos.'), ('turning', 'I am turning thirty-one.', 'Estou fazendo trinta e um anos.'), 'Turn + idade: I’m turning thirty = vou fazer trinta.'),
  vb('send', '💌', 'mandar / enviar', ('send', 'I send cards to my friends.', 'Eu mando cartões para meus amigos.'), ('sends', 'Omar sends a text.', 'O Omar manda uma mensagem.'), ('sent', 'She sent a gift.', 'Ela mandou um presente.'), ('sending', 'I am sending a card.', 'Estou mandando um cartão.'), 'Passado irregular: send vira sent.'),
  vb('have', '🍰', 'ter / fazer', ('have', 'I have a party in May.', 'Eu faço uma festa em maio.'), ('has', 'She has a birthday in June.', 'O aniversário dela é em junho.'), ('had', 'We had a big party.', 'Nós fizemos uma festa grande.'), ('having', 'I am having a party.', 'Estou fazendo uma festa.'), 'Have a party = fazer festa. Passado: had.'),
  vb('get', '🎁', 'ganhar / ficar', ('get', 'I get a gift.', 'Eu ganho um presente.'), ('gets', 'Omar gets a cake.', 'O Omar ganha um bolo.'), ('got', 'She got flowers.', 'Ela ganhou flores.'), ('getting', 'I am getting older.', 'Estou ficando mais velho.'), 'Get a gift = ganhar presente. Passado: got.'),
  vb('invite', '💌', 'convidar', ('invite', 'I invite my friends.', 'Eu convido meus amigos.'), ('invites', 'Omar invites his sister.', 'O Omar convida a irmã.'), ('invited', 'We invited you.', 'Nós convidamos você.'), ('inviting', 'I am inviting everyone.', 'Estou convidando todo mundo.'), 'Passado só com -d: invited.')],
 verb_game=[
  dict(scene='Seu aniversário de 31 anos está chegando.', en='I am ___ thirty-one in June.', opts=['turn', 'turning', 'turned'], ans=1, pt='Vou fazer trinta e um anos em junho.', why='“am” + verbo termina em -ing: turning.'),
  dict(scene='O Omar convida a irmã para a festa.', en='Omar ___ his sister.', opts=['invite', 'invites', 'invited'], ans=1, pt='O Omar convida a irmã dele.', why='Com “Omar” (ele) o presente leva -s: invites.'),
  dict(scene='Ontem ela ganhou flores.', en='Yesterday she ___ flowers.', opts=['gets', 'getting', 'got'], ans=2, pt='Ontem ela ganhou flores.', why='“Yesterday” pede passado irregular: got.'),
  dict(scene='Vocês fazem uma festa em maio.', en='We ___ a party in May.', opts=['have', 'has', 'had'], ans=0, pt='Nós fazemos uma festa em maio.', why='Com “we” o presente fica na forma base: have.')],
 expressions=[
  dict(en='How old are you?', pt='Quantos anos você tem?', ex='How old are you?', exp='Para perguntar a idade (com cuidado).', c='a'),
  dict(en='I’m thirty.', pt='Eu tenho trinta anos.', ex='I’m thirty years old.', exp='Em inglês a idade usa “be”, não “have”.', c='b'),
  dict(en='My birthday is in…', pt='Meu aniversário é em…', ex='My birthday is in June.', exp='Para dizer o mês do aniversário.', c='c'),
  dict(en='Happy birthday!', pt='Feliz aniversário!', ex='Happy birthday, Omar!', exp='Para parabenizar no dia.', c='d'),
  dict(en='Happy early birthday!', pt='Feliz aniversário adiantado!', ex='Happy early birthday!', exp='Quando o aniversário ainda não chegou.', c='a'),
  dict(en='have a party', pt='fazer uma festa', ex='I have a party in May.', exp='Verbo frasal: organizar uma festa.', c='b')],
 expr_game=[
  dict(cue='Você quer saber a idade do Omar.', opts=['How old are you?', 'Happy birthday!', 'My birthday is in May.'], ans=0, why='How old are you? pergunta a idade.'),
  dict(cue='Hoje é aniversário do seu vizinho.', opts=['I’m thirty.', 'Happy birthday!', 'How old are you?'], ans=1, why='Happy birthday! parabeniza no dia.'),
  dict(cue='Você quer dizer o mês do seu aniversário.', opts=['My birthday is in June.', 'I’m thirty.', 'Happy birthday!'], ans=0, why='My birthday is in + mês.')])
