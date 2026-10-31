import sys,re
# uso: merge_extra.py alvo.txt extra.txt  -> insere linhas r: do extra antes do q: de cada bloco
tgt,ext=sys.argv[1:3]
def blocks(fn):
    out={};order=[];cur=None
    for ln in open(fn,encoding='utf-8'):
        ln=ln.rstrip('\n')
        if ln.startswith('#'):cur=ln[1:].split()[0];out[cur]=[ln];order.append(cur)
        elif cur and ln.strip():out[cur].append(ln)
    return out,order
T,order=blocks(tgt);X,_=blocks(ext)
miss=[k for k in X if k not in T];assert not miss,miss
res=[]
for k in order:
    b=T[k]
    if k in X:
        add=[l for l in X[k][1:] if l.startswith('r:')]
        i=next(i for i,l in enumerate(b) if l.startswith('q:'))
        b=b[:i]+add+b[i:]
    res+=b
open(tgt,'w',encoding='utf-8').write('\n'.join(res)+'\n')
