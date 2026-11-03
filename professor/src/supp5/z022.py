"""Bloco de verbos e expressões da aula 22: convite para uma festa."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('join', '🎉', 'juntar-se / vir', ('join', 'I join the party at eight.', 'Eu chego à festa às oito.'), ('joins', 'Tom joins us later.', 'O Tom se junta a nós mais tarde.'), ('joined', 'She joined us for dinner.', 'Ela jantou com a gente.'), ('joining', 'I am joining them now.', 'Estou me juntando a eles agora.'), 'Join us! é um convite simpático para se juntar ao grupo.'),
  vb('bring', '🍪', 'levar / trazer', ('bring', 'I bring juice.', 'Eu levo suco.'), ('brings', 'Ana brings cookies.', 'A Ana leva biscoitos.'), ('brought', 'He brought chips.', 'Ele levou salgadinhos.'), ('bringing', 'I am bringing a drink.', 'Estou levando uma bebida.'), 'Irregular: bring vira brought no passado.'),
  vb('host', '💌', 'receber / sediar', ('host', 'We host a party every year.', 'Nós recebemos uma festa todo ano.'), ('hosts', 'Lina hosts at her place.', 'A Lina recebe na casa dela.'), ('hosted', 'Tom hosted the dinner.', 'O Tom recebeu o jantar.'), ('hosting', 'I am hosting this weekend.', 'Vou receber gente neste fim de semana.'), 'Host é quem recebe a festa em casa; o passado só acrescenta -ed.'),
  vb('greet', '👋', 'cumprimentar', ('greet', 'I greet everyone at the door.', 'Eu cumprimento todos na porta.'), ('greets', 'Lina greets each guest.', 'A Lina cumprimenta cada convidado.'), ('greeted', 'She greeted me with a hug.', 'Ela me cumprimentou com um abraço.'), ('greeting', 'I am greeting the guests.', 'Estou recebendo os convidados.'), 'Greet = cumprimentar quem chega, com palavras ou um abraço.'),
  vb('hang', '🎈', 'pendurar', ('hang', 'We hang balloons before eight.', 'Nós penduramos balões antes das oito.'), ('hangs', 'Tom hangs a banner.', 'O Tom pendura uma faixa.'), ('hung', 'I hung the lights yesterday.', 'Eu pendurei as luzes ontem.'), ('hanging', 'We are hanging the balloons.', 'Estamos pendurando os balões.'), 'Irregular: hang, hung (para decoração e roupas).')],
 verb_game=[
  dict(scene='Você diz que vai levar uma bebida.', en='I will ___ a drink.', opts=['bring', 'brings', 'brought'], ans=0, pt='Eu vou levar uma bebida.', why='Depois de “will” o verbo fica na forma base: bring.'),
  dict(scene='Ontem o Tom veio juntar-se à festa da Lina.', en='Tom ___ us at the party yesterday.', opts=['join', 'joins', 'joined'], ans=2, pt='O Tom se juntou a nós na festa ontem.', why='“Yesterday” pede passado: joined.'),
  dict(scene='A Lina pendurou os balões ontem.', en='Lina ___ the balloons yesterday.', opts=['hang', 'hung', 'hanging'], ans=1, pt='A Lina pendurou os balões ontem.', why='Passado irregular de hang: hung.'),
  dict(scene='Neste fim de semana a Lina vai receber os amigos.', en='Lina is ___ her friends this weekend.', opts=['host', 'hosts', 'hosting'], ans=2, pt='A Lina está recebendo os amigos neste fim de semana.', why='“is” + verbo com -ing: hosting.')],
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
