#!/usr/bin/env python3
"""Expande as especificações compactas (lessons_*.py) em aulas de ~1 hora (professor/data/lessons/NNN.json) + índice.
Uso: python3 professor/src/build.py"""
import glob, importlib.util, json, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, '..', 'data')
sys.path.insert(0, HERE)
from roster import PEOPLE, LOOK

def pairs(s):
    r = []
    for x in [x.strip() for x in re.split(r'\|', s) if x.strip()]:
        a, b = x.split('=', 1); r.append((a.strip(), b.strip()))
    return r

def lvl(n): return 'A1' if n <= 70 else 'A2'
GEN = ['book', 'water', 'phone', 'house', 'bus', 'coffee', 'friend', 'street', 'bag', 'door', 'table', 'window', 'ticket', 'map', 'hat', 'key']

def mcq(q, opts, ans, **k):
    return dict(t='mcq', q=q, opts=opts, ans=ans, **k)

def shuffle_opts(correct, wrong, seed):
    u = []
    for w in wrong:
        if w != correct and w not in u: u.append(w)
    o = [correct] + u[:3]; r = random.Random(seed); r.shuffle(o); return o, o.index(correct)

def expand(S):
    n = S['n']; rnd = random.Random(n)
    W = pairs(S['w']); PH = pairs(S['ph']); D = []
    for ln in S['dlg'].split('|'):
        who, rest = ln.split(':', 1); en, pt = rest.split('=', 1); D.append(dict(who=who.strip(), en=en.strip(), pt=pt.strip()))
    cast = S['who']; people = {p['name']: p for p in PEOPLE}
    fic = dict(scene=S['sc'], tod=S.get('tod', 'day'), decor=S.get('decor', []), cast=[dict(p=dict(LOOK[c], arms=['wave', 'point', 'out', 'up'][i % 4])) for i, c in enumerate(cast[:4])])
    allw = [w[0] for w in W]
    sl = []
    def add(t, m, **k): sl.append(dict(t=t, min=m, **k))
    add('cover', 1, title=S['t'], pt=S['pt'], level=lvl(n), n=n, cast=cast[:4])
    add('goals', 1, goal=S['goal'], canDo=S['can'].split('|'))
    add('warm', 3, q=S['warm'].split('=')[0], pt=S['warm'].split('=')[1], chips=[p[0] for p in PH[:4]])
    add('scene', 2, text=S['sit'], line=D[0]['en'], who=cast[:4])
    add('vocab', 5, words=[dict(en=a, pt=b) for a, b in W])
    # listen & pick
    qs = []
    for i, (a, b) in enumerate(W[:6]):
        wrong = [x[1] for x in W if x[1] != b]; rnd.shuffle(wrong)
        o, c = shuffle_opts(b, wrong[:3], n * 31 + i)
        qs.append(dict(q='Ouça e escolha o significado', say=a, opts=o, ans=c))
    add('mcq', 2, title='Escute e escolha', items=qs, mode='listen')
    add('match', 3, pairs=[dict(en=a, pt=b) for a, b in W[:6]])
    add('dialog', 4, lines=D, who=cast[:4])
    cq = []
    for i, s in enumerate(S['q']):
        q, rest = s.split('=', 1); opts = rest.split('|'); o, c = shuffle_opts(opts[0], opts[1:], n * 17 + i); cq.append(dict(q=q, opts=o, ans=c))
    add('mcq', 2, title='Compreensão do diálogo', items=cq, mode='read')
    add('phrases', 3, items=[dict(en=a, pt=b) for a, b in PH])
    add('shadow', 3, items=[a for a, b in PH[:6]] + [d['en'] for d in D[:2]])
    pats = S['pat']
    p0 = pats[0]
    add('pattern', 2, frame=p0[0], note=p0[1], slots=[dict(en=a, pt=b) for a, b in pairs(p0[2])])
    add('drill', 4, frame=p0[0], cues=[dict(en=a, pt=b) for a, b in pairs(p0[2])])
    sc = []
    for a, b in PH + [(d['en'], d['pt']) for d in D]:
        ws = re.findall(r"[\w'’]+|[.,!?]", a)
        if len(ws) >= 4 and len(ws) <= 9 and a not in [x['en'] for x in sc]: sc.append(dict(words=ws, en=a, pt=b))
        if len(sc) == 5: break
    add('scramble', 2, items=sc)
    # gap fill from dialogue
    gp = []
    for i, d in enumerate(D[1:5]):
        ws = d['en'].split(); idx = [j for j, w in enumerate(ws) if len(re.sub(r'\W', '', w)) > 2]
        if not idx: continue
        j = idx[(i * 2 + 1) % len(idx)]; ans = re.sub(r'[^\w\'’]', '', ws[j])
        wrong = [x for x in allw + GEN if x.lower() != ans.lower()]; rnd.shuffle(wrong)
        o, c = shuffle_opts(ans, wrong[:3], n * 13 + i)
        gp.append(dict(before=' '.join(ws[:j]), after=' '.join(ws[j + 1:]), ans=ans, opts=o, ci=c, who=d['who'], pt=d['pt']))
    add('gap', 2, items=gp)
    add('roleplay', 4, lines=D, a=D[0]['who'], b=next((d['who'] for d in D if d['who'] != D[0]['who']), D[0]['who']))
    if len(pats) > 1:
        p1 = pats[1]
        add('pattern', 1, frame=p1[0], note=p1[1], slots=[dict(en=a, pt=b) for a, b in pairs(p1[2])])
        add('drill', 3, frame=p1[0], cues=[dict(en=a, pt=b) for a, b in pairs(p1[2])])
    rq = []
    for i, s in enumerate(S['rq']):
        q, rest = s.split('=', 1); opts = rest.split('|'); o, c = shuffle_opts(opts[0], opts[1:], n * 19 + i); rq.append(dict(q=q, opts=o, ans=c))
    add('read', 4, title=S['rt'], text=S['rd'], pt=S.get('rdpt', ''), qs=rq)
    add('dict', 2, items=[a for a, b in PH[2:5]] + [D[1]['en']])
    add('write', 5, prompt=S['wr'], frame=S.get('wf', ''), words=allw[:8])
    add('speak', 4, task=S['sp'], hints=[a for a, b in PH[:4]])
    gq = []
    pool = W + [(a, b) for a, b in PH]
    for i in range(8):
        a, b = pool[(i * 3 + n) % len(pool)]
        if i % 2 == 0:
            wrong = [x[1] for x in pool if x[1] != b]; rnd.shuffle(wrong); o, c = shuffle_opts(b, wrong[:3], n * 7 + i); gq.append(dict(q=a, opts=o, ans=c, say=a))
        else:
            wrong = [x[0] for x in pool if x[0] != a]; rnd.shuffle(wrong); o, c = shuffle_opts(a, wrong[:3], n * 7 + i); gq.append(dict(q=b, opts=o, ans=c))
    add('game', 3, title='Jogo rápido', items=gq)
    add('culture', 1, title=S['cuh'], text=S['cu'])
    add('recap', 1, canDo=S['can'].split('|'), homework=S['hw'])
    return dict(n=n, level=lvl(n), title=S['t'], pt=S['pt'], scene=S['sc'], tod=S.get('tod', 'day'), cast=cast[:4], fic=fic, minutes=sum(s['min'] for s in sl), slides=sl)

def main():
    LS = {}
    for fn in sorted(glob.glob(os.path.join(HERE, 'lessons_*.py'))):
        spec = importlib.util.spec_from_file_location('m', fn); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for S in m.LESSONS: LS[S['n']] = S
    idx = []
    for n, S in sorted(LS.items()):
        L = expand(S)
        json.dump(L, open(os.path.join(OUT, 'lessons', '%03d.json' % n), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
        idx.append(dict(n=n, level=L['level'], title=S['t'], pt=S['pt'], scene=S['sc'], tod=L['tod'], minutes=L['minutes'], slides=len(L['slides']), fic=L['fic'], words=len(pairs(S['w']))))
    json.dump(dict(course='en', series='Maple Street', lessons=idx), open(os.path.join(OUT, 'index.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    json.dump([dict(PEOPLE[i], look=LOOK[PEOPLE[i]['name']]) for i in range(100)], open(os.path.join(OUT, 'elenco.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    print('aulas:', len(idx), '| min/aula:', sorted({i['minutes'] for i in idx}))
main()
