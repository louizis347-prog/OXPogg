const { chromium } = require('playwright');
(async()=>{
 const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
 const p=await b.newPage({viewport:{width:420,height:900}});
 p.on('pageerror',e=>console.log('PAGEERR',e.message,(e.stack||'').split('\n').slice(0,3).join('|')));
 p.on('console',m=>{if(m.type()==='error'&&!/Failed to load resource|bad HTTP/.test(m.text()))console.log('C',m.text().slice(0,200))});
 p.on('dialog',d=>{console.log('DIALOG',d.message());d.dismiss()});
 await p.goto('http://localhost:8765/index.html');await p.waitForTimeout(2500);
 await p.evaluate(()=>document.querySelector('[data-go="comm"]').click());await p.waitForTimeout(1200);
 await p.evaluate(()=>document.querySelector('[data-ct="chat"]').click());await p.waitForTimeout(1200);
 await p.evaluate(()=>{const t=[...document.querySelectorAll('#app button')].find(x=>x.innerText.trim()==='Criar conta');t.click()});await p.waitForTimeout(800);
 console.log(await p.evaluate(()=>[...document.querySelectorAll('#app input')].map(e=>e.id+':'+e.type).join(',')));
 await p.fill('#a-email','teste@exemplo.com').catch(()=>{});
 const ids=await p.evaluate(()=>[...document.querySelectorAll('#app input')].map(e=>e.id));
 for(const id of ids){const ty=await p.evaluate(i=>document.getElementById(i).type,id);if(ty==='password')await p.fill('#'+id,'senha123');else if(ty==='text')await p.fill('#'+id,'Teste');}
 await p.evaluate(()=>document.querySelector('#a-go').click());await p.waitForTimeout(2500);
 await p.evaluate(()=>document.querySelector('.pg-room[data-room]').click());await p.waitForTimeout(2000);
 await p.screenshot({path:'comm4.png'});
 console.log('conv:',(await p.evaluate(()=>document.querySelector('#pgchat').innerText.slice(0,300))).replace(/\n/g,'|'));
 console.log(await p.evaluate(()=>[...document.querySelectorAll('#pgchat input,#pgchat textarea,#pgchat button')].map(e=>e.tagName+'#'+e.id+'.'+e.className+':'+(e.innerText||e.placeholder||'').slice(0,20)).join('\n')));
 const ta=await p.$('#pgchat textarea, #pgchat input[type=text]');if(ta){await ta.fill('Hello everyone!');await p.keyboard.press('Enter');await p.waitForTimeout(1500);}
 await p.screenshot({path:'comm5.png'});
 await p.fill('#c-in','Hello again!');await p.click('#c-send');await p.waitForTimeout(1500);console.log('after send:',(await p.evaluate(()=>[...document.querySelectorAll('.pg-msgs')].map(m=>m.innerText.slice(-80)).join('|'))).replace(/\n/g,' '));
 console.log(await p.evaluate(()=>{const r=e=>{const b=document.querySelector(e).getBoundingClientRect();return e+' top '+Math.round(b.top)+' bottom '+Math.round(b.bottom)};return [r('#c-in'),r('#c-send'),r('.pg-nav,nav,#pgnav'),'vh '+innerHeight,'scrollY '+scrollY,'docH '+document.documentElement.scrollHeight].join(' | ')}));
 await p.evaluate(()=>window.scrollTo(0,document.body.scrollHeight));await p.waitForTimeout(500);await p.screenshot({path:'comm6.png'});
 console.log(await p.evaluate(()=>{const b=document.querySelector('#c-in').getBoundingClientRect();const el=document.elementFromPoint(b.left+20,Math.min(b.top+10,innerHeight-2));return 'in top '+Math.round(b.top)+' bottom '+Math.round(b.bottom)+' at point: '+(el&&el.tagName+'.'+el.className)}));
 console.log((await p.evaluate(()=>document.querySelector('#app').innerText.slice(0,500))).replace(/\n/g,'|'));
 await b.close();
})();
