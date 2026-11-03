X = dict(
 key={'big': 'How do you want your eggs?', 'label': 'Pedir ovos no café da manhã', 'sub': 'Em lanchonetes dos EUA, o garçom costuma perguntar como você quer os ovos; os estilos mais comuns são scrambled, fried e boiled.'},
 mini=[
  {'who': 'Leo', 'en': 'Good morning! Table for {one|two|three}?', 'pt': 'Bom dia! Mesa para {um|dois|três}?'},
  {'who': 'You', 'en': 'Yes, please. {Coffee|Tea|Juice}, please.', 'pt': 'Sim, por favor. {Café|Chá|Suco}, por favor.'},
  {'who': 'Leo', 'en': 'Are you ready to order? How do you want your {eggs|pancakes|toast}?', 'pt': 'Pronto para pedir? Como quer {seus ovos|suas panquecas|sua torrada}?'},
  {'who': 'You', 'en': 'I’d like {scrambled|fried|boiled} eggs, please.', 'pt': 'Eu gostaria de ovos {mexidos|fritos|cozidos}, por favor.'}],
 dlg=[
  {'who': 'Leo', 'en': 'Good morning! Table for {one|two|three}?', 'pt': 'Bom dia! Mesa para {um|dois|três}?'},
  {'who': 'You', 'en': 'Yes, please.', 'pt': 'Sim, por favor.'},
  {'who': 'Leo', 'en': 'Here’s the menu. {Coffee|Tea|Juice}?', 'pt': 'Aqui está o cardápio. {Café|Chá|Suco}?'},
  {'who': 'You', 'en': 'Yes, please. With {milk|sugar|lemon}.', 'pt': 'Sim, por favor. Com {leite|açúcar|limão}.'},
  {'who': 'Leo', 'en': 'Are you ready to order?', 'pt': 'Pronto para pedir?'},
  {'who': 'You', 'en': 'I’d like {pancakes|toast|bacon} and eggs.', 'pt': 'Eu gostaria de {panquecas|torrada|bacon} e ovos.'},
  {'who': 'Leo', 'en': 'How do you want your {eggs|toast|bacon}?', 'pt': 'Como quer {seus ovos|sua torrada|seu bacon}?'},
  {'who': 'You', 'en': '{Scrambled|Fried|Boiled}, please.', 'pt': '{Mexidos|Fritos|Cozidos}, por favor.'},
  {'who': 'Leo', 'en': 'Enjoy your {breakfast|meal|lunch}!', 'pt': 'Aproveite seu {café da manhã|refeição|almoço}!'}],
 vocab=[
  {'w': 'breakfast', 'pt': 'café da manhã', 'e': '🍳', 'ex': ['I have breakfast at seven.', 'Enjoy your breakfast!']},
  {'w': 'pancakes', 'pt': 'panquecas', 'e': '🥞', 'ex': ['I’d like pancakes, please.', 'The pancakes are hot.']},
  {'w': 'bacon', 'pt': 'bacon', 'e': '🥓', 'ex': ['Eggs and bacon, please.', 'I like bacon.']},
  {'w': 'juice', 'pt': 'suco', 'e': '🧃', 'ex': ['A glass of orange juice, please.', 'The juice is cold.']},
  {'w': 'toast', 'pt': 'torrada', 'e': '🍞', 'ex': ['Toast with butter, please.', 'I want toast and eggs.']},
  {'w': 'scrambled', 'pt': 'mexido', 'e': '🥚', 'ex': ['Scrambled eggs, please.', 'I like my eggs scrambled.']}],
 molds=[
  {'title': 'Pedir o prato', 'frame': 'I’d like {food} and eggs.', 'slots': [{'key': 'food', 'opts': ['pancakes', 'toast', 'bacon']}], 'model': 'I’d like pancakes and eggs.', 'note': 'I’d like… é um pedido educado, mais suave que I want.'},
  {'title': 'Escolher o estilo dos ovos', 'frame': '{style}, please.', 'slots': [{'key': 'style', 'opts': ['Scrambled', 'Fried', 'Boiled']}], 'model': 'Scrambled, please.', 'note': 'Responda à pergunta How do you want your eggs? com o estilo.'},
  {'title': 'Pedir bebida (escrever)', 'frame': 'Coffee with {extra} and a glass of {drink}, please.', 'slots': [{'key': 'extra', 'opts': ['milk', 'sugar', 'lemon']}, {'key': 'drink', 'opts': ['juice', 'water', 'milk']}], 'model': 'Coffee with milk and a glass of juice, please.', 'note': 'With + ingrediente mostra o que vem na bebida.'}],
 sounds=[
  {'say': 'I’d like pancakes and eggs.', 'tag': 'redução: and', 'tip': 'And fica fraco: “n”. Diga “pancakes-n-eggs”.'},
  {'say': 'Are you ready to order?', 'tag': 'ritmo: palavras fortes', 'tip': 'Acentue ready e order; are you soa leve, quase “aryu”.'},
  {'say': 'Scrambled, please.', 'tag': 'acento: scrambled', 'tip': 'A sílaba forte é SCRAM. Fale “SCRAM-buld”.'}],
 role={'turns': [
  {'npc': 'Good morning! Table for one?', 'opts': [
   {'en': 'Yes, please.', 'pt': 'Sim, por favor.', 'reply': 'Great! Here’s the menu. Coffee?'},
   {'en': 'Yes, for one, please.', 'pt': 'Sim, para um, por favor.', 'reply': 'Right this way. Here’s the menu. Coffee?'},
   {'en': 'Yes, thanks. By the window?', 'pt': 'Sim, obrigado. Perto da janela?', 'reply': 'Sure! Here’s the menu. Coffee?'}]},
  {'npc': 'Here’s the menu. Coffee?', 'opts': [
   {'en': 'Yes, please. With milk.', 'pt': 'Sim, por favor. Com leite.', 'reply': 'Coffee with milk. Are you ready to order?'},
   {'en': 'Tea, please. With lemon.', 'pt': 'Chá, por favor. Com limão.', 'reply': 'Tea with lemon. Are you ready to order?'},
   {'en': 'Orange juice, please.', 'pt': 'Suco de laranja, por favor.', 'reply': 'One orange juice. Are you ready to order?'}]},
  {'npc': 'Are you ready to order?', 'opts': [
   {'en': 'I’d like pancakes and eggs.', 'pt': 'Eu gostaria de panquecas e ovos.', 'reply': 'Pancakes and eggs. How do you want your eggs?'},
   {'en': 'I’d like toast and eggs.', 'pt': 'Eu gostaria de torrada e ovos.', 'reply': 'Toast and eggs. How do you want your eggs?'},
   {'en': 'I’d like bacon and eggs.', 'pt': 'Eu gostaria de bacon e ovos.', 'reply': 'Bacon and eggs. How do you want your eggs?'}]},
  {'npc': 'How do you want your eggs?', 'opts': [
   {'en': 'Scrambled, please.', 'pt': 'Mexidos, por favor.', 'reply': 'Scrambled. Enjoy your breakfast!'},
   {'en': 'Fried, please.', 'pt': 'Fritos, por favor.', 'reply': 'Fried. Enjoy your breakfast!'},
   {'en': 'Boiled, please.', 'pt': 'Cozidos, por favor.', 'reply': 'Boiled. Enjoy your breakfast!'}]}],
  'change': ['Você está com um amigo: peça mesa para dois.', 'Não tem leite: peça o café com açúcar.', 'Você não come bacon: peça só ovos e torrada.']},
 writing={'task': 'Escreva seu pedido de café da manhã para o garçom Leo: bebida, comida e estilo dos ovos.',
  'model': 'Good morning! I’d like coffee with milk, pancakes and scrambled eggs, please. Thank you!',
  'kw': ['coffee', 'pancakes', 'eggs', 'please'],
  'checks': ['Usei I’d like para pedir.', 'Pedi bebida, comida e ovos.', 'Terminei com please ou thank you.']},
 scenes={'pool': ['diner', 'restaurant', 'cafe2', 'kitchen'], 'npc': {'g': 'm', 'role': 'waiter'}, 'you': {'g': 'f'}},
 convo={'npc': {'name': 'Leo'}, 'story': 'Você está numa lanchonete de manhã. Leo é o garçom. Peça seu café da manhã.', 'turns': [
  {'npc': 'Good morning! Table for one?', 'pt': 'Bom dia! Mesa para um?', 'opts': [
   {'en': 'Good night!', 'pt': 'Boa noite!', 'ok': False, 'fb': 'É de manhã; boa noite é despedida à noite.'},
   {'en': 'Yes, please.', 'pt': 'Sim, por favor.', 'ok': True, 'fb': 'Resposta direta à pergunta.'},
   {'en': 'I’d like pancakes and eggs.', 'pt': 'Eu gostaria de panquecas e ovos.', 'ok': False, 'fb': 'É cedo para pedir comida; primeiro a mesa.'}]},
  {'npc': 'Here’s the menu. Coffee?', 'pt': 'Aqui está o cardápio. Café?', 'opts': [
   {'en': 'Yes, please. With milk.', 'pt': 'Sim, por favor. Com leite.', 'ok': True, 'fb': 'Aceita e especifica o café.'},
   {'en': 'Table for one.', 'pt': 'Mesa para um.', 'ok': False, 'fb': 'Isso já foi resolvido; agora é a bebida.'},
   {'en': 'Enjoy your coffee!', 'pt': 'Aproveite seu café!', 'ok': False, 'fb': 'Quem diz isso é o garçom.'}]},
  {'npc': 'Are you ready to order?', 'pt': 'Pronto para pedir?', 'opts': [
   {'en': 'Scrambled, please.', 'pt': 'Mexidos, por favor.', 'ok': False, 'fb': 'Ele ainda não perguntou dos ovos; diga o que quer comer.'},
   {'en': 'No, I’m the waiter.', 'pt': 'Não, eu sou o garçom.', 'ok': False, 'fb': 'O garçom é Leo.'},
   {'en': 'I’d like pancakes and eggs.', 'pt': 'Eu gostaria de panquecas e ovos.', 'ok': True, 'fb': 'Pedido claro e educado.'}]},
  {'npc': 'How do you want your eggs?', 'pt': 'Como quer seus ovos?', 'opts': [
   {'en': 'Scrambled, please.', 'pt': 'Mexidos, por favor.', 'ok': True, 'fb': 'Descreve o estilo dos ovos.'},
   {'en': 'Yes, I’d like eggs.', 'pt': 'Sim, eu gostaria de ovos.', 'ok': False, 'fb': 'É pergunta de “como”, não de sim ou não.'},
   {'en': 'Eggs are good for breakfast.', 'pt': 'Ovos são bons no café da manhã.', 'ok': False, 'fb': 'Verdade, mas não responde como quer os ovos.'}]},
  {'npc': 'Enjoy your breakfast!', 'pt': 'Bom apetite!', 'opts': [
   {'en': 'Thank you!', 'pt': 'Obrigado!', 'ok': True, 'fb': 'Agradecer é a resposta natural.'},
   {'en': 'Are you ready to order?', 'pt': 'Está pronto para pedir?', 'ok': False, 'fb': 'Essa pergunta é do garçom, e o pedido já foi feito.'},
   {'en': 'Table for one, please.', 'pt': 'Mesa para um, por favor.', 'ok': False, 'fb': 'Você já está sentado e comendo.'}]}]},
)
