"""Browser smoke checks for the individually rebuilt English episode 177."""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/usr/bin/chromium", headless=True, args=["--no-sandbox"])
    errors = []
    for width, height in [(1280, 900), (390, 844), (390, 560)]:
        page = browser.new_page(viewport={"width": width, "height": height}, service_workers="block")
        page.on("pageerror", lambda err: errors.append(str(err)))
        page.goto("http://127.0.0.1:8767/app.html", wait_until="load")
        page.evaluate("""async () => {
          PogBilling.allow=()=>true; await ensureLangLoaded('en-a1');
          window.speak=()=>{}; window.say=()=>{}; play('en-a1',176);
        }""")
        assert page.evaluate("P.e.n") == 910016
        assert page.evaluate("P.e.fr.length") == 19
        assert page.locator("#player").evaluate("x=>x.classList.contains('regular-pilot')")
        frames = page.evaluate("P.e.fr")
        for index, frame in enumerate(frames):
            page.evaluate("i=>{P.i=i;render();}", index)
            assert page.locator("#pstage").inner_text().strip()
            assert "undefined" not in page.locator("#pstage").inner_text()
            if frame["k"] == "hotscene":
                page.locator(".ps-hot").evaluate_all("xs=>xs.forEach(x=>x.click())")
                page.wait_for_timeout(800)
                assert frame["obra"]["name"] in page.locator("#pgobra").inner_text()
            if frame["k"] == "pgscene":
                assert page.locator(".ps-ln").count() == 8
                assert page.locator(".ps-face").count() == 8
            if frame["k"] == "pgsheet":
                if index == 15:
                    assert page.locator(".ps-fig").count() == 5
                    page.locator(".ps-fig").evaluate_all("xs=>xs.forEach(x=>x.click())")
                for question, item in enumerate(frame["items"]):
                    page.locator(f".ps-q[data-i='{question}'] .ps-o[data-j='{item['a']}']").evaluate("x=>x.click()")
                assert page.locator(".ps-q .ps-o.ok").count() == len(frame["items"])
            if frame["k"] == "pgrule":
                page.locator(f".ps-qq .ps-o[data-j='{frame['q']['a']}']").evaluate("x=>x.click()")
                assert page.locator(".ps-qq .ps-o.ok").count() == 1
            if frame["k"] == "pgmission":
                for mission_index, mission in enumerate(frame["missions"]):
                    page.evaluate("i=>{P.i=i;render();}", index)
                    page.locator(".ps-mc").nth(mission_index).evaluate("x=>x.click()")
                    page.locator("#fxta").evaluate("(x, text)=>{x.value=text;x.dispatchEvent(new Event('input',{bubbles:true}))}", mission["data"]["model"])
                    assert page.locator(".rw-goals li.done").count() == 3
            if frame["k"] == "pgmold":
                page.locator(".ps-slot").evaluate_all("xs=>xs.forEach(x=>x.click())")
        page.evaluate("""() => { const b=document.getElementById('pbub');
          b.textContent='Ouça a primeira fala, localize o problema e responda com a informação que a equipe precisa.';
          b.classList.add('p2on'); }
        """)
        dims = page.evaluate("""() => {const r=s=>document.querySelector(s).getBoundingClientRect().toJSON();
          return {body:r('.p-body'), foot:r('.p-foot'), bubble:r('#pbub')};} """)
        assert dims["body"]["bottom"] <= dims["foot"]["y"] + 1
        assert dims["bubble"]["y"] >= dims["foot"]["y"] - 1
        page.screenshot(path=f"/tmp/english-177-{width}.png")
        page.close()
    browser.close()
    assert not errors, errors
print("PASS: episode 177 rendered and interacted with in three viewports.")
