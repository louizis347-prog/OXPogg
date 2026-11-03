"""Bloco de verbos e expressões da aula 42: jantar na casa de um amigo."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('wrap', '🎀', 'embrulhar', ('wrap', 'I wrap the gift.', 'Eu embrulho o presente.'), ('wraps', 'Ana wraps the book.', 'A Ana embrulha o livro.'), ('wrapped', 'He wrapped a box.', 'Ele embrulhou uma caixa.'), ('wrapping', 'I am wrapping a gift.', 'Estou embrulhando um presente.'), 'Wrap dobra o p: wrapped, wrapping.'),
  vb('unwrap', '🎁', 'desembrulhar', ('unwrap', 'We unwrap the gifts.', 'Nós desembrulhamos os presentes.'), ('unwraps', 'She unwraps a box.', 'Ela desembrulha uma caixa.'), ('unwrapped', 'I unwrapped the cake.', 'Eu desembrulhei o bolo.'), ('unwrapping', 'He is unwrapping it.', 'Ele está desembrulhando.'), 'Unwrap também dobra o p: unwrapped.'),
  vb('tidy', '🧹', 'arrumar', ('tidy', 'I tidy the room.', 'Eu arrumo a sala.'), ('tidies', 'Jordan tidies up.', 'O Jordan arruma tudo.'), ('tidied', 'We tidied the kitchen.', 'Nós arrumamos a cozinha.'), ('tidying', 'I am tidying up.', 'Estou arrumando.'), 'Tidy vira tidies e tidied; o -ing é tidying.'),
  vb('toast', '🥂', 'brindar', ('toast', 'We toast the host.', 'Nós brindamos ao anfitrião.'), ('toasts', 'He toasts his friends.', 'Ele brinda aos amigos.'), ('toasted', 'They toasted Jordan.', 'Eles brindaram ao Jordan.'), ('toasting', 'We are toasting now.', 'Estamos brindando agora.'), 'Toast é regular: toasted.'),
  vb('welcome', '🤗', 'receber / dar boas-vindas', ('welcome', 'We welcome the guests.', 'Nós recebemos os convidados.'), ('welcomes', 'Jordan welcomes everyone.', 'O Jordan recebe todo mundo.'), ('welcomed', 'She welcomed us.', 'Ela nos recebeu.'), ('welcoming', 'I am welcoming guests.', 'Estou recebendo convidados.'), 'Welcome perde o e: welcoming.')],
 verb_game=[
  dict(scene='Jordan recebe cada convidado na porta.', en='Jordan ___ every guest at the door.', opts=['welcome', 'welcomes', 'welcomed'], ans=1, pt='O Jordan recebe cada convidado na porta.', why='Jordan (ele) no presente leva -s: welcomes.'),
  dict(scene='A Ana embrulha o presente todas as vezes.', en='Ana ___ the gift every time.', opts=['wrap', 'wraps', 'wrapped'], ans=1, pt='A Ana embrulha o presente toda vez.', why='Ana (ela) no presente leva -s: wraps.'),
  dict(scene='Na semana passada seus amigos brindaram ao anfitrião.', en='They ___ the host last week.', opts=['toast', 'toasts', 'toasted'], ans=2, pt='Eles brindaram ao anfitrião semana passada.', why='“Last week” pede passado regular: toasted.'),
  dict(scene='Jordan está arrumando a sala agora.', en='Jordan is ___ the living room now.', opts=['tidy', 'tidies', 'tidying'], ans=2, pt='O Jordan está arrumando a sala agora.', why='“is” + verbo com -ing: tidying.')],
 expressions=[
  dict(en='What should I bring?', pt='O que devo levar?', ex='What should I bring? — Just yourself.', exp='Para perguntar, ao aceitar um convite, o que levar.', c='a'),
  dict(en='I’d love to!', pt='Eu adoraria!', ex='Dinner on Friday? I’d love to!', exp='Para aceitar um convite com entusiasmo.', c='b'),
  dict(en='Just yourself.', pt='Só você mesmo.', ex='What should I bring? — Just yourself.', exp='Resposta do anfitrião quando não precisa de nada.', c='c'),
  dict(en='Thanks for coming!', pt='Obrigado por vir!', ex='Thanks for coming! See you soon.', exp='O anfitrião diz ao se despedir dos convidados.', c='d'),
  dict(en='at my place', pt='na minha casa', ex='Let’s have dinner at my place.', exp='Jeito informal de dizer “na minha casa”.', c='a'),
  dict(en='See you on Friday.', pt='Até sexta.', ex='Thanks, Jordan! See you on Friday.', exp='Despedida combinando o dia do encontro.', c='b')],
 expr_game=[
  dict(cue='Você quer aceitar o convite com alegria.', opts=['I’d love to!', 'Thanks for coming!', 'Just yourself.'], ans=0, why='I’d love to! aceita um convite.'),
  dict(cue='Você quer saber se deve levar algo.', opts=['See you on Friday.', 'What should I bring?', 'At my place.'], ans=1, why='What should I bring? pergunta o que levar.'),
  dict(cue='Você é o anfitrião e seus amigos estão indo embora.', opts=['Thanks for coming!', 'I’d love to!', 'What should I bring?'], ans=0, why='Thanks for coming! agradece a visita.')])
