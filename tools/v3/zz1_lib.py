# Lote A do A1: troca de obra (literatura infantil, contos, fábulas, cantigas, clássicos, poemas) em episódios que repetiam obra.
# Cada episódio é declarado uma vez com EP(...). Instalação:
#   put_layer(n)  -> camada ova2 (módulos A1 com E e install); ova1_zz_a.py faz isso.
#   full(n, ...)  -> usado dentro dos módulos sem camada (ep_fix_* e ep() de forma longa): devolve o episódio completo.
# Dados: zz1_d*.py. Obras: obras_new_a1_zz_a.json (gerado por zz1_works.py).
import re
SPECS = {}
# episódios cujos módulos não têm camada (ep_fix_* e ep() de forma longa): o bloco do episódio chama full() diretamente
FULL = {7030010, 7070020, 7010151, 7070021, 7030011, 7070022, 7910005, 7010152, 7070023, 7030012, 7070024, 7010153, 7070025, 7070044, 7010163,
        7910010, 7030023, 7910011, 7070047, 7030024, 7010165, 7070049, 7030025, 7910012, 7010166, 7030026, 7070052, 7010167, 7910013, 7010168,
        7030028, 7010169, 7030029, 910014, 7910014, 7010170, 7070059, 7070060, 7010171, 7070062, 7910015, 7010172, 7010173, 7070065}


def load():
    import glob, os, importlib
    here = os.path.dirname(os.path.abspath(__file__))
    for f in sorted(glob.glob(os.path.join(here, 'zz1_d*.py'))):
        importlib.import_module('v3.' + os.path.basename(f)[:-3])


def EP(n, rs, names, ids, ob, title, sub, why, cs, cv, voc, hot, lines, quiz, vb, lab, gp, ex):
    assert len(voc) == 6 and len(hot) == 5 and len(lines) == 8 and len(quiz) == 3 and len(vb) == 4 and len(lab[4]) == 3 and len(gp) == 4 and len(ex) == 4, n
    SPECS[n] = dict(n=n, rs=rs, names=tuple(names), ids=list(ids), ob=ob, title=title, sub=sub, why=why, cs=cs, cv=cv, voc=voc, hot=hot, lines=lines, quiz=quiz, vb=vb, lab=lab, gp=gp, ex=ex)


def work(s):
    name, kind, year, desc, topic, theme, emojis, len_, lpt = s['ob']
    return name, '%s · %s' % (kind, year), '%s é %s A referência ajuda a falar de %s. A cena é autoral; não adapta nem cita a obra.' % (name, desc, topic), theme, emojis


def _parts(s):
    a, b = s['names']
    lines = [[a if i % 2 == 0 else b, en, pt] for i, (en, pt) in enumerate(s['lines'])]
    vocab = [(e, w, pt, 'Soa como “%s”.' % pr) for (e, w, pt, pr) in s['voc']]
    verbs = [(v, ic, pt, eu, ele, ex, ept, '**%s** = %s.' % (v, pt)) for (v, ic, pt, eu, ele, ex, ept) in s['vb']]
    hot = [(v[0], v[1], v[2], h[0], h[1]) for v, h in zip(s['voc'], s['hot'])]
    quiz = []
    for (q, qpt, li, ok, w1, w2) in s['quiz']:
        quiz.append((q, qpt, [ok, w1, w2], 0, li, '%s diz: “%s”' % (lines[li][0], lines[li][1])))
    return lines, vocab, verbs, hot, quiz


def put_layer(n):
    from v3 import ova2 as O
    from v3 import ova2b as B
    s = SPECS[n]
    name, kind, text, theme, emojis = work(s)
    O.Wk(n, name, kind, text.replace(' A cena é autoral; não adapta nem cita a obra.', ''), theme, emojis)
    lines, vocab, verbs, hot, quiz = _parts(s)
    sh, ti, pt, tip, ws = s['lab']
    lab = O.L(sh, ti, pt, tip, [O.Lw(*w) for w in ws])
    O.OVR[n] = dict(names=s['names'], ids=s['ids'], cv=s['cv'], vocab=vocab, hot=hot, verbs=verbs, lab=lab, lines=lines, quiz=quiz, fill=[], rs=s['rs'])
    gp, ex = s['gp'], s['ex']

    def post(k):
        h = k['hot']
        k['title'], k['sub'], k['why'] = s['title'], s['sub'], s['why']
        k['cover'] = (s['cs'], s['cv'])
        k['dictate'] = [[x[3], x[4]] for x in h[:4]]
        k['speak'] = [[x[3], x[4]] for x in h[:2]]
        B._derive(k, gp, ex)
    O.OVR[n]['post'] = post


def full(n, pattern, teaser, review=True):
    """Episódio completo (mesmo formato de short.E) para módulos sem camada."""
    load()
    from v3 import ova2 as O
    from v3 import ova2b as B
    from v3.short import E
    from v3.lib import OB
    s = SPECS[n]
    lines, vocab, verbs, hot, quiz = _parts(s)
    sh, ti, pt, tip, ws = s['lab']
    lab = O._labd(O.L(sh, ti, pt, tip, [O.Lw(*w) for w in ws]), hot[0])
    k = dict(n=n, title=s['title'], sub=s['sub'], pattern=pattern, why=s['why'], names=s['names'], ids=s['ids'], rs=s['rs'],
             obra=OB(n, lines[0][1], lines[0][2], p='b'), hot=hot, cover=(s['cs'], s['cv']), vocab=vocab, lines=lines, quiz=quiz,
             dictate=[[x[3], x[4]] for x in hot[:4]], speak=[[x[3], x[4]] for x in hot[:2]], teaser=teaser, lab=lab,
             verbs=('Verbos do episódio', 'Quatro verbos: ' + ', '.join(v[0] for v in verbs[:3]) + ' e ' + verbs[3][0] + '.', verbs), review=review)
    B._derive(k, s['gp'], s['ex'])
    return E(**k)
