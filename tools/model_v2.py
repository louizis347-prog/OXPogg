#!/usr/bin/env python3
"""Modelo de 12 quadros ("padrão do dia em uma obra") aplicado aos 5 primeiros episódios do A1 de inglês.

Quadros: capa com personagens · cena clicável (obra) · cena (diálogo) · quiz · padrão · palavras com figura ·
complete a fala · qual está certa · fale · missão · revisão (ep. 2 em diante) · fechamento com figurinha.
Uso: python3 tools/model_v2.py
"""
import json, os, sys, copy, subprocess

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from model_v2_data import V2  # noqa: E402


def main_chars(st):
    ids = [c[0] for c in st['chars']][:2]
    pos = [(32, 0), (68, 1)] if len(ids) > 1 else [(50, 0)]
    return [[i, x, fl, 1.0] for i, (x, fl) in zip(ids, pos)]


def build(old, X):
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
    frames.append(fr('hotscene', title='Explore a cena', hint='Toque nos objetos brilhantes para ouvir o nome em inglês.',
                     rs=st['rs'], chars=st['chars'], hot=X['hot'], say='Toque nos objetos brilhantes!',
                     obra=dict(name=ob['name'], kind=ob['kind'], text=ob['text'], line=ob['line'], pa=ob['pa'])))
    frames.append(fr('scene', art=B['scene_art'], cast=B['cast'], lines=B['lines'], rs=st['rs']))
    frames.append(fr('dquiz', title='Você entendeu?', items=B['quiz'], cast=B['cast'], lines=B['lines'], rs=rs['dquiz'], chars=mc,
                     bubble=[b, 'What do you remember?', 'De que você se lembra?']))
    frames.append(fr('rdg', title='Descubra o padrão', s=B['rdg_s'], rule=B['rule'], q=B['rdg_q'],
                     say='Toque nas frases da cena. O que se repete? Depois, uma perguntinha!', rs=rs['rdg'], chars=mc,
                     bubble=[a, 'Look at my sentences. What repeats?', 'Olhe as minhas frases. O que se repete?']))
    # palavras com figura: alvo + 3 distratores da lista de balões
    pool = [(e, w) for e, w in B['balloons']]
    rounds = []
    for i, it in enumerate(B['vplay']):
        tgt = (it['ic'], it['v'])
        others = [p for p in pool if p[1].lower() != it['v'].lower()][:3]
        opts = others[:]
        opts.insert((i * 3 + 1) % 4, tgt)
        rounds.append({'q': 'Ouça e toque na imagem certa', 'say': it['v'], 'opts': [list(o) for o in opts],
                       'a': opts.index(tgt), 'why': '%s — %s. %s' % (it['v'], it['pt'], it.get('note', ''))})
    frames.append(fr('tapimg', title='Palavras da cena', rounds=rounds, say='Ouça a palavra e toque na figura certa.',
                     rs=rs['vplay'], chars=mc, bubble=[a, 'Help me find the words!', 'Me ajude a achar as palavras!']))
    frames.append(fr('gap', title='Complete a fala', rounds=[dict(r, en='Escolha a palavra que completa a frase.', say=r['q'].replace('___', r['opts'][r['a']])) for r in X['gap']],
                     say='Escolha a palavra que completa a fala.', rs=rs['build'], chars=mc,
                     bubble=[b, 'Complete the sentence!', 'Complete a frase!']))
    frames.append(fr('trap', title='Qual está certa?', rounds=[dict(r, say=r['opts'][r['a']]) for r in X['trap']],
                     say='Só uma frase está certa.', rs=rs['order'], chars=mc,
                     bubble=[b, 'Careful! Only one is right.', 'Cuidado! Só uma está certa.']))
    frames.append(fr('pgspeak', title='Sua vez de falar', items=[list(x) for x in B['dictate'][:3]], say='Ouça, toque no microfone e repita.',
                     rs=rs['dictate'], chars=mc, bubble=[a, 'Say it with me!', 'Diga comigo!']))
    pr = dict(B['produce'])
    frames.append(fr('produce', title='Missão: sua vez!', rs=rs['produce'], chars=mc,
                     bubble=[a, 'Now tell me about you!', 'Agora me conte sobre você!'], **pr))
    if X['review']:
        R = B['review']
        frames.append(fr('review', prev=R['prev'], work=R['work'], recap=R['recap'], bag=R['bag'],
                         lead='Abra cada bolso da mochila e relembre o episódio anterior!',
                         next='Hoje: **%s**' % B['pattern_label'], say='Bora relembrar o episódio anterior antes de seguir!',
                         rs=rs['review'], chars=mc))
    frames.append(fr('wrap', title='Para levar', recap=B['wrap_recap'], teaser=B['teaser'], sticker=X['sticker'], rs=rs['wrap'], chars=mc))

    e = copy.deepcopy(old)
    e['t'] = B['title']
    e['s'] = B['sub']
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
                    d[i] = build(e, X)
                    done += 1
    for f, d in files.items():
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
    print('episódios reescritos:', done)


if __name__ == '__main__':
    main()
