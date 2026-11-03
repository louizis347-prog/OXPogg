"""Suplemento Quest v5 · aula 88: At the beach + regular What's the weather like? (Rain)."""
SUPP = {
 'reg': 107,
 'badge': {'icon': '🏖️', 'name': 'Beach Ready', 'desc': 'Talk about water, sun, sunscreen and beach things'},
 'culture': {
  'hook': 'On a US beach, the first things to check are the weather, the water and the lifeguard flags. Then you can put on sunscreen and enjoy the day.',
  'mythfact': [
   {'s': 'Many US beaches have lifeguards, but not every beach has one.', 'ans': True, 'why': 'Lifeguards work at many popular beaches, often in the warm season. Look for the tower and the signs.'},
   {'s': 'Sunscreen is only for hot summer days.', 'ans': False, 'why': 'The sun can burn your skin on cloudy days too, so many people use sunscreen all year at the beach.'},
   {'s': 'A red flag at a beach often means the water is dangerous.', 'ans': True, 'why': 'Flag colors can change from place to place, so read the sign or ask the lifeguard.'},
   {'s': 'The water is warm at every beach in the USA.', 'ans': False, 'why': 'It can be cold in places like California or Maine, and warm in places like Florida or Hawaii.'},
   {'s': '“Rain” is a children’s poem by Robert Louis Stevenson.', 'ans': True, 'why': 'It is from the 1885 book A Child’s Garden of Verses.'}],
  'wild': [
   {'kind': 'Beach sign', 'lines': ['**Swim near the lifeguard.**', 'No lifeguard after 6 p.m.', 'Keep the beach clean.'], 'decode': {'q': 'Where should you swim?', 'opts': ['Near the lifeguard', 'Far from the beach', 'In the rain'], 'ans': 0, 'why': '“Swim near the lifeguard.”'}},
   {'kind': 'Weather report', 'lines': ['**Today: sunny and 82°F**', 'Water: warm', 'UV: very high'], 'decode': {'q': 'What is the weather today?', 'opts': ['Sunny', 'Rainy', 'Snowy'], 'ans': 0, 'why': 'The report says sunny.'}}],
  'compare': {'br': 'In Brazil, many people rent a chair and an umbrella on the beach and buy snacks from vendors.', 'us': 'In the USA, people often bring their own umbrella, towel and cooler. Some beaches rent chairs, but many do not, so check before you go.', 'tip': 'Ask: “Is the water cold?”', 'ask': 'Do you like the beach? What do you bring? Say it in English.'},
  'quiz': [
   {'q': 'You want to know the water temperature. You ask…', 'opts': ['Is the water cold?', 'The water is cold?', 'Water cold is?'], 'ans': 0, 'why': 'Question: Is + the water + cold?'},
   {'q': 'You forget your sunscreen. You say…', 'opts': ['I need sunscreen.', 'I am need sunscreen.', 'I needing sunscreen.'], 'ans': 0, 'why': 'Need is a state verb: I need…'},
   {'q': 'What is a wave?', 'opts': ['moving water in the sea', 'a type of sand', 'a beach chair'], 'ans': 0, 'why': 'Waves come from the sea to the beach.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'A warm day in Honolulu',
  'text': [
   'It is a sunny day in Honolulu. Nora and her friend Serena walk to the sand. “**What a beautiful beach!**” Serena says. “**Yes! Is the water cold?**” Nora asks. “**No, it’s warm. Let’s swim!**”',
   '“**Wait. I need sunscreen**,” Nora says. Her skin burns easily in the sun. “**Here, use mine**,” Serena says, and she gives Nora a bottle. Nora puts it on her face, her arms and her legs.',
   '“**Thanks. Where is the towel?**” Nora asks. “**It’s under the umbrella**,” Serena says. The umbrella is big and red. It makes a nice shade on the hot sand. Nora finds the towel and smiles. “**Perfect. Let’s go!**”',
   'A lifeguard sits in a high chair. She watches the water and the people. The waves are small and slow. A boy builds a castle in the sand. Nora thinks about a poem called “Rain.” It says rain falls on fields and trees. Today there is no rain, only blue sky.',
   'The girls swim for an hour. The sea is clear and warm. A woman by the water says, “**Have fun at the beach!**” Nora laughs and jumps over a small wave. It is a perfect day.'],
  'glossary': [{'w': 'sand', 'pt': 'areia'}, {'w': 'warm', 'pt': 'morna, quente'}, {'w': 'swim', 'pt': 'nadar'}, {'w': 'sunscreen', 'pt': 'protetor solar'}, {'w': 'skin', 'pt': 'pele'}, {'w': 'umbrella', 'pt': 'guarda-sol'}, {'w': 'lifeguard', 'pt': 'salva-vidas'}, {'w': 'waves', 'pt': 'ondas'}, {'w': 'castle', 'pt': 'castelo'}, {'w': 'clear', 'pt': 'transparente'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Two friends spend a day at the beach', 'A man rents a car', 'A girl goes camping'], 'ans': 0, 'why': 'Nora and Serena go to the beach and swim.'},
  'scan': [{'q': 'Is the water cold?', 'ans': 'no', 'alt': ['no, it is warm', 'it is warm', 'warm']}, {'q': 'What does Nora need?', 'ans': 'sunscreen', 'alt': ['she needs sunscreen']}, {'q': 'Where is the towel?', 'ans': 'under the umbrella', 'alt': ['umbrella']}],
  'tf': [{'s': 'The water is warm.', 'ans': True, 'why': 'Serena says, “It’s warm.”'}, {'s': 'Nora has her own sunscreen.', 'ans': False, 'why': 'Serena gives her a bottle.'}, {'s': 'The umbrella is blue.', 'ans': False, 'why': 'The umbrella is big and red.'}, {'s': 'A lifeguard watches the water.', 'ans': True, 'why': 'She sits in a high chair and watches.'}],
  'order': ['The girls arrive at the beach.', 'Nora asks about the water.', 'Nora puts on sunscreen.', 'She finds the towel.', 'They swim in the sea.'],
  'ctx': [{'sent': 'The water is warm.', 'w': 'warm', 'opts': ['a little hot', 'very cold', 'very dirty'], 'ans': 0, 'why': 'Warm = morno.'}, {'sent': 'The sea is clear.', 'w': 'clear', 'opts': ['you can see through it', 'very loud', 'very far'], 'ans': 0, 'why': 'Clear = transparente.'}, {'sent': 'A lifeguard sits in a high chair.', 'w': 'lifeguard', 'opts': ['a person who watches swimmers', 'a beach shop', 'a type of boat'], 'ans': 0, 'why': 'A lifeguard helps people in the water.'}],
  'chunkHunt': ['What a beautiful beach!', 'Is the water cold?', 'I need sunscreen.', 'Have fun at the beach!'],
  'think': 'What do you always bring to the beach?'},
 'convo': {'npc': {'name': 'Serena'}, 'story': 'You arrive at the beach with your friend Serena. Answer her.', 'turns': [
  {'npc': 'What a beautiful beach!', 'pt': 'Que praia linda!', 'opts': [
   {'en': 'Yes! Is the water cold?', 'pt': 'Sim! A água está fria?', 'ok': True, 'fb': 'Agrees and asks a good question.'},
   {'en': 'Yes! The water is cold?', 'pt': 'Sim! A água é fria?', 'ok': False, 'fb': 'Question order: Is the water…?'},
   {'en': 'I am a beach.', 'pt': 'Eu sou uma praia.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'No, it’s warm. Let’s swim!', 'pt': 'Não, está morna. Vamos nadar!', 'opts': [
   {'en': 'Wait. I need sunscreen.', 'pt': 'Espera. Preciso de protetor solar.', 'ok': True, 'fb': 'Natural and short.'},
   {'en': 'Wait. I am needing sunscreen.', 'pt': 'Espera. Estou precisando de protetor solar.', 'ok': False, 'fb': 'Need is a state verb: no -ing.'},
   {'en': 'It’s warm. Let’s swim!', 'pt': 'Está morna. Vamos nadar!', 'ok': False, 'fb': 'You repeat her words.'}]},
  {'npc': 'Here, use mine.', 'pt': 'Toma, use o meu.', 'opts': [
   {'en': 'Thanks. Where is the towel?', 'pt': 'Valeu. Onde está a toalha?', 'ok': True, 'fb': 'Thanks first, then a question.'},
   {'en': 'Thanks. Where the towel is?', 'pt': 'Valeu. Onde a toalha está?', 'ok': False, 'fb': 'Say: Where is the towel?'},
   {'en': 'I need sunscreen.', 'pt': 'Preciso de protetor solar.', 'ok': False, 'fb': 'She just gave it to you.'}]},
  {'npc': 'It’s under the umbrella.', 'pt': 'Está debaixo do guarda-sol.', 'opts': [
   {'en': 'It is a big umbrella.', 'pt': 'É um guarda-sol grande.', 'ok': False, 'fb': 'Does not follow the plan.'},
   {'en': 'Under umbrella is yes.', 'pt': 'Debaixo guarda-sol é sim.', 'ok': False, 'fb': 'Does not make sense.'},
   {'en': 'Perfect. Let’s go!', 'pt': 'Perfeito. Vamos!', 'ok': True, 'fb': 'Ready to go.'}]},
  {'npc': 'Have fun at the beach!', 'pt': 'Divirta-se na praia!', 'opts': [
   {'en': 'Thanks! You too!', 'pt': 'Obrigado! Você também!', 'ok': True, 'fb': 'Natural reply.'},
   {'en': 'I have fun at beach.', 'pt': 'Eu me divirto em praia.', 'ok': False, 'fb': 'Wrong grammar here.'},
   {'en': 'Welcome to the beach!', 'pt': 'Bem-vindo à praia!', 'ok': False, 'fb': 'Wrong moment.'}]}]},
 'errors': [
  {'wrong': 'I am needing sunscreen.', 'fix': 'I need sunscreen.', 'alt': 'I am need sunscreen.', 'why': 'Need is a state verb. Do not use -ing.'},
  {'wrong': 'The water is cold today?', 'fix': 'Is the water cold today?', 'alt': 'Is cold the water today?', 'why': 'For a yes/no question, put Is first.'},
  {'wrong': 'Where is the towels?', 'fix': 'Where are the towels?', 'alt': 'Where is towel?', 'why': 'Plural: are + towels. One towel: is.'},
  {'wrong': 'It is in under the umbrella.', 'fix': 'It’s under the umbrella.', 'alt': 'It is at the umbrella.', 'why': 'Use under alone. Do not add in.'}],
 'homework': 'Write a short dialogue: you arrive at a beach, ask about the water and ask for sunscreen.',
 'homework_items': ['Write 5 things you take to the beach.', 'Say aloud: Is the water cold?', 'Listen to the dialogue and shadow Serena.', 'Review: It’s sunny / It’s windy / It’s rainy.']}
