#!/usr/bin/env python3
"""Gera o roteiro de cada episódio do Pocket de inglês do B1 #451 ao C2 #800 (2.750 episódios).

Insumos (todos já no repositório):
  • data/pk-<nivel>_*.json  -> ordem, arco/posição, personagem-guia e título atual de cada episódio;
  • data/en-*.json          -> catálogo regular (casa o episódio do Pocket pela obra + título da lição);
  • data/skel/en-*.json     -> roteiro do catálogo regular: gramática, tema, vocabulário, verbos, expressões, gírias, gancho.
Saída: data/pk-roteiro/pk-<nivel>.json, docs/roteiro-pocket-b1-c2.csv (o visualizador é roteiro/pocket.html)."""
import json,glob,re,csv,os,collections
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'));D=os.path.join(R,'data')
def load_pk(lv):
    e=[]
    for f in sorted(glob.glob(f'{D}/pk-{lv}_*.json')):e+=json.load(open(f))
    return sorted(e,key=lambda x:x['n'])
reg={}
for f in sorted(glob.glob(f'{D}/en-*_*.json')):
    for x in json.load(open(f)):reg[x['n']]=x
skel={}
for lv in ['a1','a2','b1','b2','c1','c2']:
    for x in json.load(open(f'{D}/skel/en-{lv}.json')):x['_lv']=lv;skel[x['n']]=x
byw=collections.defaultdict(list)
for n,x in reg.items():
    w=(x.get('a') or {}).get('w','').lower()
    if w:byw[w].append(n)
byt=collections.defaultdict(list)
for n,x in skel.items():byt[x['titulo'].lower()].append(n)
CEN={'lobby1':'um saguão de empresa ou hotel','lobby2':'um saguão de empresa ou hotel','home1':'uma casa','home2':'uma casa','park2':'um parque','yard':'um quintal','shop':'uma loja','cafe2':'um café','cafe3':'um café','diner':'uma lanchonete','cafe':'um café','living':'uma sala de estar','street':'a rua','office':'um escritório','station':'uma estação','library':'uma biblioteca','ballroom':'um salão de festas','community-center':'um centro comunitário','cultural-study':'uma sala de estudos culturais','kitchen':'uma cozinha','market':'um mercado','park':'um parque','airport':'um aeroporto','school':'uma escola','hotel':'um hotel','hospital':'um hospital','museum':'um museu','theater':'um teatro','home':'uma casa','plaza':'uma praça'}
INTER=['Conversa de abertura: o guia apresenta o tema e a pessoa responde com naturalidade.',
 'Pedir ou dar uma informação concreta, com pergunta e resposta que avançam a conversa.',
 'Um imprevisto ou problema a resolver, com pelo menos uma objeção ou mudança de plano.',
 'Troca de opiniões: cada lado explica o porquê, e alguém muda de ideia ou concede um ponto.',
 'Comparar duas opções e tomar uma decisão que o diálogo justifica.',
 'Alguém conta o que aconteceu (relato curto, com sequência de fatos) e o outro reage.',
 'Convencer ou negociar: um pedido, uma contraproposta e um acordo possível.',
 'Uma mensagem escrita (e-mail, recado, post) que é lida ou ditada em voz alta e comentada.',
 'Cultura e humor: a obra de referência entra na conversa e provoca uma piada ou uma descoberta.',
 'MINI-CHEFE do arco: conversa mais longa que reencontra as palavras e a gramática dos 9 episódios anteriores.']
def pick_skel(lv,e,used):
    """B2–C2: casa obra+título com o catálogo regular e devolve o roteiro regular (skel)."""
    w=e['a']['w'].lower();title=e['t'].split(' · ')[0].lower()
    for n in byw.get(w,[]):
        if reg[n]['t'].lower()==title and n in skel and n not in used:return skel[n]
    for n in byw.get(w,[]):
        if n in skel and n not in used:return skel[n]
    for n in byt.get(title,[]):
        if n not in used:return skel[n]
    return None
out={};rows=[]
b1sk=sorted([x for x in skel.values() if x['_lv']=='b1'],key=lambda x:x['o'])
b1pool=[x for x in b1sk if x['papel']=='principal']
extra=[x for x in b1sk if x['papel']!='principal']
b1pick=sorted(b1pool+extra[:350-len(b1pool)],key=lambda x:x['o'])[:350]
for lv,lo in [('b1',450),('b2',0),('c1',0),('c2',0)]:
    E=load_pk(lv);used=set();res=[]
    for i,e in enumerate(E):
        if i<lo:continue
        order=i+1;pos=(order-1)%10+1;arc=(order-1)//10+1
        s=b1pick[i-lo] if lv=='b1' else pick_skel(lv,e,used)
        if s:used.add(s['n'])
        ch=E[(arc-1)*10]['character'] if 'character' in E[(arc-1)*10] else e['character']
        prev=res[-1] if res else None
        r={'n':e['n'],'nivel':lv.upper(),'ordem':order,'arco':arc,'pos':pos,'chefe':pos==10,
           'titulo_atual':e['t'],'guia':{'nome':ch['name'],'genero':ch.get('gender',''),'cidade':ch['city'],'papel':ch['role']}}
        if s:
            r.update({'titulo_en':s['titulo'],'tema_pt':s['tema'],'gramatica':s['gramatica']['estrutura'],
              'obra':s['obra'],'gancho':{'en':s['frase_gancho'][0],'pt':s['frase_gancho'][1]},
              'vocabulario':s['vocabulario_pt'][:5] if len(s['vocabulario_pt'])>=5 else s['vocabulario_pt'],
              'verbos':s['verbos'][:3],'expressoes':s['expressoes'][:3],'girias':(s.get('girias') or [])[:2],
              'cenario':CEN.get(s['cenario'],s['cenario']),'fonte':'roteiro regular %s #%s'%(s['_lv'].upper(),s['ep'])})
        else:
            r.update({'titulo_en':e['t'].split(' · ')[0],'tema_pt':e['s'],'gramatica':'(definir pelo nível; veja o guia do nível no prompt)',
              'obra':e['a']['w'],'gancho':{'en':e['h']['l'],'pt':e['h']['tr']},'vocabulario':[v[:2] for v in e['v']][:5],
              'verbos':[],'expressoes':[],'girias':[],'cenario':CEN.get(e.get('sc'),e.get('sc','')),'fonte':'dados atuais do Pocket (sem par no catálogo regular)'})
        r['interacao']=INTER[pos-1]
        r['situacao']=('%s (%s, %s), em %s. Tema: %s. Interação: %s Gancho cultural: a obra «%s».'%(ch['name'],ch['role'],ch['city'],r['cenario'] or 'um lugar do dia a dia',r['tema_pt'],INTER[pos-1],str(r['obra']).split(' (')[0]))
        if prev and prev['arco']==arc:
            r['reciclar']={'de':prev['n'],'titulo':prev['titulo_en'],'palavras':[v[0] for v in prev['vocabulario'][:2]]}
        else:r['reciclar']=None
        res.append(r)
    for a,b in zip(res,res[1:]):a['proximo']=b['titulo_en']
    if res:res[-1]['proximo']=None
    for r in res:
        if r['chefe']:r['reciclar_chefe']=[v[0] for q in res if q['arco']==r['arco'] and q['pos']<10 for v in q['vocabulario'][:1]]
    out[lv]=res
os.makedirs(f'{D}/pk-roteiro',exist_ok=True)
tot=0
for lv,res in out.items():
    json.dump(res,open(f'{D}/pk-roteiro/pk-{lv}.json','w'),ensure_ascii=False,separators=(',',':'));tot+=len(res)
with open(f'{R}/docs/roteiro-pocket-b1-c2.csv','w',newline='',encoding='utf-8') as f:
    w=csv.writer(f);w.writerow(['n','nivel','ordem','arco','pos','chefe','titulo_en','tema_pt','gramatica','obra','cenario','guia','vocabulario','verbos','expressoes','gancho_en','situacao'])
    for res in out.values():
        for r in res:w.writerow([r['n'],r['nivel'],r['ordem'],r['arco'],r['pos'],'sim' if r['chefe'] else '',r['titulo_en'],r['tema_pt'],r['gramatica'],r['obra'],r['cenario'],'%s (%s, %s)'%(r['guia']['nome'],r['guia']['papel'],r['guia']['cidade']),'; '.join(v[0]+'='+v[1] for v in r['vocabulario']),'; '.join(v[0] for v in r['verbos']),'; '.join(v[0] for v in r['expressoes']),r['gancho']['en'],r['situacao']])
print('roteiros:',{k:len(v) for k,v in out.items()},'total',tot)
sem=sum(1 for res in out.values() for r in res if r['fonte'].startswith('dados'));print('sem par no regular:',sem)
