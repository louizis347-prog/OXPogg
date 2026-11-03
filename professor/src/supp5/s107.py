"""Suplemento Quest v5 · aula 107: Lunch with coworkers + regular What's for breakfast?"""
SUPP = {'reg': 113, 'badge': {'icon': '🥪', 'name': 'Lunch Buddy', 'desc': 'Accept an invitation and order lunch with coworkers in English'},
 'culture': {'hook': 'Lunch with coworkers is a great way to make friends at a new job. Learn how to say yes, ask what is good and order a sandwich like a local.',
  'mythfact': [
   {'s': 'Coworkers often invite a new person to lunch.', 'ans': True, 'why': 'It is a friendly way to welcome someone to the team.'},
   {'s': 'The new person must pay for everyone.', 'ans': False, 'why': 'In many groups each person pays for their own food.'},
   {'s': 'Many people bring lunch from home.', 'ans': True, 'why': 'A homemade lunch in a bag or box is common.'},
   {'s': 'Lunch at work is always two hours long.', 'ans': False, 'why': 'It is often 30 to 60 minutes.'}],
  'wild': [
   {'kind': 'Deli menu board', 'lines': ['**Turkey sandwich**  $9', '**Tuna sandwich**  $8', '**Side salad**  +$3'], 'decode': {'q': 'How much is a turkey sandwich with a side salad?', 'opts': ['$12', '$11', '$9'], 'ans': 0, 'why': '$9 + $3 = $12.'}},
   {'kind': 'Message from a coworker', 'lines': ['Hi Alex! Lunch at 12:30?', 'We meet in the lobby.', 'The deli is on the corner. – Cole'], 'decode': {'q': 'Where do they meet?', 'opts': ['In the lobby', 'At the deli', 'At the park'], 'ans': 0, 'why': '“We meet in the lobby.”'}}],
  'compare': {'br': 'In Brazil many people have a long lunch, often a hot meal, and sometimes the company gives a meal ticket.', 'us': 'In the USA lunch is often shorter and lighter, like a sandwich or a salad, and many people eat with coworkers or at their desk.', 'tip': 'Say yes with “I’d love to!” and ask “What’s good there?” It shows interest.', 'ask': 'What do you eat for lunch at work? Say it in English.'},
  'quiz': [
   {'q': 'A coworker says, “Do you want to have lunch with us?” You say…', 'opts': ['Yes, I’d love to!', 'Yes, I have lunch.', 'No, I am lunch.'], 'ans': 0, 'why': 'I’d love to! is a warm yes.'},
   {'q': 'You want to know the best food at the deli. You ask…', 'opts': ['What’s good there?', 'What is the deli?', 'Where are you good?'], 'ans': 0, 'why': 'What’s good there? asks for a tip.'},
   {'q': 'To order your sandwich you say…', 'opts': ['I’ll have a turkey sandwich.', 'I am a turkey sandwich.', 'Turkey sandwich me.'], 'ans': 0, 'why': 'I’ll have + food is a natural order.'}]},
 'reading': {'genre': 'Diary', 'title': 'Lunch with the Team',
  'text': ['It is twelve o’clock at the office. Alex is new, and he is a little shy. His coworker Cole comes to his desk. “**Do you want to have lunch with us?**” Cole asks.',
   '“**Yes, I’d love to!**” Alex says. “**Where are we going?**” “To the **deli** on the corner,” Cole says. He looks at the clock. “**Let’s go before it’s crowded.**” Two more coworkers come, and they all walk outside.',
   'The deli is small and warm. Alex looks at the menu. “**What’s good there?**” he asks. “**The sandwiches are great**,” Cole says. There is tuna, ham and turkey. “**I’ll have a turkey sandwich**,” Alex says. “**Me too**,” says Cole. “And a salad.”',
   'Soon the deli is full. The line reaches the door. Alex puts some mustard on his sandwich. The coworkers talk about the weekend and laugh. Alex is not shy now. He feels part of the team.',
   'After lunch, Cole asks, “**Do you bring lunch from home?**” “Sometimes,” says Alex. “But today I like the deli.” Their break is almost over, so they walk back to the office in the sun.'],
  'glossary': [{'w': 'shy', 'pt': 'tímido'}, {'w': 'coworker', 'pt': 'colega de trabalho'}, {'w': 'deli', 'pt': 'delicatessen'}, {'w': 'crowded', 'pt': 'cheio de gente'}, {'w': 'menu', 'pt': 'cardápio'}, {'w': 'tuna', 'pt': 'atum'}, {'w': 'mustard', 'pt': 'mostarda'}, {'w': 'break', 'pt': 'intervalo'}, {'w': 'weekend', 'pt': 'fim de semana'}, {'w': 'laugh', 'pt': 'rir'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A new worker has lunch with coworkers', 'A cooking class', 'A birthday party'], 'ans': 0, 'why': 'Alex goes to lunch with his team.'},
  'scan': [{'q': 'Who invites Alex?', 'ans': 'Cole', 'alt': ['cole']}, {'q': 'Where do they go?', 'ans': 'the deli', 'alt': ['deli', 'to the deli']}, {'q': 'What does Alex order?', 'ans': 'a turkey sandwich', 'alt': ['turkey sandwich', 'turkey']}],
  'tf': [{'s': 'Alex is new at the office.', 'ans': True, 'why': 'He is new and shy.'}, {'s': 'The deli is far from the office.', 'ans': False, 'why': 'It is on the corner.'}, {'s': 'Cole orders a turkey sandwich too.', 'ans': True, 'why': '“Me too,” says Cole.'}, {'s': 'Alex always brings lunch from home.', 'ans': False, 'why': 'He says “Sometimes.”'}],
  'order': ['Cole invites Alex to lunch.', 'They walk to the deli.', 'Alex asks what is good.', 'They order sandwiches.', 'They walk back to the office.'],
  'ctx': [{'sent': 'Alex is new, and he is a little shy.', 'w': 'shy', 'opts': ['not very open with new people', 'very hungry', 'very tall'], 'ans': 0, 'why': 'Shy = quiet with people you do not know.'}, {'sent': 'Let’s go before it’s crowded.', 'w': 'crowded', 'opts': ['full of people', 'very cold', 'closed'], 'ans': 0, 'why': 'Crowded = many people.'}, {'sent': 'Their break is almost over.', 'w': 'break', 'opts': ['a rest from work', 'a broken plate', 'a long trip'], 'ans': 0, 'why': 'A break is a short rest.'}],
  'chunkHunt': ['Do you want to have lunch with us?', 'I’d love to!', 'What’s good there?', 'I’ll have a turkey sandwich.'], 'think': 'Who do you eat lunch with? Where do you go?'},
 'convo': {'npc': {'name': 'Cole'}, 'story': 'You are new at an office. Your coworker Cole invites you to lunch at the deli.', 'turns': [
  {'npc': 'Hi! Do you want to have lunch with us?', 'pt': 'Oi! Quer almoçar com a gente?', 'opts': [
   {'en': 'No, I am lunch.', 'pt': 'Não, eu sou almoço.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'Yes, I’d love to! Where are we going?', 'pt': 'Quero sim! Aonde vamos?', 'ok': True, 'fb': 'A warm yes plus a question.'},
   {'en': 'I have lunch yesterday.', 'pt': 'Eu tenho almoço ontem.', 'ok': False, 'fb': 'Wrong tense and not an answer.'}]},
  {'npc': 'To the deli on the corner.', 'pt': 'À delicatessen da esquina.', 'opts': [
   {'en': 'Great. What’s good there?', 'pt': 'Ótimo. O que é bom lá?', 'ok': True, 'fb': 'Ask for a tip about the food.'},
   {'en': 'Great. Where is you?', 'pt': 'Ótimo. Onde é você?', 'ok': False, 'fb': 'Wrong grammar: Where are you?'},
   {'en': 'The corner is a deli.', 'pt': 'A esquina é uma delicatessen.', 'ok': False, 'fb': 'It does not continue the talk.'}]},
  {'npc': 'The sandwiches are great.', 'pt': 'Os sanduíches são ótimos.', 'opts': [
   {'en': 'I have a turkey sandwich.', 'pt': 'Eu tenho um sanduíche de peru.', 'ok': False, 'fb': 'To order, say I’ll have…'},
   {'en': 'I’ll have a turkey sandwich.', 'pt': 'Vou querer um sanduíche de peru.', 'ok': True, 'fb': 'I’ll have + food = order.'},
   {'en': 'You are great sandwiches.', 'pt': 'Você é sanduíches ótimos.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Me too. And a salad.', 'pt': 'Eu também. E uma salada.', 'opts': [
   {'en': 'Let’s go before it’s crowded.', 'pt': 'Vamos antes de ficar cheio.', 'ok': True, 'fb': 'Natural idea at lunch time.'},
   {'en': 'Let’s to go crowded.', 'pt': 'Vamos para ir cheio.', 'ok': False, 'fb': 'Let’s + verb, no to.'},
   {'en': 'I am the corner.', 'pt': 'Eu sou a esquina.', 'ok': False, 'fb': 'Does not make sense.'}]},
  {'npc': 'Do you bring lunch from home?', 'pt': 'Você traz almoço de casa?', 'opts': [
   {'en': 'Sometimes, but today I like the deli.', 'pt': 'Às vezes, mas hoje gosto da delicatessen.', 'ok': True, 'fb': 'A real answer with a reason.'},
   {'en': 'Yes, I bring home.', 'pt': 'Sim, eu trago casa.', 'ok': False, 'fb': 'You bring lunch from home.'},
   {'en': 'The lunch is from me.', 'pt': 'O almoço é de mim.', 'ok': False, 'fb': 'Unnatural.'}]}]},
 'homework': 'Invite a friend to lunch in English: “Do you want to have lunch with me?” Say what you will have.',
 'homework_items': ['Write 3 sentences: where you eat lunch and what you have.', 'Say: I’d love to! / What’s good there? aloud 5 times.', 'Listen to the dialogue and shadow Cole.', 'Review: I’ll have… / Me too. / Let’s go before it’s crowded.'],
 'errors': [
  {'wrong': 'I will to have a sandwich.', 'fix': 'I’ll have a sandwich.', 'alt': 'I will having a sandwich.', 'why': 'After will, use the base verb: have.'},
  {'wrong': 'Do you want have lunch?', 'fix': 'Do you want to have lunch?', 'alt': 'Do you wanting have lunch?', 'why': 'want + to + verb.'},
  {'wrong': 'What is good in there?', 'fix': 'What’s good there?', 'alt': 'What good there?', 'why': 'What’s good there? is the short natural question.'},
  {'wrong': 'Me too, and also a salad.', 'fix': 'Me too. And a salad.', 'alt': 'Me too, and a salad also.', 'why': 'Keep it short: Me too. And a…'}]}
