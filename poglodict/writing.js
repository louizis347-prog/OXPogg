const kanaRows=[
 ['a i u e o','あいうえお','アイウエオ'],
 ['ka ki ku ke ko','かきくけこ','カキクケコ'],
 ['sa shi su se so','さしすせそ','サシスセソ'],
 ['ta chi tsu te to','たちつてと','タチツテト'],
 ['na ni nu ne no','なにぬねの','ナニヌネノ'],
 ['ha hi fu he ho','はひふへほ','ハヒフヘホ'],
 ['ma mi mu me mo','まみむめも','マミムメモ'],
 ['ya yu yo','やゆよ','ヤユヨ'],
 ['ra ri ru re ro','らりるれろ','ラリルレロ'],
 ['wa wo n','わをん','ワヲン'],
 ['ga gi gu ge go','がぎぐげご','ガギグゲゴ'],
 ['za ji zu ze zo','ざじずぜぞ','ザジズゼゾ'],
 ['da ji zu de do','だぢづでど','ダヂヅデド'],
 ['ba bi bu be bo','ばびぶべぼ','バビブベボ'],
 ['pa pi pu pe po','ぱぴぷぺぽ','パピプペポ']
];
const combinations=[
 ['ky','き','キ'],['gy','ぎ','ギ'],['sh','し','シ'],['j','じ','ジ'],
 ['ch','ち','チ'],['ny','に','ニ'],['hy','ひ','ヒ'],['by','び','ビ'],
 ['py','ぴ','ピ'],['my','み','ミ'],['ry','り','リ']
];
const kanaPairs=rows=>rows.flatMap(([sounds,hira,kata])=>sounds.split(' ').map((sound,i)=>[hira[i],kata[i],sound]));
const compoundKana=combinations.flatMap(([sound,hira,kata])=>['a','u','o'].map((v,i)=>
  [hira+'ゃゅょ'[i],kata+'ャュョ'[i],sound+v]));
const pinyinInitials=[
 ['b','bā','八'],['p','pà','怕'],['m','mā','妈'],['f','fǎ','法'],['d','dà','大'],['t','tā','他'],
 ['n','nǐ','你'],['l','lái','来'],['g','gǒu','狗'],['k','kàn','看'],['h','hǎo','好'],
 ['j','jī','鸡'],['q','qī','七'],['x','xué','学'],['zh','zhōng','中'],['ch','chē','车'],
 ['sh','shū','书'],['r','rén','人'],['z','zǒu','走'],['c','cài','菜'],['s','sān','三']
];
const pinyinFinals=[
 ['a','mā','妈'],['o','wǒ','我'],['e','hē','喝'],['i','nǐ','你'],['u','lù','路'],['ü','nǚ','女'],
 ['ai','lái','来'],['ei','měi','美'],['ao','hǎo','好'],['ou','dōu','都'],
 ['an','kàn','看'],['en','hěn','很'],['ang','máng','忙'],['eng','lěng','冷'],['ong','zhōng','中'],['er','ér','儿'],
 ['ia','jiā','家'],['ie','xiè','谢'],['iao','xiǎo','小'],['iou → iu','liù','六'],
 ['ian','tiān','天'],['in','xīn','心'],['iang','xiǎng','想'],['ing','tīng','听'],['iong','xióng','熊'],
 ['ua','huā','花'],['uo','duō','多'],['uai','kuài','快'],['uei → ui','shuǐ','水'],
 ['uan','duǎn','短'],['uen → un','chūn','春'],['uang','guāng','光'],['ueng','wēng','翁'],
 ['üe','yuè','月'],['üan','yuán','元'],['ün','yún','云']
];
const tones=[
 ['1º · alto e estável','mā','妈','mãe','M3 6h42'],
 ['2º · ascendente','má','麻','cânhamo','M3 20 45 6'],
 ['3º · baixo; cai e sobe em isolamento','mǎ','马','cavalo','M3 6q18 31 42 3'],
 ['4º · descendente','mà','骂','repreender','M3 5 45 22'],
 ['Neutro · breve, sem marca','ma','吗','partícula de pergunta','M17 12h13']
];
const hanziStrokes=[
 ['一','yī','um',['M8 19h25']],
 ['二','èr','dois',['M12 12h17','M7 28h27']],
 ['三','sān','três',['M11 10h19','M13 19h15','M6 31h28']],
 ['十','shí','dez',['M7 16h26','M20 6v28']],
 ['人','rén','pessoa',['M22 7q-1 17-14 25','M21 15q4 13 12 17']],
 ['口','kǒu','boca',['M9 10v21','M9 10h22v21','M9 29h22']],
 ['木','mù','árvore',['M6 14h28','M20 6v28','M19 15q-5 9-13 14','M21 16q5 8 13 13']],
 ['日','rì','sol, dia',['M10 8v25','M10 8h20v25','M10 19h20','M10 31h20']]
];
function writingAudio(text,label,note=''){
  return '<button type="button" class="writing-audio" data-writing-say="'+clean(text)+'"><strong lang="'+languages[lang][2]+'">'+clean(text)+'</strong><span>'+clean(label)+'</span>'+(note?'<small>'+clean(note)+'</small>':'')+'</button>';
}
function kanaTable(items){
  return '<div class="kana-grid">'+items.map(([h,k,r])=>'<div class="kana-pair">'+writingAudio(h,r)+writingAudio(k,r)+'</div>').join('')+'</div>';
}
function pinyinTable(items){
  return '<div class="kana-grid">'+items.map(([sound,pron,hanzi])=>writingAudio(hanzi,pron,sound)).join('')+'</div>';
}
function strokeSteps(paths){
  return '<div class="stroke-steps">'+paths.map((_,i)=>'<svg viewBox="0 0 40 40" role="img" aria-label="Traço '+(i+1)+'">'+
    paths.slice(0,i+1).map((path,j)=>'<path d="'+path+'" fill="none" style="stroke:'+(j===i?'#9b486a':'#687866')+'" stroke-width="2" stroke-linecap="round"/>').join('')+'</svg>').join('')+'</div>';
}
function drawWriting(){
  const region=$('writing');
  region.hidden=lang!=='jpn'&&lang!=='cmn';
  if(region.hidden){region.innerHTML='';return;}
  if(lang==='jpn'){
    region.innerHTML='<div class="section-head"><div><h2>Hiragana e katakana</h2><p>Dois silabários. Toque nos caracteres para ouvir.</p></div></div>'+
      '<div class="lesson-card"><p>O <strong>hiragana</strong> aparece em partículas, terminações e palavras japonesas. O <strong>katakana</strong> é comum em empréstimos, nomes estrangeiros e onomatopeias. Em cada par, o hiragana aparece à esquerda.</p>'+
      '<h3>46 sinais básicos em cada silabário</h3>'+kanaTable(kanaPairs(kanaRows.slice(0,10)))+
      '<details><summary>Dakuten e handakuten</summary>'+kanaTable(kanaPairs(kanaRows.slice(10)))+
      '<p>゛ modifica consoantes, como か → が. ゜ forma a série p, como は → ぱ. を, escrito <em>wo</em>, costuma soar <em>o</em> quando é partícula.</p></details>'+
      '<details><summary>Combinações e duração</summary>'+kanaTable(compoundKana)+
      '<p>O っ ou ッ pequeno marca uma pausa antes da consoante seguinte, como em がっこう. O traço ー alonga a vogal anterior em katakana, como em コーヒー. Em hiragana, vogais longas costumam ser escritas com outro kana.</p></details></div>';
    region.insertAdjacentHTML('beforeend','<p role="status" id="writingStatus"></p>');
    return;
  }
  region.innerHTML='<div class="section-head"><div><h2>Pinyin, tons e hanzi</h2><p>Use a romanização para estudar a pronúncia. Os caracteres são o sistema de escrita.</p></div></div><div class="lesson-card">'+
    '<h3>Alfabeto latino usado no pinyin</h3><p class="pinyin-alphabet" lang="zh-Latn">a b c d e f g h i j k l m n o p q r s t u v w x y z</p>'+
    '<p>A letra <strong>v</strong> costuma representar <strong>ü</strong> na digitação. O pinyin escrito usa <strong>ü</strong> quando ele precisa ser indicado. As letras <strong>y</strong> e <strong>w</strong> ajudam a escrever sílabas sem inicial consonantal.</p>'+
    '<h3>Quatro tons e tom neutro</h3><div class="tone-grid">'+tones.map(([label,py,hanzi,pt,svg])=>'<div class="tone-card"><svg viewBox="0 0 48 26" aria-hidden="true"><path d="'+svg+'"/></svg>'+writingAudio(hanzi,py,pt)+'<p>'+label+'</p></div>').join('')+
    '</div><p>As marcas mostram o tom de referência. Em sequência, a pronúncia muda às vezes. Em 你好, o primeiro terceiro tom sobe na fala natural.</p>'+
    '<details><summary>21 iniciais</summary>'+pinyinTable(pinyinInitials)+'</details><details><summary>Finais e exemplos</summary>'+pinyinTable(pinyinFinals)+
    '<p>Depois de j, q e x, escreve-se u onde o som é ü. Por exemplo, xū usa esse som mesmo sem os dois pontos.</p></details>'+
    '<h3>Primeiros caracteres e ordem dos traços</h3><p>O traço em rosa é o que se acrescenta em cada etapa. Compare as etapas para copiar o caractere.</p><div class="hanzi-grid">'+hanziStrokes.map(([hanzi,py,pt,paths])=>'<article>'+writingAudio(hanzi,py,pt)+strokeSteps(paths)+'</article>').join('')+'</div></div><p role="status" id="writingStatus"></p>';
}
