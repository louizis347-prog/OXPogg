#!/usr/bin/env python3
"""Aula 52 · Music and concerts (A1, 60 min). Gera data/v3/052.json."""
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


S = dict(n=52, k=4, topic='Music and concerts', title='Music and Live Shows', pt='Música e shows ao vivo', cast=['Hana', 'Carlos'], roles=['Hana', 'Carlos'], scene='concert', tod='night',
 sit='You arrive at a concert and talk to a stranger in line. You ask who is playing, share the music you love and ask if he has been to other shows.',
 goal='By the end of the class you can talk about music you love, ask who is playing, ask about past experiences and make small talk at a concert.',
 canDo=['Ask: Who’s playing?', 'Say what you love: I love… / I’m a big fan of…', 'Ask: Have you ever been to…?', 'Answer with: Yes, twice / No, never'],
 success=['I ask who is playing.', 'I say what music I love.', 'I ask about a past experience.', 'I keep the small talk going.'],
 think='What do you say to a stranger at a show? Do you talk about the band or about something else?',
 recall='Last class: the movie theater. Ask: What movie did you see last? Did you like it?',
 warm=[('What music do you listen to?', 'Que música você escuta?', ['Pop.', 'Rock and samba.', 'A little of everything.']), ('Do you play an instrument?', 'Você toca algum instrumento?', ['Yes, the…', 'No, but I sing.', 'Not yet.']), ('Do you like live music?', 'Você gosta de música ao vivo?', ['Yes, a lot!', 'Sometimes.', 'I prefer headphones.'])],
 ctitle='Live music in the USA', cintro='Live music is a big part of social life in the USA, from small bars to big festivals. Look and guess before you read.',
 cards=[('obj:bag', 'Bag rules', 'Regras para bolsas', 'Many concert venues limit bag size, and some only allow clear bags. Check the rules before you go.'), ('obj:phone', 'Lights up', 'Luzes para o alto', 'At slow songs, fans often lift their phone lights and sway to the music.'), ('tod:night', 'The encore', 'O bis', 'After the last song, the crowd claps and cheers. The band comes back for one or two more songs: the encore.')],
 cqs=[('What is an encore?', 'O que é um encore?', 'One more song.', 'The band plays one or two more songs after the show.', 'After the main set, the crowd cheers until the band returns for an encore.', 'The encore is a shared ritual: the audience calls the band back, and artists often save a favorite song for it.'),
      ('How do you protect your ears at a loud show?', 'Como proteger os ouvidos em um show alto?', 'Use earplugs.', 'You can wear earplugs. They lower the noise.', 'Many fans wear earplugs, which lower the volume but keep the music clear.', 'Earplugs made for music reduce the volume without ruining the sound, and many regular concertgoers carry a pair.'),
      ('What is good manners at a show?', 'O que é educação em um show?', 'Do not push people.', 'Do not push and do not block the view.', 'Keep your phone down during songs if people are behind you, and respect personal space.', 'In a crowd, respecting space and sightlines matters more than anything: it keeps the experience good for everyone.')],
 compare='In Brazil crowds often sing every word and dance together. In the USA fans also sing along, and they often wait for the encore. Is there a custom at shows where you live?',
 cans=['Q1: bis, músicas extras depois do show.', 'Q2: protetores de ouvido (earplugs).', 'Q3: não empurrar nem bloquear a visão.'],
 p1=('Where are they?', 'Onde eles estão?', ['At a concert', 'At a bank', 'At a bus stop'], 0),
 p2=[('First band', 'Blue Rivers', ['blue']), ('Main band time', 'nine', ['9']), ('Hana’s first show?', 'first show', ['first']), ('Carlos gives her', 'earplugs', ['extra pair'])],
 dialog=[(0, 'Hey! **Who’s playing** first tonight?', 'Ei! Quem toca primeiro hoje?'), (1, 'The Blue Rivers. The main band comes on at nine.', 'Os Blue Rivers. A banda principal entra às nove.'), (0, 'Cool! **I love** the main band. **I’m a big fan of** their drummer.', 'Legal! Eu amo a banda principal. Sou muito fã do baterista deles.'),
  (1, 'Me too! **Have you ever been to** one of their shows?', 'Eu também! Você já foi a algum show deles?'), (0, 'No, this is **my first show**. And you?', 'Não, este é o meu primeiro show. E você?'), (1, 'Three times! **It gets** very loud. **Bring earplugs.**', 'Três vezes! Fica muito alto. Leve protetores de ouvido.'),
  (0, 'Oh no, I forgot them.', 'Ah não, eu esqueci.'), (1, 'No problem. I have an extra pair. Take these.', 'Sem problema. Tenho um par extra. Pegue.'), (0, 'Thank you so much! You’re a lifesaver.', 'Muito obrigada! Você me salvou.')],
 dqs=[('Who plays first?', ['The Blue Rivers', 'The main band', 'Nobody'], 0), ('What time does the main band start?', ['Seven', 'Nine', 'Eleven'], 1), ('Has Hana been to their shows?', ['Yes, twice', 'No, it’s her first', 'Yes, three times'], 1), ('What does Carlos give her?', ['A ticket', 'Earplugs', 'A T-shirt'], 1)],
 retell=['Hana asks…', 'The main band plays at…', 'It is Hana’s…', 'Carlos gives her…'], dans=['The Blue Rivers · nine · her first show · earplugs'],
 chunks=[('Who’s playing?', 'Quem vai tocar?', 'Ask about the band or artist.', 'neutral', 'Also: **Who’s on tonight?**', True), ('I love…', 'Eu amo…', 'Say music or a song you love.', 'neutral', 'Stronger: **I’m obsessed with…**', True), ('I’m a big fan of…', 'Sou muito fã de…', 'Say you really like a band or artist.', 'neutral', 'Short: **I’m a fan of…**', True), ('Have you ever been to…?', 'Você já foi a…?', 'Ask about a past experience.', 'neutral', 'Also: **Have you been to…before?**', True),
  ('It gets loud.', 'Fica alto.', 'Say a place becomes noisy.', 'neutral', None, False), ('Bring earplugs.', 'Leve protetores de ouvido.', 'Give simple advice.', 'neutral', None, False), ('My first show', 'Meu primeiro show', 'Say it is your first time.', 'neutral', None, False)],
 fns=['Asking who plays', 'Saying you love music', 'Asking about experience', 'Giving advice', 'Sharing a first time'],
 disc=[('Who’s playing on Friday?', 'Asking who plays'), ('I love this song.', 'Saying you love music'), ('Have you ever seen them live?', 'Asking about experience'), ('Bring a jacket.', 'Giving advice'), ('This is my first festival.', 'Sharing a first time')],
 pats=[('Asking who plays', '**Who’s playing** + when/where?', ['Who’s playing tonight?', 'Who’s playing at the festival?', 'Who’s playing next?'], True), ('Saying you love something', '**I love** + noun  /  **I’m a big fan of** + noun', ['I love this song.', 'I’m a big fan of jazz.', 'I love dancing.'], True), ('Experience questions', '**Have you ever been to** + place?', ['Have you ever been to a concert?', 'Have you ever been to a festival?'], False), ('Answering', '**Yes, twice.** / **No, never.** / **Once.**', ['Yes, three times!', 'No, never.', 'Once, last year.'], False)],
 swap=('I love {music}. Have you ever been to {event}?', 'Eu amo {music}. Você já foi a {event}?', [('music', 'Music', [('rock', 'rock'), ('jazz', 'jazz'), ('samba', 'samba'), ('country music', 'música country')]), ('event', 'Event', [('a concert', 'um show'), ('a music festival', 'um festival de música'), ('an opera', 'uma ópera')])]),
 reg=[['Who’s on tonight?', 'Which artists are performing this evening?'], ['I’m a huge fan.', 'I greatly admire this artist.'], ['Have you ever been to one?', 'Have you ever attended a concert?'], ['It gets crazy loud.', 'The volume becomes very high.']],
 pron=dict(focus='Key vowel sounds', tip='Music words have vowels that are easy to confuse: “love” (/ʌ/), “loud” (/aʊ/), “band” (/æ/). Open your mouth for /æ/ and relax for /ʌ/.',
  items=[('I love this band.', 'I LOVE this BAND.', '/aɪ lʌv ðɪs bænd/', 'oOoO'), ('It gets very loud.', 'It gets VE-ry LOUD.', '/ɪt gɛts ˈvɛri laʊd/', 'ooOoO'), ('Who’s playing tonight?', 'Who’s PLAY-ing toNIGHT?', '/huz ˈpleɪɪŋ təˈnaɪt/', 'oOooO')],
  id=[(['I love this song.', 'I live this song.', 'I leave this song.'], 0), (['It gets loud.', 'It gets lied.', 'It gets load.'], 0)], own='Write a sentence with “love” or “loud” about music you like.', crit='Say it twice. Is “love” short and relaxed, and “loud” long and open?'),
 chal=([('mcq', '1. You want to know the artist for tonight.', ['Who’s playing tonight?', 'Who play tonight is?', 'What is playing person?'], 0, 'Who’s playing + time.'), ('mcq', '2. You really like a band.', ['I’m a big fan of this band.', 'I am fan big this band.', 'I big like band.'], 0, 'I’m a big fan of + noun.'), ('mcq', '3. You ask about past experience.', ['Have you ever been to a concert?', 'You ever go concert?', 'Did you ever to a concert?'], 0, 'Have you ever been to + place?'), ('mcq', '4. You went to three shows.', ['Yes, three times.', 'Yes, three time.', 'Yes, three is.'], 0, 'Use times for frequency.')],
  [('gap', '___ playing tonight?', 'Who’s', ['Who’s', 'What’s', 'When’s'], 'Who’s playing + time.'), ('gap', 'Have you ever ___ to a festival?', 'been', ['been', 'go', 'went'], 'Have you ever been to + place?'), ('swap', 'Say it with “I’m a big fan of”:', 'I like this singer a lot.', ['I’m a big fan of this singer.', 'I’m a big fan of this singer'], 'I’m a big fan of this singer.', 'I’m a big fan of + noun shows strong interest.'), ('swap', 'Ask about experience:', 'concert', ['Have you ever been to a concert?', 'Have you ever been to a concert'], 'Have you ever been to a concert?', 'Have you ever been to + a + noun?'), ('reply', 'Have you ever been to a festival?', ['Yes, twice! It was great.', 'Yes, I am festival.', 'I have fest.'], 0, 'Answer yes + how many times + a short comment.')]),
 chans=['1: Who’s playing tonight? · 2: I’m a big fan of this band. · 3: Have you ever been to a concert? · 4: Yes, three times.', 'Gap: Who’s · been · I’m a big fan of this singer. · Have you ever been to a concert? · Yes, twice! It was great.'],
 role=dict(title='small talk at a concert', teacher='You are a stranger in line at the concert (change the plan during the scene!).', student='You are a fan: ask who is playing, share your favorite music and ask about past shows.',
  orders=['Talk about your favorite band', 'Talk about a show you went to', 'Talk about a festival you want to go to'], comp=['The stranger doesn’t know your band: describe their music.', 'The stranger asks for the name of a song: answer.', 'You lost your friend in the crowd: ask for help.', 'You didn’t hear the question: ask the person to repeat.'],
  chunks=['Who’s playing?', 'I love…', 'I’m a big fan of…', 'Have you ever been to…?'], kw=['band', 'love', 'loud', 'first time', 'encore'], stretch=['Peça que o estudante recomende uma banda e explique o porquê em três frases.']),
 lab=dict(rounds=[('Who’s playing?', 3, 'Ask who is on the festival stage. Answer with the schedule card.', 'Who’s playing…? / The band is…', False), ('Music you love', 3, 'Tell your partner about two artists you love.', 'I love… / I’m a big fan of…', False), ('Have you ever…?', 3, 'Ask about shows and festivals. Use “twice”, “once”, “never”.', 'Have you ever been to…?', False), ('Dream lineup', 2, 'Whole group: each pair names the best festival line-up.', 'Our festival has… because…', True)],
  gt='Festival schedule', at='Student A has the stage list', atask='You know the Friday acts. Ask your partner about Saturday.', bt='Student B has the stage list', btask='You know the Saturday acts. Ask your partner about Friday.',
  rows=[('Friday 6 pm', 'Blue Rivers', ''), ('Friday 9 pm', '', 'Luna Fox'), ('Saturday 7 pm', 'Los Gatos', ''), ('Saturday 10 pm', '', 'The Sunset Kids')], ans='A tem Friday 6 pm (Blue Rivers) e Saturday 7 pm (Los Gatos); B tem Friday 9 pm (Luna Fox) e Saturday 10 pm (The Sunset Kids). Cada um pergunta “Who’s playing…?”.'),
 miss=dict(title='festival day', goal='Each group must talk to new people at a festival, share music tastes and plan what to see.',
  list=[('A', 'Fans in line', 'Find out who is playing and who is your favorite band.', 'Use “Who’s playing…?” and “I’m a big fan of…”', 'Hi! Who’s playing tonight?'), ('B', 'Festival friends', 'Compare which shows you have been to and choose one to see together.', 'Use “Have you ever been to…?” twice.', 'Hey! Have you ever been to…'), ('C', 'Roommates', 'Plan a night out: choose a band, a time and what to bring.', 'Use “I love…” and give advice like “Bring…”.', 'Let’s go! I love…')],
  model='“Who’s playing tonight?” → “The Blue Rivers.” → “I love them! Have you ever seen them live?” → “Yes, twice. Bring earplugs.”'),
 write=dict(task='Write a short post for social media about a show you want to see or you saw. Say who plays and why you love it.', steps=['Name of the artist', 'Where and when', 'Why you love them', 'Invitation'],
  model='Tonight I’m going to see the Blue Rivers! **I’m a big fan of** their songs and **I love** their drummer. **Have you ever been to** one of their shows? Come with me next time!', check=['I said who plays.', 'I said where or when.', 'I said why I love it.', 'I asked a question or invited someone.']),
 fb=('Example: You asked about the band and shared your own taste.', 'Example: Keep “love” short: /lʌv/, not “loove”.', 'Example: Tell a friend about a past show in four sentences.'),
 exit=dict(tasks=[('❓', 'Build a question', 'Without notes: ask who is on stage tonight.', 'Who’s playing tonight?'), ('💬', 'Respond to a situation', 'A stranger asks: “Have you ever been to a festival?” You went once.', 'Yes, once. It was great!'), ('⭐', 'Use a new expression', 'Say you really like jazz.', 'I’m a big fan of jazz.')],
  hw=['Record a 45–60 second audio about your favorite band.', 'Write a short post about a show you want to see.', 'Review three expressions from the class and create your own examples.', 'Listen to the dialogue again and identify two expressions.'],
  next=['Who’s playing?', 'I love…', 'Have you ever been to…?'], week=['I’m a big fan of…', 'It gets loud.', 'Bring earplugs.'], unit=['Invite · plan · share · react']),
 ladder=[('A1', 'I love music. Rock, please!', 'Say what you love with short phrases.'), ('A2', 'I love this band. Have you ever seen them live?', 'Share taste and ask about experience.'), ('B1', 'I’ve been a fan of this band for years, but I’ve never seen them live.', 'Talk about experience over time.'), ('B2', 'Seeing them live had been on my list for ages, so I jumped at the chance when tickets came out.', 'Tell a story with reasons.'), ('C1', 'Their live shows are said to be a different experience altogether, and I can see why people rave about them.', 'Express views with distance.'), ('C2', 'It’s one of those rare shows where the crowd and the band seem to breathe together.', 'Describe atmosphere with style.')],
 err=[('I am fan of this band.', 'I’m a fan of this band.'), ('Who is play tonight?', 'Who’s playing tonight?'), ('Have you ever went to a concert?', 'Have you ever been to a concert?'), ('I love very much this song.', 'I love this song so much.'), ('Three time.', 'Three times.'), ('I have been in a concert.', 'I’ve been to a concert.'), ('It have loud.', 'It’s loud. / It gets loud.'), ('I like of rock.', 'I like rock.')],
 xq=['What is your favorite song right now?', 'Have you ever been to a festival?', 'Who would you like to see live?', 'Do you sing in the shower?', 'What was the first concert you went to?', 'Do you prefer small shows or big stadiums?', 'What song makes you happy?', 'Do you listen to music while you work?'], tchr=None)


LESSON = build(S)

if __name__ == '__main__':
    print('ok', finish(LESSON), len(LESSON['pages']), 'páginas')
