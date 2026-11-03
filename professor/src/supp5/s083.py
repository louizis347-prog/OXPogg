"""Suplemento Quest v5 · aula 83: My morning routine + regular Wake Up, Get Up (Sleeping Beauty)."""
SUPP = {
 'reg': 73,
 'badge': {'icon': '⏰', 'name': 'Early Bird', 'desc': 'Tell your morning routine in English'},
 'sticker': {'cat': 'Everyday culture', 'title': 'Morning Routines', 'sub': 'Coffee first!'},
 'culture': {
  'hook': 'Many Americans talk about their morning routine with friends and coworkers. It is an easy way to start a chat, and you can answer with simple steps and times.',
  'polite': 'To ask about a routine, say **What time do you get up?** Use **first**, **then** and **after that** to order your steps.',
  'mythfact': [
   {'s': 'Many people in the USA drink coffee in the morning.', 'ans': True, 'why': 'Coffee is a very common morning drink, but tea and juice are common too.'},
   {'s': 'Everybody gets up at the same time.', 'ans': False, 'why': 'People get up at different times for work or school.'},
   {'s': '“What time do you get up?” is a normal small-talk question.', 'ans': True, 'why': 'People often compare routines.'},
   {'s': '“I’m not a morning person” means you love mornings.', 'ans': False, 'why': 'It means mornings are hard for you.'},
   {'s': 'Toast and cereal are common breakfast foods.', 'ans': True, 'why': 'Many people eat them, but breakfast changes from home to home.'}],
  'wild': [
   {'kind': 'Phone alarm', 'lines': ['**Alarm 1**  6:30 AM', '**Alarm 2**  6:40 AM', '**Repeat**  Mon · Tue · Wed · Thu · Fri'], 'decode': {'q': 'When does the first alarm ring?', 'opts': ['6:30', '6:40', '7:30'], 'ans': 0, 'why': 'Alarm 1 is at 6:30 AM.'}},
   {'kind': 'Text message', 'lines': ['Running late! Can you start without me?', 'Sure. I get coffee first. See you at 8.'], 'decode': {'q': 'What does the friend do first?', 'opts': ['Gets coffee', 'Takes a shower', 'Goes home'], 'ans': 0, 'why': '“I get coffee first.”'}}],
  'compare': {'br': 'In Brazil many people have “pão com café” in the morning and some start work very early.', 'us': 'In the USA many people have coffee, toast or cereal at home, and some take a coffee to go.', 'tip': 'Use simple present for routines: I get up, I take a shower, I go to work.', 'ask': 'What is the first thing you do in the morning? Say it in English.'},
  'quiz': [
   {'q': 'You ask a friend about the morning. You say…', 'opts': ['What time do you get up?', 'What time you get up?', 'When is you up?'], 'ans': 0, 'why': 'Use What time do you…?'},
   {'q': 'Which sentence is a routine?', 'opts': ['I take a shower and brush my teeth.', 'I am taking a bus yesterday.', 'I will to shower.'], 'ans': 0, 'why': 'Routines use the simple present.'},
   {'q': '“I’m not a morning person.” What does it mean?', 'opts': ['I do not like mornings.', 'I wake up at five.', 'I am a person.'], 'ans': 0, 'why': 'It means mornings are hard for you.'}]},
 'reading': {
  'genre': 'Diary', 'title': 'Una’s morning in Boston',
  'text': [
   'Una lives in **Boston**. Her alarm rings at six thirty every morning. She says, “**Five more minutes**,” but then she gets up. Una is not a morning person, but she likes her routine.',
   'First, she takes a shower and **brushes her teeth**. Then she **gets dressed**. After that, she goes to the kitchen. Her friend Grace has coffee and toast. Una has tea and fruit. They talk about the day.',
   'Una thinks about a fairy tale she loves. “**Sleeping Beauty**” is a story by Charles Perrault from 1697. A princess sleeps for a hundred years. Una laughs: “I only sleep for eight hours, but I **wake up** slowly too!”',
   'At seven thirty, Una leaves home. She takes the bus to work. The sun is up, and the street is busy. A man says, “**Rise and shine!**” “Good morning!” Una says. Mornings are better with a smile.',
   'At work, Una has a meeting at nine. She feels ready. “**Coffee first**,” she says to her coworker. Then they start. It is a good day. Her morning routine helps her a lot.'],
  'glossary': [{'w': 'alarm', 'pt': 'despertador'}, {'w': 'brushes her teeth', 'pt': 'escova os dentes'}, {'w': 'gets dressed', 'pt': 'se veste'}, {'w': 'toast', 'pt': 'torrada'}, {'w': 'fruit', 'pt': 'frutas'}, {'w': 'wake up', 'pt': 'acordar'}, {'w': 'rise and shine', 'pt': 'acorde e brilhe'}, {'w': 'busy', 'pt': 'movimentada'}, {'w': 'meeting', 'pt': 'reunião'}],
  'fast': {'q': 'What is this text about?', 'opts': ['The morning routine of a woman in Boston', 'A day at the beach', 'Buying a lamp'], 'ans': 0, 'why': 'The text follows Una from the alarm to work.'},
  'scan': [{'q': 'What time does the alarm ring?', 'ans': 'six thirty', 'alt': ['6:30', '6.30', 'half past six']}, {'q': 'What does Una have for breakfast?', 'ans': 'tea and fruit', 'alt': ['tea', 'fruit']}, {'q': 'How does Una go to work?', 'ans': 'by bus', 'alt': ['bus', 'she takes the bus']}],
  'tf': [{'s': 'Una lives in Boston.', 'ans': True, 'why': 'The first line says so.'}, {'s': 'Una loves mornings.', 'ans': False, 'why': 'She is not a morning person.'}, {'s': 'Grace has coffee and toast.', 'ans': True, 'why': 'The text says Grace has coffee and toast.'}, {'s': 'Una has a meeting at six.', 'ans': False, 'why': 'The meeting is at nine.'}],
  'order': ['Una’s alarm rings.', 'She takes a shower and brushes her teeth.', 'She has tea and fruit.', 'She takes the bus to work.', 'She has a meeting at nine.'],
  'ctx': [{'sent': 'Una gets dressed after her shower.', 'w': 'gets dressed', 'opts': ['puts on clothes', 'takes off clothes', 'goes to bed'], 'ans': 0, 'why': 'Get dressed = put on clothes.'}, {'sent': 'The street is busy at seven thirty.', 'w': 'busy', 'opts': ['full of people and cars', 'very quiet', 'very dark'], 'ans': 0, 'why': 'Busy = a lot of activity.'}, {'sent': 'Wake up, it is time to go!', 'w': 'Wake up', 'opts': ['Stop sleeping', 'Go to sleep', 'Eat now'], 'ans': 0, 'why': 'Wake up = stop sleeping.'}],
  'chunkHunt': ['What time do you get up?', 'I take a shower and brush my teeth.', 'Then I have breakfast.', 'Coffee first.'],
  'think': 'Write your morning in four steps with First, Then, After that and Finally.'},
 'convo': {'npc': {'name': 'Grace'}, 'story': 'You talk to your friend Grace in Boston about your morning routine.',
  'turns': [
   {'npc': 'What time do you get up?', 'pt': 'A que horas você acorda?', 'opts': [
    {'en': 'I get up at six thirty.', 'pt': 'Acordo às seis e meia.', 'ok': True, 'fb': 'Use at + time.'},
    {'en': 'I am up in six thirty.', 'pt': 'Estou de pé em seis e meia.', 'ok': False, 'fb': 'Use at, not in.'},
    {'en': 'Six thirty is me.', 'pt': 'Seis e meia sou eu.', 'ok': False, 'fb': 'Wrong meaning.'}]},
   {'npc': 'That’s early! What do you do first?', 'pt': 'Cedo! O que você faz primeiro?', 'opts': [
    {'en': 'I do shower and teeth.', 'pt': 'Eu faço banho e dentes.', 'ok': False, 'fb': 'Use take a shower and brush my teeth.'},
    {'en': 'First is the morning.', 'pt': 'Primeiro é a manhã.', 'ok': False, 'fb': 'It does not answer.'},
    {'en': 'I take a shower and brush my teeth.', 'pt': 'Tomo banho e escovo os dentes.', 'ok': True, 'fb': 'Two steps with and.'}]},
   {'npc': 'Then I have breakfast.', 'pt': 'Depois tomo café da manhã.', 'opts': [
    {'en': 'What do you have?', 'pt': 'O que você come?', 'ok': True, 'fb': 'A natural follow-up question.'},
    {'en': 'What you have?', 'pt': 'O que você come?', 'ok': False, 'fb': 'Use do: What do you have?'},
    {'en': 'I am breakfast.', 'pt': 'Eu sou café da manhã.', 'ok': False, 'fb': 'Wrong meaning.'}]},
   {'npc': 'Coffee and toast. And you?', 'pt': 'Café e torrada. E você?', 'opts': [
    {'en': 'I have tea and fruit.', 'pt': 'Eu tomo chá e como frutas.', 'ok': True, 'fb': 'Answer with have + food.'},
    {'en': 'Me, tea and fruit I am.', 'pt': 'Eu, chá e frutas sou.', 'ok': False, 'fb': 'Word order.'},
    {'en': 'No, thanks.', 'pt': 'Não, valeu.', 'ok': False, 'fb': 'It does not answer.'}]},
   {'npc': 'Have a great day at work!', 'pt': 'Tenha um ótimo dia de trabalho!', 'opts': [
    {'en': 'I have a work.', 'pt': 'Eu tenho um trabalho.', 'ok': False, 'fb': 'It does not answer the wish.'},
    {'en': 'Good night!', 'pt': 'Boa noite!', 'ok': False, 'fb': 'It is morning.'},
    {'en': 'Thanks! You too!', 'pt': 'Valeu! Você também!', 'ok': True, 'fb': 'Natural answer.'}]}]},
 'errors': [
  {'wrong': 'I wake up in six thirty.', 'fix': 'I get up at six thirty.', 'alt': 'I get up on six thirty.', 'why': 'Use at with clock times.'},
  {'wrong': 'I take a bath my teeth.', 'fix': 'I brush my teeth.', 'alt': 'I wash my teeth.', 'why': 'The verb for teeth is brush.'},
  {'wrong': 'What time you get up?', 'fix': 'What time do you get up?', 'alt': 'What time are you get up?', 'why': 'Add do in the question.'},
  {'wrong': 'I make breakfast coffee.', 'fix': 'I have coffee for breakfast.', 'alt': 'I make coffee breakfast.', 'why': 'Use have for what you eat or drink.'}],
 'homework': 'Write 5 sentences about your morning with times and say them aloud.',
 'homework_items': ['Write 5 morning sentences with times.', 'Record your routine in 40 seconds.', 'Shadow the dialogue with Grace.', 'Review: get up / take a shower / have breakfast.']}
