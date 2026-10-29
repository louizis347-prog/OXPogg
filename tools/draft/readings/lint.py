import glob,re,sys
bad=0
for fn in sorted(glob.glob('/home/user/OXPogg/tools/draft/readings/b_*.txt')):
    cur=None
    for i,ln in enumerate(open(fn,encoding='utf-8'),1):
        if ln.startswith('#'):cur=ln.strip();continue
        if ln.startswith('d:'):
            f=[x.strip() for x in ln[2:].split(' // ')]
            if len(f)!=3:print(fn[-12:],i,'campos',ln[:60]);bad+=1;continue
            ce=re.findall(r'\{([^}]*)\}',f[1]);cp=re.findall(r'\{([^}]*)\}',f[2])
            if len(ce)!=len(cp) or any(len(a.split('|'))!=len(b.split('|')) for a,b in zip(ce,cp)):
                print(fn[-12:],i,cur,'chips',f[1][:50],'|',f[2][:50]);bad+=1
        if ln.startswith(('r:','q:')):
            f=ln[2:].split(' // ')
            if ln.startswith('r:') and len(f)!=2:print(fn[-12:],i,'r campos');bad+=1
            if ln.startswith('q:') and len(f)!=6:print(fn[-12:],i,'q campos');bad+=1
print('problemas',bad)
