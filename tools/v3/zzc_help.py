# Auxiliares das sobrescritas ova2b_241_zz_c*.py (lote C: obras novas de TV, teatro, quadrinhos, jogos, ópera/balé, mitos e músicas).
from v3.ova2b import X, W, L, Q, G


def vb(v, ic, pt, subj, third, rest, pron, ex, expt):
    """Verbo: frase certa/errada na 3a pessoa; ex = segunda frase (en/pt)."""
    return (v, ic, pt, '%s %s %s.' % (subj, third, rest), '%s %s %s.' % (subj, v, rest), ex, expt, '%s **%s**.' % (pron, third))


def EP(n, names, ids, w, voc, hot, lines, quiz, verbs, lab, gp, ex, cv):
    X(n, names, ids, W(*w), [(a, b, c, 'Soa como “%s”.' % d) for a, b, c, d in voc], hot, [list(x) for x in lines],
      [Q(*q) for q in quiz], verbs=[vb(*v) for v in verbs], lab=lab, cv=cv)
    G(n, gp, ex)
