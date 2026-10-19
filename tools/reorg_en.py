# -*- coding: utf-8 -*-
# Reorganiza os pares original + continuação do curso de inglês: conteúdo ↔ prática, cultura trabalhada, cortes sob medida.
# Uso: git checkout -- data  (partir do estado anterior)  &&  python3 tools/reorg_en.py en-a1 en-a2 ...
import json,glob,sys,os,re,copy,random
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
HERE=os.path.dirname(os.path.abspath(__file__));sys.path.insert(0,os.path.join(HERE,'rdg'))
import reg3 as r
try:
    import importlib
    A1T={}
    for f in sorted(glob.glob(os.path.join(HERE,'rdg','a1_*.py'))):
        for k,v in importlib.import_module(os.path.basename(f)[:-3]).D.items(): A1T[k]=v[0]
    import play_a1
    for k,v in play_a1.P.items(): A1T[k]=A1T.get(k) or v[0].replace('Missão: ','').capitalize()
except Exception as e: A1T={}
KNOWN={'cover','review','read','words','wsent','verbs','scene','dquiz','pat','sbuild','lplay','tdlg','convo','produce','soundlab','cexp','xpr','ctxv','vplay','scenebuild','wlat','rdg','rdgplay','follow','lexpack','cultq','cult','bridge','pbridge'}
def cap(s,field,n):
    if isinstance(s.get(field),list) and len(s[field])>n: s[field]=s[field][:n]
def first(fr,k):
    for s in fr:
        if s['k']==k: return s
def words(t,n=40):
    w=t.split();
    if len(w)<=n: return t
    cut=' '.join(w[:n]);m=max(cut.rfind('. '),cut.rfind('! '))
    return cut[:m+1] if m>20 else cut+'…'
def author(cw): return str(cw.get('by','')).split(' · ')[0].strip()
def year(cw):
    y=str(cw.get('year','')).strip();return int(y) if re.fullmatch(r'\d{3,4}',y) else None
def run(cid):
    it=[]
    for f in sorted(glob.glob('/home/user/OXPogg/data/%s_*.json'%cid)): it+=json.load(open(f))
    if any(x.get('reorg') for x in it): print(cid,'já reorganizado');return
    mains={x['n']:x for x in it if not x.get('xof')}
    pool_auth=sorted({author(m['fr'][0]['cw']) for m in mains.values() if m.get('fr') and m['fr'][0].get('cw') and author(m['fr'][0]['cw'])})
    nm=0
    for x in it:
        if not x.get('xof') or x['xof'] not in mains: continue
        m=mains[x['xof']];mf=m['fr'];xf=x['fr']
        cov=first(mf,'cover');cw=(cov or {}).get('cw')
        rnd=random.Random(x['xof'])
        # ---- ORIGINAL ----
        M={k:first(mf,k) for k in ['cover','review','read','words','wsent','verbs','scene','dquiz','pat','sbuild','lplay','tdlg','convo','produce']}
        X={k:first(xf,k) for k in ['cover','rdg','rdgplay','soundlab','cexp','xpr','ctxv','vplay','scenebuild','wlat','scene','pat','lexpack','pbridge','bridge']}
        if M['read']: M['read']['s']=M['read']['s'][:9]
        cap(M['dquiz'],'items',3) if M['dquiz'] else 0
        cap(M['lplay'],'rounds',4) if M['lplay'] else 0
        cultq=None
        if cw and author(cw):
            au=author(cw);opts=[a for a in rnd.sample(pool_auth,min(8,len(pool_auth))) if a!=au][:2]
            if len(opts)==2:
                o=[au]+opts;rnd.shuffle(o)
                cultq={'k':'cultq','title':'Cultura em 1 toque','pa':cw.get('pa'),'work':cw['work'],'tag':cw.get('kind'),'q':{'q':'Quem criou “%s”?'%cw['work'],'o':o,'a':o.index(au),'why':'“%s” é de %s%s.'%(cw['work'],au,' (%s)'%cw['year'] if cw.get('year') else '')},'say':'Uma pergunta rápida sobre a obra de hoje!'}
        vp=X['vplay']
        if vp:
            n7=0
            for it2 in vp['items']:
                keep=[]
                for fm in it2['f']:
                    if n7<7: keep.append(fm);n7+=1
                it2['f']=keep
            vp['items']=[i for i in vp['items'] if i['f']]
        cx=X['ctxv'];ctx_main=None
        if cx:
            ctx_main=copy.deepcopy(cx);ctx_main['items']=cx['items'][:4];cx['items']=cx['items'][4:] or cx['items'][-2:]
        order=['cover']+(['cultq'] if cultq else [])+['review','read','lplay','words','wsent','verbs','vplay','scene','dquiz','ctxv','tdlg','convo','produce']
        pool={**M,'cultq':cultq,'vplay':vp,'ctxv':ctx_main}
        newm=[pool[k] for k in order if pool.get(k)]
        newm+= [s for s in mf if s['k'] not in ('pat','sbuild') and not any(s is q for q in newm)]
        # ---- CONTINUAÇÃO ----
        title=A1T.get(x['xof'])
        pat=copy.deepcopy(M['pat']) if M['pat'] else None
        if X['pat']:
            if pat: pat['pages']=(pat['pages'][:2]+X['pat']['pages'][:1])
            else: pat=X['pat']
        if not title: title=(pat or {}).get('title') or m['t']
        sb=M['sbuild'];
        if sb: cap(sb,'rounds',5)
        for k,f,n in [('cexp','items',3),('xpr','items',3),('wlat','items',2),('scenebuild','rounds',3)]:
            if X[k]: cap(X[k],f,n)
        if X['scene']: cap(X['scene'],'lines',6)
        cult=None
        if cw and cw.get('fact'):
            y=year(cw)
            if y:
                ys={y};
                while len(ys)<3:
                    d=rnd.choice([-1,1])*rnd.randint(4,45);yy=y+d
                    if 0<yy<=2025 and abs(yy-y)>=3:ys.add(yy)
                o=[str(v) for v in ys];rnd.shuffle(o);ans=o.index(str(y));q='Em que ano foi criado(a) “%s”?'%cw['work']
            elif author(cw) and len(pool_auth)>=3:
                au=author(cw);o=[au]+[a for a in rnd.sample(pool_auth,min(8,len(pool_auth))) if a!=au][:2];rnd.shuffle(o);ans=o.index(au);q='Quem criou “%s”?'%cw['work'];y=cw.get('year') or ''
            else:
                o=None
            if o:
                cult={'k':'cult','title':'%s Você sabia?'%cw['fact'][0],'pa':cw.get('pa'),'work':cw['work'],'tag':cw.get('kind'),'fact':words(cw['fact'][2]),'q':{'q':q,'o':o,'a':ans,'why':'“%s”: %s.'%(cw['work'],o[ans])},'say':'Mais uma curiosidade cultural!'}
        xc=X['cover'] or {}
        if xc: xc['sub']='Regra, som, expressões e escrita';xc['say']='Hoje vamos entender o porquê do que você aprendeu!'
        rd=X['rdgplay'] or X['rdg']
        uniq=[s for s in xf if s['k'] not in KNOWN]
        u1=uniq[:1];u2=uniq[1:]
        newx=[xc] if xc else []
        newx+=[s for s in (X['pbridge'],X['bridge']) if s]
        newx+=[s for s in (cult,rd,pat,sb,X['soundlab'],X['cexp'],X['ctxv']) if s]
        newx+=u1+[s for s in (X['xpr'],) if s]+u2+[s for s in (X['wlat'],X['scene'],X['scenebuild'],X['lexpack']) if s]
        # ilustração em toda tela que não tem: banner com a arte da obra do dia
        if cw and cw.get('pa'):
            for s in newm+newx:
                if s['k'] in ('rdg','cexp','soundlab','wlat','sbuild','dquiz','xpr') and 'ban' not in s and 'banner' not in s:
                    s['banner']={'pa':cw['pa']}
        m['fr']=newm;x['fr']=newx;m['reorg']=1;x['reorg']=1
        x['t']=title;x['s']='Regra, som, expressões e escrita';x['p']='O porquê de %s: regra, som, expressões e escrita na tela.'%m['t']
        nm+=1
    tmp='/tmp/_reorg_%s.json'%cid;json.dump(it,open(tmp,'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
    r.data(cid,tmp);print(cid,'pares reorganizados',nm)
if __name__=='__main__':
    for c in sys.argv[1:]: run(c)
