# Camada de reescrita dos episódios B1 86–172 (continuações e falas de enchimento).
# Cada módulo b1_086_090 … b1_167_172 chama install(globals(), 'E' ou 'S'); os episódios listados em OVR (n -> dict) recebem
# obra, elenco, vocabulário, verbos, laboratório de sons, cena e perguntas PRÓPRIOS (modelo dos episódios 2–5 do A1); os demais só trocam as falas de enchimento (fill).
import re, glob, os, importlib

OVR = {}
HOOK = {}  # n -> f(base, k): substituição completa do episódio (camadas ovrb1_zz_*.py)


def L(short, title, pt, tip, words):
    """Laboratório de sons: words = [(palavra, pronúncia, tradução, dica, par parecido, pronúncia do par)] (3 palavras)."""
    return dict(short=short, title=title, pt=pt, tip=tip, words=words)


def _labd(lab, hot0):
    ws = lab['words']
    return dict(short=lab['short'], title=lab['title'],
                say=', '.join(w[0] for w in ws) + ': sons do episódio. Vamos ouvir?',
                what=' '.join('**%s** soa **“%s”**.' % (w[0], w[1]) for w in ws),
                how='Diga ' + ', '.join('“%s”' % w[1] for w in ws) + '.', pt=lab['pt'],
                ex=[(w[0], w[1], w[2], w[3]) for w in ws],
                pairs=[(w[0], w[4], '%s × %s' % (w[1].lower(), w[5].lower())) for w in ws],
                tip=lab['tip'], phrase=[hot0[3], hot0[4]],
                rounds=[(w[0], [w[0], w[4]], 0, '**%s** é a palavra do episódio.' % w[0]) for w in ws])


def _fixq(quiz, mp):
    return [tuple(q[:5]) + (re.sub(r'^(%s) diz' % '|'.join(re.escape(x) for x in mp), lambda m: mp[m.group(1)] + ' diz', q[5]),) for q in quiz]


def _pre(k, o):
    """Aplica o override o ao dict de argumentos k (comum a E e S)."""
    if o.get('vocab'):
        k['vocab'] = o['vocab']
        k['sub'] = re.sub(r'\([^()]*\)\s*$', '(' + ', '.join(v[1] for v in o['vocab']) + ')', k['sub'])
    if o.get('hot4'):
        k['hot'] = list(k['hot'][:4]) + [tuple(o['hot4'])]
    if o.get('cv'):
        k['cover'] = (k['cover'][0], o['cv'])


def _fix():
    try:  # episódios já corrigidos pelo outro fluxo (b1fix) não são sobrescritos aqui
        from v3.b1fix import FIX
        return FIX
    except Exception:
        return {}


def install(g, style):
    base = g['E'] if style == 'E' else g['S']

    def S2(**k):
        if k.get('n') in HOOK:
            return HOOK[k['n']](base, k)
        o = {} if k.get('n') in _fix() else OVR.get(k.get('n'), {})
        if o:
            _pre(k, o)
            if o.get('names'):
                mp = dict(zip(k['names'], o['names']))
                k['lines'] = [[mp.get(x[0], x[0])] + list(x[1:]) for x in k['lines']]
                k['quiz'] = _fixq(k['quiz'], mp)
                k['names'], k['ids'] = o['names'], o['ids']
            if o.get('rs'): k['rs'] = o['rs']
            if o.get('obra'): k['obra'] = (o['obra'][0], o['obra'][1])
            for f in ('lines', 'quiz', 'lab', 'verbs', 'scenes'):
                if o.get(f): k[f] = o[f]
            k['fill'] = o['fill']
        return base(**k)

    def E2(**k):
        if k.get('n') in HOOK:
            return HOOK[k['n']](base, k)
        o = None if k.get('n') in _fix() else OVR.get(k.get('n'))
        if o is None:
            return base(**k)
        _pre(k, o)
        old = k['names']
        if o.get('names'):
            new = o['names']; k['names'], k['ids'] = new, o['ids']
            mp = dict(zip(old, new))
            k['exp_scene'] = [[mp.get(s[0], s[0])] + list(s[1:]) for s in k['exp_scene']]
            k['lines'] = [[mp.get(x[0], x[0])] + list(x[1:]) for x in k['lines']]
            k['quiz'] = _fixq(k['quiz'], mp)
            r = dict(k['rule']); r['who'] = o['ids'][0]; k['rule'] = r
        if o.get('rs'): k['rs'] = o['rs']
        if o.get('obra'):
            from v3.lib import OB
            k['obra'] = OB(k['n'], o['obra'][0], o['obra'][1], p='b')
        if o.get('lines'): k['lines'] = o['lines']
        if o.get('quiz'): k['quiz'] = o['quiz']
        if o.get('lab'): k['lab'] = _labd(o['lab'], k['hot'][0])
        if o.get('verbs'):
            vb = o['verbs']
            k['verbs'] = ('Verbos do episódio', 'Quatro verbos: ' + ', '.join(v[0] for v in vb[:3]) + ' e ' + vb[3][0] + '.', vb)
        if o.get('scenes'): k['scenes'] = o['scenes']
        a, b = k['names']
        es = list(k['exp_scene'][:4]) + [[a if i % 2 == 0 else b] + list(f) for i, f in enumerate(o['fill'])]
        k['exp_scene'] = es
        return base(**k)

    g['E' if style == 'E' else 'S'] = E2 if style == 'E' else S2
    for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ovrb1_*.py'))):
        importlib.import_module('v3.' + os.path.basename(f)[:-3])
