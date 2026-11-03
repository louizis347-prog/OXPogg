"""Suplemento Quest v5 · aula 66: Furniture shopping + regular Could I try it on? (Confessions of a Shopaholic)."""
SUPP = {
 'reg': 152,
 'badge': {'icon': '🛋️', 'name': 'Sofa Shopper', 'desc': 'Ask for a sofa, check the price, try it and choose delivery'},
 'culture': {
  'hook': 'A furniture store is a good place to practice English. You can sit, touch, ask the price and ask about delivery, all in short, simple questions.',
  'mythfact': [
   {'s': 'Austin is the capital of Texas.', 'ans': True, 'why': 'Austin is the capital city of the state of Texas.'},
   {'s': 'In many furniture stores, you can sit on a sofa before you buy it.', 'ans': True, 'why': 'Showrooms usually want you to test the furniture.'},
   {'s': 'In the USA, every store delivers furniture for free.', 'ans': False, 'why': 'Many stores charge for delivery, so it is smart to ask.'},
   {'s': '“Sofa” and “couch” are very different things in the USA.', 'ans': False, 'why': 'People often use both words for the same thing.'},
   {'s': 'Some furniture comes in a flat box, and you build it at home.', 'ans': True, 'why': 'This is common for desks, shelves and beds.'}],
  'wild': [
   {'kind': 'Price tag', 'lines': ['**GRAY SOFA**  $400', 'Delivery  $50', 'Free delivery on Fridays'], 'decode': {'q': 'How much is the sofa without delivery?', 'opts': ['$400', '$450', '$50'], 'ans': 0, 'why': 'The sofa is $400. Delivery is another price.'}},
   {'kind': 'Store sign', 'lines': ['**WEEKEND SALE**', '20% off all chairs', 'Saturday and Sunday only'], 'decode': {'q': 'When is the sale?', 'opts': ['On the weekend', 'Every day', 'On Monday'], 'ans': 0, 'why': '“Saturday and Sunday only.”'}}],
  'compare': {'br': 'In Brazil, many people look for furniture in stores or online and often ask about payment in parts.', 'us': 'In the USA, stores usually let you sit on the furniture, and they often ask about the delivery day.', 'tip': 'Ask two things: “How much is this one?” and “When do you deliver?”', 'ask': 'What furniture do you want in your home? Say it in English.'},
  'quiz': [
   {'q': 'You enter a store and want a sofa. You say…', 'opts': ['Hi! I’m looking for a sofa.', 'Hi! I am a sofa.', 'Sofa, where, yes?'], 'ans': 0, 'why': 'I’m looking for… is the natural way.'},
   {'q': 'The seller says, “Sit down and try it.” What should you do?', 'opts': ['Sit on the sofa', 'Pay now', 'Go home'], 'ans': 0, 'why': 'Try it means test the sofa.'},
   {'q': '“We deliver on Friday.” It means…', 'opts': ['They bring it to your home on Friday', 'You take it on Friday', 'The store is closed Friday'], 'ans': 0, 'why': 'Deliver = bring to your home.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'A gray sofa',
  'text': [
   'Saturday in **Austin**. Omar needs a new sofa. His old sofa is small and hard. He walks into a big furniture store. A woman in a blue shirt smiles at him.',
   '“**I\'m looking for a sofa**,” Omar says. “We have many,” she says. “What color do you like?” “Gray,” he answers. He sees a gray sofa near a lamp. “**How much is this one?**” “It\'s four hundred dollars.” Omar thinks, “It\'s **a bit pricey**.” He says, “Let\'s **look around**.”',
   'They see a desk, a bed and a nice table, but the gray sofa is the best. “**Is it comfortable?**” he asks. “Sit down and try it,” she says. Omar sits. The pillow is soft. “It\'s **so comfy**!” he says. He could nap here.',
   '“**I\'ll take it**,” says Omar. He pays by card. “We deliver on Friday,” she says. “Great, thank you!” Omar smiles. On the way out, he thinks of the film Confessions of a Shopaholic. In the film, a young woman loves shopping and asks, “Could I try it on?” Omar laughs. He wants only one sofa today.',
   'On Friday, two men bring the sofa to his house. They put it in the living room. Omar sits down with a cup of tea. “Perfect,” he says.'],
  'glossary': [{'w': 'furniture', 'pt': 'móveis'}, {'w': 'sofa', 'pt': 'sofá'}, {'w': 'hard', 'pt': 'duro'}, {'w': 'gray', 'pt': 'cinza'}, {'w': 'pricey', 'pt': 'caro (informal)'}, {'w': 'comfy', 'pt': 'confortável (informal)'}, {'w': 'pillow', 'pt': 'almofada / travesseiro'}, {'w': 'deliver', 'pt': 'entregar'}, {'w': 'nap', 'pt': 'cochilar'}, {'w': 'desk', 'pt': 'escrivaninha'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Buying a sofa in a store', 'Cooking dinner', 'A trip to the beach'], 'ans': 0, 'why': 'Omar buys a gray sofa.'},
  'scan': [{'q': 'What color is the sofa?', 'ans': 'gray', 'alt': ['grey']}, {'q': 'How much is the sofa?', 'ans': 'four hundred dollars', 'alt': ['$400', '400', 'four hundred']}, {'q': 'When do they deliver?', 'ans': 'on Friday', 'alt': ['friday']}],
  'tf': [{'s': 'Omar\'s old sofa is big and soft.', 'ans': False, 'why': 'His old sofa is small and hard.'}, {'s': 'Omar thinks the sofa is a bit pricey.', 'ans': True, 'why': '“It\'s a bit pricey.”'}, {'s': 'Omar sits on the sofa before he buys it.', 'ans': True, 'why': 'The woman says, “Sit down and try it.”'}, {'s': 'Omar takes the sofa home in his car.', 'ans': False, 'why': 'Two men bring it on Friday.'}],
  'order': ['Omar walks into the store.', 'He says he is looking for a sofa.', 'He sits on the gray sofa.', 'He says, “I\'ll take it.”', 'Two men bring the sofa on Friday.'],
  'ctx': [{'sent': 'It\'s a bit pricey.', 'w': 'pricey', 'opts': ['costs a lot', 'is very small', 'is very old'], 'ans': 0, 'why': 'Pricey = expensive.'}, {'sent': 'Sit down and try it.', 'w': 'try', 'opts': ['test it', 'sell it', 'wash it'], 'ans': 0, 'why': 'Try = test to see if you like it.'}, {'sent': 'Two men bring the sofa on Friday.', 'w': 'bring', 'opts': ['carry to a place', 'throw away', 'paint'], 'ans': 0, 'why': 'Bring = carry something to a place.'}],
  'chunkHunt': ['I\'m looking for a sofa.', 'How much is this one?', 'Is it comfortable?', 'I\'ll take it.'],
  'think': 'What is the most important thing for you in a sofa: color, price or comfort?'},
 'convo': {'npc': {'name': 'Tess'}, 'story': 'You are in a furniture store in Austin. Tess works there. Find a sofa and buy it.', 'turns': [
  {'npc': 'Hi! Can I help you?', 'pt': 'Oi! Posso ajudar?', 'opts': [
   {'en': 'I\'m looking for a sofa.', 'pt': 'Estou procurando um sofá.', 'ok': True, 'fb': 'Natural way to say what you want.'},
   {'en': 'I am looking a sofa.', 'pt': 'Eu estou olhando um sofá.', 'ok': False, 'fb': 'Say looking for.'},
   {'en': 'I have a sofa.', 'pt': 'Eu tenho um sofá.', 'ok': False, 'fb': 'She asks what you need.'}]},
  {'npc': 'We have many. What color do you like?', 'pt': 'Temos vários. Que cor você gosta?', 'opts': [
   {'en': 'I like it very.', 'pt': 'Eu gosto muito dele.', 'ok': False, 'fb': 'Name a color.'},
   {'en': 'Four hundred dollars.', 'pt': 'Quatrocentos dólares.', 'ok': False, 'fb': 'She asks about color, not price.'},
   {'en': 'Gray, please.', 'pt': 'Cinza, por favor.', 'ok': True, 'fb': 'Short and clear.'}]},
  {'npc': 'This one is four hundred dollars.', 'pt': 'Este custa quatrocentos dólares.', 'opts': [
   {'en': 'Is it comfortable?', 'pt': 'É confortável?', 'ok': True, 'fb': 'Good question before you buy.'},
   {'en': 'It is comfort?', 'pt': 'É conforto?', 'ok': False, 'fb': 'Use the adjective comfortable.'},
   {'en': 'I am Omar, thanks.', 'pt': 'Sou o Omar, valeu.', 'ok': False, 'fb': 'It does not answer the price.'}]},
  {'npc': 'Sit down and try it.', 'pt': 'Sente e experimente.', 'opts': [
   {'en': 'It is not a table.', 'pt': 'Não é uma mesa.', 'ok': False, 'fb': 'It does not fit the situation.'},
   {'en': 'Yes, it\'s very comfy. I\'ll take it.', 'pt': 'Sim, é muito confortável. Vou levar.', 'ok': True, 'fb': 'You decide: I\'ll take it.'},
   {'en': 'I take it yesterday.', 'pt': 'Eu levo ontem.', 'ok': False, 'fb': 'Use I\'ll take it for a new decision.'}]},
  {'npc': 'Great. We deliver on Friday.', 'pt': 'Ótimo. Entregamos na sexta.', 'opts': [
   {'en': 'Friday is good. Thanks!', 'pt': 'Sexta está bom. Obrigado!', 'ok': True, 'fb': 'Accepts the day politely.'},
   {'en': 'I deliver Friday you.', 'pt': 'Eu entrego sexta você.', 'ok': False, 'fb': 'The store delivers to you.'},
   {'en': 'Where is the bed?', 'pt': 'Onde está a cama?', 'ok': False, 'fb': 'It changes the subject.'}]}]},
 'errors': [
  {'wrong': 'I\'m looking a sofa.', 'fix': 'I\'m looking for a sofa.', 'alt': 'I look for to a sofa.', 'why': 'Use look for when you search for something.'},
  {'wrong': 'How many is this one?', 'fix': 'How much is this one?', 'alt': 'How much costs this one?', 'why': 'For price, say how much is it.'},
  {'wrong': 'The sofa is very confortable.', 'fix': 'The sofa is very comfortable.', 'alt': 'The sofa is very comfort.', 'why': 'Write comfortable with m: comf-ortable. The adjective ends in -able.'},
  {'wrong': 'We delivery on Friday.', 'fix': 'We deliver on Friday.', 'alt': 'We deliver in Friday.', 'why': 'Deliver is the verb; delivery is the noun. Use on with days.'}],
 'homework': 'Write 4 short lines to buy a chair or a sofa: what you want, the color, the price and the delivery day.',
 'homework_items': ['Say 3 pieces of furniture you have at home.', 'Write: I\'m looking for a… in…', 'Listen to the dialogue again and shadow Omar.', 'Review: How much is this one? / Is it comfortable? / I\'ll take it.']}
