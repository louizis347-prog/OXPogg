"""Relatório automático de qualidade das aulas ao vivo do Painel do Professor (Quest = data/v4, Real-Life = data/v3).
Gera docs/qualidade-aulas-painel.md e docs/qualidade-aulas-painel.csv (fila de revisão).
Mede: falas curtas, estrutura repetida nas falas, esqueleto de telas igual, títulos de tela repetidos,
obras repetidas/de ligação fraca (heurística), vocabulário que não volta. Não substitui revisão humana."""
import collections, csv, glob, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(HERE, '..'); D = os.path.join(R, '..', 'docs')
STOP = set('a o as os um uma de do da dos das em no na nos nas e ou que com para por se ao à é são foi um uns umas sua seu suas seus como mais já ele ela eles elas the of and to in is are for on with that this it as at by from'.split())
def toks(s): return {w for w in re.findall(r'[a-zà-ú]{4,}', (s or '').lower()) if w not in STOP}
def words(s): return re.findall(r"[A-Za-z’']+", re.sub(r'\*\*', '', s or ''))

def load(folder):
    out = []
    for f in sorted(glob.glob(os.path.join(R, 'data', folder, '[0-9]*.json'))):
        d = json.load(open(f)); out.append(d)
    return out

def analyze(lessons, tag):
    rows = []
    skel = collections.Counter(); skel_of = {}
    title_by_kind = collections.defaultdict(collections.Counter)
    works = collections.Counter()
    vocab_in = collections.defaultdict(set)
    for d in lessons:
        n = d['n']
        kinds = tuple(p.get('kind') or p.get('k') or '?' for p in d['pages'] if not p.get('x'))
        skel_of[n] = kinds; skel[kinds] += 1
        for p in d['pages']:
            if p.get('x'): continue
            k = p.get('kind')
            if k: title_by_kind[k][p.get('title', '')] += 1
            if k == 'work': works[p['work'].get('title', '')] += 1
            if k == 'vocab':
                for w in p['words']: vocab_in[w[0].lower()].add(n)
    dom_skel, dom_n = skel.most_common(1)[0]
    for d in lessons:
        n = d['n']; flags = []; m = {}
        lines = (d.get('dialog') or {}).get('lines') or d.get('dialog') or []
        en = [l['en'] for l in lines if isinstance(l, dict) and l.get('en')]
        wl = [len(words(x)) for x in en] or [0]
        m['falas'] = len(en); m['palavras_por_fala'] = round(sum(wl) / max(1, len(wl)), 1)
        short = sum(1 for x in wl if x <= 3) / max(1, len(wl)); m['falas_curtas_%'] = round(100 * short)
        if en and (sum(wl) / len(wl) < 5): flags.append('falas curtas (média < 5 palavras)')
        if short > .4: flags.append('muitas falas com até 3 palavras')
        # estrutura repetida: trigramas/aberturas
        tri = collections.Counter(); op = collections.Counter()
        for x in en:
            w = [t.lower() for t in words(x)]
            for i in range(len(w) - 2): tri[' '.join(w[i:i + 3])] += 1
            if len(w) >= 2: op[' '.join(w[:2])] += 1
        top3 = tri.most_common(1)[0] if tri else ('', 0); topop = op.most_common(1)[0] if op else ('', 0)
        m['trigrama_mais_repetido'] = '%s ×%d' % top3
        if en and top3[1] >= max(4, .35 * len(en)): flags.append('estrutura “%s” em %d de %d falas' % (top3[0], top3[1], len(en)))
        if en and topop[1] >= max(5, .5 * len(en)): flags.append('abertura “%s” em %d de %d falas' % (topop[0], topop[1], len(en)))
        # esqueleto
        sk = skel_of[n]; m['telas'] = len(sk); m['esqueleto_igual_ao_dominante'] = int(sk == dom_skel)
        # obra
        wk = next((p['work'] for p in d['pages'] if p.get('kind') == 'work'), None)
        if wk:
            m['obra'] = wk.get('title', ''); m['obra_ano'] = wk.get('year', '')
            if works[wk.get('title', '')] > 1: flags.append('obra repetida em %d aulas' % works[wk['title']])
            if not wk.get('year'): flags.append('obra sem ano')
            link = toks(' '.join([d.get('title', ''), d.get('topic', '') or '', d.get('pt', '')])) & toks(wk.get('note', '') + ' ' + wk.get('title', ''))
            m['obra_ligacao'] = len(link)
            if not link: flags.append('obra com ligação fraca com o tema (heurística)')
        # vocabulário que não volta
        mine = [w[0].lower() for p in d['pages'] if p.get('kind') == 'vocab' for w in p['words']]
        if mine:
            back = sum(1 for w in mine if len(vocab_in[w]) > 1)
            m['vocab'] = len(mine); m['vocab_reaparece_em_outra_aula_%'] = round(100 * back / len(mine))
        m['flags'] = len(flags)
        rows.append(dict(curso=tag, aula=n, titulo=d.get('title', ''), nivel=d.get('level', ''), **m, avisos=' | '.join(flags)))
    # títulos de tela repetidos (nível de curso)
    rep = {k: (c.most_common(1)[0][0], c.most_common(1)[0][1]) for k, c in title_by_kind.items() if c and c.most_common(1)[0][1] >= .5 * len(lessons) and len(lessons) > 5}
    return rows, dict(dom_skel_share=round(100 * dom_n / len(lessons)), n_skel=len(skel), titulos_repetidos=rep, obras_distintas=len(works), obras_repetidas=sum(1 for c in works.values() if c > 1), aulas=len(lessons))

allrows = []; md = ['# Qualidade das aulas ao vivo do Painel do Professor', '', 'Gerado por `professor/src/quality_report.py`. É uma fila de revisão automática: aponta onde olhar, não substitui a revisão humana.', '']
for folder, tag in (('v4', 'Quest'), ('v3', 'Real-Life')):
    ls = load(folder)
    if not ls: continue
    rows, g = analyze(ls, tag); allrows += rows
    md += ['## %s (%d aulas)' % (tag, g['aulas']), '',
           '- Esqueleto de telas: %d%% das aulas têm exatamente a mesma sequência (%d sequências distintas).' % (g['dom_skel_share'], g['n_skel']),
           '- Obras culturais distintas: %d; repetidas em mais de uma aula: %d.' % (g['obras_distintas'], g['obras_repetidas']),
           '- Títulos de tela repetidos em ≥50%% das aulas: %s.' % ('; '.join('%s → “%s” (%d×)' % (k, v[0], v[1]) for k, v in g['titulos_repetidos'].items()) or 'nenhum'), '']
    flagged = sorted([r for r in rows if r['flags']], key=lambda r: -r['flags'])
    md += ['Aulas com mais avisos (primeiras 15):', ''] + ['- **%s %s** · %s — %s' % (tag, r['aula'], r['titulo'], r['avisos']) for r in flagged[:15]] + ['']
    cnt = collections.Counter(a.split(' ')[0] + ' ' + a.split(' ')[1] if False else re.sub(r'“.*?”', '“…”', re.sub(r'\d+', 'N', a)) for r in rows for a in r['avisos'].split(' | ') if a)
    md += ['Resumo dos avisos:', ''] + ['- %s: %d aulas' % (k, v) for k, v in cnt.most_common()] + ['']
os.makedirs(D, exist_ok=True)
keys = sorted({k for r in allrows for k in r}, key=lambda k: ['curso', 'aula', 'titulo', 'nivel'].index(k) if k in ('curso', 'aula', 'titulo', 'nivel') else 9)
with open(os.path.join(D, 'qualidade-aulas-painel.csv'), 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.DictWriter(f, fieldnames=keys, delimiter=';'); w.writeheader(); w.writerows(allrows)
open(os.path.join(D, 'qualidade-aulas-painel.md'), 'w', encoding='utf-8').write('\n'.join(md))
print('\n'.join(md[:40]))
