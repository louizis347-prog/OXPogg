#!/usr/bin/env python3
"""Aplica (ou só valida) os patches de PONTE obra↔episódio em data/. Idempotente: pode ser reaplicado depois de qualquer reconstrução dos dados.
Patches: tools/audit/bridge_patches/<curso>_<parte>.json = lista de
  {"n": 7010178,
   "cena": [{"cena": 1, "i": 3, "en": "...", "pt": "..."}],        # troca a fala i (0-based) da cena 1 ou 2; o falante e o resto da cena ficam
   "missao": {"prompt": "...", "model": "...", "chips": ["..."], "check": [3 textos], "kw": [3 regex], "tips": [[[en, pt], ...], x3], "ok": [3], "reply": [en, pt]}}
Uso: python3 tools/audit/apply_bridge_patches.py [--check] [arquivo.json ...]   (--check não grava)"""
import glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'plan'))
import plan_lib as P
fold = P.fold
STOP = {'the', 'and', 'with', 'from', 'that', 'this', 'filme', 'livro', 'série', 'serie', 'peça', 'poema', 'música', 'musica', 'quadro', 'jogo', 'uma', 'esta', 'este', 'essa', 'esse', 'aula', 'cena', 'onde', 'como', 'para', 'sobre', 'mais', 'muito', 'entre', 'depois', 'antes', 'quando', 'obra'}


def work_words(e):
    a = e.get('a') or {}
    title = re.sub(r'\(.*?\)', '', a.get('w', ''))
    caps = {fold(t) for t in re.findall(r"\b[A-ZÀ-Ý][\wÀ-ÿ'’-]{3,}", a.get('d', ''))}
    w = {t for t in fold(title).split() if len(t) >= 4} | caps | {t for t in fold((e.get('h') or {}).get('src', '')).split() if len(t) >= 4}
    return {x for x in w if x not in STOP}


def validar(e, p):
    erros = []
    ww = work_words(e)
    fr = {}
    for f in e['fr']:
        fr.setdefault(f['k'], []).append(f)
    scs = fr['pgscene']
    ws = ww | {fold(c) for c in (scs[0].get('cast') or {})}
    for c in p.get('cena', []):
        s = scs[c['cena'] - 1]
        if not 0 <= c['i'] < len(s['lines']):
            erros.append('índice de fala fora da cena'); continue
        old = s['lines'][c['i']][1]
        txt = fold(c['en'])
        if not any(t in txt.split() or t in txt for t in ws):
            erros.append('a fala nova não cita a obra/personagem: ' + c['en'])
        quoted = ' '.join(json.dumps(x, ensure_ascii=False) for f in fr.get('pgsheet', []) for x in f.get('items', []))
        if old and old in quoted and old != c['en']:
            erros.append('a fala trocada é citada em perguntas (“why”): ' + old)
    m = p.get('missao')
    if m:
        txt = fold(m['prompt'] + ' ' + m['model'])
        if not any(t in txt for t in ws):
            erros.append('a missão não cita a obra/personagem')
        kw = m.get('kw', [])
        if len(kw) != 3 or len(m.get('check', [])) != 3 or len(m.get('tips', [])) != 3 or len(m.get('ok', [])) != 3:
            erros.append('missão precisa de 3 check, 3 kw, 3 tips e 3 ok')
        for k in kw:
            try:
                if not re.search(k, m['model'], re.I):
                    erros.append('kw não casa com o modelo: ' + k)
            except re.error as x:
                erros.append('regex inválida: %s' % x)
        if not any(re.search(k, m['model'], re.I) for k in kw[:1]):
            pass
    return erros


def main():
    check = '--check' in sys.argv
    files = [a for a in sys.argv[1:] if not a.startswith('--')] or sorted(glob.glob(os.path.join(HERE, 'bridge_patches', '*.json')))
    patches = {}
    for f in files:
        for p in json.load(open(f, encoding='utf-8')):
            patches[p['n']] = p
    datafiles = sorted(glob.glob(os.path.join(ROOT, 'data', 'en-*_*.json')))
    done = 0; bad = 0
    for df in datafiles:
        d = json.load(open(df, encoding='utf-8')); ch = False
        for e in d:
            p = patches.get(e['n'])
            if not p:
                continue
            erros = validar(e, p)
            if erros:
                bad += 1
                print('ERRO n=%s: %s' % (e['n'], '; '.join(erros)))
                continue
            scs = [f for f in e['fr'] if f['k'] == 'pgscene']
            for c in p.get('cena', []):
                ln = scs[c['cena'] - 1]['lines'][c['i']]
                scs[c['cena'] - 1]['lines'][c['i']] = [ln[0], c['en'], c['pt']]
            if p.get('missao'):
                mi = [f for f in e['fr'] if f['k'] == 'pgmission'][0]['missions'][0]
                m = p['missao']
                mi['name'] = 'Cena da obra'
                mi['desc'] = m.get('desc') or mi.get('desc')
                dd = mi['data']
                for k in ('prompt', 'model', 'chips', 'check', 'kw', 'tips', 'ok', 'reply'):
                    if k in m:
                        dd[k] = m[k]
            e['ponte'] = 1
            ch = True; done += 1
        if ch and not check:
            open(df, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
    print('patches:', len(patches), '| aplicados%s:' % (' (simulado)' if check else ''), done, '| com erro:', bad)
    sys.exit(1 if bad else 0)


main()
