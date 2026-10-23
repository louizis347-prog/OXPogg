/* Pogglot · personagens ilustrados (SVG próprio, inspirados nas obras, sem usar arte oficial).
   PogChars.svg(id) devolve um SVG 100×150 com os pés em y=146. */
(function(){
'use strict';
const SK='#f4c7a1',SKD='#e6a97c';
const eye=(x,y,r)=>`<circle cx="${x}" cy="${y}" r="${r||3.2}" fill="#2a2230"/><circle cx="${x+1}" cy="${y-1.1}" r="${(r||3.2)*.38}" fill="#fff"/>`;
const cheek=(x,y)=>`<ellipse cx="${x}" cy="${y}" rx="4.2" ry="2.6" fill="#ff8aa0" opacity=".45"/>`;
const smile=(x,y,w)=>`<path d="M${x-w} ${y} Q${x} ${y+w*.9} ${x+w} ${y}" stroke="#7a3b2e" stroke-width="2" fill="none" stroke-linecap="round"/>`;
const shadow='<ellipse cx="50" cy="146" rx="26" ry="3.6" fill="#000" opacity=".16"/>';
const wrap=b=>`<svg class="ps-ch" viewBox="0 0 100 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">${shadow}${b}</svg>`;
const hand=(x,y,c)=>`<circle cx="${x}" cy="${y}" r="5.5" fill="${c||SK}"/>`;
const head=(c,r)=>`<circle cx="50" cy="48" r="${r||24}" fill="${c||SK}"/>`;

const C={
bear:()=>wrap(`
 <ellipse cx="38" cy="140" rx="9" ry="5" fill="#5a3a1c"/><ellipse cx="62" cy="140" rx="9" ry="5" fill="#5a3a1c"/>
 <path d="M26 128 Q24 88 36 78 L64 78 Q76 88 74 128 Z" fill="#2f5fa8"/>
 <path d="M50 78 V128" stroke="#244b87" stroke-width="2"/>
 <rect x="40" y="90" width="5" height="9" rx="2.5" fill="#d9b27c"/><rect x="55" y="90" width="5" height="9" rx="2.5" fill="#d9b27c"/><rect x="40" y="106" width="5" height="9" rx="2.5" fill="#d9b27c"/><rect x="55" y="106" width="5" height="9" rx="2.5" fill="#d9b27c"/>
 ${hand(24,104,'#8a5a2b')}${hand(76,104,'#8a5a2b')}
 <circle cx="28" cy="36" r="9" fill="#8a5a2b"/><circle cx="72" cy="36" r="9" fill="#8a5a2b"/><circle cx="28" cy="36" r="4.5" fill="#c98a57"/><circle cx="72" cy="36" r="4.5" fill="#c98a57"/>
 <circle cx="50" cy="52" r="26" fill="#8a5a2b"/>
 <ellipse cx="50" cy="61" rx="14" ry="11" fill="#e6c08c"/><ellipse cx="50" cy="55" rx="5.5" ry="3.8" fill="#2a1a12"/>
 ${eye(40,46,3.6)}${eye(60,46,3.6)}
 <path d="M44 65 Q50 70 56 65" stroke="#5a2f1a" stroke-width="2" fill="none" stroke-linecap="round"/>
 <ellipse cx="50" cy="34" rx="30" ry="6" fill="#a32a20"/><path d="M30 34 Q32 14 50 13 Q68 14 70 34 Z" fill="#c0392b"/><path d="M33 31 Q50 36 67 31" stroke="#8f1f17" stroke-width="2" fill="none"/>`),
mrs:()=>wrap(`
 <rect x="36" y="128" width="9" height="16" rx="4" fill="#3b2f2f"/><rect x="55" y="128" width="9" height="16" rx="4" fill="#3b2f2f"/>
 <path d="M28 130 Q24 86 38 76 L62 76 Q76 86 72 130 Z" fill="#3f8f6b"/><path d="M50 76 V130" stroke="#2e7455" stroke-width="2"/>
 <path d="M38 76 Q50 90 62 76 Q50 82 38 76Z" fill="#f2b84b"/>
 ${hand(26,106)}${hand(74,106)}
 <circle cx="50" cy="22" r="10" fill="#6b3f26"/>${head()}
 <path d="M26 46 Q26 22 50 22 Q74 22 74 46 Q66 34 50 34 Q34 34 26 46Z" fill="#6b3f26"/>
 ${eye(41,50)}${eye(59,50)}${cheek(35,58)}${cheek(65,58)}${smile(50,60,6)}`),
alice:()=>wrap(`
 <rect x="38" y="130" width="8" height="14" rx="4" fill="#fff"/><rect x="54" y="130" width="8" height="14" rx="4" fill="#fff"/>
 <ellipse cx="42" cy="144" rx="7" ry="3.2" fill="#222"/><ellipse cx="58" cy="144" rx="7" ry="3.2" fill="#222"/>
 <path d="M50 74 L22 132 Q50 140 78 132 Z" fill="#7ec8f0"/><path d="M50 78 L34 132 Q50 137 66 132 Z" fill="#fff"/>
 <rect x="40" y="74" width="20" height="10" rx="4" fill="#7ec8f0"/>
 ${hand(26,108)}${hand(74,108)}
 <path d="M24 56 Q18 24 50 22 Q82 24 76 56 Q80 78 70 84 Q70 60 62 40 L38 40 Q30 60 30 84 Q20 78 24 56Z" fill="#f0cf5e"/>
 ${head()}
 <path d="M28 44 Q50 22 72 44 Q50 34 28 44Z" fill="#f0cf5e"/><path d="M28 42 Q50 24 72 42" stroke="#222" stroke-width="3.4" fill="none"/>
 ${eye(41,50)}${eye(59,50)}${cheek(35,58)}${cheek(65,58)}${smile(50,61,6)}`),
rabbit:()=>wrap(`
 <ellipse cx="40" cy="142" rx="10" ry="4.4" fill="#f4f0f0"/><ellipse cx="60" cy="142" rx="10" ry="4.4" fill="#f4f0f0"/>
 <path d="M28 130 Q26 88 38 78 L62 78 Q74 88 72 130 Z" fill="#fff"/>
 <path d="M34 82 Q50 100 66 82 L70 120 Q50 128 30 120Z" fill="#c0392b"/>
 <path d="M50 90 V122" stroke="#8f1f17" stroke-width="2"/><circle cx="58" cy="108" r="5.5" fill="#f2c94c" stroke="#b8891a" stroke-width="1.6"/><path d="M58 104 V108 H61" stroke="#8a6410" stroke-width="1.2" fill="none"/>
 ${hand(24,104,'#fff')}${hand(76,104,'#fff')}
 <ellipse cx="38" cy="24" rx="7.5" ry="19" fill="#fff" stroke="#e8dede" stroke-width="1.4"/><ellipse cx="62" cy="24" rx="7.5" ry="19" fill="#fff" stroke="#e8dede" stroke-width="1.4"/>
 <ellipse cx="38" cy="26" rx="3.6" ry="13" fill="#ffb3c4"/><ellipse cx="62" cy="26" rx="3.6" ry="13" fill="#ffb3c4"/>
 <circle cx="50" cy="54" r="22" fill="#fff" stroke="#e8dede" stroke-width="1.4"/>
 ${eye(41,50,3)}${eye(59,50,3)}<ellipse cx="50" cy="58" rx="3.6" ry="2.6" fill="#ff8aa0"/>
 <path d="M44 64 Q50 69 56 64" stroke="#7a3b2e" stroke-width="1.8" fill="none" stroke-linecap="round"/>
 <path d="M44 76 L50 72 L56 76 L50 80Z" fill="#2f5fa8"/>`),
cat:()=>wrap(`
 <path d="M84 120 Q104 100 90 84 Q96 108 74 118" stroke="#b56cc9" stroke-width="9" fill="none" stroke-linecap="round"/>
 <ellipse cx="50" cy="112" rx="26" ry="30" fill="#b56cc9"/>
 <path d="M30 100 H40 M30 112 H42 M60 100 H70 M58 112 H70" stroke="#8a3fa3" stroke-width="3" stroke-linecap="round"/>
 <ellipse cx="38" cy="140" rx="9" ry="5" fill="#a259b8"/><ellipse cx="62" cy="140" rx="9" ry="5" fill="#a259b8"/>
 <path d="M24 44 L22 18 L42 32Z" fill="#b56cc9"/><path d="M76 44 L78 18 L58 32Z" fill="#b56cc9"/><path d="M27 38 L26 26 L35 32Z" fill="#ffb3d9"/><path d="M73 38 L74 26 L65 32Z" fill="#ffb3d9"/>
 <ellipse cx="50" cy="52" rx="28" ry="24" fill="#c47fd6"/>
 <path d="M38 34 V40 M50 31 V38 M62 34 V40" stroke="#8a3fa3" stroke-width="3" stroke-linecap="round"/>
 <ellipse cx="39" cy="50" rx="7" ry="8" fill="#f2f7a0"/><ellipse cx="61" cy="50" rx="7" ry="8" fill="#f2f7a0"/><ellipse cx="39" cy="51" rx="2.6" ry="6" fill="#2a2230"/><ellipse cx="61" cy="51" rx="2.6" ry="6" fill="#2a2230"/>
 <path d="M28 62 Q50 84 72 62 Q50 70 28 62Z" fill="#fff" stroke="#7a3b2e" stroke-width="1.6"/><path d="M34 65 V69 M42 68 V73 M50 70 V75 M58 68 V73 M66 65 V69" stroke="#7a3b2e" stroke-width="1.4"/>
 <path d="M47 58 L53 58 L50 62Z" fill="#ff8aa0"/>`),
dorothy:()=>wrap(`
 <rect x="39" y="128" width="8" height="12" rx="3" fill="#fff"/><rect x="53" y="128" width="8" height="12" rx="3" fill="#fff"/>
 <ellipse cx="42" cy="142" rx="8" ry="4.6" fill="#d62828"/><ellipse cx="58" cy="142" rx="8" ry="4.6" fill="#d62828"/><circle cx="40" cy="140" r="1.4" fill="#ffd6d6"/><circle cx="60" cy="140" r="1.4" fill="#ffd6d6"/>
 <path d="M50 74 L26 132 Q50 140 74 132 Z" fill="#5b8def"/>
 <path d="M34 112 H66 M30 122 H70 M42 90 V134 M58 90 V134" stroke="#fff" stroke-width="2.4" opacity=".55"/>
 <rect x="40" y="74" width="20" height="9" rx="4" fill="#fff"/>
 ${hand(27,108)}${hand(73,108)}
 <path d="M28 50 Q28 74 24 90" stroke="#6b3f26" stroke-width="8" stroke-linecap="round" fill="none"/><path d="M72 50 Q72 74 76 90" stroke="#6b3f26" stroke-width="8" stroke-linecap="round" fill="none"/><circle cx="24" cy="92" r="3" fill="#d62828"/><circle cx="76" cy="92" r="3" fill="#d62828"/>
 ${head()}<path d="M26 48 Q26 22 50 22 Q74 22 74 48 Q64 34 50 36 Q36 34 26 48Z" fill="#6b3f26"/>
 ${eye(41,50)}${eye(59,50)}${cheek(35,58)}${cheek(65,58)}${smile(50,61,6)}`),
scarecrow:()=>wrap(`
 <rect x="38" y="128" width="9" height="14" rx="4" fill="#6b4a2b"/><rect x="53" y="128" width="9" height="14" rx="4" fill="#6b4a2b"/>
 <path d="M28 130 Q24 88 38 78 L62 78 Q76 88 72 130 Z" fill="#5d6f8f"/><rect x="40" y="96" width="14" height="12" rx="2" fill="#c0392b" opacity=".85"/><path d="M40 96 L54 108 M54 96 L40 108" stroke="#6b3a2a" stroke-width="1.2"/>
 <path d="M22 100 L8 94 M22 104 L8 106 M78 100 L92 94 M78 104 L92 106" stroke="#e0b94d" stroke-width="3" stroke-linecap="round"/>
 ${hand(24,102,'#e6c78a')}${hand(76,102,'#e6c78a')}
 <circle cx="50" cy="52" r="23" fill="#e6c78a"/><circle cx="62" cy="62" r="4" fill="#8aa5d6" opacity=".7"/>
 ${eye(41,49,3.2)}${eye(59,49,3.2)}<path d="M42 62 Q50 68 58 62" stroke="#6b3a2a" stroke-width="2" fill="none" stroke-linecap="round"/><path d="M45 60 V66 M50 62 V68 M55 60 V66" stroke="#6b3a2a" stroke-width="1.2"/>
 <ellipse cx="50" cy="34" rx="30" ry="6" fill="#8a6a3b"/><path d="M32 34 Q34 12 50 12 Q66 12 68 34Z" fill="#a07f46"/><path d="M30 34 L18 40 M70 34 L82 40 M34 36 L28 46" stroke="#e0b94d" stroke-width="3" stroke-linecap="round"/>`),
lion:()=>wrap(`
 <path d="M80 126 Q100 118 94 98" stroke="#d9822b" stroke-width="7" fill="none" stroke-linecap="round"/><circle cx="94" cy="96" r="6" fill="#8a4b16"/>
 <ellipse cx="50" cy="112" rx="26" ry="28" fill="#e6a23c"/><ellipse cx="50" cy="118" rx="14" ry="18" fill="#f3cf86"/>
 <ellipse cx="36" cy="140" rx="10" ry="5" fill="#d9822b"/><ellipse cx="64" cy="140" rx="10" ry="5" fill="#d9822b"/>
 <circle cx="50" cy="50" r="33" fill="#b8651b"/><circle cx="50" cy="50" r="30" fill="#d9822b"/>
 <circle cx="28" cy="30" r="7" fill="#e6a23c"/><circle cx="72" cy="30" r="7" fill="#e6a23c"/>
 <circle cx="50" cy="54" r="22" fill="#f3cf86"/>
 ${eye(41,50,3.2)}${eye(59,50,3.2)}<path d="M44 58 L56 58 L50 64Z" fill="#7a3b2e"/><path d="M50 64 V68 M44 70 Q50 74 56 70" stroke="#7a3b2e" stroke-width="2" fill="none" stroke-linecap="round"/>${cheek(36,60)}${cheek(64,60)}`),
wendy:()=>wrap(`
 <rect x="39" y="132" width="8" height="10" rx="3" fill="${SK}"/><rect x="53" y="132" width="8" height="10" rx="3" fill="${SK}"/><ellipse cx="42" cy="144" rx="7" ry="3.4" fill="#f2c0d0"/><ellipse cx="58" cy="144" rx="7" ry="3.4" fill="#f2c0d0"/>
 <path d="M50 74 L24 136 Q50 144 76 136 Z" fill="#cfe8ff"/><path d="M40 100 Q50 108 60 100" stroke="#a8cdef" stroke-width="2" fill="none"/>
 <rect x="40" y="74" width="20" height="9" rx="4" fill="#cfe8ff"/>
 ${hand(27,110)}${hand(73,110)}
 <path d="M26 52 Q22 82 34 92 Q30 62 34 44Z" fill="#8a5a3b"/><path d="M74 52 Q78 82 66 92 Q70 62 66 44Z" fill="#8a5a3b"/>
 ${head()}<path d="M26 50 Q26 22 50 22 Q74 22 74 50 Q64 34 50 36 Q36 34 26 50Z" fill="#8a5a3b"/><path d="M60 28 L74 22 L70 36Z M60 28 L72 38 L68 24Z" fill="#ff7aa8"/>
 ${eye(41,50)}${eye(59,50)}${cheek(35,58)}${cheek(65,58)}${smile(50,61,6)}`),
peter:()=>wrap(`
 <ellipse cx="41" cy="142" rx="9" ry="4.6" fill="#6b4a2b"/><ellipse cx="59" cy="142" rx="9" ry="4.6" fill="#6b4a2b"/>
 <rect x="37" y="120" width="10" height="22" rx="4" fill="#9ad08a"/><rect x="53" y="120" width="10" height="22" rx="4" fill="#9ad08a"/>
 <path d="M28 124 Q26 86 38 78 L62 78 Q74 86 72 124 Z" fill="#3f9b4a"/><path d="M28 112 H72" stroke="#6b4a2b" stroke-width="4"/><path d="M32 78 L36 90 L42 80 L48 92 L54 80 L60 92 L66 80 L68 78Z" fill="#2e7d3a"/>
 ${hand(25,106)}${hand(75,106)}
 ${head()}<path d="M26 46 Q26 24 50 24 Q74 24 74 46 Q70 34 60 34 Q52 40 40 34 Q30 34 26 46Z" fill="#a8602a"/>
 <path d="M34 30 Q40 6 72 8 Q60 16 62 30Z" fill="#3f9b4a"/><path d="M62 18 Q82 4 90 14 Q78 12 70 24Z" fill="#d62828"/>
 ${eye(41,50)}${eye(59,50)}${cheek(35,58)}${cheek(65,58)}<path d="M43 60 Q50 67 57 60" stroke="#7a3b2e" stroke-width="2" fill="none" stroke-linecap="round"/>`),
tinker:()=>wrap(`
 <circle cx="50" cy="70" r="46" fill="#fff7b0" opacity=".5"/>
 <path d="M42 66 Q8 30 24 14 Q46 22 46 62Z" fill="#cfefff" opacity=".85" stroke="#9ed3f0" stroke-width="1.4"/><path d="M58 66 Q92 30 76 14 Q54 22 54 62Z" fill="#cfefff" opacity=".85" stroke="#9ed3f0" stroke-width="1.4"/>
 <path d="M50 66 L36 110 Q50 118 64 110Z" fill="#7ad98a"/><path d="M36 106 L30 116 L38 112 L42 120 L50 112 L58 120 L62 112 L70 116 L64 106Z" fill="#5cc572"/>
 <rect x="43" y="108" width="5" height="22" rx="2.5" fill="${SK}"/><rect x="52" y="108" width="5" height="22" rx="2.5" fill="${SK}"/><ellipse cx="45" cy="132" rx="6" ry="3" fill="#2e7d3a"/><ellipse cx="55" cy="132" rx="6" ry="3" fill="#2e7d3a"/>
 <circle cx="50" cy="50" r="17" fill="${SK}"/><circle cx="50" cy="28" r="8" fill="#f2c94c"/><path d="M33 48 Q33 30 50 30 Q67 30 67 48 Q60 38 50 40 Q40 38 33 48Z" fill="#f2c94c"/>
 ${eye(44,52,2.6)}${eye(56,52,2.6)}${smile(50,59,4.4)}
 <circle cx="12" cy="30" r="2" fill="#ffe46b"/><circle cx="88" cy="40" r="2.4" fill="#ffe46b"/><circle cx="22" cy="86" r="1.8" fill="#ffe46b"/>`),
hook:()=>wrap(`
 <rect x="37" y="128" width="10" height="14" rx="4" fill="#2a2230"/><rect x="53" y="128" width="10" height="14" rx="4" fill="#2a2230"/><ellipse cx="42" cy="143" rx="9" ry="4.2" fill="#1b1520"/><ellipse cx="58" cy="143" rx="9" ry="4.2" fill="#1b1520"/>
 <path d="M26 132 Q22 86 36 76 L64 76 Q78 86 74 132 Z" fill="#8b1e2d"/><path d="M50 76 V132" stroke="#5d1420" stroke-width="2"/><circle cx="42" cy="96" r="2.4" fill="#f2c94c"/><circle cx="42" cy="110" r="2.4" fill="#f2c94c"/><circle cx="42" cy="124" r="2.4" fill="#f2c94c"/>
 ${hand(24,106)}
 <path d="M76 106 Q92 108 92 94 Q92 86 84 88" stroke="#c9d1d9" stroke-width="4.4" fill="none" stroke-linecap="round"/>
 <path d="M24 52 Q16 80 28 90 Q26 66 32 50Z" fill="#1b1520"/><path d="M76 52 Q84 80 72 90 Q74 66 68 50Z" fill="#1b1520"/>
 ${head()}
 <path d="M38 62 Q50 58 62 62 Q56 68 50 64 Q44 68 38 62Z" fill="#1b1520"/>
 ${eye(41,50,2.8)}${eye(59,50,2.8)}<path d="M36 44 L46 46 M64 44 L54 46" stroke="#1b1520" stroke-width="2.2" stroke-linecap="round"/>
 <path d="M24 38 Q26 22 50 20 Q74 22 76 38 Q50 30 24 38Z" fill="#1b1520"/><path d="M20 38 Q50 26 80 38 Q74 46 50 40 Q26 46 20 38Z" fill="#2f2a3a"/><circle cx="50" cy="31" r="4" fill="#f4f0f0"/>`),
cowboy:()=>wrap(`
 <rect x="37" y="118" width="10" height="24" rx="4" fill="#3a63b5"/><rect x="53" y="118" width="10" height="24" rx="4" fill="#3a63b5"/>
 <path d="M34 132 Q36 146 48 146 L48 140 L40 132Z" fill="#7a4a24"/><path d="M66 132 Q64 146 52 146 L52 140 L60 132Z" fill="#7a4a24"/>
 <path d="M28 122 Q24 84 38 76 L62 76 Q76 84 72 122 Z" fill="#f2c94c"/><path d="M36 76 L50 124 L64 76 L56 76 L50 92 L44 76Z" fill="#8b5a2b"/><circle cx="44" cy="100" r="3" fill="#fff" opacity=".8"/><circle cx="56" cy="110" r="3" fill="#fff" opacity=".8"/>
 <path d="M28 100 L22 120 M72 100 L78 120" stroke="#f2c94c" stroke-width="9" stroke-linecap="round"/>${hand(21,122)}${hand(79,122)}
 <path d="M44 76 L50 82 L56 76 L52 70 L48 70Z" fill="#c0392b"/>
 ${head()}<path d="M31 50 Q31 36 50 38 Q69 36 69 50 Q60 42 50 44 Q40 42 31 50Z" fill="#8a5a3b"/>
 ${eye(41,52)}${eye(59,52)}${cheek(35,59)}${cheek(65,59)}${smile(50,61,6)}
 <ellipse cx="50" cy="34" rx="34" ry="7" fill="#6b3f1a"/><path d="M33 34 Q33 12 50 12 Q67 12 67 34Z" fill="#8a5a2b"/><rect x="33" y="28" width="34" height="5" fill="#5a3412"/>
 <path d="M62 90 L64 95 L69 95 L65 98 L67 103 L62 100 L57 103 L59 98 L55 95 L60 95Z" fill="#f4f0f0" stroke="#c0a24a" stroke-width="1"/>`),
ranger:()=>wrap(`
 <rect x="38" y="118" width="10" height="22" rx="4" fill="#f4f4f6"/><rect x="52" y="118" width="10" height="22" rx="4" fill="#f4f4f6"/><path d="M36 140 Q38 148 49 146 L49 140Z M64 140 Q62 148 51 146 L51 140Z" fill="#7a4fd0"/>
 <path d="M14 96 Q8 70 24 70 L30 92Z M86 96 Q92 70 76 70 L70 92Z" fill="#9a6ae8" opacity=".8"/>
 <path d="M28 122 Q24 84 38 76 L62 76 Q76 84 72 122 Z" fill="#f4f4f6"/><rect x="38" y="88" width="24" height="22" rx="5" fill="#5bd05b"/><circle cx="44" cy="96" r="2.4" fill="#c0392b"/><circle cx="50" cy="96" r="2.4" fill="#f2c94c"/><circle cx="56" cy="96" r="2.4" fill="#3a63b5"/><rect x="42" y="102" width="16" height="3.4" rx="1.7" fill="#2a2230" opacity=".5"/>
 <path d="M28 100 L22 118 M72 100 L78 118" stroke="#f4f4f6" stroke-width="9" stroke-linecap="round"/><circle cx="21" cy="120" r="6" fill="#7a4fd0"/><circle cx="79" cy="120" r="6" fill="#7a4fd0"/>
 <rect x="34" y="68" width="32" height="10" rx="4" fill="#7a4fd0"/>
 <circle cx="50" cy="46" r="27" fill="#dff4ff" opacity=".55" stroke="#9ad7f2" stroke-width="2.4"/>
 <circle cx="50" cy="50" r="19" fill="${SK}"/><path d="M33 48 Q36 32 50 32 Q64 32 67 48 Q58 40 50 42 Q42 40 33 48Z" fill="#7a4a24"/>
 ${eye(43,52,2.8)}${eye(57,52,2.8)}<path d="M45 60 Q50 65 55 60" stroke="#7a3b2e" stroke-width="2" fill="none" stroke-linecap="round"/>
 <path d="M34 36 Q40 26 52 25" stroke="#fff" stroke-width="2.4" fill="none" stroke-linecap="round" opacity=".8"/>
 <path d="M36 68 L40 62 M64 68 L60 62" stroke="#5bd05b" stroke-width="3" stroke-linecap="round"/>`)
};
window.PogChars={ids:Object.keys(C),svg:id=>C[id]?C[id]():'',face:id=>C[id]?C[id]().replace('viewBox="0 0 100 150"','viewBox="14 2 72 72"').replace(shadow,''):''};
})();
