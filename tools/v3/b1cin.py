# Construtor compacto dos episódios B1 411–450 (cinema): C(...) deriva missões, perguntas e rótulos dos campos escritos à mão e chama S.
import re
from v3.b1h import *

_ALL = ['street', 'hall', 'lobby1', 'cafe2', 'living', 'park', 'office', 'home1', 'kitchen', 'yard', 'school', 'lake']


def _rx(chunk):
    return r'\b' + r'\s+'.join(re.escape(w) for w in chunk.lower().split()) + r'\b'


def _cap(s):
    return s[0].upper() + s[1:]


def _items(rows):
    """rows = [(emoji, chunk, en, pt)] -> itens da missão (label, regex, en, pt, ok)."""
    out = []
    for ico, chunk, en, pt, verb in rows:
        assert chunk.lower() in en.lower(), (chunk, en)
        out.append((verb + ' ' + chunk + '?', _rx(chunk), en, pt, _cap(chunk.split()[0]) + '! ' + ico))
    return out


def C(n, title, topic, pat, who, rs, obra, goal, cover_say, nxt, rule, mold, hot, vocab, lab, verbs, scene, quiz, exps, fill, gaps, traps):
    n1, n2, i1, i2 = who
    names = (n1, n2)
    for h in hot:
        assert h[1].lower() in h[3].lower(), (n, h[1], h[3])
    assert len(hot) == 5 and len(vocab) == 6 and len(verbs) == 4 and len(exps) == 4 and len(fill) == 4 and len(scene) == 8, n
    assert len(gaps) == 4 and len(traps) == 2 and len(quiz) == 3 and len(mold) == 3 and len(lab[2]) == 3, n
    for e in exps:
        assert e[1].lower() in e[4].lower(), (n, e[1], e[4])
    sub = topic + ': ' + ', '.join(h[1] for h in hot[:3])
    why = 'Hoje você aprende ' + topic + ': ' + ' '.join(h[3] for h in hot[:3])
    cover = (f'{title}: em 10 minutos você {goal}, no clima de {obra}', cover_say)
    teaser = ('Próximo episódio', 'Próximo: ' + nxt)
    fm = []
    for k in (0, 1):
        m = mold[k]
        fm.append((m[0], m[1], m[3][0][0].strip(), m[1] + m[3][0][0], rule[3 + k]))
    prod = (hot[0][0], 'Cena', 'Use ' + ', '.join(h[1] for h in hot[:2]) + ' e ' + hot[2][1],
            'Fale. **Diga: ' + ' '.join(h[4] for h in hot[:3]) + '**', hot[2][1], ' '.join(h[3] for h in hot[:3]),
            _items([(h[0], h[1], h[3], h[4], 'Usei') for h in hot[:3]]))
    m2 = (exps[0][0], 'Fixas', 'Use ' + ', '.join(e[1].lower() for e in exps[:2]) + ' e ' + exps[2][1].lower(),
          'Fale. **Diga: ' + ' '.join(e[5] for e in exps[:3]) + '**', exps[2][1].lower(), ' '.join(e[4] for e in exps[:3]),
          _items([(e[0], e[1].lower(), e[4], e[5], 'Disse') for e in exps[:3]]))
    gp = []
    for g in gaps:
        s, pt, w1, w2 = g
        m = re.search(r'\[(.+?)\]', s)
        ans = m.group(1)
        gp.append((s.replace(m.group(0), '___'), pt, [ans, w1, w2], 0, s.replace(m.group(0), '**' + ans + '**')))
    tp = [('Qual frase está certa?', [traps[0][0], traps[0][1], traps[0][2]], 0, traps[0][3]),
          ('Qual está certa?', [traps[1][0], traps[1][1], traps[1][2]], 0, traps[1][3])]
    lines = [[names[s], en, pt] for s, en, pt in scene]
    qz = [(q[0], q[1], [(q[2], q[3]), (q[4], q[5]), (q[6], q[7])], 0, q[8], q[9]) for q in quiz]
    words = lab[2]
    L = dict(short=words[0][0][:2].lower(), title='Laboratório de sons: ' + words[0][0] + ', ' + words[1][0] + ' e ' + words[2][0],
             pt=lab[0], tip=lab[1], words=words)
    scenes = [rs] + [x for x in _ALL if x != rs][:5]
    return S(n=n, title=title, sub=sub, pattern=pat, why=why, names=names, ids=[i1, i2], rs=rs, obra=(obra, obra),
             hot=hot, gaps=gp, traps=tp, rule=rule[:3], fm=fm, cover=cover, vocab=vocab, lines=lines, quiz=qz,
             teaser=teaser, exps=exps, lab=L, verbs=verbs, mold=mold, prod=prod, m2=m2, scenes=scenes, fill=fill)
