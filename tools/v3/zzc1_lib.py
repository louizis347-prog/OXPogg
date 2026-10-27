# Lote C do A1 (séries, teatro, quadrinhos, videogames, óperas/balés, mitos e músicas): troca de obra de episódios cujo módulo ep_*.py usa E (camada ova2).
# Cada episódio é um bloco de texto compacto em zzc1_d*.py (ver parse) e é instalado por ova1_zz_c.py via put(n), reaproveitando zz_a_lib.EP/put_ova2.
# Campos (um por linha; separados por '|'):
#   N n                      C Nome1,Nome2 | id1,id2 | resumo da capa (pt)
#   F obra | tipo | ano/criador | descrição (pt, minúscula, termina em ponto) | tema que ajuda a falar (pt) | cenário (art) | e1,e2,e3 | fala da obra en | pt
#   V emoji|palavra|pt|pronúncia (6)      L en|pt (8 falas alternadas)      H i,i,i,i,i (índices das falas que viram os 5 objetos)
#   Q pergunta|pt|índice da fala|emoji certo|emoji errado|emoji errado (3; cada opção 'emoji texto')
#   B verbo|emoji|pt|objeto|exemplo en|exemplo pt (4; eu/ele derivados)
#   LAB curto|pt|dica      W palavra|pron|pt|dica|par|pron do par (3)
#   G índice do objeto|palavra-chave|errada1|errada2 (4)      X emoji|expressão|pt|uso|exemplo en|exemplo pt (4; o exemplo precisa conter a expressão e vira a segunda cena)
import re
from v3 import zz_a_lib as Z

SPECS = {}


def _sp(s):
    return [x.strip() for x in s.split('|')]


def _v3(v):
    w = v.split(' ')
    h = w[0]
    if h == 'have': h2 = 'has'
    elif h == 'go': h2 = 'goes'
    elif h == 'do': h2 = 'does'
    elif re.search(r'(s|sh|ch|x|z|o)$', h): h2 = h + 'es'
    elif re.search(r'[^aeiou]y$', h): h2 = h[:-1] + 'ies'
    else: h2 = h + 's'
    return ' '.join([h2] + w[1:])


def parse(txt):
    d = {'V': [], 'L': [], 'Q': [], 'B': [], 'W': [], 'G': [], 'X': []}
    for ln in txt.strip().split('\n'):
        ln = ln.strip()
        if not ln or ln.startswith('#'): continue
        k, rest = ln.split(' ', 1)
        if k in ('N', 'H', 'LAB', 'C', 'F'): d[k] = rest.strip()
        else: d[k].append(rest.strip())
    n = int(d['N'])
    nm, ids, cv = _sp(d['C'])
    names = tuple(x.strip() for x in nm.split(','))
    ids = [x.strip() for x in ids.split(',')]
    f = _sp(d['F'])
    voc = [tuple(_sp(x)) for x in d['V']]
    lines = [tuple(_sp(x)) for x in d['L']]
    assert len(f) in (7, 9), (n, len(f))
    if len(f) == 7: f += [lines[0][0], lines[0][1]]
    ob = (f[0], f[1], f[2], f[3], f[4], f[5], [e.strip() for e in f[6].split(',')], f[7], f[8])
    hi = [int(i) for i in d['H'].split(',')]
    hot = [lines[i] for i in hi]
    for v, h in zip(voc, hot):
        w = v[1].lower()
        if w[:max(3, len(w) - 2)] not in h[0].lower(): print('AVISO hot sem a palavra', n, v[1], '|', h[0])
    quiz = []
    for q in d['Q']:
        a = _sp(q)
        o = [tuple(x.split(' ', 1)) for x in a[3:6]]
        quiz.append((a[0], a[1], int(a[2]), o[0], o[1], o[2]))
    vb = []
    for b in d['B']:
        v, ic, pt, obj, ex, ept = _sp(b)
        vb.append((v, ic, pt, 'I %s %s.' % (v, obj), 'She %s %s.' % (_v3(v), obj), ex, ept))
    sh, lpt, tip = _sp(d['LAB'])
    ws = [tuple(_sp(w)) for w in d['W']]
    lab = (sh, 'Laboratório de sons: %s e %s' % (', '.join(w[0] for w in ws[:2]), ws[2][0]), lpt, tip, ws)
    gp = []
    for g in d['G']:
        i, key, w1, w2 = _sp(g)
        gp.append((int(i), key, w1, w2))
    ex = []
    for x in d['X']:
        a = _sp(x)
        if len(a) == 4:
            hit = [l for l in lines if a[1].lower() in l[0].lower()]
            assert hit, (n, 'expressão fora das falas', a[1])
            a += [hit[0][0], hit[0][1]]
        if a[1].lower() not in a[4].lower() and a[1].rstrip('.!?,').lower() in a[4].lower(): a[1] = a[1].rstrip('.!?,')
        ex.append(tuple(a))
    assert len(voc) == 6 and len(lines) == 8 and len(hot) == 5 and len(quiz) == 3 and len(vb) == 4 and len(ws) == 3 and len(gp) == 4 and len(ex) == 4, n
    for (i, key, w1, w2) in gp:
        assert key in hot[i][0], (n, key, hot[i][0])
    for (e, x, pt, use, en, ept) in ex:
        assert x.lower() in en.lower(), (n, x, en)
    Z.EP(n, None, names, ids, ob, cv, voc, [(h[0], h[1]) for h in hot], [(l[0], l[1]) for l in lines], quiz, vb, lab, gp, ex)
    SPECS[n] = d
    return n


def put(n):
    Z.put_ova2(n)
