# Correções de conteúdo dos itens 1–85 do B1 (modelo 2–5 do A1): cada episódio, inclusive continuação, tem obra, elenco,
# 6 palavras, 4 verbos, 3 sons e falas próprios. Os módulos b1_001_005 … b1_081_085 importam E daqui; o dicionário FIX
# (tools/v3/b1fix_data_*.py) sobrescreve só os campos informados, por número de episódio.
import glob, importlib, os, re
import v3.short as _short
from v3.lib import OB

FIX = {}
_here = os.path.dirname(os.path.abspath(__file__))
for _f in sorted(glob.glob(os.path.join(_here, 'b1fix_data_*.py'))):
    FIX.update(importlib.import_module('v3.' + os.path.basename(_f)[:-3]).FIX)


# obras próprias das continuações: gera tools/v3/obras_new_b1_001_085.json (lido por OB) a partir de FIX
def _write_obras():
    import json
    d = {}
    for n, fx in sorted(FIX.items()):
        if 'obra' in fx:
            nm, kind, text, cen, cpt, t, emo = fx['obra']
            d[str(n)] = dict(name=nm, kind=kind, text=text, line=[cen, cpt], pa=dict(t=t, e=emo, v=0))
    out = os.path.join(_here, 'obras_new_b1_001_085.json')
    new = json.dumps(d, ensure_ascii=False, indent=1)
    if not os.path.exists(out) or open(out, encoding='utf-8').read() != new:
        open(out, 'w', encoding='utf-8').write(new)


_write_obras()


def _lab(L):
    short, title, pt, tip, ws, phrase = L
    return dict(short=short, title=title, say=', '.join(w[0] for w in ws) + ': sons do episódio. Vamos ouvir?',
                what=' '.join('**%s** soa **“%s”**.' % (w[0], w[1]) for w in ws), how='Diga ' + ', '.join('“%s”' % w[1] for w in ws) + '.', pt=pt,
                ex=[(w[0], w[1], w[2], w[3]) for w in ws], pairs=[(w[0], w[4], '%s × %s' % (w[1].lower(), w[5].lower())) for w in ws],
                tip=tip, phrase=phrase, rounds=[(w[0], [w[0], w[4]], 0, '**%s** é a palavra do episódio.' % w[0]) for w in ws])


def _rep(x, pairs, used):
    if isinstance(x, str):
        for i, (a, b) in enumerate(pairs):
            if a in x:
                x = x.replace(a, b); used.add(i)
        return x
    if isinstance(x, (list, tuple)):
        y = [_rep(v, pairs, used) for v in x]
        return y if isinstance(x, list) else tuple(y)
    if isinstance(x, dict):
        return {k: _rep(v, pairs, used) for k, v in x.items()}
    return x


def E(**kw):
    n = kw['n']
    fx = FIX.get(n)
    if fx:
        kw = dict(kw)
        if 'rep' in fx:  # trocas de frase quando a nova obra pede outro cenário (aplicadas antes de tudo)
            used = set()
            for k in ('title', 'sub', 'pattern', 'why', 'hot', 'gaps', 'traps', 'rule', 'vocab', 'lines', 'quiz', 'dictate', 'exps', 'exp_scene', 'lab', 'verbs', 'mold', 'speak', 'produce', 'mission2', 'teaser'):
                if k in kw:
                    kw[k] = _rep(kw[k], fx['rep'], used)
            miss = [fx['rep'][i][0] for i in range(len(fx['rep'])) if i not in used]
            if miss:
                print('AVISO %s: troca não encontrada: %s' % (n, miss))
        a0, b0 = kw['names']
        if 'obra' in fx:
            o = fx['obra']
            kw['obra'] = OB(n, o[3], o[4], p='b')
        if 'cover' in fx:
            kw['cover'] = (kw['cover'][0], fx['cover'])
        if 'cast' in fx:
            a1, b1, ia, ib = fx['cast']
            mp = {a0: a1, b0: b1}
            kw['names'] = (a1, b1); kw['ids'] = [ia, ib]
            r = dict(kw['rule']); r['who'] = ia; kw['rule'] = r
            fix_l = lambda L: [[mp.get(l[0], l[0])] + list(l[1:]) for l in L]
            kw['lines'] = fix_l(kw['lines']); kw['exp_scene'] = fix_l(kw['exp_scene'])
            kw['quiz'] = [tuple(q[:5]) + (re.sub(r'^(%s|%s) diz' % (re.escape(a0), re.escape(b0)), lambda m: mp[m.group(1)] + ' diz', q[5]),) for q in kw['quiz']]
        if 'vocab' in fx:
            assert len(fx['vocab']) == 6; kw['vocab'] = fx['vocab']
        if 'verbs' in fx:
            assert len(fx['verbs']) == 4
            kw['verbs'] = ('Verbos da cena', 'Quatro verbos: ' + ', '.join(v[0] for v in fx['verbs'][:3]) + ' e ' + fx['verbs'][3][0] + '.', fx['verbs'])
        if 'lab' in fx:
            L = fx['lab']; kw['lab'] = _lab((L[0], L[1], L[2], L[3], L[4], kw['lab']['phrase']))
        if 'hot' in fx:
            kw['hot'] = fx['hot']
        if 'fill' in fx:
            es = [list(l) for l in kw['exp_scene']]
            assert len(fx['fill']) == 4 and not any('**' in l[1] for l in es[-4:]), n
            for i, f in enumerate(fx['fill']):
                es[-4 + i] = [es[-4 + i][0], f[0], f[1]]
            kw['exp_scene'] = es
    return _short.E(**kw)

