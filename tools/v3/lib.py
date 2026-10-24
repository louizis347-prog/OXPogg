# Atalhos para escrever os episódios 86–110 do A1 de inglês no modelo piloto (tools/model_v2.py).
HOT_POS = [(14, 16), (40, 14), (66, 14), (88, 16), (50, 84)]
SAYPT = {}
COLORS = ['#B7791F', '#2b6cb0', '#2f855a', '#b83280', '#6b46c1']
SCENES = ['home1', 'park', 'kitchen', 'school', 'street', 'cafe2', 'yard', 'lake', 'living', 'bedroom', 'hall', 'diner', 'shop', 'office']


def hot(rows):
    out = []
    for (e, en, pt, say, sp), (x, y) in zip(rows, HOT_POS):
        out.append(dict(e=e, x=x, y=y, en=en, pt=pt, say=say))
        SAYPT[say] = sp
    return out


def gap(q, pt, opts, a, why):
    return dict(q=q, pt=pt, opts=opts, a=a, why=why)


def trap(q, opts, a, why):
    return dict(q=q, opts=opts, a=a, why=why)


def exp(ic, en, tag, pt, use, ex_en, ex_pt):
    return dict(ic=ic, en=en, tag=tag, pt=pt, use=use, ex=[ex_en, ex_pt])


def verb(v, ic, pt, eu, ele, ex_en, ex_pt, note):
    return dict(v=v, ic=ic, pt=pt, f=[['eu', eu], ['ele/ela', ele]], ex=[ex_en, ex_pt], note=note)


def page(label, slots, end='.'):
    return dict(label=label, slots=[dict(cat=c, opts=[list(o) for o in opts]) for c, opts in slots], end=[end, end])


def mission(ic, name, desc, prompt, chips, model, check, kw, tips, ok, reply):
    return dict(ic=ic, name=name, desc=desc, data=dict(prompt=prompt, ph='Escreva a sua resposta aqui…', chips=chips, model=model, check=check, kw=kw,
                                                         tips=tips, ok=ok, reply=reply))


def hw(say, opts, a, why, ask='Ouça e toque na palavra.'):
    return dict(fig='🎧', say=say, ask=ask, opts=opts, a=a, why=why)


def hp(say, emojis, a, why, ask='Ouça e toque na figura.'):
    return dict(fig='🎧', say=say, ask=ask, opts=[[e, ''] for e in emojis], a=a, why=why, pic=1)


def rnd(say, opts, a, why):
    return dict(fig='🎧', say=say, ask='Qual palavra você ouviu?', opts=opts, a=a, why=why)


def make_rs(scenes):
    keys = ['rdg', 'pat', 'vplay', 'sbuild', 'build', 'order', 'balloons', 'dictate', 'soundlab', 'scene', 'dquiz', 'scenebuild', 'produce', 'review', 'wrap']
    return {k: scenes[i % len(scenes)] for i, k in enumerate(keys)}


def ep(n, title, sub, pattern, why, review, names, cast_ids, stage_rs, stage_chars, obra, gancho, hot_rows, gap_rows, trap_rows, sticker, rule, mission_ic,
       cover_sub, cover_say, vocab, balloons, lines, quiz, rdg_q, dictate, produce, wrap_recap, teaser, scenes,
       exps, exp_scene, lab, hunt, verbs_title, verbs_tip, verbs, mold, speak, mtrap, mgap, expq, missions, sc='park', exp_rs='cafe2'):
    a, b = names
    cast = {a: ['🧑', COLORS[0]], b: ['🧑', COLORS[1]]}
    cast.update({x: ['🧑', COLORS[i + 2]] for i, x in enumerate(sorted({l[0] for l in lines} - {a, b}))})
    base = dict(n=n, title=title, sub=sub, pattern_label=pattern, why=why, vocab=vocab, balloons=balloons, cast=cast, lines=lines, quiz=quiz,
                rdg_q=rdg_q, dictate=dictate, produce=produce, wrap_recap=wrap_recap, teaser=teaser, cover_sub=cover_sub, cover_say=cover_say,
                cover_art={'s': sc, 'items': [], 'seed': 'v3_%d' % n}, rs=make_rs(scenes), sc=sc)
    v2 = dict(base=base, n=n, review=review, names=names, stage=dict(rs=stage_rs, chars=stage_chars), obra=obra, gancho=gancho,
              hot=hot(hot_rows), gap=gap_rows, trap=trap_rows, sticker=sticker, rule=rule, mission_ic=mission_ic,
              speakers=cast_ids if isinstance(cast_ids, dict) else dict(zip(names, cast_ids)))
    extra = dict(exp=exps, exp_scene=dict(rs=exp_rs, lines=exp_scene), lab=lab, hunt=hunt)
    vb = dict(title=verbs_title, tip=verbs_tip, items=verbs)
    more = dict(mold=mold, speak=speak, trap=mtrap, gap=mgap, expq=expq, missions=missions)
    return dict(n=n, v2=v2, extra=extra, verbs=vb, more=more)


def OB(n, line_en, line_pt, p='b', text=None, year=None):
    """Obra do episódio reaproveitada do episódio antigo (tools/v3/obras_old_121_160.json): nome, tipo, ano, texto e arte da capa."""
    import json, os, re
    here = os.path.dirname(os.path.abspath(__file__))
    redo = json.load(open(os.path.join(here, 'obras_redo.json'), encoding='utf-8'))
    if str(n) in redo:  # episódio refeito: obra vem do quadro da cena clicável anterior
        r = dict(redo[str(n)])
        r['year'] = r['kind'].split('· ')[-1]
        r['line'] = [line_en, line_pt]
        r['pa'] = dict(r['pa'], p=p)
        return r
    o = json.load(open(os.path.join(here, 'obras_old_121_160.json'), encoding='utf-8')).get(str(n))
    if o is None:  # episódios 6–115, guardados do quadro cultob antigo
        o = {**json.load(open(os.path.join(here, 'obras_old_006_115.json'), encoding='utf-8')), **json.load(open(os.path.join(here, 'obras_old_181_200.json'), encoding='utf-8')), **json.load(open(os.path.join(here, 'obras_old_201_230.json'), encoding='utf-8')), **json.load(open(os.path.join(here, 'obras_old_231_250.json'), encoding='utf-8')), **json.load(open(os.path.join(here, 'obras_old_251_350.json'), encoding='utf-8')), **json.load(open(os.path.join(here, 'obras_old_351_466.json'), encoding='utf-8'))}[str(n)]
        ch = o['chips'] or []
        o = dict(a=dict(w=o['work'], k=ch[0] if ch else '📖', y=(ch[1] if len(ch) > 1 else '')), panel=o['panel'], pa=o['pa'])
    a = o['a']
    if text is None:
        t = o['panel'].strip()
        if len(t) > 340:
            t = t[:340]
            t = t[:max(t.rfind('. '), t.rfind('.')) + 1]
        text = t
    pa = o['pa'] or {}
    y = year or a['y']
    return dict(name=a['w'], kind='%s · %s' % (a['k'], y), year=y, text=text, line=[line_en, line_pt], pa=dict(t=pa.get('t', 'toyshop'), e=pa.get('e', ['📖', '✨', '🎈']), p=p, v=0))
