# B1 lote ZZ-A: troca de obra repetida por obra nova (livro infantil, conto, fábula, cantiga, poema, clássico) com o episódio inteiro refeito.
# Cada episódio é declarado uma vez com EP(...) em zz_b1a_d*.py; o gancho ovrb1.HOOK substitui o episódio por completo
# (obra, elenco, 6 palavras, 5 objetos quentes, 4 verbos, 3 sons, cena de 8 falas, 3 perguntas, lacunas, armadilhas, regra, molde, missões e expressões).
# Obras gravadas em obras_new_b1_zz_a.json por gen_zz_b1a_works.py.
import re, os, json

SPECS = {}


def EP(n, rs, names, ids, ob, cv, voc, hot, lines, quiz, vb, lab, gp, ex):
    assert len(voc) == 6 and len(hot) == 5 and len(lines) == 8 and len(quiz) == 3 and len(vb) == 4 and len(lab[4]) == 3 and len(gp) == 4 and len(ex) == 4, n
    for g in gp:
        assert g[1] in hot[g[0]][3], (n, g)
    for e in ex:
        assert e[1].lower() in e[4].lower(), (n, e)
    vw = {v[1] for v in voc}
    for w in lab[4]:
        assert w[0] in vw, (n, 'lab', w[0])
    SPECS[n] = dict(n=n, rs=rs, names=tuple(names), ids=list(ids), ob=ob, cv=cv, voc=voc, hot=hot, lines=lines, quiz=quiz, vb=vb, lab=lab, gp=gp, ex=ex)


def work(s):
    name, kind, year, desc, topic, theme, emojis = s['ob']
    return dict(name=name, kind='%s · %s' % (kind, year), text='%s é %s A referência ajuda a falar de %s. A cena é autoral; não adapta nem cita a obra.' % (name, desc, topic),
                line=['', ''], pa=dict(t=theme, e=list(emojis), v=0))


def _hook(n):
    def f(base, k):
        from v3 import short
        from v3 import ova2b as B
        from v3.lib import OB
        s = SPECS[n]
        a, b = s['names']
        lines = [[a if i % 2 == 0 else b, en, pt] for i, (en, pt) in enumerate(s['lines'])]
        vocab = [(e, w, pt, 'Soa como “%s”.' % pr) for (e, w, pt, pr) in s['voc']]
        hot = [tuple(h) for h in s['hot']]
        quiz = [(q[0], q[1], [q[3], q[4], q[5]], 0, q[2], '%s diz: “%s”' % (lines[q[2]][0], lines[q[2]][1])) for q in s['quiz']]
        verbs = [(v, ic, pt, eu, ele, ex, ept, '**%s** = %s.' % (v, pt)) for (v, ic, pt, eu, ele, ex, ept) in s['vb']]
        lb = s['lab']
        lab = B.L(lb[0], lb[1], lb[2], lb[3], lb[4], [hot[0][3], hot[0][4]])
        why = k['why']
        if ': ' in why:
            why = why.split(': ')[0] + ': ' + ' '.join(h[3] for h in hot[:3])
        kk = dict(n=n, title=k['title'], sub=re.sub(r'\([^()]*\)\s*$', '(' + ', '.join(v[1] for v in s['voc']) + ')', k['sub']), pattern=k['pattern'], why=why,
                  names=s['names'], ids=s['ids'], rs=s['rs'], obra=OB(n, lines[0][1], lines[0][2], p='b'), hot=hot, cover=(k['cover'][0], s['cv']),
                  vocab=vocab, lines=lines, quiz=quiz, dictate=[[h[3], h[4]] for h in hot[:4]], teaser=k['teaser'], lab=lab,
                  verbs=('Verbos do episódio', 'Quatro verbos: ' + ', '.join(v[0] for v in verbs[:3]) + ' e ' + verbs[3][0] + '.', verbs),
                  speak=[[h[3], h[4]] for h in hot[:2]], scenes=k.get('scenes'))
        B._derive(kk, s['gp'], s['ex'])
        return short.E(**kk)
    return f


def install_all():
    from v3 import ovrb1
    for n in SPECS:
        ovrb1.HOOK[n] = _hook(n)
