"""Aulas de revisão espaçada e de avaliação: reciclam o vocabulário, as lacunas e os verbos das aulas da unidade."""
import json,os
from card import *
def unit_lessons(unit,before):
    out=[]
    for fn in sorted(os.listdir(OUT)):
        if fn=='index.json' or not fn.endswith('.json'):continue
        d=json.load(open(OUT+'/'+fn))
        if d['unit']==unit and PLAN[d['id']]['g']<PLAN[before]['g'] and PLAN[d['id']]['kind']=='core':out.append(d)
    return out
def collect(ls):
    voc=[];gaps=[];verbs=[];focus=[];prons=[];exprs=[]
    for d in ls:
        focus.append(d['focus'])
        for fr in d['frames']:
            for b in fr['blocks']:
                if b['type']=='vocab' and fr['tag']=='Vocabulário':voc+=[(v['w'],v['pt']) for v in b['items']]
                if b['type']=='gap' and fr['tag']=='Prática':gaps+=[dict(s=g['s'],a=g['a'],why=g.get('why',''),say=g.get('say')) for g in b['items']][:1]
                if b['type']=='verbs':verbs+=[(v['v'],v['pt']) for v in b['items']]
                if b['type']=='box' and b['kind']=='culture' and fr['tag']=='Vocabulário':exprs+=[x for x in b['body']]
        prons.append(d['targets']['pron'])
    return voc,gaps,verbs,focus,list(dict.fromkeys(prons)),exprs
def RV(id,title,*,goal,read,tf,mc,recap,dlg,speak_,wr,teach,exam_extra=()):
    P=PLAN[id];ls=unit_lessons(P['unit'],id);assess=P['kind']=='assess'
    voc,gaps,verbs,focus,prons,exprs=collect(ls);seed=P['g']
    vocab_=[dict(w=w,pt=pt) for w,pt in voc]
    sample=voc[::max(1,len(voc)//18)][:18]
    mm=[]
    seen=set()
    for w,pt in voc:
        if pt not in seen and len(mm)<6:seen.add(pt);mm.append((w,pt))
    mm=mm[::-1] if seed%2 else mm
    gp=[(g['s'],g['a'],g['why'],g.get('say')) for g in gaps[:6]]
    vb=list(dict.fromkeys(verbs))
    f1=f('Abertura','Lesson %d · %s'%(P['n'],title),
      box('look','Nesta '+('avaliação' if assess else 'revisão'),['**Aulas da unidade:** '+str(len(ls))+' aulas anteriores.']+['**%s**'%x for x in focus[:8]]+['**%d palavras** da unidade voltam em contextos novos.'%len(voc)]),
      p('**Objetivo de comunicação (%s):** %s'%(CEFR[P['level']],goal)),
      box('exam','Ponte para as provas',['A **revisão espaçada** é a técnica mais eficiente para guardar vocabulário: rever aos **1, 3 e 7 dias**.' if not assess else 'Uma **avaliação** simula a pressão de tempo das provas: faça sem consultar as aulas anteriores.','Faça este quadro **sem olhar a tradução** primeiro.']))
    f2=f('Aquecimento','Recall · What do you remember?',p('Leia as palavras e **cubra a tradução** na sua cabeça. Diga o sentido em português. Toque em 🔊 para conferir a pronúncia.'),words(*[(w,pt) for w,pt in sample]))
    f3=f('Leitura',read[0],read[1])
    f4=f('Compreensão','Did you understand?',tfng(tf),mcq(mc,'Vocabulary in context'))
    f5=f('Gramática','Grammar recap',*recap)
    f6=f('Prática','Practice · Mixed review',gap(gp,'Complete the sentences (from the unit)'),match(mm,'Match the word to its meaning'))
    rids=sorted([k for k,x in PLAN.items() if x['kind'] in('review','assess')],key=lambda k:PLAN[k]['g'])
    from pool import EXPRPOOL
    nv=fresh(4,id);ni=rids.index(id)*2;nx=[EXPRPOOL[(ni+j)%len(EXPRPOOL)] for j in range(2)]
    f7=f('Vocabulário','Unit word bank',words(*[(w,pt) for w,pt in voc]),dict(type='vocab',items=nv),box('culture','Novas expressões da revisão',['**%s** — %s'%e for e in nx]),box('tip','Estratégia','Escolha **5 palavras** que ainda travam. Escreva uma frase **sua** com cada uma e diga em voz alta.'))
    f8=f('Verbos','Verbs of the unit',table(['Verbo','Significado'],[['**%s**'%v,pt] for v,pt in vb] or [['be','ser, estar']],'Verbos vistos nesta unidade'),box('look','Revisão','Diga uma frase com cada verbo. Atenção a **he / she / it**: o verbo muda (**has, does, goes**).'))
    f9=f('Escuta e diálogo',dlg[0],dialog(dlg[0],dlg[1]),dict(type='pron',title='Pronúncia da unidade',items=[dict(label=x,note='Revise com o áudio das aulas anteriores.',words=[]) for x in prons[:5]]))
    f10=f('Fala','Speaking',speak(speak_))
    f11=f('Escrita','Writing',write(wr[0],wr[1],wr[2],wr[3] if len(wr)>3 else ''))
    am=auto_mcq([dict(w=w,pt=pt) for w,pt in sample[:5]],seed,5)
    if assess:
        last=f('Revisão e exame','Assessment · Score and next steps',table(['Parte','O que avaliar','Pontos'],[['Leitura','Quadros 3–4: ideias principais e vocabulário','/ 10'],['Escuta','Quadro 9: entender o diálogo e repetir','/ 10'],['Fala','Quadro 10: frases completas sem pausas longas','/ 10'],['Escrita','Quadro 11: frases corretas com a lista de verificação','/ 10']],'Autoavaliação (40 pontos)'),box('look','Critério de conclusão','**28 a 40 pontos:** siga para a próxima unidade. **20 a 27:** repita as aulas em que errou mais. **Menos de 20:** volte à Unidade e refaça os exercícios dos quadros 5 e 6.'),mcq(am,'Final check'),box('exam','Estratégia para as provas',['Controle o tempo: 1 minuto por pergunta de múltipla escolha.']+list(exam_extra)),box('teach','Nota para o futuro professor',teach))
    else:
        last=f('Revisão e exame','Review · Spaced practice · Teacher’s note',mcq(am,'Check yourself'),box('exam','Plano de revisão espaçada',['**Hoje:** refaça os quadros 6 e 7.','**Em 3 dias:** diga as frases do quadro 10 sem olhar.','**Em 7 dias:** escreva de memória o texto do quadro 11.']+list(exam_extra)),box('teach','Nota para o futuro professor',teach))
    targets=dict(grammar=P['focus'],pron='',verbs=[],pv=[],expr=[],words=[w for w,_ in voc],field=P['field'].split(' (')[0],genre='Revisão',skill=P['skill'],words_min=1)
    return lesson(id,title,CEFR[P['level']],P['level'],P['unit'],P['focus'],targets,[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,last])
