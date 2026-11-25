#!/usr/bin/env python3
"""Gera poglodict/english-a1-extra.js e poglodict/plano-ingles-a1-181-300.csv a partir dos JSON de
poglodict/fontes/a1-181-300/NNN.json (uma lição por arquivo, formato descrito em fontes/a1-181-300/LEIA-ME.md).
Uso: python3 tools/poglodict_build_a1.py   (de qualquer pasta)
O JS gerado só ACRESCENTA entradas aos arranjos de english-a1-plan.js / english-a1-content.js (índice = lição − 1)."""
import csv, glob, json, os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
P = os.path.join(ROOT, 'poglodict'); 

def photo_file(key):
    for f in ('photo-%s.webp' % key, '%s.webp' % key, key):
        if os.path.exists(os.path.join(P, f)): return f
    raise SystemExit('foto inexistente: %s' % key)

def gen(srcdir, level, jsname, csvname):
    """level 'a1' acrescenta aos arranjos englishA1*; 'a2' preenche englishA2Data (índice = lição − 1)."""
    SRC = os.path.join(P, 'fontes', srcdir)
    lessons = {}
    for f in sorted(glob.glob(os.path.join(SRC, '[0-9]*.json'))):
        d = json.load(open(f, encoding='utf-8')); lessons[d['n']] = d
    ns = sorted(lessons)
    out = ['// %s · lições %d–%d · conteúdo próprio no padrão das 50 primeiras (gerado por tools/poglodict_build_a1.py; edite fontes/%s/*.json).' % (level.upper(), ns[0], ns[-1], srcdir),
           '// Cada índice = número da lição − 1. Plano, conteúdo, padrão gramatical, mini-história, tema visual e par de fotos.',
           '(function(){',
           'const plans=[],content=[],patterns=[],themes=[],photos=[],stories={},extras={};']
    rows = []
    for n in ns:
        d = lessons[n]; u = n - 1
        plan = {'title': d['title'], 'file': photo_file(d['photo']), 'grammar': d['grammar'], 'goal': d['goal'], 'words': d['words']}
        out.append('plans[%d]=%s;' % (u, json.dumps(plan, ensure_ascii=False)))
        out.append('content[%d]=%s;' % (u, json.dumps([d['reading'], d['dialogue'], d['pron'], d['gram']], ensure_ascii=False)))
        out.append('patterns[%d]=new RegExp(%s,"i");' % (u, json.dumps(d['pattern'])))
        out.append('themes[%d]=%s;' % (u, json.dumps(d['art'])))
        out.append('photos[%d]=%s;' % (u, json.dumps([photo_file(re.sub(r'^photo-|\.webp$', '', x)) if not x.endswith('.webp') else x for x in d['photos']])))
        if 'story' in d:
            t, body = d['story']
            for en, pt in body:
                assert '|' not in en + pt and '~' not in en + pt, n
            out.append('stories[%d]=%s;' % (u, json.dumps([t, '|'.join('%s~%s' % (en, pt) for en, pt in body)], ensure_ascii=False)))
        if d.get('extra'): out.append('extras[%d]=%s;' % (u, json.dumps(d['extra'], ensure_ascii=False)))
        words = ' / '.join('%s — %s' % (a, b) for a, b in d['words'])
        rows.append([n, level.upper(), d['title'], words, d['grammar'], d['goal'], '', 'Imagem a definir (provisória: %s)' % plan['file'], '', '', '', ''])
    if level == 'a1':
        out += [
            'for(const [u,v] of plans.entries())if(v)englishA1Plans[u]=v;',
            'for(const [u,v] of content.entries())if(v)englishA1Content[u]=v;',
            'for(const [u,v] of patterns.entries())if(v)englishA1GrammarPatterns[u]=v;',
            'for(const [u,v] of themes.entries())if(v)englishA1PhotoThemes[u]=v;',
            'for(const [u,v] of photos.entries())if(v)englishA1BlockPhotoFiles[u]=v;',
            'Object.assign(englishA1MiniStories,stories);',
            'Object.assign(englishA1ExtraWordExamples,extras);']
    else:
        out += [
            'for(const [u,v] of plans.entries())if(v)englishA2Plans[u]=v;',
            'for(const [u,v] of content.entries())if(v)englishA2Content[u]=v;',
            'for(const [u,v] of patterns.entries())if(v)englishA2Patterns[u]=v;',
            'for(const [u,v] of themes.entries())if(v)englishA2PhotoThemes[u]=v;',
            'Object.assign(englishA2MiniStories,stories);',
            'Object.assign(englishA2ExtraWordExamples,extras);']
    if level == 'a2': out.insert(2, 'var englishA2Patterns=typeof englishA2Patterns==="undefined"?[]:englishA2Patterns;')
    out += ['})();', '']
    open(os.path.join(P, jsname), 'w', encoding='utf-8').write('\n'.join(out))
    with open(os.path.join(P, csvname), 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.writer(fh, delimiter=';', quoting=csv.QUOTE_ALL)
        w.writerow(['Lição', 'Nível', 'Título', 'Vocabulário inglês — português', 'Gramática', 'Objetivo', 'Imagem', 'Descrição da imagem', 'Autoria', 'Fonte', 'Licença', 'URL da licença'])
        w.writerows(rows)
    print('lições:', len(ns), '| js:', os.path.getsize(os.path.join(P, jsname)), 'bytes')

def main():
    gen('a1-181-360', 'a1', 'english-a1-extra.js', 'plano-ingles-a1-181-360.csv')
    if glob.glob(os.path.join(P, 'fontes', 'a2-1-80', '[0-9]*.json')):
        gen('a2-1-80', 'a2', 'english-a2-extra.js', 'plano-ingles-a2-01-80.csv')
    else:
        open(os.path.join(P, 'english-a2-extra.js'), 'w').write('// A2: sem lições autorais ainda\n')

if __name__ == '__main__':
    main()
