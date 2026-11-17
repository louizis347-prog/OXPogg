#!/bin/bash
# uso: tools/finish.sh 1002 1003 ... — constrói, escolhe o cenário pintado e aplica o padrão novo
cd "$(dirname "$0")/.." || exit 1
for n in "$@"; do python3 src/build_v5.py $n | tail -1; done
python3 - "$@" <<'PY'
import json,sys
out=[]
for n in sys.argv[1:]:
    d=json.load(open('data/v4/%03d.json'%int(n)));w=[p for p in d['pages'] if p.get('kind')=='work'][0]['work']['title']
    out.append({'n':int(n),'t':d['title'],'w':w,'rs':d.get('scene')})
json.dump(out,open('/tmp/_pl.json','w'))
PY
cat > /tmp/_pick.js <<'JS'
const {chromium}=require('/opt/node22/lib/node_modules/playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({serviceWorkers:'block'});await p.goto('http://localhost:8765/app.html');await p.waitForTimeout(1500);
const L=JSON.parse(fs.readFileSync('/tmp/_pl.json'));
const r=await p.evaluate(L=>{const o={};L.forEach(x=>{const e={n:3000+x.n,uid:'pro'+x.n,t:x.t,a:{w:x.w}};const k=PogPaint.pick(x.rs,e);o[x.n]=k?{name:k.name.replace('-night','-gold'),flip:k.flip,hue:k.hue,theme:k.theme}:null});return o},L);
const f='data/paint.json';const P=JSON.parse(fs.readFileSync(f));Object.assign(P,r);fs.writeFileSync(f,JSON.stringify(P));await b.close()})()
JS
curl -s -o /dev/null localhost:8765/ || { echo "inicie o servidor: python3 -m http.server 8765"; exit 1; }
NODE_PATH=$(npm root -g) node /tmp/_pick.js 2>&1 | tail -2
python3 tools/enrich_v6.py
