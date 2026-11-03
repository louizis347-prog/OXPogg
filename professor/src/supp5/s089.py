"""Suplemento Quest v5 · aula 89: Camping + regular A Camping Weekend (Moonrise Kingdom)."""
SUPP = {
 'reg': 83,
 'badge': {'icon': '⛺', 'name': 'Happy Camper', 'desc': 'Set up a camp: tent, campfire, flashlight and sleep'},
 'culture': {
  'hook': 'Camping is very popular in the USA. People drive to a campground, choose a flat spot for the tent, make a campfire, and look at the stars at night.',
  'mythfact': [
   {'s': 'Many US campgrounds ask you to reserve a spot, often online.', 'ans': True, 'why': 'Popular campgrounds can be full in summer, so people often book early.'},
   {'s': 'You can make a campfire anywhere in a US forest.', 'ans': False, 'why': 'Fire rules change by place and season. Use fire rings and follow the local rules.'},
   {'s': 'A flat, dry place is a good spot for a tent.', 'ans': True, 'why': 'Flat ground is more comfortable, and dry ground keeps you from getting wet.'},
   {'s': 'It is a good idea to leave food outside your tent at night.', 'ans': False, 'why': 'In many places, food is stored in a car or a special box so animals do not come to your camp.'},
   {'s': '“Moonrise Kingdom” is a 2012 film by Wes Anderson.', 'ans': True, 'why': 'It is about two young people who run away to camp near the sea.'}],
  'wild': [
   {'kind': 'Campground sign', 'lines': ['**Check-in 2 p.m.**', 'Quiet hours 10 p.m. – 7 a.m.', 'Fires only in fire rings.'], 'decode': {'q': 'Where can you make a fire?', 'opts': ['In fire rings', 'Next to the tent', 'In the trees'], 'ans': 0, 'why': '“Fires only in fire rings.”'}},
   {'kind': 'Packing list', 'lines': ['**Tent · sleeping bag**', 'Flashlight · water', 'Warm jacket'], 'decode': {'q': 'What do you need to see at night?', 'opts': ['A flashlight', 'A jacket', 'Water'], 'ans': 0, 'why': 'A flashlight gives light in the dark.'}}],
  'compare': {'br': 'In Brazil, many campgrounds are near beaches or waterfalls, and people often bring a barbecue.', 'us': 'In the USA, people often reserve a numbered spot at a campground. Rules about fire, noise and food are common, so read the signs.', 'tip': 'Ask the ranger: “Where can I put my tent?”', 'ask': 'Do you like camping? What do you bring? Say it in English.'},
  'quiz': [
   {'q': 'You want to ask where to put the tent. You say…', 'opts': ['Where should we put the tent?', 'Where we should put the tent?', 'Where put the tent?'], 'ans': 0, 'why': 'Question word + should + we + verb.'},
   {'q': 'You say what you need for the fire. You say…', 'opts': ['We need wood.', 'We are needing wood.', 'We needs wood.'], 'ans': 0, 'why': 'Need is a state verb, and we + need has no -s.'},
   {'q': 'What is a flashlight?', 'opts': ['a small light you carry', 'a kind of tent', 'a campfire'], 'ans': 0, 'why': 'You use it to see in the dark.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'A night in the woods',
  'text': [
   'Jonah and his friend Eli drive to a campground near Denver. It is Saturday afternoon. They want to sleep in the woods for one night. Jonah looks around. “**Where should we put the tent?**” he asks. “**Over there, near the trees**,” Eli says.',
   '“**Good. Is the ground flat?**” “**Yes. Let’s build a fire.**” “**We need wood**,” Jonah says. Eli walks to the pile at the camp office. “**I’ll get some.**” He comes back with six logs. Jonah puts up the tent and puts two sleeping bags inside.',
   '“**Where is the flashlight?**” Eli asks. “**It’s in my backpack**,” Jonah says. Eli finds it next to a map and a bottle of water. “**Thanks. It’s getting dark.**” The sky turns orange, then purple, and the woods become quiet.',
   'The fire is warm and bright. The friends cook sausages and talk. Eli remembers “Moonrise Kingdom,” a film from 2012 about two young campers by the sea. “Pack your bag, and let’s go camping!” he laughs. “What a view!” Jonah says.',
   'Later, the stars come out, hundreds of them. They put out the fire with water and go to the tent. “**Sleep well in the tent!**” Jonah says. “You too,” Eli answers. A little wind moves the trees, and soon both friends sleep.'],
  'glossary': [{'w': 'campground', 'pt': 'área de camping'}, {'w': 'tent', 'pt': 'barraca'}, {'w': 'flat', 'pt': 'plano'}, {'w': 'fire', 'pt': 'fogueira'}, {'w': 'logs', 'pt': 'toras de lenha'}, {'w': 'sleeping bags', 'pt': 'sacos de dormir'}, {'w': 'flashlight', 'pt': 'lanterna'}, {'w': 'backpack', 'pt': 'mochila'}, {'w': 'sausages', 'pt': 'salsichas'}, {'w': 'stars', 'pt': 'estrelas'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Two friends camp for a night', 'A girl goes to a museum', 'A man rents a car'], 'ans': 0, 'why': 'Jonah and Eli put up a tent and sleep in the woods.'},
  'scan': [{'q': 'Where do they put the tent?', 'ans': 'near the trees', 'alt': ['over there, near the trees', 'trees']}, {'q': 'What does Jonah need for the fire?', 'ans': 'wood', 'alt': ['we need wood', 'logs']}, {'q': 'Where is the flashlight?', 'ans': 'in Jonah’s backpack', 'alt': ['in his backpack', 'backpack', 'in the backpack']}],
  'tf': [{'s': 'The ground is flat.', 'ans': True, 'why': 'Eli says, “Yes.”'}, {'s': 'Eli gets the wood.', 'ans': True, 'why': 'He says, “I’ll get some.”'}, {'s': 'The flashlight is in Eli’s bag.', 'ans': False, 'why': 'It is in Jonah’s backpack.'}, {'s': 'The friends sleep in a hotel.', 'ans': False, 'why': 'They sleep in a tent.'}],
  'order': ['The friends choose a place for the tent.', 'Eli gets wood.', 'They find the flashlight.', 'They cook by the fire.', 'They put out the fire and sleep.'],
  'ctx': [{'sent': 'Is the ground flat?', 'w': 'flat', 'opts': ['not hilly', 'very hot', 'very wet'], 'ans': 0, 'why': 'Flat = plano.'}, {'sent': 'Eli puts the fire out with water.', 'w': 'puts the fire out', 'opts': ['stops the fire', 'starts the fire', 'looks at the fire'], 'ans': 0, 'why': 'Put out = apagar.'}, {'sent': 'They sleep in sleeping bags.', 'w': 'sleeping bags', 'opts': ['warm bags for sleeping', 'bags for food', 'bags for water'], 'ans': 0, 'why': 'A sleeping bag is a warm bed bag.'}],
  'chunkHunt': ['Where should we put the tent?', 'Let’s build a fire.', 'We need wood.', 'It’s getting dark.'],
  'think': 'Do you want to camp in the woods? What do you bring?'},
 'convo': {'npc': {'name': 'Jonah'}, 'story': 'You are at a campground with your friend Jonah. Answer him.', 'turns': [
  {'npc': 'Where should we put the tent?', 'pt': 'Onde devemos montar a barraca?', 'opts': [
   {'en': 'Over there, near the trees.', 'pt': 'Ali, perto das árvores.', 'ok': True, 'fb': 'Gives a place.'},
   {'en': 'We should put it yes.', 'pt': 'Devemos pôr sim.', 'ok': False, 'fb': 'It does not answer where.'},
   {'en': 'Is a big tent.', 'pt': 'É uma barraca grande.', 'ok': False, 'fb': 'He asks where, not what.'}]},
  {'npc': 'Good. Is the ground flat?', 'pt': 'Bom. O chão é plano?', 'opts': [
   {'en': 'The ground is flat yes.', 'pt': 'O chão é plano sim.', 'ok': False, 'fb': 'Short answer: Yes, it is.'},
   {'en': 'Yes. Let’s build a fire.', 'pt': 'Sim. Vamos fazer uma fogueira.', 'ok': True, 'fb': 'Answers and suggests the next step.'},
   {'en': 'No, I am flat.', 'pt': 'Não, eu sou plano.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'We need wood.', 'pt': 'Precisamos de lenha.', 'opts': [
   {'en': 'I’ll get some. Where is the flashlight?', 'pt': 'Eu pego. Onde está a lanterna?', 'ok': True, 'fb': 'Offers help and asks.'},
   {'en': 'I am needing wood.', 'pt': 'Estou precisando de lenha.', 'ok': False, 'fb': 'Need has no -ing.'},
   {'en': 'We need wood too.', 'pt': 'Nós também precisamos de lenha.', 'ok': False, 'fb': 'It repeats and does not help.'}]},
  {'npc': 'It’s in my backpack.', 'pt': 'Está na minha mochila.', 'opts': [
   {'en': 'Thanks. It’s getting dark.', 'pt': 'Valeu. Está escurecendo.', 'ok': True, 'fb': 'Natural reason for the flashlight.'},
   {'en': 'Thanks. It is dark getting.', 'pt': 'Valeu. Está escurecendo (ordem errada).', 'ok': False, 'fb': 'Word order: It’s getting dark.'},
   {'en': 'The backpack is wood.', 'pt': 'A mochila é lenha.', 'ok': False, 'fb': 'Does not fit.'}]},
  {'npc': 'Sleep well in the tent!', 'pt': 'Durma bem na barraca!', 'opts': [
   {'en': 'I sleep well in tent.', 'pt': 'Eu durmo bem em barraca.', 'ok': False, 'fb': 'Wrong grammar.'},
   {'en': 'Thanks! You too!', 'pt': 'Obrigado! Você também!', 'ok': True, 'fb': 'Natural reply.'},
   {'en': 'Welcome to the tent!', 'pt': 'Bem-vindo à barraca!', 'ok': False, 'fb': 'Wrong moment.'}]}]},
 'errors': [
  {'wrong': 'Where we should put the tent?', 'fix': 'Where should we put the tent?', 'alt': 'Where should put we the tent?', 'why': 'In questions, should comes before we.'},
  {'wrong': 'We are needing wood.', 'fix': 'We need wood.', 'alt': 'We needs wood.', 'why': 'Need is a state verb: no -ing.'},
  {'wrong': 'It’s in the my backpack.', 'fix': 'It’s in my backpack.', 'alt': 'It’s on my backpack.', 'why': 'Do not use the with my.'},
  {'wrong': 'It’s getting dark?', 'fix': 'It’s getting dark.', 'alt': 'It’s get dark.', 'why': 'Say it as a statement: It’s getting dark.'}],
 'homework': 'Write a short dialogue: two friends put up a tent, make a fire and look for a flashlight.',
 'homework_items': ['Write 5 things you take camping.', 'Say aloud: Where should we put the tent?', 'Listen to the dialogue and shadow Jonah.', 'Review: Pack your bag / Let’s go camping!']}
