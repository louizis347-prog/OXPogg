#!/usr/bin/env python3
"""Aula 56 · Real-Life Mission Day 7 (A1, 60 min). Gera data/v3/056.json."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from rl_common import PLAN, teach, finish

# ---- construtor compacto (dados -> páginas rl_*) ----
UNIT_NAME = 'Free time'
UNIT_MAP = ['Hobbies and interests', 'Weekend plans and sports', 'At the cinema', 'Music and concerts', 'Going to a party', 'Messages and social media', 'Making friends online', 'Real-Life Mission Day 7']

def build(S):
    R = S['roles']; cast = S['cast']
    dlg = dict(speakers={R[0]: {'name': cast[0]}, R[1]: {'name': cast[1]}}, lines=[dict(who=R[w], en=en, pt=pt) for w, en, pt in S['dialog']])
    E = S['err']; X = S['xq']
    def er(k): return [dict(w=E[(2 * k + i) % len(E)][0], r=E[(2 * k + i) % len(E)][1]) for i in range(2)]
    def ex(k): return [X[k % len(X)], X[(k + 3) % len(X)]]
    T = S['tchr']
    unit = dict(n=7, k=S['k'], of=8, name=UNIT_NAME)
    P = []
    P.append(dict(t='rl_open', stage='warm', title=S['title'], pt=S['pt'], level='A1', unit=dict(unit, map=UNIT_MAP),
      situation=dict(text=S['sit'], scene=S['scene'], tod=S.get('tod', 'day'), cast=cast), goal=S['goal'], canDo=S['canDo'], success=S['success'], think=S['think'],
      teach=teach(goal='Abrir a aula pela situação real, não pela regra.', solo=['Leia o objetivo em voz alta e peça que o estudante diga, com as próprias palavras, o que vai conseguir fazer hoje.', 'Faça a pergunta “Think about it” antes de mostrar qualquer expressão.'],
        group=['Cada estudante diz UMA palavra que associa à situação de hoje.', 'Mostre os critérios de sucesso: eles são a missão final da aula.'], extra=ex(0), support=['Aceite respostas curtas ou em português na primeira rodada e reformule em inglês.'])))
    P.append(dict(t='rl_warm', stage='warm', title='Connection & warm-up', intro=dict(solo='Start with real questions about the student’s life, not a grammar test.', group='One question per student, then a question back to a classmate.'),
      recall=S['recall'], qs=[dict(q=q, pt=pt, sup=sup) for q, pt, sup in S['warm']], tip='Use the answers to find gaps and to recycle earlier content. The goal is to enter English from the first minute.',
      teach=teach(goal='Entrar no idioma no primeiro minuto e retomar a aula anterior.', extra=ex(1), errors=er(0), support=['Ofereça as respostas-modelo (chips) e peça apenas que escolham uma.'])))
    P.append(dict(t='rl_culture', stage='immersion', title='Cultural snapshot — ' + S['ctitle'], intro=S['cintro'],
      cards=[dict(vis=v, en=en, pt=pt, note=n) for v, en, pt, n in S['cards']],
      qs=[dict(q=q, pt=pt, levels=dict(A1=a1, A2=a2, B1=b1, B2=b2)) for q, pt, a1, a2, b1, b2 in S['cqs']], compare=S['compare'],
      teach=teach(goal='Ativar o contexto cultural e as primeiras hipóteses.', solo=['Mostre os 3 cartões e peça hipóteses antes de explicar.', 'Peça que o estudante compare com o que acontece no Brasil.'], group=['Cada estudante escolhe um cartão e explica em uma frase.', 'Pergunte “Do you agree?” entre colegas.'],
        answers=S['cans'], extra=ex(2), support=['Use as respostas do nível A1 como andaime e peça que repitam.'], stretch=['B2: compare as convenções sociais do Brasil e dos EUA nessa situação.'])))
    p1 = S['p1']; p2 = S['p2']
    P.append(dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene=S['scene'], tod=S.get('tod', 'day'), cast=cast),
      pass1=dict(q=p1[0], pt=p1[1], opts=p1[2], ans=p1[3]), pass2=dict(tasks=[dict(label=l, ans=a, **({'alt': al} if al else {})) for l, a, al in p2]),
      teach=teach(goal='Compreender a situação antes de ver o texto: ideia principal e depois informações específicas.', solo=['Esconda o texto. 1ª escuta: só a ideia principal.', '2ª escuta: as informações da lista.', 'Mostre o texto só depois da 2ª escuta.'],
        group=['Escuta coletiva; duplas anotam as respostas antes de revelar.', 'Compare as respostas entre as duplas e só então mostre o texto.'], answers=['Pass 1: ' + p1[2][p1[3]] + '.', 'Pass 2: ' + ' · '.join(a for _, a, _ in p2)],
        extra=['Who is speaking? How do you know?', ex(3)[0]], support=['Use o botão “Slow” na 2ª escuta.', 'Pause depois de cada fala se necessário.'])))
    P.append(dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation', qs=[dict(q=q, opts=o, ans=a) for q, o, a in S['dqs']],
      retell=dict(prompt='Retell the conversation in your own words, at your level.', starters=S['retell']),
      teach=teach(goal='Ler o diálogo, perceber os chunks e recontar.', solo=['O estudante lê um papel; você lê o outro. Depois troquem.', 'Peça que reconte a conversa no nível que conseguir.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia: uma frase por estudante.'],
        answers=S['dans'], extra=ex(4), errors=er(1), support=['Mostre a tradução (botão PT) depois da 2ª leitura.'])))
    P.append(dict(t='rl_chunks', stage='notice', title='Useful expressions',
      items=[dict(en=en, pt=pt, use=use, reg=reg, **({'alt': alt} if alt else {}), **({'pri': True} if pri else {})) for en, pt, use, reg, alt, pri in S['chunks']],
      discover=dict(fns=S['fns'], items=[dict(en=en, fn=fn) for en, fn in S['disc']]),
      note='Instead of memorizing the whole list, choose 3–5 expressions (★) to use again and again. The others are for understanding and for stretching later.',
      teach=teach(goal='Escolher 3–5 chunks para uso repetido e descobrir a função de cada um.', solo=['Pergunte “When do you say it?” antes de dar o significado.', 'Compare formal × informal e peça um exemplo próprio.'], group=['Cada estudante escolhe a expressão que mais usaria e explica quando.', 'Compare equivalentes formais e informais em duplas.'],
        answers=[' · '.join(S['fns'])], extra=ex(5), errors=er(2), support=['Trabalhe só as 3 expressões ★ nesta aula.'])))
    sw = S['swap']
    P.append(dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns',
      patterns=[dict(name=n, formula=f, ex=e, **({'main': True} if m else {})) for n, f, e, m in S['pats']],
      swap=dict(frame=sw[0], tpt=sw[1], slots=[dict(k=k, label=l, opts=[dict(en=a, pt=b) for a, b in o]) for k, l, o in sw[2]]),
      register=dict(head=['Spoken English', 'Written English'], rows=S['reg'], note='These are differences of context and register, not absolute rules: contractions and short forms also appear in informal writing.'),
      teach=teach(goal='Fixar os 2 padrões principais; os outros são expansão. Usar a troca de palavras para variar a fala.', solo=['Mostre o padrão DENTRO do diálogo (grife os chunks).', 'Use “Swap the words”: toque em cada peça e peça a frase completa.', 'Compare spoken × written em 2 exemplos.'],
        group=['Troca em cadeia: cada estudante muda UMA peça e o próximo repete a frase.', 'Em pares: um escolhe as peças, o outro fala.'], answers='Os padrões 01 e 02 são o foco; os demais são expansão para quem avançar rápido.', extra=ex(6), errors=er(3),
        support=['Fique só com o primeiro padrão na primeira rodada.'], stretch=['Combinar dois padrões na mesma frase.'])))
    pr = S['pron']
    P.append(dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English', focus=pr['focus'], tip=pr['tip'],
      items=[dict(say=s, linked=l, ipa=i, rhythm=r) for s, l, i, r in pr['items']], identify=[dict(q='Which one do you hear?', opts=o, ans=a, say=o[a]) for o, a in pr['id']],
      own=dict(prompt=pr['own'], criteria=pr['crit']),
      teach=teach(goal='UM só fenômeno: ' + pr['focus'] + '.', solo=['3 passagens: escutar e identificar → reproduzir ritmo e entonação → usar em frase com conteúdo próprio.', 'Modele devagar e normal; peça que o estudante bata palmas na sílaba forte.'], group=['Coro, depois duplas; circule ouvindo.', 'Cada estudante cria uma frase própria.'],
        answers=['Identify: ' + ' · '.join(o[a] for o, a in pr['id'])], errors=er(4), support=['Reduza a velocidade e conte as batidas em voz alta.'])))
    C = S['chal']
    def mk(it):
        t = it[0]
        if t == 'mcq': return dict(type='mcq', q=it[1], opts=it[2], ans=it[3], why=it[4])
        if t == 'gap': d = dict(type='gap', text=it[1], ans=it[2], why=it[4]); (d.update(bank=it[3]) if it[3] else None); return d
        if t == 'swap': d = {'type': 'swap', 'instr': it[1], 'frm': it[2], 'ans': it[3], 'model': it[4], 'why': it[5]}; return d
        if t == 'reply': return dict(type='reply', npc=it[1], q='Choose the best reply.', opts=it[2], ans=it[3], why=it[4])
    P.append(dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges',
      levels=[dict(h='Controlled practice — choose the best answer', items=[mk(i) for i in C[0]]), dict(h='Guided practice — complete, substitute and transform', items=[mk(i) for i in C[1]])],
      teach=teach(goal='Do controlado ao guiado: completar, substituir e transformar antes da fala livre.', solo=['Peça que o estudante justifique cada resposta.', 'Se acertar rápido, peça a versão mais informal ou mais educada.'], group=['Resolvam em duplas e comparem antes de revelar.', 'Equipes: ponto por resposta justificada.'],
        answers=S['chans'], extra=ex(7), errors=er(5), support=['Ofereça o banco de palavras (chips) nas lacunas.'])))
    ro = S['role']
    P.append(dict(t='rl_role', for_='solo', stage='speak1', title='Personalized roleplay — ' + ro['title'], brief=dict(teacher=ro['teacher'], student=ro['student']), orders=ro['orders'], complications=ro['comp'],
      rounds=[dict(label='With support', desc='Chunks on screen', help=ro['chunks']), dict(label='Keywords', desc='Only the keywords', help=ro['kw'], kw=True), dict(label='No script', desc='Free', help=[])], success=S['success'],
      teach=teach(goal='Simulação com complicação inesperada e três rodadas com menos apoio.', solo=['Ligue o cenário à vida do estudante.', 'Rodada 1: com chunks. Rodada 2: só palavras-chave. Rodada 3: sem roteiro.', 'Meta de fala: 60–70% do tempo para o estudante. Anote 2–3 correções para a devolutiva.'],
        extra=ex(8), errors=er(6), support=['Volte à rodada 1 se travar; peça que repita só a primeira frase.'], stretch=ro['stretch'])))
    lb = S['lab']
    P.append(dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations', rounds=[dict(title=t, min=m, task=k, hint=h, **({'whole': True} if w else {})) for t, m, k, h, w in lb['rounds']],
      infogap=dict(title=lb['gt'], instr='Ask your partner and complete your card. Do not look at the other card!', a=dict(title=lb['at'], task=lb['atask'], rows=[dict(k=k, v=v) for k, v, _ in lb['rows']]), b=dict(title=lb['bt'], task=lb['btask'], rows=[dict(k=k, v=v) for k, _, v in lb['rows']])),
      teach=teach(goal='Fluência por repetição da função com informações novas a cada rodada.', group=['Troque os pares a cada rodada (A+B / C+D → A+C / B+D → A+D / B+C → grupo todo). Com 6 estudantes, três duplas simultâneas.', 'Sem salas simultâneas: interações sequenciais enquanto uma dupla apresenta.', 'Responsabilidade individual: cada aluno faz ≥1 pergunta e ≥1 resposta.'],
        answers=[lb['ans']], extra=ex(9), errors=er(7), support=['Entregue frases-modelo no chat da turma.'])))
    mi = S['miss']
    P.append(dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — ' + mi['title'], goal=mi['goal'], missions=[dict(who=w, role=r, mission=m, constraint=c, start=s) for w, r, m, c, s in mi['list']], min=11, success=S['success'],
      teach=teach(goal='Realizar algo com o inglês: o objetivo é resolver, não só falar certo.', group=['Cada grupo recebe papel, restrição e missão. Alterne os papéis.', 'Progressão: 1ª rodada com frases de apoio, 2ª só palavras-chave, 3ª sem roteiro.', 'Observe e anote 2–3 correções prioritárias; devolutiva no fim.'],
        answers=[mi['model']], extra=ex(10), support=['Dê o início de frase (“Start with”) em cada cartão.'])))
    wr = S['write']
    P.append(dict(t='rl_write', stage='write', title='Writing — a small real-life task', task=wr['task'], steps=wr['steps'], model=wr['model'], checklist=wr['check'],
      tip='Fix only 2–3 priority points. Show a more natural way to say the same idea instead of rewriting everything.', fix=dict(n=3),
      teach=teach(goal='Produção escrita curta ligada à situação comunicativa.', solo=['Peça o texto; corrija 2–3 pontos prioritários e mostre uma forma mais natural.'], group=['Cada estudante escreve; depois troquem os textos entre colegas e corrijam em duplas.'],
        extra=ex(11), errors=er(8), support=['Dê o modelo e peça só para trocar os dados.'])))
    fb = S['fb']
    P.append(dict(t='rl_feedback', stage='write', title='Feedback & review — Speaking Performance Check',
      criteria=[dict(k='flu', name='Fluency', desc='Mantém a comunicação sem interrupções excessivas.'), dict(k='lan', name='Language use', desc='Utiliza adequadamente padrões, vocabulário e expressões.'), dict(k='pro', name='Pronunciation', desc='É compreensível e usa ritmo e entonação adequados.'), dict(k='int', name='Interaction', desc='Responde, pergunta, esclarece e desenvolve a conversa.')],
      interpret=[dict(max=8, text='Needs more support. Revisit the main patterns with guided practice before the next lesson.'), dict(max=13, text='Functional performance. Work on the lowest criteria in the next lesson.'), dict(max=17, text='Good control. Raise complexity and speed; add follow-up questions.'), dict(max=20, text='Strong performance. Move to a more demanding situation.')],
      prompts=dict(well=fb[0], improve=fb[1], next=fb[2]),
      teach=teach(goal='Avaliar o que o aluno conseguiu comunicar, não só os erros gramaticais.', solo=['O estudante se autoavalia primeiro; depois você.', 'Feche com os três blocos: What you did well · What to improve · Your next challenge.'], group=['Dê um comentário por critério a cada estudante.', 'Cada um escolhe o próprio próximo desafio.'],
        answers='A rubrica é uma ferramenta interna de acompanhamento, não uma certificação CEFR.')))
    xt = S['exit']
    P.append(dict(t='rl_exit', stage='exit', title='Exit ticket & homework', tasks=[dict(ic=ic, name=n, prompt=p, model=m) for ic, n, p, m in xt['tasks']],
      homework=dict(h='Your real-life English mission', min='10–15', items=xt['hw']), spaced=dict(next=xt['next'], week=xt['week'], unit=xt['unit']),
      teach=teach(goal='Toda aula termina com uma produção observável.', solo=['Sem consultar as anotações: construir uma pergunta, responder a uma situação e usar uma expressão nova.'], group=['Exit challenge individual; compare com o colega e combine a tarefa de continuidade.'],
        answers=[' · '.join(m for _, _, _, m in xt['tasks'])], extra=['Revisão espaçada: retomar na próxima aula, depois de uma semana e na missão de encerramento da unidade.'])))
    lv = S['ladder']
    P.append(dict(t='rl_levels', stage='exit', title='Level up — the same situation from A1 to C2', you='A1', intro='You do not need six different methods: the structure stays, while language complexity and autonomy grow.',
      ladder=[dict(lv=a, say=b, goal=c) for a, b, c in lv],
      note='This progression is illustrative: complex sentences do not define a level on their own. CEFR also considers comprehension, autonomy, fluency, accuracy, interaction and appropriateness.',
      teach=teach(goal='Mostrar a progressão sem criar seis metodologias.', solo=['Mostre onde o estudante está e a próxima etapa.'], group=['Cada um escolhe a frase do próprio nível e a do próximo.'])))
    return dict(n=S['n'], topic=S['topic'], level='A1', title=S['title'], pt=S['pt'], unit=unit, minutes=60, cast=cast, scene=S['scene'], tod=S.get('tod', 'day'), plan=PLAN, dialog=dlg, pages=P)


S = dict(n=56, k=8, topic='Real-Life Mission Day 7', title='Mission Day: A Free Saturday', pt='Missão da unidade 7: um sábado livre', cast=['Paul', 'Isla', 'Beto'], roles=['Paul', 'Isla'], scene='park',
 sit='It is Saturday and you are free. You invite a friend, plan the day, get movie tickets, go to a party, share photos and message a new friend: one day, six real situations.',
 goal='By the end of the class you can chain six situations from the unit: talk about hobbies, invite and plan, buy tickets, go to a party, send messages and meet someone online.',
 canDo=['Invite a friend and plan a day', 'Buy tickets and give an opinion', 'Go to a party and leave politely', 'Message friends and stay safe online'],
 success=['I invite and plan.', 'I solve a small problem.', 'I share and react.', 'I stay polite and clear.'],
 think='If you have a free Saturday, which parts of this unit would you use first?',
 recall='Unit 7 review: I like to… · Do you want to…? · Two tickets for… · Can I bring…? · Send me the… · Where are you from?',
 warm=[('What do you usually do on Saturdays?', 'O que você costuma fazer aos sábados?', ['I rest.', 'I meet friends.', 'I play sports.']), ('Which class in this unit did you like the most?', 'De qual aula desta unidade você mais gostou?', ['The movie one.', 'The party one.', 'Hobbies.']), ('What is one new expression you use now?', 'Qual expressão nova você usa agora?', ['Do you want to…?', 'Send me the…', 'I’d better go.'])],
 ctitle='A free Saturday in the USA', cintro='A free Saturday in the USA can mix many things: a sport in the park, a movie, a party and chats with friends. Look and guess before you read.',
 cards=[('obj:ball', 'Park and sports', 'Parque e esportes', 'Many parks have fields and courts where people play for free.'), ('obj:envelope', 'Tickets and messages', 'Ingressos e mensagens', 'Plans are often made by text, and tickets are usually bought online or at the box office.'), ('prop:cake', 'Parties and potlucks', 'Festas e potlucks', 'Guests often bring a dish. It is polite to ask the host first.')],
 cqs=[('How do friends make plans in the USA?', 'Como amigos fazem planos nos EUA?', 'They text.', 'They text or use a group chat.', 'Plans are often made by text, then confirmed the same day.', 'Short messages make a plan flexible: people suggest a time, a place and adjust until it works.'),
      ('What helps conversation in a new place?', 'O que ajuda a conversar em um lugar novo?', 'Easy questions.', 'Easy questions like “Where are you from?”.', 'Simple questions about hobbies and plans start a friendly chat.', 'Light topics such as hobbies, teams and plans make it easy to connect without being too personal.'),
      ('Why is politeness important in all these situations?', 'Por que a educação é importante em todas essas situações?', 'It is friendly.', 'It makes people feel comfortable.', 'Please, thanks and a short reason make requests and goodbyes sound friendly.', 'Small words like please and thanks, plus a short reason to leave or decline, keep every interaction smooth.')],
 compare='In Brazil a free Saturday often means friends, food and music too. Which situation from this unit would you use most on your Saturday?',
 cans=['Q1: mensagens e grupos de conversa.', 'Q2: perguntas simples sobre hobbies e planos.', 'Q3: please, thanks e um motivo curto.'],
 p1=('What are they planning?', 'O que eles estão planejando?', ['A day together', 'A job interview', 'A trip abroad'], 0),
 p2=[('Meeting time', 'ten', ['10']), ('Sport', 'soccer', []), ('Movie time', 'seven', ['7']), ('Isla brings', 'snacks', ['camera'])],
 dialog=[(0, 'Hey Isla! **Do you want to** spend Saturday together?', 'Ei, Isla! Você quer passar o sábado comigo?'), (1, 'Sure! What’s the plan?', 'Claro! Qual é o plano?'), (0, '**Let’s meet** at ten in the park. We can play soccer.', 'Vamos nos encontrar às dez no parque. Podemos jogar futebol.'),
  (1, 'Great! And after that?', 'Ótimo! E depois?'), (0, '**Two tickets for** the movie at seven? I’ll buy them.', 'Dois ingressos para o filme das sete? Eu compro.'), (1, 'Perfect! **I’ll bring** snacks. And my camera.', 'Perfeito! Eu levo lanches. E a minha câmera.'),
  (0, 'Nice! **Send me the** photos later.', 'Legal! Me manda as fotos depois.'), (1, 'Sure. **BTW**, should I bring a jacket?', 'Claro. A propósito, devo levar um casaco?'), (0, 'Yes, it gets cold at night.', 'Sim, fica frio à noite.'), (1, 'Got it! See you Saturday!', 'Entendi! Nos vemos no sábado!')],
 dqs=[('Where do they meet?', ['At the park', 'At the cinema', 'At school'], 0), ('What do they play?', ['Soccer', 'Chess', 'Tennis'], 0), ('What time is the movie?', ['Seven', 'Ten', 'Nine'], 0), ('What does Isla bring?', ['Snacks and a camera', 'A cake', 'Nothing'], 0)],
 retell=['Paul invites Isla to…', 'They meet at…', 'After soccer, they go to…', 'Isla brings…'], dans=['The park at ten · soccer · the movie at seven · snacks and a camera'],
 chunks=[('Do you want to…?', 'Você quer…?', 'Invite a friend (class 50).', 'neutral', 'More polite: **Would you like to…?**', True), ('Let’s meet at…', 'Vamos nos encontrar em/às…', 'Fix a time and a place (class 50).', 'neutral', None, True), ('Two tickets for…', 'Dois ingressos para…', 'Buy tickets (class 51).', 'neutral', None, True), ('Send me the…', 'Me manda o/a…', 'Ask for a link or photo (class 54).', 'casual', None, True),
  ('Can I bring…?', 'Posso levar…?', 'Ask before a party (class 53).', 'neutral', None, False), ('I’m into…', 'Eu curto…', 'Say your interests (class 49).', 'casual', None, False), ('Where are you from?', 'De onde você é?', 'Meet a new friend (class 55).', 'neutral', None, False)],
 fns=['Inviting', 'Fixing time and place', 'Buying tickets', 'Asking for something', 'Meeting someone'],
 disc=[('Do you want to watch the game?', 'Inviting'), ('Let’s meet at six.', 'Fixing time and place'), ('Two tickets for the nine o’clock show.', 'Buying tickets'), ('Send me the photos, please.', 'Asking for something'), ('Where are you from?', 'Meeting someone')],
 pats=[('Inviting and planning', '**Do you want to** + verb?  /  **Let’s** + verb', ['Do you want to play soccer?', 'Let’s meet at ten.', 'Let’s go to the movies.'], True), ('Asking and offering', '**Can I bring** + noun?  /  **I’ll bring** + noun', ['Can I bring dessert?', 'I’ll bring snacks.', 'I’ll bring my camera.'], True), ('Buying and asking', '**Two tickets for** + movie  /  **Send me the** + noun', ['Two tickets for the seven o’clock show.', 'Send me the photos.'], False), ('Meeting people', '**Where are you from?**  /  **What do you do for fun?**', ['Where are you from?', 'What do you do for fun?'], False)],
 swap=('Do you want to {do} {when}? I’ll bring {thing}.', 'Você quer {do} {when}? Eu levo {thing}.', [('do', 'Activity', [('play soccer', 'jogar futebol'), ('see a movie', 'ver um filme'), ('go to a party', 'ir a uma festa'), ('go to a concert', 'ir a um show')]), ('when', 'When', [('on Saturday', 'no sábado'), ('tonight', 'hoje à noite'), ('on Sunday', 'no domingo')]), ('thing', 'What', [('snacks', 'lanches'), ('drinks', 'bebidas'), ('my camera', 'minha câmera')])]),
 reg=[['Wanna come?', 'Would you like to join us?'], ['Send me the pics.', 'Could you please send me the photos?'], ['BTW, bring a jacket.', 'By the way, please bring a jacket.'], ['I’d better go.', 'I should be leaving now.']],
 pron=dict(focus='Sentence stress', tip='Review of the unit: the important words are strong and the small words are weak. “Do you WANT to PLAY SOCcer?” Say the plan with this rhythm.',
  items=[('Let’s meet at ten.', 'Let’s MEET at TEN.', '/lɛts ˈmit ət ˈtɛn/', 'oOoO'), ('Two tickets for the seven o’clock show.', 'Two TICK-ets for the SEV-en o’CLOCK SHOW.', '/ˈtu ˈtɪkəts fər ðə ˈsɛvən əˈklɑk ˈʃoʊ/', 'oOooooOoOO'), ('Send me the photos later.', 'SEND me the PHO-tos LA-ter.', '/ˈsɛnd mi ðə ˈfoʊtoʊz ˈleɪtər/', 'OooOoOo')],
  id=[(['Let’s meet at ten.', 'Let’s meet at tent.', 'Let’s meat at ten.'], 0), (['Send me the photos.', 'Send me the foods.', 'Send me the fuzz.'], 0)], own='Write a sentence about your Saturday plan.', crit='Say it twice. Did the important words sound stronger than the small words?'),
 chal=([('mcq', '1. You want to invite a friend to play soccer.', ['Do you want to play soccer?', 'You want soccer play?', 'Do you want playing soccer?'], 0, 'Do you want to + verb?'), ('mcq', '2. You want to buy movie tickets.', ['Two tickets for the seven o’clock show, please.', 'I want tickets two seven.', 'Give seven ticket.'], 0, 'Two tickets for + show, with please.'), ('mcq', '3. You go to a party and you want to bring something.', ['Can I bring dessert?', 'I can to bring dessert?', 'Bring I dessert?'], 0, 'Can I + base verb.'), ('mcq', '4. You meet a new friend online.', ['Where are you from?', 'Where you from are?', 'From where are?'], 0, 'Where are you from?')],
  [('gap', 'Let’s ___ at ten.', 'meet', ['meet', 'meeting', 'met'], 'Let’s + base verb.'), ('gap', 'I’d ___ go. It’s late.', 'better', ['better', 'best', 'good'], 'I’d better + base verb.'), ('swap', 'Ask for the photos politely:', 'Send me the photos.', ['Could you send me the photos?', 'Could you send me the photos, please?'], 'Could you send me the photos?', 'Could you + base verb is polite.'), ('swap', 'Say what you are into:', 'music', ['I’m into music.', 'I’m into music!'], 'I’m into music.', 'I’m into + noun.'), ('reply', 'Did you like the movie?', ['Yes! It was great.', 'Yes, I am great.', 'Movie liked me.'], 0, 'Yes + opinion.')]),
 chans=['1: Do you want to play soccer? · 2: Two tickets for the seven o’clock show, please. · 3: Can I bring dessert? · 4: Where are you from?', 'Gap: meet · better · Could you send me the photos? · I’m into music. · Yes! It was great.'],
 role=dict(title='a free Saturday', teacher='You are the friend who changes plans during the day (change the plan during the scene!).', student='You are the main person: invite, plan, buy tickets, go to a party and message a friend.',
  orders=['Plan a Saturday with soccer and a movie', 'Plan a Saturday with a concert and a party', 'Plan a Saturday with a hobby, a movie and a message'], comp=['The movie you want is sold out: choose another show.', 'Your friend can’t come at ten: suggest a new time.', 'At the party you don’t know anyone: start a conversation.', 'A new online friend asks for your address: refuse politely.'],
  chunks=['Do you want to…?', 'Let’s meet at…', 'Two tickets for…', 'Send me the…'], kw=['invite', 'movie', 'party', 'photos', 'safe'], stretch=['Peça que o estudante conte o sábado inteiro, do convite à despedida.']),
 lab=dict(rounds=[('Invite and plan', 3, 'Station 1: invite your partner and fix a time and place.', 'Do you want to…? / Let’s meet at…', False), ('Movie and snacks', 3, 'Station 2: buy tickets and ask the show time.', 'Two tickets for… / What time is the show?', False), ('Party and chat', 3, 'Station 3: arrive at a party, ask to bring something, meet a new person.', 'Can I bring…? / Where are you from?', False), ('Our Saturday', 2, 'Whole group: each pair shares the best Saturday plan.', 'First we… then we…', True)],
  gt='Saturday plan', at='Student A has Paul’s plan', atask='You know the morning and the evening. Ask about the afternoon and the night.', bt='Student B has Isla’s plan', btask='You know the afternoon and the night. Ask about the morning and the evening.',
  rows=[('10:00 morning', 'Soccer in the park', ''), ('2:00 afternoon', '', 'Lunch with Beto'), ('7:00 evening', 'Movie “Moon Pirates”', ''), ('10:00 night', '', 'Party at Finn’s')], ans='A tem 10:00 (soccer) e 7:00 (movie); B tem 2:00 (lunch with Beto) e 10:00 (party at Finn’s). Cada um pergunta “What do you do at…?”.'),
 miss=dict(title='a free Saturday', goal='Each group must chain at least four situations from the unit in one story: invite, plan, buy tickets or go to a party, share and react.',
  list=[('A', 'Friends: morning to afternoon', 'Talk about hobbies, invite a friend to play, plan a time and a place, and choose snacks.', 'Use “I’m into…”, “Do you want to…?” and “Let’s meet at…”.', 'Hey! What do you do in your free time?'), ('B', 'Friends: afternoon to evening', 'Buy two movie tickets, choose a time, order popcorn and say if you liked the movie.', 'Use “Two tickets for…”, “What time is the show?” and “Did you like it?”.', 'Hi! Two tickets for…'), ('C', 'Friends: night', 'Go to a party, offer to bring something, send photos by text and meet a new friend online.', 'Use “Can I bring…?”, “Send me the…” and “Where are you from?”.', 'Hi! Thanks for having me.')],
  model='“Do you want to play soccer?” → “Sure! Let’s meet at ten.” → “Two tickets for the seven o’clock show, please.” → “Can I bring snacks?” → “Send me the photos.”'),
 write=dict(task='Write a message to a friend with your plan for a free Saturday. Invite, plan, ask for something and say goodbye.', steps=['Greeting', 'Invitation', 'Plan (time and place)', 'Request and closing'],
  model='Hi Isla! **Do you want to** spend Saturday together? **Let’s meet** at ten in the park. After that, **two tickets for** the seven o’clock movie? **Send me the** photos later, please. See you!', check=['I greeted my friend.', 'I invited my friend.', 'I gave a time and a place.', 'I asked for something and said goodbye.']),
 fb=('Example: You invited, planned and solved a small problem with confidence.', 'Example: Put the strong stress on the important words in your plan.', 'Example: Tell the whole Saturday story in one minute without notes.'),
 exit=dict(tasks=[('❓', 'Build a question', 'Without notes: invite a friend to see a movie.', 'Do you want to see a movie?'), ('💬', 'Respond to a situation', 'A friend says: “Let’s meet at ten.” You agree.', 'Sounds good!'), ('⭐', 'Use a new expression', 'Say you have to leave a party politely.', 'I’d better go. Thanks for having me!')],
  hw=['Record a 60-second audio telling your free Saturday plan.', 'Write a short message inviting a friend to your plan.', 'Review three expressions from the unit and create your own examples.', 'Listen to the dialogue again and identify two expressions.'],
  next=['Do you want to…?', 'Let’s meet at…', 'Two tickets for…'], week=['Can I bring…?', 'Send me the…', 'Where are you from?'], unit=['Invite · plan · share · react']),
 ladder=[('A1', 'Saturday? Park! Soccer, please.', 'Suggest a plan with short phrases.'), ('A2', 'Do you want to play soccer on Saturday? Let’s meet at ten.', 'Invite and fix a time.'), ('B1', 'I thought we could play soccer in the morning and catch a movie afterwards, if you’re up for it.', 'Combine two plans.'), ('B2', 'How about we start with a game in the park and see where the day takes us from there?', 'Suggest a flexible plan.'), ('C1', 'I’d suggest keeping the day loose: a kickabout in the morning, then we can play the rest by ear.', 'Plan with nuance.'), ('C2', 'Let’s leave the afternoon open and let the day shape itself.', 'Express relaxed intent with style.')],
 err=[('You want play soccer?', 'Do you want to play soccer?'), ('Let’s to go.', 'Let’s go.'), ('Two ticket for the movie.', 'Two tickets for the movie.'), ('Can I to bring snacks?', 'Can I bring snacks?'), ('I better go.', 'I’d better go.'), ('Send to me the photos.', 'Send me the photos.'), ('Where you are from?', 'Where are you from?'), ('I have 20 years.', 'I’m 20.')],
 xq=['What would be your perfect Saturday?', 'Who do you invite first?', 'What do you bring to a party?', 'What movie do you want to see?', 'Which hobby do you want to try?', 'What do you text your friends?', 'What do you never share online?', 'What was your favorite class in this unit?'], tchr=None)


LESSON = build(S)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(LESSON['pages']), 'páginas')
