import re,sys
def swap(fn,R):
    s=open(fn).read()
    for w,new in R.items():
        pat=re.compile(r"'"+re.escape(w)+r";[^';]*;[^';]*;[^';]*'")
        m=pat.findall(s)
        if len(m)!=1:print('!',w,len(m));continue
        s=pat.sub("'"+new+"'",s)
    open(fn,'w').write(s)
