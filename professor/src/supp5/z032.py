"""Bloco de verbos e expressões da aula 032: pedir água no restaurante."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('drink', '🥤', 'beber', ('drink', 'I drink water with lunch.', 'Eu bebo água no almoço.'), ('drinks', 'Maya drinks lemonade.', 'A Maya bebe limonada.'), ('drank', 'He drank a glass of water.', 'Ele bebeu um copo de água.'), ('drinking', 'I am drinking cold water.', 'Estou bebendo água gelada.'), 'Irregular: drink vira drank no passado.'),
  vb('want', '🙋', 'querer', ('want', 'I want some water.', 'Eu quero um pouco de água.'), ('wants', 'She wants ice.', 'Ela quer gelo.'), ('wanted', 'We wanted lemonade.', 'Nós queríamos limonada.'), ('wanting', 'I am wanting nothing now.', 'Agora não estou querendo nada.'), 'Want é direto; I would like (I’d like) soa mais educado.'),
  vb('bring', '🍽️', 'trazer', ('bring', 'We bring the water.', 'Nós trazemos a água.'), ('brings', 'Maya brings a glass.', 'A Maya traz um copo.'), ('brought', 'She brought a napkin.', 'Ela trouxe um guardanapo.'), ('bringing', 'Maya is bringing the water.', 'A Maya está trazendo a água.'), 'Irregular: bring vira brought.'),
  vb('need', '🧻', 'precisar', ('need', 'I need a napkin.', 'Eu preciso de um guardanapo.'), ('needs', 'He needs a fork.', 'Ele precisa de um garfo.'), ('needed', 'I needed more ice.', 'Eu precisei de mais gelo.'), ('needing', 'We are needing a spoon.', 'Estamos precisando de uma colher.'), 'Need + substantivo: need a fork. Na prática, I need… é muito usado.'),
  vb('take', '⏱️', 'levar / tomar', ('take', 'I take my time.', 'Eu levo o meu tempo.'), ('takes', 'He takes five minutes.', 'Ele leva cinco minutos.'), ('took', 'We took ten minutes.', 'Nós levamos dez minutos.'), ('taking', 'I am taking my time.', 'Estou levando o meu tempo.'), 'Irregular: take vira took. Take your time = sem pressa.')],
 verb_game=[
  dict(scene='Maya traz água para a mesa agora.', en='Maya ___ the water to the table.', opts=['bring', 'brings', 'brought'], ans=1, pt='A Maya traz a água para a mesa.', why='Com “Maya” (ela), o presente leva -s: brings.'),
  dict(scene='Ontem ele bebeu só água.', en='Yesterday he ___ just water.', opts=['drink', 'drank', 'drinking'], ans=1, pt='Ontem ele bebeu só água.', why='“Yesterday” pede passado; drink é irregular: drank.'),
  dict(scene='Você pede mais tempo para decidir.', en='I need to ___ my time.', opts=['take', 'took', 'takes'], ans=0, pt='Eu preciso levar meu tempo.', why='Depois de “to” o verbo fica na forma base: take.'),
  dict(scene='Você está sem guardanapo.', en='I ___ a napkin, please.', opts=['needs', 'need', 'needed'], ans=1, pt='Eu preciso de um guardanapo, por favor.', why='Com “I” o presente usa a forma base: need.')],
 expressions=[
  dict(en='Just water, please.', pt='Só água, por favor.', ex='Just water, please. No ice.', exp='Para pedir só água, sem mais nada.', c='a'),
  dict(en='No ice, please.', pt='Sem gelo, por favor.', ex='Water with no ice, please.', exp='Quando você não quer gelo na bebida.', c='b'),
  dict(en='Take your time.', pt='Fique à vontade / sem pressa.', ex='No problem. Take your time.', exp='O garçom diz isso quando você ainda não decidiu.', c='c'),
  dict(en='Ready to order?', pt='Pronto para pedir?', ex='Hi! Ready to order?', exp='Pergunta do garçom antes de anotar o pedido.', c='d'),
  dict(en='Not yet.', pt='Ainda não.', ex='Not yet. Five more minutes.', exp='Resposta curta quando você ainda não está pronto.', c='a'),
  dict(en='Here you go.', pt='Aqui está.', ex='Here you go. Enjoy your meal!', exp='Ao entregar algo à mesa.', c='b')],
 expr_game=[
  dict(cue='Você quer água, sem gelo.', opts=['No ice, please.', 'Not yet.', 'Here you go.'], ans=0, why='No ice, please = sem gelo, por favor.'),
  dict(cue='O garçom pergunta se você já quer pedir, mas você ainda não decidiu.', opts=['Just water, please.', 'Not yet.', 'Enjoy your meal!'], ans=1, why='Not yet = ainda não.'),
  dict(cue='Você quer dizer ao garçom que ele pode ir sem pressa.', opts=['Take your time.', 'Here you go.', 'Ready to order?'], ans=0, why='Take your time = sem pressa.')])
