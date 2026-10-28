"""Converte os episódios legados A2 950960–950999 para regular-pilot-v1."""
import copy, json, importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('base',ROOT/'tools/editorial/es_a2_189_198.py')
base=importlib.util.module_from_spec(spec); spec.loader.exec_module(base)

WORKS=[
('El museo de la memoria','2010','Santiago','Visita al museo','describir una exposición y expresar una impresión',['museo','entrada','sala','retrato','memoria','guía'],['visitar','observar','explicar','recordar'],['A primera vista','À primeira vista','De hecho','De fato','Por un lado','Por um lado','Al final','No fim'],('b e v'),['Lucía','Mateo']),
('La bicicleta de la ciudad','2012','Bogotá','Bicicleta pública','organizar un trayecto y pedir una indicación',['bicicleta','carril','casco','semáforo','esquina','mapa'],['pedalear','girar','buscar','llegar'],['Por aquí','Por aqui','A la vuelta','Na volta','Con cuidado','Com cuidado','Ya que','Já que'],('b e v'),['Marta','Diego']),
('El mercado de los recuerdos','2008','Quito','Mercado local','comparar productos y negociar una compra',['mercado','puesto','precio','canasta','fruta','moneda'],['mirar','comparar','elegir','pagar'],['Cuánto cuesta','Quanto custa','Por ahora','Por enquanto','Me parece','Parece-me','Al final','No fim'],('r e rr'),['Nora','Iván']),
('La casa de los espíritus del barrio','1982','Chile','Casa familiar','describir una casa y contar una costumbre',['pasillo','patio','ventana','abuela','costumbre','recuerdo'],['vivir','crecer','contar','cuidar'],['De pequeño','Quando eu era pequeno','Cada vez que','Cada vez que','Por entonces','Naquela época','Qué curioso','Que curioso'],('b e v'),['Elena','Rafael']),
('El jardín de los senderos','1941','Buenos Aires','Jardín comunitario','proponer una mejora y repartir tareas',['jardín','semilla','sendero','regadera','banco','sombra'],['plantar','regar','limpiar','proponer'],['Entre todos','Entre todos','Poco a poco','Pouco a pouco','Qué buena idea','Que boa ideia','De cara a','Pensando em'],('ll e y'),['Ana','Bruno']),
('La voz del puerto','2019','Valparaíso','Radio local','relatar una noticia y comprobar una fuente',['puerto','radio','noticia','fuente','barco','barrio'],['escuchar','informar','confirmar','transmitir'],['Según parece','Ao que parece','Por lo visto','Pelo visto','De momento','Por enquanto','Sin duda','Sem dúvida'],('r e rr'),['Sofía','Tomás']),
('El sabor de la lluvia','2016','Medellín','Café de barrio','pedir una bebida y comentar el ambiente',['cafetería','taza','grano','lluvia','mesa','aroma'],['pedir','servir','probar','comentar'],['Para empezar','Para começar','Qué rico','Que gostoso','A propósito','A propósito','Enseguida','Imediatamente'],('r e rr'),['Camila','Julián']),
('El mapa de las montañas','2005','Cusco','Trilha de montanha','descrever uma rota e dar um conselho',['montaña','sendero','mochila','puente','altura','descanso'],['subir','seguir','llevar','descansar'],['A mitad de camino','No meio do caminho','Por si acaso','Por via das dúvidas','Más vale','É melhor','Que yo sepa','Que eu saiba'],('ll e y'),['Paula','Iván']),
('La plaza de las voces','2014','Oaxaca','Praça do bairro','convidar pessoas e combinar um evento',['plaza','cartel','vecino','música','escenario','fecha'],['invitar','organizar','colgar','participar'],['Nos vemos','A gente se vê','Qué te parece','O que você acha','Entre todos','Entre todos','A partir de ahora','A partir de agora'],('j e g'),['Marina','Leo']),
('El tren de la frontera','2017','Montevideo','Viagem de trem','contar um plano e confirmar horários',['tren','andén','billete','horario','maleta','frontera'],['salir','llegar','confirmar','guardar'],['A qué hora','A que horas','En punto','Em ponto','Por lo tanto','Portanto','Hasta luego','Até logo'],('r e rr'),['Valeria','Nicolás']),
]
# 40 episodios: cada bloco repete o cenário comunicativo com léxico e obra distintos.
rows=[]
for i in range(40):
    w,y,place,short,focus,nouns,verbs,expr,sound,names=WORKS[i%len(WORKS)]
    # pequenas variações para que cada roteiro seja realmente específico
    suffix=['una decisión','una pregunta','un cambio','una visita'][i//10]
    title=f'{short}: {suffix} {i+1}'
    work=f'{w} · edición {i+1}'
    desc=f'La referencia cultural {w} abre una situación autoral en {place}. La escena invita a resolver una tarea cotidiana, explicar una elección y escuchar otra perspectiva.'
    v=[]
    ptmap={'museo':'museu','entrada':'entrada','sala':'sala','retrato':'retrato','memoria':'memória','guía':'guia','bicicleta':'bicicleta','carril':'ciclovia','casco':'capacete','semáforo':'semáforo','esquina':'esquina','mapa':'mapa','mercado':'mercado','puesto':'barraca','precio':'preço','canasta':'cesta','fruta':'fruta','moneda':'moeda','pasillo':'corredor','patio':'pátio','ventana':'janela','abuela':'avó','costumbre':'costume','recuerdo':'lembrança','jardín':'jardim','semilla':'semente','sendero':'trilha','regadera':'regador','banco':'banco','sombra':'sombra','puerto':'porto','radio':'rádio','noticia':'notícia','fuente':'fonte','barco':'barco','barrio':'bairro','cafetería':'cafeteria','taza':'xícara','grano':'grão','lluvia':'chuva','mesa':'mesa','aroma':'aroma','montaña':'montanha','mochila':'mochila','puente':'ponte','altura':'altura','descanso':'descanso','plaza':'praça','cartel':'cartaz','vecino':'vizinho','música':'música','escenario':'palco','fecha':'data','tren':'trem','andén':'plataforma','billete':'bilhete','horario':'horário','maleta':'mala','frontera':'fronteira'}
    for j,n in enumerate(nouns): v.append((n,ptmap.get(n,n),f'{n[:3].upper()}-a'))
    # manter seis entradas
    s1=[[names[0],f'En {place}, preparamos {nouns[0]} para la actividad.',f'Em {place}, preparamos {ptmap.get(nouns[0],nouns[0])} para a atividade.'],[names[1],f'¿Trajiste {nouns[1]} y {nouns[2]}?',f'Você trouxe {ptmap.get(nouns[1],nouns[1])} e {ptmap.get(nouns[2],nouns[2])}?'],[names[0],f'Sí, también guardé {nouns[3]} en la mochila.',f'Sim, também guardei {ptmap.get(nouns[3],nouns[3])} na mochila.'],[names[1],f'¿Qué propones para resolver la situación?',f'O que você propõe para resolver a situação?'],[names[0],f'{expr[0]}, podemos {verbs[0]} juntos.',f'{expr[1]}, podemos {verbs[0]} juntos.'],[names[1],f'{expr[2]}, primero debemos {verbs[1]} el lugar.',f'{expr[3]}, primeiro precisamos {verbs[1]} o lugar.'],[names[0],f'{expr[4]}, comprobamos {nouns[4]} antes de empezar.',f'{expr[5]}, verificamos {ptmap.get(nouns[4],nouns[4])} antes de começar.'],[names[1],f'{expr[6]}, la decisión queda clara.',f'{expr[7]}, a decisão fica clara.']]
    s2=[[names[0],f'**{expr[0]}**, revisamos {nouns[0]} otra vez.',f'{expr[1]}, revisamos {ptmap.get(nouns[0],nouns[0])} outra vez.'],[names[1],f'**{expr[2]}**, usamos la ruta más segura.',f'{expr[3]}, usamos a rota mais segura.'],[names[0],f'**{expr[4]}**, podemos pedir otra opinión.',f'{expr[5]}, podemos pedir outra opinião.'],[names[1],f'**{expr[6]}**, terminamos la tarea juntos.',f'{expr[7]}, terminamos a tarefa juntos.'],[names[0],f'La actividad empieza después de {nouns[5]}.',f'A atividade começa depois de {ptmap.get(nouns[5],nouns[5])}.'],[names[1],f'Cada persona tiene una tarea concreta.',f'Cada pessoa tem uma tarefa concreta.'],[names[0],f'Después contamos lo que aprendimos.',f'Depois contamos o que aprendemos.'],[names[1],f'Y dejamos una idea para la próxima vez.',f'E deixamos uma ideia para a próxima vez.']]
    rows.append({'n':950960+i,'t':title,'focus':focus,'work':work,'year':y,'desc':desc,'region':place,'v':v,'vb':verbs,'ex':expr,'sound':(sound,[x[0] for x in v[:3]]),'s1':s1,'s2':s2})

# Locate records and rebuild sequentially. First episode uses the preceding legacy episode for review.
files={}
for path in (ROOT/'data').glob('es-a2_*.json'):
 data=json.loads(path.read_text(encoding='utf-8'))
 for e in data: files[e['n']]=(path,e)
prev=files[950959][1]
for p in rows:
 path,old=files[p['n']]
 new=base.make(old,p,prev)
 new['t']=p['t']; new['s']=f"{p['region']} · {p['focus']} · referencia: {p['work']} · {p['year']}"
 new['a']['w']=p['work']; new['a']['y']=p['year']; new['presentation']='regular-pilot-v1'; new['pilot']=1; new['lv']='A2'
 files[p['n']]=(path,new); prev=new
for path in sorted({p for p,e in files.values()}):
 data=json.loads(path.read_text(encoding='utf-8'))
 repl={n:e for n,(p,e) in files.items() if p==path and 950960<=n<=950999}
 if repl:
  for i,e in enumerate(data):
   if e['n'] in repl: data[i]=repl[e['n']]
  path.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
print('converted',len(rows))
