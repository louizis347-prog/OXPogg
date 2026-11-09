#!/usr/bin/env python3
"""Gera a relação de imagens do livro (docs/IMAGENS-LIVRO.md e docs/imagens-livro.csv) a partir das aulas prontas."""
import json,glob,os,re,csv,collections
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','..'))
D=R+'/professor/data/livro'
PLAN={x['id']:x for x in json.load(open(D+'/curriculo.json'))['lessons']}
def slug(w):return re.sub(r'[^a-z0-9]+','-',w.lower().replace('’','').replace("'",'')).strip('-')
rows=[];lessons=[];themes=collections.OrderedDict()
for f in sorted(glob.glob(D+'/lessons/*.json')):
    if f.endswith('index.json'):continue
    d=json.load(open(f));P=PLAN[d['id']]
    fr3=d['frames'][2];b=fr3['blocks'][0]
    rt=b.get('title') or b.get('headline') or b.get('name') or fr3['title']
    if rt.startswith('Reading'):rt=fr3['title']
    kind=P['kind']
    field=P['field'].split(' (')[0]
    words=[]
    for fr in d['frames']:
        if fr['tag']!='Vocabulário':continue
        for x in fr['blocks']:
            if x['type']=='vocab':
                for v in x['items']:words.append(v)
    genre=P.get('genre') or 'Revisão'
    hero='Foto de abertura: cena que represente "%s" (%s)%s.'%(rt,genre.lower() if genre else '', ' — tema: '+field.lower())
    lessons.append((d['id'],d['title'],d['cefr'],field,rt,genre,hero,words))
    themes.setdefault((d['cefr'],field),[]).append(d['id'])
    for v in words:
        rows.append([d['id'],d['cefr'],field,d['title'],v['w'],v['pt'],v['ex'],'palavras/%s.jpg'%slug(v['w'])])
os.makedirs(R+'/docs',exist_ok=True)
with open(R+'/docs/imagens-livro.csv','w',newline='',encoding='utf-8-sig') as fh:
    w=csv.writer(fh,delimiter=';');w.writerow(['aula','nivel','tema','titulo_da_aula','palavra','traducao','frase_exemplo (ajuda a escolher a foto)','arquivo_da_imagem'])
    w.writerows(rows)
L=['# Relação de imagens do livro (aulas 1 a %d)\n'%len(lessons),
'Use esta relação para escolher e enviar fotos reais. O livro mostra cada foto **automaticamente** assim que o arquivo existir; pode enviar aos poucos.\n',
'## Como nomear e preparar\n',
'| Onde aparece | Nome do arquivo | Formato |\n|---|---|---|',
'| Abertura de cada aula | `aulas/A1-L001.jpg` | horizontal 16:9, 1600×900, até 300 KB |',
'| Cartão de cada palavra | `palavras/<palavra>.jpg` | 4:3, 800×600, até 80 KB |\n',
'Regras do nome da palavra: minúsculas, sem apóstrofo, espaços viram hífen (`traffic light` → `traffic-light.jpg`; `grandma’s kitchen` → `grandmas-kitchen.jpg`). A planilha `imagens-livro.csv` traz o nome exato de cada arquivo, a tradução e a frase de exemplo.\n',
'## Estilo sugerido (parecido com apps de idiomas, porém mais autêntico)\n',
'- Fotos reais de pessoas e lugares do dia a dia, luz natural, sem banco de imagens genérico demais (evitar sorriso posado com fundo branco).',
'- Um único assunto por foto, bem enquadrado, para funcionar pequena no celular.',
'- Para verbos e adjetivos, prefira uma pessoa fazendo a ação ou um objeto que mostre a ideia (ex.: *tired* = pessoa cansada; *heavy* = mala pesada).',
'- Para palavras abstratas (*honesty*, *progress*), use cena simbólica ou deixe sem foto: o cartão continua funcionando sem imagem.',
'- Mostre diversidade de lugares e pessoas (Brasil, EUA, Canadá), coerente com o objetivo TOEFL/IELTS/colleges.\n',
'## Resumo por tema\n','| Nível | Tema | Aulas |\n|---|---|---|']
for (cefr,field),ids in themes.items():
    L.append('| %s | %s | %s a %s (%d aulas) |'%(cefr,field,ids[0],ids[-1],len(ids)))
L.append('\n## Aula por aula\n')
cur=None
for id,title,cefr,field,rt,genre,hero,words in lessons:
    if cefr!=cur:L.append('\n### Nível %s\n'%cefr);cur=cefr
    L.append('**%s · %s** — %s · texto: *%s*'%(id,title,field,rt))
    L.append('- Abertura (`aulas/%s.jpg`): %s'%(id,hero))
    if words:L.append('- Palavras (%d): '%len(words)+'; '.join('%s (%s)'%(v['w'],v['pt']) for v in words))
    L.append('')
open(R+'/docs/IMAGENS-LIVRO.md','w',encoding='utf-8').write('\n'.join(L))
print(len(lessons),'aulas',len(rows),'palavras')
