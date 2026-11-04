"""Suplemento Quest v5 · aula 166: Could you repeat that? + regular Ask a question, give an answer (Who Wants to Be a Millionaire?)."""
SUPP = {
 'reg': 181,
 'badge': {'icon': '🔁', 'name': 'Say It Again', 'desc': 'Ask people to repeat and speak slowly'},
 'culture': {
  'hook': 'When you do not understand someone in English, you can ask for help. Native speakers hear this question every day, and they are usually happy to say it again.',
  'mythfact': [
   {'s': 'It is rude to ask a person to say something again.', 'ans': False, 'why': 'With “Sorry, could you repeat that?” it is polite and normal.'},
   {'s': 'In the USA, $8.50 is often said “eight fifty”.', 'ans': True, 'why': 'People often drop the word “dollars” and “cents” when they speak fast.'},
   {'s': 'In most US stores, the final price can be higher than the price on the shelf.', 'ans': True, 'why': 'In many places, sales tax is added at the register.'},
   {'s': 'A receipt is a piece of paper that shows what you paid.', 'ans': True, 'why': 'It usually lists the items, the total and the date.'},
   {'s': '“Who Wants to Be a Millionaire?” is a quiz show where players answer questions for money.', 'ans': True, 'why': 'The host asks a question and the player has four answers.'}],
  'wild': [
   {'kind': 'Cafe receipt', 'lines': ['**Coffee** $4.00', '**Muffin** $3.50', 'Tax $1.00', '**Total** $8.50'], 'decode': {'q': 'What is the total?', 'opts': ['$8.50', '$7.50', '$4.00'], 'ans': 0, 'why': 'The last line says Total $8.50.'}},
   {'kind': 'Sign at a cafe counter', 'lines': ['**Order here**', 'Pick up your drink on the right', 'Ask for a receipt'], 'decode': {'q': 'Where do you order?', 'opts': ['Here', 'On the right', 'At the door'], 'ans': 0, 'why': '“Order here” shows where to order.'}}],
  'compare': {'br': 'In Brazil, people often say “Como?” or “Pode repetir?” when they do not hear well.', 'us': 'In the USA, people say “Sorry?”, “Pardon?” or “Could you repeat that?”. They often speak fast, so asking again is normal and polite.', 'tip': 'Smile and say: “Sorry, could you speak more slowly?”', 'ask': 'What do you say in Portuguese when you do not hear well? Say it in English.'},
  'quiz': [
   {'q': 'You do not hear the price. You say…', 'opts': ['Sorry, could you repeat that?', 'Sorry, I repeat you.', 'Repeat me, please.'], 'ans': 0, 'why': 'Could you repeat that? is the polite question.'},
   {'q': 'The speaker is too fast. You say…', 'opts': ['Could you speak more slowly?', 'Could you speak more slow?', 'Speak slowly more.'], 'ans': 0, 'why': 'Use more slowly with speak.'},
   {'q': 'What does “receipt” mean?', 'opts': ['the paper with the price you paid', 'a kind of coffee', 'a cashier'], 'ans': 0, 'why': 'A receipt is the paper you get after you pay.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Ana and the quiz question',
  'text': [
   'Ana is in a café in **Seattle**. She wants a coffee and a muffin. The café is busy, and the music is loud.',
   'The cashier is Mei. “Hi! The total is eight fifty,” Mei says. Ana does not hear well. “**Sorry, could you repeat that?**” “Eight dollars and fifty cents.” Ana says, “**Could you speak more slowly?**” Mei smiles. “Sure. Eight. Fifty.” “**Okay, I got it. Thank you.**”',
   'Mei asks, “Do you want a receipt?” Ana does not know the word. “**Sorry, what does “receipt” mean?**” “It’s the paper with the price.” “Yes, please.” Now Ana has a new word.',
   'Ana likes TV quiz shows. On “Who Wants to Be a Millionaire?”, the host asks a question, and the player has four answers. The player can ask, “**Could you say that again?**” Ana thinks, “I can do the same in a café.”',
   'At the table, Ana drinks her coffee. She can understand the number, the price and the new word. It is okay to ask again. People in the café are kind.'],
  'glossary': [{'w': 'busy', 'pt': 'cheio, movimentado'}, {'w': 'loud', 'pt': 'alto (som)'}, {'w': 'cashier', 'pt': 'caixa (pessoa)'}, {'w': 'total', 'pt': 'total'}, {'w': 'hear', 'pt': 'ouvir'}, {'w': 'receipt', 'pt': 'recibo'}, {'w': 'host', 'pt': 'apresentador'}, {'w': 'player', 'pt': 'jogador, participante'}, {'w': 'again', 'pt': 'de novo'}, {'w': 'understand', 'pt': 'entender'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A woman asks for help in a café', 'A man cooks dinner', 'A girl takes a plane'], 'ans': 0, 'why': 'Ana asks Mei to repeat the price.'},
  'scan': [{'q': 'What is the total?', 'ans': 'eight fifty', 'alt': ['$8.50', 'eight dollars and fifty cents', '8.50']}, {'q': 'Who is the cashier?', 'ans': 'Mei', 'alt': ['mei']}, {'q': 'How many answers does the quiz show player have?', 'ans': 'four', 'alt': ['4']}],
  'tf': [{'s': 'Ana hears the price the first time.', 'ans': False, 'why': 'She asks Mei to repeat it.'}, {'s': 'Mei speaks more slowly.', 'ans': True, 'why': '“Sure. Eight. Fifty.”'}, {'s': 'Ana knows the word “receipt”.', 'ans': False, 'why': 'She asks what it means.'}, {'s': 'The people in the café are kind.', 'ans': True, 'why': 'The last paragraph says so.'}],
  'order': ['Ana goes into the café.', 'Mei says the total.', 'Ana asks Mei to repeat it.', 'Ana asks about the word receipt.', 'Ana drinks her coffee.'],
  'ctx': [{'sent': 'The café is busy.', 'w': 'busy', 'opts': ['full of people', 'very small', 'closed'], 'ans': 0, 'why': 'Busy = a lot of people and things happening.'}, {'sent': 'Ana does not hear well.', 'w': 'hear', 'opts': ['get a sound with your ears', 'see with your eyes', 'taste food'], 'ans': 0, 'why': 'You hear with your ears.'}, {'sent': 'The host asks a question.', 'w': 'host', 'opts': ['the person who leads a show', 'a kind of coffee', 'a person who drives'], 'ans': 0, 'why': 'The host leads the quiz show.'}],
  'chunkHunt': ['Sorry, could you repeat that?', 'Could you speak more slowly?', 'Okay, I got it.', 'What does “receipt” mean?'],
  'think': 'When do you not understand English? What can you say to ask for help?'},
 'convo': {'npc': {'name': 'Mei'}, 'story': 'You are in a café in Seattle. Mei is the cashier. Talk to her.', 'turns': [
  {'npc': 'Hi! The total is eight fifty.', 'pt': 'Oi! O total é oito e cinquenta.', 'opts': [
   {'en': 'Sorry, could you repeat that?', 'pt': 'Desculpe, pode repetir?', 'ok': True, 'fb': 'Polite way to ask again.'},
   {'en': 'I repeat the price.', 'pt': 'Eu repito o preço.', 'ok': False, 'fb': 'Wrong: you ask her to repeat.'},
   {'en': 'Yes, I am eight fifty.', 'pt': 'Sim, eu sou oito e cinquenta.', 'ok': False, 'fb': 'Does not make sense.'}]},
  {'npc': 'Eight dollars and fifty cents.', 'pt': 'Oito dólares e cinquenta centavos.', 'opts': [
   {'en': 'Could you speak more slow?', 'pt': 'Pode falar mais lento?', 'ok': False, 'fb': 'Say more slowly.'},
   {'en': 'Could you speak more slowly?', 'pt': 'Pode falar mais devagar?', 'ok': True, 'fb': 'Natural and polite.'},
   {'en': 'I have eight dollars.', 'pt': 'Eu tenho oito dólares.', 'ok': False, 'fb': 'It does not answer her.'}]},
  {'npc': 'Sure. Eight. Fifty.', 'pt': 'Claro. Oito. Cinquenta.', 'opts': [
   {'en': 'Okay, I got it. Thank you.', 'pt': 'Ok, entendi. Obrigado.', 'ok': True, 'fb': 'Shows you understand now.'},
   {'en': 'Sorry, could you repeat that?', 'pt': 'Desculpe, pode repetir?', 'ok': False, 'fb': 'She just repeated it slowly.'},
   {'en': 'I am a cashier.', 'pt': 'Sou caixa.', 'ok': False, 'fb': 'Wrong person.'}]},
  {'npc': 'Do you want a receipt?', 'pt': 'Quer o recibo?', 'opts': [
   {'en': 'No, I am not receipt.', 'pt': 'Não, eu não sou recibo.', 'ok': False, 'fb': 'Wrong grammar.'},
   {'en': 'Yes, I want a coffee.', 'pt': 'Sim, quero um café.', 'ok': False, 'fb': 'She asks about a receipt.'},
   {'en': 'Sorry, what does “receipt” mean?', 'pt': 'Desculpe, o que significa “receipt”?', 'ok': True, 'fb': 'Good way to ask a word.'}]},
  {'npc': 'It’s the paper with the price.', 'pt': 'É o papel com o preço.', 'opts': [
   {'en': 'Yes, please. Thank you!', 'pt': 'Sim, por favor. Obrigado!', 'ok': True, 'fb': 'Natural answer.'},
   {'en': 'The total is eight fifty.', 'pt': 'O total é oito e cinquenta.', 'ok': False, 'fb': 'That is her job.'},
   {'en': 'Eight dollars and fifty cents.', 'pt': 'Oito dólares e cinquenta centavos.', 'ok': False, 'fb': 'Already said.'}]}]},
 'errors': [
  {'wrong': 'Can you repeat me?', 'fix': 'Could you repeat that?', 'alt': 'Can you repeat it me?', 'why': 'Repeat takes “that” or “it”, not “me”.'},
  {'wrong': 'Speak more slow, please.', 'fix': 'Please speak more slowly.', 'alt': 'Speak slowly more.', 'why': 'Use the adverb slowly (more slowly).'},
  {'wrong': 'I no understand.', 'fix': 'I don’t understand.', 'alt': 'I not understand.', 'why': 'Use don’t before the verb.'},
  {'wrong': 'What means receipt?', 'fix': 'What does “receipt” mean?', 'alt': 'What is mean receipt?', 'why': 'Question: What does + word + mean?'}],
 'homework': 'Write a short dialogue: you do not hear a price and you ask the cashier to say it again slowly.',
 'homework_items': ['Say aloud: Sorry, could you repeat that?', 'Write 3 ways to ask someone to say it again.', 'Listen to the dialogue and shadow Ana.', 'Review the numbers from one to fifty.']}
