#!/usr/bin/env python3
"""Auditoria de vocabulário por nível CEFR (CEFR-J Vocabulary Profile, Tono Lab / openlanguageprofiles/olp-en-cefrj).
Uso: cefr_audit.py [de ate]  — lista, por aula, as palavras do diálogo e do vocabulário acima do nível da aula.
Nível da aula: A1 (n<2000) ou A2 (n>=2000). Nomes próprios (elenco, cidades) e números são ignorados."""
import glob, json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')); D = os.path.join(ROOT, 'data')
W = json.load(open(os.path.join(D, 'cefrj-vocab.json'), encoding='utf-8')); RANK = {'A1': 1, 'A2': 2, 'B1': 3, 'B2': 4}
IRR = {'went':'go','gone':'go','saw':'see','seen':'see','took':'take','taken':'take','ate':'eat','eaten':'eat','bought':'buy','made':'make','came':'come','said':'say','got':'get','gave':'give','given':'give','found':'find','left':'leave','lost':'lose','met':'meet','wrote':'write','written':'write','sent':'send','paid':'pay','slept':'sleep','swam':'swim','drove':'drive','ran':'run','won':'win','brought':'bring','caught':'catch','broke':'break','broken':'break','forgot':'forget','felt':'feel','heard':'hear','told':'tell','knew':'know','thought':'think','stood':'stand','sang':'sing','wore':'wear','had':'have','did':'do','was':'be','were':'be','been':'be','am':'be','is':'be','are':'be','children':'child','men':'man','women':'woman','people':'person','feet':'foot','teeth':'tooth','spent':'spend','read':'read','sat':'sit','flew':'fly','woke':'wake','hid':'hide','built':'build','kept':'keep','held':'hold','let':'let','put':'put','cut':'cut','hit':'hit','set':'set','shut':'shut','became':'become','began':'begin','grew':'grow','threw':'throw','drank':'drink','fell':'fall','understood':'understand','lent':'lend','dug':'dig'}
SKIP = set("christmas café cafe tv ok".split()) | set('monday tuesday wednesday thursday friday saturday sunday january february march april may june july august september october november december usa america american english spanish french brazil brazilian mr mrs ms dr ok okay oh hey hi wow yeah yes no'.split())
def base_forms(w):
    yield w
    if w in IRR: yield IRR[w]
    if w.endswith("n't"): yield w[:-3]
    if w.endswith("'s") or w.endswith("'d") or w.endswith("'m"): yield w[:-2]
    if w.endswith("'ll") or w.endswith("'re") or w.endswith("'ve"): yield w[:-3]
    if w == 'café': yield 'cafe'
    if w.endswith('ies'): yield w[:-3] + 'y'
    if w.endswith('es'): yield w[:-2]
    if w.endswith('s'): yield w[:-1]
    if w.endswith('ied'): yield w[:-3] + 'y'
    if w.endswith('ed'): yield w[:-2]; yield w[:-1]
    if w.endswith('ing'): yield w[:-3]; yield w[:-3] + 'e'; 
    if w.endswith('ing') and len(w) > 5 and w[-4] == w[-5]: yield w[:-4]
    if w.endswith('ed') and len(w) > 4 and w[-3] == w[-4]: yield w[:-3]
    if w.endswith('er'): yield w[:-2]; yield w[:-1]
    if w.endswith('est'): yield w[:-3]; yield w[:-2]
    if w.endswith('ly'): yield w[:-2]
def level(w):
    if w in IRR and IRR[w] in W: return W[IRR[w]]
    if w in W: return W[w]
    for b in base_forms(w):
        if b in W: return W[b]
    return None
def names(d):
    s = set()
    for c in d.get('cast', []): s.add(c.lower())
    for k, v in (d.get('dialog', {}).get('speakers') or {}).items(): s.add(k.lower()); s.add((v.get('name') or '').lower())
    s |= {x.lower() for x in re.findall(r'[A-Z][a-z]+', d.get('unit', {}).get('name', ''))}
    return s
def words_of(d):
    out = {}
    nm = names(d)
    def add(txt, src):
        txt = txt.replace('’', "'")
        for m in re.finditer(r"[A-Za-zÀ-ÿ]+(?:'[a-z]+)?", txt):
            w = m.group(0); w2 = w.lower()
            before = txt[:m.start()].rstrip()
            sent_start = (not before) or before[-1] in '.?!“"‘' or before.endswith('**')
            if w[0].isupper() and not sent_start: continue  # nome próprio (Main Street, Ocean Hotel)
            if w2 in nm or w2 in SKIP or (w[0].isupper() and src == 'dialog' and w2 not in W): continue
            out.setdefault(w2, src)
    for l in d['dialog']['lines']: add(l['en'], 'dialog')
    for p in d['pages']:
        if p.get('kind') == 'vocab':
            for x in p.get('words', []): add(x[0], 'vocab')
    return out
def audit(n, d=None):
    d = d or json.load(open(os.path.join(D, 'v4', '%03d.json' % n if n < 1000 else '%d.json' % n), encoding='utf-8'))
    cap = 2 if n >= 2000 else 1; bad = []
    for w, src in words_of(d).items():
        lv = level(w)
        if lv is None:
            if len(w) > 2: bad.append((w, '??', src))
        elif RANK[lv] > cap: bad.append((w, lv, src))
    return bad
if __name__ == '__main__':
    a, b = (int(sys.argv[1]), int(sys.argv[2])) if len(sys.argv) > 2 else (1, 99999)
    tot = 0
    for f in sorted(glob.glob(os.path.join(D, 'v4', '[0-9]*.json'))):
        n = int(re.search(r'(\d+)\.json', f).group(1))
        if not (a <= n <= b): continue
        bad = audit(n); tot += len(bad)
        if bad: print(n, len(bad), ' '.join('%s:%s' % (w, l) for w, l, s in bad[:14]))
    print('total', tot)


def taught_words(d):
    """Palavras ensinadas na própria aula (vocabulário, glossário da leitura, verbos, expressões, ponte)."""
    s = set()
    def add(x):
        for w in re.findall(r"[A-Za-zÀ-ÿ]+(?:'[a-z]+)?", str(x).replace('’', "'")): s.add(w.lower())
    for p in d['pages']:
        k = p.get('kind')
        if k == 'vocab':
            for x in p.get('words', []): add(x[0])
        elif k == 'reading':
            for g in p.get('glossary', []): add(g.get('w', ''))
        elif k == 'verbs':
            for v in p.get('verbs', []):
                add(v.get('v', ''))
                for f in v.get('forms', []): add(f.get('en', ''))
        elif k == 'exprs':
            for e in p.get('items', []): add(e.get('en', ''))
        elif k == 'bridge':
            for w in p.get('words', []): add(w.get('w', ''))
    return s
def violations(n, d=None):
    """Palavras do diálogo acima do nível da aula e que a aula não ensina (regra do projeto)."""
    d = d or json.load(open(os.path.join(D, 'v4', '%03d.json' % n if n < 1000 else '%d.json' % n), encoding='utf-8'))
    cap = 2 if n >= 2000 else 1; t = taught_words(d); out = []
    for w, src in words_of(d).items():
        if src != 'dialog': continue
        lv = level(w)
        if lv is None or RANK[lv] <= cap: continue
        if w in t or any(b in t for b in base_forms(w)): continue
        out.append((w, lv))
    return out
