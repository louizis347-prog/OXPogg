#!/usr/bin/env python3
"""Aula 51 · At the cinema (A1, 60 min). Gera data/v3/051.json."""
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


S = dict(n=51, k=3, topic='At the cinema', title='At the Movie Theater', pt='No cinema: ingressos, sessão e opinião', cast=['Will', 'Lola'], roles=['Will', 'Lola'], scene='cinema', tod='dusk',
 sit='You go to a movie theater in the USA. You buy tickets at the box office, choose a show time and share your opinion about a movie.',
 goal='By the end of the class you can buy movie tickets, ask for the show time, order a snack and say if you liked a movie.',
 canDo=['Buy tickets: Two tickets for…', 'Ask: What time is the show?', 'Ask and answer: Did you like it?', 'Say a simple opinion: It was funny / boring'],
 success=['I ask for tickets.', 'I ask about the time.', 'I order a snack.', 'I give my opinion.'],
 think='How do you buy a movie ticket in Brazil? Do you say the name of the movie first?',
 recall='Last class: weekend plans. Ask: What are you doing on Saturday? Do you want to go to the movies?',
 warm=[('What kind of movies do you like?', 'Que tipo de filme você gosta?', ['Comedies.', 'Action movies.', 'I like dramas.']), ('When did you last go to the cinema?', 'Quando foi a última vez que você foi ao cinema?', ['Last week.', 'A month ago.', 'I don’t remember.']), ('Do you prefer cinema or streaming?', 'Você prefere cinema ou streaming?', ['Cinema!', 'Streaming.', 'Both.'])],
 ctitle='Movie theaters in the USA', cintro='Going to the movies in the USA has a routine: tickets, previews, popcorn and quiet. Look and guess before you read.',
 cards=[('obj:envelope', 'Tickets and show times', 'Ingressos e horários', 'Each movie has several shows a day. You choose a time when you buy the ticket.'), ('prop:cake', 'Popcorn and snacks', 'Pipoca e lanches', 'Popcorn, soda and candy are sold at the concession stand and people bring them into the theater.'), ('prop:clock', 'Previews first', 'Trailers primeiro', 'Before the movie starts there are previews, also called trailers. The movie begins a little later than the ticket time.')],
 cqs=[('What happens before the movie starts?', 'O que acontece antes do filme começar?', 'Previews. Trailers.', 'There are previews of other movies first.', 'Theaters show previews, so the movie starts about 15 minutes after the time on the ticket.', 'Previews and ads play first, so people can arrive a little late and not miss the main film.'),
      ('How do you buy tickets?', 'Como se compram os ingressos?', 'At the box office.', 'At the box office or online, with an app.', 'Many people buy online and choose their seats in advance.', 'Online booking with seat choice is very common, which saves time at busy theaters.'),
      ('What is a good way to ask about a movie?', 'Qual é uma boa forma de perguntar sobre um filme?', 'Did you like it?', 'Did you like the movie? What did you think?', 'Opinions are part of the conversation: “What did you think?” invites a short review.', 'People usually give an opinion and a reason: “I loved it, the music was great.” It keeps the chat natural.')],
 compare='In Brazil many people also buy tickets online and trailers play first. In the USA, people often talk about the movie right after it ends. Do you talk about a movie after you leave the theater?',
 cans=['Q1: previews/trailers.', 'Q2: bilheteria (box office) ou online.', 'Q3: Did you like it? What did you think?'],
 p1=('Where are they?', 'Onde eles estão?', ['At a movie theater', 'At a restaurant', 'At a station'], 0),
 p2=[('Movie', 'Moon Pirates', ['moon']), ('Show time chosen', 'seven', ['7']), ('Price', 'twenty dollars', ['$20', '20']), ('Snack', 'popcorn', [])],
 dialog=[(1, 'Next, please! How can I help you?', 'Próximo, por favor! Como posso ajudar?'), (0, 'Hi! **What time is the show** for “Moon Pirates”?', 'Oi! Que horas é a sessão de “Moon Pirates”?'), (1, 'There’s one at seven and one at nine thirty.', 'Tem uma às sete e outra às nove e meia.'),
  (0, '**Two tickets for** the seven o’clock show, please.', 'Dois ingressos para a sessão das sete, por favor.'), (1, 'Sure. That’s twenty dollars. Seats in the middle okay?', 'Claro. São vinte dólares. Lugares no meio, tudo bem?'), (0, 'Perfect. And one small popcorn, please.', 'Perfeito. E uma pipoca pequena, por favor.'),
  (1, 'Here you go! I saw this movie yesterday.', 'Aqui está! Eu vi esse filme ontem.'), (0, 'Oh, nice! **Did you like it?**', 'Ah, que legal! Você gostou?'), (1, 'Yes! **It was** really funny.', 'Sim! Foi muito engraçado.'), (0, 'Great! Thanks a lot.', 'Ótimo! Muito obrigado.')],
 dqs=[('What movie do they want to see?', ['Moon Pirates', 'Star Kitchen', 'Rainy Days'], 0), ('What time do they choose?', ['Seven', 'Nine thirty', 'Noon'], 0), ('How much are the tickets?', ['Ten dollars', 'Twenty dollars', 'Thirty dollars'], 1), ('What is the opinion of the movie?', ['It was funny', 'It was boring', 'It was scary'], 0)],
 retell=['A man buys…', 'He chooses the show at…', 'He also gets…', 'The worker says the movie was…'], dans=['Moon Pirates · seven · twenty dollars · popcorn · funny'],
 chunks=[('Two tickets for…', 'Dois ingressos para…', 'Ask for tickets at the box office.', 'neutral', 'More polite: **Could I get two tickets for…?**', True), ('What time is the show?', 'Que horas é a sessão?', 'Ask the show time.', 'neutral', 'Also: **When does it start?**', True), ('Did you like it?', 'Você gostou?', 'Ask for an opinion.', 'neutral', 'Also: **What did you think?**', True), ('It was funny / great / boring.', 'Foi engraçado / ótimo / chato.', 'Give a simple opinion.', 'neutral', None, True),
  ('Here you go.', 'Aqui está.', 'Give or receive something.', 'neutral', None, False), ('Seats in the middle', 'Lugares no meio', 'Choose where to sit.', 'neutral', None, False), ('Enjoy the movie!', 'Aproveite o filme!', 'The staff says it before you go.', 'neutral', None, False)],
 fns=['Buying tickets', 'Asking about time', 'Asking for opinion', 'Giving opinion', 'Staff phrases'],
 disc=[('Two tickets for the eight o’clock show.', 'Buying tickets'), ('What time is the show?', 'Asking about time'), ('Did you like it?', 'Asking for opinion'), ('It was really boring.', 'Giving opinion'), ('Enjoy the movie!', 'Staff phrases')],
 pats=[('Buying tickets', '**Two tickets for** + movie', ['Two tickets for “Moon Pirates.”', 'Three tickets for the seven o’clock show.', 'One ticket for the comedy.'], True), ('Asking about time', '**What time is** + the show / the movie?', ['What time is the show?', 'What time is the next movie?'], True), ('Asking for opinion', '**Did you like** + it / the movie?', ['Did you like it?', 'Did you like the music?'], False), ('Giving opinion', '**It was** + adjective', ['It was funny.', 'It was too long.'], False)],
 swap=('Two tickets for the {time} show of the {kind}, please.', 'Dois ingressos para a sessão das {time} da {kind}, por favor.', [('time', 'Time', [('seven', 'sete'), ('eight thirty', 'oito e meia'), ('ten', 'dez')]), ('kind', 'Movie', [('comedy', 'comédia'), ('action movie', 'filme de ação'), ('cartoon', 'desenho animado'), ('horror movie', 'filme de terror')])]),
 reg=[['Two for “Moon Pirates.”', 'I’d like to purchase two tickets for “Moon Pirates.”'], ['It was great!', 'I found the film very enjoyable.'], ['What time’s the next one?', 'At what time is the next screening?'], ['Meh, it was okay.', 'I thought it was average.']],
 pron=dict(focus='Linking and “-ed” endings', tip='Past verbs end in /t/, /d/ or /ɪd/: “liked” sounds like “likt”, “loved” like “lovd”. Do not add an extra vowel: “li-ked” is wrong.',
  items=[('I liked it.', 'I LIKT it.', '/aɪ laɪkt ɪt/', 'oOo'), ('We watched a movie.', 'We WATCHT a MOvie.', '/wi wɑtʃt ə ˈmuvi/', 'oOoOo'), ('She loved the music.', 'She LOVD the MU-sic.', '/ʃi lʌvd ðə ˈmjuzɪk/', 'oOoOo')],
  id=[(['I liked it.', 'I like it.', 'I lick it.'], 0), (['We watched a movie.', 'We watch a movie.', 'We wash a movie.'], 0)], own='Write a sentence with one -ed verb about a movie you saw.', crit='Say it twice. Did you pronounce “liked” as one sound, without “-id”?'),
 chal=([('mcq', '1. You are at the box office. You want two tickets.', ['Two tickets for “Moon Pirates,” please.', 'I want two ticket moon.', 'Give me tickets two.'], 0, 'Two tickets for + movie, with please.'), ('mcq', '2. You want to know when the movie starts.', ['What time is the show?', 'Where is time of show?', 'How many is the show?'], 0, 'What time is the show?'), ('mcq', '3. A friend left the theater. You ask for an opinion.', ['Did you like it?', 'You are liking?', 'Do you liked it?'], 0, 'Did you like it? (past, with like in base form).'), ('mcq', '4. The movie was not good. You say it politely.', ['It was a bit boring.', 'It is boring was.', 'I boring.'], 0, 'It was + adjective.')],
  [('gap', 'What ___ is the show?', 'time', ['time', 'hour', 'clock'], 'What time is the show?'), ('gap', 'Did you ___ it?', 'like', ['like', 'liked', 'likes'], 'After Did you, use the base verb.'), ('swap', 'Give an opinion about the music:', 'music / great', ['The music was great.', 'It was great.', 'The music was great'], 'The music was great.', 'Noun + was + adjective.'), ('swap', 'Ask for three tickets for the nine o’clock show:', 'tickets / three / nine', ['Three tickets for the nine o’clock show, please.', 'Three tickets for the nine o’clock show'], 'Three tickets for the nine o’clock show, please.', 'Number + tickets for + time.'), ('reply', 'Did you like it?', ['Yes! It was great.', 'Yes, I am it.', 'It liked me.'], 0, 'Answer with yes + opinion.')]),
 chans=['1: Two tickets for “Moon Pirates,” please. · 2: What time is the show? · 3: Did you like it? · 4: It was a bit boring.', 'Gap: time · like · The music was great. · Three tickets for the nine o’clock show, please. · Yes! It was great.'],
 role=dict(title='at the box office', teacher='You are the box office worker (change the plan during the scene!).', student='You are the customer: buy tickets, ask the time and ask about the movie.',
  orders=['Two tickets for a comedy at seven', 'Three tickets for an action movie and a large popcorn', 'One ticket for a cartoon and a drink'], comp=['The show you want is sold out: choose another time.', 'The price is higher than you expected: ask about a discount.', 'You don’t hear the time: ask the worker to repeat.', 'Your friend asks what you thought about the movie: answer.'],
  chunks=['Two tickets for…', 'What time is the show?', 'Did you like it?', 'It was…'], kw=['tickets', 'time', 'popcorn', 'funny', 'seats'], stretch=['Peça que o estudante descreva o filme em duas frases e dê uma nota de 1 a 5.']),
 lab=dict(rounds=[('Buy tickets', 3, 'One is the customer, the other is the worker. Buy tickets for a movie.', 'Two tickets for… / What time is the show?', False), ('Snacks', 3, 'Order tickets and a snack. Ask the price.', 'And a small popcorn, please. / How much is it?', False), ('After the movie', 3, 'Talk about a movie you saw. Ask and answer.', 'Did you like it? / It was…', False), ('Movie night', 2, 'Whole group: each pair recommends one movie.', 'I recommend… because it was…', True)],
  gt='Movie schedule', at='Student A has the cinema board', atask='You know the times for “Moon Pirates” and “Cooking Wars”. Ask about the rest.', bt='Student B has the cinema board', btask='You know the times for “Rainy Days” and “Robot Zoo”. Ask about the rest.',
  rows=[('Moon Pirates', '7:00 and 9:30', ''), ('Rainy Days', '', '6:15 and 8:45'), ('Cooking Wars', '5:30 and 8:00', ''), ('Robot Zoo', '', '4:00 and 6:30')], ans='A tem Moon Pirates e Cooking Wars; B tem Rainy Days e Robot Zoo. Cada um pergunta “What time is…?” para completar.'),
 miss=dict(title='movie night', goal='Each group must buy tickets, choose a time and share an opinion about a movie.',
  list=[('A', 'Friends', 'Buy four tickets and choose the best show time.', 'Use “Two tickets for…” (or four) and ask “What time is…?”', 'Hi! Four tickets for…'), ('B', 'Couple', 'Buy tickets, order popcorn and ask which movie people liked.', 'Ask “Did you like it?” to the worker.', 'Hello! Two tickets for…'), ('C', 'Classmates', 'After the movie, share opinions and give a score.', 'Use “It was…” and give a reason.', 'So, did you like it?')],
  model='“Two tickets for Moon Pirates, please.” → “There’s a show at seven.” → “Seven is perfect.” → “Did you like it?” → “Yes! It was really funny.”'),
 write=dict(task='Write a short review (3–4 lines) of a movie you saw. Say what it was and whether you liked it.', steps=['Name of the movie', 'When you saw it', 'Your opinion', 'Recommendation'],
  model='Last night I saw “Moon Pirates” with a friend. **It was** really funny and the music was great. **I liked it** a lot! I recommend it for a fun night.', check=['I said the name of the movie.', 'I said when I saw it.', 'I gave an opinion with “It was…”.', 'I made a recommendation.']),
 fb=('Example: You asked for tickets and the time with confidence.', 'Example: Say “liked” as /laɪkt/, with one sound at the end.', 'Example: Recommend a movie and give two reasons, without notes.'),
 exit=dict(tasks=[('❓', 'Build a question', 'Without notes: ask the show time.', 'What time is the show?'), ('💬', 'Respond to a situation', 'A friend asks: “Did you like it?” You loved it.', 'Yes! It was great.'), ('⭐', 'Use a new expression', 'Ask for two tickets for a comedy.', 'Two tickets for the comedy, please.')],
  hw=['Record a 45–60 second audio buying tickets at a movie theater.', 'Write a short review of a movie you like.', 'Review three expressions from the class and create your own examples.', 'Listen to the dialogue again and identify two expressions.'],
  next=['Two tickets for…', 'What time is the show?', 'Did you like it?'], week=['It was funny / boring.', 'Enjoy the movie!', 'Here you go.'], unit=['Invite · plan · share · react']),
 ladder=[('A1', 'Two tickets, please. Seven o’clock.', 'Buy tickets with short phrases.'), ('A2', 'Two tickets for the seven o’clock show, please. Is it in English?', 'Buy tickets and ask a detail.'), ('B1', 'I’d like two seats for tonight’s seven o’clock showing, preferably in the middle.', 'Choose seats and time.'), ('B2', 'Could you tell me whether there are any seats left for the late show? We’d prefer not to sit up front.', 'Ask indirectly and state preferences.'), ('C1', 'I was hoping to catch the late showing; would there happen to be a couple of seats together?', 'Request with tact and detail.'), ('C2', 'If there’s anything at all together towards the back, we’d be delighted to take it.', 'Phrase a request with polish.')],
 err=[('I want two tickets of Moon Pirates.', 'Two tickets for “Moon Pirates,” please.'), ('What hour is the show?', 'What time is the show?'), ('Did you liked it?', 'Did you like it?'), ('It was very fun.', 'It was really fun. / It was funny.'), ('The movie is funny yesterday.', 'The movie was funny.'), ('I saw the movie yesterday night.', 'I saw the movie last night.'), ('How much cost?', 'How much is it?'), ('li-kid (duas sílabas)', 'liked = /laɪkt/ (uma sílaba)')],
 xq=['What is your favorite movie?', 'Do you eat popcorn at the cinema?', 'Do you like previews?', 'What time do you prefer to go?', 'Who do you go to the movies with?', 'What movie do you want to see?', 'Did you cry at a movie?', 'Do you prefer comedy or action?'], tchr=None)


LESSON = build(S)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(LESSON['pages']), 'páginas')
