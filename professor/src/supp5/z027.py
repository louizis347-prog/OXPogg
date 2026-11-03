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
  vb('take', '🍽️', 'pegar / levar', ('take', 'We take the ribs.', 'Nós levamos as costelas.'), ('takes', 'Sam takes the wings.', 'O Sam pega as asinhas.'), ('took', 'I took the corn.', 'Eu peguei o milho.'), ('taking', 'We are taking the fries.', 'Estamos levando as batatas.'), 'We’ll take… é um pedido natural. Passado: took.'),
  vb('bring', '🛎️', 'trazer', ('bring', 'They bring the ribs.', 'Eles trazem as costelas.'), ('brings', 'He brings two waters.', 'Ele traz duas águas.'), ('brought', 'She brought the sides.', 'Ela trouxe os acompanhamentos.'), ('bringing', 'He is bringing the food.', 'Ele está trazendo a comida.'), 'Irregular: bring vira brought.'),
  vb('love', '❤️', 'amar / adorar', ('love', 'I love the ribs.', 'Eu adoro as costelas.'), ('loves', 'Mia loves the beans.', 'A Mia adora o feijão.'), ('loved', 'We loved the wings.', 'Nós adoramos as asinhas.'), ('loving', 'I am loving this corn.', 'Estou adorando este milho.'), 'Love é mais forte que like; ótimo para elogiar.')],
 verb_game=[
  dict(scene='Vocês dividem um prato.', en='We ___ a plate of wings.', opts=['share', 'shares', 'shared'], ans=0, pt='Nós dividimos um prato de asinhas.', why='Com “we” no presente: share.'),
  dict(scene='O garçom recomenda as costelas.', en='The waiter ___ the ribs.', opts=['recommend', 'recommends', 'recommending'], ans=1, pt='O garçom recomenda as costelas.', why='“The waiter” é ele: recommends.'),
  dict(scene='Ele trouxe as bebidas.', en='He ___ our drinks.', opts=['bring', 'brings', 'brought'], ans=2, pt='Ele trouxe nossas bebidas.', why='Passado irregular de bring: brought.'),
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
