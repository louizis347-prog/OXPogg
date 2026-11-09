from ext import A
def W(id,s):
    rows=[]
    for p in s.split('|'):
        e,t=p.split('=');rows.append('%s;%s;%s;%s'%(e,t,e[0].upper()+e[1:]+'.',t[0].upper()+t[1:]+'.'))
    A(id,"\n".join(rows))
W('B1-L029','teaching vocation=vocação docente|teacher mentor=professor mentor|classroom manager=gestor de sala|calm voice=voz calma|trial lesson=aula-teste|candidate profile=perfil do candidato|teacher quality=qualidade docente')
W('B1-L030','campus visit day=dia de visita ao campus')
W('B1-L031','stove top=fogão|soup bowl=tigela de sopa|stirring spoon=colher para mexer|kitchen clock=relógio da cozinha|cooking oil=óleo de cozinha|boiling point=ponto de fervura')
W('B1-L032','friendly smile=sorriso amigável|small gesture=pequeno gesto|new neighbor=vizinho novo')
W('B1-L033','funny dialogue=diálogo engraçado|book recommendation=indicação de livro')
