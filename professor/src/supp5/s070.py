"""Suplemento Quest v5 · aula 70: Chores at home + regular Do Homework, Do the Dishes (Phineas and Ferb)."""
SUPP = {
 'reg': 62,
 'badge': {'icon': '🧹', 'name': 'Chore Champion', 'desc': 'Share chores: ask whose turn it is, offer and ask for help'},
 'culture': {
  'hook': 'Sharing a home means sharing chores. A few short sentences help you decide whose turn it is, offer to do something and ask a friend for help.',
  'mythfact': [
   {'s': 'Boston is the capital of Massachusetts.', 'ans': True, 'why': 'Boston is the capital and biggest city of Massachusetts.'},
   {'s': '“Take out the trash” means to carry the garbage outside.', 'ans': True, 'why': 'You take the bag to the bin or the trash room.'},
   {'s': 'Many roommates in the USA make a list or chart of chores.', 'ans': True, 'why': 'It is a simple way to share the work.'},
   {'s': 'Trash day is the same day in every US city.', 'ans': False, 'why': 'Each city or building has its own schedule.'},
   {'s': 'A broom and a vacuum cleaner are the same machine.', 'ans': False, 'why': 'A broom is a stick with bristles; a vacuum cleaner is an electric machine.'}],
  'wild': [
   {'kind': 'Chore chart', 'lines': ['**MON** Dishes — Finn', '**TUE** Trash — Grace', '**WED** Vacuum — Finn'], 'decode': {'q': 'Who takes out the trash on Tuesday?', 'opts': ['Grace', 'Finn', 'Nobody'], 'ans': 0, 'why': '“TUE Trash — Grace.”'}},
   {'kind': 'Note on the fridge', 'lines': ['**Please wash your dishes.**', 'Do not leave them in the sink!', 'Thanks! — Grace'], 'decode': {'q': 'What does Grace want?', 'opts': ['Clean dishes', 'More trash', 'A new sink'], 'ans': 0, 'why': 'She asks people to wash their dishes.'}}],
  'compare': {'br': 'In Brazil, many families have someone help with the cleaning, and chores are often shared by the family.', 'us': 'In the USA, roommates and families often share chores with a chart, and people say “It\'s my turn” or “Whose turn is it?”.', 'tip': 'Offer first: “I\'ll do it now.” Then ask politely: “Can you…?”', 'ask': 'What chores do you do at home? Say two in English.'},
  'quiz': [
   {'q': 'You want to know who washes the dishes. You ask…', 'opts': ['Whose turn is it to wash the dishes?', 'Who is dishes today?', 'What turn the dishes wash?'], 'ans': 0, 'why': 'Whose turn is it to…? is the natural way.'},
   {'q': 'It is your turn. You say…', 'opts': ['It\'s mine. I\'ll do it now.', 'It is me turn.', 'I turn yesterday.'], 'ans': 0, 'why': 'It\'s mine = it is my turn.'},
   {'q': 'You ask your friend to help with the floor. You say…', 'opts': ['Can you vacuum the living room?', 'You vacuum is the room?', 'Vacuum you can living?'], 'ans': 0, 'why': 'Can you…? is a polite request.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Saturday chores',
  'text': [
   'Saturday morning in **Boston**. Grace and her roommate Finn share an apartment. The kitchen is messy and the floor is dirty. “Ugh, **chores**,” says Grace. “**Let\'s knock them out**,” says Finn.',
   '“**Whose turn is it to wash the dishes?**” Grace asks. “**It\'s mine. I\'ll do it now**,” Finn says. “**Thanks. I\'ll take out the trash**,” says Grace. She takes the bag outside to the bins.',
   'Finn washes plates, cups and pans with a sponge and hot water. “**Can you clean the kitchen too?**” he asks. “**Sure. Can you vacuum the living room?**” “**Yes, after lunch.**” Grace wipes the table and sweeps the floor with a broom.',
   'After lunch, Finn vacuums the rug. It is noisy, but the room looks nice. “**We make a great team**,” says Grace. Soon every chore is done. “**Thanks for helping out!**” she says.',
   'Finn thinks of the cartoon Phineas and Ferb. The brothers build big projects, but they also have chores, like doing the dishes. Even big inventors help at home! Finn puts on music. “**Then let\'s watch a movie**,” he says. “Done!”'],
  'glossary': [{'w': 'chores', 'pt': 'tarefas domésticas'}, {'w': 'roommate', 'pt': 'colega de apartamento'}, {'w': 'messy', 'pt': 'bagunçado'}, {'w': 'sponge', 'pt': 'esponja'}, {'w': 'wipes', 'pt': 'limpa com pano'}, {'w': 'sweeps', 'pt': 'varre'}, {'w': 'broom', 'pt': 'vassoura'}, {'w': 'rug', 'pt': 'tapete'}, {'w': 'noisy', 'pt': 'barulhento'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Two roommates doing chores', 'A trip to Boston', 'A new apartment'], 'ans': 0, 'why': 'Grace and Finn clean their apartment.'},
  'scan': [{'q': 'Who washes the dishes?', 'ans': 'Finn', 'alt': ['finn']}, {'q': 'Who takes out the trash?', 'ans': 'Grace', 'alt': ['grace']}, {'q': 'When does Finn vacuum?', 'ans': 'after lunch', 'alt': ['after the lunch']}],
  'tf': [{'s': 'The kitchen is clean at the start.', 'ans': False, 'why': 'The kitchen is messy.'}, {'s': 'Grace takes out the trash.', 'ans': True, 'why': '“I\'ll take out the trash.”'}, {'s': 'Finn vacuums before lunch.', 'ans': False, 'why': 'He vacuums after lunch.'}, {'s': 'They watch a movie at the end.', 'ans': True, 'why': 'Finn says, “Then let\'s watch a movie.”'}],
  'order': ['Grace and Finn see a messy kitchen.', 'Finn washes the dishes.', 'Grace takes out the trash.', 'Finn vacuums the rug after lunch.', 'They plan to watch a movie.'],
  'ctx': [{'sent': 'The kitchen is messy.', 'w': 'messy', 'opts': ['not tidy', 'very big', 'very cold'], 'ans': 0, 'why': 'Messy = not clean or tidy.'}, {'sent': 'Grace sweeps the floor with a broom.', 'w': 'sweeps', 'opts': ['cleans the floor with a broom', 'paints the floor', 'sits on the floor'], 'ans': 0, 'why': 'Sweep = clean with a broom.'}, {'sent': 'The vacuum is noisy.', 'w': 'noisy', 'opts': ['loud', 'quiet', 'new'], 'ans': 0, 'why': 'Noisy = makes a lot of noise.'}],
  'chunkHunt': ['Whose turn is it?', 'It\'s mine. I\'ll do it now.', 'Can you vacuum the living room?', 'We make a great team.'],
  'think': 'Which chore do you like? Which chore do you not like?'},
 'convo': {'npc': {'name': 'Grace'}, 'story': 'You share an apartment in Boston with Grace. It is Saturday and the apartment is messy. Share the chores.', 'turns': [
  {'npc': 'Whose turn is it to wash the dishes?', 'pt': 'De quem é a vez de lavar a louça?', 'opts': [
   {'en': 'It\'s mine. I\'ll do it now.', 'pt': 'É a minha. Faço agora.', 'ok': True, 'fb': 'Says it is your turn and offers.'},
   {'en': 'It is me.', 'pt': 'É eu.', 'ok': False, 'fb': 'Use mine for my turn.'},
   {'en': 'The dishes are Monday.', 'pt': 'A louça é segunda.', 'ok': False, 'fb': 'It does not answer.'}]},
  {'npc': 'Thanks. I\'ll take out the trash.', 'pt': 'Valeu. Eu levo o lixo.', 'opts': [
   {'en': 'You are welcome yesterday.', 'pt': 'De nada ontem.', 'ok': False, 'fb': 'Yesterday does not fit.'},
   {'en': 'Can you clean the kitchen too?', 'pt': 'Pode limpar a cozinha também?', 'ok': True, 'fb': 'A polite request.'},
   {'en': 'Can you clean too the kitchen?', 'pt': 'Pode limpar também a cozinha?', 'ok': False, 'fb': 'Put too at the end.'}]},
  {'npc': 'Sure. Can you vacuum the living room?', 'pt': 'Claro. Pode passar aspirador na sala?', 'opts': [
   {'en': 'Yes, after lunch.', 'pt': 'Sim, depois do almoço.', 'ok': True, 'fb': 'Says when you will do it.'},
   {'en': 'Yes, before yesterday.', 'pt': 'Sim, antes de ontem.', 'ok': False, 'fb': 'Time does not make sense.'},
   {'en': 'The room is a vacuum.', 'pt': 'A sala é um aspirador.', 'ok': False, 'fb': 'Mixes the words.'}]},
  {'npc': 'We make a great team.', 'pt': 'Formamos um ótimo time.', 'opts': [
   {'en': 'I make you a team.', 'pt': 'Eu faço você um time.', 'ok': False, 'fb': 'Does not fit.'},
   {'en': 'Yes! Then let\'s watch a movie.', 'pt': 'Sim! Depois vamos ver um filme.', 'ok': True, 'fb': 'Agrees and plans something fun.'},
   {'en': 'No team, thank you.', 'pt': 'Time não, obrigado.', 'ok': False, 'fb': 'Unfriendly and unclear.'}]},
  {'npc': 'Thanks for helping out!', 'pt': 'Valeu pela ajuda!', 'opts': [
   {'en': 'Anytime! See you later.', 'pt': 'Quando quiser! Até logo.', 'ok': True, 'fb': 'A friendly answer.'},
   {'en': 'I help out the trash.', 'pt': 'Eu ajudo fora o lixo.', 'ok': False, 'fb': 'Does not make sense.'},
   {'en': 'No help, thanks.', 'pt': 'Sem ajuda, valeu.', 'ok': False, 'fb': 'Does not answer her thanks.'}]}]},
 'errors': [
  {'wrong': 'Who turn is it?', 'fix': 'Whose turn is it?', 'alt': 'Who\'s turn is it?', 'why': 'Whose is for ownership: whose turn. Who\'s means who is.'},
  {'wrong': 'It\'s my. I do it now.', 'fix': 'It\'s mine. I\'ll do it now.', 'alt': 'It\'s me. I\'ll do it now.', 'why': 'After is, use mine, not my. I\'ll = I will for a quick decision.'},
  {'wrong': 'I go to take out the trash.', 'fix': 'I\'ll take out the trash.', 'alt': 'I take out the trash now.', 'why': 'I\'ll + verb is the natural way to offer to do something.'},
  {'wrong': 'Can you clean the kitchen to?', 'fix': 'Can you clean the kitchen too?', 'alt': 'Can you clean the kitchen two?', 'why': 'Too = também. To and two are different words.'}],
 'homework': 'Make a chore list for a week: 5 days, 5 chores, 2 names. Use “It\'s … turn.”',
 'homework_items': ['Say 5 chores you do at home.', 'Write: Whose turn is it to…? and It\'s mine.', 'Listen to the dialogue again and shadow Grace.', 'Review: I\'ll do it now. / Can you…? / We make a great team.']}
