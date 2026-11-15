import sys;sys.path.insert(0,'/home/user/OXPogg/professor/tools')
import vocab_registry as V
reg=V.load()
def used(n):
    u=set()
    for m,ws in reg.items():
        if m!=n and V.order(m)<V.order(n): u|=ws
    return u
if __name__=='__main__':
    n=int(sys.argv[1]);u=used(n)
    for w in sys.argv[2:]: print(w,'USED' if w in u else '-',end='; ')
