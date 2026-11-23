#!/usr/bin/env python3
"""Pacotes das lições 51–130 (in/block6..13.json) a partir de curriculum_51_130.json + lições 1–50 já escritas."""
import glob, json, os, re
H = os.path.dirname(os.path.abspath(__file__))
old = json.load(open(H + '/old.json')); ORDER = json.load(open(H + '/order.json')); cur = json.load(open(H + '/curriculum_51_130.json')); cur2 = json.load(open(H + '/curriculum_131_180.json'))
new = {}
for f in sorted(glob.glob(H + '/out/block*.json')): new.update(json.load(open(f)))
for f in sorted(glob.glob(H + '/out/fix*.json')):
    for k, v in json.load(open(f)).items():
        if k in new: new[k]['words'] = new[k]['words'] + [w for w in v['add'] if w[0].lower() not in {x[0].lower() for x in new[k]['words']}]
used = sorted({w[0].lower() for n in range(1, 131) for w in new[str(n)]['words']} | {w[0].lower() for c in cur2 for w in c['base_words']})
json.dump(used, open(H + '/used_words.json', 'w'), ensure_ascii=False)
gram = [old['plan'][o - 1]['grammar'] for o in ORDER] + [c['grammar'] for c in cur + cur2]
basew = [old['plan'][o - 1]['words'] for o in ORDER] + [c['base_words'] for c in cur + cur2]
# primeira lição em que cada estrutura/ palavra de estrutura pode aparecer
FIRST = {'could': 131, 'should': 135, "shouldn't": 136, 'there was': 139, 'there were': 139, 'than': 150, 'must': 46, "mustn't": 159, 'myself': 161, 'while': 166, 'had to': 176, 'yourself': 161,
         "let's": 70, 'have to': 69, 'has to': 69, 'how much': 61, 'how many': 63, 'how often': 73, 'because': 74, 'whose': 95, 'enough': 101,
         'going to': 115, 'was': 117, 'were': 117, 'didn\'t': 121, 'did': 122, 'yesterday': 127, 'ago': 127, 'went': 123, 'bought': 124, 'every': 86}
pk = []
for c in cur2:
    n = c['n']
    pk.append(dict(n=n, level='A1', title=c['title'], grammar=c['grammar'], goal=c['goal'], base_words=c['base_words'],
        grammar_taught_before=gram[:n - 1], recycle_from_previous=[w for k in range(n - 6, n - 1) for w in basew[k]],
        pron_sound=c['sound'], pron_words=c['pron_words'], mini_story=(n % 10 == 0),
        not_yet_taught=sorted(k for k, v in FIRST.items() if v > n)))
for k in range(5):
    json.dump(pk[k * 10:(k + 1) * 10], open(H + '/in/block%d.json' % (k + 14), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(pk), len(used))
