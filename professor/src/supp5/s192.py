"""Suplemento Quest v5 · aula 192: Long time no see + regular How are you, really? (Schitt's Creek)."""
SUPP = {
 'reg': 224,
 'badge': {'icon': '👋', 'name': 'Old Friend', 'desc': 'Greet an old friend and share your news'},
 'culture': {
  'hook': 'When people in the USA meet an old friend by chance, they often smile, say a short greeting and share one or two pieces of news. The talk is warm, quick and full of questions.',
  'mythfact': [
   {'s': '“Long time no see” is an informal way to greet someone you have not seen for a while.', 'ans': True, 'why': 'Friends use it a lot, with a smile or a hug.'},
   {'s': '“How have you been?” asks only about today.', 'ans': False, 'why': 'It asks about the whole time since you last met.'},
   {'s': 'In the USA, “What do you do?” usually asks about your job.', 'ans': True, 'why': 'It is a common way to start a conversation.'},
   {'s': 'You must give a long answer to “How have you been?”', 'ans': False, 'why': 'A short, positive answer is normal, like “Great, thanks!”'},
   {'s': '“Schitt’s Creek” is a Canadian comedy series.', 'ans': True, 'why': 'It started in 2015.'}],
  'wild': [
   {'kind': 'Text message', 'lines': ['**Long time no see!**', 'Coffee this Saturday?', 'I miss you!', '— Dina'], 'decode': {'q': 'What does Dina want to do?', 'opts': ['Have coffee on Saturday', 'Go to work', 'Buy a book'], 'ans': 0, 'why': 'She asks, “Coffee this Saturday?”'}},
   {'kind': 'Social media post', 'lines': ['**New job, new city!**', 'I live in Utah now.', 'Say hi if you are near!'], 'decode': {'q': 'Where does the person live now?', 'opts': ['In Utah', 'In Canada', 'In Brazil'], 'ans': 0, 'why': 'The post says “I live in Utah now.”'}}],
  'compare': {'br': 'In Brazil, people often say “Quanto tempo!” with a hug or a kiss on the cheek and ask about the family.', 'us': 'In the USA, friends usually hug, and acquaintances often smile and shake hands. Many people ask about work and new places.', 'tip': 'Say: “Long time no see! How have you been?”', 'ask': 'Who is a friend you miss? Say a sentence about them.'},
  'quiz': [
   {'q': 'You see an old friend. You say…', 'opts': ['Long time no see!', 'Long time no seeing!', 'Long time not see!'], 'ans': 0, 'why': 'The fixed phrase is Long time no see.'},
   {'q': 'You say where you live now. You say…', 'opts': ['I live in Utah now.', 'I am living in Utah since last year.', 'I lives in Utah now.'], 'ans': 0, 'why': 'Live is a state verb: I live.'},
   {'q': 'You say when it started. You say…', 'opts': ['Since last year.', 'Since one year.', 'From last year.'], 'ans': 0, 'why': 'Since + a time in the past: since last year.'}]},
 'reading': {
  'genre': 'Short story',
  'title': 'Is that you, Mark?',
  'text': ['Mark sits in a cafe in Salt Lake City. He waits for his coffee and looks at his phone. A woman at the next table looks at him for a long time. “**Oh my gosh! Is that you, Mark?**”', 'It is Dina, an old friend from school. “**Dina! Long time no see!**” Mark says. “**How have you been?**” “Great! **I live in Utah now.**” “**Really? Since when?**”', '“**Since last year. I got a new job.**” “**That’s wonderful. What do you do?**” “**I’m a graphic designer. And you?**” “**I teach English.**” Dina is married now, and she has a son.', 'Mark laughs and says, “I feel like the family in ‘Schitt’s Creek.’” It is a Canadian comedy series from 2015. A rich family loses its money and moves to a small town. At first they are sad, but later they are happy.', 'The two friends talk for an hour. Before they go, they give each other a big hug. “**I miss you**,” Dina says. “**Let’s keep in touch**,” says Mark. They share their phone numbers and smile.'],
  'glossary': [{'w': 'friend', 'pt': 'amigo'}, {'w': 'wonderful', 'pt': 'maravilhoso'}, {'w': 'married', 'pt': 'casada'}, {'w': 'hug', 'pt': 'abraço'}, {'w': 'miss', 'pt': 'sentir saudade'}, {'w': 'touch', 'pt': 'contato'}, {'w': 'rich', 'pt': 'rica'}, {'w': 'small', 'pt': 'pequena'}],
  'fast': {'q': 'What is this story about?', 'opts': ['Two old friends meet by chance in a cafe', 'A man looks for a new job', 'A woman teaches a class'], 'ans': 0, 'why': 'Mark and Dina meet in a cafe.'},
  'scan': [{'q': 'Where do they meet?', 'ans': 'in a cafe', 'alt': ['cafe', 'a cafe', 'in Salt Lake City']}, {'q': 'What is Mark’s job?', 'ans': 'graphic designer', 'alt': ['a graphic designer', 'designer']}, {'q': 'What does Dina teach?', 'ans': 'English', 'alt': ['she teaches English']}],
  'tf': [{'s': 'Dina is an old friend from school.', 'ans': True, 'why': 'The text says so.'}, {'s': 'Mark lives in Utah now.', 'ans': True, 'why': 'He says “I live in Utah now.”'}, {'s': 'Dina is a graphic designer.', 'ans': False, 'why': 'Mark is the designer. Dina teaches English.'}, {'s': 'They never talk again.', 'ans': False, 'why': 'They share their phone numbers.'}],
  'order': ['Mark waits for his coffee.', 'Dina says, “Is that you, Mark?”', 'Mark says he lives in Utah.', 'They talk about their jobs.', 'They hug and share phone numbers.'],
  'ctx': [{'sent': 'That’s wonderful.', 'w': 'wonderful', 'opts': ['very good', 'very small', 'very late'], 'ans': 0, 'why': 'Wonderful means very good.'}, {'sent': 'Dina is married now.', 'w': 'married', 'opts': ['has a husband or wife', 'has a new job', 'lives in Utah'], 'ans': 0, 'why': 'Married means you have a husband or wife.'}, {'sent': 'They give each other a big hug.', 'w': 'hug', 'opts': ['arms around a person', 'a phone call', 'a cup of coffee'], 'ans': 0, 'why': 'A hug is when you hold someone with your arms.'}],
  'chunkHunt': ['Long time no see!', 'How have you been?', 'I live in Utah now.', 'Let’s keep in touch.'],
  'think': 'Who is a friend you do not see often? What do you want to tell that person?'},
 'convo': {'npc': {'name': 'Aaron'}, 'story': 'You meet an old friend in a cafe. You have not seen each other for a long time.', 'turns': [
  {'npc': 'Oh my gosh! Is that you, Mark?', 'pt': 'Meu Deus! É você, Mark?', 'opts': [
   {'en': 'Dina! Long time no see!', 'pt': 'Dina! Quanto tempo!', 'ok': True, 'fb': 'A warm greeting for an old friend.'},
   {'en': 'No, I am not a Mark.', 'pt': 'Não, eu não sou um Mark.', 'ok': False, 'fb': 'It is not friendly or natural.'},
   {'en': 'Dina! Long time no seeing!', 'pt': 'Dina! Muito tempo sem ver!', 'ok': False, 'fb': 'The phrase is fixed: no see.'}]},
  {'npc': 'How have you been?', 'pt': 'Como você tem estado?', 'opts': [
   {'en': 'I am fine since two years.', 'pt': 'Estou bem há dois anos.', 'ok': False, 'fb': 'It mixes time words in a wrong way.'},
   {'en': 'It is a cafe.', 'pt': 'É um café.', 'ok': False, 'fb': 'It does not answer the question.'},
   {'en': 'Great! I live in Utah now.', 'pt': 'Ótimo! Moro em Utah agora.', 'ok': True, 'fb': 'Short, positive and gives news.'}]},
  {'npc': 'Really? Since when?', 'pt': 'Sério? Desde quando?', 'opts': [
   {'en': 'Since last year. I got a new job.', 'pt': 'Desde o ano passado. Arrumei um emprego novo.', 'ok': True, 'fb': 'Since + time, then the reason.'},
   {'en': 'Since I am here.', 'pt': 'Desde que estou aqui.', 'ok': False, 'fb': 'It does not say when.'},
   {'en': 'I am living here since last year.', 'pt': 'Estou morando aqui desde o ano passado.', 'ok': False, 'fb': 'Use I live here, not am living.'}]},
  {'npc': 'That’s wonderful. What do you do?', 'pt': 'Que maravilha. O que você faz?', 'opts': [
   {'en': 'I do a graphic designer.', 'pt': 'Eu faço um designer gráfico.', 'ok': False, 'fb': 'Use am: I am a designer.'},
   {'en': 'I’m a graphic designer. And you?', 'pt': 'Sou designer gráfico. E você?', 'ok': True, 'fb': 'Names the job and asks back.'},
   {'en': 'I am wonderful, thanks.', 'pt': 'Sou maravilhoso, obrigado.', 'ok': False, 'fb': 'The question is about your work.'}]},
  {'npc': 'I teach English.', 'pt': 'Eu ensino inglês.', 'opts': [
   {'en': 'That is great! I miss you.', 'pt': 'Que ótimo! Sinto sua falta.', 'ok': True, 'fb': 'Friendly reaction to the news.'},
   {'en': 'Thank you, I teach English too.', 'pt': 'Obrigado, eu ensino inglês também.', 'ok': False, 'fb': 'You are a designer, not a teacher.'},
   {'en': 'No, I do not teach.', 'pt': 'Não, eu não ensino.', 'ok': False, 'fb': 'It sounds rude and does not react.'}]}]},
 'errors': [
  {'wrong': 'I am living in Utah since last year.', 'fix': 'I live in Utah. I moved last year.', 'alt': 'I live in Utah since last year.', 'why': 'Live is a state verb, so use I live for where you stay.'},
  {'wrong': 'Long time no seeing!', 'fix': 'Long time no see!', 'alt': 'Long time not see!', 'why': 'It is a fixed phrase.'},
  {'wrong': 'I am graphic designer.', 'fix': 'I am a graphic designer.', 'alt': 'I do graphic designer.', 'why': 'Use a before a job.'},
  {'wrong': 'I work how a teacher.', 'fix': 'I work as a teacher.', 'alt': 'I work like teacher.', 'why': 'Use as for a job.'}],
 'homework': 'Write a short dialogue with an old friend: greet, ask how they have been, and say where you live and what you do.',
 'homework_items': ['Write three news about you.', 'Say aloud: Long time no see!', 'Listen to the dialogue and shadow Aaron.', 'Review: job / hug / news / wonderful.']}
