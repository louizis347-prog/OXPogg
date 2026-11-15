import sys;sys.path.insert(0,'/home/user/OXPogg/professor/tools')
import vocab_registry as V
reg=V.load()
for w in sys.argv[1:]:
    hits=[k for k,s in reg.items() if w in s and k<1096]
    print(w,'USED' if hits else 'free',hits[:3])
