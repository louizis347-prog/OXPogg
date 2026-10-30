/* Neighbors (inglês A1, episódios 1–10): quadro cheio, bordas inteiras, faixa de cena em cada quadro.
   Só liga a classe .nb-full no #player; todo o resto está em css/nbfull.css. */
(function(){
  const N=10;
  function tick(){
    const pl=document.getElementById('player');if(!pl)return;
    let on=false,e=null;
    try{if(typeof P!=='undefined'&&P&&P.cid==='nb-a1'&&P.e){e=P.e;on=(P.idx!=null?P.idx:(P.ix!=null?P.ix:0))<N||(e.n>=90001&&e.n<90001+N)}}catch(x){}
    pl.classList.toggle('nb-full',on);
    if(!on)return;
    const st=document.querySelector('#pstage .step.nbx,#pstage .step.nbo');if(!st||st.dataset.nbf||st.classList.contains('nbscene')||st.querySelector('.nbf-scene,.nb-poster'))return;
    if([...st.querySelectorAll('svg,img,canvas')].some(x=>{const r=x.getBoundingClientRect();return r.height>=90&&r.width>=160}))return;
    try{if(window.PogCover&&e){const d=document.createElement('div');d.className='nbf-scene';d.setAttribute('aria-hidden','true');d.innerHTML=PogCover.svg(e,{full:true});st.dataset.nbf='1';st.insertBefore(d,st.firstChild);
      const pb=document.getElementById('pbody');
      /* se a faixa fizer o quadro estourar (e virar "Ver mais"), ela sai */
      if((pb&&pb.scrollHeight>pb.clientHeight+2)||st.scrollHeight>st.clientHeight+2){d.remove()}}}catch(x){}
  }
  setInterval(tick,250);
})();
