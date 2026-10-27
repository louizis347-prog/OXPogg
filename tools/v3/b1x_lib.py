# Autoria compacta dos episódios B1 451–490 (modelo piloto regular-pilot-v1), obras de séries, teatro, quadrinhos, animações e sitcoms.
# Cada episódio é declarado com EP(...) nos módulos b1_451_455 … b1_486_490; EP devolve o episódio montado (mesmo formato de v3.short.E) para EPS.
# Obras: o mesmo dicionário é gravado em obras_new_b1_451_490.json por gen_b1_451_490_works.py (a montagem não depende do arquivo).
import re
from v3 import short
from v3 import ova2b as B

ORDER = [82299, 7082299, 82300, 7082300, 82301, 7082301, 82302, 7082302, 82303, 7082303, 930065, 7930065, 82305, 7082305, 82307, 7082307, 82308, 7082308,
         930066, 7930066, 82311, 7082311, 82312, 7082312, 930067, 7930067, 930068, 7930068, 82318, 7082318, 82319, 7082319, 82321, 7082321, 82322, 7082322,
         930069, 7930069, 82323, 7082323]
TITLES = {82299: 'Theater Night', 7082299: 'Ir ao teatro', 82300: 'Museum Visit', 7082300: 'Visitar um museu', 82301: 'Cooking Disasters',
          7082301: 'Desastres na cozinha', 82302: 'Recipes and Instructions', 7082302: 'Receitas e instruções', 82303: 'Eating Out',
          7082303: 'Pedir num restaurante formal', 930065: 'Dress Up, Dress Down', 7930065: 'Roupas e ocasiões', 82305: 'Hobbies and Free Time',
          7082305: 'Passatempos', 82307: 'Sarcasm and Irony', 7082307: 'Sarcasmo e ironia', 82308: 'Asking Strangers', 7082308: 'Perguntas educadas',
          930066: 'Beat Around the Bush', 7930066: 'Direto ao ponto', 82311: 'Making Small Talk', 7082311: 'Conversa leve', 82312: 'Giving Compliments',
          7082312: 'Elogios', 930067: 'Log In, Sign Up', 7930067: 'Na internet', 930068: 'City Life, Country Life', 7930068: 'Cidade ou campo',
          82318: 'Banking and Money', 7082318: 'Falar com o banco', 82319: 'Insurance and Claims', 7082319: 'Seguros e indenizações',
          82321: 'Pets and Animals', 7082321: 'Bichos de estimação', 82322: 'Gardening Talk', 7082322: 'Conversa de jardinagem',
          930069: 'Heavy Rain, Strong Coffee', 7930069: 'Combinações naturais', 82323: 'Home Repairs', 7082323: 'Consertos em casa'}

SPECS = {}


def work(n, ob):
    name, kind, year, desc, topic, theme, emojis = ob
    return dict(name=name, kind='%s · %s' % (kind, year), text='%s é %s Isso combina com %s. A cena é autoral; não adapta nem cita a obra.' % (name, desc, topic),
                line=['', ''], pa=dict(t=theme, e=list(emojis), v=0))


def EP(n, rs, scenes, names, ids, ob, pat, goal, cv, voc, hot, lines, quiz, vb, lab, gp, ex):
    """n; rs = cenário da capa/palco; scenes = 6 cenários; names/ids = 2 personagens; ob = obra; pat = padrão gramatical (campo gs);
    goal = o que o aluno faz (em pt, depois de 'você'); cv = frase da capa; voc 6; hot 5; lines 8; quiz 3; vb 4; lab; gp 4; ex 4."""
    assert n in TITLES and len(voc) == 6 and len(hot) == 5 and len(lines) == 8 and len(quiz) == 3 and len(vb) == 4 and len(lab[4]) == 3 and len(gp) == 4 and len(ex) == 4, n
    assert len(scenes) == 6 and len(names) == 2 and len(ids) == 2
    for g in gp:
        assert g[1] in hot[g[0]][3], (n, g)
    for e in ex:
        assert e[1].lower() in e[4].lower(), (n, e)
    vw = {v[1] for v in voc}
    for w in lab[4]:
        assert w[0] in vw, (n, 'lab', w[0])
    hs = {l[0] for l in lines}
    for h in hot:
        assert h[3] in hs, (n, 'hot fora das falas', h[3])
    SPECS[n] = dict(n=n, rs=rs, scenes=scenes, names=tuple(names), ids=list(ids), ob=ob, pat=pat, goal=goal, cv=cv, voc=voc, hot=hot, lines=lines, quiz=quiz, vb=vb, lab=lab, gp=gp, ex=ex)
    return build(n)


def build(n):
    s = SPECS[n]
    a, b = s['names']
    lines = [[a if i % 2 == 0 else b, en, pt] for i, (en, pt) in enumerate(s['lines'])]
    vocab = [(e, w, pt, 'Soa como “%s”.' % pr) for (e, w, pt, pr) in s['voc']]
    hot = [tuple(h) for h in s['hot']]
    quiz = [(q[0], q[1], [q[3], q[4], q[5]], 0, q[2], '%s diz: “%s”' % (lines[q[2]][0], lines[q[2]][1])) for q in s['quiz']]
    verbs = [(v, ic, pt, eu, ele, ex, ept, '**%s** = %s.' % (v, pt)) for (v, ic, pt, eu, ele, ex, ept) in s['vb']]
    lb = s['lab']
    lab = B.L(lb[0], lb[1], lb[2], lb[3], lb[4], [hot[0][3], hot[0][4]])
    i = ORDER.index(n)
    nt = TITLES[ORDER[i + 1]] if i + 1 < len(ORDER) else 'Mais inglês'
    obw = work(n, s['ob'])
    obra = dict(obw, year=obw['kind'].split('· ')[-1], line=[lines[0][1], lines[0][2]], pa=dict(obw['pa'], p='b'))
    kk = dict(n=n, title=TITLES[n], sub=s['goal'] + ': ' + ', '.join(h[1] for h in hot[:4]), pattern=s['pat'],
              why='Hoje você aprende a %s: %s' % (s['goal'], ' '.join(h[3] for h in hot[:3])),
              names=s['names'], ids=s['ids'], rs=s['rs'], obra=obra, hot=hot,
              cover=('%s: em 10 minutos você aprende a %s com %s' % (TITLES[n], s['goal'], s['ob'][0]), s['cv']),
              vocab=vocab, lines=lines, quiz=quiz, dictate=[[h[3], h[4]] for h in hot[:4]],
              teaser=(nt, ('Próximo padrão: ' + s['pat'])[:110]), lab=lab,
              verbs=('Verbos do episódio', 'Quatro verbos: ' + ', '.join(v[0] for v in verbs[:3]) + ' e ' + verbs[3][0] + '.', verbs),
              speak=[[h[3], h[4]] for h in hot[:2]], scenes=s['scenes'])
    B._derive(kk, s['gp'], s['ex'])
    return short.E(**kk)
