"""Suplemento Quest v5 · aula 181: Too much noise + regular Fall asleep, stay up (Goodnight Moon)."""
SUPP = {
 'reg': 191,
 'badge': {'icon': '🔉', 'name': 'Quiet Night', 'desc': 'Ask a neighbor politely to turn the sound down'},
 'culture': {
  'hook': 'In many American apartment buildings, people prefer a polite knock or a short note to a loud fight. A kind, short sentence usually solves a noise problem fast.',
  'mythfact': [
   {'s': 'In the USA, it is normal to knock and ask a neighbor to turn the volume down.', 'ans': True, 'why': 'A calm, polite request is the usual first step.'},
   {'s': 'You should shout through the wall at night.', 'ans': False, 'why': 'Shouting makes more noise and can make the neighbor angry.'},
   {'s': '“Sorry to bother you” is a polite way to start.', 'ans': True, 'why': 'It tells the person you know you are interrupting.'},
   {'s': 'Many buildings have quiet hours at night.', 'ans': True, 'why': 'Many rental buildings and cities have rules for late-night noise, but the hours change from place to place.'},
   {'s': '“Goodnight Moon” is a children’s book.', 'ans': True, 'why': 'Margaret Wise Brown wrote it, and it came out in 1947.'}],
  'wild': [
   {'kind': 'Sign in a building hallway', 'lines': ['**Quiet hours: 10 PM – 8 AM**', 'Please keep the volume low.', 'Thank you, neighbors!'], 'decode': {'q': 'When are the quiet hours?', 'opts': ['At night', 'At noon', 'All day'], 'ans': 0, 'why': 'From 10 PM to 8 AM.'}},
   {'kind': 'Note on a door', 'lines': ['Hi! I live in 4B.', '**The TV is a little loud at night.**', 'Could you turn it down? Thanks!'], 'decode': {'q': 'What is loud?', 'opts': ['The TV', 'The door', 'The dog'], 'ans': 0, 'why': 'The note says “The TV is a little loud.”'}}],
  'compare': {'br': 'In Brazil, many people feel okay about parties and loud music on weekends, and neighbors often talk face to face.', 'us': 'In the USA, many people ask for quiet in a very soft way, with “a little loud” and “Sorry to bother you.”', 'tip': 'Say: “Sorry to bother you. Could you turn it down, please?”', 'ask': 'How do you ask a neighbor for quiet? Say it in English.'},
  'quiz': [
   {'q': 'You knock on a neighbor’s door. First you say…', 'opts': ['Sorry to bother you.', 'Be quiet now!', 'I am the noise.'], 'ans': 0, 'why': 'It is the polite way to start.'},
   {'q': 'The music is too loud. A soft way to say it is…', 'opts': ['The music is a little loud.', 'The music has loud.', 'Music is loudly.'], 'ans': 0, 'why': 'Use is + loud. “A little” makes it softer.'},
   {'q': 'Your neighbor says sorry. You answer…', 'opts': ['It’s okay. It happens.', 'It is your sleep.', 'You are noise.'], 'ans': 0, 'why': 'It is a kind answer to sorry.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'A little loud',
  'text': [
   'Mia lives in an apartment in **Boston**. It is eleven o’clock at night. She is in bed, but she cannot sleep. Her neighbor Theo has a TV and loud music. The wall is thin, and she hears every song. She has work early in the morning.',
   'Mia puts on her jacket and knocks on his door. She is a little nervous, but she smiles. “**Hi. Sorry to bother you**,” she says. “**No problem. What’s up?**” Theo asks.',
   '“**The music is a little loud.**” “**Oh, I’m so sorry!**” “**It’s late, and I have to sleep.**” Mia speaks in a soft voice. She does not shout.',
   '“**I understand. I’ll turn it down.**” Theo goes back and turns the volume down. “**I didn’t know it was so loud**,” he says. “**It’s okay. It happens**,” Mia says. “**Thank you very much.**”',
   'Back in bed, Mia thinks about a children’s book, “Goodnight Moon.” In the book, a little rabbit says goodnight to the room, the moon and the stars. Now Mia’s room is quiet. “**Sleep tight**,” she says to herself, and she closes her eyes.'],
  'glossary': [{'w': 'bother', 'pt': 'incomodar'}, {'w': 'loud', 'pt': 'alto, barulhento'}, {'w': 'sleep', 'pt': 'dormir'}, {'w': 'neighbor', 'pt': 'vizinho'}, {'w': 'knocks', 'pt': 'bate (na porta)'}, {'w': 'shout', 'pt': 'gritar'}, {'w': 'volume', 'pt': 'volume'}, {'w': 'quiet', 'pt': 'quieto, silencioso'}, {'w': 'late', 'pt': 'tarde'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A woman asks her neighbor to turn the music down', 'A woman goes to a party', 'A man buys a new TV'], 'ans': 0, 'why': 'Mia knocks and asks Theo about the loud music.'},
  'scan': [{'q': 'What time is it?', 'ans': 'eleven o’clock', 'alt': ['11', 'eleven', 'eleven at night']}, {'q': 'What is the neighbor’s name?', 'ans': 'Theo', 'alt': ['his name is Theo']}, {'q': 'What does Mia not do?', 'ans': 'shout', 'alt': ['she does not shout', 'she doesn’t shout']}],
  'tf': [{'s': 'Mia cannot sleep.', 'ans': True, 'why': 'The music is too loud.'}, {'s': 'Mia shouts at Theo.', 'ans': False, 'why': 'She speaks in a soft voice.'}, {'s': 'Theo turns the volume down.', 'ans': True, 'why': 'He says, “I’ll turn it down.”'}, {'s': 'Theo knew the music was loud.', 'ans': False, 'why': 'He says, “I didn’t know it was so loud.”'}],
  'order': ['Mia cannot sleep.', 'Mia knocks on Theo’s door.', 'Mia says the music is loud.', 'Theo turns it down.', 'Mia says sleep tight.'],
  'ctx': [{'sent': 'Sorry to bother you.', 'w': 'bother', 'opts': ['to interrupt you', 'to see you', 'to feed you'], 'ans': 0, 'why': 'Bother = interrupt or trouble someone.'}, {'sent': 'The music is a little loud.', 'w': 'loud', 'opts': ['with a lot of sound', 'with no sound', 'very small'], 'ans': 0, 'why': 'Loud = a lot of sound.'}, {'sent': 'Mia does not shout.', 'w': 'shout', 'opts': ['speak very loudly', 'speak very softly', 'not speak'], 'ans': 0, 'why': 'Shout = speak very loudly.'}],
  'chunkHunt': ['Sorry to bother you.', 'The music is a little loud.', 'It’s late, and I have to sleep.', 'I’ll turn it down.', 'It happens.'],
  'think': 'Do you knock on a neighbor’s door, or do you write a note? What do you say?'},
 'convo': {'npc': {'name': 'Theo'}, 'story': 'It is late at night in an apartment in Boston. You knock on your neighbor Theo’s door because his music is loud.', 'turns': [
  {'npc': 'Hi. Who is it?', 'pt': 'Oi. Quem é?', 'opts': [
   {'en': 'Hi. Sorry to bother you.', 'pt': 'Oi. Desculpe incomodar.', 'ok': True, 'fb': 'Polite start.'},
   {'en': 'Hi. I am the noise.', 'pt': 'Oi. Eu sou o barulho.', 'ok': False, 'fb': 'It does not make sense.'},
   {'en': 'Goodbye. See you.', 'pt': 'Tchau. Até logo.', 'ok': False, 'fb': 'Wrong moment.'}]},
  {'npc': 'No problem. What’s up?', 'pt': 'Sem problema. O que houve?', 'opts': [
   {'en': 'The music is loudly.', 'pt': 'A música está altamente.', 'ok': False, 'fb': 'After is, use loud, not loudly.'},
   {'en': 'The music is a little loud.', 'pt': 'A música está um pouco alta.', 'ok': True, 'fb': 'Clear and soft.'},
   {'en': 'I like your music.', 'pt': 'Eu gosto da sua música.', 'ok': False, 'fb': 'It does not say the problem.'}]},
  {'npc': 'Oh, I’m so sorry!', 'pt': 'Ah, sinto muito!', 'opts': [
   {'en': 'It’s late, and I have to sleep.', 'pt': 'É tarde e preciso dormir.', 'ok': True, 'fb': 'Gives the reason.'},
   {'en': 'It is late and I must to sleep.', 'pt': 'É tarde e eu devo dormir.', 'ok': False, 'fb': 'Say have to sleep. Must is not used with to.'},
   {'en': 'You are welcome.', 'pt': 'De nada.', 'ok': False, 'fb': 'Not a reply to sorry.'}]},
  {'npc': 'I understand. I’ll turn it down.', 'pt': 'Entendo. Vou abaixar.', 'opts': [
   {'en': 'Sorry to bother you.', 'pt': 'Desculpe incomodar.', 'ok': False, 'fb': 'You already said it.'},
   {'en': 'Thank you very much.', 'pt': 'Muito obrigado.', 'ok': True, 'fb': 'Simple and kind.'},
   {'en': 'Turn it up, please.', 'pt': 'Aumente, por favor.', 'ok': False, 'fb': 'It is the opposite.'}]},
  {'npc': 'I didn’t know it was so loud.', 'pt': 'Eu não sabia que estava tão alto.', 'opts': [
   {'en': 'It’s okay. It happens.', 'pt': 'Tudo bem. Acontece.', 'ok': True, 'fb': 'Friendly end.'},
   {'en': 'It is not okay.', 'pt': 'Não está bem.', 'ok': False, 'fb': 'Too hard after he says sorry.'},
   {'en': 'I know your name.', 'pt': 'Eu sei seu nome.', 'ok': False, 'fb': 'It does not fit.'}]}]},
 'errors': [
  {'wrong': 'The music is very loudly.', 'fix': 'The music is very loud.', 'alt': 'The music is very louder.', 'why': 'After is, use the adjective: loud.'},
  {'wrong': 'I have sleep.', 'fix': 'I have to sleep.', 'alt': 'I have for sleep.', 'why': 'Have to + verb means “preciso”. I have to sleep.'},
  {'wrong': 'I turn down it.', 'fix': 'I’ll turn it down.', 'alt': 'I turn it to down.', 'why': 'With it, put it in the middle: turn it down.'},
  {'wrong': 'I no knew it was loud.', 'fix': 'I didn’t know it was loud.', 'alt': 'I not knew it was loud.', 'why': 'For past negatives, use didn’t + base verb.'}],
 'homework': 'Write a short dialogue: you knock on a neighbor’s door because of loud music.',
 'homework_items': ['Write three polite ways to start: “Sorry to…”', 'Say aloud: The music is a little loud.', 'Listen to the dialogue and shadow Grace.', 'Review: sleep / volume / knock / TV.']}
