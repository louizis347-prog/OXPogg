"""Suplemento Quest v5 · aula 172: The wrong order + regular Excuse me, pardon? (Notting Hill)."""
SUPP = {
 'reg': 213,
 'badge': {'icon': '🔁', 'name': 'Order Fixed', 'desc': 'Say politely that your food is wrong and ask to change it'},
 'culture': {
  'hook': 'When a restaurant gets your order wrong, people in the USA usually stay calm and polite. A short, kind sentence works better than a long complaint.',
  'mythfact': [
   {'s': 'In the USA, it is normal to tell the waiter if your food is wrong.', 'ans': True, 'why': 'Waiters usually want to know, and they often fix it quickly.'},
   {'s': 'You must eat the wrong food and say nothing.', 'ans': False, 'why': 'You can politely ask to change it.'},
   {'s': 'A waiter often says “My mistake” when the order is wrong.', 'ans': True, 'why': 'It is a short and polite way to say sorry.'},
   {'s': '“On the house” means you pay double.', 'ans': False, 'why': 'It means the restaurant gives it to you for free.'},
   {'s': '“Notting Hill” is a romantic comedy from 1999.', 'ans': True, 'why': 'It was directed by Roger Michell.'}],
  'wild': [
   {'kind': 'Note on a receipt', 'lines': ['Order #42', '**1 chicken plate**', '1 tomato soup', 'No onions, please'], 'decode': {'q': 'What is the customer’s main dish?', 'opts': ['Chicken', 'Fish', 'Pasta'], 'ans': 0, 'why': 'The receipt says “1 chicken plate.”'}},
   {'kind': 'Sign near the kitchen', 'lines': ['**Check your order before you leave.**', 'Problem? Tell your waiter.', 'We are happy to fix it.'], 'decode': {'q': 'What should you do if there is a problem?', 'opts': ['Tell your waiter', 'Leave quietly', 'Cook it yourself'], 'ans': 0, 'why': '“Problem? Tell your waiter.”'}}],
  'compare': {'br': 'In Brazil, many people call the waiter with a gesture or say “Moço!” or “Moça!” to ask for a change.', 'us': 'In the USA, waiters usually come to your table often. You can say “Excuse me” when they are near, and they fix a wrong dish without argument.', 'tip': 'Say: “Excuse me, I think there’s a mistake.”', 'ask': 'What do you say when your food is wrong? Say it in English.'},
  'quiz': [
   {'q': 'You get fish, but you ordered chicken. You say…', 'opts': ['I ordered chicken, not fish.', 'I order chicken no fish.', 'Chicken is my fish.'], 'ans': 0, 'why': 'Use the past: I ordered chicken.'},
   {'q': 'You want a new plate. You ask…', 'opts': ['Can you change it, please?', 'Can you changing it?', 'You change me it?'], 'ans': 0, 'why': 'Can you + verb: Can you change it?'},
   {'q': 'The soup is not hot. You say…', 'opts': ['My soup is cold.', 'My soup has cold.', 'I am cold soup.'], 'ans': 0, 'why': 'Use is + cold for the food.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Chicken, not fish',
  'text': [
   'Gil is at a restaurant in **Denver**. It is noon, and the room is busy. He is hungry, and he wants a nice lunch. The waiter, Jonah, brings a plate and a bowl of soup.',
   '“**Excuse me, I think there’s a mistake**,” Gil says. “**I’m sorry. What’s the problem?**” Jonah asks. “**I ordered chicken, not fish.**” “**Oh no, I’m so sorry.**”',
   '“**Can you change it, please?**” “**Of course. It’ll take ten minutes.**” “**That’s okay. Thank you.**” Then Gil touches the bowl. “**Also, my soup is cold.**” “**Let me heat it up for you**,” Jonah says, and he takes the plate and the soup to the kitchen.',
   'At the next table, a woman talks about the film “Notting Hill.” It is a romantic comedy from 1999. A bookshop owner meets a famous actress. The restaurant is loud, so Gil says, “**Pardon?**” The woman smiles and says it again.',
   'Ten minutes later, Jonah comes back with hot chicken and hot soup. “**My mistake**,” he says. “The dessert is **on the house**.” “**I appreciate it**,” Gil says. Now he is happy.'],
  'glossary': [{'w': 'mistake', 'pt': 'erro'}, {'w': 'waiter', 'pt': 'garçom'}, {'w': 'chicken', 'pt': 'frango'}, {'w': 'fish', 'pt': 'peixe'}, {'w': 'soup', 'pt': 'sopa'}, {'w': 'cold', 'pt': 'frio'}, {'w': 'heat', 'pt': 'esquentar'}, {'w': 'kitchen', 'pt': 'cozinha'}, {'w': 'loud', 'pt': 'barulhento'}, {'w': 'dessert', 'pt': 'sobremesa'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A man gets the wrong food and asks to change it', 'A man cooks fish at home', 'A woman buys a book'], 'ans': 0, 'why': 'Gil gets fish, but he ordered chicken.'},
  'scan': [{'q': 'What does Gil order?', 'ans': 'chicken', 'alt': ['a chicken plate', 'chicken plate']}, {'q': 'How long does it take to change the food?', 'ans': 'ten minutes', 'alt': ['10 minutes', 'ten']}, {'q': 'What is cold?', 'ans': 'the soup', 'alt': ['soup', 'his soup', 'Gil’s soup']}],
  'tf': [{'s': 'Gil gets fish.', 'ans': True, 'why': 'Jonah brings fish, but Gil wants chicken.'}, {'s': 'Gil is angry and shouts.', 'ans': False, 'why': 'Gil is polite and says, “Excuse me.”'}, {'s': 'Jonah takes the soup to the kitchen.', 'ans': True, 'why': 'He wants to heat it up.'}, {'s': 'The dessert is not free.', 'ans': False, 'why': '“On the house” means it is free.'}],
  'order': ['Jonah brings the wrong food.', 'Gil says there is a mistake.', 'Gil asks to change the plate.', 'Gil says the soup is cold.', 'Jonah gives free dessert.'],
  'ctx': [{'sent': 'I think there’s a mistake.', 'w': 'mistake', 'opts': ['something wrong', 'something tasty', 'something new'], 'ans': 0, 'why': 'A mistake is an error.'}, {'sent': 'The restaurant is loud.', 'w': 'loud', 'opts': ['with a lot of noise', 'with no people', 'with cold food'], 'ans': 0, 'why': 'Loud = a lot of noise.'}, {'sent': 'Let me heat it up.', 'w': 'heat', 'opts': ['make it warm', 'make it cold', 'make it small'], 'ans': 0, 'why': 'Heat up = make hot.'}],
  'chunkHunt': ['I think there’s a mistake.', 'I ordered chicken, not fish.', 'Can you change it, please?', 'My mistake.'],
  'think': 'What do you do when your food is wrong? Do you say something or stay quiet?'},
 'convo': {'npc': {'name': 'Jonah'}, 'story': 'You are a customer at a restaurant in Denver. Jonah is your waiter. Your food is wrong.', 'turns': [
  {'npc': 'Here is your plate. Enjoy!', 'pt': 'Aqui está o seu prato. Bom apetite!', 'opts': [
   {'en': 'Excuse me, I think there’s a mistake.', 'pt': 'Com licença, acho que há um erro.', 'ok': True, 'fb': 'Polite way to start a problem.'},
   {'en': 'Excuse me, I have a mistake.', 'pt': 'Com licença, eu tenho um erro.', 'ok': False, 'fb': 'The mistake is not yours: there’s a mistake.'},
   {'en': 'Thank you. Goodbye!', 'pt': 'Obrigado. Tchau!', 'ok': False, 'fb': 'It does not fit here.'}]},
  {'npc': 'I’m sorry. What’s the problem?', 'pt': 'Sinto muito. Qual é o problema?', 'opts': [
   {'en': 'I order chicken, no fish.', 'pt': 'Eu peço frango, não peixe.', 'ok': False, 'fb': 'Use the past: I ordered chicken, not fish.'},
   {'en': 'It is fine, thanks.', 'pt': 'Está bom, obrigado.', 'ok': False, 'fb': 'It does not say the problem.'},
   {'en': 'I ordered chicken, not fish.', 'pt': 'Pedi frango, não peixe.', 'ok': True, 'fb': 'Clear and in the past.'}]},
  {'npc': 'Oh no, I’m so sorry.', 'pt': 'Ai, não, sinto muito.', 'opts': [
   {'en': 'You are welcome.', 'pt': 'De nada.', 'ok': False, 'fb': 'Not a reply to sorry.'},
   {'en': 'Can you change it, please?', 'pt': 'Pode trocar, por favor?', 'ok': True, 'fb': 'Polite request.'},
   {'en': 'Can you changing it?', 'pt': 'Pode trocando isso?', 'ok': False, 'fb': 'After can, use the base verb: change.'}]},
  {'npc': 'Of course. It’ll take ten minutes.', 'pt': 'Claro. Vai levar dez minutos.', 'opts': [
   {'en': 'That’s okay. Thank you.', 'pt': 'Tudo bem. Obrigado.', 'ok': True, 'fb': 'Calm and polite.'},
   {'en': 'Yes, I take ten minutes.', 'pt': 'Sim, eu levo dez minutos.', 'ok': False, 'fb': 'The food takes the time, not you.'},
   {'en': 'Ten minutes is a mistake.', 'pt': 'Dez minutos é um erro.', 'ok': False, 'fb': 'Does not fit.'}]},
  {'npc': 'Anything else?', 'pt': 'Mais alguma coisa?', 'opts': [
   {'en': 'Also, my soup is cold.', 'pt': 'Também, minha sopa está fria.', 'ok': True, 'fb': 'Adds the second problem.'},
   {'en': 'Also, I am cold soup.', 'pt': 'Também, eu sou sopa fria.', 'ok': False, 'fb': 'The soup is cold, not you.'},
   {'en': 'No, I am sorry.', 'pt': 'Não, sinto muito.', 'ok': False, 'fb': 'You do not need to say sorry.'}]}]},
 'errors': [
  {'wrong': 'I asked chicken, not fish.', 'fix': 'I ordered chicken, not fish.', 'alt': 'I ordered a chicken no fish.', 'why': 'For food, use order in the past: ordered.'},
  {'wrong': 'My soup is with cold.', 'fix': 'My soup is cold.', 'alt': 'My soup has cold.', 'why': 'Use is + cold, with no with or has.'},
  {'wrong': 'Can you to change it?', 'fix': 'Can you change it?', 'alt': 'Can you changing it?', 'why': 'After can, use only the base verb.'},
  {'wrong': 'This is not what I order.', 'fix': 'This is not what I ordered.', 'alt': 'This not is what I ordered.', 'why': 'Use the past: ordered. And not goes after is.'}],
 'homework': 'Write a short dialogue: your pasta is cold and you ask the waiter to heat it up.',
 'homework_items': ['Write two things that can go wrong in a restaurant.', 'Say aloud: I think there’s a mistake.', 'Listen to the dialogue and shadow Jonah.', 'Review: chicken / fish / soup / cold.']}
