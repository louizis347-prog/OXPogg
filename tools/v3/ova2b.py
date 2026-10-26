# Camada de reescrita dos episódios A2 241–474 (continuações e repetições): cada episódio sobrescrito recebe obra, elenco, 6 palavras, 4 verbos,
# 3 sons do laboratório, objetos quentes e falas PRÓPRIOS (modelo dos episódios 2–5 do A1). Análogo ao tools/v3/ovrb1.py (B1), mas sobre o E de tools/v3/short.py.
# Cada módulo a2_NNN_MMM chama install(globals()); os episódios em OVR (n -> dict) são reescritos, os demais passam intactos.
# Os arquivos de dados são ova2b_241_*.py (importados no fim de install). Obras: ver gen_obras_a2b.py -> obras_new_a2_241_474_*.json.
import re, glob, os, importlib

OVR = {}
OLD = {}  # n -> argumentos originais do episódio (para conferir se algum quadro ainda cita a obra antiga)
GX = {}   # n -> (gp, ex): especificação de gaps/traps/regra/molde/missões/expressões


def W(name, kind, year, desc, topic, t, e, line_en, line_pt):
    """Obra real: kind = '🎬 Filme' etc.; desc = o que a obra é (sem números não verificados); topic = o que a referência ajuda a falar."""
    return dict(name=name, kind='%s · %s' % (kind, year), year=str(year),
                text='%s é %s A referência ajuda a falar de %s. A cena é autoral; não adapta nem cita a obra.' % (name, desc, topic),
                line=[line_en, line_pt + ' (frase autoral da aula)'], pa=dict(t=t, e=list(e), p='b', v=0))


def L(short, title, pt, tip, words, phrase):
    """Laboratório de sons: words = [(palavra, pronúncia, tradução, dica, par parecido, pronúncia do par)] (3 palavras)."""
    ws = words
    return dict(short=short, title=title, say=', '.join(w[0] for w in ws) + ': sons do episódio. Vamos ouvir?',
                what=' '.join('**%s** soa **“%s”**.' % (w[0], w[1]) for w in ws), how='Diga ' + ', '.join('“%s”' % w[1] for w in ws) + '.', pt=pt,
                ex=[(w[0], w[1], w[2], w[3]) for w in ws], pairs=[(w[0], w[4], '%s × %s' % (w[1].lower(), w[5].lower())) for w in ws], tip=tip, phrase=list(phrase),
                rounds=[(w[0], [w[0], w[4]], 0, '**%s** é a palavra do episódio.' % w[0]) for w in ws])


def Q(q, pt, idx, *opts):
    """Pergunta de compreensão: opts = (emoji, texto) com a primeira = certa; idx = índice da fala que responde."""
    return [q, pt, list(opts), 0, idx]


def RP(n, verbs=None, vocab=None):
    """Troca verbos/palavras repetidas com o episódio vizinho: verbs = {velho: tupla}, vocab = {velha: tupla}."""
    o = OVR.setdefault(n, dict(names=None, ids=None, ob=None, vocab=None, hot=None, lines=None, quiz=None, verbs=None, lab=None, rs=None, cv=None, scene2=None, more={}))
    o['rv'] = verbs or {}; o['rw'] = vocab or {}


def VL(n, verbs=None, lab=None, vocab=None):
    """Troca só os verbos e/ou o laboratório de um episódio já declarado com X."""
    o = OVR.setdefault(n, dict(names=None, ids=None, ob=None, vocab=None, hot=None, lines=None, quiz=None, verbs=None, lab=None, rs=None, cv=None, scene2=None, more={}))
    if verbs: o['verbs'] = verbs
    if lab: o['lab'] = lab
    if vocab: o['vocab'] = vocab


def X(n, names=None, ids=None, ob=None, vocab=None, hot=None, lines=None, quiz=None, verbs=None, lab=None, rs=None, cv=None, scene2=None, **more):
    """Campos omitidos ficam como no módulo (as falas e as perguntas só trocam os nomes quando names é dado)."""
    OVR[n] = dict(names=names, ids=ids, ob=ob, vocab=vocab, hot=hot, lines=lines, quiz=quiz, verbs=verbs, lab=lab, rs=rs, cv=cv, scene2=scene2, more=more)


def G(n, gp, ex):
    """gp = 4 x (índice do objeto quente, palavra-chave, errada1, errada2): gaps, traps, regra, molde e missão 1 saem das falas dos objetos quentes.
    ex = 4 x (emoji, expressão, tradução, uso, exemplo en, exemplo pt): expressões, cena das expressões e missão 2 (a expressão deve aparecer no exemplo)."""
    GX[n] = (gp, ex)


def _rx(text):
    out = []
    for w in re.findall(r"[\w’']+", text.lower()):
        out.append("[’']".join(re.escape(x) for x in re.split(r"[’']", w)))
    return r'\b' + r'[^\w]+'.join(out) + r'\b'


def _derive(k, gp, ex):
    from v3.lib import mission
    from v3.short import R
    hot = k['hot']; a, b = k['names']
    def sp(i):
        h = hot[gp[i][0]]; return h[3], h[4]
    gaps = []; fit = []
    for i, (hi, key, w1, w2) in enumerate(gp):
        en, pt = sp(i)
        assert key in en, (k['n'], key, en)
        gaps.append((en.replace(key, '___', 1), pt, [key, w1, w2], 0, 'Aqui o padrão pede **%s**.' % key))
    traps = []
    for i in (2, 3):
        hi, key, w1, w2 = gp[i]; en, _ = sp(i)
        traps.append(('Qual frase está certa?', [en, en.replace(key, w1, 1), en.replace(key, w2, 1)], 0, 'Aqui o padrão pede **%s**.' % key))
    e0, p0 = sp(0)
    toks = lambda s_: [[t, 3] for t in s_.split()]
    formula = []
    for i in (0, 1):
        en, pt = sp(i)
        formula.append(([['Exemplo %d' % (i + 1), 2]], toks(en), en, '**%s** é a peça do padrão.' % gp[i][1]))
    uses = [(hot[gp[i][0]][0], gp[i][1], sp(i)[0], sp(i)[1]) for i in range(4)]
    rules = []
    for i in (2, 3):
        en, _ = sp(i); rules.append((en.replace(gp[i][1], gp[i][2], 1), 1, 'Use **%s**.' % gp[i][1], en))
    rule = R(k['ids'][0], re.split(r'[:(]', k['pattern'].split(' · ')[0])[0].strip(), 'Veja o padrão na cena da obra.', [e0, p0], formula, uses, rules,
             ['Em português “%s”. Em inglês: **%s**' % (p0.rstrip('.!?'), e0)])
    k['gaps'] = gaps; k['traps'] = traps; k['rule'] = rule
    pages = []
    for j in range(3):
        opts = [[sp(i)[0].rstrip('.!?'), sp(i)[1].rstrip('.!?')] for i in [(j + t) % 4 for t in range(3)]]
        pages.append((hot[gp[j][0]][1], [('frase', opts)], '.'))
    k['mold'] = pages
    says = [sp(i)[0] for i in range(3)]
    k['produce'] = dict(ic=hot[gp[0][0]][0], name='Fale da cena', desc='Use o padrão do episódio',
                        prompt='Fale como na obra. **Diga: %s**' % ' '.join(sp(i)[1] if sp(i)[1].endswith(('.', '!', '?')) else sp(i)[1] + '.' for i in range(3)),
                        ph='Ex.: ' + ' '.join(says), chips=[gp[0][1]], model=' '.join(says), check=['Usei “%s”?' % gp[i][1] for i in range(3)],
                        kw=[_rx(s_) for s_ in says], tips=[[[sp(i)[0], sp(i)[1]]] for i in range(3)],
                        ok=['%s!' % hot[gp[i][0]][0] for i in range(3)], reply=['Nice!', 'Legal!'])
    exps = [(e, x, 'Expressão', pt, '**Fala** de %s.' % use, en, ept) for (e, x, pt, use, en, ept) in ex]
    for (e, x, pt, use, en, ept) in ex:
        assert x.lower() in en.lower(), (k['n'], x, en)
    k['exps'] = exps
    sc = []
    for i, (e, x, pt, use, en, ept) in enumerate(ex):
        bold = re.sub('(' + re.escape(x) + ')', r'**\1**', en, count=1, flags=re.I)
        ex_line = [bold, ept]; hot_line = [sp(i)[0], sp(i)[1]]
        pair = (ex_line, hot_line) if i % 2 == 0 else (hot_line, ex_line)
        sc += [[a] + pair[0], [b] + pair[1]]
    k['exp_scene'] = sc
    k['mission2'] = dict(ic=ex[0][0], name='Reagir à cena', desc='Use ' + ', '.join(x[1] for x in ex[:3]),
                         prompt='Reaja. **Diga: %s**' % ' '.join(x[5] if x[5].endswith(('.', '!', '?')) else x[5] + '.' for x in ex[:3]),
                         chips=[ex[0][1]], model=' '.join(x[4] for x in ex[:3]), check=['Disse “%s”?' % x[1] for x in ex[:3]],
                         kw=[_rx(x[1]) for x in ex[:3]], tips=[[[x[4], x[5]]] for x in ex[:3]], ok=['%s!' % x[0] for x in ex[:3]], reply=['Great!', 'Ótimo!'])


def install(g):
    base = g['E']

    def E2(**k):
        o = OVR.get(k.get('n'))
        if o is None:
            return base(**k)
        OLD[k['n']] = dict(names=k['names'], obra=k['obra']['name'], vocab=[v[1] for v in k['vocab']], hot=[h[1] for h in k['hot']], lines=k['lines'],
                           verbs=[v[0] for v in k['verbs'][2]])
        old = k['names']; mp = {}
        if o['names']:
            new = tuple(o['names']); mp = dict(zip(old, new))
            k['names'], k['ids'] = new, list(o['ids'])
            r = dict(k['rule']); r['who'] = o['ids'][0]; k['rule'] = r
        if o['rs']: k['rs'] = o['rs']
        k['exp_scene'] = o['scene2'] or [[mp.get(s[0], s[0])] + list(s[1:]) for s in k['exp_scene']]
        if o['ob']: k['obra'] = o['ob']
        if o['vocab']:
            k['vocab'] = o['vocab']
            k['sub'] = re.sub(r'\([^()]*\)\s*$', '(' + ', '.join(v[1] for v in o['vocab']) + ')', k['sub'])
        if o['hot']:
            k['hot'] = o['hot']
            if ': ' in k['why']:
                k['why'] = k['why'].split(': ')[0] + ': ' + ' '.join(h[3] for h in o['hot'][:3])
            k['dictate'] = [[h[3], h[4]] for h in o['hot'][:4]]
            k['speak'] = [[h[3], h[4]] for h in o['hot'][:2]]
        if o['lines']:
            k['lines'] = o['lines']
            k['quiz'] = [tuple(q[:5]) + ('%s diz: “%s”' % (o['lines'][q[4]][0], o['lines'][q[4]][1]),) for q in o['quiz']]
        elif mp:
            k['lines'] = [[mp.get(x[0], x[0])] + list(x[1:]) for x in k['lines']]
            def _q(t):
                for a_, b_ in mp.items():
                    t = re.sub(r'\b[Tt]he ' + re.escape(a_.lower()) + r'\b', b_, t)
                    t = re.sub(r'\b' + re.escape(a_.lower()) + r'\b', b_, t)
                    t = re.sub(r'\b' + re.escape(a_) + r'\b', b_, t)
                return t
            k['quiz'] = [(_q(q[0]),) + tuple(q[1:5]) + (re.sub(r'^(%s) diz' % '|'.join(re.escape(x) for x in mp), lambda m: mp[m.group(1)] + ' diz', q[5]),) for q in k['quiz']]
        if o['verbs']:
            vb = o['verbs']
            k['verbs'] = ('Verbos do episódio', 'Quatro verbos: ' + ', '.join(v[0] for v in vb[:3]) + ' e ' + vb[3][0] + '.', vb)
        if o['lab']: k['lab'] = o['lab']
        if o.get('rv'):
            vb = [o['rv'].get(v[0], v) for v in k['verbs'][2]]
            k['verbs'] = ('Verbos do episódio', 'Quatro verbos: ' + ', '.join(v[0] for v in vb[:3]) + ' e ' + vb[3][0] + '.', vb)
        if o.get('rw'):
            k['vocab'] = [o['rw'].get(v[1], v) for v in k['vocab']]
            k['sub'] = re.sub(r'\([^()]*\)\s*$', '(' + ', '.join(v[1] for v in k['vocab']) + ')', k['sub'])
        if o['cv']: k['cover'] = (k['cover'][0], o['cv'])
        k.update(o['more'])
        if k['n'] in GX: _derive(k, *GX[k['n']])
        return base(**k)

    g['E'] = E2
    here = os.path.dirname(os.path.abspath(__file__))
    for f in sorted(glob.glob(os.path.join(here, 'ova2b_241_*.py'))):
        importlib.import_module('v3.' + os.path.basename(f)[:-3])
