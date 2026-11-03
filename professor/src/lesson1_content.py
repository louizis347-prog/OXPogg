"""Autoria e apresentação da aula Quest 1, comum aos modos particular e grupo.

O suplemento continua sendo validado por validate_v5.py. A apresentação em passos
curtos conserva leitura, cultura, diálogo, variação, produção e revisão.
"""


def enrich(s):
    s = dict(s)
    s['badge'] = {'icon': '☕', 'name': 'Café com autonomia',
                  'desc': 'Peça, esclareça e encontre seu pedido em inglês.'}
    s['sticker'] = {'cat': 'Cultura em contexto', 'title': 'Café Society × Chicago',
                    'sub': 'Uma obra sobre encontros; uma missão de conversa real.'}
    s['culture'] = {
        'hook': 'A cafeteria pode ser um lugar de encontro e também de pedidos rápidos. Observe como a intenção muda a forma de começar a conversa.',
        'work': {'title': 'Café Society', 'year': '2016',
                 'note': 'O filme retrata encontros e espaços sociais nos Estados Unidos da década de 1930. A obra inspira a pergunta: como iniciar uma conversa? As falas da cafeteria de hoje são autorais, não citações do filme.'},
        'facts': [
            {'big': 'For here / to go', 'label': 'Ficar ou levar', 'sub': 'Uma pergunta frequente ao pedir; a forma exata varia conforme o lugar.'},
            {'big': 'Name on the cup', 'label': 'Identificar o pedido', 'sub': 'Algumas cafeterias anotam o nome, outras usam número ou entregam no balcão.'},
            {'big': 'Pickup counter', 'label': 'Onde retirar', 'sub': 'Se não souber onde pegar a bebida, pergunte: Where is the pickup counter?'},
            {'big': 'Milk options', 'label': 'Pedir uma troca', 'sub': 'Pergunte Do you have oat milk?; se não houver, escolha outra opção.'},
            {'big': 'Tip screen', 'label': 'Gorjeta', 'sub': 'Pode aparecer no pagamento; regras e expectativas variam por serviço e região.'},
        ],
        'polite': '**Can I get…?** é um pedido comum. **Could I get…?** soa um pouco mais cuidadoso. Acrescente **please** quando fizer sentido.',
        'mythfact': [
            {'s': '“To go” indica que você vai levar o pedido.', 'ans': True, 'why': 'É a resposta direta a “For here or to go?” quando você sai com a bebida.'},
            {'s': 'Toda cafeteria norte-americana escreve seu nome no copo.', 'ans': False, 'why': 'Algumas usam nomes, outras números ou entrega direta.'},
            {'s': '“Where is the pickup counter?” pede a localização do balcão de retirada.', 'ans': True, 'why': 'É uma pergunta útil depois de pagar.'},
            {'s': 'Gorjeta no balcão é sempre obrigatória.', 'ans': False, 'why': 'A prática varia; não apresente uma regra única para todo o país.'},
        ],
        'wild': [
            {'kind': 'Menu board', 'lines': ['Small coffee $3.00', 'Oat milk +$0.75', 'Tea $2.50'],
             'decode': {'q': 'How much is a small coffee with oat milk?', 'opts': ['$3.75', '$3.00', '$2.50'], 'ans': 0, 'why': '$3.00 + $0.75 = $3.75.'}},
            {'kind': 'Pickup sign', 'lines': ['ORDER HERE →', 'PICKUP COUNTER ←', 'Please wait for your name or order number.'],
             'decode': {'q': 'Where do you pick up your drink?', 'opts': ['On the left', 'At the order line', 'Outside'], 'ans': 0, 'why': 'The arrow points left to the pickup counter.'}},
        ],
        'compare': {'br': 'No Brasil, o pedido pode ser curto: “Um café, por favor”. O pagamento e a retirada mudam de estabelecimento para estabelecimento.',
                    'us': 'Em muitas cafeterias dos EUA, você escolhe tamanho e retirada, paga e espera pelo nome ou número. O processo também varia.',
                    'tip': 'Compare a função do pedido: saudação, bebida, detalhe, esclarecimento e despedida — sem decorar uma única fórmula cultural.',
                    'ask': 'Como você pediria uma bebida e descobriria onde retirá-la? Faça duas versões em inglês.'},
        'quiz': [
            {'q': 'Você quer levar a bebida. O atendente pergunta “For here or to go?”', 'opts': ['To go, please.', 'For here, please.', 'On the left.'], 'ans': 0, 'why': '“To go” indica levar.'},
            {'q': 'Não entendeu onde retirar. Qual pergunta resolve o problema?', 'opts': ['Do you have tea?', 'Where is the pickup counter?', 'How old is the counter?'], 'ans': 1, 'why': 'Where is…? pede localização.'},
            {'q': 'Não há leite de aveia. Qual resposta mantém o pedido?', 'opts': ['I am oat milk.', 'No, you are wrong.', 'Regular milk is fine, thanks.'], 'ans': 2, 'why': 'Você aceita outra opção com naturalidade.'},
        ],
    }
    s['reading'] = {
        'genre': 'Story', 'title': 'Ana orders coffee in Chicago',
        'text': [
            'It is a cool morning in **Chicago**. Ana is new to the city. She walks into a café near the train station. A sign says **ORDER HERE**. Another sign says **PICKUP ON THE LEFT**. Ana looks at the menu.',
            'Evan, the barista, smiles. “**What can I get for you?**” he asks. Ana says, “**Can I get a small coffee, please?**” Evan asks, “**For here or to go?**” Ana says, “**To go, please.**”',
            'Ana wants milk in her coffee. “**Do you have oat milk?**” she asks. Evan says, “Sorry, not today. We have regular milk.” Ana thinks for a moment. “Regular milk is fine, thanks.” Evan adds it to her order.',
            '“Anything else?” Evan asks. Ana sees a muffin on the **tray**. “No, that’s all. **How much is it?**” she says. “Three dollars,” Evan answers. Ana pays by card. Evan gives her an order number.',
            'Ana sees two counters. She does not know where to wait. “**Where is the pickup counter?**” she asks. “It is **on the left**, near the window,” Evan says. Ana walks there and waits with her order number.',
            'Evan calls her number and gives her the **cup**. Ana checks the order: small coffee, regular milk, to go. “Thanks!” she says. She leaves the café. Now she can order, change a detail and find her drink.',
        ],
        'glossary': [{'w': 'barista', 'pt': 'atendente de café'}, {'w': 'tray', 'pt': 'bandeja'},
                     {'w': 'cup', 'pt': 'copo'}, {'w': 'counter', 'pt': 'balcão'},
                     {'w': 'order number', 'pt': 'número do pedido'}, {'w': 'on the left', 'pt': 'à esquerda'},
                     {'w': 'regular milk', 'pt': 'leite comum'}, {'w': 'to go', 'pt': 'para levar'}],
        'fast': {'q': 'What does Ana do in the café?', 'opts': ['She orders and finds her drink.', 'She studies for a test.', 'She meets a film actor.'], 'ans': 0, 'why': 'She orders, changes one detail and finds the pickup counter.'},
        'scan': [{'q': 'What milk does Ana choose?', 'ans': 'regular milk', 'alt': ['milk'],
                  'opts': ['oat milk', 'regular milk', 'no milk'], 'correct': 1},
                 {'q': 'How much is the order?', 'ans': 'three dollars', 'alt': ['$3', '3 dollars'],
                  'opts': ['five dollars', 'two dollars', 'three dollars'], 'correct': 2},
                 {'q': 'Where is the pickup counter?', 'ans': 'on the left', 'alt': ['left', 'near the window'],
                  'opts': ['on the left', 'outside the café', 'behind the menu'], 'correct': 0}],
        'tf': [{'s': 'Ana asks for a large tea.', 'ans': False, 'why': 'She asks for a small coffee.'},
               {'s': 'The café has oat milk today.', 'ans': False, 'why': 'Evan says they have regular milk, not oat milk.'},
               {'s': 'Ana pays by card.', 'ans': True, 'why': 'The story says Ana pays by card.'},
               {'s': 'The pickup counter is near the window.', 'ans': True, 'why': 'It is on the left, near the window.'}],
        'order': ['Ana sees the menu.', 'She orders a small coffee to go.', 'She chooses regular milk.', 'She pays and gets an order number.', 'She finds the pickup counter.'],
        'ctx': [{'sent': 'Another sign says PICKUP ON THE LEFT.', 'w': 'on the left', 'opts': ['à esquerda', 'à direita', 'lá fora'], 'ans': 0, 'why': 'A seta aponta para a esquerda.'},
                {'sent': 'Evan adds it to her order.', 'w': 'order', 'opts': ['pedido', 'janela', 'gorjeta'], 'ans': 0, 'why': 'Order é o pedido da cliente.'},
                {'sent': 'Ana pays by card.', 'w': 'pays', 'opts': ['paga', 'espera', 'pergunta'], 'ans': 0, 'why': 'Pay é pagar.'}],
        'chunkHunt': ['Can I get…?', 'For here or to go?', 'Do you have…?', 'Where is the pickup counter?'],
        'think': 'What changes if the café has no oat milk? Ask, choose another option and keep the conversation going.',
    }
    s['convo'] = {'npc': {'name': 'Evan', 'face': 'Evan'},
        'story': 'Você está numa cafeteria em Chicago. Faça o pedido, adapte-o e encontre a retirada.',
        'turns': [
            {'npc': 'Hi! What can I get for you?', 'pt': 'Oi! O que vai ser?', 'opts': [
                {'en': 'Can I get a small coffee, please?', 'pt': 'Pode ser um café pequeno, por favor?', 'ok': True, 'fb': 'Pedido claro e cortês.'},
                {'en': 'Give me coffee now.', 'pt': 'Me dê café agora.', 'ok': False, 'fb': 'Soa como uma ordem; peça com Can I get…?'},
                {'en': 'I am a coffee.', 'pt': 'Eu sou um café.', 'ok': False, 'fb': 'Isso descreve você, não o pedido.'}]},
            {'npc': 'For here or to go?', 'pt': 'Para ficar ou levar?', 'opts': [
                {'en': 'On the left.', 'pt': 'À esquerda.', 'ok': False, 'fb': 'Essa fala indica lugar, não se você vai ficar.'},
                {'en': 'To go, please.', 'pt': 'Para levar, por favor.', 'ok': True, 'fb': 'Resposta direta ao atendente.'},
                {'en': 'I go now.', 'pt': 'Vou agora.', 'ok': False, 'fb': 'Para pedidos, use To go.'}]},
            {'npc': 'Do you want oat milk? Sorry, we are out of it.', 'pt': 'Quer leite de aveia? Desculpe, acabou.', 'opts': [
                {'en': 'You are out of me.', 'pt': 'Você acabou comigo.', 'ok': False, 'fb': 'O assunto é a bebida; escolha outra opção.'},
                {'en': 'I do not like your café.', 'pt': 'Não gosto da sua cafeteria.', 'ok': False, 'fb': 'Não resolve o pedido.'},
                {'en': 'Regular milk is fine, thanks.', 'pt': 'Leite comum serve, obrigado.', 'ok': True, 'fb': 'Você repara o pedido e mantém a conversa.'}]},
            {'npc': 'Anything else?', 'pt': 'Mais alguma coisa?', 'opts': [
                {'en': 'No, that’s all. How much is it?', 'pt': 'Não, é só isso. Quanto custa?', 'ok': True, 'fb': 'Fecha o pedido e pergunta o preço.'},
                {'en': 'No more coffee.', 'pt': 'Sem mais café.', 'ok': False, 'fb': 'Diga That’s all para encerrar.'},
                {'en': 'I finish now.', 'pt': 'Eu termino agora.', 'ok': False, 'fb': 'Não é uma forma natural de fechar o pedido.'}]},
            {'npc': 'That’s three dollars. Your number is 12.', 'pt': 'São três dólares. Seu número é 12.', 'opts': [
                {'en': 'I am twelve dollars.', 'pt': 'Eu sou doze dólares.', 'ok': False, 'fb': 'O número identifica seu pedido.'},
                {'en': 'Here you go. Thanks!', 'pt': 'Aqui está. Obrigado!', 'ok': True, 'fb': 'Você paga e agradece.'},
                {'en': 'No, I am number three.', 'pt': 'Não, sou o número três.', 'ok': False, 'fb': 'Você confundiu preço e número do pedido.'}]},
            {'npc': 'Please wait for your number.', 'pt': 'Espere chamarem seu número.', 'opts': [
                {'en': 'Where is your number?', 'pt': 'Onde está o seu número?', 'ok': False, 'fb': 'Você precisa encontrar o balcão.'},
                {'en': 'I wait in the coffee.', 'pt': 'Espero dentro do café.', 'ok': False, 'fb': 'Peça a localização com Where is…?'},
                {'en': 'Where is the pickup counter?', 'pt': 'Onde fica o balcão de retirada?', 'ok': True, 'fb': 'Boa pergunta: usa a linguagem de localização do Regular.'}]},
        ]}
    s['errors'] = [
        {'wrong': 'I want a coffee now.', 'fix': 'Can I get a coffee, please?', 'alt': 'You give me coffee.', 'why': 'Can I get…? faz um pedido; now pode soar brusco.'},
        {'wrong': 'You have oat milk?', 'fix': 'Do you have oat milk?', 'alt': 'Have you oat milk?', 'why': 'Para perguntar sobre disponibilidade: Do you have…?'},
        {'wrong': 'Where pickup counter?', 'fix': 'Where is the pickup counter?', 'alt': 'Where the pickup counter is?', 'why': 'A pergunta direta precisa de is antes do sujeito.'},
        {'wrong': 'The counter is in the left.', 'fix': 'The counter is on the left.', 'alt': 'The counter is at left.', 'why': 'Para localização: on the left.'},
    ]
    s['homework'] = 'Grave dois pedidos: o primeiro sai como previsto; no segundo falta um ingrediente. Termine perguntando onde retirar a bebida.'
    s['homework_items'] = ['Grave dois pedidos com bebidas diferentes e uma troca de ingrediente.',
                           'Escreva uma mensagem curta para retirada usando Can I get…? e Do you have…?',
                           'Reouça a conversa e repita as falas de Evan e Ana com o ritmo natural.',
                           'Amanhã: recupere To go, please. Na próxima semana: peça a localização do balcão.']
    return s


VOCAB = [
    ('coffee', 'café', 'Can I get a small coffee?', 'This coffee is for here.', 'prop:cup'),
    ('tea', 'chá', 'Do you have hot tea?', 'Can I get a large tea?', 'prop:cup'),
    ('milk', 'leite', 'Do you have oat milk?', 'Regular milk is fine.', 'prop:cup'),
    ('cup', 'copo', 'Your cup is ready.', 'Is this my cup?', 'prop:cup'),
    ('counter', 'balcão', 'Where is the pickup counter?', 'The counter is on the left.', 'prop:bag'),
    ('tray', 'bandeja', 'The muffin is on the tray.', 'Is the tray near the window?', 'prop:bag'),
]

DIALOG = [
    ('Evan', 'Hi! What can I get for you?', 'Oi! O que vai ser?'),
    ('Ana', 'Can I get a small coffee, please?', 'Pode ser um café pequeno, por favor?'),
    ('Evan', 'For here or to go?', 'Para ficar ou levar?'),
    ('Ana', 'To go, please. Do you have oat milk?', 'Para levar, por favor. Tem leite de aveia?'),
    ('Evan', 'Sorry, not today. We have regular milk.', 'Desculpe, hoje não. Temos leite comum.'),
    ('Ana', 'Regular milk is fine, thanks.', 'Leite comum serve, obrigado.'),
    ('Evan', 'Anything else?', 'Mais alguma coisa?'),
    ('Ana', 'No, that’s all. How much is it?', 'Não, é só isso. Quanto custa?'),
    ('Evan', 'Three dollars. Your order number is 12.', 'Três dólares. O número do pedido é 12.'),
    ('Ana', 'Here you go. Where is the pickup counter?', 'Aqui está. Onde fica o balcão de retirada?'),
    ('Evan', 'On the left, near the window.', 'À esquerda, perto da janela.'),
    ('Ana', 'Got it. Thank you!', 'Entendi. Obrigado!'),
]


def refine(lesson, supp):
    """Troca a apresentação da aula 1, sem alterar as demais 49 aulas Quest."""
    c, r = supp['culture'], supp['reading']
    lesson['title'] = 'A coffee to go in Chicago'
    lesson['pt'] = 'Pedir, ajustar e retirar uma bebida; usar palavras de lugar quando necessário.'
    lesson['scene'] = 'cafe2'
    lesson['cast'] = ['Evan', 'Ana']
    lesson['dialog'] = {'speakers': {'Evan': {'name': 'Evan'}, 'Ana': {'name': 'Ana'}},
                        'lines': [{'who': who, 'en': en, 'pt': pt} for who, en, pt in DIALOG]}
    lesson['sticker'] = dict(supp['sticker'], art={'rs': 'cafe2', 'chars': []})
    lesson['visual'] = 'cafe2'
    lesson['fmt'] = 'quest-focus-v1'
    pages = []

    def add(stage, kind, title, **content):
        pages.append(dict(t='q1', stage=stage, kind=kind, title=title, **content))

    add('mission', 'cover', 'Missão no café', goal='Peça uma bebida, resolva uma falta e encontre a retirada.',
        can=['Can I get a small coffee, please?', 'Regular milk is fine, thanks.', 'Where is the pickup counter?'],
        note='Do filme à vida real: observe como as pessoas começam uma conversa.')
    add('culture', 'work', 'A obra e a situação', work=c['work'], question='No filme, um encontro começa com uma aproximação. Como um cliente começa sua conversa no café de hoje?')
    add('culture', 'facts', 'Como funciona o pedido', facts=c['facts'][:3])
    add('culture', 'facts', 'Escolhas e costumes', facts=c['facts'][3:])
    add('culture', 'compare', 'Brasil e Estados Unidos', compare=c['compare'])
    add('culture', 'artifact', 'Leia o cardápio', artifact=c['wild'][0])
    add('culture', 'artifact', 'Encontre a retirada', artifact=c['wild'][1])
    add('culture', 'quiz', 'Mito ou fato?', items=c['mythfact'], instruction='Nem toda cafeteria funciona da mesma forma. Decida e explique.')
    for i in range(0, 6, 2):
        add('read', 'reading', 'A história de Ana · %s/3' % (i // 2 + 1),
            paragraphs=r['text'][i:i + 2], glossary=r['glossary'], part=i // 2 + 1,
            prompt=['Onde Ana está e o que pede?', 'O que muda no pedido?', 'Onde ela retira a bebida?'][i // 2])
    add('read', 'quiz', 'Entenda a ideia', items=[r['fast']], instruction='Leia uma vez para entender a situação geral.')
    add('read', 'quiz', 'Encontre as informações', items=[
        {'q': q['q'], 'opts': q['opts'], 'ans': q['correct'], 'why': 'Localize a resposta no texto: ' + q['ans'] + '.'}
        for q in r['scan']], instruction='Procure detalhes, não traduza palavra por palavra.')
    add('read', 'quiz', 'Palavras pelo contexto', items=[
        {'q': q['sent'] + ' O que significa “' + q['w'] + '”?', 'opts': q['opts'], 'ans': q['ans'], 'why': q['why']}
        for q in r['ctx']], instruction='Use a frase inteira como pista antes de escolher.')
    add('read', 'quiz', 'Confira as pistas', items=[
        {'q': q['s'], 'opts': ['True', 'False'], 'ans': 0 if q['ans'] else 1, 'why': q['why']} for q in r['tf']],
        instruction='A resposta precisa concordar com a história.')
    add('read', 'quiz', 'Sequência da história', items=[
        {'q': 'Depois de pedir o café, o que Ana faz?', 'opts': ['Sai sem pagar.', 'Escolhe leite comum.', 'Pede um filme.'], 'ans': 1,
         'why': 'Ela muda o ingrediente porque não há leite de aveia.'},
        {'q': 'O que acontece antes de Ana procurar o balcão de retirada?', 'opts': ['Ela paga e recebe um número.', 'Ela volta ao trem.', 'Ela pega uma bandeja vazia.'], 'ans': 0,
         'why': 'O número serve para identificar o pedido na retirada.'},
        {'q': 'Como termina a história?', 'opts': ['Ana se senta sem a bebida.', 'Evan fecha a loja.', 'Ana confere o copo e sai.'], 'ans': 2,
         'why': 'Ela verifica o pedido recebido antes de sair.'}],
        instruction='Reconstrua a sequência sem reler a história.')
    add('talk', 'dialog', 'Conversa · o pedido', lines=DIALOG[:6], instruction='Ouça. Depois substitua coffee por tea e diga o que muda.')
    add('talk', 'dialog', 'Conversa · a retirada', lines=DIALOG[6:], instruction='Troque o número do pedido e o lugar da retirada.')
    for i, t in enumerate(supp['convo']['turns']):
        add('talk', 'choice', 'Sua resposta · %s/6' % (i + 1), turn=t, position=i + 1,
            outcome=['Evan inicia o pedido.', 'Ele prepara um copo para levar.', 'O pedido continua com outra opção.',
                     'Evan informa o preço.', 'Você recebe o número 12.', 'Evan aponta para a esquerda.'][i])
    for i in range(0, 6, 3):
        add('lab', 'vocab', 'Palavras em ação · %s/2' % (i // 3 + 1), words=VOCAB[i:i + 3],
            prompt='Toque, ouça e diga uma frase sua com cada palavra.')
    add('lab', 'pattern', 'Molde: faça o pedido', frame='Can I get a {size} {drink}, please?',
        slots=[{'key': 'size', 'opts': ['small', 'medium', 'large']},
               {'key': 'drink', 'opts': ['coffee', 'tea', 'latte']}],
        model='Can I get a small coffee, please?',
        note='Na escrita, troque para Could I get…? quando desejar um tom mais cuidadoso.')
    add('lab', 'pattern', 'Molde: peça localização', frame='The {object} is {place}.',
        slots=[{'key': 'object', 'opts': ['pickup counter', 'tray', 'cup']},
               {'key': 'place', 'opts': ['on the left', 'on the right', 'near the window']}],
        model='The pickup counter is on the left.',
        note='Pergunte antes: Where is the pickup counter? Use o molde para responder.')
    add('lab', 'sound', 'Som e ritmo do café', pairs=[('tray', 'tr', 'Não acrescente vogal antes de tr.'),
                                                      ('straw', 'str', 'Comece com s; não diga “istraw”.'),
                                                      ('Can I get a coffee?', 'can I', 'Una as palavras numa pergunta natural.')],
        prompt='Ouça, repita e depois grave uma versão com tea.')
    add('arcade', 'quiz', 'Encontre a frase natural', items=[
        {'q': e['why'], 'opts': [e['wrong'], e['fix'], e['alt']], 'ans': 1, 'why': e['fix']} for e in supp['errors']],
        instruction='Escolha a forma que resolve a situação; explique o erro comum.')
    add('arcade', 'quiz', 'Transferência de contexto', items=c['quiz'],
        instruction='Agora o cliente muda uma condição: responda sem decorar o diálogo.')
    add('boss', 'role', 'Missão ao vivo', solo='Professor é Evan; estudante é Ana. Faça três rodadas: pedido normal, falta de leite de aveia, retirada em outro balcão.',
        group='Trio: cliente, atendente e observador. Troquem de papel a cada rodada. O observador marca pedido claro, reparo e localização.',
        prompts=['Can I get…?', 'Do you have…?', 'Where is…?'],
        change=['Não há leite de aveia.', 'O número é chamado, mas há dois balcões.', 'O cliente muda de “to go” para “for here”.'])
    add('write', 'pattern', 'Molde: varie por escrito', frame='Hi! Could I get a {size} {drink} to go at {time}? Do you have oat milk? Thanks, Ana.',
        slots=[{'key': 'size', 'opts': ['small', 'medium', 'large']},
               {'key': 'drink', 'opts': ['coffee', 'tea', 'latte']},
               {'key': 'time', 'opts': ['8:30', '9:00', '10:15']}],
        model='Hi! Could I get a small coffee to go at 8:30? Do you have oat milk? Thanks, Ana.',
        note='Na escrita, a saudação, o detalhe e a despedida tornam o pedido mais fácil de entender.')
    add('write', 'writing', 'Escreva para retirar', task='Escreva uma mensagem curta para fazer um pedido e perguntar por uma opção. Depois crie uma segunda versão mudando bebida, tamanho e horário.',
        model='Hi! Could I get a small coffee to go at 8:30? Do you have oat milk? Thanks, Ana.',
        checks=['Incluí bebida e tamanho.', 'Fiz uma pergunta clara.', 'Usei uma despedida natural.'],
        variants=['small coffee / 8:30', 'large tea / 9:00', 'medium latte / 10:15'])
    add('wrap', 'exit', 'Mostre o que aprendeu', prompts=['Peça um café pequeno para levar.',
        'Não há leite de aveia: escolha outra opção.', 'Pergunte onde fica a retirada.'],
        spaced=['Amanhã: faça um novo pedido sem consultar.', 'Na próxima semana: peça a localização de outro balcão.',
                'Na próxima unidade: mude o tom de um pedido escrito.'])
    add('wrap', 'finish', 'Missão concluída', badge=supp['badge'], homework=supp['homework'],
        next='Em outra cafeteria, um detalhe do pedido mudou. Como você se adaptaria?')
    lesson['pages'] = pages
    lesson['plan'] = {
        'solo': [{'id': k, 'name': name, 'min': minutes} for k, name, minutes in [
            ('mission', 'Missão', 3), ('culture', 'Contexto', 8), ('read', 'Leitura', 11),
            ('talk', 'Conversa', 13), ('lab', 'Oficina', 9), ('arcade', 'Prática', 6),
            ('boss', 'Produção oral', 5), ('write', 'Escrita', 3), ('wrap', 'Retomada', 2)]],
        'group': [{'id': k, 'name': name, 'min': minutes} for k, name, minutes in [
            ('mission', 'Missão', 3), ('culture', 'Contexto', 7), ('read', 'Leitura', 10),
            ('talk', 'Conversa', 11), ('lab', 'Oficina', 8), ('arcade', 'Prática', 5),
            ('boss', 'Interação em trios', 10), ('write', 'Escrita', 4), ('wrap', 'Retomada', 2)]]}
    assert len(pages) == 36 and all(sum(x['min'] for x in plan) == 60 for plan in lesson['plan'].values())
