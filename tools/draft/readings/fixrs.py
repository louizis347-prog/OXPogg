import json,glob
RS=['library','cafe','park','street','office','kitchen','living','bedroom','desk','lobby1','cafe2']
n=0
for fn in sorted(glob.glob('data/en-*.json')):
    d=json.load(open(fn));ch=False
    for e in d:
        fr=[f for f in e['fr'] if f.get('rs')]
        for i in range(1,len(fr)-1):
            if fr[i-1]['rs']==fr[i]['rs']==fr[i+1]['rs']:
                near={fr[j]['rs'] for j in range(max(0,i-2),min(len(fr),i+3))}
                fr[i]['rs']=next(r for r in RS if r not in near);ch=True;n+=1
    if ch:json.dump(d,open(fn,'w'),ensure_ascii=False,separators=(',',':'))
print(n)
