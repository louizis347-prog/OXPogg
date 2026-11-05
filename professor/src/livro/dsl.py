"""Ferramentas de autoria do livro: monta aulas de 12 quadros e valida a estrutura."""
import json,os,re
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
OUT=R+'/data/livro/lessons';os.makedirs(OUT,exist_ok=True)
TAGS=['Abertura','Aquecimento','Leitura','Compreensão','Gramática','Prática','Vocabulário','Verbos','Escuta e diálogo','Fala','Escrita','Revisão e exame']
def f(tag,title,*blocks):return dict(tag=tag,title=title,blocks=list(blocks))
def p(t):return dict(type='p',t=t)
def h(t):return dict(type='h',t=t)
def ul(*items):return dict(type='ul',items=list(items))
def box(kind,t,body):return dict(type='box',kind=kind,t=t,body=body)
def table(head,rows,cap=''):return dict(type='table',head=head,rows=rows,cap=cap)
def words(*items):return dict(type='words',items=[list(i) for i in items])
def vocab(*items):return dict(type='vocab',items=list(items))
def verbs(*items):return dict(type='verbs',items=list(items))
def news(headline,paras,kicker='NEWS',by='',gloss=()):return dict(type='news',headline=headline,paras=list(paras),kicker=kicker,by=by,gloss=[list(g) for g in gloss])
def bio(name,paras,years='',facts=(),gloss=()):return dict(type='bio',name=name,paras=list(paras),years=years,facts=[list(x) for x in facts],gloss=[list(g) for g in gloss])
def poem(title,lines,by='',gloss=()):return dict(type='poem',title=title,lines=list(lines),by=by,gloss=[list(g) for g in gloss])
def comic(title,panels,gloss=(),say=''):return dict(type='comic',title=title,panels=list(panels),gloss=[list(g) for g in gloss],say=say)
def mail(frm,to,subject,paras,gloss=()):return dict(type='mail',**{'from':frm},to=to,subject=subject,paras=list(paras),gloss=[list(g) for g in gloss])
def ad(title,lines,gloss=()):return dict(type='ad',title=title,lines=list(lines),gloss=[list(g) for g in gloss])
def iv(intro,qa,gloss=()):return dict(type='iv',intro=intro,qa=[list(x) for x in qa],gloss=[list(g) for g in gloss])
def dialog(title,lines):return dict(type='dialog',title=title,lines=[list(l) for l in lines])
def mcq(items,title=''):return dict(type='mcq',title=title,items=[dict(q=q,opts=o,ans=a,why=w) for q,o,a,w in items])
def tfng(items,title=''):return dict(type='tfng',title=title,items=[dict(q=q,ans=a,why=w) for q,a,w in items])
def gap(items,title='',bank=None):return dict(type='gap',title=title,bank=bank,items=[dict(s=s,a=a,why=w,**({'say':sy} if sy else {})) for s,a,w,sy in items])
def match(pairs,title=''):return dict(type='match',title=title,pairs=[list(x) for x in pairs])
def order(items,title=''):return dict(type='order',title=title,items=[dict(words=w,ans=a,pt=pt) for w,a,pt in items])
def speak(prompts,title='Speaking'):return dict(type='speak',title=title,prompts=[dict(q=q,pt=pt,model=m) for q,pt,m in prompts])
def write(task,model,checklist,words_=''):return dict(type='write',task=task,model=model,checklist=list(checklist),words=words_)
def pron(title,items):return dict(type='pron',title=title,items=[dict(label=a,note=b,words=c) for a,b,c in items])

def validate(L):
    e=[]
    if len(L['frames'])!=12:e.append('quadros=%d'%len(L['frames']))
    for i,fr in enumerate(L['frames'],1):
        if not fr['blocks']:e.append('quadro %d vazio'%i)
        if fr['tag']!=TAGS[i-1]:e.append('quadro %d tag %s'%(i,fr['tag']))
        for b in fr['blocks']:
            t=b['type']
            if t=='mcq':
                for it in b['items']:
                    if not 0<=it['ans']<len(it['opts']):e.append('mcq ans q%d'%i)
            if t=='tfng':
                for it in b['items']:
                    if it['ans'] not in('T','F','NG'):e.append('tfng ans q%d'%i)
            if t=='gap':
                for it in b['items']:
                    n=len(re.findall(r'___+',it['s']));a=it['a'] if isinstance(it['a'],list) else [it['a']]
                    if n!=len(a):e.append('gap lacunas≠respostas q%d: %s'%(i,it['s'][:30]))
            if t=='order':
                for it in b['items']:
                    if sorted(it['ans'].split())!=sorted(it['words']):e.append('order palavras≠resposta q%d'%i)
            if t=='match' and len({x[1] for x in b['pairs']})!=len(b['pairs']):e.append('match respostas repetidas q%d'%i)
    # vocabulário-alvo no texto
    voc=[v['w'] for fr in L['frames'] for b in fr['blocks'] if b['type']=='vocab' for v in b['items']]
    if L['targets'].get('genre')!='Revisão' and len(voc)<L['targets'].get('words_min',5):e.append('vocabulário=%d'%len(voc))
    return e

def save(L):
    err=validate(L)
    if err:raise SystemExit('%s: %s'%(L['id'],'; '.join(err)))
    json.dump(L,open(OUT+'/%s.json'%L['id'],'w'),ensure_ascii=False,separators=(',',':'))
    return L

def lesson(id,title,cefr,level,unit,focus,targets,frames):
    return save(dict(id=id,title=title,cefr=cefr,level=level,unit=unit,focus=focus,targets=targets,frames=frames))

def write_index(ids_titles):
    json.dump({'lessons':[dict(id=i,title=t) for i,t in ids_titles]},open(OUT+'/index.json','w'),ensure_ascii=False,separators=(',',':'))
def text(title,paras,kicker='',by='',gloss=()):return dict(type='text',title=title,paras=list(paras),kicker=kicker,by=by,gloss=[list(g) for g in gloss])
def info(title,items,note='',gloss=()):return dict(type='info',title=title,items=[list(i) for i in items],note=note,gloss=[list(g) for g in gloss])
