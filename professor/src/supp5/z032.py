"""Bloco de verbos e expressões da aula 032: pedir água no restaurante."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('refill', '🔄', 'encher de novo', ('refill', 'I refill my glass.', 'Eu encho meu copo de novo.'), ('refills', 'Maya refills the water.', 'A Maya completa a água.'), ('refilled', 'She refilled my glass.', 'Ela completou meu copo.'), ('refilling', 'Maya is refilling the glasses.', 'A Maya está completando os copos.'), 'Refill é completar o copo; muito usado em restaurantes.'),
  vb('offer', '🙋', 'oferecer', ('offer', 'We offer free water.', 'Nós oferecemos água de graça.'), ('offers', 'Maya offers some ice.', 'A Maya oferece gelo.'), ('offered', 'She offered lemonade.', 'Ela ofereceu limonada.'), ('offering', 'Maya is offering a refill.', 'A Maya está oferecendo mais água.'), 'Offer + algo: offer water. Passado regular: offered.'),
  vb('serve', '🍽️', 'servir', ('serve', 'We serve water with ice.', 'Nós servimos água com gelo.'), ('serves', 'Maya serves the table.', 'A Maya serve a mesa.'), ('served', 'She served the lemonade.', 'Ela serviu a limonada.'), ('serving', 'Maya is serving the water.', 'A Maya está servindo a água.'), 'Serve é servir comida e bebida; passado regular: served.'),
  vb('pass', '🧻', 'passar / alcançar', ('pass', 'I pass him a napkin.', 'Eu passo um guardanapo a ele.'), ('passes', 'She passes the salt.', 'Ela passa o sal.'), ('passed', 'He passed the menu.', 'Ele passou o cardápio.'), ('passing', 'I am passing the water.', 'Estou passando a água.'), 'Pass me the…, please = me passe o… (na mesa). Com he/she: passes.'),
  vb('squeeze', '🍋', 'espremer', ('squeeze', 'I squeeze lemon in my water.', 'Eu espremo limão na minha água.'), ('squeezes', 'He squeezes a lemon.', 'Ele espreme um limão.'), ('squeezed', 'She squeezed some lime.', 'Ela espremeu um pouco de limão.'), ('squeezing', 'I am squeezing a lemon.', 'Estou espremendo um limão.'), 'Squeeze a lemon: espremer limão na água.')],
 verb_game=[
  dict(scene='A Maya serve a água na mesa agora.', en='Maya ___ the water to the table.', opts=['serve', 'serves', 'served'], ans=1, pt='A Maya serve a água na mesa.', why='Com “Maya” (ela), o presente leva -s: serves.'),
  dict(scene='Ontem ele completou o copo.', en='Yesterday he ___ my glass.', opts=['refill', 'refilled', 'refilling'], ans=1, pt='Ontem ele completou meu copo.', why='“Yesterday” pede passado: refilled.'),
  dict(scene='Você espreme limão na água.', en='I ___ lemon in my water.', opts=['squeeze', 'squeezes', 'squeezed'], ans=0, pt='Eu espremo limão na minha água.', why='Com “I” o presente usa a forma base: squeeze.'),
  dict(scene='Você pede o guardanapo na mesa.', en='Can you ___ me a napkin, please?', opts=['pass', 'passes', 'passed'], ans=0, pt='Pode me passar um guardanapo, por favor?', why='Depois de “can you” a forma base: pass.')],
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
