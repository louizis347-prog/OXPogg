X = dict(
 key={'big': 'Is there meat in it?', 'label': 'Pratos vegetarianos', 'sub': 'Vegetariano (vegetarian) costuma significar sem carne; algumas pessoas também evitam peixe ou outros produtos, então vale perguntar.'},
 mini=[
  {'who': 'Carlos', 'en': 'Hi! Do you have {vegetarian dishes|vegetarian soup|vegetarian pizza}?', 'pt': 'Oi! Vocês têm {pratos vegetarianos|sopa vegetariana|pizza vegetariana}?'},
  {'who': 'You', 'en': 'Yes, we do. The {pasta|soup|salad} is vegetarian.', 'pt': 'Temos. {A massa|A sopa|A salada} é vegetariana.'},
  {'who': 'Carlos', 'en': 'Great. Is there {meat|fish|chicken} in it?', 'pt': 'Ótimo. Tem {carne|peixe|frango}?'},
  {'who': 'You', 'en': 'No {meat|fish|chicken}. Just {tomato|cheese|vegetables}.', 'pt': 'Sem {carne|peixe|frango}. Só {tomate|queijo|legumes}.'}],
 dlg=[
  {'who': 'Carlos', 'en': 'Hi! Do you have vegetarian {dishes|soups|pizzas}?', 'pt': 'Oi! Vocês têm {pratos|sopas|pizzas} vegetarianos?'},
  {'who': 'You', 'en': 'Yes, we do. The {pasta|soup|salad} is vegetarian.', 'pt': 'Temos. {A massa|A sopa|A salada} é vegetariana.'},
  {'who': 'Carlos', 'en': 'Great. Is there {meat|fish|chicken} in it?', 'pt': 'Ótimo. Tem {carne|peixe|frango}?'},
  {'who': 'You', 'en': 'No meat. Just {tomato|cheese|vegetables}.', 'pt': 'Sem carne. Só {tomate|queijo|legumes}.'},
  {'who': 'Carlos', 'en': 'I don’t eat meat or {fish|eggs|dairy}.', 'pt': 'Não como carne nem {peixe|ovos|laticínios}.'},
  {'who': 'You', 'en': 'No problem. We have a veggie {burger|pizza|salad} too.', 'pt': 'Sem problema. Também temos {hambúrguer|pizza|salada} de legumes.'},
  {'who': 'Carlos', 'en': 'I’ll have the {pasta|soup|veggie burger}, please.', 'pt': 'Vou querer {a massa|a sopa|o hambúrguer de legumes}, por favor.'},
  {'who': 'You', 'en': 'Good {choice|idea|order}!', 'pt': 'Boa {escolha|ideia|decisão}!'},
  {'who': 'Carlos', 'en': 'Enjoy your {pasta|soup|burger}!', 'pt': 'Aproveite {a massa|a sopa|o hambúrguer}!'}],
 vocab=[
  {'w': 'vegetable', 'pt': 'legume', 'e': '🥦', 'ex': ['The soup has vegetables.', 'I like vegetable pizza.']},
  {'w': 'soup', 'pt': 'sopa', 'e': '🍲', 'ex': ['The soup is hot.', 'I’ll have the vegetable soup.']},
  {'w': 'pasta', 'pt': 'massa', 'e': '🍝', 'ex': ['The pasta is vegetarian.', 'I’ll have the pasta, please.']},
  {'w': 'meat', 'pt': 'carne', 'e': '🥩', 'ex': ['Is there meat in it?', 'I don’t eat meat.']},
  {'w': 'ham', 'pt': 'presunto', 'e': '🍖', 'ex': ['Is there ham in it?', 'I like ham and cheese.']},
  {'w': 'vegetarian', 'pt': 'vegetariano', 'e': '🌱', 'ex': ['Do you have vegetarian dishes?', 'I am vegetarian.']}],
 molds=[
  {'title': 'Perguntar se tem carne', 'frame': 'Is there {food} in it?', 'slots': [{'key': 'food', 'opts': ['meat', 'fish', 'cheese']}], 'model': 'Is there meat in it?', 'note': 'Is there… in it? pergunta se um ingrediente está no prato.'},
  {'title': 'Dizer o que você não come', 'frame': 'I don’t eat {foods}.', 'slots': [{'key': 'foods', 'opts': ['meat or fish', 'pork or beef', 'fish or eggs']}], 'model': 'I don’t eat meat or fish.', 'note': 'Use or, e não and, numa frase negativa: I don’t eat meat or fish.'},
  {'title': 'Escolher o prato (escrever)', 'frame': 'I’ll have the {dish}, please. No {food}.', 'slots': [{'key': 'dish', 'opts': ['pasta', 'veggie burger', 'vegetable soup']}, {'key': 'food', 'opts': ['meat', 'fish', 'chicken']}], 'model': 'I’ll have the pasta, please. No meat.', 'note': 'No + ingrediente pede o prato sem aquele item.'}],
 sounds=[
  {'say': 'Is there meat in it?', 'tag': 'ligação: is there', 'tip': 'Is there se une: “is-thair”. Dê força a meat; in it vira “in-nit”.'},
  {'say': 'I don’t eat meat or fish.', 'tag': 'acento: don’t', 'tip': 'Dê força a don’t, meat e fish. Or fica fraco: “er”.'},
  {'say': 'vegetarian', 'tag': 'acento: vegetarian', 'tip': 'A sílaba forte é TAIR: ve-je-TAIR-i-an.'}],
 role={'turns': [
  {'npc': 'Hi! Do you have vegetarian dishes?', 'opts': [
   {'en': 'Yes, we do. The pasta is vegetarian.', 'pt': 'Temos. A massa é vegetariana.', 'reply': 'Great. Is there meat in it?'},
   {'en': 'Yes! The vegetable soup is vegetarian.', 'pt': 'Sim! A sopa de legumes é vegetariana.', 'reply': 'Great. Is there meat in it?'},
   {'en': 'Of course. The salad is vegetarian.', 'pt': 'Claro. A salada é vegetariana.', 'reply': 'Great. Is there meat in it?'}]},
  {'npc': 'Great. Is there meat in it?', 'opts': [
   {'en': 'No meat. Just tomato and cheese.', 'pt': 'Sem carne. Só tomate e queijo.', 'reply': 'Good. I don’t eat meat or fish.'},
   {'en': 'No, there isn’t. Just vegetables.', 'pt': 'Não tem. Só legumes.', 'reply': 'Good. I don’t eat meat or fish.'},
   {'en': 'No meat or fish. Only vegetables.', 'pt': 'Sem carne nem peixe. Só legumes.', 'reply': 'Perfect. I don’t eat meat or fish.'}]},
  {'npc': 'I don’t eat meat or fish.', 'opts': [
   {'en': 'No problem. We have a veggie burger too.', 'pt': 'Sem problema. Também temos hambúrguer de legumes.', 'reply': 'Nice! I’ll have the pasta, please.'},
   {'en': 'No problem. We have vegetable soup too.', 'pt': 'Sem problema. Também temos sopa de legumes.', 'reply': 'Nice! I’ll have the pasta, please.'},
   {'en': 'That’s fine. The pasta has no fish.', 'pt': 'Tudo bem. A massa não tem peixe.', 'reply': 'Great! I’ll have the pasta, please.'}]},
  {'npc': 'I’ll have the pasta, please.', 'opts': [
   {'en': 'Good choice!', 'pt': 'Boa escolha!', 'reply': 'Thanks! It looks great.'},
   {'en': 'Sure! One pasta.', 'pt': 'Claro! Uma massa.', 'reply': 'Thank you!'},
   {'en': 'Great! It’s very good.', 'pt': 'Ótimo! É muito boa.', 'reply': 'Good to know. Thanks!'}]}],
  'change': ['Carlos pergunta se o queijo é vegetariano: diga que vai confirmar com a cozinha.', 'Carlos também não come ovo: pergunte se ele quer uma opção sem ovo.', 'Acabou a massa: ofereça o hambúrguer de legumes ou a sopa.']},
 writing={'task': 'Escreva uma mensagem para um restaurante: diga que você não come carne nem peixe e pergunte se há um prato vegetariano.',
  'model': 'Hello! I don’t eat meat or fish. Do you have vegetarian dishes? Is there meat in the pasta? Thank you!',
  'kw': ['vegetarian', 'meat', 'fish', 'pasta'],
  'checks': ['Disse o que não como com I don’t eat…', 'Perguntei se há pratos vegetarianos.', 'Usei Is there… in…?']},
 scenes={'pool': ['cafe', 'cafe2', 'restaurant', 'cafe3'], 'npc': {'g': 'm', 'role': 'customer'}, 'you': {'g': 'f'}},
 convo={'npc': {'name': 'Carlos'}, 'story': 'Você trabalha num café. Carlos é vegetariano e quer saber o que pode comer.', 'turns': [
  {'npc': 'Hi! Do you have vegetarian dishes?', 'pt': 'Oi! Vocês têm pratos vegetarianos?', 'opts': [
   {'en': 'Yes, we do. The pasta is vegetarian.', 'pt': 'Temos. A massa é vegetariana.', 'ok': True, 'fb': 'Responde e dá uma opção.'},
   {'en': 'I’m vegetarian too.', 'pt': 'Eu também sou vegetariana.', 'ok': False, 'fb': 'Pode ser verdade, mas ele quer saber o que o café oferece.'},
   {'en': 'Yes, I have a dish.', 'pt': 'Sim, eu tenho um prato.', 'ok': False, 'fb': 'Não diz qual prato é vegetariano.'}]},
  {'npc': 'Great. Is there meat in it?', 'pt': 'Ótimo. Tem carne?', 'opts': [
   {'en': 'Yes, I like meat.', 'pt': 'Sim, eu gosto de carne.', 'ok': False, 'fb': 'Não responde se o prato tem carne.'},
   {'en': 'The pasta is hot.', 'pt': 'A massa está quente.', 'ok': False, 'fb': 'Ele quer saber os ingredientes.'},
   {'en': 'No meat. Just tomato and cheese.', 'pt': 'Sem carne. Só tomate e queijo.', 'ok': True, 'fb': 'Responde com os ingredientes.'}]},
  {'npc': 'I don’t eat meat or fish.', 'pt': 'Não como carne nem peixe.', 'opts': [
   {'en': 'No problem. We have a veggie burger too.', 'pt': 'Sem problema. Também temos hambúrguer de legumes.', 'ok': True, 'fb': 'Oferece outra opção sem carne.'},
   {'en': 'Eat fish, it’s good.', 'pt': 'Coma peixe, é bom.', 'ok': False, 'fb': 'Ele acabou de dizer que não come peixe.'},
   {'en': 'I don’t eat meat or fish.', 'pt': 'Não como carne nem peixe.', 'ok': False, 'fb': 'Você repete a frase dele em vez de ajudar.'}]},
  {'npc': 'I’ll have the pasta, please.', 'pt': 'Vou querer a massa, por favor.', 'opts': [
   {'en': 'Do you have vegetarian dishes?', 'pt': 'Vocês têm pratos vegetarianos?', 'ok': False, 'fb': 'Essa pergunta é dele, e já foi respondida.'},
   {'en': 'You’re welcome.', 'pt': 'De nada.', 'ok': False, 'fb': 'Ele ainda não agradeceu.'},
   {'en': 'Good choice!', 'pt': 'Boa escolha!', 'ok': True, 'fb': 'Confirma o pedido com simpatia.'}]},
  {'npc': 'Enjoy your pasta!', 'pt': 'Bom apetite!', 'opts': [
   {'en': 'Thank you! It looks great.', 'pt': 'Obrigado! Parece ótimo.', 'ok': True, 'fb': 'Agradece naturalmente.'},
   {'en': 'Is there meat in it?', 'pt': 'Tem carne?', 'ok': False, 'fb': 'Já foi esclarecido; agora é o fim da conversa.'},
   {'en': 'Yes, we do.', 'pt': 'Temos sim.', 'ok': False, 'fb': 'Não há pergunta para responder; a frase é um desejo.'}]}]},
)
