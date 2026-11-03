"""Suplemento Quest v5 · aula 15: Texting a friend + regular A letter every week (Daddy-Long-Legs)."""
def o(en, pt, ok, fb):
    return {'en': en, 'pt': pt, 'ok': ok, 'fb': fb}

SUPP = {
    'reg': 109,
    'badge': {'icon': '💬', 'name': 'Text Pro', 'desc': 'Make plans with a friend by text in English'},
    'sticker': {'cat': 'Everyday culture', 'title': 'Texting in English', 'sub': 'Are you free tonight?'},
    'culture': {
        'hook': 'Texting is how many friends make plans in the USA. Short words and quick replies are normal, so learn the most common ones.',
        'facts': [
            {'vis': 'prop:clock', 'big': 'LOL', 'label': 'Laughing out loud', 'sub': 'Used when something is funny.'},
            {'vis': 'prop:clock', 'big': 'BRB', 'label': 'Be right back', 'sub': 'You leave the chat for a short time.'},
            {'vis': 'prop:clock', 'big': 'TTYL', 'label': 'Talk to you later', 'sub': 'A friendly way to end a chat.'},
            {'vis': 'prop:cup', 'big': 'Pizza', 'label': 'A classic meet-up', 'sub': 'Friends often share a pizza near a park or after school.'},
        ],
        'polite': 'To invite someone, say **Are you free tonight?** and **Let’s…**. To accept, say **Sounds great!**',
        'mythfact': [
            {'s': 'LOL means “laugh out loud”.', 'ans': True, 'why': 'It is common in texts and chats.'},
            {'s': 'TTYL means “talk to you later”.', 'ans': True, 'why': 'People use it to say goodbye in a chat.'},
            {'s': 'Americans never send text messages.', 'ans': False, 'why': 'Texting is very common among friends and families.'},
            {'s': 'BRB means “bring red beans”.', 'ans': False, 'why': 'BRB = be right back.'},
            {'s': 'Daddy-Long-Legs is a novel made of letters.', 'ans': True, 'why': 'It was written by Jean Webster and published in 1912.'},
        ],
        'wild': [
            {'kind': 'Group chat', 'lines': ['**Cole:** Pizza at 7? Joe’s Pizza near the park.', '**Mia:** Sounds great! See you there.', '**Cole:** Can’t wait!'], 'decode': {'q': 'Where do they meet?', 'opts': ['At Joe’s Pizza', 'At the park gate at 8', 'At Mia’s house'], 'ans': 0, 'why': '“Joe’s Pizza near the park.”'}},
            {'kind': 'Short text', 'lines': ['Running late! BRB.', 'Order for me, please.', 'TTYL!'], 'decode': {'q': 'What does the person say?', 'opts': ['They are running late', 'They are at the restaurant', 'They are cooking'], 'ans': 0, 'why': '“Running late!”'}},
        ],
        'compare': {
            'br': 'In Brazil many people laugh in texts with “kkkk” and use voice messages a lot.',
            'us': 'In the USA people often write “LOL” or “haha” and often type short messages, though voice notes are common too.',
            'tip': 'Keep texts short and clear: where, when and who.',
            'ask': 'Write a text to a friend in English: invite him or her to eat pizza tonight.',
        },
        'quiz': [
            {'q': 'You want to invite a friend. You write…', 'opts': ['Are you free tonight?', 'You are free tonight?', 'Free you tonight?'], 'ans': 0, 'why': 'Are you free…? is the natural question.'},
            {'q': 'Your friend says “TTYL!”. It means…', 'opts': ['Talk to you later', 'Time to your life', 'Take that you love'], 'ans': 0, 'why': 'TTYL = talk to you later.'},
            {'q': 'You accept a plan. You write…', 'opts': ['Sounds great!', 'Sound great me!', 'Is sounds!'], 'ans': 0, 'why': 'Sounds great! accepts a plan.'},
        ],
    },
    'reading': {
        'genre': 'Short story',
        'title': 'From letters to texts',
        'text': [
            'Chloe lives in **Nashville**. Last night her friend Cole sent a text: “**Are you free tonight?**” She wrote back, “Yes! What’s up?” “Let’s get pizza at seven,” he said. “At Joe’s Pizza, near the park.”',
            'Chloe smiled. Then she thought of a book she loves, “Daddy-Long-Legs.” An American writer, Jean Webster, wrote it in 1912. In the book, a girl named Judy writes a letter every month to a man she does not know. Each letter starts with **Dear…**. The man never writes back, but Judy tells him about her life.',
            'Today we do not wait for the mail. We send a text, and our friend answers in seconds. But the old words still work. When Chloe writes a long note to her aunt, she ends it with **Write back soon**. When her aunt sends a gift, she says, “**It’s in the mail**!”',
            'At seven Chloe walked to the park. Cole and Mia were at the pizza place. “**Can’t wait!**” Cole had said that afternoon, and now he was happy. They ate, laughed and took photos of the big pizza.',
            'Chloe writes a letter and a text. Both are good. A letter feels slow and special. A text is quick and fun. Which one do you like?',
        ],
        'glossary': [{'w': 'sent', 'pt': 'enviou'}, {'w': 'text', 'pt': 'mensagem de texto'}, {'w': 'letter', 'pt': 'carta'}, {'w': 'mail', 'pt': 'correio'}, {'w': 'aunt', 'pt': 'tia'}, {'w': 'gift', 'pt': 'presente'}, {'w': 'park', 'pt': 'parque'}, {'w': 'slow', 'pt': 'lento'}, {'w': 'special', 'pt': 'especial'}],
        'fast': {'q': 'What is this text about?', 'opts': ['Making plans by text and writing letters', 'A flight to Nashville', 'A school lesson'], 'ans': 0, 'why': 'Chloe makes plans by text and thinks about letters.'},
        'scan': [
            {'q': 'What time do they eat pizza?', 'ans': 'seven', 'alt': ['7', '7:00', 'at seven']},
            {'q': 'What is the name of the pizza place?', 'ans': 'Joe’s Pizza', 'alt': ['joe\'s pizza', 'joes pizza', 'Joe\'s Pizza']},
            {'q': 'In which year did Jean Webster write the book?', 'ans': '1912', 'alt': ['in 1912']},
        ],
        'tf': [
            {'s': 'Chloe lives in Nashville.', 'ans': True, 'why': '“Chloe lives in Nashville.”'},
            {'s': 'Cole asks Chloe to meet at ten.', 'ans': False, 'why': 'He says, “Let’s get pizza at seven.”'},
            {'s': 'Judy writes a letter every month in the book.', 'ans': True, 'why': 'She writes a letter every month to a man she does not know.'},
            {'s': 'The man answers Judy’s letters.', 'ans': False, 'why': 'The man never writes back.'},
        ],
        'order': ['Cole texts Chloe.', 'Chloe says yes.', 'Chloe thinks about letters.', 'Chloe walks to the park.', 'They eat pizza and take photos.'],
        'ctx': [
            {'sent': 'She sent a text to her friend.', 'w': 'sent', 'opts': ['made someone receive', 'lost', 'erased'], 'ans': 0, 'why': 'Sent = past of send.'},
            {'sent': 'It is a special day for me.', 'w': 'special', 'opts': ['not ordinary, very good', 'very bad', 'very small'], 'ans': 0, 'why': 'Special = different and important.'},
            {'sent': 'My aunt lives in Texas.', 'w': 'aunt', 'opts': ['mother’s or father’s sister', 'a friend’s dog', 'a teacher'], 'ans': 0, 'why': 'An aunt is the sister of your mother or father.'},
        ],
        'chunkHunt': ['Are you free tonight?', 'Dear…', 'Write back soon.', 'It’s in the mail.', 'Can’t wait!'],
        'think': 'Do you prefer to send a letter or a text? Why?',
    },
    'convo': {
        'npc': {'name': 'Cole'},
        'story': 'Cole texts you. Make a plan to eat pizza at seven.',
        'turns': [
            {'npc': 'Hey! Are you free tonight?', 'pt': 'Ei! Você está livre hoje à noite?', 'opts': [
                o('Yes! What’s up?', 'Estou! O que foi?', True, 'Natural reply to a text.'),
                o('Yes, I am free today night.', 'Sim, estou livre hoje noite.', False, 'Say tonight, not today night.'),
                o('No, I am not tonight.', 'Não, eu não sou hoje à noite.', False, 'Say No, I’m busy.')]},
            {'npc': 'Let’s get pizza at seven.', 'pt': 'Vamos comer pizza às sete.', 'opts': [
                o('Is good, where?', 'É bom, onde?', False, 'Say Sounds great! Where?'),
                o('Sounds great! Where?', 'Ótimo! Onde?', True, 'Accept and ask a question.'),
                o('I want pizza seven.', 'Eu quero pizza sete.', False, 'Not a complete sentence.')]},
            {'npc': 'At Joe’s Pizza, near the park.', 'pt': 'Na Joe’s Pizza, perto do parque.', 'opts': [
                o('OK. I’ll be there.', 'Ok. Eu chego lá.', True, 'I’ll be there = I will come.'),
                o('OK. I am there.', 'Ok. Eu estou lá.', False, 'Use I’ll be there for a plan.'),
                o('OK. Pizza is round.', 'Ok. Pizza é redonda.', False, 'Out of context.')]},
            {'npc': 'Can you text Mia too?', 'pt': 'Pode mandar mensagem pra Mia também?', 'opts': [
                o('Sure. See you at seven!', 'Claro. Até as sete!', True, 'Say yes and confirm the time.'),
                o('Sure. I text her yesterday.', 'Claro. Eu mandei ontem.', False, 'Wrong time. Say I’ll text her.'),
                o('No, Mia is a pizza.', 'Não, Mia é uma pizza.', False, 'Funny, but not helpful.')]},
            {'npc': 'Can’t wait! See you!', 'pt': 'Mal posso esperar! Até lá!', 'opts': [
                o('TTYL! Bye!', 'Falamos depois! Tchau!', False, 'You will see him soon. Say See you!'),
                o('Me too! See you!', 'Eu também! Até lá!', True, 'Matching his excitement.'),
                o('I cannot waiting.', 'Eu não posso esperando.', False, 'Say Me too! or I can’t wait.')]},
        ],
    },
    'errors': [
        {'wrong': 'You are free tonight?', 'fix': 'Are you free tonight?', 'alt': 'Do you free tonight?', 'why': 'Questions with be: Are you…?'},
        {'wrong': 'Let’s to get pizza.', 'fix': 'Let’s get pizza.', 'alt': 'Let’s getting pizza.', 'why': 'After Let’s use the base verb: get.'},
        {'wrong': 'I send you a text yesterday.', 'fix': 'I sent you a text yesterday.', 'alt': 'I sended you a text yesterday.', 'why': 'Send is irregular: sent.'},
        {'wrong': 'I see you at seven.', 'fix': 'See you at seven!', 'alt': 'I will seeing you at seven.', 'why': 'See you at… is the set phrase.'},
        {'wrong': 'We meet in the 7.', 'fix': 'We meet at seven.', 'alt': 'We meet on seven.', 'why': 'Use at before a clock time.'},
    ],
    'homework': 'Write a text in English to a friend inviting him or her to do something tonight, and read it aloud in a short audio.',
    'homework_items': ['Write 3 texts: invite, accept, say goodbye.', 'Learn LOL, BRB and TTYL.', 'Listen to the dialogue again and shadow Cole.', 'Review: Are you free tonight? / Sounds great! / Can’t wait!'],
}
