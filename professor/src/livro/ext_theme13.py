from ext import A
def W(id,s):
    rows=[]
    for p in s.split('|'):
        e,t=p.split('=');rows.append('%s;%s;%s;%s'%(e,t,e[0].upper()+e[1:]+'.',t[0].upper()+t[1:]+'.'))
    A(id,"\n".join(rows))
W('B2-L001','hybrid workplace=local de trabalho híbrido|career attitude=atitude de carreira|work habit=hábito de trabalho|office policy=política do escritório|job trend=tendência de emprego|workplace survey=pesquisa no local de trabalho')
W('B2-L007','software demo=demonstração de software|easy interface=interface fácil|user instruction=instrução ao usuário|shared agreement=acordo compartilhado|product guide=guia do produto|team explanation=explicação da equipe|tool startup=startup de ferramentas|work quantity=quantidade de trabalho|office documentary=documentário de escritório')
W('B2-L013','speech speed=velocidade da fala|slow audio=áudio lento|pronunciation book=livro de pronúncia|audio lesson=aula em áudio|language writer=escritor de idiomas')
W('B2-L014','station shop=loja da estação|trip cancellation=cancelamento de viagem|cancelled ticket=bilhete cancelado|departure hall=salão de embarque|night train=trem noturno|trip preparation=preparação da viagem')
