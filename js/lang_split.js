/* Pogglot · áudio bilíngue
   O Poggie (e várias telas) falam textos que misturam o idioma da aula e o idioma do aluno
   ("Use **come up with** para falar de uma ideia."). Com uma única voz a frase fica errada.
   PogLang.plan(texto, idiomaPedido) devolve a lista de trechos [{t, lang}] já com o idioma certo,
   ou {single} quando o texto inteiro é de um só idioma (corrige também o idioma pedido errado). */
(function(){
const W=s=>new Set(s.split(/\s+/).filter(Boolean));
const STOP={
 en:W("the an and or but of to in on at for with from by about into over after before is are was were be been being am do does did have has had will would can could should must may might i you he she it we they him her us them my your his its our their this that these those there here what when where who why how which not yes if then than so as just very too also only all some any one more most much many every each other another again now today tomorrow yesterday please thanks hello let's don't doesn't didn't isn't aren't wasn't won't can't i'm it's that's there's you're we're they're i've i'll i'd who's what's"),
 pt:W("o os as um uma uns umas de do da dos das em nos nas por para pra com sem sobre entre até e ou mas que se não sim é são era foi ser estar está estão estou tem tinha tenho têm há vai vou vamos pode posso podem deve eu tu você vocês ele ela eles elas nós te lhe meu minha seu sua seus suas nosso nossa isso isto esse essa este esta aquele aquela aqui ali lá aí como quando onde quem porque porquê qual quais mais menos muito muita muitos pouco já ainda também só apenas agora hoje amanhã ontem depois antes então assim cada todo toda todos todas outro outra ouça toque escolha veja clique responda use observe diga fale leia escreva hora verbo frase palavra expressão episódio aula ao aos à às pelo pela pelos pelas num numa quer fazer faz foram ficar fica fique dá dar dê vez vezes coisa coisas muito bem tudo nada algo alguém ninguém seguir siga continue complete conecte"),
 es:W("el la los las un una unos unas de del en con por para que y o pero no sí es son está están estoy tengo tiene hay voy vamos puede yo tú usted él ella nosotros mi tu su esto eso este esta aquí allí cómo cuándo dónde quién porque más menos muy ya también solo ahora hoy mañana ayer después antes entonces así todo todos otro escucha elige toca mira haz"),
 fr:W("le la les un une des de du en dans avec pour que et ou mais ne pas oui est sont suis ai avez je il elle nous vous ils elles mon ma mes ton son sa ce cette ces ici là comment quand où qui pourquoi plus moins très déjà aussi seulement maintenant aujourd'hui demain hier après avant alors tout tous autre écoute choisis touche"),
 de:W("der die das den dem ein eine und oder aber nicht ja nein ist sind bin habe hat haben ich du er es wir ihr mein dein sein dies hier dort wie wann wo wer warum mehr weniger sehr schon auch nur jetzt heute morgen gestern nach vor dann alle andere mit für von zu auf im höre wähle"),
 it:W("il lo la gli le un una di del della in con per che e o ma non sì è sono ho ha abbiamo io tu lui lei noi voi loro mio tuo suo questo questa qui là come quando dove chi perché più meno molto già anche solo ora oggi domani ieri dopo prima allora tutto tutti altro ascolta scegli tocca")
};
const AMBIG=new Set(['a','e','me','no','as','se','so','la','le','i','in','es','son','sa','ha','y','un','una','der','die','das','den','dem','ein','eine','nos','te','el','en','de','du','ce','pas','est']);
const code=l=>String(l||'').slice(0,2).toLowerCase();
const CJK=/[぀-ヿ㐀-鿿豈-﫿가-힯]/;
function guess(tok,T,H){
  const raw=tok.replace(/\*\*/g,'');
  const w=raw.toLowerCase().replace(/^[^\p{L}']+|[^\p{L}']+$/gu,'').replace(/’/g,"'");
  if(!w)return null;
  if(CJK.test(w)) return (T==='ja'||T==='zh'||T==='ko')?'T':null;
  if((H==='pt'&&/[ãõç]/.test(w))||(H==='es'&&/[ñ¿¡]/.test(w)))return 'H';
  const inT=STOP[T]&&STOP[T].has(w),inH=STOP[H]&&STOP[H].has(w);
  if(inT&&inH)return null;
  if(inT){ if(AMBIG.has(w)&&T!=='en')return null; return 'T'}
  if(inH){ if(AMBIG.has(w)&&H!=='pt')return null; return 'H'}
  return null;
}
function plan(text,hint,opts){
  opts=opts||{};
  const target=code(opts.target||hint),home=code(opts.home||'pt');
  const src=String(text||'');
  if(!src.trim()||target===home)return null;
  const toks=[];                         /* {s, lang, strong} */
  let inBold=false,inQuote=false;
  src.split(/\s+/).filter(Boolean).forEach(piece=>{
    let s=piece,openB=0,closeB=0,openQ=0,closeQ=0;
    const nb=(s.match(/\*\*/g)||[]).length;
    if(nb){ if(!inBold&&nb%2===1){openB=1;inBold=true} else if(inBold&&nb%2===1){closeB=1} }
    if(/^[“"«]/.test(s)&&!inQuote){openQ=1;inQuote=true}
    const strong=inBold||inQuote||openB||closeB||openQ||closeQ;
    const g=guess(s,target,home);
    toks.push({s:s.replace(/\*\*/g,''),lang:g,strong:!!strong&&!(g==='H')});
    if(closeB)inBold=false;
    if(inQuote&&/[”"»][.,;:!?]*$/.test(s)&&!openQ){inQuote=false}
    else if(inQuote&&openQ&&/[”"»][.,;:!?]*$/.test(s)&&s.length>1){inQuote=false}
    if(openB&&nb>=2)inBold=false;
  });
  /* trechos em destaque/aspas sem sinal contrário viram idioma da aula */
  toks.forEach(t=>{if(t.strong&&t.lang==null)t.lang='T'});
  const decided=toks.filter(t=>t.lang);
  const nT=decided.filter(t=>t.lang==='T').length,nH=decided.length-nT;
  if(!decided.length)return null;
  if(nH===0&&nT>=1&&!toks.some(t=>t.lang==='H'))return {single:'T'};
  if(nT===0&&nH>=1)return {single:'H'};
  /* tokens sem sinal herdam o vizinho (anterior; se for o primeiro, o próximo) */
  let last=null;toks.forEach(t=>{if(t.lang)last=t.lang;else t.lang=last});
  let next=null;for(let i=toks.length-1;i>=0;i--){if(toks[i].lang)next=toks[i].lang;else toks[i].lang=next}
  /* ilhas de uma palavra sem destaque, cercadas pelo mesmo idioma, são absorvidas */
  for(let i=1;i<toks.length-1;i++){const t=toks[i];if(!t.strong&&toks[i-1].lang===toks[i+1].lang&&t.lang!==toks[i-1].lang&&!guess(t.s,target,home))t.lang=toks[i-1].lang}
  const runs=[];
  toks.forEach(t=>{const L=runs[runs.length-1];if(L&&L.lang===t.lang)L.t+=' '+t.s;else runs.push({t:t.s,lang:t.lang})});
  if(runs.length===1)return {single:runs[0].lang};
  return {runs:runs.map(r=>({t:r.t,lang:r.lang==='T'?'T':'H'}))};
}
window.PogLang={plan,guess};
})();
