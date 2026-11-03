"""Suplemento Quest v5 · aula 87: A picnic in the park + regular Which day works? (Saturday in the Park)."""
SUPP = {
 'reg': 98,
 'badge': {'icon': '🧺', 'name': 'Picnic Planner', 'desc': 'Plan a picnic: what to bring, where to sit, what to eat'},
 'culture': {
  'hook': 'In the USA, many people have picnics in a park on a sunny weekend. They bring food from home, find a shady place, and share what they have.',
  'mythfact': [
   {'s': 'Many US parks have picnic tables, and people can also sit on the grass.', 'ans': True, 'why': 'Tables are common in city and state parks, but they are often free on a first-come basis.'},
   {'s': 'In every US park, you can make a fire for your food.', 'ans': False, 'why': 'Many parks have rules about fire, and some only allow grills in special places. Read the signs.'},
   {'s': 'People often bring chips and fruit to a picnic.', 'ans': True, 'why': 'Easy food like chips, fruit and sandwiches is very common.'},
   {'s': 'You should leave your trash on the grass.', 'ans': False, 'why': 'Take it with you or use a trash can in the park.'},
   {'s': '“Saturday in the Park” is a song by the band Chicago.', 'ans': True, 'why': 'It is from 1972 and is about a happy day in a park.'}],
  'wild': [
   {'kind': 'Park sign', 'lines': ['**Picnic area**', 'Open 6 a.m. – 9 p.m.', 'Please use the trash cans.'], 'decode': {'q': 'What should you use for your trash?', 'opts': ['The trash cans', 'The grass', 'The lake'], 'ans': 0, 'why': '“Please use the trash cans.”'}},
   {'kind': 'Text from a friend', 'lines': ['**Picnic Saturday at noon?**', 'I bring the sandwiches.', 'Can you bring drinks?'], 'decode': {'q': 'What does the friend bring?', 'opts': ['Sandwiches', 'Drinks', 'A tent'], 'ans': 0, 'why': '“I bring the sandwiches.”'}}],
  'compare': {'br': 'In Brazil, a picnic in the park often has cake, juice and a lot of people sharing food.', 'us': 'In the USA, people often bring a blanket, a cooler and easy food. Many parks ask you to take your trash home or put it in a trash can.', 'tip': 'Ask a friend: “What can I bring?”', 'ask': 'What do you bring to a picnic? Say it in English.'},
  'quiz': [
   {'q': 'You want to say what is in your bag. You say…', 'opts': ['Sandwiches, fruit and juice.', 'Sandwiches fruit juice is.', 'I have in bag sandwiches.'], 'ans': 0, 'why': 'A short list is natural: A, B and C.'},
   {'q': 'You invite a friend to sit. You say…', 'opts': ['Let’s sit under that tree.', 'Let’s sitting under that tree.', 'We let sit under tree.'], 'ans': 0, 'why': 'Let’s + base verb.'},
   {'q': 'What does “shady” mean?', 'opts': ['with shade, not in the sun', 'very hot', 'very noisy'], 'ans': 0, 'why': 'Shade is the cool place under a tree.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Saturday in the park',
  'text': [
   'It is Saturday. Lena and her friend Ravi want to have a picnic. The sun is out. “**It’s a beautiful day for a picnic!**” Ravi says. Lena smiles. “**Yes! Did you bring a blanket?**” “**I did**,” he says. “**And you, what’s in your bag?**”',
   '“**Sandwiches, fruit and juice**,” Lena says. Ravi looks in his cooler. “**Great! I have chips and cookies.**” Lena laughs. “That is a lot of food for two people!” They look for a good place in the park.',
   'The grass is soft, but the sun is hot. “**Let’s sit under that tree**,” Lena says. “**Good idea. It’s shady**,” Ravi answers. They put the blanket on the grass and sit down. A cool wind moves the leaves.',
   'Lena remembers “Saturday in the Park,” a song by the American band Chicago from 1972. It is about a happy day in a park, with music and ice cream. “Which day works for a picnic?” she asks. “Saturday works for me,” Ravi says.',
   '“**Let’s eat!**” Lena says. They share the sandwiches and the chips. A man walks by with a dog and says, “**Have a great picnic!**” Lena and Ravi wave and say, “Thanks!”'],
  'glossary': [{'w': 'picnic', 'pt': 'piquenique'}, {'w': 'blanket', 'pt': 'cobertor, manta'}, {'w': 'cooler', 'pt': 'caixa térmica'}, {'w': 'chips', 'pt': 'salgadinhos (batata frita de pacote)'}, {'w': 'grass', 'pt': 'grama'}, {'w': 'soft', 'pt': 'macio'}, {'w': 'shady', 'pt': 'com sombra'}, {'w': 'wind', 'pt': 'vento'}, {'w': 'leaves', 'pt': 'folhas'}, {'w': 'share', 'pt': 'dividir'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Two friends have a picnic', 'A girl rents a car', 'A boy visits a museum'], 'ans': 0, 'why': 'Lena and Ravi have a picnic in a park.'},
  'scan': [{'q': 'What does Lena have in her bag?', 'ans': 'sandwiches, fruit and juice', 'alt': ['sandwiches', 'sandwiches fruit and juice']}, {'q': 'What does Ravi have?', 'ans': 'chips and cookies', 'alt': ['chips', 'chips and cookies']}, {'q': 'Where do they sit?', 'ans': 'under a tree', 'alt': ['under that tree', 'tree']}],
  'tf': [{'s': 'The picnic is on Saturday.', 'ans': True, 'why': 'It is Saturday.'}, {'s': 'Ravi forgets the blanket.', 'ans': False, 'why': 'He says, “I did.”'}, {'s': 'The place under the tree is shady.', 'ans': True, 'why': 'Ravi says, “It’s shady.”'}, {'s': '“Saturday in the Park” is by the band Chicago.', 'ans': True, 'why': 'It is a song by Chicago, from 1972.'}],
  'order': ['Lena and Ravi talk about the picnic.', 'They look in their bags.', 'They choose a tree.', 'They sit on the blanket.', 'A man says, “Have a great picnic!”'],
  'ctx': [{'sent': 'The place is shady.', 'w': 'shady', 'opts': ['not in the sun', 'very noisy', 'very far'], 'ans': 0, 'why': 'Shady = com sombra.'}, {'sent': 'The grass is soft.', 'w': 'soft', 'opts': ['not hard', 'very loud', 'very old'], 'ans': 0, 'why': 'Soft = macio.'}, {'sent': 'They share the chips.', 'w': 'share', 'opts': ['each person has some', 'one person has all', 'they throw them'], 'ans': 0, 'why': 'Share = dividir.'}],
  'chunkHunt': ['It’s a beautiful day for a picnic!', 'Did you bring a blanket?', 'Let’s sit under that tree.', 'Have a great picnic!'],
  'think': 'What food do you like to bring to a picnic?'},
 'convo': {'npc': {'name': 'Ravi'}, 'story': 'You and your friend Ravi are at the park for a picnic. Answer him.', 'turns': [
  {'npc': 'It’s a beautiful day for a picnic!', 'pt': 'É um lindo dia para um piquenique!', 'opts': [
   {'en': 'Yes! Did you bring a blanket?', 'pt': 'Sim! Você trouxe cobertor?', 'ok': True, 'fb': 'Agrees and asks a useful question.'},
   {'en': 'Yes! You bring a blanket?', 'pt': 'Sim! Você traz cobertor?', 'ok': False, 'fb': 'For the past, use Did you bring…?'},
   {'en': 'I am in the picnic.', 'pt': 'Eu estou no piquenique.', 'ok': False, 'fb': 'Strange here.'}]},
  {'npc': 'I did. And you, what’s in your bag?', 'pt': 'Trouxe. E você, o que tem na sua bolsa?', 'opts': [
   {'en': 'My bag is very.', 'pt': 'Minha bolsa é muito.', 'ok': False, 'fb': 'It does not answer.'},
   {'en': 'Sandwiches, fruit and juice.', 'pt': 'Sanduíches, frutas e suco.', 'ok': True, 'fb': 'A short list.'},
   {'en': 'I have sandwiches, fruit, and a juice of orange.', 'pt': 'Tenho sanduíches, fruta e um suco de laranja.', 'ok': False, 'fb': 'Too long. Say orange juice.'}]},
  {'npc': 'Great! I have chips and cookies.', 'pt': 'Ótimo! Tenho salgadinhos e biscoitos.', 'opts': [
   {'en': 'Let’s sit under that tree.', 'pt': 'Vamos sentar debaixo daquela árvore.', 'ok': True, 'fb': 'Next step of the plan.'},
   {'en': 'Let’s sitting under that tree.', 'pt': 'Vamos sentando debaixo daquela árvore.', 'ok': False, 'fb': 'Use Let’s + base verb.'},
   {'en': 'Under tree let’s.', 'pt': 'Debaixo árvore vamos.', 'ok': False, 'fb': 'The word order is wrong.'}]},
  {'npc': 'Good idea. It’s shady.', 'pt': 'Boa ideia. Tem sombra.', 'opts': [
   {'en': 'It’s a beautiful day.', 'pt': 'É um lindo dia.', 'ok': False, 'fb': 'Already said.'},
   {'en': 'Did you bring a blanket?', 'pt': 'Você trouxe cobertor?', 'ok': False, 'fb': 'Already asked and answered.'},
   {'en': 'Let’s eat!', 'pt': 'Vamos comer!', 'ok': True, 'fb': 'Time to eat.'}]},
  {'npc': 'Have a great picnic!', 'pt': 'Tenha um ótimo piquenique!', 'opts': [
   {'en': 'Thanks! You too!', 'pt': 'Obrigado! Você também!', 'ok': True, 'fb': 'Natural reply.'},
   {'en': 'I have a great picnic.', 'pt': 'Eu tenho um ótimo piquenique.', 'ok': False, 'fb': 'It sounds strange.'},
   {'en': 'Welcome to the picnic!', 'pt': 'Bem-vindo ao piquenique!', 'ok': False, 'fb': 'Wrong moment.'}]}]},
 'errors': [
  {'wrong': 'Did you brought a blanket?', 'fix': 'Did you bring a blanket?', 'alt': 'Do you brought a blanket?', 'why': 'After did, use the base verb: bring.'},
  {'wrong': 'Let’s to sit here.', 'fix': 'Let’s sit here.', 'alt': 'Let’s sitting here.', 'why': 'Let’s + base verb, without to.'},
  {'wrong': 'I have chips and cookie.', 'fix': 'I have chips and cookies.', 'alt': 'I have a chips and cookies.', 'why': 'Chips and cookies are plural.'},
  {'wrong': 'It is shade here.', 'fix': 'It’s shady here.', 'alt': 'It has shady here.', 'why': 'Shady describes the place; shade is the noun.'}],
 'homework': 'Write a short dialogue: you and a friend plan a picnic and say what you bring.',
 'homework_items': ['Write 5 picnic foods in English.', 'Say aloud: Let’s sit under that tree.', 'Listen to the dialogue and shadow Ravi.', 'Review: on Saturday / on Sunday / on the weekend.']}
