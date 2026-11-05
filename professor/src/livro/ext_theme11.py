from ext import A
def W(id,s):
    rows=[]
    for p in s.split('|'):
        e,t=p.split('=');rows.append('%s;%s;%s;%s'%(e,t,e[0].upper()+e[1:]+'.',t[0].upper()+t[1:]+'.'))
    A(id,"\n".join(rows))
W('B1-L044','broken bus=ônibus quebrado|party mix-up=confusão na festa|missed cake=bolo perdido|bus delay=atraso do ônibus|sorry text=mensagem de desculpas')
W('B1-L039','friend’s worry=preocupação do amigo')
W('B1-L045','overnight bag=mala de pernoite')
