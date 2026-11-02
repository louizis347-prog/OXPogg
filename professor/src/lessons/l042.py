#!/usr/bin/env python3
"""Aula 42 · Asking about the schedule (A1, 60 min). Gera data/v3/042.json."""
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

DIALOG = dict(speakers={'Student': {'name': 'Alma'}, 'Front desk': {'name': 'Zara'}}, lines=[
 dict(who='Student', en='Excuse me! **What time does** English class **start**?', pt='Com licença! A que horas começa a aula de inglês?'),
 dict(who='Front desk', en='It starts at nine thirty.', pt='Começa às nove e meia.'),
 dict(who='Student', en='Is that **a.m. or p.m.**?', pt='É da manhã ou da tarde/noite?'),
 dict(who='Front desk', en='A.m. — in the morning!', pt='Da manhã!'),
 dict(who='Student', en='Great. And **when is** the speaking test?', pt='Ótimo. E quando é a prova de fala?'),
 dict(who='Front desk', en='It’s next Friday at two p.m.', pt='É na próxima sexta, às duas da tarde.'),
 dict(who='Student', en='Sorry, **is it on Monday**?', pt='Desculpe, é na segunda?'),
 dict(who='Front desk', en='No, on Friday. There’s no class on Monday.', pt='Não, na sexta. Não há aula na segunda.'),
 dict(who='Student', en='**What time does** class **end**?', pt='A que horas a aula termina?'),
 dict(who='Front desk', en='At eleven. Have a good day!', pt='Às onze. Tenha um bom dia!')])

PAGES = [
 OPEN(2, 'Asking about the schedule', 'Perguntar sobre horários', 'You are a new student at a language school in the United States. You ask the front desk when class starts, when the test is and which day it is.', 'classroom', ['Alma', 'Zara'],
  'By the end of the class you can ask what time something starts or ends, ask when an event is, check the day and understand a.m. and p.m.',
  ['Ask the time: What time does… start?', 'Ask the day: When is…? / Is it on Monday?', 'Check the time: Is that a.m. or p.m.?', 'Understand days and times in a short answer'],
  ['I ask about a time.', 'I check the day.', 'I confirm a.m. or p.m.', 'I repeat the information to be sure.'],
  'In Brazil you say “às 14h”. How do you think people say this in the United States?',
  teach(goal='Abrir pela situação real: não perder a aula nem a prova por não entender o horário.', solo=['Pergunte se o estudante já perdeu um compromisso por confundir horário ou dia.', 'Mostre os 4 critérios de sucesso.'], group=['Cada estudante diz um horário em português; o grupo tenta dizer em inglês.', 'Mostre os critérios: serão a missão final.'], extra=['What time do you wake up?', 'Which day is your favorite?'], support=['Aceite respostas em português e reformule em inglês.'])),
 dict(t='rl_warm', stage='warm', title='Connection & warm-up',
  intro=dict(solo='Start with real questions about the student’s week.', group='One question per student, then a question back to a classmate.'),
  recall='First day in class (last lesson): “How do you spell…?”. Ask: How do you spell your last name?',
  qs=[dict(q='What day is today?', pt='Que dia é hoje?', sup=['It’s Monday.', 'It’s Tuesday.', 'It’s Friday.']), dict(q='What time is it now?', pt='Que horas são agora?', sup=['It’s ten o’clock.', 'It’s almost noon.', 'It’s three thirty.']), dict(q='What is your busiest day?', pt='Qual é o seu dia mais cheio?', sup=['Monday.', 'Saturday.', 'Every day!'])],
  tip='Use the answers to find gaps with numbers and days.', teach=teach(goal='Entrar no idioma e testar números e dias da semana.', extra=['What time do you eat lunch?', 'What do you do on Sundays?'], errors=[W('It’s 3 hours.', 'It’s three o’clock.'), W('In Monday', 'On Monday')], support=['Mostre os chips de resposta e peça que escolham.'])),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Life in the USA',
  intro='Times and schedules look different in the United States. Look at the cards and guess before you read.',
  cards=[dict(vis='obj:clock', en='12-hour clock', pt='Relógio de 12 horas', note='Daily life: 9:30 a.m., 2:00 p.m. — a.m. is morning, p.m. is afternoon and night.'), dict(vis='obj:board', en='Class timetable', pt='Grade de aulas', note='Many colleges use Mon/Wed/Fri or Tue/Thu classes.'), dict(vis='obj:bell', en='24-hour clock', pt='Relógio de 24 horas', note='In the US it is used mainly by the military and some jobs, like hospitals.')],
  qs=[dict(q='How do Americans say 2 p.m.?', pt='Como os americanos dizem 14h?', levels=dict(A1='Two p.m. Two o’clock.', A2='They say “two p.m.” or “two in the afternoon”.', B1='They use the 12-hour clock: 2 p.m. instead of 14:00.', B2='In daily life they use a.m./p.m. and avoid 14:00, except in the military or some professions.')), dict(q='Why is a.m. or p.m. important?', pt='Por que a.m. ou p.m. é importante?', levels=dict(A1='9 a.m. is morning. 9 p.m. is night.', A2='Without it, “nine” can be morning or night.', B1='Because the same number appears twice a day, so you must be clear.', B2='Without a.m./p.m. the time is ambiguous, so people often add “in the morning” or “at night”.')), dict(q='How can you be sure about a time?', pt='Como ter certeza do horário?', levels=dict(A1='I ask again.', A2='I say: “Is that a.m. or p.m.?”', B1='I repeat the time and ask them to confirm.', B2='I repeat it, check the day and ask them to write it down if it is important.'))],
  compare='In Brazil many schedules and tickets use the 24-hour clock (14h, 18h30). In the US it is usually a.m./p.m. What do you use at school or work?',
  teach=teach(goal='Ativar o contexto do relógio de 12 horas e das grades de horários.', solo=['Mostre os cartões e peça hipóteses.', 'Escreva 14:00 e peça que diga “two p.m.”.'], group=['Cada estudante escolhe um cartão e explica.', 'Pergunte “Do you agree?”.'], answers=['Q1: two p.m.', 'Q2: the same number appears morning and night.', 'Q3: Is that a.m. or p.m.?'], extra=['What time do your classes or work start?', 'Do you like the 24-hour clock?'], support=['Use as respostas A1 como andaime.'], stretch=['B2: compare grades de horário em escolas do Brasil e dos EUA.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='classroom', tod='day', cast=['Alma', 'Zara']),
  pass1=dict(q='What is Alma asking about?', pt='Sobre o que a Alma pergunta?', opts=['Class and test times', 'A library book', 'A bus ticket'], ans=0),
  pass2=dict(tasks=[dict(label='Class starts at', ans='nine thirty'), dict(label='The test is on (day)', ans='Friday'), dict(label='Test time (p.m.)', ans='two'), dict(label='Class ends at', ans='eleven')]),
  teach=teach(goal='Compreender horários e dias antes de ver o texto.', solo=['Esconda o texto. 1ª escuta: tema.', '2ª escuta: hora de início, dia da prova, hora da prova, término.'], group=['Duplas anotam antes de revelar.', 'Compare as respostas.'], answers=['Pass 1: class and test times.', 'Pass 2: nine thirty · Friday · two (p.m.) · eleven'], extra=['Is the class in the morning or afternoon?', 'Why does Alma ask “a.m. or p.m.?”'], support=['Use “Slow” na 2ª escuta e pause depois de cada informação.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='What time does the class start?', opts=['9:30 a.m.', '2:00 p.m.', '11:00 a.m.'], ans=0), dict(q='When is the speaking test?', opts=['Next Friday', 'Next Monday', 'Today'], ans=0), dict(q='Is there class on Monday?', opts=['No', 'Yes, at nine', 'Only in the afternoon'], ans=0), dict(q='What time does class end?', opts=['At eleven', 'At two', 'At nine thirty'], ans=0)],
  retell=dict(prompt='Retell the conversation in your own words, at your level.', starters=['Alma asks about…', 'The class starts at…', 'The test is on…', 'Class ends at…']),
  teach=teach(goal='Ler o diálogo, perceber os chunks e recontar.', solo=['Papéis invertidos na 2ª leitura.', 'Peça que reconte.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia.'], answers=['9:30 a.m. · next Friday · no · at eleven'], extra=['What time is the test? (two p.m.)', 'What day is it today?'], errors=[W('What time starts the class?', 'What time does the class start?'), W('The test is in Friday.', 'The test is on Friday.')], support=['Mostre o PT depois da 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[C('What time does… start?', 'A que horas… começa?', 'Ask the start time of a class, a movie, a meeting.', pri=True, alt='Also: **What time is the class?**'), C('When is…?', 'Quando é…?', 'Ask the day or date of an event.', pri=True), C('Is it on Monday?', 'É na segunda?', 'Check the day. Use “on” with days.', pri=True, alt='Also: **Is that on Monday?**'), C('Is that a.m. or p.m.?', 'É da manhã ou da tarde/noite?', 'Make sure you have the right part of the day.', pri=True),
         C('What time does it end?', 'A que horas termina?', 'Ask the end time.', alt='Also: **When does it finish?**'), C('It starts at…', 'Começa às…', 'Give a start time: It starts at nine.'), C('Could you write it down?', 'Você poderia anotar?', 'Ask for the time in writing when it is important.', reg='polite')],
  discover=dict(fns=['Asking the time', 'Asking the day', 'Checking', 'Answering', 'Asking for help'], items=[dict(en='What time does class start?', fn='Asking the time'), dict(en='When is the speaking test?', fn='Asking the day'), dict(en='Is that a.m. or p.m.?', fn='Checking'), dict(en='It starts at nine thirty.', fn='Answering'), dict(en='Could you write it down?', fn='Asking for help')]),
  note='Choose 3–5 expressions (★) to use again and again.', teach=teach(goal='Escolher 3–5 chunks e descobrir a função de cada um.', solo=['Pergunte “When do you say it?”.', 'Peça um exemplo com a rotina do estudante.'], group=['Cada estudante escolhe uma ★ e explica.', 'Compare em duplas.'], answers=['Asking the time · Asking the day · Checking · Answering · Asking for help'], extra=['Which one do you need for your own schedule?'], errors=[W('What hour starts?', 'What time does it start?'), W('The class is at Monday.', 'The class is on Monday.')], support=['Trabalhe só as expressões ★.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Asking for a time', formula='**What time does** + thing + start / end?', ex=['What time does class start?', 'What time does the test end?', 'What time does the library close?'], main=True), dict(name='Asking for a day', formula='**When is** + the + event?', ex=['When is the speaking test?', 'When is the next class?', 'When is the party?'], main=True),
            dict(name='Days and times', formula='**on** + day · **at** + time', ex=['It’s on Friday.', 'It’s at two p.m.', 'It’s on Monday at nine.']), dict(name='Yes/No check', formula='**Is it** + on + day?', ex=['Is it on Monday?', 'Is it at nine?'])],
  swap=dict(frame='What time does {event} {verb}? It’s {day}.', tpt='A que horas {event} {verb}? É {day}.',
   slots=[dict(k='event', label='Event', opts=O(('the class', 'a aula'), ('the test', 'a prova'), ('the movie', 'o filme'))), dict(k='verb', label='Verb', opts=O(('start', 'começa'), ('end', 'termina'), ('open', 'abre'))), dict(k='day', label='Day', opts=O(('on Monday', 'na segunda'), ('on Friday', 'na sexta'), ('on Saturday', 'no sábado')))]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['What time does it start?', 'At what time does the session begin?'], ['Two p.m.', '2:00 p.m.'], ['Is it on Monday?', 'Will it take place on Monday?'], ['It’s at nine.', 'The class begins at 9:00 a.m.']], note='These are differences of context and register, not absolute rules.'),
  teach=teach(goal='Fixar 2 padrões (What time does… / When is…?); on para dias, at para horas.', solo=['Mostre o padrão no diálogo.', 'Use “Swap the words”.'], group=['Troca em cadeia.', 'Em pares: um escolhe as peças.'], answers='Padrões 01/02 são o foco; 03/04 são expansão.', extra=['Change the day and say the sentence.', 'Ask the same question about your job.'], errors=[W('What time starts the class?', 'What time does the class start?'), W('The class starts in Monday.', 'The class starts on Monday.'), W('What time does it starts?', 'What time does it start?')], support=['Só What time does… start? na primeira rodada.'], stretch=['Combine: When is the test, and what time does it start?'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Word stress in numbers', tip='Thirteen has the strong sound at the end (thir-TEEN). Thirty has it at the start (THIR-ty). That changes the time!',
  items=[dict(say='thirteen', linked='thir·TEEN', ipa='/θɝˈtin/', rhythm='oO'), dict(say='thirty', linked='THIR·ty', ipa='/ˈθɝdi/', rhythm='Oo'), dict(say='fifteen — fifty', linked='fif·TEEN — FIF·ty', ipa='/fɪfˈtin/ — /ˈfɪfti/', rhythm='oOOo')],
  identify=[dict(q='Which one do you hear?', opts=['thirteen', 'thirty', 'three'], ans=0, say='thirteen'), dict(q='Which one do you hear?', opts=['fifteen', 'fifty', 'fit'], ans=1, say='fifty')],
  own=dict(prompt='Say three times you know: your class start, your lunch and your bedtime.', criteria='Did your partner understand 13 vs 30 and 15 vs 50?'),
  teach=teach(goal='UM só fenômeno: acento nos números -teen × -ty.', solo=['Modele thirteen × thirty e peça que o estudante bata na sílaba forte.', 'Faça o identify e depois o uso próprio.'], group=['Coro, depois duplas: um diz, o outro identifica.', 'Cada um cria uma hora própria.'], answers=['Identify 1: thirteen · Identify 2: fifty'], errors=[W('thirty com acento no fim', 'THIR-ty'), W('thirteen sem o “n” final claro', 'thir-TEEN, com a vogal longa')], support=['Use gestos: mão alta para a sílaba forte.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    MC('1. You want the start time of class.', ['What time does class start?', 'What hour is class beginning?', 'Class is what time?'], 0, 'What time does + noun + start?'),
    MC('2. You want the date of the test.', ['When is the test?', 'Where is the test?', 'Who is the test?'], 0, 'When is…? asks for the day or date.'),
    MC('3. You hear “nine”. You are not sure.', ['Is that a.m. or p.m.?', 'Is that a coffee?', 'Is that a test?'], 0, 'Check a.m. or p.m.'),
    MC('4. The class is on Friday. Which is correct?', ['It’s on Friday.', 'It’s in Friday.', 'It’s at Friday.'], 0, 'Use on with days.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    GAP('What time ___ the class start?', 'does', 'What time does…?', bank=['does', 'is', 'do']),
    GAP('The test is ___ Monday.', 'on', 'on + day.', bank=['on', 'in', 'at']),
    SW('Ask about the day:', 'the speaking test', ['When is the speaking test?', 'When is the speaking test'], 'When is the speaking test?', 'When is + event?'),
    SW('Check the day:', 'Monday', ['Is it on Monday?', 'Is it on Monday'], 'Is it on Monday?', 'Is it on + day?'),
    RP('It starts at nine.', 'You want to be sure. Choose the best reply.', ['Is that a.m. or p.m.?', 'I am nine.', 'It starts a book.'], 0, 'Check the part of the day.'),
    RP('Class ends at eleven.', 'Choose the best reply.', ['Thanks! Eleven a.m.?', 'On Friday.', 'Please, a coffee.'], 0, 'Repeat to confirm the information.')])],
  teach=teach(goal='Do controlado ao guiado antes da fala livre.', solo=['Peça que justifique cada resposta.', 'Se acertar rápido, peça a pergunta mais polida.'], group=['Resolvam em duplas e comparem.', 'Equipes: ponto por resposta justificada.'], answers=['1: What time does class start? · 2: When is the test? · 3: Is that a.m. or p.m.? · 4: It’s on Friday.', 'Gap: does · on · When is the speaking test? · Is it on Monday? · Is that a.m. or p.m.? · Thanks! Eleven a.m.?'], extra=['Say each answer with the time you really have class.'], errors=[W('What time is start?', 'What time does it start?'), W('It’s in Friday.', 'It’s on Friday.')], support=['Ofereça o banco de palavras nas lacunas.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — check your schedule',
  brief=dict(teacher='You are the front desk. Give times and days quickly, and change one detail during the scene.', student='You are a student: find out the time, the day and a.m./p.m. for your class and test.'),
  orders=['Ask the start time of the class', 'Ask the day of the speaking test', 'Check Monday and confirm a.m./p.m.', 'Ask what time class ends'],
  complications=['The desk says a time too fast.', 'The class changes to another day.', 'You do not know if it is a.m. or p.m.', 'The desk says thirteen but you heard thirty.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['What time does… start?', 'When is…?', 'Is it on Monday?', 'Is that a.m. or p.m.?']), dict(label='Keywords', desc='Only the keywords', help=['start', 'test', 'Monday', 'a.m.', 'end'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I ask about a time.', 'I check the day.', 'I confirm a.m. or p.m.', 'I repeat the information.'],
  teach=teach(goal='Simulação com complicação e três rodadas com menos apoio.', solo=['Use o horário real das aulas do estudante.', 'Rodada 1: chunks. Rodada 2: palavras-chave. Rodada 3: sem roteiro.', 'Anote 2–3 correções.'], extra=['What if the class changes to another day?'], errors=[W('The class is on the 2 hours.', 'The class is at two o’clock.')], support=['Volte à rodada 1 se travar.'], stretch=['Remarque a prova e confirme a nova data.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Simple questions', min=3, task='Ask your partner what time class starts.', hint='What time does… start?'), dict(title='Which day?', min=3, task='Ask when the test or the event is.', hint='When is…? / Is it on Monday?'), dict(title='Check a.m. or p.m.', min=3, task='Say a time fast. Your partner checks.', hint='Is that a.m. or p.m.?'), dict(title='Class timetable', min=2, whole=True, task='Whole group: build one week of classes together.', hint='It’s on… at…')],
  infogap=dict(title='Class timetable', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='Student A', task='You know English and Math. Ask about the rest.', rows=[dict(k='English', v='Mon, 9:30 a.m.'), dict(k='Math', v=''), dict(k='Art', v='Wed, 1:00 p.m.'), dict(k='Music', v='')]),
   b=dict(title='Student B', task='You know Math and Music. Ask about the rest.', rows=[dict(k='English', v=''), dict(k='Math', v='Tue, 11:00 a.m.'), dict(k='Art', v=''), dict(k='Music', v='Fri, 4:15 p.m.')])),
  teach=teach(goal='Fluência por repetição com informações novas.', group=['Troque os pares a cada rodada.', 'Sem salas simultâneas: interações sequenciais.', 'Cada aluno faz ≥1 pergunta e ≥1 resposta.'], answers=['A: English Mon 9:30 a.m.; Art Wed 1:00 p.m. B: Math Tue 11:00 a.m.; Music Fri 4:15 p.m.'], extra=['What time does Math start?', 'Is Art on Wednesday?'], errors=[W('Is on Tuesday?', 'Is it on Tuesday?'), W('Four fifteen of the afternoon', 'Four fifteen p.m.')], support=['Dê frases-modelo no chat.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — plan the week',
  goal='Each group must find the right time and day, check it and confirm it.',
  missions=[dict(who='A', role='Student + front desk', mission='Find out when and at what time the English class and the test are.', constraint='Use “What time does…?” and “When is…?”', start='Excuse me! What time…'), dict(who='B', role='Two students', mission='You both want the same class. Check the days and the a.m./p.m. and choose one.', constraint='Use “Is it on…?” and “Is that a.m. or p.m.?”', start='Hi! Is it on…'), dict(who='C', role='Student + teacher', mission='The teacher changes the class day. Ask for the new day and the time and write it down.', constraint='Ask “Could you write it down?” once.', start='Sorry, when is…')], min=11,
  success=['Ask about the time.', 'Check the day.', 'Check a.m. or p.m.', 'Repeat the information.'],
  teach=teach(goal='Realizar algo com o inglês: resolver o horário.', group=['Cada grupo recebe papel, restrição e missão.', 'Progressão: com apoio → palavras-chave → sem roteiro.', 'Anote 2–3 correções.'], answers=['Modelo: “What time does the class start?” → “At nine thirty.” → “Is that a.m. or p.m.?” → “A.m.”'], extra=['What if the teacher changes the day again?'], support=['Dê o início de frase em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short message to a friend with your class schedule for next week. Give two days and two times.',
  steps=['Greeting', 'Class and day', 'Time with a.m./p.m.', 'Closing'],
  model='Hi Sam! My class is **on Monday** and Wednesday. **It starts at** 9:30 a.m. and ends at 11:00 a.m. The test is on Friday at 2:00 p.m. See you soon!',
  checklist=['I greeted my friend.', 'I used on with the days.', 'I used a.m. or p.m.', 'I closed politely.'],
  tip='Fix only 2–3 priority points. Show a more natural way to say the same idea.', fix=dict(n=3),
  teach=teach(goal='Produção escrita curta ligada à situação.', solo=['Peça o texto; corrija 2–3 pontos.'], group=['Troquem os textos e corrijam em duplas.'], extra=['Add the room number.'], errors=[W('My class is in Monday.', 'My class is on Monday.'), W('At 9:30 of the morning.', 'At 9:30 a.m.')], support=['Dê o modelo e peça só para trocar dias e horas.'])),
 FEEDBACK('Example: You asked about the day and checked a.m. or p.m.', 'Example: Practice thirteen vs thirty.', 'Example: Ask for two schedule changes without notes.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❓', name='Build a question', prompt='Without notes: ask when the test is.', model='When is the test?'), dict(ic='💬', name='Respond to a situation', prompt='Someone says: “It starts at nine.” You are not sure.', model='Is that a.m. or p.m.?'), dict(ic='⭐', name='Use a new expression', prompt='Check if the class is on Monday.', model='Is it on Monday?')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Write your weekly schedule in English with days and times.', 'Record a 45-second audio asking about a class time.', 'Practice 13/30, 14/40, 15/50 aloud.', 'Listen to the dialogue again and underline two expressions.']),
  spaced=dict(next=['What time does… start?', 'When is…?', 'Is it on Monday?'], week=['Is that a.m. or p.m.?', 'What time does it end?', 'Could you write it down?'], unit=['Ask the time · check the day']),
  teach=teach(goal='Toda aula termina com uma produção observável.', solo=['Sem anotações: pergunta, resposta e expressão nova.'], group=['Exit challenge individual; combine a tarefa.'], answers=['When is the test? · Is that a.m. or p.m.? · Is it on Monday?'], extra=['Revisão espaçada: próxima aula, uma semana e missão da unidade.'])),
 LEVELS([('Class, nine. Monday?', 'Ask with words and gestures.'), ('What time does the class start? Is it on Monday?', 'Ask about the time and day.'), ('Could you tell me what time the speaking test starts on Friday?', 'Ask politely and indirectly.'), ('I was wondering whether the schedule has changed, since the class used to start earlier.', 'Ask about a change.'), ('I’d appreciate it if you could confirm whether the session has been moved to the afternoon.', 'Request confirmation formally.'), ('Might I trouble you to confirm whether the revised timetable still holds for Friday’s session?', 'Use formal register with tact.')], you='A1')]

LESSON = LESSON_OF(42, 'Asking about the schedule', 'Asking about the schedule', 'Perguntar sobre horários', 2, ['Alma', 'Zara'], 'classroom', DIALOG, PAGES)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
