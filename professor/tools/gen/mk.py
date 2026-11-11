def build(s):
    L=s['lines']
    pool=[('Sorry, I do not know.','Desculpe, eu não sei.','Okay, thanks.'),('Please wait a moment.','Espere um momento, por favor.','Sure.'),('Can you say that again?','Pode repetir?','Yes, of course.'),('Here you go.','Aqui está.','Thank you.'),('Hello! Can I help you?','Olá! Posso ajudar?','Yes, please.'),('Good news, it is free.','Boa notícia, é grátis.','Great.')]
    role=[]
    for k,i in enumerate((0,2,4,6)):
        a=L[i]; b=L[i+1]
        role.append([(a[1],a[2],b[1]),(pool[k][0],pool[k][1],pool[k][2]),(pool[k+2][0],pool[k+2][1],pool[k+2][2])])
    verbs=[]
    for (v,ic,pt,third,past,ing,p1,p3,pp,pg) in s['verbs']:
        reg=past in (v+'ed',v+'d')
        verbs.append((v,ic,pt,'%s = %s. %s: %s.'%(v.capitalize(),pt,'Regular' if reg else 'Passado',past),third,past,ing,p1,p3,pp,pg))
    exprs=[(L[i][1],L[i][2],L[i][1],u) for i,u in s['exprs']]
    m=dict(reg=s['reg'],title=s['title'],city=s['city'],npc=s['npc'],you='Ana' if s['npc']!='Ana' else 'Ben',face=s['face'],g=s['g'],yg=s['yg'],crole=s['crole'],sc=s['sc'],pool=s['pool'],
     story=s['story'],p=s['p'],mission=s['mission'],emo=s['emo'],teaser=s['teaser'],teaser_d=s['teaser_d'],badge=s['badge'],lines=L,open=s['open'],close=s['close'],rtitle=s['rtitle'],gloss=s['gloss'],
     fast=s['fast'],scan=s['scan'],tf=s['tf'],order=s['order'],ctx=s['ctx'],chunks=s['chunks'],think=s['think'],cu=s['cu'],errors=s['errors'],homework=s['homework'],hw=s['hw'],lab=s['lab'],cards=s['cards'],key=s['key'],vocab=s['vocab'],molds=s['molds'],sounds=s['sounds'],role=role,change=s['change'],wtask=s['wtask'],wmodel=s['wmodel'],kw=s['kw'],verbs=verbs,exprs=exprs,real=s['real'],swaps=s['swaps'],mini=s['mini'])
    return m
