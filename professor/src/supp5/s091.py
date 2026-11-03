"""Suplemento Quest v5 · aula 91: A concert night + regular Break a leg! (High School Musical)."""
SUPP = {
 'reg': 208,
 'badge': {'icon': '🎤', 'name': 'Front Row Fan', 'desc': 'Get in, find your seat and enjoy the show in English'},
 'sticker': {'cat': 'Everyday culture', 'title': 'Concert Night', 'sub': 'Section B, row five. Encore!'},
 'culture': {
  'hook': 'A live concert in the USA starts long before the first song. You show a ticket, find your section and your row, and wait with a loud, happy crowd.',
  'polite': 'If you need to pass people in your row, say **Excuse me** and **Thank you**. Do not stand in front of the people behind you.',
  'mythfact': [
   {'s': 'Many concert tickets in the USA are now on your phone.', 'ans': True, 'why': 'Mobile tickets are very common. You show a code at the door.'},
   {'s': 'An encore is the first song of the show.', 'ans': False, 'why': 'An encore is an extra song after the main show, when the crowd asks for more.'},
   {'s': 'Your ticket often tells you a section, a row and a seat.', 'ans': True, 'why': 'That is how you find your place: Section B, row five.'},
   {'s': 'Nobody sings with the band at a concert.', 'ans': False, 'why': 'Fans often sing along, and singers ask them to.'}],
  'wild': [
   {'kind': 'Mobile ticket', 'lines': ['**Doors open:** 7:00 PM', '**Show starts:** 8:00 PM', '**Section B · Row 5 · Seat 12**'], 'decode': {'q': 'What time does the show start?', 'opts': ['8:00 PM', '7:00 PM', '5:12 PM'], 'ans': 0, 'why': 'Doors open at 7:00, but the show starts at 8:00.'}},
   {'kind': 'Sign at the venue', 'lines': ['**No bags bigger than a small purse.**', '**Have your ticket ready.**', '**Drinks are $7 at the bar.**'], 'decode': {'q': 'What should you do at the door?', 'opts': ['Have your ticket ready', 'Buy a drink', 'Bring a big bag'], 'ans': 0, 'why': 'The sign says: Have your ticket ready.'}}],
  'compare': {'br': 'In Brazil many people buy tickets online too, and students can often pay half price (meia-entrada).', 'us': 'In the USA your ticket shows a section, a row and a seat, and fans often wait for an encore.', 'tip': 'Learn three words from your ticket: section, row, seat.', 'ask': 'What is the last concert you saw or want to see? Say it in English.'},
  'quiz': [
   {'q': 'Someone asks, “Do you have your ticket?” You say…', 'opts': ['Yes, it’s on my phone.', 'Yes, I have you.', 'No, I ticket.'], 'ans': 0, 'why': 'Answer with Yes, it’s on my phone.'},
   {'q': 'What does “Section B, row five” tell you?', 'opts': ['Where your seat is', 'What song is next', 'How much a drink costs'], 'ans': 0, 'why': 'It is the place of your seat.'},
   {'q': 'A song ends and the crowd keeps clapping. The band plays…', 'opts': ['An encore', 'A ticket', 'A row'], 'ans': 0, 'why': 'An encore is an extra song.'}]},
 'reading': {
  'genre': 'Diary', 'title': 'My first concert night',
  'text': [
   'Tonight I went to my first concert in the USA with my friend Omar. I was very happy. At the door, a woman asked, “**Do you have your ticket?**” I showed my phone and she said, “Great. Go in.”',
   'Inside, the room was big and **loud**. We asked, “**Where are our seats?**” Omar looked at his phone. “**Section B, row five**,” he said. We walked past many people and said, “Excuse me, sorry!” again and again.',
   'The **band** started at eight. The **crowd** screamed and the **stage** lights were red and blue. One man next to me shouted, “**This show rocks!**” I sang the words with everyone. Soon I was **losing my voice**!',
   'I remembered a school musical, “High School Musical.” It is a Disney film from 2006, and the students sing on a stage. Before the show, friends say, “**Break a leg!**” That means good luck. Tonight the band was the star.',
   'After the last song, nobody went home. We all clapped and shouted, “**Encore!**” The band came back and played one more song. It was the **best night ever**. “**Enjoy the show!**” Omar said, and I did.'],
  'glossary': [{'w': 'ticket', 'pt': 'ingresso'}, {'w': 'loud', 'pt': 'barulhento'}, {'w': 'seats', 'pt': 'lugares'}, {'w': 'row', 'pt': 'fila (de assentos)'}, {'w': 'band', 'pt': 'banda'}, {'w': 'crowd', 'pt': 'multidão'}, {'w': 'stage', 'pt': 'palco'}, {'w': 'shouted', 'pt': 'gritou'}, {'w': 'clapped', 'pt': 'aplaudiu'}, {'w': 'losing my voice', 'pt': 'ficando sem voz'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A first concert night', 'A trip to the beach', 'A school test'], 'ans': 0, 'why': 'The writer goes to a concert with Omar.'},
  'scan': [{'q': 'Who goes to the concert with the writer?', 'ans': 'Omar', 'alt': ['omar']}, {'q': 'What time does the band start?', 'ans': 'eight', 'alt': ['8', '8:00', 'at eight']}, {'q': 'What is the section?', 'ans': 'B', 'alt': ['section b', 'b']}],
  'tf': [{'s': 'The tickets are on paper.', 'ans': False, 'why': '“I showed my phone.” The ticket is on a phone.'}, {'s': 'The room is loud.', 'ans': True, 'why': '“The room was big and loud.”'}, {'s': 'The band starts at nine.', 'ans': False, 'why': 'The band started at eight.'}, {'s': 'The band plays one more song after the crowd shouts “Encore!”', 'ans': True, 'why': 'The band came back and played one more song.'}],
  'order': ['The writer shows the ticket at the door.', 'They look for their seats.', 'The band starts to play.', 'The crowd shouts “Encore!”', 'The band plays one more song.'],
  'ctx': [{'sent': 'The room was big and loud.', 'w': 'loud', 'opts': ['full of noise', 'very quiet', 'cold'], 'ans': 0, 'why': 'Loud = with a lot of noise.'}, {'sent': 'The crowd screamed when the band came out.', 'w': 'crowd', 'opts': ['one singer', 'a big group of people', 'a seat'], 'ans': 1, 'why': 'A crowd is many people together.'}, {'sent': 'The lights on the stage were red and blue.', 'w': 'stage', 'opts': ['the place where singers perform', 'the door', 'the ticket'], 'ans': 0, 'why': 'The band stands on the stage.'}],
  'chunkHunt': ['Do you have your ticket?', 'Where are our seats?', 'This show rocks!', 'Encore!'],
  'think': 'Which singer or band would you like to see live? What would you say to a friend at the door?'},
 'convo': {'npc': {'name': 'Omar'}, 'story': 'You are at a concert in Austin with your friend Omar. Get in and find your seats.', 'turns': [
  {'npc': 'Do you have your ticket?', 'pt': 'Você tem seu ingresso?', 'opts': [
   {'en': 'Yes, I have you.', 'pt': 'Sim, eu tenho você.', 'ok': False, 'fb': 'Wrong object. The thing is your ticket.'},
   {'en': 'Yes, it’s on my phone.', 'pt': 'Tenho, está no celular.', 'ok': True, 'fb': 'Natural and complete.'},
   {'en': 'No, I am ticket.', 'pt': 'Não, eu sou ingresso.', 'ok': False, 'fb': 'Not English. Say it’s on my phone.'}]},
  {'npc': 'Great. Let’s go in.', 'pt': 'Ótimo. Vamos entrar.', 'opts': [
   {'en': 'Where are our seats?', 'pt': 'Onde ficam nossos lugares?', 'ok': True, 'fb': 'Good question after you go in.'},
   {'en': 'Where is the seat our?', 'pt': 'Onde é o lugar nosso?', 'ok': False, 'fb': 'Word order: our seats.'},
   {'en': 'We are seats.', 'pt': 'Nós somos lugares.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Section B, row five.', 'pt': 'Setor B, fila cinco.', 'opts': [
   {'en': 'Thanks. It is five.', 'pt': 'Valeu. É cinco.', 'ok': False, 'fb': 'Too short and not clear.'},
   {'en': 'No, I am hungry.', 'pt': 'Não, estou com fome.', 'ok': False, 'fb': 'It does not answer.'},
   {'en': 'OK! It’s loud in here!', 'pt': 'Ok! Está barulhento aqui!', 'ok': True, 'fb': 'Natural comment about the room.'}]},
  {'npc': 'I know! The band starts at eight.', 'pt': 'Eu sei! A banda começa às oito.', 'opts': [
   {'en': 'Let’s get a drink first.', 'pt': 'Vamos tomar algo primeiro.', 'ok': True, 'fb': 'A good plan before the show.'},
   {'en': 'The band is eight.', 'pt': 'A banda é oito.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'I drink the stage.', 'pt': 'Eu bebo o palco.', 'ok': False, 'fb': 'Does not make sense.'}]},
  {'npc': 'Enjoy the show!', 'pt': 'Aproveite o show!', 'opts': [
   {'en': 'You are welcome.', 'pt': 'De nada.', 'ok': False, 'fb': 'Not a reply to Enjoy the show.'},
   {'en': 'You too! This show rocks!', 'pt': 'Você também! Este show é demais!', 'ok': True, 'fb': 'Happy and natural.'},
   {'en': 'Yes, I enjoy you.', 'pt': 'Sim, eu aprecio você.', 'ok': False, 'fb': 'Wrong object.'}]}]},
 'errors': [
  {'wrong': 'Where is our seats?', 'fix': 'Where are our seats?', 'alt': 'Where our seats are?', 'why': 'Seats is plural, so use are.'},
  {'wrong': 'I have my ticket in the phone.', 'fix': 'My ticket is on my phone.', 'alt': 'My ticket is at the phone.', 'why': 'Use on my phone.'},
  {'wrong': 'The band start at eight.', 'fix': 'The band starts at eight.', 'alt': 'The band is start at eight.', 'why': 'He, she and it (and the band) take -s: starts.'},
  {'wrong': 'It’s very noisy and loud here.', 'fix': 'It’s loud in here!', 'alt': 'It is loudly in here!', 'why': 'Loud is an adjective: it is loud.'}],
 'homework': 'Write 5 sentences about a concert, real or imaginary: where, who, what time and what you sing.',
 'homework_items': ['Write the name of a band you like and the time the show starts.', 'Say “Where are our seats?” 5 times with a friend.', 'Listen to the dialogue again and shadow Omar.', 'Review: Do you have your ticket? / This show rocks! / Encore!']}
