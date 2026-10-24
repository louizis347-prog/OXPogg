/* Five-episode art direction; preserves lessons, IDs, progression and audio. */
(function(){
'use strict';
let stage=null,observer=null,queued=false,artId=0;
// Add modeled light to the current illustrated cast without replacing their identities.
function refineArt(svg){
 if(svg.dataset.pilotRefined)return;svg.dataset.pilotRefined="true";
 const ns="http://www.w3.org/2000/svg",defs=document.createElementNS(ns,"defs"),colors=new Map();
 svg.querySelectorAll("[fill]").forEach(shape=>{
  const color=shape.getAttribute("fill");if(!/^#[0-9a-f]{6}$/i.test(color))return;
  let id=colors.get(color);
  if(!id){id="pilot-light-"+(++artId);colors.set(color,id);
   const gradient=document.createElementNS(ns,"linearGradient");
   gradient.id=id;gradient.setAttribute("x1","0");gradient.setAttribute("y1","0");gradient.setAttribute("x2",".8");gradient.setAttribute("y2","1");
   [["0%",.12],["45%",0],["100%",-.14]].forEach(([offset,mix])=>{
    const stop=document.createElementNS(ns,"stop");stop.setAttribute("offset",offset);
    const channels=[1,3,5].map(i=>parseInt(color.slice(i,i+2),16));
    stop.setAttribute("stop-color","#"+channels.map(c=>Math.round(mix>0?c+(255-c)*mix:c*(1+mix)).toString(16).padStart(2,"0")).join(""));gradient.append(stop);
   });defs.append(gradient);
  }shape.setAttribute("fill","url(#"+id+")");
 });svg.prepend(defs);
}

function apply(){
 queued=false;
 const player=document.getElementById('player');
 if(!player||typeof P==='undefined'||!P)return;
 const active=(P.cid==='en-a1'||P.cid==='en-a2'||P.cid==='es-a1'||P.cid==='frbr-a1'||P.cid==='pt-a1'||P.cid==='it-a1'||P.cid==='de-a1')&&P.e&&P.e.presentation==='regular-pilot-v1';
 player.classList.toggle('regular-pilot',active);
 const bubble=document.getElementById('pbub');
 if(bubble){bubble.tabIndex=0;bubble.setAttribute('aria-label','Orientação do Pog');}
 if(!active){if(observer)observer.disconnect();observer=null;stage=null;return;}
 if(!window.PogFace||!PogFace.portrait)return;
 const st=document.getElementById('pstage');if(!st)return;
 const f=P.e.fr[P.i];if(!f)return;
 function put(host,name){
  if(!host||!name||host.dataset.pilotName===name)return;
  const svg=PogFace.portrait(P.e,name);if(!svg)return;
  host.dataset.pilotName=name;host.classList.add('pilot-portrait');host.innerHTML=svg;
  host.setAttribute('role','img');host.setAttribute('aria-label',name);
 }
 st.querySelectorAll('.ps-ch').forEach(refineArt);
 st.querySelectorAll('.fx-av').forEach(x=>put(x.querySelector('span'),x.dataset.n));
 st.querySelectorAll('.fx-line').forEach(x=>put(x.querySelector('.fx-lav'),x.querySelector('.fx-bub b')?.textContent));
 st.querySelectorAll('.vb-say').forEach(x=>put(x.querySelector('.vb-av'),x.dataset.w||x.querySelector('.vb-bub>b')?.textContent));
 if(f.cast?.npc){
  put(st.querySelector('.td-av'),f.cast.npc[2]);
  st.querySelectorAll('.td-h').forEach(x=>put(x.querySelector(':scope>span'),(x.classList.contains('r')?f.cast.you:f.cast.npc)?.[2]));
 }
 if(stage!==st){
  if(observer)observer.disconnect();stage=st;
  observer=new MutationObserver(()=>{if(!queued){queued=true;requestAnimationFrame(apply)}});
  observer.observe(st,{childList:true,subtree:true});
 }
}
if(typeof window.render==='function'){
 const render=window.render;
 window.render=function(){const value=render.apply(this,arguments);apply();return value;};
}
window.RegularPilot={refresh:apply};
})();
