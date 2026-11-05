#!/usr/bin/env python3
"""Curso de Formação de Professores (painel do professor).

Reorganiza as 200 aulas Quest A1 (professor/data/v4, 47 quadros e 60 min cada) em 600 lições enxutas de 10 quadros:
  A · Situação e palavras      B · Conversar e estruturar      C · Ler e escrever
Nada do conteúdo é descartado: vocabulário, verbos, expressões, padrões, diálogo, leitura, sons, interação e escrita
seguem para a lição certa. Cada lição ganha um quadro de DIDÁTICA (como ensinar aquele conteúdo) e um quadro de tarefas
no formato do TOEFL iBT, montado com o próprio material da aula. Saída: professor/data/formacao/."""
import json,glob,re,os,random,collections
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'));SRC=R+'/data/v4';OUT=R+'/data/formacao'
os.makedirs(OUT+'/a1',exist_ok=True)

def pg(L,kind,stage=None):return [p for p in L['pages'] if p['kind']==kind and (stage is None or p.get('stage')==stage)]
def strip(s):return re.sub(r'\*\*','',str(s))
def rnd(L,salt):return random.Random(L['n']*131+sum(map(ord,salt)))
def words_of(s):return re.findall(r"[A-Za-z’']+",s)

# ---------- erros típicos de brasileiros (ligados ao conteúdo da aula) ----------
ERR=[(r"\b(he|she|it)\b[^.?!]{0,30}\b\w+s\b|\b\w+(ies|es)\b","Esquecer o -s da terceira pessoa: “He work here.” Peça para o aluno marcar o -s com a mão quando ele aparece."),
 (r"\bhow old\b|\bI am \d+|\byears old\b","Dizer “I have 20 years”: em inglês a idade usa o verbo be (“I’m twenty”)."),
 (r"\bthere (is|are)\b","Usar “Has a bank near here?” no lugar de “Is there a bank near here?”: há existe em inglês com there is/are."),
 (r"\b(did|was|were|\w+ed)\b","Pronúncia do -ed: /t/, /d/ ou /ɪd/ (walked, played, wanted). Português costuma pronunciar um “e” a mais."),
 (r"\bcan\b|\bcould\b","Colocar to depois do modal: “Can you to help me?”. Depois de can, o verbo vem sem to."),
 (r"\b(do|does|did)\b","Omitir o auxiliar nas perguntas: “You like coffee?” funciona na fala, mas a forma “Do you like coffee?” precisa ser dominada."),
 (r"\b(in|on|at)\b","Preposições de tempo e lugar: at (ponto), on (superfície/dia), in (espaço/período). Português usa “em” para tudo."),
 (r"\b(a|an)\b","Omitir o artigo com profissões e objetos contáveis: “I am teacher”, “I have car”."),
 (r"\b\w+ing\b|\bam\b|\bare\b","Esquecer o verbo be no presente contínuo: “I studying now” em vez de “I am studying now”."),
 (r"\b(much|many|some|any)\b","Confundir much/many e some/any: contável × incontável; any em perguntas e negativas."),
 (r"\bwant\b|\bneed\b","“I want that you come”: depois de want use objeto + to (“I want you to come”)."),
 (r"\b(th)\w*","O som de th (/θ/ e /ð/): o aluno troca por t, d ou s. Treine com a língua entre os dentes."),
 (r"\b(ship|sheep|live|leave|full|fool)\b","Vogal curta × longa (ship × sheep): o português não distingue; use pares mínimos."),
 (r"\b(the)\b","Usar the antes de generalizações: “The life is hard” em vez de “Life is hard”.")]
ERR_GEN="Traduzir palavra por palavra: avise que expressões fixas não se traduzem literalmente e peça o equivalente natural em português."
def erros(texts,n=3):
    t=' '.join(texts).lower();out=[]
    for rx,msg in ERR:
        if re.search(rx,t) and msg not in out:out.append(msg)
        if len(out)>=n:break
    if not out:out=[ERR_GEN]
    return out

# ---------- didática: sequências alternadas (variam por aula) ----------
SEQ={'A':[
 [('Ativar (2 min)','Mostre a cena do dia a dia (foto, objeto, gesto) e pergunte em português: “Quando você vive isso?”. Só depois mostre as palavras: {w3}.'),('Apresentar (3 min)','Diga cada palavra duas vezes, marque a sílaba forte e peça repetição em coro e depois individual.'),('Praticar (4 min)','“Que palavra falta?”: leia frases do quadro de cartões deixando um espaço, e os alunos completam.'),('Produzir (3 min)','Cada aluno diz uma frase verdadeira sobre a própria vida com {w1} ou {w2}.')],
 [('Pré-ensinar (2 min)','Escreva {w3} no quadro sem tradução e peça palpites pelo contexto da cena.'),('Checar sentido (3 min)','Use perguntas de checagem: “{w1}: isso é uma coisa, uma ação ou um lugar? Dê um exemplo.”'),('Fixar (4 min)','Jogo da memória em duplas: palavra + frase; quem acerta guarda o cartão.'),('Usar (3 min)','Mini-diálogo de 30 segundos em que a pessoa precisa usar {w1} e {w2}.')],
 [('Despertar (2 min)','Mímica: o professor encena {w1}; a turma adivinha a palavra em inglês ou em português.'),('Modelar (3 min)','Fale a frase-modelo do cartão com ritmo natural; os alunos batem a sílaba forte na mesa.'),('Aplicar (4 min)','Corrente de frases: cada aluno repete a anterior e acrescenta uma palavra do quadro.'),('Fechar (3 min)','Bilhete de saída: escrever uma frase com {w2} em um papel e entregar.')]],
 'B':[
 [('Contextualizar (2 min)','Apresente a missão e peça que o aluno diga em português o que espera ouvir nessa conversa.'),('Escutar (3 min)','Duas escutas: primeiro só o áudio (ideia geral), depois com o texto (detalhes).'),('Descobrir a regra (4 min)','Escreva duas frases do diálogo e pergunte: “O que mudou?”. Deixe o aluno formular a regra antes de você confirmar.'),('Encenar (4 min)','Em duplas, repetir o diálogo trocando uma informação (a parte entre chaves) a cada rodada.')],
 [('Prever (2 min)','Mostre a primeira fala do diálogo e peça a resposta provável.'),('Escutar com tarefa (3 min)','Dê uma tarefa antes da escuta: “Quantas perguntas a pessoa faz?”.'),('Guiar a descoberta (4 min)','Peça para sublinhar o padrão que aparece 3 vezes e testar uma frase nova com ele.'),('Jogar o papel (4 min)','Role-play com mudança de situação: o professor sorteia um imprevisto (a loja fechou, o preço mudou).')],
 [('Aquecer (2 min)','Pergunte aos alunos como eles reagiriam à situação em português, depois em inglês.'),('Modelar (3 min)','Dramatize o diálogo com um aluno voluntário e narre o que está fazendo.'),('Treinar o padrão (4 min)','Drill em cadeia com o molde de frase: o professor dá a deixa e o aluno responde.'),('Liberar (4 min)','Conversa livre de 1 minuto em que cada aluno cumpre a missão com as próprias palavras.')]],
 'C':[
 [('Antes de ler (2 min)','Mostre o título e a ilustração mental da cena: “Sobre o que será?”. Pré-ensine só 2 palavras do glossário.'),('Ler pela ideia (3 min)','Primeira leitura silenciosa só para a pergunta geral do quadro.'),('Ler pelo detalhe (4 min)','Segunda leitura com as perguntas de compreensão; peça que o aluno mostre no texto onde achou a resposta.'),('Escrever (4 min)','Com o modelo e a lista de verificação, o aluno escreve 2 ou 3 frases e troca com um colega para corrigir.')],
 [('Ativar o conhecimento (2 min)','Pergunte o que o aluno já sabe sobre o assunto do texto.'),('Skimming (3 min)','Leitura rápida de 30 segundos para achar o local, a pessoa e o problema.'),('Scanning (4 min)','Procurar no texto números, nomes e horários pedidos pelas perguntas.'),('Produção guiada (4 min)','Reescrever o final do texto com uma informação diferente.')],
 [('Pré-leitura (2 min)','Previsão: com 3 palavras do glossário, os alunos adivinham a história.'),('Leitura em duplas (3 min)','Uma pessoa lê um parágrafo e a outra resume em uma frase.'),('Verificar (4 min)','Perguntas de verdadeiro ou falso com correção: o aluno corrige a frase falsa.'),('Escrita curta (4 min)','Bilhete ou mensagem de 20 a 30 palavras usando a estrutura do dia.')]]}
ADAPT={'A':'Turma mais rápida: peça definições em inglês simples. Turma que precisa de apoio: use imagens e a tradução antes da repetição.','B':'Turma mais rápida: acrescente um imprevisto por rodada. Turma que precisa de apoio: deixe o diálogo visível e peça só a troca de uma palavra.','C':'Turma mais rápida: peça um parágrafo de 4 frases. Turma que precisa de apoio: dê o início das frases e leia o texto em coro antes.'}
TOEFL_TIP={'A':('Vocabulário em contexto','No TOEFL, a palavra quase nunca vem isolada: o aluno precisa escolher o sentido pela frase. Treine sempre com a frase inteira.'),
 'B':('Falar e ouvir','O TOEFL avalia falar com respostas curtas, claras e organizadas. “Listen and Repeat” treina ritmo e entonação; “Take an Interview” treina respostas de 30 a 45 segundos.'),
 'C':('Ler e escrever','O TOEFL cobra leitura rápida (palavras incompletas, avisos do dia a dia, textos acadêmicos) e escrita com precisão (montar frases, e-mail, discussão).')}
CEFR_DOC={'A1':'Nível A1 (QECR): entende e usa expressões cotidianas muito simples para necessidades imediatas. Meta de desempenho, não certificação.'}

def mut(word,rng):
    k=max(1,len(word)//2);return word[:k]+'_'*(len(word)-k)

def build_lesson(L,part):
    n=L['n'];lv=L.get('level','A1');rn=rnd(L,part)
    V=[]
    for p in pg(L,'vocab'):V+=p['words']
    vocab=[{'w':w[0],'pt':w[1],'ex':[w[2],w[3]] if len(w)>3 else [w[2]],'ic':w[5] if len(w)>5 else ''} for w in V][:6]
    verbs=[]
    for p in pg(L,'verbs'):verbs+=p['verbs']
    exprs=[]
    for p in pg(L,'exprs'):exprs+=p['items']
    pats=pg(L,'pattern');soun=pg(L,'soundlab');rd=pg(L,'reading')
    dl=[(l['who'],l['en'],l['pt']) if isinstance(l,dict) else (l[0],l[1],l[2]) for l in (L.get('dialog') or {}).get('lines',[])]
    cover=(pg(L,'cover') or [{}])[0]
    w=[x['w'] for x in vocab]+['the words']*3
    w1,w2,w3=w[0],w[1],', '.join(w[:3])
    title=L['title'];sit=L['pt']
    base={'n':n,'unit':L['unit'],'level':lv,'situation':title}
    FR=[]
    def add(k,tag,t,**kw):FR.append(dict(k=k,tag=tag,title=t,**kw))
    # ----- A · Situação e palavras -----
    if part=='A':
        add('can','SITUAÇÃO','Missão e objetivos',goal=cover.get('goal',''),can=cover.get('can',[]),note=cover.get('note',''),cefr=CEFR_DOC.get(lv,''),situation=title)
        facts=[];cmp_=None
        for p in pg(L,'facts'):facts+=p['facts']
        c=pg(L,'compare');cmp_=c[0]['compare'] if c else None
        add('context','CONTEXTO','A situação no mundo real',facts=facts[:3],compare=cmp_,work=(pg(L,'work') or [{}])[0].get('work'))
        add('cards','VOCABULÁRIO','Palavras da situação',items=[{'front':x['w'],'back':x['pt'],'ex':x['ex'],'ic':x['ic']} for x in vocab],say=True)
        add('table','VERBOS','Verbos em ação',verbs=[{'v':v['v'],'ic':v.get('ic',''),'pt':v['pt'],'note':strip(v.get('note','')),'forms':v.get('forms',[])} for v in verbs[:4]])
        add('cards','EXPRESSÕES','Expressões comuns',items=[{'front':e['en'],'back':e['pt'],'ex':[e.get('ex','')],'note':e.get('exp','')} for e in exprs[:4]],say=True)
        qs=[]
        for p in pg(L,'verbplay'):
            for it in p['items'][:3]:qs.append({'q':it['en'],'sub':it.get('scene',''),'opts':it['opts'],'ans':it['ans'],'why':it.get('why','')})
        for p in pg(L,'exprplay'):
            for it in p['items'][:3]:qs.append({'q':it['cue'],'opts':it['opts'],'ans':it['ans'],'why':it.get('why','')})
        add('quiz','PRÁTICA','Verbos e expressões em uso',items=qs[:6])
        sl=[x for x in soun if x.get('part')==1];pr=[x for x in soun if x.get('part')==2]
        add('sound','SONS','Laboratório de sons',focus=(sl[0].get('focus') if sl else ''),what=(sl[0].get('what') if sl else ''),how=(sl[0].get('how') if sl else ''),tip=(sl[0].get('tip') if sl else ''),words=(sl[0].get('words') if sl else []),pairs=(pr[0].get('pairs') if pr else []))
        txt=[e['ex'][0] for e in [{'ex':x['ex']} for x in vocab]]+[v.get('note','') for v in verbs]
        steps=[{'t':a,'d':b.format(w1=w1,w2=w2,w3=w3)} for a,b in rn.choice(SEQ['A'])]
        add('teach','DIDÁTICA','Como ensinar vocabulário, verbos e expressões',goal='Ao final, o aluno reconhece e usa %s em uma frase sobre “%s”.'%(w3,title),steps=steps,errors=erros(txt),adapt=ADAPT['A'],ccq=['“%s”: isso é uma coisa, uma ação ou um lugar? Dê um exemplo.'%x['w'] for x in vocab[:3]])
        items=[]
        for x in vocab:
            ex=x['ex'][0]
            if re.search(r'\b%s\b'%re.escape(x['w']),ex,re.I):
                others=[o['w'] for o in vocab if o['w']!=x['w']];rn.shuffle(others);opts=[x['w']]+others[:2];rn.shuffle(opts)
                items.append({'q':re.sub(r'\b%s\b'%re.escape(x['w']),'_____',ex,flags=re.I),'opts':opts,'ans':opts.index(x['w']),'why':'A palavra “%s” (%s) completa o sentido da frase.'%(x['w'],x['pt'])})
        add('toefl','TOEFL','Vocabulário em contexto',tip=TOEFL_TIP['A'],tasks=[{'type':'cloze','name':'Vocabulary in context','items':items[:4]}])
        add('wrap','FECHAMENTO','Retomar e ensinar',items=[{'cue':x['pt'],'target':x['w']} for x in vocab[:4]],micro='Ensine em 60 segundos: explique “%s” a um colega sem usar a tradução.'%w1,homework='')
    # ----- B · Conversar e estruturar -----
    elif part=='B':
        wk=(pg(L,'work') or [{}])[0].get('work')
        add('can','SITUAÇÃO','Missão da conversa',goal=cover.get('goal',''),can=cover.get('can',[]),note=cover.get('note',''),cefr=CEFR_DOC.get(lv,''),situation=title,hook=wk)
        key=[x['w'] for x in vocab][:4];dic=[]
        for i,l in enumerate(dl):
            if l[0]!='You' and len(dic)<3 and any(re.search(r'\b%s\b'%re.escape(k),l[1],re.I) for k in key):dic.append(i)
        add('listen','LISTENING','Ouça a conversa',lines=[{'who':l[0],'en':l[1],'pt':l[2]} for l in dl[:12]],dictation=[{'i':i,'en':dl[i][1],'gap':next((k for k in key if re.search(r'\b%s\b'%re.escape(k),dl[i][1],re.I)),'')} for i in dic if dl[i][1]][:3])
        ch=[]
        for p in pg(L,'choice'):
            t=p['turn'];ch.append({'npc':t['npc'],'pt':t.get('pt',''),'opts':t['opts']})
        add('respond','LISTENING','Escute e escolha a resposta',turns=ch[:5])
        sw=[]
        for p in pg(L,'dialog'):sw+=p.get('swaps',[])
        if sw:add('swaps','FALA','Varie a frase',swaps=sw[:6])
        else:add('cards','EXPRESSÕES','Expressões da conversa',items=[{'front':e['en'],'back':e['pt'],'ex':[e.get('ex','')],'note':e.get('exp','')} for e in exprs[:5]],say=True)
        add('pattern','PADRÕES','Moldes de frase',patterns=[{'title':p['title'],'frame':p['frame'],'slots':p['slots'],'model':p['model'],'note':strip(p.get('note',''))} for p in pats[:2]])
        add('grammar','GRAMÁTICA','Gramática em foco',points=[strip(p.get('note','')) for p in pats if p.get('note')],models=[p['model'] for p in pats],errors=erros([p['frame'] for p in pats]+[l[1] for l in dl]),contrast='')
        ro=(pg(L,'role') or [{}])[0]
        add('role','INTERAÇÃO','Missão ao vivo',prompts=ro.get('prompts',[]),change=ro.get('change',[]),solo=ro.get('solo',''),turns=ro.get('turns',[]))
        steps=[{'t':a,'d':b.format(w1=w1,w2=w2,w3=w3)} for a,b in rn.choice(SEQ['B'])]
        add('teach','DIDÁTICA','Como ensinar a conversa e o padrão',goal='Ao final, o aluno cumpre a missão “%s” e usa o molde “%s”.'%(title,(pats[0]['frame'] if pats else '')),steps=steps,errors=erros([p['frame'] for p in pats]+[l[1] for l in dl]),adapt=ADAPT['B'],ccq=['Quem fala primeiro nessa situação e por quê?','O que você diria se a resposta fosse “não”?'])
        you=[l for l in dl if l[0]=='You'];srt=sorted(dl,key=lambda l:len(l[1]))
        lr=[{'en':l[1],'pt':l[2]} for l in srt if len(l[1].split())>=3][:5]
        add('toefl','TOEFL','Falar no formato TOEFL',tip=TOEFL_TIP['B'],tasks=[{'type':'repeat','name':'Listen and Repeat','items':lr},{'type':'interview','name':'Take an Interview','prompts':[(c or '') for c in ro.get('change',[])][:3]}])
        add('wrap','FECHAMENTO','Retomar e ensinar',items=[{'cue':x['cue'],'target':x['target']} for p in pg(L,'exit') for x in p['items']][:4],micro='Ensine em 60 segundos: dê a regra de “%s” e um exemplo novo.'%(pats[0]['frame'] if pats else title),homework='')
    # ----- C · Ler e escrever -----
    else:
        add('can','SITUAÇÃO','Missão de leitura e escrita',goal='Ler uma história curta sobre “%s” e escrever a sua versão.'%title,can=[(pg(L,'writing') or [{}])[0].get('task','')],note='Leia primeiro pela ideia geral e só depois pelos detalhes.',cefr=CEFR_DOC.get(lv,''),situation=title)
        for i in range(3):
            if i<len(rd):
                p=rd[i];add('read','LEITURA',strip(p['title']),paragraphs=p['paragraphs'],glossary=p.get('glossary',[]),prompt=p.get('prompt',''),sentences=p.get('sentences',[]),part=i+1)
            else:
                gl=[g for p in rd for g in p.get('glossary',[])][:8]
                add('cards','VOCABULÁRIO','Vocabulário da leitura',items=[{'front':g['w'],'back':g['pt'],'ex':[]} for g in gl],say=True)
        qs=[]
        for p in pg(L,'quiz','read'):
            for it in p['items']:qs.append({'q':it['q'],'opts':it['opts'],'ans':it['ans'],'why':it.get('why','')})
        add('quiz','COMPREENSÃO','Você entendeu?',items=qs[:6])
        ar=[]
        for p in pg(L,'artifact'):
            a=p['artifact'];ar.append({'kind':a['kind'],'lines':a['lines'],'q':a['decode']['q'],'opts':a['decode']['opts'],'ans':a['decode']['ans'],'why':a['decode'].get('why','')})
        add('daily','LEITURA','Leitura do dia a dia',items=ar[:2])
        wr=(pg(L,'writing') or [{}])[0]
        add('write','ESCRITA','Escreva a sua versão',task=wr.get('task',''),model=wr.get('model',''),checks=wr.get('checks',[]),kw=wr.get('kw',[]))
        steps=[{'t':a,'d':b.format(w1=w1,w2=w2,w3=w3)} for a,b in rn.choice(SEQ['C'])]
        add('teach','DIDÁTICA','Como ensinar leitura e escrita',goal='Ao final, o aluno entende a ideia e os detalhes de um texto sobre “%s” e escreve 2 ou 3 frases suas.'%title,steps=steps,errors=erros([wr.get('model','')]+[' '.join(p.get('paragraphs',[])) for p in rd]),adapt=ADAPT['C'],ccq=['Onde no texto você encontrou a resposta?','Qual frase mostra o problema da história?'])
        cw=[];bs=[]
        sents=[s for p in rd for g in p.get('sentences',[]) for s in g]
        for s in sents:
            t=strip(s['en'])
            if 5<=len(t.split())<=9 and not any(c in t for c in '“”"') and len(bs)<3:
                ws=t.rstrip('.!?').split();sh=ws[:];rn.shuffle(sh)
                if sh==ws:sh=ws[::-1]
                bs.append({'words':sh,'answer':t,'pt':strip(s['pt'])})
        if rd:
            para=strip(' '.join(rd[0]['paragraphs'][:2]));toks=para.split();cnt=0;out=[];ans=[]
            for i,tk in enumerate(toks):
                m=re.match(r"^([A-Za-z]{5,})([.,!?]*)$",tk)
                if m and i%2==1 and cnt<6 and m.group(1)[0].islower():
                    o=mut(m.group(1),rn);out.append(o+m.group(2));ans.append(m.group(1));cnt+=1
                else:out.append(tk)
            cw=[{'text':' '.join(out),'answers':ans}]
        add('toefl','TOEFL','Ler e escrever no formato TOEFL',tip=TOEFL_TIP['C'],tasks=[{'type':'complete','name':'Complete the Words','items':cw},{'type':'build','name':'Build a Sentence','items':bs}])
        fi=(pg(L,'finish') or [{}])[0]
        add('wrap','FECHAMENTO','Fechamento e tarefa',items=[],micro='Ensine em 60 segundos: conte a história do texto com as suas palavras.',homework=fi.get('homework',''),badge=fi.get('badge'),next=fi.get('next',''))
    base['part']=part;base['frames']=FR
    return base

def main():
    idx=[];tot=0
    files=sorted(glob.glob(SRC+'/[0-9]*.json'))
    for f in files:
        L=json.load(open(f));n=L['n']
        for part,name in (('A','Situação e palavras'),('B','Conversar e estruturar'),('C','Ler e escrever')):
            les=build_lesson(L,part);assert len(les['frames'])==10,(n,part,len(les['frames']))
            les['id']='a1-%03d%s'%(n,part.lower());les['name']=name;les['pt']=L['pt'];les['title']=L['title']
            json.dump(les,open(OUT+'/a1/%03d%s.json'%(n,part.lower()),'w'),ensure_ascii=False,separators=(',',':'))
            idx.append({'id':les['id'],'n':n,'part':part,'name':name,'title':L['title'],'pt':L['pt'],'unit':L['unit'],'level':L.get('level','A1'),'minutes':20,'scene':L.get('scene')});tot+=1
    json.dump({'track':'a1','lessons':idx},open(OUT+'/index-a1.json','w'),ensure_ascii=False,separators=(',',':'))
    print('lições geradas:',tot)
if __name__=='__main__':main()
