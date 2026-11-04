"""Suplemento Quest v5 · aula 160: Wedding invitation + regular Uncle, aunt, cousin (Heidi)."""
SUPP = {
 'reg': 105,
 'badge': {'icon': '💌', 'name': 'Wedding Guest', 'desc': 'Reply to an invitation: when, where and what to wear'},
 'culture': {
  'hook': 'In the USA, a wedding invitation has the date, the time, the place and often a reply date. Guests also think about what to wear, and many avoid white clothes.',
  'mythfact': [
   {'s': 'Many guests avoid wearing white to a wedding.', 'ans': True, 'why': 'White is traditionally for the bride, so many guests choose another color.'},
   {'s': 'RSVP means “please reply.”', 'ans': True, 'why': 'It comes from French. The couple needs to know if you are coming.'},
   {'s': 'A wedding invitation always arrives one day before the party.', 'ans': False, 'why': 'Invitations often arrive weeks before, and a “Save the date” card can come months before.'},
   {'s': 'Weddings in the USA only happen in churches.', 'ans': False, 'why': 'Many take place in gardens, parks, halls, beaches and other places.'},
   {'s': '“Heidi” is a novel from Switzerland.', 'ans': True, 'why': 'Johanna Spyri wrote it in 1880. Heidi lives with her grandfather in the mountains.'}],
  'wild': [
   {'kind': 'Wedding invitation', 'lines': ['**Ellie and Cole are getting married!**', 'June 10, 4:00 p.m.', 'The Garden at Lake Park', 'RSVP by May 1'], 'decode': {'q': 'What does “RSVP by May 1” ask you to do?', 'opts': ['Reply before May 1', 'Arrive on May 1', 'Bring a cake on May 1'], 'ans': 0, 'why': 'RSVP = please reply.'}},
   {'kind': 'Save the date card', 'lines': ['**Save the date!**', 'Ellie + Cole', 'June 10', 'Invitation to follow'], 'decode': {'q': 'What does “Invitation to follow” mean?', 'opts': ['A real invitation comes later', 'You must follow Cole', 'The party is canceled'], 'ans': 0, 'why': 'The card only gives the date; the invitation arrives later.'}}],
  'compare': {'br': 'In Brazil, a formal invitation also gives date, time and place, and guests often confirm by message.', 'us': 'In the USA, you usually answer by the RSVP date, and many couples have an online gift list.', 'tip': 'Say: “Thanks for inviting me.”', 'ask': 'What do you wear to a wedding? Describe it in English.'},
  'quiz': [
   {'q': 'You want to know what to wear. You ask…', 'opts': ['What should I wear?', 'What I should wear?', 'What wear I should?'], 'ans': 0, 'why': 'In a question, should comes before I.'},
   {'q': 'The invitation says “June tenth, at four o’clock.” What is this?', 'opts': ['the date and time', 'the place', 'the gift'], 'ans': 0, 'why': 'June tenth is the date and four o’clock is the time.'},
   {'q': 'Your friend says, “Nothing white.” It means…', 'opts': ['Do not wear white', 'Wear only white', 'Bring white flowers'], 'ans': 0, 'why': 'Nothing white = no white clothes.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'A letter from Cole',
  'text': [
   'Joy lives in Charleston. Today she gets an invitation in the mail. It is from her cousin Cole. He wants her to come to his wedding.',
   '“**Did you get the invitation?**” Cole asks on the phone. “**Yes! I’m so happy for you**,” Joy says. “**Can you come to the wedding?**” “**Of course. When is it?**” “**June tenth, at four o’clock.**”',
   '“**Where is it?**” “**In a garden near the lake.**” “**What should I wear?**” “**A dress or a suit. Nothing white.**” Joy writes the date on her calendar. She puts a red circle around June tenth.',
   'Her aunt and uncle are coming too. Her little cousin Anna loves a book called “Heidi.” It is a Swiss novel from 1880. Heidi is a young girl who lives with her grandfather in the mountains. Anna says, “We are a big family, like Heidi’s!”',
   'Joy goes shopping for a dress. She finds a green one. It is not white! She also writes a card for Cole and his bride, Ellie. Joy cannot wait for June tenth.'],
  'glossary': [{'w': 'invitation', 'pt': 'convite'}, {'w': 'wedding', 'pt': 'casamento'}, {'w': 'cousin', 'pt': 'primo / prima'}, {'w': 'garden', 'pt': 'jardim'}, {'w': 'suit', 'pt': 'terno'}, {'w': 'calendar', 'pt': 'calendário'}, {'w': 'circle', 'pt': 'círculo'}, {'w': 'aunt', 'pt': 'tia'}, {'w': 'bride', 'pt': 'noiva'}, {'w': 'mountains', 'pt': 'montanhas'}],
  'fast': {'q': 'What is this story about?', 'opts': ['A woman gets a wedding invitation', 'A man buys a car', 'A girl goes to school'], 'ans': 0, 'why': 'Joy gets an invitation to Cole’s wedding.'},
  'scan': [{'q': 'When is the wedding?', 'ans': 'June tenth', 'alt': ['June 10', 'on June tenth']}, {'q': 'Where is the wedding?', 'ans': 'in a garden near the lake', 'alt': ['a garden', 'garden near the lake', 'in a garden']}, {'q': 'What color is Joy’s new dress?', 'ans': 'green', 'alt': ['a green one']}],
  'tf': [{'s': 'Cole is Joy’s cousin.', 'ans': True, 'why': 'The invitation is from her cousin Cole.'}, {'s': 'The wedding is at four o’clock.', 'ans': True, 'why': '“June tenth, at four o’clock.”'}, {'s': 'Joy wears a white dress.', 'ans': False, 'why': 'Her dress is green. Nothing white!'}, {'s': 'Joy’s family is not coming.', 'ans': False, 'why': 'Her aunt and uncle are coming too.'}],
  'order': ['Joy gets the invitation.', 'Cole calls her on the phone.', 'Joy writes the date on her calendar.', 'Joy buys a green dress.', 'Joy writes a card for Cole and Ellie.'],
  'ctx': [{'sent': 'She gets an invitation in the mail.', 'w': 'invitation', 'opts': ['a card that asks you to come', 'a small gift', 'a bill'], 'ans': 0, 'why': 'An invitation asks you to come to an event.'}, {'sent': 'She puts a red circle around the date.', 'w': 'circle', 'opts': ['a round line', 'a long road', 'a small box'], 'ans': 0, 'why': 'A circle is a round shape.'}, {'sent': 'She writes a card for his bride.', 'w': 'bride', 'opts': ['the woman who gets married', 'a friend from school', 'a family doctor'], 'ans': 0, 'why': 'The bride is the woman at the wedding.'}],
  'chunkHunt': ['Did you get the invitation?', 'Can you come to the wedding?', 'What should I wear?', 'Nothing white.'],
  'think': 'What do you wear to a special party? Why?'},
 'convo': {'npc': {'name': 'Cole'}, 'story': 'Your cousin Cole is getting married. He calls you about the invitation.', 'turns': [
  {'npc': 'Did you get the invitation?', 'pt': 'Você recebeu o convite?', 'opts': [
   {'en': 'Yes! I’m so happy for you.', 'pt': 'Sim! Estou tão feliz por você.', 'ok': True, 'fb': 'Warm and natural.'},
   {'en': 'Yes! I’m so happy by you.', 'pt': 'Sim! Estou tão feliz por você.', 'ok': False, 'fb': 'Say happy for you.'},
   {'en': 'No, I got a dress.', 'pt': 'Não, eu ganhei um vestido.', 'ok': False, 'fb': 'It does not answer the question.'}]},
  {'npc': 'Can you come to the wedding?', 'pt': 'Você pode ir ao casamento?', 'opts': [
   {'en': 'Of course. When is it?', 'pt': 'Claro. Quando é?', 'ok': True, 'fb': 'Says yes and asks the date.'},
   {'en': 'Of course. When it is?', 'pt': 'Claro. Quando é?', 'ok': False, 'fb': 'In a question: When is it?'},
   {'en': 'Yes, the garden.', 'pt': 'Sim, o jardim.', 'ok': False, 'fb': 'It does not fit.'}]},
  {'npc': 'June tenth, at four o’clock.', 'pt': 'Dez de junho, às quatro horas.', 'opts': [
   {'en': 'In June ten?', 'pt': 'Em junho dez?', 'ok': False, 'fb': 'Use June tenth.'},
   {'en': 'Where is it?', 'pt': 'Onde é?', 'ok': True, 'fb': 'Next useful question: the place.'},
   {'en': 'It is a nice dress.', 'pt': 'É um vestido bonito.', 'ok': False, 'fb': 'Does not fit.'}]},
  {'npc': 'In a garden near the lake.', 'pt': 'Em um jardim perto do lago.', 'opts': [
   {'en': 'What I should wear?', 'pt': 'O que eu devo vestir?', 'ok': False, 'fb': 'Say: What should I wear?'},
   {'en': 'What should I wear?', 'pt': 'O que devo vestir?', 'ok': True, 'fb': 'Correct word order.'},
   {'en': 'Where is the lake?', 'pt': 'Onde é o lago?', 'ok': False, 'fb': 'Possible, but you want to know the clothes.'}]},
  {'npc': 'A dress or a suit. Nothing white.', 'pt': 'Vestido ou terno. Nada branco.', 'opts': [
   {'en': 'That sounds good. See you there!', 'pt': 'Parece bom. Te vejo lá!', 'ok': True, 'fb': 'A friendly ending.'},
   {'en': 'I am white, thanks.', 'pt': 'Sou branco, valeu.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'When is it?', 'pt': 'Quando é?', 'ok': False, 'fb': 'He already told you.'}]}]},
 'errors': [
  {'wrong': 'Did you received the invitation?', 'fix': 'Did you get the invitation?', 'alt': 'You got the invitation?', 'why': 'After did, use the base verb: get (or receive).'},
  {'wrong': 'What I should wear?', 'fix': 'What should I wear?', 'alt': 'What should wear I?', 'why': 'In a question, should comes before I.'},
  {'wrong': 'I’m so happy by you.', 'fix': 'I’m so happy for you.', 'alt': 'I’m so happy with you.', 'why': 'Say happy for someone.'},
  {'wrong': 'The wedding is in June ten.', 'fix': 'The wedding is on June tenth.', 'alt': 'The wedding is at June tenth.', 'why': 'Use on with a date, and say tenth.'}],
 'homework': 'Write a reply to a wedding invitation: thank them, say you can come, and ask what to wear.',
 'homework_items': ['Say aloud: What should I wear?', 'Write the date June tenth and the time four o’clock.', 'Listen to the dialogue and shadow Cole.', 'Review: aunt, uncle, cousin.']}
