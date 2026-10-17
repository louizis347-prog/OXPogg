const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'}).catch(async()=>chromium.launch());
 const p=await b.newPage({viewport:{width:420,height:900}});
 const errs=[];p.on('pageerror',e=>errs.push('PAGEERR '+e.message));p.on('console',m=>{if(m.type()==='error')errs.push('CONSOLE '+m.text())});
 await p.goto('http://localhost:8765/index.html');await p.waitForTimeout(2500);
 console.log(await p.evaluate(()=>document.body.innerText.slice(0,300)));
 console.log(errs.join('\n'));
 await b.close();
})();
