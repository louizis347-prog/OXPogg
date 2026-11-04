"""Bloco de verbos e expressões da aula 194: dia de neve em casa."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('build', '🏗️', 'construir / fazer', ('build', 'We build a snowman.', 'Nós fazemos um boneco de neve.'), ('builds', 'Lily builds a small hill.', 'A Lily faz uma pequena colina.'), ('built', 'They built a big snowman.', 'Eles fizeram um boneco de neve grande.'), ('building', 'I am building a snow fort.', 'Estou fazendo um forte de neve.'), 'Build é irregular: built no passado.'),
  vb('cover', '🛏️', 'cobrir', ('cover', 'Snow covers the street.', 'A neve cobre a rua.'), ('covers', 'Snow covers the car.', 'A neve cobre o carro.'), ('covered', 'Snow covered the yard.', 'A neve cobriu o quintal.'), ('covering', 'Snow is covering the roof.', 'A neve está cobrindo o telhado.'), 'Cover é regular. Be covered with snow = estar coberto de neve.'),
  vb('melt', '💧', 'derreter', ('melt', 'Snow melts in the sun.', 'A neve derrete ao sol.'), ('melts', 'The snow melts fast.', 'A neve derrete rápido.'), ('melted', 'The ice melted.', 'O gelo derreteu.'), ('melting', 'The snowman is melting.', 'O boneco de neve está derretendo.'), 'Melt é regular: melted. Em geral não se usa com pessoas.'),
  vb('slide', '🛷', 'deslizar', ('slide', 'We slide down the hill.', 'Nós deslizamos pela colina.'), ('slides', 'Tom slides on the sled.', 'O Tom desliza no trenó.'), ('slid', 'I slid on the ice.', 'Eu escorreguei no gelo.'), ('sliding', 'The kids are sliding.', 'As crianças estão deslizando.'), 'Slide é irregular: slid. Perde o e antes de -ing: sliding.'),
  vb('throw', '❄️', 'jogar / atirar', ('throw', 'We throw snowballs.', 'Nós jogamos bolas de neve.'), ('throws', 'Lily throws a snowball.', 'A Lily joga uma bola de neve.'), ('threw', 'He threw a snowball.', 'Ele jogou uma bola de neve.'), ('throwing', 'They are throwing snowballs.', 'Eles estão jogando bolas de neve.'), 'Throw é irregular: threw no passado.')],
 verb_game=[
  dict(scene='Ontem eles fizeram um boneco de neve grande.', en='Yesterday they ___ a big snowman.', opts=['build', 'built', 'building'], ans=1, pt='Ontem eles fizeram um boneco de neve grande.', why='“Yesterday” pede passado irregular: built.'),
  dict(scene='Agora o boneco de neve está derretendo.', en='The snowman is ___.', opts=['melt', 'melts', 'melting'], ans=2, pt='O boneco de neve está derretendo.', why='“is” + verbo termina em -ing: melting.'),
  dict(scene='A Lily joga bolas de neve.', en='Lily ___ snowballs.', opts=['throw', 'throws', 'threw'], ans=1, pt='A Lily joga bolas de neve.', why='Com “Lily” (ela), o presente leva -s: throws.'),
  dict(scene='Nós deslizamos pela colina.', en='We ___ down the hill.', opts=['slide', 'slides', 'slid'], ans=0, pt='Nós deslizamos pela colina.', why='Com “we”, o presente fica na forma base: slide.')],
 expressions=[
  dict(en='Look outside!', pt='Olha lá fora!', ex='Look outside! It’s white!', exp='Para chamar a atenção de alguém para algo fora de casa.', c='a'),
  dict(en='snow day', pt='dia de neve', ex='Today is a snow day.', exp='Dia em que a escola ou o trabalho fecha por causa da neve.', c='b'),
  dict(en='put on', pt='vestir', ex='Put on your coat.', exp='Verbo frasal: vestir uma roupa.', c='c'),
  dict(en='take off', pt='tirar (roupa)', ex='Take off your wet boots.', exp='Verbo frasal: tirar uma roupa.', c='d'),
  dict(en='Bundle up!', pt='Agasalhe-se!', ex='It’s freezing. Bundle up!', exp='Para pedir que alguém vista roupas quentes.', c='a'),
  dict(en='Let’s build a snowman.', pt='Vamos fazer um boneco de neve.', ex='It’s a snow day! Let’s build a snowman.', exp='Para sugerir uma brincadeira.', c='b')],
 expr_game=[
  dict(cue='Você quer pedir que o irmão se agasalhe.', opts=['Bundle up!', 'Look outside!', 'Take off your boots.'], ans=0, why='Bundle up! pede para vestir roupas quentes.'),
  dict(cue='Você chegou em casa e quer tirar as botas molhadas.', opts=['Put on your boots.', 'Take off your boots.', 'Look outside!'], ans=1, why='Take off = tirar a roupa.'),
  dict(cue='Você quer sugerir uma brincadeira de neve.', opts=['Let’s build a snowman.', 'Bundle up!', 'Take off your coat.'], ans=0, why='Let’s + verbo sugere uma ideia.')])
