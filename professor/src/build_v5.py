#!/usr/bin/env python3
"""Aulas Quest v5 = JUNÇÃO enxuta do curso regular (en-a1, episódios principais) + Neighbors (nb-a1, sem revisões de arco)
+ suplemento pequeno (src/supp5/sNNN.py → SUPP: culture, reading, convo, errors, homework). Não lê data/v3.
Uso: python3 src/build_v5.py 1 2 3 | --all | --table"""
import glob, importlib.util, json, math, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
from build_v4 import CH, MIN, DESC, CHAP
def load(p):
    o = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', p + '_*.json'))): o += json.load(open(f, encoding='utf-8'))
    return o
EN = [e for e in load('en-a1') if e['n'] < 7000000]
FILLER = {'That sounds good. What should we do next?', 'Let me check the details before we decide.', 'Could you say that one more time?', 'Sure, I will explain it clearly.', 'Thanks, now I know how to continue.'}
NB = [e for e in load('nb-a1') if not str(e['t']).lower().startswith(('arc ', 'review'))]
strip = lambda s: re.sub(r'\*\*|\{\{|\}\}', '', s or '')
bold = lambda s: re.sub(r'\{\{(.+?)\}\}', r'**\1**', s or '')
# Neighbors da aula n: 1-50 sequencial; 51-200 pula situações que já apareceram antes (sem repetir situação)
SKIP_NB = {150, 151, 154, 159, 160, 161, 162, 164, 167, 168, 170, 171, 179, 180, 206}
def nb_index(n):
    if n <= 50: return n
    k, c = 50, 50
    while c < n:
        k += 1
        if k not in SKIP_NB: c += 1
    return k
def fr(e, k): return [f for f in e['fr'] if f['k'] == k]
def supp(n):
    f = os.path.join(HERE, 'supp5', 's%03d.py' % n)
    if not os.path.exists(f): return {}
    spec = importlib.util.spec_from_file_location('s5%03d' % n, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    if n == 1:
        from lesson1_content import enrich
        return enrich(m.SUPP)
    return m.SUPP

import zlib
ELENCO = [x['name'] for x in json.load(open(os.path.join(ROOT, 'professor', 'data', 'elenco.json'), encoding='utf-8'))]
def face_of(name): return ELENCO[zlib.crc32(name.encode()) % len(ELENCO)]
def extras(n):
    f = os.path.join(HERE, 'supp5', 'x%03d.py' % n)
    if not os.path.exists(f): return {}
    spec = importlib.util.spec_from_file_location('x5%03d' % n, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.X
def ylayer(n):
    f = os.path.join(HERE, 'supp5', 'y%03d.py' % n)
    if not os.path.exists(f): return {}
    spec = importlib.util.spec_from_file_location('y5%03d' % n, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.Y
def zlayer(n):
    f = os.path.join(HERE, 'supp5', 'z%03d.py' % n)
    if not os.path.exists(f): return {}
    spec = importlib.util.spec_from_file_location('z5%03d' % n, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return natural(m.Z)
# verbos de estado quase nunca usam -ing: a 4ª peça vira uma forma que o aluno realmente diz
ALT = {
 'want': ('mais educado', "I'd like", "I'd like a small coffee, please.", 'Eu queria um café pequeno, por favor.'),
 'need': ('futuro: ’ll + need', 'need', "I'll need a bag, please.", 'Vou precisar de uma sacola, por favor.'),
 'like': ('negativa', "don't like", "I don't like spicy food.", 'Eu não gosto de comida picante.'),
 'love': ('com ênfase', 'really love', 'I really love this place.', 'Eu adoro este lugar.'),
 'cost': ('pergunta: does … cost', 'cost', 'How much does it cost?', 'Quanto custa?'),
 'know': ('negativa', "don't know", "I don't know.", 'Eu não sei.'),
 'belong': ('com to', 'belong to', 'These keys belong to Ana.', 'Estas chaves são da Ana.'),
 'mean': ('pergunta: do … mean', 'mean', 'What do you mean?', 'O que você quer dizer?'),
}
def natural(Z):
    vs = []
    for v in Z.get('verbs', []):
        a = ALT.get(v['v'])
        if a:
            v['forms'][3] = dict(k=a[0], en=a[1], ex=a[2], pt=a[3])
            v['note'] = (v.get('note') or '').replace('-ing', '').strip() + ' Quase não se usa no -ing: veja a forma ao lado.'
        vs.append(v)
    Z['verbs'] = vs
    return Z
def prev_ctx(n):
    if n < 2: return None
    items, words, quiz, say = [], [], [], []
    for k, back in enumerate((1, 2)):
        m = n - back
        if m < 1: continue
        try:
            X = extras(m); c = (X.get('convo') or supp(m)['convo'])['turns']
        except Exception: continue
        oks = [[o for o in t['opts'] if o.get('ok')][0] for t in c]
        vv = X.get('vocab') or []; vem = [v.get('e', '') for v in vv]
        for i, o in enumerate(oks[:3]): items.append(((vem[i % len(vem)] if vem else '💬'), o['en'], o['pt']))
        for v in vv[:6 if k == 0 else 3]: words.append((v.get('e', '💬'), v['w'], v['pt']))
        for t in c[:2]:
            opts = [o['en'] for o in t['opts']]
            quiz.append(dict(q='Aula %d: %s — o que você responde?' % (m, t['npc']), opts=opts, ans=[o.get('ok') for o in t['opts']].index(True), why=[o for o in t['opts'] if o.get('ok')][0].get('fb', '')))
        if k == 0: say = [(o['en'], o['pt']) for o in oks[:3]]
    if not items: return None
    return dict(items=items[:6], words=words[:6], quiz=quiz[:4], say=say)
def build(n):
    S = supp(n); en, nb = EN[S.get('reg', n) - 1], NB[nb_index(n) - 1]
    nhero = fr(nb, 'nbhero')[0]; chats = fr(nb, 'nbchat'); base = dict(chats[0]); base['lines'] = [l for l in base['lines'] if l[1] not in FILLER]
    npc = [k for k in base['cast'] if k != 'You'][0]; npcface = face_of(npc)
    lines = [dict(who=w, en=bold(e), pt=p) for w, e, p in base['lines']]
    hot = fr(en, 'hotscene')[0]['hot'] if fr(en, 'hotscene') else []
    exps = fr(en, 'pgexp')[0]['items'] if fr(en, 'pgexp') else []
    mold = fr(en, 'pgmold')[0]['pages'][0] if fr(en, 'pgmold') else None
    rule = fr(en, 'pgrule')[0]['rule'] if fr(en, 'pgrule') else {}
    lab = fr(en, 'pglab')[0] if fr(en, 'pglab') else {}
    speak = fr(en, 'pgspeak')[0]['items'] if fr(en, 'pgspeak') else []
    miss = (fr(en, 'pgmission')[0]['missions'] if fr(en, 'pgmission') else [{}])[0].get('data', {})
    wrap = fr(en, 'wrap')[0]; nwrap = fr(nb, 'wrap')[0]
    tap = fr(nb, 'nbtap')[0]['items']
    for _i in tap: _i.setdefault('q', _i.get('pt') or 'Listen and choose.'); ctx = fr(nb, 'nbctx')[0]['items'] if fr(nb, 'nbctx') else []
    shadow = fr(nb, 'nbshadow')[0]['items']; vocab = fr(nb, 'nbvocab')[0]['items'] if fr(nb, 'nbvocab') else []
    dic = fr(nb, 'nbdict')[0]['items'] if fr(nb, 'nbdict') else []
    sheet = [i for f in fr(en, 'pgsheet') for i in f.get('items', [])]
    rd = fr(en, 'rdg')[0]['s'] if fr(en, 'rdg') else []
    title = re.sub(r'\s*·.*', '', en['t']); title_en = nb['t']
    def art(k, i=0):
        fs = fr(en, k); f = fs[i] if len(fs) > i else None
        if f and f.get('rs'): return dict(rs=f['rs'], chars=f.get('chars') or (en.get('stage') or {}).get('chars'))
        st = en.get('stage') or {}
        return dict(rs=st.get('rs') or en['sc'], chars=st.get('chars')) if (st.get('rs') or en.get('sc')) else None
    P = {}
    P['q_cover'] = dict(t='q_cover', title=nb['t'] + ' · ' + title, pt=en['s'], level='A1', unit=dict(n=math.ceil(n / 8), k=(n - 1) % 8 + 1, of=8, name=en['a']['w'] + ' × ' + nb['a'].get('w', '')),
        situation=dict(text=strip(nb['p']), scene=en['sc'], tod='day', cast=[npc, 'You']), goal=strip(en['p']),
        canDo=['Say: ' + strip(i['en']) for i in exps[:4]], success=['I understand the conversation.', 'I use the key expression.', 'I answer a real question.', 'I close politely.'],
        think=strip(nhero.get('mission', '')))
    cult = dict(S.get('culture', {})); cult['t'] = 'q_culture'; cult.setdefault('title', 'Cultural spotlight')
    hs = fr(en, 'hotscene')
    if hs: cult['art'] = art('hotscene'); cult['hot'] = [dict(e=h['e'], x=h['x'], y=h['y'], en=h['en'], pt=h['pt'], say=h.get('say', ''), sayPt=h.get('sayPt', '')) for h in hot]
    cult.setdefault('hook', strip(nb['a'].get('d', '') or en['a'].get('d', '')))
    cult.setdefault('facts', [dict(big=h['en'].capitalize(), label=h['pt'], sub=h.get('say', '')) for h in hot[:5]])
    P['q_culture'] = cult
    rdg = dict(S.get('reading', {})); rdg['t'] = 'q_read'
    if 'text' not in rdg: rdg.update(genre='Story', title=en['a']['w'], text=[bold(' '.join(s[0] for s in rd))], glossary=[])
    rdg['art'] = art('rdg'); rdg['title'] = 'Reading quest — ' + rdg.get('title', ''); P['q_read'] = rdg
    P['rl_dialog'] = dict(t='rl_dialog', title='Dialogue — ' + nb['t'], qs=[], retell=dict(prompt='Retell the conversation in your own words.', starters=['First,', 'Then,', 'In the end,']))
    cv = S.get('convo')
    if not cv:
        turns = []; ls = base['lines']
        for i, (w, e, p) in enumerate(ls):
            if w == 'You' and i > 0 and ls[i - 1][0] != 'You':
                turns.append(dict(npc=strip(ls[i - 1][1]), pt=ls[i - 1][2], opts=[dict(en=strip(e), pt=p, ok=True, fb='Natural reply for this situation.')]))
        cv = dict(npc=dict(name=npc, face=npcface), story=strip(nb['p']), turns=turns)
    cv = dict(cv); cv['npc'] = dict(cv.get('npc') or {'name': npc}); cv['npc'].setdefault('face', npcface); cv['npc'].setdefault('name', npc)
    P['rl_dialog']['qs'] = [dict(q='%s says: “%s” — what is the natural reply?' % (npc, t['npc']), opts=[o['en'] for o in t['opts']], ans=[o['ok'] for o in t['opts']].index(True)) for t in cv['turns'][:4] if len(t['opts']) == 3]
    P['q_choose'] = dict(t='q_choose', title='Choose your reply', **cv)
    P['rl_chunks'] = dict(t='rl_chunks', title='Useful expressions', items=[dict(en=strip(i['en']), pt=i['pt'], use=strip(i['use']), reg=i.get('tag', ''), pri=k < 4) for k, i in enumerate(exps[:8])])
    pats = [dict(name=rule.get('head', title), formula='**' + rule.get('head', '') + '**', ex=[u['en'] for u in rule.get('uses', [])][:3], main=True)] if rule else []
    sw = None
    if mold:
        fr_, tp, slots = '', '', []
        for k, s in enumerate(mold['slots']):
            key = 's%d' % k
            if len(s['opts']) == 1: fr_ += s['opts'][0][0] + ' '; tp += s['opts'][0][1] + ' '
            else:
                fr_ += '{%s} ' % key; tp += '{%s} ' % key; slots.append(dict(k=key, label=s['cat'].capitalize(), opts=[dict(en=o[0], pt=o[1]) for o in s['opts']]))
        end = mold.get('end', ['.', '.'])
        sw = dict(frame=fr_.strip().rstrip(',') + end[0], tpt=tp.strip() + end[1], slots=slots)
    P['rl_patterns'] = dict(t='rl_patterns', title='Patterns', patterns=pats, **({'swap': sw} if sw else {}))
    P['rl_pron'] = dict(t='rl_pron', title='Pronunciation lab', focus=lab.get('short', ''), tip=lab.get('tip', ''), items=[dict(say=strip(s[0]), linked=strip(s[0]), ipa='', rhythm='') for s in speak[:3]],
        identify=[dict(q=r['ask'], opts=r['opts'], ans=r['a'], say=r['say']) for r in lab.get('rounds', [])[:3]])
    games = dict(pairs=[dict(en=v[0], pt=v[2]) for v in vocab[:6]] or [dict(en=v[0], pt=v[1]) for v in en.get('v', [])[:6]],
        unscramble=[dict(words=strip(s[0]).split(), ans=strip(s[0]), pt=s[1]) for s in shadow if 3 <= len(s[0].split()) <= 9][:4],
        speed=[dict(q=strip(i['sit']), opts=i['opts'], ans=i['a'], why=i.get('why', '')) for i in ctx] + [dict(q=i['q'], opts=[o[1] for o in i['opts']], ans=i['a'], why=i.get('why', '')) for i in tap[:4]],
        dict=[dict(say=strip(d['t'])) for d in dic[:3]])
    if S.get('errors'): games['errors'] = S['errors']
    P['q_arcade'] = dict(t='q_arcade', title='Practice arcade', games=games)
    P['rl_role'] = dict(t='rl_role', title='Boss mission — ' + nb['t'], brief=dict(teacher='You are ' + npc + '. Change the plan during the scene.', student=(cv.get('story') or 'Use today’s expressions to solve the situation.') + ' You are the customer / visitor.'),
        orders=[strip(s[0]) for s in speak[:3]] or ['Say the key expressions'], complications=S.get('complications', ['Something is not available.', 'The other person did not hear you: repeat.', 'Confirm one detail.']),
        rounds=[dict(label='With support', desc='Chunks on screen', help=[strip(i['en']) for i in exps[:4]]), dict(label='Keywords', desc='Only keywords', help=[v[0] for v in vocab[:5]], kw=True), dict(label='No script', desc='Free', help=[])],
        success=['I make my request.', 'I ask one question.', 'I close politely.'])
    P['rl_write'] = dict(t='rl_write', title='Writing — your turn', task=strip(miss.get('prompt', 'Write 3 sentences.')), steps=['Greeting', 'Main idea', 'Detail', 'Closing'], model=strip(miss.get('model', '')), checklist=[strip(c) for c in miss.get('check', [])][:4] or ['I used the key expression.'], tip='Corrija só 2–3 pontos prioritários.', fix=dict(n=3))
    P['rl_exit'] = dict(t='rl_exit', title='Exit ticket & homework', tasks=[dict(ic='🎤', name='Say it', prompt=s[1], model=strip(s[0])) for s in speak[:3]],
        homework=dict(h='Your English mission', min='10–15', items=S.get('homework_items', ['Record 45 seconds using the key expressions.', 'Write 3 sentences.', 'Listen to the dialogue again.', 'Review the 4 priority expressions.'])), spaced=dict(next=[strip(i['en']) for i in exps[:3]], week=[], unit=[]))
    P['q_wrap'] = dict(t='q_wrap', title='Mission complete', recap=wrap['recap'] + nwrap['recap'], homework=S.get('homework', 'Record a short audio using today’s expressions.'), next=dict(title=wrap['teaser']['t'], teaser=wrap['teaser']['d']))
    P['q_cover']['art'] = art('hotscene')
    P['rl_dialog']['art'] = art('pgscene'); P['q_choose']['art'] = art('pgscene'); P['rl_pron']['art'] = art('pglab'); P['q_arcade']['art'] = art('pgfind')
    P['rl_role']['art'] = art('pgspeak'); P['rl_write']['art'] = art('pgmission') if fr(en, 'pgmission') else None; P['rl_chunks']['art'] = art('pgexp')
    ORDER = ['q_cover', 'q_culture', 'q_read', 'rl_dialog', 'q_choose', 'rl_chunks', 'rl_patterns', 'rl_pron', 'q_arcade', 'rl_role', 'rl_write', 'rl_exit', 'q_wrap']
    pages = []
    for t in ORDER:
        p = dict(P[t]); p['stage'] = CHAP[t]; pages.append(p)
    plan = {m: [dict(id=k, name=CH[k][1], ic=CH[k][0], c=CH[k][2], min=MIN[m][k], desc=DESC[k]) for k in CH if k != 'lab' or True] for m in MIN}
    L = dict(n=n, topic=nb['t'], level='A1', title=title, pt=en['s'], unit=P['q_cover']['unit'], minutes=60, cast=[npc, 'You'], scene=en['sc'], tod='day', plan=plan, dialog=dict(speakers={npc: dict(name=npcface), 'You': dict(name='Mia')}, lines=lines),
        pages=pages, badge=S.get('badge', dict(icon='🏅', name=nb['t'], desc=strip(en['p']))), sticker=S.get('sticker', dict(cat=en['a']['w'], title=en['a']['w'], sub=nb['t'], art=dict(rs=(wrap.get('sticker') or {}).get('rs') or en['sc'], chars=(wrap.get('sticker') or {}).get('chars')))), fmt='quest',
        src=dict(regular=en['n'], neighbors=nb['n'], reg_idx=S.get('reg', n)))
    os.makedirs(os.path.join(ROOT, 'professor', 'data', 'v4'), exist_ok=True)
    if n == 1:
        from lesson1_content import refine
        refine(L, S)
    else:
        from lesson_focus import focus
        focus(L, P, S, dict(en=en, nb=nb, lines=[dict(who=l['who'], en=l['en'], pt=l['pt']) for l in lines], vocab=[(v[0], v[1], v[2]) for v in vocab], npc=npc, npcface=npcface, face_of=face_of, extras=extras(n)))
    from lesson_post import post
    X_ = extras(n); ems = [v.get('e', '') for v in (X_.get('vocab') or [])] or (['☕', '🥐', '🥛', '🧁', '🍵'] if n == 1 else [])
    post(L, n, ylayer(n), S, X_, prev_ctx(n), ems, zlayer(n))
    f = os.path.join(ROOT, 'professor', 'data', 'v4', '%03d.json' % n); json.dump(L, open(f, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':')); return f
if __name__ == '__main__':
    a = sys.argv[1:]
    if '--table' in a:
        for i in range(len(EN)): print('R%d | %s | %s' % (i + 1, EN[i]['t'], EN[i]['a']['w']))
        for i in range(120): print("N%d | %s" % (i + 1, NB[i]["t"]))
    else:
        for n in (range(1, 121) if '--all' in a else map(int, a)): print('ok', build(n))
