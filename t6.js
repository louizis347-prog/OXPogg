const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage();
 await p.goto('http://localhost:8765/index.html');await p.waitForTimeout(2000);
 await p.evaluate(c=>{const d=document.createElement('button');d.dataset.course=c;document.body.appendChild(d);d.click();},'nb-c1');
 await p.waitForTimeout(2500);
 console.log(await p.evaluate(()=>{const e=arcSlice('nb-c1',0)[3];
   return JSON.stringify(e.fr.map(f=>{const g={...f};for(const k in g){const s=JSON.stringify(g[k]);if(s.length>330)g[k]=s.slice(0,330)+'…'}return g}),null,0)}));
 await b.close();
})();
