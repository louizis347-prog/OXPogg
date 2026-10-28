import json, glob, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
TARGET=set(range(71081,71161))

def ptline(es, topic):
    # compact, predictable translation for the generated A1 scene
    replacements={
      'Hola, ¿puedes ayudarme con ': 'Olá, você pode me ajudar com ',
      'Claro. ¿Qué necesitas?':'Claro. O que você precisa?',
      'Necesito ': 'Preciso de ',
      ' y ': ' e ',
      'También busco ': 'Também procuro ',
      'Puedes encontrar ': 'Você pode encontrar ',
      ' aquí.':' aqui.',
      '¿Y dónde está ':'E onde fica ',
      'Está cerca de ':'Fica perto de ',
      'Gracias por tu ayuda.':'Obrigado pela sua ajuda.',
      'Voy a explicar ':'Vou explicar ',
      ' a mi amiga.':' para a minha amiga.',
      'Primero, muestro ':'Primeiro, mostro ',
      'Después, usamos ':'Depois, usamos ',
      '¿Lo puedes repetir, por favor?':'Você pode repetir, por favor?',
      'Sí, está aquí.':'Sim, está aqui.',
      'Ahora entiendo ':'Agora entendo ',
      'Entonces, elijo ':'Então, escolho ',
      'Perfecto, nos vemos mañana.':'Perfeito, até amanhã.',
    }
    out=es
    for a,b in replacements.items(): out=out.replace(a,b)
    return out

for path in glob.glob(str(ROOT/'data/es-a1_*.json')):
    data=json.loads(Path(path).read_text(encoding='utf-8')); dirty=False
    for e in data:
        if e.get('n') not in TARGET: continue
        s=e.get('s',''); ref=s.split('referencia:')[-1].strip() if 'referencia:' in s else (e.get('t') or 'Referencia cultural')
        prefix=s.split('referencia:')[0].strip(' ·') if 'referencia:' in s else s
        topic=prefix.split('·',1)[-1].strip() if '·' in prefix else (e.get('t') or 'una situación cotidiana')
        vals=[]
        for row in e.get('v',[])[:6]:
            if isinstance(row,list) and row: vals.append(str(row[0]))
        while len(vals)<6: vals.append(['situación','persona','lugar','momento','ayuda','paso'][len(vals)])
        w=vals[:6]
        scene1=[
          ['Lucía',f'Hola, ¿puedes ayudarme con {topic}?',ptline(f'Hola, ¿puedes ayudarme con {topic}?',topic)],
          ['Mateo','Claro. ¿Qué necesitas?','Claro. O que você precisa?'],
          ['Lucía',f'Necesito {w[0]} y {w[1]}.',ptline(f'Necesito {w[0]} y {w[1]}.',topic)],
          ['Mateo',f'También busco {w[2]}.',ptline(f'También busco {w[2]}.',topic)],
          ['Lucía',f'Puedes encontrar {w[3]} aquí.',ptline(f'Puedes encontrar {w[3]} aquí.',topic)],
          ['Mateo',f'¿Y dónde está {w[4]}?',ptline(f'¿Y dónde está {w[4]}?',topic)],
          ['Lucía',f'Está cerca de {w[5]}.',ptline(f'Está cerca de {w[5]}.',topic)],
          ['Mateo','Gracias por tu ayuda.','Obrigado pela sua ajuda.'],
        ]
        scene2=[
          ['Lucía',f'Voy a explicar {topic} a mi amiga.',ptline(f'Voy a explicar {topic} a mi amiga.',topic)],
          ['Mateo',f'Primero, muestro {w[0]}.',ptline(f'Primero, muestro {w[0]}.',topic)],
          ['Lucía',f'Después, usamos {w[1]} y {w[2]}.',ptline(f'Después, usamos {w[1]} y {w[2]}.',topic)],
          ['Mateo','¿Lo puedes repetir, por favor?','Você pode repetir, por favor?'],
          ['Lucía','Sí, está aquí.','Sim, está aqui.'],
          ['Mateo',f'Ahora entiendo {w[3]}.',ptline(f'Ahora entiendo {w[3]}.',topic)],
          ['Lucía',f'Entonces, elijo {w[4]}.',ptline(f'Entonces, elijo {w[4]}.',topic)],
          ['Mateo','Perfecto, nos vemos mañana.','Perfeito, até amanhã.'],
        ]
        fr=e['fr']
        # Main cultural work belongs to the current episode; review.work remains the prior episode.
        for f in fr:
            if f.get('k')=='cover':
                f['obra']=ref
                f['say']=f'Hoje você vai resolver: {topic}.'
                f['sub']=f'{topic}: em 10 minutos você resolve uma situação real.'
            elif f.get('k')=='pgscene':
                if not f.get('title') or f.get('title')=='Na conversa de verdade':
                    f['title']='Cena principal' if not any(x.get('k')=='pgscene' for x in fr[:fr.index(f)]) else 'Na conversa de verdade'
                if not any(x.get('lines')==scene1 for x in fr if x.get('k')=='pgscene'):
                    # first pgscene is the first one in the list
                    idx=[i for i,x in enumerate(fr) if x.get('k')=='pgscene'][0]
                    if fr.index(f)==idx: f['lines']=scene1
                    else: f['lines']=scene2
                f['speakers']={'Lucía':'polly','Mateo':'tom'}
            elif f.get('k')=='hotscene':
                f['hot']=[{'e':['🔤','💬','🧭','📍','✨'][i%5],'x':18+i*16,'y':25+(i%2)*18,'en':w[i],'pt':next((str(r[1]) for r in e.get('v',[]) if isinstance(r,list) and r and r[0]==w[i]),w[i]),'say':w[i],'sayPt':next((str(r[1]) for r in e.get('v',[]) if isinstance(r,list) and r and r[0]==w[i]),w[i])} for i in range(5)]
            elif f.get('k')=='pgspeak':
                f['items']=[[x[1],x[2]] for x in scene1[:5]]
            elif f.get('k')=='wrap':
                f['recap']=[[x[1],x[2]] for x in scene1[-4:]]
        e['a']={'k':'🎬 Obra cultural','w':ref,'y':'','d':f'{ref} é a referência cultural desta aula; a cena é autoral e serve de ponto de partida para {topic}.'}
        e['h']={'l':scene1[0][1],'src':ref,'tr':scene1[0][2]}
        e['p']=f'Hoje você aprende a lidar com {topic} em espanhol.'
        e['presentation']='regular-pilot-v1'; e['pilot']=1
        dirty=True
    if dirty:
        Path(path).write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
        print(path)
