"""Suplemento Quest v5 · aula 17: I like, I don't like + regular Spicy or sweet? (The Gingerbread Man)."""
def o(en, pt, ok, fb):
    return {'en': en, 'pt': pt, 'ok': ok, 'fb': fb}

SUPP = {
    'reg': 111,
    'badge': {'icon': '🍳', 'name': 'Taste Talker', 'desc': 'Say what you like and do not like in English'},
    'sticker': {'cat': 'Everyday culture', 'title': 'Likes and Breakfast in the USA', 'sub': 'Do you like it?'},
    'culture': {
        'hook': 'Food is a great way to start a conversation in English. Learn how to say what you like politely, even when you do not like something.',
        'facts': [
            {'vis': 'prop:cup', 'big': 'Eggs + toast', 'label': 'A classic breakfast', 'sub': 'Many people eat eggs with toast, and coffee with milk.'},
            {'vis': 'prop:cup', 'big': 'Not a fan', 'label': 'A soft way to say no', 'sub': '“I’m not a fan of…” sounds kinder than “I hate it.”'},
            {'vis': 'prop:bag', 'big': 'Dearborn', 'label': 'A city in Michigan', 'sub': 'It has a large Arab American community and many famous restaurants.'},
            {'vis': 'prop:umbrella', 'big': 'To each their own', 'label': 'Different tastes', 'sub': 'Say this when your friend likes something different.'},
        ],
        'polite': 'Say **I’m not a fan of…** instead of **I hate…**. Then say **To each their own.**',
        'mythfact': [
            {'s': '“I’m not a fan of spicy food” is a polite way to say you do not like it.', 'ans': True, 'why': 'It is softer than “I hate it.”'},
            {'s': 'Everyone in the USA eats the same breakfast.', 'ans': False, 'why': 'People eat many different things: cereal, eggs, pancakes, toast and more.'},
            {'s': 'Dearborn, Michigan, has a large Arab American community.', 'ans': True, 'why': 'It is well known for its Middle Eastern restaurants and bakeries.'},
            {'s': 'In “The Gingerbread Man” story, the cookie runs away from the oven.', 'ans': True, 'why': 'It runs and says, “You can’t catch me!”'},
            {'s': '“To each their own” means “everybody must like the same thing”.', 'ans': False, 'why': 'It means different people can have different tastes.'},
        ],
        'wild': [
            {'kind': 'Diner menu', 'lines': ['**Breakfast Special · $8**', 'Two eggs · toast · coffee', 'Add bacon +$2 · Add hot sauce: free'], 'decode': {'q': 'How much is the special with bacon?', 'opts': ['$10', '$8', '$12'], 'ans': 0, 'why': '$8 + $2 for bacon = $10.'}},
            {'kind': 'Text message', 'lines': ['Do you like spicy food?', 'I’m not a fan, but I love tacos!', 'Let’s get lunch at Maria’s Tacos.'], 'decode': {'q': 'What does the person love?', 'opts': ['Tacos', 'Hot sauce', 'Eggs'], 'ans': 0, 'why': '“I love tacos!”'}},
        ],
        'compare': {
            'br': 'A common Brazilian breakfast is pão com manteiga, café com leite and fruit, so toast and coffee will feel familiar.',
            'us': 'In the USA breakfast can be eggs, toast, cereal or pancakes, with coffee or juice. People often say “I like it with milk.”',
            'tip': 'Say I like it. Do not forget it: “I like it,” not “I like.”',
            'ask': 'What do you like for breakfast? Say it in English.',
        },
        'quiz': [
            {'q': 'You do not like tea. You say…', 'opts': ['No, I don’t. I like coffee.', 'No, I don’t like.', 'No, I not like.'], 'ans': 0, 'why': 'Use I don’t + answer with another idea.'},
            {'q': 'A kind way to say you do not like spicy food is…', 'opts': ['I’m not a fan of spicy food.', 'Spicy food is bad.', 'I no spicy.'], 'ans': 0, 'why': 'I’m not a fan of… is polite.'},
            {'q': 'Your friend loves hot sauce, but you do not. You say…', 'opts': ['To each their own.', 'I am hot.', 'You are wrong.'], 'ans': 0, 'why': 'To each their own is friendly.'},
        ],
    },
    'reading': {
        'genre': 'Blog post',
        'title': 'Breakfast with my friend Malik',
        'text': [
            'My name is Fatima, and I live in **Dearborn**. Every Saturday I have breakfast with my friend Malik. We always go to the same small diner.',
            '“**Do you like** coffee?” Malik asked me last week. “Yes, I do. I like it with milk,” I said. “And tea?” “**No, I don’t**. I like coffee.” He laughed. “**To each their own**,” he said. He likes tea with honey.',
            'The waiter asked, “What do you like for breakfast?” “I like eggs and toast,” I said. “**Me too**! I love eggs,” said Malik. He also asked for hot sauce. “**I’m not a fan** of spicy food,” I said, “but it’s **my thing** when it is a little sweet!” I do not like it very hot. For Malik, spicy is **his thing**. For me, it is **not my thing**.',
            'That makes me think of the story of the Gingerbread Man. A woman makes a cookie, and he jumps out of the oven. He runs away and says, “Run, run, as fast as you can! You can’t catch me!” He is spicy and sweet, and everybody wants to eat him. “**Yum**!” says the fox in the end.',
            'We finished our eggs and toast. “**I like spicy food**, but not too much,” Malik said. We always eat together on Saturday. It is my favorite day of the week.',
        ],
        'glossary': [{'w': 'diner', 'pt': 'lanchonete americana'}, {'w': 'honey', 'pt': 'mel'}, {'w': 'waiter', 'pt': 'garçom'}, {'w': 'eggs', 'pt': 'ovos'}, {'w': 'toast', 'pt': 'torrada'}, {'w': 'hot sauce', 'pt': 'molho de pimenta'}, {'w': 'spicy', 'pt': 'picante'}, {'w': 'oven', 'pt': 'forno'}, {'w': 'cookie', 'pt': 'biscoito'}, {'w': 'fox', 'pt': 'raposa'}],
        'fast': {'q': 'What is this text about?', 'opts': ['Likes and breakfast with a friend', 'A trip to Europe', 'A job interview'], 'ans': 0, 'why': 'Fatima and Malik talk about food they like.'},
        'scan': [
            {'q': 'What city does Fatima live in?', 'ans': 'Dearborn', 'alt': ['dearborn']},
            {'q': 'What does Fatima like in her coffee?', 'ans': 'milk', 'alt': ['Milk', 'with milk']},
            {'q': 'What does Malik put on his eggs?', 'ans': 'hot sauce', 'alt': ['Hot sauce']},
        ],
        'tf': [
            {'s': 'Fatima likes tea.', 'ans': False, 'why': '“No, I don’t. I like coffee.”'},
            {'s': 'Malik loves eggs.', 'ans': True, 'why': '“I love eggs,” said Malik.'},
            {'s': 'Fatima loves very hot food.', 'ans': False, 'why': 'She says, “I’m not a fan of spicy food.”'},
            {'s': 'They have breakfast on Saturdays.', 'ans': True, 'why': '“Every Saturday I have breakfast with my friend Malik.”'},
        ],
        'order': ['Fatima and Malik go to the diner.', 'Malik asks about coffee and tea.', 'The waiter asks about breakfast.', 'Malik asks for hot sauce.', 'They finish their eggs and toast.'],
        'ctx': [
            {'sent': 'We eat breakfast at a small diner.', 'w': 'diner', 'opts': ['a casual restaurant', 'a hotel', 'a school'], 'ans': 0, 'why': 'A diner is a casual American restaurant.'},
            {'sent': 'This soup is very spicy.', 'w': 'spicy', 'opts': ['hot with pepper', 'cold', 'sweet'], 'ans': 0, 'why': 'Spicy = hot because of pepper.'},
            {'sent': 'The fox says, “Yum!”', 'w': 'Yum', 'opts': ['It tastes good', 'It is cold', 'I am sleepy'], 'ans': 0, 'why': 'Yum! = this tastes good.'},
        ],
        'chunkHunt': ['It’s my thing.', 'Not my thing.', 'Yum!', 'I like spicy food', 'To each their own.', 'I’m not a fan'],
        'think': 'What food is “your thing”? What food is “not your thing”?',
    },
    'convo': {
        'npc': {'name': 'Malik'},
        'story': 'You are in a diner in Dearborn. Malik asks what you like to eat and drink.',
        'turns': [
            {'npc': 'Do you like coffee?', 'pt': 'Você gosta de café?', 'opts': [
                o('Yes, I do. I like it with milk.', 'Gosto. Gosto com leite.', True, 'Use I do and add a detail.'),
                o('Yes, I like.', 'Sim, gosto.', False, 'Say I like it or I do.'),
                o('Yes, I am coffee.', 'Sim, eu sou café.', False, 'Wrong meaning.')]},
            {'npc': 'Do you like tea?', 'pt': 'Você gosta de chá?', 'opts': [
                o('No, I don’t like.', 'Não, eu não gosto.', False, 'Say No, I don’t, or I don’t like it.'),
                o('No, I don’t. I like coffee.', 'Não. Eu gosto de café.', True, 'A clear negative answer.'),
                o('No, I am not tea.', 'Não, eu não sou chá.', False, 'Wrong meaning.')]},
            {'npc': 'What do you like for breakfast?', 'pt': 'O que você gosta no café da manhã?', 'opts': [
                o('I like eggs and toast.', 'Gosto de ovos e torrada.', True, 'I like + noun.'),
                o('I am liking eggs.', 'Estou gostando de ovos.', False, 'Do not use -ing with like.'),
                o('Eggs I like it.', 'Ovos eu gosto.', False, 'Word order is wrong.')]},
            {'npc': 'Me too! I love eggs.', 'pt': 'Eu também! Adoro ovos.', 'opts': [
                o('Me neither!', 'Eu também não!', False, 'Use Me too! when you agree with something positive.'),
                o('Let’s have breakfast together.', 'Vamos tomar café da manhã juntos.', True, 'A friendly suggestion.'),
                o('I loves eggs.', 'Eu ama ovos.', False, 'With I, no -s: I love.')]},
            {'npc': 'See you at breakfast!', 'pt': 'Até o café da manhã!', 'opts': [
                o('See you! Yum!', 'Até lá! Hum!', False, 'Short, but not a normal goodbye.'),
                o('Bye, I go to eat.', 'Tchau, eu vou comer.', False, 'Not a natural phrase.'),
                o('See you! Have a good one!', 'Até lá! Tenha um ótimo dia!', True, 'A natural goodbye.')]},
        ],
    },
    'errors': [
        {'wrong': 'I like very coffee.', 'fix': 'I like coffee very much.', 'alt': 'I very like coffee.', 'why': 'Very much goes after the noun.'},
        {'wrong': 'I no like tea.', 'fix': 'I don’t like tea.', 'alt': 'I not like tea.', 'why': 'Use don’t before like.'},
        {'wrong': 'She like eggs.', 'fix': 'She likes eggs.', 'alt': 'She liking eggs.', 'why': 'He / she / it takes -s.'},
        {'wrong': 'Do you like it the coffee?', 'fix': 'Do you like coffee?', 'alt': 'Do you likes coffee?', 'why': 'No the or it before a general noun.'},
        {'wrong': 'I like it eggs.', 'fix': 'I like eggs.', 'alt': 'I like eggses.', 'why': 'Do not add it before the noun.'},
    ],
    'homework': 'Tell your teacher five things you like and two you do not like, in a 45-second audio in English.',
    'homework_items': ['Say 5 things you like (I like…).', 'Say 2 things you don’t like politely (I’m not a fan of…).', 'Listen to the dialogue again and shadow Malik.', 'Review: Do you like…? / I don’t. / To each their own.'],
}
