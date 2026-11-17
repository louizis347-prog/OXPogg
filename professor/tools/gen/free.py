import sys;sys.path.insert(0,'/home/user/OXPogg/professor/tools')
import vocab_registry as V
reg=V.load();used=set().union(*[s for k,s in reg.items() if k<1096])
print(' '.join(w for w in sys.stdin.read().split() if w not in used))
