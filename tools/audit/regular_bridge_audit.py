#!/usr/bin/env python3
"""Auditoria de PADRÃO e PONTE OBRA↔EPISÓDIO dos cursos regulares, medida contra os episódios de referência do inglês A1 (n 7009801, 70001, 7070001, 30001).
Uso: python3 tools/audit/regular_bridge_audit.py [curso ...] [--lista curso]   (padrão: en-a1 en-a2 en-b1 en-b2; ignora os 5 primeiros do curso)
Ponte obra↔episódio (o que os episódios de referência fazem):
 P1 elenco = personagens da obra (nome do elenco aparece no título/descrição da obra, na fonte do gancho ou na figurinha)
 P2 a obra aparece DENTRO das cenas (palavra do título ou personagem da obra numa fala da cena 1 ou 2)
 P3 a 1ª missão se chama “Cena da obra” e o enunciado/modelo cita personagem ou palavra da obra
 P4 o gancho da capa é a 1ª fala da cena 1 e a fonte (h.src) é a obra do episódio
 P5 a figurinha do fechamento mostra a obra do episódio e o elenco
 P6 a descrição da obra (a.d) existe, em português, com 2+ frases curtas ou 1 frase longa
Padrão/densidade: D1 cenário (rs) nunca igual ao do quadro anterior; D2 5 objetos clicáveis em posições distintas; D3 todo quadro tem `say`;
 D4 teaser aponta para o próximo episódio; D5 mochila é do episódio anterior; D6 sem elenco genérico (Woman/Man/Girl/Boy…)."""
import glob, json, os, re, sys, unicodedata
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'plan'))
import plan_lib as P

REF = {7009801, 70001, 7070001, 30001}
GEN = {'woman', 'man', 'girl', 'boy', 'mother', 'father', 'teacher', 'student', 'friend', 'customer', 'waiter', 'clerk', 'lady', 'guy', 'person', 'mulher', 'homem'}
STOP = {'the', 'and', 'with', 'from', 'that', 'this', 'filme', 'livro', 'série', 'serie', 'peça', 'poema', 'música', 'musica', 'quadro', 'jogo', 'uma', 'esta', 'este', 'essa', 'esse', 'aula', 'cena', 'onde', 'como', 'para', 'sobre', 'mais', 'muito', 'entre', 'depois', 'antes', 'quando', 'também', 'tambem', 'ainda', 'cada', 'seus', 'suas', 'dele', 'dela', 'obra', 'história', 'historia', 'sendo', 'pelo', 'pela', 'foram', 'desde', 'após'}
fold = P.fold


def toks(s, mn=4):
    return {t for t in fold(s).split() if len(t) >= mn and t not in STOP}


def caps(s):
    return {fold(t) for t in re.findall(r"\b[A-ZÀ-Ý][\wÀ-ÿ'’-]{3,}", s or '')} - STOP


def scenes(e):
    return [f for f in e['fr'] if f['k'] == 'pgscene']


def check(e, prev, nxt):
    fr = {}
    for f in e['fr']:
        fr.setdefault(f['k'], []).append(f)
    a = e.get('a') or {}
    w = a.get('w', '')
    title = re.sub(r'\(.*?\)', '', w)
    work_words = toks(title) | caps(a.get('d', '')) | toks((e.get('h') or {}).get('src', ''))
    sc = scenes(e)
    cast = list((sc[0].get('cast') or {}).keys()) if sc else []
    lines = ' '.join(l[1] for s in sc for l in s.get('lines', []))
    lines_f = fold(lines)
    r = {}
    castn = {fold(c) for c in cast}
    obra_txt = fold(w + ' ' + a.get('d', '') + ' ' + (e.get('h') or {}).get('src', '') + ' ' + json.dumps(((fr.get('wrap') or [{}])[0].get('sticker') or {}), ensure_ascii=False))
    r['P1'] = bool(castn) and any(c and c in obra_txt for c in castn) and not (castn & GEN)
    cast_obra = {c for c in castn if c and c in obra_txt}
    r['P2'] = any(t in lines_f.split() or t in lines_f for t in (work_words | cast_obra) if len(t) >= 4)
    ms = (fr.get('pgmission') or [{}])[0].get('missions') or [{}]
    m_txt = fold(json.dumps([m.get('data', {}) for m in ms], ensure_ascii=False))
    r['P3'] = fold((ms[0] if ms else {}).get('name', '')) == 'cena da obra' and (any(c in m_txt for c in castn if c) or any(t in m_txt for t in work_words))
    g = (fr.get('cover') or [{}])[0].get('gancho') or []
    l0 = (sc[0].get('lines') or [[]])[0] if sc else []
    r['P4'] = bool(g) and P.norm((e.get('h') or {}).get('src')) == P.norm(title)
    st = (fr.get('wrap') or [{}])[0].get('sticker') or {}
    r['P5'] = bool(st.get('chars')) and (P.norm(title) in P.norm(st.get('sub', '') + ' ' + st.get('title', '')) or P.norm(title) in P.norm(st.get('sub', '').split(' · ')[0]))
    d = a.get('d', '')
    r['P6'] = len(d) >= 90
    rss = [f.get('rs') for f in e['fr'] if f.get('rs')]
    r['D1'] = all(not (x == y == z) for x, y, z in zip(rss, rss[1:], rss[2:]))
    hot = (fr.get('hotscene') or [{}])[0].get('hot') or []
    r['D2'] = len(hot) == 5 and len({(h['x'], h['y']) for h in hot}) == 5
    r['D3'] = all((f.get('say') or f['k'] in ('pgscene', 'review', 'pgsheet', 'cover', 'wrap')) for f in e['fr'])
    tz = (fr.get('wrap') or [{}])[0].get('teaser') or {}
    nw = toks(re.sub(r'\(.*?\)', '', (nxt.get('a') or {}).get('w', '')), 3) if nxt else set()
    r['D4'] = (nxt is None) or bool(fold(tz.get('t', '')) and ((set(fold(tz.get('t', '')).split()) | set(fold(tz.get('d', '')).split())) & (toks(nxt['t'], 3) | nw | toks(nxt.get('gs') or '', 4))))
    rv = (fr.get('review') or [{}])[0]
    r['D5'] = prev is None or (rv.get('prev') == prev['t'])
    r['D6'] = not (castn & GEN)
    return r


def main():
    args = [x for x in sys.argv[1:] if not x.startswith('--')]
    courses = args or ['en-a1', 'en-a2', 'en-b1', 'en-b2']
    lista = '--lista' in sys.argv
    out = {}
    for c in courses:
        eps = [e for e in P.load_course(c) if e.get('presentation') == 'regular-pilot-v1']
        res = {}
        for i, e in enumerate(eps):
            prev = eps[i - 1] if i else None
            nxt = eps[i + 1] if i + 1 < len(eps) else None
            res[e['n']] = check(e, prev, nxt)
        ref = {n: v for n, v in res.items() if n in REF}
        body = [v for i, (n, v) in enumerate(res.items()) if i >= 5 and n not in REF]
        keys = list(next(iter(res.values())).keys())
        rate = {k: round(100 * sum(v[k] for v in body) / max(1, len(body)), 1) for k in keys}
        out[c] = dict(n=len(body), rate=rate, ref={n: [k for k, v in r.items() if not v] for n, r in ref.items()},
                      weak={n: [k for k in keys if not v[k]] for n, v in list(res.items())[5:] if n not in REF and any(not v[k] for k in keys if k.startswith('P'))})
        print('%s: %d episódios (do 6º em diante)' % (c, len(body)))
        print('   ' + '  '.join('%s %s%%' % (k, rate[k]) for k in keys))
        if ref: print('   referências com falha:', {n: f for n, f in out[c]['ref'].items() if f} or 'nenhuma')
        if lista:
            for n, f in list(out[c]['weak'].items())[:40]: print('   fraco', n, f)
    json.dump(out, open(os.path.join(ROOT, 'tools', 'audit', 'regular_bridge_audit.json'), 'w'), ensure_ascii=False)


main()
