# Gerador de cenários pintados (mesmo estilo da landing): gradientes, brilhos desfocados, textura, vinheta.
import random, math
W,H=800,450
class S:
    def __init__(s,seed=1):
        s.r=random.Random(seed); s.o=[]; s.d=[]; s.n=0
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
        g=s.rad([(0,col,1),(1,col,0)]); s.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{g}" opacity="{op}" style="mix-blend-mode:screen"/>')
    def shadow(s,x,y,rx,ry,op=.35):
        s.add(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#000" opacity="{op}" filter="url(#b4)"/>')
    def beam(s,pts,col='#fff6c9',op=.22):
        s.add('<polygon points="'+' '.join(f'{x},{y}' for x,y in pts)+f'" fill="{col}" opacity="{op}" filter="url(#b6)" style="mix-blend-mode:screen"/>')
    def out(s):
        defs=('<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="5"/><feColorMatrix type="saturate" values="0"/></filter>'
              '<filter id="b2" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="2"/></filter>'
              '<filter id="b4" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="4"/></filter>'
              '<filter id="b6" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="7"/></filter>'
              '<filter id="b12" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="14"/></filter>'
              '<radialGradient id="vig" cx="50%" cy="48%" r="75%"><stop offset=".55" stop-color="#140b18" stop-opacity="0"/><stop offset="1" stop-color="#140b18" stop-opacity=".5"/></radialGradient>')
        body=''.join(s.o)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice"><defs>{defs}{"".join(s.d)}</defs>{body}'
                f'<rect width="{W}" height="{H}" fill="url(#vig)"/><rect width="{W}" height="{H}" filter="url(#grain)" opacity=".07" style="mix-blend-mode:overlay"/></svg>')
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
        r=random.Random(sd); pts=[]; d=f'M0 {H} L0 {y}'
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
def books(s,x,y,w,h,rows=3):
    pal=['#c0453a','#e08a2e','#3d7fb8','#4a9b6a','#8c5aa8','#d9b44a','#2d5a7b','#b5527a']
    s.rect(x,y,w,h,'#7a5233',3); rh=h/rows
    for r_ in range(rows):
        s.rect(x+4,y+r_*rh+4,w-8,rh-6,'#5a3a22')
        bx=x+6
        while bx<x+w-12:
            bw=s.r.uniform(6,12); bh=rh-10-s.r.uniform(0,rh*.28); c=s.r.choice(pal)
            s.rect(bx,y+(r_+1)*rh-6-bh,bw,bh,c,1); s.rect(bx+1,y+(r_+1)*rh-6-bh,2,bh,'#fff',1,'opacity=".18"'); bx+=bw+1
    s.rect(x,y+h-6,w,6,'#6a4429',2)
def floor(s,y,c1,c2,lines=True):
    s.rect(0,y,W,H-y,s.grad([(0,c1),(1,c2)]))
    if lines:
        for i in range(1,9):
            yy=y+(H-y)*(i/9)**1.4; s.rect(0,yy,W,1.2,'#000',0,.12)
        for i in range(-6,15):
            s.add(f'<line x1="{W/2+(i-4)*40}" y1="{y}" x2="{W/2+(i-4)*140}" y2="{H}" stroke="#000" stroke-opacity=".08" stroke-width="1.2"/>')
def lamp(s,x,y,h,col='#ffd98a'):
    s.rect(x-2,y-h,4,h,'#4b3a2e'); s.poly([(x-18,y-h),(x+18,y-h),(x+11,y-h-26),(x-11,y-h-26)],'#f6e1b0')
    s.glow(x,y-h-10,70,col,.8); s.shadow(x,y+2,16,4)
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
    s.rect(x,y-14,16,14,col,3); s.ell(x+17,y-8,5,5,'none',1,f'stroke="{col}" stroke-width="2"'); s.ell(x+8,y-14,8,2.4,'#8a5a3a'); 
    for i in (0,1): s.path(f'M{x+5+i*5} {y-18} q-3 -8 2 -14',"none",.5,'stroke="#fff" stroke-width="2" stroke-linecap="round"')
def person_sil(s,x,y,h,col='#3b3560'):
    s.ell(x,y-h*.88,h*.1,h*.1,col); s.rect(x-h*.12,y-h*.78,h*.24,h*.5,col,h*.06); s.rect(x-h*.1,y-h*.3,h*.08,h*.3,col); s.rect(x+h*.02,y-h*.3,h*.08,h*.3,col)
