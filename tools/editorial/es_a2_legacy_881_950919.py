"""Converte o lote legado A2 881–900 e 950900–950919 para o piloto regular."""
import json, glob
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
TARGET=set(range(881,901))|set(range(950900,950920))
VERBS=[('organizar','organizar'),('explicar','explicar'),('resolver','resolver'),('comparar','comparar'),('proponer','propor'),('confirmar','confirmar'),('preparar','preparar'),('elegir','escolher'),('revisar','revisar'),('compartir','compartilhar'),('describir','descrever'),('recordar','lembrar'),('acordar','combinar'),('invitar','convidar'),('recomendar','recomendar'),('cuidar','cuidar')]
EXP=[('Por lo visto','Pelo visto'),('A mi parecer','Na minha opinião'),('En cambio','Por outro lado'),('De todos modos','De todo modo'),('Para aclarar','Para esclarecer'),('A fin de cuentas','No fim das contas'),('Si te parece','Se você achar bom'),('Por ahora','Por enquanto'),('Desde luego','Certamente'),('Qué buena idea','Que boa ideia'),('Por si acaso','Por via das dúvidas'),('Al final','No final')]

def getframe(e,k): return next((f for f in e.get('fr',[]) if f.get('k')==k),{})
def normline(x,i):
    if not isinstance(x,list): x=[f'Persona {i+1}',str(x),str(x)]
    if len(x)>=3: return [str(x[0]),str(x[1]),str(x[2])]
    if len(x)==2: return [f'Persona {i+1}',str(x[0]),str(x[1])]
    return [f'Persona {i+1}','Continuemos con la situación.','Vamos continuar com a situação.']
def vocab(e):
    out=[]
    for x in (e.get('v') or [])[:6]:
        if isinstance(x,list):
            w=str(x[0]); pt=str(x[1] if len(x)>1 else x[0]); py=str(x[2] if len(x)>2 and x[2] else w)
        else: w=pt=py=str(x)
        out.append((w,pt,py))
    while len(out)<6:
        i=len(out); out.append((f'palabra{i+1}',f'palavra{i+1}',f'pa-LA-bra'))
    return out

def make(e, prev):
    n=e['n']; v=vocab(e); oldscene=getframe(e,'scene').get('lines') or getframe(e,'cultcena').get('lines') or []
    scene1=[normline(x,i) for i,x in enumerate(oldscene[:8])]
    while len(scene1)<8: scene1.append([f'Persona {len(scene1)%2+1}','Continuemos con la situación.','Vamos continuar com a situação.'])
    oldread=getframe(e,'read').get('s') or []
    scene2=[]
    for i,x in enumerate(oldread[:8]):
        if isinstance(x,list) and len(x)>=2: scene2.append([f'Persona {i%2+1}',str(x[0]),str(x[1])])
    while len(scene2)<8: scene2.append([f'Persona {len(scene2)%2+1}',scene1[len(scene2)][1],scene1[len(scene2)][2]])
    focus=e.get('s','A2 · situação').split('·')[1].strip() if '·' in e.get('s','') else e.get('t','situação')
    work=(e.get('a') or {}).get('w') or getframe(e,'cultob').get('work') or getframe(e,'cover').get('work') or f'Obra do episódio {n}'
    year=str((e.get('a') or {}).get('y') or '')
    desc=(e.get('a') or {}).get('d') or f'Referência cultural para praticar {focus} em espanhol.'
    verbs=[]
    start=n%len(VERBS)
    for i in range(4):
        w,pt=VERBS[(start+i)%len(VERBS)]
        verbs.append({'v':w,'ic':['📝','📏','⚖️','🧭'][i],'pt':pt,'f':[['yo',f'Yo {w} la situación.'],['ella',f'Ella {w} la situación.']],'ex':[f'Ella {w} la situación.',f'Ela {pt} a situação.'],'note':f'Use {w} no contexto.'})
    ex=[]; ex_start=(n*2)%len(EXP)
    for i in range(4):
        a,b=EXP[(ex_start+i)%len(EXP)]; ex.append({'ic':['💬','🧭','⏱️','✨'][i],'en':a,'tag':'Expressão','pt':b,'use':f'Use **{a}** na situação.','ex':[a,b]})
    cards=[]
    for i,(w,pt,py) in enumerate(v):
        cards.append({'fig':['🌊','🪨','📐','🛶','⛰️','🧭'][i],'say':w,'ask':'Qual é a palavra?','opts':[w,w+'?', 'otra palabra'],'a':0,'ptWord':pt,'why':f'{w} = {pt}. Soa como “{py}”.'})
    title=e.get('t','')
    if title.startswith('A2 · Episodio'):
        title=f'{focus[:1].upper()+focus[1:]} · {work}'
    s=e.get('s',''); prefix=s.split('referencia:')[0].rstrip(' ·') if 'referencia:' in s else s.rstrip(' ·')
    e.update({'t':title,'s':f'{prefix} · referencia: {work}'+(f' · {year}' if year else ''),'a':{'k':'🎬 Obra','w':work,'y':year,'d':desc},'h':{'l':scene1[0][1],'src':work,'tr':scene1[0][2]},'p':f'Hoje você aprende a {focus}.','presentation':'regular-pilot-v1','pilot':1,'stage':{'rs':'lake','chars':[['polly',34,0,1.0],['tom',68,1,1.0]]}})
    fr=[]
    cover=getframe(e,'cover')
    cover.update({'k':'cover','sub':f'{focus}: em 10 minutos você resolve uma situação real','badge':'A2','say':f'Você vai praticar {focus}.','obra':f'{work} · {year}' if year else work,'stage':{'rs':'lake','chars':[['polly',34,0,1.0],['tom',68,1,1.0]]}})
    fr.append(cover)
    fr.append({'k':'review','prev':prev.get('t','') if prev else 'A situação anterior','work':(prev.get('a') or {}).get('w','') if prev else '', 'recap':[[x[0],x[1]] for x in (prev.get('v') or [])[:4]] if prev else [[x[0],x[1]] for x in v[:4]],'bag':[],'lead':'Abra a mochila e recupere a aula anterior.','next':f'Hoje: {focus}','say':'Recupere e avance.'})
    fr.append({'k':'hotscene','title':'Explore a cena','hint':'Toque nos elementos e ouça.','rs':'lake','chars':[['polly',34,0,1.0],['tom',68,1,1.0]],'hot':[{'e':cards[i]['fig'],'x':18+i*17,'y':25+(i%2)*18,'en':v[i][0],'pt':v[i][1],'say':scene1[i][1],'sayPt':scene1[i][2]} for i in range(5)],'say':'Observe antes de responder.'})
    fr.append({'k':'pgscene','cast':{'A':['👩','#a94b6b'],'B':['🧑','#276b7a']},'lines':scene1,'speakers':{scene1[0][0]:'polly',scene1[1][0]:'tom'},'rs':'lake','chars':[['polly',34,0,1.0],['tom',68,1,1.0]],'say':'Ouça e leia a cena.'})
    fr.append({'k':'pgsheet','title':'Você entendeu?','items':[{'ask':f'Qual informação aparece na fala {i+1}?','speak':line[1],'pt':line[2],'opts':[['🎯',line[1]],['🧩',scene1[(i+1)%8][1]],['🔎',scene1[(i+2)%8][1]]],'a':0,'why':'A resposta está na cena.'} for i,line in enumerate(scene1[::2][:3])],'say':'Confira a intenção.'})
    fr.append({'k':'pgrule','rule':{'who':scene1[0][0],'head':focus,'sub':focus,'say':[scene1[0][1],scene1[0][2]],'formula':[],'uses':[],'rules':['Observe o padrão dentro da situação.','Repita a forma com conteúdo próprio.'],'tips':['Mantenha a intenção da fala.']},'q':{'ask':'Qual opção mantém a intenção?','opts':[scene1[1][1],'Una frase sin relación','Una palabra aislada'],'a':0,'why':'A fala responde à situação.'},'say':'Descubra o padrão.'})
    fr.append({'k':'pgmold','title':'Molde de frases','pages':[{'label':'Abrir','slots':[{'cat':'fala','opts':[[scene1[0][1],scene1[0][2]],[scene1[1][1],scene1[1][2]]]}],'end':['.','.']},{'label':'Desenvolver','slots':[{'cat':'ideia','opts':[[scene1[2][1],scene1[2][2]],[scene1[3][1],scene1[3][2]]]}],'end':['.','.']},{'label':'Fechar','slots':[{'cat':'fecho','opts':[[scene1[6][1],scene1[6][2]],[scene1[7][1],scene1[7][2]]]}],'end':['.','.']}],'say':'Monte uma resposta.'})
    fr.append({'k':'pgsheet','title':'Palavras da cena','layout':'grid','items':cards,'say':'Use as seis palavras.'})
    fr.append({'k':'verbs','title':'Verbos da situação','items':verbs,'tip':f'Quatro verbos: {", ".join(x["v"] for x in verbs)}.','quiz':[],'say':'Veja os verbos em ação.'})
    fr.append({'k':'vplay','title':'Missão dos verbos','items':verbs,'plan':[[0,0],[1,0],[2,0],[3,0],[0,3],[1,3],[2,3]],'say':'Use os quatro verbos.'})
    fr.append({'k':'pgexp','title':'Expressões em uso','items':ex,'quiz':[{'ask':f'Quando usar “{x["en"]}”?','opts':[x['pt'],'Una cor','Un objeto'],'a':0,'why':f'A expressão significa {x["pt"]}.'} for x in ex],'say':'Escolha conforme a intenção.'})
    fr.append({'k':'pgscene','title':'Na conversa de verdade','cast':{'A':['👩','#a94b6b'],'B':['🧑','#276b7a']},'lines':scene2,'speakers':{scene2[0][0]:'polly',scene2[1][0]:'tom'},'rs':'forest','chars':[['polly',34,0,1.0],['tom',68,1,1.0]],'say':'Agora use as expressões.'})
    fr.append({'k':'pgsheet','title':'Complete as falas','items':[{'text':f'La situación incluye ___.','pt':f'A situação inclui {v[i][1]}.','opts':[v[i][0],v[(i+1)%6][0],v[(i+2)%6][0]],'a':0,'why':f'{v[i][0]} pertence à situação.','say':f'La situación incluye {v[i][0]}.'} for i in range(6)],'say':'Complete a fala.'})
    fr.append({'k':'pgsheet','title':'Qual está certa?','items':[{'ask':f'Qual opção usa “{v[i][0]}” corretamente?','opts':[f'La escena usa {v[i][0]}.',f'La escena usa {v[(i+1)%6][0]}?',f'La escena usa {v[(i+2)%6][0]}?'],'a':0,'why':'A primeira frase mantém a palavra da situação.'} for i in range(4)],'say':'Escolha a forma natural.'})
    sounds=[v[0][0],v[1][0],v[2][0]]
    fr.append({'k':'pglab','short':'sons','title':'Laboratório de sons','say':'Treine os sons da aula.','intro':{'what':'Ouça e repita.','how':'Compare os sons.','pt':'A pronúncia ajuda na compreensão.'},'ex':[[x,x,'palavra','som'] for x in sounds],'pairs':[[x,x+'a','compare os sons'] for x in sounds],'tip':'Repita devagar e depois acelere.','phrase':[scene2[0][1],scene2[0][2]],'rounds':[{'fig':'🎧','say':x,'ask':'Qual palavra você ouviu?','opts':[x,sounds[(i+1)%3],sounds[(i+2)%3]],'a':0,'why':'A resposta repete o som ouvido.'} for i,x in enumerate(sounds)]})
    fr.append({'k':'pgsheet','title':'Caça-sons','items':[{'fig':'🎧','say':v[i][0],'ask':'Qual palavra você ouviu?','opts':[v[i][0],v[(i+1)%6][0],v[(i+2)%6][0]],'a':0,'why':'A palavra pertence à cena.'} for i in range(6)],'say':'Ouça e encontre.'})
    fr.append({'k':'pgspeak','title':'Sua vez de falar','items':[[x[1],x[2]] for x in scene1[:5]],'who':'polly','say':'Repita e personalize.','rs':'lake','chars':[['polly',32,0,1.0],['tom',68,1,1.0]]})
    fr.append({'k':'pgmission','title':'Missão: sua vez!','missions':[{'ic':'🎬','name':'Cena da obra','data':{'prompt':f'Pratique: **{focus}.**','ph':scene1[0][1],'chips':[x[0] for x in v[:3]],'model':scene2[0][1],'check':['Usei o foco.','Falei com clareza.','Dei uma resposta completa.'],'kw':[v[0][0],v[1][0]],'tips':['Retome a cena.','Use duas palavras novas.','Finalize com intenção.'],'ok':['Foco presente.','Vocabulário usado.','Resposta completa.'],'reply':['Muito bem!','Você resolveu a situação.']}},{'ic':'🧭','name':'Situação real','data':{'prompt':f'Use **{focus}** em uma situação sua.','ph':scene2[1][1],'chips':[x[0] for x in v[2:5]],'model':scene2[1][1],'check':['Usei o padrão.','Escolhi palavras novas.','Mantive a intenção.'],'kw':[v[2][0]],'tips':['Pense em um lugar real.','Escolha uma ação.','Revise o final.'],'ok':['Padrão correto.','Ação clara.','Final natural.'],'reply':['Boa resposta!','A situação ficou clara.']}},{'ic':'✍️','name':'Produção livre','data':{'prompt':'Crie uma terceira resposta. **Inclua uma expressão da aula.**','ph':scene2[2][1],'chips':[x['en'] for x in ex[:2]],'model':scene2[2][1],'check':['Incluí uma expressão.','Usei o idioma-alvo.','Fui específico.'],'kw':[ex[0]['en']], 'tips':['Escolha uma expressão.','Relacione ao foco.','Leia em voz alta.'],'ok':['Expressão correta.','Idioma correto.','Detalhe presente.'],'reply':['Excelente!','Você criou uma fala própria.']}}],'say':'Escolha uma missão.'})
    fr.append({'k':'wrap','title':'Para levar','recap':[[x[0],x[1]] for x in v[:4]],'teaser':{'t':'Próxima situação','d':'A próxima situação amplia este repertório.'},'sticker':{'title':work,'sub':f'Obra · {year}','rs':'lake','chars':[['polly',50,0,1.0]]},'say':'Leve o que aprendeu.'})
    e['fr']=fr; e['v']=[[x[0],x[1],x[2]] for x in v]; e['o']=e['n']; e['presentation']='regular-pilot-v1'; e['pilot']=1
    return e

paths=list(Path(ROOT/'data').glob('es-a2_*.json'))
all_data=[]
for path in paths: all_data.extend([(path,i,e) for i,e in enumerate(json.loads(path.read_text(encoding='utf-8')))])
selected=[(p,i,e) for p,i,e in all_data if e.get('n') in TARGET]
selected.sort(key=lambda z:z[2]['n'])
prev=None
for p,i,e in selected:
 new=make(e,prev); pdat=json.loads(p.read_text(encoding='utf-8')); pdat[i]=new; p.write_text(json.dumps(pdat,ensure_ascii=False,separators=(',',':')),encoding='utf-8'); prev=new
print('converted',len(selected))
