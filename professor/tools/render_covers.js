/* Gera professor/img/cover/NNN.jpg com a arte de capa de cada aula (cenário + personagens). Uso: node professor/tools/render_covers.js [de] [ate] */
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const A=+process.argv[2]||1,B=+process.argv[3]||200;const OUT=path.join(__dirname,'..','img','cover');fs.mkdirSync(OUT,{recursive:true});
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:760,height:430},deviceScaleFactor:1});
await p.addInitScript(()=>{try{localStorage.setItem('pg_prof_ok',String(Date.now()))}catch(e){}});
await p.goto('http://localhost:8765/professor/aula4.html?n=1');await p.waitForTimeout(2500);
await p.evaluate(()=>{document.body.innerHTML='<div id="cv" class="q1v" style="width:640px;height:360px;position:fixed;left:10px;top:10px;overflow:hidden;border-radius:0"></div>';document.body.className='quest-l1'});
for(let n=A;n<=B;n++){const f=path.join(__dirname,'..','data','v4',String(n).padStart(3,'0')+'.json');if(!fs.existsSync(f))continue;
 const L=JSON.parse(fs.readFileSync(f,'utf8'));const pg=L.pages.find(x=>x.art&&(x.art.rs||x.art.pair))||L.pages[0];
 await p.evaluate(a=>{const art=a.pair?a.pair[1]:a;document.getElementById('cv').innerHTML='<div class="q1v-hero" style="width:100%;height:100%;border:0;border-radius:0;box-shadow:none">'+window.L1VIS.stage(Object.assign({},art,{cast:(art.cast||[]).slice(0,2)}),'cover')+'</div>'},pg.art);
 await p.waitForTimeout(120);
 await p.locator('#cv').screenshot({path:path.join(OUT,String(n).padStart(3,'0')+'.jpg'),type:'jpeg',quality:80});}
await b.close();console.log('ok')})();
