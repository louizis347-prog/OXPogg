"""Suplemento Quest v5 · aula 111: A call at work + regular Which extension? (30 Rock)."""
SUPP = {
 'reg': 189,
 'badge': {'icon': '☎️', 'name': 'Phone Pro', 'desc': 'Ask for a person, wait, and leave a message'},
 'culture': {
  'hook': 'A phone call at work follows small steps: say hello, ask for the person, wait a moment, and leave a message with your name and number if the person is out.',
  'mythfact': [
   {'s': 'At work, people often answer the phone with the company name.', 'ans': True, 'why': 'Many offices say, for example, “Good morning, Austin Print.”'},
   {'s': 'You must hang up if the person is not there.', 'ans': False, 'why': 'You can leave a message or call again later.'},
   {'s': 'A short number inside a company is called an extension.', 'ans': True, 'why': 'It connects you to one person or one desk.'},
   {'s': 'In the USA, a phone number has seven digits and no area code.', 'ans': False, 'why': 'It usually has an area code plus seven digits, ten numbers in all.'},
   {'s': '“30 Rock” is an American comedy about a TV show.', 'ans': True, 'why': 'It began in 2006 and is set in a TV office.'}],
  'wild': [
   {'kind': 'Voicemail greeting', 'lines': ['**Hi, you reached Mr. Lee.**', 'I am not at my desk right now.', 'Please leave a message after the beep.'], 'decode': {'q': 'What should you do after the beep?', 'opts': ['Leave a message', 'Hang up and wait', 'Press the extension'], 'ans': 0, 'why': '“Please leave a message after the beep.”'}},
   {'kind': 'Phone menu', 'lines': ['**Press 1** for sales.', '**Press 2** for help.', 'Press 0 to speak to the operator.'], 'decode': {'q': 'Which key helps you speak to a person?', 'opts': ['0', '1', '2'], 'ans': 0, 'why': 'Press 0 for the operator.'}}],
  'compare': {'br': 'No Brasil, muita gente atende com “Alô?” e depois diz o nome da empresa.', 'us': 'Nos EUA, no trabalho, é comum dizer logo o nome da empresa e o seu nome.', 'tip': 'Say: “Hello. Can I speak to Mr. Lee, please?”', 'ask': 'How do you answer the phone at work in your language?'},
  'quiz': [
   {'q': 'You want to talk to Mr. Lee. You say…', 'opts': ['Can I speak to Mr. Lee, please?', 'I speak Mr. Lee now.', 'Mr. Lee is a message.'], 'ans': 0, 'why': 'Can I speak to…? is the polite way.'},
   {'q': '“I’ll transfer you” means…', 'opts': ['I will send your call to someone', 'I will end the call', 'I will call you tomorrow'], 'ans': 0, 'why': 'Transfer = send the call to another line.'},
   {'q': 'Someone is not there. What can you do?', 'opts': ['Leave a message', 'Shout', 'Break the phone'], 'ans': 0, 'why': 'Leaving a message is normal.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Sam calls the office',
  'text': [
   'Sam works in a small shop in **Austin**. Today he needs to talk to Mr. Lee at the print office. He takes his phone and makes a call.',
   '“**Good morning, Austin Print.** Tessa speaking,” a woman says. “Hello. **Can I speak to Mr. Lee, please?**” Sam asks. “**One moment. I’ll transfer you.**” “Thank you.”',
   'The line is quiet. Then Tessa comes back. “**I’m sorry, he’s not here.** **Can I take a message?**” “Yes, please. Tell him Sam called.” Tessa writes it on a yellow note. “**What’s your phone number?**” Sam says it slowly, number by number.',
   'Sam likes TV, and he thinks about “30 Rock.” It is an American comedy that began in 2006. The story is about people who make a TV show, and the office phone is always ringing. In a big company, a short number called an extension connects you to one person.',
   'Ten minutes later, Sam’s phone rings. “Hi Sam, this is Mr. Lee. Thanks for your message!” Sam smiles. A good call is easy: say hello, ask for the person, wait, and leave your number.'],
  'glossary': [{'w': 'call', 'pt': 'ligação; ligar'}, {'w': 'office', 'pt': 'escritório'}, {'w': 'moment', 'pt': 'momento'}, {'w': 'transfer', 'pt': 'transferir'}, {'w': 'message', 'pt': 'recado'}, {'w': 'line', 'pt': 'linha (telefônica)'}, {'w': 'note', 'pt': 'bilhete'}, {'w': 'extension', 'pt': 'ramal'}, {'w': 'rings', 'pt': 'toca'}, {'w': 'number', 'pt': 'número'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A man calls an office', 'A woman buys shoes', 'A boy plays soccer'], 'ans': 0, 'why': 'Sam calls Austin Print.'},
  'scan': [{'q': 'Who answers the phone?', 'ans': 'Tessa', 'alt': ['tessa']}, {'q': 'Who does Sam want to talk to?', 'ans': 'Mr. Lee', 'alt': ['mr lee', 'lee']}, {'q': 'What color is the note?', 'ans': 'yellow', 'alt': ['a yellow note']}],
  'tf': [{'s': 'Sam asks for Mr. Lee.', 'ans': True, 'why': 'He says, “Can I speak to Mr. Lee, please?”'}, {'s': 'Mr. Lee is at the office when Sam calls.', 'ans': False, 'why': 'Tessa says he is not there.'}, {'s': 'Tessa writes a message.', 'ans': True, 'why': 'She writes it on a yellow note.'}, {'s': 'Mr. Lee never calls back.', 'ans': False, 'why': 'He calls Sam ten minutes later.'}],
  'order': ['Sam calls Austin Print.', 'Tessa transfers the call.', 'Tessa says Mr. Lee is not there.', 'Sam leaves his number.', 'Mr. Lee calls Sam.'],
  'ctx': [{'sent': 'One moment. I’ll transfer you.', 'w': 'transfer', 'opts': ['send the call to someone', 'throw the phone', 'hang up'], 'ans': 0, 'why': 'Transfer = move the call.'}, {'sent': 'The office phone is always ringing.', 'w': 'ringing', 'opts': ['making a sound for a call', 'being very cold', 'being broken'], 'ans': 0, 'why': 'A phone rings when someone calls.'}, {'sent': 'Please tell him Sam called.', 'w': 'tell', 'opts': ['say to someone', 'give money', 'close'], 'ans': 0, 'why': 'Tell = say something to a person.'}],
  'chunkHunt': ['Can I speak to Mr. Lee, please?', 'I’ll transfer you.', 'Can I take a message?', 'What’s your phone number?'],
  'think': 'Do you like to talk on the phone or send texts? Why?'},
 'convo': {'npc': {'name': 'Tessa'}, 'story': 'You call Austin Print because you want to talk to Mr. Lee. Tessa answers.', 'turns': [
  {'npc': 'Good morning, Austin Print. Tessa speaking.', 'pt': 'Bom dia, Austin Print. Tessa falando.', 'opts': [
   {'en': 'Hello. Can I speak to Mr. Lee, please?', 'pt': 'Olá. Posso falar com o Sr. Lee, por favor?', 'ok': True, 'fb': 'Polite way to ask for a person.'},
   {'en': 'Hello. I speak with Mr. Lee?', 'pt': 'Olá. Eu falo com o Sr. Lee?', 'ok': False, 'fb': 'Use Can I speak to…?'},
   {'en': 'Good night. I am Tessa.', 'pt': 'Boa noite. Eu sou a Tessa.', 'ok': False, 'fb': 'Tessa is the one who answers.'}]},
  {'npc': 'One moment. I’ll transfer you.', 'pt': 'Um momento. Vou transferir.', 'opts': [
   {'en': 'I transfer you too.', 'pt': 'Eu transfiro você também.', 'ok': False, 'fb': 'It does not fit.'},
   {'en': 'Thank you.', 'pt': 'Obrigado.', 'ok': True, 'fb': 'Simple and polite.'},
   {'en': 'Goodbye, Tessa.', 'pt': 'Tchau, Tessa.', 'ok': False, 'fb': 'Too early to say goodbye.'}]},
  {'npc': 'I’m sorry, he’s not here. Can I take a message?', 'pt': 'Sinto muito, ele não está. Posso anotar um recado?', 'opts': [
   {'en': 'Yes. Please tell him Sam called.', 'pt': 'Sim. Diga que o Sam ligou.', 'ok': True, 'fb': 'Gives the message.'},
   {'en': 'Yes. I take a message.', 'pt': 'Sim. Eu pego um recado.', 'ok': False, 'fb': 'You want Tessa to take it.'},
   {'en': 'No, he is here.', 'pt': 'Não, ele está aqui.', 'ok': False, 'fb': 'She said he is not there.'}]},
  {'npc': 'What’s your phone number?', 'pt': 'Qual é o seu telefone?', 'opts': [
   {'en': 'My phone is blue.', 'pt': 'Meu telefone é azul.', 'ok': False, 'fb': 'She asks for the number.'},
   {'en': 'It’s five five five, zero one nine nine.', 'pt': 'É cinco cinco cinco, zero um nove nove.', 'ok': True, 'fb': 'Say the numbers one by one.'},
   {'en': 'I am call you.', 'pt': 'Eu sou ligar você.', 'ok': False, 'fb': 'Wrong grammar and it does not answer.'}]},
  {'npc': 'Thanks! Mr. Lee will call you back.', 'pt': 'Obrigada! O Sr. Lee vai retornar a ligação.', 'opts': [
   {'en': 'Thank you. Goodbye!', 'pt': 'Obrigado. Tchau!', 'ok': True, 'fb': 'Natural way to end a call.'},
   {'en': 'Good morning!', 'pt': 'Bom dia!', 'ok': False, 'fb': 'That is a greeting, not a goodbye.'},
   {'en': 'Can I speak to Mr. Lee?', 'pt': 'Posso falar com o Sr. Lee?', 'ok': False, 'fb': 'She just said he is out.'}]}]},
 'errors': [
  {'wrong': 'I want speak with Mr. Lee.', 'fix': 'I want to speak to Mr. Lee.', 'alt': 'I want speaking to Mr. Lee.', 'why': 'After want, use to + verb.'},
  {'wrong': 'Can I leave a recado?', 'fix': 'Can I leave a message?', 'alt': 'Can I leave a messages?', 'why': 'Message is the English word; use one message.'},
  {'wrong': 'My number is five five five zero one nine nine, thanks.', 'fix': 'It’s five five five, zero one nine nine.', 'alt': 'Is five five five, zero one nine nine.', 'why': 'On the phone, say numbers one by one with a pause in the middle.'},
  {'wrong': 'He is not in here.', 'fix': 'He’s not here.', 'alt': 'He not is here.', 'why': 'Say He’s not here, short and natural.'}],
 'homework': 'Write a short phone dialogue: you call a school and ask for a teacher who is out.',
 'homework_items': ['Write 3 lines to ask for a person on the phone.', 'Say your phone number aloud in English.', 'Listen to the dialogue and shadow Tessa.', 'Review: moment / message / transfer.']}
