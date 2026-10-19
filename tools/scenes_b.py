# -*- coding: utf-8 -*-
# "Monte a cena" para as continuações do B1 em diante (objetos e lugares sorteados por episódio; ordens no nível do curso).
import json,glob,sys,random
sys.path.insert(0,'/tmp/claude-0/-home-user-OXPogg/097f2c11-a1d9-5802-aa7c-396fb7b01940/scratchpad')
import reg3 as r
O=[('☕','coffee','o café','it'),('🗺️','map','o mapa','it'),('🧳','bag','a mala','it'),('📱','phone','o celular','it'),('📕','book','o livro','it'),('🔑','key','a chave','it'),('🎒','backpack','a mochila','it'),('☂️','umbrella','o guarda-chuva','it'),('🎁','gift','o presente','it'),('💡','lamp','a luminária','it'),('📷','camera','a câmera','it'),('🧢','cap','o boné','it'),('🍎','apple','a maçã','it'),('🕰️','clock','o relógio','it'),('🔦','flashlight','a lanterna','it'),('🧸','toy','o brinquedo','it')]
S=[('🪑','chair','on the chair','na cadeira'),('🚌','bus','on the bus','no ônibus'),('🚪','door','next to the door','ao lado da porta'),('🛏️','bed','under the bed','embaixo da cama'),('📦','box','in the box','na caixa'),('🪟','window','by the window','perto da janela'),('🛒','cart','in the cart','no carrinho'),('🌳','tree','under the tree','embaixo da árvore'),('🛋️','sofa','on the sofa','no sofá'),('🧺','basket','in the basket','na cesta'),('📚','shelf','on the shelf','na prateleira'),('🚕','taxi','in the taxi','no táxi')]
def cap(s):return s[0].upper()+s[1:]
def pron(o):return 'a' if o[2].startswith('a ') else 'o'
def sent(level,steps,it,sp):
    # devolve (say[], pt[]) conforme o nível
    en=[];pt=[]
    def A(i):return it[i][1]
    def Ap(i):return it[i][2]
    def P(j):return sp[j][2]
    def Pp(j):return sp[j][3]
    if level=='b1':
        w=[('First, put the %s %s.','Primeiro, ponha %s %s.'),('Then move the %s %s.','Depois, mova %s %s.'),('After that, put the %s %s.','Depois disso, ponha %s %s.')]
        for n,(i,j) in enumerate(steps):
            en.append(w[n][0]%(A(i),P(j)));pt.append(w[n][1]%(Ap(i),Pp(j)))
    elif level=='b2':
        w=[('Before you leave, make sure the %s is %s.','Antes de sair, certifique-se de que %s está %s.'),('And put the %s %s, please.','E ponha %s %s, por favor.'),('Finally, check that the %s is %s.','Por fim, confira se %s está %s.')]
        for n,(i,j) in enumerate(steps):
            en.append(w[n][0]%(A(i),P(j)));pt.append(w[n][1]%(Ap(i),Pp(j)))
    elif level=='c1':
        i,j=steps[0];en.append('Unless the %s is already %s, put it there.'%(A(i),P(j)));pt.append('A menos que %s já esteja %s, ponha-%s lá.'%(Ap(i),Pp(j),pron(it[i])))
        for (i,j) in steps[1:]:
            en.append('Then leave the %s %s.'%(A(i),P(j)));pt.append('Depois deixe %s %s.'%(Ap(i),Pp(j)))
    else:
        w=[('Having left the %s %s,','Depois de deixar %s %s,'),('carry the %s %s,','leve %s %s,'),('and finally set the %s %s.','e, por fim, coloque %s %s.')]
        parts=[];ptp=[]
        for n,(i,j) in enumerate(steps):
            parts.append(w[n][0]%(A(i),P(j)));ptp.append(w[n][1]%(Ap(i),Pp(j)))
        en=[' '.join(parts)];pt=[' '.join(ptp)]
    return en,pt
def build(level,rnd):
    its=rnd.sample(range(len(O)),4);sps=rnd.sample(range(len(S)),4)
    items=[[O[i][0],O[i][1]] for i in its];spots=[[S[j][0],S[j][1]] for j in sps]
    it=[O[i] for i in its];sp=[S[j] for j in sps]
    sizes={'b1':[2,2,3],'b2':[2,2,3],'c1':[2,3,3],'c2':[3,3,3]}[level]
    rounds=[]
    for n in sizes:
        ii=rnd.sample(range(4),n);jj=rnd.sample(range(4),n)
        steps=[[ii[k],jj[k]] for k in range(n)]
        en,pt=sent(level,steps,it,sp)
        extra=[x for x in range(4) if x not in ii]
        rounds.append({'say':en,'pt':pt,'steps':steps,'items':ii+extra[:1]})
    return {'k':'scenebuild','title':'Monte a cena','say':'Ouça as ordens e coloque cada objeto no lugar certo.','intro':'Ouça com atenção. Toque no objeto e depois no lugar.','items':items,'spots':spots,'rounds':rounds}
def run(cid,level):
    it=[]
    for f in sorted(glob.glob('/home/user/OXPogg/data/%s_*.json'%cid)): it+=json.load(open(f))
    n=0
    for x in it:
        if not x.get('xof') or any(s['k']=='scenebuild' for s in x['fr']): continue
        rnd=random.Random(x['xof']*13+len(level))
        sb=build(level,rnd);fr=x['fr']
        pos=next((i+1 for i,s in enumerate(fr) if s['k']=='wlat'),len(fr))
        fr.insert(pos,sb);n+=1
    tmp='/tmp/_sb_%s.json'%cid;json.dump(it,open(tmp,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    r.data(cid,tmp);print(cid,'scenebuild em',n)
if __name__=='__main__':
    for c,l in [('en-b1','b1'),('en-b2','b2'),('en-c1','c1'),('en-c2','c2')]: run(c,l)
