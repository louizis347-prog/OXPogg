"""Reelabora o bloco legado A2 761–800 no padrão regular-pilot-v1."""
import ast, copy, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
base=ROOT/'tools/editorial/es_a2_189_198.py'
tree=ast.parse(base.read_text(encoding='utf-8'))
ns={'copy':copy}
for node in tree.body:
    if isinstance(node,ast.FunctionDef) and node.name in {'make','verbs_pt'}:
        exec(compile(ast.Module(body=[node], type_ignores=[]),str(base),'exec'),ns)
make=ns['make']

FOCUS_PT={
 'comparar dos barrios':'comparar dois bairros','describir una experiencia laboral':'descrever uma experiência profissional',
 'explicar un plan de fin de semana':'explicar um plano de fim de semana','contar un viaje reciente':'contar uma viagem recente',
 'cambiar una reserva':'mudar uma reserva','hacer una reclamación educada':'fazer uma reclamação educada',
 'organizar una celebración':'organizar uma celebração','resolver un problema de transporte':'resolver um problema de transporte',
 'hablar de una fotografía':'falar de uma fotografia','proponer una mejora':'propor uma melhoria',
 'narrar una decisión':'narrar uma decisão','pedir orientaciones':'pedir orientações','comentar una tradición':'comentar uma tradição',
 'describir una escena':'descrever uma cena','expresar una preferencia':'expressar uma preferência',
}
VERBS=[
 'comparar','explicar','contar','organizar','resolver','proponer','describir','reconocer','preparar','confirmar',
 'revisar','acordar','reservar','elegir','recomendar','buscar','cambiar','compartir','invitar','celebrar',
 'recordar','imaginar','observar','proteger','encontrar','esperar','visitar','caminar','subir','bajar',
 'aprender','practicar','preguntar','responder','avisar','entender','aclarar','decidir','comenzar','terminar'
]
EXPRS=[
 ('Por eso','Por isso'),('A decir verdad','Para dizer a verdade'),('De todos modos','De todo modo'),('Si te parece','Se você achar bom'),
 ('En primer lugar','Em primeiro lugar'),('A fin de cuentas','No fim das contas'),('Por lo visto','Pelo visto'),('En cambio','Em contrapartida'),
 ('Por un lado','Por um lado'),('Por otro lado','Por outro lado'),('De momento','Por enquanto'),('Al final','No final'),
 ('A partir de ahora','A partir de agora'),('En ese caso','Nesse caso'),('Con tal de que','Desde que'),('Sin embargo','No entanto'),
 ('De hecho','De fato'),('Por si acaso','Por via das dúvidas'),('En pocas palabras','Em poucas palavras'),('A la larga','A longo prazo'),
 ('Hasta cierto punto','Até certo ponto'),('En principio','A princípio'),('Dicho esto','Dito isso'),('Como mínimo','No mínimo'),
 ('Lo más importante','O mais importante'),('De vez en cuando','De vez em quando'),('Mientras tanto','Enquanto isso'),('En realidad','Na realidade'),
 ('Por lo tanto','Portanto'),('A propósito','A propósito'),('Sin duda','Sem dúvida'),('Por ahora','Por agora'),
 ('En general','Em geral'),('A primera vista','À primeira vista'),('En resumen','Em resumo'),('De acuerdo','De acordo'),
 ('Qué buena idea','Que boa ideia'),('Tiene sentido','Faz sentido'),('Vamos por partes','Vamos por partes'),('Vale la pena','Vale a pena'),
]
NAMES=[('Lucía','Mateo'),('Inés','Bruno'),('Camila','Sergio'),('Nora','Tomás'),('Valentina','Diego'),('Marta','Iván'),('Elena','Julián'),('Paula','Raúl'),('Sofía','Andrés'),('Clara','Nicolás')]

def clean_word(item):
    w=str(item[0]).strip().split()[0].strip('.,;:!?¿¡()[]')
    pt=str(item[1]).strip().split(',')[0].strip() if len(item)>1 else w
    pr=str(item[2]).strip() if len(item)>2 else w
    return [w,pt,pr]

def focus_data(e):
    raw=e.get('s','')
    parts=[x.strip() for x in raw.split('·')]
    region=parts[0] if parts else 'la comunidad'
    focus=parts[1] if len(parts)>1 else 'resolver una situación cotidiana'
    focus=focus.strip()
    for a,b in {
      'comparar dois bairros':'comparar dos barrios','descrever uma experiência laboral':'describir una experiencia laboral',
      'explicar um plano de fim de semana':'explicar un plan de fin de semana','contar uma viagem recente':'contar un viaje reciente',
      'mudar uma reserva':'cambiar una reserva','fazer uma reclamação educada':'hacer una reclamación educada',
      'organizar uma celebração':'organizar una celebración','resolver um problema de transporte':'resolver un problema de transporte',
      'descrever uma experiência profissional':'describir una experiencia laboral','falar de uma fotografia':'hablar de una fotografía',
    }.items(): focus=focus.replace(a,b)
    return region,focus

def old_work(e):
    a=e.get('a') or {}
    if a.get('w'): return str(a['w']),str(a.get('y','s. XX')),str(a.get('d',''))
    for fr in e.get('fr',[]):
        if fr.get('k')=='cover' and fr.get('work'): return str(fr['work']),str(fr.get('year','s. XX')),str(fr.get('intro',''))
    return 'Una referencia cultural', 's. XX', ''

def unique_work(e,used):
    w,y,d=old_work(e)
    if w not in used: return w,y,d
    # Preserve a concrete cultural reference while avoiding collisions.
    bank=['El Museo del Oro de Bogotá','El Gran Teatro de La Habana','El Carnaval de Barranquilla','Las Islas Galápagos','La Biblioteca Vasconcelos','El Mercado de San Miguel','El Parque Nacional Tayrona','La Feria de Cali','El Palacio de Bellas Artes','El Museo Larco','El Teatro Colón de Buenos Aires','El Casco Antiguo de Panamá','El Museo del Prado','El Caminito de Buenos Aires','La Casa de América','El Museo de la Memoria y los Derechos Humanos','Truman','La reconquista','El buen patrón','La vida era eso']
    for c in bank:
        if c not in used: return c,'s. XX',f'{c} é uma referência cultural para observar linguagem, memória e vida cotidiana.'
    return f'{w} — mirada A2 {e["n"]}','s. XX',d

def make_plan(e,idx,used):
    region,focus=focus_data(e); work,year,desc=unique_work(e,used); used.add(work)
    vals=[]
    for item in e.get('v',[]):
        x=clean_word(item)
        if x[0] and x[0] not in [v[0] for v in vals]: vals.append(x)
    fallback=[('situación','situação','si-tu-a-SIÓN'),('acuerdo','acordo','a-KUÊR-do'),('detalle','detalhe','de-TÁ-lle'),('propuesta','proposta','pro-pu-ÊS-ta'),('horario','horário','o-RÁ-rio'),('camino','caminho','ka-MÍ-no'),('decisión','decisão','de-si-SIÓN'),('ayuda','ajuda','a-IÚ-da')]
    for x in fallback:
        if len(vals)>=6: break
        if x[0] not in [v[0] for v in vals]: vals.append(list(x))
    vals=vals[:6]
    vb=[VERBS[(idx+i*7)%len(VERBS)] for i in range(4)]
    ex=[]
    for i in range(4): ex.extend(EXPRS[(idx*3+i)%len(EXPRS)])
    names=NAMES[idx%len(NAMES)]
    # Reuse up to two concrete lines from the old cultural scene when they are sound.
    oldlines=[]
    for fr in e.get('fr',[]):
        if fr.get('k')=='cultcena': oldlines=fr.get('lines',[]); break
    seeds=[]
    for line in oldlines:
        if len(line)>=2 and isinstance(line[1],str) and line[1] and 'Muy bien' not in line[1] and 'Propongo que ' not in line[1] and line[1] not in [x[1] for x in seeds]:
            seeds.append([names[len(seeds)%2],re.sub(r'\*\*','',line[1]),line[2] if len(line)>2 else line[1]])
        if len(seeds)>=2: break
    ptfocus=FOCUS_PT.get(focus,focus)
    w0,w0pt=vals[0][0],vals[0][1]; w1,w1pt=vals[1][0],vals[1][1]
    A,B=names
    s1=seeds[:]
    s1 += [[B,f'En {region.lower()}, podemos {vb[0]} el {w0}.',f'Em {region.lower()}, podemos {vb[0]}r {w0pt}.'],
           [A,f'¿Te parece si {vb[1]} la situación con calma?',f'Você acha bom {vb[1]} a situação com calma?'],
           [B,f'Sí; después podemos {vb[2]} una alternativa.',f'Sim; depois podemos {vb[2]} uma alternativa.'],
           [A,f'Quiero {vb[3]} el próximo paso antes de decidir.',f'Quero {vb[3]} o próximo passo antes de decidir.'],
           [B,f'{ex[0]}, revisamos todos los detalles.',f'{ex[1]}, revisamos todos os detalhes.'],
           [A,f'{ex[2]}, la propuesta queda más clara.',f'{ex[3]}, a proposta fica mais clara.']]
    s1=s1[:8]
    while len(s1)<8: s1.append([A if len(s1)%2==0 else B,'Entonces avanzamos con un plan concreto.','Então avançamos com um plano concreto.'])
    s2=[[A,f'{ex[4]}, podemos {vb[0]} el {w1}.',f'{ex[5]}, podemos {vb[0]}r {w1pt}.'],
        [B,f'Claro; prefiero {vb[1]} primero.',f'Claro; prefiro {vb[1]} primeiro.'],
        [A,f'{ex[6]}, preguntamos antes de actuar.',f'{ex[7]}, perguntamos antes de agir.'],
        [B,f'La referencia de {work} nos ayuda a mirar el contexto.',f'A referência de {work} nos ajuda a olhar o contexto.'],
        [A,f'Podemos {vb[2]} una solución que funcione para todos.',f'Podemos {vb[2]} uma solução que funcione para todos.'],
        [B,f'{ex[0]}, dejamos constancia del acuerdo.',f'{ex[1]}, registramos o acordo.'],
        [A,'Así la conversación queda clara y respetuosa.','Assim a conversa fica clara e respeitosa.'],
        [B,'Y terminamos con una próxima acción concreta.','E terminamos com uma próxima ação concreta.']]
    return {'n':e['n'],'t':e.get('t') or f'A2 · episódio {e["n"]}','focus':focus,'work':work,'year':year,'desc':desc or f'{work} é uma referência cultural para praticar {focus}.','v':vals,'vb':vb,'ex':list(ex),'sound':('ritmo e pronúncia',[vals[0][0],vals[1][0],vals[2][0]]),'names':names,'s1':s1,'s2':s2,'region':region,'ptfocus':ptfocus}

# Locate the two files and preserve all other records.
paths=list((ROOT/'data').glob('es-a2_*.json'))
records={}
for path in paths:
 data=json.loads(path.read_text(encoding='utf-8'))
 for e in data: records[e['n']]=(path,e)
used=set()
for n,(path,e) in records.items():
 if 138<=n<=400:
  for fr in e.get('fr',[]):
   if fr.get('k')=='cover' and fr.get('obra'): used.add(fr['obra'])
for n in sorted(n for n in records if 761<=n<=800):
 e=records[n][1]; p=make_plan(e,n-761,used); prev=records[400][1] if n==761 else records[n-1][1]
 new=make(e,p,prev)
 new['s']=f'{p["region"]} · {p["focus"]} · referencia: {p["work"]}'
 new['t']=p['t']; records[n]=(records[n][0],new)
# write only affected files
for path in sorted({records[n][0] for n in range(761,801)}):
 data=json.loads(path.read_text(encoding='utf-8'))
 repl={n:records[n][1] for n in records if records[n][0]==path and 761<=n<=800}
 for i,e in enumerate(data):
  if e['n'] in repl: data[i]=repl[e['n']]
 path.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
print('converted',len([n for n in records if 761<=n<=800]))
