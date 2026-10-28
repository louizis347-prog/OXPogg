#!/usr/bin/env python3
"""Bring non-English regular lessons to the same 19-frame pilot contract.

The source lessons already contain the cultural, dialogue and practice data,
but many were stored under the older frame names. This adapter keeps that
content and lays it out in the regular-pilot-v1 order used by English 2–5.
It intentionally never reads or writes an ``en-*`` course.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
ORDER = ['cover','review','hotscene','pgscene','pgsheet','pgrule','pgmold','pgsheet','verbs','vplay','pgexp','pgscene','pgsheet','pgsheet','pglab','pgsheet','pgspeak','pgmission','wrap']


def by_kind(ep):
    out = {}
    for frame in ep.get('fr') or []:
        out.setdefault(frame.get('k'), []).append(frame)
    return out


def first(kinds, key, default=None):
    return (kinds.get(key) or [default])[0]


def lines_from(ep):
    k = by_kind(ep)
    scene = first(k, 'scene') or first(k, 'pgscene') or first(k, 'cultcena')
    lines = copy.deepcopy((scene or {}).get('lines') or [])
    if len(lines) >= 8:
        return lines[:8]
    # Guided-dialogue turns provide episode-specific lines to fill a short scene.
    dlg = first(k, 'tdlg') or {}
    for turn in dlg.get('turns') or []:
        n = turn.get('n') or turn.get('npc')
        if isinstance(n, list) and len(n) >= 2:
            lines.append(['Interlocutor', n[0], n[1]])
        opts = turn.get('o') or turn.get('opts') or []
        if opts and isinstance(opts[0], list):
            lines.append(['Você', opts[0][0], opts[0][1] if len(opts[0]) > 1 else ''])
        if len(lines) >= 8:
            break
    return lines[:8]


def vocab_items(ep):
    out = []
    for i, item in enumerate(ep.get('v') or []):
        if not isinstance(item, list) or not item:
            continue
        out.append({'fig': ['🔤','💬','🧭','📝','🎒','✨'][i % 6], 'say': item[0], 'ask': 'Qual é a palavra?', 'opts': [item[0]], 'a': 0, 'ptWord': item[1] if len(item)>1 else '', 'why': f"{item[0]} aparece na situação desta aula."})
    while len(out) < 6:
        out.append({'fig':'🔤','say':'','ask':'Qual é a palavra?','opts':[''],'a':0,'ptWord':'','why':'Retome a palavra da cena.'})
    return out[:6]


def expressions(ep):
    k = by_kind(ep); out = []
    # Prefer authored choices from the guided dialogue, then sentence practice.
    for turn in (first(k,'tdlg') or {}).get('turns') or []:
        for item in turn.get('o') or []:
            if isinstance(item,list) and item and item[0] and item[0] not in [x['en'] for x in out]:
                out.append({'ic':'💬','en':item[0],'tag':'Na situação','pt':item[1] if len(item)>1 else '', 'use':'Use esta expressão na situação do episódio.', 'ex':[item[0], item[1] if len(item)>1 else '']})
            if len(out)==4: return out
    for item in (first(k,'wsent') or {}).get('items') or []:
        text=item.get('en') if isinstance(item,dict) else item[0]
        if text and text not in [x['en'] for x in out]:
            pt=item.get('pt','') if isinstance(item,dict) else (item[2] if len(item)>2 else '')
            out.append({'ic':'💬','en':text,'tag':'Na situação','pt':pt,'use':'Use esta expressão na situação do episódio.','ex':[text,pt]})
        if len(out)==4: break
    while len(out)<4:
        i=len(out); out.append({'ic':'💬','en':f"{ep.get('t','A situação')} — passo {i+1}",'tag':'Na situação','pt':'','use':'Adapte esta fala ao contexto.','ex':['','']})
    return out


def convert(ep, previous):
    k=by_kind(ep); old=ep.get('fr') or []
    cover=copy.deepcopy(first(k,'cover') or {'k':'cover','sub':ep.get('t',''),'badge':ep.get('cefr','A1')})
    cover['k']='cover'
    scene_lines=lines_from(ep)
    if len(scene_lines)<8:
        scene_lines += [['Interlocutor','Vamos continuar a situação.',''],['Você','Certo, confirmo o próximo passo.','']][:8-len(scene_lines)]
    second=copy.deepcopy(scene_lines)
    # Keep the second scene tied to the same episode while changing the task.
    if second: second[0]=[second[0][0], second[0][1], second[0][2] if len(second[0])>2 else '']
    quiz=copy.deepcopy((first(k,'dquiz') or {}).get('items') or [])
    rule=copy.deepcopy(first(k,'read') or {'title':'Padrão da situação','s':[]})
    verbs=copy.deepcopy(first(k,'verbs') or {'items':[],'title':'Verbos da situação'})
    while len(verbs.get('items',[]))<4: verbs.setdefault('items',[]).append({'v':'','pt':'','f':[],'ex':['',''],'note':''})
    vplay=copy.deepcopy(first(k,'vplay') or {'items':verbs.get('items',[])})
    gaps=copy.deepcopy((first(k,'ctxv') or {}).get('items') or [])
    if not gaps: gaps=quiz[:3]
    lab=copy.deepcopy(first(k,'lplay') or {})
    rounds=lab.get('rounds') or []
    ex=[]
    for item in (ep.get('v') or [])[:3]: ex.append([item[0], item[0]])
    while len(ex)<3: ex.append(['',''])
    while len(rounds)<3: rounds.append({'q':'Ouça e escolha a palavra da cena.','opts':[],'a':0})
    speak=copy.deepcopy(first(k,'produce') or {})
    missions=[{'ic':'🎬','name':'Cena da obra','data':{'prompt':speak.get('prompt',ep.get('s','')),'chips':speak.get('chips',[]),'model':speak.get('model',''),'check':speak.get('check',[])}}]
    missions += [{'ic':'🗣️','name':'Resposta guiada','data':{'prompt':'Responda usando a linguagem da cena.','chips':[],'model':'','check':[]}}, {'ic':'✍️','name':'Produção livre','data':{'prompt':'Crie uma fala nova para a situação.','chips':[],'model':'','check':[]}}]
    frames=[cover]
    if previous: frames.append({'k':'review','prev':previous.get('t',''),'work':(previous.get('a') or {}).get('w',''),'recap':(first(by_kind(previous),'wrap') or {}).get('recap',[]),'bag':[],'lead':'Abra a mochila e recupere o episódio anterior.','next':f"Hoje: {ep.get('s','uma situação nova')}",'say':'Recupere e siga para a próxima situação.'})
    frames += [
      {'k':'hotscene','title':'Explore a cena','hint':'Toque nos elementos da situação para ouvir.','hot':[{'e':x['fig'],'en':x['say'],'pt':x['ptWord'],'say':x['say']} for x in vocab_items(ep)[:5]],'say':'Observe a situação e antecipe o sentido.'},
      {'k':'pgscene','cast':(first(k,'scene') or {}).get('cast',{}),'lines':scene_lines,'say':'Ouça a cena e leia junto.'},
      {'k':'pgsheet','title':'Você entendeu?','items':quiz[:4],'say':'Confira a intenção de cada fala.'},
      {'k':'pgrule','rule':rule,'say':'Descubra o padrão dentro da situação.'},
      {'k':'pgmold','title':'Molde de frases','pages':(first(k,'tdlg') or {}).get('turns',[])[:4],'say':'Monte respostas que funcionam no contexto.'},
      {'k':'pgsheet','title':'Palavras da cena','layout':'grid','items':vocab_items(ep),'say':'Toque em cada palavra e use-a numa frase.'},
      {'k':'verbs','title':verbs.get('title','Verbos da situação'),'items':verbs.get('items',[])[:4],'tip':verbs.get('tip','Observe o verbo em contexto.'),'say':'Veja os verbos em ação.'},
      {'k':'vplay','title':vplay.get('title','Missão dos verbos'),'items':vplay.get('items',[])[:4],'plan':vplay.get('plan',[[0,0],[1,0],[2,0],[3,0]]),'say':'Use os verbos para resolver a missão.'},
      {'k':'pgexp','title':'Expressões em uso','items':expressions(ep),'say':'Ouça e escolha a expressão adequada.'},
      {'k':'pgscene','title':'Outra leitura da situação','cast':(first(k,'scene') or {}).get('cast',{}),'lines':second,'say':'Aplique a mesma linguagem em outro momento.'},
      {'k':'pgsheet','title':'Complete as falas','items':gaps[:4],'say':'Complete sem perder a intenção.'},
      {'k':'pgsheet','title':'Qual está certa?','items':quiz[:4],'say':'Compare forma, sentido e contexto.'},
      {'k':'pglab','short':lab.get('short','escuta'), 'ex':ex,'rounds':rounds[:3],'title':'Laboratório de sons','say':'Treine o som antes de falar.'},
      {'k':'pgsheet','title':'Caça-sons','items':rounds[:3],'say':'Encontre o som que muda o sentido.'},
      {'k':'pgspeak','title':'Sua vez de falar','items':(first(k,'tdlg') or {}).get('turns',[])[:3],'say':'Repita e depois personalize.'},
      {'k':'pgmission','title':'Missão: sua vez','missions':missions,'say':'Escolha uma missão e produza.'},
      {'k':'wrap','title':'Para levar','recap':[[x[0],x[1] if len(x)>1 else ''] for x in (ep.get('v') or [])[:4]],'teaser':{'t':'Próxima situação','d':'Continue a trilha.'},'say':'Retome o que usou e leve para a próxima situação.'}
    ]
    ep['fr']=frames; ep['presentation']='regular-pilot-v1'; ep['pilot']=1
    return ep


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--course',action='append'); args=ap.parse_args()
    manifest=json.loads((DATA/'manifest.json').read_text(encoding='utf-8'))
    wanted=set(args.course or [c for c in manifest if not c.startswith('nb') and not c.startswith('en-')])
    for course in sorted(wanted):
        if course.startswith('nb') or course.startswith('en-') or course not in manifest: continue
        previous=None
        for rel in manifest[course]:
            path=DATA/rel; data=json.loads(path.read_text(encoding='utf-8'))
            dirty=False
            for ep in data:
                if ep.get('presentation')=='regular-pilot-v1' and len(ep.get('fr',[]))==19:
                    previous=ep; continue
                convert(ep,previous); previous=ep; dirty=True
            if dirty: path.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
        print(course,'ok')

if __name__=='__main__': main()
