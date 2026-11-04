"""Suplemento Quest v5 · aula 159: Surprise party + regular Because and So (Bluey)."""
SUPP = {
 'reg': 42,
 'badge': {'icon': '🎉', 'name': 'Surprise Keeper', 'desc': 'Hide, stay quiet and shout Surprise!'},
 'culture': {
  'hook': 'In the USA, a surprise party is a fun birthday tradition. Friends arrive early, hide, turn off the lights and shout “Surprise!” when the guest of honor comes in.',
  'mythfact': [
   {'s': 'At a surprise party, the birthday person should not know about it.', 'ans': True, 'why': 'That is the idea. Friends keep it a secret until the big moment.'},
   {'s': 'In the USA, people usually sing “Happy Birthday to You.”', 'ans': True, 'why': 'It is the most common birthday song in English.'},
   {'s': 'Many people blow out the candles and make a wish.', 'ans': True, 'why': 'It is a common custom in many places, and friends say, “Make a wish!”'},
   {'s': 'Every guest must bring an expensive gift.', 'ans': False, 'why': 'A card or a small gift is fine. The party is about being together.'},
   {'s': '“Bluey” is a cartoon from Australia.', 'ans': True, 'why': 'It started in 2018 and is about a blue puppy and her family.'}],
  'wild': [
   {'kind': 'Party invitation', 'lines': ['**Surprise party for Mia!**', 'Saturday, 7 p.m. at Rosa’s house', 'Please arrive by 6:45', 'Shh! Keep it a secret.'], 'decode': {'q': 'When should guests arrive?', 'opts': ['By 6:45', 'At 8:00', 'After the party'], 'ans': 0, 'why': '“Please arrive by 6:45.”'}},
   {'kind': 'Birthday card', 'lines': ['**Happy Birthday, Mia!**', 'Make a wish and blow out the candles.', 'Love, Hugo'], 'decode': {'q': 'What does Hugo want Mia to do?', 'opts': ['Make a wish', 'Go home', 'Hide'], 'ans': 0, 'why': '“Make a wish and blow out the candles.”'}}],
  'compare': {'br': 'In Brazil, people also sing “Parabéns pra você” and cut the cake. Surprise parties exist too.', 'us': 'In the USA, the song is “Happy Birthday to You.” At a surprise party, guests arrive early and stay quiet.', 'tip': 'Say: “Keep it a secret.”', 'ask': 'Do you like surprises? Say yes or no and why.'},
  'quiz': [
   {'q': 'The guest of honor is coming. You say…', 'opts': ['Shh! She’s coming.', 'She is coming shh.', 'Shh! Coming she.'], 'ans': 0, 'why': 'Shh! She’s coming. is short and clear.'},
   {'q': 'You ask if the cake is ready. You say…', 'opts': ['Is the cake ready?', 'The cake is ready?', 'Is ready the cake?'], 'ans': 0, 'why': 'Questions with be start with Is.'},
   {'q': 'What do you shout when the person walks in?', 'opts': ['Surprise!', 'Goodbye!', 'Sorry!'], 'ans': 0, 'why': 'Surprise! is the traditional shout.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Shh! She’s coming',
  'text': [
   'Hugo is at a surprise party in Houston. It is Mia’s birthday, and her friend Rosa has a plan. Ten friends are in the living room. A big cake and some balloons are on the table.',
   '“**Shh! She’s coming**,” Rosa says. “**Everyone hide!**” Hugo says. People go behind the sofa, the door and the curtain. “**Is the cake ready?**” “**Yes, it’s on the table.**”',
   '“**Turn off the lights.**” The room is dark. “**Quiet, quiet…**” The door opens, and Mia comes in. “**Surprise! Happy birthday!**” everyone shouts. Mia laughs. “**Oh my gosh! I can’t believe it!**” “**You didn’t know?**” Rosa asks. “No!” Mia says.',
   'Mia’s little brother asks, “How come the lights are off?” Rosa smiles. “Just because!” she says. Hugo thinks about “Bluey,” a cartoon from Australia. It is about a blue puppy who plays games with her family. Tonight, the games are for Mia.',
   'Mia blows out the candles and makes a wish. Her brother eats the first piece of cake. “This is my best birthday,” Mia says. They sing and dance until late.'],
  'glossary': [{'w': 'surprise', 'pt': 'surpresa'}, {'w': 'hide', 'pt': 'esconder-se'}, {'w': 'curtain', 'pt': 'cortina'}, {'w': 'dark', 'pt': 'escuro'}, {'w': 'shouts', 'pt': 'grita'}, {'w': 'cartoon', 'pt': 'desenho animado'}, {'w': 'puppy', 'pt': 'filhote de cachorro'}, {'w': 'wish', 'pt': 'desejo'}, {'w': 'blows', 'pt': 'sopra'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A surprise birthday party', 'A trip to a museum', 'A day at school'], 'ans': 0, 'why': 'Friends hide and surprise Mia.'},
  'scan': [{'q': 'Where is the cake?', 'ans': 'on the table', 'alt': ['table', 'the table']}, {'q': 'What do the friends do with the lights?', 'ans': 'turn them off', 'alt': ['they turn off the lights', 'off']}, {'q': 'What is Bluey?', 'ans': 'a cartoon', 'alt': ['cartoon', 'a blue puppy']}],
  'tf': [{'s': 'Mia knows about the party.', 'ans': False, 'why': 'She says, “I can’t believe it!”'}, {'s': 'The friends hide behind the sofa and the door.', 'ans': True, 'why': 'They go behind the sofa, the door and the curtain.'}, {'s': 'The cake is in the kitchen.', 'ans': False, 'why': 'It is on the table.'}, {'s': 'Mia makes a wish.', 'ans': True, 'why': 'She blows out the candles and makes a wish.'}],
  'order': ['Rosa says, “Shh! She’s coming.”', 'The friends hide.', 'Rosa turns off the lights.', 'Everyone shouts, “Surprise!”', 'Mia blows out the candles.'],
  'ctx': [{'sent': 'The room is dark.', 'w': 'dark', 'opts': ['without light', 'very big', 'very hot'], 'ans': 0, 'why': 'Dark = no light.'}, {'sent': 'Everyone shouts, “Surprise!”', 'w': 'shouts', 'opts': ['says very loudly', 'whispers', 'sleeps'], 'ans': 0, 'why': 'Shout = speak very loudly.'}, {'sent': 'Mia makes a wish.', 'w': 'wish', 'opts': ['a hope for something good', 'a small cake', 'a loud song'], 'ans': 0, 'why': 'A wish is something you hope will happen.'}],
  'chunkHunt': ['Shh! She’s coming.', 'Is the cake ready?', 'Turn off the lights.', 'I can’t believe it!'],
  'think': 'Do you want a surprise party for your birthday? Why or why not?'},
 'convo': {'npc': {'name': 'Rosa'}, 'story': 'You are at Mia’s surprise party. Help Rosa get ready.', 'turns': [
  {'npc': 'Shh! She’s coming.', 'pt': 'Shh! Ela está chegando.', 'opts': [
   {'en': 'Everyone hide!', 'pt': 'Todos se escondam!', 'ok': True, 'fb': 'Short and quick, like the moment.'},
   {'en': 'Everyone hides!', 'pt': 'Todos se esconde!', 'ok': False, 'fb': 'An order uses the base verb: hide.'},
   {'en': 'Happy birthday to you!', 'pt': 'Feliz aniversário!', 'ok': False, 'fb': 'Too early. She is not here yet.'}]},
  {'npc': 'Is the cake ready?', 'pt': 'O bolo está pronto?', 'opts': [
   {'en': 'Yes, is on the table.', 'pt': 'Sim, é na mesa.', 'ok': False, 'fb': 'Say: it’s on the table.'},
   {'en': 'Yes, it’s on the table.', 'pt': 'Sim, está na mesa.', 'ok': True, 'fb': 'Clear and complete.'},
   {'en': 'Yes, I am a cake.', 'pt': 'Sim, eu sou um bolo.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Turn off the lights.', 'pt': 'Apague as luzes.', 'opts': [
   {'en': 'Okay. Quiet, quiet…', 'pt': 'Ok. Silêncio, silêncio…', 'ok': True, 'fb': 'Agrees and asks for quiet.'},
   {'en': 'Turn on the music!', 'pt': 'Ligue a música!', 'ok': False, 'fb': 'Wrong: they need to be quiet.'},
   {'en': 'The lights are not.', 'pt': 'As luzes não são.', 'ok': False, 'fb': 'Does not make sense.'}]},
  {'npc': 'Here she comes! Ready?', 'pt': 'Lá vem ela! Prontos?', 'opts': [
   {'en': 'Sorry, goodbye!', 'pt': 'Desculpe, tchau!', 'ok': False, 'fb': 'It does not fit the moment.'},
   {'en': 'Surprise! Happy birthday!', 'pt': 'Surpresa! Feliz aniversário!', 'ok': True, 'fb': 'The traditional shout.'},
   {'en': 'Where is the cake?', 'pt': 'Onde está o bolo?', 'ok': False, 'fb': 'You already know: on the table.'}]},
  {'npc': 'Look at her face! She didn’t know.', 'pt': 'Olhe a cara dela! Ela não sabia.', 'opts': [
   {'en': 'She not knew!', 'pt': 'Ela não soube!', 'ok': False, 'fb': 'Use didn’t know.'},
   {'en': 'Shh! She’s coming.', 'pt': 'Shh! Ela está chegando.', 'ok': False, 'fb': 'She is already here.'},
   {'en': 'Yes! It’s a great surprise.', 'pt': 'Sim! É uma ótima surpresa.', 'ok': True, 'fb': 'A happy reaction.'}]}]},
 'errors': [
  {'wrong': 'The cake is ready?', 'fix': 'Is the cake ready?', 'alt': 'Is ready the cake?', 'why': 'Yes/no questions with be start with Is.'},
  {'wrong': 'I can’t to believe it!', 'fix': 'I can’t believe it!', 'alt': 'I no can believe it!', 'why': 'After can/can’t, use the base verb without to.'},
  {'wrong': 'You didn’t knew?', 'fix': 'You didn’t know?', 'alt': 'You not knew?', 'why': 'After didn’t, use the base verb: know.'},
  {'wrong': 'Yes, is on the table.', 'fix': 'Yes, it’s on the table.', 'alt': 'Yes, it on the table.', 'why': 'English needs it: it’s on the table.'}],
 'homework': 'Write 4 short lines for a surprise party: she is coming, hide, turn off the lights, surprise.',
 'homework_items': ['Say aloud: Shh! She’s coming.', 'Write: Is the cake ready? and a short answer.', 'Listen to the dialogue and shadow Rosa.', 'Review: because / just because.']}
