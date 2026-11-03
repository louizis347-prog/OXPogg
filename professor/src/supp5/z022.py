"""Bloco de verbos e expressões da aula 22: convite para uma festa."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('come', '🎉', 'vir', ('come', 'I come at eight.', 'Eu venho às oito.'), ('comes', 'Lina comes early.', 'A Lina vem cedo.'), ('came', 'Tom came to the party.', 'O Tom veio à festa.'), ('coming', 'We are coming on Saturday.', 'Nós vamos no sábado.'), 'Come irregular: passado came. Em PT “ir” à festa de alguém costuma ser come.'),
  vb('bring', '🍪', 'levar / trazer', ('bring', 'I bring juice.', 'Eu levo suco.'), ('brings', 'Ana brings cookies.', 'A Ana leva biscoitos.'), ('brought', 'He brought chips.', 'Ele levou salgadinhos.'), ('bringing', 'I am bringing a drink.', 'Estou levando uma bebida.'), 'Irregular: bring vira brought no passado.'),
  vb('invite', '💌', 'convidar', ('invite', 'We invite our friends.', 'Nós convidamos nossos amigos.'), ('invites', 'Lina invites me.', 'A Lina me convida.'), ('invited', 'She invited ten people.', 'Ela convidou dez pessoas.'), ('inviting', 'I am inviting Sam.', 'Estou convidando o Sam.'), 'Termina em -e: só acrescente -d no passado (invited).'),
  vb('see', '👋', 'ver', ('see', 'I see you on Saturday.', 'Eu vejo você no sábado.'), ('sees', 'Tom sees Lina there.', 'O Tom vê a Lina lá.'), ('saw', 'We saw the house.', 'Nós vimos a casa.'), ('seeing', 'I am seeing Ana tonight.', 'Estou vendo a Ana hoje à noite.'), 'Irregular: see vira saw. “See you!” é despedida comum.'),
  vb('start', '⏰', 'começar', ('start', 'We start at eight.', 'Nós começamos às oito.'), ('starts', 'The party starts at eight.', 'A festa começa às oito.'), ('started', 'It started late.', 'Começou tarde.'), ('starting', 'It is starting now.', 'Está começando agora.'), 'Start serve para festa, aula, filme: starts at + hora.')],
 verb_game=[
  dict(scene='Você diz que vai levar uma bebida.', en='I will ___ a drink.', opts=['bring', 'brings', 'brought'], ans=0, pt='Eu vou levar uma bebida.', why='Depois de “will” o verbo fica na forma base: bring.'),
  dict(scene='Ontem o Tom foi à festa da Lina.', en='Tom ___ to the party yesterday.', opts=['come', 'came', 'coming'], ans=1, pt='O Tom veio à festa ontem.', why='“Yesterday” pede passado irregular: came.'),
  dict(scene='A festa começa às oito.', en='The party ___ at eight.', opts=['start', 'starts', 'started'], ans=1, pt='A festa começa às oito.', why='“The party” é ele/ela no presente: starts.'),
  dict(scene='Agora a Lina está chamando amigos.', en='Lina is ___ her friends.', opts=['invite', 'invites', 'inviting'], ans=2, pt='A Lina está convidando os amigos.', why='“is” + verbo com -ing: inviting.')],
 expressions=[
  dict(en='Can you come?', pt='Você pode vir?', ex='Can you come to my party?', exp='Para convidar alguém.', c='a'),
  dict(en='I’d love to!', pt='Eu adoraria!', ex='I’d love to! What time is it?', exp='Para aceitar um convite com alegria.', c='b'),
  dict(en='What time is it?', pt='Que horas é?', ex='What time is the party?', exp='Para saber o horário do evento.', c='c'),
  dict(en='Can I bring something?', pt='Posso levar alguma coisa?', ex='Can I bring a drink?', exp='Para oferecer ajuda ao anfitrião.', c='d'),
  dict(en='Here’s the address.', pt='Aqui está o endereço.', ex='Here’s the address. See you there!', exp='Para passar o endereço de um lugar.', c='a'),
  dict(en='See you then!', pt='Até lá!', ex='Great! See you then!', exp='Despedida depois de marcar um dia e hora.', c='b')],
 expr_game=[
  dict(cue='Você quer saber o horário da festa.', opts=['What time is it?', 'I’d love to!', 'Here’s the address.'], ans=0, why='What time…? pergunta as horas do evento.'),
  dict(cue='Você aceita o convite com entusiasmo.', opts=['Here’s the address.', 'I’d love to!', 'Can you come?'], ans=1, why='I’d love to! aceita um convite.'),
  dict(cue='Você quer ajudar levando algo.', opts=['See you then!', 'Can I bring something?', 'What time is it?'], ans=1, why='Can I bring something? oferece ajuda.')])
