import sys;sys.path.insert(0,'/tmp/gen')
from common import *
def conv(npc,story,turns):
    return {'npc':{'name':npc},'story':story,'turns':[{'npc':t[0],'pt':t[1],'opts':[O(t[2][0],t[2][1],True,t[2][2]),O(t[3][0],t[3][1],False,t[3][2]),O(t[4][0],t[4][1],False,t[4][2])]} for t in turns]}
def conv_s(npc,story,turns): return conv(npc,story,turns)
def role(turns,change): return {'turns':[{'npc':t[0],'opts':[R(*o) for o in t[1]]} for t in turns],'change':change}
def culture(hook,mf,wild,compare,quiz):
    return {'hook':hook,'mythfact':[{'s':a,'ans':b,'why':c} for a,b,c in mf],
      'wild':[{'kind':k,'lines':l,'decode':{'q':q,'opts':o,'ans':0,'why':w}} for k,l,q,o,w in wild],
      'compare':{'br':compare[0],'us':compare[1],'tip':compare[2],'ask':compare[3]},
      'quiz':[{'q':q,'opts':o,'ans':0,'why':w} for q,o,w in quiz]}
def reading(title,gloss,fast,scan,tf,order,ctx,chunks,think,S):
    text=[' '.join(e for e,p in par) for par in S]
    return {'genre':'Short story','title':title,'glossary':[{'w':a,'pt':b} for a,b in gloss],'fast':{'q':'What is the story about?','opts':fast[0],'ans':0,'why':fast[1]},
      'scan':[{'q':q,'ans':a,'alt':al} for q,a,al in scan],'tf':[{'s':s,'ans':a,'why':w} for s,a,w in tf],'order':order,
      'ctx':[{'sent':s,'w':w,'opts':o,'ans':0,'why':why} for s,w,o,why in ctx],'chunkHunt':chunks,'think':think,'text':text}
def errs(L): return [{'wrong':a,'fix':b,'alt':c,'why':d} for a,b,c,d in L]
def verbs(L): return [V(*v) for v in L]
def vg(L): return [{'scene':pt,'en':en,'opts':o,'ans':a,'pt':pt,'why':w} for en,pt,o,a,w in L]
def exprs(L): return [{'en':a,'pt':b,'ex':c,'exp':d,'c':e} for a,b,c,d,e in L]
def eg(L): return [{'cue':c,'opts':o,'ans':a,'why':w} for c,o,a,w in L]
def vocab(L): return [{'w':a,'pt':b,'e':c,'ex':[d,e]} for a,b,c,d,e in L]
def molds(L): return [{'title':t,'frame':f,'slots':[{'key':k,'opts':o} for k,o in sl],'model':m,'note':n} for t,f,sl,m,n in L]
def sounds(L): return [{'say':a,'tag':b,'tip':c} for a,b,c in L]
def lab(focus,what,how,tip,words,pairs,phrase): return {'focus':focus,'what':what,'how':how,'tip':tip,'words':[{'w':a,'pt':b} for a,b in words],'pairs':[{'a':a,'b':b} for a,b in pairs],'phrase':{'en':phrase[0],'pt':phrase[1]}}
def cards(L): return [{'icon':a,'big':b,'label':c,'sub':d} for a,b,c,d in L]
def writing(task,model,kw,checks): return {'task':task,'model':model,'kw':kw,'checks':checks}

def dlg(nbi,swaps):
    import build_v5 as B
    nb=B.NB[nbi-1];ch=[f for f in nb['fr'] if f['k']=='nbchat'][0];L=[l for l in ch['lines'] if l[1] not in B.FILLER]
    out=[]
    for i,l in enumerate(L):
        en=l[1].replace('{{','').replace('}}','');pt=l[2]
        if i in swaps:
            eo,ea,po,pa=swaps[i]
            assert eo in en,(i,eo,en);assert po in pt,(i,po,pt)
            en=en.replace(eo,'{'+'|'.join([eo]+ea)+'}',1);pt=pt.replace(po,'{'+'|'.join([po]+pa)+'}',1)
        out.append({'who':l[0],'en':en,'pt':pt})
    return out
def mini_from(d,idx): return [d[i] for i in idx]
def lesson(n,SUPP,reading_S,Y,X,Z,convo_t,npc,story,dl,mini_idx):
    X=dict(X);X['dlg']=dl;X['mini']=mini_from(dl,mini_idx);X['convo']=conv(npc,story,convo_t);SUPP=dict(SUPP);SUPP['convo']=X['convo']
    emit(n,SUPP,Y,X,Z,reading_S)

def dlg_lines(L,swaps):
    out=[]
    for i,l in enumerate(L):
        en,pt=l[1],l[2]
        if i in swaps:
            eo,ea,po,pa=swaps[i]
            assert eo in en,(i,eo,en);assert po in pt,(i,po,pt)
            en=en.replace(eo,'{'+'|'.join([eo]+ea)+'}',1);pt=pt.replace(po,'{'+'|'.join([po]+pa)+'}',1)
        out.append({'who':l[0],'en':en,'pt':pt})
    return out
def lesson_own(n,SUPP,reading_S,Y,X,Z,convo_t,own,swaps,mini_idx):
    SUPP=dict(SUPP);SUPP['own']=own;SUPP.pop('nb',None)
    dl=dlg_lines(own['lines'],swaps)
    lesson(n,SUPP,reading_S,Y,X,Z,convo_t,own['npc'],own['story'],dl,mini_idx)
