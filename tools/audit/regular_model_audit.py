#!/usr/bin/env python3
"""Auditoria dos episódios do inglês regular contra o modelo dos episódios 2–5 do A1 (7009801, 70001, 7070001, 30001).
Uso: python3 tools/audit/regular_model_audit.py [curso ...]   (sem argumentos: en-a1 en-a2 en-b1)  -> imprime resumo e grava tools/audit/regular_model_audit.json"""
import json, glob, os, re, sys, collections
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools')); sys.path.insert(0, os.path.join(ROOT, 'tools', 'v3'))
KINDS = ['cover', 'review', 'hotscene', 'pgscene', 'pgsheet', 'pgrule', 'pgmold', 'pgsheet', 'verbs', 'vplay', 'pgexp', 'pgscene', 'pgsheet', 'pgsheet', 'pglab', 'pgsheet', 'pgspeak', 'pgmission', 'wrap']
FILL = {'Good.', 'Coffee?', 'Please.', 'Here.'}
GENERIC = {'woman', 'man', 'girl', 'boy', 'teacher', 'student', 'friend', 'a', 'b'}
courses = sys.argv[1:] or ['en-a1', 'en-a2', 'en-b1']

def load(c):
    it = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', c + '_*.json'))):
        it += json.load(open(f, encoding='utf-8'))
    it.sort(key=lambda e: e['o']); return it

def F(e):
    d = collections.defaultdict(list)
    for f in e['fr']: d[f['k']].append(f)
    return d

def sets(e):
    f = F(e)
    return dict(
        obra={(e.get('a') or {}).get('w', '')} - {''},
        vocab={w[0].lower() for w in (e.get('v') or [])},
        verbos={v['v'].lower() for v in f.get('verbs', [{}])[0].get('items', [])},
        lab={x[0].lower() for x in f.get('pglab', [{}])[0].get('ex', [])},
        hot={h.get('en', '').lower() for h in f.get('hotscene', [{}])[0].get('hot', [])})

def norm(s): return set(re.findall(r'[a-zà-ú0-9]+', (s or '').lower())) - {'o', 'a', 'de', 'do', 'da', 'the', 'of', 'e', 'and', 'um', 'uma'}

report = {}; summary = {}
for c in courses:
    items = [e for e in load(c) if e.get('presentation') == 'regular-pilot-v1']
    # arte (ids de personagem) usada por obras diferentes
    art_works = collections.defaultdict(set)
    for e in items:
        f = F(e); w = (e.get('a') or {}).get('w', '')
        for hs in f.get('hotscene', []):
            for ch in hs.get('chars', []): art_works[ch[0]].add(w)
    pt_by_en = collections.defaultdict(set)
    for e in items:
        for sc in F(e).get('pgscene', []):
            for l in sc['lines']: pt_by_en[l[1].strip()].add(l[2].strip())
    bad = collections.defaultdict(list)
    for i, e in enumerate(items):
        n = e['n']; f = F(e); kinds = [x['k'] for x in e['fr']]
        want = KINDS if i else [k for k in KINDS if k != 'review']
        if kinds != want and not (i == 0 and kinds == KINDS): bad['K1 sequência de quadros'].append(n)
        sc = f.get('pgscene', [])
        if sc and len(sc[0]['lines']) not in (6, 7, 8): bad['K2 cena com 6–8 falas'].append(n)
        cast = list(sc[0]['cast']) if sc else []
        if cast and all(x.lower() in GENERIC for x in cast): bad['K3 elenco genérico (Woman/Man…)'].append(n)
        ids = [ch[0] for hs in f.get('hotscene', []) for ch in hs.get('chars', [])]
        if ids and all(len(art_works[x]) >= 4 for x in ids): bad['K4 arte de personagem genérica (usada em 4+ obras)'].append(n)
        w = f.get('wrap', [{}])[0]; st = w.get('sticker') or {}; aw = (e.get('a') or {}).get('w', '')
        if not st or not st.get('sub', '').split(' · ')[0] or norm(st['sub'].split(' · ')[0]) != norm(aw) and not (norm(st['sub']) & norm(aw)):
            bad['K5 figurinha/fechamento sem a obra do episódio'].append(n)
        if i + 1 < len(items):
            nx = items[i + 1]; tz = (w.get('teaser') or {})
            alvo = norm(nx['t']) | norm((nx.get('a') or {}).get('w', '')) | norm(nx.get('gs')) | norm(nx.get('s'))
            if not ((norm(tz.get('t')) | norm(tz.get('d'))) - {'próximo', 'padrão', 'para', 'com', 'em', 'breve'}) & alvo:
                bad['K6 teaser não aponta para o próximo episódio'].append(n)
        if i and 'review' in f:
            rv = f['review'][0]; pv = items[i - 1]
            if rv.get('prev') != pv['t'] or norm(rv.get('work')) != norm((pv.get('a') or {}).get('w', '')):
                bad['K7 revisão não é do episódio anterior'].append(n)
        for nb in ([items[i - 1]] if i else []):
            A, B = sets(e), sets(nb)
            for k in ('obra', 'vocab', 'verbos', 'lab', 'hot'):
                lim = 1 if k == 'obra' else 2  # uma palavra comum (ex.: play) é normal; 2+ é repetição
                if len(A[k] & B[k]) >= lim: bad['K8 repete %s do episódio vizinho' % k].append(n)
        if sum(1 for l in (sc[1]['lines'] if len(sc) > 1 else []) if l[1] in FILL) >= 2: bad['K9 falas de enchimento padrão'].append(n)
        sub = (f.get('cover', [{}])[0].get('sub') or '')
        if 'em 10 minutos' not in sub.lower(): bad['K10 capa sem "Em 10 minutos…"'].append(n)
        ms = f.get('pgmission', [{}])[0].get('missions', [])
        if len(ms) != 3 or (ms and ms[0]['name'] != 'Cena da obra'): bad['K11 missões fora do padrão'].append(n)
        for sc_ in sc:
            for l in sc_['lines']:
                if len(pt_by_en[l[1].strip()]) > 1: bad['K12 mesma fala com traduções diferentes'].append(n); break
            else: continue
            break
    report[c] = {k: v for k, v in bad.items()}
    summary[c] = (len(items), {k: len(set(v)) for k, v in bad.items()})
json.dump(report, open(os.path.join(ROOT, 'tools/audit/regular_model_audit.json'), 'w'), ensure_ascii=False, indent=1)
for c, (n, d) in summary.items():
    print('\n==', c, '·', n, 'episódios no modelo')
    for k in sorted(d): print('  %-58s %4d  (%d%%)' % (k, d[k], round(100 * d[k] / n)))
    if not d: print('  nenhuma incoerência')
