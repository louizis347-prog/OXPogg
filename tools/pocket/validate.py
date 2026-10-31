#!/usr/bin/env python3
import json,glob,collections,sys
eps=[]
for f in sorted(glob.glob('../../data/pk-*_*.json')):eps+=json.load(open(f))
bad=[];keys=collections.Counter(e['g']['t'] for e in eps);titles=collections.Counter(e['t'] for e in eps)
print(len(eps),'episódios;',len({e['n'] for e in eps}),'ids únicos')
for k,v in keys.items():
    if v>1:bad.append(('chave repetida',k))
for k,v in titles.items():
    if v>1:bad.append(('título repetido',k))
for e in eps:
    fr=e['fr'];n=e['n']
    if [f['k'] for f in fr]!=['pkhero','pkdlg','pkvoc','pkread','pkbuild','pkspeak','wrap']:bad.append((n,'frames'))
    d=fr[1]
    if not 6<=len(d['lines'])<=10:bad.append((n,'dlg',len(d['lines'])))
    if not any(l[0]=='You' for l in d['lines']):bad.append((n,'sem You'))
    for b in fr[4]['items']:
        if b['en'].count('{')!=b['pt'].count('{') or '{0}' not in b['en']:bad.append((n,'slot',b['en']))
        if len(b['opts'])<2 or any(len(o)!=2 for o in b['opts']):bad.append((n,'opts',b['en']))
    if len(fr[5]['items'])!=2:bad.append((n,'speak'))
    if len(fr[6]['recap'])!=4:bad.append((n,'recap'))
    if len(e['v'])<5:bad.append((n,'vocab'))
    txt=' '.join(l[1].lower() for l in d['lines'])
    miss=[v[0] for v in e['v'] if v[0].lower().split(' ')[0] not in txt]
    if len(miss)>2:bad.append((n,'vocab-fora',miss))
    for l in d['lines']:
        if not l[1].strip() or not l[2].strip():bad.append((n,'linha vazia'))
print(len(bad),'problemas');[print(' ',b) for b in bad[:30]]
