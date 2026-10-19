# -*- coding: utf-8 -*-
# Divide a "Missão dos verbos" (16 passos) em 7 + 7: original (completar + ouvir) e continuação "Verbo em ação" (montar + forma com he/she).
import json,glob,sys,copy
sys.path.insert(0,'/tmp/claude-0/-home-user-OXPogg/097f2c11-a1d9-5802-aa7c-396fb7b01940/scratchpad')
import reg3 as r
def plan(k,steps):
    out=[]
    for s in steps:
        for v in range(k):
            if len(out)<7: out.append([v,s])
    return out
def run(cid):
    it=[]
    for f in sorted(glob.glob('/home/user/OXPogg/data/%s_*.json'%cid)): it+=json.load(open(f))
    mains={x['n']:x for x in it if not x.get('xof')};n=0
    for x in it:
        if not x.get('xof') or x['xof'] not in mains: continue
        m=mains[x['xof']];vb=next((s for s in m['fr'] if s['k']=='verbs'),None);mv=next((s for s in m['fr'] if s['k']=='vplay'),None)
        if not vb or not mv: continue
        k=len(vb['items'])
        mv['items']=copy.deepcopy(vb['items']);mv['plan']=plan(k,[0,3]);mv['say']='Missão dos verbos: 7 passos. Eu ajudo você!'
        xv={'k':'vplay','title':'Verbo em ação','items':copy.deepcopy(vb['items']),'plan':plan(k,[1,2]),'say':'Verbo em ação: monte as frases e descubra a forma certa com he e she!'}
        x['fr']=[s for s in x['fr'] if not(s['k']=='vplay')]
        pos=next((i+1 for i,s in enumerate(x['fr']) if s['k']=='soundlab'),len(x['fr']))
        x['fr'].insert(pos,xv);n+=1
    tmp='/tmp/_vplan_%s.json'%cid;json.dump(it,open(tmp,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    r.data(cid,tmp);print(cid,'verbos divididos em',n)
if __name__=='__main__':
    for c in sys.argv[1:]: run(c)
