"""Suplemento Quest v5 · aula 71: Wi-Fi and internet + regular Search it online (Marie Kondo)."""
SUPP = {
 'reg': 166,
 'badge': {'icon': '📶', 'name': 'Wi-Fi Fixer', 'desc': 'Ask for the password and fix a simple internet problem'},
 'culture': {
  'hook': 'In the USA, almost every home, hotel and cafe has Wi-Fi. Learn how to ask for the password and what to say when the internet stops working.',
  'mythfact': [
   {'s': 'Wi-Fi stands for "Wireless Fidelity".', 'ans': False, 'why': 'It is only a brand name. The "Wireless Fidelity" idea is a common myth.'},
   {'s': 'The Wi-Fi password is often written on a sticker on the router.', 'ans': True, 'why': 'Many routers have the network name and the password on the back or bottom.'},
   {'s': 'Public Wi-Fi in a cafe is always safe for your bank account.', 'ans': False, 'why': 'Public networks can be risky. Many people avoid banking on them.'},
   {'s': 'Turning the router off and on again can fix a small problem.', 'ans': True, 'why': 'It is the first tip from many internet companies.'},
   {'s': 'Libraries in many US cities offer free Wi-Fi.', 'ans': True, 'why': 'Free Wi-Fi is a common service in public libraries.'}],
  'wild': [
   {'kind': 'Sign in a cafe', 'lines': ['**FREE WI-FI** for customers', 'Network: **BlueBean_Guest**', 'Password: ask at the counter'], 'decode': {'q': 'How do you get the password?', 'opts': ['Ask at the counter', 'Look on the menu', 'Pay five dollars'], 'ans': 0, 'why': 'The sign says: "Password: ask at the counter".'}},
   {'kind': 'Text from a neighbor', 'lines': ['Hi! The internet is down again.', 'The light on my router is red.', 'Can you come and look? Thanks!'], 'decode': {'q': 'What color is the light?', 'opts': ['Red', 'Green', 'Blue'], 'ans': 0, 'why': '"The light on my router is red."'}}],
  'compare': {'br': 'In Brazil, many people also ask "Qual é a senha do Wi-Fi?" in cafes, bars and friends\' homes, and the password is often on a small card or on the wall.', 'us': 'In the USA it is the same: guests ask politely, and the host says the network name and the password slowly, letter by letter if needed.', 'tip': 'Ask, "What\'s the Wi-Fi password?" and repeat it back to be sure.', 'ask': 'How do you ask for the Wi-Fi password where you live? Say it in English.'},
  'quiz': [
   {'q': 'You are at a friend\'s home. You want to use the internet. You say...', 'opts': ['What\'s the Wi-Fi password?', 'Give me your phone now.', 'Where is the Wi-Fi food?'], 'ans': 0, 'why': 'This is the natural question for a guest.'},
   {'q': 'The internet does not work. A simple first step is...', 'opts': ['Turn the router off and on again', 'Throw the router away', 'Wait one year'], 'ans': 0, 'why': 'Restarting the router often fixes small problems.'},
   {'q': 'The light on the router is red. This usually means...', 'opts': ['There may be a problem', 'Everything is perfect', 'It is a party light'], 'ans': 0, 'why': 'The colors depend on the router, but red often means a problem.'}]},
 'reading': {
  'genre': 'Blog post',
  'title': 'No internet in Miami',
  'text': [
   'My name is Lia and I live in **Miami**. Last Saturday my friend Cole came to my apartment. He had his laptop and a lot of work to do.',
   '"Hi! **What\'s the Wi-Fi password?**" he asked. "**It\'s on the router**," I said. He looked at the small box and typed the password. Then he said, "**It doesn\'t work.**"',
   'I said, "**Let me check.** Is the light green?" Cole looked again. "No, **it\'s red**," he said. I smiled. "**The Wi-Fi is down!** Don\'t worry. **Try resetting it.** Turn it off and on again."',
   'We turned the router off. We counted to ten. Then we turned it on and waited. After a minute, the light was green. "**Now it works!**" Cole said. "**You\'re a genius!**"',
   'I am not a genius. Before he came, I looked it up online: "internet down, what to do?" A website told me to restart the router. That is how I learned the trick.',
   'Now Cole is happy. The internet is fast again, and he can work. Next time, I will write the password on a card for my guests.'],
  'glossary': [{'w': 'router', 'pt': 'roteador'}, {'w': 'laptop', 'pt': 'notebook'}, {'w': 'password', 'pt': 'senha'}, {'w': 'typed', 'pt': 'digitou'}, {'w': 'check', 'pt': 'conferir'}, {'w': 'light', 'pt': 'luz'}, {'w': 'turned', 'pt': 'desligamos (turn off)'}, {'w': 'counted', 'pt': 'contamos'}, {'w': 'website', 'pt': 'site'}, {'w': 'trick', 'pt': 'truque'}],
  'fast': {'q': 'What is this text about?', 'opts': ['Fixing a Wi-Fi problem', 'Cooking dinner', 'A trip to the beach'], 'ans': 0, 'why': 'Lia and Cole fix the internet by restarting the router.'},
  'scan': [{'q': 'Where does Lia live?', 'ans': 'Miami', 'alt': ['in miami']}, {'q': 'What color is the light at first?', 'ans': 'red', 'alt': ['it is red']}, {'q': 'How long do they wait after turning the router on?', 'ans': 'a minute', 'alt': ['one minute', '1 minute', 'minute']}],
  'tf': [
   {'s': 'Cole came to Lia\'s apartment on Saturday.', 'ans': True, 'why': '"Last Saturday my friend Cole came to my apartment."'},
   {'s': 'The password is on the laptop.', 'ans': False, 'why': '"It\'s on the router."'},
   {'s': 'The light is green at first.', 'ans': False, 'why': 'Cole says, "No, it\'s red."'},
   {'s': 'Lia learned the trick on a website.', 'ans': True, 'why': '"A website told me to restart the router."'}],
  'order': ['Cole asks for the Wi-Fi password.', 'He types it, but it does not work.', 'Lia checks the light: it is red.', 'They turn the router off and on.', 'The light is green and the internet works.'],
  'ctx': [
   {'sent': 'Let me check. Is the light green?', 'w': 'check', 'opts': ['look and see', 'break', 'buy'], 'ans': 0, 'why': '"Let me check" = let me look and see.'},
   {'sent': 'The Wi-Fi is down.', 'w': 'down', 'opts': ['not working', 'very fast', 'on the floor'], 'ans': 0, 'why': 'When the Wi-Fi is down, it is not working.'},
   {'sent': 'You\'re a genius!', 'w': 'genius', 'opts': ['a very smart person', 'a bad friend', 'a router'], 'ans': 0, 'why': 'A genius is a very smart person.'}],
  'chunkHunt': ['What\'s the Wi-Fi password?', 'It doesn\'t work.', 'Let me check.', 'Try resetting it.'],
  'think': 'Do you know a simple trick to fix a problem with your phone or computer? Tell it in English.'},
 'convo': {'npc': {'name': 'Cole'}, 'story': 'You are at home in Miami. Your friend Cole is a guest and needs the internet for his laptop.', 'turns': [
  {'npc': 'Hi! What\'s the Wi-Fi password?', 'pt': 'Oi! Qual é a senha do Wi-Fi?', 'opts': [
   {'en': 'It\'s on the router.', 'pt': 'Está no roteador.', 'ok': True, 'fb': 'Natural answer: it is on the router.'},
   {'en': 'I am the password.', 'pt': 'Eu sou a senha.', 'ok': False, 'fb': 'This does not answer the question.'},
   {'en': 'The Wi-Fi is Tuesday.', 'pt': 'O Wi-Fi é terça.', 'ok': False, 'fb': 'No sense. Say where the password is.'}]},
  {'npc': 'It doesn\'t work.', 'pt': 'Não está funcionando.', 'opts': [
   {'en': 'Yes, I like it.', 'pt': 'Sim, eu gosto.', 'ok': False, 'fb': 'It does not answer the problem.'},
   {'en': 'Let me check. Is the light green?', 'pt': 'Deixe-me ver. A luz está verde?', 'ok': True, 'fb': 'Offer to help and ask a simple question.'},
   {'en': 'You work very well.', 'pt': 'Você trabalha muito bem.', 'ok': False, 'fb': '"Work" here is about the Wi-Fi, not about people.'}]},
  {'npc': 'No, it\'s red.', 'pt': 'Não, está vermelha.', 'opts': [
   {'en': 'Turn it off and on again.', 'pt': 'Desligue e ligue de novo.', 'ok': True, 'fb': 'The classic fix for a small problem.'},
   {'en': 'Red is a nice color.', 'pt': 'Vermelho é uma cor bonita.', 'ok': False, 'fb': 'True, but it does not help here.'},
   {'en': 'Turn it on and on.', 'pt': 'Ligue e ligue.', 'ok': False, 'fb': 'The idea is off AND on.'}]},
  {'npc': 'OK. Now it works!', 'pt': 'Ok. Agora funciona!', 'opts': [
   {'en': 'Good morning, Cole.', 'pt': 'Bom dia, Cole.', 'ok': False, 'fb': 'It does not fit the moment.'},
   {'en': 'I don\'t have a router.', 'pt': 'Eu não tenho roteador.', 'ok': False, 'fb': 'You just used it!'},
   {'en': 'Great. Enjoy the internet!', 'pt': 'Ótimo. Aproveite a internet!', 'ok': True, 'fb': 'A friendly way to finish.'}]}]},
 'homework': 'Look at your own router or phone Wi-Fi. Write the network name and say in English how you ask a friend for the password.',
 'homework_items': ['Write 4 sentences about an internet problem and how to fix it.', 'Record yourself saying: What\'s the Wi-Fi password? It doesn\'t work. Let me check.', 'Listen to the dialogue again and shadow Cole.', 'Review: It doesn\'t work. / Let me check. / Turn it off and on again.'],
 'errors': [
  {'wrong': 'The Wi-Fi no works.', 'fix': 'The Wi-Fi doesn\'t work.', 'alt': 'The Wi-Fi not work.', 'why': 'Use doesn\'t + base verb for the present negative.'},
  {'wrong': 'Where is the password of Wi-Fi?', 'fix': 'What\'s the Wi-Fi password?', 'alt': 'What is the password from Wi-Fi?', 'why': 'In English the noun comes first: Wi-Fi password.'},
  {'wrong': 'Turn off it and on.', 'fix': 'Turn it off and on again.', 'alt': 'Turn it off and on.', 'why': 'With a pronoun, put it in the middle: turn it off.'},
  {'wrong': 'The internet is very slowly.', 'fix': 'The internet is very slow.', 'alt': 'The internet is slowly.', 'why': 'After is, use the adjective slow, not slowly.'}]}
