#!/usr/bin/env python3
"""Conserta incoerências mecânicas do inglês regular: (1) teaser do fechamento aponta para o episódio que de fato vem depois;
(2) quadro de revisão (mochila) refeito a partir do episódio anterior real. Uso: python3 tools/audit/fix_mechanical.py [curso ...]"""
import json, glob, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools')); sys.path.insert(0, os.path.join(ROOT, 'tools', 'v3'))
import model_v2 as M
import model_v3 as MV
courses = sys.argv[1:] or ['en-a1', 'en-a2', 'en-b1']
STOP = {'próximo', 'padrão', 'para', 'com', 'em', 'breve', 'o', 'a', 'de', 'do', 'da', 'the', 'of', 'e', 'and', 'um', 'uma'}
norm = lambda s: set(re.findall(r'[a-zà-ú0-9]+', (s or '').lower())) - STOP
tot = {'teaser': 0, 'review': 0}
for c in courses:
    files = sorted(glob.glob(os.path.join(ROOT, 'data', c + '_*.json')))
    data = {f: json.load(open(f, encoding='utf-8')) for f in files}
    items = [(f, i, e) for f, d in data.items() for i, e in enumerate(d)]
    items.sort(key=lambda t: t[2]['o'])
    pil = [t for t in items if t[2].get('presentation') == 'regular-pilot-v1']
    ch = set()
    for k, (f, i, e) in enumerate(pil):
        fr = {x['k']: x for x in e['fr']}
        if k + 1 < len(pil):
            nx = pil[k + 1][2]
            w = fr.get('wrap')
            if w is not None:
                tz = w.get('teaser') or {}
                alvo = norm(nx['t']) | norm((nx.get('a') or {}).get('w', '')) | norm(nx.get('gs')) | norm(nx.get('s'))
                if not (norm(tz.get('t')) | norm(tz.get('d'))) & alvo:
                    gs = (nx.get('gs') or nx.get('s') or '').strip()
                    w['teaser'] = {'t': nx['t'].split(' · ')[0], 'd': ('Próximo padrão: ' + gs)[:110]}
                    tot['teaser'] += 1; ch.add(f)
        if k and 'review' in fr:
            pv = pil[k - 1][2]; rv = fr['review']
            wk = (pv.get('a') or {}).get('w', '')
            if rv.get('prev') != pv['t'] or norm(rv.get('work')) != norm(wk):
                P = MV.prev_from_pilot(pv) if any(x['k'] == 'pgrule' for x in pv['fr']) else MV.prev_from_old(pv)
                X, XT, VB = P
                rv['prev'] = pv['t']; rv['work'] = wk
                rv['recap'] = [list(x) for x in X['base']['wrap_recap']]
                try: rv['bag'] = [g for g in M.bag_of(P) if g['items']]
                except Exception as ex: print('  bag não refeito', e['n'], ex)
                tot['review'] += 1; ch.add(f)
            gs = e.get('gs') or ''
            if gs and ('**%s**' % gs) not in (rv.get('next') or ''):
                rv['next'] = 'Hoje: **%s**' % gs; ch.add(f)
    for f in ch:
        json.dump(data[f], open(f, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print(tot)
