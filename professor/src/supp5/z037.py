"""Bloco de verbos e expressões da aula 037: sorvete."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('choose', '🍨', 'escolher', ('choose', 'I choose vanilla.', 'Eu escolho baunilha.'), ('chooses', 'She chooses chocolate.', 'Ela escolhe chocolate.'), ('chose', 'He chose strawberry.', 'Ele escolheu morango.'), ('choosing', 'I am choosing a flavor.', 'Estou escolhendo um sabor.'), 'Irregular: choose vira chose.'),
  vb('want', '🙋', 'querer', ('want', 'I want two scoops.', 'Eu quero duas bolas.'), ('wants', 'He wants a cone.', 'Ele quer uma casquinha.'), ('wanted', 'She wanted vanilla.', 'Ela queria baunilha.'), ('wanting', 'I am wanting chocolate.', 'Estou querendo chocolate.'), 'What flavor do you want? é a pergunta típica.'),
  vb('like', '❤️', 'gostar', ('like', 'I like strawberry.', 'Eu gosto de morango.'), ('likes', 'She likes vanilla.', 'Ela gosta de baunilha.'), ('liked', 'He liked the chocolate.', 'Ele gostou do chocolate.'), ('liking', 'I am liking this flavor.', 'Estou gostando deste sabor.'), 'Like + sabor: I like vanilla. Com ele/ela: likes.'),
  vb('try', '👅', 'provar / tentar', ('try', 'I try the vanilla.', 'Eu provo a baunilha.'), ('tries', 'She tries a small spoon.', 'Ela prova uma colherinha.'), ('tried', 'He tried chocolate.', 'Ele provou chocolate.'), ('trying', 'I am trying a new flavor.', 'Estou provando um sabor novo.'), 'Try vira tries e tried (y vira ie/i).'),
  vb('eat', '😋', 'comer', ('eat', 'We eat ice cream.', 'Nós comemos sorvete.'), ('eats', 'He eats a cone.', 'Ele come uma casquinha.'), ('ate', 'I ate two scoops.', 'Eu comi duas bolas.'), ('eating', 'She is eating vanilla.', 'Ela está comendo baunilha.'), 'Irregular: eat vira ate.')],
 verb_game=[
  dict(scene='Ontem ele escolheu morango.', en='Yesterday he ___ strawberry.', opts=['choose', 'chose', 'chooses'], ans=1, pt='Ontem ele escolheu morango.', why='Passado irregular de choose: chose.'),
  dict(scene='A Ana gosta de baunilha.', en='Ana ___ vanilla.', opts=['like', 'likes', 'liking'], ans=1, pt='A Ana gosta de baunilha.', why='Com “Ana” (ela), o presente leva -s: likes.'),
  dict(scene='Você está provando um sabor novo.', en='I am ___ a new flavor.', opts=['try', 'tries', 'trying'], ans=2, pt='Estou provando um sabor novo.', why='“am” + -ing: trying.'),
  dict(scene='Vocês querem duas bolas.', en='We ___ two scoops.', opts=['want', 'wants', 'wanted'], ans=0, pt='Nós queremos duas bolas.', why='Com “we” o presente fica na forma base: want.')],
 expressions=[
  dict(en='What flavor do you want?', pt='Que sabor você quer?', ex='Hi! What flavor do you want?', exp='A pergunta do atendente.', c='a'),
  dict(en='One scoop or two?', pt='Uma bola ou duas?', ex='One scoop or two? — Two, please.', exp='Para escolher a quantidade.', c='b'),
  dict(en='In a cup or a cone?', pt='No copo ou na casquinha?', ex='A cone, please.', exp='O atendente pergunta como você quer servir.', c='c'),
  dict(en='Can I try it?', pt='Posso provar?', ex='Can I try the vanilla?', exp='Para pedir uma provinha do sabor.', c='d'),
  dict(en='Chocolate, please.', pt='Chocolate, por favor.', ex='Chocolate, please. In a cone.', exp='Resposta curta para escolher o sabor.', c='a'),
  dict(en='Here you go.', pt='Aqui está.', ex='Here you go. Four dollars.', exp='Ao entregar o sorvete ou o dinheiro.', c='b')],
 expr_game=[
  dict(cue='Você quer duas bolas.', opts=['Two scoops, please.', 'In a cone.', 'Can I try it?'], ans=0, why='Two scoops, please pede duas bolas.'),
  dict(cue='O atendente pergunta copo ou casquinha e você escolhe casquinha.', opts=['A cone, please.', 'Chocolate, please.', 'One scoop.'], ans=0, why='A cone, please = casquinha, por favor.'),
  dict(cue='Você quer provar o sabor antes.', opts=['Can I try the vanilla?', 'What flavor do you want?', 'Here you go.'], ans=0, why='Can I try…? pede uma prova.')])
