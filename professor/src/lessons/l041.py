#!/usr/bin/env python3
"""Aula 41 · First day in class (A1, 60 min). Gera data/v3/041.json."""
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

DIALOG = dict(speakers={'New student': {'name': 'Mina'}, 'Classmate': {'name': 'Ryo'}}, lines=[
 dict(who='New student', en='Hi! **Is this seat taken?**', pt='Oi! Este lugar está ocupado?'),
 dict(who='Classmate', en='No, please sit! I’m Ryo.', pt='Não, pode sentar! Eu sou o Ryo.'),
 dict(who='New student', en='Thanks, Ryo. **I’m new here.** **Please call me** Mina.', pt='Obrigada, Ryo. Eu sou nova aqui. Pode me chamar de Mina.'),
 dict(who='Classmate', en='Welcome, Mina! **How do you spell** your name?', pt='Bem-vinda, Mina! Como se escreve o seu nome?'),
 dict(who='New student', en='M-I-N-A. And **how do you spell** your name?', pt='M-I-N-A. E como se escreve o seu nome?'),
 dict(who='Classmate', en='R-Y-O. It’s short! Listen: the teacher says, “Open to page twelve.”', pt='R-Y-O. É curto! Escute: a professora disse “Abram na página doze”.'),
 dict(who='New student', en='**Sorry, can you repeat that?** I didn’t catch it.', pt='Desculpe, você pode repetir? Eu não entendi.'),
 dict(who='Classmate', en='Page twelve. Here, use my book.', pt='Página doze. Aqui, use o meu livro.'),
 dict(who='New student', en='Thank you, Ryo! **Let’s work together.**', pt='Obrigada, Ryo! Vamos trabalhar juntos.'),
 dict(who='Classmate', en='Sure! Ask me anything.', pt='Claro! Pergunte o que quiser.')])

PAGES = [
 OPEN(1, 'First day in class', 'Primeiro dia de aula', 'It is your first day in an English class in the United States. You find a seat, say your name, spell it and ask a classmate to repeat an instruction.', 'classroom', ['Mina', 'Ryo'],
  'By the end of the class you can sit down, say you are new, give and ask for a spelling, and ask someone to repeat something — politely and clearly.',
  ['Ask if a seat is free: Is this seat taken?', 'Say who you are: I’m new here. Please call me…', 'Spell a name: How do you spell…?', 'Ask for repetition: Sorry, can you repeat that?'],
  ['I start the conversation.', 'I give my name and spell it.', 'I ask for repetition when I do not understand.', 'I close the talk in a friendly way.'],
  'On a first day, what do you say to the person next to you in Portuguese? Is it short or long?',
  teach(goal='Abrir pela situação real: o primeiro dia, o nervosismo e o que se pode fazer com poucas palavras.',
   solo=['Leia o objetivo e pergunte como foi (ou será) um primeiro dia de aula para o estudante.', 'Peça que diga, em qualquer língua, o que sente. Depois mostre os 4 critérios.'],
   group=['Cada estudante diz uma palavra que associa a “first day”.', 'Mostre os 4 critérios: eles serão a missão final.'], extra=['Do you remember your first day at school?', 'Who sat next to you?'], support=['Aceite português na primeira rodada e reformule em inglês.'])),
 dict(t='rl_warm', stage='warm', title='Connection & warm-up',
  intro=dict(solo='Start with real questions about the student’s own life.', group='One question per student, then a question back to a classmate.'),
  recall='Meeting new people (Unit 1): “Nice to meet you. I’m from…”. Ask: Where are you from?',
  qs=[dict(q='Where are you from?', pt='De onde você é?', sup=['I’m from…', 'I’m from Brazil.', 'I live in…']), dict(q='What do you do in the morning?', pt='O que você faz de manhã?', sup=['I work.', 'I study English.', 'I make coffee.']), dict(q='Are you nervous when you meet new people?', pt='Você fica nervoso ao conhecer pessoas novas?', sup=['A little.', 'Not really.', 'Sometimes.'])],
  tip='Use the answers to find gaps. Keep the questions simple and let the student finish the sentence.',
  teach=teach(goal='Entrar no idioma e retomar apresentações simples.', extra=['What is your full name?', 'Is your name easy to say in English?'], errors=[W('I am agree.', 'I agree.'), W('I have 30 years.', 'I’m 30.')], support=['Ofereça as respostas de apoio (chips) e peça que escolham uma.'])),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Life in the USA',
  intro='In many US classrooms people are friendly and informal. Look at the cards and guess before you read.',
  cards=[dict(vis='obj:book', en='First names', pt='Nomes próprios', note='In many language classes teachers and students use first names.'), dict(vis='obj:door', en='Sit anywhere', pt='Sentar onde quiser', note='Seats are often free: you ask “Is this seat taken?”'), dict(vis='obj:phone', en='“Say that again?”', pt='Pedir para repetir', note='Asking someone to repeat is normal and polite.')],
  qs=[dict(q='What do you call your teacher?', pt='Como você chama o professor?', levels=dict(A1='By first name. Or “teacher”.', A2='Many teachers say: “Call me Anna.”', B1='In language classes it is common to use first names, but some teachers prefer Mr. or Ms.', B2='It depends on the school: some teachers want a title, so you can ask “What should I call you?”.')),
      dict(q='What do you do if you do not understand?', pt='O que fazer se você não entende?', levels=dict(A1='I say: “Sorry?”', A2='I say: “Can you repeat that, please?”', B1='I ask the person to repeat or to say it more slowly.', B2='I ask for repetition and then check: “So it is page twelve, right?”')),
      dict(q='How do you give your name clearly?', pt='Como dizer seu nome com clareza?', levels=dict(A1='I say the letters.', A2='I spell it: M-I-N-A.', B1='I spell it and say a word for each letter if needed.', B2='I spell it letter by letter, slowly, and let the other person write it down.'))],
  compare='In Brazil students often say “professor/professora” and use titles. In many US classes people use first names. What do you call teachers where you live?',
  teach=teach(goal='Ativar o contexto cultural da sala de aula e as primeiras hipóteses.', solo=['Mostre os 3 cartões e peça hipóteses antes de explicar.', 'Compare com a sala de aula que o estudante conhece.'], group=['Cada estudante escolhe um cartão e explica em uma frase.', 'Pergunte “Do you agree?”.'],
   answers=['Q1: first names (but it depends).', 'Q2: Can you repeat that, please?', 'Q3: spell the name letter by letter.'], extra=['What is the best way to ask a teacher for help?', 'Is it rude to ask someone to repeat?'], support=['Use as respostas A1 como andaime e peça que repitam.'], stretch=['B2: discuta quando usar título (Professor) e quando usar o primeiro nome.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='classroom', tod='day', cast=['Mina', 'Ryo']),
  pass1=dict(q='Where are the two people?', pt='Onde as duas pessoas estão?', opts=['In a classroom', 'At a restaurant', 'At the airport'], ans=0),
  pass2=dict(tasks=[dict(label='Mina’s name (spelling)', ans='M-I-N-A'), dict(label='Ryo’s name (spelling)', ans='R-Y-O'), dict(label='Page number', ans='twelve'), dict(label='What Ryo shares', ans='book')]),
  teach=teach(goal='Compreender a situação antes de ver o texto: ideia principal e depois 3–4 informações.', solo=['Esconda o texto. 1ª escuta: só onde estão.', '2ª escuta: as letras dos nomes, a página e o que o Ryo oferece.', 'Mostre o texto só depois.'], group=['Escuta coletiva; duplas anotam antes de revelar.', 'Compare entre as duplas.'],
   answers=['Pass 1: in a classroom.', 'Pass 2: M-I-N-A · R-Y-O · twelve · book.'], extra=['How does Mina feel? How do you know?', 'Why does she ask Ryo to repeat?'], support=['Use o botão “Slow” na 2ª escuta e pause depois de cada fala.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='What does Mina ask first?', opts=['Is this seat taken?', 'What time is it?', 'Where is the door?'], ans=0), dict(q='What does Mina say about herself?', opts=['She is new here.', 'She is the teacher.', 'She is late.'], ans=0), dict(q='What does Mina not understand?', opts=['The teacher’s instruction', 'Ryo’s name', 'The price'], ans=0), dict(q='What does Ryo do at the end?', opts=['He shares his book.', 'He leaves.', 'He calls the teacher.'], ans=0)],
  retell=dict(prompt='Retell the conversation in your own words, at your level.', starters=['Mina sits next to…', 'She says she is…', 'They spell…', 'Ryo helps her with…']),
  teach=teach(goal='Ler o diálogo, perceber os chunks e recontar.', solo=['O estudante lê o papel da Mina; você lê o do Ryo.', 'Peça que reconte.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia.'],
   answers=['Is this seat taken? · she is new · the teacher’s instruction · he shares his book'], extra=['What would you say to Ryo?', 'Is Ryo friendly? Why?'], errors=[W('I am new in here.', 'I’m new here.'), W('How you spell your name?', 'How do you spell your name?')], support=['Mostre a tradução (botão PT) depois da 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[C('Is this seat taken?', 'Este lugar está ocupado?', 'Ask before you sit next to someone.', pri=True, alt='Also: **Is anyone sitting here?**'), C('I’m new here.', 'Eu sou novo aqui.', 'Say it on your first day. People are usually kind.', pri=True, alt='Also: **It’s my first day.**'),
         C('How do you spell…?', 'Como se escreve…?', 'Ask for a spelling of a name or word.', pri=True, alt='Also: **Can you spell that, please?**'), C('Sorry, can you repeat that?', 'Desculpe, pode repetir?', 'Use it when you do not understand.', pri=True, alt='Shorter: **Sorry?** / **Say that again?**', reg='polite'),
         C('Please call me…', 'Pode me chamar de…', 'Say the name you prefer.', alt='Also: **You can call me…**'), C('I didn’t catch that.', 'Eu não entendi (o que você disse).', 'Say you missed the words, not the idea.', reg='informal'), C('Let’s work together.', 'Vamos trabalhar juntos.', 'Invite a classmate to do an activity.')],
  discover=dict(fns=['Asking permission', 'Introducing yourself', 'Spelling', 'Asking for help', 'Inviting'], items=[dict(en='Is this seat taken?', fn='Asking permission'), dict(en='Please call me Mina.', fn='Introducing yourself'), dict(en='How do you spell your name?', fn='Spelling'), dict(en='Sorry, can you repeat that?', fn='Asking for help'), dict(en='Let’s work together.', fn='Inviting')]),
  note='Choose 3–5 expressions (★) to use again and again. The others are for understanding.',
  teach=teach(goal='Escolher 3–5 chunks para uso repetido e descobrir a função de cada um.', solo=['Pergunte “When do you say it?” antes de dar o significado.', 'Peça um exemplo próprio para cada ★.'], group=['Cada estudante escolhe a expressão que mais usaria e explica quando.', 'Compare em duplas.'],
   answers=['Asking permission · Introducing yourself · Spelling · Asking for help · Inviting'], extra=['Which one is useful outside class?', 'Which one do you say to a stranger?'], errors=[W('You can repeat?', 'Can you repeat that?'), W('How is writing your name?', 'How do you spell your name?')], support=['Trabalhe só as 3–4 expressões ★ nesta aula.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Saying who you are', formula='**I’m** + new / a student / from + place', ex=['I’m new here.', 'I’m a student.', 'I’m from Brazil.'], main=True), dict(name='Asking for a spelling', formula='**How do you spell** + your name / that?', ex=['How do you spell your name?', 'How do you spell “library”?', 'How do you spell that?'], main=True),
            dict(name='Asking for repetition', formula='**Can you** + repeat / spell / say + that?', ex=['Can you repeat that?', 'Can you say that again?']), dict(name='Choosing a name', formula='**Please call me** + name', ex=['Please call me Mina.', 'Please call me Dan.'])],
  swap=dict(frame='Hi! I’m {who}. How do you {verb} {thing}?', tpt='Oi! Eu sou {who}. Como você {verb} {thing}?',
   slots=[dict(k='who', label='Who', opts=O(('new here', 'novo aqui'), ('a new student', 'um aluno novo'), ('from Brazil', 'do Brasil'))), dict(k='verb', label='Verb', opts=O(('spell', 'escreve'), ('say', 'diz'), ('write', 'escreve (à mão)'))), dict(k='thing', label='Thing', opts=O(('your name', 'o seu nome'), ('this word', 'esta palavra'), ('“Monday”', '“Monday”')))]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['Is this seat taken?', 'Is this seat available?'], ['I’m new here.', 'I have recently joined this class.'], ['Say that again?', 'Could you please repeat that?'], ['It’s M-I-N-A.', 'My name is spelled M-I-N-A.']], note='These are differences of context and register, not absolute rules.'),
  teach=teach(goal='Fixar 2 padrões principais (I’m… e How do you spell…?); os outros são expansão.', solo=['Mostre o padrão DENTRO do diálogo.', 'Use “Swap the words”: o estudante diz a frase completa a cada troca.'], group=['Troca em cadeia: cada estudante muda UMA peça.', 'Em pares: um escolhe as peças, o outro fala.'],
   answers='Padrões 01/02 são o foco; 03/04 são expansão.', extra=['Make it polite: Say that again → Can you say that again?', 'Change one word and say the sentence.'], errors=[W('I am new in the class.', 'I’m new in the class / I’m new here.'), W('How do you spells it?', 'How do you spell it?'), W('Repeat, please.', 'Can you repeat that, please?')], support=['Fique só com I’m new here e How do you spell…? na primeira rodada.'], stretch=['Combinar: I’m new here. Can you spell your name, please?'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='The English alphabet', tip='Names are often spelled aloud. Learn the vowel letters first: A /eɪ/, E /i/, I /aɪ/, O /oʊ/, U /ju/. They are different from Portuguese.',
  items=[dict(say='M-I-N-A', linked='em · eye · en · ay', ipa='/ɛm aɪ ɛn eɪ/', rhythm='OOOO'), dict(say='R-Y-O', linked='ar · why · oh', ipa='/ɑr waɪ oʊ/', rhythm='OOO'), dict(say='E-M-M-A', linked='ee · em · em · ay', ipa='/i ɛm ɛm eɪ/', rhythm='OOOO')],
  identify=[dict(q='Which one do you hear?', opts=['I-A-N', 'E-N-A', 'A-N-E'], ans=0, say='I-A-N'), dict(q='Which one do you hear?', opts=['A-L-E-X', 'E-L-E-X', 'A-L-A-X'], ans=0, say='A-L-E-X')],
  own=dict(prompt='Spell your own first name and one other name you know (a friend or a city).', criteria='Say the letters slowly, with a small pause between them. Did your partner write the right name?'),
  teach=teach(goal='UM só fenômeno: o alfabeto inglês falado (especialmente A, E, I, O, U, G, J, R).', solo=['3 passagens: escutar e identificar → repetir o alfabeto → soletrar nomes próprios.', 'Mostre A (ei), E (i), I (ai), G (dji), J (djei) e peça que repita.'], group=['Coro, depois duplas: um soletra, o outro escreve.', 'Troque de parceiro.'],
   answers=['Identify 1: I-A-N · Identify 2: A-L-E-X'], errors=[W('E = “é”, I = “i”', 'E = /i/ (“i”), I = /aɪ/ (“ai”)'), W('G = “gê”, J = “jota”', 'G = “dji”, J = “djei”'), W('R = “érre”', 'R = “ar”')], support=['Ensine só as cinco vogais e pratique com o nome do estudante.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    MC('1. You want to sit next to someone. What do you ask?', ['Is this seat taken?', 'Who is your seat?', 'Seat is mine?'], 0, 'Is this seat taken? is the natural question.'),
    MC('2. It is your first day. What do you say?', ['I’m new here.', 'I am agree.', 'I new here am.'], 0, 'I’m new here is short and natural.'),
    MC('3. You want to write a name correctly.', ['How do you spell your name?', 'How you write name?', 'What is spell?'], 0, 'How do you spell…? asks for the letters.'),
    MC('4. You did not understand the teacher.', ['Sorry, can you repeat that?', 'No. Stop.', 'I am understand.'], 0, 'A polite request for repetition.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    GAP('Hi! ___ this seat taken?', 'Is', 'Is this seat taken?', bank=['Is', 'Do', 'Are']),
    GAP('How do you ___ your name?', 'spell', 'How do you spell…?', bank=['spell', 'say it', 'repeat']),
    SW('Make it polite with “Can you”:', 'Repeat that.', ['Can you repeat that?', 'Can you repeat that, please?', 'Could you repeat that?'], 'Can you repeat that, please?', 'Can you… is softer than an order.'),
    SW('Ask about the spelling:', 'your name', ['How do you spell your name?', 'How do you spell your name'], 'How do you spell your name?', 'How do you spell + object?'),
    RP('Page twelve, please.', 'You did not hear. Choose the best reply.', ['Sorry, can you repeat that?', 'I am twelve.', 'The seat is free.'], 0, 'Ask for repetition politely.'),
    RP('Welcome! What’s your name?', 'Choose the best reply.', ['I’m Mina. M-I-N-A.', 'Yes, please.', 'It is page twelve.'], 0, 'Give your name and spell it.')])],
  teach=teach(goal='Do controlado ao guiado: completar, substituir e transformar antes da fala livre.', solo=['Peça que o estudante justifique cada resposta.', 'Se acertar rápido, peça a versão mais informal.'], group=['Resolvam em duplas e comparem.', 'Equipes: ponto por resposta justificada.'],
   answers=['1: Is this seat taken? · 2: I’m new here. · 3: How do you spell your name? · 4: Sorry, can you repeat that?', 'Gap: Is · spell · Can you repeat that, please? · How do you spell your name? · Sorry, can you repeat that? · I’m Mina. M-I-N-A.'], extra=['Say each answer aloud with a friendly tone.'],
   errors=[W('Can you repeat?', 'Can you repeat that?'), W('How do you spell it your name?', 'How do you spell your name?')], support=['Ofereça o banco de palavras (chips) nas lacunas.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — your first day',
  brief=dict(teacher='You are a friendly classmate. Speak a bit fast once and use a long name to create a problem.', student='You are the new student: sit down, introduce yourself, spell your name and ask for repetition.'),
  orders=['Ask if the seat next to you is free', 'Say you are new and spell your name', 'Ask your classmate to spell his or her name', 'Ask to repeat the homework'],
  complications=['The classmate speaks too fast.', 'The classmate’s name is difficult: ask for the spelling.', 'You do not hear the page number.', 'Someone says your name wrong: correct it kindly.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['Is this seat taken?', 'I’m new here.', 'How do you spell…?', 'Sorry, can you repeat that?']), dict(label='Keywords', desc='Only the keywords', help=['seat', 'new', 'spell', 'repeat', 'together'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I start the conversation.', 'I give my name and spell it.', 'I ask for repetition.', 'I close the talk in a friendly way.'],
  teach=teach(goal='Simulação com complicação inesperada e três rodadas com menos apoio.', solo=['Use o nome real do estudante ou um nome difícil para a soletração.', 'Rodada 1: com chunks. Rodada 2: palavras-chave. Rodada 3: sem roteiro.', 'Meta: 60–70% da fala é do estudante. Anote 2–3 correções.'],
   extra=['What if you do not hear the answer twice?'], errors=[W('I not understand.', 'I don’t understand. / Sorry, can you repeat that?')], support=['Volte à rodada 1 se travar; peça só a primeira frase.'], stretch=['Introduza-se a dois colegas e peça ajuda com o livro.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Seats and names', min=3, task='Ask if the seat is free. Say your name.', hint='Is this seat taken? / Please call me…'), dict(title='Spell it', min=3, task='Ask your partner to spell the name. Write it.', hint='How do you spell…?'), dict(title='Say it again', min=3, task='Give an instruction fast. Your partner asks for repetition.', hint='Sorry, can you repeat that?'), dict(title='Class list', min=2, whole=True, task='Whole group: each one spells a classmate’s name.', hint='His name is… M-A-X.')],
  infogap=dict(title='Class list', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='Student A', task='You know two names. Ask about the rest.', rows=[dict(k='Student 1', v='Mina Park'), dict(k='Student 2', v=''), dict(k='Student 3', v='Alma Reyes'), dict(k='Student 4', v='')]),
   b=dict(title='Student B', task='You know two names. Ask about the rest.', rows=[dict(k='Student 1', v=''), dict(k='Student 2', v='Ryo Sato'), dict(k='Student 3', v=''), dict(k='Student 4', v='Zara Khan')])),
  teach=teach(goal='Fluência por repetição da função com informações novas a cada rodada.', group=['Troque os pares a cada rodada.', 'Sem salas simultâneas: interações sequenciais.', 'Cada aluno faz ≥1 pergunta e ≥1 resposta.'],
   answers=['Info gap: A tem Mina Park e Alma Reyes; B tem Ryo Sato e Zara Khan. Cada um pergunta e soletra.'], extra=['How do you spell Reyes?', 'Can you spell the last name?'], errors=[W('How is your last name?', 'What’s your last name?'), W('Spell me, please.', 'Can you spell that, please?')], support=['Entregue frases-modelo no chat da turma.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — your first day',
  goal='Each group must get something done in English: start a conversation, spell, ask for repetition and close it.',
  missions=[dict(who='A', role='New students', mission='Find a seat. Introduce yourselves and spell both names.', constraint='Use “Is this seat taken?” and “How do you spell…?”', start='Hi! Is this seat…'), dict(who='B', role='New student + classmate', mission='The classmate gives a fast instruction. The new student asks for repetition twice.', constraint='Use “Sorry, can you repeat that?” two times.', start='Excuse me, what…'), dict(who='C', role='Two classmates', mission='Teach a new student the names of three people in the class.', constraint='Spell at least one name and use “Let’s work together.”', start='Welcome! I’m…')], min=11,
  success=['Start the conversation.', 'Say and spell your name.', 'Ask for repetition.', 'Close the conversation in a friendly way.'],
  teach=teach(goal='Realizar algo com o inglês: o objetivo é resolver, não só falar certo.', group=['Cada grupo recebe papel, restrição e missão. Alterne os papéis.', 'Progressão: 1ª rodada com apoio, 2ª palavras-chave, 3ª sem roteiro.', 'Anote 2–3 correções prioritárias.'],
   answers=['Modelo: “Hi! Is this seat taken?” → “No, sit down! I’m Ryo.” → “I’m new here. How do you spell your name?”'], extra=['What if you do not understand the second time?'], support=['Dê o início de frase (“Start with”) em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short note to introduce yourself to your new class. Say your name, how to spell it and what you want to learn.',
  steps=['Greeting', 'Name and spelling', 'What you want', 'Closing'],
  model='Hi everyone! **I’m new here.** **Please call me** Mina. My name is spelled M-I-N-A. I want to practice speaking English. See you in class!',
  checklist=['I greeted the class.', 'I said my name and the spelling.', 'I said one thing I want to learn.', 'I closed in a friendly way.'],
  tip='Fix only 2–3 priority points. Show a more natural way to say the same idea.', fix=dict(n=3),
  teach=teach(goal='Produção escrita curta ligada à situação comunicativa.', solo=['Peça a nota; corrija 2–3 pontos e mostre uma forma mais natural.'], group=['Cada estudante escreve; troquem os textos e corrijam em duplas.'], extra=['Add one thing about your job or city.'], errors=[W('My name is write M-I-N-A.', 'My name is spelled M-I-N-A.'), W('I want learn English.', 'I want to learn English.')], support=['Dê o modelo e peça só para trocar os dados.'])),
 FEEDBACK('Example: You asked if the seat was free and spelled your name clearly.', 'Example: Say the letters E and I carefully when you spell.', 'Example: Introduce yourself to two people and ask each one for the spelling.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❓', name='Build a question', prompt='Without notes: ask how to spell a classmate’s name.', model='How do you spell your name?'), dict(ic='💬', name='Respond to a situation', prompt='The teacher says something fast. You did not hear it.', model='Sorry, can you repeat that?'), dict(ic='⭐', name='Use a new expression', prompt='It is your first day. Tell the person next to you.', model='I’m new here.')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 30-second audio: say your name and spell it.', 'Write three names of people you know and spell them aloud.', 'Review the alphabet and the vowels A, E, I, O, U.', 'Listen to the dialogue again and underline two expressions.']),
  spaced=dict(next=['Is this seat taken?', 'I’m new here.', 'How do you spell…?'], week=['Sorry, can you repeat that?', 'Please call me…', 'Let’s work together.'], unit=['Introduce · spell · ask for repetition']),
  teach=teach(goal='Toda aula termina com uma produção observável.', solo=['Sem anotações: uma pergunta, uma resposta a uma situação e uma expressão nova.'], group=['Exit challenge individual; compare com o colega e combine a tarefa.'], answers=['How do you spell your name? · Sorry, can you repeat that? · I’m new here.'], extra=['Revisão espaçada: retomar na próxima aula, em uma semana e na missão da unidade.'])),
 LEVELS([('I’m new. Hello.', 'Say who you are. Short phrases, models and pictures.'), ('Hi, I’m new here. Can you repeat that, please?', 'Ask for repetition and for help.'), ('I just joined this class, so could you say that more slowly?', 'Explain a need and ask for adjustment.'), ('I’m still getting used to the pace, so would you mind going over the instructions again?', 'Ask for clarification with nuance.'), ('I’m afraid I missed that; could you walk me through it once more?', 'Handle a communication gap smoothly.'), ('Forgive me, I seem to have lost the thread; would you mind running through that again?', 'Manage the interaction with tact.')], you='A1')]

LESSON = LESSON_OF(41, 'First day in class', 'First day in class', 'Primeiro dia de aula', 1, ['Mina', 'Ryo'], 'classroom', DIALOG, PAGES)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
