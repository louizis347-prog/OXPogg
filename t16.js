const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage({viewport:{width:420,height:900}});
 p.on('pageerror',e=>console.log('PAGEERR',e.message,(e.stack||'').split('\n').slice(0,3).join('|')));
 await p.goto('http://localhost:8765/index.html');await p.waitForTimeout(2500);
 await p.evaluate(c=>{const d=document.createElement('button');d.dataset.course=c;document.body.appendChild(d);d.click();},'nb-c1');
 await p.waitForTimeout(3000);
 console.log('p2test count',await p.evaluate(()=>document.querySelectorAll('.p2test').length));
 await p.evaluate(()=>{const t=document.querySelector('.p2test');t.scrollIntoView();t.click()});await p.waitForTimeout(2500);
 console.log((await p.evaluate(()=>document.querySelector('#pstage')?document.querySelector('#pstage').innerText.slice(0,120):'NO PLAYER')).replace(/\n/g,'|'));
 await p.screenshot({path:'mt1.png'});
 await b.close();
})();
