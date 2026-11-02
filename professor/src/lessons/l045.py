#!/usr/bin/env python3
"""Aula 45 · A simple job interview (A1, 60 min). Gera data/v3/045.json."""
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

DIALOG = dict(speakers={'Candidate': {'name': 'Tessa'}, 'Interviewer': {'name': 'Ian'}}, lines=[
 dict(who='Interviewer', en='Hi, Tessa! Please sit down. **Tell me about yourself.**', pt='Oi, Tessa! Por favor, sente-se. Fale um pouco sobre você.'),
 dict(who='Candidate', en='Thank you! I’m friendly, and I work in a bookstore.', pt='Obrigada! Sou simpática e trabalho em uma livraria.'),
 dict(who='Interviewer', en='Nice. What are you good at?', pt='Legal. Em que você é boa?'),
 dict(who='Candidate', en='**I’m good at** talking to people. And I’m always on time.', pt='Sou boa em conversar com pessoas. E sempre chego no horário.'),
 dict(who='Interviewer', en='Do you have any work experience?', pt='Você tem alguma experiência de trabalho?'),
 dict(who='Candidate', en='Yes. **I have experience in** customer service. Two years.', pt='Tenho. Tenho experiência em atendimento ao cliente. Dois anos.'),
 dict(who='Interviewer', en='Excellent. Do you have any questions for me?', pt='Excelente. Você tem alguma pergunta para mim?'),
 dict(who='Candidate', en='Yes. What time does the shift start?', pt='Tenho. A que horas começa o turno?'),
 dict(who='Interviewer', en='At nine. We’ll call you this week.', pt='Às nove. Vamos ligar para você esta semana.'),
 dict(who='Candidate', en='Great. **Thank you for your time.**', pt='Ótimo. Obrigada pelo seu tempo.')])

PAGES = [
 OPEN(5, 'A simple job interview', 'Entrevista de emprego simples', 'You have a short interview for a job in a store in the United States. You introduce yourself, say what you are good at and talk about your experience.', 'office', ['Tessa', 'Ian'],
  'By the end of the class you can introduce yourself in an interview, say what you are good at, talk about your experience and close the interview politely.',
  ['Introduce yourself: Tell me about yourself → I’m… I work…', 'Say your strengths: I’m good at…', 'Talk about experience: I have experience in…', 'Close politely: Thank you for your time.'],
  ['I introduce myself.', 'I say one thing I am good at.', 'I talk about my experience.', 'I thank the interviewer.'],
  'How do you feel in a job interview? What helps you to stay calm?',
  teach(goal='Abrir pela situação real: a primeira entrevista em inglês.', solo=['Pergunte se o estudante já fez uma entrevista e como se sentiu.', 'Mostre os 4 critérios.'], group=['Cada estudante diz uma qualidade que um bom candidato tem.', 'Mostre os critérios: missão final.'], extra=['What job do you want?', 'What is your best quality?'], support=['Aceite respostas curtas ou em português.'])),
 dict(t='rl_warm', stage='warm', title='Connection & warm-up',
  intro=dict(solo='Start with real questions about work and study.', group='One question per student, then a question back to a classmate.'),
  recall='Workplace small talk (last lesson): “How was your weekend?”. Ask: How was your week?',
  qs=[dict(q='What do you do?', pt='O que você faz?', sup=['I’m a student.', 'I work in…', 'I’m a teacher.']), dict(q='Do you like your job?', pt='Você gosta do seu trabalho?', sup=['Yes, a lot.', 'It’s okay.', 'I’m looking for one.']), dict(q='What is your dream job?', pt='Qual é o seu emprego dos sonhos?', sup=['A chef.', 'A designer.', 'I don’t know yet.'])],
  tip='Use the answers to find the jobs and words the student needs.', teach=teach(goal='Entrar no idioma e levantar vocabulário de profissões.', extra=['Where do you work?', 'How long have you worked there?'], errors=[W('I work with teacher.', 'I’m a teacher.'), W('I am student of English.', 'I’m an English student.')], support=['Mostre os chips de resposta.'])),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Life in the USA',
  intro='Interviews have their own habits in the United States. Look at the cards and guess before you read.',
  cards=[dict(vis='obj:clock', en='Arrive on time', pt='Chegar no horário', note='Being on time, or a few minutes early, shows respect.'), dict(vis='obj:nametag', en='Handshake and eye contact', pt='Aperto de mão e contato visual', note='A firm handshake and eye contact are common and show interest.'), dict(vis='obj:envelope', en='Thank-you note', pt='Agradecimento depois', note='Many candidates send a short thank-you email after the interview.')],
  qs=[dict(q='How do you greet the interviewer?', pt='Como cumprimentar o entrevistador?', levels=dict(A1='I say: “Hello.” I shake hands.', A2='I say “Nice to meet you” and shake hands.', B1='A smile, a handshake and “Nice to meet you” are a good start.', B2='A brief handshake, eye contact and a warm greeting set a professional tone.')), dict(q='What can you say about yourself?', pt='O que dizer sobre você?', levels=dict(A1='My name. My job.', A2='My name, my job and one thing I am good at.', B1='A short summary of your work, your skills and what you want.', B2='A concise story: who you are, what experience you bring and why this job fits you.')), dict(q='What do you do after the interview?', pt='O que fazer depois da entrevista?', levels=dict(A1='I say thank you.', A2='I say thank you and send a short email.', B1='I send a thank-you email the same or the next day.', B2='A brief thank-you email restates your interest and thanks them for their time.'))],
  compare='In Brazil people also value being on time and a good first impression. Interviews may feel more formal or more personal. What is normal where you live?',
  teach=teach(goal='Ativar o contexto: etiqueta de entrevista nos EUA.', solo=['Mostre os cartões e peça hipóteses.', 'Compare com a experiência do estudante.'], group=['Cada estudante escolhe um cartão e explica.', 'Pergunte “Do you agree?”.'], answers=['Q1: handshake + greeting.', 'Q2: name, job, strength.', 'Q3: thank-you email.'], extra=['What do you wear to an interview?', 'Is eye contact easy for you?'], support=['Use as respostas A1 como andaime.'], stretch=['B2: discuta como normas de contato visual variam entre culturas, sem generalizar.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='office', tod='day', cast=['Tessa', 'Ian']),
  pass1=dict(q='What is happening?', pt='O que está acontecendo?', opts=['A job interview', 'A birthday party', 'A phone call to a friend'], ans=0),
  pass2=dict(tasks=[dict(label='Tessa works in a…', ans='bookstore'), dict(label='She is good at…', ans='talking to people'), dict(label='Her experience', ans='two years'), dict(label='The shift starts at', ans='nine')]),
  teach=teach(goal='Compreender o essencial antes de ver o texto.', solo=['Esconda o texto. 1ª escuta: o que acontece.', '2ª escuta: onde trabalha, o que faz bem, experiência e horário.'], group=['Duplas anotam antes de revelar.', 'Compare as respostas.'], answers=['Pass 1: a job interview.', 'Pass 2: bookstore · talking to people · two years · nine'], extra=['Is Tessa nervous? How do you know?', 'What does Ian say at the end?'], support=['Use “Slow” na 2ª escuta.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='Where does Tessa work now?', opts=['In a bookstore', 'In a bank', 'In a school'], ans=0), dict(q='What is Tessa good at?', opts=['Talking to people', 'Cooking', 'Driving'], ans=0), dict(q='How much experience does she have?', opts=['Two years', 'Ten years', 'None'], ans=0), dict(q='What does Tessa ask at the end?', opts=['What time the shift starts', 'How much the job pays', 'Where Ian lives'], ans=0)],
  retell=dict(prompt='Retell the conversation in your own words, at your level.', starters=['Ian asks Tessa…', 'She is good at…', 'She has experience in…', 'At the end she says…']),
  teach=teach(goal='Ler o diálogo, perceber os chunks e recontar.', solo=['O estudante lê a Tessa; você lê o Ian.', 'Peça que reconte.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia.'], answers=['In a bookstore · talking to people · two years · what time the shift starts'], extra=['What would YOU say about yourself?', 'Is Tessa a good candidate? Why?'], errors=[W('I am good in talk.', 'I’m good at talking.'), W('I have experience on customer service.', 'I have experience in customer service.')], support=['Mostre o PT depois da 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[C('Tell me about yourself.', 'Fale um pouco sobre você.', 'The most common opening question in an interview.', pri=True, alt='Also: **Can you tell me about yourself?**'), C('I’m good at…', 'Eu sou bom em…', 'Say a skill: I’m good at cooking.', pri=True, alt='Also: **I’m great with…**'), C('I have experience in…', 'Tenho experiência em…', 'Talk about your work history.', pri=True, alt='Also: **I’ve worked in…**'), C('Thank you for your time.', 'Obrigado pelo seu tempo.', 'Close the interview politely.', pri=True, reg='polite'),
         C('What are you good at?', 'Em que você é bom?', 'The interviewer asks about your strengths.'), C('Do you have any questions for me?', 'Você tem alguma pergunta para mim?', 'The interviewer invites your questions.'), C('I’m always on time.', 'Eu sempre chego no horário.', 'A simple quality that employers like.')],
  discover=dict(fns=['Opening', 'Strengths', 'Experience', 'Questions', 'Closing'], items=[dict(en='Tell me about yourself.', fn='Opening'), dict(en='I’m good at talking to people.', fn='Strengths'), dict(en='I have experience in customer service.', fn='Experience'), dict(en='Do you have any questions for me?', fn='Questions'), dict(en='Thank you for your time.', fn='Closing')]),
  note='Choose 3–5 expressions (★) to use again and again.', teach=teach(goal='Escolher 3–5 chunks e descobrir a função.', solo=['Pergunte “When do you say it?”.', 'Peça um exemplo próprio.'], group=['Cada estudante escolhe uma ★ e explica.', 'Compare em duplas.'], answers=['Opening · Strengths · Experience · Questions · Closing'], extra=['Which one is hardest for you?'], errors=[W('I am good in…', 'I’m good at…'), W('I have experience with years.', 'I have two years of experience.')], support=['Só as 3–4 ★.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Saying what you are good at', formula='**I’m good at** + noun / verb-ing', ex=['I’m good at cooking.', 'I’m good at math.', 'I’m good at talking to people.'], main=True), dict(name='Talking about experience', formula='**I have experience in** + field / job', ex=['I have experience in customer service.', 'I have experience in teaching.', 'I have experience in sales.'], main=True),
            dict(name='Introducing yourself', formula='**I’m** + adjective · **I work in** + place', ex=['I’m friendly.', 'I work in a bookstore.']), dict(name='Ability', formula='**I can** + base verb', ex=['I can work on weekends.', 'I can start on Monday.'])],
  swap=dict(frame='I’m good at {skill}. I have experience in {field}.', tpt='Eu sou bom em {skill}. Tenho experiência em {field}.',
   slots=[dict(k='skill', label='Skill', opts=O(('talking to people', 'conversar com pessoas'), ('using computers', 'usar computadores'), ('working in a team', 'trabalhar em equipe'), ('cooking', 'cozinhar'))), dict(k='field', label='Field', opts=O(('customer service', 'atendimento ao cliente'), ('teaching', 'ensino'), ('sales', 'vendas')))]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['I’m good at talking to people.', 'I have strong communication skills.'], ['I have experience in sales.', 'I have two years of experience in sales.'], ['Thanks for your time.', 'Thank you for taking the time to meet with me.'], ['I can start Monday.', 'I am available to begin on Monday.']], note='These are differences of context and register, not absolute rules.'),
  teach=teach(goal='Fixar 2 padrões (I’m good at… / I have experience in…). Verbo -ing depois de at.', solo=['Mostre o padrão no diálogo.', 'Use “Swap the words”.'], group=['Troca em cadeia.', 'Em pares.'], answers='Padrões 01/02 são o foco; 03/04 são expansão.', extra=['Say a skill you do NOT have yet.', 'Change the field and say the sentence.'], errors=[W('I’m good in cooking.', 'I’m good at cooking.'), W('I’m good at cook.', 'I’m good at cooking.'), W('I have experience at sales.', 'I have experience in sales.')], support=['Só I’m good at + um substantivo na 1ª rodada.'], stretch=['Combine: I’m good at… because I have experience in…'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Sentence stress', tip='English gives strength to the important words (nouns, verbs, adjectives) and weakens small words. Strong words: GOOD, TALKing, PEOple.',
  items=[dict(say='I’m good at talking to people.', linked='I’m GOOD at TALK·ing to PEO·ple.', ipa='/aɪm ɡʊd ət/', rhythm='oOoOoooOo'), dict(say='I have experience in sales.', linked='I have ex·PE·ri·ence in SALES.', ipa='/ɪkˈspɪriəns/', rhythm='ooooOoooO'), dict(say='Thank you for your time.', linked='THANK you for your TIME.', ipa='/θæŋk ju fər jər taɪm/', rhythm='OoooO')],
  identify=[dict(q='Which one do you hear?', opts=['I’m GOOD at cooking.', 'I’m good at COOKing.', 'I’m good AT cooking.'], ans=0, say='I’m good at cooking.'), dict(q='Which one do you hear?', opts=['Tell me about YOURself.', 'TELL me about yourself.', 'Tell ME about yourself.'], ans=1, say='Tell me about yourself.')],
  own=dict(prompt='Write one sentence about what you are good at. Mark the strong words.', criteria='Say it twice, clapping on the strong words. Did the small words get weaker?'),
  teach=teach(goal='UM só fenômeno: ênfase na frase (palavras de conteúdo fortes, palavras funcionais fracas).', solo=['Bata palmas nas sílabas fortes ao modelar.', 'Identify e depois uso próprio.'], group=['Coro, depois duplas.', 'Cada um marca e diz a própria frase.'], answers=['Identify 1: I’m GOOD at cooking. · Identify 2: TELL me about yourself.'], errors=[W('Todas as palavras com a mesma força', 'Palavras-chave fortes, pequenas fracas'), W('experience com acento em “ex”', 'ex-PE-ri-ence')], support=['Marque só uma palavra forte por frase no início.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    MC('1. The interviewer says: “Tell me about yourself.”', ['I’m friendly, and I work in a store.', 'Yes, I am about.', 'Tell you me.'], 0, 'A short answer: who you are, where you work.'),
    MC('2. You want to say you cook well.', ['I’m good at cooking.', 'I’m good in cook.', 'I good cooking.'], 0, 'I’m good at + verb-ing.'),
    MC('3. You worked in sales for three years.', ['I have experience in sales.', 'I have experience at sales years.', 'I am experience sales.'], 0, 'I have experience in + field.'),
    MC('4. The interview ends. What do you say?', ['Thank you for your time.', 'Bye, see you.', 'I time thank.'], 0, 'A polite, professional closing.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    GAP('I’m good ___ talking to people.', 'at', 'good at.', bank=['at', 'in', 'on']),
    GAP('I have experience ___ customer service.', 'in', 'experience in.', bank=['in', 'at', 'of']),
    SW('Say it about yourself:', 'cooking', ['I’m good at cooking.', 'I’m good at cooking'], 'I’m good at cooking.', 'I’m good at + noun / verb-ing.'),
    SW('Talk about experience:', 'sales', ['I have experience in sales.', 'I have experience in sales'], 'I have experience in sales.', 'I have experience in + field.'),
    RP('Do you have any questions for me?', 'Choose the best reply.', ['Yes. What time does the shift start?', 'Yes, I am good.', 'No, thank you for the coffee.'], 0, 'Ask a useful question about the job.'),
    RP('We’ll call you this week.', 'Choose the best reply.', ['Great. Thank you for your time.', 'I am week.', 'Where is my coffee?'], 0, 'Close politely.')])],
  teach=teach(goal='Do controlado ao guiado antes da fala livre.', solo=['Peça que justifique cada resposta.', 'Se acertar rápido, peça outra qualidade.'], group=['Resolvam em duplas e comparem.', 'Equipes: ponto por resposta justificada.'], answers=['1: I’m friendly, and I work in a store. · 2: I’m good at cooking. · 3: I have experience in sales. · 4: Thank you for your time.', 'Gap: at · in · I’m good at cooking. · I have experience in sales. · Yes. What time does the shift start? · Great. Thank you for your time.'], extra=['Say each answer as if you are in a real interview.'], errors=[W('I’m good in sales.', 'I’m good at sales.'), W('I have experience on sales.', 'I have experience in sales.')], support=['Ofereça o banco de palavras.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — your interview',
  brief=dict(teacher='You are the interviewer. Ask short questions and one surprising question.', student='You are the candidate: introduce yourself, say what you are good at, talk about experience and close.'),
  orders=['Answer “Tell me about yourself”', 'Say what you are good at', 'Talk about your experience', 'Ask one question and close politely'],
  complications=['You do not understand a question.', 'You have no experience: say what you can do.', 'The interviewer asks “Can you work weekends?”', 'You forget a word: explain with other words.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['Tell me about yourself.', 'I’m good at…', 'I have experience in…', 'Thank you for your time.']), dict(label='Keywords', desc='Only the keywords', help=['friendly', 'good at', 'experience', 'question', 'thank you'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I introduce myself.', 'I say one thing I am good at.', 'I talk about my experience.', 'I thank the interviewer.'],
  teach=teach(goal='Simulação com complicação e três rodadas com menos apoio.', solo=['Use um emprego real ou desejado pelo estudante.', 'Rodada 1: chunks. Rodada 2: palavras-chave. Rodada 3: sem roteiro.', 'Anote 2–3 correções.'], extra=['What if you have no experience? What can you say?'], errors=[W('I have experience no.', 'I don’t have experience, but I can learn fast.')], support=['Volte à rodada 1 se travar.'], stretch=['Explique por que você quer a vaga.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Introduce yourself', min=3, task='Answer “Tell me about yourself” in 3 sentences.', hint='I’m… I work in…'), dict(title='Skills', min=3, task='Say two things you are good at. Your partner asks a follow-up.', hint='I’m good at… / Why?'), dict(title='Experience', min=3, task='Talk about your experience. Your partner asks how long.', hint='I have experience in…'), dict(title='Best candidate', min=2, whole=True, task='Whole group: choose the best candidate for a job and explain.', hint='I choose… because…')],
  infogap=dict(title='Job ad', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='Student A', task='You know the job and the place. Ask about the rest.', rows=[dict(k='Job', v='sales assistant'), dict(k='Experience needed', v=''), dict(k='Place', v='bookstore'), dict(k='Start time', v='')]),
   b=dict(title='Student B', task='You know the experience and the time. Ask about the rest.', rows=[dict(k='Job', v=''), dict(k='Experience needed', v='1 year'), dict(k='Place', v=''), dict(k='Start time', v='9:00 a.m.')])),
  teach=teach(goal='Fluência por repetição com informações novas.', group=['Troque os pares a cada rodada.', 'Sem salas simultâneas: interações sequenciais.', 'Cada aluno faz ≥1 pergunta e ≥1 resposta.'], answers=['A: sales assistant; bookstore. B: 1 year; 9:00 a.m.'], extra=['What is the job?', 'Do you need experience?'], errors=[W('What the job is?', 'What is the job?'), W('How many experience do you need?', 'How much experience do you need?')], support=['Dê frases-modelo no chat.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — the interview',
  goal='Each group must run a short job interview in English and decide who gets the job.',
  missions=[dict(who='A', role='Interviewer + candidate', mission='Interview for a café job. Ask about skills and experience.', constraint='Use “Tell me about yourself” and “I’m good at…”', start='Hi! Please sit down. Tell me…'), dict(who='B', role='Interviewer + candidate', mission='The candidate has no experience. Show other skills and ask a question.', constraint='Use “I can…” and “Do you have any questions for me?”', start='Thank you for seeing me. I’m…'), dict(who='C', role='Panel of two + candidate', mission='Two interviewers ask one question each. The candidate closes politely.', constraint='Use “I have experience in…” and “Thank you for your time.”', start='Good morning! Tell me about…')], min=11,
  success=['Introduce yourself.', 'Say what you are good at.', 'Talk about experience.', 'Close politely.'],
  teach=teach(goal='Realizar algo com o inglês: conduzir e responder a uma entrevista curta.', group=['Cada grupo recebe papel, restrição e missão.', 'Progressão: com apoio → palavras-chave → sem roteiro.', 'Anote 2–3 correções.'], answers=['Modelo: “Tell me about yourself.” → “I’m friendly, and I work in a bookstore.” → “I’m good at talking to people.”'], extra=['Who is the best candidate? Why?'], support=['Dê o início de frase em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short thank-you email after a job interview. Thank the interviewer and say you want the job.',
  steps=['Greeting', 'Thanks', 'One strength', 'Closing'],
  model='Hi Ian, **thank you for your time** today. I enjoyed learning about the job. **I’m good at** talking to people, and I would love to join your team. Best, Tessa',
  checklist=['I greeted the interviewer.', 'I said thank you.', 'I mentioned one strength.', 'I closed politely (Best, / Thanks,).'],
  tip='Fix only 2–3 priority points. Show a more natural way to say the same idea.', fix=dict(n=3),
  teach=teach(goal='Produção escrita curta ligada à situação.', solo=['Peça o texto; corrija 2–3 pontos.'], group=['Troquem os textos e corrijam em duplas.'], extra=['Add one question about the job.'], errors=[W('Thanks you for your time.', 'Thank you for your time.'), W('I want very the job.', 'I really want the job.')], support=['Dê o modelo e peça só para trocar os dados.'])),
 FEEDBACK('Example: You gave a clear strength and a clear closing.', 'Example: Stress the key words: I’m GOOD at TALKing.', 'Example: Answer five interview questions without notes.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❓', name='Build a sentence', prompt='Without notes: say one thing you are good at.', model='I’m good at cooking.'), dict(ic='💬', name='Respond to a situation', prompt='“Do you have any experience?” You worked in sales.', model='Yes. I have experience in sales.'), dict(ic='⭐', name='Use a new expression', prompt='The interview ends. Close politely.', model='Thank you for your time.')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 60-second audio: tell me about yourself.', 'Write three things you are good at in English.', 'Practice the stress: I’m GOOD at TALKing.', 'Listen to the dialogue again and underline two expressions.']),
  spaced=dict(next=['Tell me about yourself.', 'I’m good at…', 'I have experience in…'], week=['Thank you for your time.', 'Do you have any questions for me?', 'I’m always on time.'], unit=['Introduce · strengths · experience']),
  teach=teach(goal='Toda aula termina com uma produção observável.', solo=['Sem anotações: frase, resposta e expressão nova.'], group=['Exit challenge individual; combine a tarefa.'], answers=['I’m good at cooking. · Yes. I have experience in sales. · Thank you for your time.'], extra=['Revisão espaçada: próxima aula, uma semana e missão da unidade.'])),
 LEVELS([('Hello. I work. Store.', 'Say a few words about yourself.'), ('I’m friendly. I’m good at talking to people.', 'Say your strengths.'), ('I have experience in customer service, and I’m good at solving problems.', 'Connect experience and skills.'), ('Having spent two years in customer service, I’ve learned to stay calm under pressure.', 'Use examples and nuance.'), ('What draws me to this role is the chance to apply my customer-service background to a team that values it.', 'Link your goals to the job.'), ('I would welcome the opportunity to contribute the depth of experience I have built, while continuing to learn.', 'Use a polished, persuasive register.')], you='A1')]

LESSON = LESSON_OF(45, 'A simple job interview', 'A simple job interview', 'Entrevista de emprego simples', 5, ['Tessa', 'Ian'], 'office', DIALOG, PAGES)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
