"""Estrutura de autoria por 'cartão': o autor escreve o conteúdo único da aula; a estrutura monta os 12 quadros,
gera exercícios de reciclagem (ordenar, ligar, vocabulário) e valida contra o plano do currículo (verbos, phrasal verbs, expressões, pronúncia, vocabulário)."""
import json,os,re
from dsl import *
CUR=json.load(open(R+'/data/livro/curriculo.json'))
PLAN={x['id']:x for x in CUR['lessons']}
UNIT={u['id']:u for u in CUR['units']}
CEFR={'A0':'Pré-A1','A1':'A1','A2':'A2','B1':'B1','B2':'B2','C1':'C1','C2':'C2'}
NW={'A0':6,'A1':8,'A2':10,'B1':12,'B2':14,'C1':16,'C2':18}
SK={'Leitura':'ler textos curtos e achar informação (IELTS Reading, TOEFL Reading)','Escuta':'ouvir e anotar informações (IELTS Listening, TOEFL Listening)','Fala':'responder em frases completas (IELTS Speaking, TOEFL Speaking)','Escrita':'escrever frases claras e corretas (IELTS Writing, TOEFL Writing)'}
LEVEL_EXAM={'A0':'Nesta fase você ainda não faz as provas, mas cada habilidade que treina aqui é a base delas.','A1':'Você ainda não faz as provas, mas já treina o formato de tarefas curtas que elas usam.','A2':'Você começa a praticar tarefas curtas no formato das provas.'}
def V(w,pos,pt,ex,expt,note=None):
    d=dict(w=w,pos=pos,pt=pt,ex=ex,expt=expt)
    if note:d['note']=note
    return d
def VB(v,pt,forms,note=None):
    d=dict(v=v,pt=pt,forms=[list(x) for x in forms])
    if note:d['note']=note
    return d
def clean(s):return re.sub(r'[.!?,;:“”"]','',s).replace('’',"'")
def shuffle(ws,seed):
    ws=ws[:];k=(seed%max(1,len(ws)-1))+1;return ws[k:]+ws[:k] if ws[k:]+ws[:k]!=ws else ws[::-1]
def auto_order(dlg,seed,n=2):
    c=[l for l in dlg if 3<=len(clean(l[1]).split())<=7]
    c=sorted(c,key=lambda l:len(l[1]))[:n]
    return [(shuffle(clean(l[1]).split(),seed+i),clean(l[1]),l[2]) for i,l in enumerate(c)]
def auto_match(vocab,n=5):
    seen=set();out=[]
    for v in vocab:
        if v['pt'] not in seen and len(out)<n:seen.add(v['pt']);out.append((v['w'],v['pt']))
    return out
def auto_mcq(vocab,seed,n=4):
    items=[]
    for i,v in enumerate(vocab[:n]):
        others=[x['pt'] for x in vocab if x['pt']!=v['pt']]
        o=[others[(i+k)%len(others)] for k in (0,2)];o=list(dict.fromkeys(o))
        while len(o)<2:o.append(others[-1])
        opts=[v['pt']]+o[:2];a=(seed+i)%3;opts.insert(a,opts.pop(0))
        items.append(('What does “%s” mean?'%v['w'],opts,a,'**%s** = %s.'%(v['w'],v['pt'])))
    return items

def _used(skip):
    s={}
    for fn in os.listdir(OUT):
        if not fn.endswith('.json') or fn=='index.json' or fn[:-5]==skip:continue
        d=json.load(open(OUT+'/'+fn))
        for fr in d['frames']:
            for b in fr['blocks']:
                if b['type']=='vocab':
                    for v in b['items']:s[v['w'].lower()]=d['id']
    return s
def fresh(n,skip,avoid=()):
    from pool import POOL
    from pool2 import POOL2
    used=_used(skip);out=[]
    for p in POOL+POOL2:
        w=p[0].lower()
        if '(' in w or w in used or w in avoid or any(o['w'].lower()==w for o in out):continue
        out.append(V(p[0],'word',p[1],p[2],p[3]))
        if len(out)==n:break
    return out
def chunks(dl,have,n=3):
    out=[]
    for mx in(7,12):
        for l in dl:
            k=len(l[1].replace('?','').replace('!','').split())
            if 2<=k<=mx and l[1].lower() not in have and l[1] not in [o[0] for o in out]:out.append((l[1],l[2]))
            if len(out)==n:return out
    return out
def L(id,title,*,goal,read,tf,mc,gram,gaps,vocab,dlg,pron,speak_,wr,rev,exam,teach,verbs=None,pv=None,expr=None,warm=None,vnote=None,readbox=None,gaprint=None):
    P=PLAN[id];lv=P['level'];seed=P['g']
    # ---- verificações contra o plano ----
    nw=NW[lv]
    if len(vocab)!=nw:raise SystemExit('%s: vocabulário=%d, cota=%d'%(id,len(vocab),nw))
    used=_used(id);seenw=set();legacy=id.startswith(('A0-','A1-'))
    for i,v in enumerate(vocab):
        w=v['w'].lower()
        if w in used or w in seenw:
            if not legacy:
                bad=[x['w'] for x in vocab if x['w'].lower() in used]
                raise SystemExit('%s: palavras repetidas %s'%(id,', '.join(bad)))
            r=fresh(1,id,avoid=seenw|{x['w'].lower() for x in vocab})[0];vocab[i]=r;w=r['w'].lower()
        seenw.add(w)
    have_v=[x['v'] for x in (verbs or [])]
    for v in P['verbs']:
        if v not in have_v:raise SystemExit('%s: falta o verbo %s'%(id,v))
    have_pv=[x['w'] for x in (pv or [])]
    for v in P['pv']:
        if v not in have_pv:raise SystemExit('%s: falta o phrasal verb %s'%(id,v))
    exprs=expr or []
    for e in P['expr']:
        if not any(e.lower().replace('’',"'") in (x[0].lower().replace('’',"'")) for x in exprs):raise SystemExit('%s: falta a expressão %s'%(id,e))
    targets=dict(grammar=P['focus'],pron=P['pron'],verbs=P['verbs'],pv=P['pv'],expr=P['expr'],words=[v['w'] for v in vocab],field=P['field'].split(' (')[0],genre=P['genre'],skill=P['skill'],words_min=nw)
    skill=SK.get(P['skill'],'integrar leitura, escuta, fala e escrita')
    f1=f('Abertura','Lesson %d · %s'%(P['n'],title),
      box('look','Nesta aula',['**Foco:** '+P['focus']+'.']+(['**Verbos:** '+', '.join(P['verbs'])+'.'] if P['verbs'] else [])+(['**Phrasal verbs:** '+', '.join(P['pv'])+'.'] if P['pv'] else [])+(['**Expressões:** '+'; '.join(P['expr'])+'.'] if P['expr'] else [])+['**Pronúncia:** '+P['pron']+'.','**%d palavras novas** (%s).'%(nw,P['field'].split(' (')[0].lower()),'**Texto do dia:** '+P['genre'].lower()+'.']),
      p('**Objetivo de comunicação (%s):** %s'%(CEFR[lv],goal)),
      box('exam','Ponte para as provas',[LEVEL_EXAM.get(lv,''),'Esta aula treina **%s**.'%skill]))
    f2=f('Aquecimento',(warm or ('Warm-up · Say the words',''))[0],
      p((warm or ('', 'Toque em 🔊, ouça e repita cada palavra. Depois tente adivinhar o sentido.'))[1]),
      words(*[(v['w'],v['pt']) for v in vocab]))
    f3=f('Leitura',read[0],read[1],*( [readbox] if readbox else []))
    f4=f('Compreensão','Did you understand?',tfng(tf),mcq(mc,'Vocabulary in context'))
    f5=f('Gramática',gram[0],*gram[1])
    om=auto_order(dlg[1],seed);orders=[order(om,'Put the words in order')] if om else []
    f6=f('Prática','Practice',gap([(s,a,w,sy) for s,a,w,sy in [g if len(g)==4 else (g[0],g[1],g[2],None) for g in gaps]],'Complete the sentences'),match(auto_match(vocab),'Match the word to its meaning'),*orders)
    b7=[vocab_(vocab)]
    ck=chunks(dlg[1],[e[0].lower() for e in exprs])
    items7=['**%s** — %s'%(e[0],e[1]) for e in exprs]+['**%s** — %s'%c for c in ck]
    if len(items7)<3:raise SystemExit('%s: poucas expressões no quadro (%d)'%(id,len(items7)))
    b7.append(box('culture','Expressões desta aula',items7))
    if vnote:b7.append(box('tip','Dica',vnote))
    f7=f('Vocabulário','Words and expressions',*b7)
    b8=[]
    if verbs:b8.append(verbs_(verbs))
    if pv:b8.append(table(['Phrasal verb','Significado','Exemplo'],[['**%s**'%x['w'],x['pt'],'%s — %s'%(x['ex'],x['expt'])] for x in pv],'Phrasal verbs'))
    if not b8:b8.append(box('tip','Verbos desta aula','Esta aula revisa verbos já vistos dentro das frases do diálogo e dos exercícios. Observe: **%s**.'%(', '.join(P['verbs']) or 'be, have, do')))
    f8=f('Verbos','Verbs in focus',*b8)
    f9=f('Escuta e diálogo',dlg[0],dialog(dlg[0],dlg[1]),pron_(P['pron'],pron[0],pron[1]))
    f10=f('Fala','Speaking',speak(speak_))
    f11=f('Escrita','Writing',write(wr[0],wr[1],wr[2],wr[3] if len(wr)>3 else ''))
    f12=f('Revisão e exame','Review · Exam strategy · Teacher’s note',mcq(auto_mcq(vocab,seed)+rev,'Check yourself'),box('exam','Estratégia para as provas',exam),box('teach','Nota para o futuro professor',teach))
    return lesson(id,title,CEFR[lv],lv,P['unit'],P['focus'],targets,[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12])
def vocab_(v):return dict(type='vocab',items=v)
def verbs_(v):return dict(type='verbs',items=v)
def pron_(label,note,words_):return dict(type='pron',title='Pronúncia: '+label,items=[dict(label=label,note=note,words=words_)])

def build_index():
    ids=sorted(fn[:-5] for fn in os.listdir(OUT) if fn.endswith('.json') and fn!='index.json')
    out=[]
    for i in ids:
        d=json.load(open(OUT+'/%s.json'%i));out.append((i,d['title']))
    write_index(out);return out
