#!/usr/bin/env python3
"""Constrói os episódios do A1 de inglês no modelo "padrão do dia em uma obra" a partir de especificações compactas.

Cada lote (tools/a1_gen/batch_XX.py) define EPS = [ dict(B=…, X=…, XT=…, VB=…, MR=…, CX=…), … ] na ordem do curso.
O primeiro episódio do primeiro lote tem como "anterior" o episódio piloto 5; os demais encadeiam entre si.
  python3 tools/a1_gen/make.py --check            # só valida os lotes
  python3 tools/a1_gen/make.py                    # valida e grava em data/en-a1_NN.json
"""
import glob, importlib.util, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import model_v2 as M  # noqa: E402
from model_v2_data import V2  # noqa: E402
from model_v2_extra import EXTRA, VERBS  # noqa: E402
import model_v3 as M3  # noqa: E402

OLD_RS = 'cafe living market airport lobby station subway park pier lake nyc flags cafe2 airport2 lobby1 lobby2 sub2 tick cafe3 diner home1 yard park2 school shop office clinic kitchen bedroom bath counter gym hall street'.split()
NEW_RS = 'beach zoo farm playground busstop bakery supermarket bookshop postoffice bank pharmacy restaurant hotelroom mountain forest snow stage library museum castlehall garden fair pool stadium harbor chefkitchen musicroom traincar soccerfield fishing artroom nightcity meetingroom christmas'.split()
RS = set(OLD_RS + NEW_RS)
NAMED = set('bear mrs alice rabbit cat dorothy scarecrow lion wendy peter tinker hook cowboy ranger polly tommy oliver bumble ishmael ahab townmouse countrymouse mary lamb shepherd wolf matilda misshoney jack jill tom huck peterrabbit mcgregor kittenA kittenB dartagnan athos slugger coach tokio rio quijote sancho chavo florinda petitprince pilote asterix obelix linguini remy'.split())
RSK = 'review dquiz rdg pat vplay build order soundlab produce wrap dictate'.split()


class V(Exception):
    pass


def need(c, msg=""):
    if not c:
        raise V(msg)


def pair(x, what):
    need(isinstance(x, (list, tuple)) and len(x) >= 2 and all(isinstance(i, str) for i in x[:2]), what + ' deve ser [en, pt]')


def charid(c, what):
    need(c in NAMED or re.fullmatch(r'p:(short|long|bun|curly|bald|cap):[0-9a-fA-F]{6}:[0-9a-fA-F]{6}:[0-9a-fA-F]{6}:(none|glasses|hat|crown|scarf|beard|bow):(shirt|dress|suit)', c) or re.fullmatch(r'e:\S', c) or c.startswith('e:'), what + ': personagem inválido ' + repr(c))


def chars(cs, what):
    need(isinstance(cs, list) and cs, what + ' vazio')
    for c in cs:
        need(len(c) == 4, what + ': cada personagem é [id, x%, espelhar, escala]')
        charid(c[0], what)


def opts_ok(o, a, n, what, pic=False):
    need(isinstance(o, list) and len(o) == n, '%s: precisa de %d opções' % (what, n))
    need(isinstance(a, int) and 0 <= a < n, what + ': índice da resposta inválido')
    for x in o:
        if pic:
            need(isinstance(x, list) and len(x) == 2, what + ': opções são [emoji, texto]')
        else:
            need(isinstance(x, str) and x, what + ': opção vazia')
    need(len({json.dumps(x, ensure_ascii=False) for x in o}) == n, what + ': opções repetidas')


def validate(S, i):
    B, X, XT, VB, MR, CX = (S[k] for k in ('B', 'X', 'XT', 'VB', 'MR', 'CX'))
    w = 'ep%s' % X.get('n')
    for k in ('title', 'sub', 'pattern_label', 'why', 'cover_sub', 'cover_say'):
        need(isinstance(B.get(k), str) and B[k], w + ' B.' + k)
    need(len(B['vocab']) >= 6 and all(len(v) == 3 for v in B['vocab']), w + ' B.vocab: >=6 itens [palavra, pt, nota]')
    need(len(B['balloons']) >= 6 and all(len(v) == 2 for v in B['balloons']), w + ' B.balloons: >=6 [emoji, palavra]')
    need(isinstance(B['cover_art'], dict) and 'items' in B['cover_art'], w + ' B.cover_art')
    need(len(B['wrap_recap']) == 4, w + ' B.wrap_recap: 4 pares')
    for p in B['wrap_recap']: pair(p, w + ' wrap_recap')
    need(set(B['teaser']) >= {'t', 'd'}, w + ' B.teaser')
    cast = B['cast']
    need(isinstance(cast, dict) and len(cast) >= 2, w + ' B.cast')
    need(8 <= len(B['lines']) <= 10, w + ' B.lines: 8 a 10 falas')
    for l in B['lines']:
        need(len(l) == 3 and l[0] in cast, w + ' B.lines: [quem, en, pt] com quem em cast: %r' % (l,))
    need(len(B['quiz']) == 3, w + ' B.quiz: 3 perguntas')
    for q in B['quiz']:
        opts_ok(q['opts'], q['a'], 3, w + ' quiz', pic=True)
        need(q['q'] and q['pt'] and q['why'], w + ' quiz campos')
    r = B['rdg_q']; need(set(r) >= {'q', 'o', 'a', 'why'}, w + ' rdg_q'); opts_ok(r['o'], r['a'], 3, w + ' rdg_q')
    need(len(B['dictate']) >= 3, w + ' B.dictate >=3')
    for p in B['dictate']: pair(p, w + ' dictate')
    P = B['produce']
    need(set(P) >= {'prompt', 'ph', 'chips', 'model', 'check', 'kw', 'tips', 'ok', 'reply'}, w + ' produce chaves')
    need(len(P['check']) == len(P['kw']) == len(P['tips']) == len(P['ok']) == 3, w + ' produce: check/kw/tips/ok com 3 itens')
    for k in P['kw']: re.compile(k, re.I)
    need(P['model'] and any(re.search(k, P['model'], re.I) for k in P['kw']), w + ' produce: o texto-modelo deve passar nos regex kw')
    need(all(re.search(k, P['model'], re.I) for k in P['kw']), w + ' produce: o texto-modelo deve passar em TODOS os kw')
    pair(P['reply'], w + ' produce.reply')
    need(set(B['rs']) >= set(RSK) and all(v in RS for v in B['rs'].values()), w + ' B.rs: chaves %s com cenas válidas' % RSK)
    need(isinstance(B.get('sc'), str) and B['sc'], w + ' B.sc')
    # X
    need(isinstance(X['n'], int) and isinstance(X['review'], bool), w + ' X.n/review')
    a, b = X['names']; need(a in cast and b in cast, w + ' X.names em cast')
    need(X['stage']['rs'] in RS, w + ' stage.rs'); chars(X['stage']['chars'], w + ' stage.chars')
    ob = X['obra']; need(set(ob) >= {'name', 'kind', 'year', 'text', 'line', 'pa'}, w + ' obra'); pair(ob['line'], w + ' obra.line')
    need(set(ob['pa']) >= {'t', 'e', 'p', 'v'}, w + ' obra.pa')
    need(len(X['gancho']) == 3, w + ' gancho [quem, en, pt]')
    need(len(X['hot']) == 5, w + ' hot: 5 objetos')
    for h in X['hot']:
        need(set(h) >= {'e', 'x', 'y', 'en', 'pt', 'say', 'sayPt'}, w + ' hot item: ' + str(h))
        need(0 <= h['x'] <= 100 and 0 <= h['y'] <= 100, w + ' hot x/y 0..100')
    need(len(X['gap']) == 4, w + ' gap: 4')
    for g in X['gap']:
        need('___' in g['q'], w + ' gap q precisa de ___'); opts_ok(g['opts'], g['a'], 3, w + ' gap'); need(g['pt'] and g['why'], w + ' gap pt/why')
    need(len(X['trap']) == 2, w + ' trap: 2')
    for t in X['trap']: opts_ok(t['opts'], t['a'], 3, w + ' trap')
    st = X['sticker']; need(set(st) >= {'title', 'sub', 'rs', 'chars'}, w + ' sticker'); chars(st['chars'], w + ' sticker')
    need(set(X['speakers']) == set(cast) and all(not charid(v, w + ' speakers') for v in X['speakers'].values()), w + ' speakers: um personagem para cada nome de cast')
    ru = X['rule']
    need(set(ru) >= {'who', 'head', 'sub', 'say', 'uses', 'rules', 'tips'} and ('formula' in ru or 'pairs' in ru), w + ' rule chaves (formula ou pairs)')
    charid(ru['who'], w + ' rule.who'); pair(ru['say'], w + ' rule.say')
    need(all('from_' in f and 'to' in f for f in ru.get('formula', [])) and (ru.get('formula') or ru.get('pairs')), w + ' rule.formula/pairs')
    need(len(ru['uses']) >= 2 and all(set(u) >= {'ico', 'tag', 'en', 'pt'} for u in ru['uses']), w + ' rule.uses >=2')
    need(len(ru['rules']) >= 2 and all(set(u) >= {'tag', 'c', 'text', 'ex'} for u in ru['rules']), w + ' rule.rules >=2')
    need(X['mission_ic'], w + ' mission_ic')
    # XT
    need(len(XT['exp']) == 4, w + ' exp: 4')
    for x in XT['exp']:
        need(set(x) >= {'ic', 'en', 'tag', 'pt', 'use', 'ex'} and x['tag'] in ('Expressão', 'Informal', 'Gíria'), w + ' exp item: ' + str(x.get('en')))
        pair(x['ex'], w + ' exp.ex')
    es = XT['exp_scene']; need(es['rs'] in RS and len(es['lines']) >= 5, w + ' exp_scene')
    for l in es['lines']: need(len(l) == 3 and l[0] in cast, w + ' exp_scene lines')
    need(any('**' in l[1] for l in es['lines']), w + ' exp_scene deve destacar as expressões com **')
    lab = XT['lab']
    need(set(lab) >= {'short', 'title', 'say', 'intro', 'ex', 'pairs', 'tip', 'phrase', 'rounds'}, w + ' lab chaves')
    need(set(lab['intro']) >= {'what', 'how', 'pt'}, w + ' lab.intro')
    need(len(lab['ex']) == 3 and all(len(e) == 4 for e in lab['ex']), w + ' lab.ex: 3 x [palavra, pronúncia, pt, dica]')
    need(len(lab['pairs']) >= 3 and all(len(p) == 3 for p in lab['pairs']), w + ' lab.pairs >=3 x [a, b, nota]')
    pair(lab['phrase'], w + ' lab.phrase')
    need(len(lab['rounds']) == 3, w + ' lab.rounds: 3')
    for r_ in lab['rounds']: opts_ok(r_['opts'], r_['a'], 2, w + ' lab round'); need(r_['say'] in r_['opts'][r_['a']:r_['a'] + 1], w + ' lab round: say deve ser a resposta')
    need(len(XT['hunt']) >= 3, w + ' hunt >=3')
    for h in XT['hunt']:
        need(isinstance(h['a'], int) and h['a'] < len(h['opts']), w + ' hunt a')
    # VB
    need(len(VB['items']) == 4 and VB['title'] and VB['tip'], w + ' verbos: 4')
    for v in VB['items']:
        need(set(v) >= {'v', 'ic', 'pt', 'f', 'ex', 'note'}, w + ' verbo ' + str(v.get('v')))
        need(len(v['f']) == 2 and '**' in v['f'][1][1], w + ' verbo %s: f[1] deve marcar o -s com **' % v['v'])
        pair(v['ex'], w + ' verbo.ex')
    # MR
    need(len(MR['mold']) == 3, w + ' mold: 3 páginas')
    for pg in MR['mold']: need(pg['slots'] and all(s['opts'] for s in pg['slots']), w + ' mold slots')
    need(len(MR['speak']) == 2, w + ' speak: 2')
    need(len(MR['trap']) == 2 and len(MR['gap']) == 2 and len(MR['expq']) == 3 and len(MR['missions']) == 2, w + ' MR contagens (trap 2, gap 2, expq 3, missions 2)')
    for t in MR['trap'] + MR['expq']: opts_ok(t['opts'], t['a'], 3, w + ' MR trap/expq')
    for g in MR['gap']: need('___' in g['text']); opts_ok(g['opts'], g['a'], 3, w + ' MR gap')
    for m in MR['missions']:
        d = m['data']; need(len(d['kw']) == 3 and len(d['check']) == 3 and len(d['tips']) == 3 and len(d['ok']) == 3, w + ' missão ' + m['name'])
        for k in d['kw']: re.compile(k, re.I)
        need(all(re.search(k, d['model'], re.I) for k in d['kw']), w + ' missão %s: modelo deve passar em todos os kw' % m['name'])
    # CX
    need(len(CX) == 6, w + ' CX: 6 contextos')
    for c in CX:
        need('___' in c['text'] and c['a'] == 0, w + ' CX: ___ no texto e resposta certa SEMPRE na posição 0'); opts_ok(c['opts'], 0, 3, w + ' CX')


def load_batches():
    out = []
    only = [a.split('=', 1)[1] for a in sys.argv if a.startswith('--only=')]
    for f in sorted(glob.glob(os.path.join(HERE, 'batch_*.py'))):
        if only and os.path.basename(f)[:-3] not in only:
            continue
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        out += [(os.path.basename(f), s) for s in m.EPS]
    return out


def main():
    items = load_batches()
    errs = 0
    seen = set()
    for i, (f, S) in enumerate(items):
        try:
            validate(S, i)
            n = S['X']['n']
            need(n not in seen, 'ep%s duplicado' % n); seen.add(n)
        except (V, KeyError, TypeError, IndexError, re.error) as ex:
            errs += 1
            print('ERRO %s #%d: %s: %s' % (f, i, type(ex).__name__, ex))
    print('especificações:', len(items), 'erros:', errs)
    if errs or '--check' in sys.argv or any(a.startswith('--only=') for a in sys.argv):
        sys.exit(1 if errs else 0)
    files, where = {}, {}
    for fp in sorted(glob.glob(os.path.join(ROOT, 'data', 'en-a1_*.json'))):
        files[fp] = json.load(open(fp, encoding='utf-8'))
        for k, e in enumerate(files[fp]):
            where[e['n']] = (fp, k)
    order = sorted(where, key=lambda n: files[where[n][0]][where[n][1]]['o'])
    known = {}  # n -> (X, XT, VB) dos episódios já escritos à mão (pilotos 1-5, tools/v3)
    for k in range(5):
        known[V2[k]['n']] = (V2[k], EXTRA[k], VERBS[k])
    for E in M3.load_eps():
        known[E['n']] = (E['v2'], E['extra'], E['verbs'])
    specs = {S['X']['n']: S for f, S in items}
    done = 0
    for n in sorted(specs, key=order.index):
        S = specs[n]
        X = dict(S['X']); X['base'] = S['B']
        fp, k = where[n]
        pn = order[order.index(n) - 1]
        pfp, pk = where[pn]
        pit = files[pfp][pk]
        if pn in specs:
            ps = specs[pn]; px = dict(ps['X']); px['base'] = ps['B']; prev = (px, ps['XT'], ps['VB'])
        elif pn in known:
            prev = known[pn]
        else:
            prev = M3.prev_from_old(pit)
        built = M.build(files[fp][k], X, S['XT'], S['VB'], prev, S['MR'], S['CX'])
        for key in ('xn', 'xof', 'regram'):
            built.pop(key, None)
        built['presentation'] = 'regular-pilot-v1'
        for fr in built['fr']:
            if fr['k'] == 'review':
                fr['bag'] = [g for g in fr['bag'] if g['items']]
        files[fp][k] = built
        done += 1
    for fp, d in files.items():
        open(fp, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, separators=(',', ':')) + '\n')
    print('episódios gravados:', done)


if __name__ == '__main__':
    main()
