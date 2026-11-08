"""Gera data/livro/imgs.json: aula -> palavras do vocabulário que têm foto em img/livro/palavras."""
import json, os, re
R = os.path.join(os.path.dirname(__file__), '..', '..', '..')
def slug(w): return re.sub(r'^-|-$', '', re.sub(r'[^a-z0-9]+', '-', w.lower().replace("’", '').replace("'", '')))
have = set(os.listdir(os.path.join(R, 'img', 'livro', 'palavras')))
out = {}
for f in sorted(os.listdir(os.path.join(R, 'data', 'livro', 'lessons'))):
    if f == 'index.json': continue
    L = json.load(open(os.path.join(R, 'data', 'livro', 'lessons', f)))
    ws = []
    for fr in L['frames']:
        for b in fr['blocks']:
            if b['type'] == 'vocab': ws += [(x['w'], x['pt']) for x in b['items'] if slug(x['w']) + '.jpg' in have]
    if len(ws) >= 4: out[f[:-5]] = ws
json.dump(out, open(os.path.join(R, 'data', 'livro', 'imgs.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
print(len(out), 'aulas com >=4 fotos')
