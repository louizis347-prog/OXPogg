"""Bloco de verbos e expressões da aula 037: sorvete."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('choose', '🍦', 'escolher', ('choose', 'I choose chocolate.', 'Eu escolho chocolate.'), ('chooses', 'Ana chooses vanilla.', 'A Ana escolhe baunilha.'), ('chose', 'He chose two flavors.', 'Ele escolheu dois sabores.'), ('choosing', 'I am choosing a flavor.', 'Estou escolhendo um sabor.'), 'Choose vira chose no passado (irregular).'),
  vb('give', '🎁', 'dar / entregar', ('give', 'We give a cone to Ben.', 'Nós damos uma casquinha ao Ben.'), ('gives', 'She gives me a spoon.', 'Ela me dá uma colher.'), ('gave', 'He gave me a cup.', 'Ele me deu um copo.'), ('giving', 'I am giving her a cone.', 'Estou dando uma casquinha a ela.'), 'Give vira gave no passado (irregular).'),
  vb('take', '🍨', 'pegar / levar', ('take', 'I take a small cone.', 'Eu pego uma casquinha pequena.'), ('takes', 'Ana takes a napkin.', 'A Ana pega um guardanapo.'), ('took', 'He took a cup.', 'Ele pegou um copo.'), ('taking', 'I am taking a spoon.', 'Estou pegando uma colher.'), 'Take vira took no passado; o -ing perde o e: taking.'),
  vb('try', '👅', 'provar / tentar', ('try', 'I try the vanilla.', 'Eu provo a baunilha.'), ('tries', 'She tries a small spoon.', 'Ela prova uma colherinha.'), ('tried', 'He tried chocolate.', 'Ele provou chocolate.'), ('trying', 'I am trying a new flavor.', 'Estou provando um sabor novo.'), 'Try vira tries e tried (y vira ie/i).'),
  vb('share', '🤝', 'dividir / compartilhar', ('share', 'We share a big sundae.', 'Nós dividimos um sundae grande.'), ('shares', 'Ana shares her ice cream.', 'A Ana divide o sorvete dela.'), ('shared', 'He shared his cone.', 'Ele dividiu a casquinha dele.'), ('sharing', 'I am sharing my cone.', 'Estou dividindo minha casquinha.'), 'Share perde o e antes de -ing: sharing.'),],
 verb_game=[
  dict(scene='Ontem ele escolheu dois sabores.', en='Yesterday he ___ two flavors.', opts=['choose', 'chose', 'chooses'], ans=1, pt='Ontem ele escolheu dois sabores.', why='Passado irregular de choose: chose.'),
  dict(scene='A Ana pega um guardanapo.', en='Ana ___ a napkin.', opts=['take', 'takes', 'took'], ans=1, pt='A Ana pega um guardanapo.', why='Com “Ana” (ela), o presente leva -s: takes.'),
  dict(scene='Você divide o sorvete agora.', en='I am ___ my ice cream.', opts=['share', 'shares', 'sharing'], ans=2, pt='Estou dividindo meu sorvete.', why='“am” + -ing: sharing (sem o e).'),
  dict(scene='Vocês dão uma casquinha ao Ben.', en='We ___ a cone to Ben.', opts=['give', 'gives', 'gave'], ans=0, pt='Nós damos uma casquinha ao Ben.', why='Com “we” o presente fica na forma base: give.')],
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
