#!/usr/bin/env python3
"""Aula 98 · A short presentation (A2, 60 min). Gera data/v3/098.json."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from rl_common import PLAN, finish

UNIT = dict(n=13, k=0, of=6, name='A2 consolidation')
UMAP = ['Planning a trip together', 'Workplace requests', 'Online shopping and delivery', 'A short presentation', 'A2 situations review', 'A2 Final Mission']

def unit(k):
    return dict(UNIT, k=k)

def T(goal, solo=None, group=None, answers=None, extra=None, errors=None, support=None, stretch=None):
    d = dict(goal=goal)
    for k, v in (('solo', solo), ('group', group), ('answers', answers), ('extra', extra), ('support', support), ('stretch', stretch)):
        if v:
            d[k] = v
    if errors:
        d['errors'] = [dict(w=w, r=r) for w, r in errors]
    return d

def mcq(q, opts, ans, why):
    return dict(type='mcq', q=q, opts=opts, ans=ans, why=why)

def gap(text, ans, why, bank=None):
    d = dict(type='gap', text=text, ans=ans, why=why)
    if bank:
        d['bank'] = bank
    return d

def swp(instr, frm, ans, model, why):
    return dict(type='swap', instr=instr, frm=frm, ans=ans, model=model, why=why)

def rep(npc, q, opts, ans, why):
    return dict(type='reply', npc=npc, q=q, opts=opts, ans=ans, why=why)

def warm(recall, qs, goal, extra, errors, support):
    return dict(t='rl_warm', stage='warm', title='Connection & warm-up',
     intro=dict(solo='Start with real questions about the student’s life, then link them to today’s situation.', group='One question per student, then ask a classmate the same question back.'),
     recall=recall, qs=[dict(q=q, pt=p, sup=s) for q, p, s in qs],
     tip='Use the answers to find gaps and to recycle earlier A2 content. Aim for longer answers: two or three connected sentences.',
     teach=T(goal, extra=extra, errors=errors, support=support))

def feedback(well, improve, nxt, tip_pt):
    return dict(t='rl_feedback', stage='write', title='Feedback & review — Speaking Performance Check',
     criteria=[dict(k='flu', name='Fluency', desc='Mantém a comunicação sem interrupções excessivas.'), dict(k='lan', name='Language use', desc='Utiliza adequadamente padrões, vocabulário e expressões.'), dict(k='pro', name='Pronunciation', desc='É compreensível e usa ritmo e entonação adequados.'), dict(k='int', name='Interaction', desc='Responde, pergunta, esclarece e desenvolve a conversa.')],
     interpret=[dict(max=8, text='Needs more support. Revisit the main patterns with guided practice before the next lesson.'), dict(max=13, text='Functional performance. Work on the lowest criteria in the next lesson.'), dict(max=17, text='Good control. Raise complexity and speed; add follow-up questions.'), dict(max=20, text='Strong performance. Move to a more demanding situation.')],
     prompts=dict(well=well, improve=improve, next=nxt),
     teach=T('Avaliar o que o aluno conseguiu comunicar, não só os erros gramaticais. ' + tip_pt,
      solo=['O estudante se autoavalia primeiro; depois você.', 'Feche com os três blocos: What you did well · What to improve · Your next challenge.'], group=['Dê um comentário por critério a cada estudante.', 'Cada um escolhe o próprio próximo desafio.'],
      answers='A rubrica é uma ferramenta interna de acompanhamento, não uma certificação CEFR.'))

def levels(rows, goal):
    gs = ['Say it with short phrases and models.', 'Give a reason and handle a small problem.', 'Explain and compare options with connectors.', 'Negotiate with nuance and appropriate register.', 'Handle complications diplomatically.', 'Manage the situation with precision and tact.']
    return dict(t='rl_levels', stage='exit', title='Level up — the same situation from A1 to C2', you='A2',
     intro='The structure stays the same; language complexity and autonomy grow.',
     ladder=[dict(lv=lv, say=s, goal=g if g else gs[i]) for i, (lv, (s, g)) in enumerate(zip(['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], rows))],
     note='This progression is illustrative: complex sentences do not define a level on their own. CEFR also considers comprehension, autonomy, fluency, accuracy, interaction and appropriateness.',
     teach=T(goal, solo=['Mostre onde o estudante está e a próxima etapa.'], group=['Cada um escolhe a frase do próprio nível e a do próximo.']))

DIALOG = dict(
 speakers={'Presenter': {'name': 'Mina'}, 'Classmate': {'name': 'Ryo'}},
 lines=[
  dict(who='Presenter', en='Okay, here’s my practice. **Today I’m going to talk about** recycling at school.', pt='Certo, aqui está meu ensaio. Hoje vou falar sobre reciclagem na escola.'),
  dict(who='Classmate', en='Nice start. Say your name first, then the topic, and smile.', pt='Bom começo. Diga seu nome primeiro, depois o tema, e sorria.'),
  dict(who='Presenter', en='Got it. **First,** I’ll explain why plastic is a problem. **Then** I’ll show three easy solutions.', pt='Entendi. Primeiro, vou explicar por que o plástico é um problema. Depois mostro três soluções fáceis.'),
  dict(who='Classmate', en='Good. Add an example, so people remember your idea.', pt='Bom. Acrescente um exemplo, para as pessoas lembrarem da sua ideia.'),
  dict(who='Presenter', en='Right. **For example,** our cafeteria uses a lot of plastic bottles every day.', pt='Certo. Por exemplo, nossa lanchonete usa muitas garrafas plásticas todos os dias.'),
  dict(who='Classmate', en='That works. How will you finish your talk?', pt='Isso funciona. Como você vai terminar a apresentação?'),
  dict(who='Presenter', en='**To sum up,** small changes make a big difference. **Thank you for listening.**', pt='Resumindo, pequenas mudanças fazem uma grande diferença. Obrigada por ouvirem.'),
  dict(who='Classmate', en='Perfect. Slow down a little, and ask if there are any questions.', pt='Perfeito. Fale um pouco mais devagar e pergunte se há dúvidas.')])

PAGES = [
 dict(t='rl_open', stage='warm', title='A Short Presentation', pt='Uma apresentação curta', level='A2',
  unit=dict(unit(4), map=UMAP),
  situation=dict(text='You must give a short presentation in class. You practice with a classmate: open the talk, explain your points in order, give an example and finish clearly.', scene='classroom', tod='day', cast=['Mina', 'Ryo']),
  goal='By the end of the class you can give a two-minute talk with an opening, two or three ordered points, an example and a closing, and answer a question.',
  canDo=['Open a talk: Today I’m going to talk about…', 'Order your ideas: First… Then… Finally…', 'Give an example: For example…', 'Close the talk: To sum up… Thank you for listening.'],
  success=['I introduce my topic.', 'I order my ideas.', 'I give an example.', 'I finish and invite questions.'],
  think='Do you feel nervous when you speak in front of people? What helps you feel calm?',
  teach=T('Abrir a aula pela situação real: uma apresentação curta com começo, meio e fim.',
   solo=['Leia o objetivo em voz alta e peça que o estudante diga com as próprias palavras o que vai fazer hoje.', 'Pergunte “Think about it” antes de mostrar qualquer expressão.'],
   group=['Cada estudante diz um tema sobre o qual poderia falar por dois minutos.', 'Mostre os 4 critérios de sucesso: é a missão final da aula.'],
   extra=['Have you ever given a presentation in English?', 'What topic could you talk about for two minutes?'],
   support=['Aceite respostas curtas ou em português na primeira rodada e reformule em inglês.'])),
 warm('Review: requests at work with Could you…? Ask: Could you explain your job or studies in two sentences?',
  [('What is something you know a lot about?', 'Sobre o que você sabe muito?', ['Cooking.', 'Football.', 'My city.']),
   ('Did you ever speak in front of a group?', 'Você já falou na frente de um grupo?', ['Yes, at school.', 'Only once.', 'Never.']),
   ('What makes a talk interesting for you?', 'O que torna uma apresentação interessante para você?', ['Good examples.', 'Pictures.', 'A short talk.'])],
  'Entrar no idioma e ativar vocabulário de tópicos pessoais e experiências passadas.', ['What was the best talk you ever heard?', 'What do you do before an important talk?'],
  [('I am agree with you.', 'I agree with you.'), ('I speaked at school.', 'I spoke at school.')], ['Ofereça as respostas-modelo (chips) e peça apenas que escolham uma.']),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Presentation structure',
  intro='Many English-speaking audiences like a clear structure. Look and guess before you read.',
  cards=[dict(vis='prop:book', en='Open, middle, close', pt='Abertura, desenvolvimento, fechamento', note='A common structure: say the topic, give your points, then sum up.'),
         dict(vis='prop:computer', en='Signpost words', pt='Palavras que guiam', note='“First,” “then” and “finally” help listeners follow your talk.'),
         dict(vis='prop:camera', en='Eye contact and questions', pt='Contato visual e perguntas', note='Speakers usually look at the audience and invite questions at the end.')],
  qs=[dict(q='How do speakers usually organize a short talk?', pt='Como se costuma organizar uma apresentação curta?', levels=dict(A1='First, second, last.', A2='They open, give two or three points and finish with a summary.', B1='A typical talk has an introduction, a few clear points with examples and a short conclusion.', B2='A clear opening, a logical sequence of points supported by examples and a concise conclusion are the usual expectation.')),
      dict(q='Why do speakers use “first,” “then” and “finally”?', pt='Por que se usam “first”, “then” e “finally”?', levels=dict(A1='To show the order.', A2='They help the audience follow the order of ideas.', B1='These words show the audience where you are in the talk.', B2='Signposting guides listeners through the structure so they do not get lost.')),
      dict(q='What do people often do at the end of a talk?', pt='O que as pessoas costumam fazer no final de uma apresentação?', levels=dict(A1='Say thank you.', A2='They say thank you and ask if there are any questions.', B1='They thank the audience and invite questions.', B2='They sum up the key idea, thank the audience and open the floor to questions.'))],
  compare='In Brazil, some talks start with a long background before the main point. Many English-speaking audiences like to hear the topic early: “Today I’m going to talk about…”. How do you start a talk where you live?',
  teach=T('Ativar o contexto cultural: estrutura clara e palavras de organização.',
   solo=['Mostre os 3 cartões e peça hipóteses antes de explicar.', 'Peça que o estudante compare com apresentações que já fez na escola ou no trabalho.'], group=['Cada estudante escolhe um cartão e explica em uma frase.', 'Pergunte “Do you agree?” entre colegas.'],
   answers=['Q1: abertura, 2–3 pontos, resumo.', 'Q2: ajudam a plateia a seguir a ordem.', 'Q3: agradecer e perguntar se há dúvidas.'], extra=['Do you prefer short or long talks?', 'What do you do when you forget a word?'],
   support=['Use as respostas do nível A1 como andaime e peça que repitam.'], stretch=['B2: explique como adaptar a mesma apresentação para colegas e para um chefe.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='classroom', tod='day', cast=['Mina', 'Ryo']),
  pass1=dict(q='What is Mina doing?', pt='O que a Mina está fazendo?', opts=['Practicing a short talk', 'Taking an exam', 'Asking for directions'], ans=0),
  pass2=dict(tasks=[dict(label='Topic', ans='recycling'), dict(label='Problem', ans='plastic'), dict(label='Number of solutions', ans='three'), dict(label='Her example is about the…', ans='cafeteria'), dict(label='Ryo’s last advice', ans='slow down')]),
  teach=T('Compreender a situação antes de ver o texto: ideia principal e depois 5 informações.',
   solo=['Esconda o texto. 1ª escuta: só a ideia principal.', '2ª escuta: tema, problema, número de soluções, exemplo e último conselho.', 'Mostre o texto só depois da 2ª escuta.'], group=['Escuta coletiva; duplas anotam as respostas antes de revelar.', 'Compare as respostas entre as duplas e só então mostre o texto.'],
   answers=['Pass 1: practicing a short talk.', 'Pass 2: recycling · plastic · three · cafeteria · slow down.'], extra=['What advice does Ryo give?', 'Is Mina’s talk clear? Why?'],
   support=['Use o botão “Slow” na 2ª escuta.', 'Pause depois de cada fala se necessário.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='What is Mina’s topic?', opts=['Recycling at school', 'Her summer trip', 'A new movie'], ans=0), dict(q='What does Ryo tell her to do first?', opts=['Say her name and the topic', 'Show a photo', 'Ask a question'], ans=0), dict(q='Why does Ryo want an example?', opts=['So people remember the idea', 'To make the talk longer', 'Because it is required'], ans=0), dict(q='How does Mina finish the talk?', opts=['With a summary and thanks', 'With a joke', 'With a long story'], ans=0)],
  retell=dict(prompt='Retell the conversation in your own words, at your level.', starters=['Mina practices…', 'First she says…', 'Ryo suggests…', 'At the end, she…']),
  teach=T('Ler o diálogo, perceber os chunks e recontar.',
   solo=['O estudante lê o papel da Mina; você lê o do Ryo.', 'Peça que reconte a conversa no nível que conseguir.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia: uma frase por estudante.'],
   answers=['Recycling at school · her name and the topic · so people remember · a summary and thanks'], extra=['What would YOU say in the opening?', 'What happens if you forget your next point?'],
   errors=[('Today I going to talk about…', 'Today I’m going to talk about…'), ('At the end, I will summary.', 'To sum up, … / In summary, …')], support=['Mostre a tradução (botão PT) depois da 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[dict(en='Today I’m going to talk about…', pt='Hoje vou falar sobre…', use='Open a talk and introduce the topic.', reg='neutral', alt='Also: **My topic today is…**', pri=True),
         dict(en='First, … Then, … Finally, …', pt='Primeiro… Depois… Por fim…', use='Put your ideas in order.', reg='neutral', pri=True),
         dict(en='For example, …', pt='Por exemplo…', use='Give an example to explain an idea.', reg='neutral', alt='Also: **For instance, …**', pri=True),
         dict(en='To sum up, …', pt='Resumindo…', use='Start your closing summary.', reg='neutral', alt='Also: **In summary, …**', pri=True),
         dict(en='Thank you for listening.', pt='Obrigado por ouvirem.', use='Finish the talk politely.', reg='neutral'),
         dict(en='Are there any questions?', pt='Há alguma pergunta?', use='Invite the audience to ask.', reg='neutral'),
         dict(en='Let me explain.', pt='Deixe-me explicar.', use='Go deeper into one idea.', reg='neutral'),
         dict(en='Let’s move on to…', pt='Vamos passar para…', use='Change to the next point.', reg='neutral')],
  discover=dict(fns=['Opening', 'Ordering ideas', 'Giving an example', 'Closing'],
   items=[dict(en='Today I’m going to talk about sleep.', fn='Opening'), dict(en='First, I’ll explain the problem.', fn='Ordering ideas'), dict(en='For example, many people drink coffee late.', fn='Giving an example'), dict(en='To sum up, sleep is important.', fn='Closing'), dict(en='Finally, I’ll give three tips.', fn='Ordering ideas')]),
  note='Choose the four ★ expressions to use again and again. The others help you understand and stretch.',
  teach=T('Escolher 4 chunks para uso repetido e descobrir a função de cada um.',
   solo=['Pergunte “When do you say it?” antes de dar o significado.', 'Peça que o estudante use cada ★ em uma frase sobre um tema dele.'], group=['Cada estudante escolhe a expressão que mais usaria e explica quando.', 'Compare em duplas: onde cada expressão aparece numa apresentação?'],
   answers=['Opening · Ordering ideas · Giving an example · Closing · Ordering ideas'], extra=['Which expression helps you the most when you are nervous?'], errors=[('Firstly, secondly, thirdly… (excesso)', 'First, then, finally (mais natural em fala).')], support=['Trabalhe só 3 das expressões ★ na primeira rodada.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Opening a talk', formula='**Today I’m going to talk about** + noun', ex=['Today I’m going to talk about sleep.', 'Today I’m going to talk about my hometown.', 'Today I’m going to talk about healthy habits.'], main=True),
            dict(name='Ordering ideas', formula='**First,** … **Then,** … **Finally,** …', ex=['First, I’ll explain the problem.', 'Then I’ll show three solutions.', 'Finally, I’ll answer your questions.'], main=True),
            dict(name='Giving an example', formula='**For example,** + sentence', ex=['For example, our cafeteria uses plastic bottles.', 'For example, I walk to work every day.']),
            dict(name='Closing', formula='**To sum up,** + main idea', ex=['To sum up, small changes matter.', 'To sum up, sleep helps us learn.'])],
  swap=dict(frame='Today I’m going to talk about {topic}. {order}, I’ll {action}.', tpt='Hoje vou falar sobre {topic}. {order}, vou {action}.',
   slots=[dict(k='topic', label='Topic', opts=[dict(en='recycling', pt='reciclagem'), dict(en='my hometown', pt='minha cidade natal'), dict(en='healthy habits', pt='hábitos saudáveis'), dict(en='remote work', pt='trabalho remoto')]),
          dict(k='order', label='Order', opts=[dict(en='First', pt='Primeiro'), dict(en='Then', pt='Depois'), dict(en='Finally', pt='Por fim')]),
          dict(k='action', label='Action', opts=[dict(en='explain the problem', pt='explicar o problema'), dict(en='give an example', pt='dar um exemplo'), dict(en='show three solutions', pt='mostrar três soluções')])]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['Today I’m going to talk about sleep.', 'This presentation will focus on sleep.'], ['First, I’ll explain the problem.', 'The first section describes the problem.'], ['For example, …', 'For instance, …'], ['To sum up, …', 'In conclusion, …']],
   note='These are differences of context and register, not absolute rules: “To sum up” is used in both speech and writing.'),
  teach=T('Fixar 2 padrões principais (01 e 02); os outros são expansão. Usar a troca de palavras para variar a fala.',
   solo=['Mostre o padrão DENTRO do diálogo (grife os chunks).', 'Use “Swap the words”: toque em cada peça e peça que o estudante diga a frase completa.', 'Compare spoken × written em 2 exemplos.'], group=['Troca em cadeia: cada estudante muda UMA peça e o próximo repete a frase.', 'Em pares: um escolhe as peças, o outro fala.'],
   answers='Padrão 01/02 são o foco; 03/04 são expansão para quem avançar rápido.', extra=['Open your own talk with Today I’m going to talk about…', 'Change one word and say the new sentence.'],
   errors=[('Today I talk about my city.', 'Today I’m going to talk about my city.'), ('First of all, I will to explain.', 'First, I’ll explain…'), ('For example: I like…', 'For example, I like… (vírgula depois de For example)')], support=['Fique só com abertura + First/Then/Finally na primeira rodada.'], stretch=['Adicionar uma transição: Now let’s move on to the solutions.'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Pausing and thought groups', tip='Speakers pause between ideas, not between every word: “Today I’m going to talk about / recycling at school.” Short pauses help the audience follow you. The goal is to be clear and natural, not to remove your accent.',
  items=[dict(say='Today I’m going to talk about recycling.', linked='Today I’m gonna talk about | RE-cy-cling.', ipa='/ˈgɔnə/', rhythm='ooooOoooOoo'), dict(say='First, I’ll explain the problem.', linked='FIRST | I’ll ex-PLAIN the PROB-lem.', ipa='/fɜːrst/', rhythm='OoooOoOo'), dict(say='To sum up, small changes matter.', linked='To SUM UP | SMALL CHAN-ges MAT-ter.', ipa='/tə sʌm ʌp/', rhythm='oOOoOOoO')],
  identify=[dict(q='Which one do you hear?', opts=['First, | I’ll explain the problem.', 'First I’ll | explain the problem.', 'First I’ll explain | the problem.'], ans=0, say='First, I’ll explain the problem.'), dict(q='Which one do you hear?', opts=['To sum up, | small changes matter.', 'To sum | up small changes matter.', 'To sum up small | changes matter.'], ans=0, say='To sum up, small changes matter.')],
  own=dict(prompt='Write your own opening sentence and your first point for a talk.', criteria='Say them with a short pause after the opening. Could your partner follow where one idea ended?'),
  teach=T('UM só fenômeno: pausas e grupos de ideias (thought groups).',
   solo=['3 passagens: escutar e identificar → reproduzir ritmo e pausas → usar em abertura e primeiro ponto próprios.', 'Marque as pausas com uma barra no texto e peça que o estudante respire nelas.'], group=['Coro, depois duplas; circule ouvindo.', 'Cada estudante lê um trecho com as pausas marcadas pelo colega.'],
   answers=['Identify 1: First, | I’ll explain the problem. · Identify 2: To sum up, | small changes matter.'], errors=[('Falar tudo sem pausa, muito rápido.', 'Pausar curto depois de cada ideia.'), ('Pausar no meio do grupo: To sum | up.', 'Manter “to sum up” junto.')], support=['Reduza a velocidade e marque as pausas com barras no texto.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    mcq('1. You start your talk about healthy habits.', ['Today I’m going to talk about healthy habits.', 'Today I talk habits healthy.', 'I am talk healthy today.'], 0, 'Today I’m going to talk about + topic.'),
    mcq('2. You want to introduce your second idea.', ['Then I’ll show three solutions.', 'Then I am show three solution.', 'After I to show.'], 0, 'Then + I’ll + verb keeps the order clear.'),
    mcq('3. You want to explain an idea with a real case.', ['For example, our cafeteria uses plastic bottles.', 'For exampling, cafeteria.', 'Example, I am cafeteria.'], 0, 'For example, + sentence.'),
    mcq('4. You are at the end of your talk.', ['To sum up, small changes matter. Thank you for listening.', 'The end, bye bye.', 'I finish now, nothing.'], 0, 'To sum up + main idea + thanks.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    gap('Today I’m going to ___ about my city.', 'talk', 'going to + base verb.', ['talk', 'talking', 'speak']),
    gap('___, I’ll answer your questions.', 'Finally', 'Finally marks the last point.', ['Finally', 'Firstly', 'Example']),
    swp('Turn it into an opening:', 'my hometown', ['Today I’m going to talk about my hometown.'], 'Today I’m going to talk about my hometown.', 'Today I’m going to talk about + topic.'),
    swp('Add an example:', 'Many people sleep too little. / my brother', ['For example, my brother sleeps only five hours.', 'For example, my brother only sleeps five hours.', 'For example, my brother sleeps five hours.'], 'For example, my brother sleeps only five hours.', 'For example, + new sentence.'),
    rep('Are there any questions?', 'You want to ask for time to think. Choose the best reply.', ['Good question. Let me think for a second.', 'No, question is good.', 'I think that you ask.'], 0, 'A natural way to gain time.')])],
  teach=T('Do controlado ao guiado: completar, substituir e transformar antes da fala livre.',
   solo=['Peça que o estudante justifique cada resposta.', 'Se acertar rápido, peça a versão mais informal ou mais formal.'], group=['Resolvam em duplas e comparem antes de revelar.', 'Equipes: ponto por resposta justificada.'],
   answers=['1: Today I’m going to talk about healthy habits. · 2: Then I’ll show three solutions. · 3: For example, our cafeteria uses plastic bottles. · 4: To sum up, small changes matter. Thank you for listening.', 'Gap: talk · Finally · Today I’m going to talk about my hometown. · For example, my brother sleeps only five hours. · Good question. Let me think…'], extra=['Say each correct answer aloud with pauses.'],
   errors=[('I’m going to talking about…', 'I’m going to talk about…'), ('Finally of all…', 'Finally, …')], support=['Ofereça o banco de palavras (chips) nas lacunas.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — give a short talk',
  brief=dict(teacher='You are the audience (ask a question at the end!).', student='You give a one-minute talk about a topic you know well. Open, order, give an example and close.'),
  orders=['A talk about your hometown', 'A talk about a hobby', 'A talk about a good habit'],
  complications=['The audience asks you to repeat a point.', 'You forget a word.', 'Someone asks a question you don’t understand.', 'You have only one minute left.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['Today I’m going to talk about…', 'First… Then… Finally…', 'For example…', 'To sum up…']), dict(label='Keywords', desc='Only the keywords', help=['topic', 'first', 'example', 'sum up', 'questions'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I introduce my topic.', 'I order my ideas.', 'I give an example.', 'I finish and invite questions.'],
  teach=T('Simulação com complicação inesperada e três rodadas com menos apoio.',
   solo=['Combine o tema com um assunto real do aluno (hobby, cidade, trabalho).', 'Rodada 1: com chunks. Rodada 2: só palavras-chave. Rodada 3: sem roteiro.', 'Meta de fala: 60–70% do tempo para o estudante. Anote 2–3 correções para a devolutiva.'],
   extra=['What if someone asks a question you can’t answer?'], errors=[('I don’t know the answer.', 'Good question. I’m not sure, but I can find out.')], support=['Volte à rodada 1 se travar; peça que repita só a primeira frase.'], stretch=['Responda a duas perguntas do público no final.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Open the talk', min=3, task='Introduce your topic in two sentences. Your partner gives feedback.', hint='Today I’m going to talk about…'), dict(title='Order and example', min=3, task='Explain two points in order and give an example.', hint='First… Then… For example…'), dict(title='Close and ask', min=3, task='Close with a summary and invite questions.', hint='To sum up… Are there any questions?'), dict(title='Share talks', min=2, whole=True, task='Whole group: each pair shares one talk opening and ending.', hint='My partner talked about…')],
  infogap=dict(title='Talk planner', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='You know the topics', task='You know two speakers and their topics. Ask about the rest.', rows=[dict(k='Speaker 1 topic', v='Recycling'), dict(k='Speaker 2 topic', v='Sleep'), dict(k='Speaker 1 time', v=''), dict(k='Speaker 2 time', v='')]),
   b=dict(title='You know the times', task='You know the speaking times. Ask about the rest.', rows=[dict(k='Speaker 1 topic', v=''), dict(k='Speaker 2 topic', v=''), dict(k='Speaker 1 time', v='9:30, two minutes'), dict(k='Speaker 2 time', v='9:40, three minutes')])),
  teach=T('Fluência por repetição da função com informações novas a cada rodada.',
   group=['Troque os pares a cada rodada (A+B / C+D → A+C / B+D → A+D / B+C → grupo todo). Com 6 estudantes, três duplas simultâneas.', 'Sem salas simultâneas: interações sequenciais enquanto uma dupla apresenta.', 'Responsabilidade individual: cada aluno faz ≥1 pergunta e ≥1 resposta.'],
   answers=['Info gap: A tem os temas (Recycling, Sleep); B tem horários (9:30, 2 min; 9:40, 3 min). Cada um completa perguntando.'], extra=['What is the first speaker’s topic?', 'How long is the second talk?'],
   errors=[('What time is begin?', 'What time does it begin?'), ('Three minutes of time.', 'Three minutes long.')], support=['Entregue frases-modelo no chat da turma.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — a two-minute talk',
  goal='Each group must prepare and give a short talk in English: open, order the ideas, give an example and close.',
  missions=[dict(who='A', role='Speaker and audience', mission='Give a talk about a place you love. Include one example and answer a question from the audience.', constraint='Use “Today I’m going to talk about…” and “To sum up…”.', start='Hello everyone! Today I’m going to talk about…'),
            dict(who='B', role='Speaker and audience', mission='Give a talk about a hobby. The audience must ask two questions.', constraint='Use “First… Then… Finally…” and “For example…”.', start='Hi! Today I’m going to talk about…'),
            dict(who='C', role='Speaker and audience', mission='Give a talk with three tips for learning English. Everyone gives feedback.', constraint='Use a number (three tips) and finish with “Thank you for listening.”', start='Good morning! Today I’m going to give you three tips…')], min=11,
  success=['Introduce the topic.', 'Order the ideas.', 'Give an example.', 'Finish and invite questions.'],
  teach=T('Realizar algo com o inglês: o objetivo é comunicar a ideia com clareza.',
   group=['Cada grupo recebe papéis, restrição e missão. Alterne orador e plateia.', 'Progressão: 1ª rodada com frases de apoio, 2ª só palavras-chave, 3ª sem roteiro.', 'Observe e anote 2–3 correções prioritárias; devolutiva no fim.'],
   answers=['Modelo: “Today I’m going to talk about my hometown. First, I’ll describe it. Then… For example… To sum up… Are there any questions?”'], extra=['What if the audience doesn’t understand?'], support=['Dê o início de frase (“Start with”) em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write the opening and closing of a short talk, with three ordered points in the middle.',
  steps=['Opening', 'Points in order', 'Example', 'Closing'],
  model='**Today I’m going to talk about** sleep. **First,** I’ll explain why it matters. **Then** I’ll share two simple tips. **For example,** I put my phone away at ten. **To sum up,** good sleep helps us learn. Thank you for listening!',
  checklist=['I introduced my topic.', 'I used First / Then / Finally.', 'I gave an example.', 'I closed with To sum up and thanks.'],
  tip='Fix only 2–3 priority points. Show a more natural way to say the same idea instead of rewriting everything.', fix=dict(n=3),
  teach=T('Produção escrita curta ligada à situação comunicativa.',
   solo=['Peça o texto; corrija 2–3 pontos prioritários e mostre uma forma mais natural.'], group=['Cada estudante escreve; depois troquem os textos entre colegas e corrijam em duplas.'],
   extra=['Add one question for the audience.'], errors=[('First of all, I going to…', 'First, I’m going to…'), ('To summary…', 'To sum up, …')], support=['Dê o modelo e peça só para trocar os dados.'])),
 feedback('Example: Your talk had a clear opening, order and ending.', 'Example: Pause between ideas, not between every word.', 'Example: Give a two-minute talk and answer a question without notes.', 'Observe a estrutura (abertura, ordem, fechamento) e o ritmo com pausas.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='🎤', name='Open a talk', prompt='Without notes: open a talk about your city.', model='Today I’m going to talk about my city.'), dict(ic='💬', name='Give an example', prompt='Give an example about why exercise helps.', model='For example, I walk for thirty minutes every day and I feel better.'), dict(ic='⭐', name='Close a talk', prompt='Close a talk and invite questions.', model='To sum up, exercise is important. Thank you for listening. Are there any questions?')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 60–90 second audio giving a mini talk.', 'Write the opening and closing of a talk on a topic you know well.', 'Review the four ★ expressions and write two examples for each.', 'Watch a short talk in English and note how the speaker opens and closes.']),
  spaced=dict(next=['Today I’m going to talk about…', 'First… Then… Finally…', 'For example…'], week=['To sum up…', 'Are there any questions?', 'Let’s move on to…'], unit=['Open · order · exemplify · close']),
  teach=T('Toda aula termina com uma produção observável.', solo=['Sem consultar as anotações: abrir uma apresentação, dar um exemplo e fechar.'], group=['Exit challenge individual; compare com o colega e combine a tarefa de continuidade.'],
   answers=['Today I’m going to talk about my city. · For example, I walk… · To sum up, … Are there any questions?'], extra=['Revisão espaçada: retomar na próxima aula, depois de uma semana e na missão de encerramento da unidade.'])),
 levels([('My talk: dogs. Dogs are good.', None), ('Today I’m going to talk about dogs. First, I’ll explain why they are good pets. To sum up, they are loyal.', 'Open, order, close with simple phrases.'), ('I’d like to talk about why dogs make good pets. I’ll give three reasons, with a personal example for each one.', None), ('This afternoon I’d like to explore why dogs are such effective companions, drawing on both research and my own experience.', None), ('My aim today is to challenge the assumption that dogs are merely pets, and to argue that they are genuine partners.', None), ('I shall argue that the dog’s place in human life is not incidental but constitutive of how we understand loyalty.', None)], 'Mostrar a progressão sem criar seis metodologias.')
]

LESSON = dict(n=98, topic='A short presentation', level='A2', title='A Short Presentation', pt='Uma apresentação curta', unit=unit(4), minutes=60, cast=['Mina', 'Ryo'], scene='classroom', tod='day', plan=PLAN, dialog=DIALOG, pages=PAGES)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
