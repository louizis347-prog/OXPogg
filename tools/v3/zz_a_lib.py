# Lote A (obras novas de livros infantis, contos de fadas, fábulas, cantigas, literatura clássica/juvenil e poemas) para episódios A2 que repetiam obra.
# Cada episódio é declarado uma vez com EP(...) e instalado na camada certa:
#   put_ova2(n)  -> v3.ova2  (itens 1-240; usa o gancho 'post' do ova2.E2 para refazer gaps, regra, molde, missões e expressões)
#   put_ova2b(n) -> v3.ova2b (itens 241+; X + G)
# Arquivos de dados: zz_a_d*.py (não casam com os globs ova2_*.py / ova2b_241_*.py; são importados por ova2_zz_a.py e ova2b_241_zz_a.py).
SPECS = {}


def EP(n, rs, names, ids, ob, cv, voc, hot, lines, quiz, vb, lab, gp, ex):
    assert len(voc) == 6 and len(hot) == 5 and len(lines) == 8 and len(quiz) == 3 and len(vb) == 4 and len(lab[4]) == 3 and len(gp) == 4 and len(ex) == 4, n
    SPECS[n] = dict(n=n, rs=rs, names=tuple(names), ids=list(ids), ob=ob, cv=cv, voc=voc, hot=hot, lines=lines, quiz=quiz, vb=vb, lab=lab, gp=gp, ex=ex)


def _lines(s):
    a, b = s['names']
    return [[a if i % 2 == 0 else b, en, pt] for i, (en, pt) in enumerate(s['lines'])]


def _vocab(s):
    return [(e, w, pt, 'Soa como “%s”.' % pr) for (e, w, pt, pr) in s['voc']]


def _verbs(s):
    return [(v, ic, pt, eu, ele, ex, ept, '**%s** = %s.' % (v, pt)) for (v, ic, pt, eu, ele, ex, ept) in s['vb']]


def _hot(s):
    return [(v[0], v[1], v[2], h[0], h[1]) for v, h in zip(s['voc'], s['hot'])]


def _obtext(s):
    name, kind, year, desc, topic, theme, emojis, len_, lpt = s['ob']
    return name, '%s · %s' % (kind, year), '%s é %s A referência ajuda a falar de %s.' % (name, desc, topic), theme, emojis


def put_ova2(n):
    from v3 import ova2 as O
    from v3 import ova2b as B
    s = SPECS[n]
    name, kind, text, theme, emojis = _obtext(s)
    O.Wk(n, name, kind, text, theme, emojis)
    a, b = s['names']
    ws = s['lab'][4]
    lab = O.L(s['lab'][0], s['lab'][1], s['lab'][2], s['lab'][3], [O.Lw(*w) for w in ws])
    quiz = [tuple(q) for q in s['quiz']]
    O.X(n, s['names'], s['ids'], s['cv'], [O.V(*v) for v in s['voc']], [tuple(h) for h in s['hot']], [O.VB(*v) for v in s['vb']], lab, _lines(s), quiz, [], rs=s['rs'])
    gp, ex = s['gp'], s['ex']

    def post(k):
        h = k['hot']
        if ': ' in k['why']:
            k['why'] = k['why'].split(': ')[0] + ': ' + ' '.join(x[3] for x in h[:3])
        k['dictate'] = [[x[3], x[4]] for x in h[:4]]
        k['speak'] = [[x[3], x[4]] for x in h[:2]]
        B._derive(k, gp, ex)
    O.OVR[n]['post'] = post


def put_ova2b(n):
    from v3 import ova2b as B
    s = SPECS[n]
    name, kind, text, theme, emojis = _obtext(s)
    w = B.W(s['ob'][0], s['ob'][1], s['ob'][2], s['ob'][3], s['ob'][4], theme, emojis, s['ob'][7], s['ob'][8])
    lab = B.L(s['lab'][0], s['lab'][1], s['lab'][2], s['lab'][3], s['lab'][4], list(s['hot'][0]))
    B.X(n, s['names'], s['ids'], w, _vocab(s), _hot(s), _lines(s), [B.Q(*q) for q in s['quiz']], _verbs(s), lab, cv=s['cv'], rs=s['rs'])
    B.G(n, s['gp'], s['ex'])
