import pprint
def O(en,pt,ok,fb): return {'en':en,'pt':pt,'ok':ok,'fb':fb}
def R(en,pt,reply): return {'en':en,'pt':pt,'reply':reply}
def w(f,s): open('supp5/'+f,'w',encoding='utf-8').write(s)
def V(v,ic,pt,note,a,b,c,d):
    return {'v':v,'ic':ic,'pt':pt,'note':note,'forms':[{'k':'eu · você · nós · eles','en':a[0],'ex':a[1],'pt':a[2]},{'k':'ele · ela','en':b[0],'ex':b[1],'pt':b[2]},{'k':'passado','en':c[0],'ex':c[1],'pt':c[2]},{'k':'-ing','en':d[0],'ex':d[1],'pt':d[2]}]}
def emit(n,SUPP,Y,X,Z,S):
    w('s%03d.py'%n,'"""Suplemento Quest v5 aula %d."""\nSUPP = '%n+pprint.pformat(SUPP,width=170)+'\n')
    Y['sentences']=[[{'en':e,'pt':p} for e,p in par] for par in S]
    w('y%03d.py'%n,'"""Bloco complementar aula %d."""\nY = '%n+pprint.pformat(Y,width=170)+'\n')
    w('x%03d.py'%n,'"""Quest v5 aula %d (x)."""\nX = '%n+pprint.pformat(X,width=170)+'\n')
    w('z%03d.py'%n,'"""Quest v5 aula %d (z)."""\nZ = '%n+pprint.pformat(Z,width=170)+'\n')
