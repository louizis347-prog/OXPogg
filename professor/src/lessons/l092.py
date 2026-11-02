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

DIALOG = dict(speakers={'Visitor': {'name': 'Carlos'}, 'Friend': {'name': 'Hana'}}, lines=[
 dict(who='Visitor', en='Hana, this fair is so lively! **What do people usually do** for festivals in Korea?', pt='Hana, esta feira está tão animada! O que as pessoas costumam fazer nos festivais na Coreia?'),
 dict(who='Friend', en='**In my country,** we celebrate Seollal, the Lunar New Year. **People usually** wear hanbok and visit their families.', pt='No meu país, comemoramos o Seollal, o Ano Novo Lunar. As pessoas costumam usar hanbok e visitar a família.'),
 dict(who='Visitor', en='Nice! What do you eat then?', pt='Legal! O que vocês comem nessa data?'),
 dict(who='Friend', en='**We eat** tteokguk, a rice cake soup. We also bow to our elders to show respect.', pt='Comemos tteokguk, uma sopa de bolinho de arroz. Também fazemos reverência aos mais velhos para mostrar respeito.'),
 dict(who='Visitor', en='Interesting! **In Spain,** on New Year’s Eve, we eat twelve grapes at midnight.', pt='Interessante! Na Espanha, na véspera de Ano Novo, comemos doze uvas à meia-noite.'),
 dict(who='Friend', en='Twelve grapes? Why?', pt='Doze uvas? Por quê?'),
 dict(who='Visitor', en='One grape for each chime of the clock. **It’s supposed to** bring good luck for the new year.', pt='Uma uva para cada badalada do relógio. Dizem que traz sorte para o ano novo.'),
 dict(who='Friend', en='I love that! We don’t do that in Korea, but I’d like to try it.', pt='Adorei! Não fazemos isso na Coreia, mas eu gostaria de experimentar.'),
 dict(who='Visitor', en='Come to my place next December. **We’ll celebrate** together!', pt='Venha à minha casa em dezembro. Vamos comemorar juntos!')])

PAGES = [
 dict(t='rl_open', stage='warm', title='Traditions and festivals', pt='Tradições e festivais', level='A2', unit=unit(6),
  situation=dict(text='At a fair you meet someone from another country. You explain a tradition from your culture, ask about theirs and compare them respectfully.', scene='fairground', tod='day', cast=['Hana', 'Carlos']),
  goal='By the end of the class you can describe a tradition (when, what people do and eat), ask about another culture and compare politely.',
  canDo=['Start with In my country…', 'Say what people usually do', 'Explain the meaning: It’s supposed to…', 'Ask and compare with curiosity'],
  success=['I describe a tradition.', 'I explain what people usually do.', 'I ask about their tradition.', 'I compare respectfully.'],
  think='What is one tradition in your family or city that visitors would find interesting? How would you explain it in English?',
  teach=teach(goal='Abrir pela situação: explicar uma tradição e conhecer a de outro.', solo=['Peça uma tradição que o aluno gosta.', 'Mostre os 4 critérios.'], group=['Cada estudante cita um festival ou data especial.', 'Anote no quadro.'], extra=['What is your favorite holiday?', 'What do you eat on special days?'], support=['Aceite palavras soltas e reformule em frases.'])),
 dict(t='rl_warm', stage='warm', title='Connection & warm-up',
  intro=dict(solo='Ask about holidays and family gatherings, and recycle news sharing.', group='One question per student, then a question back to a classmate.'),
  recall='News and events (class 91): “Did you hear about…?”. Ask: Did you hear about any event in your city?',
  qs=[dict(q='What is your favorite holiday?', pt='Qual é o seu feriado favorito?', sup=['Christmas.', 'Carnival.', 'My birthday.']),
      dict(q='What do you usually do on that day?', pt='O que você costuma fazer nesse dia?', sup=['I visit family.', 'I eat special food.', 'I rest.']),
      dict(q='Who do you celebrate with?', pt='Com quem você comemora?', sup=['My family.', 'Friends.', 'Alone.'])],
  tip='Collect the holidays the student mentions; they are the base for the tradition talk.',
  teach=teach(goal='Ativar vocabulário de feriados e comemorações.', extra=['What is a tradition you do not like?', 'What did you do last New Year’s Eve?'], errors=[E('In my country we have the habit of…', 'In my country, people usually…'), E('I celebrate in the family.', 'I celebrate with my family.')], support=['Use as respostas-chip.'])),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Sharing traditions',
  intro='Talking about traditions is a warm way to connect with people from other cultures. Look and guess before you read.',
  cards=[dict(vis='flag:kr', en='Seollal in Korea', pt='Seollal na Coreia', note='Families gather for the Lunar New Year, bow to elders and eat tteokguk.'),
         dict(vis='flag:es', en='Twelve grapes in Spain', pt='Doze uvas na Espanha', note='On New Year’s Eve many people eat twelve grapes at midnight, one for each chime.'),
         dict(vis='prop:cake', en='Food tells a story', pt='A comida conta uma história', note='Special dishes often carry meaning: luck, family or respect.')],
  qs=[dict(q='Why do people say “usually” when describing traditions?', pt='Por que se diz “usually” ao descrever tradições?', levels=dict(A1='Not everybody does it.', A2='Because not everyone does the same thing.', B1='It avoids generalizing: traditions vary between families and regions.', B2='It acknowledges variation within a culture and keeps the description accurate and respectful.')),
      dict(q='How can you show interest in someone’s tradition?', pt='Como demonstrar interesse na tradição de alguém?', levels=dict(A1='Ask: Why?', A2='Ask “What do you eat?” and “Why?”', B1='Ask about the meaning and say you would like to try it.', B2='Ask open questions about meaning and personal experience, and avoid judging.')),
      dict(q='Which word is better: “strange” or “different”?', pt='Qual palavra é melhor: “strange” ou “different”?', levels=dict(A1='Different.', A2='“Different” is more polite.', B1='“Different” or “interesting” is more respectful than “strange”.', B2='“Strange” can sound judgmental; “different”, “unfamiliar” or “interesting” keep a respectful tone.'))],
  compare='In Brazil, people share traditions such as New Year’s Eve clothes in white and festas juninas. In English you say “In my country…” and “People usually…”. What tradition would you present?',
  teach=teach(goal='Mostrar como descrever tradições com respeito e curiosidade.', solo=['Mostre os 3 cartões e peça hipóteses.', 'Pergunte que tradição brasileira o aluno apresentaria.'], group=['Cada estudante escolhe um cartão e explica.', 'Pergunte “Do you agree?”.'], answers=['Q1: because not everybody does it.', 'Q2: ask what and why.', 'Q3: different / interesting.'], extra=['What is a tradition from your region?', 'What would you ask a visitor about their traditions?'], support=['Use as respostas A1.'], stretch=['B2: discuta como não generalizar sobre uma cultura.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='fairground', tod='day', cast=['Hana', 'Carlos']),
  pass1=dict(q='What are Hana and Carlos comparing?', pt='O que Hana e Carlos comparam?', opts=['New Year traditions', 'Train schedules', 'Job offers'], ans=0),
  pass2=dict(tasks=[dict(label='Hana’s festival', ans='Seollal'), dict(label='Traditional clothes', ans='hanbok'), dict(label='Food', ans='tteokguk'), dict(label='Carlos’s grapes', ans='twelve', alt=['12']), dict(label='When he eats them', ans='midnight')]),
  teach=teach(goal='Entender a conversa e 5 informações.', solo=['Esconda o texto. 1ª escuta: tema.', '2ª escuta: festival, roupa, comida, uvas e horário.'], group=['Escuta coletiva; duplas anotam antes de revelar.', 'Mostre o texto no final.'], answers=['Pass 1: New Year traditions.', 'Pass 2: Seollal · hanbok · tteokguk · twelve · midnight.'], extra=['Which tradition do you like more?', 'Are the traditions similar?'], support=['Use “Slow” e pause após cada fala.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='What festival does Hana describe?', opts=['Seollal', 'Carnival', 'Halloween'], ans=0), dict(q='What do people eat at Seollal, according to Hana?', opts=['Tteokguk', 'Pizza', 'Tacos'], ans=0), dict(q='How many grapes does Carlos eat?', opts=['Twelve', 'Ten', 'One'], ans=0), dict(q='What is the grape tradition supposed to bring?', opts=['Good luck', 'Rain', 'Money only'], ans=0)],
  retell=dict(prompt='Retell the conversation and compare the two traditions.', starters=['In Korea, people…', 'In Spain, people…', 'They both…', 'Hana would like to…']),
  teach=teach(goal='Ler o diálogo, perceber os chunks e comparar as tradições.', solo=['O estudante lê Hana; você lê Carlos.', 'Peça que compare com uma tradição brasileira.'], group=['Leitura em duplas.', 'Reconto em cadeia.'], answers=['Seollal · Tteokguk · Twelve · Good luck'], extra=['Which tradition would you like to try?', 'What is similar to your country?'], errors=[E('In my country we do the Christmas.', 'In my country, we celebrate Christmas.'), E('People usually celebrates.', 'People usually celebrate.')], support=['Mostre a tradução (PT) após a 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[dict(en='In my country,…', pt='No meu país,…', use='Introduce a general custom.', reg='neutral', alt='Also: **Where I’m from,…**', pri=True),
         dict(en='People usually…', pt='As pessoas costumam…', use='Say what is common, not universal.', reg='neutral', alt='Also: **Many people…**', pri=True),
         dict(en='We celebrate…', pt='Nós comemoramos…', use='Name the festival.', reg='neutral', pri=True),
         dict(en='It’s supposed to bring good luck.', pt='Dizem que traz sorte.', use='Explain the meaning of a tradition.', reg='neutral', pri=True),
         dict(en='What do you eat?', pt='O que vocês comem?', use='Ask about food traditions.', reg='neutral'),
         dict(en='to show respect', pt='para mostrar respeito', use='Explain why people do something.', reg='neutral'),
         dict(en='I’d like to try it.', pt='Eu gostaria de experimentar.', use='Show interest.', reg='polite'),
         dict(en='We don’t do that.', pt='Nós não fazemos isso.', use='Say something is not part of your culture.', reg='neutral')],
  discover=dict(fns=['Introducing a custom', 'Saying what is common', 'Explaining meaning', 'Showing interest', 'Comparing'],
   items=[dict(en='In my country, we celebrate Seollal.', fn='Introducing a custom'), dict(en='People usually visit their families.', fn='Saying what is common'), dict(en='It’s supposed to bring good luck.', fn='Explaining meaning'), dict(en='I’d like to try it.', fn='Showing interest'), dict(en='We don’t do that in Korea.', fn='Comparing')]),
  note='Choose the 4 starred expressions to use again and again; the others help you ask and compare.',
  teach=teach(goal='Escolher 4 chunks para descrever e perguntar sobre tradições.', solo=['Pergunte “When do you say it?”.', 'Peça uma tradição brasileira com cada chunk.'], group=['Cada estudante escolhe um chunk e dá um exemplo.', 'Duplas: apresentar uma tradição.'], answers=['Introducing · Common · Meaning · Interest · Comparing'], extra=['Which of these makes you sound respectful?'], errors=[E('Here in Brazil is a tradition to…', 'In Brazil, people usually…'), E('It suppose to bring luck.', 'It’s supposed to bring luck.')], support=['Trabalhe só as 4 expressões ★.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Describing a custom', formula='**In my country,** + present simple', ex=['In my country, we celebrate Seollal.', 'In Spain, we eat grapes at midnight.', 'In Brazil, we celebrate Carnival.'], main=True),
            dict(name='Saying what is usual', formula='**People usually** + verb', ex=['People usually visit their families.', 'People usually wear special clothes.', 'People usually eat together.'], main=True),
            dict(name='Explaining meaning', formula='**It’s supposed to** + verb / **to show** + noun', ex=['It’s supposed to bring good luck.', 'We bow to show respect.'])],
  swap=dict(frame='In {place}, people usually {custom}.', tpt='Em {place}, as pessoas costumam {custom}.',
   slots=[dict(k='place', label='Place', opts=[dict(en='Korea', pt='Coreia'), dict(en='Spain', pt='Espanha'), dict(en='Brazil', pt='Brasil')]),
          dict(k='custom', label='Custom', opts=[dict(en='celebrate with family', pt='comemorar com a família'), dict(en='eat special food', pt='comer comidas especiais'), dict(en='wear special clothes', pt='usar roupas especiais')])]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['In my country, we eat…', 'In my culture, it is customary to eat…'], ['It’s supposed to bring luck.', 'It is believed to bring good fortune.'], ['People usually go home.', 'It is common to return to one’s family.'], ['We don’t do that.', 'This is not a tradition where I come from.']], note='“It is believed to…” is common in written descriptions.'),
  teach=teach(goal='Descrever costumes com present simple e usually, e explicar significado.', solo=['Mostre os padrões no diálogo.', 'Use “Swap the words” em voz alta.'], group=['Troca em cadeia: cada estudante muda UMA peça.', 'Duplas: um descreve e o outro compara.'], answers='Padrões 01/02 são o foco; 03 é expansão.', extra=['Describe one tradition with “People usually…”.', 'Tell me why people do it.'], errors=[E('In my country people celebrates.', 'In my country, people celebrate.'), E('They usually are eating…', 'They usually eat…'), E('It’s suppose to…', 'It’s supposed to…')], support=['Fique só com In my country, + People usually…'], stretch=['Compare duas tradições em uma frase.'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Word stress', tip='In English one syllable is stronger: CELebrate, TRAdition, FESTival. The wrong stress can make a word hard to understand.',
  items=[dict(say='We celebrate the festival.', linked='We CEL·e·brate the FES·ti·val.', ipa='/ˈsɛləbreɪt/', rhythm='oOooooOoo'), dict(say='It’s a family tradition.', linked='It’s a FAM·i·ly tra·DI·tion.', ipa='/trəˈdɪʃən/', rhythm='ooOooooOo'), dict(say='People usually wear special clothes.', linked='PEO·ple U·su·al·ly wear SPE·cial clothes.', ipa='/ˈjuʒuəli/', rhythm='OoOoooOoo')],
  identify=[dict(q='Which stress do you hear?', opts=['TRAdition', 'traDItion', 'tradiTION'], ans=1, say='tradition'), dict(q='Which stress do you hear?', opts=['CELebrate', 'celeBRATE', 'celebRATE'], ans=0, say='celebrate')],
  own=dict(prompt='Write one sentence about a tradition with a three-syllable word.', criteria='Say it twice: mark the stressed syllable with your hand. Did the word sound natural?'),
  teach=teach(goal='UM só fenômeno: acento de palavra (celebrate, tradition, festival).', solo=['Escutar e identificar → repetir → frase própria.', 'Bata palmas na sílaba forte.'], group=['Coro, depois duplas.', 'Cada estudante diz uma frase.'], answers=['Identify 1: traDItion · Identify 2: CELebrate'], errors=[E('tradiTION (acento na última)', 'traDItion'), E('celeBRATE (acento no fim)', 'CELebrate')], support=['Reduza a velocidade e bata palmas.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    dict(type='mcq', q='1. You want to introduce a custom from your country.', opts=['In my country, we celebrate Carnival.', 'My country have Carnival.', 'In country my, Carnival.'], ans=0, why='In my country, + present simple.'),
    dict(type='mcq', q='2. Why use “usually” when describing traditions?', opts=['Not everyone does the same.', 'It means always.', 'It means never.'], ans=0, why='Usually avoids generalizing.'),
    dict(type='mcq', q='3. You want to say why people bow.', opts=['They bow to show respect.', 'They bow for respect to.', 'They bow respect show.'], ans=0, why='to + verb shows purpose.'),
    dict(type='mcq', q='4. A friend tells you about a tradition you don’t know.', opts=['That sounds interesting! What do you eat?', 'That is so strange.', 'I never do.'], ans=0, why='Show curiosity, not judgment.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    dict(type='gap', text='In my country, we ___ New Year’s Eve with fireworks.', ans='celebrate', bank=['celebrate', 'celebrates', 'celebrating'], why='We + base verb.'),
    dict(type='gap', text='People ___ wear special clothes at festivals.', ans='usually', bank=['usually', 'usual', 'use'], why='Adverb of frequency.'),
    dict(type='swap', instr='Add a reason with “to”:', frm='We bow. We show respect.', ans=['We bow to show respect.'], model='We bow to show respect.', why='to + verb for purpose.'),
    dict(type='swap', instr='Make it less absolute:', frm='People eat rice cake soup.', ans=['People usually eat rice cake soup.', 'Many people eat rice cake soup.'], model='People usually eat rice cake soup.', why='Use usually / many people.'),
    dict(type='reply', npc='In Spain, we eat twelve grapes at midnight.', q='Choose the best reaction.', opts=['Really? Why do you do that?', 'That is strange.', 'I am grapes.'], ans=0, why='Show interest and ask for the meaning.')])],
  teach=teach(goal='Do controlado ao guiado antes da fala livre.', solo=['Peça que justifique cada resposta.', 'Peça uma versão com a tradição do aluno.'], group=['Duplas comparam antes de revelar.', 'Pontos por resposta justificada.'], answers=['1: In my country, we celebrate Carnival. · 2: Not everyone does the same. · 3: They bow to show respect. · 4: That sounds interesting! What do you eat?', 'Gap: celebrate · usually · We bow to show respect. · People usually eat rice cake soup. · Really? Why do you do that?'], extra=['Say each answer with warm intonation.'], errors=[E('We celebrates.', 'We celebrate.'), E('That is strange.', 'That’s different! / That sounds interesting!')], support=['Ofereça o banco de palavras.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — share your tradition',
  brief=dict(teacher='You are a visitor from another country. Ask about the tradition and share one of yours.', student='Explain a real tradition: when, what people do, what they eat and what it means.'),
  orders=['A family holiday', 'A city or regional festival', 'A birthday or wedding tradition'],
  complications=['The visitor does not know a word: explain it.', 'You do not remember why people do it.', 'The visitor asks “Is it the same everywhere?”', 'The visitor says their tradition is different from yours: compare.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['In my country…', 'People usually…', 'We celebrate…', 'It’s supposed to…']), dict(label='Keywords', desc='Only the keywords', help=['family', 'food', 'luck', 'respect'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I describe a tradition.', 'I explain what people usually do.', 'I ask about their tradition.', 'I compare respectfully.'],
  teach=teach(goal='Apresentar uma tradição e comparar com respeito.', solo=['Use uma tradição real do aluno.', 'Rodada 1 com chunks, 2 palavras-chave, 3 livre.', 'Anote 2–3 correções.'], extra=['What if you do not know the origin?', 'How do you explain a word like “festa junina”?'], errors=[E('The festa junina is a party.', 'Festa junina is a June festival with food and dancing.')], support=['Volte à rodada 1 se travar.'], stretch=['Explique a tradição para uma criança e para um adulto.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='My tradition', min=3, task='Describe a tradition from your family or country.', hint='In my country, we…'), dict(title='Ask and answer', min=3, task='Ask what people eat and why.', hint='What do you eat? / Why…?'), dict(title='Compare', min=3, task='Find one similarity and one difference.', hint='We both… / We don’t…'), dict(title='Group festival', min=2, whole=True, task='Whole group: each pair shares the most interesting tradition.', hint='In X, people usually…')],
  infogap=dict(title='Festival guide', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='Student A: festival notes', task='You know La Tomatina and Las Fallas. Ask about the rest.', rows=[dict(k='La Tomatina', v='Buñol, Spain: people throw tomatoes in August'), dict(k='Seollal', v=''), dict(k='Las Fallas', v='Valencia, Spain: big sculptures, in March'), dict(k='Chuseok', v='')]),
   b=dict(title='Student B: festival notes', task='You know Seollal and Chuseok. Ask about the rest.', rows=[dict(k='La Tomatina', v=''), dict(k='Seollal', v='Korea: Lunar New Year, tteokguk'), dict(k='Las Fallas', v=''), dict(k='Chuseok', v='Korea: harvest festival, songpyeon')])),
  teach=teach(goal='Fluência em descrever e comparar festivais com informações novas.', group=['Troque os pares a cada rodada.', 'Responsabilidade individual: cada aluno descreve uma tradição.', 'Sem salas simultâneas.'], answers=['Info gap: A tem La Tomatina e Las Fallas; B tem Seollal e Chuseok. Fatos: La Tomatina em Buñol (Espanha) em agosto; Las Fallas em Valencia em março; Seollal é o Ano Novo Lunar coreano; Chuseok é a festa da colheita (songpyeon).'], extra=['Where is La Tomatina?', 'What do people eat at Chuseok?'], errors=[E('Where happens La Tomatina?', 'Where does La Tomatina happen?'), E('People throw tomatos.', 'People throw tomatoes.')], support=['Entregue frases-modelo no chat.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — a festival fair',
  goal='Each group must present a tradition and learn about one from another group.',
  missions=[dict(who='A', role='Presenters', mission='Prepare a 1-minute presentation of a tradition: when, what people do, what they eat.', constraint='Use “In my country…” and “People usually…”.', start='In my country, we celebrate…'),
            dict(who='B', role='Visitors', mission='Visit two stands, ask questions and report one difference.', constraint='Ask “What do you eat?” and say “I’d like to try it.”', start='Hi! What do people usually do…'),
            dict(who='C', role='Festival judges', mission='Listen to two presentations and decide which has the clearest explanation.', constraint='Use “It’s supposed to…” to explain a meaning.', start='In this tradition…')], min=11,
  success=['Describe a tradition.', 'Say what people usually do.', 'Ask a question.', 'Compare with respect.'],
  teach=teach(goal='Apresentar e ouvir tradições com respeito.', group=['Cada grupo recebe papéis e restrição.', 'Progressão: com chunks, palavras-chave, sem roteiro.', 'Anote 2–3 correções.'], answers=['Modelo: “In my country, we celebrate Festa Junina. People usually eat corn and dance.” → “I’d like to try it!”'], extra=['Which tradition was new to you?'], support=['Dê o início de frase em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short paragraph describing one tradition from your country or family and invite someone to join.',
  steps=['Name the tradition', 'What people usually do', 'Meaning', 'Invitation'],
  model='In my country, we celebrate Seollal, the Lunar New Year. People usually wear hanbok and visit their families. We eat tteokguk, and it’s supposed to bring a good year. Would you like to celebrate with us?',
  checklist=['I started with In my country…', 'I used People usually…', 'I explained the meaning.', 'I ended with an invitation.'],
  tip='Fix only 2–3 priority points and show a more natural way to say the same idea.', fix=dict(n=3),
  teach=teach(goal='Produção escrita curta: descrever uma tradição.', solo=['Corrija 2–3 pontos prioritários.'], group=['Troquem os textos; cada um faz uma pergunta sobre a tradição.'], extra=['Add what people eat.'], errors=[E('We celebrates the Christmas.', 'We celebrate Christmas.'), E('People usually are going to church.', 'People usually go to church.')], support=['Dê o modelo e peça só para trocar os dados.'])),
 fb_page('Example: You described the tradition and explained why people do it.', 'Example: Stress the first syllable of CELebrate and FESTival.', 'Example: Present a tradition for one minute without notes.', 'descrição de tradições com respeito.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❓', name='Introduce a tradition', prompt='Without notes: say you celebrate Carnival in your country.', model='In my country, we celebrate Carnival.'), dict(ic='💬', name='Say what people do', prompt='Say that people usually eat special food at festivals.', model='People usually eat special food at festivals.'), dict(ic='⭐', name='Explain the meaning', prompt='Say it brings good luck.', model='It’s supposed to bring good luck.')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 45–60 second audio describing a tradition.', 'Write a short paragraph with In my country… and People usually….', 'Review the four expressions ★ and create your own examples.', 'Listen to the dialogue again and note two similarities between the traditions.']),
  spaced=dict(next=['In my country,…', 'People usually…', 'We celebrate…'], week=['It’s supposed to…', 'I’d like to try it.', 'Apparently…'], unit=['Invite · experiences · stories · directions · news · traditions']),
  teach=teach(goal='Toda aula termina com uma produção observável.', solo=['Sem anotações: introduzir, descrever e explicar o significado.'], group=['Exit challenge individual.'], answers=['In my country, we celebrate Carnival. · People usually eat special food at festivals. · It’s supposed to bring good luck.'], extra=['Revisão espaçada: próxima aula, uma semana depois e na missão da unidade.'])),
 lv_page([('Festival. Food. Family.', 'Name a festival with key words.'), ('In my country, we celebrate Carnival. People usually dance.', 'Describe a tradition with usually.'), ('In my country, people usually celebrate with family, and it’s supposed to bring good luck.', 'Describe and explain meaning.'), ('Although traditions vary by region, most families celebrate by gathering, and the food usually has a symbolic meaning.', 'Generalize with nuance.'), ('What strikes visitors is how a ritual that seems purely festive is, for many families, a quiet way of honoring those who came before.', 'Interpret traditions thoughtfully.'), ('It is a custom that wears its meaning lightly: you take part first, and only later does it dawn on you what you have inherited.', 'Reflect on traditions with elegance.')])
]
LESSON = mk(92, 6, 'Traditions and festivals', 'Tradições e festivais', ['Hana', 'Carlos'], 'fairground', 'day', PAGES, DIALOG)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
