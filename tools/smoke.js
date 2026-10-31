/* Teste de fumaça: sintaxe de todos os scripts + o app precisa montar a home. Usado pelo ship.sh. */
const fs=require('fs'),path=require('path'),http=require('http'),cp=require('child_process'),R=path.resolve(__dirname,'..');
let bad=0;
for(const f of fs.readdirSync(path.join(R,'js')).filter(x=>x.endsWith('.js'))){const r=cp.spawnSync('node',['--check',path.join(R,'js',f)]);if(r.status){console.log('SINTAXE:',f,String(r.stderr).split('\n')[1]||'');bad++}}
for(const h of ['app.html','index.html']){const s=fs.readFileSync(path.join(R,h),'utf8');let i=0;for(const m of s.matchAll(/<script>([\s\S]*?)<\/script>/g)){const t='/tmp/_smoke_'+i++ +'.js';fs.writeFileSync(t,m[1]);const r=cp.spawnSync('node',['--check',t]);if(r.status){console.log('SINTAXE inline:',h,i,String(r.stderr).split('\n')[1]||'');bad++}}}
if(bad){console.log('smoke: FALHOU (sintaxe)');process.exit(1)}
const T={'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml'};
const srv=http.createServer((q,r)=>{let p=decodeURIComponent(q.url.split('?')[0]);const f=path.join(R,p==='/'?'index.html':p);fs.readFile(f,(e,b)=>{if(e){r.writeHead(404);return r.end()}r.writeHead(200,{'content-type':T[path.extname(f)]||'application/octet-stream'});r.end(b)})}).listen(0,async()=>{
 const port=srv.address().port;let chromium;try{chromium=require('playwright').chromium}catch(e){console.log('smoke: playwright ausente, só sintaxe verificada');srv.close();process.exit(0)}
 const b=await chromium.launch();const p=await (await b.newContext({serviceWorkers:'block'})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.route(/cdnjs|googleapis|gstatic/,r=>r.abort());
 await p.goto('http://localhost:'+port+'/app.html');
 let ok=false;for(let i=0;i<30&&!ok;i++){await new Promise(r=>setTimeout(r,500));ok=await p.evaluate(()=>{const a=document.getElementById('app');return !!a&&a.innerText.trim().length>20&&!/Carregando o Pogglot/.test(a.innerText)}).catch(()=>false)}
 await b.close();srv.close();
 if(!ok){console.log('smoke: FALHOU (a home não montou)',errs.slice(0,3));process.exit(1)}
 console.log('smoke: ok');process.exit(0)});
