#!/usr/bin/env python3
"""Roteiro por episódio (inglês regular): junta o que foi escolhido em tools/roteiro/<nivel>_NN.txt com os esqueletos
(data/skel/*.json) e gera páginas simples em roteiro/ + atualiza os esqueletos. Nada de conteúdo de aula: só identificação.
Formato de cada linha dos .txt:  n_principal|verbos (4, ou = para manter)|exp=pt;exp=pt;exp=pt;exp=pt|giria=pt;giria=pt"""
import glob, html, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LV = ['en-a1', 'en-a2', 'en-b1', 'en-b2', 'en-c1', 'en-c2']
NAME = {'en-a1': 'A1', 'en-a2': 'A2', 'en-b1': 'B1', 'en-b2': 'B2', 'en-c1': 'C1', 'en-c2': 'C2'}
KINDS = ['pgexp', 'pgscene']


def pairs(txt):
    out = []
    for p in (x.strip() for x in txt.split(';')):
        if not p: continue
        a, _, b = p.partition('=')
        out.append([a.strip(), b.strip()])
    return out


def read(level):
    d = {}
    for f in sorted(glob.glob(os.path.join(ROOT, 'tools/roteiro/%s_*.txt' % level.replace('en-', '')))):
        for ln in open(f, encoding='utf-8'):
            ln = ln.strip()
            if not ln: continue
            n, vb, ex, gi = ln.split('|')
            d[int(n)] = dict(verbos=vb, exp=pairs(ex), gir=pairs(gi))
    return d


def build():
    summary = {}
    for c in LV:
        sk = json.load(open(os.path.join(ROOT, 'data/skel/%s.json' % c), encoding='utf-8'))
        by = {e['n']: e for e in sk}
        au = read(c)
        rows, miss = [], []
        for e in sk:
            if e['papel'] != 'principal': continue
            mate = by.get(e['par'])
            a = au.get(e['n'])
            if not a:
                miss.append(e['n']); continue
            vb = [v for v in a['verbos'].split(',')] if a['verbos'] != '=' else [v[0] for v in e['verbos']]
            vb = [v.strip() for v in vb if v.strip()]
            assert len(vb) == 4, (c, e['n'], vb)
            assert len(a['exp']) == 4 and len(a['gir']) == 2, (c, e['n'])
            pt = {v[0]: v[1] for v in e['verbos']}
            verbos = [[v, pt.get(v, '')] for v in vb]
            for x in [e] + ([mate] if mate else []):
                x['verbos'] = verbos; x['expressoes'] = a['exp']; x['girias'] = a['gir']; x['status'] = 'roteiro'
                for q in x['quadros']:
                    if q['k'] == 'verbs': q['plano'] = 'Verbos: %s.' % ', '.join(vb)
                    if q['k'] == 'vplay': q['plano'] = 'Mesmos verbos: %s.' % ', '.join(vb)
                    if q['k'] == 'pgexp': q['plano'] = 'Expressões comuns: %s. Gírias: %s.' % ('; '.join('«%s»' % z[0] for z in a['exp']), '; '.join('«%s»' % z[0] for z in a['gir']))
                    if q['k'] == 'pgscene' and 'conversa de verdade' in q['plano']: q['plano'] = 'Na conversa de verdade: as mesmas expressões e gírias em uso.'
            rows.append((e, mate, verbos, a))
        json.dump(sk, open(os.path.join(ROOT, 'data/skel/%s.json' % c), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        summary[c] = (len(rows), miss)
        page(c, rows)
    index(summary)
    return summary


CSS = 'body{font:15px/1.4 system-ui,sans-serif;margin:16px;max-width:1400px}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ccc;padding:5px 7px;vertical-align:top;text-align:left}th{background:#eee;position:sticky;top:0}tr:nth-child(even){background:#fafafa}small{color:#666}'


def page(c, rows):
    os.makedirs(os.path.join(ROOT, 'roteiro'), exist_ok=True)
    h = ['<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Roteiro %s</title><style>%s</style>' % (NAME[c], CSS),
         '<h1>Roteiro de inglês %s <small>(%d pares de episódios)</small></h1><p><a href="index.html">← níveis</a></p>' % (NAME[c], len(rows)),
         '<table><tr><th>eps<th>título<th>estrutura gramatical<th>vocabulário<th>4 verbos<th>expressões comuns<th>gírias<th>obra</tr>']
    for e, mate, verbos, a in rows:
        eps = '%d–%d' % (e['ep'], mate['ep']) if mate else str(e['ep'])
        li = lambda L: '<br>'.join('%s <small>%s</small>' % (html.escape(x[0]), html.escape(x[1])) for x in L)
        h.append('<tr><td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td><small>%s</small></tr>' % (
            eps, html.escape(e['titulo']), html.escape(e['gramatica']['estrutura']), html.escape(', '.join(e['vocabulario'])),
            html.escape(', '.join(v[0] for v in verbos)), li(a['exp']), li(a['gir']), html.escape(e['obra'])))
    h.append('</table>')
    open(os.path.join(ROOT, 'roteiro/%s.html' % c), 'w', encoding='utf-8').write('\n'.join(h))


def index(summary):
    h = ['<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Roteiro dos episódios</title><style>%s</style>' % CSS,
         '<h1>Roteiro dos episódios de inglês regular</h1><p>Só identificação (sem criar aula): estrutura gramatical, vocabulário, 4 verbos, expressões comuns e gírias de cada par de episódios. Os episódios já prontos (1–120 do A1) não entram.</p><ul>']
    for c, (n, miss) in summary.items():
        h.append('<li><a href="%s.html">%s</a> — %d pares%s</li>' % (c, NAME[c], n, (' <small>(faltam %d)</small>' % len(miss)) if miss else ''))
    h.append('</ul>')
    open(os.path.join(ROOT, 'roteiro/index.html'), 'w', encoding='utf-8').write('\n'.join(h))


if __name__ == '__main__':
    s = build()
    for c, (n, miss) in s.items(): print(c, 'pares com roteiro', n, 'faltando', len(miss))
