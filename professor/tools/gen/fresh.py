import sys;sys.path.insert(0,'/home/user/OXPogg/professor/tools')
import vocab_registry as V
r=V.load(); allw=set().union(*r.values())
print('FRESH',[w for w in dict.fromkeys(sys.argv[1:]) if w not in allw])
