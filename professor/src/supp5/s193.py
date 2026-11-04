"""Suplemento Quest v5 · aula 193: May I borrow a ladder? + regular No worries! No problem! (The Lion King)."""
SUPP = {
 'reg': 227,
 'badge': {'icon': '🪜', 'name': 'Good Neighbor', 'desc': 'Borrow something politely from a neighbor'},
 'culture': {
  'hook': 'In the USA, neighbors often lend each other small things like a ladder or a tool. People ask politely, say what they need it for and bring it back soon.',
  'mythfact': [
   {'s': 'It is normal to ask a neighbor to borrow a simple tool.', 'ans': True, 'why': 'Many neighbors are happy to help if you ask politely.'},
   {'s': '“Could I borrow…?” is a polite way to ask.', 'ans': True, 'why': 'Could is softer than Can.'},
   {'s': 'You can keep a borrowed item for months and say nothing.', 'ans': False, 'why': 'You should bring it back soon and say thanks.'},
   {'s': '“No worries” can mean “it is not a problem.”', 'ans': True, 'why': 'People say it to calm someone.'},
   {'s': '“The Lion King” is a Disney film from 1994.', 'ans': True, 'why': 'It was directed by Roger Allers and Rob Minkoff.'}],
  'wild': [
   {'kind': 'Note on a door', 'lines': ['**Hi neighbor!**', 'May I borrow your hammer?', 'I will bring it back tonight.', '— Sam, Apt 4'], 'decode': {'q': 'What does Sam want to borrow?', 'opts': ['A hammer', 'A ladder', 'A bike'], 'ans': 0, 'why': 'The note says “May I borrow your hammer?”'}},
   {'kind': 'Garage sign', 'lines': ['**TOOLS FOR LOAN**', 'Ask before you take', 'Return in two days'], 'decode': {'q': 'When should you return the tools?', 'opts': ['In two days', 'Never', 'In two months'], 'ans': 0, 'why': 'The sign says “Return in two days.”'}}],
  'compare': {'br': 'In Brazil, many neighbors also lend things, often with a simple “Me empresta?” and a friendly chat.', 'us': 'In the USA, people often add a polite phrase: “Do you have a minute?” or “Could I borrow…?” and say when they will return it.', 'tip': 'Say: “Could I borrow your ladder? I’ll bring it back soon.”', 'ask': 'What do you borrow from a neighbor? Say it in English.'},
  'quiz': [
   {'q': 'You want to ask a neighbor for a favor. You say…', 'opts': ['Do you have a minute?', 'Do you have time to minute?', 'Have you a minute?'], 'ans': 0, 'why': 'Do you have a minute? is a common opener.'},
   {'q': 'You want to use a ladder for a short time. You say…', 'opts': ['Could I borrow your ladder?', 'Could I borrowing your ladder?', 'Could I lend your ladder?'], 'ans': 0, 'why': 'You borrow from someone, and the other person lends.'},
   {'q': 'You promise to return it. You say…', 'opts': ['I’ll bring it back soon.', 'I will back it soon.', 'I bring back it soon.'], 'ans': 0, 'why': 'Bring it back is the usual phrase.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'No worries, neighbor',
  'text': ['Sam lives in an apartment building in Chicago. One light bulb in the hallway is broken. The ceiling is high, and Sam has no ladder. He thinks of his neighbor, Jordan. Jordan lives next door and has many tools.', 'Sam knocks on the door. “**Hi, Jordan! Do you have a minute?**” “**Sure. What do you need?**” “**Could I borrow your ladder?**” “**Of course. What for?**”', '“**I need to change a light bulb.**” “**Is it high?**” “**Yes, in the hallway.**” “**The ladder is in the garage.**” Sam is a little worried about the noise at night. “**No worries!**” Jordan says. “**No problem.**”', 'Jordan hums a song from “The Lion King.” It is a Disney film from 1994. In the song, “Hakuna Matata” means “no worries.” Sam laughs and takes the ladder. He climbs up with a new bulb and changes it in two minutes.', 'Now the hallway is bright again. Sam carries the ladder back to the garage. “**Thank you. I’ll bring it back soon**,” he says, and he gives Jordan a box of cookies. Jordan smiles. “Anytime!”'],
  'glossary': [{'w': 'light bulb', 'pt': 'lâmpada'}, {'w': 'hallway', 'pt': 'corredor'}, {'w': 'ceiling', 'pt': 'teto'}, {'w': 'ladder', 'pt': 'escada'}, {'w': 'garage', 'pt': 'garagem'}, {'w': 'knocks', 'pt': 'bate'}, {'w': 'climbs', 'pt': 'sobe'}, {'w': 'bright', 'pt': 'claro'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A man borrows a ladder from a neighbor', 'A man buys a new house', 'A man paints a wall'], 'ans': 0, 'why': 'Sam needs a ladder to change a bulb.'},
  'scan': [{'q': 'What is broken?', 'ans': 'a light bulb', 'alt': ['the light bulb', 'bulb', 'one light bulb']}, {'q': 'Where is the ladder?', 'ans': 'in the garage', 'alt': ['garage', 'the garage']}, {'q': 'What does Sam give Jordan?', 'ans': 'a box of cookies', 'alt': ['cookies', 'box of cookies']}],
  'tf': [{'s': 'Sam has a ladder.', 'ans': False, 'why': 'He has no ladder.'}, {'s': 'The light is in the hallway.', 'ans': True, 'why': 'The bulb is in the hallway.'}, {'s': 'Jordan says no.', 'ans': False, 'why': 'Jordan says, “Of course.”'}, {'s': 'Sam returns the ladder.', 'ans': True, 'why': 'He carries it back to the garage.'}],
  'order': ['Sam sees a broken light bulb.', 'Sam knocks on Jordan’s door.', 'Sam asks to borrow a ladder.', 'Sam changes the bulb.', 'Sam returns the ladder with cookies.'],
  'ctx': [{'sent': 'Sam knocks on the door.', 'w': 'knocks', 'opts': ['hits the door softly', 'opens the window', 'paints the door'], 'ans': 0, 'why': 'You knock to say you are there.'}, {'sent': 'He climbs up with a new bulb.', 'w': 'climbs', 'opts': ['goes up', 'goes down', 'goes home'], 'ans': 0, 'why': 'Climb means go up.'}, {'sent': 'Now the hallway is bright again.', 'w': 'bright', 'opts': ['full of light', 'very dark', 'very cold'], 'ans': 0, 'why': 'Bright means full of light.'}],
  'chunkHunt': ['Do you have a minute?', 'Could I borrow your ladder?', 'I’ll bring it back soon.', 'No worries!'],
  'think': 'What do you borrow from other people? What do you say when you ask?'},
 'convo': {'npc': {'name': 'Jordan'}, 'story': 'You need a ladder. You ask your neighbor Jordan for help.', 'turns': [
  {'npc': 'Hi! What’s up?', 'pt': 'Oi! E aí?', 'opts': [
   {'en': 'Hi! Do you have a minute?', 'pt': 'Oi! Tem um minutinho?', 'ok': True, 'fb': 'A polite opener before a favor.'},
   {'en': 'Hi! I have a minute.', 'pt': 'Oi! Eu tenho um minuto.', 'ok': False, 'fb': 'It changes who has time.'},
   {'en': 'Goodbye, see you!', 'pt': 'Tchau, até logo!', 'ok': False, 'fb': 'It does not fit the start.'}]},
  {'npc': 'Sure. What do you need?', 'pt': 'Claro. Do que precisa?', 'opts': [
   {'en': 'Could I lend your ladder?', 'pt': 'Posso emprestar sua escada?', 'ok': False, 'fb': 'You borrow from him; he lends.'},
   {'en': 'Could I borrow your ladder?', 'pt': 'Posso pegar sua escada emprestada?', 'ok': True, 'fb': 'Polite request with borrow.'},
   {'en': 'I am a ladder.', 'pt': 'Eu sou uma escada.', 'ok': False, 'fb': 'It does not make sense.'}]},
  {'npc': 'Of course. What for?', 'pt': 'Claro. Para quê?', 'opts': [
   {'en': 'For a ladder.', 'pt': 'Para uma escada.', 'ok': False, 'fb': 'He asks about the reason.'},
   {'en': 'I need change a light bulb.', 'pt': 'Preciso trocar uma lâmpada.', 'ok': False, 'fb': 'After need, use to: I need to change.'},
   {'en': 'I need to change a light bulb.', 'pt': 'Preciso trocar uma lâmpada.', 'ok': True, 'fb': 'Gives the reason.'}]},
  {'npc': 'Is it high?', 'pt': 'É alto?', 'opts': [
   {'en': 'Yes, in the hallway.', 'pt': 'Sim, no corredor.', 'ok': True, 'fb': 'Answers yes and gives the place.'},
   {'en': 'Yes, I am high.', 'pt': 'Sim, eu estou alto.', 'ok': False, 'fb': 'It says something different.'},
   {'en': 'No, thank you.', 'pt': 'Não, obrigado.', 'ok': False, 'fb': 'It does not answer the place.'}]},
  {'npc': 'The ladder is in the garage.', 'pt': 'A escada está na garagem.', 'opts': [
   {'en': 'Thank you. I’ll bring it back soon.', 'pt': 'Obrigado. Devolvo logo.', 'ok': True, 'fb': 'Thanks and a promise.'},
   {'en': 'Thank you. I keep it.', 'pt': 'Obrigado. Eu fico com ela.', 'ok': False, 'fb': 'It is not polite for a loan.'},
   {'en': 'What for?', 'pt': 'Para quê?', 'ok': False, 'fb': 'Jordan already asked this.'}]}]},
 'errors': [
  {'wrong': 'Could I lend your ladder?', 'fix': 'Could I borrow your ladder?', 'alt': 'Could I borrowing your ladder?', 'why': 'Borrow is to take for a short time; lend is to give.'},
  {'wrong': 'I need change a light bulb.', 'fix': 'I need to change a light bulb.', 'alt': 'I need changing a light bulb.', 'why': 'After need, use to + verb.'},
  {'wrong': 'I bring back it soon.', 'fix': 'I’ll bring it back soon.', 'alt': 'I will back it soon.', 'why': 'Use I’ll for a promise, and it goes between bring and back.'},
  {'wrong': 'Have you a minute?', 'fix': 'Do you have a minute?', 'alt': 'Do you have minute?', 'why': 'Use do you have, and a before minute.'}],
 'homework': 'Write a short note to a neighbor: ask to borrow a tool and say when you will bring it back.',
 'homework_items': ['Write three things you can borrow.', 'Say aloud: Could I borrow your ladder?', 'Listen to the dialogue and shadow Jordan.', 'Review: ladder / bulb / tool / nail.']}
