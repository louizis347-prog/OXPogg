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
from model_v2_more import MORE  # noqa: E402


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
        opts = [it['v'], form, LG['wrong'](it['v'], form)]
        out.append(dict(text=sent.replace(form, '___', 1), pt=LG['vq'] % (it['v'], it['pt']), opts=opts,
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
    return [dict(ic='📌', l=u('Padrão'), items=pat), dict(ic='🔤', l=u('Palavras'), items=words), dict(ic='🏃', l=u('Verbos'), items=verbs),
            dict(ic='💬', l=u('Expressões'), items=exps), dict(ic='🎧', l=u('Sons'), items=snd)]


HOTPT = {
    "It's late. I'm tired.": 'É tarde. Estou cansado.', "I'm at the station.": 'Estou na estação.', "I'm from Peru.": 'Eu sou do Peru.',
    "I'm Paddington. This is my bag.": 'Eu sou o Paddington. Esta é a minha mala.', "I'm hungry. I want a sandwich.": 'Estou com fome. Quero um sanduíche.',
    "Oh dear! I'm late!": 'Meu Deus! Estou atrasado!', 'Are you in a hurry?': 'Você está com pressa?', 'Are you lost?': 'Você está perdida?',
    'Are you new here?': 'Você é nova aqui?', 'Are you a hat? No, I am not!': 'Você é um chapéu? Não, não sou!',
    "She's Glinda. She's a good witch.": 'Ela é a Glinda. Ela é uma bruxa boa.', "He's the Wizard of Oz.": 'Ele é o Mágico de Oz.',
    "He's kind. She's kind.": 'Ele é gentil. Ela é gentil.', "She's far from home.": 'Ela está longe de casa.',
    "She's from Kansas, over the rainbow.": 'Ela é do Kansas, além do arco-íris.',
    'Is she a fairy? Yes, she is.': 'Ela é uma fada? Sim, é.', "Is it Captain Hook's ship?": 'É o navio do Capitão Gancho?',
    "Is it a bird? No, it isn't.": 'É um pássaro? Não, não é.', 'Is he angry? Yes, he is!': 'Ele está bravo? Sim, está!',
    'Is it a star? Yes, it is.': 'É uma estrela? Sim, é.',
    'I see two toys.': 'Vejo dois brinquedos.', 'I see three balloons.': 'Vejo três balões.', 'Andy loves puppies.': 'O Andy adora cachorrinhos.',
    'I love stories about planets.': 'Eu adoro histórias sobre planetas.', 'Parties are fun!': 'Festas são divertidas!',
}

LG = dict(ui={}, 
    hint='Toque nos objetos brilhantes para ouvir o nome em inglês.', badge='A1',
    remember=('What do you remember?', 'De que você se lembra?'), swap=('Swap the pieces and build sentences!', 'Troque as peças e monte frases!'),
    words=('Listen and choose the word!', 'Ouça e escolha a palavra da figura!'), verbs=("These are today's verbs!", 'Estes são os verbos de hoje!'),
    vmission=('Verb mission! I will help you.', 'Missão dos verbos! Eu ajudo você.'), exps=('This is how people really talk!', 'É assim que as pessoas falam de verdade!'),
    complete=('Complete the sentences!', 'Complete as frases!'), careful=('Careful! Only one is right.', 'Cuidado! Só uma está certa.'),
    lab=("Let's train our ears!", 'Vamos treinar o ouvido!'), hunt=('Listen and hunt the sound!', 'Ouça e cace o som certo!'),
    pick=('Pick a mission! Which one do you want?', 'Escolha uma missão! Qual você quer?'), wrong=lambda v, form: ing(v), vq='Verbo **%s** (%s) com he/she.')


def u(t):
    return LG['ui'].get(t, t)


def build(old, X, XT, VB, prev, MR=None):
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
    frames.append(fr('cover', art=B['cover_art'], sub=B['cover_sub'], badge=LG['badge'], snd=old['fr'][0].get('snd', 'bell'),
                     say=B['cover_say'], gancho=X['gancho'], obra='%s · %s' % (ob['name'], ob['year']),
                     stage=dict(rs=st['rs'], chars=st['chars'])))
    if X['review'] and prev:  # revisão do episódio anterior fica no INÍCIO deste episódio
        Bp = prev[0]['base']
        frames.append(fr('review', prev=Bp['title'], work=prev[0]['obra']['name'],
                         recap=[list(x) for x in Bp['wrap_recap']], bag=bag_of(prev),
                         lead=u('Abra cada bolso da mochila e relembre o episódio anterior!'),
                         next=u('Hoje: **%s**') % B['pattern_label'], say=u('Bora relembrar o episódio anterior antes de seguir!'),
                         rs=rs['review'], chars=mc))
    frames.append(fr('hotscene', title=u('Explore a cena'), hint=LG['hint'],
                     rs=st['rs'], chars=st['chars'], hot=[dict(h, sayPt=HOTPT.get(h['say'], '')) for h in X['hot']], say=u('Toque nos objetos brilhantes!'),
                     obra=dict(name=ob['name'], kind=ob['kind'], text=ob['text'], line=ob['line'], pa=ob['pa'])))
    frames.append(fr('pgscene', cast=B['cast'], lines=B['lines'], speakers=X['speakers'], rs=st['rs'], chars=st['chars'],
                     say=u('Ouça a cena e leia junto.')))
    # você entendeu?
    quiz = [dict(ask=it['q'], speak=it['q'], pt=it['pt'], opts=it['opts'], a=it['a'], why=it['why']) for it in B['quiz']]
    frames.append(fr('pgsheet', title=u('Você entendeu?'), items=quiz, rs=rs['dquiz'], chars=mc, review=False,
                     bubble=[b, *LG['remember']]))
    # padrão com ilustração
    R = dict(X['rule'])
    R['formula'] = [{'from': r['from_'], 'to': r['to'], 'say': r.get('say'), 'note': r.get('note')} for r in R.get('formula', [])]
    frames.append(fr('pgrule', rule=R, q=B['rdg_q'], rs=rs['rdg'], say=u('Veja o padrão com figuras e ouça os exemplos.')))
    frames.append(fr('pgmold', title=u('Molde de frases'), pages=MR['mold'], rs=rs['pat'], chars=mc,
                     say=u('Toque nas peças e veja várias frases.'), bubble=[a, *LG['swap']]))
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
        items.append(dict(fig=emo, say=w, ask=u('Qual é a palavra?'), opts=opts, a=opts.index(w), ptWord=p,
                          why='**%s** = %s.%s' % (w, p, (' ' + note) if note else '')))
    frames.append(fr('pgsheet', title=u('Palavras da cena'), layout='grid', items=items, rs=rs['vplay'], chars=mc,
                     bubble=[a, *LG['words']]))
    # verbos (4) + missão dos verbos
    frames.append(fr('verbs', title=VB['title'], items=VB['items'], tip=VB['tip'], say=u('Vamos ver os verbos de hoje!'), rs=rs['build'], chars=mc,
                     quiz=verb_quiz(VB), bubble=[b, *LG['verbs']]))
    frames.append(fr('vplay', title=u('Missão dos verbos'), items=VB['items'], plan=[[0, 0], [1, 0], [2, 0], [3, 0], [0, 3], [1, 3], [2, 3]],
                     say=u('Missão dos verbos: 7 passos. Eu ajudo você!'), rs=rs['build'], chars=mc,
                     bubble=[a, *LG['vmission']]))
    # expressões comuns e gírias + cena com as expressões
    frames.append(fr('pgexp', title=u('Expressões e gírias'), items=XT['exp'], quiz=MR['expq'], rs=rs['vplay'], chars=mc,
                     say=u('Toque para ouvir cada expressão.'), bubble=[a, *LG['exps']]))
    es = XT['exp_scene']
    frames.append(fr('pgscene', title=u('Na conversa de verdade'), cast=B['cast'], lines=es['lines'], speakers=X['speakers'], rs=es['rs'],
                     chars=st['chars'], say=u('Veja as expressões em uso. Elas estão destacadas.')))
    gap = [dict(text=r['q'], pt=r['pt'], opts=r['opts'], a=r['a'], why=r['why'],
                say=r['q'].replace('___', r['opts'][r['a']])) for r in X['gap']]
    gap = gap + MR['gap']
    frames.append(fr('pgsheet', title=u('Complete as falas'), items=gap, rs=rs['build'], chars=mc,
                     bubble=[b, *LG['complete']]))
    trap = [dict(ask=r['q'], opts=r['opts'], a=r['a'], why=r['why'], say=strip_tags(r['opts'][r['a']])) for r in X['trap']]
    trap = trap + [dict(ask=r['ask'], opts=r['opts'], a=r['a'], why=r['why'], say=r.get('say') or strip_tags(r['opts'][r['a']])) for r in MR['trap']]
    frames.append(fr('pgsheet', title=u('Qual está certa?'), items=trap, rs=rs['order'], chars=mc,
                     bubble=[b, *LG['careful']]))
    # laboratório de sons + caça-sons (só se o episódio ainda não tiver o laboratório)
    if not any(f['k'] in ('soundlab', 'pglab') for f in frames):
        lab = dict(XT['lab'])
        frames.append(fr('pglab', rs=rs['soundlab'], chars=mc, bubble=[a, *LG['lab']], **lab))
        frames.append(fr('pgsheet', title=u('Caça-sons'), items=XT['hunt'], rs=rs['soundlab'], chars=mc,
                         bubble=[b, *LG['hunt']]))
    frames.append(fr('pgspeak', title=u('Sua vez de falar'), items=[list(x) for x in B['dictate'][:3]] + [list(x) for x in MR['speak']], who=mc[0][0],
                     say=u('Ouça cada frase e repita em voz alta.'), rs=rs['dictate'], chars=mc))
    pr = dict(B['produce'])
    m1 = dict(ic=X['mission_ic'], name=u('Cena da obra'), desc=u('Fale como os personagens.'),
              data=dict(prompt=pr['prompt'], ph=u('Escreva a sua resposta aqui…'), chips=[pr['chips'][0]], model=pr['model'], check=pr['check'],
                        kw=pr['kw'], tips=pr['tips'], ok=pr['ok'], reply=pr['reply']))
    frames.append(fr('pgmission', title=u('Missão: sua vez!'), missions=[m1] + MR['missions'], rs=rs['produce'], chars=mc,
                     say=u('Escolha uma missão e mostre o que você aprendeu!'), bubble=[a, *LG['pick']]))
    frames.append(fr('wrap', title=u('Para levar'), recap=B['wrap_recap'], teaser=B['teaser'], sticker=X['sticker'], rs=rs['wrap'], chars=mc))

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
                    d[i] = build(e, X, EXTRA[k], VERBS[k], prev, MORE[k])
                    done += 1
    for f, d in files.items():
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
    print('episódios reescritos:', done)


if __name__ == '__main__':
    main()
