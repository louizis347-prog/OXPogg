"""Roteiro do professor por tela (teach) e plano de 1h30 (plan.solo90/group90) para as aulas Quest.
Gerado a partir do conteúdo de cada aula; não altera nada além de p['teach'] e L['plan'][...90]."""
import re
PLAN90 = [('mission',5),('culture',10),('read',14),('talk',16),('pause',5),('lab',12),('arcade',8),('boss',12),('write',5),('wrap',3)]
def _s(x,n=140):
    x=re.sub(r'\*\*','',str(x or '')).strip(); return x if len(x)<=n else x[:n-1].rstrip()+'…'
def plan90(L):
    out={}
    for mode in ('solo','group'):
        base={s['id']:s for s in (L.get('plan') or {}).get(mode,[])}
        if not base: return {}
        seq=[]
        for sid,mi in PLAN90:
            if sid=='pause': seq.append(dict(id='pause',name='Pausa',ic='☕',c='#9aa3b5',min=5,desc='5 minutos: câmera e microfone desligados. O professor anota 3 erros reais ouvidos até aqui para a correção final.'))
            else:
                b=dict(base.get(sid,{'id':sid,'name':sid,'c':'#2f6fe0'})); b['min']=mi; seq.append(b)
        out[mode+'90']=seq
    return out
def _ans_idx(it):
    o=it.get('opts') or []; a=it.get('ans')
    return o[a] if isinstance(a,int) and 0<=a<len(o) else ''
def teach(p,L):
    k=p.get('kind'); sp=(L.get('dialog') or {}).get('speakers',{}); npc=next((v.get('name') for w,v in sp.items() if w!='You'),'o personagem')
    t=dict(); g=[];s=[];e90=[];ans=[];err=[]
    if k=='cover':
        t['goal']='Abrir a aula: objetivo e primeira hipótese.'
        g=['Leia o objetivo em voz alta: “'+_s(p.get('goal'),110)+'”.','Peça que cada aluno diga, em português, quando precisaria disso na vida real.']
        s=['Leia o objetivo e pergunte: “Quando você precisa disso?”. Anote a resposta para retomar no fim.']
        e90=['Faça a rodada de acolhida (3 min): cada aluno diz o nome e uma palavra sobre o dia.','Peça um palpite sobre o que acontece na cena antes de abrir o diálogo.']
    elif k=='me':
        t['goal']='Primeira produção do aluno com o modelo da aula.'
        g=['Mostre o modelo: “'+_s(p.get('model'))+'”.','Cada aluno diz a sua versão trocando um item do quadro de opções.']
        s=['Modele a frase e peça a versão do aluno, trocando um item.']
        e90=['Repita em duplas, trocando de parceiro uma vez.']
    elif k=='review':
        t['goal']='Retomar o que já foi aprendido na mochila.'
        g=['Mostre os cartões e peça que digam em inglês o significado de cada um antes de virar.','Se alguém travar, diga o começo da frase e deixe o grupo completar.']
        s=['Aponte 3 cartões e peça a frase completa em inglês.']
        e90=['Peça uma frase nova com cada cartão que os alunos acertarem rápido.']
    elif k in('work','story'):
        t['goal']='Contexto da obra que inspira a cena.'
        w=(p.get('work') or {}).get('title','a obra')
        g=['Conte em 1 minuto a ideia de “'+_s(w,60)+'” e ligue à situação de hoje.',_s(p.get('question'),160) or 'Pergunte como a história ajuda a imaginar a cena.']
        s=['Resuma a obra em uma frase e pergunte o que o aluno conhece dela.']
        e90=['Peça uma comparação com uma história parecida que o aluno conhece.']
    elif k=='bridge':
        t['goal']='Ponte português → inglês com palavras úteis.'
        ws=[x.get('w') for x in (p.get('words') or []) if isinstance(x,dict)][:6]
        g=['Palavras: '+', '.join(filter(None,ws))+'.','Aluno diz em português um uso real, depois a palavra em inglês.']
        s=['Peça uma frase pessoal com 2 das palavras.']
        e90=['Cada aluno escolhe a palavra mais útil e explica por quê.']
    elif k=='facts':
        t['goal']='Situação em contexto.'
        fs=[x.get('big') for x in (p.get('facts') or []) if isinstance(x,dict)][:3]
        g=['Pontos para explicar: '+'; '.join(map(str,filter(None,fs)))+'.','Peça um exemplo real da vida de cada aluno.']
        s=['Pergunte em que situação o aluno já passou por isso.']
        e90=['Aluno cria uma frase com cada ponto, sem olhar a tela.']
    elif k=='compare':
        c=p.get('compare') or {}
        t['goal']='Comparar Brasil e Estados Unidos.'
        g=['Leia as duas colunas e peça que apontem a maior diferença.','Pergunta: '+_s(c.get('ask'),130)]
        s=['Peça uma experiência pessoal do aluno com essa diferença.']
        e90=['Dupla: um fala como no Brasil, o outro como nos EUA.']
    elif k=='artifact':
        a=(p.get('artifact') or {}).get('decode') or {}
        t['goal']='Ler um objeto real (placa, cartão, aviso).'
        g=['Pergunta: '+_s(a.get('q'),110),'Peça que justifiquem pela pista no texto.']
        s=['Pergunte e peça a pista do texto.']
        if a.get('opts') and isinstance(a.get('ans'),int): ans.append(_s(a.get('q'),70)+' → '+str(a['opts'][a['ans']]))
        e90=['Peça que inventem um objeto parecido com outra informação.']
    elif k=='quiz':
        its=p.get('items') or []
        t['goal']='Checar compreensão.'
        g=['Cada aluno decide sozinho, depois compare as respostas e peça uma justificativa.','Corrija pela pista do texto, não só dizendo “certo/errado”.']
        s=['Aluno responde e justifica; você mostra a pista.']
        for it in its[:6]:
            if 's' in it: ans.append(_s(it['s'],70)+' → '+('Verdadeiro' if it.get('ans') else 'Falso')+(' ('+_s(it.get('why'),70)+')' if it.get('why') else ''))
            elif 'q' in it: ans.append(_s(it['q'],70)+' → '+_s(_ans_idx(it),60))
        e90=['Peça que cada aluno invente uma pergunta igual para o colega.']
    elif k=='reading':
        t['goal']='Leitura compartilhada da cena.'
        gl=[x.get('w') for x in (p.get('glossary') or []) if isinstance(x,dict)][:9]
        g=['Leitura em voz alta, um parágrafo por aluno, depois pergunta: “'+_s(p.get('prompt'),90)+'”.','Glossário: '+', '.join(filter(None,gl))+'. Peça que usem 2 palavras em frases suas.']
        s=['Leiam em turnos; faça a pergunta do prompt no fim.']
        e90=['Segunda leitura: coro, depois sem olhar o texto (aluno conta o que lembra).']
    elif k=='dialog':
        t['goal']='Ouvir e ensaiar o diálogo.'
        ls=p.get('lines') or []
        g=['Toque o áudio; depois leia em duplas, trocando de papel ('+str(len(ls))+' falas).','Aponte as palavras coloridas e peça o que muda se a troca for feita.']
        s=['Você lê '+npc+'; o aluno lê “You”. Depois trocam.']
        e90=['Terceira leitura: aluno faz os dois papéis, em pé, com gesto.']
    elif k=='choice':
        tr=p.get('turn') or {}
        t['goal']='Escolher a resposta natural.'
        g=['Leia a fala de '+npc+': “'+_s(tr.get('npc'),100)+'”.','Cada aluno escolhe, justifica e então vê o resultado.']
        s=['Pergunte por que as outras opções não servem.']
        for o in tr.get('opts') or []:
            if o.get('ok'): ans.append(_s(o.get('en'),90))
        e90=['Peça que reformulem a resposta certa de duas formas.']
    elif k=='vocab':
        t['goal']='Praticar as palavras da aula.'
        ws=[x[0] for x in (p.get('words') or []) if isinstance(x,(list,tuple))][:6]
        g=['Palavras: '+', '.join(ws)+'.','Toque, ouça, repita; cada aluno cria uma frase sua com uma palavra.']
        s=['Peça uma frase pessoal com cada palavra.']
        e90=['Jogo: o professor diz o português, o aluno responde a palavra em inglês e uma frase.']
    elif k=='verbs':
        vs=[x.get('v') for x in (p.get('verbs') or []) if isinstance(x,dict)]
        t['goal']='Formas dos verbos da aula.'
        g=['Verbos: '+', '.join(filter(None,vs))+'.','Mostre as formas e peça uma frase com cada verbo.']
        s=['Aluno diz uma frase com cada forma.']
        e90=['Conjugação em cadeia: cada aluno muda o sujeito.']
    elif k in('verbplay','exprplay','exit'):
        t['goal']={'verbplay':'Aplicar os verbos no contexto.','exprplay':'Escolher a expressão certa.','exit':'Mostrar o que aprendeu.'}[k]
        g=['Cada aluno responde antes de ver a correção.','Explique o “por quê” de cada resposta em uma frase.']
        s=['Aluno responde; você explica o porquê.']
        for it in (p.get('items') or [])[:5]:
            if k=='exit': ans.append(_s(it.get('target'),90))
            else: ans.append(_s(it.get('en') or it.get('cue'),60)+' → '+_s(_ans_idx(it),50))
        e90=['Peça que digam a resposta em voz alta com a frase inteira.']
    elif k=='exprs':
        t['goal']='Expressões úteis.'
        es=[x.get('en') for x in (p.get('items') or []) if isinstance(x,dict)][:6]
        g=['Expressões: '+'; '.join(filter(None,es))+'.','Escolha 3 prioritárias para usar o resto da aula.']
        s=['Aluno diz quando usaria cada uma.']
        e90=['Cada aluno usa 2 expressões em uma mini-cena de 20 segundos.']
    elif k=='pattern':
        sl=[o for x in (p.get('slots') or []) if isinstance(x,dict) for o in (x.get('opts') or [])][:3]
        t['goal']='Padrão da frase.'
        g=['Padrão: “'+_s(p.get('frame'),90)+'”. Nota: '+_s(p.get('note'),90),'Cada aluno troca um espaço: '+', '.join(sl)+'.']
        s=['Aluno diz a frase com 3 combinações.']
        e90=['Peça a versão negativa ou em pergunta.']
    elif k=='soundlab':
        t['goal']='Um som só.'
        g=['Foco: '+_s(p.get('focus'),70)+'. '+_s(p.get('how'),120),'Coro, depois um a um; ouça sem corrigir tudo.']
        s=['Modele, peça repetição, depois uso livre.']
        e90=['Cada aluno grava um áudio de 10 segundos e compara com o modelo.']
    elif k=='role':
        t['goal']='Missão ao vivo.'
        g=[_s(p.get('group'),160),'Complicações para introduzir: '+' / '.join(_s(x,70) for x in (p.get('change') or [])[:3])]
        s=[_s(p.get('solo'),160),'Repita 3 vezes com menos apoio.']
        e90=['Em duplas: 3 rodadas de 3 minutos com a complicação trocada a cada rodada. Troque de parceiro.','Observador anota 2 acertos e 2 erros.']
    elif k=='writing':
        t['goal']='Escrever a versão do aluno.'
        g=['Tarefa: '+_s(p.get('task'),110),'Modelo: “'+_s(p.get('model'),120)+'”.','Troquem textos e corrijam em duplas.']
        s=['Corrija só 2–3 pontos prioritários e mostre uma forma mais natural.']
        for c in (p.get('checks') or [])[:4]: ans.append(_s(c,70))
        e90=['Leitura em voz alta de uma frase de cada aluno.']
    elif k=='finish':
        t['goal']='Fechar e passar a tarefa.'
        g=['Recapitule 3 coisas aprendidas.','Tarefa: '+_s(p.get('homework'),130),'Pergunta de adaptação: '+_s(p.get('next'),120)]
        s=['Aluno diz o que aprendeu e lê a tarefa.']
        e90=['Correção coletiva (3 min): mostre 3 frases anotadas na pausa e no jogo de papéis, sem expor o autor.']
    elif k=='reviewwords':
        t['goal']='Retomar palavras da aula anterior.'
        ws=[x.get('w') for x in (p.get('words') or []) if isinstance(x,dict)][:8]
        g=['Palavras da mochila: '+', '.join(filter(None,ws))+'.','Mostre a figura e peça a palavra em inglês antes de revelar.']
        s=['Aponte 4 figuras e peça uma frase com cada uma.']
        e90=['Cada aluno escolhe 2 palavras e as usa em uma frase nova.']
    elif k=='reviewsay':
        t['goal']='Retomar frases da aula anterior em voz alta.'
        es=[x.get('en') for x in (p.get('items') or []) if isinstance(x,dict)][:4]
        g=['Frases: '+' / '.join(map(lambda z:_s(z,60),filter(None,es)))+'.','Coro, depois um a um; sem olhar a tela na segunda vez.']
        s=['Aluno diz as frases sem olhar; você corrige 1 ponto.']
        e90=['Aluno troca uma palavra em cada frase e diz a nova.']
    elif k=='bridge2':
        t['goal']='Como não traduzir palavra por palavra.'
        its=[x for x in (p.get('items') or []) if isinstance(x,dict)][:4]
        g=['Compare erro e forma natural: '+' | '.join(_s(x.get('wrong'),50)+' → '+_s(x.get('fix'),50) for x in its)+'.','Peça que digam a forma natural em voz alta.']
        s=['Pergunte por que o erro acontece em português e como evitar.']
        for x in its: err.append({'w':_s(x.get('wrong'),60),'r':_s(x.get('fix'),60)})
        e90=['Cada aluno cria um erro típico seu e o grupo corrige.']
    else: return None
    t['solo']=s; t['group']=g; t['extra90']=e90
    if ans: t['answers']=ans
    if err: t['errors']=err
    return t
def apply(L):
    for p in L.get('pages',[]):
        t=teach(p,L)
        if t: p['teach']=t
    pl=plan90(L)
    if pl: L['plan'].update(pl)
    return L
