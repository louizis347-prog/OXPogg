"""Padrão Quest 'focus' (36+ quadros) para as aulas 2–50, gerado dos textos de cada aula (supp5) e dos dados do Neighbors.
O visual (cenas, pessoas, palavras que trocam) é descrito nos próprios quadros (art, swaps, mini, turns)."""
import re, random, zlib

RS = set('cafe living market airport lobby station subway park pier lake nyc cafe2 airport2 lobby1 lobby2 sub2 cafe3 diner home1 yard park2 school shop office clinic kitchen bedroom bath counter gym hall street beach zoo farm playground busstop bakery supermarket bookshop postoffice bank pharmacy restaurant hotelroom mountain forest snow stage library museum castlehall garden fair pool stadium harbor chefkitchen musicroom traincar soccerfield fishing artroom nightcity meetingroom christmas laundry bikeshop airportsecurity baggageclaim apartmenthall kidsroom diningroom gasstation parking classroom dentist eyedoctor hardware drycleaner carwash atmstreet phonestore mall clothesstore shoestore hairsalon cinema concert ballpark campsite hiketrail drivethru partyroom weddinghall bowling minigolf elevator'.split())
FAM = {'cafe': ['cafe2', 'cafe3', 'bakery', 'cafe'], 'cafe2': ['cafe', 'cafe3', 'bakery'], 'cafe3': ['cafe', 'cafe2', 'bakery'], 'bakery': ['cafe', 'market', 'cafe2'], 'market': ['supermarket', 'bakery', 'street'], 'supermarket': ['market', 'bakery', 'street'],
       'restaurant': ['diner', 'cafe2', 'kitchen'], 'diner': ['restaurant', 'cafe2', 'kitchen'], 'street': ['nyc', 'park2', 'busstop'], 'park': ['park2', 'street', 'garden'], 'park2': ['park', 'street', 'garden'], 'airport': ['airport2', 'lobby', 'street'],
       'bank': ['street', 'office', 'lobby'], 'office': ['meetingroom', 'lobby', 'street'], 'school': ['library', 'hall', 'playground'], 'home1': ['living', 'kitchen', 'bedroom'], 'living': ['home1', 'kitchen', 'bedroom'],
       'subway': ['sub2', 'station', 'street'], 'station': ['traincar', 'subway', 'street'], 'busstop': ['street', 'station', 'nyc'], 'hotelroom': ['lobby', 'street', 'bedroom'], 'clinic': ['pharmacy', 'street', 'lobby'], 'pharmacy': ['clinic', 'street', 'shop'],
       'gym': ['park2', 'street', 'pool'], 'beach': ['pier', 'park', 'street'], 'shop': ['street', 'market', 'bookshop'], 'kitchen': ['living', 'home1', 'restaurant']}
STOP = set('a an the and or of to in on at is are am it you i we he she they me my your his her our this that these those do does did can could will would please yes no not for with from be been was were what who where when how why have has had get got just also very'.split())

def clean(s): return re.sub(r'\*\*', '', s or '')
def hsh(s): return zlib.crc32(str(s).encode())
def gender(name): return 'f' if hsh(name) % 2 == 0 else 'm'

def pool(sc, sc2):
    out = []
    for s in [sc, sc2] + FAM.get(sc, []) + FAM.get(sc2, []):
        if s in RS and s not in out: out.append(s)
    for s in ['street', 'park2', 'nyc', 'cafe2', 'living']:
        if s in RS and s not in out and len(out) < 6: out.append(s)
    return out

SETS = [[('Hi', 'Oi'), ('Hello', 'Olá'), ('Hey', 'E aí')], [('Good morning', 'Bom dia'), ('Good afternoon', 'Boa tarde'), ('Good evening', 'Boa noite')],
        [('Thanks', 'Obrigado'), ('Thank you', 'Muito obrigado'), ('Thanks a lot', 'Muito obrigado')], [('one', 'um'), ('two', 'dois'), ('three', 'três'), ('four', 'quatro'), ('five', 'cinco')],
        [('small', 'pequeno'), ('medium', 'médio'), ('large', 'grande')], [('today', 'hoje'), ('tomorrow', 'amanhã'), ('tonight', 'hoje à noite')],
        [('Monday', 'segunda-feira'), ('Tuesday', 'terça-feira'), ('Friday', 'sexta-feira')], [('red', 'vermelho'), ('blue', 'azul'), ('green', 'verde')],
        [('morning', 'manhã'), ('afternoon', 'tarde'), ('evening', 'noite')], [('here', 'aqui'), ('there', 'ali'), ('outside', 'fora')]]

def swaps(en, pt, vocab):
    """troca uma palavra da fala por {a|b|c}; o pt acompanha quando a tradução aparece na linha"""
    best = None
    for w, _, wp in vocab:
        m = re.search(r'\b' + re.escape(w) + r'(es|s)?\b', en, re.I)
        if m and (best is None or m.start() < best[0].start()): best = (m, w, wp)
    if best:
        m, w, wp = best; suf = m.group(1) or ''
        others = [(x, y) for x, _, y in vocab if x.lower() != w.lower()][:2]
        if others:
            en2 = en[:m.start()] + '{' + m.group(0) + '|' + '|'.join(x + suf for x, _ in others) + '}' + en[m.end():]
            pt2 = pt
            mm = re.search(re.escape(wp) + r'(es|s)?\b', pt, re.I) if wp else None
            if mm:
                ps = mm.group(1) or ''
                pt2 = pt[:mm.start()] + '{' + mm.group(0) + '|' + '|'.join(y + ps for _, y in others) + '}' + pt[mm.end():]
            return en2, pt2
    for st in SETS:
        for k, (e0, p0) in enumerate(st):
            m = re.search(r'\b' + re.escape(e0) + r'\b', en, re.I)
            if not m: continue
            others = [x for j, x in enumerate(st) if j != k][:2]
            en2 = en[:m.start()] + '{' + m.group(0) + '|' + '|'.join(x[0] for x in others) + '}' + en[m.end():]
            pt2 = pt
            mm = re.search(re.escape(p0), pt, re.I)
            if mm: pt2 = pt[:mm.start()] + '{' + mm.group(0) + '|' + '|'.join(x[1] for x in others) + '}' + pt[mm.end():]
            return en2, pt2
    return en, pt

def focus(L, P, S, ctx):
    n, en, nb, lines, vocab, npc = L['n'], ctx['en'], ctx['nb'], ctx['lines'], ctx['vocab'], ctx['npc']
    X = ctx.get('extras') or {}
    cu, rd, cv = S['culture'], S['reading'], (X.get('convo') or S['convo'])
    speakers = []
    for l in lines:
        if l['who'] not in speakers: speakers.append(l['who'])
    face_of = ctx['face_of']
    me_sp = 'You' if 'You' in speakers else (speakers[1] if len(speakers) > 1 else 'You')
    learner = me_sp if me_sp != 'You' else 'Mia'
    npc = next((x for x in speakers if x != me_sp), npc); npcface = face_of(npc)
    sc, sc2 = nb.get('sc') or 'street', en.get('sc') or 'street'
    try:
        from scene_pools import POOLS
        try:
            from scene_pools_201_250 import POOLS_201_250
            POOLS = {**POOLS, **POOLS_201_250}
        except Exception:
            pass
        pl = [x for x in POOLS.get(L.get('n'), []) if x in RS and x != 'counter']
    except Exception:
        pl = []
    pl = pl or [x for x in (X.get('scenes') or {}).get('pool', []) if x in RS and x != 'counter'] or pool(sc if sc in RS else sc2, sc2); rsn = [0]
    def scene():
        s = pl[rsn[0] % len(pl)]; rsn[0] += 1; return s
    xs = X.get('scenes') or {}
    role_npc = (xs.get('npc') or {}).get('role') or ('barista' if sc in ('cafe', 'cafe2', 'cafe3', 'bakery', 'diner', 'restaurant') else 'friend')
    me = lambda x, fl=0, **o: dict({'n': learner, 'g': (xs.get('you') or {}).get('g', 'f'), 'role': 'customer', 'x': x, 'flip': fl}, **o)
    other = lambda x, fl=1, **o: dict({'n': npc, 'g': (xs.get('npc') or {}).get('g') or gender(npc), 'role': role_npc, 'x': x, 'flip': fl}, **o)
    def art(kind, k=0):
        s = scene()
        if kind == 'solo': return {'rs': s, 'cast': [me(48)]}
        if kind == 'npc': return {'rs': s, 'cast': [other(50)]}
        if kind == 'pair': return {'pair': [{'rs': s, 'cast': [other(50)]}, {'rs': scene(), 'cast': [me(50)]}]}
        return {'rs': s, 'cast': [me(30), other(70, 1, **({'prop': 'cup'} if k % 2 and role_npc == 'barista' else {}))]}
    faces = {w: face_of(w) for w in speakers}; faces['You'] = 'Mia'; faces[learner] = face_of(learner) if learner != 'Mia' else 'Mia'
    pages = []
    def add(stage, kind, title, a=None, **c):
        d = dict(t='q1', stage=stage, kind=kind, title=title, **c)
        d['art'] = a if a is not None else art('both', len(pages)); pages.append(d)
    oks = [[o for o in t['opts'] if o.get('ok')][0] for t in cv['turns']]
    L['title'] = nb['t']; L['scene'] = sc; L['cast'] = [npc, learner]; L['visual'] = sc
    L['dialog'] = {'speakers': {w: {'name': faces[w]} for w in speakers}, 'lines': [{'who': l['who'], 'en': clean(l['en']), 'pt': l['pt']} for l in lines]}
    # 1 capa
    situ = P['q_cover']['situation']['text']
    add('mission', 'cover', 'Missão: ' + nb['t'], goal=situ, can=[o['en'] for o in oks[:3]], note='Observe como as pessoas começam, esclarecem e terminam a conversa.',
        heading=nb['t'], kicker=('A2' if n >= 2000 else 'A1') + ' · Aula %d' % (n - 2000 if n >= 2000 else n))
    # 2 obra
    a = en.get('a', {})
    add('culture', 'work', 'A obra e a situação', a=art('both', 1), work={'title': a.get('w', ''), 'year': a.get('y', ''), 'note': re.sub(r'\s+', ' ', a.get('d', ''))[:420]},
        question='Como a história dessa obra ajuda você a imaginar a situação de hoje? Diga uma ideia em inglês.')
    # 3-4 fatos
    # fatos: não repetem o "mito ou fato"; vêm de gancho, tom, comparação e dos textos do cotidiano
    cm = cu.get('compare') or {}
    facts = []
    if cu.get('hook'): facts.append({'big': nb['t'], 'label': 'O contexto', 'sub': clean(cu['hook'])})
    if cu.get('polite'): facts.append({'big': 'Soa natural', 'label': 'Educação e tom', 'sub': clean(cu['polite'])})
    for w in cu.get('wild', [])[:2]:
        d = w.get('decode') or {}
        facts.append({'big': w.get('kind', 'No dia a dia'), 'label': 'No dia a dia', 'sub': clean(d.get('why', ''))})
    if cm.get('tip'): facts.append({'big': 'Ponte de uso', 'label': 'Brasil × EUA', 'sub': clean(cm['tip'])})
    while len(facts) < 4: facts.append({'big': nb['t'], 'label': 'Situação', 'sub': clean(cu['hook'])})
    first = X.get('key') or {'big': nb['t'], 'label': 'Situação', 'sub': clean(cu['hook'])}
    mini = list(X.get('mini') or [])
    if not mini:
        for l in lines[:4]:
            e2, p2 = swaps(clean(l['en']), l['pt'], vocab); mini.append({'who': l['who'], 'en': e2, 'pt': p2})
    add('culture', 'facts', 'A situação em contexto', a=art('both', 2), facts=[first] + facts[:2], mini=mini, me=me_sp, faces=faces)
    add('culture', 'facts', 'Costumes e escolhas', a=art('npc'), facts=facts[2:5] if len(facts) > 3 else facts[:2])
    add('culture', 'compare', 'Brasil e Estados Unidos', a=art('pair'), compare=cu['compare'])
    for w in cu['wild'][:2]:
        add('culture', 'artifact', 'Leia: ' + w['kind'].lower(), a=art('both', 3), artifact=w)
    mf = cu['mythfact']; hm = (len(mf) + 1) // 2
    add('culture', 'quiz', 'Mito ou fato? · 1/2', a=art('both', 4), items=mf[:hm], instruction='Decida e explique com suas palavras.')
    add('culture', 'quiz', 'Mito ou fato? · 2/2', a=art('npc'), items=mf[hm:], instruction='Mais uma rodada: decida e explique.')
    # leitura em 3 partes
    tx = rd['text']; k = max(1, -(-len(tx) // 3)); parts = [tx[i:i + k] for i in range(0, len(tx), k)][:3]
    prompts = ['Onde começa e o que acontece?', 'O que muda ou complica?', 'Como termina?']
    for i, pr in enumerate(parts):
        add('read', 'reading', '%s · %d/%d' % (rd['title'], i + 1, len(parts)), a=art('solo' if i == 0 else 'both', i), paragraphs=pr, glossary=rd['glossary'], part=i + 1, prompt=prompts[i])
    stem = lambda q: dict(q)
    add('read', 'quiz', 'Entenda a ideia', a=art('both', 5), items=[rd['fast']], instruction='Leia uma vez para entender a situação geral.')
    ans = [s['ans'] for s in rd['scan']]
    sc_items = []
    for i, q in enumerate(rd['scan']):
        ds = [x for j, x in enumerate(ans) if j != i][:2]
        for extra in ['nothing', 'nobody', 'nowhere']:
            if len(ds) < 2 and extra not in ds: ds.append(extra)
        opts = [q['ans']] + ds; random.Random(n * 7 + i).shuffle(opts)
        sc_items.append({'q': q['q'], 'opts': opts, 'ans': opts.index(q['ans']), 'why': 'Procure no texto: ' + q['ans'] + '.'})
    add('read', 'quiz', 'Encontre as informações', a=art('both', 6), items=sc_items, instruction='Procure detalhes, não traduza palavra por palavra.')
    add('read', 'quiz', 'Palavras pelo contexto', a=art('both', 7), items=[{'q': c['sent'] + ' O que significa “' + c['w'] + '”?', 'opts': c['opts'], 'ans': c['ans'], 'why': c['why']} for c in rd['ctx']], instruction='Use a frase inteira como pista.')
    add('read', 'quiz', 'Confira as pistas', a=art('both', 8), items=[{'q': t['s'], 'opts': ['True', 'False'], 'ans': 0 if t['ans'] else 1, 'why': t['why']} for t in rd['tf']], instruction='A resposta precisa concordar com a história.')
    ev = rd['order']; oi = []
    for j in (1, 2, 3):
        ds = [e for m_, e in enumerate(ev) if m_ not in (j - 1, j)][:2]; opts = [ev[j - 1]] + ds; random.Random(n + j).shuffle(opts)
        oi.append({'q': 'O que acontece antes de: “' + ev[j] + '”?', 'opts': opts, 'ans': opts.index(ev[j - 1]), 'why': 'Reconstrua a ordem da história.'})
    add('read', 'quiz', 'Sequência da história', a=art('both', 9), items=oi, instruction='Reconstrua a sequência sem reler a história.')
    # conversa
    half = (len(lines) + 1) // 2
    for idx, (title, part) in enumerate([('Conversa · começo', lines[:half]), ('Conversa · final', lines[half:])]):
        sw = []
        xd = X.get('dlg') or []
        for j, l in enumerate(part):
            gi = (0 if idx == 0 else half) + j
            if gi < len(xd) and xd[gi].get('who') == l['who']: sw.append({'who': l['who'], 'en': xd[gi]['en'], 'pt': xd[gi]['pt']})
            else:
                e2, p2 = swaps(clean(l['en']), l['pt'], vocab); sw.append({'who': l['who'], 'en': e2, 'pt': p2})
        add('talk', 'dialog', title, a=art('both', idx), lines=[(l['who'], clean(l['en']), l['pt']) for l in part], swaps=sw, me=me_sp, faces=faces, instruction='Ouça. Depois toque nas palavras coloridas e diga o que muda.')
    for i, t in enumerate(cv['turns']):
        add('talk', 'choice', 'Sua resposta · %d/%d' % (i + 1, len(cv['turns'])), a=art('both', i), turn=t, position=i + 1, total=len(cv['turns']), npc=cv['npc']['name'], npcface=npcface, outcome='A conversa continua.')
    # vocabulário
    def exs(w):
        pool_ = [clean(x) for x in [l['en'] for l in lines] + [t for t in tx for t in re.split(r'(?<=[.!?”])\s+', t)] if re.search(r'\b' + re.escape(w) + r'\b', clean(x), re.I) and len(clean(x).split()) <= 12]
        out = []
        for s_ in pool_:
            s_ = s_.strip('“” ')
            if s_ not in out: out.append(s_)
        while len(out) < 2: out.append('I need ' + w + '.' if len(out) == 0 else 'This is my ' + w + '.')
        return out[:2]
    words = [(w, wp, exs(w)[0], exs(w)[1], 'prop:cup', e) for w, e, wp in vocab[:6]]
    if X.get('vocab'): words = [(v['w'], v['pt'], v['ex'][0], v['ex'][1], 'prop:cup', v.get('e', '')) for v in X['vocab'][:6]]
    for i in range(0, len(words), 3):
        grp = words[i:i + 3]
        if grp: add('lab', 'vocab', 'Palavras em ação · %d/%d' % (i // 3 + 1, -(-len(words) // 3)), a=art('both', i), words=grp, prompt='Toque, ouça e diga uma frase sua com cada palavra.')
    # moldes
    sw0 = P['rl_patterns'].get('swap'); vlist = [w for w, _, _ in vocab]
    def mold_from(sentence):
        for w in vlist:
            if re.search(r'\b' + re.escape(w) + r'\b', sentence, re.I) and len(vlist) >= 3:
                opts = [w] + [x for x in vlist if x != w][:2]
                return {'frame': re.sub(r'\b' + re.escape(w) + r'\b', '{item}', sentence, count=1, flags=re.I), 'slots': [{'key': 'item', 'opts': opts}], 'model': sentence}
        return None
    ms = []
    if sw0 and sw0.get('slots') and len(sw0['slots'][0]['opts']) >= 2:
        slots = [{'key': s_['k'], 'opts': [o['en'] for o in s_['opts']]} for s_ in sw0['slots']]
        fr_ = sw0['frame']; mdl = fr_
        for s_ in slots: mdl = mdl.replace('{' + s_['key'] + '}', s_['opts'][0])
        ms.append({'frame': fr_, 'slots': slots, 'model': mdl})
    for o in oks:
        m_ = mold_from(o['en'])
        if m_ and len(ms) < 2 and all(m_['frame'] != x['frame'] for x in ms): ms.append(m_)
    if not ms: ms.append({'frame': 'I would like {item}, please.', 'slots': [{'key': 'item', 'opts': vlist[:3] or ['water', 'tea', 'coffee']}], 'model': 'I would like water, please.'})
    titles = ['Molde: faça o pedido', 'Molde: varie a frase']
    xm = X.get('molds') or []
    if len(xm) >= 3: ms = [{'frame': m['frame'], 'slots': m['slots'], 'model': m['model'], 'note': m.get('note', ''), 'title': m.get('title')} for m in xm]
    for i in range(2):
        m_ = ms[i % len(ms)]
        add('lab', 'pattern', m_.get('title') or titles[i], a=art('both', i), frame=m_['frame'], slots=m_['slots'], model=m_['model'], note=m_.get('note') or 'Troque duas opções e diga a frase em voz alta, sem ler.')
    # sons
    pr = P['rl_pron']; items = [clean(x['say']) for x in pr.get('items', [])][:3]
    if len(items) < 3: items += [clean(o['en']) for o in oks if clean(o['en']) not in items][:3 - len(items)]
    pairs_ = [(t, 'ritmo', 'Ouça, repita no mesmo ritmo e grave sua versão.') for t in items[:3]]
    if X.get('sounds'): pairs_ = [(x['say'], x['tag'], x['tip']) for x in X['sounds'][:3]]
    add('lab', 'sound', 'Som e ritmo', a=art('solo'), pairs=pairs_, prompt='Ouça, repita e depois grave uma versão sua.')
    # arcade
    ex = []
    for e in S['errors'][:4]:
        opts = [e['wrong'], e['fix'], e.get('alt') or e['wrong'] + '?']; opts = list(dict.fromkeys(opts)); random.Random(hsh(e['fix'])).shuffle(opts)
        ex.append({'q': 'Escolha a frase mais natural.', 'opts': opts[:3], 'ans': opts.index(e['fix']) if e['fix'] in opts[:3] else 0, 'why': e['why']})
    add('arcade', 'quiz', 'Encontre a frase natural', a=art('both', 3), items=ex, instruction='Escolha a forma que resolve a situação; explique o erro comum.')
    add('arcade', 'quiz', 'Transferência de contexto', a=art('both', 4), items=cu['quiz'], instruction='Agora o cliente muda uma condição: responda sem decorar o diálogo.')
    # roleplay dinâmico
    turns = []
    for i in range(0, len(lines) - 1):
        if lines[i]['who'] == npc and lines[i + 1]['who'] == me_sp and len(turns) < 4:
            you = clean(lines[i + 1]['en']); rep = clean(lines[i + 2]['en']) if i + 2 < len(lines) and lines[i + 2]['who'] == npc else ''
            opts = [[you, lines[i + 1]['pt'], rep or 'OK.']]
            e2, p2 = swaps(you, lines[i + 1]['pt'], vocab)
            m_ = re.search(r'\{([^{}]+)\}', e2)
            if m_:
                for alt in m_.group(1).split('|')[1:]:
                    opts.append([e2.replace(m_.group(0), alt), p2, (re.sub(re.escape(m_.group(1).split('|')[0]), alt, rep, flags=re.I) if rep else 'OK.')])
            turns.append({'npc': clean(lines[i]['en']), 'opts': opts[:3]})
    if (X.get('role') or {}).get('turns'): turns = [{'npc': t['npc'], 'opts': [[o['en'], o['pt'], o['reply']] for o in t['opts']]} for t in X['role']['turns']]
    chg = (X.get('role') or {}).get('change') or ['Falta um item.', 'O atendente não entende: repita com outras palavras.', 'O cliente muda de ideia.']
    add('boss', 'role', 'Missão ao vivo', a=art('both', 5), solo='Professor é %s; estudante faz o papel de cliente. Escolham as falas e refaçam a conversa em três rodadas.' % npc,
        group='Trio: cliente, %s e observador. Troquem de papel a cada rodada. O observador marca pedido claro, esclarecimento e despedida.' % npc,
        prompts=[o['en'] for o in oks[:3]], change=chg, turns=turns or None, me=me_sp, npcname=npc, faces=faces)
    # escrita
    model = ' '.join(o['en'] for o in oks[:3]); kw = [w for w in vlist if re.search(r'\b' + re.escape(w) + r'\b', model, re.I)] + ['please', 'thanks']
    xw = X.get('writing') or {}
    if xw: model = xw['model']; kw = [k_.lower() for k_ in xw.get('kw', kw)]
    mm = (ms[2] if len(xm) >= 3 else (mold_from(oks[0]['en']) or ms[0]))
    add('write', 'pattern', mm.get('title') or 'Molde: varie por escrito', a=art('both', 6), frame=mm['frame'], slots=mm['slots'], model=mm['model'], note=mm.get('note') or 'Na escrita, a saudação, o detalhe e a despedida deixam a mensagem mais clara.')
    add('write', 'writing', 'Escreva a sua versão', a=art('solo'), task=xw.get('task') or 'Escreva 3 frases: faça seu pedido ou sua pergunta, esclareça um detalhe e termine com uma despedida natural. Depois crie uma segunda versão mudando um item.',
        model=model, checks=xw.get('checks') or ['Usei uma expressão da aula.', 'Fiz uma pergunta clara.', 'Usei uma despedida natural.'], variants=[], kw=kw, placeholder='Hi! Could I…?')
    add('wrap', 'exit', 'Mostre o que aprendeu', a=art('both', 7), prompts=['Diga em voz alta: ' + o['pt'] for o in oks[:3]],
        spaced=['Amanhã: refaça a conversa sem consultar.', 'Na próxima semana: use as expressões em uma situação nova.', 'Na próxima unidade: mude o tom por escrito.'])
    add('wrap', 'finish', 'Missão concluída', a=art('both', 8), badge=S.get('badge') or {'name': nb['t'], 'desc': 'Conversa concluída em inglês.'}, homework=S.get('homework', ''), next='Em outra situação, um detalhe mudou. Como você se adaptaria?')
    L['pages'] = pages
    minutes = [('mission', 'Missão'), ('culture', 'Contexto'), ('read', 'Leitura'), ('talk', 'Conversa'), ('lab', 'Oficina'), ('arcade', 'Prática'), ('boss', 'Interação'), ('write', 'Escrita'), ('wrap', 'Retomada')]
    L['plan'] = {m: [{'id': k, 'name': nm, 'min': v} for (k, nm), v in zip(minutes, vals)] for m, vals in (('solo', [3, 8, 11, 13, 9, 6, 5, 3, 2]), ('group', [3, 7, 10, 11, 8, 5, 10, 4, 2]))}
    L['fmt'] = 'quest-focus-v1'
