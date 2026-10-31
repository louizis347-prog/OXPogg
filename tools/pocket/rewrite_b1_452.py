#!/usr/bin/env python3
"""Editorial replacement for B1 #452, following its main-branch script."""
import json
from pathlib import Path

data = Path(__file__).resolve().parents[2] / 'data'
path = data / 'pk-b1_10.json'
episodes = json.loads(path.read_text(encoding='utf-8'))
e = next(item for item in episodes if item['n'] == 952452)
plan = next(item for item in json.loads((data/'pk-roteiro/pk-b1.json').read_text(encoding='utf-8')) if item['n'] == 952452)
fr = {f['k']:f for f in e['fr']}
lines = [
    ['Jordan', 'The café lost power while we were setting up the storytelling night.', 'O café ficou sem energia enquanto preparávamos a noite de histórias.'],
    ['You', 'I was checking the speakers when the lights went out.', 'Eu estava verificando as caixas de som quando as luzes se apagaram.'],
    ['Jordan', 'Could we move everyone to the courtyard? The campfire is still burning.', 'Podemos levar todos para o pátio? A fogueira ainda está acesa.'],
    ['You', 'A wanderer was telling a legend when the rain started.', 'Um andarilho estava contando uma lenda quando a chuva começou.'],
    ['Jordan', 'Then the courtyard is out. The old tavern across the street has a roof.', 'Então o pátio está fora de questão. A velha taverna do outro lado da rua tem cobertura.'],
    ['You', 'While the embers were fading, I carried the chairs into the tavern.', 'Enquanto as brasas perdiam o brilho, levei as cadeiras para a taverna.'],
    ['Jordan', 'Good call. The group can finish its journey there, like the pilgrims in The Canterbury Tales.', 'Boa ideia. O grupo pode terminar sua jornada lá, como os peregrinos de Os Contos da Cantuária.'],
    ['You', 'I was opening the door when the wanderer offered to finish his tale indoors.', 'Eu estava abrindo a porta quando o andarilho se ofereceu para terminar seu conto lá dentro.'],
]
words = [['campfire','fogueira','🔥'],['wanderer','andarilho','🚶'],['tavern','taverna','🏠'],['legend','lenda','📖'],['embers','brasas','🪵']]
e['t']='While the Fire Was Burning'; e['s']=plan['tema_pt']; e['sc']='cafe'
e['a']={'k':'📖 Conto','w':'The Canterbury Tales','y':'c. 1400','d':'Na obra de Geoffrey Chaucer, peregrinos contam histórias durante uma viagem. Aqui, uma noite de histórias muda de lugar por causa da chuva.'}
e['h']={'l':lines[1][1],'tr':lines[1][2],'src':'Pocket'}
e['p']='Hoje você conta o que estava acontecendo quando surgiu um imprevisto.'
e['g']={'t':lines[7][1]}; e['v']=[x[:] for x in words]
e['character']={'id':'pk_jordan','name':'Jordan','gender':'f','role':'organizadora comunitária','city':'New Orleans','recurring':True}
e['arc']={'i':46,'pos':2,'of':10}
fr['pkhero'].update({'num':452,'lvl':'B1','face':'👩🏾','name':'Jordan','city':'New Orleans','sub':'While the Fire Was Burning','mission':e['p'],'hook':[lines[1][1],lines[1][2]],'boss':False})
fr['pkdlg'].update({'lines':lines,'vocab':[[w,p] for w,p,_ in words],'cast':{'Jordan':['👩🏾','#FF7A7A'],'You':['🙂','#e85d75']}})
examples=[lines[2],lines[3],lines[4],lines[3],lines[5]]
fr['pkvoc'].update({'cards':[[w,p,ic,row[1],row[2]] for (w,p,ic),row in zip(words,examples)],'notes':[{'en':'was telling ... when the rain started','pt':'estava contando ... quando a chuva começou','txt':'💡 A ação longa usa past continuous; o acontecimento que a interrompe usa past simple.'}]})
pars=[(['At a café in New Orleans,','Num café em Nova Orleans,'],['the storytelling night takes an unexpected turn.','a noite de histórias muda de rumo.'],None,'🏙️')]
pars += [([('Jordan says:','Jordan diz:') if row[0]=='Jordan' else ('You answer:','Você responde:')][0],[row[1],row[2]],row[0],'💬') for row in lines]
pars.append((['After the rain,','Depois da chuva,'],['the group finishes the tale safely inside the tavern.','o grupo termina o conto em segurança dentro da taverna.'],None,'📖'))
fr['pkread'].update({'pars':[{'lead':list(lead),'q':q,'who':who,'ic':ic} for lead,q,who,ic in pars],'vocab':[[w,p] for w,p,_ in words]})
fr['pkbuild']['items']=[
 {'en':'I was checking the speakers when the lights {0}.','pt':'Eu estava verificando as caixas de som quando as luzes se {0}.','opts':[['went out','apagaram'],['came back','acenderam'],['stayed on','mantiveram acesas']],'note':'Past continuous descreve a ação em curso; past simple marca a interrupção.'},
 {'en':'While the embers were fading, I {0} the chairs inside.','pt':'Enquanto as brasas perdiam o brilho, eu {0} as cadeiras para dentro.','opts':[['carried','levei'],['left','deixei'],['counted','contei']],'note':'While introduz a ação em andamento.'}
]
fr['pkspeak']['items']=[
 {'who':'Jordan','line':[lines[0][1],lines[0][2]],'target':lines[1][1],'pt':lines[1][2]},
 {'who':'Jordan','line':[lines[4][1],lines[4][2]],'target':lines[5][1],'pt':lines[5][2]}
]
fr['wrap'].update({'recap':[[row[1],row[2]] for row in (lines[1],lines[3],lines[5],lines[7])],
 'expr':[['Good call.','Boa ideia.']],
 'culture':'Em The Canterbury Tales, de Geoffrey Chaucer, viajantes contam histórias uns aos outros. A conversa retoma essa ideia ao mudar a roda de histórias para um lugar coberto.',
 'teaser':{'t':plan['proximo'],'d':'Uma surpresa muda outra história.'},
 'sticker':{'name':'Jordan','face':'👩🏾','role':'organizadora comunitária','city':'New Orleans','boss':False},
 'stickers':[[w,p,ic,row[1],row[2]] for (w,p,ic),row in zip(words,examples)]})
path.write_text(json.dumps(episodes,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
