#!/usr/bin/env python3
"""Aula 53 · Going to a party (A1, 60 min). Gera data/v3/053.json."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from rl_common import PLAN, teach, finish

# ---- construtor compacto (dados -> páginas rl_*) ----
UNIT_NAME = 'Free time'
UNIT_MAP = ['Hobbies and interests', 'Weekend plans and sports', 'At the cinema', 'Music and concerts', 'Going to a party', 'Messages and social media', 'Making friends online', 'Real-Life Mission Day 7']

def build(S):
    R = S['roles']; cast = S['cast']
    dlg = dict(speakers={R[0]: {'name': cast[0]}, R[1]: {'name': cast[1]}}, lines=[dict(who=R[w], en=en, pt=pt) for w, en, pt in S['dialog']])
    E = S['err']; X = S['xq']
    def er(k): return [dict(w=E[(2 * k + i) % len(E)][0], r=E[(2 * k + i) % len(E)][1]) for i in range(2)]
    def ex(k): return [X[k % len(X)], X[(k + 3) % len(X)]]
    T = S['tchr']
    unit = dict(n=7, k=S['k'], of=8, name=UNIT_NAME)
    P = []
    P.append(dict(t='rl_open', stage='warm', title=S['title'], pt=S['pt'], level='A1', unit=dict(unit, map=UNIT_MAP),
      situation=dict(text=S['sit'], scene=S['scene'], tod=S.get('tod', 'day'), cast=cast), goal=S['goal'], canDo=S['canDo'], success=S['success'], think=S['think'],
      teach=teach(goal='Abrir a aula pela situação real, não pela regra.', solo=['Leia o objetivo em voz alta e peça que o estudante diga, com as próprias palavras, o que vai conseguir fazer hoje.', 'Faça a pergunta “Think about it” antes de mostrar qualquer expressão.'],
        group=['Cada estudante diz UMA palavra que associa à situação de hoje.', 'Mostre os critérios de sucesso: eles são a missão final da aula.'], extra=ex(0), support=['Aceite respostas curtas ou em português na primeira rodada e reformule em inglês.'])))
    P.append(dict(t='rl_warm', stage='warm', title='Connection & warm-up', intro=dict(solo='Start with real questions about the student’s life, not a grammar test.', group='One question per student, then a question back to a classmate.'),
      recall=S['recall'], qs=[dict(q=q, pt=pt, sup=sup) for q, pt, sup in S['warm']], tip='Use the answers to find gaps and to recycle earlier content. The goal is to enter English from the first minute.',
      teach=teach(goal='Entrar no idioma no primeiro minuto e retomar a aula anterior.', extra=ex(1), errors=er(0), support=['Ofereça as respostas-modelo (chips) e peça apenas que escolham uma.'])))
    P.append(dict(t='rl_culture', stage='immersion', title='Cultural snapshot — ' + S['ctitle'], intro=S['cintro'],
      cards=[dict(vis=v, en=en, pt=pt, note=n) for v, en, pt, n in S['cards']],
      qs=[dict(q=q, pt=pt, levels=dict(A1=a1, A2=a2, B1=b1, B2=b2)) for q, pt, a1, a2, b1, b2 in S['cqs']], compare=S['compare'],
      teach=teach(goal='Ativar o contexto cultural e as primeiras hipóteses.', solo=['Mostre os 3 cartões e peça hipóteses antes de explicar.', 'Peça que o estudante compare com o que acontece no Brasil.'], group=['Cada estudante escolhe um cartão e explica em uma frase.', 'Pergunte “Do you agree?” entre colegas.'],
        answers=S['cans'], extra=ex(2), support=['Use as respostas do nível A1 como andaime e peça que repitam.'], stretch=['B2: compare as convenções sociais do Brasil e dos EUA nessa situação.'])))
    p1 = S['p1']; p2 = S['p2']
    P.append(dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene=S['scene'], tod=S.get('tod', 'day'), cast=cast),
      pass1=dict(q=p1[0], pt=p1[1], opts=p1[2], ans=p1[3]), pass2=dict(tasks=[dict(label=l, ans=a, **({'alt': al} if al else {})) for l, a, al in p2]),
      teach=teach(goal='Compreender a situação antes de ver o texto: ideia principal e depois informações específicas.', solo=['Esconda o texto. 1ª escuta: só a ideia principal.', '2ª escuta: as informações da lista.', 'Mostre o texto só depois da 2ª escuta.'],
        group=['Escuta coletiva; duplas anotam as respostas antes de revelar.', 'Compare as respostas entre as duplas e só então mostre o texto.'], answers=['Pass 1: ' + p1[2][p1[3]] + '.', 'Pass 2: ' + ' · '.join(a for _, a, _ in p2)],
        extra=['Who is speaking? How do you know?', ex(3)[0]], support=['Use o botão “Slow” na 2ª escuta.', 'Pause depois de cada fala se necessário.'])))
    P.append(dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation', qs=[dict(q=q, opts=o, ans=a) for q, o, a in S['dqs']],
      retell=dict(prompt='Retell the conversation in your own words, at your level.', starters=S['retell']),
      teach=teach(goal='Ler o diálogo, perceber os chunks e recontar.', solo=['O estudante lê um papel; você lê o outro. Depois troquem.', 'Peça que reconte a conversa no nível que conseguir.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia: uma frase por estudante.'],
        answers=S['dans'], extra=ex(4), errors=er(1), support=['Mostre a tradução (botão PT) depois da 2ª leitura.'])))
    P.append(dict(t='rl_chunks', stage='notice', title='Useful expressions',
      items=[dict(en=en, pt=pt, use=use, reg=reg, **({'alt': alt} if alt else {}), **({'pri': True} if pri else {})) for en, pt, use, reg, alt, pri in S['chunks']],
      discover=dict(fns=S['fns'], items=[dict(en=en, fn=fn) for en, fn in S['disc']]),
      note='Instead of memorizing the whole list, choose 3–5 expressions (★) to use again and again. The others are for understanding and for stretching later.',
      teach=teach(goal='Escolher 3–5 chunks para uso repetido e descobrir a função de cada um.', solo=['Pergunte “When do you say it?” antes de dar o significado.', 'Compare formal × informal e peça um exemplo próprio.'], group=['Cada estudante escolhe a expressão que mais usaria e explica quando.', 'Compare equivalentes formais e informais em duplas.'],
        answers=[' · '.join(S['fns'])], extra=ex(5), errors=er(2), support=['Trabalhe só as 3 expressões ★ nesta aula.'])))
    sw = S['swap']
    P.append(dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
      patterns=[dict(name=n, formula=f, ex=e, **({'main': True} if m else {})) for n, f, e, m in S['pats']],
      swap=dict(frame=sw[0], tpt=sw[1], slots=[dict(k=k, label=l, opts=[dict(en=a, pt=b) for a, b in o]) for k, l, o in sw[2]]),
      register=dict(head=['Spoken English', 'Written English'], rows=S['reg'], note='These are differences of context and register, not absolute rules: contractions and short forms also appear in informal writing.'),
      teach=teach(goal='Fixar os 2 padrões principais; os outros são expansão. Usar a troca de palavras para variar a fala.', solo=['Mostre o padrão DENTRO do diálogo (grife os chunks).', 'Use “Swap the words”: toque em cada peça e peça a frase completa.', 'Compare spoken × written em 2 exemplos.'],
        group=['Troca em cadeia: cada estudante muda UMA peça e o próximo repete a frase.', 'Em pares: um escolhe as peças, o outro fala.'], answers='Os padrões 01 e 02 são o foco; os demais são expansão para quem avançar rápido.', extra=ex(6), errors=er(3),
        support=['Fique só com o primeiro padrão na primeira rodada.'], stretch=['Combinar dois padrões na mesma frase.'])))
    pr = S['pron']
    P.append(dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English', focus=pr['focus'], tip=pr['tip'],
      items=[dict(say=s, linked=l, ipa=i, rhythm=r) for s, l, i, r in pr['items']], identify=[dict(q='Which one do you hear?', opts=o, ans=a, say=o[a]) for o, a in pr['id']],
      own=dict(prompt=pr['own'], criteria=pr['crit']),
      teach=teach(goal='UM só fenômeno: ' + pr['focus'] + '.', solo=['3 passagens: escutar e identificar → reproduzir ritmo e entonação → usar em frase com conteúdo próprio.', 'Modele devagar e normal; peça que o estudante bata palmas na sílaba forte.'], group=['Coro, depois duplas; circule ouvindo.', 'Cada estudante cria uma frase própria.'],
        answers=['Identify: ' + ' · '.join(o[a] for o, a in pr['id'])], errors=er(4), support=['Reduza a velocidade e conte as batidas em voz alta.'])))
    C = S['chal']
    def mk(it):
        t = it[0]
        if t == 'mcq': return dict(type='mcq', q=it[1], opts=it[2], ans=it[3], why=it[4])
        if t == 'gap': d = dict(type='gap', text=it[1], ans=it[2], why=it[4]); (d.update(bank=it[3]) if it[3] else None); return d
        if t == 'swap': d = {'type': 'swap', 'instr': it[1], 'frm': it[2], 'ans': it[3], 'model': it[4], 'why': it[5]}; return d
        if t == 'reply': return dict(type='reply', npc=it[1], q='Choose the best reply.', opts=it[2], ans=it[3], why=it[4])
    P.append(dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
      levels=[dict(h='Controlled practice — choose the best answer', items=[mk(i) for i in C[0]]), dict(h='Guided practice — complete, substitute and transform', items=[mk(i) for i in C[1]])],
      teach=teach(goal='Do controlado ao guiado: completar, substituir e transformar antes da fala livre.', solo=['Peça que o estudante justifique cada resposta.', 'Se acertar rápido, peça a versão mais informal ou mais educada.'], group=['Resolvam em duplas e comparem antes de revelar.', 'Equipes: ponto por resposta justificada.'],
        answers=S['chans'], extra=ex(7), errors=er(5), support=['Ofereça o banco de palavras (chips) nas lacunas.'])))
    ro = S['role']
    P.append(dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — ' + ro['title'], brief=dict(teacher=ro['teacher'], student=ro['student']), orders=ro['orders'], complications=ro['comp'],
      rounds=[dict(label='With support', desc='Chunks on screen', help=ro['chunks']), dict(label='Keywords', desc='Only the keywords', help=ro['kw'], kw=True), dict(label='No script', desc='Free', help=[])], success=S['success'],
      teach=teach(goal='Simulação com complicação inesperada e três rodadas com menos apoio.', solo=['Ligue o cenário à vida do estudante.', 'Rodada 1: com chunks. Rodada 2: só palavras-chave. Rodada 3: sem roteiro.', 'Meta de fala: 60–70% do tempo para o estudante. Anote 2–3 correções para a devolutiva.'],
        extra=ex(8), errors=er(6), support=['Volte à rodada 1 se travar; peça que repita só a primeira frase.'], stretch=ro['stretch'])))
    lb = S['lab']
    P.append(dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations', rounds=[dict(title=t, min=m, task=k, hint=h, **({'whole': True} if w else {})) for t, m, k, h, w in lb['rounds']],
      infogap=dict(title=lb['gt'], instr='Ask your partner and complete your card. Do not look at the other card!', a=dict(title=lb['at'], task=lb['atask'], rows=[dict(k=k, v=v) for k, v, _ in lb['rows']]), b=dict(title=lb['bt'], task=lb['btask'], rows=[dict(k=k, v=v) for k, _, v in lb['rows']])),
      teach=teach(goal='Fluência por repetição da função com informações novas a cada rodada.', group=['Troque os pares a cada rodada (A+B / C+D → A+C / B+D → A+D / B+C → grupo todo). Com 6 estudantes, três duplas simultâneas.', 'Sem salas simultâneas: interações sequenciais enquanto uma dupla apresenta.', 'Responsabilidade individual: cada aluno faz ≥1 pergunta e ≥1 resposta.'],
        answers=[lb['ans']], extra=ex(9), errors=er(7), support=['Entregue frases-modelo no chat da turma.'])))
    mi = S['miss']
    P.append(dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — ' + mi['title'], goal=mi['goal'], missions=[dict(who=w, role=r, mission=m, constraint=c, start=s) for w, r, m, c, s in mi['list']], min=11, success=S['success'],
      teach=teach(goal='Realizar algo com o inglês: o objetivo é resolver, não só falar certo.', group=['Cada grupo recebe papel, restrição e missão. Alterne os papéis.', 'Progressão: 1ª rodada com frases de apoio, 2ª só palavras-chave, 3ª sem roteiro.', 'Observe e anote 2–3 correções prioritárias; devolutiva no fim.'],
        answers=[mi['model']], extra=ex(10), support=['Dê o início de frase (“Start with”) em cada cartão.'])))
    wr = S['write']
    P.append(dict(t='rl_write', stage='write', title='Writing — a small real-life task', task=wr['task'], steps=wr['steps'], model=wr['model'], checklist=wr['check'],
      tip='Fix only 2–3 priority points. Show a more natural way to say the same idea instead of rewriting everything.', fix=dict(n=3),
      teach=teach(goal='Produção escrita curta ligada à situação comunicativa.', solo=['Peça o texto; corrija 2–3 pontos prioritários e mostre uma forma mais natural.'], group=['Cada estudante escreve; depois troquem os textos entre colegas e corrijam em duplas.'],
        extra=ex(11), errors=er(8), support=['Dê o modelo e peça só para trocar os dados.'])))
    fb = S['fb']
    P.append(dict(t='rl_feedback', stage='write', title='Feedback & review — Speaking Performance Check',
      criteria=[dict(k='flu', name='Fluency', desc='Mantém a comunicação sem interrupções excessivas.'), dict(k='lan', name='Language use', desc='Utiliza adequadamente padrões, vocabulário e expressões.'), dict(k='pro', name='Pronunciation', desc='É compreensível e usa ritmo e entonação adequados.'), dict(k='int', name='Interaction', desc='Responde, pergunta, esclarece e desenvolve a conversa.')],
      interpret=[dict(max=8, text='Needs more support. Revisit the main patterns with guided practice before the next lesson.'), dict(max=13, text='Functional performance. Work on the lowest criteria in the next lesson.'), dict(max=17, text='Good control. Raise complexity and speed; add follow-up questions.'), dict(max=20, text='Strong performance. Move to a more demanding situation.')],
      prompts=dict(well=fb[0], improve=fb[1], next=fb[2]),
      teach=teach(goal='Avaliar o que o aluno conseguiu comunicar, não só os erros gramaticais.', solo=['O estudante se autoavalia primeiro; depois você.', 'Feche com os três blocos: What you did well · What to improve · Your next challenge.'], group=['Dê um comentário por critério a cada estudante.', 'Cada um escolhe o próprio próximo desafio.'],
        answers='A rubrica é uma ferramenta interna de acompanhamento, não uma certificação CEFR.')))
    xt = S['exit']
    P.append(dict(t='rl_exit', stage='exit', title='Exit ticket & homework', tasks=[dict(ic=ic, name=n, prompt=p, model=m) for ic, n, p, m in xt['tasks']],
      homework=dict(h='Your real-life English mission', min='10–15', items=xt['hw']), spaced=dict(next=xt['next'], week=xt['week'], unit=xt['unit']),
      teach=teach(goal='Toda aula termina com uma produção observável.', solo=['Sem consultar as anotações: construir uma pergunta, responder a uma situação e usar uma expressão nova.'], group=['Exit challenge individual; compare com o colega e combine a tarefa de continuidade.'],
        answers=[' · '.join(m for _, _, _, m in xt['tasks'])], extra=['Revisão espaçada: retomar na próxima aula, depois de uma semana e na missão de encerramento da unidade.'])))
    lv = S['ladder']
    P.append(dict(t='rl_levels', stage='exit', title='Level up — the same situation from A1 to C2', you='A1', intro='You do not need six different methods: the structure stays, while language complexity and autonomy grow.',
      ladder=[dict(lv=a, say=b, goal=c) for a, b, c in lv],
      note='This progression is illustrative: complex sentences do not define a level on their own. CEFR also considers comprehension, autonomy, fluency, accuracy, interaction and appropriateness.',
      teach=teach(goal='Mostrar a progressão sem criar seis metodologias.', solo=['Mostre onde o estudante está e a próxima etapa.'], group=['Cada um escolhe a frase do próprio nível e a do próximo.'])))
    return dict(n=S['n'], topic=S['topic'], level='A1', title=S['title'], pt=S['pt'], unit=unit, minutes=60, cast=cast, scene=S['scene'], tod=S.get('tod', 'day'), plan=PLAN, dialog=dlg, pages=P)


S = dict(n=53, k=5, topic='Going to a party', title='Going to a Party', pt='Ir a uma festa: chegar, levar algo e se despedir', cast=['Jade', 'Finn'], roles=['Finn', 'Jade'], scene='livingroom', tod='night',
 sit='You go to a house party in the USA. You meet the host, bring a dish, talk to the people and leave politely.',
 goal='By the end of the class you can arrive at a party, greet the host, offer to bring something, ask a simple question and say goodbye politely.',
 canDo=['Greet the host: Nice to meet you', 'Offer or ask: Can I bring…?', 'Ask an easy question about the house or the party', 'Leave politely: I’d better go'],
 success=['I greet the host.', 'I bring or offer something.', 'I ask one question.', 'I say goodbye politely.'],
 think='What do you take to a party in Brazil? And what do you say when you leave?',
 recall='Last class: music and concerts. Ask: Who’s your favorite artist? Have you ever been to a concert?',
 warm=[('Do you like parties?', 'Você gosta de festas?', ['Yes, a lot!', 'Small ones.', 'Not really.']), ('What do you take to a party?', 'O que você leva para uma festa?', ['Drinks.', 'Food.', 'A gift.']), ('Do you arrive early or late?', 'Você chega cedo ou tarde?', ['A little late.', 'On time.', 'Early.'])],
 ctitle='House parties in the USA', cintro='In the USA, a house party often has simple rules that nobody says out loud: bring something, ask before you do something and say thanks. Look and guess before you read.',
 cards=[('prop:cake', 'Bring a dish', 'Levar um prato', 'At a potluck, each guest brings a dish to share. The host usually tells you in the invitation.'), ('obj:door', 'Shoes at the door', 'Sapatos na porta', 'In many homes people take their shoes off at the door. It is polite to ask: “Should I take my shoes off?”'), ('prop:clock', 'Time of arrival', 'Horário de chegada', 'For a dinner, arrive on time. For a casual party, a little late is often okay. If in doubt, ask the host.')],
 cqs=[('What is a potluck?', 'O que é um potluck?', 'Each person brings food.', 'Each guest brings a dish to share with everyone.', 'At a potluck, the party is a shared meal: everyone contributes a dish.', 'A potluck spreads the work and the cost: guests bring dishes, and the table becomes a mix of home cooking.'),
      ('Why do guests ask “Should I take my shoes off?”', 'Por que perguntar “Should I take my shoes off?”?', 'Some homes are shoe-free.', 'In some homes people do not wear shoes inside.', 'Some hosts prefer shoes off, and asking shows respect for the house.', 'Customs differ from home to home, so a quick question avoids awkward moments and shows respect.'),
      ('What is a polite way to leave a party?', 'Qual é uma forma educada de sair de uma festa?', 'Thank you for having me.', 'Say thanks and give a reason: “I’d better go.”', 'Thank the host, say you had fun and give a short reason before you leave.', 'A warm thanks plus a light reason (“early day tomorrow”) lets you leave without seeming to dislike the party.')],
 compare='In Brazil guests often arrive later and bring drinks or dessert. In the USA people also bring something, but they often ask the host first. What would you bring to a friend’s party?',
 cans=['Q1: cada convidado leva um prato.', 'Q2: algumas casas pedem que se tire o sapato.', 'Q3: agradecer e dar um motivo breve.'],
 p1=('Where is the conversation?', 'Onde é a conversa?', ['At a party', 'At a doctor', 'At school'], 0),
 p2=[('What Jade brings', 'salad', []), ('Where the salad goes', 'kitchen', []), ('Where the drinks are', 'table', []), ('Why Jade leaves', 'work tomorrow', ['work'])],
 dialog=[(0, 'Hi! I’m Finn. You must be Jade.', 'Oi! Eu sou o Finn. Você deve ser a Jade.'), (1, 'Yes! **Nice to meet you.** Thanks for having me.', 'Sim! Prazer em conhecer você. Obrigada por me receber.'), (0, 'Nice to meet you, too. Come in!', 'Prazer também. Entre!'),
  (1, '**Can I bring** this salad to the kitchen?', 'Posso levar esta salada para a cozinha?'), (0, 'Sure, thank you! The drinks are on the table.', 'Claro, obrigado! As bebidas estão na mesa.'), (1, 'Your place is great! **Should I take my shoes off?**', 'Sua casa é ótima! Devo tirar os sapatos?'),
  (0, 'Not at all. Keep them on!', 'Não precisa. Fique com eles!'), (1, 'This was fun! **I’d better go** now. I work tomorrow.', 'Foi divertido! É melhor eu ir agora. Eu trabalho amanhã.'), (0, 'Already? Thanks for coming!', 'Já? Obrigado por vir!'), (1, '**Thanks again.** Good night!', 'Obrigada de novo. Boa noite!')],
 dqs=[('What does Jade bring?', ['A salad', 'A cake', 'Pizza'], 0), ('Where are the drinks?', ['In the kitchen', 'On the table', 'In the garden'], 1), ('Does Jade take her shoes off?', ['Yes', 'No, she keeps them on', 'She doesn’t ask'], 1), ('Why does Jade leave?', ['She works tomorrow', 'She is sick', 'She is hungry'], 0)],
 retell=['Jade meets…', 'She brings…', 'She asks about…', 'She leaves because…'], dans=['A salad · on the table · keeps her shoes on · works tomorrow'],
 chunks=[('Can I bring…?', 'Posso levar…?', 'Ask if you can bring something.', 'neutral', 'Also: **What can I bring?**', True), ('Thanks for having me.', 'Obrigado por me receber.', 'Thank the host when you arrive or leave.', 'polite', 'Also: **Thanks for the invite.**', True), ('Should I take my shoes off?', 'Devo tirar os sapatos?', 'Ask about a house rule.', 'neutral', None, True), ('I’d better go.', 'É melhor eu ir.', 'Leave politely and give a reason.', 'neutral', 'Also: **I should get going.**', True),
  ('Nice to meet you.', 'Prazer em conhecer você.', 'Greet someone new.', 'neutral', None, False), ('Come in!', 'Entre!', 'The host welcomes you.', 'neutral', None, False), ('Thanks again.', 'Obrigado de novo.', 'Say thanks one more time.', 'neutral', None, False)],
 fns=['Offering', 'Thanking the host', 'Asking about house rules', 'Leaving', 'Greeting'],
 disc=[('Can I bring dessert?', 'Offering'), ('Thanks for having me.', 'Thanking the host'), ('Should I take my shoes off?', 'Asking about house rules'), ('I’d better go.', 'Leaving'), ('Nice to meet you.', 'Greeting')],
 pats=[('Asking permission', '**Can I** + verb + object?', ['Can I bring dessert?', 'Can I sit here?', 'Can I help in the kitchen?'], True), ('Giving advice or a reason', '**I’d better** + verb', ['I’d better go.', 'I’d better call my ride.', 'I’d better leave now.'], True), ('Asking about rules', '**Should I** + verb?', ['Should I take my shoes off?', 'Should I bring something?'], False), ('Thanking', '**Thanks for** + noun / -ing', ['Thanks for the party.', 'Thanks for having me.'], False)],
 swap=('Can I bring {thing} {to}?', 'Posso levar {thing} {to}?', [('thing', 'What', [('a salad', 'uma salada'), ('some drinks', 'algumas bebidas'), ('a cake', 'um bolo'), ('chips', 'salgadinhos')]), ('to', 'Where', [('to the kitchen', 'para a cozinha'), ('to the table', 'para a mesa'), ('to the party', 'para a festa')])]),
 reg=[['Can I bring something?', 'May I bring something to the gathering?'], ['I’d better go.', 'I should be leaving now.'], ['Thanks for having me!', 'Thank you for your kind hospitality.'], ['Make yourself at home.', 'Please feel comfortable.']],
 pron=dict(focus='The American flap T', tip='In American English, the “t” between vowels often sounds like a quick “d”: “better” sounds like “beddy”, “party” like “par-dy”.',
  items=[('I’d better go.', 'I’d BED-der GO.', '/aɪd ˈbɛɾər goʊ/', 'oOoO'), ('It’s a great party.', 'It’s a GREAT PAR-dy.', '/ɪts ə ˈɡreɪt ˈpɑɾi/', 'ooOOo'), ('Thanks for the invitation.', 'Thanks for the IN-vi-TA-tion.', '/θæŋks fər ði ˌɪnvɪˈteɪʃən/', 'oooOoOo')],
  id=[(['I’d better go.', 'I’d bitter go.', 'I’d beat her go.'], 0), (['It’s a pretty party.', 'It’s a pity party.', 'It’s a petty party.'], 0)], own='Write a sentence with “better”, “party” or “water”.', crit='Say it twice. Did the “t” sound like a quick “d”?'),
 chal=([('mcq', '1. You arrive and the host opens the door.', ['Hi! Thanks for having me.', 'I come to your house.', 'Where is my food?'], 0, 'Thank the host when you arrive.'), ('mcq', '2. You want to bring a dessert.', ['Can I bring dessert?', 'I can to bring dessert?', 'Can bring I dessert?'], 0, 'Can I + base verb.'), ('mcq', '3. You are not sure about the shoes.', ['Should I take my shoes off?', 'Do I shoes off take?', 'Shoes off, yes?'], 0, 'Should I + base verb?'), ('mcq', '4. It is late and you want to leave.', ['I’d better go. Thanks for the party!', 'I go now, bye.', 'I better to leaving.'], 0, 'I’d better + base verb, with thanks.')],
  [('gap', 'Can I ___ a salad?', 'bring', ['bring', 'brings', 'to bring'], 'Can I + base verb.'), ('gap', 'I’d ___ go. It’s late.', 'better', ['better', 'best', 'good'], 'I’d better + base verb.'), ('swap', 'Say it politely with “Should I”:', 'Take shoes off?', ['Should I take my shoes off?', 'Should I take shoes off?'], 'Should I take my shoes off?', 'Should I + base verb asks about a rule.'), ('swap', 'Thank the host:', 'party', ['Thanks for the party.', 'Thank you for the party.', 'Thanks for the party!'], 'Thanks for the party.', 'Thanks for + noun.'), ('reply', 'Thanks for coming!', ['Thanks for having me!', 'Thanks, I come.', 'You are welcome party.'], 0, 'A friendly answer from the guest.')]),
 chans=['1: Hi! Thanks for having me. · 2: Can I bring dessert? · 3: Should I take my shoes off? · 4: I’d better go. Thanks for the party!', 'Gap: bring · better · Should I take my shoes off? · Thanks for the party. · Thanks for having me!'],
 role=dict(title='arrive and leave a party', teacher='You are the host (change the plan during the scene!).', student='You are a guest: greet the host, offer something and leave politely.',
  orders=['Arrive at a friend’s birthday party with a cake', 'Arrive at a potluck with a salad', 'Arrive at a house party and bring drinks'], comp=['The host already has a lot of food: offer another help.', 'You don’t know anyone: ask the host to introduce you.', 'You must leave early: explain politely.', 'You didn’t hear the name: ask the person to repeat.'],
  chunks=['Thanks for having me.', 'Can I bring…?', 'Should I take my shoes off?', 'I’d better go.'], kw=['salad', 'kitchen', 'shoes', 'late', 'thanks'], stretch=['Peça que o estudante apresente um amigo ao anfitrião.']),
 lab=dict(rounds=[('Arrive', 3, 'Greet the host. Say thanks and offer to bring something.', 'Nice to meet you. / Can I bring…?', False), ('House rules', 3, 'Ask one question about the house (shoes, drinks, bathroom).', 'Should I…? / Is it okay to…?', False), ('Meet people', 3, 'Meet a new guest. Ask one question and answer.', 'Nice to meet you. / Where are you from?', False), ('Say goodbye', 2, 'Whole group: each pair shows a polite way to leave.', 'I’d better go. / Thanks for…', True)],
  gt='Potluck list', at='Student A has the first list', atask='You know who brings the salad and the cake. Ask about the rest.', bt='Student B has the second list', btask='You know who brings the drinks and the chips. Ask about the rest.',
  rows=[('Salad', 'Jade', ''), ('Drinks', '', 'Finn'), ('Cake', 'Mia', ''), ('Chips', '', 'Omar')], ans='A tem Salad (Jade) e Cake (Mia); B tem Drinks (Finn) e Chips (Omar). Cada um pergunta “Who’s bringing…?” para completar.'),
 miss=dict(title='party night', goal='Each group must arrive at a party, talk to the host and guests, and leave politely.',
  list=[('A', 'Guests at a potluck', 'Arrive, say who brings what and ask where to put it.', 'Use “Can I bring…?” and “Thanks for having me.”', 'Hi! Thanks for having me.'), ('B', 'Friends at a house party', 'Meet two new people and ask one question each.', 'Use “Nice to meet you” and one follow-up question.', 'Hi! Nice to meet you.'), ('C', 'Late guests', 'It’s late. Say goodbye to the host and thank everyone.', 'Use “I’d better go” and a reason.', 'This was great! I’d better go.')],
  model='“Hi! Thanks for having me. Can I bring this salad to the kitchen?” → “Sure! Drinks are on the table.” → “Should I take my shoes off?” → “Not at all.”'),
 write=dict(task='Write a short thank-you message to the host of a party you went to.', steps=['Greeting', 'Thanks', 'One detail you liked', 'Closing'],
  model='Hi Finn! **Thanks for having me** last night. The food was great and the music was fun. **I’d better go** to bed early next time! Let’s do it again soon. Jade', check=['I greeted the host.', 'I said thanks.', 'I gave a detail I liked.', 'I closed in a friendly way.']),
 fb=('Example: You greeted the host and asked a natural question.', 'Example: Use the flap T in “better”: BED-der.', 'Example: Go to an imaginary party and talk to two new people without notes.'),
 exit=dict(tasks=[('❓', 'Build a question', 'Without notes: ask if you can bring dessert.', 'Can I bring dessert?'), ('💬', 'Respond to a situation', 'It is late and you want to leave the party.', 'I’d better go. Thanks for having me!'), ('⭐', 'Use a new expression', 'Ask about the shoes at the door.', 'Should I take my shoes off?')],
  hw=['Record a 45–60 second audio arriving at a party.', 'Write a thank-you message to a host.', 'Review three expressions from the class and create your own examples.', 'Listen to the dialogue again and identify two expressions.'],
  next=['Can I bring…?', 'Thanks for having me.', 'I’d better go.'], week=['Should I take my shoes off?', 'Nice to meet you.', 'Thanks again.'], unit=['Invite · plan · share · react']),
 ladder=[('A1', 'Hello! I bring cake.', 'Arrive and offer food with short phrases.'), ('A2', 'Hi! Thanks for having me. Can I bring this cake to the kitchen?', 'Greet, thank and offer.'), ('B1', 'Thanks so much for inviting me. I hope it’s okay that I brought some dessert.', 'Thank and check politely.'), ('B2', 'It’s really kind of you to have us over. I took the liberty of bringing a little something for the table.', 'Show warmth and good manners.'), ('C1', 'I hope you don’t mind, but I couldn’t arrive empty-handed, so I brought a little something to share.', 'Use tact and nuance.'), ('C2', 'It was good of you to have us; I’d hate to turn up without at least a small token of thanks.', 'Be gracious with style.')],
 err=[('I am bring a salad.', 'I’m bringing a salad. / I brought a salad.'), ('Can I to bring a cake?', 'Can I bring a cake?'), ('Thanks to invite me.', 'Thanks for inviting me. / Thanks for having me.'), ('I better go.', 'I’d better go.'), ('I have to go to my house.', 'I have to go home.'), ('Nice to meet you, to.', 'Nice to meet you, too.'), ('I take off my shoes?', 'Should I take my shoes off?'), ('Where is the bath?', 'Where is the bathroom?')],
 xq=['What do you take to a party?', 'Do you like to dance at parties?', 'Who is your party friend?', 'What time do parties start where you live?', 'Have you ever hosted a party?', 'What is your favorite party food?', 'Do you take your shoes off at home?', 'How do you say goodbye at a party?'], tchr=None)


LESSON = build(S)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(LESSON['pages']), 'páginas')
