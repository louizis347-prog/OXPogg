#!/usr/bin/env python3
"""Restaura as continuações do inglês ao mínimo de 13 quadros.
 1) volta aos quadros de antes do enxugamento (commit bb87965) em todas as continuações;
 2) as 12 continuações reescritas do en-a1 (9 quadros) recuperam soundlab/vplay/cexp/ctxv/wlat do histórico (9acc50f);
 3) as 38 continuações do en-a1 sem 'Você sabia?' ganham um culttl só com curiosidade (tools/cult/facts_en-a1_cont.json).
Uso: python3 tools/cult/restore_cont.py"""
import json,glob,subprocess,collections,os
def git(ref,path): return json.loads(subprocess.check_output(['git','show','%s:%s'%(ref,path)]))
def iscont(e):
    o=e.get('o');return isinstance(o,(int,float)) and (o%1)>0.4
facts=json.load(open('tools/cult/facts_en-a1_cont.json')) if os.path.exists('tools/cult/facts_en-a1_cont.json') else {}
ORDER=['cover','scene','culttl','pbridge','rdgplay','rdg','pat','sbuild','soundlab','vplay','cexp','ctxv','docread','mystery','upgrade','xpr','paraphrase','rhetoric','balloons','wlat','scene','scenebuild','lexpack','produce']
st=collections.Counter()
for f in sorted(glob.glob('data/en-*_*.json')):
    name=f.split('/')[-1];cid=name.rsplit('_',1)[0]
    cur=json.load(open(f));bb=git('bb87965','data/'+name)
    bbmap={e['n']:e for e in bb}
    oldmap={e['n']:e for e in git('9acc50f','data/'+name)}
    ch=False
    for e in cur:
        if not iscont(e) or e['n'] not in bbmap: continue
        fr=[dict(x) for x in bbmap[e['n']]['fr']]
        if len(fr)<=9 and e['n'] in oldmap:                       # protótipos: recupera os exercícios do histórico
            have={x['k'] for x in fr}
            add=[x for x in oldmap[e['n']]['fr'] if x['k'] in('soundlab','vplay','cexp','ctxv','wlat') and x['k'] not in have]
            order_ins={'soundlab':'sbuild','vplay':'soundlab','cexp':'vplay','ctxv':'cexp','wlat':'xpr'}
            for x in add:
                prev=order_ins[x['k']]
                idx=max([i for i,y in enumerate(fr) if y['k']==prev]+[-1])
                if x['k']=='wlat': idx=max(i for i,y in enumerate(fr) if y['k']=='xpr')
                fr.insert(idx+1,x)
            st['protótipo completado']+=1
        if cid=='en-a1' and not any(x['k']=='culttl' for x in fr) and str(e['n']) in facts:
            art=next((x.get('pa') for x in fr if x.get('pa')),None)
            c={'k':'culttl','title':'🗣️ Você sabia?','fact':facts[str(e['n'])],'works':[]}
            if art: c['pa']=art
            fr.insert(1,c);st['culttl de curiosidade']+=1
        e['fr']=fr;ch=True;st['restaurada']+=1
    if ch: json.dump(cur,open(f,'w'),ensure_ascii=False,separators=(',',':'))
print(dict(st))
