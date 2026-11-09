"""Enriquece as aulas Quest (data/v4/NNN.json) com o que veio do curso "Inglês do zero ao C2":
- data/v4/vocabx.json: classe, IPA (CMUdict), famílias e colocações por palavra;
- novas telas (marcadas x:1, idempotente): famílias e colocações, foto→palavra, complete a frase, sinônimo/oposto,
  palavra que não combina, armadilha de tradução, "qual frase está correta?";
- registro (formal/neutro/informal) nas expressões.
O laboratório de sons NÃO é tocado.
Uso: python3 quest_enrich.py [pasta com c*.json dos agentes]"""
import glob, hashlib, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
sys.path.insert(0, os.path.join(HERE, 'livro', 'tools'))
import ipa as IPA
V4 = os.path.join(ROOT, 'data', 'v4')
X = os.path.join(ROOT, 'data', 'v4x'); os.makedirs(X, exist_ok=True)
PHOTOS = set(f[:-4] for f in os.listdir(os.path.join(ROOT, 'img', 'livro', 'palavras')) if f.endswith('.jpg'))
def slug(w): return re.sub(r'^-|-$', '', re.sub(r'[^a-z0-9]+', '-', w.lower().replace('’', '').replace("'", '')))
def h(*a): return int(hashlib.md5('|'.join(map(str, a)).encode()).hexdigest()[:8], 16)
def shuffle(opts, correct, seed):
    o = list(opts); k = h(seed) % len(o)
    o = o[k:] + o[:k]
    # garante a resposta em posição variada
    i = o.index(correct); want = h(seed, 'p') % len(o)
    o[i], o[want] = o[want], o[i]
    return o, o.index(correct)

# 1) extras dos agentes -> data/v4x/extra.json
if len(sys.argv) > 1:
    ex = {}
    for f in sorted(glob.glob(os.path.join(sys.argv[1], 'c*.json'))):
        try: d = json.load(open(f))
        except Exception as e: print('JSON inválido', f, e); continue
        for n, v in d.items():
            if isinstance(v, dict): ex[str(int(n))] = v
    json.dump(ex, open(os.path.join(X, 'extra.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
    print('extras:', len(ex), 'aulas')
EXTRA = json.load(open(os.path.join(X, 'extra.json'))) if os.path.exists(os.path.join(X, 'extra.json')) else {}

# 2) metadados de palavras (livro + CMUdict)
LV = {}
for f in glob.glob(os.path.join(ROOT, 'data', 'livro', 'vocab', '*.json')):
    d = json.load(open(f))
    for w, it in d['items'].items():
        e = LV.setdefault(w.lower(), {})
        if it.get('pos') and 'p' not in e: e['p'] = it['pos']
        for a, b in d.get('family', []):
            if a.lower() == w.lower() and 'f' not in e: e['f'] = b
        for ph, tr in d.get('colloc', []):
            if re.search(r'\b' + re.escape(w.lower()) + r'\b', ph.lower()) and 'c' not in e: e['c'] = [ph, tr]
VX = {}
files = sorted(glob.glob(os.path.join(V4, '[0-9]*.json')))
LES = {}
for f in files:
    d = json.load(open(f)); LES[d['n']] = (f, d)
    for p in d['pages']:
        if p['kind'] == 'vocab':
            for w in p['words']:
                k = w[0].lower(); e = dict(LV.get(k, {}))
                i = IPA.ipa(w[0])
                if i: e['i'] = i
                if e: VX[k] = e
json.dump(VX, open(os.path.join(V4, 'vocabx.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
print('vocabx:', len(VX), 'palavras | com classe:', sum('p' in v for v in VX.values()), '| com IPA:', sum('i' in v for v in VX.values()),
      '| com família:', sum('f' in v for v in VX.values()), '| com colocação:', sum('c' in v for v in VX.values()))

# 3) telas novas
st = dict(added=0, lessons=0)
def blank(sentence, word):
    m = re.search(re.escape(word), sentence, re.I)
    return (sentence[:m.start()] + '_____' + sentence[m.end():]) if m else None
for n, (f, d) in sorted(LES.items()):
    pages = [p for p in d['pages'] if not p.get('x')]
    words = []
    for p in pages:
        if p['kind'] == 'vocab': words += p['words']
    names = [w[0] for w in words]
    ext = EXTRA.get(str(n), {})
    new_after_vocab, new_trap, new_fix = [], [], []
    base = lambda title, kind='quiz', stage='lab': {'t': 'q1', 'stage': stage, 'kind': kind, 'title': title, 'x': 1}
    # famílias e colocações
    rows = [(w[0], VX[w[0].lower()]) for w in words if w[0].lower() in VX and ('f' in VX[w[0].lower()] or 'c' in VX[w[0].lower()])]
    if len(rows) >= 2:
        pg = base('Famílias e colocações', 'famcol'); pg['rows'] = [{'w': w, 'f': e.get('f'), 'c': e.get('c')} for w, e in rows[:4]]
        new_after_vocab.append(pg)
    # foto -> palavra
    ph = [w for w in words if slug(w[0]) in PHOTOS]
    if len(ph) >= 3 and len(names) >= 4:
        items = []
        for i, w in enumerate(ph[:4]):
            others = [x for x in names if x != w[0]][:]; others = sorted(others, key=lambda x: h(n, i, x))[:3]
            opts, ans = shuffle([w[0]] + others, w[0], (n, 'img', i))
            items.append({'q': 'Qual palavra combina com a foto?', 'img': 'palavras/' + slug(w[0]) + '.jpg', 'opts': opts, 'ans': ans, 'why': w[0] + ' = ' + w[1] + '.'})
        pg = base('Associe a foto à palavra'); pg['instruction'] = 'Olhe a foto e escolha a palavra certa.'; pg['items'] = items
        new_after_vocab.append(pg)
    # complete a frase
    items = []
    for i, w in enumerate(words):
        s = w[2] if len(w) > 2 else ''
        b = blank(s, w[0]) if s else None
        if not b: continue
        others = sorted([x for x in names if x != w[0]], key=lambda x: h(n, i, x, 'g'))[:3]
        if len(others) < 2: continue
        opts, ans = shuffle([w[0]] + others, w[0], (n, 'gap', i))
        items.append({'q': b, 'opts': opts, 'ans': ans, 'why': w[0] + ' = ' + w[1] + '. Frase completa: ' + s})
        if len(items) == 5: break
    if len(items) >= 3:
        pg = base('Complete a frase'); pg['instruction'] = 'Escolha a palavra que completa cada frase.'; pg['items'] = items
        new_after_vocab.append(pg)
    # sinônimo / oposto
    syn = [s for s in ext.get('syn', []) if isinstance(s, list) and len(s) >= 3]
    if len(syn) >= 2:
        pool = [s[1] for s in syn] + names
        items = []
        for i, s in enumerate(syn[:4]):
            a, b, kind = s[0], s[1], s[2]
            dis = sorted([x for x in pool if x.lower() not in (b.lower(), a.lower())], key=lambda x: h(n, i, x, 's'))[:2]
            opts, ans = shuffle([b] + dis, b, (n, 'syn', i))
            q = ('Which word is the opposite of “%s”?' if kind == 'ant' else 'Which word means almost the same as “%s”?') % a
            items.append({'q': q, 'opts': opts, 'ans': ans, 'why': '“%s” e “%s” são %s.' % (a, b, 'opostas' if kind == 'ant' else 'parecidas')})
        pg = base('Palavra parecida ou oposta?'); pg['instruction'] = 'Pense no significado.'; pg['items'] = items
        new_after_vocab.append(pg)
    # palavra que não combina
    cl = ext.get('classify') or {}
    A, B = cl.get('A') or [], cl.get('B') or []
    if len(A) >= 3 and len(B) >= 2:
        items = []
        for i in range(min(3, len(B))):
            trio = sorted(A, key=lambda x: h(n, i, x, 'c'))[:3]
            odd = B[i]
            opts, ans = shuffle(trio + [odd], odd, (n, 'odd', i))
            items.append({'q': 'Which word does not belong with the others?', 'opts': opts, 'ans': ans, 'why': 'As outras três são do tema: %s.' % cl.get('title', 'a aula')})
        pg = base('Qual palavra não combina?'); pg['instruction'] = 'Três palavras são do mesmo tema. Ache a diferente.'; pg['items'] = items
        new_after_vocab.append(pg)
    # armadilha de tradução
    tr = ext.get('trap')
    if isinstance(tr, dict) and tr.get('wrong') and tr.get('right') and tr.get('why'):
        pg = base('Armadilha de tradução', 'trap'); pg['trap'] = {k: tr.get(k, '') for k in ('label', 'wrong', 'right', 'why')}
        new_trap.append(pg)
    # qual frase está correta
    fx = [q for q in ext.get('fix', []) if isinstance(q, dict) and isinstance(q.get('opts'), list) and len(q['opts']) == 3 and isinstance(q.get('ans'), int) and 0 <= q['ans'] < 3]
    if len(fx) >= 2:
        pg = base('Qual frase está correta?', 'quiz', 'arcade'); pg['instruction'] = 'Só uma frase está correta. Procure o erro típico.'
        pg['items'] = [{'q': q.get('q', 'Which sentence is correct?'), 'opts': q['opts'], 'ans': q['ans'], 'why': q.get('why', '')} for q in fx[:3]]
        new_fix.append(pg)
    # registro nas expressões
    reg = ext.get('reg') or {}
    for p in pages:
        if p['kind'] == 'exprs':
            for it in p['items']:
                r = reg.get(it['en']) or reg.get(it['en'].strip())
                if r in ('formal', 'neutro', 'informal'): it['reg'] = r
    # monta a ordem
    out = []; last_vocab = max([i for i, p in enumerate(pages) if p['kind'] == 'vocab'], default=-1)
    last_exprplay = max([i for i, p in enumerate(pages) if p['kind'] == 'exprplay'], default=-1)
    last_arcade = max([i for i, p in enumerate(pages) if p['stage'] == 'arcade'], default=-1)
    for i, p in enumerate(pages):
        out.append(p)
        if i == last_vocab: out += new_after_vocab
        if i == last_exprplay: out += new_trap
        if i == last_arcade: out += new_fix
    if last_vocab < 0: out = pages
    added = len(out) - len(pages)
    d['pages'] = out
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    st['added'] += added; st['lessons'] += bool(added)
print('telas novas:', st['added'], 'em', st['lessons'], 'aulas')
