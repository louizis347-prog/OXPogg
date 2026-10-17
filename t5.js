const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage();
 p.on('pageerror',e=>console.log('PAGEERR',e.message));
 await p.goto('http://localhost:8765/index.html');await p.waitForTimeout(2000);
 await p.evaluate(c=>{const d=document.createElement('button');d.dataset.course=c;document.body.appendChild(d);d.click();},'nb-c1');
 await p.waitForTimeout(2500);
 console.log(await p.evaluate(()=>{const eps=arcSlice('nb-c1',0);const e=eps[0];
   return JSON.stringify({n:eps.length,keys:Object.keys(e),q:(e.q||[]).length,v:(e.v||[]).slice(0,2),dl:e.dl&&Object.keys(e.dl),fr:(e.fr||[]).map(f=>f.k),b:e.b}).slice(0,1500)}));
 await b.close();
})();
