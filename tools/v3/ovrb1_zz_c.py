# Lote C (B1, alvos com obra repetida no curso): substituição COMPLETA do episódio por obra nova (série, teatro, quadrinhos, jogo, ópera/balé, mito, música, podcast, pintura).
# Cada episódio é declarado uma vez com EP(...) nos arquivos ovrb1_zz_c_d*.py; o gancho HOOK (ovrb1.install) reconstrói obra, elenco, vocabulário, objetos quentes,
# falas, perguntas, verbos, laboratório, gaps, armadilhas, regra, molde, missões e expressões a partir da especificação (usa ova2b._derive).
import re
from v3.ovrb1 import HOOK
from v3.ova2b import W, L, Q, _derive

SPEC = {}


def vb(v, ic, pt, subj, third, rest, pron, ex, expt):
    return (v, ic, pt, '%s %s %s.' % (subj, third, rest), '%s %s %s.' % (subj, v, rest), ex, expt, '%s **%s**.' % (pron, third))


def EP(n, rs, names, ids, w, cv, voc, hot, lines, quiz, verbs, lab, gp, ex):
    assert len(voc) == 6 and len(hot) == 5 and len(lines) == 8 and len(quiz) == 3 and len(verbs) == 4 and len(lab[4]) == 3 and len(gp) == 4 and len(ex) == 4, n
    for (hi, key, w1, w2) in gp:
        assert key in hot[hi][0] and key not in (w1, w2), (n, key, hot[hi][0])
    for x in ex:
        assert x[1].lower() in x[4].lower(), (n, x[1], x[4])
    SPEC[n] = dict(rs=rs, names=tuple(names), ids=list(ids), w=w, cv=cv, voc=voc, hot=hot, lines=lines, quiz=quiz, verbs=verbs, lab=lab, gp=gp, ex=ex)
    HOOK[n] = _hook


def work(n):
    return W(*SPEC[n]['w'])


def _hook(base, k):
    import v3.b1h as H
    s = SPEC[k['n']]
    real, cap = H.E, {}
    H.E = lambda **kw: cap.update(kw) or {}
    try:
        base(**k)
    finally:
        H.E = real
    e = cap
    e['names'], e['ids'], e['rs'] = s['names'], s['ids'], s['rs']
    e['obra'] = work(k['n'])
    e['vocab'] = [(a, b, c, 'Soa como “%s”.' % d) for a, b, c, d in s['voc']]
    e['sub'] = re.sub(r'\([^()]*\)\s*$', '(' + ', '.join(v[1] for v in s['voc']) + ')', e['sub'])
    e['hot'] = [(v[0], v[1], v[2], h[0], h[1]) for v, h in zip(s['voc'], s['hot'])]
    if ': ' in e['why']:
        e['why'] = e['why'].split(': ')[0] + ': ' + ' '.join(h[0] for h in s['hot'][:3])
    e['dictate'] = [[h[0], h[1]] for h in s['hot'][:4]]
    e['speak'] = [[h[0], h[1]] for h in s['hot'][:2]]
    e['lines'] = [list(x) for x in s['lines']]
    qs = [Q(*q) for q in s['quiz']]
    e['quiz'] = [tuple(q[:5]) + ('%s diz: “%s”' % (e['lines'][q[4]][0], e['lines'][q[4]][1]),) for q in qs]
    vbs = [vb(*v) for v in s['verbs']]
    e['verbs'] = ('Verbos do episódio', 'Quatro verbos: ' + ', '.join(v[0] for v in vbs[:3]) + ' e ' + vbs[3][0] + '.', vbs)
    e['lab'] = L(s['lab'][0], s['lab'][1], s['lab'][2], s['lab'][3], s['lab'][4], list(s['hot'][0]))
    e['cover'] = (e['cover'][0], s['cv'])
    e['scenes'] = [s['rs']] + [x for x in (e.get('scenes') or []) if x != s['rs']][:5]
    r = dict(e['rule']); r['who'] = s['ids'][0]; e['rule'] = r
    _derive(e, s['gp'], s['ex'])
    return real(**e)


for _m in ('d1', 'd2', 'd3', 'd4'):
    try:
        __import__('v3.ovrb1_zz_c_' + _m)
    except ModuleNotFoundError as _x:
        if _x.name != 'v3.ovrb1_zz_c_' + _m:
            raise
