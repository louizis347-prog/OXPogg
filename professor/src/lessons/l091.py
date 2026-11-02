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

DIALOG = dict(speakers={'Reporter': {'name': 'Amy'}, 'Colleague': {'name': 'Tessa'}}, lines=[
 dict(who='Reporter', en='Tessa, **did you hear about** the new bridge downtown?', pt='Tessa, você ficou sabendo da nova ponte no centro?'),
 dict(who='Colleague', en='No! What happened?', pt='Não! O que aconteceu?'),
 dict(who='Reporter', en='**Apparently,** it opens this Saturday, after three years of work.', pt='Pelo visto, ela abre neste sábado, depois de três anos de obras.'),
 dict(who='Colleague', en='Wow. **I read that** there will be a street festival, too.', pt='Uau. Li que também vai ter um festival de rua.'),
 dict(who='Reporter', en='Is that right? Where did you read it?', pt='É mesmo? Onde você leu?'),
 dict(who='Colleague', en='On the city’s website. But **I’m not sure** about the time.', pt='No site da prefeitura. Mas não tenho certeza do horário.'),
 dict(who='Reporter', en='Let me check. **According to** the mayor’s office, it starts at ten a.m.', pt='Deixa eu conferir. Segundo o gabinete do prefeito, começa às dez da manhã.'),
 dict(who='Colleague', en='Great! I’ll tell my neighbors. Should I share the link?', pt='Ótimo! Vou contar para os meus vizinhos. Devo compartilhar o link?'),
 dict(who='Reporter', en='Yes, please. Just say it starts at ten and the source is the city.', pt='Sim, por favor. Só diga que começa às dez e que a fonte é a prefeitura.')])

PAGES = [
 dict(t='rl_open', stage='warm', title='News and events', pt='Notícias e eventos', level='A2', unit=unit(5),
  situation=dict(text='At work you hear about an event in your city. You share the news with a colleague, say where you heard it and check what you are not sure about.', scene='newsroom', tod='day', cast=['Amy', 'Tessa']),
  goal='By the end of the class you can share news, say where you heard it, show when you are not sure and react to what you hear.',
  canDo=['Start with Did you hear about…?', 'Share news: Apparently… / I read that…', 'Name the source: According to…', 'React: Is that right? / No way!'],
  success=['I introduce the news.', 'I say where I heard it.', 'I show how sure I am.', 'I react to my partner’s news.'],
  think='When you pass on news in Portuguese, do you say where you read or heard it? Why is that useful?',
  teach=teach(goal='Abrir pela situação: compartilhar notícias com a fonte.', solo=['Peça uma notícia recente que o aluno acompanhou.', 'Mostre os 4 critérios.'], group=['Cada estudante diz um evento da cidade.', 'Anote no quadro.'], extra=['Where do you get your news?', 'Do you prefer reading or watching the news?'], support=['Aceite palavras soltas e reformule em frases.'])),
 dict(t='rl_warm', stage='warm', title='Connection & warm-up',
  intro=dict(solo='Ask where the student gets information and recycle directions language.', group='One question per student, then a question back to a classmate.'),
  recall='Detailed directions (class 90): “Turn left at the…”. Ask: How do you get from here to your favorite place?',
  qs=[dict(q='What was the last piece of news you read?', pt='Qual foi a última notícia que você leu?', sup=['It was about…', 'I don’t remember.', 'Something about sports.']),
      dict(q='Where do you usually get your news?', pt='Onde você costuma se informar?', sup=['On my phone.', 'On TV.', 'From friends.']),
      dict(q='What is going on in your city this week?', pt='O que está acontecendo na sua cidade esta semana?', sup=['A concert.', 'A festival.', 'Nothing special.'])],
  tip='Note the topics the student likes (sports, music, weather); use them for the news sharing.',
  teach=teach(goal='Ativar vocabulário de notícias e eventos.', extra=['Do you share news on social media?', 'Who tells you the news first in your family?'], errors=[E('Have a festival in my city.', 'There is a festival in my city.')], support=['Use as respostas-chip.'])),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Sharing news',
  intro='How you share news says as much as the news itself. Look and guess before you read.',
  cards=[dict(vis='prop:telephone', en='Did you hear about…?', pt='Você ficou sabendo de…?', note='A friendly opening for news or gossip, often followed by the details.'),
         dict(vis='prop:computer', en='Name the source', pt='Cite a fonte', note='“I read that…” and “According to…” show where the information comes from.'),
         dict(vis='obj:globe', en='Be careful with certainty', pt='Cuidado com a certeza', note='“Apparently” and “I’m not sure” warn that you have not confirmed it.')],
  qs=[dict(q='Why do speakers say “Apparently…”?', pt='Por que se diz “Apparently…”?', levels=dict(A1='To say “it seems”.', A2='To say they heard it, but are not 100% sure.', B1='It signals that the information comes from someone else and may need checking.', B2='It distances the speaker from the claim, hedging responsibility for its accuracy.')),
      dict(q='Why name the source of news?', pt='Por que citar a fonte?', levels=dict(A1='To be clear.', A2='So people know where it comes from.', B1='It helps listeners trust or check the information.', B2='Attribution lets listeners judge reliability and protects you from spreading unverified claims.')),
      dict(q='How can you react to news?', pt='Como reagir a uma notícia?', levels=dict(A1='Really?', A2='Is that right? No way!', B1='Is that right? That’s interesting. I hadn’t heard that.', B2='Short reactions like “Is that right?” or “Wow, I had no idea” invite the speaker to add details.'))],
  compare='In Brazil, “fiquei sabendo que…” and “dizem que…” do a similar job of hedging. In English, “Apparently…” and “I read that…” are the usual tools. Which ones do you use?',
  teach=teach(goal='Entender como se compartilham notícias com cuidado: fonte e grau de certeza.', solo=['Mostre os 3 cartões e peça hipóteses.', 'Compare com “fiquei sabendo que…”.'], group=['Cada estudante escolhe um cartão e explica.', 'Pergunte “Do you agree?”.'], answers=['Q1: heard it, not sure.', 'Q2: so people can check.', 'Q3: Is that right? / No way!'], extra=['Have you ever shared a rumor that was false?', 'How do you check if news is true?'], support=['Use as respostas A1.'], stretch=['B2: discuta por que citar a fonte importa na era das redes sociais.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='newsroom', tod='day', cast=['Amy', 'Tessa']),
  pass1=dict(q='What are Amy and Tessa talking about?', pt='Sobre o que Amy e Tessa conversam?', opts=['A local event', 'A job interview', 'A restaurant'], ans=0),
  pass2=dict(tasks=[dict(label='What is new?', ans='bridge'), dict(label='Opening day', ans='Saturday'), dict(label='Years of work', ans='three years', alt=['three', '3']), dict(label='Extra event', ans='street festival', alt=['festival']), dict(label='Where Tessa read it', ans='website')]),
  teach=teach(goal='Entender a notícia e 5 informações.', solo=['Esconda o texto. 1ª escuta: tema.', '2ª escuta: o que é novo, dia, anos, evento extra e fonte.'], group=['Escuta coletiva; duplas anotam antes de revelar.', 'Mostre o texto no final.'], answers=['Pass 1: a local event.', 'Pass 2: bridge · Saturday · three years · street festival · website.'], extra=['Is Tessa sure about the time?', 'How does Amy check?'], support=['Use “Slow” e pause após cada fala.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='What is opening on Saturday?', opts=['A bridge', 'A park', 'A museum'], ans=0), dict(q='Where did Tessa read about the festival?', opts=['On the city’s website', 'In a newspaper', 'On the radio'], ans=0), dict(q='What is Tessa not sure about?', opts=['The time', 'The day', 'The place'], ans=0), dict(q='What time does it start, according to the mayor’s office?', opts=['Ten a.m.', 'Noon', 'Eight a.m.'], ans=0)],
  retell=dict(prompt='Retell the news in your own words and say who said what.', starters=['Amy told Tessa that…', 'Apparently…', 'Tessa read that…', 'According to…']),
  teach=teach(goal='Ler o diálogo, perceber os chunks e recontar com a fonte.', solo=['O estudante lê Tessa; você lê Amy.', 'Peça o reconto com “according to”.'], group=['Leitura em duplas.', 'Reconto em cadeia.'], answers=['A bridge · On the city’s website · The time · Ten a.m.'], extra=['Would you go to the festival?', 'What would you ask about the bridge?'], errors=[E('Yes, I heard.', 'Yes, I did. / No, I didn’t.'), E('I read that in the website.', 'I read that on the website.')], support=['Mostre a tradução (PT) após a 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[dict(en='Did you hear about…?', pt='Você ficou sabendo de…?', use='Introduce news.', reg='neutral', alt='Also: **Have you heard about…?**', pri=True),
         dict(en='Apparently,…', pt='Pelo visto,…', use='Share news you have heard but not confirmed.', reg='neutral', pri=True),
         dict(en='I read that…', pt='Li que…', use='Share information and name the type of source.', reg='neutral', alt='Also: **I heard that…**', pri=True),
         dict(en='According to…', pt='Segundo…', use='Name the exact source.', reg='neutral', pri=True),
         dict(en='Is that right?', pt='É mesmo?', use='React with interest.', reg='neutral'),
         dict(en='I’m not sure.', pt='Não tenho certeza.', use='Show you are not certain.', reg='neutral'),
         dict(en='Let me check.', pt='Deixa eu conferir.', use='Offer to verify.', reg='casual'),
         dict(en='No way!', pt='Não acredito!', use='React with surprise.', reg='casual')],
  discover=dict(fns=['Introducing news', 'Showing doubt', 'Naming a source', 'Reacting', 'Checking'],
   items=[dict(en='Did you hear about the new bridge?', fn='Introducing news'), dict(en='Apparently, it opens on Saturday.', fn='Showing doubt'), dict(en='According to the mayor’s office, it starts at ten.', fn='Naming a source'), dict(en='Is that right?', fn='Reacting'), dict(en='Let me check.', fn='Checking')]),
  note='Choose the 4 starred expressions to use again and again; the others help you react and check.',
  teach=teach(goal='Escolher 4 chunks e ligar cada um à função de compartilhar notícias.', solo=['Pergunte “When do you say it?”.', 'Peça uma notícia real com cada chunk.'], group=['Cada estudante escolhe um chunk e dá um exemplo.', 'Duplas: contar uma notícia curta.'], answers=['Introducing · Showing doubt · Naming a source · Reacting · Checking'], extra=['Which one sounds most careful?'], errors=[E('Apparently, it is 100% true.', 'Apparently = pelo visto (ainda não confirmado).'), E('Did you heard about…?', 'Did you hear about…?')], support=['Trabalhe só as 4 expressões ★.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Introducing news', formula='**Did you hear about** + noun?', ex=['Did you hear about the new bridge?', 'Did you hear about the concert?', 'Did you hear about Mia’s job?'], main=True),
            dict(name='Sharing with the source', formula='**I read that / Apparently / According to** + clause', ex=['I read that there will be a festival.', 'Apparently, it opens on Saturday.', 'According to the mayor’s office, it starts at ten.'], main=True),
            dict(name='Showing certainty', formula='**I’m (not) sure** + about + noun', ex=['I’m not sure about the time.', 'I’m sure it starts at ten.'])],
  swap=dict(frame='I read that the {thing} {event}.', tpt='Li que {thing} {event}.',
   slots=[dict(k='thing', label='Thing', opts=[dict(en='bridge', pt='a ponte'), dict(en='library', pt='a biblioteca'), dict(en='stadium', pt='o estádio')]),
          dict(k='event', label='Event', opts=[dict(en='opens on Saturday', pt='abre no sábado'), dict(en='closes next week', pt='fecha na próxima semana'), dict(en='is under construction', pt='está em obras')])]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['Did you hear about…?', 'Have you heard about…?'], ['Apparently, it opens Saturday.', 'It has been reported that it will open on Saturday.'], ['I read that…', 'According to reports…'], ['No way!', 'That is surprising.']], note='“According to reports” is common in news writing; “Apparently” is more spoken.'),
  teach=teach(goal='Introduzir notícias, citar a fonte e mostrar o grau de certeza.', solo=['Mostre os padrões no diálogo.', 'Use “Swap the words” em voz alta.'], group=['Troca em cadeia: cada estudante muda UMA peça.', 'Duplas: uma notícia com fonte.'], answers='Padrões 01/02 são o foco; 03 é expansão.', extra=['Tell me one piece of news with “apparently”.', 'Share a rumor with “I’m not sure”.'], errors=[E('Did you heard…?', 'Did you hear…?'), E('I read that in the news that…', 'I read that… / I read in the news that…'), E('According me…', 'According to me… / In my opinion…')], support=['Fique só com Did you hear about… + Apparently…'], stretch=['Combine os 3 padrões em um comentário.'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Intonation', tip='A question that expects “yes/no” goes up at the end; a statement goes down. “Did you hear about the bridge?” ↗ · “It opens Saturday.” ↘',
  items=[dict(say='Did you hear about the bridge?', linked='Did-ya HEAR a·bout the BRIDGE? ↗', ipa='/dɪdʒə/', rhythm='ooOooOo'), dict(say='Apparently, it opens Saturday.', linked='a·PAR·ent·ly, it O·pens SAT·ur·day. ↘', ipa='/əˈpɛrəntli/', rhythm='oOoooOoo'), dict(say='Is that right?', linked='Is THAT RIGHT? ↗', ipa='/raɪt/', rhythm='oOO')],
  identify=[dict(q='Which one do you hear?', opts=['Did you hear about the bridge?', 'Do you hear about the bridge?', 'Did you hear a bridge?'], ans=0, say='Did you hear about the bridge?'), dict(q='Which one do you hear?', opts=['Is that right?', 'Is that bright?', 'Is it right?'], ans=0, say='Is that right?')],
  own=dict(prompt='Write a question that starts with “Did you hear about…” using real news.', criteria='Say it twice: with rising intonation, then as a statement. Can your partner hear the difference?'),
  teach=teach(goal='UM só fenômeno: entonação ascendente em perguntas e descendente em afirmações.', solo=['Escutar e identificar → repetir com a mão subindo e descendo.', 'Faça perguntas e afirmações para o estudante distinguir.'], group=['Coro, depois duplas.', 'Cada estudante cria uma pergunta com entonação.'], answers=['Identify 1: Did you hear about the bridge? · Identify 2: Is that right?'], errors=[E('Pergunta com entonação plana', 'Subir no final da pergunta'), E('“hear” e “here” confundidos', '/hɪr/ para os dois (mesma pronúncia); o contexto muda')], support=['Reduza a velocidade e use a mão como guia.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    dict(type='mcq', q='1. You want to share news politely. What do you say?', opts=['Did you hear about the new bridge?', 'You hear the bridge?', 'Hear you bridge?'], ans=0, why='Did you hear about + noun?'),
    dict(type='mcq', q='2. You heard it from a friend, but you are not sure it is true.', opts=['Apparently, it opens on Saturday.', 'It opens on Saturday, I am sure.', 'It is true because I say.'], ans=0, why='Apparently signals secondhand information.'),
    dict(type='mcq', q='3. You read it on the city’s website.', opts=['I read that it opens on Saturday.', 'I have read opens Saturday.', 'I reading that.'], ans=0, why='I read that + clause.'),
    dict(type='mcq', q='4. A friend tells you surprising news. What do you reply?', opts=['Is that right?', 'I am right.', 'Surprising is me.'], ans=0, why='Is that right? is a natural reaction.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    dict(type='gap', text='Did you ___ about the new bridge?', ans='hear', bank=['hear', 'listen', 'hearing'], why='Did you hear about…?'),
    dict(type='gap', text='___ to the mayor’s office, it starts at ten.', ans='According', bank=['According', 'Apparently', 'Reading'], why='According to + source.'),
    dict(type='swap', instr='Add the source:', frm='It opens on Saturday.', ans=['I read that it opens on Saturday.', 'Apparently, it opens on Saturday.', 'According to the website, it opens on Saturday.'], model='I read that it opens on Saturday.', why='Add a source or hedge.'),
    dict(type='swap', instr='Show you are not sure:', frm='It starts at ten.', ans=['I’m not sure, but I think it starts at ten.', 'Apparently, it starts at ten.', 'I’m not sure it starts at ten.'], model='I’m not sure, but I think it starts at ten.', why='Hedging shows uncertainty.'),
    dict(type='reply', npc='Did you hear about the concert on Friday?', q='Choose the best reply.', opts=['No! What happened?', 'Yes, I am hearing.', 'Concert is Friday I.'], ans=0, why='Show interest and ask for details.')])],
  teach=teach(goal='Do controlado ao guiado antes da fala livre.', solo=['Peça que justifique cada resposta.', 'Peça uma versão com outra fonte.'], group=['Duplas comparam antes de revelar.', 'Pontos por resposta justificada.'], answers=['1: Did you hear about the new bridge? · 2: Apparently, it opens on Saturday. · 3: I read that it opens on Saturday. · 4: Is that right?', 'Gap: hear · According · I read that… · I’m not sure, but I think… · No! What happened?'], extra=['Say each answer with natural intonation.'], errors=[E('Did you heard about…?', 'Did you hear about…?'), E('Apparently, I am sure.', 'Apparently, it starts at ten. / I’m sure it starts at ten.')], support=['Ofereça o banco de palavras.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — share the news',
  brief=dict(teacher='You are a colleague who does not know the news. Ask where you heard it and whether it is sure.', student='Share one piece of local news: say what, when, source and how sure you are.'),
  orders=['A new restaurant opening', 'A concert or festival in the city', 'A road closing for repairs'],
  complications=['The colleague already knows and adds details.', 'You are not sure about the time.', 'The colleague asks “Where did you read it?”', 'The news turns out to be wrong: correct yourself.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['Did you hear about…?', 'Apparently…', 'I read that…', 'According to…']), dict(label='Keywords', desc='Only the keywords', help=['bridge', 'Saturday', 'website', 'ten'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I introduce the news.', 'I say where I heard it.', 'I show how sure I am.', 'I react to my partner’s news.'],
  teach=teach(goal='Compartilhar notícia com fonte e grau de certeza.', solo=['Use notícias reais da cidade do aluno.', 'Rodada 1 com chunks, 2 palavras-chave, 3 livre.', 'Anote 2–3 correções.'], extra=['What if the information was wrong?', 'How do you correct yourself politely?'], errors=[E('Sorry, I mistake.', 'Sorry, I was wrong. / Sorry, I made a mistake.')], support=['Volte à rodada 1 se travar.'], stretch=['Conte a mesma notícia a um chefe e a um amigo.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Share one piece of news', min=3, task='Tell your partner one piece of local news.', hint='Did you hear about…?'), dict(title='Name the source', min=3, task='Say where you read or heard it.', hint='I read that… / According to…'), dict(title='Check and react', min=3, task='Your partner reacts, asks, and says if they are sure.', hint='Is that right? / I’m not sure.'), dict(title='News flash', min=2, whole=True, task='Whole group: each pair gives a 20-second news flash.', hint='Breaking news: …')],
  infogap=dict(title='City news board', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='Student A: your news', task='You know the bridge and the library. Ask about the rest.', rows=[dict(k='New bridge', v='opens Saturday at 10 a.m.'), dict(k='Street festival', v=''), dict(k='Library', v='closed on Monday'), dict(k='Stadium', v='')]),
   b=dict(title='Student B: your news', task='You know the festival and the stadium. Ask about the rest.', rows=[dict(k='New bridge', v=''), dict(k='Street festival', v='free, with food trucks'), dict(k='Library', v=''), dict(k='Stadium', v='concert on Friday night')])),
  teach=teach(goal='Fluência em compartilhar e checar notícias com informações novas.', group=['Troque os pares a cada rodada.', 'Responsabilidade individual: cada aluno compartilha uma notícia e reage a outra.', 'Sem salas simultâneas.'], answers=['Info gap: A tem bridge e library; B tem festival e stadium. Cada um completa com “Did you hear about…?”.'], extra=['Did you hear about the festival?', 'Is the library open on Monday?'], errors=[E('The bridge opens in Saturday.', 'The bridge opens on Saturday.'), E('The festival is free of cost.', 'The festival is free.')], support=['Entregue frases-modelo no chat.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — news of the day',
  goal='Each group must share news, name the source and decide what is certain.',
  missions=[dict(who='A', role='Morning news team', mission='Each student shares one piece of news. The others react and ask for the source.', constraint='Use “Did you hear about…?” and “According to…”.', start='Did you hear about…'),
            dict(who='B', role='Rumor checkers', mission='One student shares a rumor; the group decides what to check.', constraint='Use “Apparently” and “I’m not sure”.', start='Apparently…'),
            dict(who='C', role='Event planners', mission='Share information about an event and agree on three facts.', constraint='Use “I read that…” and “Is that right?”.', start='I read that…')], min=11,
  success=['Introduce the news.', 'Name the source.', 'Show how sure you are.', 'React and ask.'],
  teach=teach(goal='Compartilhar notícias e distinguir o que é certo do que é dúvida.', group=['Cada grupo recebe papéis e restrição.', 'Progressão: com chunks, palavras-chave, sem roteiro.', 'Anote 2–3 correções.'], answers=['Modelo: “Did you hear about the new bridge?” → “Apparently, it opens on Saturday.” → “Is that right? Where did you read it?”'], extra=['Which news was the most surprising?'], support=['Dê o início de frase em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short message to a friend sharing news about an event and say where you read it.',
  steps=['Greeting + news', 'Details', 'Source', 'Closing'],
  model='Hi Tessa! Did you hear about the new bridge? Apparently, it opens this Saturday at ten a.m., and I read that there will be a street festival. I’m not sure about the exact time. Want to go together?',
  checklist=['I introduced the news.', 'I gave one or two details.', 'I said where I read it or how sure I am.', 'I asked a question to close.'],
  tip='Fix only 2–3 priority points and show a more natural way to say the same idea.', fix=dict(n=3),
  teach=teach(goal='Produção escrita curta: compartilhar notícias por mensagem.', solo=['Corrija 2–3 pontos prioritários.'], group=['Troquem os textos e respondam como amigos.'], extra=['Add a source and one doubt.'], errors=[E('Did you heard about…?', 'Did you hear about…?'), E('Apparently, I’m sure.', 'Apparently, it starts at ten.')], support=['Dê o modelo e peça só para trocar os dados.'])),
 fb_page('Example: You gave the source and showed how sure you were.', 'Example: Use rising intonation in “Did you hear about…?”.', 'Example: Share news for one minute without notes.', 'notícias com fonte e certeza.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❓', name='Introduce news', prompt='Without notes: ask about a new restaurant.', model='Did you hear about the new restaurant?'), dict(ic='💬', name='Share with a source', prompt='Say you read that the museum is free on Sundays.', model='I read that the museum is free on Sundays.'), dict(ic='⭐', name='Show doubt', prompt='Say it starts at ten, but you are not sure.', model='Apparently, it starts at ten, but I’m not sure.')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 45–60 second audio sharing a piece of news.', 'Write three sentences with Apparently, I read that and According to.', 'Review the four expressions ★ and create your own examples.', 'Listen to the dialogue again and find two reactions.']),
  spaced=dict(next=['Did you hear about…?', 'Apparently…', 'I read that…'], week=['According to…', 'Is that right?', 'Could you tell me how to get to…?'], unit=['Invite · experiences · stories · directions · news']),
  teach=teach(goal='Toda aula termina com uma produção observável.', solo=['Sem anotações: introduzir, citar a fonte e mostrar dúvida.'], group=['Exit challenge individual.'], answers=['Did you hear about the new restaurant? · I read that the museum is free on Sundays. · Apparently, it starts at ten, but I’m not sure.'], extra=['Revisão espaçada: próxima aula, uma semana depois e na missão da unidade.'])),
 lv_page([('News! Bridge open Saturday.', 'Share news with a few key words.'), ('Did you hear about the bridge? It opens on Saturday.', 'Share news with a simple opening.'), ('Apparently, the bridge opens on Saturday, but I’m not sure about the time.', 'Share news with a source and hedge.'), ('According to the city, the bridge is due to open on Saturday, although there has been no official confirmation of the time.', 'Report news with attribution and precision.'), ('While the city insists the bridge will open on Saturday, I’d take that with a pinch of salt given the delays so far.', 'Evaluate news critically.'), ('One suspects the Saturday date is aspirational at best, given how long that bridge has taken.', 'Comment on news with tone and irony.')])
]
LESSON = mk(91, 5, 'News and events', 'Notícias e eventos', ['Amy', 'Tessa'], 'newsroom', 'day', PAGES, DIALOG)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
