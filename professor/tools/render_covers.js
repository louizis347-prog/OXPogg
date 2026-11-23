/* Gera professor/img/cover/NNN.jpg com a arte de capa de cada aula (cenário + personagens). Uso: node professor/tools/render_covers.js [de] [ate] */
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const A=+process.argv[2]||1,B=+process.argv[3]||4500;const BASE=process.env.BASE||'http://localhost:8765';const FORCE=!!process.env.FORCE;
const pad=n=>String(n).padStart(3,'0');
/* mesmo nome que o painel (index.html) espera */
const coverName=n=>n>=4000?'B2-'+pad(n-4000):n>=3000?'B1-'+pad(n-3000):n>=2000?'A2-'+pad(n-2000):n>=1000?pad(n-1000)+' +':pad(n);const OUT=path.join(__dirname,'..','img','cover');fs.mkdirSync(OUT,{recursive:true});
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:760,height:430},deviceScaleFactor:1});
await p.addInitScript(()=>{try{localStorage.setItem('pg_prof_ok',String(Date.now()))}catch(e){}});
await p.goto(BASE+'/professor/aula4.html?n=1');await p.waitForTimeout(2500);
await p.evaluate(()=>{document.body.innerHTML='<div id="cv" class="q1v" style="width:640px;height:360px;position:fixed;left:10px;top:10px;overflow:hidden;border-radius:0"></div>';document.body.className='quest-l1'});
let done=0,skip=0;for(let n=A;n<=B;n++){const out=path.join(OUT,coverName(n)+'.jpg');if(!FORCE&&fs.existsSync(out)){skip++;continue}const f=path.join(__dirname,'..','data','v4',String(n).padStart(3,'0')+'.json');if(!fs.existsSync(f))continue;
 const L=JSON.parse(fs.readFileSync(f,'utf8'));const pg=L.pages.find(x=>x.art&&(x.art.rs||x.art.pair))||L.pages[0];
 await p.evaluate(a=>{const art=a.pair?a.pair[1]:a;document.getElementById('cv').innerHTML='<div class="q1v-hero" style="width:100%;height:100%;border:0;border-radius:0;box-shadow:none">'+window.L1VIS.stage(Object.assign({},art,{cast:(art.cast||[]).slice(0,2)}),'cover')+'</div>'},pg.art);
 await p.waitForTimeout(120);
 await p.locator('#cv').screenshot({path:out,type:'jpeg',quality:80});if(++done%100===0)console.log('capas geradas:',done,'(até a aula',n+')');}
await b.close();console.log('ok · geradas',done,'· já existiam',skip)})();
