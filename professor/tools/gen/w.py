import sys;sys.path.insert(0,'/home/user/OXPogg/professor/tools')
import vocab_registry as R
reg=R.load();used={}
for n,ws in reg.items():
    if R.order(n)<R.order(int(sys.argv[1])):
        for w in ws: used.setdefault(w,[]).append(n)
for w in sys.argv[2:]: print(w, 'USED' if w in used else 'free')
