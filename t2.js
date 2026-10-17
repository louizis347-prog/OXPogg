const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage({viewport:{width:420,height:900}});
 const errs=[];p.on('pageerror',e=>errs.push('PAGEERR '+e.message));
 p.on('response',r=>{if(r.status()>=400)errs.push('HTTP '+r.status()+' '+r.url())});
 await p.goto('http://localhost:8765/index.html');await p.waitForTimeout(2000);
 console.log(await p.evaluate(()=>[...document.querySelectorAll('button,a,[data-lang],[data-course]')].map(e=>(e.dataset.lang||e.dataset.course||'')+'|'+e.innerText.trim().slice(0,30)).slice(0,40).join('\n')));
 console.log([...new Set(errs)].slice(0,10).join('\n'));
 await b.close();
})();
