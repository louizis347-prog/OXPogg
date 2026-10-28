import json, glob
from pathlib import Path

WORKS = [
 ('Los diarios de motocicleta','filme','2004'),('El mercader de Venecia','teatro','1596'),('La Celestina','obra literaria','1499'),('Don Quijote de la Mancha','novela','1605'),('Fuenteovejuna','teatro','1619'),('El burlador de Sevilla','teatro','1630'),('Poeta en Nueva York','poesía','1929'),('Veinte poemas de amor','poesía','1924'),('La muerte de Artemio Cruz','novela','1962'),('El lugar sin límites','novela','1966'),('El cuento de la criada','novela','1985'),('El juguete rabioso','novela','1926'),('La ciudad de los prodigios','novela','1986'),('Nada','novela','1945'),('El árbol de la ciencia','novela','1911'),('La verdad sobre el caso Savolta','novela','1975'),('La plaza del Diamante','novela','1962'),('Los santos inocentes','novela','1981'),('El buen patrón','filme','2021'),('La reconquista','filme','2016'),('El candidato','filme','2016'),('Una mujer fantástica','filme','2017'),('Gloria','filme','2013'),('No','filme','2012'),('Conducta','filme','2014'),('Los pasos de la memoria','proyecto cultural','2020'),('La casa de las palabras','biblioteca comunitaria','2018'),('El mapa de los afectos','novela','2020'),('La voz de los árboles','documental','2019'),('La plaza de los oficios','centro cultural','2021'),('La ruta de las luciérnagas','documental','2022'),('El archivo de las mareas','exposición','2021'),('La estación de las preguntas','podcast','2020'),('El barrio de los nombres','crónica','2019'),('La ventana abierta','cuento','1921'),('El jardín de senderos','cuento','1941'),('El libro de los abrazos','crónica','1989'),('La música de las esferas','concierto','2017'),('El puente de los recuerdos','instalación','2022'),('La ciudad que escucha','proyecto artístico','2023')]

# locations are distinct enough for the visual setting
SCENES=['plaza','cafe','station','market','library','museum','coast','mountain','garden','workshop']
VERBSETS=[['organizar','explicar','elegir','confirmar'],['proponer','comparar','resolver','avisar'],['reservar','revisar','cambiar','avisar'],['buscar','encontrar','recomendar','compartir'],['preparar','invitar','aceptar','agradecer']]
EXPS=[['por eso','sin embargo','a fin de cuentas','de momento'],['por si acaso','en cambio','al final','desde luego'],['de todos modos','por lo visto','en realidad','a partir de ahora'],['qué te parece','con tal de que','por un lado','por otro lado'],['hasta cierto punto','en primer lugar','a la vez','en resumen']]
ICONS=['🧭','📌','🌱','🎒','🗺️','🔎']

def old_files():
  return ['data/es-a2_13.json','data/es-a2_14.json']

def make_episode(e, idx):
  n=e['n']; oldv=e.get('v',[])[:6]
  while len(oldv)<6: oldv.append([f'palabra{len(oldv)+1}','palavra',''])
  vocab=[(str(x[0]),str(x[1])) for x in oldv]
  work,kind,year=WORKS[idx]
  region=e.get('region') or ['España','México','Caribe hispánico','Andes','Cono Sur'][idx%5]
  situation=(e.get('authorship') or {}).get('situation') or e.get('s','').split('·')[1].strip() if '·' in e.get('s','') else e.get('t','').lower()
  situation=situation.replace('referencia:', '').strip()
  topic=f'{region} · {situation}'
  title=f"{e.get('t','Situación nueva')} · {work}"
  # Ensure title is unique and natural enough while retaining the old trigger.
  wwords=[v[0] for v in vocab]
  verbs=VERBSETS[idx%len(VERBSETS)]
  exps=EXPS[idx%len(EXPS)]
  names=['Lucía','Mateo']
  a,b=names
  line_text=[
    f'{a}: Hoy necesitamos {verbs[0]} la situación con calma.',
    f'{b}: Primero quiero {verbs[1]} lo que ocurrió.',
    f'{a}: Tengo que revisar {wwords[0]} y {wwords[1]}.',
    f'{b}: **{exps[0]}**, podemos elegir una salida.',
    f'{a}: Entonces propongo {verbs[2]} el siguiente paso.',
    f'{b}: **{exps[1]}**, escucho tu propuesta.',
    f'{a}: También podemos usar {wwords[2]} y {wwords[3]}.',
    f'{b}: De acuerdo; vamos a {verbs[3]} antes de terminar.'
  ]
  def lines(trans=True, second=False):
    out=[]
    for i,s in enumerate(line_text):
      speaker=s.split(':',1)[0]; txt=s.split(':',1)[1].strip()
      if second: txt=txt.replace('Hoy','Mañana').replace('Primero','Después').replace('Entonces','Por eso')
      pt=txt.replace('Hoy','Hoje').replace('Mañana','Amanhã').replace('necesitamos','precisamos').replace('con calma','com calma').replace('Primero quiero','Primeiro quero').replace('revisar','revisar').replace('Tengo que','Tenho que').replace('podemos','podemos').replace('elegir','escolher').replace('Entonces propongo','Então proponho').replace('escucho tu propuesta','ouço sua proposta').replace('También podemos usar','Também podemos usar').replace('De acuerdo; vamos a','Certo; vamos').replace('antes de terminar','antes de terminar').replace('la situación','a situação').replace('lo que ocurrió','o que aconteceu').replace('el siguiente paso','o próximo passo')
      out.append([speaker,txt,pt])
    return out
  scene1=lines(); scene2=lines(second=True)
  cover={'k':'cover','art':{'s':SCENES[idx%len(SCENES)],'items':[['🧭',28,72,15,'bob'],['📚',55,66,16,'bob'],['✨',82,58,15,'bob']],'seed':f'es-a2-{n}'},'sub':f'{situation}: em 10 minutos você resolve uma situação real','badge':'A2','snd':'bell','say':f'{a} e {b} enfrentam uma situação ligada a {situation}.','gancho':[a,scene1[0][1],scene1[0][2]],'obra':f'{work} · {year}','stage':{'rs':SCENES[idx%len(SCENES)],'chars':[['polly',34,0,1.0],['tom',68,1,1.0]]}}
  review={'k':'review','prev':'A situação do episódio anterior','work':WORKS[idx-1][0] if idx else work,'recap':[[vocab[i][0],vocab[i][1]] for i in range(4)],'bag':[{'ic':'🔤','l':'Palavras','items':[{'ic':'🔤','t':x,'pt':y} for x,y in vocab[:4]]},{'ic':'🏃','l':'Verbos','items':[{'ic':'🏃','t':v,'pt':v} for v in verbs]}],'lead':'Abra a mochila e recupere uma ideia anterior.','next':f'Hoje: {situation}','say':'Recupere e avance.'}
  hot=[{'e':ICONS[i],'x':18+i*17,'y':25+(i%2)*18,'en':vocab[i][0],'pt':vocab[i][1],'say':vocab[i][0],'sayPt':vocab[i][1]} for i in range(5)]
  hotscene={'k':'hotscene','title':'Explore a cena','hint':'Toque nos elementos e ouça.','rs':SCENES[idx%len(SCENES)],'chars':[['polly',34,0,1.0],['tom',68,1,1.0]],'hot':hot,'say':'Observe antes de responder.'}
  qs=[{'ask':q,'speak':q,'pt':q,'opts':[[f'{a} inicia a situação',''],['Apenas repete',''],['Não há informação','']],'a':0,'why':'A cena apresenta essa intenção.'} for q in ['Qual é a situação central?','Quem propõe o próximo passo?','Que palavra ajuda a avançar?']]
  pg_sheet={'k':'pgsheet','title':'Você entendeu?','items':qs,'say':'Confira intenção e informação.'}
  rule_head=f'{verbs[0]} + infinitivo · expressões para organizar a conversa'
  pgrule={'k':'pgrule','rule':{'who':a,'head':rule_head,'sub':situation,'say':[f'Hoje usamos {rule_head} em contexto.',f'Observe a forma dentro da conversa.'],'formula':[],'uses':[{'ico':'📌','tag':x,'en':x,'pt':x} for x in exps],'rules':['Observe a relação entre forma e intenção.','Use a estrutura dentro de uma frase completa.'],'tips':['Leia a frase inteira antes de escolher.']},'q':{'ask':'Qual opção pertence ao padrão?','opts':[rule_head,'uma palavra isolada','um nome próprio'],'a':0,'why':'O padrão aparece na cena.'},'say':'Descubra o padrão.'}
  pages=[{'label':'Abrir','slots':[{'label':'Pessoa','options':[a,b]},{'label':'Ação','options':verbs[:2]}],'end':['.']},{'label':'Desenvolver','slots':[{'label':'Conector','options':exps[:2]},{'label':'Palavra','options':wwords[:3]}],'end':['.']},{'label':'Fechar','slots':[{'label':'Ação','options':verbs[2:]},{'label':'Conector','options':exps[2:]}],'end':['.']}]
  pgmold={'k':'pgmold','title':'Molde de frases','pages':pages,'say':'Monte frases com intenção.'}
  verb_items=[]
  for i,v in enumerate(verbs): verb_items.append({'v':v,'ic':ICONS[i],'pt':v,'f':[['yo',f'yo {v}'],['él',f'él {v}']], 'ex':[f'{a} {v} la situación.',f'{a} {v} a situação.'],'note':f'Use **{v}** no contexto.'})
  verbsf={'k':'verbs','title':'Verbos da situação','items':verb_items,'tip':'Quatro verbos em uso comunicativo.','quiz':[{'text':f'Yo ___ la situación.','opts':[v,verbs[(i+1)%4],verbs[(i+2)%4]],'a':0,'why':f'Use {v} no contexto.'} for i,v in enumerate(verbs)],'say':'Veja os verbos em uso.'}
  vplay={'k':'vplay','title':'Missão dos verbos','items':verb_items,'plan':[[0,0],[1,0],[2,0],[3,0],[0,3],[1,3],[2,3]],'say':'Use os quatro verbos.'}
  exp_items=[{'ic':ICONS[i],'en':x,'tag':'Expressão','pt':x,'use':f'Use **{x}** no contexto.','ex':[f'{x}, seguimos con cuidado.',f'{x}, seguimos com cuidado.']} for i,x in enumerate(exps)]
  pgexp={'k':'pgexp','title':'Expressões em uso','items':exp_items,'quiz':[{'ask':'Qual expressão pertence à situação?','opts':[x,exps[(i+1)%4],exps[(i+2)%4]],'a':0,'why':f'{x} aparece na cena.'} for i,x in enumerate(exps)],'say':'Escolha a expressão adequada.'}
  pglab={'k':'pglab','short':'r e j','title':'Laboratório de sons','say':'Treine os sons de hoje.','intro':{'what':'Ouça e repita os sons ligados às palavras da aula.','how':'Comece devagar e depois junte a frase.','pt':'A pronúncia é escrita para brasileiros.'},'ex':[[v.upper(),v.upper(),v,'repita com clareza'] for v in wwords[:3]],'pairs':[[v,v+'a','contraste de ritmo'] for v in wwords[:3]],'tip':'Não acrescente vogais ao final das palavras.','phrase':[scene1[0][1],scene1[0][2]],'rounds':[{'fig':'🎧','say':v,'ask':'Qual palavra você ouviu?','opts':[v,wwords[(i+1)%6],wwords[(i+2)%6]],'a':0,'why':f'{v} é a resposta.'} for i,v in enumerate(wwords[:3])]}
  pgsheet2={'k':'pgsheet','title':'Recupere e transforme','items':[{'ask':f'Reescreva usando {x}.','speak':f'Reescreva usando {x}.','pt':f'Reescreva usando {x}.','opts':[[x,x],['otra opción','outra opção'],['sin relación','sem relação']],'a':0,'why':'A escolha mantém a intenção.'} for x in exps[:3]],'say':'Transforme a frase com intenção.'}
  pgsheet3={'k':'pgsheet','title':'Ponte cultural e linguística','items':[{'ask':f'Como você usaria {v}?','speak':f'Como você usaria {v}?','pt':f'Como você usaria {v}?','opts':[[f'En una frase sobre {situation}',f'Em uma frase sobre {situation}'],['No contexto errado','No contexto errado'],['Sem verbo','Sem verbo']],'a':0,'why':'A palavra ganha sentido em uma situação.'} for v in wwords[:3]],'say':'Relacione palavra, situação e intenção.'}
  pgsheet4={'k':'pgsheet','title':'Desafio de compreensão','items':[{'ask':'Qual resposta mantém a conversa?','speak':'Qual resposta mantém a conversa?','pt':'Qual resposta mantém a conversa?','opts':[[scene2[i][1],scene2[i][2]],[exps[(i+1)%4],''],['No responde','Não responde']],'a':0,'why':'A resposta retoma o objetivo.'} for i in range(3)],'say':'Escolha a resposta que faz a conversa avançar.'}
  scene2f={'k':'pgscene','title':'Segunda situação cotidiana','cast':{'A':['👩','#a94b6b'],'B':['🧑','#276b7a']},'lines':scene2,'speakers':{a:'polly',b:'tom'},'rs':SCENES[(idx+2)%len(SCENES)],'chars':[['polly',34,0,1.0],['tom',68,1,1.0]],'say':'Agora use as expressões em outro contexto.'}
  pgspeak={'k':'pgspeak','title':'Sua vez de falar','items':[[scene2[i][1],scene2[i][2]] for i in range(5)],'who':'polly','say':'Repita e personalize.','rs':SCENES[idx%len(SCENES)],'chars':[['polly',32,0,1.0],['tom',68,1,1.0]]}
  missions=[{'ic':'🎬','name':'Cena da obra','data':{'prompt':f'Pratique: {situation}.','ph':scene1[0][1],'chips':wwords[:3],'model':scene1[1][1],'check':['Usei o foco.','Falei com clareza.','Dei uma resposta completa.'],'kw':wwords[:2],'tips':['Retome a cena.','Use duas palavras novas.','Finalize com intenção.'],'ok':['Foco presente.','Vocabulário usado.','Resposta completa.'],'reply':['Muito bem!','Você resolveu a situação.']}},{'ic':'🧭','name':'Situação do aluno','data':{'prompt':f'Use {situation} em uma situação sua.','ph':scene2[0][1],'chips':wwords[2:5],'model':scene2[1][1],'check':['Usei o padrão.','Escolhi palavras novas.','Mantive a intenção.'],'kw':wwords[2:4],'tips':['Pense em um lugar real.','Escolha uma ação.','Revise o final.'],'ok':['Padrão correto.','Ação clara.','Final natural.'],'reply':['Boa resposta!','A situação ficou clara.']}},{'ic':'✍️','name':'Produção livre','data':{'prompt':'Crie uma terceira resposta com uma expressão da aula.','ph':scene2[2][1],'chips':exps[:2],'model':scene2[2][1],'check':['Incluí uma expressão.','Usei o idioma-alvo.','Fui específico.'],'kw':exps[:1],'tips':['Escolha uma expressão.','Relacione ao foco.','Leia em voz alta.'],'ok':['Expressão correta.','Idioma correto.','Detalhe presente.'],'reply':['Excelente!','Você criou uma fala própria.']}}]
  pgmission={'k':'pgmission','title':'Missão: sua vez!','missions':missions,'say':'Escolha uma missão.'}
  wrap={'k':'wrap','title':'Para levar','recap':[[x,y] for x,y in vocab[:4]],'teaser':{'t':'Próxima situação','d':'A próxima missão amplia este repertório.'},'sticker':{'title':work,'sub':f'{kind} · {year}','rs':SCENES[idx%len(SCENES)],'chars':[['polly',50,0,1.0]]},'say':'Leve o que aprendeu para a próxima situação.'}
  e['t']=title; e['s']=f'{region} · {situation} · referencia: {work} · {year}'; e['a']={'k':kind,'w':work,'y':year,'d':f'{work} apresenta uma situação cultural que abre espaço para falar de {situation}.'}; e['presentation']='regular-pilot-v1'; e['pilot']=1; e['fr']=[cover,review,hotscene,{'k':'pgscene','cast':{'A':['👩','#a94b6b'],'B':['🧑','#276b7a']},'lines':scene1,'speakers':{a:'polly',b:'tom'},'rs':SCENES[idx%len(SCENES)],'chars':[['polly',34,0,1.0],['tom',68,1,1.0]],'say':'Ouça e leia a cena.'},pg_sheet,pgrule,pgmold,{'k':'pgsheet','title':'Palavras em frases','items':[{'ask':f'Use {v[0]} numa frase.','speak':f'Use {v[0]} numa frase.','pt':f'Use {v[0]} numa frase.','opts':[[f'{v[0]} aparece em contexto.',f'{v[1]} aparece em contexto.'],['Sem contexto',''],['Outra estrutura','']],'a':0,'why':'A palavra aparece em uma frase real.'} for v in vocab],'say':'Ligue cada palavra a uma frase real.'},verbsf,vplay,pgexp,scene2f,pgsheet2,pgsheet3,pglab,pgsheet4,pgspeak,pgmission,wrap]
  e['v']=[[w,p,f'Soa como “{w}”.'] for w,p in vocab]
  return e

paths=old_files(); changed=[]
idx=0
for path in paths:
 data=json.load(open(path)); dirty=False
 for e in data:
  if 801<=e.get('n',0)<=840:
   e2=make_episode(e,idx); data[data.index(e)]=e2; idx+=1; dirty=True
 if dirty:
  with open(path,'w') as fh: json.dump(data,fh,ensure_ascii=False,separators=(',',':'))
  changed.append(path)
print('changed',changed,'episodes',idx)
