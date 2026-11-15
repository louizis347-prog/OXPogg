import sys;sys.path.insert(0,'/home/user/OXPogg/professor/tools')
import vocab_registry as r
reg=r.load();n=int(sys.argv[1])
used=set()
for m,ws in reg.items():
    if m!=n and r.order(m)<r.order(n): used|=ws
print(' '.join(w+(':USED' if w in used else ':ok') for w in sys.argv[2:]))
