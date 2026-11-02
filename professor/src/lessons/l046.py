#!/usr/bin/env python3
"""Aula 46 · Emails and phone at work (A1, 60 min). Gera data/v3/046.json."""
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

DIALOG = dict(speakers={'Writer': {'name': 'Amy'}, 'Colleague': {'name': 'Max'}}, lines=[
 dict(who='Colleague', en='Hi Amy! You look busy.', pt='Oi, Amy! Você parece ocupada.'),
 dict(who='Writer', en='Yes! I’m writing an email to a client. Can you check it?', pt='Sim! Estou escrevendo um e-mail para uma cliente. Você pode revisar?'),
 dict(who='Colleague', en='Sure. Read it to me.', pt='Claro. Leia para mim.'),
 dict(who='Writer', en='“Dear Ms. Lee, **I’m writing to** ask about my order.”', pt='“Prezada Sra. Lee, escrevo para perguntar sobre o meu pedido.”'),
 dict(who='Colleague', en='Good. Now ask for what you need.', pt='Bom. Agora peça o que você precisa.'),
 dict(who='Writer', en='“**Could you send** the invoice by Friday?”', pt='“Você poderia enviar a fatura até sexta?”'),
 dict(who='Colleague', en='Perfect. Now the ending.', pt='Perfeito. Agora o final.'),
 dict(who='Writer', en='“**Thanks for your help.** Best, Amy.”', pt='“Obrigada pela ajuda. Abraços, Amy.”'),
 dict(who='Colleague', en='Great! If she doesn’t reply, call her.', pt='Ótimo! Se ela não responder, ligue.'),
 dict(who='Writer', en='Good idea. I’ll say, “**This is Amy** from Blue Sky.”', pt='Boa ideia. Vou dizer: “Aqui é a Amy, da Blue Sky.”')])

PAGES = [
 OPEN(6, 'Emails and phone at work', 'E-mails e telefone no trabalho', 'You write a short work email in English and prepare for a phone call. A colleague helps you with the opening, the request and the closing.', 'office', ['Amy', 'Max'],
  'By the end of the class you can open a work email, make a polite request, close it with thanks, and introduce yourself on the phone.',
  ['Open an email: I’m writing to…', 'Make a request: Could you send…?', 'Close: Thanks for your help. Best, …', 'Introduce yourself on the phone: This is Amy from…'],
  ['I open the email clearly.', 'I make one polite request.', 'I close with thanks.', 'I introduce myself on the phone.'],
  'How do you start and end a work email in Portuguese? Do you use “Prezado” and “Atenciosamente”?',
  teach(goal='Abrir pela situação real: escrever o primeiro e-mail de trabalho em inglês.', solo=['Pergunte se o estudante escreve e-mails no trabalho e o que acha difícil.', 'Mostre os 4 critérios.'], group=['Cada estudante diz uma coisa que escreve por e-mail.', 'Mostre os critérios: missão final.'], extra=['Do you prefer email or phone?', 'How many emails do you write a day?'], support=['Aceite respostas curtas ou em português.'])),
 dict(t='rl_warm', stage='warm', title='Connection & warm-up',
  intro=dict(solo='Start with real questions about communication at work.', group='One question per student, then a question back to a classmate.'),
  recall='A simple job interview (last lesson): “I’m good at…”. Ask: What are you good at?',
  qs=[dict(q='Do you check email every day?', pt='Você olha e-mail todo dia?', sup=['Yes, many times.', 'Once a day.', 'Not really.']), dict(q='Do you like phone calls?', pt='Você gosta de ligações?', sup=['Not really.', 'Yes, I do.', 'I prefer messages.']), dict(q='What is your email address?', pt='Qual é o seu endereço de e-mail?', sup=['It’s… at… dot com.', 'I use Gmail.', 'I have two.'])],
  tip='Use the answers to practice saying “at” and “dot”.', teach=teach(goal='Entrar no idioma e levantar vocabulário de comunicação.', extra=['Who do you write to most?', 'Do you use WhatsApp for work?'], errors=[W('My email is arroba…', 'My email is … at … dot com.'), W('I send message.', 'I send messages. / I send an email.')], support=['Mostre os chips de resposta.'])),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Life in the USA',
  intro='Work emails in English have a clear shape. Look at the cards and guess before you read.',
  cards=[dict(vis='obj:envelope', en='Opening', pt='Abertura', note='Hi Sam, (friendly) or Dear Ms. Lee, (more formal).'), dict(vis='obj:pen', en='Closing', pt='Fecho', note='Best, · Thanks, · Best regards, — short and polite.'), dict(vis='obj:phone', en='Phone call', pt='Ligação', note='You say “This is Amy”, not “I am Amy”.')],
  qs=[dict(q='How do you start a work email?', pt='Como começar um e-mail de trabalho?', levels=dict(A1='Hi Sam, or Dear Ms. Lee,', A2='“Hi” for a friend, “Dear Ms. Lee” for a new contact.', B1='Use Hi + first name with colleagues, and Dear + title + last name when it is formal or new.', B2='Match the tone to the relationship: Hi Sam, for a colleague, Dear Ms. Lee, for a new or formal contact.')), dict(q='How do you end a work email?', pt='Como terminar um e-mail de trabalho?', levels=dict(A1='Best, Amy', A2='“Thanks,” or “Best,” and then your name.', B1='Common endings are Best, Thanks, and Best regards, followed by your name.', B2='Short closings such as Best, or Thanks, are common; Sincerely, is saved for very formal letters.')), dict(q='How do you say your name on the phone?', pt='Como dizer seu nome ao telefone?', levels=dict(A1='This is Amy.', A2='“This is Amy from Blue Sky.”', B1='You say “This is Amy” and then the company, and ask: “Can I speak to…?”', B2='“Hello, this is Amy from Blue Sky; could I speak to Ms. Lee?” is a standard opening.'))],
  compare='In Brazilian emails “Prezado(a)” and “Atenciosamente” are common. In English, “Hi” and “Best,” are often enough at work. What do you use in your company?',
  teach=teach(goal='Ativar o contexto: abertura e fecho de e-mails, e “This is…”.', solo=['Mostre os cartões e peça hipóteses.', 'Compare com e-mails do estudante.'], group=['Cada estudante escolhe um cartão e explica.', 'Pergunte “Do you agree?”.'], answers=['Q1: Hi/Dear + name.', 'Q2: Best, / Thanks, + name.', 'Q3: This is Amy from…'], extra=['How formal are your emails?', 'What is a good subject line?'], support=['Use as respostas A1 como andaime.'], stretch=['B2: compare tom e formalidade em e-mails no Brasil e nos EUA.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='office', tod='day', cast=['Amy', 'Max']),
  pass1=dict(q='What is Amy doing?', pt='O que a Amy está fazendo?', opts=['Writing an email', 'Calling a taxi', 'Eating lunch'], ans=0),
  pass2=dict(tasks=[dict(label='The email is to', ans='Ms. Lee'), dict(label='Amy asks for the', ans='invoice'), dict(label='Deadline', ans='Friday'), dict(label='Closing word', ans='Best')]),
  teach=teach(goal='Compreender o essencial antes de ver o texto.', solo=['Esconda o texto. 1ª escuta: o que a Amy faz.', '2ª escuta: destinatária, pedido, prazo e fecho.'], group=['Duplas anotam antes de revelar.', 'Compare as respostas.'], answers=['Pass 1: writing an email.', 'Pass 2: Ms. Lee · invoice · Friday · Best'], extra=['Is the email formal? How do you know?', 'What does Amy plan to do next?'], support=['Use “Slow” na 2ª escuta.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='Who is the email for?', opts=['A client, Ms. Lee', 'Max', 'The boss'], ans=0), dict(q='What does Amy ask for?', opts=['The invoice', 'A meeting room', 'A day off'], ans=0), dict(q='When does she need it?', opts=['By Friday', 'By tomorrow', 'By Monday'], ans=0), dict(q='What will Amy do if there is no reply?', opts=['Call her', 'Write again tomorrow', 'Wait a month'], ans=0)],
  retell=dict(prompt='Retell the conversation in your own words, at your level.', starters=['Amy writes an email to…', 'She asks for…', 'She closes with…', 'If there is no reply, she will…']),
  teach=teach(goal='Ler o diálogo, perceber os chunks e recontar.', solo=['O estudante lê a Amy; você lê o Max.', 'Peça que reconte.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia.'], answers=['A client, Ms. Lee · the invoice · by Friday · call her'], extra=['What would you write in the email?', 'Why does Max say “Now ask for what you need”?'], errors=[W('I’m writing for ask…', 'I’m writing to ask…'), W('Could you send me the invoice until Friday?', 'Could you send the invoice by Friday?')], support=['Mostre o PT depois da 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[C('I’m writing to…', 'Estou escrevendo para…', 'Open an email and say your reason: I’m writing to ask about…', pri=True, alt='Also: **I’m contacting you about…**'), C('Could you send…?', 'Você poderia enviar…?', 'Make a polite request: Could you send the file?', pri=True, reg='polite', alt='More direct: **Can you send…?**'), C('Thanks for your help.', 'Obrigado pela ajuda.', 'Close an email or a call kindly.', pri=True, alt='Also: **Thanks in advance.**'), C('This is Amy from…', 'Aqui é a Amy, da…', 'Say your name on the phone.', pri=True),
         C('Dear Ms. Lee,', 'Prezada Sra. Lee,', 'A formal email opening.', reg='formal', alt='Friendly: **Hi Sam,**'), C('Best,', 'Abraços / Atenciosamente', 'A short, friendly closing before your name.'), C('Can I speak to…?', 'Posso falar com…?', 'Ask for a person on the phone.', reg='polite')],
  discover=dict(fns=['Opening', 'Request', 'Closing', 'Phone', 'Formal greeting'], items=[dict(en='I’m writing to ask about the order.', fn='Opening'), dict(en='Could you send the invoice?', fn='Request'), dict(en='Thanks for your help.', fn='Closing'), dict(en='This is Amy from Blue Sky.', fn='Phone'), dict(en='Dear Ms. Lee,', fn='Formal greeting')]),
  note='Choose 3–5 expressions (★) to use again and again.', teach=teach(goal='Escolher 3–5 chunks e descobrir a função.', solo=['Pergunte “When do you say it?”.', 'Peça um exemplo próprio.'], group=['Cada estudante escolhe uma ★ e explica.', 'Compare em duplas.'], answers=['Opening · Request · Closing · Phone · Formal greeting'], extra=['Which one is for email only? Which for the phone?'], errors=[W('I am Amy (ao telefone).', 'This is Amy.'), W('Send me the file.', 'Could you send me the file?')], support=['Só as 3–4 ★.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Giving a reason', formula='**I’m writing to** + base verb', ex=['I’m writing to ask about the order.', 'I’m writing to confirm the meeting.', 'I’m writing to say thank you.'], main=True), dict(name='Polite requests', formula='**Could you send** + thing + (by day)?', ex=['Could you send the invoice?', 'Could you send the file by Friday?', 'Could you send me your number?'], main=True),
            dict(name='Thanking', formula='**Thanks for** + noun', ex=['Thanks for your help.', 'Thanks for your email.']), dict(name='Phone opening', formula='**This is** + name + from + company', ex=['This is Amy from Blue Sky.', 'This is Max.'])],
  swap=dict(frame='I’m writing to {reason}. Could you send {thing} {when}?', tpt='Estou escrevendo para {reason}. Você poderia enviar {thing} {when}?',
   slots=[dict(k='reason', label='Reason', opts=O(('ask about my order', 'perguntar sobre o meu pedido'), ('confirm the meeting', 'confirmar a reunião'), ('say thank you', 'agradecer'))), dict(k='thing', label='Thing', opts=O(('the invoice', 'a fatura'), ('the file', 'o arquivo'), ('your number', 'o seu número'))), dict(k='when', label='When', opts=O(('by Friday', 'até sexta'), ('today', 'hoje'), ('this week', 'esta semana')))]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['Can you send it?', 'Could you please send it at your earliest convenience?'], ['Thanks!', 'Thank you for your assistance.'], ['This is Amy.', 'My name is Amy and I work at Blue Sky.'], ['Talk soon.', 'I look forward to hearing from you.']], note='These are differences of context and register, not absolute rules.'),
  teach=teach(goal='Fixar 2 padrões (I’m writing to… / Could you send…?). to + verbo base; Could + base.', solo=['Mostre o padrão no diálogo.', 'Use “Swap the words”.'], group=['Troca em cadeia.', 'Em pares.'], answers='Padrões 01/02 são o foco; 03/04 são expansão.', extra=['Make it shorter for a colleague: Can you send…?', 'Change the deadline.'], errors=[W('I’m writing for ask.', 'I’m writing to ask.'), W('Could you to send?', 'Could you send?'), W('Thanks by your help.', 'Thanks for your help.')], support=['Só I’m writing to… na primeira rodada.'], stretch=['Combine: I’m writing to confirm. Could you send the file? Thanks for your help.'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='The “th” sound', tip='Put your tongue lightly between your teeth: Thanks /θ/. Portuguese speakers often say “t” or “s”: avoid “tanks” and “sanks”.',
  items=[dict(say='Thanks for your help.', linked='THANKS for your help.', ipa='/θæŋks/', rhythm='OoooO'), dict(say='Thursday', linked='THURS·day', ipa='/ˈθɝzdeɪ/', rhythm='Oo'), dict(say='Thank you for your time.', linked='THANK you for your TIME.', ipa='/θæŋk/', rhythm='OoooO')],
  identify=[dict(q='Which one do you hear?', opts=['Thanks', 'Tanks', 'Sanks'], ans=0, say='Thanks'), dict(q='Which one do you hear?', opts=['three', 'tree', 'free'], ans=0, say='three')],
  own=dict(prompt='Write one sentence with “th” words: thanks, Thursday, think, three.', criteria='Say it twice. Did your tongue touch your teeth lightly?'),
  teach=teach(goal='UM só fenômeno: o som “th” /θ/ (thanks, Thursday, three).', solo=['Mostre a língua entre os dentes no espelho.', 'Identify e depois uso próprio.'], group=['Coro, depois duplas.', 'Cada um cria uma frase.'], answers=['Identify 1: Thanks · Identify 2: three'], errors=[W('Tanks / Sanks', 'Thanks /θæŋks/'), W('Free (por three)', 'Three /θri/')], support=['Pratique só “thanks” e “Thursday”.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    MC('1. You start an email to a client. Give your reason.', ['I’m writing to ask about my order.', 'I write for ask the order.', 'I’m writing ask order.'], 0, 'I’m writing to + base verb.'),
    MC('2. You need a file.', ['Could you send the file?', 'You send me the file.', 'Could you to send file?'], 0, 'Could you + base verb is polite.'),
    MC('3. You close an email.', ['Thanks for your help. Best, Amy', 'Bye bye, Amy', 'Thanks by help'], 0, 'A short, polite closing.'),
    MC('4. You call a client.', ['This is Amy from Blue Sky.', 'I am Amy from Blue Sky.', 'Amy is me.'], 0, 'On the phone: This is + name.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    GAP('I’m writing ___ ask about my order.', 'to', 'I’m writing to + verb.', bank=['to', 'for', 'at']),
    GAP('Could you ___ the invoice?', 'send', 'Could you + base verb.', bank=['send', 'sending', 'sent']),
    SW('Make it polite with “Could you”:', 'Send the file.', ['Could you send the file?', 'Could you send the file, please?', 'Could you send the file'], 'Could you send the file, please?', 'Could you… is softer than an order.'),
    SW('Say your name on the phone:', 'Amy / Blue Sky', ['This is Amy from Blue Sky.', 'This is Amy from Blue Sky'], 'This is Amy from Blue Sky.', 'This is + name + from + company.'),
    RP('Could you send the file by Friday?', 'Choose the best reply.', ['Sure! I’ll send it by Friday.', 'No, I am Friday.', 'This is the file.'], 0, 'Agree and repeat the deadline.'),
    RP('Thanks for your help.', 'Choose the best reply.', ['You’re welcome!', 'Yes, send.', 'This is Amy.'], 0, 'The usual reply to thanks.')])],
  teach=teach(goal='Do controlado ao guiado antes da fala livre.', solo=['Peça que justifique cada resposta.', 'Se acertar rápido, peça outra versão formal.'], group=['Resolvam em duplas e comparem.', 'Equipes: ponto por resposta justificada.'], answers=['1: I’m writing to ask about my order. · 2: Could you send the file? · 3: Thanks for your help. Best, Amy · 4: This is Amy from Blue Sky.', 'Gap: to · send · Could you send the file, please? · This is Amy from Blue Sky. · Sure! I’ll send it by Friday. · You’re welcome!'], extra=['Read each answer as if you were on a call.'], errors=[W('I’m writing for ask.', 'I’m writing to ask.'), W('Could you to send?', 'Could you send?')], support=['Ofereça o banco de palavras.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — the phone call',
  brief=dict(teacher='You are the client (Ms. Lee). Answer the phone and add a small problem.', student='You are an employee: call, say who you are, ask for the file and close with thanks.'),
  orders=['Say who you are on the phone', 'Say why you are calling or writing', 'Ask the client to send something by a day', 'Close with thanks'],
  complications=['The client cannot hear you well: repeat slowly.', 'The client is not available: leave a message.', 'You need to spell your email address.', 'The client asks you to send it again.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['This is Amy from…', 'I’m writing to…', 'Could you send…?', 'Thanks for your help.']), dict(label='Keywords', desc='Only the keywords', help=['this is', 'writing', 'send', 'by Friday', 'thanks'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I introduce myself.', 'I say my reason.', 'I make one polite request.', 'I close with thanks.'],
  teach=teach(goal='Simulação com complicação e três rodadas com menos apoio.', solo=['Use empresa e nomes reais ou fictícios do estudante.', 'Rodada 1: chunks. Rodada 2: palavras-chave. Rodada 3: sem roteiro.', 'Anote 2–3 correções.'], extra=['How do you leave a message?'], errors=[W('Can I leave recado?', 'Can I leave a message?')], support=['Volte à rodada 1 se travar.'], stretch=['Deixe uma mensagem de voz de 20 segundos.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Phone opening', min=3, task='Call your partner. Say who you are and why you call.', hint='This is… from… / I’m calling about…'), dict(title='Make a request', min=3, task='Ask your partner to send something by a day.', hint='Could you send…?'), dict(title='Close it', min=3, task='Close the call with thanks.', hint='Thanks for your help.'), dict(title='Email together', min=2, whole=True, task='Whole group: write one email, one sentence each.', hint='Dear… / I’m writing to…')],
  infogap=dict(title='Contact list', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='Student A', task='You know two contacts. Ask about the rest.', rows=[dict(k='Ms. Lee', v='invoice, by Friday'), dict(k='Mr. Cruz', v=''), dict(k='Ms. Park', v='contract, today'), dict(k='Mr. Sato', v='')]),
   b=dict(title='Student B', task='You know two contacts. Ask about the rest.', rows=[dict(k='Ms. Lee', v=''), dict(k='Mr. Cruz', v='report, on Monday'), dict(k='Ms. Park', v=''), dict(k='Mr. Sato', v='photos, this week')])),
  teach=teach(goal='Fluência por repetição com informações novas.', group=['Troque os pares a cada rodada.', 'Sem salas simultâneas: interações sequenciais.', 'Cada aluno faz ≥1 pergunta e ≥1 resposta.'], answers=['A: Lee invoice Friday; Park contract today. B: Cruz report Monday; Sato photos this week.'], extra=['What do you need from Mr. Cruz?', 'When do you need it?'], errors=[W('What he needs?', 'What does he need?'), W('Until Monday', 'By Monday')], support=['Dê frases-modelo no chat.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — email and call',
  goal='Each group must write a short work email and make a phone call to follow up.',
  missions=[dict(who='A', role='Employee + client', mission='Write an email asking for a file. The client calls back.', constraint='Use “I’m writing to…” and “Could you send…?”', start='Dear Ms. Lee, I’m writing…'), dict(who='B', role='Employee + client', mission='Call a client who is not there. Leave a message.', constraint='Use “This is… from…” and “Can I leave a message?”', start='Hello, this is…'), dict(who='C', role='Two colleagues', mission='Write a thank-you email after a meeting, then read it aloud.', constraint='Use “Thanks for your help.” and a friendly closing.', start='Hi team, thanks for…')], min=11,
  success=['Open clearly.', 'Make a polite request.', 'Close with thanks.', 'Use the right tone.'],
  teach=teach(goal='Realizar algo com o inglês: e-mail e telefone no mesmo contexto.', group=['Cada grupo recebe papel, restrição e missão.', 'Progressão: com apoio → palavras-chave → sem roteiro.', 'Anote 2–3 correções.'], answers=['Modelo: “Dear Ms. Lee, I’m writing to ask about my order. Could you send the invoice by Friday? Thanks for your help. Best, Amy”'], extra=['Is your email too long?'], support=['Dê o início de frase em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short work email. Ask someone to send a document by a day. Use a clear opening and closing.',
  steps=['Greeting', 'Reason', 'Request', 'Closing'],
  model='Hi Sam, **I’m writing to** ask about the schedule. **Could you send** the new list by Thursday? **Thanks for your help.** Best, Amy',
  checklist=['I used Hi / Dear and a name.', 'I gave my reason.', 'I made one polite request.', 'I closed with thanks and my name.'],
  tip='Fix only 2–3 priority points. Show a more natural way to say the same idea.', fix=dict(n=3),
  teach=teach(goal='Produção escrita curta ligada à situação.', solo=['Peça o e-mail; corrija 2–3 pontos.'], group=['Troquem os textos e corrijam em duplas.'], extra=['Add a subject line.'], errors=[W('Send me the document until Friday.', 'Could you send me the document by Friday?'), W('Att, Amy', 'Best, Amy')], support=['Dê o modelo e peça só para trocar os dados.'])),
 FEEDBACK('Example: Your opening and request were clear and polite.', 'Example: Say “th” in Thanks with the tongue between your teeth.', 'Example: Make a phone call and leave a message without notes.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❓', name='Build a sentence', prompt='Without notes: start an email and give your reason (ask about a meeting).', model='I’m writing to ask about the meeting.'), dict(ic='💬', name='Respond to a situation', prompt='You call a client. Say who you are.', model='This is Amy from Blue Sky.'), dict(ic='⭐', name='Use a new expression', prompt='Ask someone to send a file by Friday.', model='Could you send the file by Friday?')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Write a 4-sentence email to a coworker (opening, request, thanks, closing).', 'Record a 30-second voicemail with your name and reason.', 'Practice “th”: thanks, Thursday, three, think.', 'Listen to the dialogue again and underline two expressions.']),
  spaced=dict(next=['I’m writing to…', 'Could you send…?', 'Thanks for your help.'], week=['This is Amy from…', 'Can I speak to…?', 'Best,'], unit=['Write · request · call']),
  teach=teach(goal='Toda aula termina com uma produção observável.', solo=['Sem anotações: frase, resposta e expressão nova.'], group=['Exit challenge individual; combine a tarefa.'], answers=['I’m writing to ask about the meeting. · This is Amy from Blue Sky. · Could you send the file by Friday?'], extra=['Revisão espaçada: próxima aula, uma semana e missão da unidade.'])),
 LEVELS([('Hi. File, please. Thanks.', 'Write a very short message.'), ('Hi Sam, could you send the file? Thanks for your help.', 'Write a polite request.'), ('I’m writing to ask about my order. Could you send the invoice by Friday?', 'Give a reason and a deadline.'), ('I’d appreciate it if you could send the invoice by Friday, as we need it for our records.', 'Explain why you ask.'), ('Should it be convenient, I’d be grateful if you could forward the invoice before the end of the week.', 'Use formal, indirect language.'), ('I would be most obliged if you could see your way to forwarding the invoice at your earliest convenience.', 'Use refined formal register with tact.')], you='A1')]

LESSON = LESSON_OF(46, 'Emails and phone at work', 'Emails and phone at work', 'E-mails e telefone no trabalho', 6, ['Amy', 'Max'], 'office', DIALOG, PAGES)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
