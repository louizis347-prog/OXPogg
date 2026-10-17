const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage({viewport:{width:420,height:900}});
 p.on('pageerror',e=>console.log('PAGEERR',e.message,(e.stack||'').split('\n').slice(0,3).join('|')));
 p.on('console',m=>{if(m.type()==='error'&&!/Failed to load resource|bad HTTP/.test(m.text()))console.log('C',m.text().slice(0,200))});
 await p.goto('http://localhost:8765/index.html');await p.waitForTimeout(2500);
 await p.evaluate(()=>document.querySelector('[data-go="comm"]').click());await p.waitForTimeout(1500);
 await p.evaluate(()=>document.querySelector('[data-ct="chat"]').click());await p.waitForTimeout(1500);
 await p.screenshot({path:'comm2.png'});
 console.log((await p.evaluate(()=>document.querySelector('#app').innerText.slice(0,400))).replace(/\n/g,'|'));
 console.log(await p.evaluate(()=>[...document.querySelectorAll('#app input,#app button')].map(e=>e.tagName+'#'+e.id+'.'+e.className+':'+(e.type||'')+':'+(e.innerText||e.placeholder||'').slice(0,25)).join('\n')));
 await b.close();
})();
