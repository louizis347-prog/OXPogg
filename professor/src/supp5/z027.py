"""Bloco de verbos e expressões da aula 27: restaurante de churrasco para dividir."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('share', '🍖', 'dividir / compartilhar', ('share', 'We share a rack of ribs.', 'Nós dividimos uma costela.'), ('shares', 'Tom shares his fries.', 'O Tom divide suas batatas.'), ('shared', 'We shared the wings.', 'Nós dividimos as asinhas.'), ('sharing', 'We are sharing a plate.', 'Estamos dividindo um prato.'), 'Share termina em -e: shared, sharing.'),
  vb('recommend', '⭐', 'recomendar', ('recommend', 'I recommend the ribs.', 'Eu recomendo as costelas.'), ('recommends', 'She recommends the wings.', 'Ela recomenda as asinhas.'), ('recommended', 'He recommended the corn.', 'Ele recomendou o milho.'), ('recommending', 'They are recommending the beans.', 'Eles estão recomendando o feijão.'), 'What do you recommend? é ótimo para pedir dica.'),
  vb('lead', '🍽️', 'levar / guiar', ('lead', 'I lead the group to the table.', 'Eu levo o grupo até a mesa.'), ('leads', 'The host leads us inside.', 'O anfitrião nos leva para dentro.'), ('led', 'He led us to a booth.', 'Ele nos levou a uma mesa.'), ('leading', 'She is leading us now.', 'Ela está nos levando agora.'), 'Irregular: lead, led (pronuncia-se “led”).'),
  vb('hand', '🛎️', 'entregar', ('hand', 'I hand the waiter my menu.', 'Eu entrego o cardápio ao garçom.'), ('hands', 'He hands us the menus.', 'Ele nos entrega os cardápios.'), ('handed', 'She handed me a napkin.', 'Ela me entregou um guardanapo.'), ('handing', 'He is handing out the drinks.', 'Ele está distribuindo as bebidas.'), 'Hand me… = me passe…; o passado só acrescenta -ed.'),
  vb('lick', '😋', 'lamber', ('lick', 'I lick my fingers after the ribs.', 'Eu lambo os dedos depois das costelas.'), ('licks', 'Tim licks the sauce off.', 'O Tim lambe o molho.'), ('licked', 'She licked her fingers.', 'Ela lambeu os dedos.'), ('licking', 'We are licking our fingers.', 'Estamos lambendo os dedos.'), 'Lick your fingers = chupar os dedos, sinal de comida boa.')],
 verb_game=[
  dict(scene='Vocês dividem um prato.', en='We ___ a plate of wings.', opts=['share', 'shares', 'shared'], ans=0, pt='Nós dividimos um prato de asinhas.', why='Com “we” no presente: share.'),
  dict(scene='O garçom recomenda as costelas.', en='The waiter ___ the ribs.', opts=['recommend', 'recommends', 'recommending'], ans=1, pt='O garçom recomenda as costelas.', why='“The waiter” é ele: recommends.'),
  dict(scene='Ele entregou as bebidas para nós.', en='He ___ us our drinks.', opts=['hand', 'hands', 'handed'], ans=2, pt='Ele nos entregou nossas bebidas.', why='O fato já aconteceu: passado com -ed, handed.'),
  dict(scene='Agora vocês dividem a mesa.', en='We are ___ the ribs.', opts=['share', 'sharing', 'shared'], ans=1, pt='Estamos dividindo as costelas.', why='“are” + -ing: sharing.')],
 expressions=[
  dict(en='Do you want to share?', pt='Vocês querem dividir?', ex='Welcome! Do you want to share?', exp='Pergunta sobre mesa ou prato compartilhado.', c='a'),
  dict(en='What do you recommend?', pt='O que você recomenda?', ex='What do you recommend?', exp='Para pedir uma sugestão.', c='b'),
  dict(en='What’s good here?', pt='O que é bom aqui?', ex='Yes. What’s good here?', exp='Para saber o prato mais gostoso.', c='c'),
  dict(en='We’ll have…', pt='Nós vamos querer…', ex='We’ll have one rack of ribs.', exp='Fazer o pedido pelo grupo.', c='d'),
  dict(en='a side of…', pt='um acompanhamento de…', ex='A side of corn, please.', exp='Pedir um acompanhamento.', c='a'),
  dict(en='Enjoy the ribs!', pt='Bom apetite!', ex='Here you go. Enjoy the ribs!', exp='Dito ao servir a comida.', c='b')],
 expr_game=[
  dict(cue='Você quer uma sugestão do garçom.', opts=['What do you recommend?', 'We’ll have the ribs.', 'Enjoy the ribs!'], ans=0, why='What do you recommend? pede uma dica.'),
  dict(cue='Vocês decidem pedir as costelas.', opts=['What’s good here?', 'We’ll have the ribs.', 'Do you want to share?'], ans=1, why='We’ll have… faz o pedido.'),
  dict(cue='Você quer milho como acompanhamento.', opts=['A side of corn, please.', 'What do you recommend?', 'Enjoy the ribs!'], ans=0, why='A side of… pede um acompanhamento.')])
