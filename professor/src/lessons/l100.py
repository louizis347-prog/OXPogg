#!/usr/bin/env python3
"""Aula 100 · A2 Final Mission (A2, 60 min). Gera data/v3/100.json."""
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
 speakers={'Traveler 1': {'name': 'Mia'}, 'Traveler 2': {'name': 'Ken'}},
 lines=[
  dict(who='Traveler 1', en='Ken! Did you see the board? Our flight is delayed by two hours.', pt='Ken! Você viu o painel? Nosso voo está atrasado duas horas.'),
  dict(who='Traveler 2', en='Oh no. **Could you** wait here while I talk to the airline desk?', pt='Ah, não. Você poderia esperar aqui enquanto eu falo com o balcão da companhia?'),
  dict(who='Traveler 1', en='Sure. **What about** asking for a later hotel check-in, too? Eva is expecting us tonight.', pt='Claro. Que tal pedir também um check-in mais tarde no hotel? A Eva está nos esperando hoje à noite.'),
  dict(who='Traveler 2', en='Good idea. **Would it be possible to** sit together on the new flight? I’ll ask.', pt='Boa ideia. Seria possível sentarmos juntos no novo voo? Vou perguntar.'),
  dict(who='Traveler 2', en='Good news! They gave us free snacks, and **I’d like to change** nothing else.', pt='Boas notícias! Eles nos deram lanches de graça, e eu não quero mudar mais nada.'),
  dict(who='Traveler 1', en='Great. **I’ll take care of** the hotel message. Does the new flight land at six?', pt='Ótimo. Eu cuido da mensagem para o hotel. O novo voo pousa às seis?'),
  dict(who='Traveler 2', en='Yes, at six instead of four. **To sum up:** two hours late, seats together, snacks.', pt='Sim, às seis em vez de quatro. Resumindo: duas horas de atraso, assentos juntos, lanches.'),
  dict(who='Traveler 1', en='Perfect. **Let’s** text Eva now, so she isn’t worried.', pt='Perfeito. Vamos mandar mensagem para a Eva agora, para ela não se preocupar.')])

PAGES = [
 dict(t='rl_open', stage='warm', title='A2 Final Mission', pt='Missão final do A2', level='A2',
  unit=dict(unit(6), map=UMAP),
  situation=dict(text='You and a friend are at the airport. Your flight is delayed, a friend is waiting for you at the destination, and you must talk to the airline, plan what to do and send a clear update. This is the final mission of A2.', scene='airport', tod='day', cast=['Mia', 'Ken', 'Eva']),
  goal='By the end of the class you can meet, plan, ask for help, solve a travel problem and negotiate a solution in one connected conversation, with little support.',
  canDo=['Understand the problem and explain it', 'Suggest and negotiate a plan with a partner', 'Ask staff politely for a solution', 'Summarize the new plan and inform someone'],
  success=['I explain the problem.', 'I suggest and negotiate.', 'I ask politely for a solution.', 'I sum up and confirm the plan.'],
  think='What is the hardest part of solving a problem while traveling: understanding, asking, or staying calm?',
  teach=T('Abrir a missão final da unidade A2: uma situação integrada, com poucos apoios.',
   solo=['Leia o objetivo em voz alta e peça que o estudante diga o que já consegue fazer em inglês depois do A2.', 'Pergunte “Think about it” antes de mostrar qualquer expressão.'],
   group=['Cada estudante cita uma coisa que aprendeu no A2 e que usaria numa viagem.', 'Mostre os 4 critérios de sucesso: é a missão final da unidade.'],
   extra=['What was the biggest progress you made in A2?', 'What would you like to practice in B1?'],
   support=['Aceite respostas curtas ou em português na primeira rodada e reformule em inglês.'])),
 warm('Spaced review of A2: planning, requests, problems and presentations. Ask: Which A2 situation did you enjoy most?',
  [('Tell me about a trip you took or want to take.', 'Fale de uma viagem que fez ou quer fazer.', ['I went to…', 'I’d like to go to…', 'By plane.']),
   ('What do you do when something goes wrong on a trip?', 'O que você faz quando algo dá errado numa viagem?', ['I ask for help.', 'I stay calm.', 'I call my friend.']),
   ('What can you do in English now that you couldn’t do before?', 'O que você consegue fazer em inglês agora que não conseguia antes?', ['I can order food.', 'I can ask for help.', 'I can write a message.'])],
  'Retomar o A2 inteiro e celebrar o progresso antes da missão.', ['What was your favorite A2 lesson?', 'Which expression is now natural for you?'],
  [('I have travel to Italy.', 'I traveled to Italy. / I have been to Italy.'), ('My flight was delay.', 'My flight was delayed.')], ['Ofereça as respostas-modelo (chips) e peça apenas que escolham uma.']),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Integrated mission: a trip with a problem to solve',
  intro='Airports run on information: boards, announcements, desks and apps. Look and guess before you read.',
  cards=[dict(vis='prop:airplane', en='Delays happen', pt='Atrasos acontecem', note='Flight information is shown on boards and apps, and staff can explain your options.'),
         dict(vis='prop:suitcase', en='Be specific and calm', pt='Seja específico e calmo', note='Giving your flight and time helps staff find a solution quickly.'),
         dict(vis='prop:telephone', en='Tell the people waiting', pt='Avise quem está esperando', note='A short message with the new time avoids worry.')],
  qs=[dict(q='Where can you check flight information?', pt='Onde você pode ver informações do voo?', levels=dict(A1='On the board.', A2='On the board, on an app or at the airline desk.', B1='Boards, apps and announcements show gates and times, and the desk can confirm details.', B2='Airport screens, the airline app and desk staff are the usual sources, and they may differ, so it helps to confirm.')),
      dict(q='What can you ask at the airline desk?', pt='O que você pode perguntar no balcão da companhia?', levels=dict(A1='What time is my flight?', A2='Could you tell me my options? Would it be possible to change my flight?', B1='You can ask about a new flight, seat changes or help with a hotel connection.', B2='You can ask what options exist, and politely explain your constraints so the staff can propose a solution.')),
      dict(q='Why is it useful to send a short update?', pt='Por que é útil mandar uma atualização curta?', levels=dict(A1='So people know.', A2='So the person waiting knows the new time.', B1='A short message with the new arrival time avoids worry and lets others adjust.', B2='A concise update lets others adapt their plans and shows consideration.'))],
  compare='In Brazil, people often ask someone at the airport informally, and the answer depends on the person. In many English-speaking airports, polite, specific questions to the airline desk (“Could you tell me my options?”) are common. How do you ask for help when traveling?',
  teach=T('Ativar o contexto cultural da missão: informação, pedido educado e atualização.',
   solo=['Mostre os 3 cartões e peça hipóteses antes de explicar.', 'Peça que o estudante diga o que faria se o voo atrasasse.'], group=['Cada estudante escolhe um cartão e explica em uma frase.', 'Pergunte “Do you agree?” entre colegas.'],
   answers=['Q1: painel, app, balcão.', 'Q2: Could you tell me my options? / Would it be possible to…?', 'Q3: avisar o novo horário a quem espera.'], extra=['Have you ever had a delayed flight?', 'Who do you text when you are late?'],
   support=['Use as respostas do nível A1 como andaime e peça que repitam.'], stretch=['B2: explique como pedir uma solução quando o atraso já fez você perder uma conexão.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='airport', tod='day', cast=['Mia', 'Ken', 'Eva']),
  pass1=dict(q='What is the main problem?', pt='Qual é o problema principal?', opts=['The flight is delayed', 'The luggage is lost', 'The passport is missing'], ans=0),
  pass2=dict(tasks=[dict(label='How late is the flight?', ans='two hours'), dict(label='Who is waiting at the destination?', ans='Eva'), dict(label='Ken goes to the…', ans='airline desk'), dict(label='Free things from the airline', ans='snacks'), dict(label='New landing time', ans='six')]),
  teach=T('Compreender a situação antes de ver o texto: ideia principal e depois 5 informações.',
   solo=['Esconda o texto. 1ª escuta: só a ideia principal.', '2ª escuta: atraso, quem espera, para onde Ken vai, o que recebem e horário novo.', 'Mostre o texto só depois da 2ª escuta.'], group=['Escuta coletiva; duplas anotam as respostas antes de revelar.', 'Compare as respostas entre as duplas e só então mostre o texto.'],
   answers=['Pass 1: the flight is delayed.', 'Pass 2: two hours · Eva · airline desk · snacks · six.'], extra=['Who solves the problem? How?', 'Are Mia and Ken calm? How do you know?'],
   support=['Use o botão “Slow” na 2ª escuta.', 'Pause depois de cada fala se necessário.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='How late is the flight?', opts=['Two hours', 'Twenty minutes', 'One day'], ans=0), dict(q='What does Ken do?', opts=['He talks to the airline desk', 'He buys a new ticket', 'He goes home'], ans=0), dict(q='What does Ken ask for on the new flight?', opts=['Seats together', 'A bigger bag', 'A window seat for Mia'], ans=0), dict(q='What do Mia and Ken do at the end?', opts=['Text Eva', 'Call a taxi', 'Cancel the trip'], ans=0)],
  retell=dict(prompt='Retell the conversation in your own words, at your level.', starters=['Their flight is…', 'Ken goes to…', 'The airline gives them…', 'At the end, they…']),
  teach=T('Ler o diálogo, perceber os chunks de várias situações e recontar.',
   solo=['O estudante lê o papel da Mia; você lê o do Ken.', 'Peça que reconte a conversa no nível que conseguir.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia: uma frase por estudante.'],
   answers=['Two hours · talks to the airline desk · seats together · text Eva'], extra=['Which part is a request? Which part is a summary?', 'What would YOU ask the desk?'],
   errors=[('The flight is delay.', 'The flight is delayed.'), ('Would it be possible sit together?', 'Would it be possible to sit together?')], support=['Mostre a tradução (botão PT) depois da 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[dict(en='Could you tell me…?', pt='Você poderia me dizer…?', use='Ask staff for information.', reg='polite', alt='Also: **Could you tell me my options?**', pri=True),
         dict(en='Would it be possible to…?', pt='Seria possível…?', use='Ask for a change or a favor.', reg='formal', pri=True),
         dict(en='What about…?', pt='Que tal…?', use='Suggest an idea to your partner.', reg='neutral', alt='Also: **We could…**', pri=True),
         dict(en='I’ll take care of…', pt='Eu cuido de…', use='Take responsibility for a task.', reg='neutral', pri=True),
         dict(en='To sum up, …', pt='Resumindo…', use='Confirm the final plan.', reg='neutral', pri=True),
         dict(en='Our flight is delayed.', pt='Nosso voo está atrasado.', use='Explain the problem.', reg='neutral'),
         dict(en='I’d like to change…', pt='Eu gostaria de mudar…', use='Ask for a change.', reg='polite'),
         dict(en='Good news!', pt='Boas notícias!', use='Introduce a positive update.', reg='informal')],
  discover=dict(fns=['Asking staff', 'Suggesting', 'Taking responsibility', 'Summing up'],
   items=[dict(en='Could you tell me my options?', fn='Asking staff'), dict(en='What about a later check-in?', fn='Suggesting'), dict(en='I’ll take care of the hotel message.', fn='Taking responsibility'), dict(en='To sum up, we land at six.', fn='Summing up'), dict(en='Would it be possible to sit together?', fn='Asking staff')]),
  note='This is the A2 final mission: choose the five ★ expressions you want to use without notes.',
  teach=T('Retomar os chunks do A2 e escolher 5 para uso sem consulta.',
   solo=['Pergunte “Which lesson did this come from?” antes de dar o significado.', 'Peça um exemplo próprio para cada ★.'], group=['Cada estudante escolhe a expressão mais difícil e explica quando usa.', 'Compare em duplas: qual expressão vocês esquecem mais?'],
   answers=['Asking staff · Suggesting · Taking responsibility · Summing up · Asking staff'], extra=['Which expression helps you the most when you travel?'], errors=[('Could you say me…?', 'Could you tell me…?')], support=['Trabalhe só 3 das expressões ★ na primeira rodada.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Asking staff', formula='**Could you** + verb? · **Would it be possible to** + verb?', ex=['Could you tell me my options?', 'Would it be possible to sit together?', 'Could you check the next flight?'], main=True),
            dict(name='Suggest and take charge', formula='**What about** + noun/-ing? · **I’ll take care of** + noun', ex=['What about a later check-in?', 'I’ll take care of the hotel message.', 'What about asking the desk?'], main=True),
            dict(name='Explain a problem', formula='**Our flight is** + adjective / **I’d like to change** + noun', ex=['Our flight is delayed.', 'I’d like to change my seat.']),
            dict(name='Sum up', formula='**To sum up,** + plan', ex=['To sum up, we land at six.', 'To sum up, seats together and free snacks.'])],
  swap=dict(frame='Would it be possible to {action} {detail}?', tpt='Seria possível {action} {detail}?',
   slots=[dict(k='action', label='Action', opts=[dict(en='change our flight', pt='mudar nosso voo'), dict(en='sit together', pt='sentar juntos'), dict(en='get a later check-in', pt='fazer um check-in mais tarde'), dict(en='speak to a manager', pt='falar com um gerente')]),
          dict(k='detail', label='Detail', opts=[dict(en='today', pt='hoje'), dict(en='for tonight', pt='para esta noite'), dict(en='without extra cost', pt='sem custo extra')])]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['Could you tell me my options?', 'Could you please inform me of the available options?'], ['Our flight is delayed.', 'We have been informed that our flight is delayed.'], ['I’ll take care of it.', 'I will handle this and update you.'], ['To sum up, we land at six.', 'In summary, our new arrival time is 6:00 p.m.']],
   note='These are differences of context and register, not absolute rules.'),
  teach=T('Integrar os padrões principais do A2: pedir a funcionários, sugerir e resumir.',
   solo=['Mostre o padrão DENTRO do diálogo (grife os chunks).', 'Use “Swap the words”: toque em cada peça e peça que o estudante diga a frase completa.', 'Compare spoken × written em 2 exemplos.'], group=['Troca em cadeia: cada estudante muda UMA peça e o próximo repete a frase.', 'Em pares: um escolhe as peças, o outro fala.'],
   answers='Padrão 01/02 são o foco; 03/04 são expansão para quem avançar rápido.', extra=['Change one word and say the new sentence.', 'Which pattern is hardest under pressure?'],
   errors=[('Could you tell me where is the gate?', 'Could you tell me where the gate is?'), ('Would it be possible sit?', 'Would it be possible to sit?'), ('Our flight is delay.', 'Our flight is delayed.')], support=['Fique só com Could you… e What about… na primeira rodada.'], stretch=['Pedir uma solução e explicar a restrição: I have a connection at six, so would it be possible to…?'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Word stress in travel words', tip='In English, one syllable in a word is stronger: AIRport, deLAYED, reserVAtion. Stress the right syllable and people understand you at once. The goal is to be clear, not to remove your accent.',
  items=[dict(say='airport, ticket, gate', linked='AIR-port, TI-cket, GATE', ipa='/ˈɛrpɔːrt/', rhythm='OoOoO'), dict(say='delayed, reservation', linked='de-LAYED, re-ser-VA-tion', ipa='/dɪˈleɪd/', rhythm='oOoooOo'), dict(say='passenger, information', linked='PAS-sen-ger, in-for-MA-tion', ipa='/ˈpæsɪndʒər/', rhythm='OooOoooOo')],
  identify=[dict(q='Which one do you hear?', opts=['deLAYED', 'DElayed', 'delayED'], ans=0, say='delayed'), dict(q='Which one do you hear?', opts=['inforMAtion', 'INformation', 'informaTION'], ans=0, say='information')],
  own=dict(prompt='Write three travel words you use often and mark the strong syllable.', criteria='Say each word twice. Could your partner hear the stressed syllable?'),
  teach=T('UM só fenômeno: acento de palavra (sílaba forte) em vocabulário de viagem.',
   solo=['3 passagens: escutar e identificar → reproduzir ritmo → usar em palavras próprias.', 'Peça que o estudante bata palmas na sílaba forte.'], group=['Coro, depois duplas; circule ouvindo.', 'Cada estudante diz 3 palavras de viagem com a sílaba forte marcada.'],
   answers=['Identify 1: deLAYED · Identify 2: inforMAtion'], errors=[('PASsenger com acento no fim.', 'PASsenger: acento na primeira sílaba.'), ('reservation com acento no início.', 'reserVAtion: acento na terceira sílaba.')], support=['Reduza a velocidade e conte as batidas em voz alta.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    mcq('1. You want to ask the airline desk for information.', ['Could you tell me my options?', 'You tell me options.', 'Could you telling options?'], 0, 'Could you + base verb is polite.'),
    mcq('2. You ask for seats together.', ['Would it be possible to sit together?', 'Is possible sit together?', 'I sit you together.'], 0, 'Would it be possible + to + verb.'),
    mcq('3. A friend is waiting for you at the hotel.', ['I’ll take care of the message.', 'I take care message of.', 'I’m caring the message.'], 0, 'I’ll take care of + noun.'),
    mcq('4. You want to confirm the final plan.', ['To sum up, we land at six and sit together.', 'Sum up, six landing we.', 'The final is six.'], 0, 'To sum up, + plan.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    gap('Our flight is ___ by two hours.', 'delayed', 'delayed describes the flight.', ['delayed', 'delay', 'delaying']),
    gap('___ about a later check-in?', 'What', 'What about + noun.', ['What', 'How', 'Which']),
    swp('Make it polite:', 'Tell me my options.', ['Could you tell me my options?', 'Could you tell me my options, please?'], 'Could you tell me my options, please?', 'Could you + verb is polite.'),
    swp('Ask to change:', 'my seat', ['I’d like to change my seat.', 'I’d like to change my seat, please.'], 'I’d like to change my seat.', 'I’d like to change + noun.'),
    rep('We can offer you a flight at six. Is that okay?', 'Choose the best reply.', ['Yes, that works. Would it be possible to sit together?', 'Six is me okay yes.', 'I am a flight six.'], 0, 'Accept and add a polite request.')])],
  teach=T('Do controlado ao guiado: revisar funções do A2 antes da missão final.',
   solo=['Peça que o estudante justifique cada resposta.', 'Se acertar rápido, peça a versão mais informal ou mais formal.'], group=['Resolvam em duplas e comparem antes de revelar.', 'Equipes: ponto por resposta justificada.'],
   answers=['1: Could you tell me my options? · 2: Would it be possible to sit together? · 3: I’ll take care of the message. · 4: To sum up, we land at six…', 'Gap: delayed · What · Could you tell me my options, please? · I’d like to change my seat. · Yes, that works. Would it be possible…?'], extra=['Say each correct answer aloud with stress on the key words.'],
   errors=[('I’d like change my seat.', 'I’d like to change my seat.'), ('Could you to tell me?', 'Could you tell me?')], support=['Ofereça o banco de palavras (chips) nas lacunas.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — a delayed flight',
  brief=dict(teacher='You are the airline desk agent (add a new problem each time!).', student='Your flight is delayed. Explain it, ask for options, negotiate and summarize the new plan.'),
  orders=['A delayed flight and a friend waiting for you', 'A seat change for a trip with a friend', 'A missed connection and a hotel check-in problem'],
  complications=['The next flight is full.', 'The agent offers a flight a day later.', 'The airline can’t change your seats.', 'Your phone battery is low and you must write a short message.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['Could you tell me…?', 'Would it be possible to…?', 'I’ll take care of…', 'To sum up…']), dict(label='Keywords', desc='Only the keywords', help=['delay', 'options', 'seats', 'hotel', 'summary'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I explain the problem.', 'I ask politely for a solution.', 'I negotiate.', 'I sum up the new plan.'],
  teach=T('Simulação com complicação inesperada e três rodadas com menos apoio.',
   solo=['Combine o cenário com uma viagem real ou imaginária do aluno.', 'Rodada 1: com chunks. Rodada 2: só palavras-chave. Rodada 3: sem roteiro.', 'Meta de fala: 60–70% do tempo para o estudante. Anote 2–3 correções para a devolutiva.'],
   extra=['What if there is no other flight today?'], errors=[('I need to go now, do something.', 'Could you tell me my options? I need to arrive today, if possible.')], support=['Volte à rodada 1 se travar; peça que repita só a primeira frase.'], stretch=['Negocie duas coisas ao mesmo tempo: o horário e um hotel.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Explain the problem', min=3, task='Your flight is delayed. Explain it to your partner and suggest a plan.', hint='Our flight is delayed. / What about…?'), dict(title='Ask staff', min=3, task='Ask the airline desk for options and a change.', hint='Could you tell me…? / Would it be possible to…?'), dict(title='Negotiate', min=3, task='The desk offers something you don’t like. Negotiate.', hint='I’d rather… / Is there another option?'), dict(title='Sum up', min=2, whole=True, task='Whole group: each pair summarizes the final plan.', hint='To sum up, …')],
  infogap=dict(title='Flight options', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='You are the passenger', task='You know your first flight. Ask the agent about the options.', rows=[dict(k='Your flight', v='Flight 218, 2:00 p.m.'), dict(k='Option 1', v=''), dict(k='Option 2', v=''), dict(k='Hotel voucher', v='')]),
   b=dict(title='You are the agent', task='You know the options. Ask the passenger about the flight.', rows=[dict(k='Your flight', v=''), dict(k='Option 1', v='Flight 240, 6:15 p.m.'), dict(k='Option 2', v='Flight 305, tomorrow 8:00 a.m.'), dict(k='Hotel voucher', v='only for option 2')])),
  teach=T('Fluência por repetição de funções diferentes com informações novas a cada rodada.',
   group=['Troque os pares a cada rodada (A+B / C+D → A+C / B+D → A+D / B+C → grupo todo). Com 6 estudantes, três duplas simultâneas.', 'Sem salas simultâneas: interações sequenciais enquanto uma dupla apresenta.', 'Responsabilidade individual: cada aluno faz ≥1 pedido, ≥1 sugestão e ≥1 resumo.'],
   answers=['Info gap: A tem o voo 218 às 14h; B tem opção 1 (voo 240, 18h15), opção 2 (voo 305, amanhã 8h) e hotel só na opção 2. Cada um completa perguntando.'], extra=['What time is the first option?', 'Is the hotel included?'],
   errors=[('What hour is the flight 240?', 'What time is flight 240?'), ('In the tomorrow morning.', 'Tomorrow morning.')], support=['Entregue frases-modelo no chat da turma.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — the A2 trip',
  goal='Each group completes a connected trip mission in English: meet and plan, ask for help, solve a problem, negotiate and sum up.',
  missions=[dict(who='A', role='Travelers and airline agent', mission='Your flight is delayed and you will miss a dinner. Plan with your partner, ask the agent for options and choose the best one.', constraint='Use “What about…?”, “Could you tell me…?” and “To sum up…”.', start='Our flight is delayed. What about…?'),
            dict(who='B', role='Travelers and hotel desk', mission='You arrive late at a hotel. Ask for a later check-in, a quiet room and a taxi, and agree on the extra cost.', constraint='Use “Would it be possible to…?” and “I’d rather…”.', start='Hello, we’re arriving late. Would it be possible to…?'),
            dict(who='C', role='Friends', mission='A friend is waiting for you. Send a message with the new time, the reason and what you will do.', constraint='Use “I’ll take care of…” and finish with a summary.', start='Hi Eva! Quick update: our flight…')], min=11,
  success=['Explain the problem.', 'Suggest and negotiate.', 'Ask politely for a solution.', 'Sum up and confirm the plan.'],
  teach=T('Realizar algo com o inglês: missão integrada que usa o A2 inteiro com poucos apoios.',
   group=['Cada grupo recebe papéis, restrição e missão. Alterne viajantes e atendente.', 'Progressão: 1ª rodada com frases de apoio, 2ª só palavras-chave, 3ª sem roteiro.', 'Observe e anote 2–3 correções prioritárias; devolutiva e celebração do A2 no fim.'],
   answers=['Modelo: “Our flight is delayed. What about asking the desk?” → “Could you tell me my options?” → “I’d rather leave tonight.” → “To sum up, flight 240 at 6:15 p.m.”'], extra=['What if the agent says no?'], support=['Dê o início de frase (“Start with”) em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short message to a friend who is waiting for you. Explain the delay, say what you asked the airline and give the new plan.',
  steps=['Greeting and problem', 'What you asked', 'New plan', 'Closing'],
  model='Hi Eva! Quick update: **our flight is delayed** by two hours. **I asked** the desk **if it would be possible to** sit together, and they said yes. **To sum up:** we land at six, not four. **I’ll take care of** the hotel message. See you soon!',
  checklist=['I greeted my friend and explained the problem.', 'I said what I asked for.', 'I gave the new plan (time).', 'I used To sum up and closed politely.'],
  tip='Fix only 2–3 priority points. Show a more natural way to say the same idea instead of rewriting everything.', fix=dict(n=3),
  teach=T('Produção escrita curta que integra explicar, pedir e resumir.',
   solo=['Peça a mensagem; corrija 2–3 pontos prioritários e mostre uma forma mais natural.'], group=['Cada estudante escreve; depois troquem os textos entre colegas e corrijam em duplas.'],
   extra=['Add a plan B if the new flight changes again.'], errors=[('We land at six, no at four.', 'We land at six, not at four.'), ('I asked if it was possible sit.', 'I asked if it would be possible to sit.')], support=['Dê o modelo e peça só para trocar os dados.'])),
 feedback('Example: You explained the problem, asked politely and summarized the plan.', 'Example: Put the stress on the right syllable: deLAYED, inforMAtion.', 'Example: In B1, handle a longer problem and explain your reasons.', 'Use a rubrica para fechar o A2 e indicar o foco do B1.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❓', name='Ask staff', prompt='Without notes: ask the airline desk for your options.', model='Could you tell me my options?'), dict(ic='💬', name='Negotiate', prompt='The agent offers tomorrow’s flight. You prefer tonight.', model='I’d rather leave tonight, if that’s possible.'), dict(ic='⭐', name='Sum up', prompt='Sum up the new plan: flight at 6:15, seats together.', model='To sum up, we leave at 6:15 and sit together.')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 60–90 second audio solving a travel problem (delay, hotel or lost item).', 'Write a short message to a friend with a new plan.', 'Review your five favorite A2 expressions and write two examples for each.', 'Make a list of three things you want to practice in B1.']),
  spaced=dict(next=['Could you tell me…?', 'Would it be possible to…?', 'I’ll take care of…'], week=['What about…?', 'I’d rather…', 'To sum up…'], unit=['Plan · ask · solve · negotiate · sum up']),
  teach=T('Toda aula termina com uma produção observável. Feche o A2 com o que o aluno consegue fazer agora.', solo=['Sem consultar as anotações: pedir informação, negociar e resumir.'], group=['Exit challenge individual; cada um diz uma coisa que conseguiu fazer hoje e uma meta para o B1.'],
   answers=['Could you tell me my options? · I’d rather leave tonight, if that’s possible. · To sum up, we leave at 6:15 and sit together.'], extra=['Revisão espaçada: retomar no início do B1 e depois de uma semana.'])),
 levels([('Flight late. Help, please.', None), ('Our flight is delayed. Could you tell me my options? What about a later flight?', 'Explain, ask and suggest.'), ('Since the flight is delayed, we’d like to know whether there’s a later one that lands tonight, because a friend is waiting.', None), ('Given the delay, I was hoping you could rebook us on the earliest available flight and, if possible, arrange a hotel voucher.', None), ('I appreciate that these things happen, but I’d be grateful if you could find us a flight that gets us in tonight.', None), ('I fully understand the constraints you’re under; nonetheless, I’d welcome any arrangement that spares us an overnight stay.', None)], 'Mostrar a progressão A1→C2 e apontar os próximos passos no B1.')
]

LESSON = dict(n=100, topic='A2 Final Mission', level='A2', title='A2 Final Mission', pt='Missão final do A2', unit=unit(6), minutes=60, cast=['Mia', 'Ken', 'Eva'], scene='airport', tod='day', plan=PLAN, dialog=DIALOG, pages=PAGES)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
