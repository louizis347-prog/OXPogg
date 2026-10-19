# -*- coding: utf-8 -*-
# Grava itens de um curso nos blocos data/<cid>_NN.json (25 por arquivo) e atualiza manifest.json e counts.json.
import json,os
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','data')
def data(cid,tmp,per=25):
    it=json.load(open(tmp,encoding='utf-8'))
    old=[f for f in os.listdir(R) if f.startswith(cid+'_') and f.endswith('.json') and f[len(cid)+1:-5].isdigit()]
    names=[]
    for i in range(0,len(it),per):
        nm='%s_%02d.json'%(cid,i//per+1);names.append(nm)
        json.dump(it[i:i+per],open(os.path.join(R,nm),'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    for f in old:
        if f not in names: os.remove(os.path.join(R,f))
    for fn,v in (('manifest.json',names),('counts.json',len(it))):
        p=os.path.join(R,fn);d=json.load(open(p,encoding='utf-8'))
        d[cid]=v
        json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,separators=(', ',': '))
