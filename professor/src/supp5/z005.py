"""Bloco de verbos e expressões da aula 5."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('come', '🧳', 'vir', ('come', 'I come from Brazil.', 'Eu venho do Brasil.'), ('comes', 'Aisha comes from Atlanta.', 'A Aisha vem de Atlanta.'), ('came', 'My family came from Bahia.', 'Minha família veio da Bahia.'), ('coming', 'I am coming from São Paulo.', 'Estou vindo de São Paulo.'), 'Irregular: come vira came. Come from = ser de.'),
  vb('speak', '🗣️', 'falar', ('speak', 'I speak Portuguese.', 'Eu falo português.'), ('speaks', 'Aisha speaks French.', 'A Aisha fala francês.'), ('spoke', 'We spoke English.', 'Nós falamos inglês.'), ('speaking', 'I am speaking slowly.', 'Estou falando devagar.'), 'Irregular: speak vira spoke. Speak + idioma, sem “the”.'),
  vb('live', '🏠', 'morar', ('live', 'I live in Chicago.', 'Eu moro em Chicago.'), ('lives', 'Aisha lives in Boston.', 'A Aisha mora em Boston.'), ('lived', 'They lived in Rio.', 'Eles moraram no Rio.'), ('living', 'I am living in Atlanta.', 'Estou morando em Atlanta.'), 'Live in + cidade: live in Boston.'),
  vb('love', '❤️', 'amar / adorar', ('love', 'I love Brazilian food.', 'Eu adoro comida brasileira.'), ('loves', 'Aisha loves Brazilian music.', 'A Aisha adora música brasileira.'), ('loved', 'We loved the trip.', 'Nós adoramos a viagem.'), ('loving', 'I am loving this city.', 'Estou adorando esta cidade.'), 'Love é mais forte que like; passado só com -d.'),
  vb('learn', '📚', 'aprender', ('learn', 'I learn English here.', 'Eu aprendo inglês aqui.'), ('learns', 'Aisha learns Portuguese.', 'A Aisha aprende português.'), ('learned', 'He learned French.', 'Ele aprendeu francês.'), ('learning', 'I am learning Spanish.', 'Estou aprendendo espanhol.'), 'Learn + idioma: learn English. Passado: learned.')],
 verb_game=[
  dict(scene='Você diz de onde é.', en='I ___ from Brazil.', opts=['come', 'comes', 'came'], ans=0, pt='Eu sou do Brasil.', why='Com “I” o presente fica na forma base: come.'),
  dict(scene='A Aisha é de Atlanta.', en='Aisha ___ from Atlanta.', opts=['come', 'comes', 'coming'], ans=1, pt='A Aisha é de Atlanta.', why='Com “Aisha” (ela) o presente leva -s: comes.'),
  dict(scene='Você fala português e inglês.', en='I ___ Portuguese and English.', opts=['spoke', 'speaking', 'speak'], ans=2, pt='Eu falo português e inglês.', why='Presente com “I”: speak.'),
  dict(scene='Agora você está aprendendo espanhol.', en='I am ___ Spanish.', opts=['learning', 'learn', 'learns'], ans=0, pt='Estou aprendendo espanhol.', why='“am” + verbo termina em -ing: learning.')],
 expressions=[
  dict(en='Where are you from?', pt='De onde você é?', ex='Where are you from?', exp='Para perguntar a origem de alguém.', c='a'),
  dict(en='I’m from…', pt='Eu sou de…', ex='I’m from Brazil.', exp='Para dizer de onde você é.', c='b'),
  dict(en='Do you speak…?', pt='Você fala…?', ex='Do you speak Portuguese?', exp='Para perguntar sobre um idioma.', c='c'),
  dict(en='a little', pt='um pouco', ex='I speak a little French.', exp='Para dizer que você fala só um pouco.', c='d'),
  dict(en='come from', pt='vir de / ser de', ex='My family comes from Bahia.', exp='Verbo frasal: indicar a origem.', c='a'),
  dict(en='And you?', pt='E você?', ex='I’m from Brazil. And you?', exp='Para devolver a pergunta.', c='b')],
 expr_game=[
  dict(cue='Você quer saber a origem da pessoa.', opts=['Where are you from?', 'I speak a little.', 'And you?'], ans=0, why='Where are you from? pergunta a origem.'),
  dict(cue='Você quer saber se ela fala português.', opts=['Where is your family?', 'Do you speak Portuguese?', 'I’m from Brazil.'], ans=1, why='Do you speak…? pergunta sobre idiomas.'),
  dict(cue='Você fala só um pouco de francês.', opts=['I speak a little French.', 'I’m from France.', 'Do you speak French?'], ans=0, why='A little significa “um pouco”.')])
