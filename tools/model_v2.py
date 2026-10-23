#!/usr/bin/env python3
"""Modelo de quadros completos ("padrão do dia em uma obra") para os 5 primeiros episódios do A1 de inglês.

Ordem: capa · revisão do episódio anterior (ep. 2 em diante) · cena clicável com a obra · diálogo · você entendeu ·
padrão ilustrado · palavras com figura · complete as falas · qual está certa · fale · missão · fechamento.
Cada quadro mostra todas as suas perguntas de uma vez (nada de uma pergunta por tela).
Uso: python3 tools/model_v2.py
"""
import json, os, sys, copy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from model_v2_data import V2  # noqa: E402
from model_v2_extra import EXTRA, VERBS  # noqa: E402


def main_chars(st):
    ids = [c[0] for c in st['chars']][:2]
    pos = [(32, 0), (68, 1)] if len(ids) > 1 else [(50, 0)]
    return [[i, x, fl, 1.0] for i, (x, fl) in zip(ids, pos)]


def strip_tags(s):
    import re
    return re.sub(r'<[^>]+>', '', s)


def third(it):
    import re
    m = re.search(r'(\w+)\*\*(\w+)\*\*', it['f'][1][1])
    return (m.group(1) + m.group(2)) if m else it['v']


def ing(v):
    return (v[:-1] if v.endswith('e') and not v.endswith('ee') else v) + 'ing'


def verb_quiz(vb):
    """Perguntas de revisão dos verbos: a forma certa com he/she."""
    out = []
    for it in vb['items']:
        sent = it['f'][1][1].replace('**', '')
        form = third(it)
        opts = [it['v'], form, ing(it['v'])]
        out.append(dict(text=sent.replace(form, '___', 1), pt='Verbo **%s** (%s) com he/she.' % (it['v'], it['pt']), opts=opts,
                        a=1, say=sent, why='Com he/she o verbo ganha o final: **%s**.' % form))
    return out


def bag_of(prev):
    """Mochila do episódio anterior: palavras, verbos, expressões, padrão e sons."""
    Xp, XTp, VBp = prev
    Bp = Xp['base']
    pt = {w.lower(): p for w, p, _ in Bp['vocab']}
    for h in Xp['hot']:
        pt.setdefault(h['en'].lower(), h['pt'])
    words = [dict(ic=e, t=w, pt=pt.get(w.lower(), '')) for e, w in Bp['balloons']]
    verbs = [dict(ic=v['ic'], t=v['v'], pt=v['pt'], s=v['f'][0][1].rstrip('.')) for v in VBp['items']]
    exps = [dict(ic=x['ic'], t=x['en'], pt=x['pt']) for x in XTp['exp']]
    R = Xp['rule']
    pat = [dict(ic='📌', t=R['head'], pt=R['sub'])] + [dict(ic=u['ico'], t=u['en'], pt=u['pt']) for u in R.get('uses', [])[:3]]
    snd = [dict(ic='🔬', t=XTp['lab']['short'], pt='', s=', '.join(e[0] for e in XTp['lab']['ex']))]
    return [dict(ic='📌', l='Padrão', items=pat), dict(ic='🔤', l='Palavras', items=words), dict(ic='🏃', l='Verbos', items=verbs),
            dict(ic='💬', l='Expressões', items=exps), dict(ic='🎧', l='Sons', items=snd)]


def build(old, X, XT, VB, prev):
    B = X['base']
    a, b = X['names']
    st = X['stage']
    rs = B['rs']
    mc = main_chars(st)
    ob = X['obra']

    def fr(k, **kw):
        d = dict(k=k)
        d.update(kw)
        bb = d.get('bubble')
        if bb:  # quem fala vira avatar do quadro
            sid = mc[0][0] if bb[0] == a else mc[1][0]
            d['chars'] = [[sid, 50, 0, 1.0]]
            d['avatar'] = 1
        return d

    frames = []
    frames.append(fr('cover', art=B['cover_art'], sub=B['cover_sub'], badge='A1', snd=old['fr'][0].get('snd', 'bell'),
                     say=B['cover_say'], gancho=X['gancho'], obra='%s · %s' % (ob['name'], ob['year']),
                     stage=dict(rs=st['rs'], chars=st['chars'])))
    if X['review'] and prev:  # revisão do episódio anterior fica no INÍCIO deste episódio
        Bp = prev[0]['base']
        frames.append(fr('review', prev=Bp['title'], work=prev[0]['obra']['name'],
                         recap=[list(x) for x in Bp['wrap_recap']], bag=bag_of(prev),
                         lead='Abra cada bolso da mochila e relembre o episódio anterior!',
                         next='Hoje: **%s**' % B['pattern_label'], say='Bora relembrar o episódio anterior antes de seguir!',
                         rs=rs['review'], chars=mc))
    frames.append(fr('hotscene', title='Explore a cena', hint='Toque nos objetos brilhantes para ouvir o nome em inglês.',
                     rs=st['rs'], chars=st['chars'], hot=X['hot'], say='Toque nos objetos brilhantes!',
                     obra=dict(name=ob['name'], kind=ob['kind'], text=ob['text'], line=ob['line'], pa=ob['pa'])))
    frames.append(fr('pgscene', cast=B['cast'], lines=B['lines'], speakers=X['speakers'], rs=st['rs'], chars=st['chars'],
                     say='Ouça a cena e leia junto.'))
    # você entendeu?
    quiz = [dict(ask=it['q'], speak=it['q'], pt=it['pt'], opts=it['opts'], a=it['a'], why=it['why']) for it in B['quiz']]
    frames.append(fr('pgsheet', title='Você entendeu?', items=quiz, rs=rs['dquiz'], chars=mc, review=False,
                     bubble=[b, 'What do you remember?', 'De que você se lembra?']))
    # padrão com ilustração
    R = dict(X['rule'])
    R['formula'] = [{'from': r['from_'], 'to': r['to'], 'say': r.get('say'), 'note': r.get('note')} for r in R.get('formula', [])]
    frames.append(fr('pgrule', rule=R, q=B['rdg_q'], rs=rs['rdg'], say='Veja o padrão com figuras e ouça os exemplos.'))
    # palavras com figura (todas de uma vez)
    pt = {}
    for w, p, note in B['vocab']:
        pt[w.lower()] = (p, note)
    for h in X['hot']:
        pt.setdefault(h['en'].lower(), (h['pt'], ''))
    words = [(e, w) for e, w in B['balloons']]
    items = []
    for i, (emo, w) in enumerate(words):
        others = [x[1] for x in words if x[1] != w]
        opts = [w, others[(i + 1) % len(others)], others[(i + 3) % len(others)]]
        opts = [opts[(k + i) % 3] for k in range(3)]
        p, note = pt.get(w.lower(), ('', ''))
        items.append(dict(fig=emo, say=w, ask='Qual é a palavra?', opts=opts, a=opts.index(w), ptWord=p,
                          why='**%s** = %s.%s' % (w, p, (' ' + note) if note else '')))
    frames.append(fr('pgsheet', title='Palavras da cena', layout='grid', items=items, rs=rs['vplay'], chars=mc,
                     bubble=[a, 'Listen and choose the word!', 'Ouça e escolha a palavra da figura!']))
    # verbos (4) + missão dos verbos
    frames.append(fr('verbs', title=VB['title'], items=VB['items'], tip=VB['tip'], say='Vamos ver os verbos de hoje!', rs=rs['build'], chars=mc,
                     quiz=verb_quiz(VB), bubble=[b, "These are today's verbs!", 'Estes são os verbos de hoje!']))
    frames.append(fr('vplay', title='Missão dos verbos', items=VB['items'], plan=[[0, 0], [1, 0], [2, 0], [3, 0], [0, 3], [1, 3], [2, 3]],
                     say='Missão dos verbos: 7 passos. Eu ajudo você!', rs=rs['build'], chars=mc,
                     bubble=[a, 'Verb mission! I will help you.', 'Missão dos verbos! Eu ajudo você.']))
    # expressões comuns e gírias + cena com as expressões
    frames.append(fr('pgexp', title='Expressões e gírias', items=XT['exp'], rs=rs['vplay'], chars=mc,
                     say='Toque para ouvir cada expressão.', bubble=[a, 'This is how people really talk!', 'É assim que as pessoas falam de verdade!']))
    es = XT['exp_scene']
    frames.append(fr('pgscene', title='Na conversa de verdade', cast=B['cast'], lines=es['lines'], speakers=X['speakers'], rs=es['rs'],
                     chars=st['chars'], say='Veja as expressões em uso. Elas estão destacadas.'))
    gap = [dict(text=r['q'], pt=r['pt'], opts=r['opts'], a=r['a'], why=r['why'],
                say=r['q'].replace('___', r['opts'][r['a']])) for r in X['gap']]
    frames.append(fr('pgsheet', title='Complete as falas', items=gap, rs=rs['build'], chars=mc,
                     bubble=[b, 'Complete the sentences!', 'Complete as frases!']))
    trap = [dict(ask=r['q'], opts=r['opts'], a=r['a'], why=r['why'], say=strip_tags(r['opts'][r['a']])) for r in X['trap']]
    frames.append(fr('pgsheet', title='Qual está certa?', items=trap, rs=rs['order'], chars=mc,
                     bubble=[b, 'Careful! Only one is right.', 'Cuidado! Só uma está certa.']))
    # laboratório de sons + caça-sons (só se o episódio ainda não tiver o laboratório)
    if not any(f['k'] in ('soundlab', 'pglab') for f in frames):
        lab = dict(XT['lab'])
        frames.append(fr('pglab', rs=rs['soundlab'], chars=mc, bubble=[a, "Let's train our ears!", 'Vamos treinar o ouvido!'], **lab))
        frames.append(fr('pgsheet', title='Caça-sons', items=XT['hunt'], rs=rs['soundlab'], chars=mc,
                         bubble=[b, 'Listen and hunt the sound!', 'Ouça e cace o som certo!']))
    frames.append(fr('pgspeak', title='Sua vez de falar', items=[list(x) for x in B['dictate'][:3]], who=mc[0][0],
                     say='Ouça cada frase e repita em voz alta.', rs=rs['dictate'], chars=mc))
    pr = dict(B['produce'])
    frames.append(fr('produce', title='Missão: sua vez!', rs=rs['produce'], chars=mc,
                     bubble=[a, 'Now tell me about you!', 'Agora me conte sobre você!'], **pr))
    frames.append(fr('wrap', title='Para levar', recap=B['wrap_recap'], teaser=B['teaser'], sticker=X['sticker'], rs=rs['wrap'], chars=mc))

    e = copy.deepcopy(old)
    e['t'] = B['title']
    e['s'] = B['sub']
    e['pattern'] = B['pattern_label']
    e['a'] = {'k': ob['kind'].split(' ·')[0], 'w': ob['name'], 'y': ob['year'], 'd': ob['text']}
    e['h'] = {'l': X['gancho'][1], 'src': ob['name'], 'tr': X['gancho'][2]}
    e['p'] = B['why']
    e['v'] = B['vocab']
    e['fr'] = frames
    e['pilot'] = 1
    e['stage'] = dict(rs=st['rs'], chars=st['chars'])
    e['sc'] = B.get('sc', old.get('sc'))
    return e


def main():
    files = {}
    for k in ('01', '05'):
        f = os.path.join(ROOT, 'data', 'en-a1_%s.json' % k)
        files[f] = json.load(open(f, encoding='utf-8'))
    done = 0
    for X in V2:
        for f, d in files.items():
            for i, e in enumerate(d):
                if e['n'] == X['n']:
                    k = V2.index(X)
                    prev = (V2[k - 1], EXTRA[k - 1], VERBS[k - 1]) if k else None
                    d[i] = build(e, X, EXTRA[k], VERBS[k], prev)
                    done += 1
    for f, d in files.items():
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
    print('episódios reescritos:', done)


if __name__ == '__main__':
    main()
