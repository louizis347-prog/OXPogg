#!/usr/bin/env python3
"""Aulas Quest v5 = JUNÇÃO enxuta do curso regular (en-a1, episódios principais) + Neighbors (nb-a1, sem revisões de arco)
+ suplemento pequeno (src/supp5/sNNN.py → SUPP: culture, reading, convo, errors, homework). Não lê data/v3.
Uso: python3 src/build_v5.py 1 2 3 | --all | --table"""
import glob, importlib.util, json, math, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
from build_v4 import CH, MIN, DESC, CHAP
CHAP.update({'rl_write': 'write', 'q_story': 'mission', 'q_phrase': 'talk', 'q_dialog': 'talk', 'q_say': 'lab', 'q_mold': 'lab', 'q_sound': 'lab', 'q_role': 'boss', 'q_free': 'write'})
def load(p):
    o = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', p + '_*.json'))): o += json.load(open(f, encoding='utf-8'))
    return o
EN = [e for e in load('en-a1') if e['n'] < 7000000]
FILLER = {'That sounds good. What should we do next?', 'Let me check the details before we decide.', 'Could you say that one more time?', 'Sure, I will explain it clearly.', 'Thanks, now I know how to continue.'}
NB = [e for e in load('nb-a1') if not str(e['t']).lower().startswith(('arc ', 'review'))]
strip = lambda s: re.sub(r'\*\*|\{\{|\}\}', '', s or '')
bold = lambda s: re.sub(r'\{\{(.+?)\}\}', r'**\1**', s or '')
def fr(e, k): return [f for f in e['fr'] if f['k'] == k]
def supp(n):
    f = os.path.join(HERE, 'supp5', 's%03d.py' % n)
    if not os.path.exists(f): return {}
    spec = importlib.util.spec_from_file_location('s5%03d' % n, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.SUPP

import zlib
ELENCO = [x['name'] for x in json.load(open(os.path.join(ROOT, 'professor', 'data', 'elenco.json'), encoding='utf-8'))]
def face_of(name): return ELENCO[zlib.crc32(name.encode()) % len(ELENCO)]
def vis(n):
    f = os.path.join(HERE, 'vis5', 'v%03d.py' % n)
    if not os.path.exists(f): return {}
    spec = importlib.util.spec_from_file_location('v5%03d' % n, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.VIS
def build(n):
    S = supp(n); en, nb = EN[S.get('reg', n) - 1], NB[n - 1]
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
    L_dialog_lines = [dict(who=l['who'], en=l['en'], pt=l['pt']) for l in lines]
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
    if S.get('story'): P['q_story'] = dict(t='q_story', title='Story time', steps=S['story'])
    if S.get('phrase'): P['q_phrase'] = dict(t='q_phrase', title=S['phrase'].get('title', 'Situation & phrase'), **{k: v for k, v in S['phrase'].items() if k != 'title'})
    if S.get('dlg'): P['q_dialog'] = dict(t='q_dialog', title='Dialogue — ' + nb['t'], **S['dlg'])
    if S.get('say'): P['q_say'] = dict(t='q_say', title='Say it', **S['say'])
    for key, t in (('mold', 'q_mold'), ('sound', 'q_sound'), ('role', 'q_role'), ('free', 'q_free')):
        if S.get(key): P[t] = dict(t=t, title={'mold': 'Word mold', 'sound': 'Sound lab', 'role': 'Boss mission', 'free': 'Free production'}[key], **S[key])
    if S.get('speed'): P['q_arcade']['games']['speed'] = S['speed']
    for k, v in (S.get('arts') or {}).items():
        if k in P: P[k]['art'] = v
    if S.get('sticker_art'): P['q_wrap']['sticker_art'] = S['sticker_art']
    V = vis(n)
    if V:
        for k, v in (V.get('arts') or {}).items():
            if k in P: P[k]['art'] = v
        if V.get('convo'):
            cvv = dict(V['convo']); cvv['npc'] = dict(cvv.get('npc') or {'name': npc}); cvv['npc'].setdefault('face', npcface)
            P['q_choose'] = dict(t='q_choose', title='Choose your reply', art=P['q_choose'].get('art'), **cvv)
        if V.get('story_scenes'):
            tx = P['q_read']['text']; sc = V['story_scenes']; ptx = V.get('story_pt') or [''] * len(tx)
            P['q_story'] = dict(t='q_story', title='Story time', steps=[dict(en=tx[i], pt=ptx[i] if i < len(ptx) else '', art=sc[min(i, len(sc) - 1)]) for i in range(len(tx))])
        if V.get('dlg'): P['q_dialog'] = dict(t='q_dialog', title='Dialogue — ' + nb['t'], **V['dlg'])
        if V.get('phrase'): P['q_phrase'] = dict(t='q_phrase', title=V['phrase'].get('title', 'Situation & phrase'), **{k: v for k, v in V['phrase'].items() if k != 'title'})
        if V.get('say'): P['q_say'] = dict(t='q_say', title='Say it', **V['say'])
        if V.get('role'): P['q_role'] = dict(t='q_role', title='Boss mission', **V['role'])
        if V.get('sticker_art'): P['q_wrap']['sticker_art'] = V['sticker_art']
    if S.get('cando'): P['q_cover']['canDo'] = S['cando']
    if S.get('pt'): P['q_cover']['pt'] = S['pt']
    if S.get('goal'): P['q_cover']['goal'] = S['goal']
    if S.get('chunks'): P['rl_chunks']['items'] = S['chunks']
    if S.get('title_pt'): P['q_cover']['title'] = S['title_pt']
    if 'q_dialog' not in P and L_dialog_lines:
        P['q_dialog'] = dict(t='q_dialog', title='Dialogue — ' + nb['t'], me='You', faces={npc: npcface, 'You': 'Mia'}, art=P['rl_dialog'].get('art'), lines=L_dialog_lines, qs=[dict(q=x['q'], opts=x['opts'], ans=x['ans'], why='Listen to the dialogue again.') for x in P['rl_dialog'].get('qs', []) if len(x.get('opts', [])) == 3])
    ORDER = ['q_cover', 'q_story', 'q_culture', 'q_read', 'q_dialog' if 'q_dialog' in P else 'rl_dialog', 'q_phrase', 'q_choose', 'rl_chunks', 'q_say', 'rl_patterns', 'rl_pron', 'q_arcade', 'q_role' if 'q_role' in P else 'rl_role', 'rl_write', 'rl_exit', 'q_wrap']
    ORDER = [t for t in ORDER if t in P]
    pages = []
    def sub(p, t, **kw):
        q = dict(p); q.update(kw)
        if t is not None: q['title'] = t
        return q
    def explode(t, p):
        T = p.get('title', '')
        if t == 'q_cover': return [sub(p, None, view='a'), sub(p, 'Mission · what you will do', view='b')]
        if t == 'q_story':
            st = p['steps']; return [sub(p, 'Story time · %d/%d' % (i + 1, len(st)), steps=[x], art=x.get('art')) for i, x in enumerate(st)]
        if t == 'q_culture':
            names = ['Explore the scene', 'Fact file', 'Myth or fact?', 'In the wild', 'Compare', 'Quiz'] if p.get('hot') else ['Fact file', 'Myth or fact?', 'In the wild', 'Compare', 'Quiz']
            return [sub(p, 'Cultural spotlight · ' + n, only=i, nohook=(i > 0)) for i, n in enumerate(names)]
        if t == 'q_read':
            tx = p['text']; h = (len(tx) + 1) // 2
            out = [sub(p, T + ' · part 1', text=tx[:h], textOnly=True), sub(p, T + ' · part 2', text=tx[h:], textOnly=True)]
            return out + [sub(p, 'Reading quest · ' + n, only=i, text=tx) for i, n in enumerate(['Skim', 'Scan', 'True or false', 'Order the story', 'Words in context', 'Talk about it'])]
        if t == 'q_dialog':
            ln = p['lines']; h = (len(ln) + 1) // 2
            return [sub(p, 'Dialogue · part 1', lines=ln[:h], qs=[]), sub(p, 'Dialogue · part 2', lines=ln[h:], qs=[]), sub(p, 'Dialogue · check', lines=[], qonly=True)]
        if t == 'q_choose':
            tr = p['turns']; h = (len(tr) + 1) // 2
            return [sub(p, 'Choose your reply · 1/2', turns=tr[:h]), sub(p, 'Choose your reply · 2/2', turns=tr[h:])]
        if t == 'rl_chunks':
            it = p['items']; h = (len(it) + 1) // 2
            return [sub(p, 'Useful expressions · 1/2', items=it[:h]), sub(p, 'Useful expressions · 2/2', items=it[h:])]
        if t == 'q_say':
            it = p['items']; h = (len(it) + 1) // 2 + (1 if len(it) % 2 == 0 else 0)
            return [sub(p, 'Say it · 1/2', items=it[:h]), sub(p, 'Say it · 2/2', items=it[h:])]
        if t == 'q_mold':
            return [sub(p, 'Word mold · ' + f['title'], frames=[f]) for f in p['frames']]
        if t == 'q_sound':
            it = p['items']; h = (len(it) + 1) // 2
            return [sub(p, 'Sound lab · 1/3', items=it[:h], identify=[]), sub(p, 'Sound lab · 2/3', items=it[h:], identify=[]), sub(p, 'Sound lab · listen & choose', items=[], identify=p['identify'])]
        if t == 'q_arcade':
            g = p['games']; ids = [('pairs', 'Memory match', 'pairs'), ('uns', 'Unscramble', 'unscramble'), ('err', 'Error hunt', 'errors'), ('spd', 'Speed round', 'speed'), ('dic', 'Dictation', 'dict')]
            return [sub(p, 'Practice arcade · ' + n, game=i) for i, n, k in ids if g.get(k)]
        if t == 'rl_patterns':
            sw = p.get('swap'); out = []
            if p.get('patterns'): out.append(sub(p, 'Patterns', swap=None))
            if sw and sw.get('slots'): out.append(dict(t='q_mold', title='Word mold', art=p.get('art'), frames=[dict(title='Build it', frame=sw['frame'], tpt=sw.get('tpt', ''), slots=sw['slots'])], stage='lab'))
            return out or [p]
        if t == 'rl_pron':
            clean = lambda s: re.sub(r'\*\*', '', s or '')
            it = [dict(say=clean(x['say']), linked=clean(x.get('linked', '')), note=clean(x.get('note', ''))) for x in p.get('items', [])]
            idn = p.get('identify') or []
            h = (len(it) + 1) // 2; out = []
            base = dict(t='q_sound', art=p.get('art'), focus=clean(p.get('focus', '')), tip=clean(p.get('tip', '')), stage='lab')
            if len(it) > 1: out += [dict(base, title='Sound lab · 1/%d' % (3 if idn else 2), items=it[:h], identify=[]), dict(base, title='Sound lab · 2/%d' % (3 if idn else 2), items=it[h:], identify=[])]
            elif it: out.append(dict(base, title='Sound lab', items=it, identify=[]))
            if idn: out.append(dict(base, title='Sound lab · listen & choose', items=[], identify=idn))
            return out or [p]
        if t == 'rl_write':
            clean = lambda s: re.sub(r'\*\*', '', s or '')
            mdl = clean(p.get('model', '')); tg = []
            for w in re.findall(r"[A-Za-z’']{4,}", mdl.lower()):
                if w not in tg: tg.append(w)
            return [dict(t='q_free', title='Free production', art=p.get('art'), prompt=clean(p.get('task', '')), chips=[], targets=tg[:12], model=mdl, stage='write')]
        if t == 'q_wrap': return [sub(p, 'Mission complete', view='a'), sub(p, 'Sticker & next stop', view='b')]
        return [p]
    for t in ORDER:
        for q in explode(t, P[t]):
            q = dict(q); q['stage'] = CHAP[t]; pages.append(q)
    plan = {m: [dict(id=k, name=CH[k][1], ic=CH[k][0], c=CH[k][2], min=MIN[m][k], desc=DESC[k]) for k in CH if k != 'lab' or True] for m in MIN}
    L = dict(n=n, topic=nb['t'], level='A1', title=title, pt=en['s'], unit=P['q_cover']['unit'], minutes=60, cast=[npc, 'You'], scene=en['sc'], tod='day', plan=plan, dialog=dict(speakers={npc: dict(name=npcface), 'You': dict(name='Mia')}, lines=lines),
        pages=pages, badge=S.get('badge', dict(icon='🏅', name=nb['t'], desc=strip(en['p']))), sticker=S.get('sticker', dict(cat=en['a']['w'], title=en['a']['w'], sub=nb['t'], art=(vis(n).get('sticker_art')) or S.get('sticker_art') or dict(rs=(wrap.get('sticker') or {}).get('rs') or en['sc'], chars=(wrap.get('sticker') or {}).get('chars')))), fmt='quest',
        src=dict(regular=en['n'], neighbors=nb['n'], reg_idx=S.get('reg', n)))
    os.makedirs(os.path.join(ROOT, 'professor', 'data', 'v4'), exist_ok=True)
    f = os.path.join(ROOT, 'professor', 'data', 'v4', '%03d.json' % n); json.dump(L, open(f, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':')); return f
if __name__ == '__main__':
    a = sys.argv[1:]
    if '--table' in a:
        for i in range(len(EN)): print('R%d | %s | %s' % (i + 1, EN[i]['t'], EN[i]['a']['w']))
        for i in range(100): print('N%d | %s' % (i + 1, NB[i]['t']))
    else:
        for n in (range(1, 101) if '--all' in a else map(int, a)): print('ok', build(n))
