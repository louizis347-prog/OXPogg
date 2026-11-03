#!/usr/bin/env python3
"""Valida suplementos Quest v5 (src/supp5/sNNN.py) + a aula montada. Uso: validate_v5.py N [N…] | --all"""
import glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build_v5 as B
def wc(t): return len(re.findall(r"[A-Za-z’']+", re.sub(r'\*\*', '', t)))
def mcq(errs, w, q, opts, ans):
    if not (isinstance(opts, list) and len(opts) == 3 and isinstance(ans, int) and 0 <= ans < 3): errs.append(f'{w}: mcq precisa de 3 opções e ans 0-2')
def check(n):
    E = []; S = B.supp(n)
    if not S: return ['sem suplemento']
    r = S.get('reg')
    if not (isinstance(r, int) and 1 <= r <= len(B.EN)): E.append('reg: índice 1..%d do episódio regular' % len(B.EN))
    c = S.get('culture') or {}
    if wc(c.get('hook', '')) < 15: E.append('culture.hook curto (≥15 palavras)')
    if len(c.get('mythfact', [])) < 4: E.append('culture.mythfact ≥4')
    for m in c.get('mythfact', []):
        if not isinstance(m.get('ans'), bool) or not m.get('why'): E.append('mythfact item inválido')
    if not any(m['ans'] for m in c.get('mythfact', [])) or all(m['ans'] for m in c.get('mythfact', []) or [{'ans': True}]): E.append('mythfact precisa de verdadeiros e falsos')
    if len(c.get('wild', [])) < 2: E.append('culture.wild ≥2')
    for w in c.get('wild', []): mcq(E, 'wild.decode', '', (w.get('decode') or {}).get('opts'), (w.get('decode') or {}).get('ans'))
    if not (c.get('compare') or {}).get('br') or not c['compare'].get('us'): E.append('culture.compare br/us')
    if len(c.get('quiz', [])) < 3: E.append('culture.quiz ≥3')
    for q in c.get('quiz', []): mcq(E, 'culture.quiz', q.get('q'), q.get('opts'), q.get('ans'))
    d = S.get('reading') or {}; txt = ' '.join(d.get('text', []))
    if not (170 <= wc(txt) <= 320): E.append('reading.text deve ter 170–320 palavras (tem %d)' % wc(txt))
    if len(d.get('text', [])) < 4: E.append('reading.text ≥4 parágrafos')
    if len(d.get('glossary', [])) < 8: E.append('reading.glossary ≥8')
    for g in d.get('glossary', []):
        if g['w'].lower() not in txt.lower(): E.append('glossary palavra ausente no texto: ' + g['w'])
    f = d.get('fast') or {}; mcq(E, 'reading.fast', f.get('q'), f.get('opts'), f.get('ans'))
    if len(d.get('scan', [])) < 3: E.append('reading.scan ≥3')
    tf = d.get('tf', [])
    if len(tf) < 4 or not any(x['ans'] for x in tf) or all(x['ans'] for x in tf): E.append('reading.tf ≥4 com verdadeiros e falsos')
    if len(d.get('order', [])) != 5: E.append('reading.order exatamente 5 eventos na ordem correta')
    if len(d.get('ctx', [])) < 3: E.append('reading.ctx ≥3')
    for x in d.get('ctx', []):
        mcq(E, 'reading.ctx', x.get('sent'), x.get('opts'), x.get('ans'))
        if x.get('w', '').lower() not in x.get('sent', '').lower(): E.append('ctx.w fora da frase')
    cv = S.get('convo') or {}; t = cv.get('turns', [])
    if len(t) < 4: E.append('convo.turns ≥4')
    for i in t:
        o = i.get('opts', [])
        if len(o) != 3 or sum(1 for x in o if x.get('ok')) != 1: E.append('convo: cada turno com 3 opções e exatamente 1 ok')
        if o and not o[0].get('ok') and False: pass
        for x in o:
            if not x.get('en') or not x.get('pt') or not x.get('fb'): E.append('convo: opção sem en/pt/fb')
    if len(S.get('errors', [])) < 4: E.append('errors ≥4 (wrong/fix/alt/why)')
    if not S.get('homework'): E.append('homework')
    try: B.build(n)
    except Exception as e: E.append('build falhou: %s' % e)
    return E
if __name__ == '__main__':
    a = sys.argv[1:]; ns = sorted(int(os.path.basename(f)[1:4]) for f in glob.glob(os.path.join(HERE, 'supp5', 's[0-9][0-9][0-9].py'))) if '--all' in a else [int(x) for x in a]
    bad = 0
    for n in ns:
        e = check(n)
        if e: bad += 1; print('AULA %d:' % n, *['  - ' + x for x in e[:12]], sep='\n')
    print('ok' if not bad else 'aulas com erro: %d' % bad); sys.exit(1 if bad else 0)
