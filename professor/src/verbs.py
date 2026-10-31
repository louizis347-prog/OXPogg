# Verbos: forma base=tradução [irregulares: |3ª|ing|passado|particípio]. Regulares geram as formas automaticamente.
IRR = {
 'be':('is','being','was/were','been'),'have':('has','having','had','had'),'go':('goes','going','went','gone'),'do':('does','doing','did','done'),
 'eat':('eats','eating','ate','eaten'),'drink':('drinks','drinking','drank','drunk'),'see':('sees','seeing','saw','seen'),'buy':('buys','buying','bought','bought'),
 'take':('takes','taking','took','taken'),'make':('makes','making','made','made'),'give':('gives','giving','gave','given'),'get':('gets','getting','got','got'),
 'say':('says','saying','said','said'),'tell':('tells','telling','told','told'),'speak':('speaks','speaking','spoke','spoken'),'read':('reads','reading','read','read'),
 'write':('writes','writing','wrote','written'),'come':('comes','coming','came','come'),'sleep':('sleeps','sleeping','slept','slept'),'run':('runs','running','ran','run'),
 'swim':('swims','swimming','swam','swum'),'sing':('sings','singing','sang','sung'),'meet':('meets','meeting','met','met'),'know':('knows','knowing','knew','known'),
 'think':('thinks','thinking','thought','thought'),'find':('finds','finding','found','found'),'lose':('loses','losing','lost','lost'),'bring':('brings','bringing','brought','brought'),
 'send':('sends','sending','sent','sent'),'wear':('wears','wearing','wore','worn'),'put':('puts','putting','put','put'),'sit':('sits','sitting','sat','sat'),
 'stand':('stands','standing','stood','stood'),'fall':('falls','falling','fell','fallen'),'break':('breaks','breaking','broke','broken'),'build':('builds','building','built','built'),
 'draw':('draws','drawing','drew','drawn'),'drive':('drives','driving','drove','driven'),'ride':('rides','riding','rode','ridden'),'fly':('flies','flying','flew','flown'),
 'win':('wins','winning','won','won'),'forget':('forgets','forgetting','forgot','forgotten'),'feel':('feels','feeling','felt','felt'),'leave':('leaves','leaving','left','left'),
 'keep':('keeps','keeping','kept','kept'),'hold':('holds','holding','held','held'),'hear':('hears','hearing','heard','heard'),'pay':('pays','paying','paid','paid'),
 'spend':('spends','spending','spent','spent'),'sell':('sells','selling','sold','sold'),'choose':('chooses','choosing','chose','chosen'),'begin':('begins','beginning','began','begun'),
 'wake':('wakes','waking','woke','woken'),'teach':('teaches','teaching','taught','taught'),'lend':('lends','lending','lent','lent'),'cost':('costs','costing','cost','cost'),
 'hurt':('hurts','hurting','hurt','hurt'),'cut':('cuts','cutting','cut','cut'),'stay':('stays','staying','stayed','stayed'),'pick':('picks','picking','picked','picked'),
 'hang':('hangs','hanging','hung','hung'),'hide':('hides','hiding','hid','hidden'),'hit':('hits','hitting','hit','hit'),'blow':('blows','blowing','blew','blown'),'spill':('spills','spilling','spilled','spilled'),'fit':('fits','fitting','fitted','fitted'),'grow':('grows','growing','grew','grown'),'catch':('catches','catching','caught','caught'),'understand':('understands','understanding','understood','understood'),
}
DOUBLE = set('stop plan chat shop jog drop skip hug'.split())
EXTRA_PT = 'accept=aceitar|advise=aconselhar|apologize=pedir desculpas|attach=anexar|blow=soprar|chill=relaxar|comment=comentar|compare=comparar|confirm=confirmar|connect=conectar|deliver=entregar|disagree=discordar|dream=sonhar|exercise=se exercitar|experience=viver/experimentar|fit=caber/servir|hang=pendurar/sair juntos|hide=esconder|hike=fazer trilha|hit=bater|organize=organizar|prepare=preparar|reach=alcançar|reply=responder|sign=assinar|spill=derramar/revelar|talk=conversar|water=regar|wave=acenar|whisper=sussurrar'
PT = """repeat=repetir|stop=parar|plan=planejar|be=ser/estar|have=ter|go=ir|do=fazer|eat=comer|drink=beber|see=ver|buy=comprar|take=levar/pegar|make=fazer/criar|give=dar|get=conseguir/ficar|say=dizer|tell=contar|speak=falar|read=ler|write=escrever|come=vir|sleep=dormir|run=correr|swim=nadar|sing=cantar|meet=encontrar/conhecer|know=saber/conhecer|think=pensar/achar|find=achar|lose=perder|bring=trazer|send=enviar|wear=vestir/usar|put=colocar|sit=sentar|stand=ficar em pé|fall=cair|break=quebrar|build=construir|draw=desenhar|drive=dirigir|ride=andar (de)|fly=voar|win=ganhar|forget=esquecer|feel=sentir|leave=sair/deixar|keep=manter|hold=segurar|hear=ouvir|pay=pagar|spend=gastar/passar (tempo)|sell=vender|choose=escolher|begin=começar|wake=acordar|teach=ensinar|lend=emprestar|cost=custar|hurt=doer|cut=cortar|stay=ficar|pick=pegar/escolher|grow=crescer/cultivar|catch=pegar/alcançar|understand=entender|work=trabalhar|study=estudar|play=jogar/brincar|live=morar/viver|like=gostar|love=amar|want=querer|need=precisar|listen=escutar|watch=assistir|cook=cozinhar|clean=limpar|call=ligar/chamar|help=ajudar|wait=esperar|open=abrir|close=fechar|walk=caminhar|dance=dançar|travel=viajar|visit=visitar|arrive=chegar|ask=perguntar/pedir|answer=responder|use=usar|try=tentar|start=começar|finish=terminar|learn=aprender|carry=carregar|turn=virar/ligar|look=olhar|fix=consertar|paint=pintar|remember=lembrar|believe=acreditar|hope=esperar (ter esperança)|decide=decidir|invite=convidar|share=compartilhar|enjoy=curtir|hate=odiar|rest=descansar|relax=relaxar|wash=lavar|celebrate=celebrar|order=pedir (comida)|rent=alugar|book=reservar|check=conferir|change=mudar|save=salvar/economizar|count=contar (números)|spell=soletrar|point=apontar|move=mudar-se/mover|show=mostrar|laugh=rir|cry=chorar|smile=sorrir|wish=desejar|promise=prometer|borrow=pegar emprestado|practice=praticar|happen=acontecer|offer=oferecer|prefer=preferir|miss=sentir falta/perder|agree=concordar|explain=explicar|introduce=apresentar|join=juntar-se|climb=escalar|kick=chutar|jump=pular|shout=gritar|touch=tocar|taste=provar|smell=cheirar|push=empurrar|pull=puxar|plant=plantar|bake=assar|mix=misturar|add=adicionar|pour=despejar|stir=mexer|heat=aquecer|boil=ferver|chat=conversar|text=mandar mensagem|post=postar|download=baixar|search=pesquisar|click=clicar|log=entrar (login)|join=participar|apply=candidatar-se|hire=contratar|earn=ganhar (salário)|train=treinar|race=correr (competir)|score=marcar gol|cheer=torcer|rain=chover|snow=nevar|shine=brilhar|rescue=resgatar|save=salvar|hurry=apressar-se|pack=fazer a mala|park=estacionar|cross=atravessar|follow=seguir|notice=notar|imagine=imaginar|predict=prever|complain=reclamar|refund=reembolsar|thank=agradecer|greet=cumprimentar|welcome=dar boas-vindas|collect=coletar|decorate=decorar|bake=assar"""
PTD = {}
for it in PT.split('|'):
    a, b = it.split('=', 1); PTD.setdefault(a, b)
def forms(v):
    if v in IRR: s, g, p, pp = IRR[v]; return dict(base=v, s=s, ing=g, past=p, pp=pp)
    if v.endswith(('s', 'sh', 'ch', 'x', 'z', 'o')): s = v + 'es'
    elif v.endswith('y') and v[-2] not in 'aeiou': s = v[:-1] + 'ies'
    else: s = v + 's'
    if v.endswith('ie'): g = v[:-2] + 'ying'
    elif v.endswith('e') and not v.endswith('ee'): g = v[:-1] + 'ing'
    elif v in DOUBLE: g = v + v[-1] + 'ing'
    else: g = v + 'ing'
    if v.endswith('e'): p = v + 'd'
    elif v.endswith('y') and v[-2] not in 'aeiou': p = v[:-1] + 'ied'
    elif v in DOUBLE: p = v + v[-1] + 'ed'
    else: p = v + 'ed'
    return dict(base=v, s=s, ing=g, past=p, pp=p)
def entry(v):
    f = forms(v); f['pt'] = PTD.get(v, v); f['irr'] = v in IRR; return f

for it in EXTRA_PT.split('|'):
    a, b = it.split('=', 1); PTD.setdefault(a, b)
