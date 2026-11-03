"""Suplemento Quest v5 · aula 71: Wi-Fi and internet + regular It's not working (Inspector Gadget)."""
SUPP = {
 'reg': 163,
 'badge': {'icon': '📶', 'name': 'Wi-Fi Fixer', 'desc': 'Ask for a password and fix a connection problem in English'},
 'sticker': {'cat': 'Everyday culture', 'title': 'The Wi-Fi Password', 'sub': 'Is it on the router?'},
 'culture': {
  'hook': 'In many American homes, cafés and hotels, guests ask for the Wi-Fi name and password in the first minutes. Learn the words and the small talk that go with it.',
  'polite': 'Ask first: **“Could I get the Wi-Fi password, please?”** Then say **thanks**. A short **“Sorry to bother you”** is also nice.',
  'mythfact': [
   {'s': 'Many cafés in the USA have a Wi-Fi name and a password on a sign or on the receipt.', 'ans': True, 'why': 'Often the password is on the wall, on the menu or on your receipt, or you can ask the staff.'},
   {'s': 'A router is the box that sends the Wi-Fi signal around the house.', 'ans': True, 'why': 'The router connects your devices to the internet.'},
   {'s': 'Wi-Fi and the internet are exactly the same thing.', 'ans': False, 'why': 'Wi-Fi is a wireless way to connect to the network. The internet is the big network itself.'},
   {'s': '“Turn it off and on again” is a very common first tip for tech problems.', 'ans': True, 'why': 'Restarting a router or phone often fixes small problems, so people say it a lot.'},
   {'s': 'You must always pay to use Wi-Fi in a hotel.', 'ans': False, 'why': 'Many hotels offer free Wi-Fi, but some charge extra. You can check at the front desk.'}],
  'wild': [
   {'kind': 'Café sign', 'lines': ['**Free Wi-Fi for customers**', 'Network: SunnyCafe_Guest', 'Password: coffee2025', 'Please ask us if it is slow.'], 'decode': {'q': 'What is the Wi-Fi password?', 'opts': ['coffee2025', 'SunnyCafe_Guest', 'Free Wi-Fi'], 'ans': 0, 'why': 'The line says “Password: coffee2025”. SunnyCafe_Guest is the network name.'}},
   {'kind': 'Text message', 'lines': ['Hey! The Wi-Fi is down again.', 'Is the light on the router red?', 'Yes. Should I unplug it?', 'Yes, wait ten seconds, then plug it in.'], 'decode': {'q': 'What should the person do first?', 'opts': ['Unplug the router and plug it in again', 'Buy a new phone', 'Call a taxi'], 'ans': 0, 'why': 'The friend says to unplug it, wait, and plug it in again.'}}],
  'compare': {'br': 'In Brazil many people ask “Qual é a senha do Wi-Fi?” in a café or at a friend’s home, and the staff often just tell you the password.', 'us': 'In the USA it is the same, but people often start with “Do you have Wi-Fi?” and then ask for the password. Some places print it on the receipt.', 'tip': 'Say the password slowly, letter by letter. In English, “capital A” means a big letter.', 'ask': 'How do you ask for the Wi-Fi password where you live? Say it in English.'},
  'quiz': [
   {'q': 'You want to connect in a café. You ask…', 'opts': ['What’s the Wi-Fi password, please?', 'Give me internet.', 'I am the password.'], 'ans': 0, 'why': 'What’s the Wi-Fi password, please? is clear and polite.'},
   {'q': 'The Wi-Fi does not work. A friend says…', 'opts': ['Turn it off and on again.', 'Turn it up and down.', 'Eat it off and on.'], 'ans': 0, 'why': 'Turn it off and on again is the common tip.'},
   {'q': 'The router light is red. This usually means…', 'opts': ['There may be a problem', 'Everything is perfect', 'The password is short'], 'ans': 0, 'why': 'On many routers a red light shows a problem, but check the manual for your model.'}]},
 'reading': {
  'genre': 'Short story', 'title': 'The Wi-Fi is down!',
  'text': [
   'Sam works from home in Miami. One morning he opens his laptop and sees a message: “No internet.” He says, “**The Wi-Fi is down!** Ugh, the worst.”',
   'His sister Lia comes in. “What happened?” she asks. “**It’s not working**,” says Sam. “Look at the router! The light is red.” Lia **looks at** the small box and smiles.',
   'She remembers a funny old cartoon, **Inspector Gadget**. It is an animated series from 1983. The detective has many gadgets, but they often do not work, and his clever niece Penny fixes the problem. “Sam,” says Lia, “you are like the inspector today.”',
   'Then she says, “**Turn it off and on again.**” Sam pulls out the plug. They wait ten seconds. Then he plugs it in again. The light is yellow, then green.',
   'Sam opens the laptop. “**Great!** It works!” he shouts. “You’re a genius.” Lia laughs. “No, I just know the first trick.”',
   'Now Sam writes the password on a small card and puts it next to the router. “Next time,” he says, “I can try resetting it by myself.”'],
  'glossary': [{'w': 'router', 'pt': 'roteador'}, {'w': 'laptop', 'pt': 'notebook'}, {'w': 'message', 'pt': 'mensagem'}, {'w': 'plug', 'pt': 'tomada, plugue'}, {'w': 'cartoon', 'pt': 'desenho animado'}, {'w': 'detective', 'pt': 'detetive'}, {'w': 'niece', 'pt': 'sobrinha'}, {'w': 'clever', 'pt': 'esperta'}, {'w': 'trick', 'pt': 'truque, dica'}, {'w': 'password', 'pt': 'senha'}],
  'fast': {'q': 'What is this text about?', 'opts': ['A broken Wi-Fi connection that gets fixed', 'A trip to a museum', 'A new job in a bank'], 'ans': 0, 'why': 'Sam has no internet, and Lia helps him fix the router.'},
  'scan': [{'q': 'What color is the router light at first?', 'ans': 'red', 'alt': ['Red']}, {'q': 'How many seconds do they wait?', 'ans': 'ten', 'alt': ['10', '10 seconds', 'ten seconds']}, {'q': 'What is the name of the cartoon?', 'ans': 'Inspector Gadget', 'alt': ['inspector gadget', 'Gadget']}],
  'tf': [{'s': 'Sam lives in Miami.', 'ans': True, 'why': '“Sam works from home in Miami.”'}, {'s': 'The router light is blue at first.', 'ans': False, 'why': 'The light is red at first.'}, {'s': 'Lia tells Sam to turn the router off and on again.', 'ans': True, 'why': 'She says, “Turn it off and on again.”'}, {'s': 'The Wi-Fi never works again.', 'ans': False, 'why': 'After the restart, the light is green and Sam says, “It works!”'}],
  'order': ['Sam sees the message “No internet.”', 'Lia looks at the red light on the router.', 'Sam pulls out the plug.', 'They wait ten seconds and plug it in again.', 'The light turns green and Sam says, “It works!”'],
  'ctx': [{'sent': 'The Wi-Fi is down, so Sam cannot work.', 'w': 'down', 'opts': ['not working', 'under the table', 'very fast'], 'ans': 0, 'why': 'The Wi-Fi is down = it is not working now.'}, {'sent': 'Penny is a clever girl.', 'w': 'clever', 'opts': ['smart', 'tired', 'angry'], 'ans': 0, 'why': 'Clever = smart.'}, {'sent': 'I know the first trick.', 'w': 'trick', 'opts': ['a useful way to do something', 'a big box', 'a long trip'], 'ans': 0, 'why': 'A trick is a clever, simple way to solve something.'}],
  'chunkHunt': ['The Wi-Fi is down!', 'It’s not working.', 'Look at…', 'Turn it off and on again.', 'Great!'],
  'think': 'What do you do first when your internet does not work? Do you have a trick?'},
 'convo': {'npc': {'name': 'Cole'}, 'story': 'You are at home in Miami. Your neighbor Cole needs the internet. Help him in English.',
  'turns': [
   {'npc': 'Hi! What’s the Wi-Fi password?', 'pt': 'Oi! Qual é a senha do Wi-Fi?', 'opts': [
    {'en': 'It’s on the router.', 'pt': 'Está no roteador.', 'ok': True, 'fb': 'A clear answer to the question.'},
    {'en': 'Yes, I have.', 'pt': 'Sim, eu tenho.', 'ok': False, 'fb': 'It does not answer the question.'},
    {'en': 'The password is in the router inside.', 'pt': 'A senha está no roteador dentro.', 'ok': False, 'fb': 'Unnatural. Say: It’s on the router.'}]},
   {'npc': 'It doesn’t work.', 'pt': 'Não está funcionando.', 'opts': [
    {'en': 'I am sorry, it not works.', 'pt': 'Desculpe, não funciona.', 'ok': False, 'fb': 'Use doesn’t: it doesn’t work.'},
    {'en': 'Let me check. Is the light green?', 'pt': 'Deixe-me ver. A luz está verde?', 'ok': True, 'fb': 'Offer help and ask a simple question.'},
    {'en': 'I like Wi-Fi.', 'pt': 'Eu gosto de Wi-Fi.', 'ok': False, 'fb': 'Off topic.'}]},
   {'npc': 'No, it’s red.', 'pt': 'Não, está vermelha.', 'opts': [
    {'en': 'Turn it off and on again.', 'pt': 'Desligue e ligue de novo.', 'ok': True, 'fb': 'The classic tip.'},
    {'en': 'Turn off it and on again.', 'pt': 'Desligue ele e ligue de novo.', 'ok': False, 'fb': 'Word order: Turn it off.'},
    {'en': 'Red is a nice color.', 'pt': 'Vermelho é uma cor bonita.', 'ok': False, 'fb': 'Off topic.'}]},
   {'npc': 'OK. Now it works!', 'pt': 'Ok. Agora funciona!', 'opts': [
    {'en': 'You are welcome the internet.', 'pt': 'Você é bem-vindo a internet.', 'ok': False, 'fb': 'Say: Great. Enjoy the internet!'},
    {'en': 'No, I do not work.', 'pt': 'Não, eu não trabalho.', 'ok': False, 'fb': 'It does not answer Cole.'},
    {'en': 'Great. Enjoy the internet!', 'pt': 'Ótimo. Aproveite a internet!', 'ok': True, 'fb': 'Friendly and natural.'}]},
   {'npc': 'Done! Thanks for the help.', 'pt': 'Pronto! Valeu pela ajuda.', 'opts': [
    {'en': 'No problem! Anytime.', 'pt': 'Sem problema! Quando quiser.', 'ok': True, 'fb': 'A natural reply to thanks.'},
    {'en': 'Thanks you too.', 'pt': 'Obrigado você também.', 'ok': False, 'fb': 'Cole thanked you; say No problem.'},
    {'en': 'I help the Wi-Fi.', 'pt': 'Eu ajudo o Wi-Fi.', 'ok': False, 'fb': 'Not natural.'}]}]},
 'errors': [
  {'wrong': 'The Wi-Fi not works.', 'fix': 'The Wi-Fi doesn’t work.', 'alt': 'The Wi-Fi isn’t works.', 'why': 'Negative present: doesn’t + base verb.'},
  {'wrong': 'What is the password of the Wi-Fi?', 'fix': 'What’s the Wi-Fi password?', 'alt': 'What is the Wi-Fi’s password of?', 'why': 'English puts the noun before the noun: Wi-Fi password.'},
  {'wrong': 'Turn off it and on again.', 'fix': 'Turn it off and on again.', 'alt': 'Turn it off and again on.', 'why': 'With it, the word goes between turn and off.'},
  {'wrong': 'The internet is slowly.', 'fix': 'The internet is slow.', 'alt': 'The internet are slow.', 'why': 'After be, use an adjective: slow, not slowly.'}],
 'homework': 'Write the name of your Wi-Fi in English and say the steps to fix it when it does not work. Send a 30-second audio to your teacher.',
 'homework_items': ['Say 3 sentences: The Wi-Fi is down. It’s not working. Turn it off and on again.', 'Write the 5 vocabulary words with a picture or a drawing.', 'Listen to the dialogue again and shadow Cole.', 'Review: What’s the password? / Let me check. / Great!']}
