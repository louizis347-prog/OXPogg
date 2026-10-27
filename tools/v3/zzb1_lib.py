# Camada B (cinema: filmes, animações, musicais, documentários) para episódios B1 que repetiam obra.
# Cada episódio é declarado uma vez com EP(...); install() registra um HOOK em ovrb1 (substituição completa: gaps, regra, molde, missões,
# expressões, cena, laboratório, verbos, elenco e obra saem da especificação). Título, padrão (gs), teaser e cenas vêm do módulo b1_*.py.
import re, json, os

SPECS = {}
HERE = os.path.dirname(os.path.abspath(__file__))


def EP(n, rs, names, ids, ob, cv, voc, hot, lines, quiz, vb, lab, gp, ex):
    """ob = (nome, tipo, ano, descrição, tema-pt, arte, emojis, fala-en, fala-pt); voc = 6 x (emoji, palavra, pt, pronúncia);
    hot = 5 x (emoji, chave, chave-pt, frase-en, frase-pt); lines = 8 x (en, pt) alternando os dois personagens;
    quiz = 3 x (q, qpt, índice da fala, certa, errada1, errada2) com opções (emoji, texto); vb = 4 x (verbo, emoji, pt, eu, ele, ex-en, ex-pt);
    lab = (short, título, pt, dica, 3 x (palavra, pron, pt, dica, par, pron-par)); gp = 4 x (índice do hot, palavra-chave, errada1, errada2);
    ex = 4 x (emoji, expressão, pt, uso, exemplo-en, exemplo-pt)."""
    assert len(voc) == 6 and len(hot) == 5 and len(lines) == 8 and len(quiz) == 3 and len(vb) == 4 and len(lab[4]) == 3 and len(gp) == 4 and len(ex) == 4, n
    for i, (hi, key, w1, w2) in enumerate(gp):
        assert key in hot[hi][3], (n, key, hot[hi][3])
    for e in ex:
        assert e[1].lower().rstrip('.!?') in e[4].lower(), (n, e[1])
    SPECS[n] = dict(n=n, rs=rs, names=tuple(names), ids=list(ids), ob=ob, cv=cv, voc=voc, hot=hot, lines=lines, quiz=quiz, vb=vb, lab=lab, gp=gp, ex=ex)


def _rx(text):
    out = []
    for w in re.findall(r"[\w’']+", text.lower()):
        out.append("[’']".join(re.escape(x) for x in re.split(r"[’']", w)))
    return r'\b' + r'[^\w]+'.join(out) + r'\b'


def works():
    d = {}
    for n, s in SPECS.items():
        name, kind, year, desc, topic, theme, emojis, len_, lpt = s['ob']
        d[str(n)] = dict(name=name, kind='%s · %s' % (kind, year),
                         text='%s é %s A referência ajuda a falar de %s. A cena é autoral; não adapta nem cita a obra.' % (name, desc, topic),
                         line=[len_, lpt + ' (frase autoral da aula)'], pa=dict(t=theme, e=list(emojis), v=0))
    return d


def _build(s):
    def build(base, k):
        from v3.short import E, R
        from v3.lib import OB
        n = s['n']; a, b = s['names']; ids = s['ids']
        hot = [tuple(h) for h in s['hot']]
        gp = s['gp']
        vocab = [(e, w, pt, 'Soa como “%s”.' % pr) for (e, w, pt, pr) in s['voc']]
        sub = re.sub(r'\([^()]*\)\s*$', '(' + ', '.join(v[1] for v in vocab) + ')', k['sub'])
        why = k['why'].split(': ')[0] + ': ' + ' '.join(h[3] for h in hot[:3]) if ': ' in k['why'] else k['why']
        sp = lambda i: (hot[gp[i][0]][3], hot[gp[i][0]][4])
        gaps = []
        for i, (hi, key, w1, w2) in enumerate(gp):
            en, pt = sp(i)
            gaps.append((en.replace(key, '___', 1), pt, [key, w1, w2], 0, 'Aqui o padrão pede **%s**.' % key))
        traps = []
        for i in (2, 3):
            hi, key, w1, w2 = gp[i]; en, _ = sp(i)
            traps.append(('Qual frase está certa?', [en, en.replace(key, w1, 1), en.replace(key, w2, 1)], 0, 'Aqui o padrão pede **%s**.' % key))
        e0, p0 = sp(0)
        formula = []
        for i in (0, 1):
            en, pt = sp(i)
            formula.append(([['Exemplo %d' % (i + 1), 2]], [[t, 3] for t in en.split()], en, '**%s** é a peça do padrão.' % gp[i][1]))
        uses = [(h[0], h[1], h[3], h[4]) for h in hot[:4]]
        rules = []
        for i in (2, 3):
            en, _ = sp(i); rules.append((en.replace(gp[i][1], gp[i][2], 1), 1, 'Use **%s**.' % gp[i][1], en))
        rt = k['rule']
        rule = R(ids[0], rt[0], rt[1], [' '.join(h[3] for h in hot[:4]), ' '.join(h[4] for h in hot[:4])], formula, uses, rules,
                 ['Em português “%s”. Em inglês: **%s**' % (p0.rstrip('.!?'), e0)])
        pages = []
        for j in range(3):
            opts = [[sp(i)[0].rstrip('.!?'), sp(i)[1].rstrip('.!?')] for i in [(j + t) % 4 for t in range(3)]]
            pages.append((hot[gp[j][0]][1], [('frase', opts)], '.'))
        says = [sp(i)[0] for i in range(3)]
        end = lambda t: t if t.endswith(('.', '!', '?')) else t + '.'
        produce = dict(ic=hot[gp[0][0]][0], name='Fale da cena', desc='Use o padrão do episódio',
                       prompt='Fale da cena. **Diga: %s**' % ' '.join(end(sp(i)[1]) for i in range(3)),
                       ph='Ex.: ' + ' '.join(says), chips=[gp[0][1]], model=' '.join(says), check=['Usei “%s”?' % gp[i][1] for i in range(3)],
                       kw=[_rx(x) for x in says], tips=[[[sp(i)[0], sp(i)[1]]] for i in range(3)],
                       ok=['%s!' % hot[gp[i][0]][0] for i in range(3)], reply=['Nice!', 'Legal!'])
        ex = s['ex']
        exps = [(e, x, 'Expressão', pt, '**Fala** de %s.' % use, en, ept) for (e, x, pt, use, en, ept) in ex]
        sc = []
        for i, (e, x, pt, use, en, ept) in enumerate(ex):
            bold = re.sub('(' + re.escape(x.rstrip('.!?')) + ')', r'**\1**', en, count=1, flags=re.I)
            ex_line = [bold, ept]; hot_line = [sp(i)[0], sp(i)[1]]
            pair = (ex_line, hot_line) if i % 2 == 0 else (hot_line, ex_line)
            sc += [[a] + pair[0], [b] + pair[1]]
        mission2 = dict(ic=ex[0][0], name='Reagir à cena', desc='Use ' + ', '.join(x[1].rstrip('.!?') for x in ex[:3]),
                        prompt='Reaja. **Diga: %s**' % ' '.join(end(x[5]) for x in ex[:3]),
                        chips=[ex[0][1]], model=' '.join(x[4] for x in ex[:3]), check=['Disse “%s”?' % x[1].rstrip('.!?') for x in ex[:3]],
                        kw=[_rx(x[1].rstrip('.!?')) for x in ex[:3]], tips=[[[x[4], x[5]]] for x in ex[:3]], ok=['%s!' % x[0] for x in ex[:3]], reply=['Great!', 'Ótimo!'])
        lines = [[a if i % 2 == 0 else b, en, pt] for i, (en, pt) in enumerate(s['lines'])]
        quiz = []
        for qi, (q, qpt, li, ok, w1, w2) in enumerate(s['quiz']):
            opts = [w1, w2]; opts.insert(qi % 3, ok)
            quiz.append((q, qpt, opts, qi % 3, li, '%s diz: “%s”' % (lines[li][0], lines[li][1])))
        sl, st, spt, stip, ws = s['lab']
        lab = dict(short=sl, title=st, say=', '.join(w[0] for w in ws) + ': sons do episódio. Vamos ouvir?',
                   what=' '.join('**%s** soa **“%s”**.' % (w[0], w[1]) for w in ws), how='Diga ' + ', '.join('“%s”' % w[1] for w in ws) + '.', pt=spt,
                   ex=[(w[0], w[1], w[2], w[3]) for w in ws], pairs=[(w[0], w[4], '%s × %s' % (w[1].lower(), w[5].lower())) for w in ws], tip=stip,
                   phrase=[hot[0][3], hot[0][4]], rounds=[(w[0], [w[0], w[4]], 0, '**%s** é a palavra do episódio.' % w[0]) for w in ws])
        vb = [(v, ic, pt, eu, ele, ex_, ept, '**%s** = %s.' % (v, pt)) for (v, ic, pt, eu, ele, ex_, ept) in s['vb']]
        dictate = [[h[3], h[4]] for h in hot[:4]]
        return E(n=n, title=k['title'], sub=sub, pattern=k['pattern'], why=why, names=s['names'], ids=ids, rs=s['rs'],
                 obra=OB(n, lines[0][1], lines[0][2], p='b'), hot=hot, gaps=gaps, traps=traps, rule=rule, cover=(k['cover'][0], s['cv']),
                 vocab=vocab, lines=lines, quiz=quiz, dictate=dictate, teaser=k['teaser'], exps=exps, exp_scene=sc, lab=lab,
                 verbs=('Verbos do episódio', 'Quatro verbos: ' + ', '.join(v[0] for v in vb[:3]) + ' e ' + vb[3][0] + '.', vb),
                 mold=pages, speak=dictate[:2], produce=produce, mission2=mission2, scenes=k.get('scenes'))
    return build


def install():
    from v3 import ovrb1
    for n, s in SPECS.items():
        ovrb1.HOOK[n] = _build(s)
        ovrb1.OVR.pop(n, None)


def write_works(path=None):
    path = path or os.path.join(HERE, 'obras_new_b1_zz_b.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(works(), f, ensure_ascii=False, indent=1)
