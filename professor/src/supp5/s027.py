"""Suplemento Quest v5 · aula 27: Sharing food + regular These and Those (Little Jack Horner)."""
SUPP = {
 'reg': 47,
 'badge': {'icon': '🍖', 'name': 'BBQ Buddy', 'desc': 'Share a meal and order sides'},
 'sticker': {'cat': 'Everyday culture', 'title': 'Kansas City Barbecue', 'sub': 'Dig in!'},
 'culture': {
  'hook': 'Kansas City is famous for barbecue: meat cooked slowly, with a sweet, thick sauce. In a barbecue place, friends often share one big plate and eat with their hands.',
  'polite': 'Ask **What’s good here?** and say **We’ll share this one.** Say **Dig in!** when the food comes.',
  'mythfact': [
   {'s': 'Kansas City is well known for barbecue.', 'ans': True, 'why': 'Ribs, brisket and “burnt ends” are local favorites.'},
   {'s': 'Barbecue in the USA is only chicken.', 'ans': False, 'why': 'Pork, beef and chicken are all common, and each region has its own style.'},
   {'s': 'It is normal to eat ribs with your hands.', 'ans': True, 'why': 'Most people eat ribs by hand and use napkins.'},
   {'s': 'Restaurants never give you “sides”.', 'ans': False, 'why': 'Sides like corn, beans and coleslaw are very common with barbecue.'},
   {'s': 'Barbecue sauce is often sweet and a little smoky.', 'ans': True, 'why': 'Kansas City sauce is known for being thick and sweet.'}],
  'wild': [
   {'kind': 'Barbecue menu', 'lines': ['**Rack of ribs** (to share)  $22', '**Side:** corn, beans or coleslaw  $3', '**Water**  free · **Soda**  $2'], 'decode': {'q': 'How much are a rack of ribs and two sides?', 'opts': ['$26', '$25', '$28'], 'ans': 2, 'why': '$22 + $3 + $3 = $28.'}},
   {'kind': 'Sign on the table', 'lines': ['**Napkins** are in the holder', 'Ask for extra sauce', 'Wash your hands before you eat'], 'decode': {'q': 'Where are the napkins?', 'opts': ['In the holder', 'In the kitchen', 'On the menu'], 'ans': 0, 'why': '“Napkins are in the holder.”'}}],
  'compare': {'br': 'In Brazil, a churrasco is a social meal with many cuts of meat, often shared at home or at a churrascaria.', 'us': 'In the USA, a barbecue place serves big plates to share, with sides and sauce; it is casual and messy.', 'tip': 'Say “Can we share?” and “Extra napkins, please!”', 'ask': 'Do you share food with friends? What do you share? Say it in English.'},
  'quiz': [
   {'q': 'Aaron asks, “Do you want to share?” You say…', 'opts': ['Yes. What’s good here?', 'I am share.', 'No, thanks, I am.'], 'ans': 0, 'why': 'Accept and ask for a recommendation.'},
   {'q': 'A “side” is…', 'opts': ['A small extra dish', 'A table', 'A bill'], 'ans': 0, 'why': 'A side dish goes with the main dish.'},
   {'q': 'You are full. You can say…', 'opts': ['I’m stuffed!', 'I’m hungry!', 'I’m cold!'], 'ans': 0, 'why': 'Stuffed = very full.'}]},
 'reading': {
  'genre': 'Restaurant review', 'title': 'Ribs in Kansas City',
  'text': [
   'My friend Carl and I went to a barbecue restaurant in **Kansas City**. It smelled so good! A man called Aaron said, “**Welcome! Do you want to share?**” “Yes,” we said. “**What’s good here?**”',
   '“**The ribs are great**,” said Aaron. We ordered one rack of ribs. Then he asked, “**Do you want sides?**” “Corn and beans, please,” I said. “**Anything to drink?**” “Two waters, please.”',
   'The food came on one big plate. There was no knife and no fork, only napkins! Carl said, “**Dig in!**” We ate the ribs with our hands. The sauce was sweet and a little smoky. It was “**finger-lickin’ good**”, and we laughed.',
   'I remembered a nursery rhyme from England, “Little Jack Horner”. It is from about the 1700s. A boy sits in a corner and eats a Christmas pie. He pulls out a plum and says, “What a good boy am I!” We sat at a corner table too, and I felt like Jack Horner.',
   'At the end, Carl said, “**I’m stuffed!**” I said, “**Save room** for dessert.” We shared a small piece of pie. It was a perfect lunch, and we will come back soon.'],
  'glossary': [{'w': 'barbecue', 'pt': 'churrasco/barbecue'}, {'w': 'share', 'pt': 'dividir'}, {'w': 'ribs', 'pt': 'costelas'}, {'w': 'rack', 'pt': 'porção inteira de costelas'}, {'w': 'sides', 'pt': 'acompanhamentos'}, {'w': 'napkins', 'pt': 'guardanapos'}, {'w': 'sauce', 'pt': 'molho'}, {'w': 'smoky', 'pt': 'defumado'}, {'w': 'plum', 'pt': 'ameixa'}, {'w': 'stuffed', 'pt': 'empanturrado'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Sharing ribs at a barbecue restaurant', 'Buying shoes at a store', 'A flight to Paris'], 'ans': 0, 'why': 'Two friends share ribs in Kansas City.'},
  'scan': [{'q': 'What sides do they order?', 'ans': 'corn and beans', 'alt': ['corn', 'beans']}, {'q': 'What do they drink?', 'ans': 'water', 'alt': ['two waters', 'waters']}, {'q': 'What do they share for dessert?', 'ans': 'a piece of pie', 'alt': ['pie', 'a small piece of pie']}],
  'tf': [{'s': 'They order one rack of ribs.', 'ans': True, 'why': '“We ordered one rack of ribs.”'}, {'s': 'They eat the ribs with knives and forks.', 'ans': False, 'why': 'They eat with their hands.'}, {'s': 'The sauce is sweet and a little smoky.', 'ans': True, 'why': 'That is how the writer describes it.'}, {'s': 'Little Jack Horner is a story from Brazil.', 'ans': False, 'why': 'It is an English nursery rhyme.'}],
  'order': ['Aaron asks if they want to share.', 'They order ribs, corn, beans and water.', 'They eat the ribs with their hands.', 'Carl says he is stuffed.', 'They share a piece of pie.'],
  'ctx': [{'sent': 'Dig in before the ribs get cold!', 'w': 'Dig in', 'opts': ['Start eating', 'Go home', 'Wash the plate'], 'ans': 0, 'why': 'Dig in = start eating.'}, {'sent': 'I’m stuffed, so no more food, thanks.', 'w': 'stuffed', 'opts': ['very full', 'very hungry', 'very cold'], 'ans': 0, 'why': 'Stuffed = very full.'}, {'sent': 'We share one big plate.', 'w': 'share', 'opts': ['use together', 'sell', 'break'], 'ans': 0, 'why': 'Share = use or eat together.'}],
  'chunkHunt': ['Do you want to share?', 'What’s good here?', 'Do you want sides?', 'Dig in!'],
  'think': 'What food do you like to share with friends or family? Why?'},
 'convo': {'npc': {'name': 'Aaron'}, 'story': 'You and a friend are at a barbecue restaurant in Kansas City. Aaron is the server.',
  'turns': [
   {'npc': 'Welcome! Do you want to share?', 'pt': 'Bem-vindos! Querem dividir?', 'opts': [
    {'en': 'Yes. What’s good here?', 'pt': 'Sim. O que é bom aqui?', 'ok': True, 'fb': 'Accept and ask.'},
    {'en': 'I am hungry share.', 'pt': 'Eu faminto dividir.', 'ok': False, 'fb': 'Not a full sentence.'},
    {'en': 'No, welcome.', 'pt': 'Não, bem-vindo.', 'ok': False, 'fb': 'It does not answer.'}]},
   {'npc': 'The ribs are great.', 'pt': 'As costelas são ótimas.', 'opts': [
    {'en': 'We’ll have ribs one.', 'pt': 'Teremos costelas uma.', 'ok': False, 'fb': 'Word order.'},
    {'en': 'We’ll have one rack of ribs.', 'pt': 'Vamos querer uma porção de costelas.', 'ok': True, 'fb': 'We’ll have = we order.'},
    {'en': 'I am a rib.', 'pt': 'Eu sou uma costela.', 'ok': False, 'fb': 'Wrong meaning.'}]},
   {'npc': 'Do you want sides?', 'pt': 'Querem acompanhamentos?', 'opts': [
    {'en': 'Corn and beans, please.', 'pt': 'Milho e feijão, por favor.', 'ok': True, 'fb': 'Name the sides.'},
    {'en': 'Side of me.', 'pt': 'Lado de mim.', 'ok': False, 'fb': 'Wrong meaning.'},
    {'en': 'Yes, I sit side.', 'pt': 'Sim, eu sento do lado.', 'ok': False, 'fb': 'Sides are dishes.'}]},
   {'npc': 'Anything to drink?', 'pt': 'Algo para beber?', 'opts': [
    {'en': 'Water is two.', 'pt': 'Água é duas.', 'ok': False, 'fb': 'Use Two waters, please.'},
    {'en': 'I drink to the ribs.', 'pt': 'Eu bebo para as costelas.', 'ok': False, 'fb': 'Not natural.'},
    {'en': 'Two waters, please.', 'pt': 'Duas águas, por favor.', 'ok': True, 'fb': 'Number + noun + please.'}]},
   {'npc': 'Enjoy the ribs!', 'pt': 'Aproveite as costelas!', 'opts': [
    {'en': 'Thanks! They look great.', 'pt': 'Valeu! Estão ótimas.', 'ok': True, 'fb': 'Thank and comment.'},
    {'en': 'Good night!', 'pt': 'Boa noite!', 'ok': False, 'fb': 'Not the right reply.'},
    {'en': 'I enjoy yes.', 'pt': 'Eu aprecio sim.', 'ok': False, 'fb': 'Say Thanks!'}]}]},
 'errors': [
  {'wrong': 'We share the ribs, yes?', 'fix': 'Can we share the ribs?', 'alt': 'We can to share the ribs?', 'why': 'Ask with Can we…?'},
  {'wrong': 'I want one ribs.', 'fix': 'I’d like one rack of ribs.', 'alt': 'I want one rib racks.', 'why': 'Say a rack of ribs; one goes with a singular word.'},
  {'wrong': 'I am full of the food.', 'fix': 'I’m full. / I’m stuffed.', 'alt': 'I have full.', 'why': 'Use I’m full for the feeling.'},
  {'wrong': 'This ribs is good.', 'fix': 'These ribs are good.', 'alt': 'This ribs are good.', 'why': 'Plural: these ribs are.'}],
 'homework': 'Write 5 sentences about a meal you share with family or friends, then say them aloud.',
 'homework_items': ['Write 5 sentences about a shared meal.', 'Practice: these / those with 4 foods.', 'Shadow the dialogue with Aaron.', 'Review: Do you want to share? / Dig in! / I’m stuffed!']}
