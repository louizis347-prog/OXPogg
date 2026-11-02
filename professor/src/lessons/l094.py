#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from rl_common import PLAN, teach, finish

UNIT_NAME = 'Culture and communication'
UNIT_MAP = ['Invitations: accept and decline', 'Experiences (present perfect)', 'Telling stories (past continuous)', 'Detailed directions', 'News and events', 'Traditions and festivals', 'Small talk with strangers', 'Real-Life Mission Day 12']

def E(w, r): return dict(w=w, r=r)

def fb_page(well, improve, nxt, focus):
    return dict(t='rl_feedback', stage='write', title='Feedback & review — Speaking Performance Check',
     criteria=[dict(k='flu', name='Fluency', desc='Mantém a comunicação sem interrupções excessivas.'), dict(k='lan', name='Language use', desc='Utiliza adequadamente padrões, vocabulário e expressões.'), dict(k='pro', name='Pronunciation', desc='É compreensível e usa ritmo e entonação adequados.'), dict(k='int', name='Interaction', desc='Responde, pergunta, esclarece e desenvolve a conversa.')],
     interpret=[dict(max=8, text='Needs more support. Revisit the main patterns with guided practice before the next lesson.'), dict(max=13, text='Functional performance. Work on the lowest criteria in the next lesson.'), dict(max=17, text='Good control. Add follow-up questions and longer answers.'), dict(max=20, text='Strong performance. Move to a more demanding situation.')],
     prompts=dict(well=well, improve=improve, next=nxt),
     teach=teach(goal='Avaliar o que o aluno conseguiu comunicar, não só os erros gramaticais. Foco desta aula: %s' % focus,
      solo=['O estudante se autoavalia primeiro; depois você comenta.', 'Feche com os três blocos: What you did well · What to improve · Your next challenge.'], group=['Dê um comentário por critério a cada estudante.', 'Cada um escolhe o próprio próximo desafio.'],
      answers='A rubrica é uma ferramenta interna de acompanhamento, não uma certificação CEFR.'))

def lv_page(ladder, note_extra=''):
    return dict(t='rl_levels', stage='exit', title='Level up — the same situation from A1 to C2', you='A2',
     intro='The situation stays the same; the language grows in length, nuance and autonomy.',
     ladder=[dict(lv=l, say=s, goal=g) for l, s, g in zip(['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], *zip(*ladder))],
     note='This progression is illustrative: complex sentences do not define a level on their own. CEFR also considers comprehension, autonomy, fluency, accuracy, interaction and appropriateness.',
     teach=teach(goal='Mostrar a progressão sem criar seis metodologias.', solo=['Mostre onde o estudante está (A2) e a próxima etapa (B1).'], group=['Cada um escolhe a frase do próprio nível e a do próximo.']))

def mk(n, k, title, pt, cast, scene, tod, pages, dialog, level='A2'):
    return dict(n=n, topic=title, level=level, title=title, pt=pt, unit=dict(n=12, k=k, of=8, name=UNIT_NAME), minutes=60, cast=cast, scene=scene, tod=tod, plan=PLAN, dialog=dialog, pages=pages)

def unit(k): return dict(n=12, k=k, of=8, name=UNIT_NAME, map=UNIT_MAP)

DIALOG = dict(speakers={'Guest': {'name': 'Rosa'}, 'Host': {'name': 'Diego'}}, lines=[
 dict(who='Host', en='Lovely evening, isn’t it? Are you here for the cultural night?', pt='Noite linda, não é? Você veio para a noite cultural?'),
 dict(who='Guest', en='Yes! Did you hear about the music show? **Apparently,** it starts at eight and it’s free.', pt='Sim! Você ficou sabendo do show de música? Pelo visto começa às oito e é gratuito.'),
 dict(who='Host', en='I read that Hana is singing a Korean folk song. **Shall we** watch it together?', pt='Li que a Hana vai cantar uma canção folclórica coreana. Vamos assistir juntos?'),
 dict(who='Guest', en='**Sounds like a plan!** **Speaking of** music, have you ever heard Korean singing live?', pt='Combinado! Falando em música, você já ouviu canto coreano ao vivo?'),
 dict(who='Host', en='Never! But I was walking here when I heard her practicing. It sounded beautiful.', pt='Nunca! Mas eu estava vindo para cá quando a ouvi ensaiando. Soou lindo.'),
 dict(who='Guest', en='Wonderful. Could you tell me how to get to the stage?', pt='Maravilhoso. Você poderia me dizer como chegar ao palco?'),
 dict(who='Host', en='Go straight past the fountain. You can’t miss it.', pt='Siga reto passando pela fonte. Você não tem como errar.'),
 dict(who='Guest', en='Thanks! **By the way,** in my country people usually bring flowers to artists. I’ll buy some first.', pt='Obrigada! A propósito, no meu país as pessoas costumam levar flores para os artistas. Vou comprar algumas antes.'),
 dict(who='Host', en='Great idea. **Let’s meet** at the stage at quarter to eight.', pt='Ótima ideia. Vamos nos encontrar no palco às oito menos quinze.')])

PAGES = [
 dict(t='rl_open', stage='warm', title='Real-Life Mission Day 12', pt='Missão da unidade 12', level='A2', unit=unit(8),
  situation=dict(text='You arrive at a cultural evening in a plaza. In one evening you chat with a stranger, invite and decline, share news, tell a short story, ask for directions and explain a tradition.', scene='plaza', tod='dusk', cast=['Rosa', 'Diego', 'Hana']),
  goal='By the end of the class you can chain seven real-life situations in one evening, switching naturally between inviting, sharing experiences, telling stories, giving directions, sharing news and talking about traditions.',
  canDo=['Open and close a chat with a stranger', 'Invite, accept or decline politely', 'Share an experience, a story or news', 'Give directions and explain a tradition'],
  success=['I connect the situations in one conversation.', 'I use at least one expression from each class.', 'I react and ask questions.', 'I solve the small problems of the evening.'],
  think='Imagine a night out where you meet new people. Which of the seven situations of this unit would you need first?',
  teach=teach(goal='Abrir o Mission Day: revisitar as 7 situações da unidade em uma noite.', solo=['Peça que o aluno escolha a situação de que mais gostou.', 'Mostre os 4 critérios.'], group=['Cada estudante cita uma aula da unidade e uma expressão.', 'Anote no quadro como mapa da noite.'], extra=['Which class helped you most?', 'Which situation is hardest for you?'], support=['Mostre o mapa da unidade e peça uma expressão por aula.'])),
 dict(t='rl_warm', stage='warm', title='Connection & warm-up',
  intro=dict(solo='Review the unit through personal questions and let the student choose favorite expressions.', group='One question per student, then a question back to a classmate.'),
  recall='Unit 12 review: invite (87) · experiences (88) · stories (89) · directions (90) · news (91) · traditions (92) · small talk (93). Ask: Which expression do you remember from each class?',
  qs=[dict(q='Which class of this unit did you enjoy most?', pt='De qual aula desta unidade você mais gostou?', sup=['The one about…', 'Directions.', 'Traditions.']),
      dict(q='What is one expression you use now?', pt='Qual expressão você já usa?', sup=['Would you like to…?', 'Have you ever…?', 'Are you from here?']),
      dict(q='What do you do at a cultural event?', pt='O que você faz em um evento cultural?', sup=['I listen to music.', 'I try food.', 'I meet people.'])],
  tip='Use the answers to choose which situations deserve more time during the mission.',
  teach=teach(goal='Retomar toda a unidade com perguntas pessoais.', extra=['What is your favorite expression of the unit?', 'What do you still find difficult?'], errors=[E('I have enjoyed more the class about…', 'I enjoyed the class about… most.'), E('I use already this expression.', 'I already use this expression.')], support=['Mostre as 7 situações e peça que escolham uma.'])),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — A cultural evening',
  intro='At a cultural event people mix small talk, curiosity and kindness. Look and guess before you read.',
  cards=[dict(vis='tod:dusk', en='Start with a light comment', pt='Comece com um comentário leve', note='The evening, the music or the weather are easy first topics.'),
         dict(vis='prop:camera', en='Show curiosity about others', pt='Mostre curiosidade pelos outros', note='Ask questions about where people are from and what they enjoy.'),
         dict(vis='prop:cake', en='Share and connect', pt='Compartilhe e conecte', note='Food, music and stories are natural ways to connect with new people.')],
  qs=[dict(q='How do you start a conversation at an event?', pt='Como puxar conversa em um evento?', levels=dict(A1='Nice evening!', A2='Lovely evening, isn’t it?', B1='Comment on something you both see, then ask a light question.', B2='Begin with a shared observation, then widen with an open question to find common ground.')),
      dict(q='Why combine small talk with real information?', pt='Por que unir conversa leve e informação real?', levels=dict(A1='To be friendly.', A2='To be friendly and useful.', B1='Small talk builds trust, and information makes the conversation useful.', B2='Light talk builds rapport, while concrete details let the exchange lead to plans.')),
      dict(q='How can you leave a conversation politely?', pt='Como sair de uma conversa educadamente?', levels=dict(A1='Bye! Nice to meet you.', A2='It was nice talking to you. See you later!', B1='Say it was nice, give a reason or plan, and say goodbye.', B2='A warm closing remark plus a reason to move on lets both people part comfortably.'))],
  compare='In Brazil, cultural events (festas, shows in the praça) are social and people chat easily. In English, “Lovely evening, isn’t it?”, “Are you from here?” and “It was nice talking to you” do the same job. What would you add?',
  teach=teach(goal='Ativar o contexto da missão: conversar bem em um evento cultural.', solo=['Mostre os 3 cartões e peça hipóteses.', 'Pergunte que eventos culturais o aluno frequenta.'], group=['Cada estudante escolhe um cartão e explica.', 'Pergunte “Do you agree?”.'], answers=['Q1: Lovely evening, isn’t it?', 'Q2: friendly and useful.', 'Q3: It was nice talking to you.'], extra=['What cultural event would you invite me to?', 'How do you meet people at events?'], support=['Use as respostas A1.'], stretch=['B2: compare eventos culturais no Brasil e nos EUA.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='plaza', tod='dusk', cast=['Rosa', 'Diego', 'Hana']),
  pass1=dict(q='Where are Rosa and Diego?', pt='Onde Rosa e Diego estão?', opts=['At a cultural evening', 'At a bank', 'At the airport'], ans=0),
  pass2=dict(tasks=[dict(label='Event', ans='music show'), dict(label='Start time', ans='eight'), dict(label='Singer', ans='Hana'), dict(label='Landmark', ans='fountain'), dict(label='Gift for artists', ans='flowers')]),
  teach=teach(goal='Entender a conversa e 5 informações.', solo=['Esconda o texto. 1ª escuta: local.', '2ª escuta: evento, horário, cantora, ponto de referência e presente.'], group=['Escuta coletiva; duplas anotam antes de revelar.', 'Mostre o texto no final.'], answers=['Pass 1: at a cultural evening.', 'Pass 2: music show · eight · Hana · fountain · flowers.'], extra=['What time do they meet?', 'Who gives directions?'], support=['Use “Slow” e pause após cada fala.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='What event are they going to?', opts=['A music show', 'A football game', 'A movie'], ans=0), dict(q='Who is singing?', opts=['Hana', 'Rosa', 'Diego'], ans=0), dict(q='How does Rosa get to the stage?', opts=['Straight past the fountain', 'Left at the bank', 'By bus'], ans=0), dict(q='What will Rosa buy?', opts=['Flowers', 'Tickets', 'Food'], ans=0)],
  retell=dict(prompt='Retell the evening in your own words, using three situations.', starters=['They meet and talk about…', 'Diego invites Rosa to…', 'Rosa asks for…', 'They plan to…']),
  teach=teach(goal='Ler o diálogo integrado e encontrar as situações das aulas anteriores.', solo=['O estudante lê Rosa; você lê Diego.', 'Peça que aponte onde aparece cada aula.'], group=['Leitura em duplas.', 'Cada dupla marca uma aula no texto.'], answers=['A music show · Hana · Straight past the fountain · Flowers'], extra=['Which classes can you spot in the dialogue?', 'What could Rosa add?'], errors=[E('Shall we to watch it?', 'Shall we watch it?'), E('Let’s to meet at the stage.', 'Let’s meet at the stage.')], support=['Mostre a tradução (PT) após a 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[dict(en='Shall we…?', pt='Vamos…?', use='Suggest doing something together.', reg='polite', alt='Casual: **Wanna…?**', pri=True),
         dict(en='Sounds like a plan.', pt='Combinado.', use='Agree to a plan.', reg='casual', alt='Also: **Sounds good.**', pri=True),
         dict(en='Speaking of…', pt='Falando em…', use='Link to a related topic.', reg='neutral', pri=True),
         dict(en='By the way,…', pt='A propósito,…', use='Add a new topic.', reg='neutral', pri=True),
         dict(en='Let’s meet at…', pt='Vamos nos encontrar em…', use='Set a place and time.', reg='neutral', pri=True),
         dict(en='quarter to eight', pt='oito menos quinze', use='Say the time naturally.', reg='neutral'),
         dict(en='See you there!', pt='Nos vemos lá!', use='Close a plan.', reg='casual'),
         dict(en='Great idea.', pt='Ótima ideia.', use='React to a suggestion.', reg='neutral')],
  discover=dict(fns=['Suggesting', 'Agreeing', 'Linking topics', 'Adding a topic', 'Fixing a plan'],
   items=[dict(en='Shall we watch it together?', fn='Suggesting'), dict(en='Sounds like a plan!', fn='Agreeing'), dict(en='Speaking of music, have you ever heard it live?', fn='Linking topics'), dict(en='By the way, I’ll buy flowers.', fn='Adding a topic'), dict(en='Let’s meet at the stage.', fn='Fixing a plan')]),
  note='Choose the 5 starred connectors: they join the situations of the unit into one natural evening.',
  teach=teach(goal='Escolher 5 conectores que ligam as situações da unidade.', solo=['Pergunte “When do you say it?”.', 'Peça uma frase usando um chunk antigo + um novo.'], group=['Cada estudante escolhe um conector e cria uma frase.', 'Duplas: duas falas ligadas por By the way / Speaking of.'], answers=['Suggesting · Agreeing · Linking · Adding · Fixing a plan'], extra=['Which connector is the most useful for you?'], errors=[E('Speaking about music,…', 'Speaking of music,…'), E('By the way of…', 'By the way,…')], support=['Trabalhe só 3 conectores primeiro.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Suggesting and agreeing', formula='**Shall we / Let’s** + base verb', ex=['Shall we watch the show?', 'Let’s meet at the stage.', 'Shall we get some food first?'], main=True),
            dict(name='Linking topics', formula='**Speaking of / By the way,** + new topic', ex=['Speaking of music, have you ever heard it live?', 'By the way, did you hear about the festival?'], main=True),
            dict(name='Combining the unit', formula='Comment → question → plan → close', ex=['Lovely evening, isn’t it? Are you from here?', 'Would you like to go? Sounds like a plan!'])],
  swap=dict(frame='Shall we {activity} at {time}?', tpt='Vamos {activity} às {time}?',
   slots=[dict(k='activity', label='Activity', opts=[dict(en='watch the show', pt='assistir ao show'), dict(en='get some food', pt='comer alguma coisa'), dict(en='meet at the stage', pt='nos encontrar no palco')]),
          dict(k='time', label='Time', opts=[dict(en='seven', pt='sete'), dict(en='eight', pt='oito'), dict(en='quarter to eight', pt='oito menos quinze')])]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['Shall we go?', 'Would you like to go together?'], ['Sounds like a plan!', 'That arrangement suits me.'], ['By the way,…', 'Incidentally,…'], ['See you there!', 'I look forward to seeing you there.']], note='“Shall we” is a polite suggestion, common in U.S. English in invitations too.'),
  teach=teach(goal='Conectar as situações com sugestões e conectores; integrar padrões anteriores.', solo=['Mostre os padrões no diálogo.', 'Use “Swap the words” em voz alta.'], group=['Troca em cadeia: cada estudante muda UMA peça.', 'Duplas: duas falas ligadas.'], answers='Padrões 01/02 são o foco; 03 integra a unidade.', extra=['Suggest a plan for tonight.', 'Link two topics with By the way.'], errors=[E('Shall we to go?', 'Shall we go?'), E('Let’s going.', 'Let’s go.'), E('Speaking about…', 'Speaking of…')], support=['Fique só com Shall we… + Sounds like a plan.'], stretch=['Encadeie 4 situações em uma fala de 30 segundos.'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Thought groups', tip='Natural speech comes in short groups of words with a small pause between them: “By the way, | in my country, | people usually bring flowers.”',
  items=[dict(say='By the way, I’ll buy some flowers.', linked='By the WAY, | I’ll BUY some FLOW·ers.', ipa='/baɪ ðə weɪ/', rhythm='ooOooOoOo'), dict(say='Speaking of music, have you ever heard it?', linked='SPEAK·ing of MU·sic, | have-ya EV·er HEARD it?', ipa='/ˈspikɪŋ əv/', rhythm='OooOooooOoo'), dict(say='Sounds like a plan!', linked='SOUNDS like a PLAN!', ipa='/saʊndz laɪk ə/', rhythm='OooO')],
  identify=[dict(q='Which one do you hear?', opts=['By the way, I’ll buy some flowers.', 'By the way I’ll buy some flowers soon.', 'Bye, the way I buy flowers.'], ans=0, say='By the way, I’ll buy some flowers.'), dict(q='Which one do you hear?', opts=['Sounds like a plan!', 'Sounds like a pan!', 'Sounds like a plane!'], ans=0, say='Sounds like a plan!')],
  own=dict(prompt='Write one sentence with a connector (By the way / Speaking of) about the evening.', criteria='Say it twice: word by word, then in thought groups. Which sounds more natural?'),
  teach=teach(goal='UM só fenômeno: grupos de pensamento (pausas curtas entre blocos).', solo=['Escutar e identificar → repetir em blocos → frase própria.', 'Marque as pausas com uma barra.'], group=['Coro, depois duplas.', 'Cada estudante diz uma frase em blocos.'], answers=['Identify 1: By the way, I’ll buy some flowers. · Identify 2: Sounds like a plan!'], errors=[E('Falar palavra por palavra, sem blocos', 'By the WAY, | I’ll BUY some FLOWers.'), E('Pausa no meio de “Sounds like a plan”', 'Uma só unidade: Sounds-like-a-PLAN')], support=['Reduza a velocidade e marque os blocos.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    dict(type='mcq', q='1. You see a stranger at the plaza and want to start a chat.', opts=['Lovely evening, isn’t it?', 'Why you are alone?', 'Give me your phone.'], ans=0, why='Start light, with a comment.'),
    dict(type='mcq', q='2. A friend invites you, but you have a meeting. Choose the kind reply.', opts=['I’d love to, but I have a meeting. Maybe next time!', 'No. I do not like it.', 'I am meeting yes.'], ans=0, why='I’d love to, but… + maybe next time.'),
    dict(type='mcq', q='3. You want to ask where the stage is.', opts=['Could you tell me how to get to the stage?', 'Stage where is it?', 'How to be the stage?'], ans=0, why='Could you tell me how to get to… is polite.'),
    dict(type='mcq', q='4. You want to tell about a tradition in your country.', opts=['In my country, people usually bring flowers to artists.', 'My country is flowers artists.', 'People bring usually flowers in my country.'], ans=0, why='In my country, people usually + verb.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    dict(type='gap', text='___ of music, have you ever heard Korean singing?', ans='Speaking', bank=['Speaking', 'Talking', 'Telling'], why='Speaking of + noun.'),
    dict(type='gap', text='Shall we ___ the show together?', ans='watch', bank=['watch', 'to watch', 'watching'], why='Shall we + base verb.'),
    dict(type='swap', instr='Add “by the way” to a new topic:', frm='I’ll buy some flowers.', ans=['By the way, I’ll buy some flowers.'], model='By the way, I’ll buy some flowers.', why='By the way, + new topic.'),
    dict(type='swap', instr='Say you have never done it:', frm='I heard Korean music live.', ans=['I’ve never heard Korean music live.', 'I have never heard Korean music live.'], model='I’ve never heard Korean music live.', why='Present perfect with never.'),
    dict(type='reply', npc='Shall we meet at the stage at quarter to eight?', q='Choose the best reply.', opts=['Sounds like a plan! See you there.', 'I am stage.', 'No quarter.'], ans=0, why='Agree to the plan and confirm.')])],
  teach=teach(goal='Do controlado ao guiado antes da missão.', solo=['Peça que justifique cada resposta.', 'Peça a aula de origem de cada expressão.'], group=['Duplas comparam antes de revelar.', 'Pontos por resposta justificada.'], answers=['1: Lovely evening, isn’t it? · 2: I’d love to, but I have a meeting… · 3: Could you tell me how to get to the stage? · 4: In my country, people usually…', 'Gap: Speaking · watch · By the way, … · I’ve never heard… · Sounds like a plan!'], extra=['Say each answer in thought groups.'], errors=[E('Shall we to watch?', 'Shall we watch?'), E('Speaking about music', 'Speaking of music')], support=['Ofereça o banco de palavras.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — the cultural evening',
  brief=dict(teacher='You are a guest at the event. Change the plan: the show moves, someone cancels, a new friend arrives.', student='You are at the cultural evening: chat, invite, ask directions, share news and a tradition.'),
  orders=['Meet a stranger and decide to watch the show together', 'Ask for directions to the food stalls and share a tradition', 'Share news about the event and invite a friend'],
  complications=['The show is moved to another stage.', 'A friend cancels: decline another invitation kindly.', 'You need to ask for directions again.', 'Someone asks about your country’s traditions.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['Lovely evening, isn’t it?', 'Shall we…?', 'By the way,…', 'Could you tell me how to get to…?']), dict(label='Keywords', desc='Only the keywords', help=['music show', 'fountain', 'flowers', 'quarter to eight'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I connect the situations in one conversation.', 'I use at least one expression from each class.', 'I react and ask questions.', 'I solve the small problems of the evening.'],
  teach=teach(goal='Simulação integrada com mudanças de plano, três rodadas com menos apoio.', solo=['Escolha uma ordem e adicione complicações no meio.', 'Rodada 1 com chunks, 2 palavras-chave, 3 livre.', 'Anote 2–3 correções para a devolutiva da unidade.'], extra=['What if the show is cancelled?', 'What would you say to a new friend at the end?'], errors=[E('I like to see the show with you? (sem Shall we)', 'Shall we watch the show together?')], support=['Volte à rodada 1 se travar.'], stretch=['Encadeie as 7 situações em 3 minutos.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Meet and invite', min=3, task='Start a chat and invite your partner to the show.', hint='Lovely evening, isn’t it? / Would you like to…?'), dict(title='Share and tell', min=3, task='Share news and a short experience or story.', hint='Did you hear about…? / I’ve never… / I was… when…'), dict(title='Directions and traditions', min=3, task='Ask for directions and explain a tradition.', hint='Could you tell me how to get to…? / In my country…'), dict(title='Connect it all', min=2, whole=True, task='Whole group: each pair says one sentence from every class.', hint='By the way… / Speaking of…')],
  infogap=dict(title='Evening program', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='Student A: your program', task='You know the music show and the dance class. Ask about the rest.', rows=[dict(k='Music show', v='8:00, main stage'), dict(k='Food stalls', v=''), dict(k='Dance class', v='7:00, next to the library'), dict(k='Photo exhibit', v='')]),
   b=dict(title='Student B: your program', task='You know the food stalls and the photo exhibit. Ask about the rest.', rows=[dict(k='Music show', v=''), dict(k='Food stalls', v='6:00 to 9:00, near the fountain'), dict(k='Dance class', v=''), dict(k='Photo exhibit', v='all evening, next to the bank')])),
  teach=teach(goal='Fluência com todas as funções da unidade e troca de informações.', group=['Troque os pares a cada rodada.', 'Responsabilidade individual: cada aluno usa pelo menos 4 aulas diferentes.', 'Sem salas simultâneas.'], answers=['Info gap: A tem Music show e Dance class; B tem Food stalls e Photo exhibit. Cada um completa perguntando “What time…?” e “Where is…?”.'], extra=['What time is the music show?', 'Where are the food stalls?'], errors=[E('The show is at the 8.', 'The show is at eight.'), E('It’s near of the fountain.', 'It’s near the fountain.')], support=['Entregue frases-modelo no chat.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — a cultural evening',
  goal='Each group must live the whole evening in English: meet, invite, share, tell, give directions and talk about traditions.',
  missions=[dict(who='A', role='Early arrivals', mission='Meet at the plaza: chat with a stranger, invite them to the music show, they decline, then agree on another plan. Ask where the stage is.', constraint='Use at least four expressions from classes 87, 90 and 93.', start='Lovely evening, isn’t it?'),
            dict(who='B', role='News and stories team', mission='Share news about the event, tell a short story about how you heard it and ask about a classmate’s travel experiences.', constraint='Use “Apparently…”, “I was… when…” and “Have you ever…?”.', start='Did you hear about…'),
            dict(who='C', role='Culture hosts', mission='Present a tradition from your country, invite visitors to try a dish and give directions to the food stalls.', constraint='Use “In my country…”, “It’s supposed to…” and “You can’t miss it.”', start='In my country, people usually…')], min=11,
  success=['Connect at least four situations.', 'Use an expression from each assigned class.', 'React and ask questions.', 'Solve one small problem together.'],
  teach=teach(goal='Realizar a missão integrada: viver a noite inteira em inglês.', group=['Cada grupo recebe papéis e restrições; alterne os papéis.', 'Progressão: com chunks, palavras-chave, sem roteiro.', 'Anote 2–3 correções por grupo e faça a devolutiva da unidade.'], answers=['Modelo: “Lovely evening, isn’t it?” → “Would you like to watch the music show?” → “I’d love to, but I have to meet a friend. Maybe next time.” → “Could you tell me how to get to the stage?”'], extra=['Which situation was the hardest to connect?'], support=['Dê o início de frase em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short message to a friend about the cultural evening: invite them, share one piece of news and give directions.',
  steps=['Greeting + invitation', 'News', 'Directions', 'Closing plan'],
  model='Hi Hana! Would you like to come to the cultural evening in the plaza? Apparently, the music show starts at eight and it’s free. From the bank, go straight past the fountain; you can’t miss the stage. Let’s meet there at quarter to eight!',
  checklist=['I invited my friend.', 'I shared news with Apparently or I read that.', 'I gave directions with a landmark.', 'I closed with a plan (Let’s meet…).'],
  tip='Fix only 2–3 priority points and show a more natural way to say the same idea.', fix=dict(n=3),
  teach=teach(goal='Produção escrita integrada: convite, notícia e direções.', solo=['Corrija 2–3 pontos prioritários.'], group=['Troquem as mensagens e respondam.'], extra=['Add a short story about how you heard of the event.'], errors=[E('Would you like come?', 'Would you like to come?'), E('Let’s meeting at eight.', 'Let’s meet at eight.')], support=['Dê o modelo e peça só para trocar os dados.'])),
 fb_page('Example: You connected several situations smoothly and reacted to your partner.', 'Example: Speak in thought groups, not word by word.', 'Example: Run a full evening conversation for three minutes without notes.', 'integração das situações da unidade.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❓', name='Suggest a plan', prompt='Without notes: suggest watching the show together.', model='Shall we watch the show together?'), dict(ic='💬', name='Link a topic', prompt='Change the topic to music.', model='Speaking of music, have you ever heard it live?'), dict(ic='⭐', name='Close a plan', prompt='Fix a place and time to meet.', model='Let’s meet at the stage at quarter to eight.')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 60-second audio telling about an evening out, using four situations.', 'Write a message inviting a friend and giving directions.', 'Choose one favorite expression from each class of the unit and create an example.', 'Listen to the dialogue again and mark which class each expression comes from.']),
  spaced=dict(next=['Shall we…?', 'Sounds like a plan.', 'By the way,…'], week=['Speaking of…', 'Let’s meet at…', 'Would you like to…?'], unit=['Invite · experiences · stories · directions · news · traditions · small talk · connect']),
  teach=teach(goal='Toda aula termina com uma produção observável e fecha a unidade.', solo=['Sem anotações: sugerir, mudar de assunto e fechar um plano.'], group=['Exit challenge individual; cada um escolhe a expressão favorita da unidade.'], answers=['Shall we watch the show together? · Speaking of music, have you ever heard it live? · Let’s meet at the stage at quarter to eight.'], extra=['Revisão espaçada: retomar na próxima unidade e depois de uma semana.'])),
 lv_page([('Hi! Music. Eight.', 'Connect with a few words.'), ('Shall we watch the show? Sounds like a plan!', 'Suggest and agree on a plan.'), ('By the way, did you hear about the show? Apparently it’s free, so shall we go together?', 'Link news and a suggestion.'), ('Speaking of music, I’ve been wanting to see her perform; I read that tickets are free, so it would be a shame to miss it.', 'Link topics, experience and opinion.'), ('I’ve never been one for crowds, but given the reviews, I’m inclined to make an exception tonight.', 'Express nuance and personal stance.'), ('Rarely does a free evening promise so much; I’d say we owe it to ourselves to go.', 'Use stylistic control and persuasion.')])
]
LESSON = mk(94, 8, 'Real-Life Mission Day 12', 'Missão da unidade 12', ['Rosa', 'Diego', 'Hana'], 'plaza', 'dusk', PAGES, DIALOG)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
