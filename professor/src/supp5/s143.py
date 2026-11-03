"""Suplemento Quest v5 · aula 143: Foggy city (San Francisco) + regular I'm Cold and Sleepy (Twinkle, Twinkle, Little Star)."""
SUPP = {
 'reg': 41,
 'badge': {'icon': '🌉', 'name': 'Fog Walker', 'desc': 'Talk about fog, cold weather and the cable car'},
 'culture': {
  'hook': 'San Francisco is a city of hills, a red bridge and a lot of fog. Even in summer, mornings can be gray and cold, so locals always carry a jacket.',
  'mythfact': [
   {'s': 'San Francisco is often foggy, even in summer.', 'ans': True, 'why': 'Cool air from the ocean makes fog, and summer mornings are often gray.'},
   {'s': 'The Golden Gate Bridge is painted gold.', 'ans': False, 'why': 'It is a red-orange color, and fog sometimes hides it.'},
   {'s': 'San Francisco has many steep hills.', 'ans': True, 'why': 'Many streets go up and down sharply.'},
   {'s': 'You can ride a cable car in San Francisco today.', 'ans': True, 'why': 'The cable cars still run and are a popular way to see the city.'},
   {'s': 'Warm clothes are not needed in San Francisco in July.', 'ans': False, 'why': 'Many visitors are surprised: July can be chilly, so people wear layers.'}],
  'wild': [
   {'kind': 'Weather app message', 'lines': ['**Foggy** until 11 a.m.', 'Sunny after noon', 'Temp: 58°F (14°C)'], 'decode': {'q': 'When does the sun come out?', 'opts': ['After noon', 'At 8 a.m.', 'It never does'], 'ans': 0, 'why': 'The app says: sunny after noon.'}},
   {'kind': 'Cable car stop sign', 'lines': ['**Cable Car Stop**', 'Pay the conductor', 'Hold on tight!'], 'decode': {'q': 'Where do you pay?', 'opts': ['To the conductor', 'At the bridge', 'In the hotel'], 'ans': 0, 'why': 'The sign says: pay the conductor.'}}],
  'compare': {'br': 'In Brazil, people often think of the USA as sunny, and many cities are hot all year.', 'us': 'In San Francisco, the weather can be cool and foggy, and people dress in layers.', 'tip': 'Say: “It’s a bit chilly.”', 'ask': 'What do you wear when it is cold? Say it in English.'},
  'quiz': [
   {'q': 'You see a thick gray cloud near the ground. You say…', 'opts': ['It’s so foggy today.', 'It is so fog today.', 'Today is foggy so a lot.'], 'ans': 0, 'why': 'Foggy is the adjective: It’s so foggy.'},
   {'q': 'Your friend is cold. You say…', 'opts': ['Take my jacket.', 'Take me jacket.', 'Take jacket of me.'], 'ans': 0, 'why': 'Use my + noun: my jacket.'},
   {'q': '“Chilly” means…', 'opts': ['a little cold', 'very hot', 'very dry'], 'ans': 0, 'why': 'Chilly is cool and a bit cold.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Where is the bridge?',
  'text': [
   'Tom is visiting **San Francisco**. His friend Mei lives near the bay. This morning, the city is white and quiet. Tom looks out the window and cannot see the end of the street.',
   '“**Good morning! It’s so foggy today**,” Tom says. “**Yes. It’s always foggy here**,” Mei says. “**Can we see the bridge?**” “**Not right now. Maybe at noon.**” Tom sees only a gray wall. Mei smiles. “The bridge is there, but the fog is a big blanket.”',
   '“**It’s chilly too**,” Tom says. He has only a T-shirt. “**Take my jacket**,” Mei says. “**Thanks. You’re kind**,” Tom says. The jacket is warm and a little big.',
   'At night, Mei sings “Twinkle, Twinkle, Little Star” in the kitchen. It is a children’s poem about a star in the sky. “Tonight the fog hides every star,” Tom says. “But a child can still dream,” Mei says.',
   '“**Do you want to ride the cable car?**” Mei asks the next day. “**Yes! Where do we catch it?**” Tom says. They walk up a steep hill. The fog opens, and the red bridge comes out. “Now I see it!” Tom says. “Take a picture,” Mei laughs.'],
  'glossary': [{'w': 'fog', 'pt': 'neblina'}, {'w': 'foggy', 'pt': 'com neblina'}, {'w': 'bay', 'pt': 'baía'}, {'w': 'chilly', 'pt': 'frio, friozinho'}, {'w': 'kind', 'pt': 'gentil'}, {'w': 'cable car', 'pt': 'bondinho'}, {'w': 'steep', 'pt': 'íngreme'}, {'w': 'hill', 'pt': 'ladeira, colina'}, {'w': 'blanket', 'pt': 'cobertor'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A foggy day in San Francisco', 'A hot day at the beach', 'A trip to a museum'], 'ans': 0, 'why': 'Tom and Mei talk about fog, cold and the bridge.'},
  'scan': [{'q': 'Who lends a jacket?', 'ans': 'Mei', 'alt': ['mei']}, {'q': 'When can they see the bridge, maybe?', 'ans': 'at noon', 'alt': ['noon']}, {'q': 'What does Mei sing?', 'ans': 'Twinkle, Twinkle, Little Star', 'alt': ['twinkle twinkle little star', 'twinkle']}],
  'tf': [{'s': 'Tom can see the bridge in the morning.', 'ans': False, 'why': 'The fog hides it.'}, {'s': 'Mei gives Tom her jacket.', 'ans': True, 'why': '“Take my jacket.”'}, {'s': 'Tom has a warm coat.', 'ans': False, 'why': 'He has only a T-shirt.'}, {'s': 'They walk up a steep hill the next day.', 'ans': True, 'why': 'They go to catch the cable car.'}],
  'order': ['Tom says it is foggy.', 'Mei says maybe they can see the bridge at noon.', 'Mei gives Tom her jacket.', 'Mei sings a song at night.', 'They go to ride the cable car.'],
  'ctx': [{'sent': 'It’s chilly this morning.', 'w': 'chilly', 'opts': ['a little cold', 'very hot', 'very loud'], 'ans': 0, 'why': 'Chilly = cool, a bit cold.'}, {'sent': 'They walk up a steep hill.', 'w': 'steep', 'opts': ['going up sharply', 'very flat', 'very short'], 'ans': 0, 'why': 'A steep hill goes up fast.'}, {'sent': 'The fog is a big blanket.', 'w': 'fog', 'opts': ['a thick cloud near the ground', 'a strong wind', 'a heavy rain'], 'ans': 0, 'why': 'Fog is a low cloud that hides things.'}],
  'chunkHunt': ['It’s so foggy today.', 'It’s chilly too.', 'Take my jacket.', 'Where do we catch it?'],
  'think': 'Do you like foggy or sunny days? Why?'},
 'convo': {'npc': {'name': 'Mei'}, 'story': 'You visit San Francisco. Mei is your local friend. It is a foggy morning.', 'turns': [
  {'npc': 'Good morning! Look outside.', 'pt': 'Bom dia! Olhe lá fora.', 'opts': [
   {'en': 'Good morning! It’s so foggy today.', 'pt': 'Bom dia! Está tão nublado hoje.', 'ok': True, 'fb': 'Natural comment about the weather.'},
   {'en': 'Good morning! Is so fog today.', 'pt': 'Bom dia! É tão neblina hoje.', 'ok': False, 'fb': 'Say: It’s so foggy.'},
   {'en': 'Good night! It is foggy.', 'pt': 'Boa noite! Está nublado.', 'ok': False, 'fb': 'In the morning, say Good morning.'}]},
  {'npc': 'Yes. It’s always foggy here.', 'pt': 'Sim. Aqui sempre tem neblina.', 'opts': [
   {'en': 'Can we see the bridge?', 'pt': 'Dá para ver a ponte?', 'ok': True, 'fb': 'Good follow-up question.'},
   {'en': 'We can see the bridge?', 'pt': 'A gente dá para ver a ponte?', 'ok': False, 'fb': 'In a question, put Can first.'},
   {'en': 'Can we seeing the bridge?', 'pt': 'Podemos vendo a ponte?', 'ok': False, 'fb': 'After can, use the base verb: see.'}]},
  {'npc': 'Not right now. Maybe at noon.', 'pt': 'Agora não. Talvez ao meio-dia.', 'opts': [
   {'en': 'It is cold too.', 'pt': 'Também está frio.', 'ok': False, 'fb': 'Possible, but chilly is the usual word for a cool morning.'},
   {'en': 'I am chilly too.', 'pt': 'Eu sou frio também.', 'ok': False, 'fb': 'Say: It’s chilly, or I’m cold.'},
   {'en': 'It’s chilly too.', 'pt': 'Está frio também.', 'ok': True, 'fb': 'Natural way to talk about cool weather.'}]},
  {'npc': 'Take my jacket.', 'pt': 'Pegue meu casaco.', 'opts': [
   {'en': 'Thanks. You’re kind.', 'pt': 'Obrigado. Você é gentil.', 'ok': True, 'fb': 'Polite thanks.'},
   {'en': 'Thanks. You are kindly.', 'pt': 'Obrigado. Você é gentilmente.', 'ok': False, 'fb': 'Kind is the adjective, not kindly.'},
   {'en': 'No thanks. Jacket is yes.', 'pt': 'Não, obrigado. Casaco é sim.', 'ok': False, 'fb': 'It does not make sense.'}]},
  {'npc': 'Do you want to ride the cable car?', 'pt': 'Quer andar no bondinho?', 'opts': [
   {'en': 'Yes! Where do we catch it?', 'pt': 'Sim! Onde pegamos?', 'ok': True, 'fb': 'Natural reply with a question.'},
   {'en': 'Yes! Where we catch it?', 'pt': 'Sim! Onde nós pegamos?', 'ok': False, 'fb': 'Use do: Where do we catch it?'},
   {'en': 'Yes! Where is catch it?', 'pt': 'Sim! Onde é pegar?', 'ok': False, 'fb': 'Wrong structure.'}]}]},
 'errors': [
  {'wrong': 'It is so fog today.', 'fix': 'It’s so foggy today.', 'alt': 'It has so fog today.', 'why': 'Fog is a noun; foggy is the adjective after is.'},
  {'wrong': 'We can see the bridge?', 'fix': 'Can we see the bridge?', 'alt': 'Can we to see the bridge?', 'why': 'In a question, put Can first; then use the base verb.'},
  {'wrong': 'I am cold too, take me jacket.', 'fix': 'Take my jacket.', 'alt': 'Take the jacket of me.', 'why': 'Use my before a thing that is yours.'},
  {'wrong': 'Where we catch it?', 'fix': 'Where do we catch it?', 'alt': 'Where we do catch it?', 'why': 'Questions with where need do: Where do we…?'}],
 'homework': 'Write a short dialogue: it is a foggy, cold day, and you lend a jacket to a friend.',
 'homework_items': ['Write 3 words for cold weather.', 'Say aloud: It’s so foggy today.', 'Listen to the dialogue and shadow Mei.', 'Review: I’m cold / It’s chilly.']}
