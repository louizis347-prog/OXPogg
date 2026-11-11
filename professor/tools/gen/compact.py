import sys,random
sys.path.insert(0,'/tmp/gen');sys.path.insert(0,'/home/user/OXPogg/professor/src')
from dsl import *
def _garble(en,seed):
    w=en.split();r=random.Random(seed)
    if len(w)<3: return en+' '+en
    a=w[:];
    for _ in range(5):
        r.shuffle(a)
        if a!=w: break
    return ' '.join(a)
def _drop(en):
    w=en.split();
    if len(w)<4: return ' '.join(w[::-1])
    i=len(w)//2;return ' '.join(w[:i]+w[i+1:])
def compact(n,m):
    L=m['lines'];you=m['you'];npc=m['npc']
    def q(i): return L[i]
    def say(i,en=True):
        who=L[i][0];nm=you if who=='You' else npc
        return ('“%s” says %s.'%(L[i][1],nm)) if en else ('“%s”, diz %s.'%(L[i][2],nm))
    P=[m['open'],[(say(i),say(i,False)) for i in (0,1,2)],[(say(i),say(i,False)) for i in (3,4,5)],[(say(i),say(i,False)) for i in (6,7,8)],[(say(i),say(i,False)) for i in (9,10)]+m['close']]
    S=[[ (a,b) for a,b in par] for par in P]
    cu=m['cu']
    SUPP={'reg':m['reg'],'badge':m['badge'],
     'culture':culture(cu['hook'],cu['mf'],cu['wild'],cu['compare'],cu['quiz']),
     'reading':reading(m['rtitle'],m['gloss'],m['fast'],m['scan'],m['tf'],m['order'],m['ctx'],m['chunks'],m['think'],S),
     'errors':errs(m['errors']),'homework':m['homework'],
     'homework_items':['Write: '+m['hw'],'Say aloud: '+m['chunks'][0]+' '+m['chunks'][1],'Listen to the dialogue and shadow '+npc+'.','Review: '+' / '.join(w[0] for w in m['vocab'])+'.'],'convo':None}
    Y={'soundlab':lab(*m['lab']),'cards':cards(m['cards'])}
    X={'key':m['key'],'vocab':vocab(m['vocab']),'molds':molds(m['molds']),'sounds':sounds(m['sounds']),
       'role':role([(L[i][1],o) for i,o in zip((0,2,4,6),m['role'])],m['change']),
       'writing':writing(m['wtask'],m['wmodel'],m['kw'],['Usou: '+x[0].lower()+'.' for x in m['molds']]),
       'scenes':{'pool':m['pool'],'npc':{'g':m['g'],'role':m['crole']},'you':{'g':m['yg']}}}
    vb=[];vg_=[]
    for (v,ic,pt,note,third,past,ing,p1,p3,pp,pg) in m['verbs']:
        vb.append((v,ic,pt,note,(v,'We %s every day.'%v,'Nós %s todo dia.'%p1),(third,'She %s every day.'%third,'Ela %s todo dia.'%p3),(past,'I %s yesterday.'%past,'Eu %s ontem.'%pp),(ing,'He is %s now.'%ing,'Ele está %s agora.'%pg)))
    for k,(v,ic,pt,note,third,past,ing,p1,p3,pp,pg) in enumerate(m['verbs'][:4]):
        if k==0: vg_.append(('Yesterday I ___.','Ontem eu %s.'%pp,[v,past,ing],1,'Passado de %s: %s.'%(v,past)))
        if k==1: vg_.append(('She ___ every day.','Ela %s todo dia.'%p3,[v,third,ing],1,'Com she, o verbo leva -s: %s.'%third))
        if k==2: vg_.append(('He is ___ now.','Ele está %s agora.'%pg,[v,past,ing],2,'is + -ing: %s.'%ing))
        if k==3: vg_.append(('We ___ every day.','Nós %s todo dia.'%p1,[past,v,ing],1,'Com we, a forma base: %s.'%v))
    Z={'verbs':verbs(vb),'verb_game':vg(vg_),'expressions':exprs([(e[0],e[1],e[2],e[3],'abcd'[i%4]) for i,e in enumerate(m['exprs'])])}
    eg_=[]
    for k,i in enumerate((0,2,4)):
        ex=m['exprs'][i];oth=[e[0] for j,e in enumerate(m['exprs']) if j!=i][:2]
        opts=[ex[0]]+oth if k==0 else (oth[:1]+[ex[0]]+oth[1:] if k==1 else oth+[ex[0]])
        eg_.append((ex[3].rstrip('.').replace('Para','Você quer')+'.',opts,opts.index(ex[0]),ex[0]+' — '+ex[1]))
    Z['expr_game']=eg(eg_)
    turns=[]
    for k,i in enumerate((0,2,4,6,8)):
        ok=L[i+1] if i+1<len(L) else L[-1]
        turns.append((L[i][1],L[i][2],(ok[1],ok[2],'Natural e claro.'),(_garble(ok[1],n*10+k),ok[2],'A ordem das palavras está errada.'),(_drop(ok[1]),ok[2],'Falta uma palavra.')))
    own={'title':m['title'],'city':m['city'],'npc':npc,'face':m['face'],'story':m['story'],'p':m['p'],'mission':m['mission'],'emo':m['emo'],'sc':m['sc'],
      'lines':L,'vocab':[(v[0],v[2],v[1]) for v in m['vocab'][:5]],'exprs':[(e[0],e[1]) for e in m['exprs']],'real':m['real'],'teaser':m['teaser'],'teaser_d':m['teaser_d']}
    lesson_own(n,SUPP,S,Y,X,Z,turns,own,m['swaps'],m['mini'])
