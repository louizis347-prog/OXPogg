/* Garante contraste mínimo (WCAG AA) para texto escuro sobre fundo claro/pintado: escurece só o necessário. */
(function(){
 var BASE={r:200,g:200,b:200,a:1}; // pior caso estimado do fundo pintado já com o véu claro
 function P(c){var m=c&&c.match(/rgba?\(([^)]+)\)/);if(!m)return null;var a=m[1].split(',').map(parseFloat);return{r:a[0],g:a[1],b:a[2],a:a.length>3?a[3]:1}}
 function lum(c){var f=function(v){v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)};return .2126*f(c.r)+.7152*f(c.g)+.0722*f(c.b)}
 function cr(a,b){var x=lum(a),y=lum(b);return (Math.max(x,y)+.05)/(Math.min(x,y)+.05)}
 function mix(t,b){var a=t.a;return{r:t.r*a+b.r*(1-a),g:t.g*a+b.g*(1-a),b:t.b*a+b.b*(1-a),a:1}}
 function bgOf(el,stage){var layers=[],e=el;
  while(e&&e.nodeType===1&&e!==stage){var cs=getComputedStyle(e);if(cs.backgroundImage&&cs.backgroundImage!=='none')return null;
   var c=P(cs.backgroundColor);if(c&&c.a>0){layers.push(c);if(c.a>=1)break}e=e.parentElement}
  var b=BASE;for(var i=layers.length-1;i>=0;i--)b=mix(layers[i],b);return b}
 function toHsl(c){var r=c.r/255,g=c.g/255,b=c.b/255,mx=Math.max(r,g,b),mn=Math.min(r,g,b),l=(mx+mn)/2,h=0,s=0;
  if(mx!==mn){var d=mx-mn;s=l>.5?d/(2-mx-mn):d/(mx+mn);h=mx===r?(g-b)/d+(g<b?6:0):mx===g?(b-r)/d+2:(r-g)/d+4;h/=6}return{h:h,s:s,l:l}}
 function hue(p,q,t){if(t<0)t+=1;if(t>1)t-=1;return t<1/6?p+(q-p)*6*t:t<.5?q:t<2/3?p+(q-p)*(2/3-t)*6:p}
 function fromHsl(o){var r,g,b;if(o.s===0){r=g=b=o.l}else{var q=o.l<.5?o.l*(1+o.s):o.l+o.s-o.l*o.s,p=2*o.l-q;r=hue(p,q,o.h+1/3);g=hue(p,q,o.h);b=hue(p,q,o.h-1/3)}return{r:Math.round(r*255),g:Math.round(g*255),b:Math.round(b*255),a:1}}
 function fix(root){var stage=document.getElementById('stage');if(!stage)return;var els=root.querySelectorAll('*');
  for(var i=0;i<els.length;i++){var el=els[i];if(el.closest('svg')||el.hasAttribute('data-ct-skip'))continue;
   var t='';for(var k=0;k<el.childNodes.length;k++)if(el.childNodes[k].nodeType===3)t+=el.childNodes[k].textContent;if(t.trim().length<2)continue;
   var cs=getComputedStyle(el);if(cs.visibility==='hidden'||cs.display==='none')continue;
   var fg=P(cs.color);if(!fg||fg.a<.3)continue;var bg=bgOf(el,stage);if(!bg)continue;if(lum(fg)>=lum(bg))continue;
   var fs=parseFloat(cs.fontSize),big=fs>=24||(fs>=18.66&&parseInt(cs.fontWeight)>=700),need=big?3.2:4.7;
   var f0=mix(fg,bg);if(cr(f0,bg)>=need)continue;
   var h=toHsl(fg),n=0;while(n++<40){h.l-=.02;if(h.l<.06)h.l=.06;var c2=fromHsl(h);if(cr(c2,bg)>=need||h.l<=.06){el.style.setProperty('color','rgb('+c2.r+','+c2.g+','+c2.b+')','important');break}}}}
 var tm=0;function run(){clearTimeout(tm);tm=setTimeout(function(){var s=document.getElementById('stage');if(s)fix(s);var d=document.querySelector('.dock .dl');if(d)fix(d.parentNode)},16)}
 function init(){var s=document.getElementById('stage');if(!s){setTimeout(init,300);return}
  new MutationObserver(run).observe(s,{childList:true,subtree:true});run()}
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
