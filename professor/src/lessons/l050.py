#!/usr/bin/env python3
"""Aula 50 · Weekend plans and sports (A1, 60 min). Gera data/v3/050.json."""
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


S = dict(n=50, k=2, topic='Weekend plans and sports', title='Weekend Plans and Sports', pt='Planos de fim de semana e esportes', cast=['Beto', 'Jonas'], roles=['Beto', 'Jonas'], scene='stadium',
 sit='You and a friend are at a stadium. You invite him to a game on Saturday and plan what to do before it starts.',
 goal='By the end of the class you can invite a friend to a game, say which team you like, plan a time and a place, and suggest a game to play.',
 canDo=['Invite: Do you want to…?', 'Ask and answer: Who’s your team?', 'Suggest an activity: Let’s play…', 'Agree on a time and a place'],
 success=['I invite my friend.', 'I say my team.', 'I suggest a plan.', 'I agree on a time.'],
 think='What do you say when you invite a friend to a game? Is it the same in Portuguese?',
 recall='Last class: hobbies. Ask: What are you into? How often do you do it?',
 warm=[('What are you doing this weekend?', 'O que você vai fazer neste fim de semana?', ['Nothing special.', 'I’m going out.', 'I’m resting.']), ('Do you play any sport?', 'Você pratica algum esporte?', ['Yes, I play…', 'Not really.', 'I walk a lot.']), ('Do you have a favorite team?', 'Você tem um time favorito?', ['Yes, it’s…', 'No, I don’t.', 'My family’s team.'])],
 ctitle='Sports in the USA', cintro='Sports are a big part of weekends in the USA. Fans meet, eat and talk before the game even starts. Look and guess before you read.',
 cards=[('flag:us', 'Tailgating', 'Festa no estacionamento antes do jogo', 'Fans cook and eat in the parking lot before a game. This is called tailgating.'), ('obj:ball', 'Soccer, football, baseball', 'Soccer, futebol americano e beisebol', 'In the USA, “football” means American football. Our “futebol” is called “soccer”.'), ('prop:pizza', 'Game-day food', 'Comida de dia de jogo', 'Hot dogs, burgers and snacks are common at games.')],
 cqs=[('What is tailgating?', 'O que é tailgating?', 'A party before a game.', 'Fans eat and talk in the parking lot before the game.', 'Tailgating is a social tradition: people grill food and hang out near their cars before a game.', 'Tailgating turns the game into a community event: the food and the company are part of the day.'),
      ('What is the difference between “soccer” and “football” in the USA?', 'Qual a diferença entre “soccer” e “football” nos EUA?', 'Soccer: the ball with feet.', 'Soccer is our “futebol”. Football is a different sport.', 'American “football” is played with an oval ball and a lot of tackling, so the other sport is called “soccer”.', 'The word “football” belongs to a different sport in the USA, so Americans use “soccer” for the game the rest of the world calls football.'),
      ('How do people show they are fans?', 'Como as pessoas mostram que são torcedoras?', 'They wear a team shirt.', 'They wear team colors and say “Go, team!”.', 'Fans wear jerseys and caps and cheer with the crowd.', 'Wearing team colors is a way of belonging; strangers often start conversations about the team.')],
 compare='In Brazil people also talk a lot about their team and often watch the game with friends. What do you usually do before a game?',
 cans=['Q1: festa e comida no estacionamento antes do jogo.', 'Q2: soccer = nosso futebol; football = futebol americano.', 'Q3: camisa do time e “Go, team!”.'],
 p1=('What are they planning?', 'O que eles estão planejando?', ['Going to a game', 'Going to school', 'Buying a car'], 0),
 p2=[('Day', 'Saturday', []), ('Team', 'Tigers', []), ('Meeting time', 'noon', ['12']), ('Food to bring', 'hot dogs', ['hot dog'])],
 dialog=[(0, 'Hey, Jonas! **Do you want to** go to the game on Saturday?', 'Ei, Jonas! Você quer ir ao jogo no sábado?'), (1, 'Yes! **Who’s your team?**', 'Sim! Qual é o seu time?'), (0, 'The Tigers! **Let’s meet** at noon in the parking lot.', 'Os Tigers! Vamos nos encontrar ao meio-dia no estacionamento.'),
  (1, 'Good idea. I’ll bring the hot dogs.', 'Boa ideia. Eu levo os cachorros-quentes.'), (0, 'Perfect! I’ll bring chairs and a ball.', 'Perfeito! Eu levo cadeiras e uma bola.'), (1, 'Great! **Let’s play** catch before the game.', 'Ótimo! Vamos jogar bola antes do jogo.'),
  (0, 'Sounds good! **Do you want to** sit together inside?', 'Boa! Você quer sentar junto lá dentro?'), (1, 'Sure! **Go, Tigers!**', 'Claro! Vamos, Tigers!')],
 dqs=[('What day is the game?', ['Friday', 'Saturday', 'Sunday'], 1), ('What is Beto’s team?', ['The Tigers', 'The Bears', 'The Lions'], 0), ('Who brings the hot dogs?', ['Beto', 'Jonas', 'Nobody'], 1), ('What do they do before the game?', ['Play catch', 'Watch TV', 'Go shopping'], 0)],
 retell=['Beto invites Jonas to…', 'They meet at…', 'Jonas brings…', 'Before the game, they…'], dans=['Saturday · the Tigers · Jonas brings hot dogs · they play catch'],
 chunks=[('Do you want to…?', 'Você quer…?', 'Invite someone to do something.', 'neutral', 'More polite: **Would you like to…?**', True), ('Who’s your team?', 'Qual é o seu time?', 'Ask about a favorite team.', 'casual', 'Also: **Who do you root for?**', True), ('Let’s play…', 'Vamos jogar…', 'Suggest a game or sport.', 'casual', None, True), ('Let’s meet at…', 'Vamos nos encontrar às/em…', 'Fix a time or a place.', 'neutral', 'Also: **Let’s meet up at…**', True),
  ('I’ll bring…', 'Eu levo…', 'Offer to bring food or things.', 'casual', None, False), ('Sounds good!', 'Combinado! / Boa!', 'Accept a plan.', 'casual', 'Also: **Sounds great!**', False), ('Go, team!', 'Vamos, time!', 'Cheer for your team.', 'casual', None, False)],
 fns=['Inviting', 'Asking about teams', 'Suggesting', 'Fixing time and place', 'Offering'],
 disc=[('Do you want to watch the game?', 'Inviting'), ('Who’s your team?', 'Asking about teams'), ('Let’s play basketball.', 'Suggesting'), ('Let’s meet at six.', 'Fixing time and place'), ('I’ll bring the snacks.', 'Offering')],
 pats=[('Inviting', '**Do you want to** + verb?', ['Do you want to go to the game?', 'Do you want to play soccer?', 'Do you want to sit with us?'], True), ('Suggesting', '**Let’s** + verb', ['Let’s play catch.', 'Let’s meet at noon.', 'Let’s go!'], True), ('Asking about a team', '**Who’s your** + noun?', ['Who’s your team?', 'Who’s your favorite player?'], False), ('Offering', '**I’ll bring** + noun', ['I’ll bring the chairs.', 'I’ll bring water.'], False)],
 swap=('Do you want to {do} on {day}?', 'Você quer {do} no {day}?', [('do', 'Activity', [('play soccer', 'jogar futebol'), ('watch the game', 'assistir ao jogo'), ('go for a run', 'correr'), ('play tennis', 'jogar tênis')]), ('day', 'Day', [('Saturday', 'sábado'), ('Sunday', 'domingo'), ('Friday night', 'sexta à noite')])]),
 reg=[['Wanna go to the game?', 'Would you like to attend the game with me?'], ['Sounds good!', 'That works for me.'], ['Let’s meet at noon.', 'I suggest we meet at noon.'], ['Who’s your team?', 'Which team do you support?']],
 pron=dict(focus='Reductions', tip='In fast speech, “want to” often sounds like “wanna” and “let us” becomes “let’s”. You do not need to say “wanna” — but you should understand it.',
  items=[('Do you want to go?', 'D’ya WAN-na GO?', '/dʒə ˈwɑnə ˈɡoʊ/', 'oOoO'), ('Let’s play catch.', 'Let’s PLAY CATCH.', '/lɛts ˈpleɪ ˈkætʃ/', 'oOO'), ('What are you doing on Saturday?', 'Whaddaya DO-ing on SAT-ur-day?', '/ˈwʌdəjə ˈduɪŋ ɑn ˈsætərdeɪ/', 'oooOoooOo')],
  id=[(['Do you want to play?', 'Do you want to pay?', 'Do you want to stay?'], 0), (['Let’s go to the game.', 'Let’s go to the gym.', 'Let’s go to the lake.'], 0)], own='Write a question with “Do you want to…?” about a plan you really have.', crit='Say it slowly, then fast with “wanna”. Can your partner understand both?'),
 chal=([('mcq', '1. You invite a friend to play soccer.', ['Do you want to play soccer?', 'You want play soccer?', 'Do you want playing soccer?'], 0, 'Do you want to + verb?'), ('mcq', '2. You want to know your friend’s favorite team.', ['Who’s your team?', 'What is you team?', 'Where your team?'], 0, 'Who’s your team? is the usual question.'), ('mcq', '3. You suggest a game before the match.', ['Let’s play catch!', 'Let’s to play catch!', 'We play catch let!'], 0, 'Let’s + base verb.'), ('mcq', '4. Your friend says “Let’s meet at noon.” You agree.', ['Sounds good!', 'I am noon.', 'Meet me not.'], 0, 'Sounds good! accepts a plan.')],
  [('gap', 'Do you ___ to go to the game?', 'want', ['want', 'wants', 'like'], 'Do you want to + verb?'), ('gap', 'Let’s ___ at six.', 'meet', ['meet', 'meeting', 'met'], 'Let’s + base verb.'), ('swap', 'Suggest the plan with “Let’s”:', 'We play tennis.', ['Let’s play tennis.', 'Let’s play tennis'], 'Let’s play tennis.', 'Let’s + base verb makes a suggestion.'), ('swap', 'Offer to bring something:', 'water', ['I’ll bring water.', 'I will bring water.', 'I’ll bring the water.'], 'I’ll bring water.', 'I’ll bring + noun.'), ('reply', 'Do you want to go to the game on Sunday?', ['Sure! What time?', 'Game is Sunday go.', 'I am the game.'], 0, 'Accept and ask for the detail.')]),
 chans=['1: Do you want to play soccer? · 2: Who’s your team? · 3: Let’s play catch! · 4: Sounds good!', 'Gap: want · meet · Let’s play tennis. · I’ll bring water. · Sure! What time?'],
 role=dict(title='plan a game day', teacher='You are a friend who loves sports (change the plan during the scene!).', student='You are the friend: invite, choose a team and organize the day.',
  orders=['Invite a friend to a soccer game', 'Invite a friend to play basketball in the park', 'Invite a friend to watch the game at home'], comp=['Your friend is busy on that day: suggest another day.', 'Your friend supports the other team: joke about it kindly.', 'Your friend asks what to bring: answer.', 'The place is far: agree where to meet.'],
  chunks=['Do you want to…?', 'Who’s your team?', 'Let’s play…', 'Let’s meet at…'], kw=['game', 'team', 'noon', 'bring', 'Saturday'], stretch=['Peça que o estudante organize um fim de semana completo com 3 atividades.']),
 lab=dict(rounds=[('Invite and answer', 3, 'Invite your partner to a sport. Your partner accepts or says no.', 'Do you want to…? / Sorry, I can’t.', False), ('Teams and fans', 3, 'Ask about favorite teams and say why you like them.', 'Who’s your team? / They are…', False), ('Plan the day', 3, 'Choose a day, a time, a place and who brings what.', 'Let’s meet at… / I’ll bring…', False), ('Best plan', 2, 'Whole group: each pair shares its weekend plan.', 'We decided to… because…', True)],
  gt='Weekend schedule', at='Student A has Beto’s week', atask='You know Beto’s Saturday and Sunday plans. Ask about Jonas.', bt='Student B has Jonas’s week', btask='You know Jonas’s Friday and Saturday plans. Ask about Beto.',
  rows=[('Friday night', 'Beto: movie with friends', ''), ('Saturday morning', '', 'Jonas: soccer practice'), ('Saturday afternoon', 'Beto: the Tigers game', ''), ('Sunday', '', 'Jonas: barbecue at home')], ans='A tem Friday night e Saturday afternoon do Beto; B tem Saturday morning e Sunday do Jonas. Cada um pergunta para completar.'),
 miss=dict(title='plan a game day', goal='Each group must invite, choose a team, agree on a time and plan what to bring.',
  list=[('A', 'Friends', 'Plan a Saturday soccer game in the park.', 'Use “Do you want to…?” and “Let’s meet at…”', 'Hey! Do you want to…'), ('B', 'Fans', 'Plan how to watch the big game together.', 'Ask “Who’s your team?” and use “I’ll bring…”', 'Hi! Who’s your team?'), ('C', 'Classmates', 'Choose a sport for a class day and give each person a job.', 'Use “Let’s play…” and ask one question.', 'Let’s play something!')],
  model='“Do you want to play soccer on Saturday?” → “Sure! Let’s meet at ten.” → “I’ll bring the ball.” → “Sounds good!”'),
 write=dict(task='Write a short text message to invite a friend to a game this weekend.', steps=['Greeting', 'Invitation', 'Time and place', 'Closing'],
  model='Hi Jonas! **Do you want to** watch the game on Saturday? **Let’s meet** at noon at the stadium. **I’ll bring** the snacks. **Go, Tigers!**', check=['I greeted my friend.', 'I invited him with “Do you want to…?”.', 'I gave a time and a place.', 'I closed with a friendly phrase.']),
 fb=('Example: You invited your partner clearly and agreed on a time.', 'Example: Say “Do you want to” smoothly, like “d’ya wanna”.', 'Example: Plan a whole weekend with three activities, without notes.'),
 exit=dict(tasks=[('❓', 'Build a question', 'Without notes: ask about a friend’s team.', 'Who’s your team?'), ('💬', 'Respond to a situation', 'A friend says: “Let’s meet at noon.” Agree.', 'Sounds good!'), ('⭐', 'Use a new expression', 'Suggest playing tennis.', 'Let’s play tennis.')],
  hw=['Record a 45–60 second audio inviting a friend to a sport.', 'Write a short message with your weekend plan.', 'Review three expressions from the class and create your own examples.', 'Listen to the dialogue again and identify two expressions.'],
  next=['Do you want to…?', 'Let’s play…', 'Who’s your team?'], week=['Let’s meet at…', 'I’ll bring…', 'Sounds good!'], unit=['Invite · plan · share · react']),
 ladder=[('A1', 'Soccer on Saturday? Yes, please!', 'Accept a plan with short phrases.'), ('A2', 'Do you want to play soccer on Saturday? Let’s meet at ten.', 'Invite and fix a time.'), ('B1', 'I was thinking of watching the game at my place. Would you be up for it?', 'Make a flexible plan.'), ('B2', 'If you’re free on Saturday, we could catch the game together and grab something after.', 'Suggest a plan with options.'), ('C1', 'I wouldn’t mind catching the game on Saturday, if you happen to be around.', 'Invite with a soft tone.'), ('C2', 'It would be a shame to let the weekend slip by without us seeing that match.', 'Persuade with subtle humor.')],
 err=[('You want play soccer?', 'Do you want to play soccer?'), ('Let’s to go.', 'Let’s go.'), ('I want you go with me.', 'I want you to go with me. / Do you want to come?'), ('I am fan of Tigers.', 'I’m a Tigers fan.'), ('What time we meet?', 'What time do we meet?'), ('I bring the food.', 'I’ll bring the food.'), ('Where is your team?', 'Who’s your team?'), ('Football is like in Brazil.', 'In the USA, soccer is our “futebol”.')],
 xq=['What sport do you like to watch?', 'Have you ever been to a stadium?', 'What do you eat during a game?', 'Do you play any team sport?', 'Who do you watch games with?', 'What is a perfect Saturday for you?', 'Which sport is popular in your city?', 'Do you wear your team’s shirt?'], tchr=None)


LESSON = build(S)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(LESSON['pages']), 'páginas')
