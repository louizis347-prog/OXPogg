#!/usr/bin/env python3
"""Restaura o conteúdo autoral dos episódios "completos" do inglês que os scripts de densidade degradaram.

Em ~2.500 episódios (metade do curso) o vocabulário perdeu os ícones certos (virou 💡🧭⚖️🔄➡️🤝), os verbos viraram a
lista de palavras, as frases com a palavra escondida viraram a palavra solta, os sons do jogo "Caça-sons" viraram
rodadas de palavras e o quadro de leitura sumiu. Aqui os quadros words/wsent/verbs/vplay/lplay/read voltam à versão
autoral (commit f7a5b55). A leitura entra no lugar da "linha do tempo" de uma só obra, para manter 20 quadros.
Cenas/quizzes com falas genéricas ("Today, we are talking about this situation.") também voltam à versão autoral.
Reexecutável: só mexe em episódios que ainda estão degradados.
"""
import copy, json, os, subprocess

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
ORIG = 'f7a5b55'
RAND = {'💡', '🧭', '⚖️', '🔄', '➡️', '🤝'}
GENERIC = {'Today, we are talking about this situation.', 'I can explain my point of view.',
           'Let’s listen to the rhythm for a moment.'}
RESTORE = ('words', 'wsent', 'verbs', 'vplay', 'lplay')


def degraded(e):
    w = next((x for x in e['fr'] if x['k'] == 'words'), None)
    return bool(w and len(w.get('items', [])) >= 4 and sum(1 for it in w['items'] if it[1] in RAND) >= 4)


def generic_scene(e):
    sc = next((x for x in e['fr'] if x['k'] == 'scene'), None)
    return bool(sc and any(l[1] in GENERIC for l in sc.get('lines', [])))


def main():
    m = json.load(open(os.path.join(ROOT, 'manifest.json'), encoding='utf-8'))
    tot = dict(eps=0, read=0, scenes=0, no20=0)
    for lv in ['a1', 'a2', 'b1', 'b2', 'c1', 'c2']:
        for b in m['en-' + lv]:
            p = os.path.join(ROOT, b)
            data = json.load(open(p, encoding='utf-8'))
            old = {e['n']: e for e in json.loads(subprocess.check_output(['git', 'show', '%s:data/%s' % (ORIG, b)]))}
            changed = False
            for e in data:
                o = old.get(e['n'])
                if not o:
                    continue
                fo = {x['k']: x for x in o['fr']}
                idx = {x['k']: i for i, x in enumerate(e['fr'])}
                if degraded(e):
                    for k in RESTORE:
                        if k in fo and k in idx:
                            new = copy.deepcopy(fo[k])
                            for q in ('coach', 'levelProgression'):
                                if q in e['fr'][idx[k]]:
                                    new[q] = e['fr'][idx[k]][q]
                            e['fr'][idx[k]] = new
                    if 'read' in fo and 'read' not in idx:
                        rd = copy.deepcopy(fo['read'])
                        pos = idx.get('lplay', 0)
                        e['fr'].insert(pos, rd)
                        tt = next((i for i, x in enumerate(e['fr']) if x['k'] == 'culttl' and len(x.get('works', [])) <= 1), None)
                        if tt is not None:
                            del e['fr'][tt]
                        tot['read'] += 1
                    tot['eps'] += 1
                    changed = True
                if generic_scene(e):
                    idx = {x['k']: i for i, x in enumerate(e['fr'])}
                    for k in ('scene', 'dquiz', 'read'):
                        if k in fo and k in idx:
                            new = copy.deepcopy(fo[k])
                            for q in ('coach', 'levelProgression'):
                                if q in e['fr'][idx[k]]:
                                    new[q] = e['fr'][idx[k]][q]
                            e['fr'][idx[k]] = new
                    tot['scenes'] += 1
                    changed = True
                if len(e['fr']) != 20:
                    tot['no20'] += 1
            if changed:
                open(p, 'w', encoding='utf-8').write(json.dumps(data, ensure_ascii=False, separators=(',', ':')))
    print(tot)


if __name__ == '__main__':
    main()
