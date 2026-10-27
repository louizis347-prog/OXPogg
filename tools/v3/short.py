# Forma compacta de escrever um episódio no modelo piloto: o que não precisa de texto próprio é derivado dos campos escritos à mão.
from v3.lib import *


def E(n, title, sub, pattern, why, names, ids, rs, obra, hot, gaps, traps, rule, cover, vocab, lines, quiz, dictate, teaser, exps, exp_scene, lab, verbs,
      mold, speak, produce, mission2, scenes=None, review=True, sc=None, sticker_sub=None):
    a, b = names
    sc = sc or rs
    chars = [[ids[0], 34, 0, 1.0], [ids[1], 68, 1, 1.0]]
    hot_rows = [tuple(h) for h in hot]
    gap_rows = [gap(*g) for g in gaps]
    trap_rows = [trap(*t) for t in traps]
    voc = [[w, pt, pr] for (_e, w, pt, pr) in vocab]
    balloons = [[e, w] for (e, w, _pt, _pr) in vocab]
    L = lab
    rounds = [rnd(*r) for r in L['rounds']]
    pic = [h[0] for h in hot_rows]
    hunt = [hw(*L['rounds'][0]), hp(hot_rows[0][1], [pic[0], pic[1], pic[2]], 0, '**%s** = %s.' % (hot_rows[0][1], hot_rows[0][2])),
            hw(*L['rounds'][1]), hp(hot_rows[3][1], [pic[2], pic[3], pic[4]], 1, '**%s** = %s.' % (hot_rows[3][1], hot_rows[3][2])), hw(*L['rounds'][2])]
    wrap = [[h[3], h[4]] for h in hot_rows[:4]]
    r0 = traps[0]
    tr_ok = r0[1][r0[2]]
    exps_l = [exp(*x) for x in exps]
    fmt = lambda s: s.replace('**', '')
    expq = []
    for i, x in enumerate(exps):
        o = [x[1]] + [y[1] for j, y in enumerate(exps) if j != i][:2]
        expq.append({'ask': x[4].replace('**', '').rstrip('.') + '.', 'opts': o, 'a': 0, 'why': '**%s** = %s' % (x[1], x[3])})
    mtrap = [{'ask': traps[0][0], 'opts': traps[0][1], 'a': traps[0][2], 'why': traps[0][3], 'say': traps[0][1][traps[0][2]]},
             {'ask': traps[1][0], 'opts': traps[1][1], 'a': traps[1][2], 'why': traps[1][3], 'say': traps[1][1][traps[1][2]]}]
    mgap = []
    for g in gaps[:2]:
        full = g[0].replace('___', g[2][g[3]])
        mgap.append({'text': g[0], 'pt': g[1], 'opts': g[2], 'a': g[3], 'why': g[4], 'say': full})
    P = produce
    m1 = mission(P['ic'], P['name'], P['desc'], P['prompt'], P['chips'][:1], P['model'], P['check'], P['kw'], P['tips'], P['ok'], P['reply'])
    M2 = mission2
    m2 = mission(M2['ic'], M2['name'], M2['desc'], M2['prompt'], M2['chips'][:1], M2['model'], M2['check'], M2['kw'], M2['tips'], M2['ok'], M2['reply'])
    scenes = scenes or [rs, 'park', 'street', 'cafe2', 'yard', 'lake']
    gq = lines[0]
    return ep(
        n=n, title=title, sub=sub, pattern=pattern, why=why, review=review, names=names, cast_ids=ids,
        stage_rs=rs, stage_chars=chars, obra=obra, gancho=[gq[0], gq[1], gq[2]],
        hot_rows=hot_rows, gap_rows=gap_rows, trap_rows=trap_rows,
        sticker=dict(title=sticker_sub or ('%s e %s' % (a, b)), sub='%s · %s' % (obra['name'], obra['year']), rs=rs, chars=chars),
        rule=rule, mission_ic=P['ic'], cover_sub=cover[0], cover_say=cover[1], vocab=voc, balloons=balloons, lines=lines,
        quiz=[{'q': q[0], 'pt': q[1], 'opts': [list(o) for o in q[2]], 'a': q[3], 'line': q[4], 'why': q[5]} for q in quiz],
        rdg_q={'q': r0[0], 'o': r0[1], 'a': r0[2], 'why': r0[3]},
        dictate=dictate, produce=dict(prompt=P['prompt'], ph=P['ph'], chips=P['chips'], model=P['model'], check=P['check'], kw=P['kw'], tips=P['tips'], ok=P['ok'], reply=P['reply']),
        wrap_recap=wrap, teaser={'t': teaser[0], 'd': teaser[1]}, scenes=scenes,
        exps=exps_l, exp_scene=exp_scene,
        lab=dict(short=L['short'], title=L['title'], say=L['say'], intro=dict(what=L['what'], how=L['how'], pt=L['pt']), ex=L['ex'], pairs=L['pairs'], tip=L['tip'],
                 phrase=L['phrase'], rounds=rounds),
        hunt=hunt, verbs_title=verbs[0], verbs_tip=verbs[1], verbs=[verb(*v) for v in verbs[2]],
        mold=[page(*m) for m in mold], speak=speak, mtrap=mtrap, mgap=mgap, expq=expq, missions=[m1, m2], sc=sc)


def R(who, head, sub, say, formula, uses, rules, tips):
    """Quadro da regra: formula = [(from_, to_, say, note)] com from_/to_ já em pares [texto, cor]."""
    return dict(who=who, head=head, sub=sub, say=say, formula=[dict(from_=f[0], to=f[1], say=f[2], note=f[3]) for f in formula],
                uses=[dict(ico=u[0], tag=u[1], en=u[2], pt=u[3]) for u in uses],
                rules=[dict(tag=r[0], c=r[1], text=r[2], ex=r[3]) for r in rules], tips=tips)
