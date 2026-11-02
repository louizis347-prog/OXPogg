#!/usr/bin/env python3
"""Aula 54 · Messages and social media (A1, 60 min). Gera data/v3/054.json."""
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


S = dict(n=54, k=6, topic='Messages and social media', title='Messages and Social Media', pt='Mensagens, redes sociais e abreviações', cast=['Zara', 'Elif'], roles=['Zara', 'Elif'], scene='bedroom', tod='dusk',
 sit='Two friends sit in a bedroom with their phones. They share a funny post, ask for a link and a photo, and use short text abbreviations.',
 goal='By the end of the class you can ask if someone saw a post, ask a friend to send you something, understand common text abbreviations and write a short message.',
 canDo=['Ask: Did you see…?', 'Ask politely: Send me the…, please', 'Understand LOL, BTW, TTYL', 'Write a short, friendly message'],
 success=['I ask about a post.', 'I ask for a link or photo.', 'I use one abbreviation.', 'I write a clear message.'],
 think='Which abbreviations do you use when you text in Portuguese? Do they exist in English too?',
 recall='Last class: a party. Ask: What do you say when you leave a party? (I’d better go.)',
 warm=[('How often do you text your friends?', 'Com que frequência você manda mensagem para os amigos?', ['All day.', 'A few times a day.', 'Not much.']), ('Which app do you use the most?', 'Qual aplicativo você mais usa?', ['WhatsApp.', 'Instagram.', 'Messages.']), ('Do you prefer calling or texting?', 'Você prefere ligar ou mandar mensagem?', ['Texting.', 'Calling.', 'It depends.'])],
 ctitle='Texting in the USA', cintro='Short messages and abbreviations are everywhere in American texting. They save time and show a casual tone. Look and guess before you read.',
 cards=[('obj:phone', 'Abbreviations', 'Abreviações', 'LOL means “laughing out loud”. BTW means “by the way”. TTYL means “talk to you later”.'), ('obj:envelope', 'Group chats', 'Grupos de conversa', 'Friends and families use group chats to share plans, photos and links.'), ('prop:computer', 'Tone and CAPS', 'Tom e letras maiúsculas', 'Writing in ALL CAPS often feels like shouting. Emoji help show a friendly tone.')],
 cqs=[('What does BTW mean?', 'O que significa BTW?', 'By the way.', 'BTW means “by the way”. You add a new idea.', 'BTW introduces a side comment or a new topic in a casual way.', 'It softens a change of subject: you slip in new information without making it the main point.'),
      ('Why do people use abbreviations?', 'Por que as pessoas usam abreviações?', 'They are fast.', 'Texts are faster and sound friendly.', 'Abbreviations save time and give a casual, friendly tone.', 'They mark an informal register, so they fit friends and family but not a job application.'),
      ('When is it better not to use abbreviations?', 'Quando é melhor não usar abreviações?', 'In an email to a boss.', 'In a school or work email.', 'In formal emails, applications and messages to people you do not know well.', 'In formal contexts, full words show respect and avoid confusion, and abbreviations can look careless.')],
 compare='In Brazil people use “kkk”, “vc” and “blz”. In English people write LOL, U or BTW, and many also use emoji. Which short forms do you use?',
 cans=['Q1: BTW = by the way.', 'Q2: são rápidas e informais.', 'Q3: em e-mails formais ou de trabalho.'],
 p1=('What are they doing?', 'O que eles estão fazendo?', ['Looking at phones and chatting', 'Cooking dinner', 'Studying for a test'], 0),
 p2=[('What the dog wears', 'hat', []), ('What Zara wants', 'link', []), ('Day of the plan', 'Friday', []), ('Photos from the…', 'trip', [])],
 dialog=[(0, '**Did you see** Maya’s post? It’s so funny!', 'Você viu o post da Maya? É muito engraçado!'), (1, 'No! **Send me the** link, please.', 'Não! Me manda o link, por favor.'), (0, 'I just sent it. Check your phone.', 'Acabei de mandar. Olhe seu celular.'),
  (1, 'Got it! **LOL**, her dog is wearing a hat.', 'Peguei! Kkk, o cachorro dela está de chapéu.'), (0, '**BTW**, are you coming on Friday?', 'A propósito, você vem na sexta?'), (1, 'Yes! I’ll text you the time.', 'Sim! Eu te mando o horário por mensagem.'),
  (0, 'Cool. Can you **send me the** pictures from the trip?', 'Legal. Você pode me mandar as fotos da viagem?'), (1, 'Sure! Give me a minute.', 'Claro! Me dá um minuto.'), (0, 'No rush. **TTYL!**', 'Sem pressa. Falo com você mais tarde!')],
 dqs=[('What did Zara see?', ['A funny post', 'A movie', 'A song'], 0), ('What does Elif want?', ['A photo', 'The link', 'A message'], 1), ('What is the dog wearing?', ['A hat', 'A coat', 'Glasses'], 0), ('What does TTYL mean?', ['Talk to you later', 'Thank you, love', 'Time to your life'], 0)],
 retell=['Zara asks if Elif saw…', 'Elif wants…', 'They plan to meet on…', 'At the end Zara says…'], dans=['A funny post · the link · a dog with a hat · Talk to you later'],
 chunks=[('Did you see…?', 'Você viu…?', 'Ask about a post, photo or news.', 'casual', 'Also: **Have you seen…?**', True), ('Send me the…', 'Me manda o/a…', 'Ask a friend for a link, photo or file.', 'casual', 'More polite: **Could you send me the…?**', True), ('BTW', 'A propósito', 'Add a new idea (by the way).', 'casual', None, True), ('LOL', 'Kkk (rindo)', 'Show something is funny (laughing out loud).', 'casual', None, True),
  ('Got it!', 'Entendi! / Recebi!', 'Say you received or understood.', 'casual', None, False), ('Give me a minute.', 'Me dá um minuto.', 'Ask for a little time.', 'neutral', None, False), ('TTYL', 'Falo com você mais tarde', 'End a chat (talk to you later).', 'casual', None, False)],
 fns=['Asking about a post', 'Asking for something', 'Adding an idea', 'Showing a reaction', 'Ending the chat'],
 disc=[('Did you see my photo?', 'Asking about a post'), ('Send me the address.', 'Asking for something'), ('BTW, I’m late.', 'Adding an idea'), ('LOL, that’s funny!', 'Showing a reaction'), ('TTYL!', 'Ending the chat')],
 pats=[('Asking about news', '**Did you see** + noun?', ['Did you see the video?', 'Did you see my message?', 'Did you see that photo?'], True), ('Asking a friend for something', '**Send me the** + noun (+ please)', ['Send me the link.', 'Send me the photos, please.', 'Send me the address.'], True), ('Abbreviations', '**LOL** · **BTW** · **TTYL** · **IDK**', ['LOL, that’s funny!', 'BTW, are you free?', 'TTYL!'], False), ('Promising', '**I’ll text you** + noun', ['I’ll text you the time.', 'I’ll text you later.'], False)],
 swap=('Send me the {thing} {when}, please.', 'Me manda {thing} {when}, por favor.', [('thing', 'What', [('link', 'o link'), ('photos', 'as fotos'), ('address', 'o endereço'), ('video', 'o vídeo')]), ('when', 'When', [('now', 'agora'), ('tonight', 'hoje à noite'), ('later', 'mais tarde')])]),
 reg=[['LOL, that’s so funny!', 'That is very amusing.'], ['BTW, I’m late.', 'By the way, I will be late.'], ['Send me the link.', 'Could you please send me the link?'], ['TTYL!', 'I will speak with you later.']],
 pron=dict(focus='Reduction: “did you”', tip='In fast speech “did you” sounds like “didja”: /dɪdʒə/. Link the /d/ and /j/ sounds and keep the stress on the verb: “Didja SEE it?”.',
  items=[('Did you see it?', 'DIDja SEE it?', '/ˈdɪdʒə ˈsi ɪt/', 'ooOo'), ('Send me the link.', 'SEND me the LINK.', '/ˈsɛnd mi ðə ˈlɪŋk/', 'OooO'), ('Did you get my text?', 'DIDja GET my TEXT?', '/ˈdɪdʒə ˈgɛt maɪ ˈtɛkst/', 'ooOoO')],
  id=[(['Did you see it?', 'Did you sit?', 'Did you seat?'], 0), (['Send me the link.', 'Send me the lake.', 'Send me the lick.'], 0)], own='Write a sentence with “Did you…?” about something online.', crit='Say it twice. Did “did you” sound like one word, “didja”?'),
 chal=([('mcq', '1. You want to know if a friend saw a video.', ['Did you see the video?', 'You saw video?', 'Do you saw the video?'], 0, 'Did you + base verb.'), ('mcq', '2. You need a link from a friend.', ['Send me the link, please.', 'Me send the link.', 'I want link send.'], 0, 'Send me the + noun, please.'), ('mcq', '3. Your friend says something funny. You react.', ['LOL!', 'OMG no.', 'TTYL?'], 0, 'LOL shows that something is funny.'), ('mcq', '4. You want to change the subject in a text.', ['BTW, are you free tomorrow?', 'ByWay free tomorrow?', 'BTW free you?'], 0, 'BTW = by the way, then a normal sentence.')],
  [('gap', 'Did you ___ my message?', 'see', ['see', 'saw', 'seen'], 'After Did you, use the base verb.'), ('gap', 'Send ___ the photos, please.', 'me', ['me', 'I', 'my'], 'Send me + noun.'), ('swap', 'Ask politely with “Could you”:', 'Send me the link.', ['Could you send me the link?', 'Could you send me the link, please?'], 'Could you send me the link?', 'Could you + base verb is more polite.'), ('swap', 'Write it in full words:', 'BTW', ['By the way', 'by the way'], 'By the way', 'BTW means “by the way”.'), ('reply', 'Can you send me the pictures?', ['Sure! Give me a minute.', 'Pictures me yes.', 'I am sending the minute.'], 0, 'Accept and say when.')]),
 chans=['1: Did you see the video? · 2: Send me the link, please. · 3: LOL! · 4: BTW, are you free tomorrow?', 'Gap: see · me · Could you send me the link? · By the way · Sure! Give me a minute.'],
 role=dict(title='chat with a friend', teacher='You are a friend who texts a lot (change the plan during the scene!).', student='You are a friend: ask about a post, ask for a link and plan something by message.',
  orders=['Ask a friend about a funny video', 'Ask a friend to send photos from a trip', 'Ask a friend for the address of an event'], comp=['Your friend didn’t see the post: tell them what happened.', 'Your friend sends the wrong link: ask for the right one.', 'Your friend uses an abbreviation you don’t know: ask what it means.', 'Your friend doesn’t answer: write a polite follow-up.'],
  chunks=['Did you see…?', 'Send me the…', 'BTW…', 'LOL'], kw=['post', 'link', 'photo', 'funny', 'later'], stretch=['Peça que o estudante escreva uma conversa curta no chat e depois a leia em voz alta.']),
 lab=dict(rounds=[('Did you see…?', 3, 'Ask your partner about something you saw online. Your partner reacts.', 'Did you see…? / LOL!', False), ('Send me the…', 3, 'Ask for a link, a photo or an address. Your partner answers.', 'Send me the… / Give me a minute.', False), ('Decode the text', 3, 'Read short chat lines. Explain the abbreviations.', 'BTW means… / TTYL means…', False), ('Best message', 2, 'Whole group: each pair shares the best short message.', 'Our message is… because…', True)],
  gt='Chat history', at='Student A has the first half', atask='You know the first two messages. Ask your partner about the other two.', bt='Student B has the second half', btask='You know the last two messages. Ask your partner about the first two.',
  rows=[('Zara: “Did you see the post?”', 'Elif: “No! Send me the link.”', ''), ('Zara: “Check your phone.”', '', 'Elif: “Got it! LOL.”'), ('Zara: “BTW, Friday?”', 'Elif: “Yes! I’ll text you.”', ''), ('Zara: “TTYL!”', '', 'Elif: “Bye!”')], ans='A tem as linhas 1 e 3 do chat; B tem as linhas 2 e 4. Cada um pergunta “What did she say?” para completar.'),
 miss=dict(title='group chat day', goal='Each group must share something online, ask for a link or photo and make a plan by chat.',
  list=[('A', 'Friends in a group chat', 'Share a funny post and ask who saw it.', 'Use “Did you see…?” and “LOL”.', 'Did you see…'), ('B', 'Trip organizers', 'Ask a friend to send photos and the address.', 'Use “Send me the…” and “Give me a minute”.', 'Hey! Send me the…'), ('C', 'Weekend planners', 'Plan a meeting by chat and end the conversation.', 'Use “BTW” once and “TTYL” at the end.', 'Hi! BTW, are you free…')],
  model='“Did you see Maya’s post?” → “No! Send me the link.” → “LOL, her dog is wearing a hat.” → “BTW, Friday?” → “TTYL!”'),
 write=dict(task='Write 4 short text messages to a friend: ask about a post, ask for a photo and make a plan.', steps=['Greeting', 'Did you see…?', 'Send me the…', 'Plan and goodbye'],
  model='Hey Elif! **Did you see** the video I sent? LOL. **Send me the** photos from your trip, please. **BTW**, are you free on Friday? **TTYL!**', check=['I greeted my friend.', 'I asked about something they saw.', 'I asked for something.', 'I used one abbreviation.']),
 fb=('Example: You asked for what you needed in a friendly way.', 'Example: Say “didja” smoothly in “Did you see…?”.', 'Example: Write and say a short chat with three abbreviations.'),
 exit=dict(tasks=[('❓', 'Build a question', 'Without notes: ask if a friend saw your message.', 'Did you see my message?'), ('💬', 'Respond to a situation', 'A friend asks for the photos from the trip.', 'Sure! Give me a minute.'), ('⭐', 'Use a new expression', 'Write: by the way, are you free tomorrow? Use an abbreviation.', 'BTW, are you free tomorrow?')],
  hw=['Record a 45–60 second audio reading a short chat.', 'Write three short messages with LOL, BTW and TTYL.', 'Review three expressions from the class and create your own examples.', 'Listen to the dialogue again and identify two expressions.'],
  next=['Did you see…?', 'Send me the…', 'BTW'], week=['LOL', 'Got it!', 'TTYL'], unit=['Invite · plan · share · react']),
 ladder=[('A1', 'Hi! LOL! Send photo, please.', 'Send short messages with simple words.'), ('A2', 'Did you see my post? Send me the photos from the trip, please.', 'Ask and request in a message.'), ('B1', 'I saw your post earlier and loved it. Could you send me the photos when you have a minute?', 'Write a clear, polite request.'), ('B2', 'I meant to reply sooner, but I was out all day. Could you send those photos over whenever you’re free?', 'Apologize and ask with nuance.'), ('C1', 'Sorry for the late reply, things got a bit hectic; would you mind forwarding those photos when you get a chance?', 'Keep a warm and polished tone.'), ('C2', 'Forgive the radio silence; I’d be grateful if you could send those photos my way at your leisure.', 'Use register and elegance.')],
 err=[('Did you saw my message?', 'Did you see my message?'), ('Send to me the link.', 'Send me the link.'), ('I send you the photo yesterday.', 'I sent you the photo yesterday.'), ('Lol only in capitals.', 'LOL or lol: both are used.'), ('Me send the photos.', 'Send me the photos.'), ('BTW = Be The Way.', 'BTW = by the way.'), ('Did you saw?', 'Did you see it?'), ('I will text you later. (muito formal em chat)', 'I’ll text you later.')],
 xq=['Do you use emoji? Which one?', 'Do you send voice messages?', 'What was the last funny post you saw?', 'Do you have a group chat?', 'Do you answer messages right away?', 'What abbreviation do you use the most?', 'Do you prefer photos or videos?', 'Who do you text the most?'], tchr=None)


LESSON = build(S)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(LESSON['pages']), 'páginas')
