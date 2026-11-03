"""Bloco de verbos e expressões da aula 42: jantar na casa de um amigo."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('bring', '🎁', 'trazer', ('bring', 'I bring a gift.', 'Eu trago um presente.'), ('brings', 'Ana brings a cake.', 'A Ana traz um bolo.'), ('brought', 'He brought flowers.', 'Ele trouxe flores.'), ('bringing', 'I am bringing a dessert.', 'Estou trazendo uma sobremesa.'), 'Bring vira brought no passado (irregular).'),
  vb('invite', '💌', 'convidar', ('invite', 'We invite our friends.', 'Nós convidamos nossos amigos.'), ('invites', 'Jordan invites everyone.', 'O Jordan convida todo mundo.'), ('invited', 'She invited ten people.', 'Ela convidou dez pessoas.'), ('inviting', 'I am inviting my friends.', 'Estou convidando meus amigos.'), 'Invite perde o e antes de -ing: inviting.'),
  vb('meet', '🤝', 'encontrar / conhecer', ('meet', 'I meet new people.', 'Eu conheço gente nova.'), ('meets', 'Jordan meets every guest.', 'O Jordan recebe cada convidado.'), ('met', 'We met his sister.', 'Nós conhecemos a irmã dele.'), ('meeting', 'I am meeting his friends.', 'Estou conhecendo os amigos dele.'), 'Meet vira met no passado (irregular).'),
  vb('sit', '🪑', 'sentar', ('sit', 'We sit at the table.', 'Nós sentamos à mesa.'), ('sits', 'Ana sits next to me.', 'A Ana senta ao meu lado.'), ('sat', 'He sat by the window.', 'Ele sentou perto da janela.'), ('sitting', 'I am sitting here.', 'Estou sentado aqui.'), 'Sit vira sat no passado; o -ing dobra o t: sitting.'),
  vb('stay', '🏠', 'ficar', ('stay', 'I stay for dinner.', 'Eu fico para o jantar.'), ('stays', 'Ana stays late.', 'A Ana fica até tarde.'), ('stayed', 'We stayed until ten.', 'Nós ficamos até as dez.'), ('staying', 'I am staying for dessert.', 'Estou ficando para a sobremesa.'), 'Stay = ficar num lugar; passado regular: stayed.'),],
 verb_game=[
  dict(scene='Jordan recebe cada convidado na porta.', en='Jordan ___ every guest at the door.', opts=['meet', 'meets', 'met'], ans=1, pt='O Jordan recebe cada convidado na porta.', why='Jordan (ele) no presente leva -s: meets.'),
  dict(scene='A Ana traz um bolo toda vez.', en='Ana ___ a cake every time.', opts=['bring', 'brings', 'brought'], ans=1, pt='A Ana traz um bolo toda vez.', why='Ana (ela) no presente leva -s: brings.'),
  dict(scene='Na semana passada eles sentaram à mesa grande.', en='They ___ at the big table last week.', opts=['sit', 'sits', 'sat'], ans=2, pt='Eles sentaram à mesa grande semana passada.', why='“Last week” pede passado: sat (irregular).'),
  dict(scene='Jordan está convidando os amigos agora.', en='Jordan is ___ his friends now.', opts=['invite', 'invites', 'inviting'], ans=2, pt='O Jordan está convidando os amigos agora.', why='“is” + -ing: inviting (sem o e).')],
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
