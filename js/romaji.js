/* Pogglot · romaji automático em todas as telas dos episódios de japonês (Hepburn), em cor viva.
 * Converte hiragana/katakana (e as poucas palavras com kanji do curso) e acrescenta a leitura abaixo de cada texto japonês. */
(function(){
'use strict';
var B={あ:'a',い:'i',う:'u',え:'e',お:'o',か:'ka',き:'ki',く:'ku',け:'ke',こ:'ko',さ:'sa',し:'shi',す:'su',せ:'se',そ:'so',た:'ta',ち:'chi',つ:'tsu',て:'te',と:'to',な:'na',に:'ni',ぬ:'nu',ね:'ne',の:'no',
 は:'ha',ひ:'hi',ふ:'fu',へ:'he',ほ:'ho',ま:'ma',み:'mi',む:'mu',め:'me',も:'mo',や:'ya',ゆ:'yu',よ:'yo',ら:'ra',り:'ri',る:'ru',れ:'re',ろ:'ro',わ:'wa',を:'o',ん:'n',
 が:'ga',ぎ:'gi',ぐ:'gu',げ:'ge',ご:'go',ざ:'za',じ:'ji',ず:'zu',ぜ:'ze',ぞ:'zo',だ:'da',ぢ:'ji',づ:'zu',で:'de',ど:'do',ば:'ba',び:'bi',ぶ:'bu',べ:'be',ぼ:'bo',ぱ:'pa',ぴ:'pi',ぷ:'pu',ぺ:'pe',ぽ:'po',ゔ:'vu',
 ぁ:'a',ぃ:'i',ぅ:'u',ぇ:'e',ぉ:'o'};
var CB={きゃ:'kya',きゅ:'kyu',きょ:'kyo',しゃ:'sha',しゅ:'shu',しょ:'sho',ちゃ:'cha',ちゅ:'chu',ちょ:'cho',にゃ:'nya',にゅ:'nyu',にょ:'nyo',ひゃ:'hya',ひゅ:'hyu',ひょ:'hyo',みゃ:'mya',みゅ:'myu',みょ:'myo',りゃ:'rya',りゅ:'ryu',りょ:'ryo',
 ぎゃ:'gya',ぎゅ:'gyu',ぎょ:'gyo',じゃ:'ja',じゅ:'ju',じょ:'jo',びゃ:'bya',びゅ:'byu',びょ:'byo',ぴゃ:'pya',ぴゅ:'pyu',ぴょ:'pyo',
 ふぁ:'fa',ふぃ:'fi',ふぇ:'fe',ふぉ:'fo',てぃ:'ti',でぃ:'di',うぃ:'wi',うぇ:'we',うぉ:'wo',ゔぁ:'va',ゔぃ:'vi',ゔぇ:'ve',ゔぉ:'vo',しぇ:'she',じぇ:'je',ちぇ:'che'};
var KANJI={非常口:'hijōguchi',入口:'iriguchi',出口:'deguchi',時間:'jikan',円:'en',手:'te',水:'mizu',駅:'eki'};
var PUN={'。':'.','、':',','！':'!','？':'?','「':'“','」':'”','『':'“','』':'”','・':' · ','〜':'~','…':'…','　':' '};
function kata2hira(s){return s.replace(/[ァ-ヶ]/g,function(c){return String.fromCharCode(c.charCodeAt(0)-0x60)})}
var HAS=/[぀-ヿ一-鿿]/;
function conv(src){
  var s=String(src||''),k,out='';
  Object.keys(KANJI).sort(function(a,b){return b.length-a.length}).forEach(function(w){s=s.split(w).join('\u0001'+KANJI[w]+'\u0002')});
  s=kata2hira(s).replace(/(です|でした|ます)か/g,'$1 か').replace(/(でした|です|ください|ございます)/g,' $1').replace(/^ /,'');
  var chars=Array.from(s),i=0,geminate=false,toks=[],cur='';
  function push(r){if(geminate&&r){r=(r.charAt(0)==='c'&&r.charAt(1)==='h'?'t':r.charAt(0))+r;geminate=false}cur+=r}
  while(i<chars.length){var c=chars[i],two=c+(chars[i+1]||'');
    if(c==='\u0001'){var j=chars.indexOf('\u0002',i);push(chars.slice(i+1,j).join(''));i=j+1;continue}
    if(CB[two]){push(CB[two]);i+=2;continue}
    if(c==='っ'){geminate=true;i++;continue}
    if(c==='ー'){var m=/[aiueo]$/.exec(cur);if(m){var mac={a:'ā',i:'ī',u:'ū',e:'ē',o:'ō'}[m[0]];cur=cur.slice(0,-1)+mac}i++;continue}
    if(c==='ん'){var nx=chars[i+1],nr=nx?(B[nx]||''):'';push((nx!=='を'&&/^[aiueoy]/.test(nr))?"n'":'n');i++;continue}
    if(c==='は'||c==='へ'){var nxt=chars[i+1],endTok=!nxt||/[\s。、！？,.!?]/.test(nxt);
      if(endTok){var kw=/(konnichi|konban)$/.test(cur);push(c==='は'?(kw?'wa':' wa'):(kw?'e':' e'));i++;continue}}
    if(c==='を'){push(' o');i++;continue}
    if(B[c]){push(B[c]);i++;continue}
    if(PUN[c]!==undefined){toks.push(cur);cur='';toks.push(PUN[c]);i++;continue}
    if(/\s/.test(c)){toks.push(cur);cur='';toks.push(' ');i++;continue}
    if(HAS.test(c)){return null}   /* kanji desconhecido: sem romaji automático */
    push(c);i++}
  toks.push(cur);
  out=toks.join('').replace(/ou/g,'ō').replace(/uu/g,'ū').replace(/\s+/g,' ').replace(/\s([.,!?”])/g,'$1').replace(/([.,!?])(?=[A-Za-zāīūēō])/g,'$1 ').trim();
  return out}
var ZONE='#pstage',SKIP='script,style,input,textarea,select,.nb-rj,.nb-rj2,.nb-find,.nb-grid,.nb-ws,.nb-words,.kx,[data-norj],.nb-tools,svg,canvas,.pog-dock,.bubble';
var seen=new WeakSet(),busy=false;
function isJa(){try{return typeof P!=='undefined'&&P&&P.c&&/^ja/.test(P.c.tts||'')}catch(e){return false}}
function pass(){busy=false;if(!isJa())return;var st=document.querySelector(ZONE);if(!st)return;
  var w=document.createTreeWalker(st,NodeFilter.SHOW_TEXT,null),n,list=[];
  while((n=w.nextNode())){if(seen.has(n))continue;var t=n.nodeValue;if(!t||!HAS.test(t))continue;var p=n.parentElement;if(!p||p.closest(SKIP))continue;list.push(n)}
  list.forEach(function(n){seen.add(n);var p=n.parentElement,box=p.closest('.nb-b,.nb-big-line,.nb-sp');
    if(box&&box.querySelector('.nb-rj,.nb-rj2'))return;                    /* já tem a leitura do conteúdo */
    var r=conv(n.nodeValue);if(!r)return;
    var em=document.createElement('em');em.className='nb-rj nb-auto';em.textContent=r;
    var host=p;if(p.tagName==='BUTTON'||p.tagName==='SPAN'||p.tagName==='B'||p.tagName==='EM'||p.tagName==='LABEL'||p.tagName==='DIV'||p.tagName==='P'||p.tagName==='LI'||p.tagName==='STRONG')host=p;
    n.parentNode.insertBefore(em,n.nextSibling)})}
function sched(){if(busy)return;busy=true;(window.requestAnimationFrame||setTimeout)(pass)}
function boot(){try{new MutationObserver(function(ms){for(var i=0;i<ms.length;i++){var t=ms[i].target;if(t&&t.nodeType===1&&t.classList&&t.classList.contains('nb-auto'))continue;sched();return}}).observe(document.body,{childList:true,subtree:true})}catch(e){}}
window.PogRomaji={conv:conv,pass:pass};
if(document.body)boot();else document.addEventListener('DOMContentLoaded',boot);
})();
