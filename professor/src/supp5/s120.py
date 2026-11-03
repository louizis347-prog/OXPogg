"""Suplemento Quest v5 · aula 120: Volunteer day + regular Pick up your toys (Mister Rogers' Neighborhood)."""
SUPP = {
 'reg': 135,
 'badge': {'icon': '🙋', 'name': 'Park Helper', 'desc': 'Join a volunteer day and help clean the park'},
 'culture': {
  'hook': 'In the USA, many people give a few hours to help their community. A park cleanup is a simple example: you get gloves and a bag, pick up trash, and work with neighbors.',
  'mythfact': [
   {'s': 'Volunteers usually work for free.', 'ans': True, 'why': 'A volunteer gives time to help, and often no pay.'},
   {'s': 'In many places, you can join a park cleanup without special skills.', 'ans': True, 'why': 'Most cleanups welcome beginners and give basic instructions.'},
   {'s': 'Volunteers must bring all the tools from home.', 'ans': False, 'why': 'Many events give gloves, bags and sometimes vests.'},
   {'s': 'Many schools and groups in the USA encourage volunteering.', 'ans': True, 'why': 'Schools, churches and clubs often organize volunteer days.'},
   {'s': '“Mister Rogers’ Neighborhood” was a TV show for children.', 'ans': True, 'why': 'Fred Rogers hosted it, and it started in 1968.'}],
  'wild': [
   {'kind': 'Flyer in a library', 'lines': ['**Park Cleanup Day**', 'Saturday, 9 a.m. – 12 p.m.', 'Gloves and bags provided.', 'Wear closed shoes.'], 'decode': {'q': 'What do volunteers get at this event?', 'opts': ['Gloves and bags', 'Lunch and a bike', 'A new hat'], 'ans': 0, 'why': '“Gloves and bags provided.”'}},
   {'kind': 'Sign-in table', 'lines': ['**Volunteers: sign in here**', 'Name, phone, email', 'Take a vest. Team leaders wear green.'], 'decode': {'q': 'Who wears green?', 'opts': ['Team leaders', 'All volunteers', 'Nobody'], 'ans': 0, 'why': '“Team leaders wear green.”'}}],
  'compare': {'br': 'In Brazil, we have “mutirão” days, when neighbors work together for the community.', 'us': 'In the USA, a “volunteer day” can be a cleanup, a food drive or a school project. People often sign in and get a vest or T-shirt.', 'tip': 'Ask: “What can I do?”', 'ask': 'How can you help in your neighborhood? Say it in English.'},
  'quiz': [
   {'q': 'You arrive at a volunteer day. You ask…', 'opts': ['What can I do?', 'What I can do?', 'Do what can I?'], 'ans': 0, 'why': 'What can I + verb is the normal order.'},
   {'q': 'What does “Many hands make light work” mean?', 'opts': ['With more people, the job is easier', 'Hands are very light', 'Work is always hard'], 'ans': 0, 'why': 'Many people together do the work faster.'},
   {'q': 'What is a community?', 'opts': ['people who live or work near each other', 'a kind of trash', 'a big lake'], 'ans': 0, 'why': 'A community is a group of people in the same area.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Rosa’s cleanup day',
  'text': [
   'Today is Volunteer Day in **Sacramento**. Rosa arrives at the park at nine. She wears old shoes and a hat. Many people from the community are there, and a woman with a green vest is the leader.',
   '“**Welcome to Volunteer Day! Are you ready?**” “**Yes! What can I do?**” “**Please pick up trash in the park.**” The leader gives her a bag and says, “**Here are gloves and a bag.**” Rosa puts on the gloves and takes an orange vest.',
   '“**Thank you. Where do I start?**” Rosa asks. “**Start near the lake.**” She sees her friend Tom. “**OK. Can my friend help too?**” “**Of course! More hands, less work.**” Tom puts on gloves. “**Many hands make light work**,” he says.',
   'They pick up bottles, paper and cans. Soon the bags are full. “**We have lots of trash!**” Tom says. Another team plants flowers, and a man rakes the leaves. It is hard work, but everybody smiles. “**Teamwork!**” says the leader.',
   'In the TV show “Mister Rogers’ Neighborhood,” Fred Rogers teaches children to be kind and to help others. Rosa thinks of him. She and Tom **pitch in** all morning. “**It feels great** to **give back**,” she says. At noon, the park is clean.'],
  'glossary': [{'w': 'volunteer', 'pt': 'voluntário'}, {'w': 'community', 'pt': 'comunidade'}, {'w': 'leader', 'pt': 'líder'}, {'w': 'vest', 'pt': 'colete'}, {'w': 'lake', 'pt': 'lago'}, {'w': 'bottles', 'pt': 'garrafas'}, {'w': 'plants', 'pt': 'planta'}, {'w': 'rakes', 'pt': 'varre com rastelo'}, {'w': 'pitch in', 'pt': 'ajudar, colaborar'}, {'w': 'give back', 'pt': 'retribuir à comunidade'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Volunteers clean a park', 'A girl buys a hat', 'A man swims in a lake'], 'ans': 0, 'why': 'Rosa and Tom pick up trash at Volunteer Day.'},
  'scan': [{'q': 'What time does Rosa arrive?', 'ans': 'nine', 'alt': ['9', 'at nine', '9 a.m.']}, {'q': 'Where does Rosa start?', 'ans': 'near the lake', 'alt': ['the lake', 'by the lake']}, {'q': 'Who helps Rosa?', 'ans': 'her friend Tom', 'alt': ['Tom', 'her friend']}],
  'tf': [{'s': 'Rosa is late for Volunteer Day.', 'ans': False, 'why': 'She arrives at nine.'}, {'s': 'The leader gives Rosa gloves and a bag.', 'ans': True, 'why': '“Here are gloves and a bag.”'}, {'s': 'Tom cannot help.', 'ans': False, 'why': 'The leader says, “Of course!”'}, {'s': 'At noon, the park is clean.', 'ans': True, 'why': 'The last line says the park is clean.'}],
  'order': ['Rosa arrives at the park.', 'The leader gives her gloves and a bag.', 'She starts near the lake.', 'Tom joins her.', 'The park is clean.'],
  'ctx': [{'sent': 'The leader wears a green vest.', 'w': 'vest', 'opts': ['a piece of clothing without sleeves', 'a kind of bag', 'a kind of tree'], 'ans': 0, 'why': 'A vest has no sleeves.'}, {'sent': 'We pitch in on Saturday.', 'w': 'pitch in', 'opts': ['help with the work', 'throw a ball', 'sleep late'], 'ans': 0, 'why': 'Pitch in = help.'}, {'sent': 'Many people from the community are here.', 'w': 'community', 'opts': ['neighbors and local people', 'a kind of food', 'a big city'], 'ans': 0, 'why': 'A community is people in the same area.'}],
  'chunkHunt': ['What can I do?', 'Where do I start?', 'Can my friend help too?', 'Many hands make light work.'],
  'think': 'How can you help your community? What can you do this month?'},
 'convo': {'npc': {'name': 'Ms. Cole'}, 'story': 'You arrive at Volunteer Day in the park. Ms. Cole is the leader.', 'turns': [
  {'npc': 'Welcome to Volunteer Day! Are you ready?', 'pt': 'Boas-vindas ao Dia do Voluntário! Está pronto?', 'opts': [
   {'en': 'Yes! What I can do?', 'pt': 'Sim! O que eu posso fazer?', 'ok': False, 'fb': 'Say: What can I do?'},
   {'en': 'No, I am a trash.', 'pt': 'Não, eu sou um lixo.', 'ok': False, 'fb': 'Wrong meaning.'},
   {'en': 'Yes! What can I do?', 'pt': 'Sim! O que posso fazer?', 'ok': True, 'fb': 'Ready and eager.'}]},
  {'npc': 'Please pick up trash in the park. Here are gloves and a bag.', 'pt': 'Por favor, recolha o lixo no parque. Aqui estão luvas e uma sacola.', 'opts': [
   {'en': 'Thank you. Where I start?', 'pt': 'Obrigado. Onde eu começo?', 'ok': False, 'fb': 'Use: Where do I start?'},
   {'en': 'Thank you. Where do I start?', 'pt': 'Obrigado. Por onde começo?', 'ok': True, 'fb': 'Natural next question.'},
   {'en': 'Thank you. I am a bag.', 'pt': 'Obrigado. Eu sou uma sacola.', 'ok': False, 'fb': 'Wrong meaning.'}]},
  {'npc': 'Start near the lake.', 'pt': 'Comece perto do lago.', 'opts': [
   {'en': 'OK. My friend can to help too?', 'pt': 'Ok. Meu amigo pode ajudar também?', 'ok': False, 'fb': 'Say: Can my friend help too?'},
   {'en': 'OK. Start near the lake.', 'pt': 'Ok. Comece perto do lago.', 'ok': False, 'fb': 'She said it. You do not repeat it as an order.'},
   {'en': 'OK. Can my friend help too?', 'pt': 'Ok. Meu amigo pode ajudar também?', 'ok': True, 'fb': 'Polite question.'}]},
  {'npc': 'Of course! More hands, less work.', 'pt': 'Claro! Mais mãos, menos trabalho.', 'opts': [
   {'en': 'Right! Many hands make light work.', 'pt': 'Isso! Muitas mãos tornam o trabalho leve.', 'ok': True, 'fb': 'Agrees with the saying.'},
   {'en': 'Many hand make light work.', 'pt': 'Muita mão faz trabalho leve.', 'ok': False, 'fb': 'Use hands (plural) and make.'},
   {'en': 'I don’t have hands.', 'pt': 'Eu não tenho mãos.', 'ok': False, 'fb': 'It does not fit.'}]},
  {'npc': 'Thank you for helping today!', 'pt': 'Obrigada por ajudar hoje!', 'opts': [
   {'en': 'It’s great give back to the community.', 'pt': 'É ótimo retribuir à comunidade.', 'ok': False, 'fb': 'Say: It feels great to give back.'},
   {'en': 'It feels great to give back.', 'pt': 'É ótimo retribuir.', 'ok': True, 'fb': 'Natural, friendly reply.'},
   {'en': 'Please pick up the trash.', 'pt': 'Por favor, recolha o lixo.', 'ok': False, 'fb': 'That is the leader’s job to say.'}]}]},
 'errors': [
  {'wrong': 'What I can do?', 'fix': 'What can I do?', 'alt': 'What can do I?', 'why': 'In questions, can comes before I.'},
  {'wrong': 'Where I start?', 'fix': 'Where do I start?', 'alt': 'Where I do start?', 'why': 'Use do before I in present questions.'},
  {'wrong': 'Many hand make light work.', 'fix': 'Many hands make light work.', 'alt': 'Many hands makes light work.', 'why': 'Many + plural noun + make.'},
  {'wrong': 'I am volunteer in the park.', 'fix': 'I volunteer in the park.', 'alt': 'I am volunteering in a park yesterday.', 'why': 'Volunteer is also a verb. No need for am.'}],
 'homework': 'Write 3 ways you can help your community, like “I can pick up trash.”',
 'homework_items': ['Write: I can ___ in the park.', 'Say aloud: What can I do?', 'Listen to the dialogue and shadow Victor.', 'Learn: rake, vest, shovel, team.']}
