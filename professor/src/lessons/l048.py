#!/usr/bin/env python3
"""Aula 48 · Real-Life Mission Day 6 (A1, 60 min). Gera data/v3/048.json."""
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

DIALOG = dict(speakers={'New employee': {'name': 'Raj'}, 'Teammate': {'name': 'Pia'}}, lines=[
 dict(who='Teammate', en='Hi Raj! How’s your first week?', pt='Oi, Raj! Como está a sua primeira semana?'),
 dict(who='New employee', en='Good! **I just started.** **I work in** sales.', pt='Boa! Acabei de começar. Trabalho em vendas.'),
 dict(who='New employee', en='**What time does** the team meeting **start**?', pt='A que horas começa a reunião da equipe?'),
 dict(who='Teammate', en='At ten a.m., in room two.', pt='Às dez da manhã, na sala dois.'),
 dict(who='New employee', en='Thanks. **Can I borrow** a laptop for the meeting?', pt='Obrigado. Posso pegar um notebook emprestado para a reunião?'),
 dict(who='Teammate', en='Sure! Ask the front desk.', pt='Claro! Peça na recepção.'),
 dict(who='New employee', en='Great. **Could you send** me the schedule?', pt='Ótimo. Você poderia me enviar o cronograma?'),
 dict(who='Teammate', en='Of course. I’ll email it today.', pt='Claro. Vou enviar por e-mail hoje.'),
 dict(who='New employee', en='**Thanks for your help.**', pt='Obrigado pela ajuda.'),
 dict(who='Teammate', en='Anytime! Let’s have lunch together.', pt='Quando quiser! Vamos almoçar juntos.')])

PAGES = [
 OPEN(8, 'Real-Life Mission Day 6', 'Missão da unidade 6', 'It is your first week at a new job in the United States. In one day you meet people, check the schedule, borrow something, write an email and make a short call.', 'office', ['Raj', 'Pia', 'Tessa'],
  'By the end of the class you can survive a first week at work: introduce yourself, ask about times, borrow things, write a short email and close politely.',
  ['Introduce yourself: I just started. I work in…', 'Ask about time: What time does… start?', 'Borrow and request: Can I borrow…? / Could you send…?', 'Write and thank: I’m writing to… Thanks for your help.'],
  ['I introduce myself.', 'I ask about a time or a place.', 'I borrow or request something politely.', 'I write or say a polite closing.'],
  'Which situation in this unit was the most useful for you? Which one do you want to practice again?',
  teach(goal='Abrir a missão integrada: retomar as 7 situações da unidade em um único dia de trabalho.', solo=['Peça que o estudante diga qual situação da unidade foi a mais útil.', 'Mostre os 4 critérios: a missão encadeia todas.'], group=['Cada estudante escolhe uma situação da unidade e diz uma frase.', 'Mostre os critérios: missão final.'], extra=['What was the hardest lesson in this unit?', 'What do you want to say better?'], support=['Aceite respostas curtas ou em português.'])),
 dict(t='rl_warm', stage='warm', title='Connection & warm-up',
  intro=dict(solo='Review the unit with real questions, not a test.', group='One question per student, then a question back to a classmate.'),
  recall='Unit 6: first day in class, schedules, library, small talk, interview, email and phone, meeting a colleague. Ask: Which lesson did you like?',
  qs=[dict(q='How do you introduce yourself in English?', pt='Como você se apresenta em inglês?', sup=['I’m… I work in…', 'I’m new here.', 'Nice to meet you.']), dict(q='What time does your day start?', pt='A que horas seu dia começa?', sup=['At seven a.m.', 'At nine.', 'Early!']), dict(q='What can you borrow from a friend?', pt='O que você pode pegar emprestado de um amigo?', sup=['A pen.', 'A book.', 'A laptop.'])],
  tip='Use the answers to find which chunks from the unit are still weak.', teach=teach(goal='Entrar no idioma e mapear quais chunks da unidade precisam de reforço.', extra=['What is one thing you can do now that you could not before?', 'Which expression do you use most?'], errors=[W('I work on sales.', 'I work in sales.'), W('What time starts the class?', 'What time does the class start?')], support=['Mostre os chips de resposta.'])),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Life in the USA',
  intro='A first week at work in the United States uses everything in this unit. Look at the cards and guess before you read.',
  cards=[dict(vis='obj:nametag', en='Names', pt='Nomes', note='First names are common; “Ms.” and “Mr.” are for formal moments.'), dict(vis='obj:clock', en='Times', pt='Horários', note='People say 10 a.m., not 10:00; always check a.m. or p.m.'), dict(vis='obj:envelope', en='Email', pt='E-mail', note='Hi + name, a clear request and “Best,” are enough at most workplaces.')],
  qs=[dict(q='What helps in a first week at work?', pt='O que ajuda na primeira semana de trabalho?', levels=dict(A1='A smile. Short questions.', A2='Say hello, ask simple questions and say thank you.', B1='Introduce yourself, ask questions without fear and thank people for their help.', B2='Being friendly, asking for clarification early and thanking people build good relationships quickly.')), dict(q='Is it okay to ask for repetition at work?', pt='Pode pedir para repetir no trabalho?', levels=dict(A1='Yes. “Sorry?”', A2='Yes. “Sorry, can you repeat that?”', B1='Yes, it is normal and polite to ask for repetition.', B2='It shows you want to get it right, so people usually appreciate it.')), dict(q='How do you thank a colleague?', pt='Como agradecer um colega?', levels=dict(A1='Thank you!', A2='Thanks for your help.', B1='“Thanks for your help” in speech, “Thanks, Best” in email.', B2='A short, sincere thanks fits better than a long speech.'))],
  compare='In Brazil you may go out for lunch with new colleagues quickly. In the US it can be quicker or slower, depending on the company. How was it for you?',
  teach=teach(goal='Integrar os insights culturais da unidade.', solo=['Mostre os cartões e peça hipóteses.', 'Compare com a experiência do estudante.'], group=['Cada estudante escolhe um cartão e explica.', 'Pergunte “Do you agree?”.'], answers=['Q1: friendly + questions + thanks.', 'Q2: yes, it is polite.', 'Q3: Thanks for your help.'], extra=['Which cultural tip surprised you?', 'What would you tell a friend starting a job in the US?'], support=['Use as respostas A1 como andaime.'], stretch=['B2: discuta como a cultura da empresa pesa mais que “regras do país”.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='office', tod='day', cast=['Raj', 'Pia']),
  pass1=dict(q='What is Raj doing?', pt='O que o Raj está fazendo?', opts=['Asking about his first week at work', 'Looking for a book', 'Calling a restaurant'], ans=0),
  pass2=dict(tasks=[dict(label='Meeting time', ans='ten'), dict(label='Meeting place', ans='room two'), dict(label='Raj needs a…', ans='laptop'), dict(label='Pia will email the…', ans='schedule')]),
  teach=teach(goal='Compreender o essencial antes de ver o texto.', solo=['Esconda o texto. 1ª escuta: o que o Raj faz.', '2ª escuta: hora, sala, o que precisa e o que Pia envia.'], group=['Duplas anotam antes de revelar.', 'Compare as respostas.'], answers=['Pass 1: his first week at work.', 'Pass 2: ten · room two · laptop · schedule'], extra=['Which lessons do you hear in the dialogue?', 'Is Pia helpful? How do you know?'], support=['Use “Slow” na 2ª escuta.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='Where does Raj work?', opts=['In sales', 'In marketing', 'In a library'], ans=0), dict(q='What time is the meeting?', opts=['10 a.m.', '10 p.m.', '2 p.m.'], ans=0), dict(q='What does Raj borrow?', opts=['A laptop', 'A book', 'A card'], ans=0), dict(q='What does Pia send?', opts=['The schedule', 'The invoice', 'A key'], ans=0)],
  retell=dict(prompt='Retell the conversation in your own words, at your level.', starters=['Raj just started…', 'The meeting is at…', 'He borrows…', 'Pia sends…']),
  teach=teach(goal='Ler o diálogo, perceber os chunks da unidade e recontar.', solo=['O estudante lê o Raj; você lê a Pia.', 'Identifique em qual aula cada chunk apareceu.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia.'], answers=['In sales · 10 a.m. · a laptop · the schedule'], extra=['Which chunk is from which lesson?', 'What would you ask Pia?'], errors=[W('What time start the meeting?', 'What time does the meeting start?'), W('Can I borrow to you a laptop?', 'Can I borrow a laptop?')], support=['Mostre o PT depois da 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[C('I just started.', 'Acabei de começar.', 'Introduce yourself at a new job.', pri=True), C('What time does… start?', 'A que horas… começa?', 'Ask a schedule question.', pri=True), C('Can I borrow…?', 'Posso pegar emprestado…?', 'Ask politely to use something.', pri=True), C('Could you send…?', 'Você poderia enviar…?', 'Make a polite written or spoken request.', pri=True, reg='polite'),
         C('I work in…', 'Eu trabalho em…', 'Say your area.'), C('Thanks for your help.', 'Obrigado pela ajuda.', 'Close politely.'), C('Let’s have lunch.', 'Vamos almoçar.', 'A friendly invitation.', reg='informal')],
  discover=dict(fns=['Introducing', 'Schedule', 'Borrowing', 'Requesting', 'Thanking'], items=[dict(en='I just started.', fn='Introducing'), dict(en='What time does the meeting start?', fn='Schedule'), dict(en='Can I borrow a laptop?', fn='Borrowing'), dict(en='Could you send me the schedule?', fn='Requesting'), dict(en='Thanks for your help.', fn='Thanking')]),
  note='These four ★ come from the unit. They are the base of your first week at work.', teach=teach(goal='Revisitar 4 chunks da unidade e a função de cada um.', solo=['Pergunte em qual aula cada chunk apareceu.', 'Peça um exemplo próprio.'], group=['Cada estudante escolhe uma ★ e explica.', 'Compare em duplas.'], answers=['Introducing · Schedule · Borrowing · Requesting · Thanking'], extra=['Which one is most useful for you?'], errors=[W('I started just.', 'I just started.'), W('Could you to send?', 'Could you send?')], support=['Só as 4 ★.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Asking about a time', formula='**What time does** + thing + start?', ex=['What time does the meeting start?', 'What time does lunch start?', 'What time does work end?'], main=True), dict(name='Asking permission and requesting', formula='**Can I borrow** + thing? · **Could you send** + thing?', ex=['Can I borrow a laptop?', 'Could you send me the schedule?', 'Could you send the file by Friday?'], main=True),
            dict(name='Introducing yourself', formula='**I just started** · **I work in** + area', ex=['I just started this week.', 'I work in sales.']), dict(name='Thanking', formula='**Thanks for** + noun', ex=['Thanks for your help.', 'Thanks for your email.'])],
  swap=dict(frame='What time does {event} start? Can I borrow {thing}?', tpt='A que horas {event} começa? Posso pegar {thing} emprestado?',
   slots=[dict(k='event', label='Event', opts=O(('the meeting', 'a reunião'), ('the class', 'a aula'), ('lunch', 'o almoço'))), dict(k='thing', label='Thing', opts=O(('a laptop', 'um notebook'), ('your pen', 'a sua caneta'), ('the key', 'a chave')))]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['What time does it start?', 'At what time will the meeting begin?'], ['Can I borrow it?', 'May I borrow it?'], ['Could you send it?', 'Could you please send it by Friday?'], ['Thanks!', 'Thank you for your help.']], note='These are differences of context and register, not absolute rules.'),
  teach=teach(goal='Revisar os padrões-chave da unidade em combinação.', solo=['Mostre o padrão no diálogo.', 'Use “Swap the words”.'], group=['Troca em cadeia.', 'Em pares.'], answers='Padrões 01/02 são o foco; 03/04 são expansão.', extra=['Combine two patterns in one turn.', 'Make a request more polite.'], errors=[W('What time starts the meeting?', 'What time does the meeting start?'), W('Can I borrow to you the pen?', 'Can I borrow your pen?'), W('Thanks by your help.', 'Thanks for your help.')], support=['Só um padrão por vez.'], stretch=['Combine: What time does it start? Could you send me the schedule?'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Reductions in requests', tip='In fast speech, “Could you” sounds like “couldja” and “Can I” like “ca-nI”. Understand them and use them when you feel ready.',
  items=[dict(say='Could you send it?', linked='Could·ja SEND it?', ipa='/ˈkʊdʒə/', rhythm='ooOo'), dict(say='Can I borrow a laptop?', linked='Ca·nI BOR·row a LAP·top?', ipa='/kənaɪ/', rhythm='ooOooOo'), dict(say='What time does it start?', linked='What TIME does it START?', ipa='/ˈwʌt taɪm/', rhythm='oOooO')],
  identify=[dict(q='Which one do you hear?', opts=['Could you send it?', 'Can you send it?', 'Should you send it?'], ans=0, say='Could you send it?'), dict(q='Which one do you hear?', opts=['Can I borrow a laptop?', 'Can she borrow a laptop?', 'Can we borrow a laptop?'], ans=0, say='Can I borrow a laptop?')],
  own=dict(prompt='Write one request you will really make this week at work or school.', criteria='Say it twice: slowly, then linked. Does it sound natural?'),
  teach=teach(goal='UM só fenômeno: reduções e ligações nos pedidos (could you, can I).', solo=['Modele devagar e rápido.', 'Identify e depois uso próprio.'], group=['Coro, depois duplas.', 'Cada um cria um pedido.'], answers=['Identify 1: Could you send it? · Identify 2: Can I borrow a laptop?'], errors=[W('Could — you, com pausa', 'Could-ja, ligado'), W('l pronunciado em could', '“l” mudo em could')], support=['Foque em reconhecer antes de produzir.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    MC('1. It is your first week. How do you introduce yourself?', ['I just started. I work in sales.', 'I am start sales.', 'I work on start.'], 0, 'Short and natural.'),
    MC('2. You want the time of the meeting.', ['What time does the meeting start?', 'What hour starts meeting?', 'Meeting what time?'], 0, 'What time does + noun + start?'),
    MC('3. You need a laptop for an hour.', ['Can I borrow a laptop?', 'I borrow laptop now.', 'You give laptop me?'], 0, 'Can I borrow + noun?'),
    MC('4. You need a file from a client.', ['Could you send the file, please?', 'Send me file.', 'Could you to send?'], 0, 'Could you + base verb.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    GAP('What time ___ the meeting start?', 'does', 'What time does…?', bank=['does', 'is', 'do']),
    GAP('I’m writing ___ ask about the schedule.', 'to', 'I’m writing to + verb.', bank=['to', 'for', 'at']),
    SW('Make it polite with “Could you”:', 'Send the schedule.', ['Could you send the schedule?', 'Could you send the schedule, please?'], 'Could you send the schedule, please?', 'Could you… is softer than an order.'),
    SW('Ask to borrow:', 'a laptop', ['Can I borrow a laptop?', 'Can I borrow a laptop'], 'Can I borrow a laptop?', 'Can I borrow + noun?'),
    RP('Nice to meet you!', 'Choose the best reply.', ['Nice to meet you, too! I just started.', 'It is ten a.m.', 'Here is the laptop.'], 0, 'Return the greeting.'),
    RP('Thanks for your help.', 'Choose the best reply.', ['Anytime!', 'I am a help.', 'This is Raj.'], 0, 'A natural answer to thanks.')])],
  teach=teach(goal='Do controlado ao guiado antes da missão final.', solo=['Peça que justifique cada resposta.', 'Se acertar rápido, peça outra versão.'], group=['Resolvam em duplas e comparem.', 'Equipes: ponto por resposta justificada.'], answers=['1: I just started. I work in sales. · 2: What time does the meeting start? · 3: Can I borrow a laptop? · 4: Could you send the file, please?', 'Gap: does · to · Could you send the schedule, please? · Can I borrow a laptop? · Nice to meet you, too! I just started. · Anytime!'], extra=['Say each answer aloud at a natural speed.'], errors=[W('What time starts?', 'What time does it start?'), W('Could you to send?', 'Could you send?')], support=['Ofereça o banco de palavras.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — your first week',
  brief=dict(teacher='You play several people in one day: a colleague, the front desk and a client on the phone. Change the plan during the scene.', student='You are the new employee: introduce yourself, ask about a time, borrow something, make a request and close politely.'),
  orders=['Introduce yourself to a colleague', 'Ask what time the meeting starts', 'Borrow a laptop at the front desk', 'Ask a client by email or phone to send a file'],
  complications=['The meeting time changes.', 'The laptop is not available.', 'The client is not there: leave a message.', 'You do not understand: ask for repetition.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['I just started.', 'What time does… start?', 'Can I borrow…?', 'Could you send…?']), dict(label='Keywords', desc='Only the keywords', help=['started', 'meeting', 'borrow', 'send', 'thanks'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I introduce myself.', 'I ask about a time.', 'I borrow or request politely.', 'I close politely.'],
  teach=teach(goal='Simulação integrada com várias situações e três rodadas com menos apoio.', solo=['Encadeie as cenas sem pausar: colega, horário, empréstimo, pedido.', 'Rodada 1: chunks. Rodada 2: palavras-chave. Rodada 3: sem roteiro.', 'Anote 2–3 correções.'], extra=['What if two things go wrong at the same time?'], errors=[W('I am started.', 'I just started.')], support=['Volte à rodada 1 se travar.'], stretch=['Adicione uma conversa leve de intervalo de café.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Introduce and spell', min=3, task='Introduce yourself and spell your name.', hint='I just started. / How do you spell…?'), dict(title='Schedule and borrow', min=3, task='Ask a time and borrow something.', hint='What time does… start? / Can I borrow…?'), dict(title='Request and thank', min=3, task='Make a polite request and thank your partner.', hint='Could you send…? / Thanks for your help.'), dict(title='First-week tips', min=2, whole=True, task='Whole group: give one tip for a first week at work.', hint='Remember to…')],
  infogap=dict(title='Week plan', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='Student A', task='You know Monday and Wednesday. Ask about the rest.', rows=[dict(k='Monday', v='team meeting, 10 a.m.'), dict(k='Tuesday', v=''), dict(k='Wednesday', v='lunch with Pia, noon'), dict(k='Thursday', v='')]),
   b=dict(title='Student B', task='You know Tuesday and Thursday. Ask about the rest.', rows=[dict(k='Monday', v=''), dict(k='Tuesday', v='training, 2 p.m.'), dict(k='Wednesday', v=''), dict(k='Thursday', v='client call, 9:30 a.m.')])),
  teach=teach(goal='Fluência por repetição com informações novas.', group=['Troque os pares a cada rodada.', 'Sem salas simultâneas: interações sequenciais.', 'Cada aluno faz ≥1 pergunta e ≥1 resposta.'], answers=['A: Mon team meeting 10 a.m.; Wed lunch noon. B: Tue training 2 p.m.; Thu client call 9:30 a.m.'], extra=['What time is the client call?', 'Is training on Tuesday?'], errors=[W('What is Tuesday?', 'What’s on Tuesday?'), W('At 2 of the afternoon.', 'At 2 p.m.')], support=['Dê frases-modelo no chat.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — your first week at a new job',
  goal='Each group lives one chain of situations from the unit and solves every small problem in English.',
  missions=[dict(who='A', role='New employee + colleagues', mission='Meet a colleague, ask about the schedule and borrow a laptop for the meeting.', constraint='Use “I just started.” and “What time does…?”', start='Hi! I just started…'), dict(who='B', role='Employee + client + manager', mission='Write a short email to a client and call to follow up. Then thank your manager.', constraint='Use “I’m writing to…”, “Could you send…?” and “Thanks for your help.”', start='Dear Ms. Lee, I’m writing…'), dict(who='C', role='Candidate + interviewer', mission='Interview for a new job, then meet the team and exchange cards.', constraint='Use “I’m good at…” and “Here’s my card.”', start='Tell me about…')], min=11,
  success=['Introduce yourself.', 'Ask about a time or place.', 'Borrow or request something.', 'Close politely.'],
  teach=teach(goal='Realizar a missão integrada: encadear as situações da unidade com problemas pequenos.', group=['Cada grupo recebe papel, restrição e missão encadeada.', 'Progressão: com apoio → palavras-chave → sem roteiro.', 'Anote 2–3 correções prioritárias para a devolutiva.'], answers=['Modelo: “I just started.” → “What time does the meeting start?” → “Can I borrow a laptop?” → “Thanks for your help.”'], extra=['What if the meeting time changes?'], support=['Dê o início de frase em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short email to your manager at the end of your first week. Thank the team and ask for next week’s schedule.',
  steps=['Greeting', 'Thanks', 'Request', 'Closing'],
  model='Hi Pia, **thanks for your help** this week. I’m writing to ask about next week. **Could you send** me the schedule? I’d like to know the time of the team meeting. Best, Raj',
  checklist=['I greeted my manager.', 'I said thank you.', 'I made one polite request.', 'I closed with “Best,” and my name.'],
  tip='Fix only 2–3 priority points. Show a more natural way to say the same idea.', fix=dict(n=3),
  teach=teach(goal='Produção escrita curta que integra a unidade.', solo=['Peça o e-mail; corrija 2–3 pontos.'], group=['Troquem os textos e corrijam em duplas.'], extra=['Add one thing you learned this week.'], errors=[W('Thanks you for your help.', 'Thank you for your help.'), W('I want the schedule.', 'Could you send me the schedule?')], support=['Dê o modelo e peça só para trocar os dados.'])),
 FEEDBACK('Example: You chained introduction, question and request smoothly.', 'Example: Link “Could you” and “Can I” in fast speech.', 'Example: Handle a whole work day in English without notes.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❓', name='Build a question', prompt='Without notes: ask what time the meeting starts.', model='What time does the meeting start?'), dict(ic='💬', name='Respond to a situation', prompt='A new colleague says: “Nice to meet you!” You just started.', model='Nice to meet you, too! I just started.'), dict(ic='⭐', name='Use a new expression', prompt='Ask a colleague to send you a file.', model='Could you send me the file?')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 60-second audio telling your first week at a new job (real or imagined).', 'Write an email asking for a schedule.', 'Review the 7 situations of the unit and choose your 5 favorite expressions.', 'Listen to the dialogue again and underline four expressions.']),
  spaced=dict(next=['I just started.', 'What time does… start?', 'Can I borrow…?'], week=['Could you send…?', 'I’m good at…', 'Thanks for your help.'], unit=['Introduce · schedule · borrow · write']),
  teach=teach(goal='Toda aula termina com uma produção observável e fecha a unidade.', solo=['Sem anotações: pergunta, resposta e expressão nova.', 'Peça que o estudante escolha o próximo desafio.'], group=['Exit challenge individual; combine a tarefa.'], answers=['What time does the meeting start? · Nice to meet you, too! I just started. · Could you send me the file?'], extra=['Revisão espaçada: retomar a unidade na próxima aula e depois de uma semana.'])),
 LEVELS([('Hello. I work. Meeting, what time?', 'Get through the day with words and gestures.'), ('I just started. What time does the meeting start? Can I borrow a laptop?', 'Handle the basic work situations.'), ('I just started last week, so could you send me the schedule when you have a minute?', 'Make requests and give reasons.'), ('Since I’m still getting to know the team, I’d really appreciate it if you could walk me through next week.', 'Ask for support with nuance.'), ('I’d be grateful for any pointers as I settle in; so far the team has been very welcoming.', 'Show appreciation and openness.'), ('I’m conscious that I’m still finding my feet, so I would welcome any guidance you might offer.', 'Use a refined, tactful professional register.')], you='A1')]

LESSON = LESSON_OF(48, 'Real-Life Mission Day 6', 'Real-Life Mission Day 6', 'Missão da unidade 6', 8, ['Raj', 'Pia', 'Tessa'], 'office', DIALOG, PAGES)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
