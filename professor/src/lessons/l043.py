#!/usr/bin/env python3
"""Aula 43 · At the library (A1, 60 min). Gera data/v3/043.json."""
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

DIALOG = dict(speakers={'Visitor': {'name': 'Emma'}, 'Librarian': {'name': 'Maya'}}, lines=[
 dict(who='Visitor', en='Hi! **Can I borrow** this book, please?', pt='Oi! Posso pegar este livro emprestado, por favor?'),
 dict(who='Librarian', en='Sure! Do you have a library card?', pt='Claro! Você tem cartão da biblioteca?'),
 dict(who='Visitor', en='No, not yet.', pt='Não, ainda não.'),
 dict(who='Librarian', en='Show me your ID, please. Then you get a card.', pt='Mostre o seu documento, por favor. Aí você recebe um cartão.'),
 dict(who='Visitor', en='Here you go. **How long can I keep it?**', pt='Aqui está. Por quanto tempo posso ficar com ele?'),
 dict(who='Librarian', en='Three weeks. Please bring it back on time.', pt='Três semanas. Por favor, devolva no prazo.'),
 dict(who='Visitor', en='**When is it due?**', pt='Qual é a data de devolução?'),
 dict(who='Librarian', en='April ninth. It’s on the receipt.', pt='Nove de abril. Está no recibo.'),
 dict(who='Visitor', en='Thanks! **Where can I find** cooking books?', pt='Obrigada! Onde encontro livros de culinária?'),
 dict(who='Librarian', en='Second floor, on the left. Please talk quietly there.', pt='Segundo andar, à esquerda. Por favor, fale baixo lá.'),
 dict(who='Visitor', en='Got it. Thank you so much!', pt='Entendi. Muito obrigada!')])

PAGES = [
 OPEN(3, 'At the library', 'Na biblioteca', 'You visit a public library in the United States for the first time. You want a card, a book to take home and a place to find the cooking section.', 'library', ['Emma', 'Maya'],
  'By the end of the class you can ask to borrow something, ask how long you can keep it, ask for the due date and find a book in the library.',
  ['Ask to borrow: Can I borrow…?', 'Ask the time limit: How long can I keep it?', 'Ask the date: When is it due?', 'Find things: Where can I find…?'],
  ['I ask to borrow something.', 'I ask how long I can keep it.', 'I find out where something is.', 'I thank the librarian and follow the rules.'],
  'Do you have a library card? What do you usually borrow, books or something else?',
  teach(goal='Abrir pela situação real: usar uma biblioteca em inglês pela primeira vez.', solo=['Pergunte se o estudante usa biblioteca e o que busca lá.', 'Mostre os 4 critérios.'], group=['Cada estudante diz uma coisa que se pega emprestado numa biblioteca.', 'Mostre os critérios: missão final.'], extra=['What is your favorite book?', 'Do you read on paper or on a screen?'], support=['Aceite respostas curtas ou em português na primeira rodada.'])),
 dict(t='rl_warm', stage='warm', title='Connection & warm-up',
  intro=dict(solo='Start with real questions about reading and studying.', group='One question per student, then a question back to a classmate.'),
  recall='Asking about the schedule (last lesson): “What time does… start?”. Ask: What time does your class start?',
  qs=[dict(q='Do you like to read?', pt='Você gosta de ler?', sup=['Yes, a lot.', 'A little.', 'Not really.']), dict(q='Where do you study?', pt='Onde você estuda?', sup=['At home.', 'At school.', 'In a library.']), dict(q='What was the last book you read?', pt='Qual foi o último livro que você leu?', sup=['I don’t remember.', 'A story about…', 'I read an e-book.'])],
  tip='Use the answers to find vocabulary gaps (borrow, return, card).', teach=teach(goal='Entrar no idioma e levantar vocabulário de leitura.', extra=['What kind of books do you like?', 'Do you have many books at home?'], errors=[W('I like very read.', 'I like to read a lot.'), W('I study in the library of my city.', 'I study at my city library.')], support=['Mostre os chips de resposta.'])),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Life in the USA',
  intro='Public libraries are a big part of daily life in many American towns. Look at the cards and guess before you read.',
  cards=[dict(vis='obj:book', en='Library card', pt='Cartão da biblioteca', note='Residents can usually get one by showing ID or proof of address.'), dict(vis='obj:magnifier', en='Free to borrow', pt='Empréstimo gratuito', note='Most public libraries let you borrow books for free. Many also lend movies and e-books.'), dict(vis='obj:bell', en='Quiet rules', pt='Regras de silêncio', note='Many libraries have quiet areas: you talk softly or not at all.')],
  qs=[dict(q='What do you need to borrow a book?', pt='O que você precisa para pegar um livro emprestado?', levels=dict(A1='A library card.', A2='A library card and sometimes an ID.', B1='You usually need a card, which you get with an ID or proof of address.', B2='Most public libraries issue a free card after you show an ID, and some ask for proof of address as well.')), dict(q='What happens when a book is late?', pt='O que acontece se o livro atrasa?', levels=dict(A1='You return it late.', A2='Some libraries ask a small fee.', B1='It depends: some libraries charge a small late fee, and others no longer charge one.', B2='Policies vary: some libraries have removed late fines, while others still charge a small daily fee.')), dict(q='How do people behave in a library?', pt='Como as pessoas se comportam numa biblioteca?', levels=dict(A1='They are quiet.', A2='They talk softly and turn off the phone sound.', B1='They keep their voice down, but many libraries also have areas where talking is fine.', B2='Quiet study areas exist side by side with spaces for children’s events or group work, where noise is accepted.'))],
  compare='In Brazil many public and school libraries also require a registration card. How is it where you live? Is it free?',
  teach=teach(goal='Ativar o contexto: cartão, gratuidade e regras de silêncio.', solo=['Mostre os cartões e peça hipóteses.', 'Compare com a biblioteca que o estudante conhece.'], group=['Cada estudante escolhe um cartão e explica.', 'Pergunte “Do you agree?”.'], answers=['Q1: a library card (ID).', 'Q2: depends on the library.', 'Q3: quiet, but there are talking areas.'], extra=['Have you ever lost a library book?', 'What is a good place to study?'], support=['Use as respostas A1 como andaime.'], stretch=['B2: compare políticas de multa de bibliotecas.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='library', tod='day', cast=['Emma', 'Maya']),
  pass1=dict(q='What does Emma want?', pt='O que a Emma quer?', opts=['To borrow a book', 'To buy a book', 'To return a book'], ans=0),
  pass2=dict(tasks=[dict(label='Emma needs a…', ans='library card'), dict(label='How long she can keep it', ans='three weeks'), dict(label='Where the cooking books are', ans='second floor'), dict(label='How to talk there', ans='quietly')]),
  teach=teach(goal='Compreender o essencial antes de ver o texto.', solo=['Esconda o texto. 1ª escuta: o que a Emma quer.', '2ª escuta: cartão, prazo, andar e regra.'], group=['Duplas anotam antes de revelar.', 'Compare as respostas.'], answers=['Pass 1: to borrow a book.', 'Pass 2: library card · three weeks · second floor · quietly'], extra=['Why does Maya ask for an ID?', 'What is the rule on the second floor?'], support=['Use “Slow” na 2ª escuta.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='What does Emma ask to borrow?', opts=['A book', 'A laptop', 'A map'], ans=0), dict(q='What does Maya ask for?', opts=['An ID', 'Money', 'A phone number'], ans=0), dict(q='How long can Emma keep it?', opts=['Three weeks', 'Three days', 'Three months'], ans=0), dict(q='Where are the cooking books?', opts=['Second floor', 'Near the door', 'In the café'], ans=0)],
  retell=dict(prompt='Retell the conversation in your own words, at your level.', starters=['Emma wants to…', 'Maya asks for…', 'She can keep the book…', 'The cooking books are…']),
  teach=teach(goal='Ler o diálogo, perceber os chunks e recontar.', solo=['O estudante lê a Emma; você lê a Maya.', 'Peça que reconte.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia.'], answers=['A book · an ID · three weeks · second floor'], extra=['What would you borrow?', 'What is “due”?'], errors=[W('Can I borrow me this book?', 'Can I borrow this book?'), W('How much time I can stay with it?', 'How long can I keep it?')], support=['Mostre o PT depois da 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[C('Can I borrow…?', 'Posso pegar emprestado…?', 'Ask to take something home for a while.', pri=True, alt='Also: **Can I check this out?** (US)'), C('How long can I keep it?', 'Por quanto tempo posso ficar com ele?', 'Ask the borrowing time.', pri=True, alt='Also: **How long can I borrow it?**'), C('When is it due?', 'Qual é a data de devolução?', 'Ask the date you must return it.', pri=True), C('Where can I find…?', 'Onde posso encontrar…?', 'Ask where a book or section is.', pri=True, alt='Also: **Where is the… section?**'),
         C('Do you have a library card?', 'Você tem cartão da biblioteca?', 'The librarian asks this before you borrow.'), C('Please talk quietly.', 'Por favor, fale baixo.', 'A rule you hear in a quiet area.', reg='polite'), C('Could you help me find…?', 'Pode me ajudar a encontrar…?', 'Ask the librarian for help.', reg='polite')],
  discover=dict(fns=['Borrowing', 'Time limit', 'Finding', 'Rules', 'Asking for help'], items=[dict(en='Can I borrow this book?', fn='Borrowing'), dict(en='How long can I keep it?', fn='Time limit'), dict(en='Where can I find cooking books?', fn='Finding'), dict(en='Please talk quietly.', fn='Rules'), dict(en='Could you help me find a map?', fn='Asking for help')]),
  note='Choose 3–5 expressions (★) to use again and again.', teach=teach(goal='Escolher 3–5 chunks e descobrir a função.', solo=['Pergunte “When do you say it?”.', 'Peça um exemplo próprio.'], group=['Cada estudante escolhe uma ★ e explica.', 'Compare em duplas.'], answers=['Borrowing · Time limit · Finding · Rules · Asking for help'], extra=['Which one would you use at a bookstore?'], errors=[W('Where I can find?', 'Where can I find…?'), W('Can I borrow it for how long?', 'How long can I keep it?')], support=['Só as 3–4 ★.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Asking permission', formula='**Can I borrow** + this / that + thing?', ex=['Can I borrow this book?', 'Can I borrow a pen?', 'Can I borrow your card?'], main=True), dict(name='Asking where', formula='**Where can I find** + thing?', ex=['Where can I find cooking books?', 'Where can I find a computer?', 'Where can I find the exit?'], main=True),
            dict(name='Asking how long', formula='**How long can I** + keep / use + it?', ex=['How long can I keep it?', 'How long can I use the computer?']), dict(name='Due date', formula='**When is it due?** / It’s due on + date', ex=['When is it due?', 'It’s due on April ninth.'])],
  swap=dict(frame='Can I {verb} {thing}? How long can I keep it?', tpt='Posso {verb} {thing}? Por quanto tempo posso ficar com ele?',
   slots=[dict(k='verb', label='Verb', opts=O(('borrow', 'pegar emprestado'), ('use', 'usar'), ('renew', 'renovar'))), dict(k='thing', label='Thing', opts=O(('this book', 'este livro'), ('a laptop', 'um notebook'), ('this movie', 'este filme')))]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['Can I borrow this?', 'May I borrow this item?'], ['It’s due Friday.', 'The return date is Friday.'], ['Where can I find…?', 'Could you tell me where to find…?'], ['Sure!', 'Certainly.']], note='These are differences of context and register, not absolute rules.'),
  teach=teach(goal='Fixar 2 padrões (Can I borrow…? / Where can I find…?).', solo=['Mostre o padrão no diálogo.', 'Use “Swap the words”.'], group=['Troca em cadeia.', 'Em pares.'], answers='Padrões 01/02 são o foco; 03/04 são expansão.', extra=['Change the thing and say the sentence.', 'Make the question more polite: Could I borrow…?'], errors=[W('Can I borrow to you this?', 'Can I borrow this?'), W('Where I can find the book?', 'Where can I find the book?'), W('How long can I to keep it?', 'How long can I keep it?')], support=['Só Can I borrow…? na primeira rodada.'], stretch=['Combine: Can I borrow this, and when is it due?'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Question intonation', tip='Yes/no questions often go up at the end: Can I borrow this? ↗. Questions with where, when and how long usually go down: Where can I find it? ↘.',
  items=[dict(say='Can I borrow this?', linked='Can I BOR·row this? ↗', ipa='/kən aɪ ˈbɑroʊ/', rhythm='ooOoo'), dict(say='Where can I find it?', linked='WHERE can I FIND it? ↘', ipa='/wɛr kən aɪ faɪnd ɪt/', rhythm='OooOo'), dict(say='How long can I keep it?', linked='How LONG can I KEEP it? ↘', ipa='/haʊ lɔŋ/', rhythm='oOooOo')],
  identify=[dict(q='Which one goes up at the end?', opts=['Can I borrow this? ↗', 'Where can I find it? ↘', 'When is it due? ↘'], ans=0, say='Can I borrow this?'), dict(q='Which one goes down at the end?', opts=['Is it due on Friday? ↗', 'Where is the exit? ↘', 'Do you have a card? ↗'], ans=1, say='Where is the exit?')],
  own=dict(prompt='Write one yes/no question and one wh-question you would ask in a library.', criteria='Did your voice go up for the yes/no question and down for the wh-question?'),
  teach=teach(goal='UM só fenômeno: entonação de perguntas (sobe em sim/não, desce em wh-).', solo=['Use a mão para mostrar a melodia subindo e descendo.', 'Identify e depois uso próprio.'], group=['Coro, depois duplas.', 'Cada um cria duas perguntas.'], answers=['Identify 1: Can I borrow this? · Identify 2: Where is the exit?'], errors=[W('Where can I find it? ↗', 'Where can I find it? ↘'), W('Can I borrow this? com entonação plana', 'Can I borrow this? ↗')], support=['Exagere a melodia com gestos.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    MC('1. You want to take a book home.', ['Can I borrow this book?', 'I borrow book now.', 'You give book me?'], 0, 'Can I borrow + noun?'),
    MC('2. You want to know the time limit.', ['How long can I keep it?', 'How much it is?', 'What is keep?'], 0, 'How long can I keep it?'),
    MC('3. You look for a dictionary.', ['Where can I find a dictionary?', 'Where I can dictionary?', 'What is a dictionary where?'], 0, 'Where can I find + noun?'),
    MC('4. The librarian says “It’s due Friday.” You want the date again.', ['When is it due?', 'Who is Friday?', 'How due?'], 0, 'When is it due? asks the return date.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    GAP('Can I ___ this movie?', 'borrow', 'Can I borrow…?', bank=['borrow', 'buy', 'finding']),
    GAP('Where ___ I find maps?', 'can', 'Where can I find…?', bank=['can', 'do', 'am']),
    SW('Ask how long you can keep it:', 'this book', ['How long can I keep this book?', 'How long can I keep it?'], 'How long can I keep this book?', 'How long can I keep + object?'),
    SW('Ask where to find it:', 'children’s books', ['Where can I find children’s books?', 'Where can I find children’s books'], 'Where can I find children’s books?', 'Where can I find + noun?'),
    RP('Do you have a library card?', 'You do not. Choose the best reply.', ['No, not yet. Can I get one?', 'Yes, a book.', 'On the second floor.'], 0, 'Answer and ask for what you need.'),
    RP('It’s due on May second.', 'Choose the best reply.', ['Got it. Thank you!', 'I am May.', 'Where is the card?'], 0, 'Confirm that you understood.')])],
  teach=teach(goal='Do controlado ao guiado antes da fala livre.', solo=['Peça que justifique cada resposta.', 'Se acertar rápido, peça a versão mais polida.'], group=['Resolvam em duplas e comparem.', 'Equipes: ponto por resposta justificada.'], answers=['1: Can I borrow this book? · 2: How long can I keep it? · 3: Where can I find a dictionary? · 4: When is it due?', 'Gap: borrow · can · How long can I keep this book? · Where can I find children’s books? · No, not yet. Can I get one? · Got it. Thank you!'], extra=['Say each correct answer aloud with the right melody.'], errors=[W('Where I can find?', 'Where can I find…?'), W('Can I borrow?', 'Can I borrow this?')], support=['Ofereça o banco de palavras.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — borrow like a local',
  brief=dict(teacher='You are the librarian. Create a small problem during the scene.', student='You are the visitor: get a card, borrow a book and find another one.'),
  orders=['Ask to borrow a book and get a card', 'Ask how long you can keep it', 'Ask for the due date', 'Ask where to find a cooking book'],
  complications=['You forgot your ID.', 'The book is not on the shelf.', 'The librarian says “too loud, please”.', 'You want to keep the book longer.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['Can I borrow…?', 'How long can I keep it?', 'When is it due?', 'Where can I find…?']), dict(label='Keywords', desc='Only the keywords', help=['borrow', 'card', 'keep', 'due', 'find'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I ask to borrow something.', 'I ask how long I can keep it.', 'I find out where something is.', 'I thank the librarian.'],
  teach=teach(goal='Simulação com complicação e três rodadas com menos apoio.', solo=['Combine o cenário com os interesses do estudante (livro, filme, notebook).', 'Rodada 1: chunks. Rodada 2: palavras-chave. Rodada 3: sem roteiro.', 'Anote 2–3 correções.'], extra=['What if the book is not there?'], errors=[W('I forget my ID.', 'I forgot my ID.')], support=['Volte à rodada 1 se travar.'], stretch=['Peça uma renovação e explique a razão.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Borrow', min=3, task='Ask your partner to borrow something small.', hint='Can I borrow…?'), dict(title='How long', min=3, task='Ask how long you can keep it.', hint='How long can I keep it? / When is it due?'), dict(title='Find it', min=3, task='Ask where the section is. Your partner points.', hint='Where can I find…?'), dict(title='Library map', min=2, whole=True, task='Whole group: describe the floors of a library.', hint='It’s on the… floor.')],
  infogap=dict(title='Library sections', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='Student A', task='You know cooking and maps. Ask about the rest.', rows=[dict(k='Cooking books', v='second floor'), dict(k='Children’s books', v=''), dict(k='Maps', v='first floor, near the desk'), dict(k='Computers', v='')]),
   b=dict(title='Student B', task='You know children’s books and computers. Ask about the rest.', rows=[dict(k='Cooking books', v=''), dict(k='Children’s books', v='first floor, on the right'), dict(k='Maps', v=''), dict(k='Computers', v='third floor')])),
  teach=teach(goal='Fluência por repetição com informações novas.', group=['Troque os pares a cada rodada.', 'Sem salas simultâneas: interações sequenciais.', 'Cada aluno faz ≥1 pergunta e ≥1 resposta.'], answers=['A: cooking = second floor; maps = first floor near the desk. B: children’s = first floor right; computers = third floor.'], extra=['Where can I find the computers?', 'Is it near the door?'], errors=[W('It is in second floor.', 'It’s on the second floor.'), W('On left.', 'On the left.')], support=['Dê frases-modelo no chat.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — get what you need',
  goal='Each group must get something done in English: borrow, ask about time and find a book.',
  missions=[dict(who='A', role='Visitor + librarian', mission='Get a library card and borrow one book.', constraint='Use “Can I borrow…?” and show an ID.', start='Hi! Can I borrow…'), dict(who='B', role='Visitor + librarian', mission='Ask how long you can keep a movie and the due date. You need more time.', constraint='Use “How long…?” and “When is it due?”', start='Excuse me, how long…'), dict(who='C', role='Two visitors', mission='Find a cooking book and a map. Follow the quiet rule.', constraint='Use “Where can I find…?” twice and talk quietly.', start='Excuse me, where…')], min=11,
  success=['Ask to borrow.', 'Ask how long.', 'Find the book.', 'Thank the librarian.'],
  teach=teach(goal='Realizar algo com o inglês: pegar o livro e entender as regras.', group=['Cada grupo recebe papel, restrição e missão.', 'Progressão: com apoio → palavras-chave → sem roteiro.', 'Anote 2–3 correções.'], answers=['Modelo: “Can I borrow this book?” → “Do you have a card?” → “No, not yet.” → “Show me your ID.”'], extra=['What if the book is not on the shelf?'], support=['Dê o início de frase em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short message to a friend: you found a good library. Say what you borrowed and when you must return it.',
  steps=['Greeting', 'What you borrowed', 'Due date', 'Closing'],
  model='Hi Ana! I got a library card today. **I borrowed** a cooking book and a movie. **It’s due on** April ninth. Do you want to go together next week?',
  checklist=['I greeted my friend.', 'I said what I borrowed.', 'I gave the due date.', 'I closed with a question.'],
  tip='Fix only 2–3 priority points. Show a more natural way to say the same idea.', fix=dict(n=3),
  teach=teach(goal='Produção escrita curta ligada à situação.', solo=['Peça o texto; corrija 2–3 pontos.'], group=['Troquem os textos e corrijam em duplas.'], extra=['Add one thing you want to read.'], errors=[W('I borrow a book yesterday.', 'I borrowed a book yesterday.'), W('It is due in April 9.', 'It’s due on April 9.')], support=['Dê o modelo e peça só para trocar os dados.'])),
 FEEDBACK('Example: You asked the due date and the time limit clearly.', 'Example: Let your voice go up on yes/no questions.', 'Example: Ask for a renewal and explain why without notes.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❓', name='Build a question', prompt='Without notes: ask where to find maps.', model='Where can I find maps?'), dict(ic='💬', name='Respond to a situation', prompt='You got the book. Ask how much time you have.', model='How long can I keep it?'), dict(ic='⭐', name='Use a new expression', prompt='Ask to borrow a pen from a classmate.', model='Can I borrow your pen?')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 45-second audio asking to borrow a book.', 'Write three things you can borrow in a library.', 'Practice question intonation with 4 questions.', 'Listen to the dialogue again and underline two expressions.']),
  spaced=dict(next=['Can I borrow…?', 'How long can I keep it?', 'Where can I find…?'], week=['When is it due?', 'Could you help me find…?', 'Please talk quietly.'], unit=['Borrow · ask the time · find']),
  teach=teach(goal='Toda aula termina com uma produção observável.', solo=['Sem anotações: pergunta, resposta e expressão nova.'], group=['Exit challenge individual; combine a tarefa.'], answers=['Where can I find maps? · How long can I keep it? · Can I borrow your pen?'], extra=['Revisão espaçada: próxima aula, uma semana e missão da unidade.'])),
 LEVELS([('Book? Take home?', 'Ask with words and a gesture.'), ('Can I borrow this book? How long can I keep it?', 'Ask permission and the time limit.'), ('I’d like to get a library card, and I want to borrow two books.', 'Ask for a service and explain.'), ('Could you tell me whether it’s possible to renew this item online?', 'Ask about options with indirect questions.'), ('I’m afraid I’ve misplaced my card; would it be possible to look me up with my ID?', 'Solve a problem with tact.'), ('Might I impose upon you to extend the loan, as I’ve not quite finished with it?', 'Use formal register with tact.')], you='A1')]

LESSON = LESSON_OF(43, 'At the library', 'At the library', 'Na biblioteca', 3, ['Emma', 'Maya'], 'library', DIALOG, PAGES)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
