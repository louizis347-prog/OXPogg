"""Suplemento Quest v5 · aula 197: Mini golf date + regular What's your hobby? (Ponyo)."""
SUPP = {
 'reg': 134,
 'badge': {'icon': '⛳', 'name': 'Mini Golf Star', 'desc': 'Pay, pick a color and learn the rules at a mini golf course'},
 'culture': {
  'hook': 'Mini golf is a popular cheap date in the USA. You pay at a small desk, pick your club and ball, and play 18 holes if you like, one by one.',
  'mythfact': [
   {'s': 'Many mini golf courses give you a club, a ball and a small card for points.', 'ans': True, 'why': 'This is common, but the details change from place to place.'},
   {'s': 'In mini golf, you must hit the ball very far.', 'ans': False, 'why': 'The holes are short. You hit the ball softly into the hole.'},
   {'s': 'At a mini golf desk, a tip is required.', 'ans': False, 'why': 'Tips are normal in restaurants, but at a desk “Keep the change” is only a choice.'},
   {'s': 'Many mini golf courses have 18 holes.', 'ans': True, 'why': 'Eighteen holes is a very common size, but some courses have fewer.'},
   {'s': '“Ponyo” is a film about a little goldfish.', 'ans': True, 'why': 'It is a 2008 film by Hayao Miyazaki.'}],
  'wild': [
   {'kind': 'Sign at the desk', 'lines': ['**MINI GOLF**', 'Adults $10 · Kids $7', 'Club and ball included'], 'decode': {'q': 'What does the price include?', 'opts': ['A club and a ball', 'Lunch', 'A prize'], 'ans': 0, 'why': 'It says “Club and ball included.”'}},
   {'kind': 'Rule on hole 1', 'lines': ['**Hit the ball into the hole.**', 'Six tries, then move on.', 'Please wait for the group ahead.'], 'decode': {'q': 'What should you do first?', 'opts': ['Hit the ball into the hole', 'Pay again', 'Take a photo'], 'ans': 0, 'why': 'The first rule says to hit the ball into the hole.'}}],
  'compare': {'br': 'In Brazil, many people say “Quanto é?” at the desk and often pay together without splitting.', 'us': 'In the USA, the price is “each,” so for two people you pay two times the price.', 'tip': 'Say: “Two for mini golf, please.”', 'ask': 'How do you ask for tickets for two people? Say it in English.'},
  'quiz': [
   {'q': 'You want tickets for two. You say…', 'opts': ['Two for mini golf, please.', 'I want two golf mini.', 'Two mini golf is.'], 'ans': 0, 'why': 'Say the number first: Two for mini golf, please.'},
   {'q': 'You want red. You say…', 'opts': ['I’ll take red.', 'I will to take red.', 'Red I am.'], 'ans': 0, 'why': 'I’ll take + color.'},
   {'q': 'You ask how the game works. You say…', 'opts': ['How does it work?', 'How it works?', 'How do it work?'], 'ans': 0, 'why': 'With it use does: How does it work?'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Hole in one',
  'text': [
   'Dan loves mini golf. It is his hobby, and it is a fun date. On Saturday he goes to the park with Mia. The course is small and green. It has a red bridge and a big blue fish. A young woman sits at the desk.',
   '“**Hi! Two for mini golf, please.**” “**That’s ten dollars each.**” Dan gives her a twenty. “**Here’s twenty. Keep the change.**” “**Thanks. Here are your clubs and balls.**”',
   '“**Which color do you want?**” “**I’ll take red. You take yellow.**” Mia looks at the club and asks, “**How does it work?**” “**Hit the ball into the hole**,” Dan says. “**How many tries?**” “Six on each hole,” the woman says. “Then you move on.”',
   'Mia’s first shot is too hard, and the ball goes into the grass. She laughs. Dan wins the first hole, and Mia wins the second. Her favorite film is “Ponyo.” It is about a little fish who wants to be a girl. Her yellow ball makes her think of Ponyo, and she smiles. After 18 holes, Mia is the winner. Her prize is a free ice cream, and Dan says, “Great game!”'],
  'glossary': [{'w': 'hobby', 'pt': 'passatempo'}, {'w': 'course', 'pt': 'campo, percurso'}, {'w': 'bridge', 'pt': 'ponte'}, {'w': 'desk', 'pt': 'balcão, mesa'}, {'w': 'each', 'pt': 'cada'}, {'w': 'change', 'pt': 'troco'}, {'w': 'club', 'pt': 'taco'}, {'w': 'hole', 'pt': 'buraco'}, {'w': 'tries', 'pt': 'tentativas'}, {'w': 'prize', 'pt': 'prêmio'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A date at a mini golf course', 'A trip to a zoo', 'A film class'], 'ans': 0, 'why': 'Dan and Mia play mini golf.'},
  'scan': [{'q': 'How much is it for each person?', 'ans': 'ten dollars', 'alt': ['$10', '10 dollars']}, {'q': 'What color does Mia take?', 'ans': 'yellow', 'alt': ['a yellow ball']}, {'q': 'What is the prize?', 'ans': 'a free ice cream', 'alt': ['ice cream', 'free ice cream']}],
  'tf': [{'s': 'Dan pays with twenty dollars.', 'ans': True, 'why': 'He says, “Here’s twenty.”'}, {'s': 'Dan takes yellow.', 'ans': False, 'why': 'Dan takes red, and Mia takes yellow.'}, {'s': 'Mia laughs after her first shot.', 'ans': True, 'why': 'The ball goes into the grass.'}, {'s': 'Dan is the winner after 18 holes.', 'ans': False, 'why': 'Mia is the winner.'}],
  'order': ['Dan and Mia pay at the desk.', 'They get clubs and balls.', 'Mia asks how it works.', 'Mia’s first shot is too hard.', 'Mia wins a free ice cream.'],
  'ctx': [{'sent': 'Keep the change.', 'w': 'change', 'opts': ['the extra money back', 'a new club', 'a big number'], 'ans': 0, 'why': 'Change is the money you get back.'}, {'sent': 'The course has a red bridge.', 'w': 'bridge', 'opts': ['a way over water', 'a kind of ball', 'a desk'], 'ans': 0, 'why': 'A bridge goes over something.'}, {'sent': 'Her prize is a free ice cream.', 'w': 'prize', 'opts': ['a gift for the winner', 'a kind of club', 'a short game'], 'ans': 0, 'why': 'A prize is a gift for winning.'}],
  'chunkHunt': ['Two for mini golf, please.', 'Keep the change.', 'Which color do you want?', 'How does it work?'],
  'think': 'What hobby do you like? Is it fun to do with another person?'},
 'convo': {'npc': {'name': 'Claire'}, 'story': 'You are at a mini golf course in a park. Claire works at the desk.', 'turns': [
  {'npc': 'Hi! How can I help you?', 'pt': 'Oi! Como posso ajudar?', 'opts': [
   {'en': 'Hi! Two for mini golf, please.', 'pt': 'Oi! Dois para mini golfe, por favor.', 'ok': True, 'fb': 'Clear and polite.'},
   {'en': 'I am two mini golf.', 'pt': 'Eu sou dois mini golfe.', 'ok': False, 'fb': 'Say what you want: Two for mini golf.'},
   {'en': 'Goodbye!', 'pt': 'Tchau!', 'ok': False, 'fb': 'It does not fit here.'}]},
  {'npc': 'That’s ten dollars each.', 'pt': 'São dez dólares cada.', 'opts': [
   {'en': 'Ten dollars is a hole.', 'pt': 'Dez dólares é um buraco.', 'ok': False, 'fb': 'It does not fit.'},
   {'en': 'Here’s twenty. Keep the change.', 'pt': 'Aqui estão vinte. Fique com o troco.', 'ok': True, 'fb': 'Two times ten is twenty.'},
   {'en': 'I pay you ten dollar.', 'pt': 'Eu pago você dez dólar.', 'ok': False, 'fb': 'Use: Here’s twenty. For two, you pay twenty.'}]},
  {'npc': 'Thanks. Which color do you want?', 'pt': 'Obrigada. Qual cor você quer?', 'opts': [
   {'en': 'I’ll take red. You take yellow.', 'pt': 'Eu fico com vermelha. Você fica com a amarela.', 'ok': False, 'fb': 'The desk worker does not play with you.'},
   {'en': 'The red, please.', 'pt': 'A vermelha, por favor.', 'ok': True, 'fb': 'Short and clear.'},
   {'en': 'I want colors of red.', 'pt': 'Eu quero cores de vermelho.', 'ok': False, 'fb': 'Say: The red, please.'}]},
  {'npc': 'Here are your clubs and balls. Have fun!', 'pt': 'Aqui estão tacos e bolas. Divirta-se!', 'opts': [
   {'en': 'How does it work?', 'pt': 'Como funciona?', 'ok': True, 'fb': 'Asks for the rules.'},
   {'en': 'How it work?', 'pt': 'Como funciona isso?', 'ok': False, 'fb': 'Use does: How does it work?'},
   {'en': 'It is ten minutes.', 'pt': 'São dez minutos.', 'ok': False, 'fb': 'Does not answer.'}]},
  {'npc': 'Hit the ball into the hole. Six tries each hole.', 'pt': 'Acerte a bola no buraco. Seis tentativas por buraco.', 'opts': [
   {'en': 'Great! Thank you!', 'pt': 'Ótimo! Obrigado!', 'ok': True, 'fb': 'Polite end of the talk.'},
   {'en': 'Hit you the ball.', 'pt': 'Acerte você a bola.', 'ok': False, 'fb': 'Word order is wrong, and it is not polite.'},
   {'en': 'Keep the change.', 'pt': 'Fique com o troco.', 'ok': False, 'fb': 'You already paid.'}]}]},
 'errors': [
  {'wrong': 'Two mini golf, please.', 'fix': 'Two for mini golf, please.', 'alt': 'I want two for mini golf.', 'why': 'Use for between the number and the activity.'},
  {'wrong': 'How it works?', 'fix': 'How does it work?', 'alt': 'How do it work?', 'why': 'In questions with it, use does + base verb.'},
  {'wrong': 'It is ten dollars for each one persons.', 'fix': 'It is ten dollars each.', 'alt': 'It is ten dollar each.', 'why': 'Say each after the price, and use dollars for more than one.'},
  {'wrong': 'Stay with the change.', 'fix': 'Keep the change.', 'alt': 'Keep the changes.', 'why': 'Use keep, and change is singular here.'}],
 'homework': 'Write a short dialogue at a mini golf desk: ask for two tickets, pay and choose a color.',
 'homework_items': ['Write three things you need to play mini golf.', 'Say aloud: Two for mini golf, please.', 'Listen to the dialogue and shadow Claire.', 'Review: hole / golf / club / prize.']}
