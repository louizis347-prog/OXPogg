#!/usr/bin/env python3
"""Reparo e enriquecimento do curso regular de inglês (en-a1..en-c2), reexecutável.

 1. obra única por episódio: alinha cultob/culttl/bridge/wrap à obra da capa (cover.cw) e troca os
    nomes antigos nos textos de apoio;
 2. nível: `levelProgression` deixa de repetir o texto de A1 em todos os níveis;
 3. lplay.why específico ("“term” significa “gloss”…") em vez da frase fixa;
 4. fio / bridge / wrap sem as frases fixas: usam o episódio anterior e o seguinte, o gancho do
    episódio (`h.l`), a obra e o nível;
 5. episódios 70/79 ("Regra, som, expressões e escrita"): assunto e abertura derivados do conteúdo
    (cexp/lexpack/g) e propagados aos textos de fechamento.
"""
import json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
GENERIC = 'Regra, som, expressões e escrita'
LP = {
    'a1': 'Base comunicativa: reconheça fórmulas sociais e produza frases curtas com apoio.',
    'a2': 'Rotinas e experiências: conte o que faz e o que fez, com frases de duas ou três orações e conectores simples.',
    'b1': 'Autonomia: narre fatos, explique motivos e dê opinião com exemplos, mesmo com pausas para planejar.',
    'b2': 'Argumentação: defenda um ponto de vista, compare posições e ajuste o registro entre formal e informal.',
    'c1': 'Precisão e nuance: use estruturas complexas, ironia e expressões idiomáticas, e adapte o discurso ao interlocutor.',
    'c2': 'Domínio: reformule com naturalidade, controle estilo e subtexto, e escolha a palavra exata para cada contexto.',
}
PRAG = {
    'a1': 'Focus on being clear and polite: greet, thank and ask simply.',
    'a2': 'Notice politeness and tone in everyday requests and small talk.',
    'b1': 'Weigh clarity, politeness and how direct you want to sound.',
    'b2': 'Consider clarity, formality, diplomacy and the effect on the listener.',
    'c1': 'Balance nuance, register and intention: choose how much to soften or sharpen.',
    'c2': 'Fine-tune register, subtext and effect: pick the phrasing a native speaker would trust.',
}
OLD_WHY = 'A expressão aparece na cena e no vocabulário deste episódio.'
OLD_PREV = 'The previous episode and its communicative choice.'
OLD_NEXT = 'Choose how you would respond next.'
OLD_PRAG = 'Consider clarity, formality, diplomacy, intention and suitability.'
OLD_BR = 'Connect the cultural reference to the language goal of this episode.'
OLD_TEASER = 'Continue the thread with a new situation.'


def strings(o, fn):
    """aplica fn a cada string (devolve nova estrutura); ignora campos de arte"""
    if isinstance(o, str):
        return fn(o)
    if isinstance(o, list):
        return [strings(v, fn) for v in o]
    if isinstance(o, dict):
        return {k: (v if k in ('art', 'c', 'seed', 'cam', 'scene') else strings(v, fn)) for k, v in o.items()}
    return o


def topic_from(e):
    fr = {x['k']: x for x in e['fr']}
    mm = re.search(r'\*\*(.+?)\*\*', (fr.get('cexp') or {}).get('intro', ''))
    g = e.get('g') if isinstance(e.get('g'), dict) else {}
    gt = g.get('t') or ''
    base = mm.group(1) if mm else (gt.split(':')[0] if gt else e['t'])
    base = base.strip()
    base = base[0].upper() + base[1:]
    if ':' in gt:
        det = gt.split(':', 1)[1].strip()
        if det and det.lower() not in base.lower():
            base += ' — ' + det
    return base


def repair_level(lv, eps):
    for i, e in enumerate(eps):
        prev_t = eps[i - 1]['t'] if i else None
        next_t = eps[i + 1]['t'] if i + 1 < len(eps) else None
        old_s = e.get('s')
        # 5. assunto genérico
        if old_s == GENERIC:
            new_s = topic_from(e)
            mm = re.match(r'O porquê de (.+?): regra, som', e.get('p') or '')
            e['s'] = new_s
            if mm:
                e['p'] = 'O porquê de %s: %s.' % (mm.group(1), new_s[0].lower() + new_s[1:])
            sub = lambda t, o=GENERIC, n=new_s: t.replace(o, n).replace(o.lower(), n[0].lower() + n[1:])
            e['fr'] = [strings(x, sub) for x in e['fr']]
        s = e.get('s') or e['t']
        fr = e['fr']
        by = {}
        for x in fr:
            by.setdefault(x['k'], x)
        cover, cob, ctl = by.get('cover'), by.get('cultob'), by.get('culttl')
        # 1. obra única
        cw = (cover or {}).get('cw') or {}
        canon = cw.get('work') or (by.get('cultcena') or {}).get('work') or (cob or {}).get('work')
        if canon:
            olds = set()
            if cob and cob.get('work') and cob['work'] != canon:
                olds.add(cob['work']); cob['work'] = canon
            if ctl:
                for w in ctl.get('works', []):
                    if w.get('t') == 'main work' and w.get('n') != canon:
                        olds.add(w['n'])
                        w['n'] = canon
                        if cw.get('kind'): w['k'] = cw['kind']
                        if cw.get('year'): w['y'] = cw['year']
                        if cob and cob.get('panels'): w['d'] = cob['panels'][0]
            for o in olds:
                for k in ('cultob', 'culttl', 'bridge', 'wrap', 'cultgame', 'cultx'):
                    for x in fr:
                        if x['k'] == k:
                            for q, v in list(x.items()):
                                if q not in ('art', 'c', 'seed', 'cam', 'scene'):
                                    x[q] = strings(v, lambda t, o=o: t.replace(o, canon))
            for x in fr:
                if x['k'] == 'bridge': x['work'] = canon
            if cob and cob.get('facts') and olds:
                year = cw.get('year')
                cob['facts'] = [f for f in cob['facts'] if not f.startswith('Context:')]
                cob['facts'] = [('%s: %s' % (cw['kind'], canon)) if (cw.get('kind') and f.endswith(': ' + canon)) else f for f in cob['facts']]
                if year: cob['facts'].append('Context: %s' % year)
        for x in fr:
            k = x['k']
            # 2. nível
            if k in ('bridge', 'wrap') and 'levelProgression' in x:
                x['levelProgression'] = '%s Situação aplicada: %s.' % (LP[lv], s)
            # 3. lplay
            if k == 'lplay':
                gl = {}
                for y in fr:
                    if y['k'] == 'words':
                        for it in y.get('items', []):
                            if len(it) > 2 and it[2]:
                                gl[it[0]] = it[2]
                for r in x.get('rounds', []):
                    if r.get('why') == OLD_WHY and r.get('say') in gl:
                        r['why'] = '“%s” significa “%s” e aparece na cena de hoje.' % (r['say'], gl[r['say']])
            # 4. fio / bridge / wrap
            if k == 'fio':
                if x.get('previous') == OLD_PREV:
                    x['previous'] = ('Previously: %s.' % prev_t) if prev_t else 'This is where the story begins.'
                if x.get('nextLine') == OLD_NEXT:
                    h = e.get('h') if isinstance(e.get('h'), dict) else {}
                    x['nextLine'] = ('Try a reply like: “%s”' % h['l']) if h.get('l') else 'Answer in your own words with today’s phrases.'
                if x.get('pragmatics') == OLD_PRAG:
                    x['pragmatics'] = PRAG[lv]
            if k == 'bridge' and x.get('text') == OLD_BR:
                yr = (cw.get('year') or '')
                x['text'] = 'Connect %s%s to today’s goal: %s.' % (x.get('work') or canon, (' (%s)' % yr) if yr else '', s)
            if k == 'wrap' and isinstance(x.get('teaser'), dict) and x['teaser'].get('d') == OLD_TEASER:
                x['teaser']['d'] = ('Next: %s.' % next_t) if next_t else 'Next: a new situation to put today’s language to work.'


def main():
    m = json.load(open(os.path.join(ROOT, 'manifest.json'), encoding='utf-8'))
    for lv in ['a1', 'a2', 'b1', 'b2', 'c1', 'c2']:
        k = 'en-' + lv
        blocks = [(os.path.join(ROOT, b), json.load(open(os.path.join(ROOT, b), encoding='utf-8'))) for b in m[k]]
        flat = [e for _, d in blocks for e in d]
        series = {}
        for e in flat:
            series.setdefault(str(e['n'])[:2], []).append(e)     # cada série (prefixo do id) é uma sequência própria
        for grp in series.values():
            repair_level(lv, sorted(grp, key=lambda e: e['n']))
        for p, d in blocks:
            open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, separators=(',', ':')))
        print(k, 'ok', flush=True)


if __name__ == '__main__':
    main()
