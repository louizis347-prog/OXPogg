#!/usr/bin/env python3
"""Aula 95 · Planning a trip together (A2, 60 min). Gera data/v3/095.json."""
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
 speakers={'Planner': {'name': 'Eva'}, 'Friend': {'name': 'Noah'}},
 lines=[
  dict(who='Planner', en='**Let’s** plan our weekend trip. Where do you want to go?', pt='Vamos planejar nossa viagem de fim de semana. Aonde você quer ir?'),
  dict(who='Friend', en='**What about** Chicago? **We could** take the train on Friday night.', pt='Que tal Chicago? A gente poderia pegar o trem na sexta à noite.'),
  dict(who='Planner', en='Chicago sounds fun, but hotels are expensive. **We could** stay with my cousin instead.', pt='Chicago parece divertido, mas hotéis são caros. A gente poderia ficar com meu primo.'),
  dict(who='Friend', en='That would save money. **I’d rather** have my own room, though.', pt='Isso economizaria dinheiro. Mas eu prefiro ter meu próprio quarto.'),
  dict(who='Planner', en='Fair enough. **What about** a cheap hotel near the station?', pt='Justo. Que tal um hotel barato perto da estação?'),
  dict(who='Friend', en='Good idea. Should we leave Friday after work or Saturday morning?', pt='Boa ideia. Devemos sair na sexta depois do trabalho ou no sábado de manhã?'),
  dict(who='Planner', en='**I’d rather** leave Friday night, so we have two full days there.', pt='Eu prefiro sair na sexta à noite, para termos dois dias inteiros lá.'),
  dict(who='Friend', en='Perfect. **Let’s** book the tickets today, before the price goes up.', pt='Perfeito. Vamos comprar as passagens hoje, antes de o preço subir.')])

PAGES = [
 dict(t='rl_open', stage='warm', title='Planning a Trip Together', pt='Planejar uma viagem juntos', level='A2',
  unit=dict(unit(1), map=UMAP),
  situation=dict(text='You and a friend want to take a short trip. You have different ideas about the place, the money and the day to leave. You make suggestions, say what you prefer and agree on a plan.', scene='office', tod='day', cast=['Eva', 'Noah']),
  goal='By the end of the class you can suggest ideas, react to your partner’s ideas, say what you prefer and reach a decision together — politely and with reasons.',
  canDo=['Suggest a plan: Let’s… / What about…?', 'Offer an option: We could…', 'Say what you prefer: I’d rather…', 'Agree on a plan and fix the details (day, place, money)'],
  success=['I make a suggestion.', 'I give a reason.', 'I say what I prefer, politely.', 'We agree on a final plan.'],
  think='When you plan something with friends, who usually decides? How do you say “não, prefiro outra coisa” without sounding rude?',
  teach=T('Abrir a aula pela situação real: planejar algo junto exige negociar, não só dar ordens.',
   solo=['Leia o objetivo em voz alta e peça que o estudante diga com as próprias palavras o que vai fazer hoje.', 'Pergunte “Think about it” antes de mostrar qualquer expressão.'],
   group=['Cada estudante diz um lugar para uma viagem curta.', 'Mostre os 4 critérios de sucesso: é a missão final da aula.'],
   extra=['Where did you go on your last trip?', 'Do you prefer planning everything or deciding on the way?'],
   support=['Aceite respostas curtas ou em português na primeira rodada e reformule em inglês.'])),
 warm('Review: requests and routines from earlier A2 lessons. Ask: What do you usually do on weekends?',
  [('What did you do last weekend?', 'O que você fez no fim de semana passado?', ['I stayed home.', 'I went to…', 'I met some friends.']),
   ('Where would you like to go for a short trip?', 'Aonde você gostaria de ir em uma viagem curta?', ['I’d like to go to…', 'Maybe the beach.', 'Somewhere quiet.']),
   ('Do you travel with friends, family or alone?', 'Você viaja com amigos, família ou sozinho?', ['With my family.', 'With friends.', 'Alone, usually.'])],
  'Entrar no idioma e ativar passado simples e preferências antes de negociar planos.', ['What was the best trip you ever took?', 'Who plans the trips in your group of friends?'],
  [('I go to the beach last weekend.', 'I went to the beach last weekend.'), ('I prefer go by bus.', 'I prefer to go by bus. / I prefer going by bus.')], ['Ofereça as respostas-modelo (chips) e peça apenas que escolham uma.']),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Negotiating plans',
  intro='In the United States, friends usually make plans by offering ideas, not by giving orders. Look and guess before you read.',
  cards=[dict(vis='prop:map', en='Suggest, don’t order', pt='Sugerir, não mandar', note='“We could…” and “What about…?” leave room for the other person to answer.'),
         dict(vis='prop:train', en='“I’m flexible.”', pt='“Eu sou flexível.”', note='People often say “Either works for me” to show they will adapt.'),
         dict(vis='obj:coin', en='Talking about money openly', pt='Falar de dinheiro abertamente', note='Friends often discuss the budget early: “Let’s keep it under $200.”')],
  qs=[dict(q='How do friends in the USA usually suggest a plan?', pt='Como amigos nos EUA costumam sugerir um plano?', levels=dict(A1='Let’s go to the beach.', A2='They say “What about…?” or “We could…”.', B1='They offer ideas softly, like “We could try…”, and wait for a reaction.', B2='Suggestions are usually phrased as options so that nobody feels pressured to accept.')),
      dict(q='How can you say “no” to an idea politely?', pt='Como dizer “não” a uma ideia com educação?', levels=dict(A1='I’d rather go to the park.', A2='“I’d rather…” plus a reason: it’s too expensive.', B1='Say something positive first, then your preference: “Good idea, but I’d rather…”.', B2='Acknowledge the idea, give a reason and propose an alternative so the conversation keeps moving.')),
      dict(q='Why do people talk about money and dates early?', pt='Por que as pessoas falam de dinheiro e datas logo no início?', levels=dict(A1='Money. Day. Plan.', A2='So nobody is surprised later.', B1='It avoids misunderstandings and lets everyone decide if they can come.', B2='Settling budget and timing first keeps the group aligned and prevents awkward surprises.'))],
  compare='In Brazil, a plan often starts as “vamos ver” and is decided at the last minute. Among many Americans, a quick “What day works for you?” is normal. How do you decide plans with your friends?',
  teach=T('Ativar o contexto cultural: sugerir e negociar com suavidade.',
   solo=['Mostre os 3 cartões e peça hipóteses antes de explicar.', 'Peça que o estudante compare com a forma como combina planos com amigos no Brasil.'], group=['Cada estudante escolhe um cartão e explica em uma frase.', 'Pergunte “Do you agree?” entre colegas.'],
   answers=['Q1: What about… / We could…', 'Q2: I’d rather… + reason, depois de algo positivo.', 'Q3: para ninguém ser surpreendido e para alinhar o grupo.'], extra=['Is it rude to say no to a friend’s idea in your culture?', 'How far ahead do you plan trips?'],
   support=['Use as respostas do nível A1 como andaime e peça que repitam.'], stretch=['B2: explique como negociar um plano quando duas pessoas querem coisas opostas.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='office', tod='day', cast=['Eva', 'Noah']),
  pass1=dict(q='What are the two people doing?', pt='O que as duas pessoas estão fazendo?', opts=['Planning a weekend trip', 'Applying for a job', 'Choosing a restaurant'], ans=0),
  pass2=dict(tasks=[dict(label='Destination', ans='Chicago'), dict(label='Transport', ans='train'), dict(label='Where they finally decide to stay', ans='cheap hotel', alt=['hotel']), dict(label='When they leave', ans='Friday night', alt=['friday'])]),
  teach=T('Compreender a situação antes de ver o texto: ideia principal e depois 4 informações.',
   solo=['Esconda o texto. 1ª escuta: só a ideia principal.', '2ª escuta: destino, transporte, hospedagem e dia de saída.', 'Mostre o texto só depois da 2ª escuta.'], group=['Escuta coletiva; duplas anotam as respostas antes de revelar.', 'Compare as respostas entre as duplas e só então mostre o texto.'],
   answers=['Pass 1: planning a weekend trip.', 'Pass 2: Chicago · train · cheap hotel · Friday night.'], extra=['Who wants to save money? Who wants more privacy?', 'Do they agree quickly? How do you know?'],
   support=['Use o botão “Slow” na 2ª escuta.', 'Pause depois de cada fala se necessário.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='Why doesn’t Eva want to book a hotel at first?', opts=['Hotels are expensive', 'She dislikes trains', 'She has no time'], ans=0), dict(q='What does Noah say about staying with the cousin?', opts=['He’d rather have his own room', 'He loves the idea', 'He doesn’t know her cousin’s name'], ans=0), dict(q='When do they decide to leave?', opts=['Friday night', 'Saturday morning', 'Sunday evening'], ans=0), dict(q='What do they decide to do today?', opts=['Book the tickets', 'Call the cousin', 'Pack their bags'], ans=0)],
  retell=dict(prompt='Retell the conversation in your own words, at your level.', starters=['They want to…', 'Noah suggests…', 'Eva thinks the hotels…', 'In the end, they decide…']),
  teach=T('Ler o diálogo, perceber os chunks e recontar.',
   solo=['O estudante lê o papel do Noah; você lê o da Eva.', 'Peça que reconte a conversa no nível que conseguir.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia: uma frase por estudante.'],
   answers=['Hotels are expensive · he’d rather have his own room · Friday night · book the tickets'], extra=['Who is more flexible, Eva or Noah?', 'What would YOU suggest instead of Chicago?'],
   errors=[('I would rather to leave Friday.', 'I’d rather leave Friday.'), ('What about go to Chicago?', 'What about going to Chicago?')], support=['Mostre a tradução (botão PT) depois da 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[dict(en='Let’s…', pt='Vamos…', use='Make a suggestion that includes both of you.', reg='neutral', alt='Also: **Why don’t we…?**', pri=True),
         dict(en='What about…?', pt='Que tal…?', use='Offer an idea as a question, so the other person can answer.', reg='neutral', alt='Also: **How about…?**', pri=True),
         dict(en='We could…', pt='A gente poderia…', use='Offer an option without forcing it.', reg='polite', alt='Direct: **Let’s…**', pri=True),
         dict(en='I’d rather…', pt='Eu preferiria… / Prefiro…', use='Say what you prefer, politely.', reg='polite', alt='Simple: **I prefer…**', pri=True),
         dict(en='That sounds good.', pt='Parece bom.', use='Agree with an idea.', reg='neutral'),
         dict(en='Fair enough.', pt='Justo / Faz sentido.', use='Accept the other person’s point.', reg='informal'),
         dict(en='Either works for me.', pt='Qualquer um serve para mim.', use='Show you are flexible.', reg='neutral'),
         dict(en='Should we…?', pt='Devemos…?', use='Ask the other person to help you decide.', reg='neutral')],
  discover=dict(fns=['Suggesting', 'Offering an option', 'Saying a preference', 'Agreeing'],
   items=[dict(en='Let’s book the tickets today.', fn='Suggesting'), dict(en='We could take the train.', fn='Offering an option'), dict(en='I’d rather leave Friday night.', fn='Saying a preference'), dict(en='Fair enough.', fn='Agreeing'), dict(en='What about a cheap hotel?', fn='Suggesting')]),
  note='Choose the four ★ expressions and use them again and again today. The others help you understand and stretch.',
  teach=T('Escolher 4 chunks para uso repetido e descobrir a função de cada um.',
   solo=['Pergunte “When do you say it?” antes de dar o significado.', 'Compare Let’s… (direto) × We could… (suave) e peça um exemplo próprio.'], group=['Cada estudante escolhe a expressão que mais usaria e explica quando.', 'Compare em duplas: qual soa mais suave?'],
   answers=['Suggesting · Offering an option · Saying a preference · Agreeing · Suggesting'], extra=['Which one would you use with your boss? With a friend?'], errors=[('I rather go to the beach.', 'I’d rather go to the beach.')], support=['Trabalhe só 3 das expressões ★ na primeira rodada.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Suggesting', formula='**Let’s** + base verb / **What about** + noun or -ing?', ex=['Let’s book the tickets today.', 'What about a cheap hotel?', 'What about going on Friday?'], main=True),
            dict(name='Offering options', formula='**We could** + base verb', ex=['We could take the train.', 'We could stay with my cousin.', 'We could leave after work.'], main=True),
            dict(name='Saying what you prefer', formula='**I’d rather** + base verb (+ reason)', ex=['I’d rather have my own room.', 'I’d rather leave on Friday night.', 'I’d rather not drive at night.']),
            dict(name='Asking for a decision', formula='**Should we** + base verb + or …?', ex=['Should we leave Friday or Saturday?', 'Should we book a hotel?'])],
  swap=dict(frame='What about {place} {when}?', tpt='Que tal {place} {when}?',
   slots=[dict(k='place', label='Place', opts=[dict(en='Chicago', pt='Chicago'), dict(en='the beach', pt='a praia'), dict(en='a small town', pt='uma cidade pequena'), dict(en='the mountains', pt='as montanhas')]),
          dict(k='when', label='When', opts=[dict(en='this weekend', pt='neste fim de semana'), dict(en='next month', pt='no mês que vem'), dict(en='in the spring', pt='na primavera')])]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['What about Chicago?', 'Would you consider visiting Chicago?'], ['We could take the train.', 'One option would be to travel by train.'], ['I’d rather leave Friday.', 'I would prefer to depart on Friday.'], ['Sounds good. Let’s book it.', 'That sounds suitable. I will make the reservation.']],
   note='These are differences of context and register, not absolute rules: contractions are also common in informal writing.'),
  teach=T('Fixar 2 padrões principais (01 e 02); os outros são expansão. Usar a troca de palavras para variar a fala.',
   solo=['Mostre o padrão DENTRO do diálogo (grife os chunks).', 'Use “Swap the words”: toque em cada peça e peça que o estudante diga a frase completa.', 'Compare spoken × written em 2 exemplos.'], group=['Troca em cadeia: cada estudante muda UMA peça e o próximo repete a frase.', 'Em pares: um escolhe as peças, o outro fala.'],
   answers='Padrão 01/02 são o foco; 03/04 são expansão para quem avançar rápido.', extra=['Make it softer: Let’s go → We could go.', 'Change one word and say the new sentence.'],
   errors=[('What about to go to the beach?', 'What about going to the beach?'), ('We could to take the train.', 'We could take the train.'), ('I’d rather to stay home.', 'I’d rather stay home.')], support=['Fique só com What about… e We could… na primeira rodada.'], stretch=['Combinar sugestão + preferência + motivo: We could drive, but I’d rather take the train because it’s cheaper.'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Sentence stress', tip='In English, the important words (nouns, verbs, numbers) are stressed and the small words are weak. “What about Chicago?” sounds like “wha-da-BOUT CHI-ca-go”. The goal is to be clear and natural, not to remove your accent.',
  items=[dict(say='What about a cheap hotel?', linked='What-a-BOUT a CHEAP ho-TEL?', ipa='/wʌt əˈbaʊt/', rhythm='ooOoooO'), dict(say='We could take the train.', linked='We could TAKE the TRAIN.', ipa='/wi kəd/', rhythm='ooOoO'), dict(say='I’d rather leave on Friday night.', linked='I’d RA-ther LEAVE on FRI-day NIGHT.', ipa='/aɪd ˈræðər/', rhythm='oOooOoOoO')],
  identify=[dict(q='Which one do you hear?', opts=['We could take the TRAIN.', 'We could TAKE the train.', 'We COULD take the train.'], ans=0, say='We could take the train.'), dict(q='Which one do you hear?', opts=['I’d RATHer stay home.', 'I’d rather STAY home.', 'I’d rather stay HOME.'], ans=0, say='I’d rather stay home.')],
  own=dict(prompt='Write one suggestion and one preference for a trip you really want to take.', criteria='Say them twice: first flat, then with stress on the key words. Which one sounds more natural?'),
  teach=T('UM só fenômeno: acento da frase (palavras de conteúdo fortes, palavras pequenas fracas).',
   solo=['3 passagens: escutar e identificar → reproduzir ritmo e entonação → usar em frase com conteúdo próprio.', 'Peça que o estudante bata palmas nas sílabas fortes.'], group=['Coro, depois duplas; circule ouvindo.', 'Cada estudante cria uma frase própria com a sílaba forte marcada.'],
   answers=['Identify 1: We could take the TRAIN. · Identify 2: I’d RATHer stay home.'], errors=[('Acentuar todas as palavras igualmente.', 'Acentuar só as palavras de conteúdo.'), ('rather com “r” forte e /a/ aberto (rá-ther).', '/ˈræðər/ com “th” sonoro.')], support=['Reduza a velocidade e conte as batidas em voz alta.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    mcq('1. You want to suggest a trip to the beach, softly.', ['What about going to the beach?', 'You go to the beach.', 'Beach is you want?'], 0, 'What about + -ing is a friendly suggestion.'),
    mcq('2. Your friend wants Chicago, but you prefer the mountains.', ['Good idea, but I’d rather go to the mountains.', 'No. Chicago is bad.', 'I rather to mountains.'], 0, 'Positive first, then I’d rather + verb.'),
    mcq('3. Which sentence offers an option?', ['We could take a bus.', 'We take a bus not.', 'We could to take a bus.'], 0, 'We could + base verb.'),
    mcq('4. Your partner says: “Should we leave Friday or Saturday?” You don’t mind.', ['Either works for me.', 'I am no day.', 'Friday Saturday yes.'], 0, 'Either works for me shows you are flexible.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    gap('Let’s ___ the tickets today.', 'book', 'Let’s + base verb.', ['book', 'booking', 'to book']),
    gap('I’d ___ stay in a small hotel.', 'rather', 'I’d rather + base verb.', ['rather', 'prefer', 'like to']),
    swp('Make it softer with “We could”:', 'Let’s drive there.', ['We could drive there.', 'We could drive there, if you want.'], 'We could drive there.', 'We could… offers an option instead of giving a direct suggestion.'),
    swp('Say what you prefer, with a reason:', 'train / cheaper', ['I’d rather take the train because it’s cheaper.', 'I’d rather take the train, it’s cheaper.', 'I’d rather go by train because it’s cheaper.'], 'I’d rather take the train because it’s cheaper.', 'I’d rather + verb + because + reason.'),
    rep('Should we leave on Friday or on Saturday?', 'Choose the best reply.', ['I’d rather leave on Friday, if that’s okay.', 'I am leaving Friday, you not.', 'Yes, Friday or Saturday.'], 0, 'Answer the choice and show you are open to the other person.')])],
  teach=T('Do controlado ao guiado: completar, substituir e transformar antes da fala livre.',
   solo=['Peça que o estudante justifique cada resposta.', 'Se acertar rápido, peça a versão mais informal ou mais educada.'], group=['Resolvam em duplas e comparem antes de revelar.', 'Equipes: ponto por resposta justificada.'],
   answers=['1: What about going to the beach? · 2: Good idea, but I’d rather… · 3: We could take a bus. · 4: Either works for me.', 'Gap: book · rather · We could drive there. · I’d rather take the train because it’s cheaper. · I’d rather leave on Friday.'], extra=['Say each correct answer aloud with sentence stress.'],
   errors=[('I’d rather to go.', 'I’d rather go.'), ('What about we go?', 'What about going? / Why don’t we go?')], support=['Ofereça o banco de palavras (chips) nas lacunas.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — plan it together',
  brief=dict(teacher='You are the friend who wants a different plan (change the details during the scene!).', student='You want to take a short trip. Suggest a plan, say what you prefer and agree on the details.'),
  orders=['A weekend in a big city by train', 'A day at the beach with a small budget', 'A trip to see family, leaving after work'],
  complications=['Your friend wants a different destination.', 'The hotel is much more expensive than you thought.', 'Your friend can only leave on Saturday.', 'The train is full and you need another way to travel.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['Let’s…', 'What about…?', 'We could…', 'I’d rather…']), dict(label='Keywords', desc='Only the keywords', help=['place', 'day', 'money', 'prefer', 'decide'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I make a suggestion.', 'I give a reason.', 'I say what I prefer, politely.', 'We agree on a final plan.'],
  teach=T('Simulação com complicação inesperada e três rodadas com menos apoio.',
   solo=['Combine o cenário com a vida do estudante (um lugar que ele realmente quer visitar).', 'Rodada 1: com chunks. Rodada 2: só palavras-chave. Rodada 3: sem roteiro.', 'Meta de fala: 60–70% do tempo para o estudante. Anote 2–3 correções para a devolutiva.'],
   extra=['What if your friend says no to every idea?'], errors=[('No, I don’t want go there.', 'Good idea, but I’d rather go somewhere else.')], support=['Volte à rodada 1 se travar; peça que repita só a primeira frase.'], stretch=['Peça um plano para três pessoas com orçamentos diferentes.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='First ideas', min=3, task='Suggest a place for a weekend trip. Your partner reacts.', hint='Let’s… / What about…?'), dict(title='Preferences', min=3, task='Your partner disagrees. Say what you prefer and why.', hint='I’d rather… because…'), dict(title='Compromise', min=3, task='Find a plan you both like: place, day and budget.', hint='We could… / Either works for me.'), dict(title='Share decisions', min=2, whole=True, task='Whole group: each pair presents the final plan.', hint='We decided to… because…')],
  infogap=dict(title='Weekend trip options', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='You know the prices', task='You know the train and the hotel. Ask about the rest.', rows=[dict(k='Train ticket', v='$40 each'), dict(k='Hotel (one night)', v='$85'), dict(k='Museum ticket', v=''), dict(k='Leaving time', v='')]),
   b=dict(title='You know the schedule', task='You know the museum and the leaving time. Ask about the rest.', rows=[dict(k='Train ticket', v=''), dict(k='Hotel (one night)', v=''), dict(k='Museum ticket', v='$18'), dict(k='Leaving time', v='7:30 p.m. on Friday')])),
  teach=T('Fluência por repetição da função com informações novas a cada rodada.',
   group=['Troque os pares a cada rodada (A+B / C+D → A+C / B+D → A+D / B+C → grupo todo). Com 6 estudantes, três duplas simultâneas.', 'Sem salas simultâneas: interações sequenciais enquanto uma dupla apresenta.', 'Responsabilidade individual: cada aluno faz ≥1 sugestão e ≥1 pergunta.'],
   answers=['Info gap: A tem trem $40 e hotel $85; B tem museu $18 e saída 7:30 p.m. na sexta. Cada um completa o cartão perguntando.'], extra=['How much is the train ticket?', 'What time do we leave?'],
   errors=[('How many is the hotel?', 'How much is the hotel?'), ('We leave at Friday 7:30.', 'We leave on Friday at 7:30.')], support=['Entregue frases-modelo no chat da turma.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — decide on a plan',
  goal='Each group must decide on a trip plan in English: suggest, disagree politely, compromise and confirm.',
  missions=[dict(who='A', role='Friends', mission='Plan a two-day city trip. One person wants museums, the other wants food and music. Find a plan with both.', constraint='Use “What about…?” and “I’d rather…” at least once each.', start='Let’s plan our trip! What about…'),
            dict(who='B', role='Friends', mission='Plan a cheap beach day. The weather might be bad. Decide on a plan B.', constraint='Use “We could…” and give two reasons.', start='Hey! We could go to the beach if…'),
            dict(who='C', role='Family members', mission='Plan a visit to relatives. Agree on the day, the transport and who pays for what.', constraint='Ask “Should we…?” and close with a summary: “So, we decided to…”.', start='Okay, so when should we…')], min=11,
  success=['Make suggestions.', 'Give a reason.', 'Say what you prefer politely.', 'Agree on a final plan and repeat it.'],
  teach=T('Realizar algo com o inglês: o objetivo é decidir juntos, não só falar certo.',
   group=['Cada grupo recebe papéis, restrição e missão. Alterne quem propõe e quem reage.', 'Progressão: 1ª rodada com frases de apoio, 2ª só palavras-chave, 3ª sem roteiro.', 'Observe e anote 2–3 correções prioritárias; devolutiva no fim.'],
   answers=['Modelo: “What about a museum on Saturday?” → “Good idea, but I’d rather try a local restaurant first.” → “We could do both: museum in the morning, dinner at seven.”'], extra=['What if nobody can agree?'], support=['Dê o início de frase (“Start with”) em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a message to a friend to suggest a short trip. Say where, when and how you could go, and what you prefer.',
  steps=['Greeting and idea', 'Option', 'Preference with reason', 'Closing question'],
  model='Hi Sam! **What about a weekend in Boston?** We could take the bus on Saturday morning. **I’d rather** stay in a small hotel because it’s more comfortable. Does that work for you? Let me know!',
  checklist=['I greeted my friend and made a suggestion.', 'I offered at least one option (We could…).', 'I said what I prefer and why (I’d rather… because…).', 'I closed with a question.'],
  tip='Fix only 2–3 priority points. Show a more natural way to say the same idea instead of rewriting everything.', fix=dict(n=3),
  teach=T('Produção escrita curta ligada à situação comunicativa.',
   solo=['Peça a mensagem; corrija 2–3 pontos prioritários e mostre uma forma mais natural.'], group=['Cada estudante escreve; depois troquem os textos entre colegas e corrijam em duplas.'],
   extra=['Add a plan B in case it rains.'], errors=[('What about we go to Boston?', 'What about going to Boston?'), ('I rather the bus.', 'I’d rather take the bus.')], support=['Dê o modelo e peça só para trocar os dados.'])),
 feedback('Example: You made a suggestion and gave a reason for your preference.', 'Example: Stress the key words, not every word.', 'Example: Plan a trip for three people with different budgets, without notes.', 'Observe também se o aluno aceitou ideias do parceiro, não só propôs as próprias.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='💡', name='Make a suggestion', prompt='Without notes: suggest going to the mountains this weekend.', model='What about going to the mountains this weekend?'), dict(ic='💬', name='Say a preference', prompt='Your friend suggests the bus. You prefer the train because it’s faster.', model='I’d rather take the train because it’s faster.'), dict(ic='⭐', name='Offer an option', prompt='Offer to leave after work.', model='We could leave after work.')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 45–60 second audio planning a trip with an imaginary friend.', 'Write a short message suggesting a plan and a plan B.', 'Review the four ★ expressions and write two examples for each.', 'Listen to the dialogue again and mark where the speakers show they are flexible.']),
  spaced=dict(next=['Let’s…', 'What about…?', 'We could…'], week=['I’d rather…', 'Either works for me.', 'Should we…?'], unit=['Suggest · prefer · compromise · decide']),
  teach=T('Toda aula termina com uma produção observável.', solo=['Sem consultar as anotações: sugerir, dizer uma preferência e oferecer uma opção.'], group=['Exit challenge individual; compare com o colega e combine a tarefa de continuidade.'],
   answers=['What about going to the mountains this weekend? · I’d rather take the train because it’s faster. · We could leave after work.'], extra=['Revisão espaçada: retomar na próxima aula, depois de uma semana e na missão de encerramento da unidade.'])),
 levels([('Let’s go. Beach. Saturday.', None), ('What about the beach on Saturday? I’d rather go by train.', 'Suggest, give a preference and a reason.'), ('If the weather is good, we could go to the beach, but if it rains, I think we should visit a museum.', None), ('Given our budget, I’d suggest the beach, although I’m open to alternatives if you feel strongly about the city.', None), ('I’m inclined to propose the coast, but I’d be happy to reconsider if that doesn’t suit everyone.', None), ('Shall we settle on the coast, then, unless anyone has a compelling reason to object?', None)], 'Mostrar a progressão sem criar seis metodologias.')
]

LESSON = dict(n=95, topic='Planning a trip together', level='A2', title='Planning a Trip Together', pt='Planejar uma viagem juntos', unit=unit(1), minutes=60, cast=['Eva', 'Noah'], scene='office', tod='day', plan=PLAN, dialog=DIALOG, pages=PAGES)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
