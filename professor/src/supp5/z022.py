"""Bloco de verbos e expressões da aula 22: convite para uma festa."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('come', '🎉', 'vir', ('come', 'I come to the party at eight.', 'Eu venho à festa às oito.'), ('comes', 'Tom comes with a friend.', 'O Tom vem com um amigo.'), ('came', 'Tom came early yesterday.', 'O Tom veio cedo ontem.'), ('coming', 'They are coming at eight.', 'Eles estão vindo às oito.'), 'Passado irregular: come vira came.'),
  vb('bring', '🍪', 'levar / trazer', ('bring', 'I bring juice.', 'Eu levo suco.'), ('brings', 'Ana brings cookies.', 'A Ana leva biscoitos.'), ('brought', 'He brought chips.', 'Ele levou salgadinhos.'), ('bringing', 'I am bringing a drink.', 'Estou levando uma bebida.'), 'Irregular: bring vira brought no passado.'),
  vb('make', '🍕', 'fazer / preparar', ('make', 'We make pizza for the party.', 'Nós fazemos pizza para a festa.'), ('makes', 'Lina makes a cake.', 'A Lina faz um bolo.'), ('made', 'She made snacks.', 'Ela fez lanches.'), ('making', 'Lina is making snacks.', 'A Lina está fazendo lanches.'), 'Passado irregular: make vira made.'),
  vb('say', '👋', 'dizer', ('say', 'I say hi to everyone.', 'Eu digo oi para todo mundo.'), ('says', 'Lina says hello.', 'A Lina diz olá.'), ('said', 'He said hi at the door.', 'Ele disse oi na porta.'), ('saying', 'I am saying hello.', 'Estou dizendo olá.'), 'Passado irregular: say vira said (pronúncia “sed”).'),
  vb('put', '🎈', 'pôr / colocar', ('put', 'We put balloons on the wall.', 'Nós colocamos balões na parede.'), ('puts', 'Lina puts a banner up.', 'A Lina coloca uma faixa.'), ('put', 'She put the balloons up.', 'Ela colocou os balões.'), ('putting', 'I am putting up balloons.', 'Estou colocando balões.'), 'Put é igual no passado: put. -ing duplica o t.')],
 verb_game=[
  dict(scene='Você diz que vai levar uma bebida.', en='I will ___ a drink.', opts=['bring', 'brings', 'brought'], ans=0, pt='Eu vou levar uma bebida.', why='Depois de “will” o verbo fica na forma base: bring.'),
  dict(scene='Ontem o Tom veio à festa da Lina.', en='Tom ___ to Lina’s party yesterday.', opts=['come', 'comes', 'came'], ans=2, pt='O Tom veio à festa da Lina ontem.', why='“Yesterday” pede passado irregular: came.'),
  dict(scene='A Lina colocou os balões ontem.', en='Lina ___ the balloons up yesterday.', opts=['put', 'puts', 'putting'], ans=0, pt='A Lina colocou os balões ontem.', why='Passado de put é igual ao presente: put.'),
  dict(scene='Neste fim de semana a Lina prepara lanches.', en='Lina is ___ snacks this weekend.', opts=['make', 'makes', 'making'], ans=2, pt='A Lina está fazendo lanches neste fim de semana.', why='“is” + verbo com -ing: making.')],
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
