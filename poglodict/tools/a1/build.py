#!/usr/bin/env python3
"""Valida out/block*.json e gera os arquivos do app (a partir dos originais em orig/): plano, conteúdo, pronúncia e CSV."""
import csv, glob, json, os, re, sys
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, '..', '..')
old = json.load(open(H + '/old.json')); ORDER = json.load(open(H + '/order.json'))
cur = {c['n']: c for c in json.load(open(H + '/curriculum_51_130.json'))}
N = 130 if all(os.path.exists(H + '/out/block%d.json' % k) for k in range(6, 14)) else 50
FIRST2 = {"doesn't": 55, "let's": 70, 'have to': 69, 'has to': 69, 'how much': 61, 'how many': 63, 'how often': 73, 'because': 74, 'whose': 95, 'enough': 101, 'going to': 115, 'was': 117, 'were': 117, "didn't": 121, 'did': 122, 'yesterday': 127, 'ago': 127, 'went': 123, 'bought': 124}
new = {}
for f in sorted(glob.glob(H + '/out/block*.json')): new.update(json.load(open(f)))
for f in sorted(glob.glob(H + '/out/fix*.json')):
    for k, v in json.load(open(f)).items():
        if k in new:
            have = {w[0].lower() for w in new[k]['words']}
            new[k]['words'] += [w for w in v['add'] if w[0].lower() not in have]
            new[k].setdefault('extras', {}).update(v.get('extras', {}))
def W(s): return re.findall(r"[a-z’']+", s.lower().replace('’', "'"))
FIRSTTOK0 = {'would': 7, 'must': 46, 'does': 36, "doesn't": 99, "don't": 19, 'cannot': 28}
FIRSTTOK = dict(FIRSTTOK0); FIRSTTOK.update(FIRST2)
errs = []
def err(n, m): errs.append('L%d: %s' % (n, m))
def check(n, d):
    if n > 50: o = dict(words=cur[n]['base_words'])
    else: o = old['plan'][ORDER[n - 1] - 1]
    if not (8 <= len(d['words']) <= 10): err(n, 'words %d' % len(d['words']))
    terms = [w[0].lower() for w in d['words']]
    for b in o['words']:
        if b[0].lower() not in terms: err(n, 'falta base_word ' + b[0])
    if len(d['reading']) != 6: err(n, 'reading %d' % len(d['reading']))
    if len(d['dialogue']) not in (8, 10): err(n, 'dialogue %d' % len(d['dialogue']))
    lines = [x[0] for x in d['dialogue']]
    avg = sum(len(W(x)) for x in lines) / max(1, len(lines))
    if avg < 5.5: err(n, 'dialogo curto %.1f' % avg)
    txt = ' '.join(x[0] for x in d['reading'] + d['dialogue'] + (d.get('story', {}).get('lines') or []))
    low = txt.lower().replace('’', "'")
    for t, first in FIRSTTOK.items():
        if n < first and (n > 50 or t in FIRSTTOK0) and re.search(r"\b%s\b" % re.escape(t), low): err(n, 'estrutura antes da hora: ' + t)
    if n < 48 and re.search(r"\b(am|is|are|i'm|you're|we're|they're|he's|she's|it's)\s+(\w+ing)\b", low) and not re.search(r"\b(am|is|are|i'm|you're|we're|they're|he's|she's)\s+(morning|evening|building|boring|interesting|amazing|exciting|waiting\b)", low): err(n, 'present continuous antes da hora')
    if re.search(r"\b(did|was|were|went|will|gonna|yesterday)\b" if n < 117 else r"\b(will|gonna)\b", low): err(n, 'passado/futuro')
    for t in d['words']:
        tm = re.sub(r"[.…?!]+$", '', t[0].lower())
        if tm.replace('…', '') and tm not in low.replace('’', "'") and t[0].lower() not in {k.lower() for k in d.get('extras', {})}: err(n, 'palavra sem exemplo: ' + t[0])
    for p in (old['content'][ORDER[n - 1] - 1][2][2] if n <= 50 else cur[n]['pron_words']):
        for w in W(p):
            if w not in W(txt): err(n, 'pron_word ausente: ' + w)
    g = d['grammar']
    if len(g) != 5 or '___' not in g[0]: err(n, 'grammar')
    q = d['quiz']
    if [i['t'] for i in q] != ['c', 'l', 'b', 'b']: err(n, 'quiz tipos')
    for i in q:
        if i['t'] in 'cl' and len(set(i['o'])) != 3: err(n, 'quiz opções')
        if i['t'] == 'c' and '___' not in i['q']: err(n, 'quiz c sem lacuna')
        if i['t'] == 'b' and not (3 <= len(i['w']) <= 9): err(n, 'quiz b tamanho')
    ex = d['examples']; allt = {x[0] for x in d['reading'] + d['dialogue']}
    if len(ex) != 2 or any(not any(e[0] in t for t in allt) for e in ex): err(n, 'examples não copiados do texto')
    if n % 10 == 0 and len((d.get('story') or {}).get('lines', [])) < 8: err(n, 'story')
for n in range(1, N + 1):
    if str(n) not in new: err(n, 'ausente'); continue
    check(n, new[str(n)])
stemw = lambda w: re.sub(r'(ing|ed|es|s)$', '', w)
seenv = {}
for n in range(1, N + 1):
    if str(n) not in new: continue
    for t, _ in new[str(n)]['words']:
        k = stemw(t.lower())
        if len(t.split()) == 1:
            if k in seenv and seenv[k] != n and t.lower() not in {w[0].lower() for w in (old['plan'][ORDER[n - 1] - 1]['words'] if n <= 50 else cur[n]['base_words'])} and abs(seenv[k] - n) > 0 and not any(k == stemw(w[0].lower()) for w in new[str(n)]['words'][:0]): err(n, 'vocabulário repetido de L%d: %s' % (seenv[k], t))
            seenv.setdefault(k, n)
if errs:
    print('\n'.join(errs)); print(len(errs), 'problemas'); 
    if '--force' not in sys.argv: sys.exit(1)
# ---------- gerar arquivos
OR = os.path.join(H, 'orig')
src = lambda n: open(os.path.join(R if n.endswith('.js') else OR, n), encoding='utf-8').read()
js = lambda x: json.dumps(x, ensure_ascii=False, separators=(', ', ': '))
KEYS = [('health', 'farmácia médic dentista consult corte barbearia'), ('notebook', 'livro escola aula arte pintando entrevista escritório reunião'),
        ('cup', 'café sorvete pizza churrasco supermercado cozinha geladeira piquenique alimentação feira café'), ('ticket', 'ônibus táxi aeroporto metrô balão trem escada cinema show teatro'),
        ('park', 'jardim camping trilha zoológico fazenda passeio bicicleta corrida inverno skate piscina'), ('city', 'loja correio lavanderia garagem obra bombeiros floricultura caixa encanador oficina'),
        ('chat', 'família festa colegas videochamada celular wi-fi fotos'), ('flag', 'revisão casamento formatura halloween feriado')]
def theme_of(t):
    t = t.lower()
    for k, ws in KEYS:
        if any(w in t for w in ws.split()): return k
    return 'map'
plan = src('english-a1-plan.js')
lines = []
for n in range(1, N + 1):
    d = new.get(str(n))
    if n <= 50:
        o = old['plan'][ORDER[n - 1] - 1]; ws = d['words'] if d else o['words']; lines.append('|'.join([o['title'], o['file'], o['grammar'], o['goal'], ';'.join('='.join(w) for w in ws)]))
    else:
        c0 = cur[n]; ws = d['words'] if d else c0['base_words']; lines.append('|'.join([c0['title'], '', c0['grammar'], c0['goal'], ';'.join('='.join(w) for w in ws)]))
plan = re.sub(r"(englishA1Plans=`)[\s\S]*?(`\.split)", lambda m: m.group(1) + '\n'.join(lines) + m.group(2), plan, count=1)
bp = '\n'.join(' '.join(old['blockPhotos'][ORDER[n - 1] - 1]) for n in range(1, 51))
plan = re.sub(r"(englishA1BlockPhotoFiles=`)[\s\S]*?(`\.split)", lambda m: m.group(1) + bp + m.group(2), plan, count=1)
open(R + '/english-a1-plan.js', 'w', encoding='utf-8').write(plan)
c = src('english-a1-content.js')
rows = []
for n in range(1, N + 1):
    d = new.get(str(n))
    if n <= 50:
        oc = old['content'][ORDER[n - 1] - 1]
        rows.append('[' + ', '.join(js(x) for x in [d['reading'], d['dialogue'], oc[2], d['grammar'], d['examples'], d['quiz']]) + ']' if d else js(oc))
    else:
        c0 = cur[n]; pron = [c0['sound'], d.get('pron_tip', ''), c0['pron_words']]
        rows.append('[' + ', '.join(js(x) for x in [d['reading'], d['dialogue'], pron, d['grammar'], d['examples'], d['quiz']]) + ']')
c = re.sub(r"(const englishA1Content=\[\n)[\s\S]*?(\n\];)", lambda m: m.group(1) + ',\n'.join(rows) + m.group(2), c, count=1)
st = []
for n in range(10, N + 1, 10):
    d = new.get(str(n))
    if d and d.get('story'): st.append("  %d:[%s,`%s`]" % (n - 1, js(d['story']['title']), '|'.join(e + '~' + p for e, p in d['story']['lines'])))
c = re.sub(r"(const englishA1MiniStories=\{\n)[\s\S]*?(\n\};)", lambda m: m.group(1) + ',\n'.join(st) + m.group(2), c, count=1)
ex = []
for n in range(1, N + 1):
    d = new.get(str(n))
    if d and d.get('extras'): ex.append("  %d:%s" % (n - 1, js(d['extras'])))
c = re.sub(r"(const englishA1ExtraWordExamples=\{\n)[\s\S]*?(\n\};)", lambda m: m.group(1) + ',\n'.join(ex) + m.group(2), c, count=1)
th = [old['themes'][ORDER[n - 1] - 1] for n in range(1, 51)] + [theme_of(cur[n]['title']) for n in range(51, N + 1)]
tt = ',\n'.join('  ' + ','.join("'%s'" % x for x in th[i:i + 10]) for i in range(0, N, 10))
c = re.sub(r"(const englishA1PhotoThemes=\[\n)[\s\S]*?(\n\];)", lambda m: m.group(1) + tt + m.group(2), c, count=1)
open(R + '/english-a1-content.js', 'w', encoding='utf-8').write(c)
pr = [old['pron'][ORDER[n - 1] - 1] for n in range(1, 51)]
open(R + '/a1-pronunciation-data.js', 'w', encoding='utf-8').write('const a1PronunciationLab=[\n' + ',\n'.join(js(r) for r in pr) + '\n];\n')
old_csv = list(csv.reader(open(OR + '/plano-ingles-a1-01-50.csv', encoding='utf-8-sig'), delimiter=';'))
hdr = old_csv[0]; out = [hdr]
for n in range(1, N + 1):
    d = new.get(str(n))
    if n <= 50: r = list(old_csv[ORDER[n - 1]]); r[0] = str(n)
    else: r = [str(n), 'A1', cur[n]['title'], '', cur[n]['grammar'], cur[n]['goal'], '', 'Sem foto (ilustração do tema)', '', '', '', '']
    if d: r[3] = ' / '.join(a + ' — ' + b for a, b in d['words'])
    out.append(r)
with open(R + '/plano-ingles-a1-01-50.csv', 'w', encoding='utf-8-sig', newline='') as f: csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL).writerows(out)
print('gerado', N, 'lições; problemas:', len(errs))
