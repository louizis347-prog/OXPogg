# Lote B do A1 (cinema): troca de obra de episódios cujo módulo ep_*.py usa E (camada ova2 -> ova1_zz_b*.py).
# Cada episódio é escrito como bloco de texto compacto (ver parse) em zz_b_d*.py e instalado por ova1_zz_b.py via put_layer(n).
# Campos (uma linha cada; campos separados por '|'):
#   N: n do episódio            C: Nome1,Nome2 | id1,id2 | resumo da capa (pt)
#   S: prefixo do subtítulo (pt) Y: 'por que' do episódio (pt)
#   F: obra | tipo | ano | descrição (pt) | tema que ajuda a falar (pt) | cenário (castle/toyshop/bakery/viaduct/jungle/cave/rainycafe/lighthouse/ship/library) | e1,e2,e3
#   V: emoji|palavra|pt|pronúncia (6)     H: en|pt (5, falas dos 5 primeiros objetos)   L: en|pt (8 falas alternadas)
#   Q: pergunta|pt|índice da fala|emoji certo texto|emoji errado texto|emoji errado texto (3)
#   B: verbo|emoji|pt|eu|ele|exemplo en|exemplo pt (4)
#   LAB: curto|título|pt|dica    W: palavra|pron|pt|dica|par|pron do par (3)
#   G: índice do objeto|palavra-chave|errada1|errada2 (4)     X: emoji|expressão|pt|uso|exemplo en|exemplo pt (4)
import re
SPECS = {}


def _sp(s):
    return [x.strip() for x in s.split('|')]


def parse(txt):
    d = {'V': [], 'H': [], 'L': [], 'Q': [], 'B': [], 'W': [], 'G': [], 'X': []}
    for ln in txt.strip().split('\n'):
        ln = ln.strip()
        if not ln or ln.startswith('#'):
            continue
        k, v = ln.split(':', 1)
        k = k.strip(); v = v.strip()
        if k in d and isinstance(d[k], list):
            d[k].append(_sp(v))
        else:
            d[k] = _sp(v) if k in ('C', 'F', 'LAB') else v
    n = int(d['N'])
    names, ids, cv = d['C']
    assert len(d['V']) == 6 and len(d['H']) == 5 and len(d['L']) == 8 and len(d['Q']) == 3 and len(d['B']) == 4 and len(d['W']) == 3 and len(d['G']) == 4 and len(d['X']) == 4, n
    for v in d['V']: assert len(v) == 4, (n, v)
    for v in d['H'] + d['L']: assert len(v) == 2, (n, v)
    for v in d['B']: assert len(v) == 7, (n, v)
    for v in d['W']: assert len(v) == 6, (n, v)
    for v in d['X']: assert len(v) == 6, (n, v)
    assert len(d['F']) == 7 and len(d['LAB']) == 4, n
    for g in d['G']:
        en = d['H'][int(g[0])][0]; key = g[1]
        m = re.search(r'(?<![\w’\'])' + re.escape(key) + r'(?![\w’\'])', en)
        assert m and en.find(key) == m.start(), (n, 'chave', key, en)
        assert key not in (g[2], g[3]), (n, key)
    for x in d['X']:
        assert x[1].lower() in x[4].lower(), (n, 'expressao', x[1], x[4])
    SPECS[n] = dict(n=n, T=d.get('T'), names=tuple(x.strip() for x in names.split(',')), ids=[x.strip() for x in ids.split(',')], cv=cv, S=d['S'], Y=d['Y'], F=d['F'],
                    V=d['V'], H=d['H'], L=d['L'], Q=d['Q'], B=d['B'], LAB=d['LAB'], W=d['W'], G=d['G'], X=d['X'])
    return n


def add(*texts):
    for t in texts:
        for blk in re.split(r'\n(?=N:)', t.strip()):
            if blk.strip():
                parse(blk)


def put_layer(n):
    from v3 import ova2 as O
    from v3 import ova2b as B
    s = SPECS[n]
    name, kind, year, desc, topic, theme, emo = s['F']
    O.Wk(n, name, '%s · %s' % (kind, year), '%s é %s A referência ajuda a falar de %s.' % (name, desc, topic), theme, emo.split(','))
    a, b = s['names']
    lines = [[a if i % 2 == 0 else b, en, pt] for i, (en, pt) in enumerate(s['L'])]
    vocab = [(e, w, pt, 'Soa como “%s”.' % pr) for (e, w, pt, pr) in s['V']]
    verbs = [(v, ic, pt, eu, ele, ex, ept, '**%s** = %s.' % (v, pt)) for (v, ic, pt, eu, ele, ex, ept) in s['B']]
    hot = [(v[0], v[1], v[2], h[0], h[1]) for v, h in zip(s['V'], s['H'])]
    quiz = []
    for (q, qpt, li, ok, w1, w2) in s['Q']:
        li = int(li)
        o3 = []
        for t in (ok, w1, w2):
            e, tx = t.split(' ', 1)
            o3.append((e, tx))
        quiz.append((q, qpt, o3, 0, li, '%s diz: “%s”' % (lines[li][0], lines[li][1])))
    sh, ti, pt, tip = s['LAB']
    lab = O.L(sh, ti, pt, tip, [O.Lw(*w) for w in s['W']])
    O.OVR[n] = dict(names=s['names'], ids=s['ids'], cv=s['cv'], vocab=vocab, hot=hot, verbs=verbs, lab=lab, lines=lines, quiz=quiz, fill=[], rs=None)
    gp = [(int(g[0]), g[1], g[2], g[3]) for g in s['G']]
    ex = [tuple(x) for x in s['X']]

    def post(k):
        h = k['hot']
        k['sub'] = re.sub(r'\([^()]*\)\s*$', '', k['sub'])
        k['sub'] = s['S'] + ' (' + ', '.join(v[1] for v in k['vocab']) + ')'
        k['why'] = s['Y']
        if s.get('T'): k['title'] = s['T']
        k['dictate'] = [[x[3], x[4]] for x in h[:4]]
        k['speak'] = [[x[3], x[4]] for x in h[:2]]
        B._derive(k, gp, ex)
    O.OVR[n]['post'] = post
