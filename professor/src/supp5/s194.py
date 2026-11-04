"""Suplemento Quest v5 · aula 194: Snow day + regular A runny nose (The Snow Queen)."""
SUPP = {
 'reg': 159,
 'badge': {'icon': '⛄', 'name': 'Snow Day Pro', 'desc': 'Get ready and play at home on a snow day'},
 'culture': {
  'hook': 'On a snow day, children in some parts of the USA stay home from school and play in the snow. Families get ready with warm clothes and hot drinks.',
  'mythfact': [
   {'s': 'In some places in the USA, schools close when there is a lot of snow.', 'ans': True, 'why': 'This is called a snow day.'},
   {'s': 'People wear shorts to play in snow.', 'ans': False, 'why': 'They usually wear a coat, a hat, gloves and boots.'},
   {'s': 'Many families make a snowman on a snow day.', 'ans': True, 'why': 'It is a classic winter game.'},
   {'s': 'On a snow day, the snow always melts in one hour.', 'ans': False, 'why': 'It often stays for days if it is cold.'},
   {'s': '“The Snow Queen” is a fairy tale by Hans Christian Andersen.', 'ans': True, 'why': 'It is from 1844.'}],
  'wild': [
   {'kind': 'School message', 'lines': ['**SNOW DAY**', 'All schools are closed on Tuesday.', 'Stay safe and warm!'], 'decode': {'q': 'When are schools closed?', 'opts': ['On Tuesday', 'On Friday', 'Every day'], 'ans': 0, 'why': 'The message says “closed on Tuesday.”'}},
   {'kind': 'Note on the door', 'lines': ['**Boots by the door**', 'Hats and gloves in the basket', 'Wet coats on the hooks'], 'decode': {'q': 'Where do the boots go?', 'opts': ['By the door', 'In the basket', 'On the hooks'], 'ans': 0, 'why': 'The note says “Boots by the door.”'}}],
  'compare': {'br': 'In most of Brazil there is no snow, so many people see snow only on trips or on TV, and the cold in the south is a different kind of winter.', 'us': 'In the northern USA, snow is a normal part of winter, and families keep boots, gloves and shovels near the door.', 'tip': 'Say: “It’s a snow day! Let’s build a snowman.”', 'ask': 'What do you wear when it is very cold? Say it in English.'},
  'quiz': [
   {'q': 'You look out and see snow. You say…', 'opts': ['It snowed all night.', 'It snow all night.', 'It is snowed all night.'], 'ans': 0, 'why': 'Use the past for last night: snowed.'},
   {'q': 'You want to ask where your gloves are. You say…', 'opts': ['Where are my gloves?', 'Where is my gloves?', 'Where my gloves are?'], 'ans': 0, 'why': 'Gloves is plural: Where are…?'},
   {'q': 'You suggest a game. You say…', 'opts': ['Let’s build a snowman.', 'Let’s building a snowman.', 'Let’s to build a snowman.'], 'ans': 0, 'why': 'After Let’s, use the base verb.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'A cozy snow day',
  'text': ['Lily wakes up and the house is very quiet. She looks out the window and sees white everywhere. “**Look outside! It snowed all night**,” her mom says. “**Is school closed today?**” Lily asks. “**Yes, it’s a snow day!**”', 'First, the family has breakfast in the warm kitchen. Dad turns on the radio, and the news says, “About ten inches of snow.” Lily says, “**Wow! How much snow is there?**” Her little brother asks, “**Can we build a snowman?**”', '“**First, put on your coat and boots**,” Mom says. Lily looks at the door. “**Where are my gloves?**” “**They’re by the door.**” They also take a hat, a scarf and a small shovel.', 'Outside, it is very cold and the street is icy. The children roll big snowballs and build a snowman. Then they slide down a small hill on a sled. The story “The Snow Queen” is about a cold queen with a house of ice. It is a fairy tale by Hans Christian Andersen from 1844.', 'After an hour, their hands are freezing. They go inside and take off their wet boots. Mom makes hot tea and the house is cozy. Lily puts her gloves by the heater. Tomorrow the snow may melt, but today is a perfect snow day.'],
  'glossary': [{'w': 'snow day', 'pt': 'dia de neve'}, {'w': 'closed', 'pt': 'fechada'}, {'w': 'snowman', 'pt': 'boneco de neve'}, {'w': 'gloves', 'pt': 'luvas'}, {'w': 'icy', 'pt': 'com gelo'}, {'w': 'sled', 'pt': 'trenó'}, {'w': 'freezing', 'pt': 'congelando'}, {'w': 'cozy', 'pt': 'aconchegante'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A family has fun on a snow day', 'A family goes to school', 'A family cooks lunch'], 'ans': 0, 'why': 'School is closed and they play in the snow.'},
  'scan': [{'q': 'How much snow is there?', 'ans': 'about ten inches', 'alt': ['ten inches', '10 inches']}, {'q': 'Where are Lily’s gloves?', 'ans': 'by the door', 'alt': ['near the door', 'at the door']}, {'q': 'What do the children ride down the hill?', 'ans': 'a sled', 'alt': ['sled', 'a small sled']}],
  'tf': [{'s': 'School is open today.', 'ans': False, 'why': 'It is a snow day, so school is closed.'}, {'s': 'The family has breakfast first.', 'ans': True, 'why': 'They eat in the kitchen.'}, {'s': 'The children build a snowman.', 'ans': True, 'why': 'They roll big snowballs.'}, {'s': 'They stay outside all day.', 'ans': False, 'why': 'After an hour, they go inside.'}],
  'order': ['Lily sees the snow from the window.', 'The family has breakfast.', 'Lily puts on her coat and boots.', 'The children build a snowman and use a sled.', 'They go inside for hot tea.'],
  'ctx': [{'sent': 'The street is icy.', 'w': 'icy', 'opts': ['covered with ice', 'very hot', 'very dark'], 'ans': 0, 'why': 'Icy means covered with ice.'}, {'sent': 'Their hands are freezing.', 'w': 'freezing', 'opts': ['very cold', 'very clean', 'very big'], 'ans': 0, 'why': 'Freezing means very cold.'}, {'sent': 'The house is cozy.', 'w': 'cozy', 'opts': ['warm and comfortable', 'cold and empty', 'loud and busy'], 'ans': 0, 'why': 'Cozy means warm and comfortable.'}],
  'chunkHunt': ['Look outside!', 'Is school closed today?', 'Let’s build a snowman.', 'Where are my gloves?'],
  'think': 'What do you do when it is very cold? What do you wear?'},
 'convo': {'npc': {'name': 'Sabrina'}, 'story': 'You wake up and see a lot of snow. Sabrina is at home with you and talks about the snow day.', 'turns': [
  {'npc': 'Look outside! It snowed all night.', 'pt': 'Olha lá fora! Nevou a noite toda.', 'opts': [
   {'en': 'Wow! How much snow is there?', 'pt': 'Nossa! Quanta neve tem?', 'ok': True, 'fb': 'A natural reaction and question.'},
   {'en': 'Wow! How many snow is there?', 'pt': 'Nossa! Quantas neve tem?', 'ok': False, 'fb': 'Snow is uncountable: how much.'},
   {'en': 'I am hot today.', 'pt': 'Estou com calor hoje.', 'ok': False, 'fb': 'It does not fit the snowy scene.'}]},
  {'npc': 'About ten inches.', 'pt': 'Uns vinte e cinco centímetros.', 'opts': [
   {'en': 'Is school closed today?', 'pt': 'A escola está fechada hoje?', 'ok': True, 'fb': 'A natural question after heavy snow.'},
   {'en': 'School is closing me.', 'pt': 'A escola está me fechando.', 'ok': False, 'fb': 'It changes the meaning.'},
   {'en': 'It is ten snow.', 'pt': 'São dez neve.', 'ok': False, 'fb': 'It does not make sense.'}]},
  {'npc': 'Yes, it’s a snow day!', 'pt': 'Sim, é dia de neve!', 'opts': [
   {'en': 'Great! Let’s building a snowman.', 'pt': 'Ótimo! Vamos fazendo um boneco de neve.', 'ok': False, 'fb': 'After Let’s, use the base verb.'},
   {'en': 'Great! Let’s build a snowman.', 'pt': 'Ótimo! Vamos fazer um boneco de neve.', 'ok': True, 'fb': 'Let’s + base verb suggests an idea.'},
   {'en': 'Great! I go to school.', 'pt': 'Ótimo! Eu vou para a escola.', 'ok': False, 'fb': 'There is no school today.'}]},
  {'npc': 'First, put on your coat and boots.', 'pt': 'Primeiro, ponha casaco e botas.', 'opts': [
   {'en': 'Where is my gloves?', 'pt': 'Onde está minhas luvas?', 'ok': False, 'fb': 'Gloves is plural: are.'},
   {'en': 'I put on the snow.', 'pt': 'Eu coloco a neve.', 'ok': False, 'fb': 'It does not fit the request.'},
   {'en': 'Where are my gloves?', 'pt': 'Onde estão minhas luvas?', 'ok': True, 'fb': 'Asks for the missing item.'}]},
  {'npc': 'They’re by the door.', 'pt': 'Estão perto da porta.', 'opts': [
   {'en': 'Thanks! I am ready.', 'pt': 'Valeu! Estou pronto.', 'ok': True, 'fb': 'A short thanks and a status.'},
   {'en': 'Thanks! Where is my gloves?', 'pt': 'Valeu! Onde está minhas luvas?', 'ok': False, 'fb': 'You already know: they are by the door.'},
   {'en': 'No, they are not gloves.', 'pt': 'Não, elas não são luvas.', 'ok': False, 'fb': 'It is rude and wrong.'}]}]},
 'errors': [
  {'wrong': 'It snow all night.', 'fix': 'It snowed all night.', 'alt': 'It is snowed all night.', 'why': 'For last night, use the past: snowed.'},
  {'wrong': 'How many snow is there?', 'fix': 'How much snow is there?', 'alt': 'How many snows is there?', 'why': 'Snow is uncountable: use how much.'},
  {'wrong': 'Where is my gloves?', 'fix': 'Where are my gloves?', 'alt': 'Where are my glove?', 'why': 'Gloves is plural, so use are.'},
  {'wrong': 'Let’s to build a snowman.', 'fix': 'Let’s build a snowman.', 'alt': 'Let’s building a snowman.', 'why': 'After Let’s, use only the base verb.'}],
 'homework': 'Write a short routine for a snow day at home: breakfast, clothes, play and a hot drink.',
 'homework_items': ['Write five things you wear in the snow.', 'Say aloud: Where are my gloves?', 'Listen to the dialogue and shadow Sabrina.', 'Review: snowman / sled / coat / cozy.']}
