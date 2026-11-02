#!/usr/bin/env python3
"""Aula 96 · Workplace requests (A2, 60 min). Gera data/v3/096.json."""
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
 speakers={'Manager': {'name': 'Pia'}, 'Analyst': {'name': 'Raj'}},
 lines=[
  dict(who='Manager', en='Hi Raj, **could you** send me the sales report before lunch?', pt='Oi, Raj, você poderia me enviar o relatório de vendas antes do almoço?'),
  dict(who='Analyst', en='Sure. **Would it be possible to** get the final numbers from Dan first? He’s still updating them.', pt='Claro. Seria possível pegar os números finais com o Dan primeiro? Ele ainda está atualizando.'),
  dict(who='Manager', en='Of course. I’ll talk to him. Is Thursday’s meeting still on?', pt='Claro. Eu falo com ele. A reunião de quinta ainda está de pé?'),
  dict(who='Analyst', en='Yes, but **could you** move it to 3:00? I have a client call at 2:00.', pt='Sim, mas você poderia passá-la para as 15h? Tenho uma ligação com cliente às 14h.'),
  dict(who='Manager', en='No problem. **I’ll take care of** the new invitation today.', pt='Sem problema. Eu cuido do novo convite hoje.'),
  dict(who='Analyst', en='Thanks! **Would it be possible to** book the big conference room, too?', pt='Obrigado! Seria possível reservar também a sala de reuniões grande?'),
  dict(who='Manager', en='Let me check. **I’ll take care of** that and email you the room number.', pt='Deixe-me ver. Eu cuido disso e envio o número da sala por e-mail.'),
  dict(who='Analyst', en='Great. I really appreciate your help, Pia.', pt='Ótimo. Agradeço muito a sua ajuda, Pia.')])

PAGES = [
 dict(t='rl_open', stage='warm', title='Workplace Requests', pt='Pedidos no trabalho', level='A2',
  unit=dict(unit(2), map=UMAP),
  situation=dict(text='You work in an office in the United States. You need a colleague to do something by a certain time, a meeting has to change, and you must ask politely and offer to help in return.', scene='office', tod='day', cast=['Raj', 'Pia']),
  goal='By the end of the class you can ask a colleague for help politely, give a clear deadline or reason, answer a request and promise to do your part.',
  canDo=['Ask politely: Could you…?', 'Ask for something harder: Would it be possible to…?', 'Promise action: I’ll take care of…', 'Give a time and a reason so the request is clear'],
  success=['I make a polite request.', 'I give a time or a reason.', 'I answer a request clearly.', 'I thank the person.'],
  think='How do you ask a coworker for a favor in Portuguese? Do you explain why, or just say what you need?',
  teach=T('Abrir a aula pela situação real: pedir ajuda no trabalho de forma clara e educada.',
   solo=['Leia o objetivo em voz alta e peça que o estudante diga com as próprias palavras o que vai fazer hoje.', 'Pergunte “Think about it” antes de mostrar qualquer expressão.'],
   group=['Cada estudante diz um pedido comum no escritório (send a file, move a meeting…).', 'Mostre os 4 critérios de sucesso: é a missão final da aula.'],
   extra=['What kind of favors do coworkers ask each other?', 'Do you prefer to ask by email or in person?'],
   support=['Aceite respostas curtas ou em português na primeira rodada e reformule em inglês.'])),
 warm('Review: planning with Let’s… / What about…? Ask: What would you suggest for a team lunch?',
  [('What does a normal workday look like for you?', 'Como é um dia normal de trabalho ou estudo para você?', ['I start at 9.', 'I have meetings.', 'I study in the morning.']),
   ('Who do you ask for help when you have a problem?', 'A quem você pede ajuda quando tem um problema?', ['My teacher.', 'A coworker.', 'My manager.']),
   ('Did anyone help you with something this week?', 'Alguém ajudou você com algo esta semana?', ['Yes, my friend…', 'Not really.', 'A colleague helped me with…'])],
  'Entrar no idioma e ativar vocabulário de trabalho e passado simples.', ['What was your busiest day last week?', 'Is it easy for you to ask for help?'],
  [('She help me yesterday.', 'She helped me yesterday.'), ('I have meeting at nine.', 'I have a meeting at nine.')], ['Ofereça as respostas-modelo (chips) e peça apenas que escolham uma.']),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Polite requests',
  intro='In many U.S. offices, requests are polite, indirect and clear about time. Look and guess before you read.',
  cards=[dict(vis='prop:computer', en='Indirect requests', pt='Pedidos indiretos', note='“Could you send me the file?” sounds more polite than “Send me the file.”'),
         dict(vis='prop:clock', en='Say the deadline', pt='Dizer o prazo', note='“By noon” or “before lunch” tells people exactly what you need.'),
         dict(vis='prop:envelope', en='Thank people', pt='Agradecer', note='A quick “Thanks, I appreciate it” by message or email is expected.')],
  qs=[dict(q='How do people usually make requests at work?', pt='Como as pessoas costumam fazer pedidos no trabalho?', levels=dict(A1='Could you help me, please?', A2='They say “Could you…?” and add please.', B1='They use polite questions like “Could you…?” instead of commands, and often explain why.', B2='Requests are softened with modal verbs and framed around a reason or deadline, so they sound collaborative rather than demanding.')),
      dict(q='Why is it useful to say a time or a reason?', pt='Por que é útil dizer um horário ou um motivo?', levels=dict(A1='Time: 3 p.m.', A2='The other person knows what you need and when.', B1='A deadline and a reason avoid misunderstandings and help people plan their day.', B2='A clear time frame and rationale make the request easy to prioritize and harder to misread.')),
      dict(q='How can you say you can’t help right now?', pt='Como dizer que não pode ajudar agora?', levels=dict(A1='Sorry, I can’t.', A2='Sorry, I can’t today. Maybe tomorrow?', B1='“I’m afraid I can’t do it today, but I can send it tomorrow morning.”', B2='Decline softly, give a reason and offer an alternative so the person still feels supported.'))],
  compare='In Brazil, colleagues often ask in a friendly, direct way: “me manda aquele arquivo?”. In many U.S. offices a clear time and a polite modal like “could” are common. What is normal in your workplace?',
  teach=T('Ativar o contexto cultural: pedido educado, prazo claro e agradecimento.',
   solo=['Mostre os 3 cartões e peça hipóteses antes de explicar.', 'Peça que o estudante compare com o tom dos pedidos no trabalho dele.'], group=['Cada estudante escolhe um cartão e explica em uma frase.', 'Pergunte “Do you agree?” entre colegas.'],
   answers=['Q1: Could you… + please, com motivo.', 'Q2: a pessoa sabe o que e quando.', 'Q3: Sorry, I can’t today, but… (recusa + alternativa).'], extra=['Is it rude to refuse a request at work?', 'How do you thank a coworker?'],
   support=['Use as respostas do nível A1 como andaime e peça que repitam.'], stretch=['B2: explique como recusar um pedido do chefe sem parecer pouco colaborativo.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='office', tod='day', cast=['Raj', 'Pia']),
  pass1=dict(q='What are the two people doing?', pt='O que as duas pessoas estão fazendo?', opts=['Asking each other for help at work', 'Planning a vacation', 'Interviewing for a job'], ans=0),
  pass2=dict(tasks=[dict(label='What Pia needs', ans='sales report'), dict(label='Who has the final numbers', ans='Dan'), dict(label='New meeting time', ans='3:00'), dict(label='What Pia will book', ans='conference room', alt=['room'])]),
  teach=T('Compreender a situação antes de ver o texto: ideia principal e depois 4 informações.',
   solo=['Esconda o texto. 1ª escuta: só a ideia principal.', '2ª escuta: o que é pedido, quem tem os números, horário novo e sala.', 'Mostre o texto só depois da 2ª escuta.'], group=['Escuta coletiva; duplas anotam as respostas antes de revelar.', 'Compare as respostas entre as duplas e só então mostre o texto.'],
   answers=['Pass 1: asking each other for help at work.', 'Pass 2: sales report · Dan · 3:00 · conference room.'], extra=['Who asks for more favors, Pia or Raj?', 'Is the tone friendly? How do you know?'],
   support=['Use o botão “Slow” na 2ª escuta.', 'Pause depois de cada fala se necessário.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='What does Pia want before lunch?', opts=['The sales report', 'A new invitation', 'Dan’s phone number'], ans=0), dict(q='Why does Raj ask her to move the meeting?', opts=['He has a client call at 2:00', 'He is on vacation', 'The room is closed'], ans=0), dict(q='What will Pia do about the meeting?', opts=['Send a new invitation', 'Cancel it', 'Ask Dan to run it'], ans=0), dict(q='What will Pia send to Raj later?', opts=['The room number', 'The final report', 'A lunch menu'], ans=0)],
  retell=dict(prompt='Retell the conversation in your own words, at your level.', starters=['Pia asks Raj to…', 'Raj needs…', 'Pia says she will…', 'At the end, Raj…']),
  teach=T('Ler o diálogo, perceber os chunks e recontar.',
   solo=['O estudante lê o papel do Raj; você lê o da Pia.', 'Peça que reconte a conversa no nível que conseguir.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia: uma frase por estudante.'],
   answers=['The sales report · client call at 2:00 · send a new invitation · the room number'], extra=['What would you say if you couldn’t send the report before lunch?', 'Who helps more in this conversation?'],
   errors=[('Can you to send me the file?', 'Could you send me the file?'), ('I take care of this.', 'I’ll take care of this.')], support=['Mostre a tradução (botão PT) depois da 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[dict(en='Could you…?', pt='Você poderia…?', use='Ask someone to do something, politely.', reg='polite', alt='Casual: **Can you…?**', pri=True),
         dict(en='Would it be possible to…?', pt='Seria possível…?', use='Ask for something bigger or less certain.', reg='formal', alt='Also: **Is it possible to…?**', pri=True),
         dict(en='I’ll take care of…', pt='Eu cuido de…', use='Promise to handle a task.', reg='neutral', alt='Also: **I’ll handle…**', pri=True),
         dict(en='By + time', pt='Até + horário', use='Give a deadline: by noon, by Friday.', reg='neutral', pri=True),
         dict(en='I’m afraid I can’t…', pt='Receio que não posso…', use='Say no politely.', reg='polite'),
         dict(en='I really appreciate it.', pt='Agradeço muito.', use='Thank someone for help.', reg='polite'),
         dict(en='No problem.', pt='Sem problema.', use='Accept a request in a friendly way.', reg='informal'),
         dict(en='Let me check.', pt='Deixe-me verificar.', use='Gain time before answering.', reg='neutral')],
  discover=dict(fns=['Asking politely', 'Asking for something harder', 'Promising action', 'Giving a deadline', 'Saying no politely'],
   items=[dict(en='Could you send me the report?', fn='Asking politely'), dict(en='Would it be possible to move the meeting?', fn='Asking for something harder'), dict(en='I’ll take care of the invitation.', fn='Promising action'), dict(en='I need it by noon.', fn='Giving a deadline'), dict(en='I’m afraid I can’t do it today.', fn='Saying no politely')]),
  note='Choose the four ★ expressions to use again and again. The others help you understand and stretch.',
  teach=T('Escolher 4 chunks para uso repetido e descobrir a função de cada um.',
   solo=['Pergunte “When do you say it?” antes de dar o significado.', 'Compare Could you…? × Would it be possible to…? (mais formal) e peça um exemplo próprio.'], group=['Cada estudante escolhe a expressão que mais usaria e explica quando.', 'Compare equivalentes formais e informais em duplas.'],
   answers=['Asking politely · Asking for something harder · Promising action · Giving a deadline · Saying no politely'], extra=['Which one is better for your boss? For a close friend?'], errors=[('Could you to help me?', 'Could you help me?')], support=['Trabalhe só 3 das expressões ★ na primeira rodada.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Polite requests', formula='**Could you** + base verb (+ by + time)?', ex=['Could you send me the report?', 'Could you call the client by noon?', 'Could you move the meeting to 3:00?'], main=True),
            dict(name='Bigger or formal requests', formula='**Would it be possible to** + base verb?', ex=['Would it be possible to get the numbers today?', 'Would it be possible to book the big room?'], main=True),
            dict(name='Promising action', formula='**I’ll take care of** + noun / -ing', ex=['I’ll take care of the invitation.', 'I’ll take care of booking the room.', 'I’ll take care of it today.']),
            dict(name='Saying no politely', formula='**I’m afraid I can’t** + verb, **but** + offer', ex=['I’m afraid I can’t today, but I can tomorrow.', 'I’m afraid I can’t join, but I’ll send my notes.'])],
  swap=dict(frame='Could you {action} {when}?', tpt='Você poderia {action} {when}?',
   slots=[dict(k='action', label='Action', opts=[dict(en='send me the report', pt='me enviar o relatório'), dict(en='call the client', pt='ligar para o cliente'), dict(en='move the meeting', pt='mudar a reunião'), dict(en='review my slides', pt='revisar meus slides')]),
          dict(k='when', label='When', opts=[dict(en='before lunch', pt='antes do almoço'), dict(en='by Friday', pt='até sexta-feira'), dict(en='this afternoon', pt='esta tarde')])]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['Could you send me that?', 'Could you please send me the document?'], ['Sure, no problem.', 'Certainly, I will do that.'], ['I’ll take care of it.', 'I will handle this and confirm by email.'], ['Thanks, I appreciate it.', 'Thank you for your assistance.']],
   note='These are differences of context and register, not absolute rules: contractions are also common in informal emails.'),
  teach=T('Fixar 2 padrões principais (01 e 02); os outros são expansão. Usar a troca de palavras para variar a fala.',
   solo=['Mostre o padrão DENTRO do diálogo (grife os chunks).', 'Use “Swap the words”: toque em cada peça e peça que o estudante diga a frase completa.', 'Compare spoken × written em 2 exemplos.'], group=['Troca em cadeia: cada estudante muda UMA peça e o próximo repete a frase.', 'Em pares: um escolhe as peças, o outro fala.'],
   answers='Padrão 01/02 são o foco; 03/04 são expansão para quem avançar rápido.', extra=['Make it more formal: Could you… → Would it be possible to…?', 'Change one word and say the new sentence.'],
   errors=[('Could you to send me this?', 'Could you send me this?'), ('Would it be possible send the file?', 'Would it be possible to send the file?'), ('I take care of it.', 'I’ll take care of it.')], support=['Fique só com Could you… + ação + by + horário na primeira rodada.'], stretch=['Combinar pedido + motivo + prazo: Could you review this by five? I have a call at six.'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Intonation', tip='In polite yes/no questions the voice usually goes up at the end: “Could you send it?” ↗. In statements the voice goes down: “I’ll take care of it.” ↘. The goal is to be clear and natural, not to remove your accent.',
  items=[dict(say='Could you send me the report?', linked='Could-ya send me the re-PORT? ↗', ipa='/kʊdʒə/', rhythm='oooOoooO'), dict(say='Would it be possible to move it?', linked='Would-it-be POS-si-ble to MOVE it? ↗', ipa='/wʊdɪt/', rhythm='ooooOoooOo'), dict(say='I’ll take care of it.', linked='I’ll TAKE CARE of it. ↘', ipa='/aɪl/', rhythm='oOOoo')],
  identify=[dict(q='Which one do you hear?', opts=['Could you call him? (a request)', 'You could call him. (a suggestion)', 'Could he call you?'], ans=0, say='Could you call him?'), dict(q='Which one do you hear?', opts=['I’ll take care of it.', 'I’ll take care of it?', 'I’d take care of it.'], ans=0, say='I’ll take care of it.')],
  own=dict(prompt='Write one polite request you could make at work or school, and one promise with “I’ll take care of…”.', criteria='Say them twice: the request with rising intonation, the promise with falling intonation. Could your partner hear the difference?'),
  teach=T('UM só fenômeno: entonação (sobe nas perguntas de pedido, desce nas afirmações).',
   solo=['3 passagens: escutar e identificar → reproduzir ritmo e entonação → usar em frase com conteúdo próprio.', 'Desenhe a curva com a mão enquanto modela.'], group=['Coro, depois duplas; circule ouvindo.', 'Cada estudante cria uma frase própria com a entonação certa.'],
   answers=['Identify 1: Could you call him? · Identify 2: I’ll take care of it. (descendente)'], errors=[('Entonação sempre descendente nos pedidos.', 'Subir no fim de Could you…?'), ('Could you com “l” pronunciado.', '“l” mudo em could: /kʊd/')], support=['Reduza a velocidade e use gestos para mostrar a curva.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    mcq('1. You need a coworker to send a file before noon.', ['Could you send me the file by noon?', 'Send me file noon.', 'You must file noon.'], 0, 'Could you + verb + by + time is polite and clear.'),
    mcq('2. You need something difficult, and you are not sure it is possible.', ['Would it be possible to get it today?', 'I get it today?', 'Is possible today get?'], 0, 'Would it be possible to + verb? is softer.'),
    mcq('3. A coworker asks you to book a room. You will do it.', ['I’ll take care of it.', 'I am taking care of room.', 'I care it.'], 0, 'I’ll take care of it is a clear promise.'),
    mcq('4. You can’t join a meeting, but you can send notes.', ['I’m afraid I can’t join, but I’ll send my notes.', 'I no can, notes.', 'I can’t. Bye.'], 0, 'Decline softly and offer an alternative.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    gap('Could you ___ the meeting to 3:00?', 'move', 'Could you + base verb.', ['move', 'moving', 'to move']),
    gap('Would it be possible ___ book the big room?', 'to', 'Would it be possible + to + verb.', ['to', 'for', 'of']),
    swp('Make it more polite and formal:', 'Send me the report.', ['Could you send me the report?', 'Could you send me the report, please?', 'Would it be possible to send me the report?'], 'Could you send me the report, please?', 'Could you… turns a command into a polite request.'),
    swp('Promise to do it:', 'the invitation', ['I’ll take care of the invitation.', 'I’ll take care of the invitation today.'], 'I’ll take care of the invitation.', 'I’ll take care of + noun.'),
    rep('Could you send me the slides by five?', 'Choose the best reply.', ['Sure, no problem. I’ll send them by five.', 'Yes, I send by five?', 'The slides are five.'], 0, 'Accept clearly and repeat the deadline.')])],
  teach=T('Do controlado ao guiado: completar, substituir e transformar antes da fala livre.',
   solo=['Peça que o estudante justifique cada resposta.', 'Se acertar rápido, peça a versão mais informal ou mais educada.'], group=['Resolvam em duplas e comparem antes de revelar.', 'Equipes: ponto por resposta justificada.'],
   answers=['1: Could you send the file by noon? · 2: Would it be possible to…? · 3: I’ll take care of it. · 4: I’m afraid I can’t join, but…', 'Gap: move · to · Could you send me the report, please? · I’ll take care of the invitation. · Sure, no problem.'], extra=['Say each correct answer aloud with the right intonation.'],
   errors=[('Could you to send…?', 'Could you send…?'), ('Would it be possible send…?', 'Would it be possible to send…?')], support=['Ofereça o banco de palavras (chips) nas lacunas.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — ask like a colleague',
  brief=dict(teacher='You are the coworker (change the situation during the scene!).', student='You need help: ask a coworker for something, give a time, and promise something in return.'),
  orders=['Ask for a report before lunch', 'Ask to move a meeting to a later time', 'Ask someone to book a room for a presentation'],
  complications=['Your coworker says they are too busy today.', 'The deadline is too early for them.', 'They ask why you need it.', 'They offer a different solution.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['Could you…?', 'Would it be possible to…?', 'I’ll take care of…', 'by + time']), dict(label='Keywords', desc='Only the keywords', help=['report', 'before lunch', 'meeting', 'room', 'thanks'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I make a polite request.', 'I give a time or a reason.', 'I answer clearly.', 'I thank the person.'],
  teach=T('Simulação com complicação inesperada e três rodadas com menos apoio.',
   solo=['Combine o cenário com o trabalho ou estudo do aluno.', 'Rodada 1: com chunks. Rodada 2: só palavras-chave. Rodada 3: sem roteiro.', 'Meta de fala: 60–70% do tempo para o estudante. Anote 2–3 correções para a devolutiva.'],
   extra=['What if your coworker says no? What do you say?'], errors=[('You must do this today.', 'Could you do this today, if possible?')], support=['Volte à rodada 1 se travar; peça que repita só a primeira frase.'], stretch=['Peça um favor a alguém mais sênior e depois um favor a um colega próximo.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Simple requests', min=3, task='Ask your partner to do a small task. Your partner accepts.', hint='Could you…? / Sure, no problem.'), dict(title='Add time and reason', min=3, task='Make a request with a deadline and a reason.', hint='Could you… by…? I need it because…'), dict(title='Refuse and offer', min=3, task='Your partner can’t help now. Offer an alternative.', hint='I’m afraid I can’t… but I can…'), dict(title='Share solutions', min=2, whole=True, task='Whole group: each pair shares the best polite request.', hint='We asked… and decided…')],
  infogap=dict(title='Team schedule', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='You know the tasks', task='You know who does the report and the slides. Ask about the rest.', rows=[dict(k='Sales report', v='Raj, by noon'), dict(k='Slides', v='Pia, Thursday'), dict(k='Client call', v=''), dict(k='Room booking', v='')]),
   b=dict(title='You know the times', task='You know the client call and the room. Ask about the rest.', rows=[dict(k='Sales report', v=''), dict(k='Slides', v=''), dict(k='Client call', v='Tom, 2:00 p.m.'), dict(k='Room booking', v='Room 4B, 3:00 p.m.')])),
  teach=T('Fluência por repetição da função com informações novas a cada rodada.',
   group=['Troque os pares a cada rodada (A+B / C+D → A+C / B+D → A+D / B+C → grupo todo). Com 6 estudantes, três duplas simultâneas.', 'Sem salas simultâneas: interações sequenciais enquanto uma dupla apresenta.', 'Responsabilidade individual: cada aluno faz ≥1 pedido e ≥1 resposta.'],
   answers=['Info gap: A tem relatório (Raj, meio-dia) e slides (Pia, quinta); B tem ligação (Tom, 14h) e sala (4B, 15h). Cada um completa perguntando.'], extra=['Who is doing the sales report?', 'What time is the client call?'],
   errors=[('Who make the report?', 'Who is making the report? / Who’s doing the report?'), ('At 2 pm of the afternoon.', 'At 2:00 p.m.')], support=['Entregue frases-modelo no chat da turma.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — handle a busy day',
  goal='Each group must handle a workplace problem in English: ask, explain, promise action and close politely.',
  missions=[dict(who='A', role='Coworkers', mission='The presentation is tomorrow. You need slides from a colleague who is busy. Get a solution you both accept.', constraint='Use “Could you…?” with a deadline and “I’ll take care of…”.', start='Hi! Could you…'),
            dict(who='B', role='Manager and employee', mission='The employee needs to move a meeting. The manager has a conflict. Agree on a new time.', constraint='Use “Would it be possible to…?” and “I’m afraid I can’t…”.', start='Hi! Would it be possible to…'),
            dict(who='C', role='Teammates', mission='Share three tasks for a new project. Each person promises something and asks for something.', constraint='Each person says “I’ll take care of…” once and finishes with “I appreciate it.”', start='Okay, so for this project…')], min=11,
  success=['Make a polite request.', 'Give a time or reason.', 'Promise action.', 'Close politely.'],
  teach=T('Realizar algo com o inglês: o objetivo é resolver, não só falar certo.',
   group=['Cada grupo recebe papéis, restrição e missão. Alterne pedidos e respostas.', 'Progressão: 1ª rodada com frases de apoio, 2ª só palavras-chave, 3ª sem roteiro.', 'Observe e anote 2–3 correções prioritárias; devolutiva no fim.'],
   answers=['Modelo: “Could you send me the slides by three?” → “I’m afraid I can’t, I have a call. But I can send them by five.” → “That works. I’ll take care of the first part.”'], extra=['What if the other person is rude?'], support=['Dê o início de frase (“Start with”) em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short work email asking a colleague for something. Give a deadline, a reason and offer to help.',
  steps=['Greeting', 'Request with deadline', 'Reason', 'Offer and thanks'],
  model='Hi Pia, **could you** send me the client list by Thursday at noon? I need it for the meeting on Friday. **I’ll take care of** the agenda and the room. Thanks so much for your help! Best, Raj',
  checklist=['I greeted the person.', 'I used Could you… or Would it be possible to…?', 'I gave a deadline and a reason.', 'I offered something and thanked them.'],
  tip='Fix only 2–3 priority points. Show a more natural way to say the same idea instead of rewriting everything.', fix=dict(n=3),
  teach=T('Produção escrita curta ligada à situação comunicativa.',
   solo=['Peça o e-mail; corrija 2–3 pontos prioritários e mostre uma forma mais natural.'], group=['Cada estudante escreve; depois troquem os textos entre colegas e corrijam em duplas.'],
   extra=['Write a second email to say you can’t do a request.'], errors=[('Please you send me.', 'Could you send me…, please?'), ('Thanks you.', 'Thank you.')], support=['Dê o modelo e peça só para trocar os dados.'])),
 feedback('Example: You asked politely and gave a clear deadline.', 'Example: Raise your voice at the end of a request: Could you…? ↗', 'Example: Refuse a request politely and offer an alternative, without notes.', 'Observe se o pedido soou educado e claro (prazo, motivo).'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❓', name='Make a request', prompt='Without notes: ask a coworker to send a file by noon.', model='Could you send me the file by noon?'), dict(ic='💬', name='Promise action', prompt='A coworker asks you to book a room. You agree.', model='Sure, I’ll take care of it.'), dict(ic='⭐', name='Say no politely', prompt='You can’t help today, but you can tomorrow.', model='I’m afraid I can’t today, but I can tomorrow.')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 45–60 second audio asking a coworker for help.', 'Write a short email with a request, a deadline and a thank you.', 'Review the four ★ expressions and write two examples for each.', 'Listen to the dialogue again and find two ways the speakers say thank you.']),
  spaced=dict(next=['Could you…?', 'Would it be possible to…?', 'I’ll take care of…'], week=['I’m afraid I can’t…', 'by + time', 'I really appreciate it.'], unit=['Ask · promise · refuse · thank']),
  teach=T('Toda aula termina com uma produção observável.', solo=['Sem consultar as anotações: fazer um pedido, prometer uma ação e recusar com educação.'], group=['Exit challenge individual; compare com o colega e combine a tarefa de continuidade.'],
   answers=['Could you send me the file by noon? · Sure, I’ll take care of it. · I’m afraid I can’t today, but I can tomorrow.'], extra=['Revisão espaçada: retomar na próxima aula, depois de uma semana e na missão de encerramento da unidade.'])),
 levels([('Please, report. Noon.', None), ('Could you send me the report before lunch? I need it for a meeting.', 'Ask politely with a time and a reason.'), ('Would it be possible to get the report by noon? I’ll take care of the slides in the meantime.', None), ('I was wondering whether you could possibly send the report by noon, since the client meeting has been moved up.', None), ('I’d be grateful if you could prioritize the report this morning; I’m happy to take on the slides to free up your time.', None), ('If it isn’t too much trouble, might I ask you to send the report by noon? I’ll gladly return the favor.', None)], 'Mostrar a progressão sem criar seis metodologias.')
]

LESSON = dict(n=96, topic='Workplace requests', level='A2', title='Workplace Requests', pt='Pedidos no trabalho', unit=unit(2), minutes=60, cast=['Raj', 'Pia'], scene='office', tod='day', plan=PLAN, dialog=DIALOG, pages=PAGES)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
