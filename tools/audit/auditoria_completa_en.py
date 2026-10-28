#!/usr/bin/env python3
"""Auditoria completa do curso regular de inglês (A1–C2): padrão, obras únicas, ponte, capas, conteúdo próprio e densidade.
Uso: python3 tools/audit/auditoria_completa_en.py  (escreve docs/AUDITORIA_INGLES_COMPLETA.json e imprime o resumo)"""
import json, glob, re, collections, statistics, os, sys
ROOT=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LV=['a1','a2','b1','b2','c1','c2']
def load():
    out=[]
    for lv in LV:
        fs=sorted(glob.glob(f'{ROOT}/data/en-{lv}_*.json'),key=lambda x:int(re.search(r'_(\d+)\.json',x).group(1)))
        i=0
        for f in fs:
            for e in json.load(open(f)):
                i+=1;e['_lv']=lv;e['_i']=i;out.append(e)
    return out
def norm(s):
    s=(s or '').lower()
    s=re.sub(r'\([^)]*\)','',s);s=re.split(r'\s[:–—-]\s|:',s)[0]
    s=re.sub(r'^(the|a|an|o|a|os|as|un|une|el|la)\s+','',s.strip())
    s=re.sub(r'[^\w\s]','',s);s=re.sub(r'\s+',' ',s).strip()
    return s
def txt(o):
    if isinstance(o,str):return o
    if isinstance(o,dict):return ' '.join(txt(v) for v in o.values())
    if isinstance(o,list):return ' '.join(txt(v) for v in o)
    return ''
def frames(e,k):return [f for f in e.get('fr',[]) if f.get('k')==k]
def pct(a,b):return round(100*a/b,1) if b else 0.0
eps=load();N=len(eps)
R={'total':N,'por_nivel':{lv:sum(1 for e in eps if e['_lv']==lv) for lv in LV}}

# ---------- A. padrão estrutural ----------
MODEL=['cover','review','hotscene','pgscene','pgsheet','pgrule','pgmold','pgsheet','verbs','vplay','pgexp','pgscene','pgsheet','pgsheet','pglab','pgsheet','pgspeak','pgmission','wrap']
def sig(e):return [f['k'] for f in e.get('fr',[])]
std={};exact=collections.Counter();pres=collections.Counter()
for e in eps:
    s=sig(e);ok=(s==MODEL) or (s==[k for k in MODEL if k!='review'])
    exact[e['_lv']]+=ok;pres[e['_lv']]+=(e.get('presentation')=='regular-pilot-v1')
R['padrao']={lv:{'eps':R['por_nivel'][lv],'modelo_19_quadros':exact[lv],'etiqueta_presentation':pres[lv]} for lv in LV}

# ---------- B. obras únicas ----------
W=collections.defaultdict(list);kinds=collections.Counter();NOT_WORK=re.compile(r'cidade|tradi|lugar|institui|empresa|edif|monument|vulc|pessoa|ciudad|city|invenc|evento|jornal|programa',re.I)
nowork=[]
for e in eps:
    a=e.get('a') if isinstance(e.get('a'),dict) else {}
    w=a.get('w') or '';k=a.get('k') or ''
    W[norm(w)].append((e['_lv'],e['_i'],e['n'],w))
    kinds[re.sub(r'^[^\w]+','',k).lower()[:28]]+=1
    if not w:nowork.append(e['n'])
    elif NOT_WORK.search(k):nowork.append((e['_lv'],e['_i'],w,k))
dups={k:v for k,v in W.items() if k and len(v)>1}
R['obras']={'episodios':N,'distintas_normalizadas':len([k for k in W if k]),'sem_obra':sum(1 for v in nowork if not isinstance(v,tuple)),
 'grupos_repetidos':len(dups),'episodios_em_repeticao':sum(len(v) for v in dups.values()),
 'exemplos_repetidos':[{'obra':v[0][3],'eps':[(x[0],x[1]) for x in v]} for k,v in sorted(dups.items(),key=lambda kv:-len(kv[1]))[:25]],
 'nao_obra_cultural(cidade/tradicao/lugar/instituicao...)':len([v for v in nowork if isinstance(v,tuple)]),
 'por_nivel_distintas':{lv:len({norm((e.get('a') or {}).get('w')) for e in eps if e['_lv']==lv and isinstance(e.get('a'),dict)}) for lv in LV},
 'repeticoes_por_nivel':{lv:sum(1 for k,v in dups.items() for x in v if x[0]==lv) for lv in LV}}

# ---------- C. ponte da obra ----------
def toks(w):
    return [t for t in re.findall(r"[a-z']{3,}",norm(w)) if t not in {'the','and','for','from','with','that','this','dos','das'}]
bridge=collections.defaultdict(lambda:collections.Counter())
for e in eps:
    a=e.get('a') if isinstance(e.get('a'),dict) else {}
    w=a.get('w') or '';tk=toks(w);lv=e['_lv']
    if not tk:bridge[lv]['sem_tokens']+=1;continue
    def has(text):
        t=norm(text);return sum(1 for x in tk if x in t)>=max(1,(len(tk)+1)//2)
    cover=(frames(e,'cover') or [{}])[0]
    scenes=' '.join(txt(f.get('lines')) for f in frames(e,'pgscene'))
    miss=' '.join(txt(f) for f in frames(e,'pgmission'))
    bridge[lv]['eps']+=1
    bridge[lv]['capa_cita_obra']+=has(txt(cover.get('obra',''))+' '+txt(cover.get('sub','')))
    bridge[lv]['gancho_da_obra']+=bool((e.get('h') or {}).get('src') and has(txt((e.get('h') or {}).get('src',''))))
    bridge[lv]['obra_dentro_da_cena']+=has(scenes)
    bridge[lv]['obra_na_missao']+=has(miss)
    bridge[lv]['ponte_completa(cena+missao)']+=(has(scenes) and has(miss))
    wr=(frames(e,'wrap') or [{}])[0].get('sticker') or {}
    bridge[lv]['figurinha_da_obra']+=has(txt(wr))
R['ponte']={lv:{k:(v if k=='eps' else f'{v} ({pct(v,bridge[lv]["eps"])}%)') for k,v in bridge[lv].items()} for lv in LV}

# ---------- D. conteúdo distinto ----------
def vocab(e):return tuple(sorted((w[0] or '').lower() for w in (e.get('v') or []) if isinstance(w,(list,tuple)) and w))
def exps(e):
    f=frames(e,'pgexp');return tuple(sorted((it.get('en') or '').lower() for it in (f[0].get('items') if f else []) if isinstance(it,dict)))
def verbs(e):
    f=frames(e,'verbs');return tuple(sorted((it[0] if isinstance(it,(list,tuple)) else it.get('en','')).lower() for it in (f[0].get('items') if f else [])))
def pattern(e):return (e.get('pattern') or (e.get('g') or {}).get('t') or '').lower().strip()
cnt=lambda it:collections.Counter(it)
titles=cnt(e.get('t','').lower() for e in eps)
vocs=cnt(vocab(e) for e in eps if vocab(e));pats=cnt(pattern(e) for e in eps if pattern(e))
expc=collections.Counter();lines=collections.Counter();hot=collections.Counter()
for e in eps:
    for x in set(exps(e)):expc[x]+=1
    for f in frames(e,'pgscene'):
        for l in f.get('lines',[]):
            if len(l)>1:lines[l[1].strip().lower()]+=1
    h=frames(e,'hotscene')
    if h:hot[tuple(sorted(o.get('en','') for o in h[0].get('hot',[])))]+=1
rep_exp={k:v for k,v in expc.items() if v>1 and k}
R['conteudo_proprio']={'titulos_repetidos':sum(1 for v in titles.values() if v>1),'episodios_com_titulo_repetido':sum(v for v in titles.values() if v>1),
 'conjuntos_de_vocabulario_repetidos':sum(1 for v in vocs.values() if v>1),'padroes_gramaticais_repetidos(texto igual)':sum(1 for v in pats.values() if v>1),
 'expressoes_ensinadas_total':sum(expc.values()),'expressoes_distintas':len(expc),'expressoes_em_mais_de_um_episodio':len(rep_exp),
 'exemplos_expressoes_repetidas':sorted(rep_exp.items(),key=lambda kv:-kv[1])[:15],
 'falas_de_cena_repetidas_>=3_eps':sum(1 for v in lines.values() if v>=3),'conjuntos_hot_repetidos':sum(1 for v in hot.values() if v>1)}
# pares/continuação: vizinhos com mesma obra ou mesmo padrão
par=collections.Counter();par_ex=[]
for a,b in zip(eps,eps[1:]):
    if a['_lv']!=b['_lv']:continue
    wa=norm((a.get('a') or {}).get('w'));wb=norm((b.get('a') or {}).get('w'))
    if wa and wa==wb:par[a['_lv']]+=1;par_ex.append((a['_lv'],a['_i']))
    elif pattern(a) and pattern(a)==pattern(b):par[a['_lv']]+=1
R['conteudo_proprio']['vizinhos_com_mesma_obra_ou_mesmo_padrao']={lv:par[lv] for lv in LV}
# título em português (formato antigo de "par")
pt=re.compile(r'[áéíóúãõç]|\b(de|do|da|para|com|sem|e)\b',re.I)
R['conteudo_proprio']['titulos_em_portugues(formato antigo)']={lv:sum(1 for e in eps if e['_lv']==lv and pt.search(e.get('t','')) and not re.search(r'\b(the|you|are|is|it|to|of)\b',e.get('t','').lower())) for lv in LV}

# ---------- E. capas ----------
js=open(f'{ROOT}/js/obra-art.js').read()
keys=set(int(x) for x in re.findall(r'(\d{4,8}):\'[a-z]+\'',js[js.index('const KEY='):js.index('const KEY=')+400]))
R['capas']={'com_arte_refinada_propria':len([e for e in eps if e['n'] in keys]),'ids_com_arte':sorted(keys),
 'capa_gerada_pelo_modelo(seed v3_)':sum(1 for e in eps if 'v3_' in json.dumps((frames(e,'cover') or [{}])[0].get('art',{}))),
 'cenarios_distintos(rs)':len({e.get('rs') for e in eps}),
 'vizinhos_com_mesmo_cenario':sum(1 for a,b in zip(eps,eps[1:]) if a.get('rs') and a.get('rs')==b.get('rs'))}
chars=collections.defaultdict(set)
for e in eps:
    for c in ((e.get('stage') or {}).get('chars') or []):
        chars[c[0]].add(norm((e.get('a') or {}).get('w')))
gen=[c for c,w in chars.items() if len(w)>=4]
R['capas']['personagens_distintos']=len(chars);R['capas']['personagens_usados_em_4+_obras']=len(gen)
R['capas']['eps_cuja_arte_de_personagem_e_generica']=sum(1 for e in eps if any(c[0] in gen for c in ((e.get('stage') or {}).get('chars') or [])))

# ---------- F. densidade ----------
def dens(e):
    sc=frames(e,'pgscene');ms=frames(e,'pgmission');lab=frames(e,'pglab');sp=frames(e,'pgspeak')
    sheets=frames(e,'pgsheet')
    d={'vocab':len(e.get('v') or []),'verbos':len((frames(e,'verbs') or [{}])[0].get('items',[])),'expressoes':len((frames(e,'pgexp') or [{}])[0].get('items',[])),
     'cena1':len(sc[0].get('lines',[])) if sc else 0,'cena2':len(sc[1].get('lines',[])) if len(sc)>1 else 0,
     'perguntas_pgsheet':sum(len(f.get('items',[])) for f in sheets),'missoes':len((ms[0].get('missions') if ms else []) or []),
     'lab_pares':len((lab[0].get('pairs') if lab else []) or []),'fala':len((sp[0].get('items') if sp else []) or []),'quadros':len(e.get('fr',[])),
     'texto_en_chars':len(txt([f for f in e.get('fr',[])]))}
    return d
D=[dens(e) for e in eps]
def q(vals):
    vals=sorted(vals);n=len(vals)
    return {'min':vals[0],'p10':vals[n//10],'mediana':vals[n//2],'p90':vals[(9*n)//10],'max':vals[-1]}
ref=[D[i] for i,e in enumerate(eps) if e['_lv']=='a1' and 1<=e['_i']<=5]
R['densidade']={'referencia_A1_ep2a5':{k:round(statistics.mean(d[k] for d in ref[1:])) for k in ref[0]} if len(ref)>1 else {}}
for lv in LV:
    sub=[D[i] for i,e in enumerate(eps) if e['_lv']==lv]
    R['densidade'][lv]={k:q([d[k] for d in sub]) for k in ('vocab','verbos','expressoes','cena1','cena2','perguntas_pgsheet','missoes','lab_pares','fala','quadros','texto_en_chars')}
R['densidade']['abaixo_do_modelo']={}
for lv in LV:
    sub=[d for d,e in zip(D,eps) if e['_lv']==lv];n=len(sub)
    R['densidade']['abaixo_do_modelo'][lv]={'vocab<6':sum(d['vocab']<6 for d in sub),'verbos<4':sum(d['verbos']<4 for d in sub),'expressoes<4':sum(d['expressoes']<4 for d in sub),
      'cena1<8_falas':sum(d['cena1']<8 for d in sub),'cena2<8_falas':sum(d['cena2']<8 for d in sub),'missoes!=3':sum(d['missoes']!=3 for d in sub),'lab<3':sum(d['lab_pares']<3 for d in sub),'sem_fala(pgspeak)':sum(d['fala']==0 for d in sub),
      'densidade_texto<70%_da_mediana_do_nivel':sum(d['texto_en_chars']<0.7*statistics.median(x['texto_en_chars'] for x in sub) for d in sub)}
json.dump(R,open(f'{ROOT}/docs/AUDITORIA_INGLES_COMPLETA.json','w'),ensure_ascii=False,indent=1,default=str)
print(json.dumps(R,ensure_ascii=False,indent=1,default=str)[:9000])
