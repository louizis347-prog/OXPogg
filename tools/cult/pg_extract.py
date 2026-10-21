#!/usr/bin/env python3
"""Ferramenta para trechos LITERAIS de obras em domínio público (GITenberg no GitHub raw).
  pg_extract.py probe  REPO ID                 -> acha o arquivo de texto (id.txt, id-0.txt, id-8.txt)
  pg_extract.py grep   REPO ID "palavra" [N]   -> mostra N trechos de contexto onde a palavra aparece
  pg_extract.py extract REPO ID "começo" "fim" -> imprime o trecho EXATO do começo até o fim (parágrafos separados por linha em branco)
REPO é o nome do repositório em github.com/GITenberg (ex.: Pride-and-Prejudice_1342, Pygmalion_3825)."""
import sys,os,re,urllib.request,urllib.error
CACHE='/tmp/pgcache';os.makedirs(CACHE,exist_ok=True)
def norm(t):
    return (t.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('—','--').replace('–','-').replace('﻿',''))
def fetch(repo,pid):
    for fn in ('%s.txt','%s-0.txt','%s-8.txt'):
        fn=fn%pid;cp=os.path.join(CACHE,repo+'__'+fn)
        if os.path.exists(cp):return fn,open(cp,encoding='utf-8',errors='replace').read()
        try:
            r=urllib.request.urlopen('https://raw.githubusercontent.com/GITenberg/%s/master/%s'%(repo,fn),timeout=40)
            t=r.read().decode('utf-8','replace');open(cp,'w',encoding='utf-8').write(t);return fn,t
        except urllib.error.HTTPError: continue
        except Exception as e: continue
    return None,None
def body(t):
    t=norm(t);a=t.find('*** START');b=t.find('*** END')
    if a>=0:t=t[t.find('\n',a)+1:]
    if b>=0 and b>a:t=t[:t.find('*** END')]
    return t
def paras(t):
    return [re.sub(r'\s+',' ',p).strip() for p in re.split(r'\n\s*\n',t) if p.strip()]
if __name__=='__main__':
    c,repo,pid=sys.argv[1],sys.argv[2],sys.argv[3]
    fn,t=fetch(repo,pid)
    if not t:print('NAO ENCONTRADO');sys.exit(1)
    if c=='probe':print('OK',fn,len(t),'caracteres');print(norm(t)[:300].replace('\n',' '))
    elif c=='grep':
        flat=re.sub(r'\s+',' ',body(t));w=sys.argv[4];n=int(sys.argv[5]) if len(sys.argv)>5 else 6
        for m in list(re.finditer(re.escape(w),flat,re.I))[:n]:print('...',flat[max(0,m.start()-160):m.end()+240],'...\n')
    elif c=='extract':
        flat=body(t);ps=paras(flat);full='\n\n'.join(ps);s,e=norm(sys.argv[4]),norm(sys.argv[5])
        fl=re.sub(r'\s+',' ',full);i=fl.find(re.sub(r'\s+',' ',s))
        if i<0:print('COMECO NAO ENCONTRADO');sys.exit(2)
        j=fl.find(re.sub(r'\s+',' ',e),i)
        if j<0:print('FIM NAO ENCONTRADO');sys.exit(3)
        print(fl[i:j+len(e)])
