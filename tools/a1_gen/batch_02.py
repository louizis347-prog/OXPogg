# Lote 02 do A1 (posições 14 a 21). Gerado com funções auxiliares; cada episódio é montado numa função.
#
# TROCAS DE OBRA:
# pos 14: de Home, Sweet Home para Eloise (livro, 1955)
# pos 15: de Friends para Hey Arnold! (série, 1996)
# pos 16: de Friends para Happy Days (série, 1974)
# pos 17: de One, Two, Buckle My Shoe para Five Little Ducks (rima infantil)
# pos 18: de One, Two, Buckle My Shoe para Stuart Little (livro, 1945)
# pos 19: de This Old Man para Monopoly (jogo de tabuleiro, 1935)
# pos 20: de This Old Man para Spider-Man (quadrinhos, 1962)
# pos 21: de I've Been Working on the Railroad para The Polar Express (livro, 1985)
import itertools

_c = itertools.count(1)
POS = [(12, 16), (40, 14), (68, 14), (88, 18), (14, 82)]
POOL = ['beach', 'zoo', 'farm', 'playground', 'busstop', 'bakery', 'supermarket', 'bookshop', 'postoffice', 'bank',
        'pharmacy', 'restaurant', 'hotelroom', 'mountain', 'forest', 'snow', 'stage', 'library', 'museum', 'castlehall',
        'garden', 'fair', 'pool', 'stadium', 'harbor', 'chefkitchen', 'musicroom', 'traincar', 'soccerfield', 'fishing',
        'artroom', 'nightcity', 'meetingroom', 'christmas']


def mix(opts):
    k = next(_c) % len(opts)
    o = list(opts[1:])
    o.insert(k, opts[0])
    return o, k


def quiz(q, pt, opts, line, why):
    o, a = mix(opts)
    return dict(q=q, pt=pt, opts=[list(x) for x in o], a=a, line=line, why=why)


def rdg(q, opts, why):
    o, a = mix(opts)
    return dict(q=q, o=o, a=a, why=why)


def gap(q, pt, opts, why):
    o, a = mix(opts)
    return dict(q=q, pt=pt, opts=o, a=a, why=why)


def trap(opts, why, q='Qual frase está certa?'):
    o, a = mix(opts)
    return dict(q=q, opts=o, a=a, why=why)


def mtrap(ask, opts, why, say=None):
    o, a = mix(opts)
    d = dict(ask=ask, opts=o, a=a, why=why)
    if say:
        d['say'] = say
    return d


def mgap(text, pt, opts, why, say):
    o, a = mix(opts)
    return dict(text=text, pt=pt, opts=o, a=a, why=why, say=say)


def expq(ask, opts, why):
    o, a = mix(opts)
    return dict(ask=ask, opts=o, a=a, why=why)


def rnd(say, other, why):
    o, a = mix([say, other])
    return dict(fig='🎧', say=say, ask='Qual palavra você ouviu?', opts=o, a=a, why=why)


def hunt_t(say, other, why):
    o, a = mix([say, other])
    return dict(fig='🎧', say=say, ask='Ouça e toque na palavra.', opts=o, a=a, why=why)


def hunt_p(say, emojis, why):
    o, a = mix(emojis)
    return dict(fig='🎧', say=say, ask='Ouça e toque na figura.', opts=[[e, ''] for e in o], a=a, why=why, pic=1)


def hots(rows):
    return [dict(e=r[0], x=POS[i][0], y=POS[i][1], en=r[1], pt=r[2], say=r[3], sayPt=r[4]) for i, r in enumerate(rows)]


def prod(prompt, chips, model, check, kw, tips, ok, reply, ph='Escreva a sua resposta aqui…'):
    return dict(prompt=prompt, ph=ph, chips=chips, model=model, check=check, kw=kw,
                tips=[[list(p) for p in t] for t in tips], ok=ok, reply=list(reply))


def rsmap(i, stage, extra=None):
    ks = 'review dquiz rdg pat vplay build order soundlab produce wrap dictate balloons sbuild scenebuild'.split()
    pool = [s for s in POOL if s != stage]
    off = (i * 7) % len(pool)
    pool = pool[off:] + pool[:off]
    d = {k: pool[j] for j, k in enumerate(ks)}
    d['scene'] = stage
    d.update(extra or {})
    return d


def verb(v, ic, pt, s1, s2, ex, note3):
    return dict(v=v, ic=ic, pt=pt, f=[['eu', s1], ['ele/ela', s2]], ex=list(ex),
                note='**%s** = %s. Com he/she: **%s**.' % (v, pt, note3))


def pg(label, slots, end=('?', '?')):
    return dict(label=label, slots=[dict(cat=c, opts=[list(o) for o in os_]) for c, os_ in slots], end=list(end))


def mission(ic, name, desc, **kw):
    return dict(ic=ic, name=name, desc=desc, data=prod(**kw))


def exp(ic, en, tag, pt, use, ex):
    return dict(ic=ic, en=en, tag=tag, pt=pt, use=use, ex=list(ex))


def cx(rows):
    return [dict(text=t, pt=p, opts=o, a=0) for t, p, o in rows]


def cover(s, items, seed):
    return dict(s=s, items=[list(i) + ['bob'] for i in items], seed=seed)


def build(n, B, X, XT, VB, MR, CX):
    X = dict(X, n=n, review=True)
    return dict(B=B, X=X, XT=XT, VB=VB, MR=MR, CX=CX)


# ---------------------------------------------------------------- pos 14 · Eloise · Can I…? / Can you…?
def ep14():
    cast = {'Eloise': ['👧', '#E91E63'], 'Nanny': ['👵', '#455A64'], 'Clerk': ['🛎️', '#1F3A5F']}
    B = dict(
        title='Ligando para a recepção · Can I…? Can you…?',
        sub='Fazer pedidos no hotel com Can I…? e Can you…?',
        pattern_label='Can I…? / Can you…?',
        why='Hoje você aprende a pedir coisas e ajuda como a Eloise: Can I have…? e Can you…?',
        vocab=[['Key', 'Chave', 'Soa como “KÍ”.'], ['Phone', 'Telefone', 'Soa como “FÔUN”.'],
               ['Bed', 'Cama', 'Soa como “BÉD”.'], ['Water', 'Água', 'Soa como “UÓ-ter”.'],
               ['Soap', 'Sabonete', 'Soa como “SÔUP”.'], ['Help', 'Ajuda, ajudar', 'Soa como “HÉLP”.']],
        balloons=[['🔑', 'key'], ['☎️', 'phone'], ['🛏️', 'bed'], ['💧', 'water'], ['🧼', 'soap'], ['🆘', 'help']],
        cover_art=cover('hotelroom', [('🔑', 100, 54, 18), ('☎️', 138, 42, 14), ('🛎️', 84, 32, 12)], 'el1'),
        cover_sub='Can I…? Can you…? Em 10 minutos você faz pedidos como a Eloise',
        cover_say='A Eloise mora no hotel e liga para a recepção o tempo todo. Como pedir uma chave ou ajuda com educação?',
        wrap_recap=[['Can I have a key, please?', 'Posso ter uma chave, por favor?'],
                    ['Can you help me?', 'Você pode me ajudar?'],
                    ['Yes, you can.', 'Sim, pode.'],
                    ['Can you wait a minute?', 'Você pode esperar um minuto?']],
        teaser={'t': 'Hey Arnold!', 'd': 'Próximo padrão: cumprimentos informais (Hey, what\'s up?)'},
        cast=cast,
        lines=[['Eloise', 'Hello, front desk! Can you help me?', 'Olá, recepção! Você pode me ajudar?'],
               ['Clerk', 'Front desk. Yes, I can help you.', 'Recepção. Sim, posso ajudar.'],
               ['Eloise', 'Can I have a new key, please?', 'Posso ter uma chave nova, por favor?'],
               ['Clerk', 'Sure! Can you wait a minute?', 'Claro! Você pode esperar um minuto?'],
               ['Nanny', 'Eloise, can I have the phone?', 'Eloise, posso pegar o telefone?'],
               ['Eloise', 'Not now, Nanny! Can you wait, please?', 'Agora não, Babá! Você pode esperar, por favor?'],
               ['Eloise', 'One more thing! Can I have water?', 'Mais uma coisa! Posso ter água?'],
               ['Clerk', 'Yes, you can! Have a nice day, Eloise.', 'Sim, pode! Tenha um bom dia, Eloise.']],
        quiz=[quiz('What does Eloise ask for first?', 'O que a Eloise pede primeiro?',
                   [('🆘', 'Help'), ('🛏️', 'A bed'), ('🧼', 'Soap')], 0, 'Ela diz: “Can you help me?”'),
              quiz('What does Eloise want?', 'O que a Eloise quer?',
                   [('🔑', 'A new key'), ('☎️', 'A phone'), ('💧', 'Ice')], 2, 'Ela pede: “Can I have a new key?”'),
              quiz('Who wants the phone?', 'Quem quer o telefone?',
                   [('👵', 'Nanny'), ('👧', 'Eloise'), ('🛎️', 'The clerk')], 4, 'A Babá diz: “Can I have the phone?”')],
        rdg_q=rdg('Como pedir água com educação?', ['Can I have water, please?', 'I can water?', 'Can I to have water?'],
                  'Pedido: **Can I have** + coisa + please. Sem “to”.'),
        dictate=[['Can you help me?', 'Você pode me ajudar?'], ['Can I have a key, please?', 'Posso ter uma chave, por favor?'],
                 ['Yes, you can.', 'Sim, pode.'], ['Can you wait a minute?', 'Você pode esperar um minuto?']],
        produce=prod('A recepção atende: *Front desk. Can I help you?* **Peça uma coisa com Can I have…? e peça um favor com Can you…? Use please.**',
                     ['Can I have', 'Can you', 'please'],
                     'Can I have a key and water, please? Can you help me?',
                     ['Pedi algo com Can I have…?', 'Pedi um favor com Can you…?', 'Usei please?'],
                     ['\\bcan i have\\b', '\\bcan you\\b[^.!?]*\\?', '\\bplease\\b'],
                     [[('Can I have water?', 'Posso ter água?'), ('Can I have a key?', 'Posso ter uma chave?')],
                      [('Can you help me?', 'Você pode me ajudar?'), ('Can you wait?', 'Você pode esperar?')],
                      [('Please.', 'Por favor.'), ('Thank you.', 'Obrigado.')]],
                     ['Pedido educado! 🛎️', 'Favor pedido! 🙏', 'Please no final! ✨'],
                     ['Of course! I can bring them. Have a nice day!', 'Claro! Posso levar. Tenha um bom dia!']),
        rs=rsmap(0, 'hotelroom'), sc='hotelroom')
    X = dict(
        names=['Eloise', 'Clerk'],
        stage=dict(rs='hotelroom', chars=[['p:long:f2d16b:f4c7a1:e91e63:bow:dress', 26, 0, 0.9],
                                          ['p:bun:bdbdbd:f4c7a1:455a64:glasses:dress', 54, 1, 1.0],
                                          ['p:short:3b2a20:e8b48a:1f3a5f:none:suit', 84, 1, 1.0]]),
        obra=dict(name='Eloise', kind='📖 Livro infantil · 1955', year='1955',
                  text='Livro infantil de Kay Thompson, com desenhos de Hilary Knight, publicado em 1955. Eloise é uma menina de seis anos que mora no hotel Plaza, em Nova York, e adora telefonar para a recepção.',
                  line=['Can you help me, please?', 'Você pode me ajudar, por favor? (pedido típico de hotel)'],
                  pa=dict(t='rooftop', e=['🏨', '🛎️', '🔑'], p='a', v=0)),
        gancho=['Eloise', 'Hello, front desk! Can you help me?', 'Olá, recepção! Você pode me ajudar?'],
        hot=hots([('🔑', 'key', 'chave', 'Can I have a key, please?', 'Posso ter uma chave, por favor?'),
                  ('☎️', 'phone', 'telefone', 'Can you call me?', 'Você pode me ligar?'),
                  ('🛏️', 'bed', 'cama', 'Can I have a big bed?', 'Posso ter uma cama grande?'),
                  ('💧', 'water', 'água', 'Can I have water?', 'Posso ter água?'),
                  ('🧼', 'soap', 'sabonete', 'Can you bring soap?', 'Você pode trazer sabonete?')]),
        gap=[gap('___ I have a key, please?', 'Posso ter uma chave, por favor?', ['Can', 'Do', 'Am'], 'Para pedir algo: **Can I have**…?'),
             gap('Can you ___ me?', 'Você pode me ajudar?', ['help', 'helps', 'to help'], 'Depois de **can**, o verbo fica simples: Can you **help** me?'),
             gap('Yes, you ___.', 'Sim, pode.', ['can', 'do', 'are'], 'A resposta repete o **can**: Yes, you **can**.'),
             gap('Can she ___ water?', 'Ela pode trazer água?', ['bring', 'brings', 'bringing'], 'Com **can**, nada de -s: Can she **bring** water?')],
        trap=[trap(['Can I have water?', 'Can I to have water?', 'Can I having water?'], 'Depois de **can** vem o verbo simples, sem **to**: Can I **have** water?'),
              trap(['Can you wait here?', 'Do you can wait here?', 'You can wait here?'], 'Em inglês **can** abre a pergunta: **Can you** wait here?')],
        sticker=dict(title='Eloise e a recepção', sub='Eloise · 1955', rs='lobby2',
                     chars=[['p:long:f2d16b:f4c7a1:e91e63:bow:dress', 34, 0, 0.9], ['p:short:3b2a20:e8b48a:1f3a5f:none:suit', 70, 1, 1.0]]),
        speakers={'Eloise': 'p:long:f2d16b:f4c7a1:e91e63:bow:dress', 'Nanny': 'p:bun:bdbdbd:f4c7a1:455a64:glasses:dress',
                  'Clerk': 'p:short:3b2a20:e8b48a:1f3a5f:none:suit'},
        rule=dict(
            who='p:long:f2d16b:f4c7a1:e91e63:bow:dress', head='Can I…? Can you…?', sub='Para pedir uma coisa ou um favor.',
            say=['Can I have a key, please?', 'Posso ter uma chave, por favor?'],
            formula=[dict(from_=[['I', 0], ['have', 1], ['a key.', 2]], to=[['Can', 3], ['I', 0], ['have', 1], ['a key?', 2]],
                          say='Can I have a key?', note='**Can I** + verbo: você **pede** algo para si.'),
                     dict(from_=[['You', 0], ['wait.', 1]], to=[['Can', 3], ['you', 0], ['wait?', 1]],
                          say='Can you wait?', note='**Can you** + verbo: você **pede um favor** a alguém.')],
            uses=[dict(ico='🙏', tag='Pedir algo', en='Can I have water?', pt='Posso ter água?'),
                  dict(ico='🤝', tag='Pedir um favor', en='Can you help me?', pt='Você pode me ajudar?'),
                  dict(ico='✅', tag='Responder sim', en='Yes, you can.', pt='Sim, pode.')],
            rules=[dict(tag='Can I', c=0, text='Pede **permissão** ou algo para você.', ex='Can I have a key?'),
                   dict(tag='Can you', c=2, text='Pede **ajuda** a outra pessoa.', ex='Can you bring soap?'),
                   dict(tag='can + verbo', c=1, text='Depois de **can**, o verbo fica simples: sem **-s** e sem **to**.', ex='✗ Can she brings  →  ✓ Can she bring')],
            tips=['Em português basta dizer “pode?”. Em inglês, comece com **Can** e termine com **please**.']),
        mission_ic='🛎️')
    XT = dict(
        exp=[exp('👍', 'Of course!', 'Expressão', 'Claro!', 'Resposta **educada** a um pedido.', ['Of course! Here is your key.', 'Claro! Aqui está sua chave.']),
             exp('😎', 'Sure!', 'Informal', 'Claro! / Pode ser!', 'Jeito **informal** de dizer sim.', ['Sure! One minute.', 'Claro! Um minuto.']),
             exp('⏳', 'Just a minute.', 'Expressão', 'Só um minuto.', 'Quando você precisa que a pessoa **espere um pouco**.', ['Just a minute, please.', 'Só um minuto, por favor.']),
             exp('🙌', 'No problem.', 'Informal', 'Sem problema.', 'Resposta a um **obrigado** ou a um pedido.', ['No problem, Eloise!', 'Sem problema, Eloise!'])],
        exp_scene=dict(rs='lobby2', lines=[
            ['Eloise', 'Hello! Can I have soap, please?', 'Olá! Posso ter sabonete, por favor?'],
            ['Clerk', '**Of course!** **Just a minute.**', 'Claro! Só um minuto.'],
            ['Eloise', 'Can you bring water too?', 'Você pode trazer água também?'],
            ['Clerk', '**Sure!** Anything else?', 'Claro! Mais alguma coisa?'],
            ['Eloise', 'No, thank you!', 'Não, obrigada!'],
            ['Clerk', '**No problem**, Eloise.', 'Sem problema, Eloise.']]),
        lab=dict(
            short='ee × i', title='Laboratório de sons: o “ee” de please e key',
            say='Seat ou sit? O som longo “ee” muda a palavra. Vamos treinar com os pedidos da Eloise.',
            intro=dict(what='O **ee** em **please**, **key** e **need** é longo e tenso, como um “i” esticado: “iiii”.',
                       how='Estique os lábios como num sorriso e segure o som por um instante. No **i** curto (sit, fill), a boca fica mais relaxada e o som é bem rápido.',
                       pt='Em português só existe um “i”. Em inglês, **seat** (assento) ≠ **sit** (sentar). Por isso, estique o som longo.'),
            ex=[['please', 'PLÍIZ', 'por favor', 'segure o “ee” com sorriso'], ['key', 'KÍI', 'chave', 'som longo, bem esticado'],
                ['need', 'NÍID', 'precisar', 'sorriso e som longo']],
            pairs=[['seat', 'sit', 'assento × sentar'], ['feel', 'fill', 'sentir × encher'], ['leave', 'live', 'sair × morar'],
                   ['heat', 'hit', 'calor × bater']],
            tip='Sorria ao dizer **please** e **key**. Sorriso grande, som longo; boca relaxada, som curto.',
            phrase=['Can I have a key, please?', 'Posso ter uma chave, por favor?'],
            rounds=[rnd('seat', 'sit', '**Seat** (assento) tem o “ee” longo. **Sit** é curto.'),
                    rnd('fill', 'feel', '**Fill** (encher) tem o “i” curto. **Feel** tem o “ee” longo.'),
                    rnd('live', 'leave', '**Live** (morar) é curto. **Leave** (sair) é longo.')]),
        hunt=[hunt_t('leave', 'live', '**leave** = sair, com o “ee” longo.'),
              hunt_p('key', ['🔑', '🛏️', '💧'], '**key** = chave.'),
              hunt_t('heat', 'hit', '**heat** (calor) tem o “ee” longo.'),
              hunt_t('sit', 'seat', '**sit** (sentar) tem o “i” curto.'),
              hunt_p('bed', ['🛏️', '🔑', '☎️'], '**bed** = cama.')])
    VB = dict(title='Verbos para pedir no hotel', tip='Quatro verbos: bring, call, send e open.', items=[
        verb('bring', '🛎️', 'trazer', 'I bring water to the room.', 'Eloise bring**s** soap.', ['I bring water.', 'Eu trago água.'], 'brings'),
        verb('call', '☎️', 'ligar, chamar', 'I call the front desk.', 'She call**s** the clerk.', ['I call the front desk.', 'Eu ligo para a recepção.'], 'calls'),
        verb('send', '📨', 'enviar, mandar', 'I send a note.', 'He send**s** a key.', ['I send a note.', 'Eu mando um bilhete.'], 'sends'),
        verb('open', '🚪', 'abrir', 'I open the door.', 'Nanny open**s** the window.', ['I open the door.', 'Eu abro a porta.'], 'opens')])
    MR = dict(
        mold=[pg('Pedir com Can I have…?', [('pedido', [('Can I have', 'posso ter')]),
                                            ('coisa', [('a key', 'uma chave'), ('water', 'água'), ('soap', 'sabonete'), ('a bed', 'uma cama'), ('the phone', 'o telefone')])]),
              pg('Pedir um favor com Can you…?', [('pedido', [('Can you', 'você pode')]),
                                                  ('favor', [('help me', 'me ajudar'), ('wait', 'esperar'), ('call me', 'me ligar'), ('open the door', 'abrir a porta'), ('bring water', 'trazer água')])]),
              pg('Responder', [('resposta', [('Sure!', 'Claro!'), ('Of course!', 'Claro!'), ('No problem.', 'Sem problema.'), ('Just a minute.', 'Só um minuto.')])], end=('', ''))],
        speak=[['Can I have a key, please?', 'Posso ter uma chave, por favor?'], ['Sure! Just a minute.', 'Claro! Só um minuto.']],
        trap=[mtrap('“Just a minute” quer dizer…', ['Só um minuto.', 'Todo minuto.', 'Um minuto atrás.'], '**Just a minute.** = só um minuto, espere um pouco.', 'Just a minute.'),
              mtrap('Qual frase está certa?', ['Sure! I can bring water.', 'Sure! I can brings water.', 'Sure! I can to bring water.'], 'Depois de **can**, verbo simples: I can **bring**.')],
        gap=[mgap('___ you help me?', 'Você pode me ajudar?', ['Can', 'Do', 'Is'], 'Para pedir ajuda: **Can** you…?', 'Can you help me?'),
             mgap('Sure! No ___.', 'Claro! Sem problema.', ['problem', 'problems', 'minute'], '**No problem.** = sem problema.', 'No problem.')],
        expq=[expq('A recepção pede que você espere um pouco. O que ela diz?', ['Just a minute.', 'No problem.', 'Of course!'], '**Just a minute.** = só um minuto.'),
              expq('Alguém pede ajuda e você aceita com educação.', ['Of course!', 'Just a minute.', 'Can I have a key?'], '**Of course!** = claro!'),
              expq('Alguém diz “thank you”. Você responde de forma informal.', ['No problem.', 'Can you help me?', 'Just a minute.'], '**No problem.** = sem problema.')],
        missions=[mission('🛎️', 'Ligar para a recepção', 'Peça coisas ao hotel com educação.',
                          prompt='Seu quarto está sem sabonete. **Ligue para a recepção: peça sabonete com Can I have…? e peça para trazerem com Can you bring…? Diga please.**',
                          chips=['Can I have', 'Can you bring'], model='Can I have soap, please? Can you bring it to my room?',
                          check=['Pedi sabonete com Can I have…?', 'Pedi para trazer com Can you bring…?', 'Usei please?'],
                          kw=['\\bcan i have\\b[^.!?]*\\bsoap\\b', '\\bcan you bring\\b', '\\bplease\\b'],
                          tips=[[('Can I have soap?', 'Posso ter sabonete?')], [('Can you bring it?', 'Você pode trazer?')], [('Please.', 'Por favor.')]],
                          ok=['Pedido feito! 🧼', 'Favor pedido! 🛎️', 'Educado! 🙏'], reply=['Of course! Just a minute.', 'Claro! Só um minuto.']),
              mission('⏳', 'Esperar um minuto', 'Responda ao recepcionista com as expressões.',
                      prompt='O recepcionista diz: *Can you wait a minute?* **Responda com Sure ou Of course, diga No problem e agradeça com Thank you.**',
                      chips=['Sure!', 'No problem.'], model='Sure! No problem. Thank you!',
                      check=['Disse Sure ou Of course?', 'Disse No problem?', 'Agradeci?'],
                      kw=['\\b(?:sure|of course)\\b', '\\bno problem\\b', '\\bthank'],
                      tips=[[('Sure!', 'Claro!'), ('Of course!', 'Claro!')], [('No problem.', 'Sem problema.')], [('Thank you.', 'Obrigado.')]],
                      ok=['Resposta educada! 👍', 'Sem problema! 🙌', 'Obrigado! 😊'], reply=['Thank you! Here is your key.', 'Obrigado! Aqui está sua chave.'])])
    CX = cx([('You open the room with it. I need my room ___.', 'Você abre o quarto com ela. Preciso da chave do quarto.', ['key', 'soap', 'phone']),
             ('I call my mom on the ___.', 'Eu ligo para minha mãe no telefone.', ['phone', 'bed', 'water']),
             ('It is night. I am tired, and I go to ___.', 'É noite. Estou cansado e vou para a cama.', ['bed', 'key', 'help']),
             ('I am thirsty. I need a glass of ___.', 'Estou com sede. Preciso de um copo de água.', ['water', 'soap', 'bed']),
             ('I wash my hands with ___.', 'Eu lavo as mãos com sabonete.', ['soap', 'water', 'phone']),
             ('I do not know the way! Can you ___ me?', 'Não sei o caminho! Você pode me ajudar?', ['help', 'key', 'bed'])])
    return build(7070006, B, X, XT, VB, MR, CX)


# ---------------------------------------------------------------- pos 15 · Hey Arnold! · What's up? / Not much.
def ep15():
    ARN, GER, HEL = 'p:cap:f1d16a:f4c7a1:2b6cb0:none:shirt', 'p:curly:1b1b1b:8d5524:e67e22:none:shirt', 'p:long:f1d16a:f4c7a1:e84393:bow:dress'
    cast = {'Arnold': ['👦', '#2B6CB0'], 'Gerald': ['😎', '#E67E22'], 'Helga': ['🎀', '#E84393']}
    B = dict(
        title="Hey, What's Up? · Oi, e aí?",
        sub='Abrir uma conversa com amigos: Hey! What\'s up? Not much.',
        pattern_label="Hey! What's up?",
        why='Hoje você aprende a cumprimentar amigos do jeito solto dos americanos: Hey! What\'s up? Not much.',
        vocab=[['Hey', 'Ei, oi', 'Soa como “HÊI”.'], ['Buddy', 'Amigão, parceiro', 'Soa como “BÂ-di”.'],
               ['Bus', 'Ônibus', 'Soa como “BÂS”.'], ['Up', 'Para cima', 'Soa como “ÂP”.'],
               ['Friend', 'Amigo(a)', 'Soa como “FRÉND”.'], ['School', 'Escola', 'Soa como “SCUL”.']],
        balloons=[['👋', 'hey'], ['🤜', 'buddy'], ['🚌', 'bus'], ['⬆️', 'up'], ['🤝', 'friend'], ['🏫', 'school']],
        cover_art=cover('busstop', [('🚌', 102, 54, 20), ('👋', 138, 42, 14), ('🏫', 84, 32, 12)], 'ar1'),
        cover_sub="Hey, what's up? Em 10 minutos você cumprimenta amigos como o Arnold",
        cover_say="O Arnold encontra os amigos no ponto de ônibus. Ninguém diz “como vai o senhor”. Eles dizem só: Hey, what's up?",
        wrap_recap=[["Hey, what's up?", 'E aí?'], ['Not much.', 'Nada demais.'], ['Hey, buddy!', 'Ei, amigão!'], ['Hi, Helga!', 'Oi, Helga!']],
        teaser={'t': 'Happy Days', 'd': 'Próximo padrão: How\'s it going? e as despedidas See you later'},
        cast=cast,
        lines=[['Arnold', "Hey, Gerald! What's up?", 'Ei, Gerald! E aí?'],
               ['Gerald', 'Hey, Arnold! Not much. You?', 'Ei, Arnold! Nada demais. E você?'],
               ['Arnold', 'Not much. I see the bus!', 'Nada demais. Estou vendo o ônibus!'],
               ['Helga', 'Hi, Arnold! I mean... hey.', 'Oi, Arnold! Quer dizer... ei.'],
               ['Arnold', "Hey, Helga! What's up?", 'Ei, Helga! E aí?'],
               ['Helga', 'Nothing! I mean, not much!', 'Nada! Quer dizer, nada demais!'],
               ['Gerald', 'Hey, buddy! The bus is here.', 'Ei, amigão! O ônibus chegou.'],
               ['Arnold', 'Come on, friends! Bus time!', 'Vamos, amigos! Hora do ônibus!']],
        quiz=[quiz('Who says “I mean... hey”?', 'Quem diz “quer dizer... ei”?', [('🎀', 'Helga'), ('😎', 'Gerald'), ('👦', 'Arnold')], 3, 'Helga diz: “Hi, Arnold! I mean... hey.”'),
              quiz('What does Gerald say?', 'O que o Gerald responde?', [('🙂', 'Not much.'), ('😢', 'I am sad.'), ('🍕', 'I am hungry.')], 1, 'Gerald diz: “Not much.”'),
              quiz('What is here?', 'O que chegou?', [('🚌', 'The bus'), ('🚂', 'The train'), ('🚲', 'A bike')], 6, 'Gerald diz: “The bus is here.”')],
        rdg_q=rdg("Seu amigo diz “What's up?”. Qual resposta é natural?", ['Not much.', 'Yes, please.', 'Thank you very much.'],
                  "A resposta natural a **What's up?** é **Not much.** (nada demais)."),
        dictate=[["Hey, what's up?", 'E aí?'], ['Not much.', 'Nada demais.'], ['Hey, buddy!', 'Ei, amigão!'], ['Hi, Helga!', 'Oi, Helga!']],
        produce=prod("Seu amigo chega ao ponto de ônibus e diz: *Hey! What's up?* **Cumprimente com Hey ou Hi, responda Not much e pergunte What's up? de volta.**",
                     ['Hey!', 'Not much.', "What's up?"],
                     "Hey, Gerald! Not much. What's up with you?",
                     ['Cumprimentei com Hey ou Hi?', 'Respondi com Not much?', "Perguntei What's up?"],
                     ['\\b(?:hey|hi)\\b', '\\bnot much\\b|\\bnothing much\\b', '\\bwhat[\'’]?s up\\b'],
                     [[('Hey!', 'Ei!'), ('Hi!', 'Oi!')], [('Not much.', 'Nada demais.')], [("What's up?", 'E aí?'), ("What's up with you?", 'E com você?')]],
                     ['Cumprimento solto! 👋', 'Resposta natural! 😎', 'Devolveu a pergunta! 🔁'],
                     ['Not much! Come on, the bus is here!', 'Nada demais! Vamos, o ônibus chegou!']),
        rs=rsmap(1, 'busstop'), sc='busstop')
    X = dict(
        names=['Arnold', 'Gerald'],
        stage=dict(rs='busstop', chars=[[ARN, 26, 0, 1.0], [GER, 54, 1, 1.0], [HEL, 84, 1, 0.95]]),
        obra=dict(name='Hey Arnold!', kind='📺 Série animada · 1996', year='1996',
                  text='Série de desenho animado americana criada por Craig Bartlett e exibida no canal Nickelodeon a partir de 1996. Arnold é um menino que mora na cidade com os avós e anda com os amigos Gerald e Helga.',
                  line=['Hey, Arnold!', 'Ei, Arnold! (como os amigos o chamam)'],
                  pa=dict(t='busstop', e=['🚌', '👋', '🏫'], p='d', v=1)),
        gancho=['Arnold', "Hey, Gerald! What's up?", 'Ei, Gerald! E aí?'],
        hot=hots([('🚌', 'bus', 'ônibus', 'The bus is here!', 'O ônibus chegou!'),
                  ('🏫', 'school', 'escola', 'I go to school.', 'Eu vou para a escola.'),
                  ('🤝', 'friend', 'amigo', 'Gerald is my friend.', 'Gerald é meu amigo.'),
                  ('👋', 'hey', 'oi', 'Hey, Helga!', 'Ei, Helga!'),
                  ('⬆️', 'up', 'para cima', "What's up?", 'E aí?')]),
        gap=[gap('Hey, ___ up?', 'Ei, e aí?', ["what's", "where's", "who's"], "O cumprimento é **What's up?**"),
             gap('Not ___.', 'Nada demais.', ['much', 'many', 'more'], 'A resposta curta é **Not much.**'),
             gap("What's up ___ you?", 'E com você?', ['with', 'in', 'at'], "**What's up with you?** = e com você?"),
             gap('Helga ___ at Arnold.', 'A Helga acena para o Arnold.', ['waves', 'wave', 'waving'], 'Com she/he, o verbo leva **-s**: she **waves**.')],
        trap=[trap(['Not much.', "I'm eight.", 'Yes, please.'], 'Para **What\'s up?**, a resposta é **Not much.**', q="Qual resposta combina com “What's up?”"),
              trap(["What's up?", 'What are up?', "Whats' up?"], "A forma certa é **What's up?** (What is up)")],
        sticker=dict(title='Arnold e os amigos', sub='Hey Arnold! · 1996', rs='playground', chars=[[ARN, 32, 0, 1.0], [GER, 66, 1, 1.0]]),
        speakers={'Arnold': ARN, 'Gerald': GER, 'Helga': HEL},
        rule=dict(
            who=ARN, head="Hey! What's up?", sub='Como amigos se cumprimentam e respondem.',
            say=["Hey, Gerald! What's up?", 'Ei, Gerald! E aí?'],
            pairsHead='👋 Cumprimento → resposta',
            pairs=[dict(ico='🙋', a='<u>Hi</u>, Helga!', b='<u>Hey</u>, Arnold!', pta='oi, Helga', ptb='ei, Arnold', n=2),
                   dict(ico='❓', a="What's up?", b='Not <u>much</u>.', pta='E aí?', ptb='Nada demais.', n=2),
                   dict(ico='🔁', a="What's up?", b='Not much. <u>You</u>?', pta='E aí?', ptb='Nada demais. E você?', n=2),
                   dict(ico='🤜', a='Hey, <u>buddy</u>!', b='Hey, <u>friend</u>!', pta='ei, amigão', ptb='ei, amigo', n=2)],
            uses=[dict(ico='👋', tag='Cumprimentar', en='Hey, Gerald!', pt='Ei, Gerald!'),
                  dict(ico='❓', tag='Perguntar', en="What's up?", pt='E aí?'),
                  dict(ico='🙂', tag='Responder', en='Not much.', pt='Nada demais.')],
            rules=[dict(tag='Hey / Hi', c=0, text='**Hi** é oi. **Hey** é mais solto, entre amigos.', ex='Hi, Helga! · Hey, buddy!'),
                   dict(tag="What's up?", c=1, text="É **What is up?** encurtado. Quer dizer “e aí?”, não é pergunta de verdade.", ex="What's up? → Not much."),
                   dict(tag='Not much', c=2, text='Resposta curta e tranquila, mesmo se algo aconteceu.', ex='Not much. You?')],
            tips=["Não responda “What's up?” com “Up”! A resposta normal é **Not much.** (nada demais)."]),
        mission_ic='👋')
    XT = dict(
        exp=[exp('👋', "What's up?", 'Informal', 'E aí?', 'Para **abrir a conversa** com amigos e colegas.', ["Hey, what's up?", 'Ei, e aí?']),
             exp('🙂', 'Not much.', 'Informal', 'Nada demais.', 'Resposta **tranquila** a What\'s up?', ['Not much. You?', 'Nada demais. E você?']),
             exp('🤗', 'Long time no see!', 'Expressão', 'Quanto tempo!', 'Quando você **não vê alguém há muito tempo**.', ['Long time no see, Helga!', 'Quanto tempo, Helga!']),
             exp('🤜', 'Hey, buddy!', 'Gíria', 'Ei, amigão!', 'Jeito **amigável** de chamar um amigo, geralmente homem.', ['Hey, buddy! Come on!', 'Ei, amigão! Vamos!'])],
        exp_scene=dict(rs='playground', lines=[
            ['Gerald', "**Hey, buddy!** **What's up?**", 'Ei, amigão! E aí?'],
            ['Arnold', '**Not much.** You?', 'Nada demais. E você?'],
            ['Helga', 'Hi, boys! **Long time no see!**', 'Oi, meninos! Quanto tempo!'],
            ['Gerald', "Hey, Helga! **What's up?**", 'Ei, Helga! E aí?'],
            ['Helga', '**Not much.** I am happy!', 'Nada demais. Estou feliz!'],
            ['Arnold', 'Great! Come on, friends!', 'Ótimo! Vamos, amigos!']]),
        lab=dict(
            short='r americano', title='Laboratório de sons: o “r” de friend e great',
            say='O “r” americano aparece no meio e no fim das palavras. Vamos treinar com os amigos do Arnold.',
            intro=dict(what='O **r** de **great**, **friend** e **from** vem depois de outra consoante. Ele é suave, sem vibrar.',
                       how='Já na posição do “r”, arredonde um pouco os lábios e puxe a língua para trás, sem encostar em nada. Não faça o “h” do português (como em “rato”).',
                       pt='Em português o “r” forte (rato, carro) é áspero. Em inglês ele é macio. Cuidado para não trocar por **l**: **free** (grátis) ≠ **flea** (pulga).'),
            ex=[['great', 'GRÊIT', 'ótimo', 'língua solta já no “gr”'], ['friend', 'FRÉND', 'amigo', 'lábios redondos no “fr”'],
                ['from', 'FRÂM', 'de (origem)', 'sem vibrar a língua']],
            pairs=[['fry', 'fly', 'r: língua solta · l: ponta toca atrás dos dentes'], ['grass', 'glass', '“grama” × “vidro, copo”'],
                   ['free', 'flea', '“grátis” × “pulga”'], ['crowd', 'cloud', '“multidão” × “nuvem”']],
            tip='Diga “fr” de “friend” com os lábios arredondados. No “l” a ponta da língua encosta; no “r”, não.',
            phrase=['Hey, my friend! Great!', 'Ei, meu amigo! Ótimo!'],
            rounds=[rnd('grass', 'glass', '**Grass** (grama) começa com “gr”, língua solta.'),
                    rnd('fly', 'fry', '**Fly** (voar) tem “l”: a ponta da língua toca. **Fry** (fritar) tem “r”.'),
                    rnd('cloud', 'crowd', '**Cloud** (nuvem) tem “l”. **Crowd** (multidão) tem “r”.')]),
        hunt=[hunt_t('crowd', 'cloud', '**crowd** (multidão) tem “r”, sem tocar a língua.'),
              hunt_p('bus', ['🚌', '🚪', '🚗'], '**bus** = ônibus.'),
              hunt_t('fry', 'fly', '**fry** (fritar) tem “r”.'),
              hunt_t('glass', 'grass', '**glass** (vidro, copo) tem “l”.'),
              hunt_p('school', ['🏫', '🚌', '🏠'], '**school** = escola.')])
    VB = dict(title='Verbos para andar com os amigos', tip='Quatro verbos: wave, text, chill e hang out.', items=[
        verb('wave', '👋', 'acenar', 'I wave to my friend.', 'Helga wave**s** at Arnold.', ['I wave to my friend.', 'Eu aceno para meu amigo.'], 'waves'),
        verb('text', '📱', 'mandar mensagem', 'I text my buddy.', 'Gerald text**s** Arnold.', ['I text my buddy.', 'Eu mando mensagem para meu amigão.'], 'texts'),
        verb('chill', '😌', 'relaxar', 'I chill at home.', 'Arnold chill**s** after school.', ['I chill at home.', 'Eu relaxo em casa.'], 'chills'),
        verb('hang out', '🛹', 'passar tempo juntos', 'I hang out with Gerald.', 'He hang**s** out with friends.', ['I hang out with Gerald.', 'Eu saio com o Gerald.'], 'hangs out')])
    MR = dict(
        mold=[pg('Dizer oi', [('oi', [('Hey,', 'ei,'), ('Hi,', 'oi,'), ('Hello,', 'olá,')]),
                              ('quem', [('Gerald', 'Gerald'), ('Helga', 'Helga'), ('buddy', 'amigão'), ('friend', 'amigo')])], end=('!', '!')),
              pg('Perguntar o que há', [('oi', [('Hey,', 'ei,'), ('Hi,', 'oi,')]),
                                        ('quem', [('Gerald', 'Gerald'), ('buddy', 'amigão'), ('Helga', 'Helga')])], end=("! What's up?", '! E aí?')),
              pg('Responder', [('resposta', [('Not much.', 'Nada demais.'), ('Nothing much.', 'Quase nada.'), ('Not much, you?', 'Nada demais, e você?'), ('Nothing!', 'Nada!')])], end=('', ''))],
        speak=[["Hey, buddy! What's up?", 'Ei, amigão! E aí?'], ['Not much. You?', 'Nada demais. E você?']],
        trap=[mtrap('“Long time no see!” quer dizer…', ['Quanto tempo!', 'Até logo!', 'Não vejo nada!'], '**Long time no see!** = quanto tempo (sem te ver).', 'Long time no see!'),
              mtrap('Qual frase está certa?', ["Hey, buddy! What's up?", "Hey, buddy! What up is?", "Hey, buddy! Is what up?"], "A ordem fixa é **What's up?**")],
        gap=[mgap('Hey, ___ up?', 'Ei, e aí?', ["what's", 'where', 'who'], "**What's up?** = e aí?", "What's up?"),
             mgap('Not ___. You?', 'Nada demais. E você?', ['much', 'more', 'some'], '**Not much.** = nada demais.', 'Not much. You?')],
        expq=[expq('Você vê um velho amigo depois de dois anos.', ['Long time no see!', 'Not much.', "What's up?"], '**Long time no see!** = quanto tempo!'),
              expq('Um amigo diz “What’s up?”. Você não tem nada de novo.', ['Not much.', 'Long time no see!', 'Hey, buddy!'], '**Not much.** = nada demais.'),
              expq('Você quer chamar um amigo de forma carinhosa.', ['Hey, buddy!', 'Not much.', 'Long time no see!'], '**Hey, buddy!** = ei, amigão!')],
        missions=[mission('🚌', 'No ponto de ônibus', 'Cumprimente um amigo e responda.',
                          prompt="Você vê um amigo no ponto de ônibus. **Diga Hey ou Hi e o nome dele, pergunte What's up? e responda Not much.**",
                          chips=['Hey,', "What's up?", 'Not much.'], model="Hey, Gerald! What's up? Not much here.",
                          check=['Cumprimentei com Hey ou Hi?', "Perguntei What's up?", 'Respondi Not much?'],
                          kw=['\\b(?:hey|hi)\\b', '\\bwhat[\'’]?s up\\b', '\\bnot much\\b'],
                          tips=[[('Hey, Gerald!', 'Ei, Gerald!')], [("What's up?", 'E aí?')], [('Not much.', 'Nada demais.')]],
                          ok=['Oi! 👋', 'Pergunta solta! ❓', 'Resposta natural! 🙂'], reply=['Not much! Look, here is the bus!', 'Nada demais! Olha, o ônibus chegou!']),
              mission('🤗', 'Quanto tempo!', 'Use as expressões com um velho amigo.',
                      prompt='Você encontra um velho amigo. **Diga Long time no see, chame de buddy e pergunte What\'s up with you?**',
                      chips=['Long time no see!', 'buddy'], model="Long time no see, buddy! What's up with you?",
                      check=['Disse Long time no see?', 'Chamei de buddy?', "Perguntei What's up with you?"],
                      kw=['\\blong time no see\\b', '\\bbuddy\\b', '\\bwhat[\'’]?s up with you\\b'],
                      tips=[[('Long time no see!', 'Quanto tempo!')], [('Hey, buddy!', 'Ei, amigão!')], [("What's up with you?", 'E com você?')]],
                      ok=['Quanto tempo! 🤗', 'Amigão! 🤜', 'Boa pergunta! ❓'], reply=['Not much! I am so happy to see you!', 'Nada demais! Estou tão feliz em te ver!'])])
    CX = cx([('You see a friend and say "___, Gerald!"', 'Você vê um amigo e diz “Ei, Gerald!”.', ['Hey', 'Bus', 'Up']),
             ('He is my best ___. We play every day.', 'Ele é meu melhor amigão. Brincamos todo dia.', ['buddy', 'bus', 'school']),
             ('The yellow ___ takes the kids to school.', 'O ônibus amarelo leva as crianças à escola.', ['bus', 'friend', 'buddy']),
             ('The bird is high in the sky. Look ___ there!', 'O pássaro está alto no céu. Olhe lá para cima!', ['up', 'bus', 'hey']),
             ('Gerald is not only a classmate. He is my ___.', 'O Gerald não é só um colega. Ele é meu amigo.', ['friend', 'school', 'bus']),
             ('Arnold, Gerald and Helga go to ___ every morning.', 'Arnold, Gerald e Helga vão à escola toda manhã.', ['school', 'up', 'hey'])])
    return build(910001, B, X, XT, VB, MR, CX)


# ---------------------------------------------------------------- pos 16 · Happy Days · How's it going? / See you later
def ep16():
    FON, RIC, JOA = 'p:short:1b1b1b:e8b48a:5d4037:none:suit', 'p:short:b5651d:f4c7a1:2b6cb0:none:shirt', 'p:long:b5651d:f4c7a1:e57373:bow:dress'
    cast = {'Fonzie': ['😎', '#5D4037'], 'Richie': ['👦', '#2B6CB0'], 'Joanie': ['👧', '#E57373']}
    B = dict(
        title="Como vai? · How's it going?",
        sub="Perguntar como vai e se despedir: How's it going? See you later!",
        pattern_label="How's it going?",
        why="Hoje você aprende a perguntar como a pessoa está e a se despedir como os amigos: How's it going? See you later!",
        vocab=[['Great', 'Ótimo', 'Soa como “GRÊIT”.'], ['Good', 'Bom, bem', 'Soa como “GÚD”.'], ['Bad', 'Ruim, mal', 'Soa como “BÉD”.'],
               ['Later', 'Mais tarde', 'Soa como “LÊI-ter”.'], ['Soon', 'Logo, em breve', 'Soa como “SUUN”.'], ['Care', 'Cuidado, cuidar', 'Soa como “KÉR”.']],
        balloons=[['🤩', 'great'], ['👍', 'good'], ['👎', 'bad'], ['🕐', 'later'], ['🔜', 'soon'], ['💛', 'care']],
        cover_art=cover('restaurant', [('🍔', 102, 54, 18), ('🎵', 138, 42, 14), ('👋', 84, 32, 12)], 'hd1'),
        cover_sub="How's it going? Em 10 minutos você pergunta como vai e se despede como o Fonzie",
        cover_say="O Fonzie, o Richie e a Joanie se encontram na lanchonete. Como perguntar como alguém está? E como se despedir?",
        wrap_recap=[["How's it going?", 'Como vai?'], ['Pretty good.', 'Bem legal.'], ['Not bad.', 'Nada mal.'], ['See you later!', 'Até mais tarde!']],
        teaser={'t': 'Five Little Ducks', 'd': 'Próximo padrão: How much is…? e os números de 1 a 5'},
        cast=cast,
        lines=[['Richie', "Hey, Fonzie! How's it going?", 'Ei, Fonzie! Como vai?'],
               ['Fonzie', 'Pretty good, Richie! You?', 'Bem legal, Richie! E você?'],
               ['Richie', "Great! Joanie, how's it going?", 'Ótimo! Joanie, como vai?'],
               ['Joanie', 'Not bad. A little tired.', 'Nada mal. Um pouco cansada.'],
               ['Fonzie', 'Ayyy! Not bad is good!', 'Ayyy! Nada mal é bom!'],
               ['Joanie', 'Bye, boys! See you later!', 'Tchau, rapazes! Até mais tarde!'],
               ['Richie', 'See you soon, Joanie! Take care!', 'Até logo, Joanie! Se cuide!'],
               ['Fonzie', 'Take care, Richie. Ayyy!', 'Se cuide, Richie. Ayyy!']],
        quiz=[quiz('How is Fonzie?', 'Como o Fonzie está?', [('👍', 'Pretty good'), ('👎', 'Bad'), ('😴', 'Sleepy')], 1, 'Fonzie diz: “Pretty good.”'),
              quiz('How is Joanie?', 'Como a Joanie está?', [('😮‍💨', 'Not bad, a little tired'), ('🤩', 'Great'), ('😠', 'Angry')], 3, 'Joanie diz: “Not bad. A little tired.”'),
              quiz('What does Joanie say at the end?', 'O que a Joanie diz no fim?', [('👋', 'See you later!'), ('🙏', 'Thank you!'), ('🍔', 'I am hungry!')], 5, 'Ela diz: “Bye, boys! See you later!”')],
        rdg_q=rdg("Alguém pergunta “How's it going?”. Qual resposta é natural?", ['Pretty good, thanks.', "It's two dollars.", "I'm Richie."],
                  "**How's it going?** pergunta como as coisas vão. Responda: Pretty good, Not bad, Great…"),
        dictate=[["How's it going?", 'Como vai?'], ['Pretty good, thanks.', 'Bem legal, obrigado.'], ['See you later!', 'Até mais tarde!'], ['Take care!', 'Se cuide!']],
        produce=prod("Um amigo encontra você na lanchonete e diz: *Hey! How's it going?* **Responda com Pretty good, Not bad ou Great e se despeça com See you later.**",
                     ['Pretty good.', 'Not bad.', 'See you later!'],
                     "Hey! Pretty good, thanks. How's it going? Bye, see you later!",
                     ['Respondi como estou?', "Perguntei How's it going?", 'Me despedi com See you later?'],
                     ['\\b(?:pretty good|not bad|great|so-so)\\b', '\\bhow[\'’]?s it going\\b', '\\bsee you (?:later|soon)\\b'],
                     [[('Pretty good.', 'Bem legal.'), ('Not bad.', 'Nada mal.'), ('Great!', 'Ótimo!')], [("How's it going?", 'Como vai?')], [('See you later!', 'Até mais tarde!'), ('See you soon!', 'Até logo!')]],
                     ['Resposta natural! 👍', 'Pergunta devolvida! 🔁', 'Despedida solta! 👋'],
                     ['Ayyy! Take care, buddy!', 'Ayyy! Se cuide, amigão!']),
        rs=rsmap(2, 'restaurant'), sc='restaurant')
    X = dict(
        names=['Richie', 'Fonzie'],
        stage=dict(rs='restaurant', chars=[[RIC, 26, 0, 1.0], [FON, 54, 1, 1.0], [JOA, 84, 1, 0.9]]),
        obra=dict(name='Happy Days', kind='📺 Série de TV · 1974', year='1974',
                  text='Série de TV americana exibida pelo canal ABC a partir de 1974. Ela mostra, de forma divertida, a vida de uma família e de seus amigos nos anos 1950. O Fonzie é o rapaz mais descolado da turma.',
                  line=['Ayyy!', 'Ayyy! (o “E aí!” marca do Fonzie)'],
                  pa=dict(t='coffeeshop', e=['🍔', '🎵', '😎'], p='e', v=0)),
        gancho=['Richie', "Hey, Fonzie! How's it going?", 'Ei, Fonzie! Como vai?'],
        hot=hots([('🕐', 'later', 'mais tarde', 'See you later!', 'Até mais tarde!'),
                  ('🔜', 'soon', 'logo', 'See you soon!', 'Até logo!'),
                  ('💛', 'care', 'cuidado', 'Take care!', 'Se cuide!'),
                  ('👍', 'good', 'bom', 'Pretty good!', 'Bem legal!'),
                  ('👎', 'bad', 'ruim', 'Not bad!', 'Nada mal!')]),
        gap=[gap("How's ___ going?", 'Como vai?', ['it', 'you', 'he'], "O cumprimento fixo é **How's it going?**"),
             gap('See you ___!', 'Até mais tarde!', ['later', 'before', 'after'], '**See you later!** = até mais tarde!'),
             gap('___ care!', 'Se cuide!', ['Take', 'Do', 'Make'], 'A expressão é **Take care!**'),
             gap('Pretty ___!', 'Bem legal!', ['good', 'goods', 'goodly'], '**Pretty good** = bem legal.')],
        trap=[trap(["How's it going?", 'How are going it?', "How it's going?"], "A ordem certa é **How's it going?**"),
              trap(['See you later!', 'Look you later!', 'See you after!'], 'Despedida natural: **See you later!**')],
        sticker=dict(title='Fonzie e os amigos', sub='Happy Days · 1974', rs='stadium', chars=[[FON, 34, 0, 1.0], [JOA, 68, 1, 0.9]]),
        speakers={'Fonzie': FON, 'Richie': RIC, 'Joanie': JOA},
        rule=dict(
            who=FON, head="How's it going?", sub='Como perguntar como vai e como se despedir.',
            say=["Hey, Fonzie! How's it going?", 'Ei, Fonzie! Como vai?'],
            formula=[dict(from_=[['How', 0], ['is', 1], ['it going?', 2]], to=[["How's", 1], ['it going?', 2]],
                          say="How's it going?", note="**How is** vira **How's**. Pergunta pronta, a mais usada entre amigos.")],
            uses=[dict(ico='❓', tag='Perguntar', en="How's it going?", pt='Como vai?'),
                  dict(ico='🤩', tag='Muito bem', en='Great! Pretty good.', pt='Ótimo! Bem legal.'),
                  dict(ico='😐', tag='Mais ou menos', en='Not bad. So-so.', pt='Nada mal. Mais ou menos.'),
                  dict(ico='👋', tag='Despedir', en='See you later!', pt='Até mais tarde!')],
            rules=[dict(tag="How's it going?", c=0, text='Resposta curta, **sem “I am”**: Great! Pretty good. Not bad.', ex="How's it going? → Pretty good."),
                   dict(tag='Great → Bad', c=1, text='Da melhor para a pior: **Great, Pretty good, Not bad, So-so, Bad**.', ex='Great! · Not bad. · Bad.'),
                   dict(tag='See you…', c=2, text='**See you later** (mais tarde) e **See you soon** (em breve). Depois: **Take care!**', ex='See you soon! Take care!')],
            tips=["**Not bad** parece negativo, mas quer dizer “bem, tudo certo”. E nada de responder com a vida inteira: é só um cumprimento!"]),
        mission_ic='🍔')
    XT = dict(
        exp=[exp('🙋', "How's it going?", 'Informal', 'Como vai?', 'Pergunta **rápida** entre amigos, no lugar de How are you?', ["Hey, how's it going?", 'Ei, como vai?']),
             exp('😐', 'Not bad.', 'Informal', 'Nada mal.', 'Resposta **tranquila**: quer dizer que está tudo bem.', ['Not bad, thanks.', 'Nada mal, obrigado.']),
             exp('👋', 'See you later!', 'Expressão', 'Até mais tarde!', 'Despedida **simpática**, mesmo sem hora marcada.', ['Bye! See you later!', 'Tchau! Até mais tarde!']),
             exp('💛', 'Take care.', 'Expressão', 'Se cuide.', 'Despedida **carinhosa**, quando alguém vai embora.', ['Take care, Joanie.', 'Se cuide, Joanie.'])],
        exp_scene=dict(rs='stadium', lines=[
            ['Richie', "Hi, Joanie! **How's it going?**", 'Oi, Joanie! Como vai?'],
            ['Joanie', '**Not bad.** You?', 'Nada mal. E você?'],
            ['Richie', 'Pretty good! Hey, it is late.', 'Bem legal! Ei, está tarde.'],
            ['Joanie', 'Yes! Bye, Richie. **See you later!**', 'Sim! Tchau, Richie. Até mais tarde!'],
            ['Richie', '**Take care**, Joanie!', 'Se cuide, Joanie!'],
            ['Fonzie', 'Ayyy! Bye, kids!', 'Ayyy! Tchau, crianças!']]),
        lab=dict(
            short='h aspirado', title='Laboratório de sons: o “h” de hey e how',
            say='Em inglês o “h” é um sopro de ar. Vamos treinar com as saudações do Fonzie.',
            intro=dict(what='O **h** de **hey**, **how** e **hello** é só um sopro suave, como quando você embaça um vidro.',
                       how='Abra a boca, solte o ar da garganta sem fazer barulho e depois diga a vogal. Sem aspereza, e não omita o som!',
                       pt='Em português o “h” é mudo (hora, hoje). Em inglês ele existe. Por isso, **hi** (oi) ≠ **eye** (olho) e **hat** (chapéu) ≠ **at** (em).'),
            ex=[['hey', 'HÊI', 'ei, oi', 'sopre o ar antes do “êi”'], ['how', 'HÁU', 'como', 'sopro e depois “áu”'],
                ['hello', 'he-LÔU', 'olá', 'o primeiro “h” é um sopro suave']],
            pairs=[['hi', 'eye', 'com sopro × sem sopro'], ['hat', 'at', '“chapéu” × “em, no”'], ['heat', 'eat', '“calor” × “comer”'],
                   ['hear', 'ear', '“ouvir” × “orelha”']],
            tip='Coloque a mão na frente da boca e diga **hi**: você deve sentir o ar. Em **eye** não sai ar.',
            phrase=['Hey, how are you?', 'Ei, como vai você?'],
            rounds=[rnd('hat', 'at', '**Hat** (chapéu) começa com um sopro de ar: “h”.'),
                    rnd('eye', 'hi', '**Eye** (olho) começa direto na vogal. **Hi** tem o sopro.'),
                    rnd('hear', 'ear', '**Hear** (ouvir) começa com sopro. **Ear** (orelha) não.')]),
        hunt=[hunt_t('heat', 'eat', '**heat** (calor) tem o sopro do “h”.'),
              hunt_p('hat', ['🎩', '👂', '👁️'], '**hat** = chapéu.'),
              hunt_t('old', 'hold', '**old** (velho) começa sem sopro.'),
              hunt_p('ear', ['👂', '🎩', '👁️'], '**ear** = orelha.'),
              hunt_t('hi', 'eye', '**hi** (oi) tem o sopro do “h”.')])
    VB = dict(title='Verbos para encontros e despedidas', tip='Quatro verbos: meet, leave, talk e ride.', items=[
        verb('meet', '🤝', 'encontrar, conhecer', 'I meet my friends here.', 'Richie meet**s** Fonzie.', ['I meet my friends here.', 'Eu encontro meus amigos aqui.'], 'meets'),
        verb('leave', '🚪', 'sair, ir embora', 'I leave at six.', 'Joanie leave**s** early.', ['I leave at six.', 'Eu saio às seis.'], 'leaves'),
        verb('talk', '💬', 'conversar', 'I talk to Joanie.', 'He talk**s** to everyone.', ['I talk to Joanie.', 'Eu converso com a Joanie.'], 'talks'),
        verb('ride', '🏍️', 'andar de (moto, bicicleta)', 'I ride a bike.', 'Fonzie ride**s** a motorcycle.', ['I ride a bike.', 'Eu ando de bicicleta.'], 'rides')])
    MR = dict(
        mold=[pg('Perguntar como vai', [('oi', [('Hey!', 'ei!'), ('Hi!', 'oi!'), ('Hello!', 'olá!')]),
                                        ('pergunta', [("How's it going?", 'Como vai?'), ("How's it going, buddy?", 'Como vai, amigão?'), ("How's it going, Joanie?", 'Como vai, Joanie?')])], end=('', '')),
              pg('Responder', [('como estou', [('Great!', 'Ótimo!'), ('Pretty good!', 'Bem legal!'), ('Not bad.', 'Nada mal.'), ('So-so.', 'Mais ou menos.')]),
                               ('complemento', [('You?', 'E você?'), ('Thanks!', 'Obrigado!'), ('A little tired.', 'Um pouco cansado.')])], end=('', '')),
              pg('Despedir', [('despedida', [('See you later!', 'Até mais tarde!'), ('See you soon!', 'Até logo!'), ('Bye!', 'Tchau!')]),
                              ('final', [('Take care!', 'Se cuide!'), ('Bye!', 'Tchau!'), ('Ayyy!', 'Ayyy!')])], end=('', ''))],
        speak=[["Hey! How's it going?", 'Ei! Como vai?'], ['Not bad. See you later!', 'Nada mal. Até mais tarde!']],
        trap=[mtrap('“Not bad” quer dizer…', ['Nada mal, está bem.', 'Muito ruim.', 'Não tenho nada.'], '**Not bad.** = nada mal, tudo bem.', 'Not bad.'),
              mtrap('Qual frase está certa?', ['See you later, Joanie!', 'See you later, Joanie?!', 'Look you later, Joanie!'], 'A despedida é **See you later!**')],
        gap=[mgap("How's it ___?", 'Como vai?', ['going', 'go', 'goes'], "**How's it going?** = como vai?", "How's it going?"),
             mgap('Bye! See you ___!', 'Tchau! Até logo!', ['soon', 'now', 'ago'], '**See you soon!** = até logo!', 'See you soon!')],
        expq=[expq('Um amigo chega e você quer saber como ele está.', ["How's it going?", 'See you later!', 'Take care.'], "**How's it going?** = como vai?"),
              expq('Você sai da lanchonete e se despede com carinho.', ['Take care.', 'Not bad.', "How's it going?"], '**Take care.** = se cuide.'),
              expq('Alguém pergunta como vai e está tudo mais ou menos bem.', ['Not bad.', 'See you later!', 'Take care.'], '**Not bad.** = nada mal.')],
        missions=[mission('🍔', 'Encontro na lanchonete', 'Pergunte, responda e se despeça.',
                          prompt="Você encontra um amigo na lanchonete. **Pergunte How's it going?, responda com Pretty good ou Not bad e se despeça com See you later.**",
                          chips=["How's it going?", 'Pretty good.', 'See you later!'], model="How's it going? Pretty good, thanks. See you later!",
                          check=["Perguntei How's it going?", 'Respondi como estou?', 'Me despedi com See you later?'],
                          kw=['\\bhow[\'’]?s it going\\b', '\\b(?:pretty good|not bad|great)\\b', '\\bsee you (?:later|soon)\\b'],
                          tips=[[("How's it going?", 'Como vai?')], [('Pretty good.', 'Bem legal.'), ('Not bad.', 'Nada mal.')], [('See you later!', 'Até mais tarde!')]],
                          ok=['Boa pergunta! ❓', 'Resposta natural! 👍', 'Até mais! 👋'], reply=['Ayyy! Bye, see you soon!', 'Ayyy! Tchau, até logo!']),
              mission('💛', 'Se cuide', 'Despeça-se com carinho de um amigo cansado.',
                      prompt='Seu amigo está cansado e vai para casa. **Pergunte Are you okay?, diga Take care e se despeça com Bye.**',
                      chips=['Are you okay?', 'Take care.'], model='Are you okay? Take care! Bye!',
                      check=['Perguntei Are you okay?', 'Disse Take care?', 'Disse Bye?'],
                      kw=['\\bare you (?:okay|ok)\\b', '\\btake care\\b', '\\bbye\\b'],
                      tips=[[('Are you okay?', 'Você está bem?')], [('Take care.', 'Se cuide.')], [('Bye!', 'Tchau!')]],
                      ok=['Atencioso! 🫶', 'Se cuide! 💛', 'Tchau! 👋'], reply=['Thanks! Bye, see you soon!', 'Obrigado! Tchau, até logo!'])])
    CX = cx([('My team won the game today. It is a ___ day!', 'Meu time ganhou hoje. É um dia ótimo!', ['great', 'later', 'care']),
             ('Dinner was horrible. The food was ___.', 'O jantar foi horrível. A comida estava ruim.', ['bad', 'soon', 'care']),
             ('I have a test, so I cannot talk now. Bye, see you ___!', 'Tenho uma prova, então não posso falar agora. Tchau, até mais tarde!', ['later', 'great', 'bad']),
             ('The bus comes in one minute. It is coming ___.', 'O ônibus chega em um minuto. Ele chega logo.', ['soon', 'bad', 'care']),
             ('You are sick? Take ___ of yourself!', 'Você está doente? Cuide-se!', ['care', 'bad', 'soon']),
             ('The pizza is delicious. It is very ___.', 'A pizza está deliciosa. Está muito boa.', ['good', 'later', 'soon'])])
    return build(7910001, B, X, XT, VB, MR, CX)


# ---------------------------------------------------------------- pos 17 · Five Little Ducks · How much is…? 1 a 5
def ep17():
    MAMA, LIT, FROG = 'e:🦆', 'e:🐥', 'e:🐸'
    cast = {'Mama Duck': ['🦆', '#F9A825'], 'Little Duck': ['🐥', '#FBC02D'], 'Mr. Frog': ['🐸', '#43A047']}
    B = dict(
        title='Quanto custa? · How much is it?',
        sub='Perguntar o preço e dizer os números de um a cinco',
        pattern_label='How much is…?',
        why='Hoje você aprende a perguntar o preço com How much is…? e a responder com os números de um a cinco.',
        vocab=[['One', 'Um', 'Soa como “UÃN”.'], ['Two', 'Dois', 'Soa como “TUU”.'], ['Three', 'Três', 'Soa como “THRÍ”, com a língua entre os dentes.'],
               ['Four', 'Quatro', 'Soa como “FÓR”.'], ['Five', 'Cinco', 'Soa como “FÁIV”.'], ['Dollar', 'Dólar', 'Soa como “DÓ-ler”.']],
        balloons=[['1️⃣', 'one'], ['2️⃣', 'two'], ['3️⃣', 'three'], ['4️⃣', 'four'], ['5️⃣', 'five'], ['💵', 'dollar']],
        cover_art=cover('fair', [('🦆', 100, 56, 20), ('🎈', 138, 42, 14), ('💵', 84, 32, 12)], 'fd1'),
        cover_sub='How much is…? Em 10 minutos você pergunta o preço e conta até cinco',
        cover_say='A mamãe pata leva os patinhos à feira. Tudo tem preço! Como perguntar quanto custa e entender a resposta?',
        wrap_recap=[['How much is the game?', 'Quanto custa o jogo?'], ["It's four dollars.", 'São quatro dólares.'], ['One dollar.', 'Um dólar.'], ['Two dollars, please.', 'Dois dólares, por favor.']],
        teaser={'t': 'Stuart Little', 'd': 'Próximo padrão: pedir uma quantidade (I need two tickets) e contar de um a cinco'},
        cast=cast,
        lines=[['Mama Duck', 'Quack! How much is the game?', 'Quac! Quanto custa o jogo?'],
               ['Mr. Frog', "It's four dollars.", 'São quatro dólares.'],
               ['Little Duck', 'Mama, how much is the balloon?', 'Mamãe, quanto custa o balão?'],
               ['Mr. Frog', "It's three dollars.", 'São três dólares.'],
               ['Mama Duck', 'Wow! How much is the apple?', 'Uau! Quanto custa a maçã?'],
               ['Mr. Frog', 'The apple is two dollars.', 'A maçã custa dois dólares.'],
               ['Mama Duck', 'Okay! The game, please. Four dollars.', 'Certo! O jogo, por favor. Quatro dólares.'],
               ['Mr. Frog', 'Thank you! Five ducks, five smiles!', 'Obrigado! Cinco patinhos, cinco sorrisos!']],
        quiz=[quiz('How much is the balloon?', 'Quanto custa o balão?', [('3️⃣', 'Three dollars'), ('4️⃣', 'Four dollars'), ('2️⃣', 'Two dollars')], 3, 'O Sr. Sapo diz: “It’s three dollars.”'),
              quiz('How much is the game?', 'Quanto custa o jogo?', [('4️⃣', 'Four dollars'), ('1️⃣', 'One dollar'), ('5️⃣', 'Five dollars')], 1, 'O Sr. Sapo diz: “It’s four dollars.”'),
              quiz('How much is the apple?', 'Quanto custa a maçã?', [('2️⃣', 'Two dollars'), ('3️⃣', 'Three dollars'), ('1️⃣', 'One dollar')], 5, 'O Sr. Sapo diz: “The apple is two dollars.”')],
        rdg_q=rdg('Como perguntar o preço do balão?', ['How much is the balloon?', 'How many is the balloon?', 'What much is the balloon?'],
                  'Para **preço**, use **How much is**…? (Quanto custa…?)'),
        dictate=[['How much is the game?', 'Quanto custa o jogo?'], ["It's four dollars.", 'São quatro dólares.'], ['One dollar, please.', 'Um dólar, por favor.'], ['Five little ducks!', 'Cinco patinhos!']],
        produce=prod('Você está na feira e quer comprar uma maçã. **Pergunte o preço com How much is…? Diga um número de 1 a 5 e use please.**',
                     ['How much is', 'dollars', 'please'],
                     'How much is the apple? Two dollars? One apple, please.',
                     ['Perguntei com How much is…?', 'Usei um número de 1 a 5?', 'Usei please?'],
                     ['\\bhow much is\\b[^.!?]*\\?', '\\b(?:one|two|three|four|five)\\b', '\\bplease\\b'],
                     [[('How much is the apple?', 'Quanto custa a maçã?')], [('Two dollars.', 'Dois dólares.'), ('Five dollars.', 'Cinco dólares.')], [('Please.', 'Por favor.')]],
                     ['Pergunta de preço! 💵', 'Número certo! 🔢', 'Educado! 🙏'],
                     ['Yes! The apple is two dollars. Here you are!', 'Sim! A maçã custa dois dólares. Aqui está!']),
        rs=rsmap(3, 'fair'), sc='fair')
    X = dict(
        names=['Mama Duck', 'Mr. Frog'],
        stage=dict(rs='fair', chars=[[MAMA, 26, 0, 1.0], [LIT, 54, 1, 0.8], [FROG, 84, 1, 1.0]]),
        obra=dict(name='Five Little Ducks', kind='🎶 Rima infantil · tradicional', year='tradicional',
                  text='Canção infantil tradicional em inglês, usada para ensinar a contar. Cinco patinhos saem para passear. A mamãe pata chama “quack, quack, quack” e os patinhos voltam, um a um.',
                  line=['Quack, quack, quack, quack!', 'Quac, quac, quac, quac! (a mamãe pata chama)'],
                  pa=dict(t='river', e=['🦆', '🐥', '💵'], p='f', v=1)),
        gancho=['Mama Duck', 'Quack! How much is the game?', 'Quac! Quanto custa o jogo?'],
        hot=hots([('🎈', 'balloon', 'balão', 'The balloon is three dollars.', 'O balão custa três dólares.'),
                  ('🍎', 'apple', 'maçã', 'The apple is two dollars.', 'A maçã custa dois dólares.'),
                  ('💵', 'dollar', 'dólar', 'One dollar, please.', 'Um dólar, por favor.'),
                  ('🎟️', 'ticket', 'bilhete', 'How much is a ticket?', 'Quanto custa um bilhete?'),
                  ('🦆', 'duck', 'pato', 'Five little ducks!', 'Cinco patinhos!')]),
        gap=[gap('How ___ is the game?', 'Quanto custa o jogo?', ['much', 'many', 'long'], 'Para preço: **How much**…?'),
             gap("It's two ___.", 'São dois dólares.', ['dollars', 'dollar', 'dollares'], 'Dois ou mais: **dollars** (com -s).'),
             gap('One ___, please.', 'Um dólar, por favor.', ['dollar', 'dollars', "dollar's"], 'Só um: **one dollar** (sem -s).'),
             gap('How much ___ the balloon?', 'Quanto custa o balão?', ['is', 'are', 'do'], 'Uma coisa só: **How much is** the balloon?')],
        trap=[trap(['How much is it?', 'How much it is?', 'How is much it?'], 'Na pergunta o verbo vem antes: **How much is it?**'),
              trap(["It's three dollars.", "It's three dollar.", 'Is three dollars.'], 'Três dólares: **dollars** com -s. Em inglês a frase precisa de sujeito: **It\'s**…')],
        sticker=dict(title='Patinhos na feira', sub='Five Little Ducks · tradicional', rs='pool', chars=[[MAMA, 34, 0, 1.0], [LIT, 68, 1, 0.8]]),
        speakers={'Mama Duck': MAMA, 'Little Duck': LIT, 'Mr. Frog': FROG},
        rule=dict(
            who=MAMA, head='How much is…?', sub='Para perguntar o preço e dizer quanto custa.',
            say=['How much is the game?', 'Quanto custa o jogo?'],
            formula=[dict(from_=[['The game', 0], ['is', 1], ['four dollars.', 2]], to=[['How much', 3], ['is', 1], ['the game?', 0]],
                          say='How much is the game?', note='Troque o preço por **How much** e o verbo vem na frente.'),
                     dict(from_=[['one', 0], ['dollar', 1]], to=[['two', 0], ['dollars', 2]],
                          say='two dollars', note='Só **one** fica sem -s. De **two** em diante: **dollars**.')],
            uses=[dict(ico='🎈', tag='Perguntar', en='How much is the balloon?', pt='Quanto custa o balão?'),
                  dict(ico='💬', tag='Responder', en="It's three dollars.", pt='São três dólares.'),
                  dict(ico='1️⃣', tag='Um só', en='One dollar.', pt='Um dólar.'),
                  dict(ico='5️⃣', tag='Vários', en='Five dollars.', pt='Cinco dólares.')],
            rules=[dict(tag='How much is', c=0, text='Para o **preço** de uma coisa: How much is the game?', ex='How much is the apple?'),
                   dict(tag="It's + número", c=1, text='Na resposta, diga **It\'s** + número + dollar(s).', ex="It's two dollars."),
                   dict(tag='one × dollars', c=2, text='**One dollar**, mas **two dollars**: plural com -s.', ex='one dollar · two dollars')],
            tips=['Não traduza “custa” por **cost**. Em inglês fica **How much is…?** (Quanto é…?).']),
        mission_ic='💵')
    XT = dict(
        exp=[exp('💵', 'How much is it?', 'Expressão', 'Quanto custa?', 'Quando você quer saber o **preço** de algo que está apontando.', ['How much is it? It looks nice.', 'Quanto custa? Parece bom.']),
             exp('🤲', 'Here you are.', 'Expressão', 'Aqui está.', 'Ao **entregar** algo a alguém: dinheiro, bilhete, troco.', ['Here you are. Four dollars.', 'Aqui está. Quatro dólares.']),
             exp('😮', "That's too much!", 'Informal', 'É caro demais!', 'Quando o preço parece **alto** para você.', ["Five dollars? That's too much!", 'Cinco dólares? É caro demais!']),
             exp('🤝', 'Deal!', 'Informal', 'Fechado!', 'Quando você **aceita** o preço.', ['Two dollars? Deal!', 'Dois dólares? Fechado!'])],
        exp_scene=dict(rs='supermarket', lines=[
            ['Little Duck', '**How much is it**, Mama?', 'Quanto custa, mamãe?'],
            ['Mr. Frog', "It's five dollars.", 'São cinco dólares.'],
            ['Mama Duck', "Five dollars? **That's too much!**", 'Cinco dólares? É caro demais!'],
            ['Mr. Frog', 'Okay! Four dollars.', 'Certo! Quatro dólares.'],
            ['Mama Duck', '**Deal!** **Here you are.**', 'Fechado! Aqui está.'],
            ['Mr. Frog', 'Thank you! Quack, quack!', 'Obrigado! Quac, quac!']]),
        lab=dict(
            short='th de three', title='Laboratório de sons: o “th” de three',
            say='O “th” inglês não existe em português. Vamos treinar com os números dos patinhos.',
            intro=dict(what='O **th** de **three**, **thank** e **thanks** é um sopro com a língua entre os dentes.',
                       how='Coloque a ponta da língua entre os dentes de cima e de baixo e sopre o ar. Não use a voz e não feche a língua atrás dos dentes.',
                       pt='Muitos brasileiros dizem **tree** (árvore) ou **free** (grátis) no lugar de **three** (três). A língua entre os dentes muda a palavra!'),
            ex=[['three', 'THRÍ', 'três', 'língua entre os dentes, sopro'], ['thank', 'THÉNK', 'agradecer', 'sopro leve, sem voz'],
                ['think', 'THÍNK', 'pensar', 'língua para fora e sopro']],
            pairs=[['three', 'tree', 'th: língua entre os dentes · t: ponta atrás dos dentes'], ['thank', 'tank', '“agradecer” × “tanque”'],
                   ['think', 'sink', 'th × s: “pensar” × “pia”'], ['thin', 'tin', '“fino” × “lata”']],
            tip='Mostre a ponta da língua no espelho ao dizer **three**. Se ela não aparece, vira “tree”.',
            phrase=['Thank you! Three dollars.', 'Obrigado! Três dólares.'],
            rounds=[rnd('three', 'tree', '**Three** (três) tem a língua entre os dentes. **Tree** (árvore) começa com “t”.'),
                    rnd('tank', 'thank', '**Tank** (tanque) começa com “t”. **Thank** tem o “th”.'),
                    rnd('think', 'sink', '**Think** (pensar) tem o “th”. **Sink** (pia) começa com “s”.')]),
        hunt=[hunt_t('thin', 'tin', '**thin** (fino) começa com “th”.'),
              hunt_p('three', ['3️⃣', '5️⃣', '2️⃣'], '**three** = três.'),
              hunt_t('sink', 'think', '**sink** (pia) começa com “s”.'),
              hunt_p('five', ['5️⃣', '4️⃣', '1️⃣'], '**five** = cinco.'),
              hunt_t('tree', 'three', '**tree** (árvore) começa com “t”.')])
    VB = dict(title='Verbos para pagar e contar', tip='Quatro verbos: pay, buy, count e swim.', items=[
        verb('pay', '💵', 'pagar', 'I pay four dollars.', 'Mama Duck pay**s** at the game.', ['I pay four dollars.', 'Eu pago quatro dólares.'], 'pays'),
        verb('buy', '🛍️', 'comprar', 'I buy an apple.', 'Little Duck buy**s** a balloon.', ['I buy an apple.', 'Eu compro uma maçã.'], 'buys'),
        verb('count', '🔢', 'contar', 'I count to five.', 'Mama Duck count**s** the ducks.', ['I count to five.', 'Eu conto até cinco.'], 'counts'),
        verb('swim', '🏊', 'nadar', 'I swim in the pond.', 'The duck swim**s** fast.', ['I swim in the pond.', 'Eu nado no lago.'], 'swims')])
    MR = dict(
        mold=[pg('Perguntar o preço', [('pergunta', [('How much is', 'quanto custa')]),
                                       ('coisa', [('the game', 'o jogo'), ('the balloon', 'o balão'), ('the apple', 'a maçã'), ('a ticket', 'um bilhete'), ('this', 'isto')])]),
              pg('Dizer o preço', [('começo', [("It's", 'custa'), ('The game is', 'o jogo custa'), ('The apple is', 'a maçã custa')]),
                                   ('preço', [('one dollar', 'um dólar'), ('two dollars', 'dois dólares'), ('three dollars', 'três dólares'), ('four dollars', 'quatro dólares'), ('five dollars', 'cinco dólares')])], end=('.', '.')),
              pg('Pedir', [('pedido', [('The game,', 'o jogo,'), ('The apple,', 'a maçã,'), ('The balloon,', 'o balão,')]),
                           ('educação', [('please.', 'por favor.'), ('thank you.', 'obrigado.')])], end=('', ''))],
        speak=[['How much is the balloon?', 'Quanto custa o balão?'], ["It's three dollars. Deal!", 'São três dólares. Fechado!']],
        trap=[mtrap('“That’s too much!” quer dizer…', ['É caro demais!', 'É muito barato!', 'Gosto muito!'], "**That's too much!** = é caro demais.", "That's too much!"),
              mtrap('Qual frase está certa?', ["It's two dollars.", "It's two dollar.", 'Two dollar is.'], 'Dois dólares: **dollars** com -s.')],
        gap=[mgap('___ you are. Two dollars.', 'Aqui está. Dois dólares.', ['Here', 'There', 'Where'], '**Here you are.** = aqui está.', 'Here you are.'),
             mgap('Five dollars? ___!', 'Cinco dólares? Fechado!', ['Deal', 'Dealing', 'Dollar'], '**Deal!** = fechado!', 'Deal!')],
        expq=[expq('Você está entregando dinheiro ao vendedor.', ['Here you are.', 'Deal!', 'How much is it?'], '**Here you are.** = aqui está.'),
              expq('O preço é muito alto para você.', ["That's too much!", 'Deal!', 'Here you are.'], "**That's too much!** = é caro demais!"),
              expq('Você quer saber quanto custa um brinquedo.', ['How much is it?', 'Deal!', 'Here you are.'], '**How much is it?** = quanto custa?')],
        missions=[mission('🍎', 'Na feira', 'Pergunte o preço e peça com educação.',
                          prompt='Você quer um balão na feira. **Pergunte o preço com How much is…? e peça o balão com please. Use um número de 1 a 5.**',
                          chips=['How much is', 'three dollars', 'please'],
                          model='How much is the balloon? Three dollars? One balloon, please.',
                          check=['Perguntei com How much is…?', 'Usei um número de 1 a 5?', 'Usei please?'],
                          kw=['\\bhow much is\\b[^.!?]*\\?', '\\b(?:one|two|three|four|five)\\b', '\\bplease\\b'],
                          tips=[[('How much is the balloon?', 'Quanto custa o balão?')], [('Three dollars.', 'Três dólares.')], [('Please.', 'Por favor.')]],
                          ok=['Preço perguntado! 🎈', 'Número certo! 🔢', 'Educado! 🙏'], reply=["Yes! It's three dollars. Here you are!", 'Sim! São três dólares. Aqui está!']),
              mission('🤝', 'Fechado!', 'Use as expressões para negociar.',
                      prompt='O vendedor diz: *It\'s five dollars.* **Diga That\'s too much ou Deal, entregue o dinheiro com Here you are e agradeça.**',
                      chips=['Deal!', 'Here you are.'], model='Deal! Here you are. Thank you!',
                      check=["Disse That's too much ou Deal?", 'Disse Here you are?', 'Agradeci?'],
                      kw=['\\b(?:too much|deal)\\b', '\\bhere you are\\b', '\\bthank'],
                      tips=[[("That's too much!", 'É caro demais!'), ('Deal!', 'Fechado!')], [('Here you are.', 'Aqui está.')], [('Thank you.', 'Obrigado.')]],
                      ok=['Negociou! 🤝', 'Entregou! 🤲', 'Obrigado! 😊'], reply=['Thank you! Have fun at the fair!', 'Obrigado! Divirta-se na feira!'])])
    CX = cx([('Two plus two is ___.', 'Dois mais dois é quatro.', ['four', 'three', 'one']),
             ('One plus one is ___.', 'Um mais um é dois.', ['two', 'five', 'four']),
             ('One plus two is ___.', 'Um mais dois é três.', ['three', 'one', 'five']),
             ('Four plus one is ___.', 'Quatro mais um é cinco.', ['five', 'three', 'two']),
             ('Two minus one is ___.', 'Dois menos um é um.', ['one', 'two', 'four']),
             ('In the United States, the money is the ___.', 'Nos Estados Unidos, a moeda é o dólar.', ['dollar', 'five', 'one'])])
    return build(9804, B, X, XT, VB, MR, CX)


# ---------------------------------------------------------------- pos 18 · Stuart Little · How many…? + plural, 1 a 5
def ep18():
    STU, MRS, SNO = 'e:🐭', 'p:bun:8d6e63:f4c7a1:7e57c2:none:dress', 'e:🐱'
    cast = {'Stuart': ['🐭', '#8D6E63'], 'Mrs. Little': ['👩', '#7E57C2'], 'Snowbell': ['🐱', '#78909C']}
    B = dict(
        title='Quantos? · How many…?',
        sub='Contar de 1 a 5 e pedir quantidades: How many…? I need three tickets.',
        pattern_label='How many…? + número',
        why='Hoje você aprende a perguntar quantos com How many…? e a pedir coisas com número: I need three tickets.',
        vocab=[['Ticket', 'Bilhete, passagem', 'Soa como “TÍ-ket”.'], ['Coin', 'Moeda', 'Soa como “KÓIN”.'], ['Stop', 'Parada', 'Soa como “STÓP”.'],
               ['Minute', 'Minuto', 'Soa como “MÍ-nit”.'], ['Card', 'Cartão', 'Soa como “KÁRD”.'], ['Cat', 'Gato', 'Soa como “KÉT”.']],
        balloons=[['🎫', 'ticket'], ['🪙', 'coin'], ['🛑', 'stop'], ['⏱️', 'minute'], ['💳', 'card'], ['🐱', 'cat']],
        cover_art=cover('traincar', [('🎫', 100, 56, 18), ('🐭', 138, 42, 14), ('🪙', 84, 32, 12)], 'st1'),
        cover_sub='How many…? Em 10 minutos você pede quantidades como o Stuart',
        cover_say='O ratinho Stuart vai de metrô por Nova York com a mãe e o gato. Quantos bilhetes? Quantas moedas? Vamos contar!',
        wrap_recap=[['How many tickets?', 'Quantos bilhetes?'], ['I need three tickets.', 'Preciso de três bilhetes.'], ['Five coins.', 'Cinco moedas.'], ['Four stops, five minutes.', 'Quatro paradas, cinco minutos.']],
        teaser={'t': 'Monopoly', 'd': 'Próximo padrão: preços de 6 a 10 (It\'s ten dollars)'},
        cast=cast,
        lines=[['Mrs. Little', 'Stuart, how many tickets, please?', 'Stuart, quantos bilhetes, por favor?'],
               ['Stuart', 'I need three tickets. You, me and the cat.', 'Preciso de três bilhetes. Você, eu e o gato.'],
               ['Snowbell', "Meow! I'm a cat. No ticket!", 'Miau! Eu sou um gato. Sem bilhete!'],
               ['Mrs. Little', 'Yes, a ticket for the cat too.', 'Sim, um bilhete para o gato também.'],
               ['Stuart', 'Mom, how many coins?', 'Mamãe, quantas moedas?'],
               ['Mrs. Little', 'Five coins. Count, Stuart.', 'Cinco moedas. Conte, Stuart.'],
               ['Stuart', 'One, two, three, four, five!', 'Um, dois, três, quatro, cinco!'],
               ['Snowbell', 'Four stops, five minutes. Meow!', 'Quatro paradas, cinco minutos. Miau!']],
        quiz=[quiz('How many tickets?', 'Quantos bilhetes eles pedem?', [('3️⃣', 'Three tickets'), ('2️⃣', 'Two tickets'), ('5️⃣', 'Five tickets')], 1, 'Stuart diz: “I need three tickets.”'),
              quiz('How many coins?', 'Quantas moedas?', [('5️⃣', 'Five coins'), ('3️⃣', 'Three coins'), ('4️⃣', 'Four coins')], 5, 'A Sra. Little diz: “Five coins.”'),
              quiz('How many stops?', 'Quantas paradas?', [('4️⃣', 'Four stops'), ('1️⃣', 'One stop'), ('5️⃣', 'Five stops')], 7, 'Snowbell diz: “Four stops, five minutes.”')],
        rdg_q=rdg('Qual frase pede três bilhetes?', ['I need three tickets.', 'I need three ticket.', 'I need tickets three.'],
                  'Depois de **three**, o substantivo vai para o plural: **tickets**.'),
        dictate=[['How many tickets?', 'Quantos bilhetes?'], ['I need three tickets.', 'Preciso de três bilhetes.'], ['Five coins, please.', 'Cinco moedas, por favor.'], ['Four stops.', 'Quatro paradas.']],
        produce=prod('Você está na bilheteria do metrô. **Diga quantos bilhetes você precisa com I need + número + tickets e pergunte quantas moedas com How many…? Use please.**',
                     ['I need', 'tickets', 'How many'],
                     'I need two tickets, please. How many coins?',
                     ['Usei I need + número + tickets?', 'Perguntei com How many…?', 'Usei please?'],
                     ['\\bi need (?:two|three|four|five)\\b[^.!?]*\\btickets\\b', '\\bhow many\\b[^.!?]*\\?', '\\bplease\\b'],
                     [[('I need two tickets.', 'Preciso de dois bilhetes.')], [('How many coins?', 'Quantas moedas?')], [('Please.', 'Por favor.')]],
                     ['Quantidade certa! 🎫', 'Pergunta de contar! 🔢', 'Educado! 🙏'],
                     ['Two tickets? That is four coins. Here you are!', 'Dois bilhetes? São quatro moedas. Aqui está!']),
        rs=rsmap(4, 'traincar'), sc='traincar')
    X = dict(
        names=['Stuart', 'Mrs. Little'],
        stage=dict(rs='traincar', chars=[[STU, 26, 0, 0.8], [MRS, 54, 1, 1.0], [SNO, 84, 1, 0.9]]),
        obra=dict(name='Stuart Little', kind='📖 Livro infantil · 1945', year='1945',
                  text='Livro infantil do escritor americano E. B. White, publicado em 1945. Stuart é um ratinho que nasce na família Little, em Nova York, e vive aventuras pela cidade.',
                  line=['Three tickets, please.', 'Três bilhetes, por favor. (pedido típico de metrô)'],
                  pa=dict(t='tram', e=['🐭', '🚇', '🎫'], p='g', v=0)),
        gancho=['Mrs. Little', 'Stuart, how many tickets, please?', 'Stuart, quantos bilhetes, por favor?'],
        hot=hots([('🎫', 'ticket', 'bilhete', 'I need a ticket.', 'Preciso de um bilhete.'),
                  ('🪙', 'coin', 'moeda', 'I need five coins.', 'Preciso de cinco moedas.'),
                  ('💳', 'card', 'cartão', 'One card, please.', 'Um cartão, por favor.'),
                  ('⏱️', 'minute', 'minuto', 'Five minutes.', 'Cinco minutos.'),
                  ('🛑', 'stop', 'parada', 'Four stops.', 'Quatro paradas.')]),
        gap=[gap('How ___ tickets?', 'Quantos bilhetes?', ['many', 'much', 'more'], 'Para contar coisas no plural: **How many**…?'),
             gap('I need three ___.', 'Preciso de três bilhetes.', ['tickets', 'ticket', 'ticketes'], 'Depois de **three**: plural com -s.'),
             gap('One ___, please.', 'Uma moeda, por favor.', ['coin', 'coins', 'coines'], 'Só uma: singular, sem -s.'),
             gap('Four ___.', 'Quatro paradas.', ['stops', 'stop', 'stopes'], 'Quatro: **stops**, com -s.')],
        trap=[trap(['Three tickets, please.', 'Three ticket, please.', 'Tree ticket, please.'], 'Número a partir de dois: plural, **tickets**.'),
              trap(['How many coins?', 'How many coin?', 'How much coins?'], 'Coisas que se contam: **How many** + plural.')],
        sticker=dict(title='Stuart no metrô', sub='Stuart Little · 1945', rs='harbor', chars=[[STU, 34, 0, 0.8], [SNO, 68, 1, 0.9]]),
        speakers={'Stuart': STU, 'Mrs. Little': MRS, 'Snowbell': SNO},
        rule=dict(
            who=STU, head='How many…? + número', sub='Para perguntar e dizer quantos.',
            say=['How many tickets?', 'Quantos bilhetes?'],
            formula=[dict(from_=[['one', 0], ['ticket', 1]], to=[['three', 0], ['tickets', 2]],
                          say='three tickets', note='De **two** em diante, a palavra ganha **-s**: two tickets, five coins.'),
                     dict(from_=[['Three', 1], ['tickets.', 2]], to=[['How many', 3], ['tickets?', 2]],
                          say='How many tickets?', note='Para perguntar a quantidade, troque o número por **How many**.')],
            uses=[dict(ico='🎫', tag='Perguntar', en='How many tickets?', pt='Quantos bilhetes?'),
                  dict(ico='🔢', tag='Dizer quantos', en='Three tickets.', pt='Três bilhetes.'),
                  dict(ico='🪙', tag='Pedir', en='I need five coins.', pt='Preciso de cinco moedas.'),
                  dict(ico='1️⃣', tag='Só um', en='One cat.', pt='Um gato.')],
            rules=[dict(tag='How many + plural', c=0, text='Para **contar** coisas: How many coins? How many stops?', ex='How many tickets?'),
                   dict(tag='número + -s', c=1, text='**One** fica no singular. De **two** a **five**: plural com **-s**.', ex='one coin · two coins · five coins'),
                   dict(tag='I need…', c=2, text='Para pedir: **I need** + número + coisa.', ex='I need two tickets.')],
            tips=['**How much** é para preço (How much is it?). **How many** é para contar (How many tickets?).']),
        mission_ic='🎫')
    XT = dict(
        exp=[exp('⚠️', 'Watch your step.', 'Expressão', 'Cuidado onde pisa.', 'Aviso em **estações e vagões**, ao entrar ou sair.', ['Watch your step, Stuart!', 'Cuidado onde pisa, Stuart!']),
             exp('🚪', 'Hold the door!', 'Informal', 'Segure a porta!', 'Quando você corre para **pegar o trem**.', ['Hold the door, please!', 'Segure a porta, por favor!']),
             exp('📣', 'Over here!', 'Informal', 'Aqui!', 'Para **chamar** alguém e mostrar onde você está.', ['Over here, Mom!', 'Aqui, mamãe!']),
             exp('🙋', 'Excuse me.', 'Expressão', 'Com licença. / Desculpe.', 'Para **chamar a atenção** ou passar por alguém.', ['Excuse me, I need a ticket.', 'Com licença, preciso de um bilhete.'])],
        exp_scene=dict(rs='nightcity', lines=[
            ['Stuart', '**Excuse me!** I need three tickets.', 'Com licença! Preciso de três bilhetes.'],
            ['Mrs. Little', '**Over here**, Stuart!', 'Aqui, Stuart!'],
            ['Snowbell', 'Meow! **Hold the door!**', 'Miau! Segure a porta!'],
            ['Mrs. Little', '**Watch your step**, Snowbell.', 'Cuidado onde pisa, Snowbell.'],
            ['Stuart', 'Five minutes. Four stops.', 'Cinco minutos. Quatro paradas.'],
            ['Snowbell', 'Meow! We are in New York!', 'Miau! Estamos em Nova York!']]),
        lab=dict(
            short='v × b', title='Laboratório de sons: o “v” de five e very',
            say='O “v” inglês é feito com os dentes no lábio. Vamos treinar com os números dos bilhetes.',
            intro=dict(what='O **v** de **five**, **very** e **van** é um som vibrado: o lábio de baixo toca os dentes de cima.',
                       how='Encoste os dentes de cima no lábio de baixo e deixe o ar passar fazendo a voz vibrar. No **b** os dois lábios se fecham e o ar sai de uma vez.',
                       pt='Alguns brasileiros trocam **v** por **b**: dizem “bery” em vez de **very** (muito). **Vote** (votar) ≠ **boat** (barco).'),
            ex=[['five', 'FÁIV', 'cinco', 'dentes no lábio e vibre até o fim'], ['very', 'VÉ-ri', 'muito', 'dentes no lábio, sem fechar os lábios'],
                ['van', 'VÉN', 'van, furgão', 'comece com os dentes no lábio']],
            pairs=[['vest', 'best', 'v: dentes no lábio · b: lábios fechados'], ['van', 'ban', '“van” × “proibição”'],
                   ['very', 'berry', '“muito” × “fruta vermelha”'], ['vote', 'boat', '“votar” × “barco”']],
            tip='Sinta o lábio vibrar ao dizer “vvv”. Se os lábios se fecham, saiu um “b”.',
            phrase=['I need five tickets, please.', 'Preciso de cinco bilhetes, por favor.'],
            rounds=[rnd('vest', 'best', '**Vest** (colete) começa com dentes no lábio: “v”.'),
                    rnd('ban', 'van', '**Ban** (proibir) fecha os lábios: “b”.'),
                    rnd('berry', 'very', '**Berry** (fruta) começa com “b”. **Very** começa com “v”.')]),
        hunt=[hunt_t('vote', 'boat', '**vote** (votar) começa com “v”.'),
              hunt_p('five', ['5️⃣', '4️⃣', '3️⃣'], '**five** = cinco.'),
              hunt_t('best', 'vest', '**best** (melhor) começa com “b”.'),
              hunt_p('cat', ['🐱', '🐭', '🐕'], '**cat** = gato.'),
              hunt_t('very', 'berry', '**very** (muito) começa com “v”.')])
    VB = dict(title='Verbos para andar de metrô', tip='Quatro verbos: need, show, sit e wait.', items=[
        verb('need', '🧾', 'precisar de', 'I need two tickets.', 'Stuart need**s** five coins.', ['I need two tickets.', 'Eu preciso de dois bilhetes.'], 'needs'),
        verb('show', '🪪', 'mostrar', 'I show my card.', 'Mrs. Little show**s** the ticket.', ['I show my card.', 'Eu mostro meu cartão.'], 'shows'),
        verb('sit', '💺', 'sentar', 'I sit on the train.', 'Snowbell sit**s** near the door.', ['I sit on the train.', 'Eu sento no trem.'], 'sits'),
        verb('wait', '⏳', 'esperar', 'I wait for the train.', 'Stuart wait**s** at the stop.', ['I wait for the train.', 'Eu espero o trem.'], 'waits')])
    MR = dict(
        mold=[pg('Perguntar quantos', [('pergunta', [('How many', 'quantos')]),
                                       ('coisa', [('tickets', 'bilhetes'), ('coins', 'moedas'), ('stops', 'paradas'), ('minutes', 'minutos'), ('cards', 'cartões')])]),
              pg('Pedir mais de um', [('começo', [('I need', 'preciso de')]), ('número', [('two', 'dois'), ('three', 'três'), ('four', 'quatro'), ('five', 'cinco')]),
                                      ('coisa', [('tickets', 'bilhetes'), ('coins', 'moedas'), ('cards', 'cartões')])], end=('.', '.')),
              pg('Pedir só um', [('começo', [('I need', 'preciso de')]), ('coisa', [('one ticket', 'um bilhete'), ('one coin', 'uma moeda'), ('one card', 'um cartão')])], end=(', please.', ', por favor.'))],
        speak=[['How many tickets? Three, please.', 'Quantos bilhetes? Três, por favor.'], ['Excuse me! Over here!', 'Com licença! Aqui!']],
        trap=[mtrap('“Watch your step” quer dizer…', ['Cuidado onde pisa.', 'Veja seu passo.', 'Espere sua vez.'], '**Watch your step.** = cuidado onde pisa.', 'Watch your step.'),
              mtrap('Qual frase está certa?', ['I need two coins.', 'I need two coin.', 'I need coins two.'], 'Depois de **two**: **coins** com -s.')],
        gap=[mgap('___ me! I need a ticket.', 'Com licença! Preciso de um bilhete.', ['Excuse', 'Sorry', 'Please'], '**Excuse me.** = com licença.', 'Excuse me! I need a ticket.'),
             mgap('Hold the ___!', 'Segure a porta!', ['door', 'doors', 'step'], '**Hold the door!** = segure a porta!', 'Hold the door!')],
        expq=[expq('Você quer passar por uma pessoa no vagão.', ['Excuse me.', 'Over here!', 'Watch your step.'], '**Excuse me.** = com licença.'),
              expq('Um amigo não vê você na estação cheia.', ['Over here!', 'Excuse me.', 'Hold the door!'], '**Over here!** = aqui!'),
              expq('O trem vai fechar a porta e você está correndo.', ['Hold the door!', 'Over here!', 'Excuse me.'], '**Hold the door!** = segure a porta!')],
        missions=[mission('🎫', 'Na bilheteria', 'Peça bilhetes e pergunte as moedas.',
                          prompt='Você está na estação e precisa de bilhetes. **Diga I need + número + tickets e pergunte How many coins? Use please.**',
                          chips=['I need', 'How many coins?', 'please'], model='I need three tickets, please. How many coins?',
                          check=['Disse I need + número + tickets?', 'Perguntei How many…?', 'Usei please?'],
                          kw=['\\bi need (?:two|three|four|five)\\b[^.!?]*\\btickets\\b', '\\bhow many\\b[^.!?]*\\?', '\\bplease\\b'],
                          tips=[[('I need three tickets.', 'Preciso de três bilhetes.')], [('How many coins?', 'Quantas moedas?')], [('Please.', 'Por favor.')]],
                          ok=['Bilhetes pedidos! 🎫', 'Pergunta de contar! 🔢', 'Educado! 🙏'], reply=['Three tickets? Five coins, please.', 'Três bilhetes? Cinco moedas, por favor.']),
              mission('🚇', 'No vagão cheio', 'Use as expressões do metrô.',
                      prompt='O vagão está cheio. **Diga Excuse me para passar, peça Hold the door! e avise a um amigo Watch your step.**',
                      chips=['Excuse me!', 'Hold the door!'], model='Excuse me! Hold the door! Watch your step!',
                      check=['Disse Excuse me?', 'Disse Hold the door?', 'Disse Watch your step?'],
                      kw=['\\bexcuse me\\b', '\\bhold the door\\b', '\\bwatch your step\\b'],
                      tips=[[('Excuse me.', 'Com licença.')], [('Hold the door!', 'Segure a porta!')], [('Watch your step.', 'Cuidado onde pisa.')]],
                      ok=['Educado! 🙋', 'Porta segura! 🚪', 'Cuidado! ⚠️'], reply=['Thank you! Next stop: Times Square.', 'Obrigado! Próxima parada: Times Square.'])])
    CX = cx([('You need it to ride the train. I need a ___.', 'Você precisa dele para andar de trem. Preciso de um bilhete.', ['ticket', 'cat', 'stop']),
             ('It is round and made of metal. You pay with it. It is a ___.', 'É redonda e de metal. Você paga com ela. É uma moeda.', ['coin', 'cat', 'minute']),
             ('The bus stops here. This is the bus ___.', 'O ônibus para aqui. Esta é a parada de ônibus.', ['stop', 'card', 'coin']),
             ('Wait one ___, please. I am coming.', 'Espere um minuto, por favor. Já vou.', ['minute', 'ticket', 'cat']),
             ('I do not have money. I pay with a credit ___.', 'Não tenho dinheiro. Pago com cartão de crédito.', ['card', 'cat', 'stop']),
             ('It says meow, it has whiskers and it sleeps a lot. It is a ___.', 'Faz miau, tem bigodes e dorme muito. É um gato.', ['cat', 'coin', 'card'])])
    return build(7009804, B, X, XT, VB, MR, CX)


# ---------------------------------------------------------------- pos 19 · Monopoly · Ten dollars, please. 6 a 10
def ep19():
    MON, SCO, BAN = 'p:short:f5f5f5:f4c7a1:263238:hat:suit', 'e:🐕', 'p:short:222222:c68642:2e7d32:glasses:suit'
    cast = {'Mr. Monopoly': ['🎩', '#263238'], 'Scottie': ['🐶', '#8D6E63'], 'Banker': ['🏦', '#2E7D32']}
    B = dict(
        title='Dez dólares, por favor · Ten dollars, please',
        sub='Contar de 6 a 10 e pedir ou cobrar valores: Ten dollars, please.',
        pattern_label='Número + dollars, please',
        why='Hoje você aprende os números de seis a dez e a pedir ou cobrar dinheiro: Ten dollars, please. That\'s eight dollars.',
        vocab=[['Six', 'Seis', 'Soa como “SÍKS”.'], ['Seven', 'Sete', 'Soa como “SÉ-ven”.'], ['Eight', 'Oito', 'Soa como “ÊIT”.'],
               ['Nine', 'Nove', 'Soa como “NÁIN”.'], ['Ten', 'Dez', 'Soa como “TÉN”.'], ['Bank', 'Banco', 'Soa como “BÉNK”.']],
        balloons=[['6️⃣', 'six'], ['7️⃣', 'seven'], ['8️⃣', 'eight'], ['9️⃣', 'nine'], ['🔟', 'ten'], ['🏦', 'bank']],
        cover_art=cover('bank', [('🏦', 100, 54, 18), ('🎩', 138, 42, 14), ('💵', 84, 32, 12)], 'mo1'),
        cover_sub='Ten dollars, please. Em 10 minutos você conta até dez e cobra como no Monopoly',
        cover_say='No jogo Monopoly, todo mundo paga e recebe dinheiro. Como pedir dez dólares? Como dizer o total?',
        wrap_recap=[['Ten dollars, please.', 'Dez dólares, por favor.'], ["That's seven dollars.", 'São sete dólares.'], ['Here you are.', 'Aqui está.'], ['Six, seven, eight, nine, ten.', 'Seis, sete, oito, nove, dez.']],
        teaser={'t': 'Spider-Man', 'd': 'Próximo padrão: números de 6 a 10 em trens e plataformas (Is this the seven train?)'},
        cast=cast,
        lines=[['Scottie', 'Woof! Banker, ten dollars, please.', 'Au! Banqueiro, dez dólares, por favor.'],
               ['Banker', 'Sure. Here you are, ten dollars.', 'Claro. Aqui está, dez dólares.'],
               ['Scottie', 'Thank you! Hello, Mr. Monopoly!', 'Obrigado! Olá, Sr. Monopoly!'],
               ['Mr. Monopoly', "Hello, Scottie! That's seven dollars, please.", 'Olá, Scottie! São sete dólares, por favor.'],
               ['Scottie', 'Seven dollars? Okay. Here you are, ten.', 'Sete dólares? Certo. Aqui está, dez.'],
               ['Mr. Monopoly', 'Thank you! Three dollars back.', 'Obrigado! Três dólares de volta.'],
               ['Scottie', 'I count: six, seven, eight, nine, ten!', 'Eu conto: seis, sete, oito, nove, dez!'],
               ['Banker', 'Good game, Scottie! Your turn!', 'Bom jogo, Scottie! Sua vez!']],
        quiz=[quiz('How much?', 'Quanto o Scottie pede ao Banqueiro?', [('🔟', 'Ten dollars'), ('7️⃣', 'Seven dollars'), ('8️⃣', 'Eight dollars')], 0, 'Scottie diz: “ten dollars, please.”'),
              quiz('How much is the street?', 'Quanto custa a rua?', [('7️⃣', 'Seven dollars'), ('🔟', 'Ten dollars'), ('6️⃣', 'Six dollars')], 3, 'Mr. Monopoly diz: “That’s seven dollars.”'),
              quiz('How much is the change?', 'Quanto é o troco?', [('3️⃣', 'Three dollars'), ('9️⃣', 'Nine dollars'), ('2️⃣', 'Two dollars')], 5, 'Ele diz: “Three dollars back.”')],
        rdg_q=rdg('Como cobrar sete dólares?', ["That's seven dollars.", "That seven dollars.", "That's seven dollar."],
                  'Total: **That\'s** + número + **dollars** (plural).'),
        dictate=[['Ten dollars, please.', 'Dez dólares, por favor.'], ["That's seven dollars.", 'São sete dólares.'], ['Here you are.', 'Aqui está.'], ['Six, seven, eight, nine, ten.', 'Seis, sete, oito, nove, dez.']],
        produce=prod('Você joga Monopoly. **Peça dinheiro ao banqueiro com um número de 6 a 10 + dollars, please. Depois diga um total com That\'s… e agradeça.**',
                     ['Ten dollars, please.', "That's", 'Thank you.'],
                     "Eight dollars, please. That's eight dollars. Thank you!",
                     ['Pedi com número de 6 a 10 + dollars?', "Disse um total com That's…?", 'Agradeci?'],
                     ['\\b(?:six|seven|eight|nine|ten) dollars\\b', '\\bthat[\'’]?s (?:six|seven|eight|nine|ten)\\b', '\\bthank'],
                     [[('Ten dollars, please.', 'Dez dólares, por favor.')], [("That's nine dollars.", 'São nove dólares.')], [('Thank you.', 'Obrigado.')]],
                     ['Pedido feito! 💵', 'Total dito! 🧾', 'Obrigado! 😊'],
                     ['Here you are! Good game!', 'Aqui está! Bom jogo!']),
        rs=rsmap(5, 'bank'), sc='bank')
    X = dict(
        names=['Scottie', 'Banker'],
        stage=dict(rs='bank', chars=[[SCO, 26, 0, 0.8], [BAN, 54, 1, 1.0], [MON, 84, 1, 1.0]]),
        obra=dict(name='Monopoly', kind='🎲 Jogo de tabuleiro · 1935', year='1935',
                  text='Jogo de tabuleiro da empresa americana Parker Brothers, lançado em 1935. Os jogadores compram ruas, pagam aluguel e usam dinheiro de papel. O Sr. Monopoly é o personagem símbolo do jogo, e o cachorro Scottie é um dos pinos.',
                  line=['Go to jail.', 'Vá para a cadeia. (carta famosa do jogo)'],
                  pa=dict(t='vault', e=['🎲', '🏦', '🎩'], p='h', v=0)),
        gancho=['Scottie', 'Woof! Banker, ten dollars, please.', 'Au! Banqueiro, dez dólares, por favor.'],
        hot=hots([('🏦', 'bank', 'banco', 'Ten dollars, please.', 'Dez dólares, por favor.'),
                  ('🪙', 'coin', 'moeda', 'Six coins, please.', 'Seis moedas, por favor.'),
                  ('💵', 'money', 'dinheiro', "That's eight dollars.", 'São oito dólares.'),
                  ('🎩', 'hat', 'cartola', 'Hello, Mr. Monopoly!', 'Olá, Sr. Monopoly!'),
                  ('🎲', 'dice', 'dados', 'Six and four is ten.', 'Seis e quatro são dez.')]),
        gap=[gap('Ten ___, please.', 'Dez dólares, por favor.', ['dollars', 'dollar', 'dolars'], 'Dez: mais de um, então **dollars** com -s.'),
             gap("___ seven dollars.", 'São sete dólares.', ["That's", 'Is', 'Thats'], 'Para dizer o total: **That\'s** seven dollars.'),
             gap('Here you ___.', 'Aqui está.', ['are', 'is', 'am'], 'A expressão é **Here you are.**'),
             gap('Seven dollars, ___.', 'Sete dólares, por favor.', ['please', 'pleased', 'pleases'], 'Para pedir com educação: **please**.')],
        trap=[trap(['Ten dollars, please.', 'Ten dollar, please.', 'Tens dollars, please.'], 'Dez dólares: **dollars** com -s, e **ten** nunca leva -s.'),
              trap(["It's eight dollars.", 'Its eight dollars.', 'It eight dollars.'], 'Contração certa: **It\'s** (It is). Sem apóstrofo seria posse.')],
        sticker=dict(title='Scottie no banco', sub='Monopoly · 1935', rs='fair', chars=[[SCO, 34, 0, 0.8], [MON, 68, 1, 1.0]]),
        speakers={'Mr. Monopoly': MON, 'Scottie': SCO, 'Banker': BAN},
        rule=dict(
            who=MON, head='Número + dollars, please', sub='Para pedir e cobrar dinheiro de 6 a 10.',
            say=['Ten dollars, please.', 'Dez dólares, por favor.'],
            pairsHead='🔢 Número → valor',
            pairs=[dict(ico='6️⃣', a='six', b='<u>six dollars</u>, please.', pta='seis', ptb='seis dólares, por favor.', n=6),
                   dict(ico='7️⃣', a='seven', b='<u>seven dollars</u>, please.', pta='sete', ptb='sete dólares, por favor.', n=7),
                   dict(ico='8️⃣', a='eight', b='<u>eight dollars</u>, please.', pta='oito', ptb='oito dólares, por favor.', n=8),
                   dict(ico='9️⃣', a='nine', b='<u>nine dollars</u>, please.', pta='nove', ptb='nove dólares, por favor.', n=9),
                   dict(ico='🔟', a='ten', b='<u>ten dollars</u>, please.', pta='dez', ptb='dez dólares, por favor.', n=10)],
            uses=[dict(ico='🙏', tag='Pedir', en='Ten dollars, please.', pt='Dez dólares, por favor.'),
                  dict(ico='🧾', tag='Cobrar', en="That's seven dollars.", pt='São sete dólares.'),
                  dict(ico='🤲', tag='Entregar', en='Here you are.', pt='Aqui está.')],
            rules=[dict(tag='número + dollars', c=0, text='De seis a dez, sempre **dollars** com -s. Termine com **please**.', ex='Eight dollars, please.'),
                   dict(tag="That's + total", c=1, text="Para dizer **quanto é**: That's + número + dollars.", ex="That's nine dollars."),
                   dict(tag='6 · 7 · 8 · 9 · 10', c=2, text='six · seven · eight · nine · ten. Nenhum leva -s.', ex='✗ tens dollars  →  ✓ ten dollars')],
            tips=['Pronuncie **ten** (10) com “e” curto. Os números com **-teen** (13 a 19) e **-ty** (20 a 90) têm o som parecido, mas a sílaba forte muda.']),
        mission_ic='🎲')
    XT = dict(
        exp=[exp('🪙', 'Keep the change.', 'Expressão', 'Fique com o troco.', 'Quando você paga com mais dinheiro e **não quer o troco**.', ['Here you are. Keep the change.', 'Aqui está. Fique com o troco.']),
             exp('🎲', 'Your turn!', 'Informal', 'Sua vez!', 'Em **jogos**, para dizer que é a vez de alguém.', ['Your turn, Scottie!', 'Sua vez, Scottie!']),
             exp('🏆', 'Good game!', 'Expressão', 'Bom jogo!', 'No **fim da partida**, para elogiar o outro jogador.', ['Good game! See you soon.', 'Bom jogo! Até logo.']),
             exp('✅', "That's all.", 'Expressão', 'É só isso.', 'Quando você termina o pedido: **não preciso de mais nada**.', ["Ten dollars, please. That's all.", 'Dez dólares, por favor. É só isso.'])],
        exp_scene=dict(rs='stadium', lines=[
            ['Scottie', 'Eight dollars, please. **That\'s all.**', 'Oito dólares, por favor. É só isso.'],
            ['Banker', 'Sure. Here you are.', 'Claro. Aqui está.'],
            ['Scottie', 'Thanks! **Your turn**, Mr. Monopoly!', 'Obrigado! Sua vez, Sr. Monopoly!'],
            ['Mr. Monopoly', 'Six and four is ten! Here you are.', 'Seis e quatro são dez! Aqui está.'],
            ['Scottie', '**Keep the change!**', 'Fique com o troco!'],
            ['Banker', '**Good game**, Scottie!', 'Bom jogo, Scottie!']]),
        lab=dict(
            short='-teen × -ty', title='Laboratório de sons: ten × -teen × -ty',
            say='Sixteen ou sixty? A sílaba forte muda tudo. Vamos treinar com os números do jogo.',
            intro=dict(what='Os números **-teen** (13 a 19) e **-ty** (20 a 90) são parecidos, mas em **-teen** o fim é longo e forte.',
                       how='Em **sixteen**, as duas sílabas são fortes: “six-TIIN”, com o “ee” longo. Em **sixty**, só a primeira é forte: “SIX-ti”, e o final é curto.',
                       pt='Em português “dezesseis” e “sessenta” são bem diferentes. Em inglês a diferença está no final: **-TEEN** (longo) × **-ty** (curto).'),
            ex=[['ten', 'TÉN', 'dez', 'termine com a língua atrás dos dentes'], ['sixteen', 'siks-TÍIN', 'dezesseis', 'final longo e forte'],
                ['sixty', 'SÍKS-ti', 'sessenta', 'final curto e fraco']],
            pairs=[['sixteen', 'sixty', '16 × 60: final longo × curto'], ['seventeen', 'seventy', '17 × 70'], ['eighteen', 'eighty', '18 × 80'], ['nineteen', 'ninety', '19 × 90']],
            tip='Estique o final de **-teen** como se fosse “tiiin”. Em **-ty**, é só um toque rápido: “ti”.',
            phrase=['Sixty or sixteen dollars?', 'Sessenta ou dezesseis dólares?'],
            rounds=[rnd('sixty', 'sixteen', '**Sixty** (60) tem final curto: “SIX-ti”.'),
                    rnd('eighteen', 'eighty', '**Eighteen** (18) termina com “-TEEN”, longo e forte.'),
                    rnd('seventy', 'seventeen', '**Seventy** (70) tem final curto.')]),
        hunt=[hunt_t('ninety', 'nineteen', '**ninety** (90) tem final curto: “ti”.'),
              hunt_p('ten', ['🔟', '9️⃣', '8️⃣'], '**ten** = dez.'),
              hunt_t('seventeen', 'seventy', '**seventeen** (17) termina com “-TEEN” longo.'),
              hunt_p('seven', ['7️⃣', '6️⃣', '1️⃣'], '**seven** = sete.'),
              hunt_t('eighty', 'eighteen', '**eighty** (80) tem final curto.')])
    VB = dict(title='Verbos para jogar e pagar', tip='Quatro verbos: take, give, hold e roll.', items=[
        verb('take', '🤲', 'pegar', 'I take ten dollars.', 'Scottie take**s** a card.', ['I take ten dollars.', 'Eu pego dez dólares.'], 'takes'),
        verb('give', '🎁', 'dar', 'I give seven dollars.', 'The Banker give**s** money.', ['I give seven dollars.', 'Eu dou sete dólares.'], 'gives'),
        verb('hold', '✋', 'segurar', 'I hold the money.', 'Mr. Monopoly hold**s** his hat.', ['I hold the money.', 'Eu seguro o dinheiro.'], 'holds'),
        verb('roll', '🎲', 'rolar, jogar (dados)', 'I roll the dice.', 'Scottie roll**s** the dice.', ['I roll the dice.', 'Eu jogo os dados.'], 'rolls')])
    MR = dict(
        mold=[pg('Pedir dinheiro', [('número', [('Six', 'seis'), ('Seven', 'sete'), ('Eight', 'oito'), ('Nine', 'nove'), ('Ten', 'dez')]),
                                    ('unidade', [('dollars', 'dólares')])], end=(', please.', ', por favor.')),
              pg('Dizer o total', [('começo', [("That's", 'são'), ("It's", 'são')]),
                                   ('total', [('six dollars', 'seis dólares'), ('seven dollars', 'sete dólares'), ('eight dollars', 'oito dólares'), ('nine dollars', 'nove dólares'), ('ten dollars', 'dez dólares')])], end=('.', '.')),
              pg('Somar', [('soma', [('Six and four', 'seis e quatro'), ('Seven and three', 'sete e três'), ('Eight and two', 'oito e dois'), ('Nine and one', 'nove e um')]),
                           ('resultado', [('is ten.', 'é dez.')])], end=('', ''))],
        speak=[['Ten dollars, please. That\'s all.', 'Dez dólares, por favor. É só isso.'], ['Here you are. Keep the change!', 'Aqui está. Fique com o troco!']],
        trap=[mtrap('“Keep the change” quer dizer…', ['Fique com o troco.', 'Mude de lugar.', 'Guarde o cartão.'], '**Keep the change.** = fique com o troco.', 'Keep the change.'),
              mtrap('Qual frase está certa?', ['Eight dollars, please.', 'Eight dollar, please.', 'Eights dollars, please.'], 'Oito: **dollars** com -s, e o número nunca leva -s.')],
        gap=[mgap('___ game! See you soon.', 'Bom jogo! Até logo.', ['Good', 'Well', 'Nice'], '**Good game!** = bom jogo!', 'Good game!'),
             mgap('Ten dollars, please. That\'s ___.', 'Dez dólares, por favor. É só isso.', ['all', 'few', 'less'], "**That's all.** = é só isso.", "That's all.")],
        expq=[expq('Você pagou dez dólares por algo de oito e não quer o troco.', ['Keep the change.', 'Your turn!', 'Good game!'], '**Keep the change.** = fique com o troco.'),
              expq('É a vez do seu amigo no jogo.', ['Your turn!', "That's all.", 'Keep the change.'], '**Your turn!** = sua vez!'),
              expq('O jogo acabou e você cumprimenta o rival.', ['Good game!', 'Your turn!', 'Keep the change.'], '**Good game!** = bom jogo!')],
        missions=[mission('🏦', 'No banco', 'Peça dinheiro e agradeça.',
                          prompt='Você joga Monopoly e precisa de dinheiro. **Peça ao banqueiro com um número de 6 a 10 + dollars, please. Depois agradeça.**',
                          chips=['Ten dollars, please.', 'Thank you.'], model='Ten dollars, please. Thank you!',
                          check=['Disse um número de 6 a 10 + dollars?', 'Disse please?', 'Agradeci?'],
                          kw=['\\b(?:six|seven|eight|nine|ten) dollars\\b', '\\bplease\\b', '\\bthank'],
                          tips=[[('Ten dollars, please.', 'Dez dólares, por favor.')], [('Please.', 'Por favor.')], [('Thank you.', 'Obrigado.')]],
                          ok=['Valor pedido! 💵', 'Educado! 🙏', 'Obrigado! 😊'], reply=['Sure! Here you are, ten dollars.', 'Claro! Aqui está, dez dólares.']),
              mission('🧾', 'Pagar o aluguel', 'Diga o total, entregue e use as expressões.',
                      prompt='Você caiu numa rua cara. **Diga o total com That\'s + número + dollars, entregue o dinheiro com Here you are e diga Keep the change.**',
                      chips=["That's", 'Here you are.', 'Keep the change.'], model="That's eight dollars. Here you are, ten. Keep the change!",
                      check=["Disse That's + número + dollars?", 'Disse Here you are?', 'Disse Keep the change?'],
                      kw=['\\bthat[\'’]?s (?:six|seven|eight|nine|ten) dollars\\b', '\\bhere you are\\b', '\\bkeep the change\\b'],
                      tips=[[("That's nine dollars.", 'São nove dólares.')], [('Here you are.', 'Aqui está.')], [('Keep the change.', 'Fique com o troco.')]],
                      ok=['Total certo! 🧾', 'Entregue! 🤲', 'Troco para você! 🪙'], reply=['Thank you! Good game!', 'Obrigado! Bom jogo!'])])
    CX = cx([('Two plus four is ___.', 'Dois mais quatro é seis.', ['six', 'seven', 'nine']),
             ('Three plus four is ___.', 'Três mais quatro é sete.', ['seven', 'six', 'ten']),
             ('Four plus four is ___.', 'Quatro mais quatro é oito.', ['eight', 'ten', 'six']),
             ('Five plus four is ___.', 'Cinco mais quatro é nove.', ['nine', 'eight', 'seven']),
             ('Five plus five is ___.', 'Cinco mais cinco é dez.', ['ten', 'eight', 'seven']),
             ('I keep my money in the ___.', 'Eu guardo meu dinheiro no banco.', ['bank', 'ten', 'nine'])])
    return build(70007, B, X, XT, VB, MR, CX)


# ---------------------------------------------------------------- pos 20 · Spider-Man · Is this the seven train? 6 a 10
def ep20():
    PET, MAY, MJ = 'p:short:5d4037:f4c7a1:c0392b:none:shirt', 'p:bun:e0e0e0:f4c7a1:8e44ad:glasses:dress', 'p:long:c0392b:f4c7a1:2e7d32:none:dress'
    cast = {'Peter': ['🕷️', '#C0392B'], 'Aunt May': ['👵', '#8E44AD'], 'MJ': ['👩‍🦰', '#2E7D32']}
    B = dict(
        title='Qual trem? · Is this the seven train?',
        sub='Usar os números de 6 a 10 em trens e paradas: Take the seven train.',
        pattern_label='Is this the … train?',
        why='Hoje você usa os números de seis a dez para achar o trem certo: Is this the seven train? Yes, it is.',
        vocab=[['Six', 'Seis', 'Soa como “SÍKS”.'], ['Seven', 'Sete', 'Soa como “SÉ-ven”.'], ['Eight', 'Oito', 'Soa como “ÊIT”.'],
               ['Nine', 'Nove', 'Soa como “NÁIN”.'], ['Ten', 'Dez', 'Soa como “TÉN”.'], ['Train', 'Trem', 'Soa como “TRÊIN”.']],
        balloons=[['6️⃣', 'six'], ['7️⃣', 'seven'], ['8️⃣', 'eight'], ['9️⃣', 'nine'], ['🔟', 'ten'], ['🚇', 'train']],
        cover_art=cover('nightcity', [('🚇', 100, 56, 20), ('🕷️', 138, 42, 14), ('7️⃣', 84, 32, 14)], 'sp1'),
        cover_sub='Is this the seven train? Em 10 minutos você acha o trem certo como o Peter',
        cover_say='Peter Parker e a tia May vão de metrô para o Queens. Mas qual é o trem certo? O seis? O sete?',
        wrap_recap=[['Is this the seven train?', 'Este é o trem sete?'], ['Yes, it is.', 'Sim, é.'], ["No, it isn't.", 'Não, não é.'], ['Take the seven train.', 'Pegue o trem sete.']],
        teaser={'t': 'Pedir mais de uma coisa', 'd': 'Próximo padrão: pedir mais de uma coisa (Two tickets, please)'},
        cast=cast,
        lines=[['Peter', 'Aunt May, is this the seven train?', 'Tia May, este é o trem sete?'],
               ['Aunt May', 'No, Peter. This is the six train.', 'Não, Peter. Este é o trem seis.'],
               ['Peter', 'Oops! Is that the seven train?', 'Opa! Aquele é o trem sete?'],
               ['MJ', 'Yes, it is! Take the seven train.', 'Sim, é! Pegue o trem sete.'],
               ['Aunt May', 'MJ, how many stops?', 'MJ, quantas paradas?'],
               ['MJ', 'Nine stops, ten minutes. Then exit eight.', 'Nove paradas, dez minutos. Depois a saída oito.'],
               ['Peter', 'Great! Hold the door!', 'Ótimo! Segure a porta!'],
               ['Aunt May', 'Careful, Peter! Watch your step.', 'Cuidado, Peter! Cuidado onde pisa.']],
        quiz=[quiz('What train is it first?', 'Qual é o primeiro trem?', [('6️⃣', 'The six train'), ('7️⃣', 'The seven train'), ('8️⃣', 'The eight train')], 1, 'Tia May diz: “This is the six train.”'),
              quiz('How many stops?', 'Quantas paradas?', [('9️⃣', 'Nine stops'), ('🔟', 'Ten stops'), ('6️⃣', 'Six stops')], 5, 'MJ diz: “Nine stops, ten minutes.”'),
              quiz('Who says “Take the seven train”?', 'Quem diz “Pegue o trem sete”?', [('👩‍🦰', 'MJ'), ('🕷️', 'Peter'), ('👵', 'Aunt May')], 3, 'MJ diz: “Take the seven train.”')],
        rdg_q=rdg('Qual frase pergunta pelo trem sete?', ['Is this the seven train?', 'Is this the train seven?', 'This is seven the train?'],
                  'Em inglês o número vem **antes**: **the seven train**.'),
        dictate=[['Is this the seven train?', 'Este é o trem sete?'], ['Yes, it is.', 'Sim, é.'], ["No, it isn't.", 'Não, não é.'], ['Take the six train.', 'Pegue o trem seis.']],
        produce=prod('Você está na estação e quer o trem sete. **Pergunte Is this the … train? com um número de 6 a 10, escreva a resposta com Yes, it is ou No, it isn\'t e agradeça.**',
                     ['Is this the', "No, it isn't.", 'Thank you.'],
                     "Is this the seven train? No, it isn't. Thank you!",
                     ['Perguntei Is this the … train?', "Escrevi Yes, it is ou No, it isn't?", 'Agradeci?'],
                     ['\\bis this the (?:six|seven|eight|nine|ten)\\b[^.!?]*\\?', '\\b(?:yes,? it is|no,? it isn[\'’]t)\\b', '\\bthank'],
                     [[('Is this the six train?', 'Este é o trem seis?')], [('Yes, it is.', 'Sim, é.'), ("No, it isn't.", 'Não, não é.')], [('Thank you.', 'Obrigado.')]],
                     ['Pergunta de trem! 🚇', 'Resposta curta! ✅', 'Obrigado! 😊'],
                     ['Yes, it is! Take it now. Watch your step!', 'Sim, é! Pegue agora. Cuidado onde pisa!']),
        rs=rsmap(6, 'nightcity'), sc='nightcity')
    X = dict(
        names=['Peter', 'MJ'],
        stage=dict(rs='nightcity', chars=[[PET, 26, 0, 1.0], [MAY, 54, 1, 1.0], [MJ, 84, 1, 1.0]]),
        obra=dict(name='Spider-Man', kind='🦸 Quadrinhos · 1962', year='1962',
                  text='Super-herói criado por Stan Lee e Steve Ditko e publicado pela Marvel em 1962. Peter Parker é um jovem de Nova York que ganha poderes de aranha e balança entre os prédios da cidade.',
                  line=['With great power comes great responsibility.', 'Com grandes poderes vêm grandes responsabilidades. (frase famosa)'],
                  pa=dict(t='viaduct', e=['🕷️', '🚇', '🏙️'], p='i', v=1)),
        gancho=['Peter', 'Aunt May, is this the seven train?', 'Tia May, este é o trem sete?'],
        hot=hots([('🚇', 'train', 'trem', 'Take the seven train.', 'Pegue o trem sete.'),
                  ('6️⃣', 'six', 'seis', 'This is the six train.', 'Este é o trem seis.'),
                  ('🔟', 'ten', 'dez', 'Ten minutes.', 'Dez minutos.'),
                  ('9️⃣', 'nine', 'nove', 'Nine stops.', 'Nove paradas.'),
                  ('8️⃣', 'eight', 'oito', 'Exit eight.', 'Saída oito.')]),
        gap=[gap('___ this the seven train?', 'Este é o trem sete?', ['Is', 'Are', 'Do'], 'Com **this** o verbo é **is**: **Is** this…?'),
             gap('Yes, it ___.', 'Sim, é.', ['is', 'are', 'does'], 'Resposta curta: Yes, it **is**.'),
             gap("No, it ___.", 'Não, não é.', ["isn't", "doesn't", "don't"], 'Resposta curta: No, it **isn\'t**.'),
             gap('Take ___ six train.', 'Pegue o trem seis.', ['the', 'a', 'an'], 'Um trem específico: **the** six train.')],
        trap=[trap(['Is this the seven train?', 'Is the seven this train?', 'Does this the seven train?'], 'Na pergunta, **Is** vem primeiro: **Is this** the seven train?'),
              trap(['the seven train', 'the train seven', 'train the seven'], 'Em inglês o número vem **antes** do substantivo.', q='Qual ordem está certa?')],
        sticker=dict(title='Peter no metrô', sub='Spider-Man · 1962', rs='museum', chars=[[PET, 34, 0, 1.0], [MJ, 68, 1, 1.0]]),
        speakers={'Peter': PET, 'Aunt May': MAY, 'MJ': MJ},
        rule=dict(
            who=PET, head='Is this the … train?', sub='Para achar o trem certo com os números de 6 a 10.',
            say=['Is this the seven train?', 'Este é o trem sete?'],
            formula=[dict(from_=[['This', 0], ['is', 1], ['the seven train.', 2]], to=[['Is', 1], ['this', 0], ['the seven train?', 2]],
                          say='Is this the seven train?', note='Na pergunta, **is** passa para a frente de **this**.'),
                     dict(from_=[['the seven train', 2]], to=[['Take', 3], ['the seven train.', 2]],
                          say='Take the seven train.', note='**Take the** + número + **train**: pegue o trem sete.')],
            uses=[dict(ico='❓', tag='Perguntar', en='Is this the seven train?', pt='Este é o trem sete?'),
                  dict(ico='✅', tag='Responder sim', en='Yes, it is.', pt='Sim, é.'),
                  dict(ico='❌', tag='Responder não', en="No, it isn't.", pt='Não, não é.'),
                  dict(ico='🚇', tag='Mandar pegar', en='Take the six train.', pt='Pegue o trem seis.')],
            rules=[dict(tag='Is this…?', c=0, text='Pergunta sobre **uma coisa que está perto**: Is this the six train?', ex='Is this the six train?'),
                   dict(tag='Yes, it is', c=2, text='Resposta curta com **it**: Yes, it is. · No, it isn\'t.', ex="No, it isn't."),
                   dict(tag='the + número + train', c=1, text='O número vem **antes**: the seven train, não “the train seven”.', ex='✗ the train seven  →  ✓ the seven train')],
            tips=['Em português dizemos “trem sete” ou “linha 7”. Em inglês: **the seven train**, com **the** na frente.']),
        mission_ic='🚇')
    XT = dict(
        exp=[exp('🏃', 'Coming through!', 'Informal', 'Com licença, passando!', 'Quando você precisa **passar** por uma multidão.', ['Coming through! Sorry!', 'Passando! Desculpe!']),
             exp('✋', 'Step back, please.', 'Expressão', 'Afaste-se, por favor.', 'Aviso para **dar espaço** antes de o trem chegar.', ['Step back, please. The train is here.', 'Afaste-se, por favor. O trem chegou.']),
             exp('😅', 'Oops!', 'Informal', 'Opa!', 'Quando você **erra** de leve ou deixa algo cair.', ['Oops! Wrong train.', 'Opa! Trem errado.']),
             exp('👉', 'This way.', 'Expressão', 'Por aqui.', 'Para **mostrar o caminho** a alguém.', ['This way, Aunt May.', 'Por aqui, tia May.'])],
        exp_scene=dict(rs='museum', lines=[
            ['Peter', '**Coming through!** Is this the seven train?', 'Passando! Este é o trem sete?'],
            ['MJ', 'No, it isn\'t. **This way!**', 'Não, não é. Por aqui!'],
            ['Peter', '**Oops!** Sorry, MJ.', 'Opa! Desculpe, MJ.'],
            ['Aunt May', '**Step back, please.** The train is here.', 'Afaste-se, por favor. O trem chegou.'],
            ['MJ', 'Yes, it is! The seven train!', 'Sim, é! O trem sete!'],
            ['Peter', 'Great! Take the seven train.', 'Ótimo! Pegue o trem sete.']]),
        lab=dict(
            short='s + consoante', title='Laboratório de sons: o “s” de station e stop',
            say='Em inglês, palavras como station começam direto com “s”. Vamos treinar com o metrô de Nova York.',
            intro=dict(what='Em **station**, **stop** e **school**, o **s** vem junto de outra consoante: “st”, “sp”, “sk”.',
                       how='Faça um “sss” comprido e só depois solte o “t”. Não coloque uma vogal antes do “s”.',
                       pt='Muitos brasileiros dizem “estation”, “eschool” (com “e” no começo). Em inglês é **station** (STÊI-shun), sem o “e”!'),
            ex=[['station', 'STÊI-shun', 'estação', 'comece com “sss”, sem vogal antes'], ['stop', 'STÓP', 'parar, parada', 'sss e só depois o “t”'],
                ['school', 'SKUUL', 'escola', 'sss e depois o “k”']],
            pairs=[['stop', 'top', 'com s: sss + t · sem s: só t'], ['spin', 'pin', '“girar” × “alfinete”'], ['star', 'tar', '“estrela” × “piche”'], ['spill', 'pill', '“derramar” × “comprimido”']],
            tip='Segure o “sss” por um instante antes do “t”: **sss-tation**. Nada de “e” no começo.',
            phrase=['Is this the station? Stop here.', 'Esta é a estação? Pare aqui.'],
            rounds=[rnd('stop', 'top', '**Stop** (parar) começa com “sss”. **Top** (topo) começa com “t”.'),
                    rnd('pin', 'spin', '**Pin** (alfinete) começa com “p”. **Spin** começa com “sp”.'),
                    rnd('star', 'tar', '**Star** (estrela) começa com “sss”.')]),
        hunt=[hunt_t('spill', 'pill', '**spill** (derramar) começa com “sp”.'),
              hunt_p('train', ['🚇', '🚌', '✈️'], '**train** = trem.'),
              hunt_t('top', 'stop', '**top** (topo) começa com “t”.'),
              hunt_p('school', ['🏫', '🚇', '🏠'], '**school** = escola.'),
              hunt_t('tar', 'star', '**tar** (piche) começa com “t”.')])
    VB = dict(title='Verbos para um herói de Nova York', tip='Quatro verbos: climb, jump, swing e push.', items=[
        verb('climb', '🧗', 'escalar, subir', 'I climb the stairs.', 'Peter climb**s** the wall.', ['I climb the stairs.', 'Eu subo as escadas.'], 'climbs'),
        verb('jump', '🦘', 'pular', 'I jump on the train.', 'He jump**s** very high.', ['I jump on the train.', 'Eu pulo no trem.'], 'jumps'),
        verb('swing', '🕸️', 'balançar', 'I swing from the bridge.', 'Spider-Man swing**s** over the city.', ['I swing from the bridge.', 'Eu me balanço na ponte.'], 'swings'),
        verb('push', '👉', 'empurrar', 'I push the door.', 'MJ push**es** the door.', ['I push the door.', 'Eu empurro a porta.'], 'pushes')])
    MR = dict(
        mold=[pg('Perguntar pelo trem', [('pergunta', [('Is this', 'este é')]),
                                         ('lugar', [('the six train', 'o trem seis'), ('the seven train', 'o trem sete'), ('platform eight', 'a plataforma oito'), ('platform nine', 'a plataforma nove'), ('exit ten', 'a saída dez')])]),
              pg('Responder', [('resposta', [('Yes, it is.', 'Sim, é.'), ("No, it isn't.", 'Não, não é.')]),
                               ('complemento', [('This way.', 'Por aqui.'), ('Over there.', 'Ali.'), ('Step back, please.', 'Afaste-se, por favor.')])], end=('', '')),
              pg('Mandar pegar', [('verbo', [('Take', 'pegue')]),
                                  ('trem', [('the six train', 'o trem seis'), ('the seven train', 'o trem sete'), ('the eight bus', 'o ônibus oito'), ('the nine bus', 'o ônibus nove')])], end=('.', '.'))],
        speak=[['Is this the seven train? Yes, it is.', 'Este é o trem sete? Sim, é.'], ['Coming through! Step back, please.', 'Passando! Afaste-se, por favor.']],
        trap=[mtrap('“Coming through!” quer dizer…', ['Com licença, passando!', 'Estou chegando em casa!', 'Chegou o trem!'], '**Coming through!** = com licença, passando!', 'Coming through!'),
              mtrap('Qual frase está certa?', ['Take the nine bus.', 'Take the bus nine.', 'Take bus the nine.'], 'O número vem **antes**: the nine bus.')],
        gap=[mgap('___! Wrong train.', 'Opa! Trem errado.', ['Oops', 'Hello', 'Please'], '**Oops!** = opa!', 'Oops! Wrong train.'),
             mgap('Step ___, please.', 'Afaste-se, por favor.', ['back', 'on', 'off'], '**Step back, please.** = afaste-se.', 'Step back, please.')],
        expq=[expq('Você precisa passar por muita gente na plataforma.', ['Coming through!', 'This way.', 'Oops!'], '**Coming through!** = com licença, passando!'),
              expq('Você mostra o caminho para sua tia.', ['This way.', 'Oops!', 'Step back, please.'], '**This way.** = por aqui.'),
              expq('Você errou o trem sem querer.', ['Oops!', 'Coming through!', 'This way.'], '**Oops!** = opa!')],
        missions=[mission('🚇', 'Qual trem?', 'Pergunte pelo trem e agradeça.',
                          prompt='Você quer o trem sete. **Pergunte Is this the … train? com um número de 6 a 10, escreva a resposta com Yes, it is ou No, it isn\'t e agradeça.**',
                          chips=['Is this the', 'Yes, it is.', 'Thank you.'], model="Is this the seven train? Yes, it is. Thank you!",
                          check=['Perguntei Is this the … train?', "Usei Yes, it is ou No, it isn't?", 'Agradeci?'],
                          kw=['\\bis this the (?:six|seven|eight|nine|ten)\\b[^.!?]*\\?', '\\b(?:yes,? it is|no,? it isn[\'’]t)\\b', '\\bthank'],
                          tips=[[('Is this the seven train?', 'Este é o trem sete?')], [('Yes, it is.', 'Sim, é.')], [('Thank you.', 'Obrigado.')]],
                          ok=['Pergunta certa! ❓', 'Resposta curta! ✅', 'Obrigado! 😊'], reply=['Yes, it is! Take it now!', 'Sim, é! Pegue agora!']),
              mission('🏃', 'Plataforma cheia', 'Use as expressões da estação.',
                      prompt='A estação está cheia. **Diga Coming through! para passar, Oops! se errar o caminho e Step back, please. ao avisar um amigo.**',
                      chips=['Coming through!', 'Oops!'], model='Coming through! Oops! Step back, please.',
                      check=['Disse Coming through?', 'Disse Oops?', 'Disse Step back, please?'],
                      kw=['\\bcoming through\\b', '\\boops\\b', '\\bstep back\\b'],
                      tips=[[('Coming through!', 'Com licença, passando!')], [('Oops!', 'Opa!')], [('Step back, please.', 'Afaste-se, por favor.')]],
                      ok=['Passando! 🏃', 'Opa! 😅', 'Educado! ✋'], reply=['Thank you! The train is here.', 'Obrigado! O trem chegou.'])])
    CX = cx([('Three plus three is ___.', 'Três mais três é seis.', ['six', 'seven', 'nine']),
             ('A week has ___ days.', 'Uma semana tem sete dias.', ['seven', 'nine', 'ten']),
             ('A spider has ___ legs.', 'Uma aranha tem oito patas.', ['eight', 'six', 'ten']),
             ('A baseball team has ___ players on the field.', 'Um time de beisebol tem nove jogadores em campo.', ['nine', 'ten', 'seven']),
             ('I have ___ fingers on my two hands.', 'Tenho dez dedos nas duas mãos.', ['ten', 'eight', 'six']),
             ('It runs on rails and stops at stations. It is a ___.', 'Anda sobre trilhos e para em estações. É um trem.', ['train', 'six', 'ten'])])
    return build(7070007, B, X, XT, VB, MR, CX)


EPS = [f() for f in (ep14, ep15, ep16, ep17, ep18, ep19, ep20)]
