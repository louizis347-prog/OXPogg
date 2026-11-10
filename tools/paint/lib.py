# Gerador de cenários pintados (mesmo estilo da landing): gradientes, brilhos desfocados, textura, vinheta.
import random, math
W,H=800,450
class S:
    def __init__(s,seed=1):
        s.r=random.Random(seed); s.o=[]; s.d=[]; s.n=0; s.lights=[]; s.tod='day'
    def id(s,p='g'):
        s.n+=1; return f'{p}{s.n}'
    def add(s,x): s.o.append(x)
    def grad(s,stops,x1=0,y1=0,x2=0,y2=1):
        i=s.id('l'); st=''.join(f'<stop offset="{o}" stop-color="{c}"'+(f' stop-opacity="{a}"' if a is not None else '')+'/>' for o,c,a in [(t+(None,))[:3] if len(t)==2 else t for t in stops])
        s.d.append(f'<linearGradient id="{i}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">{st}</linearGradient>'); return f'url(#{i})'
    def rad(s,stops,cx=.5,cy=.5,r=.5):
        i=s.id('r'); st=''.join(f'<stop offset="{o}" stop-color="{c}"'+(f' stop-opacity="{a}"' if a is not None else '')+'/>' for o,c,a in [(t+(None,))[:3] if len(t)==2 else t for t in stops])
        s.d.append(f'<radialGradient id="{i}" cx="{cx}" cy="{cy}" r="{r}">{st}</radialGradient>'); return f'url(#{i})'
    def rect(s,x,y,w,h,fill,rx=0,op=1,extra=''):
        s.add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" opacity="{op}" {extra}/>')
    def ell(s,cx,cy,rx,ry,fill,op=1,extra=''):
        s.add(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="{fill}" opacity="{op}" {extra}/>')
    def poly(s,pts,fill,op=1,extra=''):
        s.add('<polygon points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)+f'" fill="{fill}" opacity="{op}" {extra}/>')
    def path(s,d,fill,op=1,extra=''):
        s.add(f'<path d="{d}" fill="{fill}" opacity="{op}" {extra}/>')
    def glow(s,x,y,r,col,op=.8,blur=True):
        op=op*.5
        g=s.rad([(0,col,1),(1,col,0)]); s.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{g}" opacity="{op}" style="mix-blend-mode:screen"/>')
    def shadow(s,x,y,rx,ry,op=.35):
        s.add(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#000" opacity="{op}" filter="url(#b4)"/>')
    def beam(s,pts,col='#fff6c9',op=.22):
        op=op*.45
        s.add('<polygon points="'+' '.join(f'{x},{y}' for x,y in pts)+f'" fill="{col}" opacity="{op}" filter="url(#b6)" style="mix-blend-mode:screen"/>')
    def light(s,x,y,r,col='#ffd98a',op=.8): s.lights.append((x,y,r,col,op))
    def atmos(s):
        if s.tod=='gold': s.add(f'<rect width="{W}" height="{H}" fill="#ff9a4a" opacity=".16" style="mix-blend-mode:soft-light"/><rect width="{W}" height="{H}" fill="#ffb86a" opacity=".1" style="mix-blend-mode:screen"/>')
        if s.tod=='night':
            s.add(f'<rect width="{W}" height="{H}" fill="#101a4a" opacity=".55" style="mix-blend-mode:multiply"/><rect width="{W}" height="{H}" fill="#3b2f8a" opacity=".18" style="mix-blend-mode:screen"/>')
        for (x,y,r,col,op) in s.lights:
            s.glow(x,y,r*(1.1 if s.tod=='night' else .7),col,op*(.45 if s.tod=='night' else .12))
    def begin(s,f='b2'): s.add(f'<g filter="url(#{f})">')
    def end(s): s.add('</g>')
    def out(s,horizon=300,warm='#ffb27a',cool='#4a8fbf'):
        defs=('<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="5"/><feColorMatrix type="saturate" values="0"/></filter>'
              '<filter id="b2" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="1.6"/></filter>'
              '<filter id="b4" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4"/></filter>'
              '<filter id="b6" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="7"/></filter>'
              '<filter id="b12" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="14"/></filter>'
              '<filter id="paint" x="-1%" y="-1%" width="102%" height="102%"><feTurbulence type="fractalNoise" baseFrequency="0.06" numOctaves="2" seed="3" result="t"/><feDisplacementMap in="SourceGraphic" in2="t" scale="1.6" xChannelSelector="R" yChannelSelector="G" result="d"/><feGaussianBlur in="d" stdDeviation="0.35"/></filter><filter id="plaster" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.012 0.02" numOctaves="3" seed="9"/><feColorMatrix type="matrix" values="0 0 0 0 .5  0 0 0 0 .5  0 0 0 0 .5  .9 0 0 0 -.15"/></filter>'
              '<filter id="bloom" x="-10%" y="-10%" width="120%" height="120%"><feColorMatrix type="matrix" values="2 0 0 0 -1.15  0 2 0 0 -1.15  0 0 2 0 -1.15  0 0 0 1 0"/><feGaussianBlur stdDeviation="7"/></filter>'
              '<radialGradient id="vig" cx="50%" cy="48%" r="72%"><stop offset=".5" stop-color="#0d0714" stop-opacity="0"/><stop offset="1" stop-color="#0d0714" stop-opacity=".48"/></radialGradient>')
        s.atmos(); body=''.join(s.o)
        hz=horizon/H
        gr=f'<linearGradient id="grade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{cool}"/><stop offset="1" stop-color="{warm}"/></linearGradient>'
        hzg=f'<linearGradient id="haze" x1="0" y1="0" x2="0" y2="1"><stop offset="{max(hz-.28,0):.2f}" stop-color="#fff" stop-opacity="0"/><stop offset="{hz:.2f}" stop-color="{warm}" stop-opacity=".22"/><stop offset="{min(hz+.18,1):.2f}" stop-color="{warm}" stop-opacity="0"/></linearGradient>'
        return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice"><defs>{defs}{gr}{hzg}<linearGradient id="side" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff"/><stop offset=".55" stop-color="#808080"/><stop offset="1" stop-color="#000"/></linearGradient><linearGradient id="ao" x1="0" y1="0" x2="0" y2="1"><stop offset=".62" stop-color="#fff"/><stop offset="1" stop-color="#8e8e9c"/></linearGradient>{"".join(s.d)}</defs>'
                f'<g id="sc" filter="url(#paint)">{body}</g>'
                f'<use href="#sc" xlink:href="#sc" filter="url(#bloom)" opacity=".10" style="mix-blend-mode:screen"/>'
                f'<rect width="{W}" height="{H}" fill="url(#haze)" style="mix-blend-mode:screen"/>'
                f'<rect width="{W}" height="{H}" fill="url(#grade)" opacity=".3" style="mix-blend-mode:soft-light"/><rect width="{W}" height="{H}" fill="url(#side)" opacity=".5" style="mix-blend-mode:soft-light"/><rect width="{W}" height="{H}" fill="url(#ao)" style="mix-blend-mode:multiply"/><rect width="{W}" height="{H}" filter="url(#plaster)" opacity=".16" style="mix-blend-mode:multiply"/>'
                f'<rect width="{W}" height="{H}" fill="url(#vig)"/><rect width="{W}" height="{H}" filter="url(#grain)" opacity=".13" style="mix-blend-mode:overlay"/></svg>')
# ---------- peças ----------
def sky(s,stops,sun=None):
    s.rect(0,0,W,H,s.grad(stops))
    if sun: s.glow(sun[0],sun[1],sun[2],sun[3],.9); s.ell(sun[0],sun[1],sun[2]*.16,sun[2]*.16,'#fff8dc',.95)
def clouds(s,n,y0,col='#fff',op=.55):
    for i in range(n):
        x=s.r.uniform(0,W); y=y0+s.r.uniform(0,60); sc=s.r.uniform(.7,1.5)
        for dx,dy,rx,ry in [(0,0,60,14),(-30,4,40,10),(32,3,46,12),(5,-9,34,12)]:
            s.ell(x+dx*sc,y+dy*sc,rx*sc,ry*sc,col,op,'filter="url(#b2)"')
def hills(s,layers):
    for (y,amp,col1,col2,sd) in layers:
        r=random.Random(sd); d=f'M0 {H} L0 {y}'
        x=0
        while x<=W+80:
            d+=f' Q{x+40} {y-amp*r.uniform(.2,1)} {x+80} {y+r.uniform(-amp*.3,amp*.3)}'; x+=80
        d+=f' L{W} {H}Z'; s.path(d,s.grad([(0,col1),(1,col2)]))
def tree(s,x,y,h,leaf=('#2f7d4f','#5fb36a','#b6e07a'),trunk='#5a3a28'):
    w=h*.16; s.rect(x-w/2,y-h*.42,w,h*.42,trunk)
    for dx,dy,r in [(0,-.62,.34),(-.2,-.5,.26),(.22,-.52,.26),(0,-.8,.24)]:
        s.ell(x+dx*h,y+dy*h,r*h,r*h*.9,leaf[0])
    for dx,dy,r in [(-.04,-.68,.22),(.14,-.58,.16),(-.12,-.56,.14)]:
        s.ell(x+dx*h,y+dy*h,r*h,r*h*.85,leaf[1],.9)
    s.ell(x-.06*h,y-.76*h,.12*h,.1*h,leaf[2],.8)
    s.shadow(x,y+2,h*.3,h*.05,.3)
def pine(s,x,y,h,c=('#1d5a45','#2f8a63')):
    for i in range(4):
        w=h*(.34-.06*i); yy=y-h*(.22+.22*i)
        s.poly([(x-w,yy+h*.2),(x,yy-h*.2),(x+w,yy+h*.2)],c[i%2])
    s.rect(x-h*.03,y-h*.12,h*.06,h*.14,'#4a2e1f')
def window(s,x,y,w,h,sky_stops=None,frame='#f4ead6',mull=2,view=None,blind=False):
    s.rect(x-6,y-6,w+12,h+12,frame,6)
    g=s.grad(sky_stops or [(0,'#8fd0f0'),(.7,'#cfeaf6'),(1,'#ffe9b8')])
    s.rect(x,y,w,h,g)
    if view: view(x,y,w,h)
    s.rect(x+w/2-mull/2,y,mull,h,frame); s.rect(x,y+h/2-mull/2,w,mull,frame)
    s.rect(x-8,y+h+4,w+16,6,'#d8c9a8',3)
    s.beam([(x+w*.1,y+h),(x+w*.9,y+h),(x+w*1.6,y+h*2.6),(x-w*.2,y+h*2.6)],'#fff3c2',.18)
    s.light(x+w/2,y+h/2,w*.6,'#bfe6ff',.5)
def books(s,x,y,w,h,rows=3):
    pal=['#c0453a','#e08a2e','#3d7fb8','#4a9b6a','#8c5aa8','#d9b44a','#2d5a7b','#b5527a']
    s.rect(x,y,w,h,'#7a5233',3); rh=h/rows
    for r_ in range(rows):
        s.rect(x+4,y+r_*rh+4,w-8,rh-6,'#5a3a22')
        bx=x+6
        while bx<x+w-12:
            bw=s.r.uniform(6,12); bh=rh-10-s.r.uniform(0,rh*.28); c=s.r.choice(pal)
            s.rect(bx,y+(r_+1)*rh-6-bh,bw,bh,c,1); s.rect(bx+1,y+(r_+1)*rh-6-bh,2,bh,'#fff',0,.18); bx+=bw+1
    s.rect(x,y+h-6,w,6,'#6a4429',2)
def floor(s,y,c1,c2,lines=True):
    s.rect(0,y,W,H-y,s.grad([(0,c1),(1,c2)]))
    if lines:
        for i in range(1,9):
            yy=y+(H-y)*(i/9)**1.4; s.rect(0,yy,W,1.2,'#000',0,.12)
        for i in range(-6,15):
            s.add(f'<line x1="{W/2+(i-4)*40}" y1="{y}" x2="{W/2+(i-4)*140}" y2="{H}" stroke="#000" stroke-opacity=".08" stroke-width="1.2"/>')
    s.rect(0,y,W,H-y,s.grad([(0,'#fff'),(.5,'#fff',0)]) if False else '#fff',0,.0)
def lamp(s,x,y,h,col='#ffd98a'):
    s.rect(x-2,y-h,4,h,'#4b3a2e'); s.poly([(x-18,y-h),(x+18,y-h),(x+11,y-h-26),(x-11,y-h-26)],'#f6e1b0')
    s.glow(x,y-h-10,70,col,.8); s.shadow(x,y+2,16,4); s.light(x,y-h-10,50,col,.9)
def plant(s,x,y,sz=1):
    s.poly([(x-14*sz,y-22*sz),(x+14*sz,y-22*sz),(x+10*sz,y),(x-10*sz,y)],'#b5683d')
    for a in range(-3,4):
        s.path(f'M{x} {y-22*sz} Q{x+a*14*sz} {y-60*sz} {x+a*20*sz} {y-(48+abs(a)*3)*sz}',"none",1,f'stroke="#3d8a52" stroke-width="{5*sz}" stroke-linecap="round"')
    s.shadow(x,y+2,18*sz,4)
def frame(s,x,y,w,h,col1='#5aa7c8',col2='#f0b46a'):
    s.rect(x-4,y-4,w+8,h+8,'#6b4a30',2); s.rect(x,y,w,h,s.grad([(0,col1),(1,col2)])); s.poly([(x,y+h),(x+w*.4,y+h*.45),(x+w*.7,y+h*.75),(x+w,y+h*.4),(x+w,y+h)],'#2f6a58',.85)
def sofa(s,x,y,w,col=('#4f8fa8','#6fb0c2')):
    h=w*.34; s.shadow(x+w/2,y+4,w*.52,10,.35)
    s.rect(x,y-h,w,h,s.grad([(0,col[1]),(1,col[0])]),14); s.rect(x-w*.07,y-h*.62,w*.12,h*.7,col[0],10); s.rect(x+w*.95,y-h*.62,w*.12,h*.7,col[0],10)
    s.rect(x+w*.06,y-h*.3,w*.88,h*.3,col[1],8); s.rect(x+w*.1,y-h*.92,w*.36,h*.52,col[1],8,.9); s.rect(x+w*.54,y-h*.92,w*.36,h*.52,col[1],8,.9)
def table(s,x,y,w,h=14,col='#b27b4a'):
    s.shadow(x+w/2,y+h+34,w*.5,8,.3); s.rect(x,y,w,h,s.grad([(0,'#d09660'),(1,col)]),5)
    for lx in (x+8,x+w-14): s.rect(lx,y+h,6,34,'#7a5233')
def cup(s,x,y,col='#fff'):
    s.rect(x,y-14,16,14,col,3); s.ell(x+17,y-8,5,5,'none',1,f'stroke="{col}" stroke-width="2"'); s.ell(x+8,y-14,8,2.4,'#8a5a3a')
    for i in (0,1): s.path(f'M{x+5+i*5} {y-18} q-3 -8 2 -14',"none",.5,'stroke="#fff" stroke-width="2" stroke-linecap="round"')
def person_sil(s,x,y,h,col='#3b3560'):
    s.ell(x,y-h*.88,h*.1,h*.1,col); s.rect(x-h*.12,y-h*.78,h*.24,h*.5,col,h*.06); s.rect(x-h*.1,y-h*.3,h*.08,h*.3,col); s.rect(x+h*.02,y-h*.3,h*.08,h*.3,col)
# ======== DETALHES (sobrescreve peças simples) ========
def wood_floor(s,y,c1='#b78a5a',c2='#8a6038',plank=46):
    s.rect(0,y,W,H-y,s.grad([(0,c1),(1,c2)]))
    r=random.Random(11); rows=7
    for i in range(rows):
        t0=(i/rows)**1.5; t1=((i+1)/rows)**1.5; ya=y+(H-y)*t0; yb=y+(H-y)*t1
        x=-r.uniform(0,plank*2)
        while x<W:
            w=r.uniform(plank*1.4,plank*3)*(1+t0*1.6)
            s.rect(x,ya,w,yb-ya,'#000' if r.random()<.5 else '#fff',0,r.uniform(.02,.07))
            s.rect(x,ya,1,yb-ya,'#000',0,.22); x+=w
        s.rect(0,yb-1,W,1.4,'#000',0,.2)
    s.rect(0,y,W,(H-y)*.5,s.grad([(0,'#fff'),(1,'#fff',0)]) if False else '#fff',0,.0)
    s.add(f'<rect x="0" y="{y}" width="{W}" height="{(H-y)*.45}" fill="{s.grad([(0,"#ffffff",.16),(1,"#ffffff",0)])}"/>')
def tile_floor(s,y,c1='#d8d4cc',c2='#a9a498',n=8):
    s.rect(0,y,W,H-y,s.grad([(0,c1),(1,c2)]))
    for i in range(1,n+1):
        yy=y+(H-y)*(i/n)**1.5; s.rect(0,yy,W,1.2,'#000',0,.18)
    for k in range(-10,22): s.add(f'<line x1="{W/2+(k-5)*34}" y1="{y}" x2="{W/2+(k-5)*120}" y2="{H}" stroke="#000" stroke-opacity=".12" stroke-width="1.2"/>')
    s.add(f'<rect x="0" y="{y}" width="{W}" height="{(H-y)*.4}" fill="{s.grad([(0,"#ffffff",.22),(1,"#ffffff",0)])}"/>')
def skirting(s,y,c='#f4ece0'):
    s.rect(0,y-14,W,14,c); s.rect(0,y-14,W,2,'#fff',0,.6); s.rect(0,y,W,5,'#000',0,.22)
def crown(s,c='#f7f1e6'):
    s.rect(0,0,W,12,c); s.rect(0,12,W,3,'#000',0,.12)
def wallpaper(s,y1,y2,col='#000',op=.035,step=26):
    for x in range(0,W,step): s.rect(x,y1,step/2,y2-y1,col,0,op)
def curtain(s,x,y,w,h,col=('#9a4a4a','#7a3a3a')):
    n=6
    for i in range(n):
        xx=x+i*w/n; s.rect(xx,y,w/n+1,h,s.grad([(0,col[0]),(.5,col[1]),(1,col[0])],0,0,1,0))
    s.rect(x-4,y-8,w+8,8,'#5a4030',3)
def window(s,x,y,w,h,sky_stops=None,frame='#f4ead6',mull=3,view=None,blind=False,curt=None,sill=True):
    s.rect(x-9,y-9,w+18,h+18,'#000',8,.14)
    s.rect(x-7,y-7,w+14,h+14,frame,5); s.rect(x-7,y-7,w+14,3,'#fff',0,.5)
    g=s.grad(sky_stops or [(0,'#8fd0f0'),(.7,'#cfeaf6'),(1,'#ffe9b8')]); s.rect(x,y,w,h,g)
    if view: view(x,y,w,h)
    # reflexo do vidro
    s.poly([(x+w*.12,y),(x+w*.32,y),(x+w*.12,y+h),(x-w*.08,y+h)],'#fff',.12); s.poly([(x+w*.5,y),(x+w*.56,y),(x+w*.36,y+h),(x+w*.3,y+h)],'#fff',.08)
    s.rect(x+w/2-mull/2,y,mull,h,frame); s.rect(x,y+h/2-mull/2,w,mull,frame); s.rect(x,y,w,2,'#000',0,.2)
    if sill: s.rect(x-12,y+h+5,w+24,7,'#e6d9bf',3); s.rect(x-12,y+h+10,w+24,3,'#000',0,.18)
    if curt: curtain(s,x-34,y-4,34,h+30,curt); curtain(s,x+w,y-4,34,h+30,curt)
    s.beam([(x+w*.1,y+h),(x+w*.9,y+h),(x+w*1.5,y+h*2.4),(x-w*.2,y+h*2.4)],'#fff3c2',.14)
def books(s,x,y,w,h,rows=3):
    pal=['#b5453a','#d9822e','#3d7fb8','#4a9b6a','#8c5aa8','#d9b44a','#2d5a7b','#b5527a','#e8e0cc','#5a6a4a']
    s.rect(x,y,w,h,'#6a4429',3); rh=h/rows
    for r_ in range(rows):
        s.rect(x+4,y+r_*rh+4,w-8,rh-5,'#3e2616'); s.rect(x+4,y+r_*rh+4,w-8,5,'#000',0,.3)
        bx=x+7; base=y+(r_+1)*rh-4
        while bx<x+w-14:
            bw=s.r.uniform(6,13); bh=rh-12-s.r.uniform(0,rh*.3); c=s.r.choice(pal)
            lean=s.r.random()<.06
            if lean: s.poly([(bx,base),(bx+bw,base),(bx+bw+bh*.25,base-bh),(bx+bh*.25,base-bh)],c)
            else:
                s.rect(bx,base-bh,bw,bh,c); s.rect(bx,base-bh,bw,bh,'#000',0,.12); s.rect(bx+1,base-bh,2,bh,'#fff',0,.2)
                s.rect(bx+1,base-bh*.78,bw-2,2,'#f0d890',0,.65)
            bx+=bw+.6
            if s.r.random()<.05: s.ell(bx+8,base-8,7,8,'#3d8a52'); s.rect(bx+3,base-2,10,2,'#7a5a3a'); bx+=18
        s.rect(x+4,base,w-8,4,'#7a5233')
def sofa(s,x,y,w,col=('#4f8fa8','#6fb0c2')):
    h=w*.34; s.shadow(x+w/2,y+6,w*.55,9,.4)
    for lx in (x+w*.05,x+w*.9): s.rect(lx,y,8,12,'#3a2a1c',2)
    s.rect(x,y-h,w,h,s.grad([(0,col[1]),(1,col[0])]),14); s.rect(x-w*.07,y-h*.62,w*.13,h*.72,col[0],10); s.rect(x+w*.94,y-h*.62,w*.13,h*.72,col[0],10)
    for i in range(2):
        cx=x+w*(.08+.46*i); s.rect(cx,y-h*.92,w*.42,h*.56,col[1],10); s.rect(cx,y-h*.92,w*.42,h*.56,'#000',10,.08); s.rect(cx+4,y-h*.9,w*.42-8,6,'#fff',3,.15)
    s.rect(x+w*.06,y-h*.34,w*.88,h*.34,col[1],8); s.rect(x+w*.5-1,y-h*.34,2,h*.34,'#000',0,.2)
    s.poly([(x+w*.1,y-h*.5),(x+w*.2,y-h*.55),(x+w*.22,y-h*.2),(x+w*.12,y-h*.15)],'#e9b45a',1); s.poly([(x+w*.74,y-h*.55),(x+w*.9,y-h*.5),(x+w*.88,y-h*.15),(x+w*.72,y-h*.2)],'#d9694a',1)
def table(s,x,y,w,h=14,col='#b27b4a'):
    s.shadow(x+w/2,y+h+38,w*.52,7,.32); s.rect(x,y,w,h,s.grad([(0,'#d6a06a'),(1,col)]),5); s.rect(x,y,w,2,'#fff',2,.35); s.rect(x,y+h-2,w,2,'#000',0,.25)
    for lx in (x+8,x+w-14): s.rect(lx,y+h,6,36,'#6a4529'); s.rect(lx,y+h,2,36,'#fff',0,.12)
def chair(s,x,y,col='#8a5a3a'):
    s.shadow(x+18,y+46,26,5,.3); s.rect(x,y-52,6,52,col); s.rect(x,y-52,36,5,col,2); s.rect(x,y-30,36,6,col,2); s.rect(x+30,y-30,6,52,col); s.rect(x,y,36,7,col,3); s.rect(x+2,y+7,5,36,col); s.rect(x+29,y+7,5,36,col)
def rug(s,cx,cy,rx,ry,c1='#a55a4a',c2='#e8d8b8'):
    s.ell(cx,cy+3,rx,ry,'#000',.22); s.ell(cx,cy,rx,ry,c1); s.ell(cx,cy,rx*.86,ry*.84,c2,.9); s.ell(cx,cy,rx*.76,ry*.74,c1)
    for i in range(7): s.ell(cx,cy,rx*(.7-i*.1),ry*(.68-i*.1),'none',.5,f'stroke="{c2}" stroke-width="1.4"')
def plant(s,x,y,sz=1):
    s.shadow(x,y+3,20*sz,5,.3)
    s.poly([(x-15*sz,y-26*sz),(x+15*sz,y-26*sz),(x+11*sz,y),(x-11*sz,y)],'#b5683d'); s.rect(x-17*sz,y-30*sz,34*sz,6*sz,'#c97a4a',2); s.poly([(x+4*sz,y-26*sz),(x+15*sz,y-26*sz),(x+11*sz,y),(x+2*sz,y)],'#000',.14)
    for a in range(-5,6):
        ax=x+a*13*sz; ay=y-(70+abs(a)*-3+ (a%2)*10)*sz
        s.path(f'M{x} {y-30*sz} Q{x+a*8*sz} {y-(50)*sz} {ax} {ay}',"none",1,f'stroke="#2f7a46" stroke-width="{3*sz}" stroke-linecap="round"')
        s.ell(ax,ay,9*sz,18*sz,'#3d9a56',1,f'transform="rotate({a*14} {ax} {ay})"'); s.ell(ax-2*sz,ay-3*sz,3*sz,9*sz,'#7ccf8a',.6,f'transform="rotate({a*14} {ax} {ay})"')
def frame(s,x,y,w,h,col1='#5aa7c8',col2='#f0b46a'):
    s.rect(x-9,y-9,w+18,h+18,'#000',2,.2); s.rect(x-7,y-7,w+14,h+14,'#5a3d28',2); s.rect(x-5,y-5,w+10,h+10,'#f5efe2',1)
    s.rect(x,y,w,h,s.grad([(0,col1),(1,col2)])); s.poly([(x,y+h),(x+w*.3,y+h*.5),(x+w*.5,y+h*.72),(x+w*.75,y+h*.38),(x+w,y+h*.7),(x+w,y+h)],'#2f6a58',.9); s.ell(x+w*.75,y+h*.25,w*.06,w*.06,'#fff3c0')
    s.poly([(x,y),(x+w*.45,y),(x,y+h*.6)],'#fff',.12)
def lamp(s,x,y,h,col='#ffd98a'):
    s.shadow(x,y+2,18,4,.3); s.rect(x-2,y-h,4,h,'#3a2c22'); s.ell(x,y,14,4,'#3a2c22')
    s.poly([(x-20,y-h),(x+20,y-h),(x+12,y-h-28),(x-12,y-h-28)],s.grad([(0,'#fff1cf'),(1,'#e8c98c')],0,0,1,0)); s.light(x,y-h-12,46,col,.9)
def cup(s,x,y,col='#fff'):
    s.ell(x+8,y+1,13,3,'#000',.2); s.rect(x,y-14,16,14,col,3); s.rect(x,y-14,5,14,'#000',3,.08); s.ell(x+17,y-8,5,5,'none',1,f'stroke="{col}" stroke-width="2"'); s.ell(x+8,y-14,8,2.4,'#6a4228')
    for i in (0,1): s.path(f'M{x+5+i*5} {y-18} q-3 -8 2 -14',"none",.4,'stroke="#fff" stroke-width="1.6" stroke-linecap="round"')
def hanging_lamp(s,x,y,h,col='#ffcf80'):
    s.rect(x-1,y,2,h,'#222'); s.poly([(x-24,y+h),(x+24,y+h),(x+15,y+h-26),(x-15,y+h-26)],s.grad([(0,'#3a3a44'),(1,'#1e1e26')])); s.ell(x,y+h,24,5,'#ffe9b0',.9); s.light(x,y+h+6,50,col,.9)
def tree(s,x,y,h,leaf=('#2f7d4f','#5fb36a','#b6e07a'),trunk='#5a3a28'):
    r=random.Random(int(x*7+y)); w=h*.12
    s.shadow(x,y+2,h*.34,h*.05,.3)
    s.poly([(x-w/2,y),(x-w*.35,y-h*.5),(x+w*.35,y-h*.5),(x+w/2,y)],trunk); s.poly([(x+w*.1,y),(x+w*.35,y-h*.5),(x+w/2,y)],'#000',.2)
    s.path(f'M{x} {y-h*.35} q{-w} {-h*.12} {-w*1.6} {-h*.2}',"none",1,f'stroke="{trunk}" stroke-width="{w*.35}" stroke-linecap="round"')
    pts=[(r.uniform(-.34,.34),r.uniform(-.98,-.5),r.uniform(.14,.24)) for _ in range(16)]
    for dx,dy,rr in pts: s.ell(x+dx*h,y+dy*h,rr*h,rr*h*.9,leaf[0])
    for dx,dy,rr in pts[::2]: s.ell(x+dx*h-.04*h,y+dy*h-.04*h,rr*h*.7,rr*h*.6,leaf[1],.9)
    for dx,dy,rr in pts[::4]: s.ell(x+dx*h-.07*h,y+dy*h-.07*h,rr*h*.35,rr*h*.28,leaf[2],.85)
    for dx,dy,rr in pts[1::3]: s.ell(x+dx*h+.06*h,y+dy*h+.07*h,rr*h*.55,rr*h*.4,'#000',.1)
def facade(s,x,y,w,h,c1,c2,seed=1):
    r=random.Random(seed); s.rect(x,y-h,w,h,s.grad([(0,c1),(1,c2)])); s.rect(x,y-h,w,3,'#fff',0,.35); s.rect(x,y-h,3,h,'#fff',0,.14); s.rect(x+w-4,y-h,4,h,'#000',0,.15)
    for k in range(int(h//46)): s.rect(x,y-h+k*46+44,w,2,'#000',0,.1)
    if r.random()<.5: s.rect(x+w*.3,y-h-16,w*.4,16,'#8a8f9e'); s.rect(x+w*.3,y-h-16,w*.4,3,'#fff',0,.3)
    if r.random()<.4: s.rect(x+w/2,y-h-40,2,40,'#555')
def city_blocks(s,y,n,cols,hr=(120,240),wr=(50,100),seed=3,wins=True):
    s.begin('b2'); r=random.Random(seed); x=-20
    while x<W+20:
        w=r.uniform(*wr); h=r.uniform(*hr); c=r.choice(cols); facade(s,x,y,w,h,c[0],c[1],int(x))
        if wins:
            for wy in range(int(y-h+14),int(y-14),18):
                for wx in range(int(x+9),int(x+w-12),15):
                    if r.random()<.62:
                        lit=s.tod=='night' and r.random()<.55
                        s.rect(wx-1,wy-1,10,13,'#000',1,.18); s.rect(wx,wy,8,11,'#ffd98a' if lit else ('#b9d4e8' if s.tod!='night' else '#26356a'),1,.95)
                        if not lit and s.tod!='night': s.rect(wx,wy,8,3,'#fff',1,.3)
        x+=w+r.uniform(0,6)
    s.end()
def mist(s,y,h=90,op=.25,col='#ffffff'):
    s.rect(0,y,W,h,s.grad([(0,col,0),(.5,col,op),(1,col,0)]))
