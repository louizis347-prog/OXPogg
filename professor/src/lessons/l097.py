#!/usr/bin/env python3
"""Aula 97 · Online shopping and delivery (A2, 60 min). Gera data/v3/097.json."""
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
 speakers={'Agent': {'name': 'Elif'}, 'Customer': {'name': 'Zara'}},
 lines=[
  dict(who='Agent', en='Customer service, this is Elif. **How can I help** you today?', pt='Atendimento ao cliente, aqui é a Elif. Como posso ajudar hoje?'),
  dict(who='Customer', en='Hi. **My order hasn’t arrived** yet. It was supposed to come on Monday.', pt='Oi. Meu pedido ainda não chegou. Ele deveria ter vindo na segunda.'),
  dict(who='Agent', en='I’m sorry about that. Can you give me your order number?', pt='Sinto muito por isso. Você pode me dar o número do pedido?'),
  dict(who='Customer', en='It’s 48213. **Can I track** the package online?', pt='É 48213. Posso rastrear o pacote on-line?'),
  dict(who='Agent', en='Yes, I’ll send you a tracking link. It looks like it’s stuck at a local post office.', pt='Sim, vou enviar um link de rastreamento. Parece que ficou parado em uma agência local.'),
  dict(who='Customer', en='Oh no. **I’d like to change** the delivery address to my office, if possible.', pt='Ah, não. Eu gostaria de mudar o endereço de entrega para o meu escritório, se possível.'),
  dict(who='Agent', en='I can do that. **It should arrive** tomorrow before five.', pt='Posso fazer isso. Deve chegar amanhã antes das cinco.'),
  dict(who='Customer', en='Great. Thanks for your help. I’ll watch the link.', pt='Ótimo. Obrigada pela ajuda. Vou acompanhar o link.')])

PAGES = [
 dict(t='rl_open', stage='warm', title='Online Shopping and Delivery', pt='Compras online e entregas', level='A2',
  unit=dict(unit(3), map=UMAP),
  situation=dict(text='You bought something online but it has not arrived. You call customer service, give your order number, track the package and change the delivery address.', scene='bedroom', tod='day', cast=['Zara', 'Elif']),
  goal='By the end of the class you can explain a delivery problem, ask to track a package, ask for a change and check what happens next.',
  canDo=['Report a problem: My order hasn’t arrived.', 'Ask about tracking: Can I track…?', 'Ask for a change: I’d like to change…', 'Understand when a package should arrive'],
  success=['I explain the problem.', 'I give the information they ask for.', 'I ask for a solution.', 'I confirm what happens next.'],
  think='Have you ever waited for a package that was late? What did you do or say?',
  teach=T('Abrir a aula pela situação real: um pedido atrasado e uma ligação para o atendimento.',
   solo=['Leia o objetivo em voz alta e peça que o estudante diga com as próprias palavras o que vai fazer hoje.', 'Pergunte “Think about it” antes de mostrar qualquer expressão.'],
   group=['Cada estudante diz algo que comprou online.', 'Mostre os 4 critérios de sucesso: é a missão final da aula.'],
   extra=['What do you buy online most often?', 'Do you read reviews before you buy?'],
   support=['Aceite respostas curtas ou em português na primeira rodada e reformule em inglês.'])),
 warm('Review: polite requests with Could you…? Ask: Could you tell me what you bought last month?',
  [('What was the last thing you bought online?', 'Qual foi a última coisa que você comprou online?', ['A pair of shoes.', 'Some books.', 'I bought a phone case.']),
   ('Did it arrive on time?', 'Chegou no prazo?', ['Yes, it did.', 'No, it was late.', 'It came early.']),
   ('Do you prefer shopping online or in a store?', 'Você prefere comprar online ou em loja?', ['Online, it’s easier.', 'In a store.', 'It depends.'])],
  'Entrar no idioma e ativar passado simples (bought, arrived) e preferências.', ['What is the longest you ever waited for a package?', 'Do you check the tracking often?'],
  [('I buyed a jacket.', 'I bought a jacket.'), ('It arrive late.', 'It arrived late.')], ['Ofereça as respostas-modelo (chips) e peça apenas que escolham uma.']),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Delivery culture',
  intro='Online shopping is part of everyday life in the United States. Look and guess before you read.',
  cards=[dict(vis='prop:mailbox', en='Packages at the door', pt='Pacotes na porta', note='Many packages are left at the front door or in a mailroom when nobody is home.'),
         dict(vis='prop:telephone', en='Tracking and updates', pt='Rastreamento e avisos', note='Stores send a tracking number or link, and you can follow the package by phone.'),
         dict(vis='prop:bag', en='Returns', pt='Devoluções', note='Many stores accept returns for a limited time. Always check the return policy.')],
  qs=[dict(q='What do people use to follow a package?', pt='O que as pessoas usam para acompanhar um pacote?', levels=dict(A1='A tracking number.', A2='They use a tracking number or link and check it online.', B1='Most stores send a tracking link by email or text, so people can see where the package is.', B2='Tracking numbers and notifications let customers follow each step and plan to be home if needed.')),
      dict(q='What can you do if your order is late?', pt='O que fazer se o pedido atrasar?', levels=dict(A1='Call the store.', A2='You can check the tracking, then contact customer service.', B1='Check the tracking first, then contact customer service with your order number.', B2='Verify the status, gather the order number and delivery estimate, and ask the store for a solution.')),
      dict(q='Why do customer service agents ask for an order number?', pt='Por que o atendimento pede o número do pedido?', levels=dict(A1='To find the order.', A2='They need it to find your order quickly.', B1='The number identifies your purchase, so they can see the details and the delivery status.', B2='It links your request to the right order, which speeds up verification and any change or refund.'))],
  compare='In Brazil, deliveries often require someone to receive the package at home. In the U.S., packages are often left at the door, so people check the tracking to know when they will arrive. How are deliveries where you live?',
  teach=T('Ativar o contexto cultural: rastreamento, entrega na porta e atendimento ao cliente.',
   solo=['Mostre os 3 cartões e peça hipóteses antes de explicar.', 'Peça que o estudante compare com o que acontece no Brasil quando ninguém está em casa.'], group=['Cada estudante escolhe um cartão e explica em uma frase.', 'Pergunte “Do you agree?” entre colegas.'],
   answers=['Q1: tracking number/link.', 'Q2: ver o rastreamento e depois falar com o atendimento.', 'Q3: para achar o pedido rapidamente.'], extra=['Have you ever had a package stolen or lost?', 'Do you read the return policy?'],
   support=['Use as respostas do nível A1 como andaime e peça que repitam.'], stretch=['B2: explique como pedir reembolso de um pedido que nunca chegou.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='bedroom', tod='day', cast=['Zara', 'Elif']),
  pass1=dict(q='Why is the customer calling?', pt='Por que a cliente está ligando?', opts=['Her order hasn’t arrived', 'She wants a refund for a broken item', 'She wants to buy a new phone'], ans=0),
  pass2=dict(tasks=[dict(label='Order number', ans='48213'), dict(label='Expected day', ans='Monday'), dict(label='Where is the package now?', ans='post office'), dict(label='New delivery address', ans='office'), dict(label='When it will arrive', ans='tomorrow')]),
  teach=T('Compreender a situação antes de ver o texto: ideia principal e depois 5 informações.',
   solo=['Esconda o texto. 1ª escuta: só a ideia principal.', '2ª escuta: número do pedido, dia esperado, onde está o pacote, endereço novo e quando chega.', 'Mostre o texto só depois da 2ª escuta.'], group=['Escuta coletiva; duplas anotam as respostas antes de revelar.', 'Compare as respostas entre as duplas e só então mostre o texto.'],
   answers=['Pass 1: her order hasn’t arrived.', 'Pass 2: 48213 · Monday · post office · office · tomorrow.'], extra=['Is Zara upset or calm? How do you know?', 'Does the agent solve the problem?'],
   support=['Use o botão “Slow” na 2ª escuta.', 'Pause depois de cada fala se necessário.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='What was supposed to happen on Monday?', opts=['Zara’s order was supposed to arrive', 'Zara was supposed to call', 'The store was supposed to open'], ans=0), dict(q='What does the agent send Zara?', opts=['A tracking link', 'A refund', 'A new package'], ans=0), dict(q='Where does Zara want the package to go?', opts=['To her office', 'To her neighbor', 'Back to the store'], ans=0), dict(q='When should the package arrive now?', opts=['Tomorrow before five', 'Monday morning', 'Next week'], ans=0)],
  retell=dict(prompt='Retell the conversation in your own words, at your level.', starters=['Zara calls because…', 'The agent asks for…', 'Then Zara asks to…', 'In the end, the package…']),
  teach=T('Ler o diálogo, perceber os chunks e recontar.',
   solo=['O estudante lê o papel da Zara; você lê o da Elif.', 'Peça que reconte a conversa no nível que conseguir.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia: uma frase por estudante.'],
   answers=['Her order was supposed to arrive · a tracking link · her office · tomorrow before five'], extra=['What would you say if the package never came?', 'Why does Zara change the address?'],
   errors=[('My order didn’t arrive yet.', 'My order hasn’t arrived yet.'), ('I want change the address.', 'I’d like to change the address.')], support=['Mostre a tradução (botão PT) depois da 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[dict(en='My order hasn’t arrived.', pt='Meu pedido não chegou.', use='Report a late delivery.', reg='neutral', alt='Also: **My package is late.**', pri=True),
         dict(en='Can I track…?', pt='Posso rastrear…?', use='Ask how to follow a package.', reg='neutral', alt='Also: **Is there a tracking number?**', pri=True),
         dict(en='I’d like to change…', pt='Eu gostaria de mudar…', use='Ask for a change: address, date, size.', reg='polite', alt='Also: **Could I change…?**', pri=True),
         dict(en='It should arrive…', pt='Deve chegar…', use='Say when something is expected.', reg='neutral', pri=True),
         dict(en='Your order number, please.', pt='O número do pedido, por favor.', use='The agent asks for information.', reg='neutral'),
         dict(en='It’s stuck at…', pt='Está parado em…', use='Say where a package is.', reg='neutral'),
         dict(en='I’d like a refund.', pt='Eu gostaria de um reembolso.', use='Ask for your money back.', reg='polite'),
         dict(en='Thanks for your help.', pt='Obrigado pela ajuda.', use='Close the conversation politely.', reg='neutral')],
  discover=dict(fns=['Reporting a problem', 'Asking about tracking', 'Asking for a change', 'Giving an expected time'],
   items=[dict(en='My package hasn’t arrived yet.', fn='Reporting a problem'), dict(en='Can I track my order?', fn='Asking about tracking'), dict(en='I’d like to change the address.', fn='Asking for a change'), dict(en='It should arrive on Friday.', fn='Giving an expected time'), dict(en='It was supposed to come yesterday.', fn='Reporting a problem')]),
  note='Choose the four ★ expressions to use again and again. The others help you understand and stretch.',
  teach=T('Escolher 4 chunks para uso repetido e descobrir a função de cada um.',
   solo=['Pergunte “When do you say it?” antes de dar o significado.', 'Compare My order hasn’t arrived (agora) × It didn’t arrive (passado) e peça um exemplo próprio.'], group=['Cada estudante escolhe a expressão que mais usaria e explica quando.', 'Compare equivalentes em duplas.'],
   answers=['Reporting a problem · Asking about tracking · Asking for a change · Giving an expected time · Reporting a problem'], extra=['Which expression would you use on the phone? In a chat?'], errors=[('My order not arrived.', 'My order hasn’t arrived.')], support=['Trabalhe só 3 das expressões ★ na primeira rodada.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Reporting a problem', formula='**My order hasn’t arrived** (yet).', ex=['My order hasn’t arrived yet.', 'My package hasn’t come.', 'The shoes haven’t arrived.'], main=True),
            dict(name='Asking about tracking', formula='**Can I track** + noun (online)?', ex=['Can I track the package online?', 'Can I track my order?', 'Can I track it by phone?'], main=True),
            dict(name='Asking for a change', formula='**I’d like to change** + noun', ex=['I’d like to change the address.', 'I’d like to change the size.', 'I’d like to change the delivery date.']),
            dict(name='Expected time', formula='**It should arrive** + time', ex=['It should arrive tomorrow.', 'It should arrive before five.'])],
  swap=dict(frame='I’d like to change {thing} {where}.', tpt='Eu gostaria de mudar {thing} {where}.',
   slots=[dict(k='thing', label='Thing', opts=[dict(en='the address', pt='o endereço'), dict(en='the size', pt='o tamanho'), dict(en='the delivery date', pt='a data de entrega'), dict(en='the color', pt='a cor')]),
          dict(k='where', label='Detail', opts=[dict(en='on my order', pt='no meu pedido'), dict(en='before it ships', pt='antes de ser enviado'), dict(en='if possible', pt='se possível')])]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['My order hasn’t arrived yet.', 'I am writing to report that my order has not been delivered.'], ['Can I track it?', 'Is it possible to track the shipment?'], ['I’d like to change the address.', 'I would like to request a change of delivery address.'], ['Thanks for your help.', 'Thank you for your assistance.']],
   note='These are differences of context and register, not absolute rules: contractions are also common in informal emails.'),
  teach=T('Fixar 2 padrões principais (01 e 02); os outros são expansão. Usar a troca de palavras para variar a fala.',
   solo=['Mostre o padrão DENTRO do diálogo (grife os chunks).', 'Use “Swap the words”: toque em cada peça e peça que o estudante diga a frase completa.', 'Compare spoken × written em 2 exemplos.'], group=['Troca em cadeia: cada estudante muda UMA peça e o próximo repete a frase.', 'Em pares: um escolhe as peças, o outro fala.'],
   answers='Padrão 01/02 são o foco; 03/04 são expansão para quem avançar rápido.', extra=['Change the sentence: hasn’t arrived → hasn’t come.', 'Change one word and say the new sentence.'],
   errors=[('My order didn’t arrive yet.', 'My order hasn’t arrived yet.'), ('Can I to track it?', 'Can I track it?'), ('I’d like change.', 'I’d like to change it.')], support=['Fique só com My order hasn’t arrived e Can I track…? na primeira rodada.'], stretch=['Combinar problema + pedido: My order hasn’t arrived, so I’d like to change the address.'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Numbers: -teen vs. -ty', tip='“Fifteen” stresses the end (fif-TEEN). “Fifty” stresses the beginning (FIF-ty). In order numbers and prices, this difference matters. The goal is to be clear, not to remove your accent.',
  items=[dict(say='thirteen, thirty', linked='thir-TEEN, THIR-ty', ipa='/ˌθɜːrˈtiːn/ · /ˈθɜːrti/', rhythm='oOOo'), dict(say='Your order number is 48213.', linked='Your ORder NUMber is FORty-eight, two-THIR-teen.', ipa='/ˈfɔːrti/', rhythm='ooOoooOoOo'), dict(say='It costs fifteen dollars.', linked='It COSTS fif-TEEN DOL-lars.', ipa='/fɪfˈtiːn/', rhythm='oOoOOo')],
  identify=[dict(q='Which one do you hear?', opts=['fifteen', 'fifty', 'five'], ans=0, say='fifteen'), dict(q='Which one do you hear?', opts=['sixty dollars', 'sixteen dollars', 'six dollars'], ans=0, say='sixty dollars')],
  own=dict(prompt='Write your phone number or a price using one -teen and one -ty number.', criteria='Say it twice. Can your partner write exactly what they hear?'),
  teach=T('UM só fenômeno: números -teen × -ty (acento da palavra).',
   solo=['3 passagens: escutar e identificar → reproduzir ritmo → usar com números próprios (CEP, preço, número do pedido).', 'Modele devagar e normal; peça que o estudante bata palmas na sílaba forte.'], group=['Coro, depois duplas; um dita, o outro escreve.', 'Cada estudante dita um número próprio.'],
   answers=['Identify 1: fifteen · Identify 2: sixty dollars'], errors=[('fifteen com acento no início (FIFteen).', 'fifTEEN: acento no fim.'), ('Falar “fifty” e “fifteen” igual.', 'Acentos diferentes: FIFty × fifTEEN.')], support=['Reduza a velocidade e conte as batidas em voz alta.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    mcq('1. Your package is late. You call the store.', ['My order hasn’t arrived yet.', 'My order not come me.', 'I am arrived the order.'], 0, 'hasn’t arrived + yet describes a late delivery now.'),
    mcq('2. You want to follow your package online.', ['Can I track the package online?', 'Can I tracking package?', 'I can’t track I?'], 0, 'Can I + base verb.'),
    mcq('3. You need the package to go to your office.', ['I’d like to change the delivery address.', 'I want change you address.', 'Please, change me.'], 0, 'I’d like to change + noun is polite.'),
    mcq('4. The agent says: “It should arrive tomorrow.” What does it mean?', ['Tomorrow is the expected day.', 'It arrived yesterday.', 'It will never arrive.'], 0, 'should + arrive gives an expectation.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    gap('My order hasn’t ___ yet.', 'arrived', 'hasn’t + past participle.', ['arrived', 'arrive', 'arriving']),
    gap('Can I ___ my package online?', 'track', 'Can I + base verb.', ['track', 'tracking', 'to track']),
    swp('Say you want to change the size:', 'the size', ['I’d like to change the size.', 'I’d like to change the size, please.'], 'I’d like to change the size.', 'I’d like to change + noun.'),
    swp('Make a sentence about a late package:', 'shoes / not arrived', ['My shoes haven’t arrived yet.', 'The shoes haven’t arrived yet.', 'My shoes haven’t arrived.'], 'My shoes haven’t arrived yet.', 'Plural: haven’t arrived.'),
    rep('Can you give me your order number?', 'Choose the best reply.', ['Sure, it’s 48213.', 'Yes, I give you the number is.', 'I order the number.'], 0, 'Answer directly and give the number.')])],
  teach=T('Do controlado ao guiado: completar, substituir e transformar antes da fala livre.',
   solo=['Peça que o estudante justifique cada resposta.', 'Se acertar rápido, peça a versão mais informal ou mais educada.'], group=['Resolvam em duplas e comparem antes de revelar.', 'Equipes: ponto por resposta justificada.'],
   answers=['1: My order hasn’t arrived yet. · 2: Can I track the package online? · 3: I’d like to change the delivery address. · 4: Tomorrow is the expected day.', 'Gap: arrived · track · I’d like to change the size. · My shoes haven’t arrived yet. · Sure, it’s 48213.'], extra=['Say each correct answer aloud with the right stress.'],
   errors=[('My order didn’t arrived.', 'My order didn’t arrive. / My order hasn’t arrived.'), ('Can I to track?', 'Can I track?')], support=['Ofereça o banco de palavras (chips) nas lacunas.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — call customer service',
  brief=dict(teacher='You are the customer service agent (change the plan during the call!).', student='You are the customer: your order is late. Explain the problem and ask for a solution.'),
  orders=['A pair of shoes that hasn’t arrived', 'A phone case delivered to the wrong address', 'A jacket in the wrong size'],
  complications=['The agent can’t find your order number.', 'The package is still at a warehouse.', 'You need the delivery to go to another address.', 'The agent offers a refund, but you prefer the item.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['My order hasn’t arrived.', 'Can I track…?', 'I’d like to change…', 'It should arrive…']), dict(label='Keywords', desc='Only the keywords', help=['order number', 'late', 'tracking', 'address', 'refund'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I explain the problem.', 'I give the information.', 'I ask for a solution.', 'I confirm what happens next.'],
  teach=T('Simulação com complicação inesperada e três rodadas com menos apoio.',
   solo=['Combine o cenário com uma compra real do aluno.', 'Rodada 1: com chunks. Rodada 2: só palavras-chave. Rodada 3: sem roteiro.', 'Meta de fala: 60–70% do tempo para o estudante. Anote 2–3 correções para a devolutiva.'],
   extra=['What if the agent says the package is lost?'], errors=[('The package is not coming.', 'My package hasn’t arrived yet.')], support=['Volte à rodada 1 se travar; peça que repita só a primeira frase.'], stretch=['Peça reembolso ou envio de um novo pacote e pergunte pelo prazo.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Report the problem', min=3, task='Your order is late. Call the agent and explain.', hint='My order hasn’t arrived. / It was supposed to…'), dict(title='Ask for information', min=3, task='Ask about tracking and the arrival time.', hint='Can I track…? / When should it arrive?'), dict(title='Ask for a change', min=3, task='Change the address or the date.', hint='I’d like to change… / Is that possible?'), dict(title='Share solutions', min=2, whole=True, task='Whole group: each pair shares the best solution.', hint='We decided to… because…')],
  infogap=dict(title='Package status', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='Customer has the order', task='You know the item and the order number. Ask about the rest.', rows=[dict(k='Item', v='Blue backpack'), dict(k='Order number', v='73604'), dict(k='Where is it now?', v=''), dict(k='Arrival', v='')]),
   b=dict(title='Agent has the tracking', task='You know where it is and the new date. Ask about the rest.', rows=[dict(k='Item', v=''), dict(k='Order number', v=''), dict(k='Where is it now?', v='At a local post office'), dict(k='Arrival', v='Friday before noon')])),
  teach=T('Fluência por repetição da função com informações novas a cada rodada.',
   group=['Troque os pares a cada rodada (A+B / C+D → A+C / B+D → A+D / B+C → grupo todo). Com 6 estudantes, três duplas simultâneas.', 'Sem salas simultâneas: interações sequenciais enquanto uma dupla apresenta.', 'Responsabilidade individual: cada aluno faz ≥1 pergunta e ≥1 resposta.'],
   answers=['Info gap: A tem mochila azul e pedido 73604; B tem local (agência) e chegada (sexta antes do meio-dia). Cada um completa perguntando.'], extra=['What is the order number?', 'Where is the package now?'],
   errors=[('The package is in the post office now.', 'It’s at a local post office.'), ('What hour arrive?', 'What time should it arrive?')], support=['Entregue frases-modelo no chat da turma.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — solve a delivery problem',
  goal='Each group must solve a delivery problem in English: explain, ask, change something and confirm.',
  missions=[dict(who='A', role='Customer and agent', mission='A package was supposed to arrive three days ago. Find where it is and agree on a new delivery time.', constraint='Use “My order hasn’t arrived” and “Can I track…?”', start='Hello, my order hasn’t arrived…'),
            dict(who='B', role='Customer and agent', mission='You will be away on Friday. Change the delivery address to a neighbor or your office.', constraint='Use “I’d like to change…” and ask for a confirmation.', start='Hi, I’d like to change…'),
            dict(who='C', role='Customer and agent', mission='The wrong size arrived. Ask to change it and ask how long it will take.', constraint='Give the order number and ask “How long will it take?”', start='Hi, I received the wrong size…')], min=11,
  success=['Explain the problem.', 'Give information.', 'Ask for a solution.', 'Confirm what happens next.'],
  teach=T('Realizar algo com o inglês: o objetivo é resolver, não só falar certo.',
   group=['Cada grupo recebe papéis, restrição e missão. Alterne cliente e atendente.', 'Progressão: 1ª rodada com frases de apoio, 2ª só palavras-chave, 3ª sem roteiro.', 'Observe e anote 2–3 correções prioritárias; devolutiva no fim.'],
   answers=['Modelo: “My order hasn’t arrived yet.” → “Can you give me the order number?” → “It’s 73604. Can I track it?” → “It should arrive Friday.”'], extra=['What if the agent can’t help you?'], support=['Dê o início de frase (“Start with”) em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short message to customer service about a late order. Give the order number, explain the problem and ask for a solution.',
  steps=['Greeting', 'Problem and order number', 'Request', 'Thanks'],
  model='Hello, **my order hasn’t arrived** yet. The order number is 73604, and it was supposed to come on Monday. **I’d like to change** the delivery address to my office. **It should arrive** before Friday. Could you confirm that, please? Thank you.',
  checklist=['I greeted the agent.', 'I explained the problem and gave the order number.', 'I asked for a solution politely.', 'I closed with thanks.'],
  tip='Fix only 2–3 priority points. Show a more natural way to say the same idea instead of rewriting everything.', fix=dict(n=3),
  teach=T('Produção escrita curta ligada à situação comunicativa.',
   solo=['Peça a mensagem; corrija 2–3 pontos prioritários e mostre uma forma mais natural.'], group=['Cada estudante escreve; depois troquem os textos entre colegas e corrijam em duplas.'],
   extra=['Add a second request: a refund or a faster delivery.'], errors=[('My order not arrive.', 'My order hasn’t arrived.'), ('Please solve me.', 'Could you help me with this, please?')], support=['Dê o modelo e peça só para trocar os dados.'])),
 feedback('Example: You explained the problem and gave the order number clearly.', 'Example: Say “fifteen” and “fifty” with different stress.', 'Example: Ask for a refund and a new delivery date in the same call, without notes.', 'Observe se o aluno conseguiu dar e entender números e datas.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='❗', name='Report a problem', prompt='Without notes: tell customer service your order is late.', model='My order hasn’t arrived yet.'), dict(ic='💬', name='Ask about tracking', prompt='Ask if you can follow the package online.', model='Can I track the package online?'), dict(ic='⭐', name='Ask for a change', prompt='Ask to change the address to your office.', model='I’d like to change the delivery address to my office.')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 45–60 second audio simulating a call about a late order.', 'Write a short message to customer service with an order number.', 'Review the four ★ expressions and write two examples for each.', 'Listen to the dialogue again and write down the numbers and days you hear.']),
  spaced=dict(next=['My order hasn’t arrived.', 'Can I track…?', 'I’d like to change…'], week=['It should arrive…', 'It’s stuck at…', 'Thanks for your help.'], unit=['Explain · track · change · confirm']),
  teach=T('Toda aula termina com uma produção observável.', solo=['Sem consultar as anotações: relatar um problema, perguntar sobre rastreamento e pedir uma mudança.'], group=['Exit challenge individual; compare com o colega e combine a tarefa de continuidade.'],
   answers=['My order hasn’t arrived yet. · Can I track the package online? · I’d like to change the delivery address to my office.'], extra=['Revisão espaçada: retomar na próxima aula, depois de uma semana e na missão de encerramento da unidade.'])),
 levels([('No package. Help, please.', None), ('My order hasn’t arrived yet. Can I track it?', 'Report a problem and ask for a solution.'), ('My order was supposed to arrive on Monday, but it’s still not here. Could you check what happened?', None), ('I’d appreciate it if you could look into my order, since the tracking hasn’t been updated in three days.', None), ('Given that the package appears to be stuck, I’d like to know whether a replacement or a refund would be quicker.', None), ('I’d rather not wait any longer, so I’d be grateful if you could expedite a replacement or process a refund.', None)], 'Mostrar a progressão sem criar seis metodologias.')
]

LESSON = dict(n=97, topic='Online shopping and delivery', level='A2', title='Online Shopping and Delivery', pt='Compras online e entregas', unit=unit(3), minutes=60, cast=['Zara', 'Elif'], scene='bedroom', tod='day', plan=PLAN, dialog=DIALOG, pages=PAGES)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
