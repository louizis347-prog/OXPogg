const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage();
 await p.goto('http://localhost:8765/index.html');await p.waitForTimeout(2000);
 await p.evaluate(c=>{const d=document.createElement('button');d.dataset.course=c;document.body.appendChild(d);d.click();},'nb-c1');
 await p.waitForTimeout(2500);
 console.log(await p.evaluate(()=>{const e=arcSlice('nb-c1',0)[3];const g=k=>e.fr.find(f=>f.k===k);
   return JSON.stringify({tap:g('nbtap').items[0],tapType:typeof g('nbtap').items,swap:g('nbswap').pages[0],ctx:g('nbctx').items[0],chat:g('nbchat').lines.slice(0,2)}).slice(0,2500)}));
 await b.close();
})();
