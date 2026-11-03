"""Bloco de verbos e expressões da aula 42: jantar na casa de um amigo."""
K = ['eu · você · nós · eles', 'ele · ela', 'passado', '-ing']
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('invite', '💌', 'convidar', ('invite', 'I invite friends for dinner.', 'Eu convido amigos para jantar.'), ('invites', 'Jordan invites me.', 'O Jordan me convida.'), ('invited', 'She invited us to lunch.', 'Ela nos convidou para almoçar.'), ('inviting', 'He is inviting you.', 'Ele está convidando você.'), 'Invite + pessoa + to + evento: invite me to dinner.'),
  vb('bring', '🎁', 'trazer / levar', ('bring', 'I bring dessert.', 'Eu levo a sobremesa.'), ('brings', 'Ana brings flowers.', 'A Ana leva flores.'), ('brought', 'We brought juice.', 'Nós levamos suco.'), ('bringing', 'I am bringing bread.', 'Estou levando pão.'), 'Irregular: bring vira brought no passado.'),
  vb('cook', '🍳', 'cozinhar', ('cook', 'I cook pasta on Fridays.', 'Eu cozinho massa às sextas.'), ('cooks', 'Jordan cooks well.', 'O Jordan cozinha bem.'), ('cooked', 'He cooked soup.', 'Ele cozinhou sopa.'), ('cooking', 'She is cooking dinner.', 'Ela está cozinhando o jantar.'), 'Cook é regular: cooked, cooking.'),
  vb('come', '🚪', 'vir / chegar', ('come', 'You come at seven.', 'Você vem às sete.'), ('comes', 'Sam comes early.', 'O Sam vem cedo.'), ('came', 'They came on Friday.', 'Eles vieram na sexta.'), ('coming', 'I am coming now.', 'Estou indo agora.'), 'Irregular: come vira came. Para o convidado, “vir” é come.'),
  vb('love', '❤️', 'amar / adorar', ('love', 'I love pasta.', 'Eu adoro massa.'), ('loves', 'Jordan loves soup.', 'O Jordan adora sopa.'), ('loved', 'We loved the dinner.', 'Nós adoramos o jantar.'), ('loving', 'I am loving this soup.', 'Estou adorando esta sopa.'), 'I’d love to! é a resposta calorosa a um convite.')],
 verb_game=[
  dict(scene='Jordan convida você; você aceita animado.', en='I’d ___ to!', opts=['love', 'loves', 'loved'], ans=0, pt='Eu adoraria!', why='Depois de I’d (I would), usa-se a forma base: love.'),
  dict(scene='A Ana sempre leva flores à casa dos amigos.', en='Ana ___ flowers every time.', opts=['bring', 'brings', 'brought'], ans=1, pt='A Ana leva flores toda vez.', why='Ana (ela) no presente leva -s: brings.'),
  dict(scene='Na semana passada seus amigos vieram jantar.', en='They ___ to dinner last week.', opts=['come', 'comes', 'came'], ans=2, pt='Eles vieram jantar semana passada.', why='“Last week” pede passado; come vira came.'),
  dict(scene='Jordan está preparando a massa agora.', en='Jordan is ___ pasta now.', opts=['cook', 'cooks', 'cooking'], ans=2, pt='O Jordan está cozinhando massa agora.', why='“is” + verbo com -ing: cooking.')],
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
