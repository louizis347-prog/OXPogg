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

DIALOG = dict(speakers={'Neighbor': {'name': 'Sam'}, 'Stranger': {'name': 'Una'}}, lines=[
 dict(who='Neighbor', en='**Lovely day, isn’t it?**', pt='Dia lindo, não é?'),
 dict(who='Stranger', en='It really is! Finally some sun after all that rain.', pt='É mesmo! Finalmente um pouco de sol depois de tanta chuva.'),
 dict(who='Neighbor', en='Tell me about it. **Are you from here?**', pt='Nem me fale. Você é daqui?'),
 dict(who='Stranger', en='Not originally. I moved here last year for work. How about you?', pt='Originalmente não. Me mudei para cá no ano passado, por trabalho. E você?'),
 dict(who='Neighbor', en='I grew up in Dublin, but I’ve lived here for ten years now.', pt='Cresci em Dublin, mas moro aqui há dez anos.'),
 dict(who='Stranger', en='Nice! **Do you know if** the number 12 bus comes often?', pt='Legal! Você sabe se o ônibus número 12 passa com frequência?'),
 dict(who='Neighbor', en='Every ten minutes or so. It should be here soon.', pt='A cada dez minutos, mais ou menos. Deve chegar logo.'),
 dict(who='Stranger', en='Great, thanks. **It was nice talking to you.**', pt='Ótimo, obrigada. Foi bom conversar com você.'),
 dict(who='Neighbor', en='Likewise! **Have a nice day!**', pt='Igualmente! Tenha um bom dia!')])

PAGES = [
 dict(t='rl_open', stage='warm', title='Small talk with strangers', pt='Conversa informal com estranhos', level='A2', unit=unit(7),
  situation=dict(text='You wait at a bus stop next to a stranger. You start a light conversation, ask one personal question, ask for a small piece of information and end the chat politely.', scene='busstop', tod='day', cast=['Sam', 'Una']),
  goal='By the end of the class you can start a short, friendly chat with a stranger, keep it going with two questions and say goodbye naturally.',
  canDo=['Open with a comment: Lovely day, isn’t it?', 'Ask Are you from here? and return How about you?', 'Ask for information: Do you know if…?', 'Close: It was nice talking to you. Have a nice day!'],
  success=['I start the conversation.', 'I ask and answer one question.', 'I keep it light and short.', 'I close politely.'],
  think='Do you talk to strangers at bus stops in your country? What topics feel comfortable and which ones do not?',
  teach=teach(goal='Abrir pela situação: conversa leve com desconhecidos.', solo=['Pergunte se o aluno puxa conversa com estranhos.', 'Mostre os 4 critérios.'], group=['Cada estudante diz um assunto seguro para um ponto de ônibus.', 'Anote no quadro.'], extra=['Where do people talk to strangers in your city?', 'Is it rude to ignore a stranger?'], support=['Aceite palavras soltas e reformule em frases.'])),
 dict(t='rl_warm', stage='warm', title='Connection & warm-up',
  intro=dict(solo='Ask about the student’s day and recycle traditions language.', group='One question per student, then a question back to a classmate.'),
  recall='Traditions (class 92): “In my country, people usually…”. Ask: What do people usually do on weekends in your city?',
  qs=[dict(q='How’s the weather today?', pt='Como está o tempo hoje?', sup=['It’s sunny.', 'It’s rainy.', 'It’s cold.']),
      dict(q='How do you usually get around the city?', pt='Como você costuma se locomover pela cidade?', sup=['By bus.', 'By subway.', 'On foot.']),
      dict(q='Have you ever had a nice chat with a stranger?', pt='Você já teve uma boa conversa com um estranho?', sup=['Yes, on a trip.', 'Not really.', 'At a café.'])],
  tip='Use the weather question as a live example of the opening comment.',
  teach=teach(goal='Ativar vocabulário de clima e transporte.', extra=['What is the weather like in your favorite season?', 'Who is the most talkative person you know?'], errors=[E('Today is making sun.', 'It’s sunny today.'), E('I go by foot.', 'I go on foot.')], support=['Use as respostas-chip.'])),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Light conversation',
  intro='Small talk is short, friendly and low-risk. Look and guess before you read.',
  cards=[dict(vis='prop:umbrella', en='Start with the weather', pt='Comece pelo tempo', note='The weather is a common safe topic: everyone shares it.'),
         dict(vis='prop:bus', en='Keep it light and short', pt='Seja leve e breve', note='A couple of comments and questions is enough while you wait.'),
         dict(vis='prop:clock', en='End before it gets awkward', pt='Termine antes de ficar estranho', note='“It was nice talking to you” is a polite way to finish.')],
  qs=[dict(q='Why do people talk about the weather?', pt='Por que as pessoas falam do tempo?', levels=dict(A1='Everyone sees it.', A2='It’s a safe topic that everyone can answer.', B1='It is neutral, so it opens a conversation without being personal.', B2='The weather is a low-risk shared topic that signals friendliness without demanding personal disclosure.')),
      dict(q='What topics do people usually avoid with strangers?', pt='Que assuntos se evitam com estranhos?', levels=dict(A1='Money. Age.', A2='Money, age and very personal topics.', B1='Salary, age, politics and other personal topics are usually avoided with strangers.', B2='Topics like income, age or politics can feel intrusive until you know the person better.')),
      dict(q='How can you end small talk politely?', pt='Como encerrar educadamente?', levels=dict(A1='Bye. Have a nice day.', A2='It was nice talking to you. Have a nice day!', B1='Say it was nice talking, wish them well and leave.', B2='A brief closing remark plus a friendly wish lets both people part comfortably.'))],
  compare='In Brazil, talking to strangers while waiting is also common, often about the heat, the traffic or the football. In English the weather and “Are you from here?” are classic openers. What do you usually talk about?',
  teach=teach(goal='Mostrar como puxar e encerrar uma conversa leve.', solo=['Mostre os 3 cartões e peça hipóteses.', 'Compare com “calor/trânsito/futebol” no Brasil.'], group=['Cada estudante escolhe um cartão e explica.', 'Pergunte “Do you agree?”.'], answers=['Q1: safe shared topic.', 'Q2: money, age, personal topics.', 'Q3: It was nice talking to you.'], extra=['What topics are safe in your culture?', 'How do you feel about small talk?'], support=['Use as respostas A1.'], stretch=['B2: discuta quando é melhor não puxar conversa.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='busstop', tod='day', cast=['Sam', 'Una']),
  pass1=dict(q='What are Sam and Una doing?', pt='O que Sam e Una estão fazendo?', opts=['Chatting at a bus stop', 'Buying tickets', 'Arguing'], ans=0),
  pass2=dict(tasks=[dict(label='Weather', ans='sun'), dict(label='When Una moved', ans='last year'), dict(label='Where Sam grew up', ans='Dublin'), dict(label='Bus number', ans='number 12', alt=['12']), dict(label='How often it comes', ans='ten minutes', alt=['ten', '10'])]),
  teach=teach(goal='Entender a conversa e 5 informações.', solo=['Esconda o texto. 1ª escuta: situação.', '2ª escuta: tempo, mudança, cidade, ônibus e frequência.'], group=['Escuta coletiva; duplas anotam antes de revelar.', 'Mostre o texto no final.'], answers=['Pass 1: chatting at a bus stop.', 'Pass 2: sun · last year · Dublin · number 12 · ten minutes.'], extra=['Are they friends?', 'Who asks more questions?'], support=['Use “Slow” e pause após cada fala.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='What do they talk about first?', opts=['The weather', 'Their jobs', 'The price of tickets'], ans=0), dict(q='When did Una move here?', opts=['Last year', 'Ten years ago', 'Last week'], ans=0), dict(q='Where did Sam grow up?', opts=['Dublin', 'London', 'Paris'], ans=0), dict(q='What does Una ask about the bus?', opts=['If it comes often', 'How much it costs', 'Where it goes'], ans=0)],
  retell=dict(prompt='Retell the conversation in your own words.', starters=['Sam says…', 'Una is not from…', 'She asks if…', 'In the end, they…']),
  teach=teach(goal='Ler o diálogo, perceber os chunks e recontar.', solo=['O estudante lê Una; você lê Sam.', 'Reconto no nível que conseguir.'], group=['Leitura em duplas.', 'Reconto em cadeia.'], answers=['The weather · Last year · Dublin · If it comes often'], extra=['What would you ask Sam next?', 'Does Una talk too much?'], errors=[E('Are you of here?', 'Are you from here?'), E('Have a nice day for you.', 'Have a nice day!')], support=['Mostre a tradução (PT) após a 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[dict(en='Lovely day, isn’t it?', pt='Dia lindo, não é?', use='Open a conversation with a comment.', reg='casual', alt='Also: **Nice weather today, huh?**', pri=True),
         dict(en='Are you from here?', pt='Você é daqui?', use='Ask a light personal question.', reg='neutral', pri=True),
         dict(en='It was nice talking to you.', pt='Foi bom conversar com você.', use='End the chat politely.', reg='neutral', pri=True),
         dict(en='Have a nice day!', pt='Tenha um bom dia!', use='Say goodbye with a wish.', reg='neutral', alt='Also: **Take care!**', pri=True),
         dict(en='How about you?', pt='E você?', use='Return the question.', reg='neutral'),
         dict(en='Tell me about it.', pt='Nem me fale.', use='Agree strongly.', reg='casual'),
         dict(en='Do you know if…?', pt='Você sabe se…?', use='Ask for information politely.', reg='polite'),
         dict(en='Likewise!', pt='Igualmente!', use='Return a good wish.', reg='neutral')],
  discover=dict(fns=['Opening', 'Asking about someone', 'Returning', 'Asking for information', 'Closing'],
   items=[dict(en='Lovely day, isn’t it?', fn='Opening'), dict(en='Are you from here?', fn='Asking about someone'), dict(en='How about you?', fn='Returning'), dict(en='Do you know if the bus comes often?', fn='Asking for information'), dict(en='Have a nice day!', fn='Closing')]),
  note='Choose the 4 starred expressions to use again and again; the others help you react and keep going.',
  teach=teach(goal='Escolher 4 chunks para abrir, perguntar e encerrar.', solo=['Pergunte “When do you say it?”.', 'Peça um exemplo real para cada ★.'], group=['Cada estudante escolhe um chunk e usa.', 'Duplas: mini conversa de 4 falas.'], answers=['Opening · Asking · Returning · Info · Closing'], extra=['Which of these would you use with an older person?'], errors=[E('Are you from here? Yes, I’m from here yes.', 'Yes, I am. / No, I’m from São Paulo.'), E('Do you know if the bus comes? (sem “often”)', 'Do you know if the bus comes often?')], support=['Trabalhe só as 4 expressões ★.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Comment + tag', formula='**It’s** + adjective, **isn’t it?**', ex=['Lovely day, isn’t it?', 'It’s cold today, isn’t it?', 'The bus is late, isn’t it?'], main=True),
            dict(name='Question + return', formula='**Are you from** + place? / **How about you?**', ex=['Are you from here?', 'I’m from Dublin. How about you?', 'Do you live nearby?'], main=True),
            dict(name='Polite information question', formula='**Do you know if** + subject + verb?', ex=['Do you know if the bus comes often?', 'Do you know if this seat is free?'])],
  swap=dict(frame='It’s {adj} {time}, isn’t it?', tpt='Está {adj} {time}, né?',
   slots=[dict(k='adj', label='Adjective', opts=[dict(en='lovely', pt='lindo'), dict(en='cold', pt='frio'), dict(en='hot', pt='quente')]),
          dict(k='time', label='Time', opts=[dict(en='today', pt='hoje'), dict(en='this morning', pt='hoje de manhã'), dict(en='this afternoon', pt='hoje à tarde')])]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['Lovely day, isn’t it?', 'The weather is pleasant today.'], ['Are you from around here?', 'Are you a local resident?'], ['Do you know if…?', 'Could you inform me whether…?'], ['Take care!', 'I wish you a pleasant day.']], note='In speech, short and relaxed forms are the norm.'),
  teach=teach(goal='Comentário + tag question; perguntas leves e retorno com “How about you?”.', solo=['Mostre os padrões no diálogo.', 'Use “Swap the words” em voz alta.'], group=['Troca em cadeia: cada estudante muda UMA peça.', 'Duplas: comentário e resposta.'], answers='Padrões 01/02 são o foco; 03 é expansão.', extra=['Make a comment about the room.', 'Ask me two light questions.'], errors=[E('It’s cold today, no?', 'It’s cold today, isn’t it?'), E('Do you know if does the bus come?', 'Do you know if the bus comes often?'), E('Are you from here? (entonação descendente demais)', 'Are you from here? ↗')], support=['Fique só com Lovely day, isn’t it? + Are you from here?'], stretch=['Mantenha 5 falas sem pausar.'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Intonation of tag questions', tip='When you are sure and want agreement, the tag falls: “Lovely day, isn’t it? ↘”. When you really ask, it rises ↗.',
  items=[dict(say='Lovely day, isn’t it?', linked='LOVE·ly DAY, is·n’t it? ↘', ipa='/ˈɪzntɪt/', rhythm='OooOooo'), dict(say='Are you from here?', linked='Are-ya from HERE? ↗', ipa='/ɑrjə/', rhythm='ooooO'), dict(say='Have a nice day!', linked='Ha·va NICE DAY! ↘', ipa='/ˈhævə/', rhythm='oooOO')],
  identify=[dict(q='Which one do you hear?', opts=['Lovely day, isn’t it?', 'Lovely day, aren’t you?', 'Lovely day, wasn’t it?'], ans=0, say='Lovely day, isn’t it?'), dict(q='Which one do you hear?', opts=['Are you from here?', 'Are you from there?', 'Were you from here?'], ans=0, say='Are you from here?')],
  own=dict(prompt='Write a comment with a tag about the place where you are now.', criteria='Say it twice: with falling tag, then rising. Can your partner hear the difference?'),
  teach=teach(goal='UM só fenômeno: entonação da tag question.', solo=['Escutar e identificar → repetir com a mão → frase própria.', 'Contraste tag descendente e ascendente.'], group=['Coro, depois duplas.', 'Cada estudante cria um comentário com tag.'], answers=['Identify 1: Lovely day, isn’t it? · Identify 2: Are you from here?'], errors=[E('isn’t it? com entonação plana', 'Cair (↘) ou subir (↗) com intenção'), E('“isn’t” com o /t/ forçado', 'is·n’t reduzido: /ˈɪzn̩t/')], support=['Reduza a velocidade e use a mão.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    dict(type='mcq', q='1. You are at a bus stop and the sun is out. How do you open a chat?', opts=['Lovely day, isn’t it?', 'Why you are here?', 'How much money you earn?'], ans=0, why='A weather comment is a safe opener.'),
    dict(type='mcq', q='2. You want to know where someone lives.', opts=['Are you from here?', 'Where are you being?', 'You live why?'], ans=0, why='A light question about origin.'),
    dict(type='mcq', q='3. The stranger answers your question. How do you keep going?', opts=['I’m from São Paulo. How about you?', 'I’m from São Paulo. Bye.', 'I answer you no.'], ans=0, why='Return the question.'),
    dict(type='mcq', q='4. The bus arrives. How do you end politely?', opts=['It was nice talking to you. Have a nice day!', 'Stop talking now.', 'Goodbye forever.'], ans=0, why='Polite closing with a wish.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    dict(type='gap', text='It’s cold today, ___ it?', ans='isn’t', bank=['isn’t', 'is', 'doesn’t'], why='It’s → isn’t it?'),
    dict(type='gap', text='Do you ___ if the bus comes often?', ans='know', bank=['know', 'knew', 'known'], why='Do you know if…?'),
    dict(type='swap', instr='Add a tag question:', frm='It’s a lovely morning.', ans=['It’s a lovely morning, isn’t it?'], model='It’s a lovely morning, isn’t it?', why='Add isn’t it? for agreement.'),
    dict(type='swap', instr='Make it polite:', frm='Does the bus come often?', ans=['Do you know if the bus comes often?'], model='Do you know if the bus comes often?', why='Do you know if… is more polite.'),
    dict(type='reply', npc='Are you from here?', q='Choose the best reply.', opts=['Not originally. I moved here last year. How about you?', 'Yes, no.', 'I here is.'], ans=0, why='Short answer + detail + return the question.')])],
  teach=teach(goal='Do controlado ao guiado antes da fala livre.', solo=['Peça que justifique cada resposta.', 'Peça uma segunda resposta possível.'], group=['Duplas comparam antes de revelar.', 'Pontos por resposta justificada.'], answers=['1: Lovely day, isn’t it? · 2: Are you from here? · 3: I’m from… How about you? · 4: It was nice talking to you.', 'Gap: isn’t · know · It’s a lovely morning, isn’t it? · Do you know if… · Not originally…'], extra=['Say each answer with friendly intonation.'], errors=[E('It’s cold, isn’t?', 'It’s cold, isn’t it?'), E('Do you know where is the bus?', 'Do you know where the bus is?')], support=['Ofereça o banco de palavras.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — chat with a stranger',
  brief=dict(teacher='You are a stranger at the bus stop. Be friendly, but give short answers.', student='Start the chat, ask one question, return “How about you?” and end politely.'),
  orders=['At a bus stop in the morning', 'In a waiting room', 'At a coffee line'],
  complications=['The stranger answers with one word.', 'You do not know what to say next: ask about the bus.', 'The stranger asks a personal question you prefer not to answer.', 'The bus arrives early: close quickly.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['Lovely day, isn’t it?', 'Are you from here?', 'How about you?', 'Have a nice day!']), dict(label='Keywords', desc='Only the keywords', help=['weather', 'from', 'bus', 'nice talking'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I start the conversation.', 'I ask and answer one question.', 'I keep it light and short.', 'I close politely.'],
  teach=teach(goal='Puxar, manter e encerrar uma conversa leve.', solo=['Use um local real do aluno.', 'Rodada 1 com chunks, 2 palavras-chave, 3 livre.', 'Anote 2–3 correções.'], extra=['How do you decline a personal question politely?', 'What if the stranger does not want to talk?'], errors=[E('I don’t want to answer that. (seco)', 'I’d rather not say. / Let’s talk about something else.')], support=['Volte à rodada 1 se travar.'], stretch=['Mantenha a conversa por 6 trocas e encerre sem silêncio.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Open and answer', min=3, task='Open with a comment; your partner answers and adds one more.', hint='Lovely day, isn’t it? / It really is!'), dict(title='Ask and return', min=3, task='Ask Are you from here? and return the question.', hint='Are you from here? / How about you?'), dict(title='Keep it going', min=3, task='Use Do you know if…? and one reaction.', hint='Do you know if…? / Tell me about it.'), dict(title='Best opener', min=2, whole=True, task='Whole group: each pair shares the best opener.', hint='We liked…')],
  infogap=dict(title='People at the bus stop', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='Student A: your notes', task='You know where Una is from and what Sam does. Ask about the rest.', rows=[dict(k='Una: hometown', v='Chicago'), dict(k='Sam: hometown', v=''), dict(k='Una: job', v=''), dict(k='Sam: job', v='mail carrier')]),
   b=dict(title='Student B: your notes', task='You know where Sam is from and what Una does. Ask about the rest.', rows=[dict(k='Una: hometown', v=''), dict(k='Sam: hometown', v='Dublin'), dict(k='Una: job', v='architect'), dict(k='Sam: job', v='')])),
  teach=teach(goal='Fluência em conversa leve com troca de informações.', group=['Troque os pares a cada rodada.', 'Responsabilidade individual: cada aluno abre e encerra uma conversa.', 'Sem salas simultâneas.'], answers=['Info gap: A tem Una de Chicago e Sam carteiro; B tem Sam de Dublin e Una arquiteta. Completam com “Where is Una from?”, “What does Sam do?”.'], extra=['Where is Sam from?', 'What does Una do?'], errors=[E('Where is from Sam?', 'Where is Sam from?'), E('He is mailman.', 'He’s a mail carrier.')], support=['Entregue frases-modelo no chat.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — bus stop chats',
  goal='Each group must start, keep and end a short friendly conversation with a stranger.',
  missions=[dict(who='A', role='Commuters', mission='Chat at a bus stop for one minute. Include the weather and one personal question.', constraint='Use “Lovely day, isn’t it?” and “How about you?”.', start='Lovely day, isn’t it?'),
            dict(who='B', role='New neighbors', mission='Meet a new neighbor at the elevator. Find two things in common.', constraint='Ask “Are you from here?” and “Do you know if…?”.', start='Hi! Are you from here?'),
            dict(who='C', role='Waiting room', mission='Chat while waiting for an appointment. End when your name is called.', constraint='Close with “It was nice talking to you.”', start='Hi! Busy today, isn’t it?')], min=11,
  success=['Start the conversation.', 'Ask and return questions.', 'Keep it light.', 'End politely.'],
  teach=teach(goal='Realizar conversas leves reais e terminar com naturalidade.', group=['Cada grupo recebe papéis e restrição.', 'Progressão: com chunks, palavras-chave, sem roteiro.', 'Anote 2–3 correções.'], answers=['Modelo: “Lovely day, isn’t it?” → “It really is!” → “Are you from here?” → “Not originally. How about you?” → “It was nice talking to you.”'], extra=['Which opener felt most natural?'], support=['Dê o início de frase em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short note to a new neighbor you chatted with, saying it was nice to meet them.',
  steps=['Greeting', 'Remember the chat', 'Question or invitation', 'Closing'],
  model='Hi Una! It was nice talking to you at the bus stop yesterday. I hope the number 12 came on time! Are you free for coffee this weekend? Have a nice day!',
  checklist=['I greeted the person.', 'I mentioned our chat.', 'I asked a question or invited.', 'I closed with a friendly wish.'],
  tip='Fix only 2–3 priority points and show a more natural way to say the same idea.', fix=dict(n=3),
  teach=teach(goal='Produção escrita curta: bilhete amigável.', solo=['Corrija 2–3 pontos prioritários.'], group=['Troquem os bilhetes e respondam.'], extra=['Add one more question.'], errors=[E('Nice to talk with you yesterday.', 'It was nice talking to you yesterday.'), E('Have nice day.', 'Have a nice day.')], support=['Dê o modelo e peça só para trocar os dados.'])),
 fb_page('Example: You started the chat and returned the question naturally.', 'Example: Use falling intonation in the tag: “isn’t it? ↘”.', 'Example: Keep a chat going for two minutes without notes.', 'conversa leve e despedida natural.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❓', name='Open a chat', prompt='Without notes: comment on the weather with a tag.', model='Lovely day, isn’t it?'), dict(ic='💬', name='Ask and return', prompt='Ask if the person is from here, then return their question.', model='Are you from here? How about you?'), dict(ic='⭐', name='Close politely', prompt='End the chat when the bus comes.', model='It was nice talking to you. Have a nice day!')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 45–60 second audio of a bus-stop chat.', 'Write a short note to a new neighbor.', 'Review the four expressions ★ and create your own examples.', 'Listen to the dialogue again and find two ways to react.']),
  spaced=dict(next=['Lovely day, isn’t it?', 'Are you from here?', 'Have a nice day!'], week=['It was nice talking to you.', 'Do you know if…?', 'People usually…'], unit=['Invite · experiences · stories · directions · news · traditions · small talk']),
  teach=teach(goal='Toda aula termina com uma produção observável.', solo=['Sem anotações: abrir, perguntar e encerrar.'], group=['Exit challenge individual.'], answers=['Lovely day, isn’t it? · Are you from here? How about you? · It was nice talking to you. Have a nice day!'], extra=['Revisão espaçada: próxima aula (Mission Day), uma semana depois e na missão da unidade.'])),
 lv_page([('Hello. Nice day.', 'Greet and comment with a few words.'), ('Lovely day, isn’t it? Are you from here?', 'Open a chat and ask one question.'), ('Lovely day, isn’t it? I’m waiting for the 12; do you know if it comes often?', 'Combine comment and request.'), ('I couldn’t help noticing the sunshine; it’s a nice change after all that rain, isn’t it?', 'Open with a more personal comment.'), ('One can only hope this weather lasts; I’m rather tired of the rain myself.', 'Keep a polished, light tone.'), ('It would be a shame to waste a day like this waiting for a bus, wouldn’t it?', 'Use wit and subtle humor.')])
]
LESSON = mk(93, 7, 'Small talk with strangers', 'Conversa informal com estranhos', ['Sam', 'Una'], 'busstop', 'day', PAGES, DIALOG)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
