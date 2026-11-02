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

DIALOG = dict(speakers={'Musician': {'name': 'Colin'}, 'Friend': {'name': 'Vera'}}, lines=[
 dict(who='Friend', en='Colin, you look so happy! What happened this morning?', pt='Colin, você parece tão feliz! O que aconteceu esta manhã?'),
 dict(who='Musician', en='**You won’t believe it.** **I was playing** my fiddle in the park **when** a man stopped to listen.', pt='Você não vai acreditar. Eu estava tocando meu violino no parque quando um homem parou para ouvir.'),
 dict(who='Friend', en='**And then what happened?**', pt='E o que aconteceu depois?'),
 dict(who='Musician', en='**While** I was playing, he took out his phone and started recording. **Suddenly** he said, “Can you play that again?”', pt='Enquanto eu tocava, ele pegou o celular e começou a gravar. De repente disse: “Você pode tocar isso de novo?”'),
 dict(who='Friend', en='Wait, what? What was he doing in the park?', pt='Peraí, o quê? O que ele estava fazendo no parque?'),
 dict(who='Musician', en='He was walking his dog. He’s a radio producer, and he was looking for a street musician.', pt='Ele estava passeando com o cachorro. Ele é produtor de rádio e estava procurando um músico de rua.'),
 dict(who='Friend', en='That’s incredible! So how did it end?', pt='Que incrível! E como terminou?'),
 dict(who='Musician', en='**In the end,** he gave me his card and invited me to play on his radio show!', pt='No fim, ele me deu o cartão e me convidou para tocar no programa de rádio dele!'),
 dict(who='Friend', en='Congratulations! I knew it was going to be a good day for you.', pt='Parabéns! Eu sabia que seria um bom dia para você.')])

PAGES = [
 dict(t='rl_open', stage='warm', title='Telling stories (past continuous)', pt='Contar histórias no passado', level='A2', unit=unit(3),
  situation=dict(text='Something surprising happened to you this morning. In the park, you tell a friend the story: what you were doing, what happened and how it ended.', scene='park', tod='day', cast=['Colin', 'Vera']),
  goal='By the end of the class you can tell a short story with a beginning, a surprise and an ending, using was/were + -ing and linking words.',
  canDo=['Set the scene: I was… when…', 'Use while for two actions at the same time', 'Use Suddenly / Then / In the end', 'React to a story: And then what happened?'],
  success=['I set the scene.', 'I tell what happened.', 'I end the story.', 'I react to my partner’s story.'],
  think='Think of a small surprising thing that happened to you recently. What were you doing at that moment?',
  teach=teach(goal='Abrir pela situação: contar o que aconteceu de forma organizada.', solo=['Peça ao estudante um momento surpreendente recente.', 'Mostre os 4 critérios.'], group=['Cada estudante diz o que estava fazendo ontem às 8 da noite.', 'Anote no quadro.'], extra=['What is the best story you tell at parties?', 'Who tells the best stories in your family?'], support=['Aceite respostas curtas e reformule em inglês.'])),
 dict(t='rl_warm', stage='warm', title='Connection & warm-up',
  intro=dict(solo='Ask about the student’s week; listen for the past simple and recycle travel experiences.', group='One question per student, then a question back to a classmate.'),
  recall='Experiences (class 88): “Have you ever…?” and “I’ve never…”. Ask: What is something you have never done?',
  qs=[dict(q='What were you doing at 8 p.m. yesterday?', pt='O que você estava fazendo às 8 da noite de ontem?', sup=['I was watching TV.', 'I was cooking.', 'I was studying.']),
      dict(q='Did anything funny happen this week?', pt='Aconteceu algo engraçado esta semana?', sup=['Yes, I…', 'Not really.', 'My friend…']),
      dict(q='Who tells the best stories in your family?', pt='Quem conta as melhores histórias na sua família?', sup=['My grandfather.', 'My mom.', 'My best friend.'])],
  tip='Use the first question to hear was/were + -ing naturally, without naming the grammar.',
  teach=teach(goal='Ativar passado e criar contexto para histórias.', extra=['What were you doing when you got my message?', 'What were you doing last Sunday afternoon?'], errors=[E('I was go to the park.', 'I went to the park. / I was going to the park.'), E('I seen him yesterday.', 'I saw him yesterday.')], support=['Use as respostas-chip.'])),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Story structure',
  intro='Good stories follow a simple pattern that English speakers recognize. Look and guess before you read.',
  cards=[dict(vis='prop:clock', en='Set the scene', pt='Situe a cena', note='When, where, what you were doing: “I was walking in the park…”'),
         dict(vis='prop:umbrella', en='Add the surprise', pt='Conte a surpresa', note='“Suddenly…” or “Then…” brings the event that changes everything.'),
         dict(vis='prop:telephone', en='Listeners react', pt='Os ouvintes reagem', note='“Really?”, “No way!”, “And then what happened?” keep the story alive.')],
  qs=[dict(q='Why is “Suddenly” useful in a story?', pt='Por que “Suddenly” é útil numa história?', levels=dict(A1='It shows something new.', A2='It shows a surprise: something changed quickly.', B1='It marks the turning point after the background description.', B2='It signals a sudden event in the narrative and creates a moment of suspense.')),
      dict(q='What do listeners do while you tell a story?', pt='O que os ouvintes fazem enquanto você conta?', levels=dict(A1='They say “Really?”', A2='They say “Really?” or “No way!” and ask questions.', B1='They react and ask follow-ups, such as “And then what happened?”', B2='They use short reactions and questions to show they are following and invite more detail.')),
      dict(q='How do stories usually end?', pt='Como as histórias costumam terminar?', levels=dict(A1='With “In the end…”', A2='With “In the end…” and how you felt.', B1='With the result and a short comment about how you felt or what you learned.', B2='With the outcome and a brief reflection, often with a light or humorous comment.'))],
  compare='In Brazil, people also love telling stories and listeners interrupt with “nossa!” and “e aí?”. In English, short reactions like “Really?” and “And then?” do the same job. Which reactions do you use?',
  teach=teach(goal='Mostrar a estrutura de uma boa história e as reações do ouvinte.', solo=['Mostre os 3 cartões e peça hipóteses.', 'Compare com “nossa!” e “e aí?”.'], group=['Cada estudante escolhe um cartão e explica.', 'Pergunte “Do you agree?”.'], answers=['Q1: shows a sudden event.', 'Q2: react and ask questions.', 'Q3: In the end… + feeling.'], extra=['What reactions do you use in Portuguese?', 'Do you like long or short stories?'], support=['Use as respostas A1 como andaime.'], stretch=['B2: conte a mesma história em 3 frases e em 8.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='park', tod='day', cast=['Colin', 'Vera']),
  pass1=dict(q='What is Colin doing?', pt='O que o Colin está fazendo?', opts=['Telling a story about his morning', 'Asking for directions', 'Complaining about the weather'], ans=0),
  pass2=dict(tasks=[dict(label='Where was Colin playing?', ans='park'), dict(label='Instrument', ans='fiddle'), dict(label='What was the man walking?', ans='dog'), dict(label='The man’s job', ans='radio producer', alt=['producer']), dict(label='The invitation', ans='radio show', alt=['radio'])]),
  teach=teach(goal='Entender a história e depois 5 informações.', solo=['Esconda o texto. 1ª escuta: ideia principal.', '2ª escuta: lugar, instrumento, cachorro, profissão e convite.'], group=['Escuta coletiva; duplas anotam antes de revelar.', 'Mostre o texto só no final.'], answers=['Pass 1: a story about his morning.', 'Pass 2: park · fiddle · dog · radio producer · radio show.'], extra=['How does Vera react?', 'Is Colin lucky? Why?'], support=['Use “Slow” e pause após cada fala.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='What was Colin doing when the man stopped?', opts=['Playing his fiddle', 'Eating lunch', 'Reading a book'], ans=0), dict(q='What did the man do while Colin was playing?', opts=['He recorded him', 'He walked away', 'He asked for money'], ans=0), dict(q='Why was the man in the park?', opts=['He was walking his dog and looking for a musician', 'He was lost', 'He was selling tickets'], ans=0), dict(q='How did the story end?', opts=['The man invited him to a radio show', 'Colin lost his fiddle', 'It started to rain'], ans=0)],
  retell=dict(prompt='Retell the story in your own words.', starters=['Colin was playing when…', 'While he was playing, the man…', 'Suddenly…', 'In the end…']),
  teach=teach(goal='Ler o diálogo, perceber os chunks e recontar com a estrutura da história.', solo=['O estudante lê Colin; você lê Vera.', 'Reconto com os conectores.'], group=['Leitura em duplas.', 'Reconto em cadeia: uma frase por estudante, cada uma começando com um conector.'], answers=['Playing his fiddle · He recorded him · walking his dog and looking for a musician · invited to a radio show'], extra=['What would you do in Colin’s place?', 'What was Vera doing while Colin played? (She was not there.)'], errors=[E('I was play the fiddle.', 'I was playing the fiddle.'), E('When I played, a man was stopping.', 'I was playing when a man stopped.')], support=['Mostre a tradução (PT) após a 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[dict(en='I was… when…', pt='Eu estava… quando…', use='Set the scene and introduce the event.', reg='neutral', pri=True),
         dict(en='While we were…', pt='Enquanto a gente estava…', use='Two actions at the same time.', reg='neutral', pri=True),
         dict(en='Suddenly…', pt='De repente…', use='Introduce a surprise.', reg='neutral', pri=True),
         dict(en='And then what happened?', pt='E o que aconteceu depois?', use='Ask the storyteller to continue.', reg='neutral', pri=True),
         dict(en='You won’t believe it.', pt='Você não vai acreditar.', use='Start an exciting story.', reg='casual'),
         dict(en='In the end,', pt='No fim,', use='Close the story.', reg='neutral'),
         dict(en='Wait, what?', pt='Peraí, o quê?', use='Show surprise.', reg='casual'),
         dict(en='That’s incredible!', pt='Que incrível!', use='React to good news.', reg='neutral')],
  discover=dict(fns=['Setting the scene', 'Two actions together', 'Surprise', 'Asking for more', 'Ending'],
   items=[dict(en='I was walking in the park when it started to rain.', fn='Setting the scene'), dict(en='While I was cooking, he was watching TV.', fn='Two actions together'), dict(en='Suddenly, the lights went out.', fn='Surprise'), dict(en='And then what happened?', fn='Asking for more'), dict(en='In the end, we all laughed.', fn='Ending')]),
  note='Choose the 4 starred expressions for your own stories; the others help you react and close.',
  teach=teach(goal='Escolher 4 chunks e relacionar cada um à parte da história.', solo=['Pergunte “Where does it go in a story?”.', 'Peça uma frase própria para cada chunk ★.'], group=['Cada estudante escolhe um chunk e usa em uma frase.', 'Duplas: contar uma história de 3 frases.'], answers=['Scene · two actions · surprise · more · ending'], extra=['Which of these would you use with a child?'], errors=[E('I was walking when it begins to rain.', 'I was walking when it began to rain.'), E('Suddenly I was seeing a dog.', 'Suddenly I saw a dog.')], support=['Trabalhe só as 4 expressões ★.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Background action', formula='**I was / we were** + verb-ing', ex=['I was playing my fiddle.', 'We were walking in the park.', 'He was looking for a musician.'], main=True),
            dict(name='Interrupting action', formula='**I was** -ing **when** + past simple', ex=['I was playing when a man stopped.', 'We were eating when the lights went out.', 'She was driving when the phone rang.'], main=True),
            dict(name='Two actions at once', formula='**While** + past continuous, past simple / continuous', ex=['While I was playing, he recorded me.', 'While we were talking, it started to rain.'])],
  swap=dict(frame='I was {doing} when {event}.', tpt='Eu estava {doing} quando {event}.',
   slots=[dict(k='doing', label='Doing', opts=[dict(en='playing my fiddle', pt='tocando meu violino'), dict(en='walking in the park', pt='caminhando no parque'), dict(en='having lunch', pt='almoçando')]),
          dict(k='event', label='Event', opts=[dict(en='it started to rain', pt='começou a chover'), dict(en='my phone rang', pt='meu celular tocou'), dict(en='I saw an old friend', pt='vi um velho amigo')])]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['I was just walking and, bam, it rained.', 'I was walking when it began to rain.'], ['So then he’s like, “Play it again.”', 'Then he asked me to play it again.'], ['Wait, what?', 'I did not understand what he said.'], ['Long story short, he loved it.', 'In short, he was very pleased.']], note='In informal storytelling you may hear “he’s like…”; in writing, use the full structure.'),
  teach=teach(goal='Past continuous = cena de fundo; past simple = evento. Foco em “was/were + -ing” e “when”.', solo=['Mostre os padrões no diálogo.', 'Use “Swap the words” em voz alta.'], group=['Troca em cadeia: cada estudante muda UMA peça.', 'Duplas: um conta o fundo, o outro o evento.'], answers='Padrões 01/02 são o foco; 03 é expansão.', extra=['What were you doing when the teacher called you?', 'Tell me what you were doing at midnight yesterday.'], errors=[E('I was play.', 'I was playing.'), E('I played when he stopped. (ação interrompida)', 'I was playing when he stopped.'), E('While I played, he was recorded.', 'While I was playing, he recorded me.')], support=['Fique só com “I was… when…” na primeira rodada.'], stretch=['Combine os três padrões em uma frase.'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Weak forms', tip='“Was” and “were” are weak in connected speech: /wəz/ and /wɚ/. The strong word is the verb: “I was PLAYing”.',
  items=[dict(say='I was playing in the park.', linked='I wəz PLAY·ing in the PARK.', ipa='/wəz/', rhythm='ooOooOo'), dict(say='While we were walking…', linked='While wer WALK·ing…', ipa='/wɚ/', rhythm='oooOo'), dict(say='Suddenly, he stopped.', linked='SUD·den·ly, he STOPPED.', ipa='/ˈsʌdənli/', rhythm='OoooO')],
  identify=[dict(q='Which one do you hear?', opts=['I was playing.', 'I was paying.', 'I was praying.'], ans=0, say='I was playing.'), dict(q='Which one do you hear?', opts=['While we were walking…', 'While we were working…', 'While we were waiting…'], ans=0, say='While we were walking…')],
  own=dict(prompt='Write a sentence with “I was … when …” about something real.', criteria='Say it twice: slowly, then with weak “was”. Did the verb sound stronger than “was”?'),
  teach=teach(goal='UM só fenômeno: forma fraca de was/were e acento no verbo.', solo=['Escutar e identificar → repetir → frase própria.', 'Bata palmas nas sílabas fortes.'], group=['Coro, depois duplas.', 'Cada estudante cria uma frase.'], answers=['Identify 1: I was playing. · Identify 2: While we were walking…'], errors=[E('WAS pronunciado forte /wʌz/', '“was” fraco /wəz/'), E('Acentuar was em vez do verbo', 'I was PLAYing')], support=['Reduza a velocidade e conte as batidas.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    dict(type='mcq', q='1. Set the scene: you were reading in the park.', opts=['I was reading in the park.', 'I reading in the park.', 'I was read in the park.'], ans=0, why='was + verb-ing.'),
    dict(type='mcq', q='2. A dog ran up while you were eating. Which is correct?', opts=['I was eating when a dog ran up.', 'I ate when a dog was running up.', 'I was eat when a dog ran up.'], ans=0, why='Long action in the continuous, interruption in the past simple.'),
    dict(type='mcq', q='3. Which word introduces a surprise?', opts=['Suddenly', 'Usually', 'Always'], ans=0, why='Suddenly marks a quick change.'),
    dict(type='mcq', q='4. A friend says “You won’t believe what happened!” You respond:', opts=['And then what happened?', 'I don’t be believe.', 'Happen what then?'], ans=0, why='A natural reaction that invites the story.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    dict(type='gap', text='We ___ walking in the park when it started to rain.', ans='were', bank=['were', 'was', 'are'], why='we + were.'),
    dict(type='gap', text='___ I was playing, he recorded me.', ans='While', bank=['While', 'Suddenly', 'And'], why='While + past continuous.'),
    dict(type='swap', instr='Put in the past continuous:', frm='I play my fiddle.', ans=['I was playing my fiddle.'], model='I was playing my fiddle.', why='was + -ing.'),
    dict(type='swap', instr='Join with “when”:', frm='I was cooking. The phone rang.', ans=['I was cooking when the phone rang.', 'I was cooking when my phone rang.'], model='I was cooking when the phone rang.', why='Background + when + event.'),
    dict(type='reply', npc='I was walking home when I saw a rainbow.', q='Choose the best reaction.', opts=['Really? And then what happened?', 'I am walking too.', 'A rainbow is colors.'], ans=0, why='Show interest and ask for more.')])],
  teach=teach(goal='Do controlado ao guiado antes da fala livre.', solo=['Peça que justifique cada resposta.', 'Peça a história completa a partir de cada item.'], group=['Duplas comparam antes de revelar.', 'Pontos por resposta justificada.'], answers=['1: I was reading in the park. · 2: I was eating when a dog ran up. · 3: Suddenly · 4: And then what happened?', 'Gap: were · While · I was playing my fiddle. · I was cooking when the phone rang. · Really? And then what happened?'], extra=['Say each answer with story intonation.'], errors=[E('I was eating when a dog was running.', 'I was eating when a dog ran up.'), E('While I playing…', 'While I was playing…')], support=['Ofereça o banco de palavras.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — tell your story',
  brief=dict(teacher='You are a curious friend. Ask “And then what happened?” and react with surprise.', student='Tell a short true (or invented) story: set the scene, say what happened and how it ended.'),
  orders=['A surprising meeting', 'A funny moment on a trip', 'A day when everything went wrong'],
  complications=['Your friend interrupts with questions.', 'You forget a word: describe it.', 'The friend says “Really? That happened to me too!”', 'You need to finish in 30 seconds.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['I was… when…', 'While…', 'Suddenly…', 'In the end…']), dict(label='Keywords', desc='Only the keywords', help=['park', 'fiddle', 'radio', 'invited'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I set the scene.', 'I tell what happened.', 'I end the story.', 'I react to my partner’s story.'],
  teach=teach(goal='Contar uma história pessoal com começo, surpresa e fim.', solo=['Use uma história real do aluno.', 'Rodada 1 com chunks, 2 palavras-chave, 3 livre.', 'Anote 2–3 correções.'], extra=['What was the last funny thing that happened to you?', 'What was your best day ever?'], errors=[E('Yesterday I was go to the market and I seen…', 'Yesterday I went to the market and I saw…')], support=['Volte à rodada 1 se travar.'], stretch=['Conte a história de forma mais curta e mais dramática.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='What were you doing?', min=3, task='Ask your partner what they were doing at 8 p.m. yesterday.', hint='I was… / What were you doing?'), dict(title='Interrupted!', min=3, task='Tell what happened while you were doing something.', hint='I was… when…'), dict(title='Story in 4 parts', min=3, task='Scene, surprise, reaction, ending.', hint='Suddenly… / In the end…'), dict(title='Best story', min=2, whole=True, task='Whole group: each pair tells the best story in 30 seconds.', hint='You won’t believe it…')],
  infogap=dict(title='Who was where?', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='Student A: witness notes', task='You know what Tom was doing at 8:00 and Mia at 9:00. Ask about the rest.', rows=[dict(k='Tom at 8:00', v='reading in the park'), dict(k='Mia at 8:00', v=''), dict(k='Tom at 9:00', v=''), dict(k='Mia at 9:00', v='running by the river')]),
   b=dict(title='Student B: witness notes', task='You know Mia at 8:00 and Tom at 9:00. Ask about the rest.', rows=[dict(k='Tom at 8:00', v=''), dict(k='Mia at 8:00', v='having breakfast'), dict(k='Tom at 9:00', v='taking photos'), dict(k='Mia at 9:00', v='')])),
  teach=teach(goal='Fluência em perguntas e respostas no passado contínuo.', group=['Troque os pares a cada rodada.', 'Responsabilidade individual: cada aluno faz ≥2 perguntas What was… doing?', 'Sem salas simultâneas.'], answers=['Info gap: A tem Tom 8:00 e Mia 9:00; B tem Mia 8:00 e Tom 9:00. Respostas com “was … -ing”.'], extra=['What was Tom doing at 9:00?', 'Who was taking photos?'], errors=[E('What Tom was doing?', 'What was Tom doing?')], support=['Entregue frases-modelo no chat.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — tell a story together',
  goal='Each group must build and tell a short story with scene, surprise and ending.',
  missions=[dict(who='A', role='Storytellers', mission='Create a story with five sentences: one person starts, each adds one sentence.', constraint='Use “was/were -ing”, “when” and “Suddenly” at least once.', start='I was walking when…'),
            dict(who='B', role='Reporters', mission='Interview a classmate about a strange thing that happened to them. Ask follow-up questions.', constraint='Ask “And then what happened?” twice.', start='You won’t believe it…'),
            dict(who='C', role='Detectives', mission='Find out who broke a vase: ask what each person was doing at 7 p.m.', constraint='Use “What were you doing…?” and “While…”.', start='What were you doing at…')], min=11,
  success=['Set the scene.', 'Tell what happened.', 'End the story.', 'React to others.'],
  teach=teach(goal='Construir uma história coletiva usando passado contínuo e simples.', group=['Cada grupo recebe papéis e restrição.', 'Progressão: com chunks, palavras-chave, sem roteiro.', 'Anote 2–3 correções.'], answers=['Modelo: “I was walking when I saw a big dog.” → “And then what happened?” → “Suddenly it ran to me. In the end, it was friendly.”'], extra=['Which story was funniest?'], support=['Dê o início de frase em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short story (4–5 sentences) about a surprising moment: scene, surprise and ending.',
  steps=['Scene', 'Surprise', 'Reaction', 'Ending'],
  model='Last Sunday I was walking in the park when I heard music. While I was listening, a man asked me to play with him. Suddenly, everyone was clapping! In the end, I made a new friend.',
  checklist=['I set the scene (was/were -ing).', 'I used when or while.', 'I used Suddenly or Then.', 'I closed with In the end.'],
  tip='Fix only 2–3 priority points and show a more natural way to say the same idea.', fix=dict(n=3),
  teach=teach(goal='Produção escrita curta: uma história com estrutura.', solo=['Corrija 2–3 pontos prioritários.'], group=['Troquem os textos e leiam em voz alta.'], extra=['Add a surprising ending.'], errors=[E('I was walking when I hear music.', 'I was walking when I heard music.'), E('Suddenly, I am see.', 'Suddenly, I saw…')], support=['Dê o modelo e peça só para trocar os dados.'])),
 fb_page('Example: You told the story in order and used “when” and “while”.', 'Example: Use weak “was” and stress the verb.', 'Example: Tell a two-minute story without notes.', 'estrutura da história e passado contínuo.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❓', name='Set the scene', prompt='Without notes: say you were cooking when the phone rang.', model='I was cooking when the phone rang.'), dict(ic='💬', name='React to a story', prompt='A friend says “I was walking home when I saw a rainbow.” Reply.', model='Really? And then what happened?'), dict(ic='⭐', name='Add a surprise', prompt='Add a surprise to your story with a word.', model='Suddenly, it started to rain.')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 45–60 second audio telling a short story.', 'Write a 5-sentence story with when, while and suddenly.', 'Review the four expressions ★ and create your own examples.', 'Listen to the dialogue again and find two reactions.']),
  spaced=dict(next=['I was… when…', 'While we were…', 'Suddenly…'], week=['And then what happened?', 'In the end,', 'Have you ever…?'], unit=['Invite · tell experiences · tell stories']),
  teach=teach(goal='Toda aula termina com uma produção observável.', solo=['Sem anotações: cena, reação e surpresa.'], group=['Exit challenge individual.'], answers=['I was cooking when the phone rang. · Really? And then what happened? · Suddenly, it started to rain.'], extra=['Revisão espaçada: próxima aula, uma semana depois e na missão da unidade.'])),
 lv_page([('I walk. Rain. I run.', 'Tell a story in very short phrases.'), ('I was walking when it started to rain. Then I ran home.', 'Tell a short story with when and then.'), ('While I was walking home, it suddenly started to pour, so I ran into a café.', 'Link events with while and suddenly.'), ('I had just left work when the sky opened up, so I ducked into a café, soaked.', 'Add sequence and detail.'), ('No sooner had I stepped outside than the heavens opened, which, frankly, felt like the perfect end to the day.', 'Control tense, emphasis and tone.'), ('I’d barely reached the corner when the rain came down, as if the day itself had been waiting to make its point.', 'Narrate with stylistic nuance.')])
]
LESSON = mk(89, 3, 'Telling stories (past continuous)', 'Contar histórias no passado', ['Colin', 'Vera'], 'park', 'day', PAGES, DIALOG)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
