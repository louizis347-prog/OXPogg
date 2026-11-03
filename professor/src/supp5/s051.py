"""Suplemento Quest v5 · aula 51: Renting a bike + regular We Are a Team (Olympic Games)."""
SUPP = {
 'reg': 65,
 'badge': {'icon': '🚲', 'name': 'Bike Renter', 'desc': 'Rent a bike, ask about a lane and ride'},
 'sticker': {'cat': 'Everyday culture', 'title': 'Rent a Bike', 'sub': 'Helmet? Lock? Bike lane?'},
 'culture': {
  'hook': 'In many American cities you can rent a bike for an hour or a day, and ride along a lake or a park. Learn the few words you need before you pay and ride away.',
  'polite': 'Say **I’d like to rent a bike, please.** Ask **Is there a bike lane?** if you want a safe route.',
  'mythfact': [
   {'s': 'Orlando is a city in Florida.', 'ans': True, 'why': 'Orlando is in the state of Florida.'},
   {'s': 'Many US cities have bike lanes for riders.', 'ans': True, 'why': 'A bike lane is a part of the road marked for bikes.'},
   {'s': 'A rented bike is always free.', 'ans': False, 'why': 'You usually pay by the hour or by the day.'},
   {'s': 'Helmet rules are the same in every US state.', 'ans': False, 'why': 'Helmet laws are different from state to state and often depend on your age.'},
   {'s': 'The first modern Olympic Games were in Athens in 1896.', 'ans': True, 'why': 'Cycling was one of the sports in those Games.'}],
  'wild': [
   {'kind': 'Rental sign', 'lines': ['**City bike**  $5 per hour', '**Helmet**  free', '**Lock**  free', '**Return by 6:00 p.m.**'], 'decode': {'q': 'How much is a city bike for two hours?', 'opts': ['$5', '$10', '$15'], 'ans': 1, 'why': '$5 each hour, two hours = $10.'}},
   {'kind': 'Park sign', 'lines': ['**Bike lane** on the left', '**Walkers** on the right', '**Slow down** near the bridge'], 'decode': {'q': 'Where do the walkers go?', 'opts': ['On the left', 'On the right', 'On the bridge'], 'ans': 1, 'why': 'The sign says walkers on the right.'}}],
  'compare': {'br': 'In Brazil many cities have a ciclovia or ciclofaixa, and some have bikes you can rent with an app.', 'us': 'In the USA you often pay by the hour at a shop or with a bike-share app, and many places give you a helmet and a lock.', 'tip': 'Ask about the helmet and the lock before you pay.', 'ask': 'Do you like to ride a bike? Where do you ride? Say it in English.'},
  'quiz': [
   {'q': 'You want a bike for two hours. You say…', 'opts': ['I’d like to rent a bike for two hours.', 'I rent bike two hours.', 'Bike for I two.'], 'ans': 0, 'why': 'I’d like to + verb is polite.'},
   {'q': '“Do you want a helmet?” Yes, you do. You say…', 'opts': ['Yes, please.', 'Yes, I am.', 'I helmet.'], 'ans': 0, 'why': 'Yes, please is short and polite.'},
   {'q': 'A “lock” is used to…', 'opts': ['keep your bike safe', 'stop at a light', 'carry water'], 'ans': 0, 'why': 'You lock your bike when you stop.'}]},
 'reading': {
  'genre': 'Travel diary', 'title': 'A bike day by the lake',
  'text': [
   'Today my friend Darius and I are in **Orlando**. The sky is blue and the day is warm. We see a small shop with many bikes outside. “**Let’s ride!**” says Darius.',
   'Inside, the worker smiles. Darius says, “Hi! **I’d like to rent a bike.**” The worker asks, “**For how long?**” “**For two hours**,” he says. “That’s ten dollars. **Do you want a helmet?**” “**Yes, please.** And a lock.”',
   'Then I ask, “**Is there a bike lane?**” “Yes, **along the lake**,” the worker says. It is a long, flat path, and it is good for beginners. We say thanks and take our bikes.',
   'We ride slowly at first. The lake is beautiful and I see ducks and trees. After one hour, I am **out of breath**. “**Take five**,” I say. We sit on a bench and drink water. “**Wait up!**” says Darius, because I am slow again.',
   'I think of the Olympic Games. The modern Games began in Athens in 1896, and cycling was one of the sports. We are not Olympic riders, but we are a team. We **have fun riding**, and the day is perfect.'],
  'glossary': [{'w': 'rent', 'pt': 'alugar'}, {'w': 'helmet', 'pt': 'capacete'}, {'w': 'lock', 'pt': 'cadeado'}, {'w': 'bike lane', 'pt': 'ciclovia'}, {'w': 'lake', 'pt': 'lago'}, {'w': 'path', 'pt': 'caminho'}, {'w': 'beginners', 'pt': 'iniciantes'}, {'w': 'bench', 'pt': 'banco (de praça)'}, {'w': 'out of breath', 'pt': 'sem fôlego'}, {'w': 'team', 'pt': 'equipe'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Renting bikes and riding by a lake', 'Buying a car', 'A trip by train'], 'ans': 0, 'why': 'The friends rent bikes and ride.'},
  'scan': [{'q': 'In which city are the friends?', 'ans': 'Orlando', 'alt': []}, {'q': 'How much is the rental?', 'ans': 'ten dollars', 'alt': ['10', '$10', '10 dollars']}, {'q': 'Where is the bike lane?', 'ans': 'along the lake', 'alt': ['lake', 'by the lake']}],
  'tf': [{'s': 'The friends rent bikes for two hours.', 'ans': True, 'why': '“For two hours.”'}, {'s': 'Darius says no to the helmet.', 'ans': False, 'why': 'He says, “Yes, please.”'}, {'s': 'The bike lane is along the lake.', 'ans': True, 'why': 'The worker says so.'}, {'s': 'The writer is out of breath after one hour.', 'ans': True, 'why': 'The writer says “out of breath”.'}],
  'order': ['The friends see a bike shop.', 'Darius asks to rent a bike.', 'The worker asks about a helmet.', 'They ride along the lake.', 'They sit on a bench.'],
  'ctx': [{'sent': 'Let’s ride! The day is perfect.', 'w': 'Let’s ride', 'opts': ['Let us start riding', 'Let us sleep', 'Let us eat'], 'ans': 0, 'why': 'Let’s + verb = a suggestion.'}, {'sent': 'I am out of breath after the hill.', 'w': 'out of breath', 'opts': ['tired from moving', 'very happy', 'very cold'], 'ans': 0, 'why': 'Out of breath = you cannot breathe easily after exercise.'}, {'sent': 'Take five and drink some water.', 'w': 'Take five', 'opts': ['rest for a short time', 'count to five', 'pay five dollars'], 'ans': 0, 'why': 'Take five = take a short break.'}],
  'chunkHunt': ['I’d like to rent a bike.', 'For how long?', 'Do you want a helmet?', 'Is there a bike lane?'],
  'think': 'Where can you ride a bike in your city? Is there a bike lane near your home?'},
 'convo': {'npc': {'name': 'Darius'}, 'story': 'You work at a bike shop in Orlando. Darius is a customer. Answer him like a local!',
  'turns': [
   {'npc': 'Hi! I’d like to rent a bike.', 'pt': 'Oi! Eu gostaria de alugar uma bicicleta.', 'opts': [
    {'en': 'I rent bike you.', 'pt': 'Eu alugo bicicleta você.', 'ok': False, 'fb': 'Word order is wrong.'},
    {'en': 'Sure. For how long?', 'pt': 'Claro. Por quanto tempo?', 'ok': True, 'fb': 'Natural and helpful.'},
    {'en': 'Yes, I am a bike.', 'pt': 'Sim, eu sou uma bicicleta.', 'ok': False, 'fb': 'Wrong meaning.'}]},
   {'npc': 'For two hours.', 'pt': 'Por duas horas.', 'opts': [
    {'en': 'That’s ten dollars. Do you want a helmet?', 'pt': 'São dez dólares. Quer um capacete?', 'ok': True, 'fb': 'Price and a useful question.'},
    {'en': 'Two hours are ten dollar.', 'pt': 'Duas horas são dez dólar.', 'ok': False, 'fb': 'Say That’s ten dollars.'},
    {'en': 'I like the lake.', 'pt': 'Eu gosto do lago.', 'ok': False, 'fb': 'It does not answer the customer.'}]},
   {'npc': 'Yes, please. And a lock.', 'pt': 'Sim, por favor. E um cadeado.', 'opts': [
    {'en': 'No lock here.', 'pt': 'Sem cadeado aqui.', 'ok': False, 'fb': 'Rude and unclear.'},
    {'en': 'I have lock not.', 'pt': 'Eu tenho cadeado não.', 'ok': False, 'fb': 'Word order is wrong.'},
    {'en': 'Here you go. Have fun!', 'pt': 'Aqui está. Divirta-se!', 'ok': True, 'fb': 'Hand over the things and wish them well.'}]},
   {'npc': 'Is there a bike lane?', 'pt': 'Tem ciclovia?', 'opts': [
    {'en': 'Yes, along the lake.', 'pt': 'Sim, ao longo do lago.', 'ok': True, 'fb': 'Short and clear.'},
    {'en': 'Yes, I am lake.', 'pt': 'Sim, eu sou lago.', 'ok': False, 'fb': 'Wrong meaning.'},
    {'en': 'There are not lane.', 'pt': 'Não há faixa.', 'ok': False, 'fb': 'Use There isn’t a bike lane.'}]},
   {'npc': 'Have fun riding!', 'pt': 'Divirta-se pedalando!', 'opts': [
    {'en': 'Good night!', 'pt': 'Boa noite!', 'ok': False, 'fb': 'Not the right reply.'},
    {'en': 'I ride yes.', 'pt': 'Eu pedalo sim.', 'ok': False, 'fb': 'Say Thanks!'},
    {'en': 'Thanks! See you later!', 'pt': 'Valeu! Até mais!', 'ok': True, 'fb': 'Natural.'}]}]},
 'errors': [
  {'wrong': 'I want rent a bike.', 'fix': 'I’d like to rent a bike.', 'alt': 'I want to renting a bike.', 'why': 'Use I’d like to + base verb.'},
  {'wrong': 'For how much time?', 'fix': 'For how long?', 'alt': 'How long for?', 'why': 'For how long? is the natural question.'},
  {'wrong': 'Have a bike lane?', 'fix': 'Is there a bike lane?', 'alt': 'Are there bike lane?', 'why': 'Use Is there + singular noun.'},
  {'wrong': 'I put the helmet in the head.', 'fix': 'I put the helmet on my head.', 'alt': 'I put the helmet at my head.', 'why': 'Use on for a helmet.'}],
 'homework': 'Write 5 sentences about renting a bike, with a helmet, a lock and a bike lane, then say them aloud.',
 'homework_items': ['Write 5 sentences about a bike day.', 'Record yourself renting a bike.', 'Shadow the dialogue with Darius.', 'Review: For how long? / Is there a bike lane? / Take five.']}
