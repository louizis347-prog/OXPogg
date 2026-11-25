/* Original, lesson-specific illustrations for the English A1 pilot. */
const mangaTitles=[
  'Apresentações à mesa','Arrumando a mochila','No balcão do café','Um pão na padaria',
  'Duas porções no balcão','Comprando uma passagem só de ida','Pedindo um café para viagem',
  'Conferindo o bilhete impresso','Nomeando objetos à mesa','Pedindo água no restaurante',
  'A espera na biblioteca','Apresentando a vizinhança','Perguntando sobre um parque',
  'Onde eu moro','À beira do lago','Escolhendo o lugar de sentar','O caminho até a estação',
  'Escrevendo o nome no papel','Uma instrução de segurança no trajeto',
  'Descrevendo a cidade à beira-mar'
];
function mangaPilot(){return lang==='eng'&&level===0&&unit>=0&&unit<20;}
function mangaFile(n){return 'manga/a1-'+String(n).padStart(2,'0')+'.webp';}
function mangaThumbFile(n){return 'manga/thumbs/a1-'+String(n).padStart(2,'0')+'.webp';}
function mangaArtwork(n,kind='scene',variant=0){
  const focus=variant%3;
  const thumbnail=kind==='icon'||kind==='thumb';
  return '<img class="manga-art manga-art--'+kind+' manga-art--focus-'+focus+'" src="'+(thumbnail?mangaThumbFile(n):mangaFile(n))+
    '" alt="" width="'+(thumbnail?256:1280)+'" height="'+(thumbnail?160:800)+'" loading="lazy" decoding="async">';
}
function mangaMoment(index=0,kind='scene'){
  return {manga:true,n:unit+1,kind:kind==='reading'?'scene':'thumb',variant:index,width:1280,height:800};
}
function mangaFigure(photo,className,priority=false){
  const hero=className==='lesson-hero-photo';
  const n=photo.n;
  return '<figure class="'+className+' manga-figure"><img class="manga-art manga-art--'+(hero?'scene':photo.kind)+
    ' manga-art--focus-'+(photo.variant%3)+'" src="'+mangaFile(n)+'" alt="'+
    (hero?'Cena ilustrada: '+mangaTitles[n-1]:'')+'" width="1280" height="800" decoding="async"'+
    (priority?' fetchpriority="high"':' loading="lazy"')+'></figure>';
}
