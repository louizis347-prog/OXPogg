import json, importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('base',ROOT/'tools/editorial/es_a2_189_198.py'); base=importlib.util.module_from_spec(spec); spec.loader.exec_module(base)
# Conversão editorial: usa a referência cultural legada de cada episódio como obra principal,
# mas reconstrói todo o roteiro no contrato A1, sem reaproveitar os quadros antigos.
PT={'casa':'casa','calle':'rua','amigo':'amigo','familia':'família','libro':'livro','foto':'foto','pan':'pão','agua':'água','escuela':'escola','trabajo':'trabalho','parque':'parque','tienda':'loja','día':'dia','hora':'hora','comida':'comida','música':'música','puerta':'porta','mesa':'mesa','ciudad':'cidade','viaje':'viagem','mercado':'mercado','precio':'preço','mapa':'mapa','plaza':'praça','barrio':'bairro','estación':'estação','hotel':'hotel','café':'café','familia':'família'}
NOUNS=list(PT.keys()); VERBS=['hablar','mirar','buscar','comprar','vivir','tener','ir','hacer','querer','poder','necesitar','encontrar','llevar','dar','decir','venir','comer','beber','leer','escribir']; EX=[('Hola','Olá','¿Qué tal?','Tudo bem?','Por favor','Por favor','Gracias','Obrigado'),('Buenos días','Bom dia','Hasta luego','Até logo','Con permiso','Com licença','De acuerdo','Certo'),('Me gusta','Eu gosto','No sé','Não sei','Por supuesto','É claro','Qué bien','Que bom'),('¿Dónde está?','Onde fica?','Aquí está','Aqui está','Un momento','Um momento','Muchas gracias','Muito obrigado')]
files={}
for path in (ROOT/'data').glob('es-a1_*.json'):
 data=json.loads(path.read_text(encoding='utf8'))
 for e in data: files[e['n']]=(path,e)
ids=sorted(n for n in files if 950400<=n<=950499)
prev=files.get(7071200,(None,None))[1]
for i,n in enumerate(ids):
 path,old=files[n]
 review=next((f for f in old.get('fr',[]) if f.get('k')=='review'),{})
 work=review.get('work') or f'Referencia cultural A1 {i+401}'
 focus=(old.get('s') or 'hablar de una situación cotidiana').split('·')[0].strip()
 place=(old.get('s') or 'Comunidades hispanas').split('·')[0].strip()
 nouns=[NOUNS[(i+j)%len(NOUNS)] for j in range(6)]; v=[(x,PT[x],x[:3].upper()) for x in nouns]; vb=[VERBS[(i+j)%len(VERBS)] for j in range(4)]; ex=list(EX[i%len(EX)]); names=['Lucía','Mateo'] if i%2==0 else ['Marta','Diego']
 s1=[[names[0],f'En {place}, hablamos de {nouns[0]}.',f'Em {place}, falamos de {PT[nouns[0]]}.'],[names[1],f'¿Trajiste {nouns[1]} y {nouns[2]}?',f'Você trouxe {PT[nouns[1]]} e {PT[nouns[2]]}?'],[names[0],f'Sí, también tengo {nouns[3]}.',f'Sim, também tenho {PT[nouns[3]]}.'],[names[1],'¿Qué podemos hacer ahora?','O que podemos fazer agora?'],[names[0],f'{ex[0]}, podemos {vb[0]} juntos.',f'{ex[1]}, podemos {vb[0]} juntos.'],[names[1],f'{ex[2]}, primero vamos a {vb[1]}.',f'{ex[3]}, primeiro vamos {vb[1]}.'],[names[0],f'{ex[4]}, después vamos a {vb[2]}.',f'{ex[5]}, depois vamos {vb[2]}.'],[names[1],f'{ex[6]}, la situación está clara.',f'{ex[7]}, a situação está clara.']]
 s2=[[names[0],f'**{ex[0]}**, repetimos la idea.',f'{ex[1]}, repetimos a ideia.'],[names[1],f'**{ex[2]}**, seguimos el plan.',f'{ex[3]}, seguimos o plano.'],[names[0],f'**{ex[4]}**, pedimos ayuda.',f'{ex[5]}, pedimos ajuda.'],[names[1],f'**{ex[6]}**, terminamos juntos.',f'{ex[7]}, terminamos juntos.'],[names[0],f'La actividad es en {place}.',f'A atividade é em {place}.'],[names[1],'Cada persona tiene una tarea.','Cada pessoa tem uma tarefa.'],[names[0],'Después contamos lo que aprendimos.','Depois contamos o que aprendemos.'],[names[1],'Y dejamos una idea para la próxima vez.','E deixamos uma ideia para a próxima vez.']]
 p={'n':n,'focus':focus,'work':work,'year':'s.d.','desc':f'La referencia cultural {work} abre una situación A1 en {place}. La escena invita a nombrar, pedir y responder con claridad.','region':place,'v':v,'vb':vb,'ex':ex,'sound':('vocales y ritmo',[x[0] for x in v[:3]]),'s1':s1,'s2':s2}
 new=base.make(old,p,prev); new['n']=n; new['t']=f'{focus} · A1 {i+401}'; new['s']=f'{place} · {focus} · referencia: {work}'; new['a']={'k':'🎬 Obra','w':work,'y':'s.d.','d':p['desc']}; new['lv']='A1'; new['cefr']='A1'; new['presentation']='regular-pilot-v1'; new['pilot']=1; new['p']=f'Hoje você aprende a {focus.lower()}.'
 cover=next(f for f in new['fr'] if f.get('k')=='cover'); cover.update({'badge':'A1','obra':work,'sub':f'Español para brasileños · A1 · episódio {i+401}','say':f'Hoje você vai {focus.lower()}.'})
 files[n]=(path,new); prev=new
for path in sorted({p for p,e in files.values() if any(p==pp and 950400<=nn<=950499 for nn,(pp,ee) in files.items())}):
 data=json.loads(path.read_text(encoding='utf8')); repl={n:e for n,(p,e) in files.items() if p==path and 950400<=n<=950499}
 for i,e in enumerate(data):
  if e['n'] in repl: data[i]=repl[e['n']]
 path.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')),encoding='utf8')
print('converted',len(ids))
