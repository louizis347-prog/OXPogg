"""Auxiliar da Unidade 10 (A2): monta as 14/15 telas rl_* a partir do conteúdo de cada aula e gera o roteiro do professor."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from rl_common import PLAN, teach, finish

UNIT = 'Daily life: past and plans'
MAP = ['Last weekend (past simple)', 'Describing people', 'Comparing things', 'Making and changing reservations', 'Opinions and preferences', 'Giving advice', 'Talking about plans (going to)', 'Real-Life Mission Day 10']
CRIT = [dict(k='flu', name='Fluency', desc='Mantém a comunicação sem interrupções excessivas.'), dict(k='lan', name='Language use', desc='Utiliza adequadamente padrões, vocabulário e expressões.'), dict(k='pro', name='Pronunciation', desc='É compreensível e usa ritmo e entonação adequados.'), dict(k='int', name='Interaction', desc='Responde, pergunta, esclarece e desenvolve a conversa.')]
INTERP = [dict(max=8, text='Needs more support. Revisit the main patterns with guided practice before the next lesson.'), dict(max=13, text='Functional performance. Work on the lowest criteria in the next lesson.'), dict(max=17, text='Good control. Raise complexity and speed; add follow-up questions.'), dict(max=20, text='Strong performance. Move to a more demanding situation.')]


def build(c):
    n = c['n']; T = c['tx']  # T: por tela -> dict(extra, errors, answers, goal)
    def tc(key, goal, solo=None, group=None, support=None, stretch=None, answers=None):
        t = T.get(key, {})
        kw = dict(goal=t.get('goal', goal))
        if solo: kw['solo'] = solo
        if group: kw['group'] = group
        a = t.get('answers', answers)
        if a: kw['answers'] = a
        if t.get('extra'): kw['extra'] = t['extra']
        if t.get('errors'): kw['errors'] = [dict(w=w, r=r) for w, r in t['errors']]
        if support: kw['support'] = support
        if stretch: kw['stretch'] = stretch
        return teach(**kw)
    ca = c['cast']
    sp = c['speakers']
    DIALOG = dict(speakers={r: dict(name=nm) for r, nm in sp}, lines=[dict(who=w, en=e, pt=p) for w, e, p in c['lines']])
    tasks = c['listen_tasks']
    ch_ans = []
    for lv in c['challenge']:
        for it in lv['items']:
            ch_ans.append(it.get('ans') if isinstance(it.get('ans'), str) else (it['opts'][it['ans']] if 'opts' in it else it.get('model')))
    pages = [
     dict(t='rl_open', stage='warm', title=c['title'], pt=c['pt'], level='A2', unit=dict(n=10, k=c['k'], of=8, name=UNIT, map=MAP),
      situation=dict(text=c['situation'], scene=c['scene'], tod=c['tod'], cast=ca), goal=c['goal'], canDo=c['canDo'], success=c['success'], think=c['think'],
      teach=tc('open', 'Abrir a aula pela situação real, não pela regra.', solo=['Leia o objetivo e peça que o estudante diga, com as próprias palavras, o que vai conseguir fazer hoje.', 'Faça a pergunta “Think about it” antes de mostrar qualquer expressão.'], group=['Cada estudante diz uma palavra ou ideia que associa à situação.', 'Mostre os critérios de sucesso: eles são a missão final da aula.'], support=['Aceite respostas curtas ou em português na primeira rodada e reformule em inglês.'])),
     dict(t='rl_warm', stage='warm', title='Connection & warm-up', intro=dict(solo='Start with real questions about the student’s life, not a grammar test.', group='One question per student, then a follow-up question to a classmate.'),
      recall=c['recall'], qs=[dict(q=q, pt=p, sup=s) for q, p, s in c['warm']], tip='Use the answers to find gaps and to recycle earlier content. The goal is to enter English from the first minute.',
      teach=tc('warm', 'Entrar no idioma no primeiro minuto e mapear lacunas.', support=['Ofereça as respostas-modelo (chips) e peça apenas que escolham uma e a ampliem com um motivo.'])),
     dict(t='rl_culture', stage='immersion', title=c['culture_title'], intro=c['culture_intro'], cards=[dict(vis=v, en=e, pt=p, note=nt) for v, e, p, nt in c['cards']],
      qs=[dict(q=q, pt=p, levels=dict(A1=a1, A2=a2, B1=b1, B2=b2)) for q, p, a1, a2, b1, b2 in c['culture_qs']], compare=c['compare'],
      teach=tc('culture', 'Ativar o contexto cultural e as primeiras hipóteses.', solo=['Mostre os cartões e peça hipóteses antes de explicar.', 'Peça que compare com o que acontece no Brasil.'], group=['Cada estudante escolhe um cartão e explica em uma frase.', 'Pergunte “Do you agree?” entre colegas.'], support=['Use as respostas de nível A1 como andaime e peça que repitam.'], stretch=['B2: compare o registro e o tom entre Brasil e EUA com exemplos reais.'], answers=c['culture_ans'])),
     dict(t='rl_listen', stage='immersion', title='Scene & listening', scene=dict(scene=c['scene'], tod=c['tod'], cast=ca), pass1=c['pass1'], pass2=dict(tasks=[dict(**t) for t in tasks]),
      teach=tc('listen', 'Compreender a situação antes de ver o texto: ideia principal e depois informações específicas.', solo=['Esconda o texto. 1ª escuta: só a ideia principal.', '2ª escuta: peça os detalhes pedidos nas tarefas. Só depois mostre o texto.'], group=['Escuta coletiva; duplas anotam antes de revelar.', 'Compare as respostas entre duplas e só então mostre o texto.'], support=['Use o botão “Slow” na 2ª escuta.', 'Pause depois de cada fala se necessário.'], answers=['Pass 1: ' + c['pass1']['opts'][c['pass1']['ans']], 'Pass 2: ' + ' · '.join(t['ans'] for t in tasks)])),
     dict(t='rl_dialog', stage='notice', title='Dialogue — a real-life conversation', qs=c['dialog_qs'], retell=dict(prompt='Retell the conversation in your own words, at your level.', starters=c['retell']),
      teach=tc('dialog', 'Ler o diálogo, perceber os chunks e recontar.', solo=['O estudante lê um papel e você lê o outro; depois troquem.', 'Peça que reconte a conversa no nível que conseguir.'], group=['Leitura em duplas e troca de papéis.', 'Reconto em cadeia: uma frase por estudante.'], support=['Mostre a tradução (botão PT) depois da 2ª leitura.'], answers=[' · '.join(q['opts'][q['ans']] for q in c['dialog_qs'])])),
     dict(t='rl_chunks', stage='notice', title='Useful expressions', items=c['chunks'], discover=c['discover'],
      note='Instead of memorizing the whole list, choose 3–5 expressions (★) to use again and again. The others are for understanding and for stretching later.',
      teach=tc('chunks', 'Escolher 3–5 chunks para uso repetido e descobrir a função de cada um.', solo=['Pergunte “When do you say it?” antes de dar o significado.', 'Compare formal × informal e peça um exemplo próprio.'], group=['Cada estudante escolhe a expressão que mais usaria e explica quando.', 'Comparem equivalentes em duplas.'], support=['Trabalhe só as expressões ★ nesta aula.'], answers=[' · '.join(c['discover']['fns'])])),
     dict(t='rl_patterns', stage='gram', title='Grammar in context — speaking patterns', patterns=c['patterns'], swap=c['swap'], register=c['register'],
      teach=tc('patterns', 'Fixar os padrões principais (01 e 02); os outros são expansão. Usar a troca de palavras para variar a fala.', solo=['Mostre o padrão DENTRO do diálogo (grife os chunks).', 'Use “Swap the words”: toque em cada peça e peça que o estudante diga a frase completa.', 'Compare spoken × written em 2 exemplos.'], group=['Troca em cadeia: cada estudante muda UMA peça e o próximo repete a frase.', 'Em pares: um escolhe as peças, o outro fala.'], support=['Fique só com o padrão 01 na primeira rodada.'], stretch=['Combine dois padrões na mesma resposta.'], answers='Padrões 01 e 02 são o foco; 03 e 04 são expansão para quem avançar rápido.')),
     dict(t='rl_pron', stage='gram', title='Pronunciation lab — natural American English', focus=c['pron']['focus'], tip=c['pron']['tip'], items=c['pron']['items'], identify=c['pron']['identify'], own=c['pron']['own'],
      teach=tc('pron', 'UM só fenômeno de pronúncia: ' + c['pron']['focus'] + '.', solo=['3 passagens: escutar e identificar, reproduzir ritmo e entonação, usar em frase com conteúdo próprio.', 'Modele devagar e em velocidade normal; peça que bata palmas na sílaba forte.'], group=['Coro, depois duplas; circule ouvindo.', 'Cada estudante cria uma frase própria usando o fenômeno.'], support=['Reduza a velocidade e conte as batidas em voz alta.'], answers=['Identify: ' + ' · '.join(q['opts'][q['ans']] for q in c['pron']['identify'])])),
     dict(t='rl_challenge', stage=dict(solo='practice', group='gram'), title='Guided challenges', levels=c['challenge'],
      teach=tc('challenge', 'Do controlado ao guiado: escolher, completar, substituir e responder antes da fala livre.', solo=['Peça que o estudante justifique cada resposta.', 'Se acertar rápido, peça uma versão mais informal ou mais educada.'], group=['Resolvam em duplas e comparem antes de revelar.', 'Equipes: ponto por resposta justificada.'], support=['Ofereça o banco de palavras (chips) nas lacunas.'], answers=[' · '.join(str(a) for a in ch_ans)])),
     dict(t='rl_role', for_='solo', stage='speak1', title=c['role_title'], brief=c['brief'], orders=c['orders'], complications=c['complications'],
      rounds=[dict(label='With support', desc='Chunks on screen', help=c['help1']), dict(label='Keywords', desc='Only the keywords', help=c['help2'], kw=True), dict(label='No script', desc='Free', help=[])], success=c['success'],
      teach=tc('role', 'Simulação com complicação inesperada e três rodadas com menos apoio.', solo=['Combine o cenário com a vida real do estudante.', 'Rodada 1: com chunks. Rodada 2: só palavras-chave. Rodada 3: sem roteiro.', 'Meta de fala: 60–70% do tempo para o estudante. Anote 2–3 correções para a devolutiva.'], support=['Volte à rodada 1 se travar; peça que repita só a primeira frase.'], stretch=['Acrescente uma segunda complicação no meio da cena.'])),
     dict(t='rl_lab', for_='group', stage='speak1', title='Communication lab — conversation rotations', rounds=c['lab_rounds'], infogap=c['infogap'],
      teach=tc('lab', 'Fluência por repetição da função com informações novas a cada rodada.', group=['Troque os pares a cada rodada (A+B / C+D → A+C / B+D → A+D / B+C → grupo todo).', 'Responsabilidade individual: cada aluno faz ≥1 pergunta e ≥1 resposta.', 'Circule anotando 2–3 correções prioritárias.'], support=['Entregue frases-modelo no chat da turma.'], answers=c['infogap_ans'])),
     dict(t='rl_mission', for_='group', stage='speak2', title='Group mission — ' + c['mission_name'], goal=c['mission_goal'], missions=c['missions'], min=11, success=c['success'],
      teach=tc('mission', 'Realizar algo com o inglês: o objetivo é resolver, não só falar certo.', group=['Cada grupo recebe papel, restrição e missão. Alterne os papéis.', 'Progressão: 1ª rodada com frases de apoio, 2ª só palavras-chave, 3ª sem roteiro.', 'Observe e anote 2–3 correções prioritárias; devolutiva no fim.'], support=['Dê o início de frase (“Start with”) em cada cartão.'], answers=c.get('mission_ans'))),
     dict(t='rl_write', stage='write', title='Writing — a small real-life task', task=c['write']['task'], steps=c['write']['steps'], model=c['write']['model'], checklist=c['write']['checklist'],
      tip='Fix only 2–3 priority points. Show a more natural way to say the same idea instead of rewriting everything.', fix=dict(n=3),
      teach=tc('write', 'Produção escrita curta ligada à situação comunicativa.', solo=['Peça o texto; corrija 2–3 pontos prioritários e mostre uma forma mais natural.'], group=['Cada estudante escreve; depois troquem os textos e corrijam em duplas.'], support=['Dê o modelo e peça só para trocar os dados.'])),
     dict(t='rl_feedback', stage='write', title='Feedback & review — Speaking Performance Check', criteria=CRIT, interpret=INTERP, prompts=c['prompts'],
      teach=teach(goal='Avaliar o que o aluno conseguiu comunicar, não só os erros gramaticais.', solo=['O estudante se autoavalia primeiro; depois você.', 'Feche com os três blocos: What you did well · What to improve · Your next challenge.'], group=['Dê um comentário por critério a cada estudante.', 'Cada um escolhe o próprio próximo desafio.'], answers='A rubrica é uma ferramenta interna de acompanhamento, não uma certificação CEFR.')),
     dict(t='rl_exit', stage='exit', title='Exit ticket & homework', tasks=c['exit_tasks'], homework=dict(h='Your real-life English mission', min='10–15', items=c['homework']), spaced=c['spaced'],
      teach=tc('exit', 'Toda aula termina com uma produção observável.', solo=['Sem consultar as anotações: construir uma pergunta, responder a uma situação e usar uma expressão nova.'], group=['Exit challenge individual; compare com o colega e combine a tarefa de continuidade.'], answers=[' · '.join(t['model'] for t in c['exit_tasks'])])),
     dict(t='rl_levels', stage='exit', title='Level up — the same situation from A1 to C2', you='A2', intro='You do not need six different methods: the structure stays, while language complexity and autonomy grow.',
      ladder=[dict(lv=lv, say=s, goal=g) for lv, s, g in c['ladder']], note='This progression is illustrative: complex sentences do not define a level on their own. CEFR also considers comprehension, autonomy, fluency, accuracy, interaction and appropriateness.',
      teach=teach(goal='Mostrar a progressão sem criar seis metodologias.', solo=['Mostre onde o estudante está e a próxima etapa.'], group=['Cada um escolhe a frase do próprio nível e a do próximo.'], extra=['Which sentence would you like to be able to say next month?'])),
    ]
    L = dict(n=n, topic=c['topic'], level='A2', title=c['title'], pt=c['pt'], unit=dict(n=10, k=c['k'], of=8, name=UNIT), minutes=60, cast=ca, scene=c['scene'], tod=c['tod'], plan=PLAN, dialog=DIALOG, pages=pages)
    return finish(L)

def mcq(q, opts, ans, why): return dict(type='mcq', q=q, opts=opts, ans=ans, why=why)
def gap(text, ans, why, bank=None):
    d = dict(type='gap', text=text, ans=ans, why=why)
    if bank: d['bank'] = bank
    return d
def swp(instr, frm, ans, model, why): return dict(type='swap', instr=instr, frm=frm, ans=ans, model=model, why=why)
def reply(npc, opts, ans, why, q='Choose the best reply.'): return dict(type='reply', npc=npc, q=q, opts=opts, ans=ans, why=why)
def ch(en, pt, use, reg='neutral', alt=None, pri=False):
    d = dict(en=en, pt=pt, use=use, reg=reg)
    if alt: d['alt'] = alt
    if pri: d['pri'] = True
    return d
