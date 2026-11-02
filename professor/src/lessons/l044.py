#!/usr/bin/env python3
"""Aula 44 · Workplace small talk (A1, 60 min). Gera data/v3/044.json."""
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

DIALOG = dict(speakers={'Coworker': {'name': 'Raj'}, 'Teammate': {'name': 'Pia'}}, lines=[
 dict(who='Coworker', en='Good morning, Pia! **How was your weekend?**', pt='Bom dia, Pia! Como foi o seu fim de semana?'),
 dict(who='Teammate', en='Pretty good, thanks! I went hiking. And you?', pt='Muito bom, obrigada! Fui fazer trilha. E você?'),
 dict(who='Coworker', en='Nice! **Did you** go with friends?', pt='Legal! Você foi com amigos?'),
 dict(who='Teammate', en='Yes, with my sister. It was sunny.', pt='Sim, com a minha irmã. Fez sol.'),
 dict(who='Coworker', en='Great weather! Mine was quiet. I watched a movie.', pt='Que tempo ótimo! O meu foi tranquilo. Assisti a um filme.'),
 dict(who='Teammate', en='**Sounds relaxing!** Want some coffee?', pt='Parece relaxante! Quer um café?'),
 dict(who='Coworker', en='Yes, please. **Are you busy** this afternoon?', pt='Sim, por favor. Você está ocupada esta tarde?'),
 dict(who='Teammate', en='Not really. Why?', pt='Na verdade, não. Por quê?'),
 dict(who='Coworker', en='Want to have lunch together later?', pt='Quer almoçar junto mais tarde?'),
 dict(who='Teammate', en='Sure! See you at noon.', pt='Claro! Nos vemos ao meio-dia.')])

PAGES = [
 OPEN(4, 'Workplace small talk', 'Conversa informal no trabalho', 'It is Monday morning at your new office in the United States. You meet a coworker at the coffee machine and have a short, friendly chat.', 'office', ['Raj', 'Pia'],
  'By the end of the class you can start a friendly chat at work, ask about the weekend, ask a simple follow-up question and invite someone for lunch.',
  ['Start a chat: How was your weekend?', 'Ask a follow-up: Did you…?', 'React: Sounds nice! / Sounds relaxing!', 'Check availability: Are you busy…?'],
  ['I start the chat.', 'I ask one follow-up question.', 'I react to the answer.', 'I end the chat in a friendly way.'],
  'What do you talk about with coworkers in Portuguese? Are those topics “safe” everywhere?',
  teach(goal='Abrir pela situação real: o café da manhã de segunda-feira no escritório.', solo=['Pergunte sobre o que o estudante conversa no intervalo do trabalho.', 'Mostre os 4 critérios.'], group=['Cada estudante diz um assunto típico de intervalo.', 'Mostre os critérios: missão final.'], extra=['Do you like your coworkers?', 'What do you usually drink at work?'], support=['Aceite respostas curtas ou em português.'])),
 dict(t='rl_warm', stage='warm', title='Connection & warm-up',
  intro=dict(solo='Start with real questions about weekends and work.', group='One question per student, then a question back to a classmate.'),
  recall='At the library (last lesson): “Can I borrow…?”. Ask: Can I borrow your pen?',
  qs=[dict(q='What did you do last weekend?', pt='O que você fez no fim de semana passado?', sup=['I stayed home.', 'I saw friends.', 'I worked.']), dict(q='Do you like Mondays?', pt='Você gosta de segundas-feiras?', sup=['Not really!', 'Yes, I do.', 'They’re okay.']), dict(q='What is your favorite weekend activity?', pt='Qual é a sua atividade favorita no fim de semana?', sup=['Cooking.', 'Sleeping!', 'Playing soccer.'])],
  tip='Use the answers to practice simple past: stayed, saw, worked.', teach=teach(goal='Entrar no idioma e ativar o passado simples de verbos comuns.', extra=['Where did you go?', 'Who did you go with?'], errors=[W('I go to the beach yesterday.', 'I went to the beach yesterday.'), W('I stay at home.', 'I stayed at home.')], support=['Mostre os chips de resposta.'])),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Life in the USA',
  intro='Small talk is part of the work day in the United States. Look at the cards and guess before you read.',
  cards=[dict(vis='obj:cup', en='Coffee-break chat', pt='Conversa na pausa do café', note='Short, friendly talks near the coffee machine or in the kitchen.'), dict(vis='obj:umbrella', en='Safe topics', pt='Assuntos seguros', note='Weather, weekend, food, hobbies, travel and sports.'), dict(vis='obj:speech', en='Questions to avoid', pt='Perguntas a evitar', note='With new people: salary, age, politics, religion.')],
  qs=[dict(q='What do coworkers talk about in small talk?', pt='Sobre o que os colegas conversam?', levels=dict(A1='The weekend. The weather.', A2='They talk about the weekend, food or plans.', B1='Typical topics are the weekend, the weather, food, hobbies and travel.', B2='Light topics such as the weekend, sports or travel help people connect without getting too personal.')), dict(q='Is “How are you?” a real question?', pt='“How are you?” é uma pergunta de verdade?', levels=dict(A1='It is a greeting.', A2='Often it is a greeting. You say “Good, thanks!”', B1='It is usually a greeting, so a short answer like “Good, thanks. You?” is enough.', B2='Usually it works as a greeting, not as a request for details, unless you know the person well.')), dict(q='How do you end a short chat?', pt='Como terminar uma conversa curta?', levels=dict(A1='I say: “See you!”', A2='I say: “Nice talking to you. See you later!”', B1='I say something friendly and mention work: “I should get back to it. Talk later!”', B2='I wrap up politely, for example “Good to catch up; I’d better get back to work.”'))],
  compare='In Brazil people may ask more personal questions early on (family, age, salary can come up). In the US small talk often stays lighter at first. What is normal where you live?',
  teach=teach(goal='Ativar o contexto: temas seguros e pergunta-cumprimento.', solo=['Mostre os cartões e peça hipóteses.', 'Compare com o ambiente de trabalho do estudante.'], group=['Cada estudante escolhe um cartão e explica.', 'Pergunte “Do you agree?”.'], answers=['Q1: weekend, weather, food, hobbies.', 'Q2: usually a greeting.', 'Q3: friendly closing and back to work.'], extra=['What topic is too personal for you?', 'What do people talk about in your office?'], support=['Use as respostas A1 como andaime.'], stretch=['B2: discuta como as normas variam por região e empresa; evite generalizações absolutas.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='office', tod='day', cast=['Raj', 'Pia']),
  pass1=dict(q='What are Raj and Pia doing?', pt='O que Raj e Pia estão fazendo?', opts=['Having a friendly chat', 'Having a job interview', 'Calling a client'], ans=0),
  pass2=dict(tasks=[dict(label='Pia’s weekend activity', ans='hiking'), dict(label='Who she went with', ans='sister'), dict(label='What Raj watched', ans='movie'), dict(label='Lunch time', ans='noon')]),
  teach=teach(goal='Compreender o essencial antes de ver o texto.', solo=['Esconda o texto. 1ª escuta: o que fazem.', '2ª escuta: atividade, com quem, filme e hora do almoço.'], group=['Duplas anotam antes de revelar.', 'Compare as respostas.'], answers=['Pass 1: friendly chat.', 'Pass 2: hiking · sister · movie · noon'], extra=['Who is more talkative?', 'How do they feel about the weekend?'], support=['Use “Slow” na 2ª escuta.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='What did Pia do on the weekend?', opts=['She went hiking.', 'She stayed home.', 'She worked.'], ans=0), dict(q='What did Raj do?', opts=['He watched a movie.', 'He went to the beach.', 'He cooked for friends.'], ans=0), dict(q='What does Pia offer?', opts=['Coffee', 'A ride', 'Her book'], ans=0), dict(q='When do they have lunch?', opts=['At noon', 'At nine', 'At five'], ans=0)],
  retell=dict(prompt='Retell the conversation in your own words, at your level.', starters=['Raj asks Pia about…', 'Pia went…', 'Raj watched…', 'Then they decide to…']),
  teach=teach(goal='Ler o diálogo, perceber os chunks e recontar.', solo=['O estudante lê o Raj; você lê a Pia.', 'Peça que reconte.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia.'], answers=['She went hiking · he watched a movie · coffee · at noon'], extra=['What did YOU do last weekend?', 'Is this chat formal?'], errors=[W('Did you went with friends?', 'Did you go with friends?'), W('How was the your weekend?', 'How was your weekend?')], support=['Mostre o PT depois da 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[C('How was your weekend?', 'Como foi o seu fim de semana?', 'Start small talk, especially on Monday.', pri=True, alt='Also: **Did you have a good weekend?**'), C('Did you…?', 'Você…? (passado)', 'Ask a follow-up about the past: Did you go out?', pri=True), C('Are you busy…?', 'Você está ocupado…?', 'Check if the person has time: Are you busy now?', pri=True, alt='Also: **Do you have a minute?**'), C('Sounds nice!', 'Parece legal!', 'React to good news or plans. Also: Sounds relaxing / fun.', pri=True),
         C('And you?', 'E você?', 'Give the turn back after your answer.'), C('Want some coffee?', 'Quer um café?', 'A friendly offer at work.', reg='informal', alt='More polite: **Would you like some coffee?**'), C('Not much.', 'Nada de mais.', 'A short answer to “What did you do?”', reg='informal')],
  discover=dict(fns=['Starting a chat', 'Follow-up', 'Reacting', 'Checking time', 'Giving the turn back'], items=[dict(en='How was your weekend?', fn='Starting a chat'), dict(en='Did you go with friends?', fn='Follow-up'), dict(en='Sounds relaxing!', fn='Reacting'), dict(en='Are you busy this afternoon?', fn='Checking time'), dict(en='And you?', fn='Giving the turn back')]),
  note='Choose 3–5 expressions (★) to use again and again.', teach=teach(goal='Escolher 3–5 chunks e descobrir a função.', solo=['Pergunte “When do you say it?”.', 'Peça um exemplo próprio.'], group=['Cada estudante escolhe uma ★ e explica.', 'Compare em duplas.'], answers=['Starting a chat · Follow-up · Reacting · Checking time · Giving the turn back'], extra=['Which one is for a friend and which for a boss?'], errors=[W('How was the weekend of you?', 'How was your weekend?'), W('You are busy?', 'Are you busy?')], support=['Só as 3–4 ★.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Asking about the past', formula='**How was** + your + weekend / trip / day?', ex=['How was your weekend?', 'How was your trip?', 'How was your day?'], main=True), dict(name='Follow-up questions', formula='**Did you** + base verb + …?', ex=['Did you go with friends?', 'Did you watch the game?', 'Did you cook?'], main=True),
            dict(name='Checking availability', formula='**Are you busy** + now / today / after lunch?', ex=['Are you busy now?', 'Are you busy after lunch?']), dict(name='Answering with past verbs', formula='**I** + past verb', ex=['I went hiking.', 'I watched a movie.', 'I stayed home.'])],
  swap=dict(frame='How was your {thing}? Did you {verb} {extra}?', tpt='Como foi o seu {thing}? Você {verb} {extra}?',
   slots=[dict(k='thing', label='Thing', opts=O(('weekend', 'fim de semana'), ('trip', 'viagem'), ('day', 'dia'))), dict(k='verb', label='Verb', opts=O(('go', 'foi'), ('see', 'viu'), ('cook', 'cozinhou'))), dict(k='extra', label='Extra', opts=O(('with friends', 'com amigos'), ('a movie', 'um filme'), ('anything new', 'algo novo')))]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['How was your weekend?', 'I hope you had a pleasant weekend.'], ['Not much.', 'Nothing in particular.'], ['Want some coffee?', 'Would you care for some coffee?'], ['Are you busy?', 'Do you have a moment?']], note='These are differences of context and register, not absolute rules.'),
  teach=teach(goal='Fixar 2 padrões (How was…? / Did you…?). Did + verbo base.', solo=['Mostre o padrão no diálogo.', 'Use “Swap the words”.'], group=['Troca em cadeia.', 'Em pares.'], answers='Padrões 01/02 são o foco; 03/04 são expansão.', extra=['Ask a different follow-up question.', 'Answer with a past verb.'], errors=[W('Did you went?', 'Did you go?'), W('How is your weekend? (já passou)', 'How was your weekend?'), W('I am busy not.', 'I’m not busy.')], support=['Só How was your weekend? e a resposta I went… na 1ª rodada.'], stretch=['Combine: How was your trip? Did you see anything famous?'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Reductions', tip='In fast speech, did you sounds like “didja” and want to sounds like “wanna”. You do not have to say them this way, but you should understand them.',
  items=[dict(say='Did you go?', linked='Did·ja go?', ipa='/ˈdɪdʒə/', rhythm='ooO'), dict(say='Want to have lunch?', linked='Wanna have LUNCH?', ipa='/ˈwɑnə/', rhythm='oooO'), dict(say='How was your weekend?', linked='How wuz yer WEEK·end?', ipa='/ˈhaʊ wəz jər/', rhythm='oooOo')],
  identify=[dict(q='Which one do you hear?', opts=['Did you go?', 'Do you go?', 'Are you going?'], ans=0, say='Did you go?'), dict(q='Which one do you hear?', opts=['Want to have lunch?', 'What to have lunch?', 'Went to have lunch?'], ans=0, say='Want to have lunch?')],
  own=dict(prompt='Write one question with “Did you…?” and one with “Want to…?” for a coworker.', criteria='Say each one twice: slowly, then reduced. Does your partner understand both?'),
  teach=teach(goal='UM só fenômeno: reduções (did you → didja, want to → wanna).', solo=['Modele devagar e rápido.', 'Identify e depois uso próprio.'], group=['Coro, depois duplas.', 'Cada um cria duas perguntas.'], answers=['Identify 1: Did you go? · Identify 2: Want to have lunch?'], errors=[W('Did you com “d-i-d-y-o-u” separado e lento sempre', 'Did-ja, ligado'), W('Want to com “t” duro e pausa', 'Wanna, ligado')], support=['Foque em reconhecer (escuta); só depois em produzir.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    MC('1. It is Monday. You start small talk.', ['How was your weekend?', 'What is your salary?', 'Where is the report?'], 0, 'A safe, friendly topic.'),
    MC('2. Your coworker says “I went hiking.” Ask a follow-up.', ['Did you go with friends?', 'Do you went with friends?', 'You are hiking?'], 0, 'Did you + base verb.'),
    MC('3. Your coworker says “I watched a great movie.”', ['Sounds nice!', 'I am busy.', 'No, thank you.'], 0, 'React to what you hear.'),
    MC('4. You want to invite someone for lunch. Check first.', ['Are you busy at noon?', 'Is you busy noon?', 'You busy are?'], 0, 'Are you busy…? checks availability.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    GAP('How ___ your weekend?', 'was', 'How was…? for the past.', bank=['was', 'is', 'were']),
    GAP('Did you ___ to the park?', 'go', 'Did + base verb.', bank=['go', 'went', 'going']),
    SW('Make it a question about the past:', 'You went out.', ['Did you go out?', 'Did you go out'], 'Did you go out?', 'Did you + base verb?'),
    SW('Ask about their trip:', 'trip', ['How was your trip?', 'How was your trip'], 'How was your trip?', 'How was your + noun?'),
    RP('How was your weekend?', 'Choose the best reply.', ['Pretty good, thanks! And you?', 'It is Monday.', 'I am a weekend.'], 0, 'Answer and give the turn back.'),
    RP('Are you busy this afternoon?', 'You are free. Choose the best reply.', ['Not really. Why?', 'Yes, it is afternoon.', 'I am afternoon.'], 0, 'Answer and ask why.')])],
  teach=teach(goal='Do controlado ao guiado antes da fala livre.', solo=['Peça que justifique cada resposta.', 'Se acertar rápido, peça duas versões.'], group=['Resolvam em duplas e comparem.', 'Equipes: ponto por resposta justificada.'], answers=['1: How was your weekend? · 2: Did you go with friends? · 3: Sounds nice! · 4: Are you busy at noon?', 'Gap: was · go · Did you go out? · How was your trip? · Pretty good, thanks! And you? · Not really. Why?'], extra=['Say each answer naturally, with a smile.'], errors=[W('Did you went?', 'Did you go?'), W('How was you weekend?', 'How was your weekend?')], support=['Ofereça o banco de palavras.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — chat at the coffee machine',
  brief=dict(teacher='You are a coworker. Ask about the weekend and give short answers to test the student.', student='You are a new employee: start a chat, ask a follow-up and invite the coworker to lunch.'),
  orders=['Greet and ask about the weekend', 'Ask a follow-up with Did you…?', 'React with Sounds nice!', 'Invite to lunch (check Are you busy…?)'],
  complications=['The coworker only says “Fine.” Ask another question.', 'The coworker is busy.', 'You do not know a word: ask for help.', 'Someone asks a personal question: change the topic politely.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['How was your weekend?', 'Did you…?', 'Sounds nice!', 'Are you busy…?']), dict(label='Keywords', desc='Only the keywords', help=['weekend', 'did', 'nice', 'busy', 'lunch'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I start the chat.', 'I ask a follow-up.', 'I react.', 'I end the chat in a friendly way.'],
  teach=teach(goal='Simulação com complicação e três rodadas com menos apoio.', solo=['Use o fim de semana real do estudante.', 'Rodada 1: chunks. Rodada 2: palavras-chave. Rodada 3: sem roteiro.', 'Anote 2–3 correções.'], extra=['What do you say when you are very busy?'], errors=[W('I am went.', 'I went.')], support=['Volte à rodada 1 se travar.'], stretch=['Mude de assunto com naturalidade: “By the way…”.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Weekend', min=3, task='Ask your partner about the weekend.', hint='How was your weekend?'), dict(title='Follow-up', min=3, task='Ask two follow-up questions.', hint='Did you…? / Who did you go with?'), dict(title='React and invite', min=3, task='React and invite your partner for lunch or coffee.', hint='Sounds nice! / Are you busy…?'), dict(title='Pair report', min=2, whole=True, task='Whole group: tell the class one thing about your partner.', hint='He/She went…')],
  infogap=dict(title='Weekend plans', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='Student A', task='You know two weekend activities. Ask about the rest.', rows=[dict(k='Saturday morning', v='soccer'), dict(k='Saturday night', v=''), dict(k='Sunday morning', v='sleep late'), dict(k='Sunday night', v='')]),
   b=dict(title='Student B', task='You know two weekend activities. Ask about the rest.', rows=[dict(k='Saturday morning', v=''), dict(k='Saturday night', v='dinner with friends'), dict(k='Sunday morning', v=''), dict(k='Sunday night', v='watch a movie')])),
  teach=teach(goal='Fluência por repetição com informações novas.', group=['Troque os pares a cada rodada.', 'Sem salas simultâneas: interações sequenciais.', 'Cada aluno faz ≥1 pergunta e ≥1 resposta.'], answers=['A: soccer; sleep late. B: dinner with friends; watch a movie.'], extra=['What do you do on Saturday night?', 'Do you like Sundays?'], errors=[W('I play soccer in Saturday.', 'I play soccer on Saturday.'), W('What you do?', 'What do you do?')], support=['Dê frases-modelo no chat.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — the coffee-machine chat',
  goal='Each group must keep a friendly work chat going for two minutes and end it politely.',
  missions=[dict(who='A', role='Two coworkers', mission='Start small talk on Monday. Ask about the weekend and give a full answer.', constraint='Use “How was your weekend?” and “Did you…?”', start='Good morning! How was…'), dict(who='B', role='Two coworkers', mission='One person is busy. Check availability and agree on a time to talk.', constraint='Use “Are you busy…?” and “Sounds nice!”', start='Hi! Are you busy…'), dict(who='C', role='Three coworkers', mission='Plan a team lunch. Ask about each person’s weekend first.', constraint='Each person asks one question and gives one answer.', start='Hi everyone! How…')], min=11,
  success=['Start the chat.', 'Ask a follow-up.', 'React.', 'End the chat in a friendly way.'],
  teach=teach(goal='Realizar algo com o inglês: manter uma conversa leve.', group=['Cada grupo recebe papel, restrição e missão.', 'Progressão: com apoio → palavras-chave → sem roteiro.', 'Anote 2–3 correções.'], answers=['Modelo: “How was your weekend?” → “Good! I went hiking. And you?” → “Sounds nice! Did you…?”'], extra=['How do you end a chat politely?'], support=['Dê o início de frase em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short chat message to a coworker. Ask about the weekend and invite the person to coffee.',
  steps=['Greeting', 'Question about the weekend', 'Invitation', 'Closing'],
  model='Hi Pia! **How was your weekend?** I stayed home and watched a movie. **Are you busy** at 3 p.m.? Want to get a coffee? Let me know!',
  checklist=['I greeted my coworker.', 'I asked about the weekend.', 'I invited my coworker.', 'I closed in a friendly way.'],
  tip='Fix only 2–3 priority points. Show a more natural way to say the same idea.', fix=dict(n=3),
  teach=teach(goal='Produção escrita curta ligada à situação.', solo=['Peça o texto; corrija 2–3 pontos.'], group=['Troquem os textos e corrijam em duplas.'], extra=['Add one sentence about your weekend.'], errors=[W('I stay home yesterday.', 'I stayed home yesterday.'), W('You want a coffee?', 'Do you want a coffee? / Want to get a coffee?')], support=['Dê o modelo e peça só para trocar os dados.'])),
 FEEDBACK('Example: You asked a follow-up and reacted to the answer.', 'Example: Use did + base verb: Did you go?', 'Example: Keep a two-minute chat going without notes.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❓', name='Build a question', prompt='Without notes: ask a coworker about the weekend.', model='How was your weekend?'), dict(ic='💬', name='Respond to a situation', prompt='A coworker says: “I went to the beach.” React.', model='Sounds nice!'), dict(ic='⭐', name='Use a new expression', prompt='Check if someone is free this afternoon.', model='Are you busy this afternoon?')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 45-second audio: tell what you did last weekend.', 'Write three follow-up questions with Did you…?', 'Practice didja / wanna by listening to a short video.', 'Listen to the dialogue again and underline two expressions.']),
  spaced=dict(next=['How was your weekend?', 'Did you…?', 'Are you busy…?'], week=['Sounds nice!', 'And you?', 'Want some coffee?'], unit=['Chat · ask · react · invite']),
  teach=teach(goal='Toda aula termina com uma produção observável.', solo=['Sem anotações: pergunta, resposta e expressão nova.'], group=['Exit challenge individual; combine a tarefa.'], answers=['How was your weekend? · Sounds nice! · Are you busy this afternoon?'], extra=['Revisão espaçada: próxima aula, uma semana e missão da unidade.'])),
 LEVELS([('Weekend? Good?', 'Start with words and a smile.'), ('How was your weekend? Did you go out?', 'Ask and follow up.'), ('How was your weekend? I stayed home, but I heard you went hiking.', 'Share and ask about a detail.'), ('I’ve been meaning to ask how your trip went, since you mentioned it last week.', 'Refer back to earlier talk.'), ('I hope you managed to get some rest over the weekend; it sounded like a hectic few days.', 'Show interest with nuance.'), ('I trust the weekend afforded you some well-earned respite after such a demanding week.', 'Use a polished register with warmth.')], you='A1')]

LESSON = LESSON_OF(44, 'Workplace small talk', 'Workplace small talk', 'Conversa informal no trabalho', 4, ['Raj', 'Pia'], 'office', DIALOG, PAGES)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
