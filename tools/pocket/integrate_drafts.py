#!/usr/bin/env python3
"""Integrate only reviewed one-episode Pocket drafts into their data block."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build

ROOT=Path(__file__).resolve().parents[2]
DATA=ROOT/'data'
for arg in sys.argv[1:]:
    n=int(arg); level={952:'b1',953:'b2',954:'c1',955:'c2'}[n//1000]
    draft=ROOT/'drafts/pocket'/f'{level}_{n%1000}.txt'
    plan=next(row for row in json.loads((DATA/'pk-roteiro'/f'pk-{level}.json').read_text()) if row['n']==n)
    parsed=build.parse_txt(draft)
    if len(parsed)!=1: raise SystemExit(f'{draft}: expected one episode')
    x=parsed[0]
    if len(x['dlg']) < (10 if plan['chefe'] else 8) or len(x['vocab'])!=5 or len(x['build'])!=2 or len(x['speak'])!=2 or len(x['recap'])!=4:
        raise SystemExit(f'{draft}: incomplete episode')
    if any('{0}' not in b['en'] or '{0}' not in b['pt'] for b in x['build']): raise SystemExit(f'{draft}: broken build slot')
    text=' '.join(line[1] for line in x['dlg']).lower()
    if any(word[0].lower() not in text for word in x['vocab']): raise SystemExit(f'{draft}: vocabulary absent from dialogue')
    x['teaser']='Próximo: '+str(plan.get('proximo') or 'Nova situação'); x['boss']=bool(plan['chefe'])
    e=build.episode(level,plan['arco']-1,plan['pos']-1,x,{'b1':952000,'b2':953000,'c1':954000,'c2':955000}[level],n%1000)
    e['a']={'k':'Obra cultural','w':plan['obra'].split(' (')[0],'y':'','d':x['culture']}
    e['v']=[[v[0],v[1],build.EMO.get(v[0].lower(),'📌')] for v in x['vocab']]
    slot=(n%1000-1)//50+1; path=DATA/f'pk-{level}_{slot:02d}.json'
    episodes=json.loads(path.read_text(encoding='utf-8'))
    for i,old in enumerate(episodes):
        if old['n']==n: episodes[i]=e;break
    else: raise SystemExit(f'{n} missing from {path}')
    path.write_text(json.dumps(episodes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('integrated',n)
