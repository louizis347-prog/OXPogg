#!/usr/bin/env python3
"""Audit the regular-course episode script supplied by the editor.

English regular courses are intentionally excluded from mutation and from this
report's selected set. The audit checks structure and obvious editorial defects;
it does not pretend to judge whether a translated sentence is idiomatic.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
ORDER = ['cover','review','hotscene','pgscene','pgsheet','pgrule','pgmold','pgsheet','verbs','vplay','pgexp','pgscene','pgsheet','pgsheet','pglab','pgsheet','pgspeak','pgmission','wrap']
WORD = re.compile(r"\s|/")
FILLER = re.compile(r"^(Good\.?|Coffee\??|Please\.?|Here\.?|Okay\.?|Bom\.?|Café\??|Por favor\.?)$", re.I)


def load(manifest, course):
    out=[]
    for rel in manifest[course]:
        out.extend(json.loads((DATA/rel).read_text(encoding='utf-8')))
    return out


def audit(course, episodes):
    failures=[]; works=Counter(); previous=None
    for ordinal,e in enumerate(episodes,1):
        label=f'{course}:{e.get("n")}'
        fr=e.get('fr') or []; kinds=[x.get('k') for x in fr]
        if e.get('presentation')!='regular-pilot-v1': failures.append((label,'presentation'))
        if ordinal>1 and kinds!=ORDER: failures.append((label,'ordem dos quadros'))
        if len(e.get('v') or [])!=6: failures.append((label,'vocabulário != 6'))
        if any(WORD.search(str(x[0])) for x in (e.get('v') or []) if isinstance(x,list) and x): failures.append((label,'vocabulário contém frase'))
        by={}
        for x in fr: by.setdefault(x.get('k'),[]).append(x)
        if len((by.get('hotscene') or [{}])[0].get('hot') or [])!=5: failures.append((label,'hotscene != 5 objetos'))
        if len((by.get('pgmold') or [{}])[0].get('pages') or [])!=3: failures.append((label,'molde != 3 páginas'))
        scenes=by.get('pgscene') or []
        if len(scenes)!=2 or len(scenes[0].get('lines') or [])<8: failures.append((label,'cena 1 curta'))
        minimum=6 if course.rsplit('-',1)[-1] in ('a1','a2') else 8
        if len(scenes)!=2 or len(scenes[1].get('lines') or [])<minimum: failures.append((label,'cena 2 curta'))
        if any(FILLER.match(str(line[1]).strip()) for scene in scenes for line in scene.get('lines') or [] if isinstance(line,list) and len(line)>1): failures.append((label,'fala de enchimento'))
        if len((by.get('verbs') or [{}])[0].get('items') or [])!=4: failures.append((label,'verbos != 4'))
        if len((by.get('pgexp') or [{}])[0].get('items') or [])!=4: failures.append((label,'expressões != 4'))
        lab=(by.get('pglab') or [{}])[0]
        if len(lab.get('ex') or [])!=3 or len(lab.get('rounds') or [])!=3: failures.append((label,'laboratório != 3+3'))
        if len((by.get('pgspeak') or [{}])[0].get('items') or [])!=5: failures.append((label,'fala guiada != 5'))
        missions=(by.get('pgmission') or [{}])[0].get('missions') or []
        if len(missions)!=3 or not str(missions[0].get('name','')).lower().startswith('cena da obra'): failures.append((label,'missões inválidas'))
        if ordinal>1:
            review=fr[1] if len(fr)>1 else {}
            if review.get('k')!='review': failures.append((label,'mochila ausente'))
            elif len(review.get('bag') or [])!=5: failures.append((label,'mochila sem 5 bolsos'))
        cover=by.get('cover',[{}])[0]
        if 'em 10 minutos' not in str(cover.get('sub','')).lower(): failures.append((label,'capa sem em 10 minutos'))
        if not (e.get('a') or {}).get('w'): failures.append((label,'obra ausente'))
        else: works[(e.get('a') or {}).get('w')]+=1
        previous=e
    for work,count in works.items():
        if count>1: failures.append((course,f'obra repetida: {work} ({count}x)'))
    return failures


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--course',action='append'); ap.add_argument('--json')
    args=ap.parse_args(); manifest=json.loads((DATA/'manifest.json').read_text(encoding='utf-8'))
    selected=args.course or [c for c in manifest if not c.startswith('nb') and not c.startswith('en-')]
    report={}
    for c in selected:
        failures=audit(c,load(manifest,c)); report[c]={'failures':failures}
        print(f'{c}: {len(failures)} falhas')
    if args.json: Path(args.json).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    return 1 if any(x['failures'] for x in report.values()) else 0


if __name__=='__main__': raise SystemExit(main())
