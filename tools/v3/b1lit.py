# Atalho compacto para os episódios B1 371–410 (categoria literatura): monta os argumentos de S (v3.b1h) a partir de uma ficha curta.
# Cada ficha traz obra, elenco, 6 palavras, 4 verbos, laboratório de 3 sons, 5 objetos, 8 falas, segunda cena (4 expressões + 4 falas) e missões PRÓPRIOS.
import re
from v3.b1h import *

ORDER = [(82243, 'Safe Travel'), (7082243, 'Segurança em viagem'), (82245, 'Travel Review'), (7082245, 'Avaliar uma viagem'),
         (930053, 'To Begin With'), (7930053, 'Em ordem'), (82246, 'Describing Symptoms'), (7082246, 'Descrever sintomas'),
         (82247, "At the Doctor's"), (7082247, 'Falar com o médico'), (82248, 'Mental Health'), (7082248, 'Estresse e descanso'),
         (82250, 'Healthy Diet'), (7082250, 'Alimentação saudável'), (930054, 'Saying No Gently'), (7930054, 'Dizer não com gentileza'),
         (82252, 'Accidents and First Aid'), (7082252, 'Primeiros socorros'), (82253, 'Allergies and Reactions'), (7082253, 'Falar de alergias'),
         (930055, 'Check Up On, Check Out'), (7930055, 'Verificar'), (82258, 'Medical Vocabulary'), (7082258, 'Termos médicos'),
         (82259, 'News Headlines'), (7082259, 'Manchetes'), (930056, "Don't Cry Over Spilled Milk"), (7930056, 'Seguir em frente'),
         (82260, 'Fake News'), (7082260, 'Notícias falsas'), (930057, 'Break a Record'), (7930057, 'Quebrar recorde'),
         (82266, 'Podcasts and Audio'), (7082266, 'Falar de podcasts'), (82267, 'Gaming Culture'), (7082267, 'Falar de videogames'),
         (82269, 'Tech Support'), (7082269, 'Suporte técnico'), (930058, 'Weather Extremes'), (7930058, 'Clima intenso')]
TITLE = dict(ORDER)
NEXT = {a[0]: b[1] for a, b in zip(ORDER, ORDER[1:])}


def _p(s):
    return 'Soa como “%s”.' % s


def _rx(key):
    return r'\b' + r'\s+'.join(re.escape(w) for w in key.split()) + r'\b'


def _strip(s):
    return re.sub(r'[.!?]+$', '', s.strip())


def _mis(ic, name, verb, items, chip):
    """items = [(trecho, frase em inglês, tradução)] ; o trecho precisa aparecer na frase."""
    keys = [i[0] for i in items]
    ptl = [_strip(i[2])[0].lower() + _strip(i[2])[1:] for i in items]
    lst = ', '.join(keys[:-1]) + ' e ' + keys[-1]
    pl = ', '.join(ptl[:-1]) + ' e ' + ptl[-1]
    model = ' '.join(i[1] for i in items)
    its = [('%s %s?' % (verb, i[0]), _rx(i[0]), i[1], i[2], '%s! %s' % (i[0].split()[0].capitalize(), ic)) for i in items]
    return (ic, name, 'Use ' + lst, 'Fale. **Diga ' + pl + '.**', chip, model, its)


def X(n, sub, gs, why, names, ids, rs, scenes, cover, rule, fm, vocab, lab, verbs, mold, prod, m2, hot, gaps, traps, lines, quiz, exps, fill, obra):
    title = TITLE[n]
    teaser = ('Mais episódios', 'Próximo: ' + NEXT.get(n, 'novo tema'))
    voc = [(v[0], v[1], v[2], _p(v[3])) for v in vocab]
    L = dict(short=lab[0], title='Laboratório de sons: ' + ', '.join(w[0] for w in lab[3][:2]) + ' e ' + lab[3][2][0], pt=lab[1], tip=lab[2], words=lab[3])
    vb = []
    for v in verbs:
        hint = re.sub('(' + re.escape(v[0]) + ')', r'**\1**', v[3], count=1, flags=re.I)
        vb.append((v[0], v[1], v[2], v[3], v[4], v[5], v[6], hint))
    fmm = [(f[0], f[1], f[2], f[1] + ' ' + f[2], f[3]) for f in fm]
    gp = [(g[0], g[1], [g[2], g[3], g[4]], 0, g[5] if len(g) > 5 else '**%s**.' % g[2]) for g in gaps]
    tr = [(t[0], [t[1], t[2], t[3]], 0, t[4]) for t in traps]
    qz = [(q[0], q[1], q[2], 0, q[3], q[4]) for q in quiz]
    return S(n=n, title=title, sub=sub, pattern=gs, why=why, names=names, ids=ids, rs=rs, obra=obra, hot=hot, gaps=gp, traps=tr, rule=rule,
             fm=fmm, cover=cover, vocab=voc, lines=lines, quiz=qz, teaser=teaser, exps=exps, lab=L, verbs=verbs_t(vb), mold=mold,
             prod=_mis(prod[0], prod[1], 'Usei', prod[2], prod[3]), m2=_mis(m2[0], m2[1], 'Disse', m2[2], m2[3]), scenes=scenes, fill=fill)


def verbs_t(vb):
    return vb
