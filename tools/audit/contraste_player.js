// Mede o contraste de TODO texto visível do player (quadro a quadro): esconde o texto, lê o fundo real da captura e compara.
// Uso: node tools/audit/contraste_player.js WxH idx curso [maxFrames]   (precisa de `python3 -m http.server 8123` na raiz). Limite: 4,5:1 (3:1 para texto grande).
const {chromium}=require(process.env.PLAYWRIGHT||'/opt/node22/lib/node_modules/playwright');
const [,,vp,idx,cid,mx]=process.argv;const [W,H]=vp.split('x').map(Number);
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:W,height:H}});
await p.goto('http://localhost:8123/app.html');await p.evaluate(()=>{try{sessionStorage.setItem('pogglot:intro','1')}catch(e){}});await p.reload();await p.waitForTimeout(2000);
try{await p.click('text=Agora não',{timeout:1500})}catch(e){}
await p.evaluate(async([c,ix])=>{await ensureLangLoaded(c);if(window.PogBilling)PogBilling.allow=()=>true;play(c,ix)},[cid||'en-a1',+idx]);
await p.addStyleTag({content:'*,*::before,*::after{animation:none!important;transition:none!important}'});await p.waitForTimeout(1800);
const all=[];
for(let i=0;i<(+mx||30);i++){
  const k=await p.evaluate(()=>P.steps[P.i]);
  await p.evaluate(()=>{[...document.querySelectorAll('body *')].forEach(e=>{if(e.children.length===0&&/^Sem voz de texto-para-fala/.test(e.textContent.trim())){let t=e;while(t.parentElement&&t.parentElement.children.length===1&&t.parentElement!==document.body)t=t.parentElement;t.style.display='none'}})});
  // coleta elementos de texto e esconde o texto para ler só o fundo
  const items=await p.evaluate(()=>{
    const out=[],pl=document.getElementById('player');
    const w=document.createTreeWalker(pl,NodeFilter.SHOW_TEXT);const seen=new Set();
    while(w.nextNode()){const n=w.currentNode;if(!n.nodeValue.trim()||!/[A-Za-z0-9]/.test(n.nodeValue))continue;const el=n.parentElement;if(!el||seen.has(el))continue;if(el.tagName==='MARK'||el.closest('[class*=lx-float]'))continue;if(el.querySelector('button,.ps-chip,.dl-p'))continue;if(el.querySelector('button,.ps-chip,.dl-p'))continue;
      const cs=getComputedStyle(el);if(cs.visibility==='hidden'||cs.display==='none'||+cs.opacity===0)continue;
      if(el.closest('svg,script,style,.toast,#toast'))continue;
      const r=document.createRange();r.selectNodeContents(n);const b=r.getBoundingClientRect();if(b.width<4||b.height<4)continue;
      if(b.bottom<0||b.top>innerHeight||b.right<0||b.left>innerWidth)continue;
      const tp=document.elementFromPoint(b.left+b.width/2,b.top+b.height/2);if(!tp||!(el.contains(tp)||tp.contains(el)))continue; /* coberto ou cortado pela rolagem */
      seen.add(el);
      out.push({t:n.nodeValue.trim().slice(0,40),c:cs.color,fs:parseFloat(cs.fontSize),fw:+cs.fontWeight,x:b.left,y:b.top,w:b.width,h:b.height,cls:(el.className&&el.className.baseVal===undefined?String(el.className):'').slice(0,50)+' << '+(()=>{const o=[];for(let e=el.parentElement,d=0;e&&d<4&&e.id!=='player';e=e.parentElement,d++){const c=e.className&&e.className.baseVal===undefined?String(e.className).trim().split(/\s+/)[0]:'';if(c)o.push(c)}return o.join(' < ')})(),tag:el.tagName,op:+cs.opacity});
      el.dataset._c=el.style.color||'';el.style.setProperty('color','transparent','important');el.style.setProperty('text-shadow','none','important');el.style.setProperty('-webkit-text-fill-color','transparent','important');
    }
    return out});
  const shot=await p.screenshot();
  await p.evaluate(()=>{document.querySelectorAll('#player *').forEach(el=>{if('_c' in el.dataset){el.style.removeProperty('color');el.style.removeProperty('text-shadow');el.style.removeProperty('-webkit-text-fill-color');if(el.dataset._c)el.style.color=el.dataset._c;delete el.dataset._c}})});
  const bad=await p.evaluate(async({b64,items,k,i})=>{
    const img=new Image();img.src='data:image/png;base64,'+b64;await img.decode();
    const cv=document.createElement('canvas');cv.width=img.width;cv.height=img.height;const cx=cv.getContext('2d',{willReadFrequently:true});cx.drawImage(img,0,0);
    const sx=img.width/innerWidth,sy=img.height/innerHeight;
    const px=(x,y)=>{x=Math.max(0,Math.min(img.width-1,Math.round(x*sx)));y=Math.max(0,Math.min(img.height-1,Math.round(y*sy)));const d=cx.getImageData(x,y,1,1).data;return [d[0],d[1],d[2]]};
    const lum=([r,g,b])=>{const f=v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)};return .2126*f(r)+.7152*f(g)+.0722*f(b)};
    const cr=(a,b)=>{const A=lum(a),B=lum(b);return (Math.max(A,B)+.05)/(Math.min(A,B)+.05)};
    const out=[];
    for(const it of items){
      const m=it.c.match(/rgba?\(([^)]+)\)/);if(!m)continue;const v=m[1].split(',').map(Number);const fg=v.slice(0,3),al=(v.length>3?v[3]:1)*(it.op);
      const ss=[];for(let a=0;a<6;a++)for(let c2=0;c2<3;c2++)ss.push(px(it.x+it.w*(a+.5)/6,it.y+it.h*(c2+.5)/3));
      ss.sort((p1,p2)=>lum(p1)-lum(p2));const bg=ss[ss.length>>1];
      if(al<.05)continue;const eff=fg.map((f,j)=>Math.round(f*al+bg[j]*(1-al)));
      const ratio=cr(eff,bg);const large=it.fs>=24||(it.fs>=18.66&&it.fw>=700);const need=large?3:4.5;
      if(ratio<need)out.push({frame:i,k,text:it.t,ratio:+ratio.toFixed(2),need,fs:it.fs,cls:it.cls,tag:it.tag,fg:eff.join(','),bg:bg.join(',')});
    }
    return out},{b64:shot.toString('base64'),items,k,i});
  all.push(...bad);
  if(k==='done'||i>=await p.evaluate(()=>P.steps.length))break;
  await p.evaluate(()=>{document.querySelectorAll('.ps-q').forEach(q=>{const o=q.querySelectorAll('.ps-o:not([disabled])');if(o.length)o[0].click()})});await p.waitForTimeout(150);
  await p.evaluate(()=>{const b=document.getElementById('pcta');if(b&&!b.disabled)b.click();else document.getElementById('pskip')&&document.getElementById('pskip').click()});await p.waitForTimeout(700);
}
const g={};for(const o of all){const key=o.cls+'|'+o.tag;(g[key]=g[key]||[]).push(o)}
console.log('textos com contraste baixo:',all.length,'| grupos:',Object.keys(g).length);
for(const [k,v] of Object.entries(g).sort((a,b)=>b[1].length-a[1].length).slice(0,25))console.log(String(v.length).padStart(3),k,'| pior',Math.min(...v.map(x=>x.ratio)),'| ex:',JSON.stringify(v[0].text),'fg',v[0].fg,'bg',v[0].bg,'frame',v[0].k);
await b.close()})();
