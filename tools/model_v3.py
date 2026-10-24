#!/usr/bin/env python3
"""Reescreve os episódios 86–110 do A1 de inglês no modelo piloto (mesmo molde de tools/model_v2.py).

Cada episódio é escrito à mão em tools/v3/ep_*.py (função ep() de tools/v3/lib.py) e montado aqui com model_v2.build().
Uso: python3 tools/model_v3.py [n ...]   (sem argumentos, monta todos os episódios escritos)
"""
import glob, importlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import model_v2 as M  # noqa: E402
from v3 import lib  # noqa: E402


def load_eps():
    eps = []
    for f in sorted(glob.glob(os.path.join(HERE, 'v3', 'ep_*.py'))):
        m = importlib.import_module('v3.' + os.path.basename(f)[:-3])
        eps += m.EPS
    return eps


def prev_from_old(it):
    """Mochila de um episódio anterior que ainda está no formato antigo (usa palavras, verbos e padrão do próprio episódio)."""
    voc = it['v']
    ico = {}
    for s in it['fr']:
        if s['k'] == 'words':
            for w in s['items']:
                ico[w[0]] = w[1]
    base = dict(title=it['t'], wrap_recap=[], vocab=voc, balloons=[(ico.get(w[0], '🔤'), w[0]) for w in voc])
    vb = [s for s in it['fr'] if s['k'] == 'verbs']
    items = vb[0]['items'] if vb else []
    verbs = dict(title='', tip='', items=[dict(v=i['v'], ic=i['ic'], pt=i['pt'], f=i['f']) for i in items])
    rd = [s for s in it['fr'] if s['k'] in ('rdg', 'read')]
    head = (it.get('g') or {}).get('t') or it['t']
    sub = it.get('s') or ''
    ex = [list(x) for x in (rd[0].get('s') or [])][:3] if rd else []
    rule = dict(head=head, sub=sub, uses=[dict(ico='📌', en=e[0].replace('{{', '').replace('}}', ''), pt=e[1]) for e in ex])
    base['wrap_recap'] = [[e[0].replace('{{', '').replace('}}', ''), e[1]] for e in ex][:4]
    X = dict(base=base, hot=[], rule=rule, obra=dict(name=it['a']['w']))
    XT = dict(exp=[], lab=dict(short=(next((s.get('short') for s in it['fr'] if s['k'] == 'lplay'), '') or ''), ex=[['']]))
    return (X, XT, verbs)


def prev_from_pilot(it):
    """Mochila de um episódio anterior que já está no modelo piloto mas não foi escrito em tools/v3 (os 5 primeiros)."""
    F = {}
    for f in it['fr']:
        F.setdefault(f['k'], []).append(f)
    grid = next((f for f in F['pgsheet'] if f.get('title') == 'Palavras da cena'), None)
    if grid:
        words = [(f_['fig'], f_['say'], f_.get('ptWord', '')) for f_ in grid['items']]
    else:  # episódios feitos por outro fluxo: usa os objetos da cena clicável
        words = [(h['e'], h['en'], h.get('pt', '')) for h in F['hotscene'][0]['hot']]
    rule = F['pgrule'][0]['rule']
    base = dict(title=it['t'], wrap_recap=F['wrap'][0]['recap'], vocab=[[w, p, ''] for _e, w, p in words], balloons=[(e, w) for e, w, _p in words])
    X = dict(base=base, hot=[], rule=dict(head=rule['head'], sub=rule['sub'], uses=rule.get('uses', [])), obra=dict(name=''))
    XT = dict(exp=F['pgexp'][0]['items'], lab=dict(short=F['pglab'][0]['short'], ex=F['pglab'][0]['ex']))
    return (X, XT, F['verbs'][0])


def main(only=None):
    chunks = {}
    where = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'en-a1_*.json'))):
        d = json.load(open(f, encoding='utf-8'))
        chunks[f] = d
        for i, e in enumerate(d):
            where[e['n']] = (f, i)
    order = sorted(where, key=lambda n: chunks[where[n][0]][where[n][1]]['o'])
    eps = sorted(load_eps(), key=lambda e: order.index(e['n']))
    done = 0
    for k, E in enumerate(eps):
        if only and E['n'] not in only:
            continue
        f, i = where[E['n']]
        old = chunks[f][i]
        P = eps[k - 1] if k else None
        if P and order.index(P['n']) == order.index(E['n']) - 1:
            prev = (P['v2'], P['extra'], P['verbs'])
        else:
            pi = order[order.index(E['n']) - 1]
            pf, pj = where[pi]
            pit = chunks[pf][pj]
            prev = prev_from_pilot(pit) if any(x['k'] == 'pgrule' for x in pit['fr']) else prev_from_old(pit)
        M.HOTPT.update(lib.SAYPT)
        chunks[f][i] = M.build(old, E['v2'], E['extra'], E['verbs'], prev, E['more'])
        for fr in chunks[f][i]['fr']:
            if fr['k'] == 'review':
                fr['bag'] = [g for g in fr['bag'] if g['items']]  # sem bolsos vazios (episódio anterior ainda no formato antigo)
        done += 1
    for f, d in chunks.items():
        out = json.dumps(d, ensure_ascii=False, separators=(',', ':'))
        if d != json.load(open(f, encoding='utf-8')):  # só reescreve o que mudou (outros fluxos editam os arquivos seguintes)
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(out)
    print('episódios montados:', done)


if __name__ == '__main__':
    main({int(x) for x in sys.argv[1:]} or None)
