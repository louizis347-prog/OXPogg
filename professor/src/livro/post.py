"""Pós-processamento de cada aula: cota de palavras, verbos e expressões; palavras e verbos nunca se repetem entre aulas."""
import json,os,re
from dsl import OUT
from ext import EXT
try:
    from pools import FIELD,EXPRS,VERBS
except ImportError:
    FIELD={};EXPRS=[];VERBS=[]
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
_RES={}
_rf=os.path.join(os.path.dirname(__file__),'reserved.txt')
if os.path.exists(_rf) and not os.environ.get('COLLECT'):
    for _l2 in open(_rf):
        _a,_b=_l2.rstrip('\n').split('|',1);_RES[_b]=_a
_PL={x['id']:x for x in json.load(open(R+'/data/livro/curriculo.json'))['lessons']}
QUOTA={'A0':10,'A1':14,'A2':16,'B1':18,'B2':20,'C1':22,'C2':24}      # palavras novas por aula-núcleo
EXPR_MIN={'A0':5,'A1':6,'A2':7,'B1':8,'B2':9,'C1':10,'C2':11}      # itens no quadro "Expressões desta aula"
VERB_MIN={'A0':0,'A1':1,'A2':1,'B1':1,'B2':1,'C1':1,'C2':1}         # verbos novos por aula-núcleo (além dos listados no plano)
LEGACY=('A0-','A1-')
def _scan(skip):
    w={};v={};p={};xs=set()
    for fn in os.listdir(OUT):
        if not fn.endswith('.json') or fn=='index.json' or fn[:-5]==skip:continue
        d=json.load(open(OUT+'/'+fn))
        for fr in d['frames']:
            for b in fr['blocks']:
                if b['type']=='vocab':
                    for x in b['items']:w[x['w'].lower()]=d['id']
                if b['type']=='verbs':
                    for x in b['items']:v[x['v'].lower()]=d['id']
                if b['type']=='box' and b['t'] in('Expressões desta aula','Novas expressões da revisão'):
                    for i in b['body']:
                        if '**' in i:xs.add(re.sub(r'[^a-z]','',i.split('**')[1].lower()))
                if b['type']=='table' and b.get('cap')=='Phrasal verbs':
                    for r in b['rows']:p[r[0].replace('*','').lower()]=d['id']
    return w,v,p,xs
def _strs(o):
    if isinstance(o,str):return [o]
    if isinstance(o,dict):return [x for v in o.values() for x in _strs(v)]
    if isinstance(o,list):return [x for v in o for x in _strs(v)]
    return []
def _V(r):
    q=r.split(';')
    if len(q)==4:q=[q[0],'word']+q[1:]
    return dict(w=q[0],pos=q[1],pt=q[2],ex=q[3],expt=q[4])
def _s(v):
    if v.endswith(('s','sh','ch','x','o')):return v+'es'
    if v.endswith('y') and v[-2] not in 'aeiou':return v[:-1]+'ies'
    return v+'s'
def fix(L):
    if L['targets'].get('genre')=='Revisão':return L
    id=L['id'];lv=L['level'];ext=EXT.get(id,{});plan=os.environ.get('PLAN')
    uw,uv,up,_usedx=_scan(id);rep=[]
    fr7=next(f for f in L['frames'] if f['tag']=='Vocabulário');vb=next(b for b in fr7['blocks'] if b['type']=='vocab')
    kept=[]
    for v in vb['items']:
        w=v['w'].lower()
        if w in uw:
            open('dropped.txt','a').write('%s|%s\n'%(id,v['w']))
            continue
        kept.append(v)
    seen={v['w'].lower() for v in kept}
    for r in ext.get('add',[]):
        v=_V(r);w=v['w'].lower()
        if w in uw or w in seen:
            continue
        seen.add(w);kept.append(v)
    if len(kept)>QUOTA[lv]:kept=kept[:QUOTA[lv]]
    filled=[]
    if os.environ.get('COLLECT'):
        open(_rf,'a').write(''.join('%s|%s\n'%(id,v['w'].lower()) for v in kept))
    elif len(kept)<QUOTA[lv]:
        fld=_PL[id]['field'].split(' (')[0]
        stems={w[:5] for w in re.findall(r'[a-z]{4,}',' '.join(_strs(L)).lower())}
        cands=[]
        for k,v in FIELD.items():
            for j,r in enumerate(v):
                q=_V(r);w=q['w'].lower()
                if w in uw or w in seen or (w in _RES and _RES[w]!=id):continue
                sc=sum(1 for t in re.findall(r'[a-z]{4,}',(q['w']+' '+q['ex']).lower()) if t[:5] in stems)
                cands.append((-(sc*2+(1 if k==fld else 0)),j,q))
        cands.sort(key=lambda c:(c[0],c[1]))
        for _,_,q in cands:
            if len(kept)>=QUOTA[lv]:break
            w=q['w'].lower()
            if w in seen:continue
            seen.add(w);kept.append(q);filled.append(q['w'])
    if filled:open(os.path.join(os.path.dirname(__file__),'fills.txt'),'a').write('%s | %s | %s\n'%(id,L['title'][:38],', '.join(filled)))
    need=QUOTA[lv]-len(kept)
    if need!=0:
        if plan:rep.append('palavras %+d'%need)
        else:raise SystemExit('%s: vocabulário=%d, cota=%d'%(id,len(kept),QUOTA[lv]))
    vb['items']=kept
    for f in L['frames']:
        if f['tag']=='Aquecimento':
            for b in f['blocks']:
                if b['type']=='words':b['items']=[[v['w'],v['pt']] for v in kept]
    for f0 in L['frames']:
        if f0['tag']=='Abertura':
            for b0 in f0['blocks']:
                if b0['type']=='box' and isinstance(b0.get('body'),list):
                    b0['body']=[re.sub(r'^\d+ palavras:',str(QUOTA[lv])+' palavras:',re.sub(r'\*\*\d+ palavras novas\*\*','**%d palavras novas**'%QUOTA[lv],i)) for i in b0['body']]
    L['targets']['words_min']=len(kept) if plan else QUOTA[lv];L['targets']['words']=[v['w'] for v in kept]
    # verbos
    f8=next(f for f in L['frames'] if f['tag']=='Verbos')
    vbk=next((b for b in f8['blocks'] if b['type']=='verbs'),None)
    have={x['v'].lower() for x in (vbk['items'] if vbk else [])}
    newv=[]
    for r in ext.get('verbs',[]):
        v,pt,a,b3=r[:4]
        if v.lower() in uv or v.lower() in have:continue
        newv.append(dict(v=v,pt=pt,forms=[['I / you / we / they '+v,a],['he / she / it '+_s(v),b3]]))
    if lv!='A0' and len(have)+len(newv)<VERB_MIN[lv]:
        for r in VERBS:
            q=r.split(';')
            if q[0].lower() in uv or q[0].lower() in have or q[0].lower() in {x['v'].lower() for x in newv}:continue
            newv.append(dict(v=q[0],pt=q[1],forms=[['I / you / we / they '+q[0],q[2]],['he / she / it '+_s(q[0]),q[3]]]));break
    if newv:
        if vbk:vbk['items']+=newv
        else:f8['blocks']=[b for b in f8['blocks'] if not(b['type']=='box' and b['t']=='Verbos desta aula')];f8['blocks'].insert(0,dict(type='verbs',items=newv))
    nverbs=len(have)+len(newv)
    if lv!='A0' and nverbs<VERB_MIN[lv]:
        if plan:rep.append('verbos %+d'%(VERB_MIN[lv]-nverbs))
        else:raise SystemExit('%s: faltam verbos (%d)'%(id,nverbs))
    # phrasal verbs
    pvs=ext.get('pv',[])
    if pvs:
        rows=[['**%s**'%a,b,'%s — %s'%(c,d)] for a,b,c,d in pvs]
        pvs=[x for x in pvs if x[0].lower() not in up]
        rows=[['**%s**'%a,b,'%s — %s'%(c,d)] for a,b,c,d in pvs]
        tb=next((b for f in L['frames'] for b in f['blocks'] if b['type']=='table' and b.get('cap')=='Phrasal verbs'),None)
        if tb:tb['rows']+=rows
        else:f8['blocks'].append(dict(type='table',head=['Phrasal verb','Significado','Exemplo'],rows=rows,cap='Phrasal verbs'))
    # expressões
    bx=next((b for b in fr7['blocks'] if b['type']=='box' and b['t']=='Expressões desta aula'),None)
    items=list(bx['body']) if bx else []
    for e in ext.get('expr',[]):
        items.append('**%s** — %s'%(e[0],e[1]))
    if len(items)<EXPR_MIN[lv]:
        have_e={re.sub(r'[^a-z]','',i.split('**')[1].lower()) for i in items if '**' in i}
        for r in EXPRS:
            if len(items)>=EXPR_MIN[lv]:break
            en,pt=r.split('=',1);k=re.sub(r'[^a-z]','',en.lower())
            if k in have_e or k in _usedx:continue
            have_e.add(k);items.append('**%s** — %s'%(en,pt));_usedx.add(k)
    if len(items)<EXPR_MIN[lv]:
        if plan:rep.append('expressões %+d'%(EXPR_MIN[lv]-len(items)))
        else:raise SystemExit('%s: expressões=%d, mínimo=%d'%(id,len(items),EXPR_MIN[lv]))
    if bx:bx['body']=items
    else:fr7['blocks'].append(dict(type='box',kind='culture',t='Expressões desta aula',body=items))
    if plan and rep:open(os.path.join(os.path.dirname(__file__),'plan_ext.txt'),'a').write('%s | %s | %s\n'%(id,L['title'][:40],'; '.join(rep)))
    return L
