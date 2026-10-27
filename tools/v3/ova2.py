# Camada de reescrita dos episódios A2 1–240 (continuações e falas de enchimento), análoga à ovrb1.py do B1.
# Cada módulo a2_001_005 … a2_239_243 chama install(globals(), 'E'); os episódios listados em OVR (n -> dict) recebem obra, elenco,
# vocabulário, objetos quentes, verbos, laboratório de sons, cena e perguntas PRÓPRIOS (modelo dos episódios 2–5 do A1).
# Quem só tem 'fill' troca apenas as falas de enchimento da segunda cena. As obras (WORKS) são gravadas em obras_new_a2_001_240_*.json
# por tools/v3/gen_ova2_works.py. Arquivos de dados: ova2_001_*.py (NÃO a2_*: o model_v3 carrega a2_* como módulos de episódio).
import re, glob, os, importlib

OVR = {}
WORKS = {}


def Wk(n, name, kind, text, theme, emojis):
    """Obra própria do episódio n (JSON de obras): kind = '📖 Romance · 1865'; text em português, termina com a nota de cena autoral."""
    WORKS[str(n)] = dict(name=name, kind=kind, text=text + ' A cena é autoral; não adapta nem cita a obra.', line=['', ''], pa=dict(t=theme, e=list(emojis), v=0))


def V(e, w, pt, pron):
    return (e, w, pt, 'Soa como “%s”.' % pron)


def Lw(w, pron, pt, tip, pair, pair_pron):
    return (w, pron, pt, tip, pair, pair_pron)


def L(short, title, pt, tip, words):
    return dict(short=short, title=title, pt=pt, tip=tip, words=words)


def VB(v, ic, pt, eu, ele, ex_en, ex_pt, note=None):
    return (v, ic, pt, eu, ele, ex_en, ex_pt, note or '**%s** = %s.' % (v, pt))


def D(a, b, pairs):
    """Falas alternadas a, b, a, b… ; pairs = [(en, pt), ...]."""
    return [[a if i % 2 == 0 else b, en, pt] for i, (en, pt) in enumerate(pairs)]


def Q(lines, q, qpt, li, ok, w1, w2):
    """Pergunta de compreensão: ok/w1/w2 = (emoji, texto); a resposta certa vem na posição 0; li = índice da fala."""
    return (q, qpt, [ok, w1, w2], 0, li, '%s diz: “%s”' % (lines[li][0], lines[li][1]))


def X(n, names, ids, cv, vocab, says, verbs, lab, lines, quiz, fill, rs=None):
    """Monta o override do episódio n. says = 5 pares (en, pt) dos objetos quentes (os 5 primeiros vocábulos); quiz = [(q, qpt, li, ok, w1, w2)]*3."""
    OVR[n] = dict(names=names, ids=ids, cv=cv, vocab=vocab, hot=[(v[0], v[1], v[2], s[0], s[1]) for v, s in zip(vocab, says)], verbs=verbs, lab=lab,
                  lines=lines, quiz=[Q(lines, *q) for q in quiz], fill=fill, rs=rs)


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


def install(g, style='E'):
    if 'E' not in g:  # módulos do A1 escritos com ep() (lib): sem camada, reescrever o episódio no próprio módulo
        return
    base = g['E']

    def E2(**k):
        o = OVR.get(k.get('n'))
        if o is None:
            return base(**k)
        a, b = k['names']
        if o.get('swap') and not o.get('vocab'):  # troca pontual de verbos que se repetem com o vizinho
            t, tip, items = k['verbs']
            items = [o['swap'].get(v[0], v) for v in items]
            k['verbs'] = (t, tip, items)
            return base(**k)
        if o.get('fill') and not o.get('vocab'):  # só enchimento
            k['exp_scene'] = list(k['exp_scene'][:4]) + [[a if i % 2 == 0 else b] + list(f) for i, f in enumerate(o['fill'])]
            return base(**k)
        k['vocab'] = o['vocab']
        k['sub'] = re.sub(r'\([^()]*\)\s*$', '(' + ', '.join(v[1] for v in o['vocab']) + ')', k['sub'])
        k['hot'] = [tuple(h) for h in o['hot']]
        k['cover'] = (k['cover'][0], o['cv'])
        mp = dict(zip(k['names'], o['names']))
        k['exp_scene'] = [[mp.get(s[0], s[0])] + list(s[1:]) for s in k['exp_scene']]
        k['names'], k['ids'] = o['names'], o['ids']
        r = dict(k['rule']); r['who'] = o['ids'][0]; k['rule'] = r
        if o.get('rs'): k['rs'] = o['rs']
        from v3.lib import OB
        k['obra'] = OB(k['n'], o['lines'][0][1], o['lines'][0][2], p='b')
        k['lines'], k['quiz'] = o['lines'], o['quiz']
        k['lab'] = _labd(o['lab'], k['hot'][0])
        vb = o['verbs']
        k['verbs'] = ('Verbos do episódio', 'Quatro verbos: ' + ', '.join(v[0] for v in vb[:3]) + ' e ' + vb[3][0] + '.', vb)
        x, y = o['names']
        k['exp_scene'] = list(k['exp_scene'][:4]) + [[x if i % 2 == 0 else y] + list(f) for i, f in enumerate(o['fill'])]
        if o.get('post'): o['post'](k)  # gancho opcional: reescreve por completo os quadros derivados (gaps, regra, molde, missões, expressões)
        return base(**k)

    g['E'] = E2
    here = os.path.dirname(os.path.abspath(__file__))
    for f in sorted(glob.glob(os.path.join(here, 'ova2_*.py')) + glob.glob(os.path.join(here, 'ova1_*.py'))):
        importlib.import_module('v3.' + os.path.basename(f)[:-3])


def SW(n, **sw):
    """Troca pontual: SW(n, velho=VB(...)) substitui o verbo 'velho' do episódio n."""
    OVR[n] = dict(swap=sw)
