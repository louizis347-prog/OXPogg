"""Suplemento Quest v5 · aula 28: I'm hungry! + regular Snack Time (Oliver Twist)."""
SUPP = {
 'reg': 27,
 'badge': {'icon': '🥤', 'name': 'Snack Team', 'desc': 'Say you are hungry or thirsty and share the work'},
 'sticker': {'cat': 'Everyday culture', 'title': 'Hungry in Miami', 'sub': 'Perfect team!'},
 'culture': {
  'hook': 'Miami is a city of many cultures, and food is everywhere: Cuban sandwiches, coffee windows and food trucks. Learn how to say you are hungry and offer to help.',
  'polite': 'Say **I’m hungry** or **I’m thirsty**, then offer: **I’ll get the drinks.** Say **My treat!** if you pay.',
  'mythfact': [
   {'s': 'Miami has a large Cuban community.', 'ans': True, 'why': 'Cuban food and coffee are a big part of the city.'},
   {'s': 'A food truck is a vehicle that sells food.', 'ans': True, 'why': 'Taco trucks and food trucks sell lunch and snacks on the street.'},
   {'s': 'In English, “I have hunger” is the normal way to say it.', 'ans': False, 'why': 'Say “I’m hungry”: be + adjective, not have.'},
   {'s': 'Miami is in the state of California.', 'ans': False, 'why': 'Miami is in Florida.'},
   {'s': '“My treat!” means “I’ll pay for you.”', 'ans': True, 'why': 'Treat = you pay for a friend.'}],
  'wild': [
   {'kind': 'Coffee window sign', 'lines': ['**Cafecito** · $2', '**Cuban sandwich** · $8', '**Fresh juice** · $4'], 'decode': {'q': 'How much are a Cuban sandwich and a fresh juice?', 'opts': ['$12', '$10', '$14'], 'ans': 0, 'why': '$8 + $4 = $12.'}},
   {'kind': 'Text message', 'lines': ['I’m famished! Let’s eat.', 'Same here. Taco truck on 5th street?', 'Sounds like a plan. My treat!'], 'decode': {'q': 'Where do they want to eat?', 'opts': ['At a taco truck', 'At home', 'At school'], 'ans': 0, 'why': '“Taco truck on 5th street?”'}}],
  'compare': {'br': 'In Brazil, people say “Tô com fome” and often go to a lanchonete for a salgado and a suco.', 'us': 'In the USA, people say “I’m hungry” and grab a quick snack or a sandwich, often from a truck or a counter.', 'tip': 'English uses be: I’m hungry, I’m thirsty, I’m cold. Not “I have hungry”.', 'ask': 'What do you eat when you are hungry? Say it in English.'},
  'quiz': [
   {'q': 'You want to say you need food. You say…', 'opts': ['I’m hungry.', 'I have hungry.', 'I am hunger.'], 'ans': 0, 'why': 'Be + hungry.'},
   {'q': 'Your friend says, “I’ll get the drinks.” You say…', 'opts': ['Perfect team!', 'You are hungry.', 'Good night!'], 'ans': 0, 'why': 'Share the job and say thanks.'},
   {'q': '“Let’s get a snack” means…', 'opts': ['Let’s get something small to eat', 'Let’s sleep', 'Let’s go home'], 'ans': 0, 'why': 'A snack is a small meal.'}]},
 'reading': {
  'genre': 'Diary', 'title': 'A hungry day in Miami',
  'text': [
   'It is noon in **Miami**, and I am with my friend Cole. We walk on the beach, and the sun is hot. Cole says, “**I’m hungry. Are you hungry?**” “Yes, very!” I say. “**And I’m thirsty.**”',
   'Near the beach, there is a little window with a sign: “Sandwiches and fresh juice”. “**Let’s get a snack**,” says Cole. “**Do you want a sandwich?**” “Yes, and a juice, please.” We make a plan. “**I’ll get the sandwiches**,” I say. “**I’ll get the drinks**,” says Cole. **Perfect team!**',
   'Soon, we sit under a big tree and eat. The sandwich is warm, with ham and cheese. The juice is cold and sweet. “**I’m famished!**” says Cole, and he laughs. “**My treat** tomorrow,” I say.',
   'I think about “Oliver Twist”, a novel by Charles Dickens from 1838. Oliver is a poor boy, and there is very little food for him. One day, he stands up with his bowl and says, “Please, sir, I want some more.” It is a famous line. Today, I am lucky: I can have a snack, and I don’t need to ask for more.',
   'Now we are full and happy. Cole says, “**Sounds like a plan**. Tomorrow, tacos!” I smile. I love a day with a sunny beach and good food.'],
  'glossary': [{'w': 'hungry', 'pt': 'com fome'}, {'w': 'thirsty', 'pt': 'com sede'}, {'w': 'snack', 'pt': 'lanche'}, {'w': 'window', 'pt': 'janelinha'}, {'w': 'plan', 'pt': 'plano'}, {'w': 'famished', 'pt': 'faminto'}, {'w': 'treat', 'pt': 'convidar/pagar'}, {'w': 'novel', 'pt': 'romance'}, {'w': 'poor', 'pt': 'pobre'}, {'w': 'lucky', 'pt': 'sortudo'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Two friends get a snack in Miami', 'A flight to Paris', 'A math class'], 'ans': 0, 'why': 'Cole and the writer get a snack.'},
  'scan': [{'q': 'Who is the writer with?', 'ans': 'Cole', 'alt': ['a friend', 'her friend Cole']}, {'q': 'What does the writer get?', 'ans': 'the sandwiches', 'alt': ['sandwiches', 'sandwich']}, {'q': 'Who wrote “Oliver Twist”?', 'ans': 'Charles Dickens', 'alt': ['dickens']}],
  'tf': [{'s': 'The friends are hungry and thirsty.', 'ans': True, 'why': 'Both words are in the dialogue.'}, {'s': 'Cole gets the sandwiches.', 'ans': False, 'why': 'The writer gets the sandwiches; Cole gets the drinks.'}, {'s': 'The sandwich is warm.', 'ans': True, 'why': '“The sandwich is warm.”'}, {'s': 'Oliver Twist was published in 1938.', 'ans': False, 'why': 'It is from 1838.'}],
  'order': ['The friends walk on the beach.', 'Cole says he is hungry.', 'They decide who gets what.', 'They sit under a tree and eat.', 'They make a plan for tomorrow.'],
  'ctx': [{'sent': 'I’m famished, so let’s eat now.', 'w': 'famished', 'opts': ['very hungry', 'very tired', 'very happy'], 'ans': 0, 'why': 'Famished = very hungry.'}, {'sent': 'Let’s have a snack.', 'w': 'snack', 'opts': ['a small meal', 'a big dinner', 'a game'], 'ans': 0, 'why': 'A snack = a small meal.'}, {'sent': 'It’s my treat today.', 'w': 'treat', 'opts': ['I pay', 'I sleep', 'I leave'], 'ans': 0, 'why': 'My treat = I pay.'}],
  'chunkHunt': ['I’m hungry.', 'Let’s get a snack.', 'I’ll get the drinks.', 'Sounds like a plan.'],
  'think': 'What do you do when you are very hungry? Who pays when you eat with friends?'},
 'convo': {'npc': {'name': 'Cole'}, 'story': 'You and your friend Cole are on the beach in Miami and you are hungry. Plan a snack.',
  'turns': [
   {'npc': 'I’m hungry. Are you hungry?', 'pt': 'Estou com fome. Você está com fome?', 'opts': [
    {'en': 'I have hungry.', 'pt': 'Eu tenho faminto.', 'ok': False, 'fb': 'Use I’m hungry.'},
    {'en': 'I am a sandwich.', 'pt': 'Eu sou um sanduíche.', 'ok': False, 'fb': 'Wrong meaning.'},
    {'en': 'Yes, very! And I’m thirsty.', 'pt': 'Sim, muito! E estou com sede.', 'ok': True, 'fb': 'Answer and add.'}]},
   {'npc': 'Let’s get a snack.', 'pt': 'Vamos pegar um lanche.', 'opts': [
    {'en': 'Do you want a sandwich?', 'pt': 'Você quer um sanduíche?', 'ok': True, 'fb': 'A natural suggestion.'},
    {'en': 'You are snack.', 'pt': 'Você é lanche.', 'ok': False, 'fb': 'Wrong meaning.'},
    {'en': 'Snack is good no.', 'pt': 'Lanche é bom não.', 'ok': False, 'fb': 'Not natural.'}]},
   {'npc': 'Yes, and a juice, please.', 'pt': 'Sim, e um suco, por favor.', 'opts': [
    {'en': 'I get the sandwiches.', 'pt': 'Eu pego os sanduíches.', 'ok': False, 'fb': 'Use I’ll get… to offer.'},
    {'en': 'I’ll get the sandwiches.', 'pt': 'Eu pego os sanduíches.', 'ok': True, 'fb': 'I’ll = a decision now.'},
    {'en': 'I am the sandwiches.', 'pt': 'Eu sou os sanduíches.', 'ok': False, 'fb': 'Wrong meaning.'}]},
   {'npc': 'Thanks! I’ll get the drinks.', 'pt': 'Valeu! Eu pego as bebidas.', 'opts': [
    {'en': 'Perfect team!', 'pt': 'Time perfeito!', 'ok': True, 'fb': 'Happy to share the job.'},
    {'en': 'Drinks are me.', 'pt': 'Bebidas são eu.', 'ok': False, 'fb': 'Not natural.'},
    {'en': 'You are welcome yes.', 'pt': 'De nada sim.', 'ok': False, 'fb': 'Not needed here.'}]},
   {'npc': 'Here’s your sandwich. Enjoy!', 'pt': 'Aqui está seu sanduíche. Bom apetite!', 'opts': [
    {'en': 'Thanks! You too!', 'pt': 'Valeu! Você também!', 'ok': True, 'fb': 'A natural reply.'},
    {'en': 'I enjoy my sandwich.', 'pt': 'Eu aproveito meu sanduíche.', 'ok': False, 'fb': 'Say Thanks!'},
    {'en': 'Good night!', 'pt': 'Boa noite!', 'ok': False, 'fb': 'It is lunchtime.'}]}]},
 'errors': [
  {'wrong': 'I have hungry.', 'fix': 'I’m hungry.', 'alt': 'I am hunger.', 'why': 'In English, use be: I’m hungry.'},
  {'wrong': 'I have thirst.', 'fix': 'I’m thirsty.', 'alt': 'I am thirst.', 'why': 'Say I’m thirsty with be + adjective.'},
  {'wrong': 'We can to eat a snack.', 'fix': 'We can eat a snack.', 'alt': 'We can eating a snack.', 'why': 'After can, use the base verb.'},
  {'wrong': 'I take the sandwiches.', 'fix': 'I’ll get the sandwiches.', 'alt': 'I getting the sandwiches.', 'why': 'Use I’ll get for a quick offer.'}],
 'homework': 'Write 5 sentences about what you eat and drink when you are hungry or thirsty, and say them aloud.',
 'homework_items': ['Write 5 sentences: I’m hungry / I’m thirsty…', 'Make a plan for a snack with a friend in English.', 'Shadow the dialogue with Cole.', 'Review: I’m hungry. / Let’s get a snack. / I’ll get…']}
