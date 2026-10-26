# Camada de reescrita dos episódios A2 241–474 (continuações e repetições): cada episódio sobrescrito recebe obra, elenco, 6 palavras, 4 verbos,
# 3 sons do laboratório, objetos quentes e falas PRÓPRIOS (modelo dos episódios 2–5 do A1). Análogo ao tools/v3/ovrb1.py (B1), mas sobre o E de tools/v3/short.py.
# Cada módulo a2_NNN_MMM chama install(globals()); os episódios em OVR (n -> dict) são reescritos, os demais passam intactos.
# Os arquivos de dados são ova2b_241_*.py (importados no fim de install). Obras: ver gen_obras_a2b.py -> obras_new_a2_241_474_*.json.
import re, glob, os, importlib

OVR = {}


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


def X(n, names=None, ids=None, ob=None, vocab=None, hot=None, lines=None, quiz=None, verbs=None, lab=None, rs=None, cv=None, scene2=None, **more):
    """Campos omitidos ficam como no módulo (as falas e as perguntas só trocam os nomes quando names é dado)."""
    OVR[n] = dict(names=names, ids=ids, ob=ob, vocab=vocab, hot=hot, lines=lines, quiz=quiz, verbs=verbs, lab=lab, rs=rs, cv=cv, scene2=scene2, more=more)


def install(g):
    base = g['E']

    def E2(**k):
        o = OVR.get(k.get('n'))
        if o is None:
            return base(**k)
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
            k['quiz'] = [tuple(q[:5]) + (re.sub(r'^(%s) diz' % '|'.join(re.escape(x) for x in mp), lambda m: mp[m.group(1)] + ' diz', q[5]),) for q in k['quiz']]
        if o['verbs']:
            vb = o['verbs']
            k['verbs'] = ('Verbos do episódio', 'Quatro verbos: ' + ', '.join(v[0] for v in vb[:3]) + ' e ' + vb[3][0] + '.', vb)
        if o['lab']: k['lab'] = o['lab']
        if o['cv']: k['cover'] = (k['cover'][0], o['cv'])
        k.update(o['more'])
        return base(**k)

    g['E'] = E2
    here = os.path.dirname(os.path.abspath(__file__))
    for f in sorted(glob.glob(os.path.join(here, 'ova2b_241_*.py'))):
        importlib.import_module('v3.' + os.path.basename(f)[:-3])
