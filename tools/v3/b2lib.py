"""Biblioteca comum dos módulos B2 (tools/v3/b2_*.py): work(), mission() e add(dict(...)) montam um episódio no modelo regular-pilot-v1."""
from v3.short import E, R

EPS = []  # cada módulo importa isto, chama add() e expõe EPS


def work(name, kind, year, text, line, place, emoji):
    return dict(name=name, kind=f'{kind} · {year}', year=str(year), text=text,
                line=line, pa=dict(t=place, e=[emoji, '✨', '🎬'], p='b', v=0))


def mission(icon, name, desc, prompt, model, checks, reply):
    return dict(ic=icon, name=name, desc=desc, prompt=prompt, ph='Escreva sua resposta aqui…', chips=[model], model=model,
                check=[x[0] for x in checks], kw=[x[1] for x in checks],
                tips=[[[x[2], x[3]]] for x in checks], ok=[x[4] for x in checks], reply=reply)


def add(s, out=None):
    # Cada dado abaixo é da situação desta aula. A mecânica usa as próprias palavras e frases do episódio.
    v=s['vocab']; h=s['hot']; a,b=s['names']
    gaps=[
      (s['gap'][0], s['gap'][1], s['gap'][2], 0, s['gap'][3]),
      (s['gap2'][0], s['gap2'][1], s['gap2'][2], 0, s['gap2'][3]),
      (s['gap3'][0], s['gap3'][1], s['gap3'][2], 0, s['gap3'][3]),
      (s['gap4'][0], s['gap4'][1], s['gap4'][2], 0, s['gap4'][3]),
    ]
    traps=[
      (s['trap'][0], s['trap'][1], 0, s['trap'][2]),
      (s['trap2'][0], s['trap2'][1], 0, s['trap2'][2]),
    ]
    quiz=[
      (s['q1'][0], s['q1'][1], [('🎯',s['q1'][2]),('🧩',s['q1'][3]),('🔎',s['q1'][4])],0,0,s['q1'][5]),
      (s['q2'][0], s['q2'][1], [('🎯',s['q2'][2]),('🧩',s['q2'][3]),('🔎',s['q2'][4])],0,2,s['q2'][5]),
      (s['q3'][0], s['q3'][1], [('🎯',s['q3'][2]),('🧩',s['q3'][3]),('🔎',s['q3'][4])],0,4,s['q3'][5]),
    ]
    rule=R(s['ids'][0], s['rule'][0], s['rule'][1], [s['rule'][2],s['rule'][3]], s['rule'][4], s['rule'][5], s['rule'][6], [s['rule'][7]])
    lab=s['lab']
    labd=dict(short=s['short'], title=s['labtitle'], say=s['labsay'], what=s['labwhat'],how=s['labhow'],pt=s['labpt'],
       ex=lab, pairs=s['pairs'], tip=s['labtip'], phrase=[h[0][3],h[0][4]],
       rounds=[(x[0],[x[0],x[4]],0,f'**{x[0]}** é a palavra da cena.') for x in lab])
    exps=[dict(ic=x[0],en=x[1],tag='Expressão',pt=x[2],use=x[3],ex=[x[4],x[5]]) for x in s['exps']]
    # A segunda cena encena as quatro expressões em contexto, com mais quatro falas novas.
    exp_scene=[]
    for i,x in enumerate(s['exps']): exp_scene.append([a if i%2==0 else b,x[4],x[5]])
    exp_scene += s['scene2extra']
    verbs=[dict(v=x[0],ic=x[1],pt=x[2],f=[['eu',x[3]],['ele/ela',x[4]]],ex=[x[5],x[6]],note=x[7]) for x in s['verbs']]
    molds=[]
    for label, startdata, ends in s['molds']:
        start, pt = startdata
        molds.append(dict(label=label,slots=[dict(cat='começo',opts=[[start,pt]]),dict(cat='fim',opts=[[x,y] for x,y in ends])],end=['.','.']))
    voc=[[x[1],x[2],x[3]] for x in v]
    balloons=[[x[0],x[1]] for x in v]
    E0=E(n=s['n'],title=s['title'],sub=s['sub'],pattern=s['pattern'],why=s['why'],names=s['names'],ids=s['ids'],rs=s['rs'],obra=s['obra'],hot=h,gaps=gaps,traps=traps,rule=rule,
       cover=s['cover'],vocab=s['vocab'],lines=s['lines'],quiz=quiz,dictate=[[x[3],x[4]] for x in h[:4]],teaser=s['teaser'],exps=[(x['ic'],x['en'],x['tag'],x['pt'],x['use'],x['ex'][0],x['ex'][1]) for x in exps],exp_scene=exp_scene,
       lab=labd,verbs=('Verbos em ação',s['verbtip'],s['verbs']),mold=[(m['label'],[(z['cat'],z['opts']) for z in m['slots']],'.') for m in molds],speak=s['speak'],produce=s['produce'],mission2=s['mission2'],scenes=s['scenes'],sc=s['rs'])
    (EPS if out is None else out).append(E0)

