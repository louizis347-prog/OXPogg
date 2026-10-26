# Atalho de autoria do B1: gera os campos repetitivos do episódio (R, lab, mold, produce, mission2, exp_scene…).
import re
from v3.short import *

FILL = [['Good.', 'Bom.'], ['Coffee?', 'Café?'], ['Please.', 'Por favor.'], ['Here.', 'Aqui.']]


def _bold(s, expr):
    m = re.search(re.escape(expr.rstrip('.').lower()), s.lower())
    if not m:
        return s
    return s[:m.start()] + '**' + s[m.start():m.end()] + '**' + s[m.end():]


def S(n, title, sub, pattern, why, names, ids, rs, obra, hot, gaps, traps, rule, fm, cover, vocab, lines, quiz,
      teaser, exps, lab, verbs, mold, prod, m2, scenes, fill=None):
    A, B = names
    who = ids[0]
    en_all = ' '.join(h[3] for h in hot[:4])
    pt_all = ' '.join(h[4] for h in hot[:4])
    formula = [([[f[0], 2]], [[f[1], 3], [f[2], 3]], f[3], f[4]) for f in fm]
    uses = [(h[0], h[1], h[1][0].upper() + h[1][1:] + '.', h[2][0].upper() + h[2][1:] + '.') for h in hot[:4]]
    rules = [(traps[0][1][1], 1, traps[0][3], traps[0][1][0]), (traps[1][1][1], 2, traps[1][3], traps[1][1][0])]
    R_ = R(who, rule[0], rule[1], [en_all, pt_all], formula, uses, rules, [rule[2]])
    ws = lab['words']
    labd = dict(short=lab['short'], title=lab['title'],
                say=', '.join(w[0] for w in ws) + ': sons do episódio. Vamos ouvir?',
                what=' '.join(f'**{w[0]}** soa **“{w[1]}”**.' for w in ws),
                how='Diga ' + ', '.join(f'“{w[1]}”' for w in ws) + '.', pt=lab['pt'],
                ex=[(w[0], w[1], w[2], w[3]) for w in ws],
                pairs=[(w[0], w[4], f'{w[1].lower()} × {w[5].lower()}') for w in ws],
                tip=lab['tip'], phrase=[hot[0][3], hot[0][4]],
                rounds=[(w[0], [w[0], w[4]], 0, f'**{w[0]}** é a palavra do episódio.') for w in ws])
    molds = [(m[0], [('começo', [[m[1], m[2]]]), ('fim', [[' ' + a.strip(), ' ' + b.strip()] for a, b in m[3]])], '') for m in mold]
    dictate = [[h[3], h[4]] for h in hot[:4]]

    def prod_d(p, lead):
        ic, name, desc, prompt, chip, model, items = p
        return dict(ic=ic, name=name, desc=desc, prompt=prompt, ph='Ex.: ' + model, chips=[chip], model=model,
                    check=[i[0] for i in items], kw=[i[1] for i in items], tips=[[[i[2], i[3]]] for i in items],
                    ok=[i[4] for i in items], reply=lead)
    exps_d = [(e[0], e[1], 'Expressão', e[2], '**Fala** de ' + e[3] + '.', e[4], e[5]) for e in exps]
    sc = []
    for k, e in enumerate(exps):
        sc.append([A if k % 2 == 0 else B, _bold(e[4], e[1]), e[5]])
    for k, f in enumerate(fill or FILL):
        sc.append([A if k % 2 == 0 else B] + f)
    return E(n=n, title=title, sub=sub, pattern=pattern, why=why, names=names, ids=ids, rs=rs,
             obra=OB(n, obra[0], obra[1], p='b'), hot=hot, gaps=gaps, traps=traps, rule=R_, cover=cover,
             vocab=vocab, lines=lines, quiz=quiz, dictate=dictate, teaser=teaser, exps=exps_d, exp_scene=sc,
             lab=labd, verbs=('Verbos do episódio', 'Quatro verbos: ' + ', '.join(v[0] for v in verbs[:3]) + ' e ' + verbs[3][0] + '.', verbs),
             mold=molds, speak=dictate[:2], produce=prod_d(prod, ['Good!', 'Bom!']),
             mission2=prod_d(m2, ['Ha!', 'Ha!']), scenes=scenes)
