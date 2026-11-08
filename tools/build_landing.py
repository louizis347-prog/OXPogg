#!/usr/bin/env python3
"""Junta e minifica o CSS da landing em css/landing.bundle.css (uma requisição em vez de sete).
Ordem = ordem original de carregamento (a cascata não muda), com landing-light.css por último.
Uso: python3 tools/build_landing.py"""
import re,os
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
ORDER=['tokens','landing','home-art','landing-new','landing-teacher','landing-wow','landing-pro','landing-connect','landing-light']
def mini(s):
    s=re.sub(r'/\*.*?\*/','',s,flags=re.S)
    s=re.sub(r'\s+',' ',s)
    s=re.sub(r'\s*([{};])\s*',r'\1',s)
    s=s.replace(';}','}')
    return s.strip()
out=[];tot=0
for n in ORDER:
    t=open(os.path.join(R,'css',n+'.css'),encoding='utf-8').read();tot+=len(t.encode());out.append(mini(t))
b='\n'.join(out)
open(os.path.join(R,'css','landing.bundle.css'),'w',encoding='utf-8').write(b)
print('pacote: %d bytes (de %d em %d arquivos)'%(len(b.encode()),tot,len(ORDER)))
