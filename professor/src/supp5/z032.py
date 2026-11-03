"""Bloco de verbos e expressões da aula 032: pedir água no restaurante."""
K = ["eu · você · nós · eles", "ele · ela", "passado", "-ing"]
def vb(v, ic, pt, base, third, past, ing, note):
    return dict(v=v, ic=ic, pt=pt, note=note, forms=[
        dict(k=K[0], en=base[0], ex=base[1], pt=base[2]), dict(k=K[1], en=third[0], ex=third[1], pt=third[2]),
        dict(k=K[2], en=past[0], ex=past[1], pt=past[2]), dict(k=K[3], en=ing[0], ex=ing[1], pt=ing[2])])
Z = dict(
 verbs=[
  vb('pour', '🫗', 'servir / despejar', ('pour', 'I pour more water.', 'Eu sirvo mais água.'), ('pours', 'Maya pours my water.', 'A Maya serve minha água.'), ('poured', 'He poured some juice.', 'Ele serviu um pouco de suco.'), ('pouring', 'She is pouring tea.', 'Ela está servindo chá.'), 'Pour é servir líquido de uma jarra.'),
  vb('help', '🙋', 'ajudar', ('help', 'We help every guest.', 'Nós ajudamos todos os clientes.'), ('helps', 'He helps us with the menu.', 'Ele nos ajuda com o cardápio.'), ('helped', 'She helped me yesterday.', 'Ela me ajudou ontem.'), ('helping', 'He is helping a family.', 'Ele está ajudando uma família.'), 'Help + pessoa: help me, help us.'),
  vb('bring', '🍽️', 'trazer', ('bring', 'We bring the water first.', 'Nós trazemos a água primeiro.'), ('brings', 'Maya brings the bread.', 'A Maya traz o pão.'), ('brought', 'He brought the soup.', 'Ele trouxe a sopa.'), ('bringing', 'She is bringing our plates.', 'Ela está trazendo nossos pratos.'), 'Passado irregular: bring vira brought.'),
  vb('pass', '🧻', 'passar / alcançar', ('pass', 'I pass him a napkin.', 'Eu passo um guardanapo a ele.'), ('passes', 'She passes the salt.', 'Ela passa o sal.'), ('passed', 'He passed the menu.', 'Ele passou o cardápio.'), ('passing', 'I am passing the water.', 'Estou passando a água.'), 'Pass me the…, please = me passe o… (na mesa). Com he/she: passes.'),
  vb('use', '🍋', 'usar', ('use', 'I use lemon in my water.', 'Eu uso limão na minha água.'), ('uses', 'He uses a straw.', 'Ele usa um canudo.'), ('used', 'She used two napkins.', 'Ela usou dois guardanapos.'), ('using', 'I am using a straw.', 'Estou usando um canudo.'), 'Use perde o e antes de -ing: using.')],
 verb_game=[
  dict(scene='A Maya traz a água para a mesa.', en='Maya ___ the water to the table.', opts=['bring', 'brings', 'brought'], ans=1, pt='A Maya traz a água para a mesa.', why='Com “Maya” (ela), o presente leva -s: brings.'),
  dict(scene='Ontem ele serviu mais água no meu copo.', en='Yesterday he ___ water in my glass.', opts=['pour', 'poured', 'pouring'], ans=1, pt='Ontem ele serviu água no meu copo.', why='“Yesterday” pede passado: poured.'),
  dict(scene='Você usa limão na água.', en='I ___ lemon in my water.', opts=['use', 'uses', 'used'], ans=0, pt='Eu uso limão na minha água.', why='Com “I” o presente usa a forma base: use.'),
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
