"""Bloco de verbos e expressões da aula 089: acampar."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('camp', '🏕️', 'acampar', ('camp', 'We camp near the trees.', 'Nós acampamos perto das árvores.'), ('camps', 'Eli camps every summer.', 'O Eli acampa todo verão.'), ('camped', 'They camped by a lake.', 'Eles acamparam perto de um lago.'), ('camping', 'We are camping this weekend.', 'Estamos acampando neste fim de semana.'), 'Go camping = ir acampar. Passado regular: camped.'),
  vb('hike', '🥾', 'fazer trilha', ('hike', 'We hike in the morning.', 'Nós fazemos trilha de manhã.'), ('hikes', 'Jonah hikes with a backpack.', 'O Jonah faz trilha com uma mochila.'), ('hiked', 'We hiked two hours.', 'Nós fizemos trilha por duas horas.'), ('hiking', 'I am hiking up the hill.', 'Estou subindo o morro a pé.'), 'Hike é a caminhada longa na natureza. Passado: hiked.'),
  vb('sleep', '😴', 'dormir', ('sleep', 'We sleep in a tent.', 'Nós dormimos numa barraca.'), ('sleeps', 'Eli sleeps well outside.', 'O Eli dorme bem ao ar livre.'), ('slept', 'I slept in a sleeping bag.', 'Eu dormi num saco de dormir.'), ('sleeping', 'Jonah is sleeping now.', 'O Jonah está dormindo agora.'), 'Sleep é irregular: slept no passado.'),
  vb('light', '🔥', 'acender', ('light', 'We light a campfire.', 'Nós acendemos uma fogueira.'), ('lights', 'Jonah lights the wood.', 'O Jonah acende a lenha.'), ('lit', 'Eli lit the fire.', 'O Eli acendeu o fogo.'), ('lighting', 'I am lighting the fire.', 'Estou acendendo o fogo.'), 'Light é irregular: lit no passado. Também é o substantivo “luz”.'),
  vb('cook', '🍳', 'cozinhar', ('cook', 'We cook sausages.', 'Nós cozinhamos salsichas.'), ('cooks', 'Jonah cooks on the fire.', 'O Jonah cozinha na fogueira.'), ('cooked', 'Eli cooked dinner.', 'O Eli preparou o jantar.'), ('cooking', 'I am cooking dinner.', 'Estou preparando o jantar.'), 'Cook dinner = preparar o jantar. Passado regular: cooked.')],
 verb_game=[
  dict(scene='O Eli acampa todo verão.', en='Eli ___ every summer.', opts=['camp', 'camps', 'camped'], ans=1, pt='O Eli acampa todo verão.', why='Com “Eli” (ele), o presente leva -s: camps.'),
  dict(scene='Ontem vocês dormiram numa barraca.', en='Last night we ___ in a tent.', opts=['sleep', 'slept', 'sleeping'], ans=1, pt='Ontem à noite nós dormimos numa barraca.', why='“Last night” pede passado: slept.'),
  dict(scene='Agora o Jonah está acendendo o fogo.', en='Jonah is ___ the fire.', opts=['light', 'lights', 'lighting'], ans=2, pt='O Jonah está acendendo o fogo.', why='“is” + verbo termina em -ing: lighting.'),
  dict(scene='Vocês preparam o jantar na fogueira.', en='We ___ dinner on the fire.', opts=['cook', 'cooks', 'cooked'], ans=0, pt='Nós preparamos o jantar na fogueira.', why='Com “we”, o presente fica na forma base: cook.')],
 expressions=[
  dict(en='Where should we put…?', pt='Onde devemos pôr…?', ex='Where should we put the tent?', exp='Para pedir uma sugestão de lugar.', c='a'),
  dict(en='Is the ground flat?', pt='O chão é plano?', ex='Is the ground flat here?', exp='Para escolher um bom lugar para a barraca.', c='b'),
  dict(en='Let’s build a fire.', pt='Vamos fazer uma fogueira.', ex='It’s cold. Let’s build a fire.', exp='Para propor fazer fogo (onde é permitido).', c='c'),
  dict(en='I’ll get some.', pt='Eu pego (um pouco).', ex='We need water. I’ll get some.', exp='Para oferecer ajuda de forma rápida.', c='d'),
  dict(en='It’s getting dark.', pt='Está escurecendo.', ex='Let’s hurry. It’s getting dark.', exp='Para avisar que a noite está chegando.', c='a'),
  dict(en='Sleep well!', pt='Durma bem!', ex='Good night! Sleep well!', exp='Despedida antes de dormir.', c='b')],
 expr_game=[
  dict(cue='Você quer saber onde armar a barraca.', opts=['Where should we put the tent?', 'Sleep well!', 'I’ll get some.'], ans=0, why='Where should we put…? pede uma sugestão.'),
  dict(cue='Seu amigo diz que precisa de lenha e você vai buscar.', opts=['It’s getting dark.', 'I’ll get some.', 'Is the ground flat?'], ans=1, why='I’ll get some oferece ajuda na hora.'),
  dict(cue='O céu ficou escuro e você precisa da lanterna.', opts=['Let’s build a fire.', 'Sleep well!', 'It’s getting dark.'], ans=2, why='It’s getting dark avisa que escurece.')])
