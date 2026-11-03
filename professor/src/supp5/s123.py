"""Suplemento Quest v5 · aula 123: I don't feel well + regular How Do You Feel Today? (Mr. Men)."""
SUPP = {
 'reg': 87,
 'badge': {'icon': '🤒', 'name': 'Feel Better', 'desc': 'Say how you feel and ask a friend for help'},
 'culture': {
  'hook': 'In the USA, when you do not feel well, people ask “Are you OK?” and offer water, rest or medicine. A simple sentence helps others understand you fast.',
  'mythfact': [
   {'s': 'In English, you say “I have a headache” for a head pain.', 'ans': True, 'why': 'Have + headache is the normal way.'},
   {'s': 'A fever is when your body is very cold.', 'ans': False, 'why': 'A fever means your body is hotter than normal.'},
   {'s': 'In the USA, many people take a sick day when they feel bad.', 'ans': True, 'why': 'Many jobs let you stay home when you are sick, but the rules vary.'},
   {'s': 'Water and rest are common first ideas when someone feels bad.', 'ans': True, 'why': 'People often say “Drink water and get some rest.”'},
   {'s': 'The Mr. Men books are about people with feelings and traits.', 'ans': True, 'why': 'Each character, like Mr. Happy or Mr. Grumpy, has one main trait.'}],
  'wild': [
   {'kind': 'Medicine label', 'lines': ['**Pain relief**', 'Adults: 1 tablet every 6 hours.', 'Do not take more than 4 a day.'], 'decode': {'q': 'How often can an adult take 1 tablet?', 'opts': ['Every 6 hours', 'Every hour', 'Once a week'], 'ans': 0, 'why': 'The label says every 6 hours.'}},
   {'kind': 'Text message', 'lines': ['I don’t feel well today.', 'I have a **headache** and I feel hot.', 'I’ll stay home and **rest**.'], 'decode': {'q': 'What will the writer do?', 'opts': ['Stay home and rest', 'Go to work', 'Go to a party'], 'ans': 0, 'why': 'The writer says: I’ll stay home and rest.'}}],
  'compare': {'br': 'In Brazil, many people say “Estou com dor de cabeça” and take a chá or a remédio at home. A friend may say “Melhoras!”.', 'us': 'In the USA, you say “I have a headache” and people may offer water, rest or medicine. “Feel better!” is the usual wish.', 'tip': 'Say what hurts first, and then what you need: “I have a headache. I need some water.”', 'ask': 'How do you say that you have a headache? Say it in English.'},
  'quiz': [
   {'q': 'Your head hurts. You say…', 'opts': ['I have a headache.', 'I am headache.', 'I do headache.'], 'ans': 0, 'why': 'Use have with pain words like headache.'},
   {'q': 'A friend asks, “Do you have a fever?” You are not hot. You say…', 'opts': ['No, I don’t.', 'No, I am not.', 'Yes, I have not.'], 'ans': 0, 'why': 'Do you have…? is answered with No, I don’t.'},
   {'q': 'What do you say to someone who feels sick?', 'opts': ['Feel better!', 'Have a good job!', 'Come here!'], 'ans': 0, 'why': 'Feel better! is the friendly wish.'}]},
 'reading': {
  'genre': 'Diary',
  'title': 'A bad day in Dallas',
  'text': [
   'Today I do **not feel well**. I woke up at seven, and my head was heavy. I have a **headache**, and I feel very **tired**. It is a hard morning in **Dallas**.',
   'I went to my friend Claire’s house because it was near. She opened the door and said, “Hi, Nell. You look tired. **Are you OK?**” I said, “No, I don’t feel well. I have a headache.”',
   'Claire asked, “**Do you have a fever?**” I said, “No, but I **feel hot**.” She put a hand on my head. “You feel a little warm,” she said. “**Do you want some water?**” I said, “Yes, please. And a **rest**.”',
   'She said, “**Lie down on the sofa.**” She put a soft blanket on me. I said, “Thanks. I’ll **take a nap**.” The room was quiet and cool.',
   'After one hour, I felt better. Claire asked, “**Do you need medicine?**” I looked at my bag. I had no pills, so she gave me one from the kitchen. She also made tea with honey.',
   'Now it is the afternoon. I am still a little tired, but my head is OK. Claire is a good friend. Tomorrow I am going to drink more water and **get some rest**.'],
  'glossary': [{'w': 'headache', 'pt': 'dor de cabeça'}, {'w': 'tired', 'pt': 'cansado'}, {'w': 'fever', 'pt': 'febre'}, {'w': 'warm', 'pt': 'quente (morno)'}, {'w': 'rest', 'pt': 'descanso'}, {'w': 'sofa', 'pt': 'sofá'}, {'w': 'blanket', 'pt': 'cobertor'}, {'w': 'nap', 'pt': 'soneca'}, {'w': 'medicine', 'pt': 'remédio'}, {'w': 'pills', 'pt': 'comprimidos'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A friend with a headache', 'A birthday party', 'A trip to Dallas'], 'ans': 0, 'why': 'Nell does not feel well and Claire helps her.'},
  'scan': [{'q': 'What does Nell have?', 'ans': 'headache', 'alt': ['a headache']}, {'q': 'Where does Nell lie down?', 'ans': 'sofa', 'alt': ['on the sofa', 'the sofa']}, {'q': 'What does Claire make?', 'ans': 'tea', 'alt': ['tea with honey']}],
  'tf': [
   {'s': 'Nell goes to Claire’s house.', 'ans': True, 'why': 'She went to Claire’s house because it was near.'},
   {'s': 'Nell has a high fever.', 'ans': False, 'why': 'She says no, but she feels hot.'},
   {'s': 'Nell takes a nap.', 'ans': True, 'why': 'She says, “I’ll take a nap.”'},
   {'s': 'Nell feels worse after one hour.', 'ans': False, 'why': 'After one hour, she felt better.'}],
  'order': ['Nell wakes up with a headache.', 'She goes to Claire’s house.', 'Claire asks about a fever and offers water.', 'Nell lies down on the sofa.', 'Nell feels better after an hour.'],
  'ctx': [
   {'sent': 'My head was heavy.', 'w': 'heavy', 'opts': ['hard to hold up', 'very small', 'very funny'], 'ans': 0, 'why': 'Heavy = not light.'},
   {'sent': 'You feel a little warm.', 'w': 'warm', 'opts': ['a bit hot', 'very cold', 'wet'], 'ans': 0, 'why': 'Warm = a bit hot.'},
   {'sent': 'She put a soft blanket on me.', 'w': 'blanket', 'opts': ['a cover for the body', 'a bag', 'a cup'], 'ans': 0, 'why': 'A blanket keeps you warm in bed.'}],
  'chunkHunt': ['I don’t feel well.', 'Do you have a fever?', 'Do you want some water?', 'Lie down on the sofa.'],
  'think': 'What do you do when you have a headache? Write two sentences.'},
 'convo': {'npc': {'name': 'Claire'}, 'story': 'You are at your friend Claire’s house in Dallas. You do not feel well.', 'turns': [
  {'npc': 'Hi! You look tired. Are you OK?', 'pt': 'Oi! Você parece cansado. Está bem?', 'opts': [
   {'en': 'No, I don’t feel well. I have a headache.', 'pt': 'Não, não me sinto bem. Estou com dor de cabeça.', 'ok': True, 'fb': 'Say how you feel and what hurts.'},
   {'en': 'I am headache.', 'pt': 'Eu sou dor de cabeça.', 'ok': False, 'fb': 'Use I have a headache.'},
   {'en': 'Yes, I look.', 'pt': 'Sim, eu pareço.', 'ok': False, 'fb': 'Answer the question: Are you OK?'}]},
  {'npc': 'Oh no. Do you have a fever?', 'pt': 'Ah, não. Você está com febre?', 'opts': [
   {'en': 'No, I am not fever.', 'pt': 'Não, eu não sou febre.', 'ok': False, 'fb': 'Use have: I don’t have a fever.'},
   {'en': 'Yes, I do. Thanks.', 'pt': 'Sim, eu tenho. Obrigado.', 'ok': False, 'fb': 'It does not match the story: no fever.'},
   {'en': 'No, but I feel hot.', 'pt': 'Não, mas sinto calor.', 'ok': True, 'fb': 'Answer and add the feeling.'}]},
  {'npc': 'Do you want some water?', 'pt': 'Quer um pouco de água?', 'opts': [
   {'en': 'Yes, please. And a rest.', 'pt': 'Quero, por favor. E um descanso.', 'ok': True, 'fb': 'Accept with please.'},
   {'en': 'Yes, I want.', 'pt': 'Sim, eu quero.', 'ok': False, 'fb': 'Sounds incomplete. Add please.'},
   {'en': 'I don’t feel water.', 'pt': 'Eu não sinto água.', 'ok': False, 'fb': 'Not natural English.'}]},
  {'npc': 'Lie down on the sofa.', 'pt': 'Deite no sofá.', 'opts': [
   {'en': 'The sofa is long.', 'pt': 'O sofá é comprido.', 'ok': False, 'fb': 'It does not answer the offer.'},
   {'en': 'I lie to you.', 'pt': 'Eu minto para você.', 'ok': False, 'fb': 'Lie down is different from lie to.'},
   {'en': 'Thanks. I’ll take a nap.', 'pt': 'Valeu. Vou tirar uma soneca.', 'ok': True, 'fb': 'Thank her and say your plan.'}]},
  {'npc': 'Do you need medicine?', 'pt': 'Precisa de remédio?', 'opts': [
   {'en': 'Yes, a little. Thank you, Claire.', 'pt': 'Sim, um pouco. Obrigado, Claire.', 'ok': True, 'fb': 'Answer, then thank your friend.'},
   {'en': 'I am medicine.', 'pt': 'Eu sou remédio.', 'ok': False, 'fb': 'Wrong verb: need.'},
   {'en': 'Good morning!', 'pt': 'Bom dia!', 'ok': False, 'fb': 'It does not answer the question.'}]}]},
 'homework': 'Say 3 sentences: how you feel today, what hurts and what you need. Record them and send them to your teacher.',
 'homework_items': ['Say: I don’t feel well. I have a headache.', 'Write 3 sentences with I have a… (headache, fever, cough).', 'Listen to the dialogue and repeat each line.', 'Review: Are you OK? / Do you want some water? / Get some rest.'],
 'errors': [
  {'wrong': 'I am headache.', 'fix': 'I have a headache.', 'alt': 'I have headache a.', 'why': 'For pain, use have a headache, not am.'},
  {'wrong': 'I no feel well.', 'fix': 'I don’t feel well.', 'alt': 'I not feel well.', 'why': 'To make a negative, use don’t before the verb.'},
  {'wrong': 'Do you have fever?', 'fix': 'Do you have a fever?', 'alt': 'Are you have a fever?', 'why': 'Use a before fever, and Do you have…? for the question.'},
  {'wrong': 'I will to take a nap.', 'fix': 'I’ll take a nap.', 'alt': 'I will taking a nap.', 'why': 'After will, use the base verb with no to.'}],
}
