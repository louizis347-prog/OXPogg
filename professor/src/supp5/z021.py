"""Bloco de verbos e expressões da aula 021."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('rain', '🌧️', 'chover', ('rain', 'It rains in spring.', 'Chove na primavera.'), ('rains', 'It rains a lot here.', 'Chove muito aqui.'), ('rained', 'It rained yesterday.', 'Choveu ontem.'), ('raining', 'It is raining now.', 'Está chovendo agora.'), 'Sujeito é sempre it.'),
  vb('snow', '❄️', 'nevar', ('snow', 'It snows in winter.', 'Neva no inverno.'), ('snows', 'It snows a lot in Chicago.', 'Neva muito em Chicago.'), ('snowed', 'It snowed last night.', 'Nevou ontem à noite.'), ('snowing', 'It is snowing!', 'Está nevando!'), 'Igual a rain: sujeito it.'),
  vb('need', '🧥', 'precisar', ('need', 'I need a warm coat.', 'Eu preciso de um casaco quente.'), ('needs', 'Tom needs a hat.', 'O Tom precisa de um chapéu.'), ('needed', 'I needed a coat.', 'Eu precisei de um casaco.'), ('needing', 'Am I needing it?', 'Será que estou precisando?'), 'Need + coisa ou need + to + verbo.'),
  vb('wear', '🧣', 'vestir / usar', ('wear', 'I wear a coat.', 'Eu uso casaco.'), ('wears', 'Ana wears a scarf.', 'A Ana usa cachecol.'), ('wore', 'I wore boots.', 'Eu usei botas.'), ('wearing', 'I am wearing gloves.', 'Estou de luvas.'), 'Irregular: wear, wore.'),
  vb('keep', '☂️', 'guardar / manter', ('keep', 'I keep an umbrella in my bag.', 'Eu guardo um guarda-chuva na bolsa.'), ('keeps', 'Sam keeps a coat at work.', 'O Sam guarda um casaco no trabalho.'), ('kept', 'I kept my coat on all day.', 'Eu fiquei de casaco o dia todo.'), ('keeping', 'I am keeping my hat on.', 'Estou ficando de chapéu.'), 'Keep my coat on = continuar de casaco. Irregular: keep, kept.')],
 verb_game=[
  dict(scene='Em Chicago neva muito.', en='It ___ a lot in Chicago.', opts=['snow', 'snows', 'snowed'], ans=1, pt='Neva muito em Chicago.', why='Com “it”: snows.'),
  dict(scene='Agora está chovendo.', en='It is ___ now.', opts=['rain', 'rains', 'raining'], ans=2, pt='Está chovendo agora.', why='“is” + -ing: raining.'),
  dict(scene='Ontem você ficou de casaco o dia todo.', en='I ___ my coat on yesterday.', opts=['keep', 'kept', 'keeping'], ans=1, pt='Eu fiquei de casaco ontem.', why='Passado de keep: kept.'),
  dict(scene='Você precisa de um casaco quente.', en='I ___ a warm coat.', opts=['need', 'needs', 'needed'], ans=0, pt='Eu preciso de um casaco quente.', why='Presente com “I”: need.')],
 expressions=[
  dict(en='Nice day, isn’t it?', pt='Dia bonito, né?', ex='Nice day, isn’t it?', exp='Puxar conversa.', c='a'),
  dict(en='It’s sunny.', pt='Está ensolarado.', ex='Yes, it’s sunny.', exp='Dizer o clima.', c='b'),
  dict(en='It’s very cold.', pt='Está muito frio.', ex='It’s very cold today.', exp='Dizer a temperatura.', c='c'),
  dict(en='Take a coat.', pt='Leve um casaco.', ex='A little cold. Take a coat!', exp='Dar um conselho.', c='d'),
  dict(en='It’s always windy.', pt='Sempre venta.', ex='Chicago is always windy.', exp='Dizer algo comum do lugar.', c='a'),
  dict(en='Stay warm!', pt='Fique aquecido!', ex='Bye! Stay warm!', exp='Despedida no frio.', c='b')],
 expr_game=[
  dict(cue='Você quer puxar conversa sobre o dia bonito.', opts=['Nice day, isn’t it?', 'Stay warm!', 'Take a coat.'], ans=0, why='Isn’t it? busca concordância.'),
  dict(cue='Está frio e você aconselha levar casaco.', opts=['It’s sunny.', 'Take a coat.', 'Nice day.'], ans=1, why='Take a coat. é conselho.'),
  dict(cue='Você se despede de alguém no frio.', opts=['Stay warm!', 'It’s hot.', 'Nice day, isn’t it?'], ans=0, why='Stay warm! é uma despedida cuidadosa.')])
