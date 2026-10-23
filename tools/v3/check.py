#!/usr/bin/env python3
"""Confere a densidade e a consistência dos episódios no modelo piloto (compara com os 5 primeiros do A1)."""
import glob, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
KINDS = ['cover', 'review', 'hotscene', 'pgscene', 'pgsheet', 'pgrule', 'pgmold', 'pgsheet', 'verbs', 'vplay', 'pgexp', 'pgscene', 'pgsheet', 'pgsheet', 'pglab', 'pgsheet', 'pgspeak', 'pgmission', 'wrap']
WANT = {'hotscene': ('hot', 5), 'pgmold': ('pages', 3), 'verbs': ('items', 4), 'vplay': ('plan', 7), 'pgexp': ('items', 4), 'pgmission': ('missions', 3), 'wrap': ('recap', 4), 'pgspeak': ('items', 5)}
SHEETS = {'Você entendeu?': 3, 'Palavras da cena': 6, 'Palavras em contexto': 6, 'Complete as falas': 6, 'Qual está certa?': 4, 'Caça-sons': 5}


def load():
    it = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'en-a1_*.json'))):
        for x in json.load(open(f, encoding='utf-8')):
            it[x['n']] = x
    return it


def check(x, first=False):
    p = []
    fr = x['fr']
    kinds = [f['k'] for f in fr]
    want = KINDS if not first else [k for i, k in enumerate(KINDS) if i != 1]
    if kinds != want:
        p.append('sequência de quadros: %s' % kinds)
    for f in fr:
        k = f['k']
        if k in WANT:
            a, n = WANT[k]
            if len(f.get(a) or []) != n:
                p.append('%s.%s=%d (esperado %d)' % (k, a, len(f.get(a) or []), n))
        if k == 'pgscene':
            ln = f['lines']
            if len(ln) < 6 or len(ln) > 8:
                p.append('pgscene lines=%d' % len(ln))
            for l in ln:
                if l[0] not in f['cast'] or not l[1] or not l[2]:
                    p.append('pgscene fala inválida %s' % l[:2])
        if k == 'pgsheet':
            t = f.get('title')
            if t in SHEETS and len(f['items']) != SHEETS[t]:
                p.append('%s items=%d (esperado %d)' % (t, len(f['items']), SHEETS[t]))
            for it in f['items']:
                o = it.get('opts') or []
                labels = [(a if isinstance(a, str) else a[-1] or a[0]) for a in o]
                if not (0 <= it.get('a', -1) < len(o)):
                    p.append('%s: resposta fora das opções' % t)
                if len(set(map(str, o))) != len(o):
                    p.append('%s: opções repetidas %s' % (t, labels))
                if not it.get('why'):
                    p.append('%s: sem explicação' % t)
        if k == 'pglab':
            for a, n in (('ex', 3), ('pairs', 3), ('rounds', 3)):
                if len(f.get(a) or []) != n:
                    p.append('pglab.%s=%d' % (a, len(f.get(a) or [])))
            for r in f['rounds']:
                if not (0 <= r['a'] < len(r['opts'])):
                    p.append('pglab: rodada com resposta inválida')
        if k == 'pgrule':
            R = f['rule']
            for a in ('head', 'sub', 'uses', 'rules', 'say'):
                if not R.get(a):
                    p.append('pgrule sem %s' % a)
            if not (R.get('formula') or R.get('pairs')):
                p.append('pgrule sem fórmula')
        if k == 'pgmold':
            for pg in f['pages']:
                if max(len(s['opts']) for s in pg['slots']) < 3:
                    p.append('pgmold: página %s sem slot com 3 opções' % pg['label'])
        if k == 'verbs':
            if len(f.get('quiz') or []) != 4:
                p.append('verbs.quiz=%d' % len(f.get('quiz') or []))
        if k == 'pgmission':
            for m in f['missions']:
                d = m['data']
                for a in ('prompt', 'model', 'check', 'kw', 'tips', 'ok', 'reply'):
                    if not d.get(a):
                        p.append('missão %s sem %s' % (m['name'], a))
                for r in d['kw']:
                    try:
                        re.compile(r)
                    except re.error:
                        p.append('regex inválida %s' % r)
                if len(d['check']) != 3 or len(d['kw']) != 3 or len(d['tips']) != 3 or len(d['ok']) != 3:
                    p.append('missão %s: check/kw/tips/ok precisam de 3 itens' % m['name'])
                for r, c in zip(d['kw'], [d['model']]):
                    pass
                for r in d['kw']:
                    if not re.search(r, d['model'], re.I):
                        p.append('missão %s: o modelo não casa com %s' % (m['name'], r))
    return p


def main(ns):
    it = load()
    bad = 0
    for n in ns:
        x = it[n]
        pr = check(x, first=False)
        print(('OK ' if not pr else 'XX '), n, x['t'], len(x['fr']), 'quadros')
        for q in pr:
            print('    -', q)
        bad += len(pr)
    print('problemas:', bad)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        ns = [int(a) for a in sys.argv[1:]]
    else:
        from model_v3 import load_eps
        ns = [e['n'] for e in load_eps()]
    main(ns)
