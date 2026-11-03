X = dict(
 key={'big': 'Hot or iced?', 'label': 'Personalizar o café', 'sub': 'Ao pedir um café nos EUA, é comum personalizar: tamanho, tipo de leite, quente ou gelado.'},
 mini=[
  {'who': 'Mei', 'en': 'Hi! What can I get started for you {today|this morning|now}?', 'pt': 'Oi! O que posso começar a preparar para você {hoje|esta manhã|agora}?'},
  {'who': 'You', 'en': 'A {latte|cappuccino|coffee}, please.', 'pt': 'Um {latte|cappuccino|café}, por favor.'},
  {'who': 'Mei', 'en': 'What size? Small, {medium|large|small} or {large|medium|extra large}?', 'pt': 'Que tamanho? Pequeno, {médio|grande|pequeno} ou {grande|médio|extra grande}?'},
  {'who': 'You', 'en': '{Medium|Large|Small}. With {oat milk|soy milk|sugar}.', 'pt': '{Médio|Grande|Pequeno}. Com {leite de aveia|leite de soja|açúcar}.'}],
 dlg=[
  {'who': 'Mei', 'en': 'Hi! What can I get started for you?', 'pt': 'Oi! O que posso preparar?'},
  {'who': 'You', 'en': 'A {latte|cappuccino|tea}, please.', 'pt': 'Um {latte|cappuccino|chá}, por favor.'},
  {'who': 'Mei', 'en': 'What size? Small, medium or large?', 'pt': 'Que tamanho? Pequeno, médio ou grande?'},
  {'who': 'You', 'en': '{Medium|Large|Small}. With {oat milk|soy milk|sugar}.', 'pt': '{Médio|Grande|Pequeno}. Com {leite de aveia|leite de soja|açúcar}.'},
  {'who': 'Mei', 'en': '{Hot|Cold|Warm} or iced?', 'pt': '{Quente|Frio|Morno} ou gelado?'},
  {'who': 'You', 'en': '{Hot|Iced|Warm}, please.', 'pt': '{Quente|Gelado|Morno}, por favor.'},
  {'who': 'Mei', 'en': 'Anything to {eat|drink|add}?', 'pt': 'Algo para {comer|beber|acrescentar}?'},
  {'who': 'You', 'en': 'A {blueberry|banana|chocolate} muffin.', 'pt': 'Um muffin de {mirtilo|banana|chocolate}.'},
  {'who': 'Mei', 'en': 'Have a great {day|morning|afternoon}!', 'pt': 'Tenha um ótimo {dia|manhã|tarde}!'}],
 vocab=[
  {'w': 'latte', 'pt': 'latte (café com leite)', 'e': '☕', 'ex': ['A latte, please.', 'This latte is hot.']},
  {'w': 'sugar', 'pt': 'açúcar', 'e': '🍬', 'ex': ['Can I have sugar?', 'No sugar, please.']},
  {'w': 'muffin', 'pt': 'muffin', 'e': '🧁', 'ex': ['A blueberry muffin, please.', 'The muffin is warm.']},
  {'w': 'hot', 'pt': 'quente', 'e': '🔥', 'ex': ['Hot, please.', 'The coffee is hot.']},
  {'w': 'iced', 'pt': 'gelado', 'e': '🧊', 'ex': ['An iced latte, please.', 'I like iced tea.']},
  {'w': 'size', 'pt': 'tamanho', 'e': '📏', 'ex': ['What size?', 'This size is small.']}],
 molds=[
  {'title': 'Pedir bebida e tamanho', 'frame': 'A {size} {drink}, please.', 'slots': [{'key': 'size', 'opts': ['medium', 'small', 'large']}, {'key': 'drink', 'opts': ['latte', 'cappuccino', 'tea']}], 'model': 'A medium latte, please.', 'note': 'Em inglês, o tamanho vem antes da bebida.'},
  {'title': 'Personalizar', 'frame': '{temp}, with {extra}, please.', 'slots': [{'key': 'temp', 'opts': ['Hot', 'Iced', 'Extra hot']}, {'key': 'extra', 'opts': ['oat milk', 'soy milk', 'sugar']}], 'model': 'Hot, with oat milk, please.', 'note': 'With + item acrescenta algo; without tira.'},
  {'title': 'Escolher um lanche (escrever)', 'frame': 'And a {flavor} muffin, please.', 'slots': [{'key': 'flavor', 'opts': ['blueberry', 'banana', 'chocolate']}], 'model': 'And a blueberry muffin, please.', 'note': 'O sabor vem antes de muffin.'}],
 sounds=[
  {'say': 'Hot or iced?', 'tag': 'entonação: escolha', 'tip': 'Suba em hot e desça em iced. A voz mostra que há duas opções.'},
  {'say': 'A latte, please.', 'tag': 'acento: latte', 'tip': 'A sílaba forte é LA: “LA-tei”. O a do início quase some.'},
  {'say': 'With oat milk.', 'tag': 'ligação: with oat', 'tip': 'With e oat se juntam: “wi-thoat”. Sem pausa.'}],
 role={'turns': [
  {'npc': 'Hi! What can I get started for you?', 'opts': [
   {'en': 'A latte, please.', 'pt': 'Um latte, por favor.', 'reply': 'A latte. What size? Small, medium or large?'},
   {'en': 'A cappuccino, please.', 'pt': 'Um cappuccino, por favor.', 'reply': 'A cappuccino. What size? Small, medium or large?'},
   {'en': 'Can I get a tea, please?', 'pt': 'Posso pedir um chá, por favor?', 'reply': 'Sure! What size? Small, medium or large?'}]},
  {'npc': 'What size? Small, medium or large?', 'opts': [
   {'en': 'Medium. With oat milk.', 'pt': 'Médio. Com leite de aveia.', 'reply': 'Medium with oat milk. Hot or iced?'},
   {'en': 'Large, please. With soy milk.', 'pt': 'Grande, por favor. Com leite de soja.', 'reply': 'Large with soy milk. Hot or iced?'},
   {'en': 'Small, with sugar, please.', 'pt': 'Pequeno, com açúcar, por favor.', 'reply': 'Small with sugar. Hot or iced?'}]},
  {'npc': 'Hot or iced?', 'opts': [
   {'en': 'Hot, please.', 'pt': 'Quente, por favor.', 'reply': 'Hot. Anything to eat?'},
   {'en': 'Iced, please.', 'pt': 'Gelado, por favor.', 'reply': 'Iced. Anything to eat?'},
   {'en': 'Hot, thanks.', 'pt': 'Quente, obrigado.', 'reply': 'Hot. Anything to eat?'}]},
  {'npc': 'Anything to eat?', 'opts': [
   {'en': 'A blueberry muffin.', 'pt': 'Um muffin de mirtilo.', 'reply': 'A blueberry muffin. Have a great day!'},
   {'en': 'A banana muffin, please.', 'pt': 'Um muffin de banana, por favor.', 'reply': 'A banana muffin. Have a great day!'},
   {'en': 'No, thanks. Just the latte.', 'pt': 'Não, obrigado. Só o latte.', 'reply': 'Just the latte. Have a great day!'}]}],
  'change': ['Está muito calor: mude para gelado e peça tamanho grande.', 'Você não toma leite comum: peça leite de aveia ou de soja.', 'O muffin acabou: escolha outro lanche.']},
 writing={'task': 'Escreva seu pedido de café para Mei: bebida, tamanho, leite, quente ou gelado e um lanche.',
  'model': 'Hi! A medium latte with oat milk, hot, please. And a blueberry muffin. Thank you!',
  'kw': ['latte', 'medium', 'hot', 'muffin'],
  'checks': ['Pedi a bebida com o tamanho.', 'Escolhi o leite e quente ou gelado.', 'Pedi um lanche e agradeci.']},
 scenes={'pool': ['cafe', 'cafe2', 'cafe3', 'bakery'], 'npc': {'g': 'f', 'role': 'barista'}, 'you': {'g': 'f'}},
 convo={'npc': {'name': 'Mei'}, 'story': 'Você está numa cafeteria. Mei é a barista. Faça o café do seu jeito.', 'turns': [
  {'npc': 'Hi! What can I get started for you?', 'pt': 'Oi! O que posso preparar?', 'opts': [
   {'en': 'Have a great day!', 'pt': 'Tenha um ótimo dia!', 'ok': False, 'fb': 'É uma despedida; você precisa pedir a bebida.'},
   {'en': 'A latte, please.', 'pt': 'Um latte, por favor.', 'ok': True, 'fb': 'Faz o pedido.'},
   {'en': 'I’m a customer.', 'pt': 'Eu sou cliente.', 'ok': False, 'fb': 'Verdade, mas ela quer saber o pedido.'}]},
  {'npc': 'What size? Small, medium or large?', 'pt': 'Que tamanho? Pequeno, médio ou grande?', 'opts': [
   {'en': 'Medium. With oat milk.', 'pt': 'Médio. Com leite de aveia.', 'ok': True, 'fb': 'Escolhe o tamanho e personaliza.'},
   {'en': 'Yes, please.', 'pt': 'Sim, por favor.', 'ok': False, 'fb': 'É pergunta de escolha: small, medium ou large.'},
   {'en': 'Hot, please.', 'pt': 'Quente, por favor.', 'ok': False, 'fb': 'Ela ainda não perguntou da temperatura.'}]},
  {'npc': 'Hot or iced?', 'pt': 'Quente ou gelado?', 'opts': [
   {'en': 'Medium, please.', 'pt': 'Médio, por favor.', 'ok': False, 'fb': 'O tamanho já foi escolhido.'},
   {'en': 'Hot, please.', 'pt': 'Quente, por favor.', 'ok': True, 'fb': 'Escolhe entre hot e iced.'},
   {'en': 'It is a latte.', 'pt': 'É um latte.', 'ok': False, 'fb': 'Ela pergunta quente ou gelado.'}]},
  {'npc': 'Anything to eat?', 'pt': 'Algo para comer?', 'opts': [
   {'en': 'Yes, I am hot.', 'pt': 'Sim, estou com calor.', 'ok': False, 'fb': 'Mistura as perguntas; ela fala de comida.'},
   {'en': 'Large, please.', 'pt': 'Grande, por favor.', 'ok': False, 'fb': 'O tamanho já foi escolhido.'},
   {'en': 'A blueberry muffin.', 'pt': 'Um muffin de mirtilo.', 'ok': True, 'fb': 'Escolhe algo para comer.'}]},
  {'npc': 'Have a great day!', 'pt': 'Tenha um ótimo dia!', 'opts': [
   {'en': 'Thanks! You too.', 'pt': 'Obrigado! Você também.', 'ok': True, 'fb': 'Retribui o desejo.'},
   {'en': 'Hot or iced?', 'pt': 'Quente ou gelado?', 'ok': False, 'fb': 'Essa pergunta era dela, e o pedido já está pronto.'},
   {'en': 'A latte, please.', 'pt': 'Um latte, por favor.', 'ok': False, 'fb': 'O pedido já foi feito; é hora de se despedir.'}]}]},
)
