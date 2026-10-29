#!/usr/bin/env python3
"""Confere um lote de trocas de obra de aulas genéricas (tools/generic/out/<lote>.json) SEM gravar em data/.
Uso: python3 tools/generic/check.py <lote> [<lote> ...]   (obra única em todo o inglês regular e entre lotes; descrição com ponte; ficha válida e única)"""
import glob, importlib.util, json, os, re, sys, unicodedata
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'ficha'))
spec = importlib.util.spec_from_file_location('fv', os.path.join(ROOT, 'tools', 'ficha', 'validate.py')); fv = importlib.util.module_from_spec(spec); spec.loader.exec_module(fv)
STOP = {'the', 'a', 'an', 'of', 'o', 'os', 'as', 'de', 'do', 'da', 'dos', 'das', 'e', 'and', 'la', 'le', 'el', 'tower', 'museum', 'film', 'in', 'on', 'to', 'for', 'at'}
MARKER = re.compile(r"A referência\s+\S")

def fold(s):
    s = unicodedata.normalize('NFKD', (s or '').split(':')[0].lower()); return ''.join(c for c in s if not unicodedata.combining(c))
def norm(s):
    s = re.sub(r'\(.*?\)', '', fold(s)); s = re.sub(r'[^a-z0-9 ]', ' ', s); s = re.sub(r'^(the|a|an|el|la|le|o|os)\s+', '', s.strip()); return ' '.join(s.split())
def toks(s): return {t for t in re.findall(r'[a-z0-9]+', norm(s)) if t not in STOP}
def similar(a, b):
    ta, tb = toks(a), toks(b)
    if not ta or not tb: return norm(a) == norm(b)
    if min(len(ta), len(tb)) < 2: return ta == tb
    return ta <= tb or tb <= ta

def load_out(lote): return json.load(open(os.path.join(ROOT, 'tools', 'generic', 'out', lote + '.json'), encoding='utf-8'))

def main(lotes):
    mine = {}
    for l in lotes:
        for n, x in load_out(l).items(): mine[int(n)] = (l, x)
    others = set()  # n de outros lotes já entregues (para cruzar obras/fichas)
    for f in glob.glob(os.path.join(ROOT, 'tools', 'generic', 'out', '*.json')):
        l = os.path.basename(f)[:-5]
        if l in lotes: continue
        for n, x in json.load(open(f, encoding='utf-8')).items(): others.add((int(n), x['obra']['nome'], json.dumps(x['ficha'])))
    works = {}
    for f in glob.glob(os.path.join(ROOT, 'data', 'en-*_*.json')):
        for e in json.load(open(f, encoding='utf-8')):
            if e['n'] not in mine: works[e['n']] = e['a']['w']
    for n, w, _ in others:
        if n not in mine: works['o%d' % n] = w
    brief = {}
    for l in lotes:
        for a in json.load(open(os.path.join(ROOT, 'tools', 'generic', 'lotes', l + '.json'), encoding='utf-8'))['alvo']: brief[a['n']] = a
    problems = []
    names = {}
    for n, (l, x) in sorted(mine.items()):
        if n not in brief: problems.append('%s: n=%s não pertence ao lote' % (l, n)); continue
        w = x['obra']['nome'].strip()
        if not w or not x['obra'].get('tipo') or not x['obra'].get('ano'): problems.append('%s: obra incompleta' % n)
        if fold(w) == fold(brief[n]['obra_atual']): problems.append('%s: obra não mudou' % n)
        for k, ow in works.items():
            if norm(w) == norm(ow) or similar(w, ow): problems.append('%s: obra “%s” já usada/parecida com “%s” (%s)' % (n, w, ow, k)); break
        for m, ow in names.items():
            if norm(w) == norm(ow) or similar(w, ow): problems.append('%s: obra “%s” repetida/parecida no lote com %s “%s”' % (n, w, m, ow))
        names[n] = w
        if not MARKER.search(x.get('desc', '')) or w not in x['desc']: problems.append('%s: desc precisa conter “A referência %s …”' % (n, w))
        f = x.get('ficha') or {}
        for e in fv.check(n, f): problems.append('%s: ficha: %s' % (n, e))
    # fichas únicas contra TODAS as existentes e contra os outros lotes
    sig = {}
    for fn in sorted(glob.glob(os.path.join(ROOT, 'tools', 'ficha', 'work', '*_*.json'))):
        for n, f in json.load(open(fn, encoding='utf-8')).items():
            if int(n) in mine or f.get('conflito'): continue
            try: sig[fv.signature(f)] = ('ficha existente', n)
            except Exception: pass
    for n, w, fj in others:
        try: sig[fv.signature(json.loads(fj))] = ('outro lote', n)
        except Exception: pass
    for n, (l, x) in sorted(mine.items()):
        try: s = fv.signature(x['ficha'])
        except Exception: continue
        if s in sig: problems.append('%s: ficha repete elenco+objeto+cenário de %s %s' % (n, *sig[s]))
        sig[s] = ('este lote', n)
    print('episódios:', len(mine), '| problemas:', len(problems))
    for p in problems: print(' -', p)
    return 1 if problems else 0

if __name__ == '__main__': sys.exit(main(sys.argv[1:]))
