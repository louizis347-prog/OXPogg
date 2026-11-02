#!/usr/bin/env python3
"""Aula 47 · Meeting a colleague (A1, 60 min). Gera data/v3/047.json."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from rl_common import PLAN, teach, finish

UNIT_NAME = 'School & work'
UNIT_MAP = ['First day in class', 'Asking about the schedule', 'At the library', 'Workplace small talk', 'A simple job interview', 'Emails and phone at work', 'Meeting a colleague', 'Real-Life Mission Day 6']
CRIT = [dict(k='flu', name='Fluency', desc='Mantém a comunicação sem interrupções excessivas.'), dict(k='lan', name='Language use', desc='Utiliza adequadamente padrões, vocabulário e expressões.'), dict(k='pro', name='Pronunciation', desc='É compreensível e usa ritmo e entonação adequados.'), dict(k='int', name='Interaction', desc='Responde, pergunta, esclarece e desenvolve a conversa.')]
INTERP = [dict(max=8, text='Needs more support. Revisit the main patterns with guided practice before the next lesson.'), dict(max=13, text='Functional performance. Work on the lowest criteria in the next lesson.'), dict(max=17, text='Good control. Raise complexity and speed; add follow-up questions.'), dict(max=20, text='Strong performance. Move to a more demanding situation.')]
LEVNOTE = 'This progression is illustrative: complex sentences do not define a level on their own. CEFR also considers comprehension, autonomy, fluency, accuracy, interaction and appropriateness.'
LEVINTRO = 'You do not need six different methods: the structure stays, while language complexity and autonomy grow.'
RUBRIC_T = teach(goal='Avaliar o que o aluno conseguiu comunicar, não só os erros gramaticais.',
 solo=['O estudante se autoavalia primeiro; depois você.', 'Feche com os três blocos: What you did well · What to improve · Your next challenge.'], group=['Dê um comentário por critério a cada estudante.', 'Cada um escolhe o próprio próximo desafio.'],
 answers='A rubrica é uma ferramenta interna de acompanhamento, não uma certificação CEFR.')

def C(en, pt, use, reg='neutral', alt=None, pri=False):
    d = dict(en=en, pt=pt, use=use, reg=reg)
    if alt: d['alt'] = alt
    if pri: d['pri'] = True
    return d
def MC(q, opts, ans, why): return dict(type='mcq', q=q, opts=opts, ans=ans, why=why)
def GAP(text, ans, why, bank=None):
    d = dict(type='gap', text=text, ans=ans, why=why)
    if bank: d['bank'] = bank
    return d
def SW(instr, frm, ans, model, why): return dict(type='swap', instr=instr, frm=frm, ans=ans, model=model, why=why)
def RP(npc, q, opts, ans, why): return dict(type='reply', npc=npc, q=q, opts=opts, ans=ans, why=why)
def O(*p): return [dict(en=a, pt=b) for a, b in p]
def W(w, r): return dict(w=w, r=r)
def FEEDBACK(well, improve, nxt):
    return dict(t='rl_feedback', stage='write', title='Feedback & review — Speaking Performance Check', criteria=CRIT, interpret=INTERP, prompts=dict(well=well, improve=improve, next=nxt), teach=RUBRIC_T)
def LEVELS(ladder, you='A1'):
    lv = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
    return dict(t='rl_levels', stage='exit', title='Level up — the same situation from A1 to C2', you=you, intro=LEVINTRO,
     ladder=[dict(lv=l, say=s, goal=g) for l, (s, g) in zip(lv, ladder)], note=LEVNOTE,
     teach=teach(goal='Mostrar a progressão sem criar seis metodologias.', solo=['Mostre onde o estudante está e a próxima etapa.'], group=['Cada um escolhe a frase do próprio nível e a do próximo.']))
def UNIT(k): return dict(n=6, k=k, of=8, name=UNIT_NAME)
def OPEN(k, title, pt, text, scene, cast, goal, canDo, success, think, tch, tod='day'):
    return dict(t='rl_open', stage='warm', title=title, pt=pt, level='A1', unit=dict(UNIT(k), map=UNIT_MAP),
     situation=dict(text=text, scene=scene, tod=tod, cast=cast), goal=goal, canDo=canDo, success=success, think=think, teach=tch)
def LESSON_OF(n, topic, title, pt, k, cast, scene, dialog, pages, tod='day'):
    return dict(n=n, topic=topic, level='A1', title=title, pt=pt, unit=UNIT(k), minutes=60, cast=cast, scene=scene, tod=tod, plan=PLAN, dialog=dialog, pages=pages)

DIALOG = dict(speakers={'New employee': {'name': 'Hugo'}, 'Colleague': {'name': 'Kira'}}, lines=[
 dict(who='Colleague', en='Hi! You must be Hugo. **Nice to meet you!**', pt='Oi! Você deve ser o Hugo. Prazer em conhecer!'),
 dict(who='New employee', en='Nice to meet you, too! **I just started** this week.', pt='Prazer também! Comecei esta semana.'),
 dict(who='Colleague', en='Welcome! I’m Kira. **I work in** marketing.', pt='Bem-vindo! Eu sou a Kira. Trabalho em marketing.'),
 dict(who='New employee', en='Great. **What’s your role** there?', pt='Legal. Qual é a sua função lá?'),
 dict(who='Colleague', en='I’m a designer. I make the posters. And you?', pt='Sou designer. Faço os cartazes. E você?'),
 dict(who='New employee', en='I work in sales. I’m the new sales assistant.', pt='Trabalho em vendas. Sou o novo assistente de vendas.'),
 dict(who='Colleague', en='Perfect! Here’s my card.', pt='Perfeito! Aqui está o meu cartão.'),
 dict(who='New employee', en='Thanks! **Here’s my card**, too.', pt='Obrigado! Aqui está o meu também.'),
 dict(who='Colleague', en='Let’s have lunch this week.', pt='Vamos almoçar esta semana.'),
 dict(who='New employee', en='Sounds great!', pt='Ótimo!')])

PAGES = [
 OPEN(7, 'Meeting a colleague', 'Conhecer um colega', 'It is your first week at a new job in the United States. A colleague comes to say hello. You say what you do and exchange business cards.', 'office', ['Hugo', 'Kira'],
  'By the end of the class you can greet a new colleague, say what area you work in, ask about their role and exchange a business card.',
  ['Greet: Nice to meet you!', 'Say your area: I work in…', 'Ask the role: What’s your role?', 'Exchange contacts: Here’s my card.'],
  ['I greet my colleague.', 'I say where I work.', 'I ask about their role.', 'I exchange a card or contact.'],
  'How do you introduce yourself at a new job? Do you use first names or titles?',
  teach(goal='Abrir pela situação real: o primeiro contato com um colega novo.', solo=['Pergunte como foi (ou será) conhecer colegas no primeiro emprego.', 'Mostre os 4 critérios.'], group=['Cada estudante diz uma profissão em inglês.', 'Mostre os critérios: missão final.'], extra=['What job would you like to have?', 'Who is your favorite coworker?'], support=['Aceite respostas curtas ou em português.'])),
 dict(t='rl_warm', stage='warm', title='Connection & warm-up',
  intro=dict(solo='Start with real questions about jobs and names.', group='One question per student, then a question back to a classmate.'),
  recall='Emails and phone at work (last lesson): “This is Amy from…”. Ask: How do you say your name on the phone?',
  qs=[dict(q='What do you do?', pt='O que você faz (profissão)?', sup=['I’m a teacher.', 'I work in a bank.', 'I’m a student.']), dict(q='Where do you work?', pt='Onde você trabalha?', sup=['At a school.', 'In an office.', 'From home.']), dict(q='Do you have a business card?', pt='Você tem cartão de visita?', sup=['Yes, I do.', 'No, I don’t.', 'Only a phone number.'])],
  tip='Use the answers to find the job words the student needs.', teach=teach(goal='Entrar no idioma e levantar vocabulário de profissões.', extra=['What is your job title?', 'Do you like your team?'], errors=[W('I am teacher.', 'I’m a teacher.'), W('I work with bank.', 'I work in a bank / at a bank.')], support=['Mostre os chips de resposta.'])),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Life in the USA',
  intro='Names and titles have habits at work. Look at the cards and guess before you read.',
  cards=[dict(vis='obj:nametag', en='First names', pt='Primeiros nomes', note='In many US offices people use first names, even with managers.'), dict(vis='obj:envelope', en='Business cards', pt='Cartões de visita', note='In the US they are exchanged simply, often at meetings or events.'), dict(vis='flag:jp', en='Business cards in Japan', pt='Cartões no Japão', note='In Japan cards are exchanged formally, usually with both hands and with a small bow.')],
  qs=[dict(q='What do you call a colleague?', pt='Como chamar um colega?', levels=dict(A1='By first name.', A2='By first name. “Mr.” and “Ms.” are for formal talk.', B1='In many US offices people use first names; with clients you may use Mr. or Ms. first.', B2='First names are the norm in many workplaces, but with customers or in formal fields people start with a title.')), dict(q='What does “Ms.” mean?', pt='O que significa “Ms.”?', levels=dict(A1='A title for a woman.', A2='A title for a woman, married or not.', B1='“Ms.” is a neutral title for a woman, whatever her marital status.', B2='“Ms.” is the standard neutral title for women in business: it does not show marital status.')), dict(q='How do you ask about someone’s job?', pt='Como perguntar sobre o trabalho de alguém?', levels=dict(A1='What do you do?', A2='What do you do? / What’s your role?', B1='You can ask “What’s your role?” or “What do you do here?”', B2='“What’s your role on the team?” is a friendly way to ask what someone is responsible for.'))],
  compare='In Brazil people often use “senhor/senhora” or “doutor” early on. In many US offices first names come quickly. What do you do where you live?',
  teach=teach(goal='Ativar o contexto: nomes, títulos e cartões de visita.', solo=['Mostre os cartões e peça hipóteses.', 'Compare com a experiência do estudante.'], group=['Cada estudante escolhe um cartão e explica.', 'Pergunte “Do you agree?”.'], answers=['Q1: first names (usually).', 'Q2: a neutral title for a woman.', 'Q3: What do you do? / What’s your role?'], extra=['What title is common where you work?', 'Do you like first names at work?'], support=['Use as respostas A1 como andaime.'], stretch=['B2: discuta cuidados ao generalizar: normas variam por empresa e setor.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='office', tod='day', cast=['Hugo', 'Kira']),
  pass1=dict(q='What are Hugo and Kira doing?', pt='O que Hugo e Kira estão fazendo?', opts=['Meeting for the first time', 'Having an argument', 'Planning a trip'], ans=0),
  pass2=dict(tasks=[dict(label='Kira works in', ans='marketing'), dict(label='Kira’s role', ans='designer'), dict(label='Hugo works in', ans='sales'), dict(label='They exchange', ans='card')]),
  teach=teach(goal='Compreender o essencial antes de ver o texto.', solo=['Esconda o texto. 1ª escuta: o que acontece.', '2ª escuta: áreas, função e o que trocam.'], group=['Duplas anotam antes de revelar.', 'Compare as respostas.'], answers=['Pass 1: meeting for the first time.', 'Pass 2: marketing · designer · sales · card'], extra=['Is Hugo friendly? How do you know?', 'What is the invitation at the end?'], support=['Use “Slow” na 2ª escuta.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='When did Hugo start?', opts=['This week', 'Last year', 'Yesterday'], ans=0), dict(q='What is Kira’s role?', opts=['Designer', 'Manager', 'Driver'], ans=0), dict(q='Where does Hugo work?', opts=['In sales', 'In marketing', 'In the kitchen'], ans=0), dict(q='What does Kira suggest?', opts=['Lunch this week', 'A trip', 'A call'], ans=0)],
  retell=dict(prompt='Retell the conversation in your own words, at your level.', starters=['Kira meets…', 'She works in…', 'Hugo works in…', 'At the end they…']),
  teach=teach(goal='Ler o diálogo, perceber os chunks e recontar.', solo=['O estudante lê o Hugo; você lê a Kira.', 'Peça que reconte.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia.'], answers=['This week · designer · in sales · lunch'], extra=['What is your role?', 'What would you ask Kira?'], errors=[W('I work on marketing.', 'I work in marketing.'), W('What is your function?', 'What’s your role? / What do you do?')], support=['Mostre o PT depois da 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[C('What’s your role?', 'Qual é a sua função?', 'Ask about someone’s job on the team.', pri=True, alt='Also: **What do you do here?**'), C('I work in…', 'Eu trabalho em / na área de…', 'Say your area: I work in sales.', pri=True, alt='Also: **I’m on the … team.**'), C('I just started.', 'Acabei de começar.', 'Say you are new at the job.', pri=True), C('Here’s my card.', 'Aqui está o meu cartão.', 'Give your business card.', pri=True, alt='Also: **Here’s my number.**'),
         C('Nice to meet you.', 'Prazer em conhecer.', 'The standard greeting at a first meeting.'), C('How do you pronounce your name?', 'Como se pronuncia o seu nome?', 'Ask this if you are not sure. People usually like it.', reg='polite'), C('Let’s have lunch.', 'Vamos almoçar.', 'A friendly invitation.', reg='informal')],
  discover=dict(fns=['Greeting', 'Area of work', 'Role', 'Contact', 'Inviting'], items=[dict(en='Nice to meet you.', fn='Greeting'), dict(en='I work in marketing.', fn='Area of work'), dict(en='What’s your role?', fn='Role'), dict(en='Here’s my card.', fn='Contact'), dict(en='Let’s have lunch.', fn='Inviting')]),
  note='Choose 3–5 expressions (★) to use again and again.', teach=teach(goal='Escolher 3–5 chunks e descobrir a função.', solo=['Pergunte “When do you say it?”.', 'Peça um exemplo próprio.'], group=['Cada estudante escolhe uma ★ e explica.', 'Compare em duplas.'], answers=['Greeting · Area of work · Role · Contact · Inviting'], extra=['Which one is for a first meeting?'], errors=[W('What is your function?', 'What’s your role?'), W('I work on sales.', 'I work in sales.')], support=['Só as 3–4 ★.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Saying where you work', formula='**I work in** + area · **I work at** + company', ex=['I work in sales.', 'I work in marketing.', 'I work at a bank.'], main=True), dict(name='Asking about a role', formula='**What’s your role** + (on the team)?', ex=['What’s your role?', 'What’s your role on the team?', 'What’s your role there?'], main=True),
            dict(name='Saying your job', formula='**I’m a** + job', ex=['I’m a designer.', 'I’m a sales assistant.']), dict(name='Offering a card', formula='**Here’s** + my card / my number', ex=['Here’s my card.', 'Here’s my number.'])],
  swap=dict(frame='Hi, I’m {name}. I work in {area}. I’m {job}.', tpt='Oi, eu sou {name}. Trabalho em {area}. Sou {job}.',
   slots=[dict(k='name', label='Name', opts=O(('Hugo', 'Hugo'), ('Kira', 'Kira'), ('Sam', 'Sam'))), dict(k='area', label='Area', opts=O(('sales', 'vendas'), ('marketing', 'marketing'), ('support', 'suporte'))), dict(k='job', label='Job', opts=O(('a designer', 'designer'), ('an assistant', 'assistente'), ('a manager', 'gerente')))]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['I work in sales.', 'I am employed in the sales department.'], ['What’s your role?', 'What is your position within the company?'], ['Here’s my card.', 'Please find my contact details below.'], ['Nice to meet you!', 'It is a pleasure to meet you.']], note='These are differences of context and register, not absolute rules.'),
  teach=teach(goal='Fixar 2 padrões (I work in… / What’s your role?). in × at.', solo=['Mostre o padrão no diálogo.', 'Use “Swap the words”.'], group=['Troca em cadeia.', 'Em pares.'], answers='Padrões 01/02 são o foco; 03/04 são expansão.', extra=['Say your real job and area.', 'Ask a classmate about his or her role.'], errors=[W('I work on sales.', 'I work in sales.'), W('I am designer.', 'I’m a designer.'), W('What is your role? (sem entonação amigável)', 'What’s your role? (com um sorriso)')], support=['Só I work in… na primeira rodada.'], stretch=['Combine: I work in sales, and I just started. What’s your role?'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Long and short “i”', tip='Meet has a long /i/ sound; it is a short, relaxed /ɪ/ in “mit” or “sit”. In Portuguese we have only one “i”: practice the difference.',
  items=[dict(say='Nice to meet you.', linked='NICE to MEET you.', ipa='/mit/', rhythm='OoOo'), dict(say='Please sit.', linked='PLEASE SIT.', ipa='/pliz sɪt/', rhythm='OO'), dict(say='He is in the team.', linked='He is in the TEAM.', ipa='/tim/', rhythm='oooooO')],
  identify=[dict(q='Which word do you hear?', opts=['seat', 'sit', 'set'], ans=1, say='sit'), dict(q='Which word do you hear?', opts=['meet', 'mit', 'mat'], ans=0, say='meet')],
  own=dict(prompt='Write one sentence with “meet”, “team” and “sit”.', criteria='Say it twice. Is “meet” long and “sit” short?'),
  teach=teach(goal='UM só fenômeno: /i/ longo × /ɪ/ curto (meet × sit).', solo=['Modele com o sorriso para /i/ e boca relaxada para /ɪ/.', 'Identify e depois uso próprio.'], group=['Coro, depois duplas.', 'Cada um cria uma frase.'], answers=['Identify 1: sit · Identify 2: meet'], errors=[W('sit = “sít” longo', 'sit /sɪt/ curto'), W('meet = “mit” curto', 'meet /mit/ longo')], support=['Pratique só meet/sit/team.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    MC('1. A colleague says hello for the first time.', ['Nice to meet you!', 'Good night!', 'See you!'], 0, 'The standard first-meeting greeting.'),
    MC('2. You want to say your area.', ['I work in sales.', 'I work on sales.', 'I am work sales.'], 0, 'I work in + area.'),
    MC('3. You want to know your colleague’s job.', ['What’s your role?', 'Who is your role?', 'Where is job?'], 0, 'What’s your role?'),
    MC('4. You want to give your contact.', ['Here’s my card.', 'My card is a here.', 'Card, give.'], 0, 'Here’s + object.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    GAP('I work ___ marketing.', 'in', 'I work in + area.', bank=['in', 'on', 'for']),
    GAP('What’s your ___?', 'role', 'What’s your role?', bank=['role', 'rule', 'row']),
    SW('Say it with “I work in”:', 'sales', ['I work in sales.', 'I work in sales'], 'I work in sales.', 'I work in + area.'),
    SW('Ask about the role:', 'your role', ['What’s your role?', 'What is your role?'], 'What’s your role?', 'What’s your role?'),
    RP('Hi! You must be Hugo. Nice to meet you!', 'Choose the best reply.', ['Nice to meet you, too!', 'I am a role.', 'Here is the lunch.'], 0, 'Return the greeting.'),
    RP('Here’s my card.', 'Choose the best reply.', ['Thanks! Here’s my card, too.', 'No, I am card.', 'I work on it.'], 0, 'Thank and exchange.')])],
  teach=teach(goal='Do controlado ao guiado antes da fala livre.', solo=['Peça que justifique cada resposta.', 'Se acertar rápido, peça outra versão.'], group=['Resolvam em duplas e comparem.', 'Equipes: ponto por resposta justificada.'], answers=['1: Nice to meet you! · 2: I work in sales. · 3: What’s your role? · 4: Here’s my card.', 'Gap: in · role · I work in sales. · What’s your role? · Nice to meet you, too! · Thanks! Here’s my card, too.'], extra=['Say each answer with a handshake and a smile.'], errors=[W('I work on marketing.', 'I work in marketing.'), W('What’s your function?', 'What’s your role?')], support=['Ofereça o banco de palavras.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — meet your team',
  brief=dict(teacher='You are a colleague. Ask about the job and give a business card at the end.', student='You are the new employee: greet, say your area, ask about the role and exchange a card.'),
  orders=['Greet and say you just started', 'Say your area and your job', 'Ask about the colleague’s role', 'Exchange cards and say goodbye'],
  complications=['You do not know how to say your job.', 'The colleague’s name is hard: ask how to pronounce it.', 'You forgot your cards: give your number.', 'The colleague speaks fast.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['Nice to meet you.', 'I work in…', 'What’s your role?', 'Here’s my card.']), dict(label='Keywords', desc='Only the keywords', help=['meet', 'work in', 'role', 'card', 'lunch'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I greet my colleague.', 'I say where I work.', 'I ask about their role.', 'I exchange a card or contact.'],
  teach=teach(goal='Simulação com complicação e três rodadas com menos apoio.', solo=['Use a profissão real do estudante.', 'Rodada 1: chunks. Rodada 2: palavras-chave. Rodada 3: sem roteiro.', 'Anote 2–3 correções.'], extra=['How do you ask for the pronunciation of a name?'], errors=[W('How I pronounce?', 'How do you pronounce your name?')], support=['Volte à rodada 1 se travar.'], stretch=['Apresente um colega a outro.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Greet', min=3, task='Say hello. Say you are new.', hint='Nice to meet you. / I just started.'), dict(title='Where do you work?', min=3, task='Say your area and ask about your partner’s role.', hint='I work in… / What’s your role?'), dict(title='Exchange', min=3, task='Exchange cards or numbers.', hint='Here’s my card.'), dict(title='Introduce a partner', min=2, whole=True, task='Whole group: introduce your partner to the group.', hint='This is… He/She works in…')],
  infogap=dict(title='Team list', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='Student A', task='You know two people. Ask about the rest.', rows=[dict(k='Kira', v='designer, marketing'), dict(k='Hugo', v=''), dict(k='Sam', v='manager, sales'), dict(k='Dina', v='')]),
   b=dict(title='Student B', task='You know two people. Ask about the rest.', rows=[dict(k='Kira', v=''), dict(k='Hugo', v='assistant, sales'), dict(k='Sam', v=''), dict(k='Dina', v='accountant, finance')])),
  teach=teach(goal='Fluência por repetição com informações novas.', group=['Troque os pares a cada rodada.', 'Sem salas simultâneas: interações sequenciais.', 'Cada aluno faz ≥1 pergunta e ≥1 resposta.'], answers=['A: Kira designer marketing; Sam manager sales. B: Hugo assistant sales; Dina accountant finance.'], extra=['What’s Dina’s role?', 'Who works in sales?'], errors=[W('He work in sales.', 'He works in sales.'), W('She is a accountant.', 'She’s an accountant.')], support=['Dê frases-modelo no chat.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — your first week',
  goal='Each group must meet new colleagues, say what they do and exchange contacts.',
  missions=[dict(who='A', role='New employee + colleague', mission='Introduce yourselves. Say your areas and roles.', constraint='Use “I work in…” and “What’s your role?”', start='Hi! Nice to meet you…'), dict(who='B', role='Two new employees', mission='Introduce yourselves to a manager and ask how to pronounce her name.', constraint='Use “How do you pronounce…?” and “I just started.”', start='Excuse me, I just started…'), dict(who='C', role='Three colleagues', mission='Exchange cards and invite each other to lunch.', constraint='Use “Here’s my card.” and “Let’s have lunch.”', start='Hi! Here’s my…')], min=11,
  success=['Greet.', 'Say where you work.', 'Ask about the role.', 'Exchange contacts.'],
  teach=teach(goal='Realizar algo com o inglês: conhecer colegas e trocar contatos.', group=['Cada grupo recebe papel, restrição e missão.', 'Progressão: com apoio → palavras-chave → sem roteiro.', 'Anote 2–3 correções.'], answers=['Modelo: “Nice to meet you!” → “I work in sales. What’s your role?” → “I’m a designer. Here’s my card.”'], extra=['What if you forget the name?'], support=['Dê o início de frase em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short message to introduce yourself to your new team. Say your name, your area and your role.',
  steps=['Greeting', 'Name and area', 'Role', 'Closing'],
  model='Hi team! I’m Hugo. **I just started** this week. **I work in** sales, and I’m the new assistant. Nice to meet you all! Let’s have lunch soon.',
  checklist=['I greeted the team.', 'I said my name and area.', 'I said my role.', 'I closed in a friendly way.'],
  tip='Fix only 2–3 priority points. Show a more natural way to say the same idea.', fix=dict(n=3),
  teach=teach(goal='Produção escrita curta ligada à situação.', solo=['Peça o texto; corrija 2–3 pontos.'], group=['Troquem os textos e corrijam em duplas.'], extra=['Add one thing you like about the new job.'], errors=[W('I am work in sales.', 'I work in sales.'), W('Nice meet you.', 'Nice to meet you.')], support=['Dê o modelo e peça só para trocar os dados.'])),
 FEEDBACK('Example: You said your area and asked about the role clearly.', 'Example: Make “meet” long and “sit” short.', 'Example: Introduce yourself to three people without notes.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❓', name='Build a question', prompt='Without notes: ask a colleague about his or her job.', model='What’s your role?'), dict(ic='💬', name='Respond to a situation', prompt='“What do you do?” You work in marketing.', model='I work in marketing.'), dict(ic='⭐', name='Use a new expression', prompt='Give your card to a new colleague.', model='Here’s my card.')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 30-second audio introducing yourself at a new job.', 'Write the job titles of three people you know in English.', 'Practice meet/sit, team/it aloud.', 'Listen to the dialogue again and underline two expressions.']),
  spaced=dict(next=['What’s your role?', 'I work in…', 'I just started.'], week=['Here’s my card.', 'Nice to meet you.', 'Let’s have lunch.'], unit=['Greet · say your area · exchange contacts']),
  teach=teach(goal='Toda aula termina com uma produção observável.', solo=['Sem anotações: pergunta, resposta e expressão nova.'], group=['Exit challenge individual; combine a tarefa.'], answers=['What’s your role? · I work in marketing. · Here’s my card.'], extra=['Revisão espaçada: próxima aula, uma semana e missão da unidade.'])),
 LEVELS([('Hi. Hugo. Sales.', 'Say your name and area with words.'), ('Nice to meet you. I work in sales. What’s your role?', 'Greet and exchange roles.'), ('I just started in sales, so I’m still learning the team.', 'Say how new you are.'), ('I joined the sales team last week, and I’m looking forward to working with marketing.', 'Show how teams connect.'), ('I’d love to hear how marketing and sales could collaborate more closely on upcoming campaigns.', 'Open a work conversation.'), ('I’d be delighted to explore where our teams’ efforts might usefully converge in the coming quarter.', 'Use a polished professional register.')], you='A1')]

LESSON = LESSON_OF(47, 'Meeting a colleague', 'Meeting a colleague', 'Conhecer um colega', 7, ['Hugo', 'Kira'], 'office', DIALOG, PAGES)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
