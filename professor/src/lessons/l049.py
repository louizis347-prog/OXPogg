#!/usr/bin/env python3
"""Aula 49 · Hobbies and interests (A1, 60 min). Gera data/v3/049.json."""
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


S = dict(n=49, k=1, topic='Hobbies and interests', title='Talking About Your Hobbies', pt='Conversar sobre hobbies e interesses', cast=['Paul', 'Isla'], roles=['Paul', 'Isla'], scene='park',
 sit='You sit on a park bench next to a stranger. You start a friendly chat and talk about what you like to do in your free time.',
 goal='By the end of the class you can start a small talk in a park, say what you like to do, ask about hobbies and suggest doing something together.',
 canDo=['Ask: What do you do in your free time?', 'Say what you like: I like to… / I’m into…', 'Say how often you do it', 'Invite someone to try your hobby'],
 success=['I ask about a hobby.', 'I say what I like to do.', 'I say how often.', 'I make a small invitation.'],
 think='What do people ask when they want to know you better? Do you ask about hobbies in Portuguese?',
 recall='Unit 6 and earlier: “I usually…” for routines. Ask: What do you usually do after work or school?',
 warm=[('How was your day?', 'Como foi o seu dia?', ['Pretty good!', 'A little tired.', 'Busy, but fine.']), ('What do you do on a free afternoon?', 'O que você faz em uma tarde livre?', ['I watch TV.', 'I go out.', 'I rest.']), ('Is there something you do just for fun?', 'Existe algo que você faz só por diversão?', ['Yes, I…', 'Not really.', 'I play…'])],
 ctitle='Life in the USA', cintro='Americans often use hobbies as small talk. It is an easy and safe topic with new people. Look and guess before you read.',
 cards=[('prop:book', 'Reading and crafts', 'Leitura e artesanato', 'Many public libraries have reading groups and craft classes.'), ('prop:camera', 'Photography', 'Fotografia', 'Photo walks and camera clubs are a popular way to meet people.'), ('obj:ball', 'Club and team sports', 'Clubes e esportes', 'Many towns have community leagues for adults.')],
 cqs=[('What is a good small-talk question with a new person?', 'Qual é uma boa pergunta para puxar conversa?', 'What do you do for fun?', 'You can ask: What do you do in your free time?', 'Asking about hobbies is friendly and not too personal.', 'Hobbies are a safe topic: they open the conversation without being too personal.'),
      ('Why do people join clubs?', 'Por que as pessoas entram em clubes?', 'To meet people.', 'They join clubs to learn something and meet new friends.', 'Clubs give people a regular activity and a group of friends who share an interest.', 'Clubs create a social routine around a shared interest, which makes it easier to build friendships as an adult.'),
      ('What happens after “I like to paint”?', 'O que acontece depois de “I like to paint”?', 'You ask: And you?', 'The other person usually asks a follow-up: Really? What do you paint?', 'A follow-up question shows interest and keeps the conversation going.', 'Native speakers rarely stop at one answer: they add a detail and return the question.')],
 compare='In Brazil people often talk about football, work or family first. In the USA, “What do you do for fun?” is also a very common opener. What is the first question you ask a new friend?',
 cans=['Q1: What do you do in your free time?', 'Q2: para conhecer pessoas e aprender algo.', 'Q3: And you? / Really? What do you…?'],
 p1=('What are they talking about?', 'Sobre o que eles estão conversando?', ['Their hobbies', 'Their jobs', 'The weather'], 0),
 p2=[('Isla’s hobby', 'paint', ['painting']), ('Paul’s hobby', 'play guitar', ['guitar']), ('How often Paul plays', 'every day', ['daily']), ('Day of the plan', 'Saturday', [])],
 dialog=[(0, 'Hi! Is this seat taken?', 'Oi! Este lugar está ocupado?'), (1, 'No, go ahead. I’m Isla.', 'Não, pode sentar. Eu sou a Isla.'), (0, 'I’m Paul. **What do you do in your free time?**', 'Eu sou o Paul. O que você faz no seu tempo livre?'),
  (1, '**I like to** paint. **I’m into** watercolors. And you?', 'Eu gosto de pintar. Eu curto aquarela. E você?'), (0, '**I like to** play guitar. I’m into folk music.', 'Eu gosto de tocar violão. Eu curto folk.'),
  (1, 'That sounds fun! **How often do you** play?', 'Parece divertido! Com que frequência você toca?'), (0, '**Every day**, after work. There’s a music club here.', 'Todo dia, depois do trabalho. Tem um clube de música aqui.'),
  (1, 'Really? **Do you want to** go together on Saturday?', 'Sério? Você quer ir junto no sábado?'), (0, 'Sure! See you at ten.', 'Claro! Nos vemos às dez.')],
 dqs=[('What does Isla like to do?', ['Paint', 'Play guitar', 'Run'], 0), ('What music is Paul into?', ['Jazz', 'Folk music', 'Rock'], 1), ('How often does Paul play?', ['Once a week', 'Every day', 'Never'], 1), ('What do they plan to do?', ['Go to the club on Saturday', 'Paint in the park', 'Have lunch'], 0)],
 retell=['Paul and Isla are…', 'Isla likes to…', 'Paul plays…', 'On Saturday, they…'], dans=['Paint (Isla) · folk music (Paul) · every day · the club on Saturday'],
 chunks=[('What do you do in your free time?', 'O que você faz no seu tempo livre?', 'Ask about someone’s hobbies.', 'neutral', 'Also: **What do you do for fun?**', True), ('I like to…', 'Eu gosto de…', 'Say an activity you enjoy.', 'neutral', 'Also: **I love to…**', True), ('I’m into…', 'Eu curto… / Sou fã de…', 'Say an interest: music, sports, art.', 'casual', 'Also: **I’m interested in…** (more formal)', True),
  ('How often do you…?', 'Com que frequência você…?', 'Ask how many times a week or month.', 'neutral', None, True), ('Every day / Once a week', 'Todo dia / Uma vez por semana', 'Say how often you do something.', 'neutral', None, False), ('That sounds fun!', 'Parece divertido!', 'React to what the other person says.', 'casual', 'Also: **That sounds great!**', False), ('Do you want to…?', 'Você quer…?', 'Invite someone to do something.', 'neutral', 'More polite: **Would you like to…?**', False)],
 fns=['Asking about hobbies', 'Saying what you like', 'Frequency', 'Reacting', 'Inviting'],
 disc=[('What do you do in your free time?', 'Asking about hobbies'), ('I’m into watercolors.', 'Saying what you like'), ('Twice a week.', 'Frequency'), ('That sounds fun!', 'Reacting'), ('Do you want to join us?', 'Inviting')],
 pats=[('Saying what you like', '**I like to** + verb  /  **I like** + noun', ['I like to paint.', 'I like to cook on Sundays.', 'I like music.'], True), ('Saying your interests', '**I’m into** + noun', ['I’m into folk music.', 'I’m into photography.', 'I’m into video games.'], True), ('Asking about frequency', '**How often do you** + verb?', ['How often do you play?', 'How often do you run?'], False), ('Answering about frequency', '**Every day** / **once a week** / **on Saturdays**', ['I paint every day.', 'I play soccer once a week.'], False)],
 swap=('I like to {verb} {when}.', 'Eu gosto de {verb} {when}.', [('verb', 'Activity', [('paint', 'pintar'), ('cook', 'cozinhar'), ('swim', 'nadar'), ('read', 'ler')]), ('when', 'When', [('every day', 'todos os dias'), ('on Saturdays', 'aos sábados'), ('after work', 'depois do trabalho')])]),
 reg=[['What do you do for fun?', 'What are your leisure activities?'], ['I’m into jazz.', 'I am interested in jazz.'], ['Wanna join?', 'Would you like to join us?'], ['Every day, pretty much.', 'I do it daily.']],
 pron=dict(focus='Sentence stress', tip='In English the important words are strong and the small words are weak: “I LIKE to PAINT”. This gives the sentence its natural rhythm.',
  items=[('I like to paint.', 'I LIKE to PAINT.', '/aɪ ˈlaɪk tə ˈpeɪnt/', 'oOoO'), ('I’m into watercolors.', 'I’m IN-to WA-ter-COL-ors.', '/aɪm ˈɪntə ˈwɔtərˌkʌlərz/', 'oOoOoOo'), ('What do you do in your free time?', 'What do you DO in your FREE TIME?', '/wʌt də ju ˈdu ɪn jər ˈfri ˌtaɪm/', 'oooOooOO')],
  id=[(['I like to paint.', 'I like to print.', 'I like to point.'], 0), (['I’m into jazz.', 'I’m into chess.', 'I’m into cats.'], 1)], own='Write a sentence with “I like to…” about your real hobby.', crit='Say it twice: first every word equal, then with strong and weak words. Which one sounds more natural?'),
 chal=([('mcq', '1. You want to know a stranger’s hobbies.', ['What do you do in your free time?', 'What you do hobbies?', 'Where is your hobby?'], 0, 'This is the natural small-talk question.'), ('mcq', '2. Someone says “I’m into photography.” You react.', ['That sounds fun!', 'I am a photography.', 'No, thanks.'], 0, 'React with interest first.'), ('mcq', '3. You want to ask how many times a week.', ['How often do you swim?', 'How many do you swim?', 'When often you swim?'], 0, 'How often do you + verb?'), ('mcq', '4. You paint every Sunday. What do you say?', ['I paint on Sundays.', 'I painting Sunday.', 'I am paint Sundays.'], 0, 'Use the base verb with on Sundays.')],
  [('gap', 'I ___ to cook on Sundays.', 'like', ['like', 'am', 'into'], 'I like to + verb.'), ('gap', 'I’m ___ folk music.', 'into', ['into', 'on', 'to'], 'I’m into + noun.'), ('swap', 'Say it with “I’m into”:', 'I like jazz.', ['I’m into jazz.', 'I’m into jazz'], 'I’m into jazz.', 'I’m into + noun is a casual way to say an interest.'), ('swap', 'Ask about frequency:', 'you / play / soccer', ['How often do you play soccer?', 'How often do you play soccer'], 'How often do you play soccer?', 'How often do you + verb?'), ('reply', 'Do you want to join the club on Saturday?', ['Sure! See you there.', 'I am Saturday.', 'Yes, club is.'], 0, 'A short, warm answer to an invitation.')]),
 chans=['1: What do you do in your free time? · 2: That sounds fun! · 3: How often do you swim? · 4: I paint on Sundays.', 'Gap: like · into · I’m into jazz. · How often do you play soccer? · Sure! See you there.'],
 role=dict(title='meet someone in the park', teacher='You are a friendly person on the next bench (change the plan during the scene!).', student='You are new in the park: talk about your real hobbies and invite the other person.',
  orders=['Talk about a sport you like', 'Talk about music or movies you like', 'Talk about something you do at home'], comp=['The other person has the same hobby: ask for details.', 'The other person doesn’t know the hobby: explain it simply.', 'You can’t go on the day they suggest: propose another day.', 'You didn’t understand: ask them to repeat.'],
  chunks=['What do you do in your free time?', 'I like to…', 'I’m into…', 'How often do you…?'], kw=['hobby', 'often', 'Saturday', 'together', 'club'], stretch=['Peça que o estudante convide e organize um encontro (dia, hora e lugar).']),
 lab=dict(rounds=[('Hobby small talk', 3, 'Ask your partner about free time. Answer with 2 hobbies.', 'What do you do…? / I like to…', False), ('How often?', 3, 'Ask how often your partner does each hobby.', 'How often do you…? / Once a week', False), ('Find a match', 3, 'Find one hobby you both like and invite your partner.', 'Me too! / Do you want to…?', False), ('Club day', 2, 'Whole group: each pair presents a new club idea.', 'We both like… so we want to start…', True)],
  gt='Hobby cards', at='Student A knows Isla’s week', atask='You know Isla’s paint and music. Ask about the rest.', bt='Student B knows Paul’s week', btask='You know Paul’s guitar and photos. Ask about the rest.',
  rows=[('Paint', 'Isla: Sundays', ''), ('Guitar', '', 'Paul: every day'), ('Photography', 'Isla: twice a month', ''), ('Chess club', '', 'Paul: on Fridays')], ans='A tem Paint (Isla: Sundays) e Photography (Isla: twice a month); B tem Guitar (Paul: every day) e Chess club (Paul: on Fridays). Cada um completa perguntando.'),
 miss=dict(title='make a new friend', goal='Each group must start a conversation, find a shared interest and plan something together.',
  list=[('A', 'New neighbors', 'Talk about your hobbies and find one thing you both like.', 'Use “I’m into…” and ask “How often…?”', 'Hi! What do you do in your free time?'), ('B', 'Club members', 'Invite a new person to join your hobby club on Saturday.', 'Use “Do you want to…?” and give a time.', 'Hi! I’m into…'), ('C', 'Friends at the park', 'Choose a new activity to try together this month.', 'Use “That sounds fun!” and “once a week”.', 'Let’s find something fun. I like to…')],
  model='“What do you do in your free time?” → “I’m into photography.” → “That sounds fun! How often do you go out?” → “Once a week. Do you want to come on Saturday?”'),
 write=dict(task='Write a short message to a new friend from the park. Say what you like to do and invite them.', steps=['Greeting', 'Your hobby', 'How often', 'Invitation'],
  model='Hi Paul! It was nice to meet you. **I like to paint** and **I’m into** watercolors. I paint **every Sunday** in the park. **Do you want to** come this Sunday? See you!', check=['I greeted my friend.', 'I said what I like to do.', 'I said how often.', 'I made an invitation.']),
 fb=('Example: You asked about hobbies and used “I’m into…”.', 'Example: Put the strong stress on the important words: I LIKE to PAINT.', 'Example: Talk about your hobby for one minute and invite someone.'),
 exit=dict(tasks=[('❓', 'Build a question', 'Without notes: ask about free time.', 'What do you do in your free time?'), ('💬', 'Respond to a situation', 'A new friend says: “I play guitar.” React and ask about frequency.', 'That sounds fun! How often do you play?'), ('⭐', 'Use a new expression', 'Say you like folk music.', 'I’m into folk music.')],
  hw=['Record a 45–60 second audio about your hobbies.', 'Write a short message inviting a friend to try your hobby.', 'Review three expressions from the class and create your own examples.', 'Listen to the dialogue again and identify two expressions.'],
  next=['I like to…', 'I’m into…', 'How often do you…?'], week=['What do you do in your free time?', 'That sounds fun!', 'Every day / Once a week'], unit=['Invite · plan · share · react']),
 ladder=[('A1', 'I like music. And you?', 'Name a hobby with short phrases.'), ('A2', 'I’m into painting. I paint every Sunday. Do you want to come?', 'Describe a hobby and invite.'), ('B1', 'I took up painting last year, and it really helps me relax after work.', 'Explain why you like it.'), ('B2', 'What I enjoy most is that it lets me switch off completely, whatever kind of week I’ve had.', 'Talk about motivation and effect.'), ('C1', 'I’d say it’s less a hobby than a way of keeping myself sane.', 'Use nuance and a personal view.'), ('C2', 'For me it has quietly become the thread that holds the week together.', 'Express subtle meaning with style.')],
 err=[('I have 25 years.', 'I’m 25.'), ('I like play guitar.', 'I like to play guitar.'), ('I’m into to music.', 'I’m into music.'), ('How many often do you run?', 'How often do you run?'), ('I like very much music.', 'I like music a lot.'), ('I play guitar all the days.', 'I play guitar every day.'), ('I am agree.', 'I agree. / Me too.'), ('Do you want go?', 'Do you want to go?')],
 xq=['What hobby would you like to try?', 'Did you have a hobby as a child?', 'Do you prefer hobbies alone or with people?', 'What is your friend’s hobby?', 'Is there a hobby club near you?', 'What do you do on rainy days?', 'How often do you listen to music?', 'What hobby is popular in your city?'], tchr=None)


LESSON = build(S)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(LESSON['pages']), 'páginas')
