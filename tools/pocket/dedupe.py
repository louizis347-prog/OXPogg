#!/usr/bin/env python3
"""Renomeia títulos (T) e frases-chave (K) repetidos entre TODOS os arquivos *_arco*.txt, só nos arquivos passados na linha de comando.
Uso: python3 dedupe.py a2_arco21.txt ..."""
import sys,glob,re
SUF=[' today',' again',' now',' here',' this time',' for me']
def tk(path):
    out=[]
    for l in open(path,encoding='utf-8'):
        if l.startswith('T: '):out.append(('T',l[3:].split(' | ')[0].strip()))
        elif l.startswith('K: '):out.append(('K',l[3:].split(' | ')[0].strip()))
    return out
mine=set(sys.argv[1:]);seen={'T':set(),'K':set()}
for f in sorted(glob.glob('*_arco*.txt')):
    if f in mine:continue
    for k,v in tk(f):seen[k].add(v.lower())
for f in sorted(mine):
    L=open(f,encoding='utf-8').read().split('\n');ch=0
    for i,l in enumerate(L):
        if l[:3] in('T: ','K: '):
            k=l[0];a=l[3:].split(' | ');v=a[0].strip()
            if v.lower() in seen[k]:
                base=v.rstrip('.?!');end=v[len(base):]
                for s in SUF:
                    n=base+s+end
                    if n.lower() not in seen[k]:v=n;break
                else:v=base+' (2)'+end
                a[0]=v;L[i]=l[:3]+' | '.join(a);ch+=1
            seen[k].add(v.lower())
    open(f,'w',encoding='utf-8').write('\n'.join(L))
    print(f,'renomeados:',ch)
