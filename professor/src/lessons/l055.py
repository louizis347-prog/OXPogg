#!/usr/bin/env python3
"""Aula 55 · Making friends online (A1, 60 min). Gera data/v3/055.json."""
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


S = dict(n=55, k=7, topic='Making friends online', title='Making Friends Online', pt='Fazer amigos online com segurança', cast=['Jin', 'Kai'], roles=['Jin', 'Kai'], scene='bedroom', tod='night',
 sit='You meet a new player in an online game and talk by voice chat. You ask where he is from, what games he plays and you add him as a friend, safely.',
 goal='By the end of the class you can start a friendly chat with a new online friend, ask where he is from, talk about games, add him and keep personal information safe.',
 canDo=['Ask: Where are you from?', 'Ask: What games do you play?', 'Say: Add me / I’ll add you', 'Keep personal information safe'],
 success=['I ask where they are from.', 'I talk about games.', 'I ask to add them.', 'I stay safe online.'],
 think='Where do you meet new people online? What information do you never share?',
 recall='Last class: messages. Ask: Did you see…? Send me the… What does BTW mean?',
 warm=[('Do you play games online?', 'Você joga online?', ['Yes, every day.', 'Sometimes.', 'No, never.']), ('Where do you meet new people?', 'Onde você conhece pessoas novas?', ['At school.', 'Online.', 'At work.']), ('Do you have friends from other countries?', 'Você tem amigos de outros países?', ['Yes, one.', 'A few.', 'Not yet.'])],
 ctitle='Online friends and safety', cintro='Many people make friends online. In the USA, schools and websites teach simple safety rules. Look and guess before you read.',
 cards=[('obj:globe', 'Friends from everywhere', 'Amigos de todo lugar', 'Online games connect people from many countries, so “Where are you from?” is a natural first question.'), ('obj:key', 'Keep it private', 'Mantenha privado', 'Do not share your password, address, school or phone number with people you only know online.'), ('prop:computer', 'Block and report', 'Bloquear e denunciar', 'Most games and apps let you block a person or report bad behavior.')],
 cqs=[('Why is “Where are you from?” a good first question?', 'Por que “Where are you from?” é uma boa primeira pergunta?', 'It is easy and friendly.', 'It is easy and starts a talk about places.', 'It is a friendly question that opens a talk about places and culture.', 'It invites a story without being too personal, and it shows curiosity about the other person.'),
      ('What information should you not share?', 'Quais informações você não deve compartilhar?', 'Password. Address.', 'Your password, address and phone number.', 'Passwords, your home address, school and phone number should stay private.', 'Anything that lets a stranger find you or enter your accounts should stay private, even if the person seems nice.'),
      ('What can you do if someone is rude online?', 'O que fazer se alguém for rude online?', 'Block them.', 'Block the person and tell an adult or a friend.', 'You can block, report and leave the conversation without answering.', 'Blocking and reporting are normal tools. You owe nothing to someone who makes you uncomfortable.')],
 compare='In Brazil many people also make friends in games and social apps. The advice is the same everywhere: use a username, keep private data private and trust your feeling. What rule do you follow online?',
 cans=['Q1: fácil, amigável e abre assunto.', 'Q2: senha, endereço e telefone.', 'Q3: bloquear, denunciar e sair da conversa.'],
 p1=('What are they doing?', 'O que eles estão fazendo?', ['Meeting online', 'Shopping', 'Cooking'], 0),
 p2=[('Jin is from', 'Busan', []), ('Kai is from', 'Hawaii', []), ('Jin plays', 'soccer', ['racing']), ('Kai’s username', 'KaiPlays', [])],
 dialog=[(0, 'Hey! Nice game! I’m Jin.', 'Ei! Bom jogo! Eu sou o Jin.'), (1, 'Thanks! I’m Kai. **Where are you from?**', 'Valeu! Eu sou o Kai. De onde você é?'), (0, 'I’m from Busan, in Korea. And you?', 'Sou de Busan, na Coreia. E você?'),
  (1, 'I’m from Hawaii! **What games do you play?**', 'Sou do Havaí! Que jogos você joga?'), (0, 'Mostly soccer and racing games. Every night!', 'Principalmente futebol e corrida. Toda noite!'), (1, 'Cool! **Add me** as a friend. My username is KaiPlays.', 'Legal! Me adicione como amigo. Meu usuário é KaiPlays.'),
  (0, 'Okay! I’ll send you a request now.', 'Ok! Vou mandar um pedido agora.'), (1, 'Great! But I never share my address online.', 'Ótimo! Mas eu nunca divulgo meu endereço online.'), (0, 'Me neither. **Safety first!**', 'Eu também não. Segurança em primeiro lugar!'), (1, '**See you online!**', 'Até já, online!')],
 dqs=[('Where is Jin from?', ['Busan', 'Texas', 'Hawaii'], 0), ('Where is Kai from?', ['Seoul', 'Hawaii', 'Paris'], 1), ('What does Jin play?', ['Soccer and racing games', 'Only chess', 'No games'], 0), ('What does Kai never share?', ['His address', 'His games', 'His username'], 0)],
 retell=['Jin and Kai meet…', 'Jin is from…', 'Kai asks…', 'They never share…'], dans=['Busan · Hawaii · soccer and racing games · address'],
 chunks=[('Where are you from?', 'De onde você é?', 'Ask about a person’s country or city.', 'neutral', 'Also: **Where do you live?**', True), ('What games do you play?', 'Que jogos você joga?', 'Ask about interests.', 'neutral', 'Also: **What do you like to play?**', True), ('Add me.', 'Me adicione.', 'Ask someone to be your online friend.', 'casual', 'Polite: **Can I add you?**', True), ('Safety first!', 'Segurança em primeiro lugar!', 'A rule about staying safe online.', 'neutral', None, True),
  ('My username is…', 'Meu usuário é…', 'Give your game or app name.', 'neutral', None, False), ('I’ll send a request.', 'Vou mandar um pedido.', 'Say what you do next.', 'neutral', None, False), ('See you online!', 'Até já, online!', 'End a chat with a friend.', 'casual', None, False)],
 fns=['Asking about origin', 'Asking about interests', 'Adding a friend', 'Staying safe', 'Ending the chat'],
 disc=[('Where are you from?', 'Asking about origin'), ('What games do you play?', 'Asking about interests'), ('Add me, please.', 'Adding a friend'), ('Never share your password.', 'Staying safe'), ('See you online!', 'Ending the chat')],
 pats=[('Asking where from', '**Where are you from?** — **I’m from** + place', ['Where are you from?', 'I’m from Busan.', 'I’m from Hawaii.'], True), ('Asking about interests', '**What** + noun + **do you** + verb?', ['What games do you play?', 'What music do you like?', 'What sports do you watch?'], True), ('Asking to add', '**Add me** / **Can I add you?**', ['Add me, please.', 'Can I add you?'], False), ('Staying safe', '**I never share** + noun', ['I never share my address.', 'I never share my password.'], False)],
 swap=('I’m from {place}. I play {game} {when}.', 'Eu sou de {place}. Eu jogo {game} {when}.', [('place', 'Place', [('Busan', 'Busan'), ('Hawaii', 'Havaí'), ('Brazil', 'Brasil'), ('Texas', 'Texas')]), ('game', 'Game', [('soccer', 'futebol'), ('racing games', 'jogos de corrida'), ('chess', 'xadrez')]), ('when', 'When', [('every night', 'toda noite'), ('on weekends', 'nos fins de semana'), ('after school', 'depois da escola')])]),
 reg=[['Add me!', 'May I add you as a friend?'], ['What games are you into?', 'Which video games do you enjoy?'], ['I’m from Brazil.', 'I come from Brazil.'], ['See you online!', 'I will see you online soon.']],
 pron=dict(focus='Linking consonant to vowel', tip='A final consonant links to the next vowel: “Where are you from?” sounds like “Wherar you from?”, and “Add me” like “Adme”. It makes speech flow.',
  items=[('Where are you from?', 'Wher-ar-YOU from?', '/wɛrˈɑr ju ˈfrʌm/', 'oooOo'), ('What games do you play?', 'What GAMES do-ya PLAY?', '/wʌt ˈgeɪmz dʒə ˈpleɪ/', 'oOooO'), ('I’m from Hawaii.', 'I’m from ha-WAI-ee.', '/aɪm frəm həˈwaɪi/', 'ooOo')],
  id=[(['Where are you from?', 'Where you are from?', 'Where do you from?'], 0), (['What games do you play?', 'What game you play?', 'What games you playing?'], 0)], own='Write a question with “Where…?” or “What…?” for a new online friend.', crit='Say it twice. Did “Where are you” flow as one smooth group?'),
 chal=([('mcq', '1. You meet a new player. You want to know his country.', ['Where are you from?', 'From where you?', 'Where is you from?'], 0, 'Where are you from?'), ('mcq', '2. You want to know the games he likes.', ['What games do you play?', 'What do you games play?', 'What game you are play?'], 0, 'What + noun + do you + verb?'), ('mcq', '3. You want to be friends in the game.', ['Add me, please!', 'Add me you!', 'I add friends me.'], 0, 'Add me, please.'), ('mcq', '4. A stranger asks for your address.', ['Sorry, I never share my address.', 'Sure, it’s…', 'Where is yours?'], 0, 'Safety first: say no politely.')],
  [('gap', 'I’m ___ Hawaii.', 'from', ['from', 'of', 'in'], 'I’m from + place.'), ('gap', 'What games do you ___?', 'play', ['play', 'plays', 'playing'], 'After do you, use the base verb.'), ('swap', 'Say it politely with “Can I”:', 'Add me.', ['Can I add you?', 'Can I add you, please?'], 'Can I add you?', 'Can I + base verb is polite.'), ('swap', 'Say a safety rule:', 'I / never / share / password', ['I never share my password.', 'I never share my password'], 'I never share my password.', 'I never + verb + noun.'), ('reply', 'Where are you from?', ['I’m from Brazil. And you?', 'I from Brazil are.', 'Brazil is me.'], 0, 'Answer and return the question.')]),
 chans=['1: Where are you from? · 2: What games do you play? · 3: Add me, please! · 4: Sorry, I never share my address.', 'Gap: from · play · Can I add you? · I never share my password. · I’m from Brazil. And you?'],
 role=dict(title='meet a new gamer', teacher='You are a new online friend (change the plan during the scene!).', student='You are a player: ask where the person is from, talk about games and add them safely.',
  orders=['Meet a player in a racing game', 'Meet a player in a puzzle app', 'Meet a player in a team game'], comp=['The person asks for your address: refuse politely.', 'The person plays a different game: ask about it.', 'You can’t hear well: ask the person to repeat.', 'The person is rude: block and say goodbye.'],
  chunks=['Where are you from?', 'What games do you play?', 'Add me.', 'Safety first!'], kw=['from', 'games', 'username', 'friend', 'safe'], stretch=['Peça que o estudante crie 3 regras de segurança em inglês.']),
 lab=dict(rounds=[('Where are you from?', 3, 'Ask where your partner is from and say where you are from.', 'Where are you from? / I’m from…', False), ('What do you play?', 3, 'Ask about games, apps or sports. Share one favorite.', 'What games do you play?', False), ('Add and stay safe', 3, 'Ask to add your partner and give a username. Say one safety rule.', 'Add me. / I never share…', False), ('Online rules', 2, 'Whole group: each pair shares the best safety rule.', 'Our rule is… because…', True)],
  gt='Player profiles', at='Student A has profile 1', atask='You know the first two players’ countries. Ask about the rest.', bt='Student B has profile 2', btask='You know the last two players’ countries. Ask about the rest.',
  rows=[('Mia', 'Brazil', ''), ('Omar', '', 'Egypt'), ('Sara', 'Spain', ''), ('Raj', '', 'India')], ans='A tem Mia (Brazil) e Sara (Spain); B tem Omar (Egypt) e Raj (India). Cada um pergunta “Where is… from?”.'),
 miss=dict(title='new friend online', goal='Each group must meet a new online friend, share interests and stay safe.',
  list=[('A', 'New gamers', 'Say where you are from and talk about games.', 'Use “Where are you from?” and “What games…?”', 'Hey! Where are you from?'), ('B', 'Teammates', 'Add each other as friends and share usernames.', 'Use “Add me” and give a username.', 'Nice game! Add me!'), ('C', 'Friends with rules', 'A stranger asks for private information. Say no and end the chat.', 'Use “I never share…” and “Safety first!”', 'Sorry, I never share…')],
  model='“Where are you from?” → “I’m from Busan. What games do you play?” → “Soccer! Add me.” → “I never share my address.” → “Safety first!”'),
 write=dict(task='Write a short chat message to a new online friend. Say where you are from, ask about games and add them.', steps=['Greeting', 'Where you are from', 'Question about games', 'Add me'],
  model='Hi Kai! Nice game! **I’m from** Busan. **What games do you play?** **Add me**: my username is JinPlays. **See you online!**', check=['I greeted my friend.', 'I said where I am from.', 'I asked about games.', 'I asked to add them without private data.']),
 fb=('Example: You asked simple questions and kept the chat going.', 'Example: Link “Where are you from?” so it flows.', 'Example: Meet a new person online and keep a one-minute chat without notes.'),
 exit=dict(tasks=[('❓', 'Build a question', 'Without notes: ask where a new friend is from.', 'Where are you from?'), ('💬', 'Respond to a situation', 'A stranger asks for your home address.', 'Sorry, I never share my address.'), ('⭐', 'Use a new expression', 'Ask a new friend if you can add them.', 'Can I add you?')],
  hw=['Record a 45–60 second audio introducing yourself to a new online friend.', 'Write three safety rules in English.', 'Review three expressions from the class and create your own examples.', 'Listen to the dialogue again and identify two expressions.'],
  next=['Where are you from?', 'What games do you play?', 'Add me.'], week=['Safety first!', 'My username is…', 'See you online!'], unit=['Invite · plan · share · react']),
 ladder=[('A1', 'I’m from Brazil. I like games.', 'Introduce yourself with short phrases.'), ('A2', 'I’m from Brazil. What games do you play? Add me, please.', 'Ask and connect.'), ('B1', 'I’m from Brazil and I’ve been playing online for years. Do you want to team up sometime?', 'Describe experience and suggest a plan.'), ('B2', 'I’ve met some great people through games, though I’m careful about what I share.', 'Talk about experience and caution.'), ('C1', 'I’m happy to chat, but I keep my personal details private until I know someone better.', 'Set boundaries with tact.'), ('C2', 'I tend to let a friendship earn its trust before any real-life details come into it.', 'Reflect on trust with style.')],
 err=[('I’m from of Brazil.', 'I’m from Brazil.'), ('Where you are from?', 'Where are you from?'), ('What games you play?', 'What games do you play?'), ('I have 20 years.', 'I’m 20.'), ('I add you?', 'Can I add you?'), ('I no share my address.', 'I never share my address.'), ('I play since two years.', 'I’ve played for two years. / I started two years ago.'), ('See you in the net.', 'See you online!')],
 xq=['Do you have a username? What kind?', 'What game would you teach a friend?', 'Who is your best online friend?', 'What do you do if someone is rude?', 'Do you play with people from other countries?', 'What time do you usually play?', 'Do you prefer voice chat or text?', 'What is a safe username?'], tchr=None)


LESSON = build(S)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(LESSON['pages']), 'páginas')
