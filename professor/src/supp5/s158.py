"""Suplemento Quest v5 · aula 158: Yoga class + regular You should rest (Bear Feels Sick)."""
SUPP = {
 'reg': 158,
 'badge': {'icon': '🧘', 'name': 'Yoga Newbie', 'desc': 'Join a first class: mat, shoes and slow breathing'},
 'culture': {
  'hook': 'In the USA, yoga studios often welcome beginners. You can say, “It is my first time,” and the teacher will help you with the mat, the place and the first steps.',
  'mythfact': [
   {'s': 'Yoga comes from India.', 'ans': True, 'why': 'It has a very long history there and is now practiced all over the world.'},
   {'s': 'In many yoga classes, people practice barefoot.', 'ans': True, 'why': 'Many studios ask you to leave your shoes at the door.'},
   {'s': 'You must be very flexible before your first class.', 'ans': False, 'why': 'Beginners are welcome. Classes help you move a little at a time.'},
   {'s': 'People usually keep their phones on silent in class.', 'ans': True, 'why': 'The room is quiet, so a loud phone bothers everyone.'},
   {'s': '“Bear Feels Sick” is a picture book.', 'ans': True, 'why': 'Karma Wilson wrote it in 2007. A bear is ill, and his friends care for him.'}],
  'wild': [
   {'kind': 'Studio door sign', 'lines': ['**Please take off your shoes.**', 'Silence your phone.', 'Mats to rent: $2'], 'decode': {'q': 'What should you do at the door?', 'opts': ['Take off your shoes', 'Call a friend', 'Bring a pizza'], 'ans': 0, 'why': '“Please take off your shoes.”'}},
   {'kind': 'Class schedule', 'lines': ['**Beginner Yoga**', 'Monday and Wednesday, 6 p.m.', 'Bring a water bottle', 'First class is free'], 'decode': {'q': 'When is the beginner class?', 'opts': ['Monday and Wednesday at 6 p.m.', 'Every morning', 'Only on Sunday'], 'ans': 0, 'why': 'The schedule says Monday and Wednesday, 6 p.m.'}}],
  'compare': {'br': 'In Brazil, yoga is also popular, in studios, gyms and parks, and many places lend mats.', 'us': 'In the USA, many studios have a short chat for new students. Some lend or rent mats, and many ask for quiet.', 'tip': 'Say: “It’s my first time.”', 'ask': 'Do you prefer to exercise alone or in a class? Say it in English.'},
  'quiz': [
   {'q': 'You want to know where to put your mat. You ask…', 'opts': ['Where should I put it?', 'Where I should put it?', 'Where put I it?'], 'ans': 0, 'why': 'In a question, should comes before I.'},
   {'q': 'The teacher says, “We practice barefoot.” It means…', 'opts': ['no shoes', 'no water', 'no mat'], 'ans': 0, 'why': 'Barefoot = without shoes or socks.'},
   {'q': 'A friend says, “You should rest.” She is…', 'opts': ['giving advice', 'saying goodbye', 'asking the price'], 'ans': 0, 'why': 'Should is used to give advice.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'My first yoga class',
  'text': [
   'Ines goes to a yoga class in San Diego. It is her first time, and she is a little nervous. The studio is quiet, and the floor is warm. Five people are already on their mats.',
   '“**Welcome to class! Is this your first time?**” Victor asks. “**Yes, I’m a little nervous**,” Ines says. “**Don’t worry. Take a mat.**” “**Where should I put it?**” “**Anywhere you like.**”',
   '“**Do I need shoes?**” “**No, we practice barefoot.**” “**Okay. What do we do first?**” “**We start by breathing slowly.**” Ines closes her eyes and breathes in and out. The room is very quiet.',
   'Then Victor says, “Bend your legs. Stretch your arms.” Ines’s back hurts a little. “You should rest,” Victor says. “You shouldn’t push too hard.” Ines remembers a children’s book, “Bear Feels Sick.” In that book, a bear is ill, and his friends say, “You should rest.”',
   'At the end, Ines lies on her mat. She feels calm. “Same time next week?” Victor asks. “Yes,” she says. She smiles and drinks some water. Then everyone says goodbye. Ines feels strong and happy.'],
  'glossary': [{'w': 'studio', 'pt': 'estúdio'}, {'w': 'nervous', 'pt': 'nervosa'}, {'w': 'mat', 'pt': 'tapete'}, {'w': 'barefoot', 'pt': 'descalço'}, {'w': 'breathes', 'pt': 'respira'}, {'w': 'bend', 'pt': 'dobrar'}, {'w': 'back', 'pt': 'costas'}, {'w': 'rest', 'pt': 'descansar'}, {'w': 'push', 'pt': 'forçar, empurrar'}, {'w': 'calm', 'pt': 'calma'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A woman in her first yoga class', 'A man who buys shoes', 'A girl at a party'], 'ans': 0, 'why': 'Ines goes to a yoga class for the first time.'},
  'scan': [{'q': 'Where is the yoga class?', 'ans': 'in San Diego', 'alt': ['San Diego']}, {'q': 'What does Ines take?', 'ans': 'a mat', 'alt': ['mat']}, {'q': 'What do they do first?', 'ans': 'breathing slowly', 'alt': ['breathe slowly', 'breathing', 'they breathe slowly']}],
  'tf': [{'s': 'Ines needs shoes for the class.', 'ans': False, 'why': 'They practice barefoot.'}, {'s': 'Ines is a little nervous.', 'ans': True, 'why': '“Yes, I’m a little nervous.”'}, {'s': 'Victor says, “You should rest.”', 'ans': True, 'why': 'Ines’s back hurts a little.'}, {'s': 'It is Ines’s tenth class.', 'ans': False, 'why': 'It is her first time.'}],
  'order': ['Ines arrives at the studio.', 'Victor tells her to take a mat.', 'They start by breathing slowly.', 'Victor says, “You should rest.”', 'Ines feels calm at the end.'],
  'ctx': [{'sent': 'We practice barefoot.', 'w': 'barefoot', 'opts': ['without shoes', 'very fast', 'at night'], 'ans': 0, 'why': 'Bare + foot: no shoes on your feet.'}, {'sent': 'You shouldn’t push too hard.', 'w': 'push', 'opts': ['try too much', 'sit down', 'go home'], 'ans': 0, 'why': 'Here push = force your body too much.'}, {'sent': 'She feels calm.', 'w': 'calm', 'opts': ['quiet and relaxed', 'very hungry', 'angry'], 'ans': 0, 'why': 'Calm = peaceful, not nervous.'}],
  'chunkHunt': ['Is this your first time?', 'Where should I put it?', 'Do I need shoes?', 'We start by breathing slowly.'],
  'think': 'Do you want to try yoga? Why or why not?'},
 'convo': {'npc': {'name': 'Victor'}, 'story': 'You are at your first yoga class. Victor, the teacher, welcomes you.', 'turns': [
  {'npc': 'Welcome to class! Is this your first time?', 'pt': 'Bem-vinda à aula! É sua primeira vez?', 'opts': [
   {'en': 'Yes, I’m a little nervous.', 'pt': 'Sim, estou um pouco nervosa.', 'ok': True, 'fb': 'Honest and natural.'},
   {'en': 'Yes, I am nervous a little.', 'pt': 'Sim, estou nervosa um pouco.', 'ok': False, 'fb': 'Say a little nervous.'},
   {'en': 'No, thanks, I have shoes.', 'pt': 'Não, obrigada, eu tenho sapatos.', 'ok': False, 'fb': 'It does not answer the question.'}]},
  {'npc': 'Don’t worry. Take a mat.', 'pt': 'Não se preocupe. Pegue um tapete.', 'opts': [
   {'en': 'Where I should put it?', 'pt': 'Onde eu devo colocar?', 'ok': False, 'fb': 'Say: Where should I put it?'},
   {'en': 'Thanks. Where should I put it?', 'pt': 'Valeu. Onde devo colocar?', 'ok': True, 'fb': 'Thanks, then a clear question.'},
   {'en': 'I am a mat, thanks.', 'pt': 'Sou um tapete, obrigada.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Anywhere you like.', 'pt': 'Onde quiser.', 'opts': [
   {'en': 'Do I need shoes?', 'pt': 'Preciso de sapatos?', 'ok': True, 'fb': 'A useful next question.'},
   {'en': 'I need shoes?', 'pt': 'Eu preciso sapatos?', 'ok': False, 'fb': 'Use Do I need…?'},
   {'en': 'Yes, I like.', 'pt': 'Sim, eu gosto.', 'ok': False, 'fb': 'It does not fit.'}]},
  {'npc': 'No, we practice barefoot.', 'pt': 'Não, praticamos descalços.', 'opts': [
   {'en': 'What we do first?', 'pt': 'O que nós fazemos primeiro?', 'ok': False, 'fb': 'Say: What do we do first?'},
   {'en': 'Okay. What do we do first?', 'pt': 'Ok. O que fazemos primeiro?', 'ok': True, 'fb': 'Natural question order.'},
   {'en': 'Okay. We practice a mat.', 'pt': 'Ok. Praticamos um tapete.', 'ok': False, 'fb': 'Does not make sense.'}]},
  {'npc': 'We start by breathing slowly.', 'pt': 'Começamos respirando devagar.', 'opts': [
   {'en': 'That sounds good. I’m ready.', 'pt': 'Parece bom. Estou pronta.', 'ok': True, 'fb': 'Positive and clear.'},
   {'en': 'I am breath slowly.', 'pt': 'Eu sou respiração devagar.', 'ok': False, 'fb': 'Breath is a noun; the verb is breathe.'},
   {'en': 'Welcome to class!', 'pt': 'Bem-vindos à aula!', 'ok': False, 'fb': 'That is the teacher’s line.'}]}]},
 'errors': [
  {'wrong': 'I am nervous a little.', 'fix': 'I’m a little nervous.', 'alt': 'I am little nervous.', 'why': 'In English, a little comes before the adjective.'},
  {'wrong': 'Where I should put it?', 'fix': 'Where should I put it?', 'alt': 'Where should put I it?', 'why': 'In a question, should comes before I.'},
  {'wrong': 'I need shoes?', 'fix': 'Do I need shoes?', 'alt': 'Need I shoes?', 'why': 'Questions with need use do: Do I need…?'},
  {'wrong': 'What we do first?', 'fix': 'What do we do first?', 'alt': 'What we do it first?', 'why': 'Question words need do before we.'}],
 'homework': 'Write 4 questions for a first class: place, shoes, water and what to do first.',
 'homework_items': ['Say aloud: Where should I put it?', 'Write: Do I need…? with 3 things.', 'Listen to the dialogue and shadow Victor.', 'Review: should / shouldn’t for advice.']}
