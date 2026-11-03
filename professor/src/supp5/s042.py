"""Suplemento Quest v5 · aula 42: Dinner at my place + regular A table for two (Beauty and the Beast)."""
SUPP = {
 'reg': 115,
 'badge': {'icon': '🍽️', 'name': 'Good Guest', 'desc': 'Accept an invitation and be a polite dinner guest'},
 'sticker': {'cat': 'Everyday culture', 'title': 'Dinner at an American Home', 'sub': 'Make yourself at home'},
 'culture': {
  'hook': 'When an American friend invites you for dinner, the evening is relaxed and friendly. Knowing a few small habits helps you feel comfortable at the table.',
  'polite': 'Say **“Thanks for having me over!”** at the door or when you leave. Hosts love to hear it.',
  'mythfact': [
   {'s': 'A guest often brings a small gift, like dessert or flowers.', 'ans': True, 'why': 'It is common and polite, but it is not a strict rule.'},
   {'s': 'You should arrive two hours early.', 'ans': False, 'why': 'Arrive on time or a few minutes after. Too early can bother the host.'},
   {'s': '“Help yourself” means you can take food on your own.', 'ans': True, 'why': 'The host invites you to serve yourself.'},
   {'s': 'Americans never say thank you after a dinner.', 'ans': False, 'why': 'A thank-you text or note the next day is very common.'}],
  'wild': [
   {'kind': 'Text invitation', 'lines': ['Hi! Dinner at my place on Friday?', 'We eat at 7. Please reply by Wednesday.', 'Just bring yourself!'], 'decode': {'q': 'When is dinner?', 'opts': ['Friday at 7', 'Wednesday at 7', 'Friday at 9'], 'ans': 0, 'why': 'Dinner is Friday at 7. Wednesday is the reply day.'}},
   {'kind': 'Thank-you text', 'lines': ['Thanks for having me over!', 'The pasta was delicious.', 'Let\'s do it again soon!'], 'decode': {'q': 'What did the guest like?', 'opts': ['The pasta', 'The music', 'The movie'], 'ans': 0, 'why': '“The pasta was delicious.”'}}],
  'compare': {'br': 'In Brazil a dinner invitation can start later, and the host often insists that you eat more.', 'us': 'In the USA dinner often starts on time, and the host usually says “Help yourself” and lets you decide how much to eat.', 'tip': 'It is fine to say “No, thanks, I’m full.” It is not rude if you are polite.', 'ask': 'What would you bring to a dinner at a friend’s home? Say it in English.'},
  'quiz': [
   {'q': 'A friend says “Dinner at my place?” You want to accept. You say…', 'opts': ['I’d love to! When?', 'I am dinner.', 'No, thanks, I eat.'], 'ans': 0, 'why': 'I’d love to! is a warm yes.'},
   {'q': 'The host says “Make yourself at home.” It means…', 'opts': ['Feel comfortable', 'Go to your house', 'Clean the kitchen'], 'ans': 0, 'why': 'It means relax and feel welcome.'},
   {'q': 'What can you ask before the dinner?', 'opts': ['What should I bring?', 'Where is my money?', 'Who is you?'], 'ans': 0, 'why': 'What should I bring? is polite.'}]},
 'reading': {
  'genre': 'Diary entry', 'title': 'Friday dinner with Jordan',
  'text': [
   'Today Jordan invited me to dinner at his apartment in Minneapolis. I answered, “**I’d love to! When?**” He said, “**Friday at seven**.” I asked, “**What should I bring?**” He laughed and said, “**Just yourself**.”',
   'But I did not want to arrive with empty hands. I bought a small chocolate cake and a bunch of yellow flowers. At seven o’clock, I rang the bell. Jordan opened the door with a big smile.',
   'I said, “**Thanks for having me over!**” “**Make yourself at home**,” he said. The apartment was small, but it was warm and clean. A candle was on the table, and I could smell garlic and tomatoes.',
   'Jordan asked, “**Do you like pasta?**” “**Yes, I love pasta!**” I answered. He put a big bowl on the table. “**Help yourself!**” he said. The sauce was simple, but I wanted more.',
   'After dinner, we ate the cake and talked about our families and our jobs. At ten o’clock I said, “**Thanks for coming**,” and Jordan laughed. “I should say that to you!” he said.',
   'On the way home, I sent a text: “Thank you so much. See you soon!” It was a lovely night.'],
  'glossary': [{'w': 'invited', 'pt': 'convidou'}, {'w': 'bring', 'pt': 'levar'}, {'w': 'empty', 'pt': 'vazias'}, {'w': 'flowers', 'pt': 'flores'}, {'w': 'rang the bell', 'pt': 'tocou a campainha'}, {'w': 'candle', 'pt': 'vela'}, {'w': 'garlic', 'pt': 'alho'}, {'w': 'bowl', 'pt': 'tigela'}, {'w': 'lovely', 'pt': 'adorável'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A dinner at a friend’s apartment', 'A job interview', 'A trip to the beach'], 'ans': 0, 'why': 'The writer goes to dinner at Jordan’s home.'},
  'scan': [{'q': 'What time is dinner?', 'ans': 'seven', 'alt': ['7', 'at seven', '7 pm']}, {'q': 'What does the writer bring?', 'ans': 'a cake and flowers', 'alt': ['cake', 'chocolate cake', 'flowers']}, {'q': 'What does Jordan cook?', 'ans': 'pasta', 'alt': ['spaghetti']}],
  'tf': [{'s': 'Jordan says “Just yourself.”', 'ans': True, 'why': 'He answers “What should I bring?” this way.'}, {'s': 'The writer arrives at midnight.', 'ans': False, 'why': 'He arrives at seven o’clock.'}, {'s': 'The writer likes pasta.', 'ans': True, 'why': '“Yes, I love pasta!”'}, {'s': 'The writer does not thank Jordan.', 'ans': False, 'why': 'He says thanks and sends a text.'}],
  'order': ['Jordan invites the writer.', 'The writer buys a cake and flowers.', 'The writer rings the bell at seven.', 'They eat pasta and then cake.', 'The writer sends a thank-you text.'],
  'ctx': [{'sent': 'I did not want to arrive with empty hands.', 'w': 'empty hands', 'opts': ['no gift', 'big hands', 'dirty hands'], 'ans': 0, 'why': 'Empty hands = with nothing to give.'}, {'sent': 'The apartment was small, but it was warm and clean.', 'w': 'warm', 'opts': ['friendly and cozy', 'very loud', 'very new'], 'ans': 0, 'why': 'Warm here means cozy and friendly.'}, {'sent': 'It was a lovely night.', 'w': 'lovely', 'opts': ['very nice', 'very dark', 'very short'], 'ans': 0, 'why': 'Lovely = very nice.'}],
  'chunkHunt': ['I’d love to!', 'What should I bring?', 'Thanks for having me over!', 'Make yourself at home.', 'Help yourself!'],
  'think': 'What do you bring when a friend invites you home? Why?'},
 'convo': {'npc': {'name': 'Jordan'}, 'story': 'Jordan lives in Minneapolis. He invites you to dinner. Accept and be a polite guest.', 'turns': [
  {'npc': 'Hi! Do you want to have dinner at my place?', 'pt': 'Oi! Quer jantar na minha casa?', 'opts': [
   {'en': 'Yes, I am dinner.', 'pt': 'Sim, eu sou jantar.', 'ok': False, 'fb': 'Wrong. Say I’d love to!'},
   {'en': 'I’d love to! When?', 'pt': 'Eu adoraria! Quando?', 'ok': True, 'fb': 'Warm yes plus a useful question.'},
   {'en': 'No, I don’t want a dinner.', 'pt': 'Não, não quero um jantar.', 'ok': False, 'fb': 'Sounds rude.'}]},
  {'npc': 'Friday at seven. Is that OK?', 'pt': 'Sexta às sete. Pode ser?', 'opts': [
   {'en': 'Perfect. What should I bring?', 'pt': 'Perfeito. O que devo levar?', 'ok': True, 'fb': 'Accept and offer to help.'},
   {'en': 'Seven is Friday.', 'pt': 'Sete é sexta.', 'ok': False, 'fb': 'Does not answer.'},
   {'en': 'I bring me.', 'pt': 'Eu levo eu.', 'ok': False, 'fb': 'Not natural English.'}]},
  {'npc': 'Just yourself. Do you like pasta?', 'pt': 'Só você mesmo. Você gosta de massa?', 'opts': [
   {'en': 'Pasta is a like.', 'pt': 'Massa é um gosto.', 'ok': False, 'fb': 'Use I love pasta.'},
   {'en': 'I am not pasta.', 'pt': 'Eu não sou massa.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'Yes, I love pasta!', 'pt': 'Sim, adoro massa!', 'ok': True, 'fb': 'Short and natural.'}]},
  {'npc': 'Great. I’ll cook for you.', 'pt': 'Ótimo. Vou cozinhar para você.', 'opts': [
   {'en': 'Thanks, Jordan! See you Friday.', 'pt': 'Valeu, Jordan! Até sexta.', 'ok': True, 'fb': 'Thank him and confirm the day.'},
   {'en': 'You cook is good.', 'pt': 'Você cozinha é bom.', 'ok': False, 'fb': 'Grammar error.'},
   {'en': 'Good morning!', 'pt': 'Bom dia!', 'ok': False, 'fb': 'Wrong greeting for this moment.'}]},
  {'npc': 'Thanks for coming!', 'pt': 'Obrigado por vir!', 'opts': [
   {'en': 'You are welcome to dinner.', 'pt': 'Você é bem-vindo ao jantar.', 'ok': False, 'fb': 'Not natural here.'},
   {'en': 'Thanks for having me over!', 'pt': 'Obrigado por me receber!', 'ok': True, 'fb': 'The perfect guest phrase.'},
   {'en': 'I have thanks.', 'pt': 'Eu tenho obrigado.', 'ok': False, 'fb': 'Say Thanks!'}]}]},
 'errors': [
  {'wrong': 'I love to dinner at your house.', 'fix': 'I’d love to have dinner at your house.', 'alt': 'I loving dinner at your house.', 'why': 'I’d love to + verb.'},
  {'wrong': 'What I should bring?', 'fix': 'What should I bring?', 'alt': 'What bring I?', 'why': 'In questions the helper (should) comes before I.'},
  {'wrong': 'I like very pasta.', 'fix': 'I like pasta very much.', 'alt': 'I very like pasta.', 'why': 'Very much goes after the object.'},
  {'wrong': 'Thanks for have me.', 'fix': 'Thanks for having me over.', 'alt': 'Thanks for to have me.', 'why': 'After for, use -ing.'}],
 'homework': 'Write a short thank-you text to a friend after a dinner, using “Thanks for having me over.”',
 'homework_items': ['Write 3 lines accepting an invitation.', 'Record: “I’d love to! When?”', 'List 3 things you can bring to a dinner.', 'Review: Make yourself at home / Help yourself.']}
