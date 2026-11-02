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

DIALOG = dict(speakers={'Tourist': {'name': 'Raj'}, 'Guide': {'name': 'Cleo'}}, lines=[
 dict(who='Tourist', en='Excuse me, **could you tell me how to get to** the Central Library?', pt='Com licença, você poderia me dizer como chegar à Biblioteca Central?'),
 dict(who='Guide', en='Sure! **Go straight** on this street for two blocks.', pt='Claro! Siga reto por esta rua por dois quarteirões.'),
 dict(who='Tourist', en='Two blocks. And then?', pt='Dois quarteirões. E depois?'),
 dict(who='Guide', en='Then **turn left at the** bank. You’ll see a big fountain on your right.', pt='Depois vire à esquerda no banco. Você vai ver uma grande fonte à sua direita.'),
 dict(who='Tourist', en='Is it far? Should I take a bus?', pt='É longe? Devo pegar um ônibus?'),
 dict(who='Guide', en='No, it’s a five-minute walk. **Walk past** the fountain and it’s on the corner, across from the post office.', pt='Não, é uma caminhada de cinco minutos. Passe pela fonte e fica na esquina, em frente ao correio.'),
 dict(who='Tourist', en='Straight two blocks, left at the bank, past the fountain. Got it.', pt='Reto dois quarteirões, esquerda no banco, passando a fonte. Entendi.'),
 dict(who='Guide', en='Perfect. **You can’t miss it** — it has tall stone columns.', pt='Perfeito. Você não tem como errar: tem colunas altas de pedra.'),
 dict(who='Tourist', en='Thanks so much! You’ve been really helpful.', pt='Muito obrigado! Você foi muito prestativa.')])

PAGES = [
 dict(t='rl_open', stage='warm', title='Detailed directions', pt='Direções detalhadas', level='A2', unit=unit(4),
  situation=dict(text='You are in a city you do not know. You ask a stranger how to get to a place and check that you understood each step.', scene='city', tod='day', cast=['Cleo', 'Raj']),
  goal='By the end of the class you can ask for directions, follow several steps using landmarks and confirm what you understood.',
  canDo=['Ask: Could you tell me how to get to…?', 'Understand Go straight / Turn left at…', 'Use landmarks: past, across from, on the corner', 'Repeat the steps to check: Got it?'],
  success=['I ask for directions politely.', 'I understand the steps.', 'I repeat to confirm.', 'I thank the person.'],
  think='When someone gives you directions in Portuguese, do you use street names, distances or landmarks? Which one helps you most?',
  teach=teach(goal='Abrir pela situação: perguntar e entender direções detalhadas.', solo=['Peça ao estudante que descreva como chega ao seu trabalho.', 'Mostre os 4 critérios.'], group=['Cada estudante cita um lugar perto da escola/casa.', 'Anote no quadro como landmarks.'], extra=['Do you use maps on your phone?', 'Have you ever been lost in a new city?'], support=['Aceite palavras soltas e reformule em frases.'])),
 dict(t='rl_warm', stage='warm', title='Connection & warm-up',
  intro=dict(solo='Ask about the student’s neighborhood and recycle story language.', group='One question per student, then a question back to a classmate.'),
  recall='Telling stories (class 89): “I was… when…”. Ask: What were you doing when you last got lost?',
  qs=[dict(q='How do you get to work or school?', pt='Como você vai para o trabalho ou a escola?', sup=['By bus.', 'On foot.', 'By car.']),
      dict(q='What is there near your home?', pt='O que tem perto da sua casa?', sup=['A supermarket.', 'A park.', 'A bakery.']),
      dict(q='Do you ask people or use your phone to find places?', pt='Você pergunta às pessoas ou usa o celular para achar lugares?', sup=['My phone.', 'I ask people.', 'Both.'])],
  tip='Note the place words the student already knows; they become landmarks in the lesson.',
  teach=teach(goal='Ativar vocabulário de lugares e transporte.', extra=['What is the best place in your neighborhood?', 'What is your favorite landmark in your city?'], errors=[E('I go to work by foot.', 'I go to work on foot. / I walk to work.'), E('It has a bakery near of my house.', 'There is a bakery near my house.')], support=['Use as respostas-chip.'])),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Landmarks',
  intro='People explain routes in different ways around the world. Look and guess before you read.',
  cards=[dict(vis='prop:map', en='Count the blocks', pt='Conte os quarteirões', note='In many U.S. cities with grid streets, people say “two blocks” and “turn left at the corner”.'),
         dict(vis='prop:compass', en='Left, right or straight', pt='Esquerda, direita ou reto', note='Simple directions work in almost every situation: go straight, turn left, turn right.'),
         dict(vis='prop:bus', en='Landmarks help', pt='Pontos de referência ajudam', note='“Turn left at the bank” is easier to follow than a street name you cannot see.')],
  qs=[dict(q='Why are landmarks useful in directions?', pt='Por que pontos de referência ajudam?', levels=dict(A1='You can see them.', A2='They are easy to see and remember.', B1='A visible bank or fountain is easier to find than a street name.', B2='Landmarks give visual confirmation that you are on the right route, especially for visitors.')),
      dict(q='What does “You can’t miss it” mean?', pt='O que significa “You can’t miss it”?', levels=dict(A1='It is easy to find.', A2='It is easy to see, so you will find it.', B1='The place is very noticeable, so you should not have trouble finding it.', B2='It reassures the listener that the place is obvious, though it is not a guarantee.')),
      dict(q='How can you check that you understood?', pt='Como confirmar que entendeu?', levels=dict(A1='Repeat it.', A2='Repeat the steps: “Straight, then left…”', B1='Summarize the route and ask “Is that right?”', B2='Paraphrase the main steps and ask for confirmation of the one you are least sure about.'))],
  compare='In Brazil, directions often use landmarks too (“depois da padaria, vira à esquerda”) and “é logo ali”. In English, “just around the corner” and “a five-minute walk” are the equivalent. What do you say?',
  teach=teach(goal='Mostrar como as direções são dadas: blocos, esquerda/direita e pontos de referência.', solo=['Mostre os 3 cartões e peça hipóteses.', 'Compare com “é logo ali”.'], group=['Cada estudante escolhe um cartão e explica.', 'Pergunte “Do you agree?”.'], answers=['Q1: easy to see and remember.', 'Q2: easy to see.', 'Q3: repeat the steps.'], extra=['Do you prefer maps or spoken directions?', 'What is the most famous landmark near you?'], support=['Use as respostas A1.'], stretch=['B2: explique por que repetir ajuda a evitar erros.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='city', tod='day', cast=['Cleo', 'Raj']),
  pass1=dict(q='What does Raj want?', pt='O que o Raj quer?', opts=['To find a place', 'To buy a ticket', 'To rent a room'], ans=0),
  pass2=dict(tasks=[dict(label='Place', ans='Central Library', alt=['library']), dict(label='Blocks to go straight', ans='two blocks', alt=['two', '2']), dict(label='Turn left at the…', ans='bank'), dict(label='Landmark on the right', ans='fountain'), dict(label='Walking time', ans='five-minute', alt=['five', '5'])]),
  teach=teach(goal='Entender as direções e anotar cada passo.', solo=['Esconda o texto. 1ª escuta: objetivo.', '2ª escuta: lugar, quarteirões, banco, fonte, tempo.'], group=['Escuta coletiva; duplas desenham o caminho antes de revelar.', 'Mostre o texto no final.'], answers=['Pass 1: to find a place.', 'Pass 2: Central Library · two blocks · bank · fountain · five-minute walk.'], extra=['Is the library on the left or right?', 'Does Raj need a bus?'], support=['Use “Slow” e pause após cada passo.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='How far should Raj go straight?', opts=['Two blocks', 'Five blocks', 'One block'], ans=0), dict(q='Where does Raj turn left?', opts=['At the bank', 'At the library', 'At the bus stop'], ans=0), dict(q='What is across from the library?', opts=['The post office', 'The fountain', 'The bank'], ans=0), dict(q='How does the library look?', opts=['It has tall stone columns', 'It is yellow', 'It is very small'], ans=0)],
  retell=dict(prompt='Explain the route to a friend, step by step.', starters=['First, go straight…', 'Then turn left at…', 'Walk past…', 'You can’t miss…']),
  teach=teach(goal='Ler o diálogo e recontar a rota passo a passo.', solo=['O estudante lê Raj; você lê Cleo; depois troquem.', 'Peça que desenhe a rota.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia: um passo por estudante.'], answers=['Two blocks · At the bank · The post office · Tall stone columns'], extra=['Would you go by bus? Why not?', 'What can go wrong with directions?'], errors=[E('Go straight two block.', 'Go straight for two blocks.'), E('Turn on left.', 'Turn left.')], support=['Mostre a tradução (PT) após a 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[dict(en='Could you tell me how to get to…?', pt='Você poderia me dizer como chegar a…?', use='Ask for directions politely.', reg='polite', alt='Casual: **How do I get to…?**', pri=True),
         dict(en='Go straight.', pt='Siga reto.', use='Continue in the same direction.', reg='neutral', alt='Also: **Keep going straight.**', pri=True),
         dict(en='Turn left / right at the…', pt='Vire à esquerda / direita no(a)…', use='Change direction at a landmark.', reg='neutral', pri=True),
         dict(en='You can’t miss it.', pt='Você não tem como errar.', use='Say the place is easy to find.', reg='casual', pri=True),
         dict(en='Walk past the…', pt='Passe pelo(a)…', use='Pass something without turning.', reg='neutral'),
         dict(en='It’s on the corner.', pt='Fica na esquina.', use='Tell where the place is.', reg='neutral'),
         dict(en='across from the…', pt='em frente ao(à)…', use='Describe a position.', reg='neutral', alt='Also: **opposite the…** (more British)'),
         dict(en='It’s a five-minute walk.', pt='É uma caminhada de cinco minutos.', use='Give the time on foot.', reg='neutral')],
  discover=dict(fns=['Asking', 'Moving', 'Turning', 'Describing place', 'Reassuring'],
   items=[dict(en='Could you tell me how to get to the station?', fn='Asking'), dict(en='Go straight for two blocks.', fn='Moving'), dict(en='Turn right at the bank.', fn='Turning'), dict(en='It’s across from the post office.', fn='Describing place'), dict(en='You can’t miss it.', fn='Reassuring')]),
  note='Choose the 4 starred expressions to use again and again; the others add detail to the route.',
  teach=teach(goal='Escolher 4 chunks prioritários e usá-los num mapa.', solo=['Use um mapa simples e mostre cada chunk.', 'Peça frases próprias.'], group=['Cada estudante escolhe um chunk e dá uma direção.', 'Duplas: um guia o outro no mapa.'], answers=['Asking · Moving · Turning · Describing place · Reassuring'], extra=['Which of these would you use to a child?'], errors=[E('Go straight ahead until the end of the street and turn left in the bank.', 'Go straight to the end, then turn left at the bank.'), E('It is in front of the post office. (confusão com “across from”)', 'It’s across from the post office.')], support=['Trabalhe só as 4 expressões ★.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Giving directions (imperative)', formula='**Go straight / Turn left / Walk past** + place', ex=['Go straight for two blocks.', 'Turn left at the bank.', 'Walk past the fountain.'], main=True),
            dict(name='Describing position', formula='**It’s** + on the corner / across from / next to + place', ex=['It’s on the corner.', 'It’s across from the post office.', 'It’s next to the bank.'], main=True),
            dict(name='Asking politely', formula='**Could you tell me how to get to** + place?', ex=['Could you tell me how to get to the library?', 'Could you tell me where the station is?'])],
  swap=dict(frame='Turn {direction} {landmark}.', tpt='Vire à {direction} {landmark}.',
   slots=[dict(k='direction', label='Direction', opts=[dict(en='left', pt='esquerda'), dict(en='right', pt='direita'), dict(en='around', pt='para o outro lado')]),
          dict(k='landmark', label='Landmark', opts=[dict(en='at the bank', pt='no banco'), dict(en='at the fountain', pt='na fonte'), dict(en='at the gas station', pt='no posto de gasolina')])]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['Go straight, then left at the bank.', 'Proceed straight ahead, then turn left at the bank.'], ['You can’t miss it.', 'The building is easy to identify.'], ['It’s just around the corner.', 'It is located a short distance away.'], ['Got it, thanks!', 'I understand, thank you.']], note='Directions are almost always spoken in short imperative sentences.'),
  teach=teach(goal='Imperativos curtos e preposições de lugar; pedir educadamente com “Could you…”.', solo=['Mostre no diálogo.', 'Use “Swap the words” com um mapa.'], group=['Troca em cadeia: cada estudante muda UMA peça.', 'Duplas: um descreve, o outro desenha.'], answers='Padrões 01/02 são o foco; 03 é expansão.', extra=['Give me directions from this room to the door.', 'Where is the nearest bank?'], errors=[E('Turn to the left in the bank.', 'Turn left at the bank.'), E('It’s in front the post office.', 'It’s across from the post office.'), E('Go straight two blocks.', 'Go straight for two blocks.')], support=['Fique só com Go straight / Turn left at…'], stretch=['Combine 3 passos em um parágrafo.'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Sentence stress', tip='In directions the stressed words are the ones that carry the route: “Turn LEFT at the BANK”. Small words are weak and quick.',
  items=[dict(say='Turn left at the bank.', linked='TURN LEFT at the BANK.', ipa='/tɝn lɛft/', rhythm='OOooO'), dict(say='Go straight for two blocks.', linked='GO STRAIGHT fer two BLOCKS.', ipa='/streɪt/', rhythm='OOoOO'), dict(say='You can’t miss it.', linked='You CAN’T MISS it.', ipa='/kænt/', rhythm='oOOo')],
  identify=[dict(q='Which one do you hear?', opts=['Turn left at the bank.', 'Turn right at the bank.', 'Turn left at the park.'], ans=0, say='Turn left at the bank.'), dict(q='Which one do you hear?', opts=['Go straight for two blocks.', 'Go straight for three blocks.', 'Go straight for two clocks.'], ans=0, say='Go straight for two blocks.')],
  own=dict(prompt='Write a three-step direction from your home to a nearby place.', criteria='Say it twice: slowly, then with strong key words. Could your partner follow the route?'),
  teach=teach(goal='UM só fenômeno: acento de frase nas palavras que carregam a rota.', solo=['Escutar e identificar → repetir → rota própria.', 'Bata palmas nas sílabas fortes.'], group=['Coro, depois duplas.', 'Cada estudante dá uma direção.'], answers=['Identify 1: left at the bank · Identify 2: two blocks'], errors=[E('Pronunciar todas as palavras com a mesma força', 'Acentue LEFT e BANK'), E('“left” e “right” confundidos por falta de ênfase', 'Enfatize a direção')], support=['Reduza a velocidade e conte as batidas.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    dict(type='mcq', q='1. You need the library. What do you ask?', opts=['Could you tell me how to get to the library?', 'Where I go library?', 'You know library?'], ans=0, why='Could you tell me how to get to… is polite.'),
    dict(type='mcq', q='2. Which instruction means “continue”?', opts=['Go straight.', 'Turn around.', 'Stop here.'], ans=0, why='Go straight = continue ahead.'),
    dict(type='mcq', q='3. The cafe is on the other side of the street from the bank.', opts=['It’s across from the bank.', 'It’s inside the bank.', 'It’s behind in bank.'], ans=0, why='across from = on the opposite side.'),
    dict(type='mcq', q='4. Someone says “You can’t miss it.” What does it mean?', opts=['It is easy to find.', 'It is closed.', 'You must not go.'], ans=0, why='It is very noticeable.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    dict(type='gap', text='Go straight ___ two blocks.', ans='for', bank=['for', 'in', 'to'], why='for + distance.'),
    dict(type='gap', text='Turn left ___ the bank.', ans='at', bank=['at', 'in', 'on'], why='turn left at + landmark.'),
    dict(type='swap', instr='Make it a polite question:', frm='How do I get to the station?', ans=['Could you tell me how to get to the station?'], model='Could you tell me how to get to the station?', why='Could you tell me how to… is more polite.'),
    dict(type='swap', instr='Give the opposite direction:', frm='Turn left at the bank.', ans=['Turn right at the bank.'], model='Turn right at the bank.', why='left ↔ right.'),
    dict(type='reply', npc='Go straight two blocks, then turn left at the bank.', q='Choose the best confirmation.', opts=['Straight two blocks, left at the bank. Got it, thanks!', 'No, I turn right.', 'Bank is money.'], ans=0, why='Repeat the steps to confirm.')])],
  teach=teach(goal='Do controlado ao guiado antes da fala livre.', solo=['Peça que justifique cada resposta.', 'Peça que desenhe a rota de cada resposta.'], group=['Duplas comparam antes de revelar.', 'Pontos por resposta justificada.'], answers=['1: Could you tell me how to get to the library? · 2: Go straight. · 3: It’s across from the bank. · 4: It is easy to find.', 'Gap: for · at · Could you tell me how to get to the station? · Turn right at the bank. · Straight two blocks…'], extra=['Say each answer with strong key words.'], errors=[E('Turn in left.', 'Turn left.'), E('Is far?', 'Is it far?')], support=['Ofereça o banco de palavras.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — ask for and give directions',
  brief=dict(teacher='You are a local with a map. Give directions and change a landmark halfway.', student='You are a visitor: ask, repeat to confirm and ask one more question.'),
  orders=['To the Central Library', 'To a pharmacy', 'To the train station'],
  complications=['The local says “turn left” but you see a road closed.', 'You do not remember the second step.', 'The local speaks fast: ask to repeat.', 'You need an alternative: a bus instead of walking.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['Could you tell me how to get to…?', 'Go straight…', 'Turn left at…', 'You can’t miss it.']), dict(label='Keywords', desc='Only the keywords', help=['two blocks', 'bank', 'fountain', 'corner'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I ask for directions politely.', 'I understand the steps.', 'I repeat to confirm.', 'I thank the person.'],
  teach=teach(goal='Simular o pedido e a explicação de rota, com confirmação.', solo=['Use um mapa do bairro real do aluno.', 'Rodada 1 com chunks, 2 palavras-chave, 3 livre.', 'Anote 2–3 correções.'], extra=['What if the street is closed?', 'How do you ask someone to repeat?'], errors=[E('Where is the library, please? (seco)', 'Excuse me, could you tell me where the library is?')], support=['Volte à rodada 1 se travar.'], stretch=['Dê direções com 5 passos e dois pontos de referência.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Simple routes', min=3, task='Give two-step directions from the classroom to a place.', hint='Go straight… / Turn left…'), dict(title='Use landmarks', min=3, task='Add at least two landmarks to your directions.', hint='Walk past… / across from…'), dict(title='Check and repeat', min=3, task='Listener repeats the route to confirm.', hint='So, straight and then left. Right?'), dict(title='Best route', min=2, whole=True, task='Whole group: each pair shares the clearest route.', hint='We said…')],
  infogap=dict(title='City map', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='Student A: your map notes', task='You know where the Bank and the Post office are. Ask about the rest.', rows=[dict(k='Bank', v='on Main Street, next to the park'), dict(k='Library', v=''), dict(k='Post office', v='on Oak Street, across from the library'), dict(k='Café', v='')]),
   b=dict(title='Student B: your map notes', task='You know where the Library and the Café are. Ask about the rest.', rows=[dict(k='Bank', v=''), dict(k='Library', v='on Oak Street, on the corner of 2nd'), dict(k='Post office', v=''), dict(k='Café', v='on Main Street, next to the bank')])),
  teach=teach(goal='Fluência em dar e receber direções com informações novas.', group=['Troque os pares a cada rodada.', 'Responsabilidade individual: cada aluno pergunta e responde uma vez.', 'Sem salas simultâneas.'], answers=['Info gap: A tem Bank e Post office; B tem Library e Café. Cada um completa perguntando “Where is the…?”.'], extra=['Where is the café?', 'What is across from the library?'], errors=[E('Where is library? (sem artigo)', 'Where is the library?'), E('It is at left.', 'It’s on the left.')], support=['Entregue frases-modelo no chat.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — find the way',
  goal='Each group must give clear directions with landmarks and check that the listener understood.',
  missions=[dict(who='A', role='Tourists and local', mission='A tourist asks for the station. The local gives three steps with landmarks.', constraint='Use “Could you tell me how to get to…?” and “You can’t miss it.”', start='Excuse me, could you tell me…'),
            dict(who='B', role='Guides', mission='Guide a blindfolded classmate across the room with directions only.', constraint='Use “Go straight” and “Turn left / right” and “Stop”.', start='Go straight…'),
            dict(who='C', role='Map makers', mission='Listen to your partner and draw the route; then compare drawings.', constraint='Repeat each step: “Straight two blocks, then left…”', start='First, go straight…')], min=11,
  success=['Ask or give directions politely.', 'Use at least two landmarks.', 'Repeat to confirm.', 'Reach the place.'],
  teach=teach(goal='Dar direções claras e confirmar a compreensão.', group=['Cada grupo recebe papéis e restrição.', 'Progressão: com chunks, palavras-chave, sem roteiro.', 'Anote 2–3 correções.'], answers=['Modelo: “Could you tell me how to get to the station?” → “Go straight two blocks, then turn left at the bank.” → “Got it, thanks!”'], extra=['What was the hardest step to explain?'], support=['Dê o início de frase em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a message to a friend explaining how to get from the station to your home or favorite café.',
  steps=['Start', 'Steps with landmarks', 'Final landmark', 'Closing'],
  model='Hi Raj! From the station, go straight for two blocks, then turn left at the bank. Walk past the fountain and the café is on the corner, across from the post office. You can’t miss it! See you soon.',
  checklist=['I used at least three steps.', 'I used Go straight / Turn left / Walk past.', 'I used a landmark.', 'I closed with “You can’t miss it” or similar.'],
  tip='Fix only 2–3 priority points and show a more natural way to say the same idea.', fix=dict(n=3),
  teach=teach(goal='Produção escrita curta: dar direções por escrito.', solo=['Corrija 2–3 pontos prioritários.'], group=['Troquem os textos; o colega desenha a rota.'], extra=['Add a landmark you can see from the street.'], errors=[E('Turn to the left at the bank.', 'Turn left at the bank.'), E('You can not miss.', 'You can’t miss it.')], support=['Dê o modelo e peça só para trocar os dados.'])),
 fb_page('Example: You gave steps in order and used landmarks.', 'Example: Stress LEFT and BANK so the route is clear.', 'Example: Give directions in two minutes without a map.', 'direções claras e confirmação.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❓', name='Ask politely', prompt='Without notes: ask how to get to the bank.', model='Could you tell me how to get to the bank?'), dict(ic='💬', name='Give two steps', prompt='Tell someone to go straight two blocks and turn right at the park.', model='Go straight two blocks, then turn right at the park.'), dict(ic='⭐', name='Confirm', prompt='Repeat the directions to check them.', model='So, straight two blocks, then left at the bank. Got it, thanks!')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 45–60 second audio giving directions from your home to a landmark.', 'Write the route in three steps.', 'Review the four expressions ★ and create your own examples.', 'Listen to the dialogue again and draw the route.']),
  spaced=dict(next=['Could you tell me how to get to…?', 'Go straight', 'Turn left at the…'], week=['You can’t miss it.', 'across from', 'I was… when…'], unit=['Invite · tell experiences · stories · directions']),
  teach=teach(goal='Toda aula termina com uma produção observável.', solo=['Sem anotações: pedir, dar e confirmar direções.'], group=['Exit challenge individual.'], answers=['Could you tell me how to get to the bank? · Go straight two blocks, then turn right at the park. · Got it, thanks!'], extra=['Revisão espaçada: próxima aula, uma semana depois e na missão da unidade.'])),
 lv_page([('Where library?', 'Ask for a place with a few words.'), ('Could you tell me how to get to the library?', 'Ask politely and follow simple steps.'), ('Go straight for two blocks, then turn left at the bank; it’s across from the post office.', 'Give clear directions with landmarks.'), ('If you take the second street on the left, you’ll see the library right after the fountain.', 'Add conditions and sequence.'), ('You’re about ten minutes away on foot, though if the street is closed, it may be quicker to cut through the park.', 'Anticipate problems and give alternatives.'), ('It’s not the most obvious route, but if you trust the river, you’ll find it tucked behind the old columns.', 'Give nuanced and imaginative directions.')])
]
LESSON = mk(90, 4, 'Detailed directions', 'Direções detalhadas', ['Cleo', 'Raj'], 'city', 'day', PAGES, DIALOG)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
