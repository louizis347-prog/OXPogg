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

DIALOG = dict(speakers={'Host': {'name': 'Rosa'}, 'Friend': {'name': 'Diego'}}, lines=[
 dict(who='Friend', en='Hey Rosa! **Would you like to** come to my photo show on Friday night?', pt='Oi, Rosa! Você gostaria de ir à minha exposição de fotos na sexta à noite?'),
 dict(who='Host', en='Oh, **I’d love to, but** I have to work late at the flower shop.', pt='Ah, eu adoraria, mas preciso trabalhar até tarde na floricultura.'),
 dict(who='Friend', en='That’s too bad. It’s my first show, so I really wanted you there.', pt='Que pena. É a minha primeira exposição, então eu queria muito você lá.'),
 dict(who='Host', en='Congratulations! **Thanks for asking** — I’m so sorry I can’t make it.', pt='Parabéns! Obrigada por convidar. Sinto muito por não poder ir.'),
 dict(who='Friend', en='No worries! **Would you like to** come on Saturday afternoon instead? It’s open all weekend.', pt='Sem problema! Quer ir no sábado à tarde? A exposição fica aberta o fim de semana todo.'),
 dict(who='Host', en='Saturday works! What time should we meet?', pt='Sábado funciona! A que horas a gente se encontra?'),
 dict(who='Friend', en='How about two o’clock? We could have coffee afterwards.', pt='Que tal às duas? Depois a gente poderia tomar um café.'),
 dict(who='Host', en='Perfect. And **maybe next time** I can bring flowers for your next opening.', pt='Perfeito. E talvez da próxima vez eu leve flores para a sua próxima abertura.'),
 dict(who='Friend', en='Ha! Great idea. See you Saturday, then.', pt='Ha! Ótima ideia. Então nos vemos no sábado.')])

PAGES = [
 dict(t='rl_open', stage='warm', title='Invitations: accept and decline', pt='Convites: aceitar e recusar', level='A2', unit=unit(1),
  situation=dict(text='A friend invites you to an event on a night when you are busy. You decline politely, show you care and suggest another day.', scene='livingroom', tod='dusk', cast=['Rosa', 'Diego']),
  goal='By the end of the class you can invite someone, accept with enthusiasm, decline politely with a reason and suggest another plan.',
  canDo=['Invite someone: Would you like to…?', 'Decline kindly: I’d love to, but…', 'Suggest another time: How about…?', 'Accept and confirm the plan'],
  success=['I invite or answer an invitation.', 'I give a short reason.', 'I suggest another plan.', 'We both end the conversation happy.'],
  think='In Portuguese, how do you say no to an invitation without hurting someone’s feelings? Do you use the same words in English?',
  teach=teach(goal='Abrir pela situação: recusar sem magoar.', solo=['Leia o objetivo e pergunte como o estudante recusa convites em português.', 'Mostre os 4 critérios: é a missão final.'], group=['Cada estudante conta (em uma frase) um convite que já recusou.', 'Escreva no quadro as razões mais comuns.'], extra=['Do you like invitations or do you feel pressure?', 'When did you last say “no” to a plan?'], support=['Aceite respostas curtas e reformule em inglês.'])),
 dict(t='rl_warm', stage='warm', title='Connection & warm-up',
  intro=dict(solo='Ask about the student’s week and weekend plans, and listen for “going to”.', group='One question per student, then a question back to a classmate.'),
  recall='Unit 11 (making plans): “I’m going to…”. Ask: What are you going to do this weekend?',
  qs=[dict(q='What are you doing this weekend?', pt='O que você vai fazer neste fim de semana?', sup=['I’m going to…', 'Nothing special.', 'I’m meeting friends.']),
      dict(q='Who do you invite when you have good news?', pt='Quem você convida quando tem uma boa notícia?', sup=['My family.', 'My best friend.', 'Everyone!']),
      dict(q='Do you prefer big parties or small dinners?', pt='Você prefere festas grandes ou jantares pequenos?', sup=['Small dinners.', 'Big parties.', 'It depends.'])],
  tip='Use the answers to find weekend vocabulary the student already has, and recycle it in the invitations.',
  teach=teach(goal='Ativar vocabulário de planos e entrar no tema.', extra=['What is your ideal Saturday night?', 'Who is the most social person you know?'], errors=[E('I have 30 years.', 'I’m 30.'), E('I will to travel.', 'I’m going to travel.')], support=['Ofereça as respostas-chip e peça que escolham uma.'])),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Declining politely',
  intro='In English, a “no” usually comes wrapped in thanks, a reason and an alternative. Look and guess before you read.',
  cards=[dict(vis='obj:envelope', en='Thank first', pt='Agradeça primeiro', note='“Thanks for asking” shows you appreciate the invitation.'),
         dict(vis='obj:clock', en='Give a short reason', pt='Dê um motivo curto', note='“I have to work late” is enough. You do not need a long story.'),
         dict(vis='obj:phone', en='Offer another plan', pt='Ofereça outro plano', note='“Maybe next time” or “How about Sunday?” keeps the friendship warm.')],
  qs=[dict(q='Why do people say “Thanks for asking” when they decline?', pt='Por que se diz “Thanks for asking” ao recusar?', levels=dict(A1='To be nice.', A2='Because they want to be polite and show they care.', B1='It shows appreciation for the invitation, so the “no” does not sound like a rejection.', B2='It separates the answer from the relationship: you refuse the plan, not the person.')),
      dict(q='Is a short reason enough?', pt='Um motivo curto basta?', levels=dict(A1='Yes. “I’m busy.”', A2='Yes. “I have to work” is enough.', B1='Usually yes. A short, honest reason is enough and a long excuse can sound strange.', B2='A brief reason is generally enough; over-explaining can make the refusal sound less sincere.')),
      dict(q='What can you say instead of a direct “no”?', pt='O que dizer no lugar de um “não” direto?', levels=dict(A1='I’d love to, but…', A2='I’d love to, but I can’t. Maybe next time.', B1='I’d love to, but I already have plans. Can we do it another day?', B2='Softening phrases such as “I’d love to, but…” plus an alternative keep the door open.'))],
  compare='In Brazil it is common to say “vou ver” (I’ll see) or “quem sabe” and leave the answer open. In English, a clear polite answer is often preferred: thank, decline, give a reason. How is it where you live?',
  teach=teach(goal='Mostrar a estrutura de uma recusa educada: agradecer, motivo, alternativa.', solo=['Mostre os 3 cartões e peça hipóteses.', 'Compare com o “vou ver” brasileiro: pergunte se o estudante concorda.'], group=['Cada estudante escolhe um cartão e explica em uma frase.', 'Pergunte “Do you agree?” entre colegas.'], answers=['Q1: appreciation / politeness.', 'Q2: yes, a short reason.', 'Q3: I’d love to, but… + maybe next time.'], extra=['Is it rude to say a simple “no, thanks”?', 'What is a good reason to decline?'], support=['Use as respostas A1 como andaime e peça que repitam.'], stretch=['B2: discuta quando um “não” direto é aceitável.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='livingroom', tod='dusk', cast=['Rosa', 'Diego']),
  pass1=dict(q='What is Diego doing?', pt='O que o Diego está fazendo?', opts=['Inviting Rosa to an event', 'Asking for a job', 'Saying goodbye'], ans=0),
  pass2=dict(tasks=[dict(label='The event', ans='photo show', alt=['photo']), dict(label='First day', ans='Friday'), dict(label='Rosa’s reason', ans='work late', alt=['work']), dict(label='New day', ans='Saturday'), dict(label='Time', ans='two o’clock', alt=['two', '2'])]),
  teach=teach(goal='Entender a situação e depois 3–5 informações.', solo=['Esconda o texto. 1ª escuta: ideia principal.', '2ª escuta: evento, dia, motivo, novo dia e hora.'], group=['Escuta coletiva; duplas anotam antes de revelar.', 'Compare as respostas e só então mostre o texto.'], answers=['Pass 1: inviting Rosa.', 'Pass 2: photo show · Friday · work late · Saturday · two o’clock.'], extra=['How does Diego feel? How do you know?', 'Does Rosa really want to go?'], support=['Use o botão “Slow” e pause após cada fala.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='What is Diego’s show about?', opts=['Flowers', 'Photos', 'Music'], ans=1), dict(q='Why can’t Rosa go on Friday?', opts=['She is sick', 'She has to work late', 'She is traveling'], ans=1), dict(q='When do they decide to go?', opts=['Saturday afternoon', 'Friday night', 'Sunday morning'], ans=0), dict(q='What does Diego suggest after the show?', opts=['Dinner', 'Coffee', 'A walk'], ans=1)],
  retell=dict(prompt='Retell the conversation in your own words.', starters=['Diego invites Rosa to…', 'She can’t go because…', 'Then he suggests…', 'In the end, they…']),
  teach=teach(goal='Ler o diálogo, perceber os chunks e recontar.', solo=['O estudante lê Rosa; você lê Diego; depois troquem.', 'Peça o reconto no nível que conseguir.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia: uma frase por estudante.'], answers=['photos · work late · Saturday afternoon · coffee'], extra=['What would you say if you could go?', 'Is Diego disappointed? How do you know?'], errors=[E('I can’t go because I work.', 'I’d love to, but I have to work.'), E('Thanks to invite me.', 'Thanks for inviting me. / Thanks for asking.')], support=['Mostre a tradução (PT) após a 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[dict(en='Would you like to…?', pt='Você gostaria de…?', use='Invite someone politely.', reg='polite', alt='Casual: **Do you want to…?**', pri=True),
         dict(en='I’d love to, but…', pt='Eu adoraria, mas…', use='Decline kindly and give a reason.', reg='polite', alt='Also: **I wish I could, but…**', pri=True),
         dict(en='Thanks for asking.', pt='Obrigado por convidar.', use='Show appreciation, even when you say no.', reg='neutral', pri=True),
         dict(en='Maybe next time.', pt='Quem sabe da próxima vez.', use='Keep the door open after declining.', reg='neutral', alt='Also: **Let’s do it another time.**', pri=True),
         dict(en='Saturday works!', pt='Sábado funciona!', use='Accept a new suggestion.', reg='casual', alt='Also: **That works for me.**'),
         dict(en='That’s too bad.', pt='Que pena.', use='Show sympathy when someone can’t come.', reg='neutral'),
         dict(en='No worries!', pt='Sem problema!', use='Tell the other person it is fine.', reg='casual'),
         dict(en='How about…?', pt='Que tal…?', use='Suggest another day or plan.', reg='neutral')],
  discover=dict(fns=['Inviting', 'Declining', 'Showing appreciation', 'Reacting', 'Suggesting'],
   items=[dict(en='Would you like to come on Saturday?', fn='Inviting'), dict(en='I’d love to, but I have to work.', fn='Declining'), dict(en='Thanks for asking.', fn='Showing appreciation'), dict(en='No worries!', fn='Reacting'), dict(en='How about two o’clock?', fn='Suggesting')]),
  note='Choose the 4 starred expressions to use again and again; the others help you understand and react.',
  teach=teach(goal='Escolher 4 chunks prioritários e descobrir a função de cada um.', solo=['Pergunte “When do you say it?” antes da tradução.', 'Compare Would you like to… × Do you want to… (formal × informal).'], group=['Cada estudante escolhe a expressão que mais usaria e explica quando.', 'Duplas: convite e recusa usando apenas 3 chunks.'], answers=['Inviting · Declining · Showing appreciation · Reacting · Suggesting'], extra=['Which expression would you use with your boss? With a friend?'], errors=[E('I can’t, sorry. (seco, sem motivo)', 'I’d love to, but I can’t. Thanks for asking.'), E('Do you want go to the cinema?', 'Do you want to go to the cinema?')], support=['Trabalhe só as 4 expressões ★.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Inviting', formula='**Would you like to** + base verb?', ex=['Would you like to come to dinner?', 'Would you like to join us on Sunday?', 'Would you like to see the show?'], main=True),
            dict(name='Declining with a reason', formula='**I’d love to, but** I + have to / can’t / already have…', ex=['I’d love to, but I have to work.', 'I’d love to, but I already have plans.', 'I’d love to, but I can’t on Friday.'], main=True),
            dict(name='Suggesting another plan', formula='**How about** + day / time / -ing?', ex=['How about Saturday?', 'How about meeting at two?', 'How about having coffee afterwards?'])],
  swap=dict(frame='Would you like to {activity} on {day}?', tpt='Você gostaria de {activity} no {day}?',
   slots=[dict(k='activity', label='Activity', opts=[dict(en='come to my show', pt='ir à minha exposição'), dict(en='have dinner with us', pt='jantar com a gente'), dict(en='go for a walk', pt='dar uma caminhada')]),
          dict(k='day', label='Day', opts=[dict(en='Friday', pt='sexta'), dict(en='Saturday', pt='sábado'), dict(en='Sunday', pt='domingo')])]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['Wanna come?', 'Would you like to join us?'], ['Can’t, sorry. Work.', 'Unfortunately, I have a work commitment.'], ['Saturday works!', 'Saturday would be convenient.'], ['No worries!', 'There is no need to apologize.']], note='“Wanna” is informal speech; use “Would you like to” when you want to sound polite.'),
  teach=teach(goal='Fixar 2 padrões principais: convidar e recusar com motivo.', solo=['Mostre os padrões DENTRO do diálogo.', 'Use “Swap the words” e peça a frase completa.'], group=['Troca em cadeia: cada estudante muda UMA peça.', 'Em pares: um convida, o outro recusa.'], answers='Padrões 01/02 são o foco; 03 é expansão.', extra=['Invite me to something you really like.', 'Decline an invitation with two different reasons.'], errors=[E('Would you like go?', 'Would you like to go?'), E('I’d love to, but I have work. (ok) / I’d love but…', 'I’d love to, but…'), E('How about to go on Saturday?', 'How about going on Saturday? / How about Saturday?')], support=['Fique só com Would you like to… + I’d love to, but… na primeira rodada.'], stretch=['Combine os 3 padrões em uma única resposta.'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Linking and reduction', tip='In fast speech “would you” sounds like “wouldja” and “to” becomes a weak “ta”. Clear does not mean slow and word by word.',
  items=[dict(say='Would you like to come?', linked='Wou·dja like ta come?', ipa='/wʊdʒə/', rhythm='oooOoO'), dict(say='I’d love to, but I can’t.', linked='I’d LOVE ta, but I CAN’T.', ipa='/lʌv tə/', rhythm='oOooooO'), dict(say='Thanks for asking.', linked='THANKS fer ASK·ing.', ipa='/fər/', rhythm='OoOo')],
  identify=[dict(q='Which one do you hear?', opts=['Would you like to come?', 'Would he like to come?', 'Could you like to come?'], ans=0, say='Would you like to come?'), dict(q='Which one do you hear?', opts=['I’d love to, but I can’t.', 'I’d love it, but I can’t.', 'I love to, but I can’t.'], ans=0, say='I’d love to, but I can’t.')],
  own=dict(prompt='Write an invitation using “Would you like to…” for a real plan.', criteria='Say it twice: slowly, then linked (“wouldja”). Did the stress fall on the key word?'),
  teach=teach(goal='UM só fenômeno: ligação e redução (would you / to / for).', solo=['Escutar e identificar → repetir ritmo → criar convite próprio.', 'Bata palmas nas sílabas fortes.'], group=['Coro, depois duplas; circule ouvindo.', 'Cada estudante cria um convite com a ligação.'], answers=['Identify 1: Would you like to come? · Identify 2: I’d love to, but I can’t.'], errors=[E('Would — you (pausa)', 'Wou·dja (ligado)'), E('Pronunciar todo “to” forte', '“to” fraco: /tə/')], support=['Reduza a velocidade e conte as batidas.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    dict(type='mcq', q='1. You want to invite a friend to dinner. What do you say?', opts=['Would you like to have dinner with me?', 'You have dinner with me.', 'Do you dinner?'], ans=0, why='Would you like to + verb is a polite invitation.'),
    dict(type='mcq', q='2. You can’t go. Which reply is kind and clear?', opts=['No.', 'I’d love to, but I have to work.', 'I don’t like parties.'], ans=1, why='Thanks/“I’d love to, but” + short reason keeps it warm.'),
    dict(type='mcq', q='3. Your friend says “Would you like to come on Sunday?” You are free.', opts=['Sunday works!', 'Sunday is working!', 'I work Sunday.'], ans=0, why='“Works” is the natural verb to accept a day.'),
    dict(type='mcq', q='4. A colleague says “It’s my birthday party on Friday!” You cannot go.', opts=['Thanks for asking. Maybe next time!', 'I will never go.', 'Why you invite me?'], ans=0, why='Thank first, then keep the door open.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    dict(type='gap', text='Would you ___ to come to the show?', ans='like', bank=['like', 'want', 'love'], why='Would you like to + verb.'),
    dict(type='gap', text='I’d love ___, but I have to work.', ans='to', bank=['to', 'it', 'for'], why='I’d love to, but…'),
    dict(type='swap', instr='Make it more polite:', frm='Do you want to come?', ans=['Would you like to come?', 'Would you like to come with us?'], model='Would you like to come?', why='Would you like to… sounds softer.'),
    dict(type='swap', instr='Suggest another day:', frm='Saturday', ans=['How about Saturday?', 'How about Saturday instead?'], model='How about Saturday?', why='How about + day.'),
    dict(type='reply', npc='Would you like to come on Friday?', q='Choose the best way to decline.', opts=['I’d love to, but I already have plans.', 'No, never.', 'I am Friday.'], ans=0, why='Kind refusal with a short reason.')])],
  teach=teach(goal='Do controlado ao guiado antes da fala livre.', solo=['Peça que justifique cada resposta.', 'Se acertar rápido, peça uma versão mais informal.'], group=['Resolvam em duplas e comparem antes de revelar.', 'Equipes: ponto por resposta justificada.'], answers=['1: Would you like to have dinner with me? · 2: I’d love to, but I have to work. · 3: Sunday works! · 4: Thanks for asking. Maybe next time!', 'Gap: like · to · Would you like to come? · How about Saturday? · I’d love to, but I already have plans.'], extra=['Say each answer with friendly intonation.'], errors=[E('Would you like to going?', 'Would you like to go?'), E('I’d love to but I don’t want.', 'I’d love to, but I can’t.')], support=['Ofereça o banco de palavras.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — invite and decline',
  brief=dict(teacher='You are the friend who invites. Keep suggesting new plans!', student='You are the invited person: decline once, then accept a new plan.'),
  orders=['A birthday dinner on Saturday', 'A beach day on Sunday morning', 'A dance class on Wednesday night'],
  complications=['The friend sounds disappointed.', 'You already have plans, but you like the person.', 'The friend suggests a time you cannot do either.', 'The friend insists: “Please come!”'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['Would you like to…?', 'I’d love to, but…', 'Thanks for asking.', 'How about…?']), dict(label='Keywords', desc='Only the keywords', help=['dinner', 'work late', 'Saturday', 'two o’clock'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I invite or answer an invitation.', 'I give a short reason.', 'I suggest another plan.', 'We both end the conversation happy.'],
  teach=teach(goal='Simulação com recusa, alternativa e aceite, com menos apoio a cada rodada.', solo=['Use eventos reais da vida do estudante.', 'Rodada 1 com chunks, 2 com palavras-chave, 3 sem roteiro.', 'Fale 30% do tempo; anote 2–3 correções.'], extra=['What if you really don’t want to go?', 'How would you decline a very close friend?'], errors=[E('I can’t because I have a thing.', 'I’d love to, but I already have plans.')], support=['Volte à rodada 1 se travar.'], stretch=['Recuse um convite de um chefe, depois de um amigo, e compare o tom.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Simple invitations', min=3, task='Invite your partner to an event. They accept.', hint='Would you like to…? / Sounds great!'), dict(title='Decline kindly', min=3, task='Invite; your partner declines with a reason.', hint='I’d love to, but… / Thanks for asking.'), dict(title='Find a new plan', min=3, task='After the “no”, agree on another day.', hint='How about…? / … works!'), dict(title='Share the best excuse', min=2, whole=True, task='Whole group: each pair shares the most polite refusal.', hint='We decided to… because…')],
  infogap=dict(title='Weekend calendar', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='Student A: your calendar', task='You know Friday and Saturday. Ask about the rest so you can plan a hangout.', rows=[dict(k='Friday night', v='busy: work late'), dict(k='Saturday afternoon', v='free'), dict(k='Sunday morning', v=''), dict(k='Sunday night', v='')]),
   b=dict(title='Student B: your calendar', task='You know Sunday. Ask about Friday and Saturday so you can plan a hangout.', rows=[dict(k='Friday night', v=''), dict(k='Saturday afternoon', v=''), dict(k='Sunday morning', v='free'), dict(k='Sunday night', v='dinner with family')])),
  teach=teach(goal='Fluência por repetição: convidar, recusar e combinar um novo dia.', group=['Troque os pares a cada rodada.', 'Responsabilidade individual: cada aluno convida e recusa pelo menos uma vez.', 'Sem salas simultâneas: interações sequenciais.'], answers=['Info gap: A sabe Friday (busy) e Saturday (free); B sabe Sunday (morning free, night dinner). Perguntando, escolhem um horário: Saturday afternoon ou Sunday morning.'], extra=['Are you free on Sunday morning?', 'What are you doing on Friday night?'], errors=[E('I am free in Sunday.', 'I’m free on Sunday.'), E('At Saturday', 'On Saturday')], support=['Entregue as frases-modelo no chat.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — invite and decline',
  goal='Each group must invite, decline politely and agree on a new plan in English.',
  missions=[dict(who='A', role='Friends', mission='Invite your friend to a birthday dinner. They cannot go on Saturday. Agree on Sunday.', constraint='Use “Would you like to…?” and “How about…?”', start='Hi! Would you like to…'),
            dict(who='B', role='Colleagues', mission='A colleague invites you to a team lunch. You have a meeting. Decline kindly.', constraint='Say “Thanks for asking” and give one reason.', start='Hey! Would you like to…'),
            dict(who='C', role='Neighbors', mission='Invite a neighbor to a small garden party. They say maybe next time. Respond kindly.', constraint='Use “No worries!” and suggest one more option.', start='Hello! Would you like to…')], min=11,
  success=['Make the invitation.', 'Decline kindly with a reason.', 'Suggest another plan.', 'End the conversation warmly.'],
  teach=teach(goal='Realizar algo com o inglês: manter a relação mesmo ao dizer não.', group=['Cada grupo recebe papéis e restrição; alterne quem convida.', 'Progressão: com chunks, só palavras-chave, sem roteiro.', 'Anote 2–3 correções prioritárias.'], answers=['Modelo: “Would you like to come to dinner on Saturday?” → “I’d love to, but I have to work. Thanks for asking.” → “No worries! How about Sunday?”'], extra=['What if you do not want to go at all?'], support=['Dê o início de frase em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short text message to a friend declining an invitation to a party and proposing another plan.',
  steps=['Thank', 'Decline + reason', 'Suggest another plan', 'Close'],
  model='Hi Diego! Thanks for asking — I’d love to come to your party, but I have to work late on Friday. Would you like to have coffee on Saturday instead? Let me know!',
  checklist=['I thanked my friend.', 'I declined kindly (I’d love to, but…).', 'I gave one short reason.', 'I suggested another plan (How about… / Would you like to…?).'],
  tip='Fix only 2–3 priority points and show a more natural way to say the same idea.', fix=dict(n=3),
  teach=teach(goal='Produção escrita curta ligada à situação.', solo=['Corrija 2–3 pontos prioritários e mostre uma forma mais natural.'], group=['Troquem os textos entre colegas e corrijam em duplas.'], extra=['Write a second message accepting the new plan.'], errors=[E('I can’t go in your party.', 'I can’t go to your party.'), E('Thank you to invite.', 'Thank you for inviting me.')], support=['Dê o modelo e peça só para trocar os dados.'])),
 fb_page('Example: You thanked your friend and gave a clear, short reason.', 'Example: Link “would you” (wouldja) and keep a friendly tone.', 'Example: Decline an invitation from your boss without notes.', 'recusa educada e alternativa.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❓', name='Invite someone', prompt='Without notes: invite a friend to see a movie on Friday.', model='Would you like to see a movie on Friday?'), dict(ic='💬', name='Decline kindly', prompt='A friend invites you, but you have to study. Reply.', model='I’d love to, but I have to study. Thanks for asking!'), dict(ic='⭐', name='Suggest another plan', prompt='Suggest another day after saying no.', model='How about Sunday?')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 45–60 second audio: invite someone and decline an invitation.', 'Write a short message declining a party invitation.', 'Review the four expressions ★ and create your own examples.', 'Listen to the dialogue again and find two ways to accept.']),
  spaced=dict(next=['Would you like to…?', 'I’d love to, but…', 'Maybe next time.'], week=['Thanks for asking.', 'How about…?', 'No worries!'], unit=['Invite · decline · suggest another plan']),
  teach=teach(goal='Toda aula termina com uma produção observável.', solo=['Sem anotações: convidar, recusar e sugerir outro plano.'], group=['Exit challenge individual; compare com o colega.'], answers=['Would you like to see a movie on Friday? · I’d love to, but I have to study. · How about Sunday?'], extra=['Revisão espaçada: aula seguinte, uma semana depois e na missão da unidade.'])),
 lv_page([('Come party? No, sorry.', 'Say yes or no in very short phrases.'), ('Would you like to come? — I’d love to, but I have to work.', 'Invite and decline with a reason.'), ('I’m afraid I can’t make it, but I’d really like to see you another time.', 'Decline and keep the relationship.'), ('I’d have loved to come, but I’ve already committed to something that night. Could we reschedule?', 'Decline with nuance and propose a plan.'), ('I do appreciate the invitation, and I’m genuinely sorry to miss it; perhaps we can make up for it soon.', 'Handle sensitive refusals diplomatically.'), ('I’m touched you thought of me, and it pains me to pass; do let me make it up to you.', 'Show subtle social awareness.')])
]
LESSON = mk(87, 1, 'Invitations: accept and decline', 'Convites: aceitar e recusar', ['Rosa', 'Diego'], 'livingroom', 'dusk', PAGES, DIALOG)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
