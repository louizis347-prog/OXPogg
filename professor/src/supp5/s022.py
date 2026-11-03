"""Suplemento Quest v5 · aula 22: Party invitation + regular Cheers! (Pat-a-Cake)."""
SUPP = {
 'reg': 12,
 'badge': {'icon': '🎉', 'name': 'Party Guest', 'desc': 'Accept an invitation and ask what to bring'},
 'sticker': {'cat': 'Everyday culture', 'title': 'The Party Invitation', 'sub': 'Can I bring something?'},
 'culture': {
  'hook': 'In the USA, a party starts with an invitation and a short reply. Learn the little words that make you a great guest, from RSVP to what to bring.',
  'polite': 'Always answer an invitation. Say **Thanks for the invite!** and ask **Can I bring something?**',
  'mythfact': [
   {'s': 'RSVP means “please reply to the invitation”.', 'ans': True, 'why': 'It comes from the French “répondez, s’il vous plaît”.'},
   {'s': 'It is rude to ask, “Can I bring something?”', 'ans': False, 'why': 'It is polite. Hosts often say, “Just a drink or a snack!”'},
   {'s': 'At a potluck, each guest brings a dish to share.', 'ans': True, 'why': 'A potluck is a meal where everybody brings some food.'},
   {'s': 'At a birthday party, people never sing.', 'ans': False, 'why': 'People usually sing “Happy Birthday to You” and the person blows out candles.'},
   {'s': 'You can say “I can’t come” to an invitation.', 'ans': True, 'why': 'A short, kind “no” is fine: “I’d love to, but I’m busy.”'}],
  'wild': [
   {'kind': 'Invitation card', 'lines': ['**Maya’s Birthday Party**', 'Saturday, May 10 · 7:00 PM', '123 Oak Street · Please RSVP by Thursday'], 'decode': {'q': 'When is the party?', 'opts': ['Thursday at 7:00', 'Saturday at 7:00 PM', 'Saturday at 10:00'], 'ans': 1, 'why': 'The card says Saturday, May 10, 7:00 PM.'}},
   {'kind': 'Text message', 'lines': ['Hi Lina! Thanks for the invite.', 'I’d love to come! Can I bring something?', 'I can make a salad. See you Saturday!'], 'decode': {'q': 'What can the guest bring?', 'opts': ['Chips', 'A salad', 'A cake'], 'ans': 1, 'why': '“I can make a salad.”'}}],
  'compare': {'br': 'In Brazil, friends often just show up and the host does the cooking; a guest may arrive later than the invitation time.', 'us': 'In the USA, guests usually reply to the invitation and often bring a drink or a snack to share.', 'tip': 'Asking “Can I bring something?” is a kind way to say thank you before the party.', 'ask': 'Do you bring something to a party where you live? What do you bring? Say it in English.'},
  'quiz': [
   {'q': 'Lina says, “Can you come to my party?” You want to go. You say…', 'opts': ['Sure! When is it?', 'Yes, I am party.', 'It is on Saturday.'], 'ans': 0, 'why': 'Accept and ask for the time.'},
   {'q': 'What does RSVP ask you to do?', 'opts': ['Bring a gift', 'Reply', 'Come early'], 'ans': 1, 'why': 'RSVP = please reply.'},
   {'q': 'A host says “A drink or a snack.” You bring…', 'opts': ['A big table', 'A bag of chips', 'Nothing, never'], 'ans': 1, 'why': 'Chips are a typical snack.'}]},
 'reading': {
  'genre': 'Email', 'title': 'Come to my party!',
  'text': [
   'Hi Nia, **it’ll be fun**! I am having a party on Saturday at eight. It is a small party at my house, and I want you to come.',
   'The address is 123 Oak Street in Oakland. **Can I bring something?** you ask. Sure! A drink or a snack is great. I will make pizza and a big cake. A cake with a bowl of fruit is my favorite.',
   'We will play music and dance. Some friends play games. At nine, we will sing “Happy Birthday” and the birthday girl will blow out the candles. We say “**Cheers!**” and raise our cups.',
   'Do you know the old rhyme “Pat-a-Cake”? It is an English nursery rhyme from a play of 1698. Children clap and say, “Bake me a cake as fast as you can.” My little brother loves it, and he will sing it at the party.',
   'Please tell me by Thursday. Can you come? If you can’t, **I’d love to see you next time**. **Thanks for the invite** is all you need to say. **See you Saturday!**'],
  'glossary': [{'w': 'party', 'pt': 'festa'}, {'w': 'address', 'pt': 'endereço'}, {'w': 'snack', 'pt': 'lanche'}, {'w': 'bring', 'pt': 'levar'}, {'w': 'candles', 'pt': 'velas'}, {'w': 'blow out', 'pt': 'soprar'}, {'w': 'rhyme', 'pt': 'rima'}, {'w': 'clap', 'pt': 'bater palmas'}, {'w': 'raise', 'pt': 'levantar'}, {'w': 'next time', 'pt': 'da próxima vez'}],
  'fast': {'q': 'What is this email about?', 'opts': ['A job interview', 'An invitation to a party', 'A trip to the beach'], 'ans': 1, 'why': 'Lina invites Nia to a party.'},
  'scan': [{'q': 'What day is the party?', 'ans': 'Saturday', 'alt': ['on saturday']}, {'q': 'What will Lina make?', 'ans': 'pizza and a cake', 'alt': ['pizza', 'a cake']}, {'q': 'Which year is the Pat-a-Cake play from?', 'ans': '1698', 'alt': []}],
  'tf': [{'s': 'The party is at Lina’s house.', 'ans': True, 'why': '“A small party at my house.”'}, {'s': 'The party starts at nine.', 'ans': False, 'why': 'It starts at eight; they sing at nine.'}, {'s': 'Guests can bring a drink or a snack.', 'ans': True, 'why': '“A drink or a snack is great.”'}, {'s': 'Lina’s sister will sing Pat-a-Cake.', 'ans': False, 'why': 'Her little brother will sing it.'}],
  'order': ['Lina invites Nia to a party.', 'Nia asks what to bring.', 'The guests dance and play games.', 'They sing Happy Birthday.', 'Nia tells Lina by Thursday.'],
  'ctx': [{'sent': 'It’ll be fun, so please come!', 'w': 'fun', 'opts': ['boring', 'enjoyable', 'expensive'], 'ans': 1, 'why': 'Fun = enjoyable.'}, {'sent': 'I want to blow out the candles.', 'w': 'blow out', 'opts': ['put out with air', 'light', 'buy'], 'ans': 0, 'why': 'Blow out = stop a flame with air.'}, {'sent': 'Please tell me by Thursday.', 'w': 'by Thursday', 'opts': ['after Thursday', 'not later than Thursday', 'only on Thursday'], 'ans': 1, 'why': 'By = not later than.'}],
  'chunkHunt': ['Can I bring something?', 'It’ll be fun!', 'Thanks for the invite.', 'See you Saturday!'],
  'think': 'What do you do at a party? Do you bring something? Tell a friend in three sentences.'},
 'convo': {'npc': {'name': 'Lina'}, 'story': 'Your friend Lina invites you to a party in Oakland. Reply like a good guest.',
  'turns': [
   {'npc': 'Hi! Can you come to my party?', 'pt': 'Oi! Você pode vir à minha festa?', 'opts': [
    {'en': 'I am party, thanks.', 'pt': 'Eu sou festa, valeu.', 'ok': False, 'fb': 'Not a reply. Say Sure!'},
    {'en': 'Sure! When is it?', 'pt': 'Claro! Quando é?', 'ok': True, 'fb': 'Accept and ask for the time.'},
    {'en': 'Where I go?', 'pt': 'Onde eu vou?', 'ok': False, 'fb': 'Use Where is it?'}]},
   {'npc': 'It’s on Saturday at eight.', 'pt': 'É no sábado às oito.', 'opts': [
    {'en': 'Where is it?', 'pt': 'Onde é?', 'ok': True, 'fb': 'The natural next question.'},
    {'en': 'Where it is?', 'pt': 'Onde é?', 'ok': False, 'fb': 'Word order: Where is it?'},
    {'en': 'It is on Saturday.', 'pt': 'É no sábado.', 'ok': False, 'fb': 'You repeat; ask the place.'}]},
   {'npc': 'At my house. Here’s the address.', 'pt': 'Na minha casa. Aqui está o endereço.', 'opts': [
    {'en': 'I bring something?', 'pt': 'Eu levo algo?', 'ok': False, 'fb': 'Use Can I bring something?'},
    {'en': 'You are welcome.', 'pt': 'De nada.', 'ok': False, 'fb': 'She did not thank you.'},
    {'en': 'Can I bring something?', 'pt': 'Posso levar alguma coisa?', 'ok': True, 'fb': 'Polite and natural.'}]},
   {'npc': 'Sure! A drink or a snack.', 'pt': 'Claro! Uma bebida ou um lanche.', 'opts': [
    {'en': 'Great. I’ll bring chips.', 'pt': 'Ótimo. Levo salgadinhos.', 'ok': True, 'fb': 'I’ll + verb for a decision now.'},
    {'en': 'I bringing chips.', 'pt': 'Eu levando salgadinhos.', 'ok': False, 'fb': 'Use I’ll bring.'},
    {'en': 'Chips are very.', 'pt': 'Salgadinhos são muito.', 'ok': False, 'fb': 'Incomplete sentence.'}]},
   {'npc': 'See you Saturday!', 'pt': 'Até sábado!', 'opts': [
    {'en': 'Good morning!', 'pt': 'Bom dia!', 'ok': False, 'fb': 'This is a goodbye.'},
    {'en': 'See you! Thanks for the invite.', 'pt': 'Até lá! Obrigado pelo convite.', 'ok': True, 'fb': 'Thank the host.'},
    {'en': 'I see you Saturday.', 'pt': 'Eu vejo você sábado.', 'ok': False, 'fb': 'Use See you Saturday.'}]}]},
 'errors': [
  {'wrong': 'I can to go to your party.', 'fix': 'I can go to your party.', 'alt': 'I can going to your party.', 'why': 'After can, use the base verb without to.'},
  {'wrong': 'The party is in Saturday.', 'fix': 'The party is on Saturday.', 'alt': 'The party is at Saturday.', 'why': 'Use on with days.'},
  {'wrong': 'Where it is?', 'fix': 'Where is it?', 'alt': 'Where it are?', 'why': 'Questions put is before it.'},
  {'wrong': 'I bring a snack, I think.', 'fix': 'I’ll bring a snack.', 'alt': 'I will to bring a snack.', 'why': 'I’ll + base verb for an offer.'}],
 'homework': 'Write a short invitation to a party (day, time, place) and a polite reply, and send them to your teacher.',
 'homework_items': ['Write an invitation: day, time, place.', 'Write a reply: yes or no, politely.', 'Shadow the dialogue with Lina.', 'Review: Can you come? / Can I bring something? / See you Saturday!']}
