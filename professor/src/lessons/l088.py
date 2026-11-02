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

DIALOG = dict(speakers={'Traveler': {'name': 'Raj'}, 'Planner': {'name': 'Nina'}}, lines=[
 dict(who='Planner', en='Raj, **have you ever been to** Japan? I’m planning a trip next spring.', pt='Raj, você já esteve no Japão? Estou planejando uma viagem para a próxima primavera.'),
 dict(who='Traveler', en='Yes! **I’ve been to** Tokyo twice. **I’ve never** seen such clean trains anywhere else.', pt='Sim! Já estive em Tóquio duas vezes. Nunca vi trens tão limpos em nenhum outro lugar.'),
 dict(who='Planner', en='Really? What was the best thing you did there?', pt='Sério? Qual foi a melhor coisa que você fez lá?'),
 dict(who='Traveler', en='**I’ve tried** ramen at a tiny shop near the station. It was the best meal of my life.', pt='Eu comi ramen numa lojinha perto da estação. Foi a melhor refeição da minha vida.'),
 dict(who='Planner', en='Wow. **Have you ever** felt lost there? I don’t speak any Japanese.', pt='Nossa. Você já se sentiu perdido lá? Eu não falo nada de japonês.'),
 dict(who='Traveler', en='Once, but people helped me. **I’ve never** met anyone unfriendly on my trips.', pt='Uma vez, mas as pessoas me ajudaram. Nunca conheci ninguém antipático nas minhas viagens.'),
 dict(who='Planner', en='That’s reassuring. I’ve never traveled alone before, so I’m a little nervous.', pt='Isso é tranquilizador. Eu nunca viajei sozinha antes, então estou um pouco nervosa.'),
 dict(who='Traveler', en='You’ll be fine! Have you ever visited another country by yourself?', pt='Você vai ficar bem! Você já visitou outro país sozinha?'),
 dict(who='Planner', en='Only Finland, for a conference. So this will be my first big adventure.', pt='Só a Finlândia, para uma conferência. Então essa vai ser minha primeira grande aventura.')])

PAGES = [
 dict(t='rl_open', stage='warm', title='Experiences (present perfect)', pt='Experiências de vida', level='A2', unit=unit(2),
  situation=dict(text='At a café, a friend asks about your travel experiences before a big trip. You share what you have done, what you have never done and one short story.', scene='cafe', tod='day', cast=['Raj', 'Nina']),
  goal='By the end of the class you can ask about life experiences, answer with “I’ve been to / I’ve never…” and add one detail in the past.',
  canDo=['Ask: Have you ever…?', 'Say what you have or have never done', 'Say how many times: once, twice, a few times', 'Add details about one experience in the past'],
  success=['I ask a Have you ever… question.', 'I answer with I’ve… or I’ve never…', 'I add one detail in the past.', 'I react to my partner’s story.'],
  think='Think of one place or thing you have experienced that most people you know have not. How would you tell that story in English?',
  teach=teach(goal='Abrir pela situação: conversar sobre experiências de vida.', solo=['Pergunte ao estudante um lugar que ele já visitou e um que nunca visitou.', 'Mostre os 4 critérios.'], group=['Cada estudante diz um país que já visitou ou quer visitar.', 'Anote no quadro.'], extra=['What is the farthest place you have been to?', 'What is on your travel wish list?'], support=['Aceite palavras soltas (a country, a food) e reformule em frases.'])),
 dict(t='rl_warm', stage='warm', title='Connection & warm-up',
  intro=dict(solo='Ask about the student’s week and recycle invitation language from the last class.', group='One question per student, then a question back to a classmate.'),
  recall='Invitations (class 87): “Would you like to…?” and “I’d love to, but…”. Ask: What invitation did you get lately?',
  qs=[dict(q='Where did you go on your last trip?', pt='Para onde você foi na sua última viagem?', sup=['I went to…', 'I didn’t travel.', 'I visited my family.']),
      dict(q='Who do you usually travel with?', pt='Com quem você costuma viajar?', sup=['With my family.', 'With friends.', 'Alone.']),
      dict(q='Do you prefer beaches, cities or mountains?', pt='Você prefere praias, cidades ou montanhas?', sup=['Beaches.', 'Cities.', 'It depends.'])],
  tip='Collect travel words (airport, hotel, beach) that the student already has; they will be useful for the experiences.',
  teach=teach(goal='Ativar vocabulário de viagem e passado simples.', extra=['What is the best trip you have ever taken?', 'Where would you go tomorrow if you could?'], errors=[E('I have gone to Rio last year.', 'I went to Rio last year.'), E('I am travel with friends.', 'I travel with friends.')], support=['Use as respostas-chip.'])),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Travel stories',
  intro='Sharing travel stories is an easy way to connect with people in English-speaking countries. Look and guess before you read.',
  cards=[dict(vis='prop:suitcase', en='Have you ever been to…?', pt='Você já esteve em…?', note='A very common question to start a friendly conversation about travel.'),
         dict(vis='prop:camera', en='Tell the story in the past', pt='Conte a história no passado', note='After “Have you ever…?”, people give details with the past: “I went in July.”'),
         dict(vis='prop:map', en='Give a tip', pt='Dê uma dica', note='Listeners often ask for recommendations: “What would you recommend?”')],
  qs=[dict(q='Why do people ask “Have you ever been to…?”', pt='Por que as pessoas perguntam “Have you ever been to…?”', levels=dict(A1='To talk about travel.', A2='To start a conversation about places you know.', B1='It invites the other person to share experiences and gives you topics to talk about.', B2='It is a low-pressure way to build rapport, since everyone has some travel story or wish.')),
      dict(q='What tense do we use for the details of a trip?', pt='Qual tempo usamos para os detalhes de uma viagem?', levels=dict(A1='Past: I went.', A2='The past simple: I went there in 2022.', B1='We use present perfect for the experience and past simple for when and what happened.', B2='Present perfect introduces the experience; past simple anchors it in time with details.')),
      dict(q='What can you ask after someone tells a travel story?', pt='O que perguntar depois de uma história de viagem?', levels=dict(A1='What was it like?', A2='What was the best part? Would you go again?', B1='How was it? What would you recommend?', B2='What surprised you most? Is there anything you would do differently?'))],
  compare='In Brazil, travel stories are also popular, especially about beaches and family trips. In English, the questions “Have you ever…?” and “What was it like?” are a ready-made way to keep the talk going. What do you usually ask?',
  teach=teach(goal='Ver as experiências de viagem como assunto social e a combinação present perfect + past simple.', solo=['Mostre os 3 cartões e peça hipóteses.', 'Pergunte que histórias o estudante gosta de ouvir.'], group=['Cada estudante escolhe um cartão e explica.', 'Debate: “Do you agree?”'], answers=['Q1: to start a conversation.', 'Q2: past simple for details.', 'Q3: What was it like? / What would you recommend?'], extra=['What is your best travel story?', 'Do you like hearing other people’s stories?'], support=['Use as respostas A1 como andaime.'], stretch=['B2: explique por que present perfect não aceita “yesterday”.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='cafe', tod='day', cast=['Raj', 'Nina']),
  pass1=dict(q='What are Raj and Nina talking about?', pt='Sobre o que Raj e Nina conversam?', opts=['Travel experiences', 'A restaurant menu', 'A job interview'], ans=0),
  pass2=dict(tasks=[dict(label='Country', ans='Japan'), dict(label='How many times Raj has been to Tokyo', ans='twice', alt=['two', '2']), dict(label='Raj’s favorite food', ans='ramen'), dict(label='How Nina feels', ans='nervous'), dict(label='Nina’s other country', ans='Finland')]),
  teach=teach(goal='Entender a conversa e depois 5 informações.', solo=['Esconda o texto. 1ª escuta: tema.', '2ª escuta: país, vezes, comida, sentimento e outro país.'], group=['Escuta coletiva; duplas anotam antes de revelar.', 'Mostre o texto só no final.'], answers=['Pass 1: travel experiences.', 'Pass 2: Japan · twice · ramen · nervous · Finland.'], extra=['Has Nina been to Japan?', 'Is Raj a good guide? Why?'], support=['Use “Slow” e pause após cada fala.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='How many times has Raj been to Tokyo?', opts=['Once', 'Twice', 'Never'], ans=1), dict(q='What does Raj say was the best meal of his life?', opts=['Ramen', 'Sushi', 'Pizza'], ans=0), dict(q='Why is Nina a little nervous?', opts=['She has never traveled alone', 'She has no money', 'She hates planes'], ans=0), dict(q='Where did Nina go by herself before?', opts=['Japan', 'Finland', 'India'], ans=1)],
  retell=dict(prompt='Retell the conversation in your own words.', starters=['Nina wants to…', 'Raj has been to…', 'He has never…', 'In the end, Nina feels…']),
  teach=teach(goal='Ler o diálogo, perceber os chunks e recontar.', solo=['O estudante lê Nina; você lê Raj; depois troquem.', 'Reconto no nível que conseguir.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia.'], answers=['Twice · Ramen · She has never traveled alone · Finland'], extra=['What would you ask Raj about Tokyo?', 'Is Nina ready for her trip?'], errors=[E('I have been in Japan.', 'I’ve been to Japan.'), E('Have you ever went to Japan?', 'Have you ever been to Japan?')], support=['Mostre a tradução (PT) após a 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[dict(en='Have you ever…?', pt='Você já…?', use='Ask about someone’s life experience.', reg='neutral', alt='Also: **Did you ever…?** (very informal in US English)', pri=True),
         dict(en='I’ve never…', pt='Eu nunca…', use='Say something you have not experienced.', reg='neutral', pri=True),
         dict(en='I’ve been to…', pt='Eu já estive em…', use='Say you have visited a place.', reg='neutral', alt='Also: **I’ve visited…**', pri=True),
         dict(en='twice / a few times', pt='duas vezes / algumas vezes', use='Say how many times something happened.', reg='neutral', pri=True),
         dict(en='What was it like?', pt='Como foi?', use='Ask for details about an experience.', reg='neutral'),
         dict(en='That’s reassuring.', pt='Isso é tranquilizador.', use='React when something makes you less worried.', reg='neutral'),
         dict(en='for the first time', pt='pela primeira vez', use='Talk about a new experience.', reg='neutral'),
         dict(en='What would you recommend?', pt='O que você recomendaria?', use='Ask for a tip.', reg='polite')],
  discover=dict(fns=['Asking about experiences', 'Saying no experience', 'Saying yes', 'Counting times', 'Asking for details'],
   items=[dict(en='Have you ever been to Japan?', fn='Asking about experiences'), dict(en='I’ve never traveled alone.', fn='Saying no experience'), dict(en='I’ve been to Tokyo.', fn='Saying yes'), dict(en='I’ve been there twice.', fn='Counting times'), dict(en='What was it like?', fn='Asking for details')]),
  note='Choose the 4 starred expressions to use again and again; the others help you react and ask more.',
  teach=teach(goal='Escolher 4 chunks prioritários e descobrir a função de cada um.', solo=['Pergunte “When do you say it?”.', 'Compare Have you ever…? e I’ve never… em perguntas e respostas.'], group=['Cada estudante escolhe a expressão que mais usaria.', 'Duplas: perguntar e responder com 3 chunks.'], answers=['Asking · No experience · Yes · Counting times · Details'], extra=['Which of these would you use on a first date? At work?'], errors=[E('I have never gone to Japan (ok) / I never have been…', 'I’ve never been to Japan.'), E('Have you ever been in Paris?', 'Have you ever been to Paris?')], support=['Trabalhe só as 4 expressões ★.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Asking about experiences', formula='**Have you ever** + past participle?', ex=['Have you ever been to Japan?', 'Have you ever tried sushi?', 'Have you ever flown alone?'], main=True),
            dict(name='Saying what you have / haven’t done', formula='**I’ve** (**never**) + past participle', ex=['I’ve been to Tokyo twice.', 'I’ve never traveled alone.', 'I’ve tried ramen.'], main=True),
            dict(name='Adding details in the past', formula='Past simple + time: **I went** / **It was**…', ex=['I went there in 2022.', 'It was the best meal of my life.'])],
  swap=dict(frame='I’ve {freq} {experience}.', tpt='Eu {freq} {experience}.',
   slots=[dict(k='freq', label='How often', opts=[dict(en='never', pt='nunca'), dict(en='already', pt='já'), dict(en='often', pt='muitas vezes')]),
          dict(k='experience', label='Experience', opts=[dict(en='tried sushi', pt='provei sushi'), dict(en='ridden a horse', pt='andei a cavalo'), dict(en='visited London', pt='visitei Londres')])]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['I’ve been there twice.', 'I have visited that country on two occasions.'], ['Never been.', 'I have never been there.'], ['Yeah, it was awesome.', 'Yes, it was an excellent experience.'], ['Wanna go?', 'Would you like to travel there?']], note='Contractions (I’ve) are normal in speech and informal writing.'),
  teach=teach(goal='Present perfect só para experiência de vida; detalhes ficam no passado simples.', solo=['Mostre os padrões dentro do diálogo.', 'Use “Swap the words” em voz alta.'], group=['Troca em cadeia: cada estudante muda UMA peça.', 'Entrevista em pares: Have you ever… ?'], answers='Padrões 01/02 são o foco; 03 liga a experiência aos detalhes.', extra=['Ask me three Have you ever… questions.', 'Say two things you have never done.'], errors=[E('Have you ever went…?', 'Have you ever gone / been…?'), E('I have been there yesterday.', 'I went there yesterday.'), E('I never have visited…', 'I’ve never visited…')], support=['Dê uma lista curta de particípios: been, seen, eaten, tried.'], stretch=['Contraste “been to” e “gone to”.'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Reduction', tip='“Have” and “been” lose strength in fast speech: “I’ve” is quick, “been” is /bɪn/, and “ever” links to “you”.',
  items=[dict(say='Have you ever been there?', linked='Hav·ya EV·er bin THERE?', ipa='/bɪn/', rhythm='ooOooO'), dict(say='I’ve never been to Tokyo.', linked='Ive NEV·er bin ta TO·kyo.', ipa='/ˈnɛvər/', rhythm='oOoooOo'), dict(say='I’ve tried it twice.', linked='Ive TRIED it TWICE.', ipa='/traɪd ɪt/', rhythm='oOoO')],
  identify=[dict(q='Which one do you hear?', opts=['Have you ever been there?', 'Have you ever seen there?', 'Did you ever be there?'], ans=0, say='Have you ever been there?'), dict(q='Which one do you hear?', opts=['I’ve never been to Tokyo.', 'I never went to Tokyo.', 'I’ve ever been to Tokyo.'], ans=0, say='I’ve never been to Tokyo.')],
  own=dict(prompt='Write a Have you ever… question about something you really want to know.', criteria='Say it twice: slowly, then reduced. Did “been” sound short?'),
  teach=teach(goal='UM só fenômeno: redução de have/been e ligação.', solo=['Escutar e identificar → repetir → pergunta própria.', 'Bata palmas nas sílabas fortes.'], group=['Coro, depois duplas.', 'Cada estudante cria uma pergunta.'], answers=['Identify 1: Have you ever been there? · Identify 2: I’ve never been to Tokyo.'], errors=[E('been pronunciado “bean” (/biːn/)', '“been” fraco /bɪn/ no inglês americano'), E('Have — you — ever (pausas)', 'Hav·ya EV·er (ligado)')], support=['Reduza a velocidade e conte as batidas.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    dict(type='mcq', q='1. You want to ask about travel experience.', opts=['Have you ever been to Brazil?', 'Did you ever be Brazil?', 'You are in Brazil?'], ans=0, why='Have you ever + past participle.'),
    dict(type='mcq', q='2. You have never eaten sushi. What do you say?', opts=['I’ve never eaten sushi.', 'I never ate sushi yet.', 'I have not eating sushi.'], ans=0, why='I’ve never + past participle.'),
    dict(type='mcq', q='3. You visited Paris in 2021. Which sentence gives a detail?', opts=['I went to Paris in 2021.', 'I have gone to Paris in 2021.', 'I am going Paris 2021.'], ans=0, why='With a finished time (in 2021) use the past simple.'),
    dict(type='mcq', q='4. A friend says “I’ve been to Rome!” What do you ask next?', opts=['What was it like?', 'What it was like?', 'Like what you?'], ans=0, why='What was it like? asks for details.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    dict(type='gap', text='Have you ever ___ to Canada?', ans='been', bank=['been', 'be', 'went'], why='been is the participle of be.'),
    dict(type='gap', text='I’ve ___ eaten Indian food. I love it!', ans='often', bank=['often', 'yesterday', 'ago'], why='often goes between have and the participle.'),
    dict(type='swap', instr='Say you never did it:', frm='I tried skiing.', ans=['I’ve never tried skiing.', 'I have never tried skiing.'], model='I’ve never tried skiing.', why='Never + present perfect.'),
    dict(type='swap', instr='Turn it into a question:', frm='You’ve been to Japan.', ans=['Have you ever been to Japan?', 'Have you been to Japan?'], model='Have you ever been to Japan?', why='Have + subject + (ever) + participle.'),
    dict(type='reply', npc='Have you ever traveled alone?', q='Choose the best reply.', opts=['Yes, twice. It was great.', 'Yes, I traveled alone yesterday ever.', 'I am alone yes.'], ans=0, why='Short yes + number of times + a past detail.')])],
  teach=teach(goal='Do controlado ao guiado antes da fala livre.', solo=['Peça que justifique cada resposta.', 'Peça a versão negativa e a pergunta.'], group=['Duplas comparam antes de revelar.', 'Pontos por resposta justificada.'], answers=['1: Have you ever been to Brazil? · 2: I’ve never eaten sushi. · 3: I went to Paris in 2021. · 4: What was it like?', 'Gap: been · often · I’ve never tried skiing. · Have you ever been to Japan? · Yes, twice. It was great.'], extra=['Say each answer aloud with natural reduction.'], errors=[E('I have ate sushi.', 'I’ve eaten sushi.'), E('Did you ever been there?', 'Have you ever been there?')], support=['Ofereça o banco de palavras.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — travel stories',
  brief=dict(teacher='You are a new friend who loves travel questions. Ask “Have you ever…?” and follow up.', student='Tell real experiences: places, food, activities. Add one detail in the past.'),
  orders=['Places you have been to', 'The best meal you have ever had', 'Something you have never done but want to try'],
  complications=['The friend has been to the same place and compares stories.', 'You have not been anywhere: say what you want to do.', 'The friend asks for a tip.', 'You cannot remember a word: describe it.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['Have you ever…?', 'I’ve been to…', 'I’ve never…', 'What was it like?']), dict(label='Keywords', desc='Only the keywords', help=['Japan', 'twice', 'ramen', 'nervous'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I ask a Have you ever… question.', 'I answer with I’ve… or I’ve never…', 'I add one detail in the past.', 'I react to my partner’s story.'],
  teach=teach(goal='Conversa guiada com perguntas de experiência e detalhes.', solo=['Use experiências reais do estudante.', 'Rodada 1 com chunks, 2 palavras-chave, 3 livre.', 'Anote 2–3 correções.'], extra=['What is the scariest thing you have ever done?', 'What would you like to do next year?'], errors=[E('I have been in Argentina last year.', 'I went to Argentina last year.')], support=['Volte à rodada 1 se travar.'], stretch=['Conte a mesma experiência para um amigo e para um desconhecido.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Have you ever…?', min=3, task='Ask your partner three Have you ever… questions.', hint='Have you ever… / Yes, I have. / No, never.'), dict(title='How many times?', min=3, task='Say how many times and where.', hint='I’ve been there twice.'), dict(title='What was it like?', min=3, task='Ask for details and answer in the past.', hint='What was it like? / It was…'), dict(title='Share a surprise', min=2, whole=True, task='Whole group: each pair shares something surprising about their partner.', hint='She has never… but she has…')],
  infogap=dict(title='Travel passport', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='Student A: your passport', task='You know Japan and Italy. Ask about the others.', rows=[dict(k='Japan', v='been twice'), dict(k='Brazil', v=''), dict(k='Italy', v='never been'), dict(k='Canada', v='')]),
   b=dict(title='Student B: your passport', task='You know Brazil and Canada. Ask about the others.', rows=[dict(k='Japan', v=''), dict(k='Brazil', v='been once'), dict(k='Italy', v=''), dict(k='Canada', v='been three times')])),
  teach=teach(goal='Fluência: perguntar e responder sobre experiências com informações novas.', group=['Troque os pares a cada rodada.', 'Responsabilidade individual: cada aluno faz ≥2 perguntas Have you ever…?', 'Sem salas simultâneas: interações sequenciais.'], answers=['Info gap: A tem Japan e Italy; B tem Brazil e Canada. Cada um completa perguntando Have you ever been to…?'], extra=['How many times have you been to Canada?', 'Have you ever been to Italy?'], errors=[E('How many times you have been?', 'How many times have you been?'), E('Yes, I have been two times.', 'Yes, twice.')], support=['Entregue frases-modelo no chat.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — find what you have in common',
  goal='Each group must discover travel experiences and plan one trip suggestion together.',
  missions=[dict(who='A', role='Travelers', mission='Find three places that everyone in your group has been to, or three that nobody has visited.', constraint='Ask at least two Have you ever…? questions.', start='Have you ever been to…'),
            dict(who='B', role='Food explorers', mission='Find one food everyone has tried and one nobody has tried. Recommend one.', constraint='Use “I’ve never…” and “What was it like?”', start='Have you ever tried…'),
            dict(who='C', role='Adventure team', mission='Find one thing nobody has done and invent a group adventure.', constraint='Use “twice or a few times” and “for the first time”.', start='Have you ever…')], min=11,
  success=['Ask Have you ever… questions.', 'Answer with I’ve… or I’ve never…', 'Add one past detail.', 'Share the group result.'],
  teach=teach(goal='Usar experiências de vida para encontrar pontos em comum.', group=['Cada grupo recebe papéis e restrição.', 'Progressão: com chunks, só palavras-chave, sem roteiro.', 'Anote 2–3 correções prioritárias.'], answers=['Modelo: “Have you ever been to Mexico?” → “Yes, twice. It was great.” → “What was it like?”'], extra=['What did you learn about your classmates?'], support=['Dê o início de frase em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short message to a friend about one travel experience: where you have been, how many times and one detail.',
  steps=['Where', 'How many times', 'One detail', 'Question to the friend'],
  model='Hi Nina! I’ve been to Tokyo twice. The first time I went in spring, and it was beautiful. I’ve never eaten better ramen! Have you ever been to Asia?',
  checklist=['I used I’ve been to…', 'I said how many times.', 'I added a past detail.', 'I asked a Have you ever… question.'],
  tip='Fix only 2–3 priority points and show a more natural way to say the same idea.', fix=dict(n=3),
  teach=teach(goal='Produção escrita curta ligada à situação.', solo=['Corrija 2–3 pontos prioritários.'], group=['Troquem os textos entre colegas.'], extra=['Add one more experience to your message.'], errors=[E('I have been to Tokyo in 2022.', 'I went to Tokyo in 2022. / I’ve been to Tokyo.'), E('I have never ate it.', 'I’ve never eaten it.')], support=['Dê o modelo e peça só para trocar os dados.'])),
 fb_page('Example: You used “I’ve been to” and added a detail in the past.', 'Example: Reduce “have you ever” so it sounds natural.', 'Example: Tell a travel story of one minute without notes.', 'experiências com present perfect e passado simples.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❓', name='Ask about experience', prompt='Without notes: ask if your partner has been to Canada.', model='Have you ever been to Canada?'), dict(ic='💬', name='Answer with a number', prompt='You went to Rome two times. Answer “Have you been to Rome?”', model='Yes, I’ve been twice.'), dict(ic='⭐', name='Say what you never did', prompt='Say you have not tried sushi.', model='I’ve never tried sushi.')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 45–60 second audio telling one travel experience.', 'Write three sentences: two with I’ve… and one with I’ve never…', 'Review the four expressions ★ and create your own examples.', 'Listen to the dialogue again and find two details in the past.']),
  spaced=dict(next=['Have you ever…?', 'I’ve never…', 'I’ve been to…'], week=['What was it like?', 'twice / a few times', 'Would you like to…?'], unit=['Invite · tell experiences · share news']),
  teach=teach(goal='Toda aula termina com uma produção observável.', solo=['Sem anotações: perguntar, responder com número e dizer algo que nunca fez.'], group=['Exit challenge individual.'], answers=['Have you ever been to Canada? · Yes, I’ve been twice. · I’ve never tried sushi.'], extra=['Revisão espaçada: próxima aula, uma semana depois e na missão da unidade.'])),
 lv_page([('I go Japan. Nice!', 'Name a place and an opinion in short phrases.'), ('I’ve been to Japan twice. It was great.', 'Talk about experiences with I’ve been / never.'), ('I’ve been to Japan twice, and I’d really like to go back in autumn.', 'Connect experiences to plans.'), ('Having been to Japan twice, I can say the trains are even better than people claim.', 'Add comparison and evaluation.'), ('Having travelled there a couple of times, I can honestly say it changed how I think about public space.', 'Reflect on experiences with nuance.'), ('Few trips have left me as quietly astonished as those two weeks in Kyoto.', 'Narrate experiences with stylistic control.')])
]
LESSON = mk(88, 2, 'Experiences (present perfect)', 'Experiências de vida', ['Raj', 'Nina'], 'cafe', 'day', PAGES, DIALOG)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
