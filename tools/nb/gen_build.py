# -*- coding: utf-8 -*-
# uso: python3 gen_build.py <eng|esa2|it> -> escreve <x>_all.json
import json, sys, re, importlib, os
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
CFG=dict(eng=dict(mod='buildeng',pre='e',arcs=15,base=95000,rev=95500,revo0=0,out='eng_all.json'),
         esa2=dict(mod='buildesa2',pre='a',arcs=30,base=90400,rev=94500,revo0=400,out='esa2_all.json'),
         it=dict(mod='buildit',pre='i',arcs=8,base=96000,rev=96500,revo0=0,out='it_all.json'),
         ja=dict(mod='buildja',pre='j',arcs=37,base=97100,rev=97500,revo0=0,out='ja_all.json'),
         de=dict(mod='buildde',pre='g',arcs=40,base=92000,rev=97100,revo0=0,out='de_all2.json'),
         fr=dict(mod='buildfr',pre='f',arcs=35,base=91000,rev=96100,revo0=0,out='fr_all2.json'),
         pten=dict(mod='buildpten',pre='t',arcs=20,base=99000,rev=99700,revo0=0,out='pten_all.json'),
         pt=dict(mod='buildpt',pre='p',arcs=15,base=93000,rev=98100,revo0=0,out='pt_all.json'))
k=sys.argv[1]; C=CFG[k]
build=importlib.import_module(C['mod'])
NEW=[];ARCS=[]
ONLY=os.environ.get('ONLY'); FROM=int(os.environ.get('FROM','1'))
if FROM>1 and not ONLY: C['out']='_new_%s.json'%k
if ONLY: C['out']='_chk_%s_%s.json'%(k,ONLY)
for a in (range(int(ONLY),int(ONLY)+1) if ONLY else range(FROM,C['arcs']+1)):
    f="%s%02d"%(C['pre'],a)
    if not os.path.exists(os.path.join(HERE,f+".py")): print('falta',f); break
    m=importlib.import_module(f); eps=getattr(m,"EPS%02d"%a)
    base=C['base']+(a-1)*10
    npart=len(eps)
    assert [e["n"] for e in eps]==list(range(base+1,base+1+npart)) and npart in (5,9),(a,[e["n"] for e in eps])
    NEW+=eps
    ARCS.append(dict(idx=a,rev_n=C['rev']+a,rev_o=C['revo0']+(a-1)*10+npart+.5,ids=range(base+1,base+1+npart)))
build.EPS[:]=NEW
out=[build.build_ep(i,e) for i,e in enumerate(NEW)]
allx=[]
for ai,arc in enumerate(ARCS):
    eps=[e for e in NEW if e["n"] in arc["ids"]]
    nxt=None
    if ai+1<len(ARCS): nxt=next(e for e in NEW if e["n"]==ARCS[ai+1]["ids"][0])
    if len(eps)<9:
        allx+=[x for x in out if x["n"] in arc["ids"]];continue
    rev=build.build_review(arc,eps,nxt)
    allx+=[x for x in out if x["n"] in arc["ids"]]+[rev]
bad=0
for e,src in zip(out,NEW):
    assert len(src["v"])==6 and len(src["chat"])==11 and len(src["chat2"])==6 and len(src["slang"][2])==6,src["n"]
    assert src["real"][0]!=src["real"][1],('real igual',src["n"])
    for it in e["fr"][2]["items"]:
        assert 0<=it["line"]<9 and it["a"]<3,(src["n"],it)
        if "why" not in it: continue
        quotes=re.findall(r"“(.+?)”",it["why"]); line=e["fr"][1]["lines"][it["line"]]
        w2=re.findall(r"\w+"," ".join(quotes).lower())[:2]
        if not any(w in line[1].lower() for w in w2): print("CONFERIR tap",e["n"],it["line"],it["why"],"|",line[1]); bad+=1
    for p in e["fr"][3]["pages"]:
        assert len(p["S"])==3 and len(p["E"])==3,(src["n"],p["label"])
        assert re.fullmatch(r"[\s.,!?¡¿:;…。！？、]*",p["end"] or ""),(src["n"],'end',p["end"])
    for kk in list(e["fr"][5]["gl"])[:5]:
        if not any(build.norm(b)==build.norm(kk) for l in e["fr"][5]["lines"] for b in re.findall(r"\*\*(.+?)\*\*",l[1])): print("GLOSA sem negrito",e["n"],kk); bad+=1
ids=[x["n"] for x in allx]; assert len(ids)==len(set(ids))
json.dump(allx,open(os.path.join(HERE,C['out']),"w"),ensure_ascii=False)
print(len(allx),"itens;",bad,"avisos")
