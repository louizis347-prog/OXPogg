// Gera prints (e checagens) de uma aula Real-Life nos dois modos, sem servidor externo.
// Uso: NODE_PATH=$(npm root -g) node professor/tools/rl_shots.js 3 [saida=/tmp]   → /tmp/rl_3_solo_00.png … e uma folha /tmp/rl_3_sheet_solo.png
const http = require('http'), fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const ROOT = '/home/user/OXPogg';
const N = +process.argv[2] || 3, OUT = process.argv[3] || '/tmp';
const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.png': 'image/png', '.svg': 'image/svg+xml' };
const srv = http.createServer((q, r) => { let f = path.join(ROOT, decodeURIComponent(q.url.split('?')[0])); if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { r.statusCode = 404; return r.end('404'); } r.setHeader('Content-Type', MIME[path.extname(f)] || 'application/octet-stream'); fs.createReadStream(f).pipe(r); });
(async () => {
  await new Promise(r => srv.listen(0, r)); const port = srv.address().port;
  const b = await chromium.launch(); let problems = 0;
  for (const mode of ['solo', 'group']) {
    const ctx = await b.newContext({ viewport: { width: 1280, height: 800 } });
    await ctx.addInitScript(m => { try { localStorage.setItem('pg_prof_ok', String(Date.now())); localStorage.setItem('pgx-mode', JSON.stringify(m)); } catch (e) {} }, mode);
    const p = await ctx.newPage(); const errs = [];
    p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error' && !/speech|voice/i.test(m.text())) errs.push('console: ' + m.text()); });
    await p.goto(`http://localhost:${port}/professor/${process.env.PAGE||'aula3.html'}?n=${N}`); await p.waitForTimeout(2200);
    const count = await p.evaluate(() => document.querySelectorAll('#rail .sg').length);
    const files = [];
    for (let k = 0; k < count; k++) {
      const info = await p.evaluate(() => { const pb = document.querySelector('.pg .pb'); const h = document.querySelector('.pg .ph h2'); return { title: h ? h.textContent : '', len: pb ? pb.innerText.length : 0, over: pb ? pb.scrollWidth - pb.clientWidth : 0, tag: (document.querySelector('.pg .ph .tag') || {}).textContent }; });
      if (info.len < 60) { console.log(`PROBLEMA [${mode}] tela ${k + 1} (${info.tag}): quase vazia`); problems++; }
      if (info.over > 4) { console.log(`PROBLEMA [${mode}] tela ${k + 1} (${info.tag}): estouro horizontal de ${info.over}px`); problems++; }
      const f = `${OUT}/${process.env.PFX||'rl'}_${N}_${mode}_${String(k).padStart(2, '0')}.png`; await p.screenshot({ path: f }); files.push(f);
      await p.keyboard.press('ArrowRight'); await p.waitForTimeout(350);
    }
    if (errs.length) { console.log(`PROBLEMA [${mode}] erros de JavaScript:`, errs.slice(0, 3)); problems += errs.length; }
    console.log(`${mode}: ${count} telas → ${OUT}/${process.env.PFX||'rl'}_${N}_${mode}_00.png …`);
    await ctx.close();
  }
  await b.close(); srv.close(); console.log(problems ? 'PROBLEMAS: ' + problems : 'visual ok'); process.exit(problems ? 1 : 0);
})();
