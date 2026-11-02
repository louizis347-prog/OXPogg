#!/usr/bin/env python3
"""Aula 99 · A2 situations review (A2, 60 min). Gera data/v3/099.json."""
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
 speakers={'Friend 1': {'name': 'Tom'}, 'Friend 2': {'name': 'Ana'}},
 lines=[
  dict(who='Friend 1', en='Hey, Ana! **What about** a picnic in the park on Saturday?', pt='Oi, Ana! Que tal um piquenique no parque no sábado?'),
  dict(who='Friend 2', en='Sounds great, but the forecast says rain. **I’d rather** go to the new food market.', pt='Parece ótimo, mas a previsão é de chuva. Eu prefiro ir à nova feira de comidas.'),
  dict(who='Friend 1', en='Good point. **Could you** check the opening hours on your phone?', pt='Boa observação. Você poderia ver o horário de funcionamento no seu celular?'),
  dict(who='Friend 2', en='Sure. It opens at ten. Oh, and **my order hasn’t arrived** yet. I bought a jacket online.', pt='Claro. Abre às dez. Ah, e meu pedido ainda não chegou. Comprei uma jaqueta online.'),
  dict(who='Friend 1', en='Then **let’s** stop by the post office first. **Would it be possible to** pick it up there?', pt='Então vamos passar primeiro no correio. Seria possível retirá-la lá?'),
  dict(who='Friend 2', en='Maybe. I’ll call them, and **I’d like to change** the delivery address if not.', pt='Talvez. Vou ligar para eles e gostaria de mudar o endereço de entrega, se não.'),
  dict(who='Friend 1', en='**To sum up:** post office at nine, market at ten, and Maya joins us after her class.', pt='Resumindo: correio às nove, feira às dez e a Maya se junta a nós depois da aula.'),
  dict(who='Friend 2', en='Perfect. **I’ll take care of** the message for Maya.', pt='Perfeito. Eu cuido da mensagem para a Maya.')])

PAGES = [
 dict(t='rl_open', stage='warm', title='A2 Situations Review', pt='Revisão de situações do A2', level='A2',
  unit=dict(unit(5), map=UMAP),
  situation=dict(text='Two friends meet in a plaza to plan a Saturday. In one short conversation they plan, ask for help, solve a delivery problem and sum up the plan. You review the A2 situations by doing them again, in a new context.', scene='plaza', tod='day', cast=['Ana', 'Tom', 'Maya']),
  goal='By the end of the class you can move between planning, polite requests, problems and summaries in one conversation, using the main A2 expressions without notes.',
  canDo=['Plan together: What about…? / I’d rather…', 'Ask for help: Could you…? / Would it be possible to…?', 'Solve a problem: My order hasn’t arrived. / I’d like to change…', 'Close with a summary: To sum up…'],
  success=['I suggest and decide.', 'I ask politely.', 'I explain and solve a problem.', 'I summarize the plan.'],
  think='Which A2 situation is easiest for you now? Which one still needs practice?',
  teach=T('Abrir a revisão espaçada: o aluno revisita situações do A2 em um contexto novo, sem lista de regras.',
   solo=['Leia o objetivo em voz alta e peça que o estudante diga quais situações do A2 ele já domina e quais quer treinar.', 'Pergunte “Think about it” antes de mostrar qualquer expressão.'],
   group=['Cada estudante escolhe uma situação do A2 (viagem, trabalho, entrega, apresentação) e explica por quê.', 'Mostre os 4 critérios de sucesso: é a missão final da aula.'],
   extra=['What was the most useful A2 lesson for you?', 'Which expression do you use most?'],
   support=['Aceite respostas curtas ou em português na primeira rodada e reformule em inglês.'])),
 warm('Spaced review: planning (What about…?), work requests (Could you…?), deliveries (My order hasn’t arrived) and talks (To sum up…).',
  [('What are you doing this weekend?', 'O que você vai fazer neste fim de semana?', ['I’m going to…', 'Nothing special.', 'I’d like to…']),
   ('Who did you ask for help last week? What did you say?', 'A quem você pediu ajuda na semana passada? O que disse?', ['I asked my…', 'Could you…?', 'Nobody.']),
   ('Tell me about something that went wrong recently.', 'Conte algo que deu errado recentemente.', ['My order…', 'I missed…', 'It was late.'])],
  'Retomar várias situações do A2 e identificar o que precisa de reforço.', ['What was the last problem you solved in English?', 'Which situation is hardest for you?'],
  [('I am agree.', 'I agree.'), ('I go there yesterday.', 'I went there yesterday.')], ['Ofereça as respostas-modelo (chips) e peça apenas que escolham uma.']),
 dict(t='rl_culture', stage='immersion', title='Cultural snapshot — Spaced review of the A2 patterns',
  intro='Real conversations mix functions: you suggest, ask, explain a problem and sum up, often in one minute. Look and guess before you read.',
  cards=[dict(vis='prop:map', en='Suggest and decide', pt='Sugerir e decidir', note='Friends suggest ideas, check the weather and the time, and choose a plan together.'),
         dict(vis='prop:telephone', en='Ask and check', pt='Pedir e verificar', note='A quick “Could you check…?” keeps the plan moving.'),
         dict(vis='prop:umbrella', en='Plan B', pt='Plano B', note='In many places, people check the forecast and have a backup plan for outdoor events.')],
  qs=[dict(q='What do friends do when the weather is bad?', pt='O que amigos fazem quando o tempo está ruim?', levels=dict(A1='They go inside.', A2='They change the plan: “I’d rather go to the market.”', B1='They suggest an indoor plan, like a market or a café, and decide together.', B2='They adapt quickly, proposing an alternative that fits the weather and everyone’s preferences.')),
      dict(q='How do you ask a friend to check something for you?', pt='Como pedir a um amigo para verificar algo?', levels=dict(A1='Can you check?', A2='Could you check the opening hours?', B1='Could you check the opening hours on your phone while I look at the map?', B2='Would you mind checking the opening hours? That would help us decide.')),
      dict(q='Why is a short summary useful?', pt='Por que um resumo curto é útil?', levels=dict(A1='So we know the plan.', A2='To check that everyone has the same plan.', B1='A summary confirms who does what and when.', B2='Summarizing the decisions prevents misunderstandings and confirms the next steps.'))],
  compare='In Brazil, plans with friends often change at the last minute and are confirmed by message. In English, the phrase “To sum up” also works in a message: “So: post office at nine, market at ten.” How do you confirm plans?',
  teach=T('Ativar o contexto cultural da revisão: como as funções do A2 se combinam numa conversa real.',
   solo=['Mostre os 3 cartões e peça hipóteses antes de explicar.', 'Peça que o estudante compare com a forma como confirma planos com amigos.'], group=['Cada estudante escolhe um cartão e explica em uma frase.', 'Pergunte “Do you agree?” entre colegas.'],
   answers=['Q1: I’d rather… / plano B.', 'Q2: Could you check…?', 'Q3: para confirmar quem faz o quê e quando.'], extra=['Do you check the weather before you plan?', 'How do you confirm a plan by message?'],
   support=['Use as respostas do nível A1 como andaime e peça que repitam.'], stretch=['B2: resuma um plano de três pessoas em duas frases.'])),
 dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene='plaza', tod='day', cast=['Ana', 'Tom', 'Maya']),
  pass1=dict(q='What are the friends doing?', pt='O que os amigos estão fazendo?', opts=['Planning their Saturday', 'Buying tickets for a flight', 'Preparing a class talk'], ans=0),
  pass2=dict(tasks=[dict(label='First idea', ans='picnic'), dict(label='Problem with the first idea', ans='rain'), dict(label='Market opens at', ans='ten'), dict(label='Ana is waiting for her', ans='jacket'), dict(label='First stop', ans='post office')]),
  teach=T('Compreender a situação antes de ver o texto: ideia principal e depois 5 informações.',
   solo=['Esconda o texto. 1ª escuta: só a ideia principal.', '2ª escuta: primeira ideia, problema, horário da feira, encomenda e primeira parada.', 'Mostre o texto só depois da 2ª escuta.'], group=['Escuta coletiva; duplas anotam as respostas antes de revelar.', 'Compare as respostas entre as duplas e só então mostre o texto.'],
   answers=['Pass 1: planning their Saturday.', 'Pass 2: picnic · rain · ten · jacket · post office.'], extra=['Who changes the plan? Why?', 'Who will contact Maya?'],
   support=['Use o botão “Slow” na 2ª escuta.', 'Pause depois de cada fala se necessário.'])),
 dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation',
  qs=[dict(q='Why does Ana prefer the market?', opts=['The forecast says rain', 'The park is closed', 'She doesn’t like picnics'], ans=0), dict(q='What does Tom ask Ana to check?', opts=['The opening hours', 'The bus schedule', 'The price of a jacket'], ans=0), dict(q='What problem does Ana have?', opts=['Her order hasn’t arrived', 'She lost her phone', 'She missed a class'], ans=0), dict(q='What is the final plan?', opts=['Post office at nine, market at ten', 'Picnic at noon', 'Market at nine, picnic at ten'], ans=0)],
  retell=dict(prompt='Retell the conversation in your own words, at your level.', starters=['Tom suggests…', 'Ana prefers… because…', 'Then they talk about…', 'In the end, they decide…']),
  teach=T('Ler o diálogo, perceber os chunks de várias situações e recontar.',
   solo=['O estudante lê o papel da Ana; você lê o do Tom.', 'Peça que reconte a conversa no nível que conseguir.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia: uma frase por estudante.'],
   answers=['The forecast says rain · the opening hours · her order hasn’t arrived · post office at nine, market at ten'], extra=['Which part is planning? Which part is a request? Which part is a problem?', 'What would YOU suggest?'],
   errors=[('I rather go to the market.', 'I’d rather go to the market.'), ('My order didn’t arrive yet.', 'My order hasn’t arrived yet.')], support=['Mostre a tradução (botão PT) depois da 2ª leitura.'])),
 dict(t='rl_chunks', stage='notice', title='Useful expressions',
  items=[dict(en='What about…?', pt='Que tal…?', use='Review: suggest an idea.', reg='neutral', alt='Also: **How about…?**', pri=True),
         dict(en='I’d rather…', pt='Eu prefiro…', use='Review: say what you prefer.', reg='polite', alt='Simple: **I prefer…**', pri=True),
         dict(en='Could you…?', pt='Você poderia…?', use='Review: ask politely for help.', reg='polite', alt='Formal: **Would it be possible to…?**', pri=True),
         dict(en='My order hasn’t arrived.', pt='Meu pedido não chegou.', use='Review: explain a delivery problem.', reg='neutral', alt='Change it: **I’d like to change…**', pri=True),
         dict(en='To sum up, …', pt='Resumindo…', use='Review: close with a summary.', reg='neutral', alt='Also: **In summary, …**', pri=True),
         dict(en='Let’s…', pt='Vamos…', use='Make a suggestion that includes both of you.', reg='neutral'),
         dict(en='I’ll take care of…', pt='Eu cuido de…', use='Promise to do something.', reg='neutral'),
         dict(en='Would it be possible to…?', pt='Seria possível…?', use='Ask for something bigger politely.', reg='formal')],
  discover=dict(fns=['Suggesting and preferring', 'Asking for help', 'Explaining a problem', 'Summing up'],
   items=[dict(en='What about a picnic on Saturday?', fn='Suggesting and preferring'), dict(en='I’d rather go to the market.', fn='Suggesting and preferring'), dict(en='Could you check the opening hours?', fn='Asking for help'), dict(en='My order hasn’t arrived yet.', fn='Explaining a problem'), dict(en='To sum up: post office at nine.', fn='Summing up')]),
  note='This is a spaced review: choose the five ★ expressions that you want to use without notes at the end of the class.',
  teach=T('Revisão espaçada: reconhecer a função de cada chunk e escolher 5 para usar sem consulta.',
   solo=['Pergunte “Which lesson did this come from?” antes de dar o significado.', 'Peça um exemplo próprio para cada ★.'], group=['Cada estudante escolhe a expressão mais difícil e explica quando usa.', 'Compare em duplas: qual expressão vocês esquecem mais?'],
   answers=['Suggesting and preferring · Asking for help · Explaining a problem · Summing up'], extra=['Which expression do you forget most often?'], errors=[('Could you to check?', 'Could you check?')], support=['Trabalhe só 3 das expressões ★ na primeira rodada.'])),
 dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
  patterns=[dict(name='Suggest and prefer', formula='**What about** + -ing / noun? · **I’d rather** + base verb', ex=['What about a picnic?', 'I’d rather go to the market.', 'What about going on Sunday?'], main=True),
            dict(name='Ask politely', formula='**Could you** + base verb? · **Would it be possible to** + base verb?', ex=['Could you check the opening hours?', 'Would it be possible to pick it up there?', 'Could you call them?'], main=True),
            dict(name='Explain a problem', formula='**My order hasn’t arrived** / **I’d like to change** + noun', ex=['My order hasn’t arrived yet.', 'I’d like to change the address.']),
            dict(name='Sum up', formula='**To sum up,** + plan', ex=['To sum up, post office at nine.', 'To sum up, we meet at ten.'])],
  swap=dict(frame='What about {place} on {day}?', tpt='Que tal {place} em {day}?',
   slots=[dict(k='place', label='Place', opts=[dict(en='a picnic', pt='um piquenique'), dict(en='the food market', pt='a feira de comidas'), dict(en='a museum', pt='um museu'), dict(en='a movie', pt='um filme')]),
          dict(k='day', label='Day', opts=[dict(en='Saturday', pt='sábado'), dict(en='Sunday', pt='domingo'), dict(en='Friday night', pt='sexta à noite')])]),
  register=dict(head=['Spoken English', 'Written English'], rows=[['What about a picnic?', 'Would you like to have a picnic?'], ['Could you check the hours?', 'Could you please confirm the opening hours?'], ['My order hasn’t arrived.', 'I am writing about a missing order.'], ['To sum up, nine and ten.', 'In summary, we will meet at nine and ten.']],
   note='These are differences of context and register, not absolute rules.'),
  teach=T('Revisar os padrões principais do A2 (sugerir/preferir e pedir com educação); os outros são expansão.',
   solo=['Mostre o padrão DENTRO do diálogo (grife os chunks).', 'Use “Swap the words”: toque em cada peça e peça que o estudante diga a frase completa.', 'Compare spoken × written em 2 exemplos.'], group=['Troca em cadeia: cada estudante muda UMA peça e o próximo repete a frase.', 'Em pares: um escolhe as peças, o outro fala.'],
   answers='Padrão 01/02 são o foco; 03/04 são expansão para quem avançar rápido.', extra=['Change one word and say the new sentence.', 'Which pattern from earlier lessons do you want to review?'],
   errors=[('What about we go?', 'What about going?'), ('Could you to check?', 'Could you check?'), ('To sum up: we goes at ten.', 'To sum up, we go at ten.')], support=['Fique só com What about… e Could you… na primeira rodada.'], stretch=['Combinar as três funções em uma fala de 3 frases.'])),
 dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English',
  focus='Reduction: could you / would you', tip='In fast speech, “could you” sounds like “couldja” and “would you” like “wouldja”. This is natural in casual American English. The goal is to be clear and natural, not to remove your accent.',
  items=[dict(say='Could you check the hours?', linked='Could-ja CHECK the HOURS?', ipa='/kʊdʒə/', rhythm='ooOoO'), dict(say='Would you like a picnic?', linked='Would-ja LIKE a PIC-nic?', ipa='/wʊdʒə/', rhythm='ooOoOo'), dict(say='What about Saturday?', linked='What-a-BOUT SAT-ur-day?', ipa='/wʌtəbaʊt/', rhythm='ooOOoo')],
  identify=[dict(q='Which one do you hear?', opts=['Could you call them?', 'Could he call them?', 'Could we call them?'], ans=0, say='Could you call them?'), dict(q='Which one do you hear?', opts=['Would you like some coffee?', 'Would he like some coffee?', 'Would we like some coffee?'], ans=0, say='Would you like some coffee?')],
  own=dict(prompt='Write one “Could you…?” and one “Would you like…?” question that you could really ask a friend.', criteria='Say them twice: slowly, then with “couldja / wouldja”. Did they sound smooth?'),
  teach=T('UM só fenômeno: redução (could you → couldja, would you → wouldja).',
   solo=['3 passagens: escutar e identificar → reproduzir ritmo e redução → usar em pergunta própria.', 'Modele devagar e normal; mostre que as palavras se unem.'], group=['Coro, depois duplas; circule ouvindo.', 'Cada estudante cria uma pergunta própria com a redução.'],
   answers=['Identify 1: Could you call them? · Identify 2: Would you like some coffee?'], errors=[('Could — you (pausa e “you” forte).', 'Could-ja (unido, “you” fraco).'), ('Could com “l” pronunciado.', '“l” mudo em could: /kʊd/')], support=['Reduza a velocidade e conte as batidas em voz alta.'])),
 dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
  levels=[dict(h='Controlled practice — choose the best answer', items=[
    mcq('1. It might rain on Saturday. You prefer a different plan.', ['I’d rather go to the market.', 'I rather the market.', 'I’d rather to market go.'], 0, 'I’d rather + base verb.'),
    mcq('2. You need a friend to check the opening hours.', ['Could you check the opening hours?', 'You check hours I.', 'Could you checking hours?'], 0, 'Could you + base verb.'),
    mcq('3. Your jacket from an online store is late.', ['My order hasn’t arrived yet.', 'My jacket not arrived me.', 'I didn’t arrive the order.'], 0, 'My order hasn’t arrived yet.'),
    mcq('4. You want to close the plan.', ['To sum up, post office at nine and market at ten.', 'The end of plan.', 'I summary: nine.'], 0, 'To sum up, + the plan.')]),
   dict(h='Guided practice — complete, substitute and transform', items=[
    gap('___ about a picnic on Sunday?', 'What', 'What about + noun.', ['What', 'How', 'Where']),
    gap('Would it be possible ___ pick it up today?', 'to', 'Would it be possible + to + verb.', ['to', 'for', 'of']),
    swp('Make it polite:', 'Check the hours.', ['Could you check the hours?', 'Could you check the hours, please?', 'Would it be possible to check the hours?'], 'Could you check the hours, please?', 'Could you + verb turns a command into a polite request.'),
    swp('Ask to change the address:', 'the address', ['I’d like to change the address.', 'I’d like to change the address, please.'], 'I’d like to change the address.', 'I’d like to change + noun.'),
    rep('Should we meet at nine or ten?', 'Choose the best reply.', ['I’d rather meet at ten, if that’s okay.', 'Nine ten we meet I.', 'Yes, I rather.'], 0, 'Answer the choice and show a preference politely.')])],
  teach=T('Do controlado ao guiado: revisar funções de várias aulas antes da fala livre.',
   solo=['Peça que o estudante justifique cada resposta e diga de qual aula é o padrão.', 'Se acertar rápido, peça a versão mais informal ou mais educada.'], group=['Resolvam em duplas e comparem antes de revelar.', 'Equipes: ponto por resposta justificada.'],
   answers=['1: I’d rather go to the market. · 2: Could you check the opening hours? · 3: My order hasn’t arrived yet. · 4: To sum up, …', 'Gap: What · to · Could you check the hours, please? · I’d like to change the address. · I’d rather meet at ten.'], extra=['Say each correct answer aloud with “couldja” where natural.'],
   errors=[('I’d rather to go.', 'I’d rather go.'), ('Would it be possible send?', 'Would it be possible to send?')], support=['Ofereça o banco de palavras (chips) nas lacunas.'])),
 dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — a full Saturday',
  brief=dict(teacher='You are the friend (add a problem each time!).', student='You plan a Saturday with a friend: suggest, ask for help, handle a problem and sum up.'),
  orders=['A picnic that might turn into a museum day', 'A lunch plan and a late online order', 'A trip to a market with a friend who arrives late'],
  complications=['The weather changes.', 'Your order is late and you need to change the address.', 'Your friend can’t come at the agreed time.', 'The place is closed on Saturdays.'],
  rounds=[dict(label='With support', desc='Chunks on screen', help=['What about…?', 'I’d rather…', 'Could you…?', 'To sum up…']), dict(label='Keywords', desc='Only the keywords', help=['plan', 'weather', 'ask', 'problem', 'summary'], kw=True), dict(label='No script', desc='Free', help=[])],
  success=['I suggest and decide.', 'I ask politely.', 'I solve a problem.', 'I summarize the plan.'],
  teach=T('Simulação com complicação inesperada e três rodadas com menos apoio.',
   solo=['Combine o cenário com o sábado real do aluno.', 'Rodada 1: com chunks. Rodada 2: só palavras-chave. Rodada 3: sem roteiro.', 'Meta de fala: 60–70% do tempo para o estudante. Anote 2–3 correções para a devolutiva.'],
   extra=['What if two problems happen at once?'], errors=[('I can’t go because rain.', 'I can’t go because of the rain. / because it’s raining.')], support=['Volte à rodada 1 se travar; peça que repita só a primeira frase.'], stretch=['Peça que resolva dois problemas na mesma conversa e faça o resumo no fim.'])),
 dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations',
  rounds=[dict(title='Suggest and prefer', min=3, task='Suggest a weekend plan. Your partner prefers something else.', hint='What about…? / I’d rather…'), dict(title='Ask for help', min=3, task='Ask your partner to check or do something for the plan.', hint='Could you…? / Would it be possible to…?'), dict(title='Solve a problem', min=3, task='Something goes wrong: late order, rain or a closed place.', hint='My order hasn’t arrived. / I’d like to change…'), dict(title='Sum up', min=2, whole=True, task='Whole group: each pair summarizes their final plan.', hint='To sum up, …')],
  infogap=dict(title='Saturday plan', instr='Ask your partner and complete your card. Do not look at the other card!',
   a=dict(title='You know the places', task='You know the places. Ask about the times.', rows=[dict(k='Post office', v='Main Street'), dict(k='Food market', v='Plaza Square'), dict(k='Post office time', v=''), dict(k='Market time', v='')]),
   b=dict(title='You know the times', task='You know the times. Ask about the places.', rows=[dict(k='Post office', v=''), dict(k='Food market', v=''), dict(k='Post office time', v='9:00'), dict(k='Market time', v='10:00')])),
  teach=T('Fluência por repetição de funções diferentes com informações novas a cada rodada.',
   group=['Troque os pares a cada rodada (A+B / C+D → A+C / B+D → A+D / B+C → grupo todo). Com 6 estudantes, três duplas simultâneas.', 'Sem salas simultâneas: interações sequenciais enquanto uma dupla apresenta.', 'Responsabilidade individual: cada aluno faz ≥1 sugestão, ≥1 pedido e ≥1 resumo.'],
   answers=['Info gap: A tem os locais (Main Street, Plaza Square); B tem os horários (9:00, 10:00). Cada um completa perguntando.'], extra=['Where is the post office?', 'What time does the market open?'],
   errors=[('What hour is the market?', 'What time does the market open?'), ('It is in Plaza Square place.', 'It’s in Plaza Square.')], support=['Entregue frases-modelo no chat da turma.'])),
 dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — a busy Saturday',
  goal='Each group must plan a Saturday in English, deal with a problem and summarize the final plan.',
  missions=[dict(who='A', role='Friends', mission='Plan a day out. The weather is bad, so change the plan, and ask a friend to check a place’s hours.', constraint='Use “What about…?”, “I’d rather…” and “Could you…?”', start='So, what about…?'),
            dict(who='B', role='Friends', mission='A package is late and you have to be home on Saturday. Solve it by changing the delivery or the plan.', constraint='Use “My order hasn’t arrived” and “I’d like to change…”.', start='I have a problem: my order hasn’t arrived…'),
            dict(who='C', role='Friends', mission='Organize a small dinner for four. Each person takes a task and promises to do it.', constraint='Use “Would it be possible to…?” and “I’ll take care of…”; finish with “To sum up…”.', start='Let’s plan the dinner. Could you…')], min=11,
  success=['Suggest and decide.', 'Ask politely.', 'Solve a problem.', 'Summarize the plan.'],
  teach=T('Realizar algo com o inglês: combinar várias situações do A2 numa só conversa.',
   group=['Cada grupo recebe papéis, restrição e missão. Alterne quem propõe e quem reage.', 'Progressão: 1ª rodada com frases de apoio, 2ª só palavras-chave, 3ª sem roteiro.', 'Observe e anote 2–3 correções prioritárias; devolutiva no fim.'],
   answers=['Modelo: “What about the park?” → “I’d rather go to a café, it’s going to rain.” → “Could you check if it’s open?” → “To sum up: café at ten.”'], extra=['What if a friend wants a different plan?'], support=['Dê o início de frase (“Start with”) em cada cartão.'])),
 dict(t='rl_write', stage='write', title='Writing — a small real-life task',
  task='Write a short message to a friend that plans a Saturday: suggest a plan, ask for help, mention a problem and sum up.',
  steps=['Suggestion', 'Request', 'Problem', 'Summary'],
  model='Hi Tom! **What about** the food market on Saturday? **Could you** check when it opens? Also, **my order hasn’t arrived** yet, so **I’d like to change** the address. **To sum up:** post office at nine, market at ten. See you there!',
  checklist=['I made a suggestion.', 'I asked for help politely.', 'I mentioned a problem and a solution.', 'I summed up the plan.'],
  tip='Fix only 2–3 priority points. Show a more natural way to say the same idea instead of rewriting everything.', fix=dict(n=3),
  teach=T('Produção escrita curta que reúne as funções revisadas.',
   solo=['Peça a mensagem; corrija 2–3 pontos prioritários e mostre uma forma mais natural.'], group=['Cada estudante escreve; depois troquem os textos entre colegas e corrijam em duplas.'],
   extra=['Add one more request to your message.'], errors=[('What about we meet?', 'What about meeting at ten?'), ('To sum up: we meet at ten o’clock hours.', 'To sum up, we meet at ten.')], support=['Dê o modelo e peça só para trocar os dados.'])),
 feedback('Example: You changed topic and function easily (planning → request → problem).', 'Example: Link “could you” as “couldja” in fast speech.', 'Example: Do the whole conversation without notes and keep it for two minutes.', 'Observe o controle de várias funções na mesma conversa.'),
 dict(t='rl_exit', stage='exit', title='Exit ticket & homework',
  tasks=[dict(ic='💡', name='Suggest and prefer', prompt='Suggest a picnic and say you prefer a market because of the rain.', model='What about a picnic? Actually, I’d rather go to the market because it might rain.'), dict(ic='💬', name='Ask politely', prompt='Ask a friend to check the opening hours.', model='Could you check the opening hours, please?'), dict(ic='⭐', name='Sum up', prompt='Sum up: post office at nine, market at ten.', model='To sum up, post office at nine and market at ten.')],
  homework=dict(h='Your real-life English mission', min='10–15', items=['Record a 60-second audio planning a day, asking for help and summing up.', 'Write a short message with a suggestion, a request, a problem and a summary.', 'Choose the three A2 expressions you still forget and write two examples for each.', 'Listen to the dialogue again and count how many functions you hear.']),
  spaced=dict(next=['What about…?', 'I’d rather…', 'Could you…?'], week=['My order hasn’t arrived.', 'I’d like to change…', 'To sum up…'], unit=['Plan · ask · solve · sum up']),
  teach=T('Toda aula termina com uma produção observável.', solo=['Sem consultar as anotações: sugerir/preferir, pedir com educação e resumir.'], group=['Exit challenge individual; compare com o colega e combine a tarefa de continuidade.'],
   answers=['What about a picnic? … I’d rather go to the market… · Could you check the opening hours? · To sum up, post office at nine and market at ten.'], extra=['Revisão espaçada: retomar na missão final da unidade (próxima aula).'])),
 levels([('Park? No. Market. Ten.', None), ('What about the park? I’d rather go to the market. Could you check when it opens?', 'Combine suggest, prefer and ask.'), ('Since it might rain, I think we should go to the market instead, and I’ll check the hours myself.', None), ('Given the forecast, I’d suggest moving indoors; would you mind checking whether the market is open?', None), ('Weather permitting, the park would be lovely, but I wouldn’t want to risk it; shall we settle on the market?', None), ('The market seems the more prudent choice, so let’s commit to it and leave the park for a drier day.', None)], 'Mostrar a progressão e retomar as situações do A2.')
]

LESSON = dict(n=99, topic='A2 situations review', level='A2', title='A2 Situations Review', pt='Revisão de situações do A2', unit=unit(5), minutes=60, cast=['Ana', 'Tom', 'Maya'], scene='plaza', tod='day', plan=PLAN, dialog=DIALOG, pages=PAGES)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(PAGES), 'páginas')
