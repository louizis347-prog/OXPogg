#!/usr/bin/env python3
"""Lições A2 (431–560): prep | dedupe | build.   uso: python3 a2.py prep|dedupe|build"""
import csv, glob, json, os, re, sys
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, '..', '..')
cur = {c['n']: c for f in sorted(glob.glob(H + '/curriculum_a2_*.json')) for c in json.load(open(f))}
ctx = json.load(open(H + '/context_a2.json'))
LOCAL = lambda n: n - 351          # índice dentro do nível A2
st = lambda w: re.sub(r'(ing|ed|es|s)$', '', w.lower())
key = lambda t: st(t) if len(t.split()) == 1 else t.lower()
# primeira lição em que cada estrutura pode aparecer (preenchido a partir do currículo)
FIRSTL = json.load(open(H + '/a2_first.json'))
FIRST = {r: n for r, n, _ in FIRSTL}
LABEL = {r: l for r, _, l in FIRSTL}
def blocks():
    d = {}
    for f in sorted(glob.glob(H + '/out/a2_block*.json')): d.update(json.load(open(f)))
    return d
def fixes():
    d = {}
    for f in sorted(glob.glob(H + '/out/a2_fix*.json')):
        for k, v in json.load(open(f)).items(): d.setdefault(k, {'add': [], 'extras': {}}); d[k]['add'] += v['add']; d[k]['extras'].update(v.get('extras', {}))
    return d
def all_words():
    u = set(ctx['words'])
    for d in blocks().values(): u |= {w[0].lower() for w in d['words']}
    for d in fixes().values(): u |= {w[0].lower() for w in d['add']}
    return u

def prep():
    basew = {n: c['base_words'] for n, c in cur.items()}
    gram = ctx['grammar_a1_1_180'] + [cur[n]['grammar'] for n in sorted(cur)]
    used = sorted(set(ctx['words']) | {w[0].lower() for c in cur.values() for w in c['base_words']})
    json.dump(used, open(H + '/used_words_a2.json', 'w'), ensure_ascii=False)
    pk = []
    ns = sorted(cur)
    a1tail = [w for c in json.load(open(H + '/curriculum_131_180.json'))[-5:] for w in c['base_words']]
    for i, n in enumerate(ns):
        prev = [w for k in ns[max(0, i - 5):i] for w in basew[k]] or a1tail
        pk.append(dict(n=n, level='A2', title=cur[n]['title'], grammar=cur[n]['grammar'], goal=cur[n]['goal'], base_words=cur[n]['base_words'],
            grammar_taught_before=gram[:180 + i], recycle_from_previous=prev, pron_sound=cur[n]['sound'], pron_words=cur[n]['pron_words'],
            mini_story=(n % 10 == 0), not_yet_taught=sorted(LABEL[k] for k, v in FIRST.items() if v > n)))
    for k in range(13): json.dump(pk[k * 10:(k + 1) * 10], open(H + '/in/a2_block%d.json' % (k + 1), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('pacotes', len(pk), 'palavras usadas', len(used))

def dedupe():
    new = blocks(); fix = fixes(); seen = {}; allbase = set()
    ctxw = {st(w) for w in ctx['words'] if len(w.split()) == 1}
    for n, c in cur.items():
        for w in c['base_words']: allbase.add(key(w[0]))
    for k, v in fix.items():
        for t, _ in v['add']: seen.setdefault(key(t), int(k))
    need = []
    byfile = {}
    for f in sorted(glob.glob(H + '/out/a2_block*.json')):
        for k in json.load(open(f)): byfile[k] = f
    cache = {f: json.load(open(f)) for f in set(byfile.values())}
    for n in sorted(cur):
        k = str(n)
        if k not in byfile: continue
        d = cache[byfile[k]][k]; base = {w[0].lower() for w in cur[n]['base_words']}; keep = []
        for t, pt in d['words']:
            kk = key(t)
            if t.lower() in base or ((kk not in seen or seen[kk] == n) and kk not in allbase and not (len(t.split()) == 1 and kk in ctxw)): keep.append([t, pt]); seen.setdefault(kk, n)
        d['words'] = keep
        extra = len(fix.get(k, {}).get('add', []))
        if len(keep) + extra < 8: need.append(dict(n=n, title=cur[n]['title'], grammar=cur[n]['grammar'], need=8 - len(keep) - extra, have=[w[0] for w in keep], reading=[x[0] for x in d['reading']], dialogue=[x[0] for x in d['dialogue']]))
    for f, d in cache.items(): json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(need, open(H + '/in/a2_fix.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(sorted(all_words()), open(H + '/used_all_a2.json', 'w'), ensure_ascii=False)
    print('lições a repor:', len(need), 'itens:', sum(x['need'] for x in need))

KEYS = [('health', 'médic saúde sono academia maratona dor remédio farmácia'), ('notebook', 'livro escola estud prova curso currículo entrevista escritório coworking voluntari carreira aula'),
        ('cup', 'cozinha receita mercado café restaurante jantar comida produtores'), ('ticket', 'trem ônibus viagem voo festival show hospedagem trânsito aplicativo transporte férias'),
        ('park', 'parque jardim trilha natureza acampamento clima ambiente'), ('city', 'banco correio loja apartamento seguro serviço reembolso bairro cidade mudança eletrônicos'),
        ('chat', 'telefone atendimento amigos família festa redes mensagem notícia tecnologia'), ('flag', 'revisão final encerramento')]
def theme_of(t):
    t = t.lower()
    for k, ws in KEYS:
        if any(w in t for w in ws.split()): return k
    return 'map'
def W(s): return re.findall(r"[a-z’']+", s.lower().replace('’', "'"))

def build(force=False):
    new = blocks(); fx = fixes(); errs = []
    def err(n, m): errs.append('L%d: %s' % (n, m))
    for k, v in fx.items():
        if k in new:
            have = {w[0].lower() for w in new[k]['words']}
            new[k]['words'] += [w for w in v['add'] if w[0].lower() not in have]; new[k].setdefault('extras', {}).update(v['extras'])
    seenv = {}
    for n in sorted(cur):
        d = new.get(str(n))
        if not d: err(n, 'ausente'); continue
        if not 8 <= len(d['words']) <= 10: err(n, 'words %d' % len(d['words']))
        terms = [w[0].lower() for w in d['words']]
        for b in cur[n]['base_words']:
            if b[0].lower() not in terms: err(n, 'falta base_word ' + b[0])
        if len(d['reading']) != 6: err(n, 'reading %d' % len(d['reading']))
        if len(d['dialogue']) not in (8, 10): err(n, 'dialogue %d' % len(d['dialogue']))
        lines = [x[0] for x in d['dialogue']]
        if sum(len(W(x)) for x in lines) / max(1, len(lines)) < 6: err(n, 'diálogo curto')
        txt = ' '.join(x[0] for x in d['reading'] + d['dialogue'] + (d.get('story', {}).get('lines') or [])); low = txt.lower().replace('’', "'")
        for t, first in FIRST.items():
            if n < first and re.search(t, low): err(n, 'estrutura antes da hora: ' + t)
        extras = {k.lower() for k in d.get('extras', {})}
        for t in d['words']:
            tm = re.sub(r"[.…?!]+$", '', t[0].lower())
            if tm.replace('…', '') and tm not in low and t[0].lower() not in extras and key(tm) not in {key(x) for x in W(low)}: err(n, 'palavra sem exemplo: ' + t[0])
        for p in cur[n]['pron_words']:
            for w in W(p):
                if not any(x.startswith(w) for x in W(txt)): err(n, 'pron_word ausente: ' + w)
        g = d['grammar']
        if len(g) != 5 or '___' not in g[0]: err(n, 'grammar')
        q = d['quiz']
        if [i['t'] for i in q] != ['c', 'l', 'b', 'b']: err(n, 'quiz tipos')
        for i in q:
            if i['t'] in 'cl' and len(set(i['o'])) != 3: err(n, 'quiz opções')
            if i['t'] == 'c' and '___' not in i['q']: err(n, 'quiz c sem lacuna')
            if i['t'] == 'b' and not 3 <= len(i['w']) <= 9: err(n, 'quiz b tamanho')
        ex = d['examples']; allt = [x[0] for x in d['reading'] + d['dialogue']]
        if len(ex) != 2 or any(not any(e[0] in t for t in allt) for e in ex): err(n, 'examples não copiados do texto')
        if n % 10 == 0 and len((d.get('story') or {}).get('lines', [])) < 8: err(n, 'story')
        base = {w[0].lower() for w in cur[n]['base_words']}
        for t, _ in d['words']:
            if len(t.split()) == 1 and t.lower() not in base:
                kk = st(t)
                if kk in seenv and seenv[kk] != n: err(n, 'vocabulário repetido de L%d: %s' % (seenv[kk], t))
                seenv.setdefault(kk, n)
    ctxw = {st(w) for w in ctx['words'] if len(w.split()) == 1}
    for n in sorted(cur):
        d = new.get(str(n))
        if d:
            for t, _ in d['words']:
                if t.lower() not in {w[0].lower() for w in cur[n]['base_words']} and len(t.split()) == 1 and st(t) in ctxw: err(n, 'palavra já usada no A1: ' + t)
    if errs:
        print('\n'.join(errs)); print(len(errs), 'problemas')
        if not force: sys.exit(1)
    js = lambda x: json.dumps(x, ensure_ascii=False, separators=(', ', ': '))
    out = ['// A2 · lições %d–%d · conteúdo próprio (gerado por tools/a1/a2.py; fontes em tools/a1/out/a2_block*.json).' % (min(cur), max(cur)),
           'const englishA2Plans=[],englishA2Content=[],englishA2MiniStories={},englishA2ExtraWordExamples={},englishA2PhotoThemes=[];']
    rows = []
    for n in sorted(cur):
        d = new[str(n)]; u = LOCAL(n); c0 = cur[n]
        out.append('englishA2Plans[%d]=%s;' % (u, js({'title': c0['title'], 'file': '', 'grammar': c0['grammar'], 'goal': c0['goal'], 'words': d['words']})))
        out.append('englishA2Content[%d]=%s;' % (u, js([d['reading'], d['dialogue'], [c0['sound'], d.get('pron_tip', ''), c0['pron_words']], d['grammar'], d['examples'], d['quiz']])))
        out.append('englishA2PhotoThemes[%d]=%s;' % (u, js(theme_of(c0['title']))))
        if d.get('story'): out.append('englishA2MiniStories[%d]=%s;' % (u, js([d['story']['title'], '|'.join(e + '~' + p for e, p in d['story']['lines'])])))
        if d.get('extras'): out.append('englishA2ExtraWordExamples[%d]=%s;' % (u, js(d['extras'])))
        rows.append([n, 'A2', c0['title'], ' / '.join(a + ' — ' + b for a, b in d['words']), c0['grammar'], c0['goal'], '', 'Sem foto (ilustração do tema)', '', '', '', ''])
    open(R + '/english-a2.js', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    with open(R + '/plano-ingles-a2-431-700.csv', 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, delimiter=';', quoting=csv.QUOTE_ALL)
        w.writerow(['Lição', 'Nível', 'Título', 'Vocabulário inglês — português', 'Gramática', 'Objetivo', 'Imagem', 'Descrição da imagem', 'Autoria', 'Fonte', 'Licença', 'URL da licença']); w.writerows(rows)
    print('gerado', len(rows), 'lições; problemas:', len(errs))

if __name__ == '__main__':
    {'prep': prep, 'dedupe': dedupe, 'build': lambda: build('--force' in sys.argv)}[sys.argv[1]]()
