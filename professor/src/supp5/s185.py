"""Suplemento Quest v5 · aula 185: At the dog park + regular Thirteen puppies (One Hundred and One Dalmatians)."""
SUPP = {
 'reg': 124,
 'badge': {'icon': '🐕', 'name': 'Park Friend', 'desc': 'Chat with another dog owner at the dog park'},
 'culture': {
  'hook': 'Dog parks are popular in many American cities. They are a place for dogs to run, and a very easy place for people to start a friendly talk.',
  'mythfact': [
   {'s': 'At a dog park, it is normal to ask the name of someone’s dog.', 'ans': True, 'why': 'Dog names are an easy way to start talking.'},
   {'s': 'You should always ask before you pet someone’s dog.', 'ans': True, 'why': 'Some dogs are shy, and the owner knows best.'},
   {'s': 'Many dog parks have a rule to pick up after your dog.', 'ans': True, 'why': 'Many parks give free bags for this.'},
   {'s': 'All dog parks let dogs run without a leash everywhere.', 'ans': False, 'why': 'Rules change. Many parks have off-leash areas, but you must read the sign.'},
   {'s': '“One Hundred and One Dalmatians” is a story about dogs.', 'ans': True, 'why': 'Dodie Smith wrote the book in 1956, and a famous Disney film came later.'}],
  'wild': [
   {'kind': 'Sign at a dog park', 'lines': ['**Dogs must be friendly.**', 'Pick up after your dog.', 'Children under 12 must stay with an adult.'], 'decode': {'q': 'What must you do after your dog goes?', 'opts': ['Pick it up', 'Leave it', 'Run away'], 'ans': 0, 'why': 'The sign says: Pick up after your dog.'}},
   {'kind': 'Tag on a dog collar', 'lines': ['**Max**', 'If found, call: 555-0123', 'I am friendly!'], 'decode': {'q': 'What is the dog’s name?', 'opts': ['Max', 'Luna', 'Rex'], 'ans': 0, 'why': 'The tag says Max.'}}],
  'compare': {'br': 'In Brazil, many people also meet at squares and parks with dogs, and people often chat about the pets.', 'us': 'In the USA, many cities have fenced dog parks. People ask the dog’s name and age first, and then talk about themselves.', 'tip': 'Say: “What a cute dog! How old is he?”', 'ask': 'How do you start a talk with a dog owner? Say it in English.'},
  'quiz': [
   {'q': 'You like a dog. You say…', 'opts': ['What a cute dog!', 'How cute is dog!', 'This dog is a cute.'], 'ans': 0, 'why': 'What a + adjective + noun.'},
   {'q': 'You ask the age of a dog. You say…', 'opts': ['How old is he?', 'How many years has he?', 'What age is he?'], 'ans': 0, 'why': 'How old is he? is the natural question.'},
   {'q': 'You want your dog to play. You say…', 'opts': ['Can my dog play with him?', 'Can my dog to play with him?', 'Can my dog plays with him?'], 'ans': 0, 'why': 'After can, use the base verb: play.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Max and Luna',
  'text': [
   'It is a sunny Saturday in **Boulder**. Jonah walks into the dog park with his dog, Luna. Luna is small, brown and a little shy. She stays near Jonah and looks at the other dogs.',
   'A young woman, Kim, has a brown and white dog. He runs fast with a green ball. “**Hi! What a cute dog!**” Jonah says. “**Thank you! His name is Max**,” Kim says. “**How old is he?**” “**He’s two years old.**”',
   '“**Is he friendly?**” “**Very! He loves to play.**” Jonah smiles. “**Can my dog play with him?**” “**Sure. What’s your dog’s name?**” “**Luna. She’s shy.**” “**That’s okay. Max is very kind.**”',
   'Max comes slowly and drops the ball near Luna. She sniffs it. Then she runs, and Max runs behind her. Their tails move fast. Jonah and Kim laugh. “**Good boy!**” Kim says. Luna is not shy now.',
   'Kim says her dog is good with other dogs. Jonah thinks about the story “One Hundred and One Dalmatians.” Dodie Smith wrote the book in 1956. It has many puppies, and one family loves them all. Today, there are only two dogs, but the park feels full of **man’s best friend**. Jonah and Kim sit on a bench and talk.'],
  'glossary': [{'w': 'park', 'pt': 'parque'}, {'w': 'shy', 'pt': 'tímido'}, {'w': 'cute', 'pt': 'fofo'}, {'w': 'friendly', 'pt': 'amigável'}, {'w': 'ball', 'pt': 'bola'}, {'w': 'tails', 'pt': 'rabos'}, {'w': 'bench', 'pt': 'banco'}, {'w': 'puppies', 'pt': 'filhotes'}, {'w': 'sniffs', 'pt': 'cheira'}, {'w': 'drops', 'pt': 'solta, deixa cair'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Two dog owners talk and their dogs play', 'A man loses his dog', 'A woman buys a dog'], 'ans': 0, 'why': 'Jonah and Kim talk while Luna and Max play.'},
  'scan': [{'q': 'What is Kim’s dog’s name?', 'ans': 'Max', 'alt': ['his name is Max']}, {'q': 'How old is Max?', 'ans': 'two years old', 'alt': ['two', '2', 'two years']}, {'q': 'Which dog is shy?', 'ans': 'Luna', 'alt': ['Jonah’s dog', 'Jonah dog']}],
  'tf': [{'s': 'Luna is a big and loud dog.', 'ans': False, 'why': 'Luna is small and shy.'}, {'s': 'Max has a green ball.', 'ans': True, 'why': 'He runs with a green ball.'}, {'s': 'Max is not friendly.', 'ans': False, 'why': 'Kim says he is very friendly.'}, {'s': 'At the end, Luna is still shy.', 'ans': False, 'why': 'Luna is not shy now.'}],
  'order': ['Jonah comes to the park.', 'Jonah says the dog is cute.', 'Jonah asks if Luna can play.', 'Max drops the ball near Luna.', 'Jonah and Kim sit and talk.'],
  'ctx': [{'sent': 'Luna is a little shy.', 'w': 'shy', 'opts': ['not very open with others', 'very loud', 'very tall'], 'ans': 0, 'why': 'Shy = quiet with new people or animals.'}, {'sent': 'Max is very friendly.', 'w': 'friendly', 'opts': ['kind to others', 'angry at others', 'afraid of others'], 'ans': 0, 'why': 'Friendly = kind and open.'}, {'sent': 'She sniffs the ball.', 'w': 'sniffs', 'opts': ['smells it', 'eats it', 'throws it'], 'ans': 0, 'why': 'Sniff = smell with the nose.'}],
  'chunkHunt': ['What a cute dog!', 'How old is he?', 'Is he friendly?', 'He loves to play.', 'Can my dog play with him?'],
  'think': 'Do you like dogs? What do you ask a person with a dog?'},
 'convo': {'npc': {'name': 'Jonah'}, 'story': 'You are at the dog park in Boulder with your dog Max. Jonah comes with his dog Luna and talks to you.', 'turns': [
  {'npc': 'Hi! What a cute dog!', 'pt': 'Oi! Que cachorro fofo!', 'opts': [
   {'en': 'Thank you! His name is Max.', 'pt': 'Obrigado! O nome dele é Max.', 'ok': True, 'fb': 'Kind and clear.'},
   {'en': 'Thank you! It is Max name.', 'pt': 'Obrigado! É nome Max.', 'ok': False, 'fb': 'Say His name is Max.'},
   {'en': 'You are welcome!', 'pt': 'De nada!', 'ok': False, 'fb': 'It is not a reply to a compliment.'}]},
  {'npc': 'How old is he?', 'pt': 'Quantos anos ele tem?', 'opts': [
   {'en': 'He has two years.', 'pt': 'Ele tem dois anos.', 'ok': False, 'fb': 'Use is: He is two years old.'},
   {'en': 'He’s two years old.', 'pt': 'Ele tem dois anos.', 'ok': True, 'fb': 'Age uses be.'},
   {'en': 'He is very friendly.', 'pt': 'Ele é muito amigável.', 'ok': False, 'fb': 'It does not answer the age.'}]},
  {'npc': 'Is he friendly?', 'pt': 'Ele é amigável?', 'opts': [
   {'en': 'Very! He loves to play.', 'pt': 'Muito! Ele adora brincar.', 'ok': True, 'fb': 'Good answer with a reason.'},
   {'en': 'Very! He love play.', 'pt': 'Muito! Ele ama brincar.', 'ok': False, 'fb': 'With he, use loves to play.'},
   {'en': 'Yes, he is two.', 'pt': 'Sim, ele tem dois.', 'ok': False, 'fb': 'It does not answer.'}]},
  {'npc': 'Can my dog play with him?', 'pt': 'Meu cachorro pode brincar com ele?', 'opts': [
   {'en': 'No, I am Max.', 'pt': 'Não, eu sou o Max.', 'ok': False, 'fb': 'It does not fit.'},
   {'en': 'Sure. What’s your dog’s name?', 'pt': 'Claro. Qual é o nome do seu cachorro?', 'ok': True, 'fb': 'Says yes and asks back.'},
   {'en': 'Sure. What is your name dog?', 'pt': 'Claro. Qual é seu nome cachorro?', 'ok': False, 'fb': 'Say your dog’s name.'}]},
  {'npc': 'Luna. She’s shy.', 'pt': 'Luna. Ela é tímida.', 'opts': [
   {'en': 'That’s okay. Max is very kind.', 'pt': 'Tudo bem. O Max é muito gentil.', 'ok': True, 'fb': 'Calm and kind.'},
   {'en': 'She is a shy dog of you.', 'pt': 'Ela é um cachorro tímido de você.', 'ok': False, 'fb': 'Wrong structure.'},
   {'en': 'Thank you, I am two.', 'pt': 'Obrigado, eu tenho dois.', 'ok': False, 'fb': 'It does not fit.'}]}]},
 'errors': [
  {'wrong': 'He has two years.', 'fix': 'He’s two years old.', 'alt': 'He has two years old.', 'why': 'In English, age uses be: He is two.'},
  {'wrong': 'It is Max the name.', 'fix': 'His name is Max.', 'alt': 'He name is Max.', 'why': 'Use his or her before name.'},
  {'wrong': 'He love to play.', 'fix': 'He loves to play.', 'alt': 'He love play.', 'why': 'With he or she, the verb takes -s: loves.'},
  {'wrong': 'Can my dog plays with him?', 'fix': 'Can my dog play with him?', 'alt': 'Can my dog to play with him?', 'why': 'After can, use the base verb.'}],
 'homework': 'Write a short dialogue: you meet a person with a dog and ask about the dog.',
 'homework_items': ['Write three questions about a dog.', 'Say aloud: What a cute dog!', 'Listen to the dialogue and shadow Jonah.', 'Review: leash / bone / bark / paw / stick / big.']}
