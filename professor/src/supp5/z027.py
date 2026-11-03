"""Bloco de verbos e expressões da aula 27: restaurante de churrasco para dividir."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('share', '🍖', 'dividir / compartilhar', ('share', 'We share a rack of ribs.', 'Nós dividimos uma costela.'), ('shares', 'Tom shares his fries.', 'O Tom divide suas batatas.'), ('shared', 'We shared the wings.', 'Nós dividimos as asinhas.'), ('sharing', 'We are sharing a plate.', 'Estamos dividindo um prato.'), 'Share termina em -e: shared, sharing.'),
  vb('tell', '🗣️', 'dizer / contar', ('tell', 'I tell him my order.', 'Eu digo meu pedido a ele.'), ('tells', 'The waiter tells us the specials.', 'O garçom nos conta os pratos do dia.'), ('told', 'She told us about the ribs.', 'Ela nos falou das costelas.'), ('telling', 'He is telling us the price.', 'Ele está nos dizendo o preço.'), 'Passado irregular: tell vira told.'),
  vb('sit', '🪑', 'sentar', ('sit', 'We sit at a big table.', 'Nós sentamos numa mesa grande.'), ('sits', 'Dad sits by the window.', 'O pai senta perto da janela.'), ('sat', 'They sat near the door.', 'Eles sentaram perto da porta.'), ('sitting', 'We are sitting outside.', 'Estamos sentados lá fora.'), 'Passado irregular: sit vira sat; -ing dobra o t.'),
  vb('bring', '🛎️', 'trazer', ('bring', 'I bring my family here.', 'Eu trago minha família aqui.'), ('brings', 'He brings the menu.', 'Ele traz o cardápio.'), ('brought', 'She brought us water.', 'Ela nos trouxe água.'), ('bringing', 'He is bringing our food.', 'Ele está trazendo nossa comida.'), 'Passado irregular: bring vira brought.'),
  vb('order', '🧾', 'pedir', ('order', 'We order ribs and wings.', 'Nós pedimos costelas e asinhas.'), ('orders', 'Mom orders a salad.', 'A mãe pede uma salada.'), ('ordered', 'I ordered a soda.', 'Eu pedi um refrigerante.'), ('ordering', 'We are ordering now.', 'Estamos pedindo agora.'), 'Order serve para pedir comida; o passado só acrescenta -ed.'),
 verb_game=[
  dict(scene='Vocês dividem um prato.', en='We ___ a plate of wings.', opts=['share', 'shares', 'shared'], ans=0, pt='Nós dividimos um prato de asinhas.', why='Com “we” no presente: share.'),
  dict(scene='O garçom conta os pratos do dia.', en='The waiter ___ us the specials.', opts=['tell', 'tells', 'telling'], ans=1, pt='O garçom nos conta os pratos do dia.', why='“The waiter” é ele: tells.'),
  dict(scene='Ele trouxe as bebidas para nós.', en='He ___ us our drinks.', opts=['bring', 'brings', 'brought'], ans=2, pt='Ele nos trouxe nossas bebidas.', why='O fato já aconteceu: passado irregular, brought.'),
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
