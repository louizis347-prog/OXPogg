from ext import A
def W(id,s):
    rows=[]
    for p in s.split('|'):
        e,t=p.split('=');rows.append('%s;%s;%s;%s'%(e,t,e[0].upper()+e[1:]+'.',t[0].upper()+t[1:]+'.'))
    A(id,"\n".join(rows))
W('B1-L089','work happiness=felicidade no trabalho|team habit=hábito de equipe|office laughter=risadas no escritório|friendly colleague=colega simpático')
W('B1-L090','empty chair=cadeira vazia|office silence=silêncio do escritório|office clue board=quadro de pistas')
W('B1-L091','career talk=conversa sobre carreira|brave choice=escolha corajosa')
W('B1-L092','repair bill=conta do conserto')
