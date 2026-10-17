const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage({viewport:{width:420,height:1400}});
 p.on('pageerror',e=>console.log('PAGEERR',e.message,(e.stack||'').split('\n').slice(0,3).join('|')));
 await p.goto('http://localhost:8765/index.html');await p.waitForTimeout(2500);
 await p.evaluate(c=>{const d=document.createElement('button');d.dataset.course=c;document.body.appendChild(d);d.click();},'nb-c1');
 await p.waitForTimeout(3500);
 await p.screenshot({path:'h1.png'});
 console.log(await p.evaluate(()=>[...document.querySelectorAll('#app button,#app a')].slice(0,30).map(e=>e.className+'|'+(e.dataset.course||e.dataset.ep||e.dataset.test||e.dataset.go||'')+'|'+e.innerText.slice(0,30).replace(/\n/g,' ')).join('\n')));
 await b.close();
})();
