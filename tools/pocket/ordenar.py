"""Ordena o Pocket A1 por complexidade gramatical e intercala 'dia a dia' (arcos 1-21) com 'tema' (arcos 22+).
Gera ordem_a1.json (títulos em ordem) e mapa_a1.csv (auditável)."""
import glob,json,re,csv,os,sys
sys.argv=['x']
import importlib.util
spec=importlib.util.spec_from_file_location('b','build.py');src=open('build.py').read().replace('\nmain()','\n')
ns={'__file__':os.path.abspath('build.py')};exec(compile(src,'build.py','exec'),ns)
load=ns['load']
files=sorted(glob.glob('a1_arco*.txt')+glob.glob('a1_arco*.py'))
eps=[]
def fnum(f):return int(re.search(r'arco(\d+)',f).group(1))
for fn in files:
    m=load(fn)
    for k,x in enumerate(m.EPS):
        x['_f']=fnum(fn);x['_k']=k;eps.append(x)
F={
 'cont':(r"\b(am|is|are) \w+ing\b",3),
 'terceira':(r"\b(he|she|it) (?!is\b|has\b|can\b|does\b|was\b)\w+s\b",3),
 'can':(r"\b(can|cannot|can't)\b",2),
 'would':(r"\b(would like|may i|could you|could i)\b",3),
 'there':(r"\bthere (is|are)\b",2),
 'wh':(r"\b(what|where|when|who|which|how (much|many|old|long|far|tall|high))\b",1),
 'dont':(r"\b(do not|does not|don't|doesn't)\b",2),
 'doq':(r"\b(do|does) (you|he|she|they|we|i)\b",1),
 'compar':(r"\b(bigger|cheaper|better|biggest|best|most|more|longer)\b",3),
 'conect':(r"\b(because|but|then|after|before|first|finally)\b",2),
 'imper':(r"^(take|put|go|turn|stand|sit|open|close|look|use|wear|pick|bring|stay|stop|hold|mix|cut|press|move)\b",1),
}
def score(x):
    t=' '.join(l[1] for l in x['dlg'])+' '+x['key'][0]
    t=t.lower();s=0;feat={}
    for k,(p,w) in F.items():
        n=len(re.findall(p,t,re.M))
        feat[k]=n;s+=min(n,3)*w
    words=len(t.split())
    s+=words/18
    return s,feat
for x in eps:x['_s'],x['_feat']=score(x)
odd=sorted([x for x in eps if x['_f']<=21],key=lambda x:(x['_s'],x['_f'],x['_k']))
even=sorted([x for x in eps if x['_f']>=22],key=lambda x:(x['_s'],x['_f'],x['_k']))
res=[];i=j=0
while i<len(odd) or j<len(even):
    ri=(i+.5)/len(odd) if i<len(odd) else 9
    rj=(j+.5)/len(even) if j<len(even) else 9
    if ri<=rj:res.append(('dia a dia',odd[i]));i+=1
    else:res.append(('tema',even[j]));j+=1
N=len(res)
json.dump([x['t'] for _,x in res],open('ordem_a1.json','w'),ensure_ascii=False,indent=0)
with open('mapa_a1.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['ordem','estagio','tipo','titulo','padrao_chave','arco_origem','pontos','vocabulario'])
    for n,(tp,x) in enumerate(res,1):
        w.writerow([n,min(10,(n-1)*10//N+1),tp,x['t'],x['key'][0],x['_f'],round(x['_s'],1),';'.join(v[0] for v in x['vocab'])])
print(N,len(odd),len(even))
