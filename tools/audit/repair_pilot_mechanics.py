#!/usr/bin/env python3
"""Repair only mechanical pilot fields from authored episode data.

No dialogue, vocabulary, work, or cultural text is generated here. The repair
keeps the first three authored mold pages, derives two more speaking prompts
from the existing scene, and rebuilds the review bag from the previous episode.
"""
from __future__ import annotations

import argparse, copy, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]; DATA=ROOT/'data'

def first(fr,k): return next((x for x in fr if x.get('k')==k),{})

def replace_value(value, old, new):
    if isinstance(value, dict):
        for k,v in list(value.items()): value[k]=replace_value(v,old,new)
    elif isinstance(value, list):
        value[:]=[replace_value(v,old,new) for v in value]
    elif isinstance(value, str) and value == old: return new
    return value

def repair(ep, previous):
    fr=ep.get('fr') or []
    mold=first(fr,'pgmold')
    if len(mold.get('pages') or [])>3: mold['pages']=mold['pages'][:3]
    if not mold.get('pages'):
        scene=next((x for x in fr if x.get('k')=='pgscene'),{})
        lines=[x for x in scene.get('lines') or [] if isinstance(x,list) and len(x)>=2]
        mold['pages']=[{'label':'Abrir a conversa','slots':[{'cat':'fala','opts':[[x[1],x[2] if len(x)>2 else ''] for x in lines[:3]]}],'end':['.','.']},
                       {'label':'Perguntar e responder','slots':[{'cat':'pergunta','opts':[[x[1],x[2] if len(x)>2 else ''] for x in lines[3:6]]}],'end':['?','?']},
                       {'label':'Fechar a situação','slots':[{'cat':'fecho','opts':[[x[1],x[2] if len(x)>2 else ''] for x in lines[6:8]]}],'end':['.','.']}]
    speak=first(fr,'pgspeak')
    if len(speak.get('items') or [])<5:
        scene=next((x for x in fr if x.get('k')=='pgscene'),{})
        for line in scene.get('lines') or []:
            if isinstance(line,list) and len(line)>=3:
                pair=[line[1],line[2]]
                if pair not in speak.setdefault('items',[]): speak['items'].append(pair)
            if len(speak['items'])>=5: break
    if len(speak.get('items') or [])>5: speak['items']=speak['items'][:5]
    cover=first(fr,'cover')
    if cover and 'em 10 minutos' not in str(cover.get('sub','')).lower():
        cover['sub']=str(cover.get('sub','')).rstrip('.')+' em 10 minutos.'
    review=first(fr,'review')
    if review and len(review.get('bag') or [])<5 and previous:
        pfr=previous.get('fr') or []
        pv=previous.get('v') or []
        vb=first(pfr,'verbs').get('items') or []
        ex=first(pfr,'pgexp').get('items') or []
        lab=first(pfr,'pglab')
        review['bag']=[
          {'ic':'📌','l':'Padrão','items':[{'ic':'📌','t':previous.get('gs') or previous.get('t',''),'pt':previous.get('s','')}]},
          {'ic':'🔤','l':'Palavras','items':[{'ic':'🔤','t':x[0],'pt':x[1] if len(x)>1 else ''} for x in pv[:6]]},
          {'ic':'🏃','l':'Verbos','items':[{'ic':'🏃','t':x.get('v',''),'pt':x.get('pt','')} for x in vb[:4]]},
          {'ic':'💬','l':'Expressões','items':[{'ic':'💬','t':x.get('en',''),'pt':x.get('pt','')} for x in ex[:4]]},
          {'ic':'🎧','l':'Sons','items':[{'ic':'🎧','t':lab.get('short',''),'pt':'','s':', '.join(str(x[0]) for x in (lab.get('ex') or [])[:3])}]},
        ]

def repair_known_work_duplicates(course, episodes):
    # These two A1 pairs were generated with the same work. Replace only the
    # duplicate episode metadata and every exact work label in that episode.
    changes={'es-a1':{7071001:('La Casa de Papel','Volver'),7071002:('Don Quijote de la Mancha','El laberinto del fauno')}}.get(course,{})
    for ep in episodes:
        if ep.get('n') in changes:
            old,new=changes[ep['n']]; replace_value(ep,old,new)
            ep.setdefault('a',{})['w']=new

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--course',required=True);args=ap.parse_args()
    manifest=json.loads((DATA/'manifest.json').read_text(encoding='utf-8'))
    if args.course not in manifest or args.course.startswith('nb') or args.course.startswith('en-'): raise SystemExit('curso fora do escopo')
    previous=None
    for rel in manifest[args.course]:
        p=DATA/rel; data=json.loads(p.read_text(encoding='utf-8'))
        for ep in data: repair(ep,previous); previous=ep
        repair_known_work_duplicates(args.course,data)
        p.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
    print(args.course,'reparado')

if __name__=='__main__':main()
