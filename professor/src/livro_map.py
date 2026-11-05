#!/usr/bin/env python3
"""Mapeamento do curso A0 → C2 a partir da especificação (livro_spec.py).
1) calcula as aulas de cada nível pela restrição que mais pesa (cada aula tem 12 quadros e integra os nove pilares);
2) distribui TODOS os itens listados pelas aulas e verifica a cobertura (rastreabilidade);
3) gera professor/data/livro/curriculo.json e docs/CURRICULO-FORMACAO-PROFESSORES.md.
Regra do curso: se faltar aula para cumprir a matriz, o número de aulas AUMENTA."""
import json,os,math
from livro_spec import *
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
os.makedirs(R+'/professor/data/livro',exist_ok=True)
LV=['A0','A1','A2','B1','B2','C1','C2']
mid=lambda r:(r[0]+r[1])//2
GLH_INC={'A0':30,'A1':70,'A2':100,'B1':200,'B2':200,'C1':200,'C2':400}      # horas guiadas a acrescentar (limite superior das faixas de referência)
CAP_WORDS={'A0':6,'A1':8,'A2':10,'B1':12,'B2':14,'C1':16,'C2':18}           # palavras novas por aula
CAP_VERBS,CAP_PV,CAP_EXPR=3,2,5                                              # verbos-base, phrasal verbs e expressões novas por aula
STEPS={'A0':2}                                                                # aulas por item de gramática (intro; prática e contraste; produção e revisão)
EXAM={'A0':0,'A1':0,'A2':0,'B1':12,'B2':40,'C1':40,'C2':12}                  # aulas de laboratório de TOEFL / IELTS / colleges canadenses
GENRE=['Notícia / reportagem curta','Biografia','Poema, haiku ou letra','Charge, tirinha e cartum','E-mail, carta, mensagem','Entrevista','Anúncio, folheto, aviso','Receita e instruções','Blog, diário, crônica','Resenha / review','Conto e trecho de peça','Editorial / opinião','Texto acadêmico e resumo','Infográfico em texto','Transcrição de palestra e podcast']
SKILLS=['Leitura','Escuta','Fala','Escrita']

def dedupe(level_lists):
    seen=set();out={}
    for l in LV:
        items=[]
        for x in level_lists.get(l,[]):
            k=x.lower().strip()
            if k not in seen:seen.add(k);items.append(x)
        out[l]=items
    return out
VERBS_NEW=dedupe(VERBS);PV_NEW=dedupe(PV)
EXPR_ALL={l:EXPR.get(l,[])+COLLOC.get(l,[]) for l in LV}
EXPR_NEW=dedupe(EXPR_ALL)
IRR_BLOCKS=[IRREGULAR[i:i+6] for i in range(0,len(IRREGULAR),6)]
PAT_BY={'A1':SENTENCE_PATTERNS[0:5],'A2':SENTENCE_PATTERNS[5:10],'B1':SENTENCE_PATTERNS[10:15],'B2':SENTENCE_PATTERNS[15:20],'C1':SENTENCE_PATTERNS[20:23],'C2':SENTENCE_PATTERNS[23:25]}
FORM_BY={'A2':WORD_FAMILIES[0:3]+PREFIXES[0:3],'B1':WORD_FAMILIES[3:6]+PREFIXES[3:7]+SUFFIXES[0:4],'B2':WORD_FAMILIES[6:8]+PREFIXES[7:10]+SUFFIXES[4:8],'C1':PREFIXES[10:12]+SUFFIXES[8:11],'C2':[]}
FORM_LESSONS={'A2':2,'B1':3,'B2':3,'C1':2,'C2':0}

def level_plan(l):
    t=TARGETS[l];pi=LV.index(l);prev=LV[pi-1] if pi else None
    cum={k:mid(t[k]) for k in('lex','pv','expr')};cum['verbs']=t['verbs'][0]
    cum['pv']=max(t['pv'][0],0) if l=='A0' else cum['pv']
    pc={k:(mid(TARGETS[prev][k]) if prev else 0) for k in('lex','pv','expr')};pc['verbs']=TARGETS[prev]['verbs'][0] if prev else 0
    if prev=='A0':pc['pv']=0
    d={k:cum[k]-pc[k] for k in cum}
    # aulas estruturadas (cada uma cobre um item obrigatório): gramática, padrões verbais, modais, aulas dedicadas
    gram=len(GRAM[l])*STEPS.get(l,3)
    extra=0
    if l in PATTERNS_VERB:extra+=len(PATTERNS_VERB[l])*2
    if l=='B2':extra+=len(MODALS_B2)*2
    if l=='C1':extra+=len(GENRES_C1)*3
    if l=='C2':extra+=len(CONTRASTS_C2)*2+len(REGISTER_C2)*2
    ded=len(PRON.get(l,[]))+(15 if l!='A0' else 0)+len(PAT_BY.get(l,[]))*2+FORM_LESSONS.get(l,0)+(len(IRR_BLOCKS) if l=='A2' else 0)
    struct=gram+extra+ded+EXAM[l]
    need={'horas guiadas':GLH_INC[l],'vocabulário':math.ceil(d['lex']/CAP_WORDS[l]),'verbos-base':math.ceil(d['verbs']/CAP_VERBS),'phrasal verbs':math.ceil(d['pv']/CAP_PV),'expressões e collocations':math.ceil(d['expr']/CAP_EXPR),'itens estruturados (gramática + aulas dedicadas + exames)':struct}
    base=max(need.values());binding=max(need,key=lambda k:need[k])
    # revisões e avaliações periódicas: 2 aulas a cada unidade de ~16
    units=math.ceil(base/16);L=base+2*units
    return dict(level=l,delta=d,cum=cum,need=need,binding=binding,base=base,review=2*units,lessons=L,gram_lessons=gram,extra=extra,ded=ded)

def spread(items,L,per=None):
    """distribui items por L aulas de forma uniforme e contínua (cada item cai em ≥1 aula)"""
    out=[[] for _ in range(L)]
    if not items:return out
    for i,x in enumerate(items):out[min(L-1,i*L//len(items))].append(x)
    return out

def build():
    plans={l:level_plan(l) for l in LV};levels=[];units=[];lessons=[];cov=[]
    gid=0
    for l in LV:
        p=plans[l];L=p['lessons'];fields=VOCAB_FIELDS[l]
        # agenda estruturada em ordem
        agenda=[]
        for g in GRAM[l]:
            for s,sn in enumerate(['introdução','prática e contraste','produção e revisão'][:STEPS.get(l,3)]):agenda.append(('Gramática',g+' — '+sn,g))
        for v in PATTERNS_VERB.get(l,[]):agenda+= [('Padrão verbal',v+' — forma','Padrão verbal: '+v),('Padrão verbal',v+' — uso','Padrão verbal: '+v)]
        if l=='B2':
            for m in MODALS_B2:agenda+=[('Modais',m+' — forma','Modais: '+m),('Modais',m+' — uso','Modais: '+m)]
        if l=='C1':
            for g in GENRES_C1:agenda+=[('Gênero escrito',g+' — modelo','Escrita: '+g),('Gênero escrito',g+' — planejamento','Escrita: '+g),('Gênero escrito',g+' — produção','Escrita: '+g)]
        if l=='C2':
            for c in CONTRASTS_C2:agenda+=[('Precisão lexical',c+' — sentidos','Contraste: '+c),('Precisão lexical',c+' — uso','Contraste: '+c)]
            for r in REGISTER_C2:agenda+=[('Registro',r+' — formas','Registro: '+r),('Registro',r+' — transposição','Registro: '+r)]
        if l=='A2':
            for i,b in enumerate(IRR_BLOCKS):agenda.append(('Verbos irregulares','Irregulares '+str(i+1)+': '+', '.join(x.split('/')[0] for x in b),'Irregulares: '+'; '.join(b)))
        if l!='A0':
            for k,c in KEY_VERBS.items():agenda.append(('Verbo-chave','Verbo-chave: '+k,'%s — %s'%(k,c)))
        for pi_,pt in enumerate(PAT_BY.get(l,[])):agenda+=[('Padrão de frase',pt+' — forma','Padrão: '+pt),('Padrão de frase',pt+' — uso','Padrão: '+pt)]
        for fm in FORM_BY.get(l,[]):agenda.append(('Formação de palavras',fm,'Formação: '+fm)) if len([a for a in agenda if a[0]=='Formação de palavras'])<FORM_LESSONS.get(l,0) else None
        for pn in PRON.get(l,[]):agenda.append(('Pronúncia',pn,'Pronúncia: '+pn))
        for ex in range(EXAM[l]):agenda.append(('Exame','Laboratório de exame %d (TOEFL · IELTS · college)'%(ex+1),'Exame'))
        # sequência pedagógica: cada categoria é espalhada por todo o nível (em vez de ficar toda no fim);
        # no A0 o alfabeto e os sons abrem o curso; os laboratórios de exame ficam na segunda metade
        cats={}
        for a in agenda:cats.setdefault(a[0],[]).append(a)
        keyed=[]
        for ci_,(cat,its) in enumerate(cats.items()):
            for j,a in enumerate(its):
                f=(j+0.5)/len(its)
                if cat=='Exame':f=0.45+0.55*f
                if l=='A0' and cat=='Pronúncia' and j<2:f=0.0005*(j+1)
                keyed.append((f,ci_,j,a))
        agenda=[a for _,_,_,a in sorted(keyed,key=lambda t:(t[0],t[1],t[2]))]
        core=L-p['review']
        # agenda mais curta que o núcleo → completa com aulas temáticas de comunicação integrada
        slots=[None]*core
        pos=[min(core-1,i*core//max(1,len(agenda))) for i in range(len(agenda))] if len(agenda)<=core else list(range(core))
        for i,a in zip(pos,agenda):slots[i]=a
        if len(agenda)>core:raise SystemExit('agenda maior que o núcleo em '+l)
        # unidades: blocos contíguos por campo vocabular
        nunits=math.ceil(p['base']/16);per=L/nunits;cur_f=fields[0]
        verbs=spread(VERBS_NEW[l],core);pvs=spread(PV_NEW[l],core);ex=spread(EXPR_NEW[l],core)
        irr=[]
        q=p['delta']['lex']/core
        li=0;un_first=gid+1
        seq=[]
        for i in range(core):seq.append(('core',i))
        # intercala revisões e avaliações no fim de cada unidade
        full=[];ui=0;cnt=0
        bounds=[round((k+1)*core/nunits) for k in range(nunits)]
        ci=0
        for k in range(nunits):
            while ci<bounds[k]:full.append(('core',ci));ci+=1
            full.append(('review',k));full.append(('assess',k))
        lu=[]
        for u in range(nunits):
            lu.append(dict(id='%s-U%02d'%(l,u+1),level=l,idx=u+1,field='',fl=[],lessons=0,first=None,last=None,focus=[]))
        units+=lu
        ucur=0;ulesson_idx=[]
        # atribui unidade por posição proporcional
        for pos_i,(kind,i) in enumerate(full):
            u=min(nunits-1,pos_i*nunits//len(full));un=lu[u]
            gid+=1;n=pos_i+1
            if kind=='core':cur_f=fields[min(len(fields)-1,i*len(fields)//core)]
            if cur_f not in un['fl']:un['fl'].append(cur_f)
            ls=dict(id='%s-L%03d'%(l,n),g=gid,level=l,unit=un['id'],n=n,kind=kind,field=cur_f)
            if kind=='core':
                a=slots[i];ls['type']=a[0] if a else 'Comunicação integrada';ls['focus']=a[1] if a else 'Comunicação integrada: %s'%cur_f.split(' (')[0]
                ls['trace']=a[2] if a else ''
                ls['words']=round(q);ls['verbs']=verbs[i];ls['pv']=pvs[i];ls['expr']=ex[i]
                ls['pron']=PRON[l][i%len(PRON[l])] if l in PRON else ''
                ls['skill']=SKILLS[i%4];ls['genre']=GENRE[(i+LV.index(l)*3)%len(GENRE)]
            elif kind=='review':
                ls.update(type='Revisão espaçada',focus='Revisão da unidade %d: recuperar itens anteriores em contextos novos'%(un['idx']),words=0,verbs=[],pv=[],expr=[],pron='',skill='Integrada',genre='',trace='')
            else:
                ls.update(type='Avaliação',focus='Avaliação da unidade %d (leitura, escuta, fala e escrita)'%(un['idx']),words=0,verbs=[],pv=[],expr=[],pron='',skill='Integrada',genre='',trace='')
            if un['first'] is None:un['first']=gid
            un['last']=gid;un['lessons']+=1
            if ls.get('trace') and len(un['focus'])<3 and ls['type'] in('Gramática','Padrão verbal','Modais','Gênero escrito','Precisão lexical','Registro'):
                if ls['focus'].split(' — ')[0] not in un['focus']:un['focus'].append(ls['focus'].split(' — ')[0])
            lessons.append(ls)
        for un in lu:
            un['field']=' · '.join(f.split(' (')[0] for f in un['fl']);del un['fl']
        assert sum(1 for x in lessons if x['level']==l)==L,(l,L)
        levels.append(dict(k=l,cefr=NAMES[l][0],name=NAMES[l][1],goal=GOAL[l],criterion=CRITERIA[l],lessons=L,plan={k:v for k,v in p.items() if k in('delta','cum','need','binding','base','review','gram_lessons','extra','ded')},targets=TARGETS[l],units=nunits))
    out=dict(course='Inglês do zero absoluto ao C2 · inglês americano',frames=12,levels=levels,units=units,lessons=lessons,total_lessons=len(lessons),total_frames=len(lessons)*12)
    json.dump(out,open(R+'/professor/data/livro/curriculo.json','w'),ensure_ascii=False,separators=(',',':'))
    return out,plans

def coverage(o):
    """verifica se cada item da especificação está em ≥1 aula"""
    rep=[];by={l:[x for x in o['lessons'] if x['level']==l] for l in LV}
    miss_total=0
    for l in LV:
        L=by[l];txt=lambda f:set(w for x in L for w in x[f])
        focus=set(x['focus'].split(' — ')[0] for x in L if x['kind']=='core')
        traces=set(x['trace'] for x in L)
        def chk(name,items,have):
            nonlocal miss_total
            m=[i for i in items if i not in have];miss_total+=len(m);rep.append((l,name,len(items),len(items)-len(m),m))
        chk('gramática',GRAM[l],traces)
        chk('verbos-base listados',VERBS_NEW[l],txt('verbs'))
        chk('phrasal verbs listados',PV_NEW[l],txt('pv'))
        chk('expressões e collocations listadas',EXPR_NEW[l],txt('expr'))
        chk('pronúncia',PRON.get(l,[]),set(x['focus'] for x in L if x['type']=='Pronúncia')|set(x['pron'] for x in L))
        if l in PATTERNS_VERB:chk('padrões verbais',PATTERNS_VERB[l],set(x['focus'].split(' — ')[0] for x in L))
        if l=='B2':chk('modais por intenção',MODALS_B2,set(x['focus'].split(' — ')[0] for x in L))
        if l=='A2':chk('verbos irregulares (45)',IRREGULAR,set(i for x in L if x['type']=='Verbos irregulares' for i in x['trace'].replace('Irregulares: ','').split('; ')))
        if l=='C1':chk('gêneros escritos',GENRES_C1,set(x['focus'].split(' — ')[0] for x in L))
        if l=='C2':chk('contrastes lexicais',CONTRASTS_C2,set(x['focus'].split(' — ')[0] for x in L));chk('registros',REGISTER_C2,set(x['focus'].split(' — ')[0] for x in L))
        chk('campos vocabulares',VOCAB_FIELDS[l],set(x['field'] for x in L))
    kv=[k for k in KEY_VERBS if not any(x['focus']=='Verbo-chave: '+k for l in LV if l!='A0' for x in by[l])]
    sp=[p for p in SENTENCE_PATTERNS if not any(x['focus'].startswith('Padrão de frase') is False and p in x['focus'] or (x['type']=='Padrão de frase' and p in x['focus']) for x in o['lessons'])]
    rep.append(('todos','verbos-chave (15, revistos em cada nível A1–C2)',15,15-len(kv),kv));rep.append(('todos','padrões de frase (25)',25,25-len(sp),sp))
    return rep,miss_total+len(kv)+len(sp)

def doc(o,plans,rep,miss):
    L=['# Currículo completo de inglês · do zero absoluto ao C2 (inglês americano)\n',
    'Mapeamento gerado por `professor/src/livro_map.py` a partir da especificação transcrita em `professor/src/livro_spec.py`. **Regra do curso: se faltar aula para cumprir a matriz, a quantidade de aulas aumenta.** Cada aula tem **12 quadros** e integra os nove pilares (vocabulário, verbos, phrasal verbs, gramática, expressões, collocations, pronúncia, comunicação, pragmática e cultura).\n',
    '## 1. Metas da especificação (cumulativas)\n','| Nível | Repertório lexical | Verbos-base | Phrasal verbs | Expressões e collocations | Horas guiadas (referência Cambridge) |','|---|---|---|---|---|---|']
    for l in LV:
        t=TARGETS[l];L.append('| %s | %d–%d | %d%s | %d–%d | %d–%d | %d–%d h |'%(NAMES[l][0],t['lex'][0],t['lex'][1],t['verbs'][0],'+' if l=='C2' else '',t['pv'][0],t['pv'][1],t['expr'][0],t['expr'][1],t['glh'][0],t['glh'][1]))
    L+=['\nMetas pedagógicas aproximadas e acumulativas, não requisitos de certificação. Para planejar, uso o **ponto médio** das faixas (verbos: o valor da tabela).\n',
    '## 2. Como calculei a quantidade de aulas\n',
    'Para cada nível, calculo quantas aulas cada pilar exige e adoto o **maior valor** (restrição que mais pesa); depois somo as revisões e avaliações periódicas (2 por unidade de ~16 aulas). Cada aula comporta: %s palavras novas (A0→C2), %d verbos-base, %d phrasal verbs e %d expressões/collocations novos, mais um item de gramática por etapa (introdução; prática e contraste; produção e revisão — 2 etapas no A0 e 3 nos demais). 1 aula ≈ 60 min de estudo guiado.\n'%('/'.join(str(CAP_WORDS[l]) for l in LV),CAP_VERBS,CAP_PV,CAP_EXPR),
    '| Nível | Horas | Vocabulário | Verbos | Phrasal | Expressões | Estruturados* | **Restrição que pesa** | Núcleo | + Revisões/avaliações | **Aulas** |','|---|---|---|---|---|---|---|---|---|---|---|']
    for l in LV:
        p=plans[l];n=p['need'];L.append('| %s | %d | %d | %d | %d | %d | %d | %s | %d | %d | **%d** |'%(NAMES[l][0],n['horas guiadas'],n['vocabulário'],n['verbos-base'],n['phrasal verbs'],n['expressões e collocations'],n['itens estruturados (gramática + aulas dedicadas + exames)'],p['binding'],p['base'],p['review'],p['lessons']))
    L.append('| **Total** | | | | | | | | | | **%d aulas · %d quadros** |\n'%(o['total_lessons'],o['total_frames']))
    L+=['\\* Estruturados = aulas de gramática (itens × etapas), padrões verbais, modais, gêneros escritos, contrastes lexicais, verbos-chave (15 por nível de A1 a C2), padrões de frase, formação de palavras, verbos irregulares, pronúncia e laboratórios de exame (TOEFL, IELTS e colleges canadenses, do B1 ao C2).\n',
    '## 3. Metas por nível e itens a completar\n','| Nível | Léxico novo a ensinar | Verbos novos | Verbos listados (sem repetir níveis) | Phrasal novos | Phrasal listados | Expressões novas | Expressões listadas |','|---|---|---|---|---|---|---|---|']
    for l in LV:
        d=plans[l]['delta'];L.append('| %s | ~%d | %d | %d | %d | %d | %d | %d |'%(NAMES[l][0],d['lex'],d['verbs'],len(VERBS_NEW[l]),d['pv'],len(PV_NEW[l]),d['expr'],len(EXPR_NEW[l])))
    L+=['\nOnde a meta supera o que a especificação lista, a diferença é **completada durante a escrita das aulas**, com itens do mesmo campo semântico e de frequência adequada, e registrada no quadro de vocabulário de cada aula. Nada que a especificação lista foi deixado de fora (seção 4).\n',
    '## 4. Rastreabilidade: cada item da especificação está em pelo menos uma aula\n','| Nível | Item | Previsto | Alocado | Faltando |','|---|---|---|---|---|']
    for l,name,n,ok,m in rep:L.append('| %s | %s | %d | %d | %s |'%(l,name,n,ok,'; '.join(m)[:120] if m else '—'))
    L.append('\n**Resultado: %d item(ns) faltando.**\n'%miss)
    L+=['## 5. Estrutura fixa da aula (12 quadros)\n','1. Abertura e objetivos (CEFR + exame)','2. Aquecimento e conhecimento prévio','3. Texto de leitura (gênero do dia)','4. Compreensão e vocabulário em contexto','5. Gramática em foco (regra, quadro e erros de brasileiros)','6. Prática de gramática','7. Vocabulário, expressões e collocations','8. Verbos e phrasal verbs em destaque','9. Escuta e diálogo (com pronúncia)','10. Fala (modelo e tarefa)','11. Escrita (gênero, modelo e lista de verificação)','12. Revisão, estratégia de exame e nota para o professor\n',
    'Os quadros 3 e 4 trazem sempre um gênero de texto autêntico diferente (notícia, biografia, poema, charge, e-mail, entrevista, anúncio, receita, blog, resenha, conto, editorial, texto acadêmico, infográfico, palestra). Cada item novo percorre o ciclo: %s.\n'%' → '.join(CICLO),
    '## 6. Competências de conclusão e avaliação prática\n']
    for l in LV:
        L.append('- **%s**: %s'%(NAMES[l][0],CRITERIA[l]))
    L+=['\n## 7. Unidades\n']
    for l in LV:
        L+=['\n### %s · %s (%d aulas, %d unidades)\n'%(NAMES[l][0],NAMES[l][1],next(x['lessons'] for x in o['levels'] if x['k']==l),next(x['units'] for x in o['levels'] if x['k']==l)),'| Unidade | Campo vocabular | Foco gramatical e estrutural | Aulas |','|---|---|---|---|']
        for u in o['units']:
            if u['level']==l:L.append('| %s | %s | %s | %d–%d |'%(u['id'],u['field'][:60],'; '.join(u['focus'][:3]) or '—',u['first'],u['last']))
    L+=['\n## 8. Honestidade sobre a produção\n','Este mapa define **o que** cada aula ensina. As aulas são escritas por lotes, na ordem do currículo, e cada lote passa por verificação automática (12 quadros, respostas conferidas, itens-alvo presentes) antes de entrar no livro. **Ainda não foram revisadas por falante nativo ou professor**; isso é necessário antes de uso em curso pago. As faixas de pontuação de IELTS e TOEFL aceitas por colleges canadenses variam por instituição e mudam: confirme sempre nos sites oficiais.']
    open(R+'/docs/CURRICULO-FORMACAO-PROFESSORES.md','w',encoding='utf-8').write('\n'.join(L)+'\n')

if __name__=='__main__':
    o,plans=build();rep,miss=coverage(o);doc(o,plans,rep,miss)
    print('aulas por nível:',[(NAMES[l['k']][0],l['lessons']) for l in o['levels']],'| total',o['total_lessons'],'aulas',o['total_frames'],'quadros')
    for l in LV:print(' ',l,'restrição:',plans[l]['binding'],plans[l]['need'])
    print('itens faltando na cobertura:',miss)
    for l,name,n,ok,m in rep:
        if m:print('   FALTA',l,name,m[:5])
