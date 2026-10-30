#!/usr/bin/env python3
"""Extrai do sprite Noto (svgmoji-noto, MIT) só os emojis usados no vocabulário Pocket -> data/pk-icons.json {emoji: svg}.
Uso: python3 build_icons.py /caminho/para/package/sprites/all.svg"""
import re,sys,json,os
R=os.path.dirname(os.path.abspath(__file__))
src=open(sys.argv[1],encoding='utf-8').read()
blocks={}
for m in re.finditer(r'<svg [^>]*?\bid="([0-9A-F-]+)"[^>]*>.*?</svg>',src,re.S):blocks[m.group(1).lower()]=m.group(0)
ems=set()
import glob
for p in ''.join(open(f,encoding='utf-8').read().replace('\n','|')+'|' for f in sorted(glob.glob(os.path.join(R,'emoji_*.txt')))).split('|'):
    if ':' in p:ems.add(p.partition(':')[2].strip())
ems|={'🏙️','❓','💬','💡','🙂','🗣️'}
def keys(e):
    cps=[f'{ord(c):04x}' for c in e];a='-'.join(cps);b='-'.join(c for c in cps if c!='fe0f')
    return [a,b,a+'-fe0f',b+'-fe0f']
out={};miss=[]
for i,e in enumerate(sorted(ems)):
    k=next((x for x in keys(e) if x in blocks),None)
    if not k:miss.append(e);continue
    s=blocks[k];pre='e%d'%i
    s=re.sub(r'^(<svg [^>]*?) id="[0-9A-F-]+"',r'\1',s,count=1);s=s.replace(' xml:space="preserve"','')
    s=re.sub(r'id="([^"]+)"',lambda m:'id="%s%s"'%(pre,m.group(1)),s)
    s=re.sub(r'url\(#([^)]+)\)',lambda m:'url(#%s%s)'%(pre,m.group(1)),s)
    s=re.sub(r'href="#([^"]+)"',lambda m:'href="#%s%s"'%(pre,m.group(1)),s)
    s=s.replace('<svg viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg"','<svg viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg"',1)
    def rd(m):
        t=re.sub(r'-?\d+\.\d{2,}',lambda n:('%.1f'%float(n.group(0))).rstrip('0').rstrip('.') or '0',m.group(2));return m.group(1)+t+'"'
    s=re.sub(r'(\b(?:d|points)=")([^"]*)"',rd,s)
    out[e]=s
json.dump(out,open(os.path.join(R,'..','..','data','pk-icons.json'),'w',encoding='utf-8'),ensure_ascii=False,separators=(',',':'))
print(len(out),'ícones;',len(miss),'sem svg',miss[:30],os.path.getsize(os.path.join(R,'..','..','data','pk-icons.json'))//1024,'KB')
