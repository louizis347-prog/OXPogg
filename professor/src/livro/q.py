"""Atalho de autoria: gera pron/exam/teach padrão e aceita vocabulário/verbos em formato compacto."""
from card import *
from review import RV
PN={'I am × I’m':('Na fala natural, I am vira I’m /aɪm/; you are vira you’re.',['I’m','you’re','she’s','we’re']),
'do you (fala rápida)':('Na fala rápida, do you soa /dʒu/ ou /dəjə/.',['Do you like it?','What do you do?','Where do you live?']),
'sílaba tônica em palavras comuns':('Em muitas palavras de duas sílabas a primeira é a forte: TAble, WAter, DOCtor.',['table','water','doctor','window']),
'ship/sheep':('/ɪ/ curto (ship) × /i/ longo (sheep).',['ship','sheep','sit','seat','live','leave']),
'bed/bad':('/ɛ/ (bed) × /æ/ (bad): abra mais a boca no /æ/.',['bed','bad','men','man','pen','pan']),
'think/this':('/θ/ sem voz (think) × /ð/ com voz (this): língua entre os dentes.',['think','this','three','that','thank','they']),
'/h/ de house':('O /h/ é um sopro de ar: house, hat, hear.',['house','hat','hear','help','home','hello']),
'r americano':('O r americano: língua curvada para trás, sem tocar o céu da boca.',['red','right','run','read','road','rice']),
'Terminações do passado':('-ed soa /t/ (worked), /d/ (played) ou /ɪd/ (wanted).',['worked','played','wanted','needed','asked','visited']),
'Plural e 3ª pessoa /s/':('O -s final soa /s/ (works), /z/ (goes) ou /ɪz/ (watches).',['works','goes','watches','buys','washes','plays']),
'Schwa /ə/':('Vogais fracas viram /ə/: about, banana, today, the.',['about','banana','today','family','another']),
'Entonação de perguntas':('Perguntas sim/não sobem; Wh- descem.',['Did you go? ↗','Where did you go? ↘','Is it open? ↗']),
'gonna e wanna (reconhecimento)':('Na fala: going to → gonna, want to → wanna. Reconheça; na escrita use a forma completa.',['I’m gonna go','I wanna eat','What are you gonna do?']),
'Word stress':('Palavras de 2+ sílabas têm uma sílaba forte: eDUcaTION, comPUter, PHOtograph, phoTOgraphy.',['education','photograph','photography','develop','different']),
'Sentence stress':('Na frase, acentue palavras de conteúdo (substantivos, verbos, adjetivos) e reduza as funcionais: I WANT to LEARN ENglish.',['I want to learn English.','She has studied for years.','Can you help me?']),
'Entonação':('Perguntas de sim/não sobem; Wh- descem; listas sobem e descem no fim; dúvida sobe.',['Have you ever studied abroad? ↗','Where did you study? ↘','books, notes, and pens ↘']),
'Contrações e fala conectada (compreensão)':('Reconheça: I’ve → /aɪv/, she’s → /ʃiz/, wouldn’t’ve, whaddaya (what do you), gonna, wanna.',['I’ve been there.','She’s been studying.','What do you want?','I’d’ve gone.']),
'Ligação entre palavras':('Consoante final liga à vogal seguinte: pick it up → pi-ki-tup.',['pick it up','turn it off','an apple','check in'])}
def _s(v):
    if v.endswith(('s','sh','ch','x','o')):return v+'es'
    if v.endswith('y') and v[-2] not in 'aeiou':return v[:-1]+'ies'
    return v+'s'
def VV(rows):
    out=[]
    for r in rows:
        p=r.split(';')
        if len(p)==4:p=[p[0],'word']+p[1:]
        out.append(V(*p))
    return out
def VBS(rows):
    return [VB(v,pt,[['I / you / we / they '+v,a],['he / she / it '+_s(v),b]],note=(n[0] if n else None)) for v,pt,a,b,*n in rows]
def Q(id,title,goal,read,tf,mc,gram,gaps,voc,dlg,sp,wr,verbs=None,pv=None,expr=None,warm=None,rev=None,exam=None,teach=None,pron=None):
    P=PLAN[id];lab=P['pron'];pn=pron or PN.get(lab,('Pratique em voz alta.',[]))
    sk=P['skill']
    ex=exam or ['Treine esta habilidade com o formato de tarefas curtas das provas (TOEFL/IELTS).','Leia o enunciado primeiro e procure as palavras-chave.']
    te=teach or ['Use exemplos reais da vida dos alunos e peça frases próprias.','Corrija o erro mais frequente da aula em grupo, sem expor o aluno.','Retome o conteúdo na aula seguinte com um exercício curto.']
    try:
        return L(id,title,goal=goal,read=read,tf=tf,mc=mc,gram=gram,gaps=gaps,vocab=VV(voc),dlg=dlg,pron=pn,speak_=sp,wr=wr,rev=rev or [],exam=ex,teach=te,verbs=VBS(verbs) if verbs else None,pv=[dict(w=a,pt=b,ex=c,expt=d) for a,b,c,d in pv] if pv else None,expr=expr,warm=warm)
    except SystemExit as e:
        if os.environ.get('DRY'):print(e);return None
        raise
def G(title,head,rows,tip=None,warn=None):
    bl=[table(head,rows,title)]
    if tip:bl.append(box('look','Regra',tip))
    if warn:bl.append(box('warn','Cuidado',warn))
    return (title,bl)
