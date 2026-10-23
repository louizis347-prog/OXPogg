#!/usr/bin/env python3
"""Visual pilot smoke test. Serve repository on localhost:8767; requires Playwright/Chromium."""
from playwright.sync_api import sync_playwright
import json
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=b.new_page(service_workers='block');errors=[];page.on('pageerror',lambda e:errors.append(e.stack))
 page.goto('http://127.0.0.1:8767/app.html')
 page.evaluate("async()=>{PogBilling.allow=()=>true;await ensureLangLoaded('en-a1');window.speak=()=>{};window.say=()=>{};}")
 for w,h in [(1280,900),(800,500),(390,844),(390,560)]:
  page.set_viewport_size({'width':w,'height':h})
  for ep in range(5):
   page.evaluate("i=>play('en-a1',i)",ep)
   assert page.locator('#player').evaluate("x=>x.classList.contains('regular-pilot')")
   n=page.evaluate('P.e.fr.length')
   for fi in range(n):
    page.evaluate("i=>{P.i=i;render();}",fi)
    assert page.locator('#pstage').inner_text().strip()
   page.evaluate("()=>{P.i=P.e.fr.findIndex(f=>f.k==='scene'||f.k==='pgscene');render();}")
   page.wait_for_timeout(600)
   page.evaluate("()=>{const x=document.getElementById('pbub');x.textContent='Observe como Mia inicia a conversa. Experimente a expressão em voz alta e compare com a resposta de Sam.';x.classList.add('p2on');}")
   page.wait_for_timeout(300)
   dims=page.evaluate("""()=>{const r=s=>document.querySelector(s).getBoundingClientRect().toJSON();return {bubble:r('#pbub'),foot:r('.p-foot'),body:r('.p-body'),button:r('#pcta'),portraits:document.querySelectorAll('.pilot-portrait,svg[data-pilot-refined]').length}}""")
   assert dims['bubble']['y']>=dims['foot']['y']-1,dims
   assert dims['body']['bottom']<=dims['foot']['y']+1,dims
   assert dims['button']['bottom']<=h,dims
   assert dims['portraits']>0,dims
   if ep==0:page.screenshot(path=f'/tmp/pilot-{w}-{h}.png')
   page.evaluate('closePlayer()')
 page.evaluate("play('en-a1',5)")
 assert not page.locator('#player').evaluate("x=>x.classList.contains('regular-pilot')")
 print(json.dumps({'errors':errors,'episodes':5,'viewports':4}));assert not errors
 b.close()
