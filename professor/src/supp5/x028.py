X = dict(
 key={'big': 'I’m hungry!', 'label': 'Fome e sede', 'sub': 'Em inglês, fome e sede usam to be (I’m hungry, I’m thirsty), e não “have hunger”.'},
 mini=[
  {'who': 'Cole', 'en': 'I’m {hungry|thirsty|tired}. Are you {hungry|thirsty|tired}?', 'pt': 'Estou com {fome|sede|sono}. Você está com {fome|sede|sono}?'},
  {'who': 'You', 'en': 'Yes, {very|really|super}! And I’m {thirsty|so thirsty|really thirsty}.', 'pt': 'Sim, {muito|demais|bastante}! E estou {com sede|com muita sede|morrendo de sede}.'},
  {'who': 'Cole', 'en': 'Let’s get a {snack|sandwich|salad}.', 'pt': 'Vamos pegar {um lanche|um sanduíche|uma salada}.'},
  {'who': 'You', 'en': 'Do you want {a sandwich|an apple|a juice}?', 'pt': 'Você quer {um sanduíche|uma maçã|um suco}?'}],
 dlg=[
  {'who': 'Cole', 'en': 'I’m {hungry|so hungry|really hungry}. Are you hungry?', 'pt': 'Estou {com fome|com muita fome|morrendo de fome}. Você está com fome?'},
  {'who': 'You', 'en': 'Yes, {very|really|super}! And I’m thirsty.', 'pt': 'Sim, {muito|demais|bastante}! E estou com sede.'},
  {'who': 'Cole', 'en': 'Let’s get a {snack|sandwich|salad}.', 'pt': 'Vamos pegar {um lanche|um sanduíche|uma salada}.'},
  {'who': 'You', 'en': 'Do you want {a sandwich|an apple|a juice}?', 'pt': 'Você quer {um sanduíche|uma maçã|um suco}?'},
  {'who': 'Cole', 'en': 'Yes, and a {juice|water|soda}, please.', 'pt': 'Sim, e {um suco|uma água|um refrigerante}, por favor.'},
  {'who': 'You', 'en': 'I’ll get the {sandwiches|apples|snacks}.', 'pt': 'Eu pego {os sanduíches|as maçãs|os lanches}.'},
  {'who': 'Cole', 'en': 'Thanks! I’ll get the {drinks|waters|juices}.', 'pt': 'Valeu! Eu pego {as bebidas|as águas|os sucos}.'},
  {'who': 'You', 'en': 'Perfect {team|plan|idea}!', 'pt': '{Time perfeito|Plano perfeito|Ideia perfeita}!'},
  {'who': 'Cole', 'en': 'Here’s your {sandwich|apple|snack}. Enjoy!', 'pt': 'Aqui está {seu sanduíche|sua maçã|seu lanche}. Bom apetite!'}],
 vocab=[
  {'w': 'hungry', 'pt': 'com fome', 'e': '😋', 'ex': ['I’m hungry.', 'Are you hungry?']},
  {'w': 'thirsty', 'pt': 'com sede', 'e': '🥵', 'ex': ['I’m very thirsty.', 'Are you thirsty?']},
  {'w': 'cracker', 'pt': 'biscoito salgado', 'e': '🍘', 'ex': ['I eat a cracker.', 'Crackers are salty.']},
  {'w': 'peanut', 'pt': 'amendoim', 'e': '🥜', 'ex': ['I eat a peanut.', 'I like peanut butter.']},
  {'w': 'apple', 'pt': 'maçã', 'e': '🍎', 'ex': ['I’d like an apple.', 'The apple is red.']},
  {'w': 'sweet', 'pt': 'doce', 'e': '🍬', 'ex': ['I want something sweet.', 'This is very sweet.']},
 molds=[
  {'title': 'Dizer como você está', 'frame': 'I’m {feeling}. Are you {feeling2}?', 'slots': [{'key': 'feeling', 'opts': ['hungry', 'thirsty', 'tired']}, {'key': 'feeling2', 'opts': ['hungry', 'thirsty', 'tired']}], 'model': 'I’m hungry. Are you hungry?', 'note': 'Fome, sede e sono usam I’m + adjetivo. Nunca “I have hungry”.'},
  {'title': 'Propor e oferecer', 'frame': 'Let’s get {food}. Do you want {item}?', 'slots': [{'key': 'food', 'opts': ['a snack', 'lunch', 'a sandwich']}, {'key': 'item', 'opts': ['a juice', 'water', 'an apple']}], 'model': 'Let’s get a snack. Do you want a juice?', 'note': 'Let’s get… propõe uma ação juntos. Do you want…? oferece um item.'},
  {'title': 'Dividir tarefas (escrever)', 'frame': 'I’ll get the {thing1}. You get the {thing2}.', 'slots': [{'key': 'thing1', 'opts': ['sandwiches', 'drinks', 'apples']}, {'key': 'thing2', 'opts': ['drinks', 'snacks', 'napkins']}], 'model': 'I’ll get the sandwiches. You get the drinks.', 'note': 'I’ll get… decide e divide a tarefa na hora.'}],
 sounds=[
  {'say': 'I’m hungry. Are you hungry?', 'tag': 'ritmo: dois hungry', 'tip': 'Acentue hungry nas duas frases. I’m e are you ficam leves.'},
  {'say': 'Let’s get a snack.', 'tag': 'ligação: get a', 'tip': 'Get a se junta: “ge-ta”. Let’s fica curto.'},
  {'say': 'I’ll get the drinks.', 'tag': 'redução: I’ll', 'tip': 'I’ll soa como “ail”. A força vai em get e drinks.'}],
 role={'turns': [
  {'npc': 'I’m hungry. Are you hungry?', 'opts': [
   {'en': 'Yes, very! And I’m thirsty.', 'pt': 'Sim, muito! E estou com sede.', 'reply': 'Let’s get a snack.'},
   {'en': 'Yes, I am. Let’s get lunch.', 'pt': 'Sim, estou. Vamos almoçar.', 'reply': 'Good idea! Let’s get a snack first.'},
   {'en': 'A little. I’m thirsty too.', 'pt': 'Um pouco. Também estou com sede.', 'reply': 'OK, let’s get a snack and a drink.'}]},
  {'npc': 'Let’s get a snack.', 'opts': [
   {'en': 'Do you want a sandwich?', 'pt': 'Você quer um sanduíche?', 'reply': 'Yes, and a juice, please.'},
   {'en': 'Do you want an apple?', 'pt': 'Você quer uma maçã?', 'reply': 'Yes, and a juice, please.'},
   {'en': 'Good idea. Sandwich or salad?', 'pt': 'Boa ideia. Sanduíche ou salada?', 'reply': 'A sandwich, and a juice, please.'}]},
  {'npc': 'Yes, and a juice, please.', 'opts': [
   {'en': 'I’ll get the sandwiches.', 'pt': 'Eu pego os sanduíches.', 'reply': 'Thanks! I’ll get the drinks.'},
   {'en': 'OK. I’ll get the food.', 'pt': 'Certo. Eu pego a comida.', 'reply': 'Thanks! I’ll get the drinks.'},
   {'en': 'Sure. I’ll buy the sandwiches.', 'pt': 'Claro. Eu compro os sanduíches.', 'reply': 'Thanks! I’ll get the drinks.'}]},
  {'npc': 'Thanks! I’ll get the drinks.', 'opts': [
   {'en': 'Perfect team!', 'pt': 'Time perfeito!', 'reply': 'Ha! Here’s your sandwich. Enjoy!'},
   {'en': 'Great plan!', 'pt': 'Ótimo plano!', 'reply': 'Here’s your sandwich. Enjoy!'},
   {'en': 'Good idea. See you at the table.', 'pt': 'Boa ideia. Te vejo na mesa.', 'reply': 'See you! Here’s your sandwich. Enjoy!'}]}],
  'change': ['Cole diz que não está com fome, só com sede: sugira só bebidas.', 'Só há maçãs hoje: adapte a ideia do lanche.', 'Vocês estão com pressa: diga que precisam comer rápido.']},
 writing={'task': 'Escreva uma mensagem para um amigo: diga que você está com fome e sede, proponha um lanche e divida quem pega o quê.',
  'model': 'I’m hungry and thirsty. Let’s get a snack! I’ll get the sandwiches. You get the drinks. Thanks!',
  'kw': ['hungry', 'thirsty', 'snack', 'drinks'],
  'checks': ['Disse I’m hungry ou I’m thirsty.', 'Propus com Let’s get…', 'Dividi tarefas com I’ll get… e You get…']},
 scenes={'pool': ['market', 'supermarket', 'street', 'cafe2', 'bakery'], 'npc': {'g': 'm', 'role': 'friend'}, 'you': {'g': 'f'}},
 convo={'npc': {'name': 'Cole'}, 'story': 'Você e seu amigo Cole estão com fome e sede no mercado. Decidam juntos.', 'turns': [
  {'npc': 'I’m hungry. Are you hungry?', 'pt': 'Estou com fome. Você está com fome?', 'opts': [
   {'en': 'I have hungry too.', 'pt': 'Eu tenho fome também.', 'ok': False, 'fb': 'Em inglês: I’m hungry, com am.'},
   {'en': 'Yes, very! And I’m thirsty.', 'pt': 'Sim, muito! E estou com sede.', 'ok': True, 'fb': 'Responde e acrescenta a sede.'},
   {'en': 'No, I’m fine, thanks. Bye!', 'pt': 'Não, estou bem, obrigado. Tchau!', 'ok': False, 'fb': 'É uma resposta possível, mas encerra a conversa cedo demais.'}]},
  {'npc': 'Let’s get a snack.', 'pt': 'Vamos pegar um lanche.', 'opts': [
   {'en': 'Do you want a sandwich?', 'pt': 'Você quer um sanduíche?', 'ok': True, 'fb': 'Continua a ideia dele.'},
   {'en': 'I’m a snack.', 'pt': 'Eu sou um lanche.', 'ok': False, 'fb': 'Não faz sentido nesta frase.'},
   {'en': 'You are welcome.', 'pt': 'De nada.', 'ok': False, 'fb': 'Ninguém agradeceu.'}]},
  {'npc': 'Yes, and a juice, please.', 'pt': 'Sim, e um suco, por favor.', 'opts': [
   {'en': 'Perfect team!', 'pt': 'Time perfeito!', 'ok': False, 'fb': 'Ainda falta dividir quem pega o quê.'},
   {'en': 'Yes, very hungry.', 'pt': 'Sim, muita fome.', 'ok': False, 'fb': 'Não responde ao pedido do suco.'},
   {'en': 'I’ll get the sandwiches.', 'pt': 'Eu pego os sanduíches.', 'ok': True, 'fb': 'Decide e divide a tarefa.'}]},
  {'npc': 'Thanks! I’ll get the drinks.', 'pt': 'Valeu! Eu pego as bebidas.', 'opts': [
   {'en': 'I’ll get the drinks too.', 'pt': 'Eu também pego as bebidas.', 'ok': False, 'fb': 'Cole já vai pegar as bebidas; dividam as tarefas.'},
   {'en': 'Perfect team!', 'pt': 'Time perfeito!', 'ok': True, 'fb': 'Comenta o plano com bom humor.'},
   {'en': 'Are you thirsty?', 'pt': 'Você está com sede?', 'ok': False, 'fb': 'Isso já foi resolvido.'}]},
  {'npc': 'Here’s your sandwich. Enjoy!', 'pt': 'Aqui está seu sanduíche. Bom apetite!', 'opts': [
   {'en': 'Thanks! You too.', 'pt': 'Valeu! Você também.', 'ok': True, 'fb': 'Agradece e retribui.'},
   {'en': 'Let’s get a snack.', 'pt': 'Vamos pegar um lanche.', 'ok': False, 'fb': 'O lanche já está na mesa.'},
   {'en': 'I’m hungry.', 'pt': 'Estou com fome.', 'ok': False, 'fb': 'Agora você vai comer; é hora de agradecer.'}]}]},
)
