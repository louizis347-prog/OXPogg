const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
const ctx=await b.newContext({viewport:{width:1280,height:760},serviceWorkers:'block'});await ctx.addInitScript(()=>localStorage.setItem('pg_prof_ok',String(Date.now())));
const p=await ctx.newPage();const res=[];
for(const n of process.argv.slice(2).map(Number)){const errs=[];const h=e=>errs.push(String(e).slice(0,120));p.on('pageerror',h);
 await p.goto('http://localhost:8765/professor/aula4.html?n='+n);await p.waitForTimeout(1000);let empty=0,steps=0;
 for(let k=0;k<44;k++){const r=await p.evaluate(()=>{const x=document.getElementById('next');if(!x)return -1;x.disabled=false;x.click();return 1});if(r<0)break;await p.waitForTimeout(70);steps++;const e=await p.evaluate(()=>{const b=document.querySelector('.pb');return b?b.innerText.trim().length:-1});if(e<15)empty++}
 res.push([n,steps,empty,errs.length]);p.off('pageerror',h)}
console.log(JSON.stringify(res));await b.close()})()
