import json,sys,re,unicodedata,glob,importlib,os,collections
sys.path.insert(0,'tools'); sys.path.insert(0,'tools/v3')
import v3.ova2b as O
for f in sorted(glob.glob('tools/v3/ova2b_241_*.py')): importlib.import_module('v3.'+os.path.basename(f)[:-3])
d=json.load(open('%s/a2_targets_c.json'%sys.argv[1]))
norm=lambda s:re.sub(r'[^a-z0-9]','',unicodedata.normalize('NFKD',s.lower()).encode('ascii','ignore').decode())
use={norm(x) for x in d['obras_em_uso']}
mine={}
bad=0
for t in d['targets']:
    o=O.OVR.get(t['n']); nm=o['ob']['name'] if o and o['ob'] else None
    if not nm: print('SEM OBRA',t['n']);bad+=1;continue
    k=norm(nm)
    if k in use: print('EM USO',t['n'],nm);bad+=1
    if k in mine: print('REPETIDA',t['n'],nm,mine[k]);bad+=1
    mine[k]=t['n']
    if t['n'] not in O.GX: print('SEM G',t['n']);bad+=1
# colisão com obras de outros episódios nas camadas
others=collections.defaultdict(list)
for n,o in O.OVR.items():
    if o['ob'] and n not in {t['n'] for t in d['targets']}: others[norm(o['ob']['name'])].append(n)
for k,n in mine.items():
    if k in others: print('COLIDE com X de outro ep',n,others[k]);bad+=1
print('alvos:',len(d['targets']),'obras distintas:',len(mine),'problemas:',bad)
