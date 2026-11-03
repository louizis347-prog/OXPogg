"""Suplemento Quest v5 · aula 14: Hello, who is this? + regular Take a photo, make a call (Black Mirror)."""
def o(en, pt, ok, fb):
    return {'en': en, 'pt': pt, 'ok': ok, 'fb': fb}

SUPP = {
    'reg': 177,
    'badge': {'icon': '📞', 'name': 'Phone Pro', 'desc': 'Start and end a phone call in English'},
    'sticker': {'cat': 'Everyday culture', 'title': 'Phone Calls in the USA', 'sub': 'Hello, who is this?'},
    'culture': {
        'hook': 'A phone call in English follows a small script. If you know the first sentences, you can speak with confidence even when you cannot see the other person.',
        'facts': [
            {'vis': 'prop:coin', 'big': '911', 'label': 'Emergency number', 'sub': 'Call 911 for police, fire or an ambulance in the USA.'},
            {'vis': 'prop:clock', 'big': '+1', 'label': 'Country code', 'sub': 'The USA calling code is +1. Brazil is +55.'},
            {'vis': 'prop:bag', 'big': '10 digits', 'label': 'Phone numbers', 'sub': 'Area code + 7 digits, like (503) 555-0123.'},
            {'vis': 'prop:cup', 'big': 'This is…', 'label': 'Say who you are', 'sub': 'On the phone say “This is Raj”, not “I am Raj”.'},
        ],
        'polite': 'Say **Hi, is Raj there?** and **Who is this?** with a friendly voice. At the end, say **Thanks, bye!**',
        'mythfact': [
            {'s': 'In the USA you call 911 in an emergency.', 'ans': True, 'why': '911 is the national emergency number.'},
            {'s': 'On the phone, you say “I am Raj” to introduce yourself.', 'ans': False, 'why': 'Native speakers say “This is Raj.”'},
            {'s': 'A US phone number has 10 digits with the area code.', 'ans': True, 'why': 'For example: (503) 555-0123.'},
            {'s': 'Brazil’s country code is +1.', 'ans': False, 'why': 'Brazil is +55. The USA is +1.'},
            {'s': '“Hold on” means “wait a moment”.', 'ans': True, 'why': 'You say it when you need a second.'},
        ],
        'wild': [
            {'kind': 'Voicemail greeting', 'lines': ['“Hi, this is Raj.', 'I can’t answer the phone right now.', 'Please leave a message and I’ll call you back later.”'], 'decode': {'q': 'What should you do after the greeting?', 'opts': ['Leave a message', 'Hang up and call 911', 'Wait for Raj to answer'], 'ans': 0, 'why': '“Please leave a message.”'}},
            {'kind': 'Text message', 'lines': ['Sorry, I’m in a meeting.', 'Can I call you back at 5?', 'Thanks!'], 'decode': {'q': 'When will the person call?', 'opts': ['At 5', 'At 7', 'Tomorrow morning'], 'ans': 0, 'why': '“Can I call you back at 5?”'}},
        ],
        'compare': {
            'br': 'In Brazil people answer “Alô?” and often ask “Quem fala?”. The emergency numbers are 190, 192 and 193.',
            'us': 'In the USA people answer “Hello?” and often say “Who’s this?” or “This is…”. The emergency number is 911.',
            'tip': 'Practice three phrases: “Is … there?”, “This is …” and “Can I call you back?”',
            'ask': 'Role-play: call a friend and say who you are. Do it out loud in English.',
        },
        'quiz': [
            {'q': 'You call Raj. He answers. You want to know if it is him. You say…', 'opts': ['Hi, is Raj there?', 'Hi, you are Raj?', 'Hi, I am Raj?'], 'ans': 0, 'why': 'Is … there? is the natural phone question.'},
            {'q': 'You want to say who you are on the phone. You say…', 'opts': ['This is Ana.', 'I am Ana here.', 'Me Ana.'], 'ans': 0, 'why': 'This is + name.'},
            {'q': 'The connection is bad. You say…', 'opts': ['You’re breaking up.', 'You are broken.', 'You break me.'], 'ans': 0, 'why': 'You’re breaking up = the signal is bad.'},
        ],
    },
    'reading': {
        'genre': 'Blog post',
        'title': 'A call from the neighbor',
        'text': [
            'My name is Raj, and I live in **San Jose**. Yesterday I was at home when my phone rang. I did not know the number. I said, “**Hello?**”',
            'A man said, “**Hi, is Raj there?**” “**This is Raj**,” I said. “**Who is this?**” He answered, “It’s your neighbor from 4B. I forgot my key. Can you open the door?” “Sure,” I said. “I’m coming now.”',
            'The call was not easy. The man was outside, and the signal was bad. “**You’re breaking up**,” I said. “**Hold on**.” I went to the window. Now I could hear him. He smiled and took a quick selfie with me at the door, a funny photo for his family.',
            'A British series called “Black Mirror” shows the dark side of phones. In real life, a phone can be very helpful. You **make a call**, you **take a selfie**, or you **hold the phone up** to find a better signal. If you **lose signal**, just go to the window.',
            'The neighbor said, “Thanks, you’re the best!” “**Anytime**,” I said. “**Call me back** later!” And now we are good friends.',
        ],
        'glossary': [{'w': 'rang', 'pt': 'tocou'}, {'w': 'neighbor', 'pt': 'vizinho'}, {'w': 'key', 'pt': 'chave'}, {'w': 'signal', 'pt': 'sinal'}, {'w': 'window', 'pt': 'janela'}, {'w': 'selfie', 'pt': 'selfie'}, {'w': 'series', 'pt': 'série'}, {'w': 'helpful', 'pt': 'útil'}, {'w': 'outside', 'pt': 'do lado de fora'}],
        'fast': {'q': 'What is this text about?', 'opts': ['A phone call from a neighbor', 'A holiday in Europe', 'A recipe'], 'ans': 0, 'why': 'The neighbor calls because he forgot his key.'},
        'scan': [
            {'q': 'Where does the neighbor live?', 'ans': '4B', 'alt': ['in 4B', 'apartment 4B']},
            {'q': 'What city does Raj live in?', 'ans': 'San Jose', 'alt': ['san jose']},
            {'q': 'What did the neighbor forget?', 'ans': 'his key', 'alt': ['key', 'the key']},
        ],
        'tf': [
            {'s': 'Raj knows the number at first.', 'ans': False, 'why': '“I did not know the number.”'},
            {'s': 'The neighbor lives in 4B.', 'ans': True, 'why': '“It’s your neighbor from 4B.”'},
            {'s': 'The signal is good during the whole call.', 'ans': False, 'why': 'Raj says, “You’re breaking up.”'},
            {'s': 'Raj opens the door.', 'ans': True, 'why': 'He says, “I’m coming now.”'},
        ],
        'order': ['Raj’s phone rings.', 'The neighbor asks for Raj.', 'The neighbor says he forgot his key.', 'The signal is bad and Raj goes to the window.', 'Raj opens the door.'],
        'ctx': [
            {'sent': 'My phone rang at ten.', 'w': 'rang', 'opts': ['made a sound', 'broke', 'fell'], 'ans': 0, 'why': 'A phone rings when someone calls.'},
            {'sent': 'The signal is bad here.', 'w': 'signal', 'opts': ['phone or internet connection', 'a street sign', 'a song'], 'ans': 0, 'why': 'The signal is the connection of a phone.'},
            {'sent': 'Please hold on a second.', 'w': 'hold on', 'opts': ['wait', 'run', 'sit down'], 'ans': 0, 'why': 'Hold on = wait.'},
        ],
        'chunkHunt': ['Hi, is Raj there?', 'This is Raj.', 'Who is this?', 'You’re breaking up.', 'Hold on.', 'make a call', 'take a selfie', 'Lose signal.', 'Call me back'],
        'think': 'How do you answer the phone in your language? How would you answer in English?',
    },
    'convo': {
        'npc': {'name': 'Victor'},
        'story': 'You call your neighbor Raj. Victor answers the phone. Be clear and polite.',
        'turns': [
            {'npc': 'Hello?', 'pt': 'Alô?', 'opts': [
                o('Hi, is Raj there?', 'Oi, o Raj está?', True, 'Natural phone question.'),
                o('Hi, I am looking Raj.', 'Oi, eu estou procurando Raj.', False, 'Say I’m looking for Raj, or Is Raj there?'),
                o('Hi, who are Raj?', 'Oi, quem são Raj?', False, 'Wrong question.')]},
            {'npc': 'This is Raj. Who is this?', 'pt': 'É o Raj. Quem fala?', 'opts': [
                o('I am your neighbor from 4B.', 'Eu sou seu vizinho do 4B.', False, 'On the phone, This is… sounds more natural.'),
                o('It’s me neighbor 4B.', 'É eu vizinho 4B.', False, 'Not a correct sentence.'),
                o('It’s your neighbor from 4B.', 'É seu vizinho do 4B.', True, 'Natural: It’s + who you are.')]},
            {'npc': 'Oh, hi! How can I help you?', 'pt': 'Ah, oi! Como posso ajudar?', 'opts': [
                o('Can you open the door? I forgot my key.', 'Pode abrir a porta? Esqueci minha chave.', True, 'Clear request and reason.'),
                o('Open the door, I forget key.', 'Abra a porta, eu esqueço chave.', False, 'Too rude and wrong tense.'),
                o('I am fine, thank you.', 'Estou bem, obrigado.', False, 'It does not answer the question.')]},
            {'npc': 'Sure. I’m coming now.', 'pt': 'Claro. Estou indo agora.', 'opts': [
                o('Thank you very many!', 'Muito obrigado!', False, 'Say Thanks a lot! or Thank you so much!'),
                o('Thanks, you’re the best!', 'Valeu, você é demais!', True, 'Friendly and natural.'),
                o('Yes, I come too.', 'Sim, eu venho também.', False, 'Out of context.')]},
            {'npc': 'Anytime. Bye!', 'pt': 'Quando quiser. Tchau!', 'opts': [
                o('Bye! Call me back later!', 'Tchau! Me ligue depois!', True, 'A natural way to close.'),
                o('Hello again!', 'Olá de novo!', False, 'Hello is for the beginning.'),
                o('Good morning!', 'Bom dia!', False, 'We say goodbye now.')]},
        ],
    },
    'errors': [
        {'wrong': 'I am Raj.', 'fix': 'This is Raj.', 'alt': 'It is I Raj.', 'why': 'On the phone, we say This is + name.'},
        {'wrong': 'Who is speaking?', 'fix': 'Who is this?', 'alt': 'Who speaks?', 'why': 'Who is this? is the usual phone question.'},
        {'wrong': 'I make a call to you later.', 'fix': 'I’ll call you later.', 'alt': 'I will to call you later.', 'why': 'Use will + base verb for a promise.'},
        {'wrong': 'I forget my key.', 'fix': 'I forgot my key.', 'alt': 'I forgotted my key.', 'why': 'Forget is irregular: forgot.'},
        {'wrong': 'Can you open me the door?', 'fix': 'Can you open the door?', 'alt': 'Can you open the door for I?', 'why': 'Do not add me after open.'},
    ],
    'homework': 'Call a friend (or pretend to) and practice the first three sentences of a call in English. Record a 30-second audio.',
    'homework_items': ['Say: “Hi, is … there?” / “This is …”.', 'Write a short voicemail greeting in English.', 'Listen to the dialogue again and shadow Victor.', 'Review: Hold on. / You’re breaking up. / Call me back.'],
}
