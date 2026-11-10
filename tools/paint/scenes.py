import sys,random,math
sys.path.insert(0,'/home/user/OXPogg/tools/paint')
from lib import *
SK={'day':[(0,'#5fb0ee'),(.6,'#b9e1f7'),(1,'#fff1d0')],'gold':[(0,'#41649f'),(.45,'#ee9a7c'),(1,'#ffd9a0')],'night':[(0,'#0a1033'),(.6,'#222c66'),(1,'#5a4a8a')]}
def mk(seed,tod):
    s=S(seed); s.tod=tod; return s
def heaven(s,sunpos=None,cl=3):
    t=s.tod; sky(s,SK[t])
    if t=='night':
        for i in range(70): s.ell(s.r.uniform(0,W),s.r.uniform(0,230),s.r.uniform(.5,1.5),s.r.uniform(.5,1.5),'#fff',s.r.uniform(.4,1))
        s.glow(620,70,60,'#cfd8ff',.7); s.ell(620,70,18,18,'#f4f1dc')
    else:
        x,y=(sunpos or (560,110)); 
        if t=='gold': y=max(y,210)
        s.glow(x,y,150,'#fff0b0' if t=='day' else '#ffb066',.9); s.ell(x,y,26,26,'#fffbe0' if t=='day' else '#ffe7b0')
        clouds(s,cl,40,'#fff' if t=='day' else '#ffd7c0',.6)
def road(s,y,col1='#4a4f5a',col2='#2a2d36'):
    s.rect(0,y,W,H-y,s.grad([(0,col1),(1,col2)]))
    for i in range(7): s.rect(40+i*120,y+(H-y)*.45,60,5,'#f4f1e8',1,.75)
# ===== EXTERIORES =====
def t_street(s):
    heaven(s,(600,120)); city_blocks(s,300,9,[('#9fb4c8','#7c93ab'),('#c7b69c','#a8957a'),('#8aa0a8','#6c838c')],(150,260),(70,130),5)
    s.rect(0,300,W,30,'#b9b4a8'); road(s,330)
    for x in (120,420,700): tree(s,x,330,110,('#2f7d4f','#5fb36a','#b6e07a')); s.light(x+10,250,30)
    for x in (260,600): lamp(s,x,330,120); s.light(x,210,40)
    s.rect(0,326,W,6,'#cfc9bb'); s.rect(0,332,W,3,'#000',0,.25)
    for x in range(30,W,150): s.rect(x,H-60,80,8,'#f1eee4',0,.7); s.rect(x+4,H-48,72,6,'#f1eee4',0,.5)
    for x,c in ((180,'#c0453a'),(520,'#3b6aa8')): s.rect(x,342,110,26,c,8); s.rect(x+20,326,60,22,c,6); s.rect(x+26,330,22,14,'#bfe6ff',3); s.rect(x+52,330,22,14,'#bfe6ff',3); s.ell(x+22,368,10,10,'#222'); s.ell(x+88,368,10,10,'#222'); s.shadow(x+55,372,60,5,.35)
    s.rect(660,330,5,40,'#8a8f9e'); s.rect(645,320,36,16,'#2f6aa8',3)
def t_skyline(s):
    heaven(s,(300,140),2)
    for k,(y,cols,hr) in enumerate([(300,[('#47507e','#3a4270')],(150,300)),(340,[('#2b3158','#232848')],(120,240))]): city_blocks(s,y,9,cols,hr,(40,90),7+k)
    s.rect(0,340,W,H-340,s.grad([(0,'#3a3f66'),(1,'#161a36')]))
    for i in range(30): s.rect(s.r.uniform(0,W),345+s.r.uniform(0,90),s.r.uniform(30,110),2,'#ffd98a',1,.35)
    s.glow(300,330,200,'#ffb066',.4)
def t_village(s):
    heaven(s,(620,130)); hills(s,[(250,40,'#9bc58a','#6ea272',2)])
    cols=[('#e8b890','#c78d68'),('#e9d49c','#c9aa68'),('#d98b7a','#b86a5a'),('#9fb9d4','#7d9abb')]
    x=20
    while x<W-60:
        w=s.r.uniform(90,140); h=s.r.uniform(110,170); c=s.r.choice(cols); y=330
        s.rect(x,y-h,w,h,s.grad([(0,c[0]),(1,c[1])])); s.poly([(x-8,y-h),(x+w/2,y-h-46),(x+w+8,y-h)],'#a4503e')
        for wx in (x+w*.2,x+w*.6):
            for wy in (y-h+22,y-h+68):
                s.rect(wx,wy,18,26,'#f4e6c0' if s.tod!='night' else '#ffd36a',2); s.rect(wx-3,wy,3,26,'#7a5a3a'); s.rect(wx+18,wy,3,26,'#7a5a3a'); s.light(wx+9,wy+13,26)
        s.rect(x+w/2-9,y-34,18,34,'#6b4630',3); x+=w+8
    s.rect(0,330,W,H-330,s.grad([(0,'#c9b99a'),(1,'#8c7b62')]))
    for i in range(12): s.ell(s.r.uniform(0,W),340+s.r.uniform(0,100),26,6,'#000',.07)
    tree(s,70,350,100,('#3f8a55','#6dbb76','#c4e88a'))
def t_desert(s):
    heaven(s,(180,160),1)
    for (x,y,w,h,c) in [(480,300,200,130,'#c8754a'),(640,300,160,100,'#b5633d'),(300,300,120,70,'#cf8559')]:
        s.poly([(x,y),(x+w*.12,y-h),(x+w*.88,y-h),(x+w,y)],s.grad([(0,c),(1,'#8a4a2e')]))
    hills(s,[(310,20,'#e0b078','#c98a54',2),(350,30,'#d99a5e','#b0693a',3)])
    s.path(f'M330 {H} L470 330 L520 330 L760 {H}Z','#58504a'); 
    for i in range(6): s.rect(398+i*10,340+i*20,5+i*2,10+i*4,'#f4e6a0',1,.8)
    for x in (80,700): s.rect(x,300,8,60,'#4a7a3a',3); s.rect(x-14,320,8,26,'#4a7a3a',3); s.rect(x+14,312,8,28,'#4a7a3a',3)
def t_lake(s):
    heaven(s,(560,120)); 
    s.poly([(0,260),(120,150),(240,250),(360,130),(520,260),(640,170),(800,250),(800,300),(0,300)],s.grad([(0,'#5f7fa6'),(1,'#9bb6cf')]))
    s.poly([(80,180),(120,150),(160,185)],'#fff',.8); s.poly([(320,150),(360,130),(400,160)],'#fff',.8)
    hills(s,[(300,30,'#4f8a64','#2f6a50',4)])
    s.rect(0,300,W,H-300,s.grad([(0,'#7fb8d6'),(1,'#3d6f98')]))
    for i in range(26): s.rect(s.r.uniform(0,W),310+s.r.uniform(0,130),s.r.uniform(30,100),2,'#fff',1,.3)
    for x,h in [(40,150),(110,120),(700,160),(760,130)]: pine(s,x,320,h)
    s.poly([(560,360),(620,360),(640,340),(540,340)],'#8a5a3a'); s.poly([(590,340),(590,290),(620,340)],'#f6f1e0')
def t_forest(s):
    s.rect(0,0,W,H,s.grad([(0,'#17402f'),(.55,'#2f7a4f'),(1,'#9ad36f')]))
    s.beam([(300,0),(380,0),(560,420),(340,420)],'#fff6b0',.3); s.beam([(520,0),(570,0),(760,420),(600,420)],'#fff6b0',.22)
    for x,h in [(60,330),(180,380),(660,360),(750,320),(300,300),(520,300)]:
        s.rect(x-h*.05,H-h,h*.1,h,'#3a2a1f'); s.ell(x,H-h,h*.28,h*.22,'#1f5a3c'); s.ell(x-h*.1,H-h+20,h*.2,h*.16,'#2e7d4f')
    s.begin('b4')
    for x,h in [(120,250),(250,280),(420,240),(590,270),(720,250)]: s.rect(x-h*.03,H-h-40,h*.06,h,'#2a4a3a',0,.7); s.ell(x,H-h-40,h*.2,h*.14,'#2f6a4a',.7)
    s.end(); mist(s,230,110,.22,'#cfeedd')
    s.rect(0,360,W,H-360,s.grad([(0,'#4d9a52'),(1,'#235a35')]))
    for x,y_,sz in [(80,400,.9),(300,420,1.1),(560,408,1),(710,425,1.2)]:
        for a in range(-4,5): s.path(f'M{x} {y_} Q{x+a*14*sz} {y_-34*sz} {x+a*24*sz} {y_-24*sz+abs(a)*4}',"none",1,'stroke="#2f7a46" stroke-width="4" stroke-linecap="round"')
    for x,y_,rr in [(200,420,26),(660,432,34)]: s.ell(x,y_,rr,rr*.55,'#7a8a86'); s.ell(x-4,y_-4,rr*.7,rr*.3,'#a9b8b2',.8)
    for x in (150,420,610): s.rect(x,372,6,16,'#f4efdc'); s.ell(x+3,372,16,10,'#d9463a'); s.ell(x-3,370,3,2,'#fff'); s.ell(x+9,375,2,2,'#fff')
    for i in range(30): s.ell(s.r.uniform(0,W),s.r.uniform(100,340),2,2,'#fff7b0',.8); 
    s.light(420,300,60,'#d8ff9a',.5)
def t_castle(s):
    heaven(s,(620,150)); hills(s,[(300,50,'#7fb27a','#4f8a5c',2)])
    s.poly([(300,310),(330,150),(480,150),(520,310)],s.grad([(0,'#cfc6b4'),(1,'#8f877a')]))
    for x in (320,400,480): s.rect(x,100,40,150 if x==400 else 90,'#cfc6b4',2); s.poly([(x-4,x and 100),(x+20,60),(x+44,100)],'#a43a3a') if False else s.poly([(x-4,100),(x+20,56),(x+44,100)],'#a43a3a')
    for x in (350,430,490): s.rect(x,180,12,26,'#3b3550',6); s.light(x+6,190,30,'#ffd27a')
    s.rect(390,260,36,50,'#4a3a2a',16); hills(s,[(340,30,'#5f9a62','#3a7048',5)])
    for x in (80,160,700): tree(s,x,340,90)
def t_harbor(s):
    heaven(s,(560,150)); s.rect(0,260,W,H-260,s.grad([(0,'#5fb0d6'),(1,'#1f5a8a')]))
    for i in range(40): s.rect(s.r.uniform(0,W),270+s.r.uniform(0,170),s.r.uniform(30,110),2,'#fff',1,.3)
    city_blocks(s,262,6,[('#d9a58a','#b27a62'),('#e0c78a','#b79a60'),('#9fb6c4','#7a92a2')],(50,110),(50,90),4)
    for x,c in [(160,'#fff'),(420,'#f4d35e'),(640,'#fff')]:
        s.poly([(x-60,330),(x+60,330),(x+42,360),(x-42,360)],'#b5482f'); s.rect(x-3,230,5,100,'#6a4a2a'); s.poly([(x+3,236),(x+3,320),(x+52,320)],c); s.poly([(x-3,250),(x-3,320),(x-44,320)],c,.9)
    s.rect(710,170,18,100,'#e9e4d4'); s.poly([(704,170),(719,140),(734,170)],'#c04a3a'); s.glow(719,152,60,'#ffe28a',.5); s.light(719,160,40)
def t_beach(s):
    heaven(s,(400,130),2); s.rect(0,250,W,100,s.grad([(0,'#2fb0d0'),(1,'#7fdcea')]))
    for i in range(10): s.path(f'M0 {265+i*8} Q200 {255+i*8} 400 {265+i*8} T800 {265+i*8}',"none",.5,'stroke="#fff" stroke-width="2"')
    s.rect(0,340,W,H-340,s.grad([(0,'#f6dfa8'),(1,'#d9b878')]))
    for x,h in [(90,230),(700,260)]:
        s.path(f'M{x} 400 Q{x+10} 280 {x+20} {400-h}',"none",1,'stroke="#7a5a3a" stroke-width="10" stroke-linecap="round"')
        for a in range(-3,4): s.path(f'M{x+20} {400-h} Q{x+20+a*40} {400-h-40} {x+20+a*60} {400-h+30}',"none",1,'stroke="#2f8a4a" stroke-width="9" stroke-linecap="round"')
    s.poly([(260,420),(330,380),(360,420)],'#e0525a'); s.poly([(300,380),(300,330),(380,380)],'#fff'); s.rect(298,330,3,90,'#6a4a2a')
def t_farm(s):
    heaven(s,(600,110)); hills(s,[(240,40,'#a8d27a','#78a85a',2),(290,30,'#8cc063','#5f9a46',3)])
    for i in range(9): s.path(f'M{-100+i*110} 450 L{250+i*60} 300',"none",.35,'stroke="#e2c55a" stroke-width="22"')
    s.rect(430,200,170,110,s.grad([(0,'#c0452f'),(1,'#8f3020')]),4); s.poly([(420,200),(515,140),(610,200)],'#7a2a1e'); s.rect(485,240,60,70,'#f1e6c8',3)
    s.rect(610,170,34,140,'#d9d2c0',3); s.ell(627,168,22,10,'#a9a28e')
    for x in (60,160,240): tree(s,x,320,100,('#3f8a4f','#74be6d','#cdeb8a'))
    s.rect(0,330,W,120,s.grad([(0,'#7fb857'),(1,'#4f8a3a')]))
def t_snow(s):
    s.rect(0,0,W,H,s.grad([(0,'#7da0d0'),(1,'#e8f1fb')])); clouds(s,3,30,'#fff',.7)
    hills(s,[(280,60,'#fff','#cfdcef',2),(330,40,'#f4f8fc','#c2d2e8',3)])
    for x,h in [(80,150),(170,120),(660,170),(740,130),(560,100)]: pine(s,x,340,h,('#2b6a58','#3f8f76')); s.poly([(x-h*.3,340-h*.38),(x,340-h*.9),(x+h*.3,340-h*.38)],'#fff',.8)
    s.rect(0,340,W,110,s.grad([(0,'#ffffff'),(1,'#c9d8ee')]))
    s.rect(330,250,130,92,'#8a5a3a',3); s.poly([(320,252),(395,200),(470,252)],'#fff'); s.rect(380,290,28,52,'#4a2f1f'); s.rect(342,268,24,22,'#ffd27a',2); s.light(354,279,40)
    for i in range(90): s.ell(s.r.uniform(0,W),s.r.uniform(0,H),s.r.uniform(1,2.6),s.r.uniform(1,2.6),'#fff',.85)
def t_space(s):
    s.rect(0,0,W,H,s.grad([(0,'#050820'),(1,'#241a5a')]))
    for i in range(160): s.ell(s.r.uniform(0,W),s.r.uniform(0,H),s.r.uniform(.4,1.6),s.r.uniform(.4,1.6),'#fff',s.r.uniform(.3,1))
    s.glow(600,170,200,'#8a4fd0',.4); s.ell(600,170,100,100,s.grad([(0,'#f0a070'),(1,'#7a3a5a')],.2,0,.8,1)); s.ell(600,170,150,18,'none',.7,'stroke="#f3d9a8" stroke-width="5" transform="rotate(-18 600 170)"')
    s.ell(150,330,60,60,s.grad([(0,'#6fb5ff'),(1,'#1f4a9a')])); s.path('M110 320 Q150 300 190 335 Q150 350 110 320Z','#3d9a5a',.8)
    s.rect(280,300,220,50,'#cfd6e8',8); s.rect(300,310,50,26,'#46c7e0',6); s.rect(500,318,60,10,'#8f98b0'); s.rect(220,326,70,8,'#8f98b0'); s.light(325,323,40,'#7fe6ff')
    s.rect(0,400,W,50,'#10122e')
def t_station(s):
    heaven(s,(300,140),2); city_blocks(s,260,6,[('#8d97ad','#6c7690')],(80,160),(60,110),3)
    s.rect(0,300,W,30,'#c7c2b6'); s.rect(0,330,W,H-330,s.grad([(0,'#6a6f7a'),(1,'#33363f')]))
    for y in (350,390): s.rect(0,y,W,5,'#b9b2a4'); 
    for i in range(14): s.rect(i*62,345,34,60,'#000',0,.12)
    s.rect(560,160,200,160,s.grad([(0,'#2f6aa8'),(1,'#1c4276')]),12); s.rect(575,185,56,44,'#bfe6ff',6); s.rect(645,185,56,44,'#bfe6ff',6); s.rect(560,300,200,18,'#d9473a'); s.glow(755,300,40,'#fff3c2',.8)
    s.rect(120,200,8,140,'#4a3a2a'); s.rect(70,200,110,40,'#f1ece0',6); s.rect(80,210,90,18,'#2f6aa8',3)
def t_airport(s):
    s.rect(0,0,W,H,s.grad(SK[s.tod if s.tod!='day' else 'day'])); clouds(s,3,40)
    s.rect(0,300,W,H-300,s.grad([(0,'#6f7480'),(1,'#3a3e48')]))
    for i in range(8): s.rect(40+i*100,372,50,4,'#f1e08a',1,.8)
    s.poly([(220,290),(520,290),(560,262),(500,262),(480,226),(430,226),(444,262),(260,262)],'#f4f6fa'); s.poly([(500,262),(560,262),(580,222),(560,222)],'#2f6aa8'); s.rect(520,274,30,8,'#2f6aa8')
    s.rect(0,0,W,120,'#2a3a52',0,.0); s.rect(0,380,W,70,'#1c2230',0,.35)
    s.rect(0,0,W,40,'#e9edf4'); s.rect(0,40,W,6,'#bcc5d6')
def t_park(s):
    heaven(s,(600,120)); hills(s,[(250,30,'#9ed27a','#6fa85c',2)])
    s.rect(0,290,W,H-290,s.grad([(0,'#7fc15a'),(1,'#3f8a3a')])); s.path(f'M-20 {H} Q300 330 420 300 T830 {H-30} L830 {H} Z','#e2cf9e')
    for x,h in [(70,170),(190,140),(690,180),(770,130)]: tree(s,x,300,h)
    s.rect(300,330,100,8,'#8a5a3a',2); s.rect(300,320,100,6,'#a6713f',2); s.rect(308,338,6,22,'#4a3a2a'); s.rect(386,338,6,22,'#4a3a2a'); lamp(s,470,340,110)
    for i in range(8): s.ell(s.r.uniform(0,W),s.r.uniform(300,H),s.r.uniform(2,5),s.r.uniform(2,5),s.r.choice(['#fff','#ffd54a','#ff7aa8']),.9)
def t_rooftop(s):
    heaven(s,(300,210)); city_blocks(s,330,10,[('#51608a','#3b4670'),('#6a5a8a','#4a3f6e')],(150,330),(50,100),9)
    s.rect(0,350,W,H-350,s.grad([(0,'#5a5f6e'),(1,'#2a2d38')])); s.rect(0,340,W,14,'#8a8f9e'); s.rect(0,336,W,3,'#e3e6ee')
    for x in range(30,800,70): s.rect(x,300,3,40,'#e3e6ee')
    for i in range(14): s.ell(30+i*58,300,6,6,'#ffe8a8',.9); s.light(30+i*58,300,22)
    s.rect(560,380,120,24,'#8a5a3a',5); s.rect(560,396,120,6,'#6a4429'); s.ell(210,396,26,12,'#000',.2)
# ===== INTERIORES =====
def wall(s,c1='#f2e6d4',c2='#e0cfb4',fy=330,fl1='#b78a5a',fl2='#8a6038',tile=False):
    s.rect(0,0,W,fy,s.grad([(0,c1),(1,c2)])); wallpaper(s,0,fy)
    (tile_floor if tile else wood_floor)(s,fy,fl1,fl2); skirting(s,fy); crown(s)
def vw(s):
    def f(x,y,w,h):
        if s.tod=='night':
            s.rect(x,y,w,h,s.grad(SK['night'])); [s.ell(x+s.r.uniform(0,w),y+s.r.uniform(0,h*.7),1,1,'#fff') for _ in range(14)]
        else:
            city_blocks_mini(s,x,y,w,h)
    return f
def city_blocks_mini(s,x,y,w,h):
    r=random.Random(int(x)); bx=x
    while bx<x+w:
        bw=r.uniform(24,44); bh=r.uniform(h*.3,h*.8); s.rect(bx,y+h-bh,min(bw,x+w-bx),bh,'#7f93aa'); bx+=bw
def t_cafe(s):
    wall(s,'#e9d8bf','#d5bf9c',320,'#9a6a40','#6a4326'); window(s,90,70,220,180,SK[s.tod],'#f6ecd8',view=vw(s)); window(s,500,70,220,180,SK[s.tod],'#f6ecd8',view=vw(s))
    s.rect(0,250,W,10,'#6a4a30'); s.rect(330,60,140,80,'#2a3a30',4); s.rect(336,66,128,68,'#33473a',3)
    for i,t in enumerate(['café','tea','cake']): s.rect(350,78+i*18,60-i*8,4,'#f2ecd8',1,.9)
    s.rect(0,320,W,10,'#8a5a38'); s.rect(120,300,560,26,s.grad([(0,'#7a4a2a'),(1,'#5a3320')]),6); s.rect(120,296,560,8,'#a86f3f',4)
    for x in (200,360,520): cup(s,x,296); s.rect(x+50,282,26,14,'#f6efe0',3)
    for x in (170,430,640): s.ell(x,292,28,6,'#000',.2)
    for x in (90,330,570): table(s,x+10,360,120); cup(s,x+50,358,'#fff'); s.rect(x+20,392,10,50,'#4a3a2e'); s.ell(x+70,372,32,10,'#000',.0)
    for x in (140,380,620): hanging_lamp(s,x,0,110)
    s.light(400,320,160,'#ffc27a',.5)
def t_library(s):
    wall(s,'#7a5638','#5a3d26',340,'#6a4528','#442b18'); 
    for i in range(4): books(s,40+i*190,50,170,250,5)
    s.rect(0,330,W,14,'#3a2415'); window(s,320,90,160,130,SK[s.tod if s.tod!='day' else 'gold'],'#d8c19a',view=vw(s)); 
    table(s,230,372,340,16,'#a56a38'); s.rect(300,358,60,14,'#c8452f',2); s.rect(380,360,70,12,'#3b6aa8',2); cup(s,500,368,'#f4efe0')
    s.rect(280,290,240,3,'#ffd98a',1,.5); s.light(400,300,200,'#ffc878',.45); lamp(s,640,420,80); s.light(640,340,70)
def t_kitchen(s):
    wall(s,'#f4efe4','#e5dccb',330,'#d9d0c0','#b5a98f',True); 
    for i in range(8):
        for j in range(5): s.rect(i*100+2,40+j*30,96,26,'#fff',2,.55)
    s.rect(0,150,W,10,'#d8cfbd'); window(s,320,50,160,90,SK[s.tod],'#fff',view=vw(s))
    for i in range(5): s.rect(40+i*150,200,140,110,s.grad([(0,'#5d8f7a'),(1,'#3f6a5a')]),6); s.rect(100+i*150,236,20,4,'#e8efe9')
    s.rect(0,300,W,70,s.grad([(0,'#3f6a5a'),(1,'#274a3e')])); s.rect(0,292,W,14,'#e9eef0',2)
    s.rect(580,230,60,62,'#cfd6dc',6); s.rect(590,244,40,24,'#2a2f38',3); s.rect(250,268,60,26,'#d9d2c0',4); s.ell(280,266,18,6,'#c0453a'); s.ell(300,262,10,8,'#7ab34a')
    s.ell(160,262,30,16,'#b9bfc7'); s.rect(138,270,44,20,'#9aa1ab',3); s.rect(432,244,80,50,'#a9b3b8',5); s.rect(444,206,18,40,'#4a6a8a')
    s.light(400,40,160,'#fff3c2',.5)
def t_living(s):
    wall(s,'#ebdfd0','#d9cbb6',320,'#b99265','#8c6a42'); window(s,520,60,200,170,SK[s.tod],'#f7f0e1',view=vw(s))
    frame(s,90,80,110,80); frame(s,220,100,70,90,'#d9825a','#f2d27a'); books(s,330,60,120,160,3)
    s.rect(170,350,460,60,s.grad([(0,'#6f9fb0'),(1,'#4a7a8d')]),14,.0)
    s.ell(400,400,230,34,'#5a8a9a',.8); sofa(s,160,372,300); lamp(s,560,420,150); s.light(560,260,90); plant(s,700,420,1.2); plant(s,60,420,1)
    s.rect(500,388,120,12,'#8a5a3a',4); s.rect(512,400,8,28,'#5a3a22'); s.rect(600,400,8,28,'#5a3a22'); s.rect(540,376,40,12,'#f4efe0',3)
def t_bedroom(s):
    wall(s,'#d7e2ec','#b7c9dd',330,'#c19a6a','#8f6a40'); window(s,90,70,170,150,SK[s.tod],'#fff',view=vw(s))
    s.rect(300,230,380,110,s.grad([(0,'#fff'),(1,'#d7e3ee')]),16); s.rect(300,205,380,40,'#7a8fb8',14); s.rect(320,250,120,50,'#fff',12); s.rect(330,300,340,26,'#6f86b8',8)
    s.rect(300,320,380,20,'#7a5a3a',4); s.shadow(490,346,200,10,.35); table(s,720,330,70,10); lamp(s,755,340,60); s.light(755,276,60)
    frame(s,380,80,150,90,'#7aa8d0','#f4c47a'); plant(s,60,420,1.1)
def t_office(s):
    wall(s,'#e6ecf2','#cfd9e4',320,'#8f98a6','#5f6878'); window(s,60,60,260,190,SK[s.tod],'#f4f7fa',view=vw(s))
    s.rect(420,70,300,150,'#f6f8fb',6); [s.rect(440+i*60,92,48,36,c,3) for i,c in enumerate(['#ffd166','#7ac2f0','#ff9aa8','#a7e0a2','#ffd166'])]
    s.rect(440,150,240,4,'#c8d0dc'); s.rect(440,170,180,4,'#c8d0dc')
    s.rect(120,330,420,16,s.grad([(0,'#d9c4a0'),(1,'#b99c70')]),5); s.rect(140,346,10,70,'#5f6878'); s.rect(510,346,10,70,'#5f6878')
    s.rect(220,262,150,66,'#2a3040',6); s.rect(228,268,134,52,'#6fb6f0',3); s.rect(280,328,30,8,'#2a3040'); s.rect(380,318,60,12,'#f1f3f7',3); s.ell(300,420,40,24,'#3a4a6a'); s.rect(260,380,80,40,'#3a4a6a',14)
    plant(s,700,420,1.4); s.light(190,70,200,'#fff3c2',.4)
def t_classroom(s):
    wall(s,'#e9efe2','#d3dcc6',330,'#b99265','#8c6a42'); s.rect(120,60,560,170,'#2d5a48',6); s.rect(110,50,580,10,'#a9733f',3); s.rect(110,230,580,10,'#a9733f',3)
    s.add('<text x="170" y="120" font-family="Georgia,serif" font-size="36" fill="#f4f1e0" opacity=".9">A  B  C   1+1=2</text>'); s.path('M170 160 q60 -30 120 0 t120 0',"none",.7,'stroke="#f4f1e0" stroke-width="3"')
    window(s,20,70,70,130,SK[s.tod],'#fff',view=vw(s))
    for i in range(3):
        x=150+i*190; s.rect(x,320,130,16,'#c8935a',4); s.rect(x+10,336,8,50,'#6a4a2a'); s.rect(x+112,336,8,50,'#6a4a2a'); s.rect(x+20,296,34,20,'#d9473a',2); s.rect(x+70,300,40,16,'#3b6aa8',2); s.rect(x+34,380,60,12,'#3d4a6a',4)
    s.ell(60,412,30,50,'#4a7a3a',.0)
def t_hospital(s):
    wall(s,'#f4f8fa','#dfeaee',330,'#cfd8dc','#9aa7ad',True); s.rect(0,230,W,10,'#7ac2d6')
    s.rect(60,80,100,150,'#fff',6); s.rect(110,100,4,110,'#e24a4a'); s.rect(80,142,60,4,'#e24a4a'); 
    window(s,520,70,230,150,SK[s.tod],'#fff',view=vw(s))
    s.rect(240,270,220,60,'#fff',8); s.rect(232,260,40,80,'#7ac2d6',8); s.rect(260,318,10,52,'#9aa7ad'); s.rect(430,318,10,52,'#9aa7ad'); s.ell(350,300,60,6,'#7ac2d6',.4)
    s.rect(500,250,8,120,'#9aa7ad'); s.rect(480,246,50,6,'#9aa7ad'); s.rect(488,262,34,40,'#bfe6ff',6,.8); s.rect(504,302,2,30,'#bfe6ff')
    s.light(350,40,200,'#e8fbff',.5)
def t_courtroom(s):
    wall(s,'#8a6a4a','#5a4030',330,'#6a4a30','#3f2a1a'); s.rect(0,50,W,10,'#c8a368',0,.5)
    for i in range(6): s.rect(30+i*130,70,60,240,'#a37a50',4,.9); s.rect(30+i*130,70,60,12,'#d9b478')
    s.rect(280,190,240,130,s.grad([(0,'#6a4a30'),(1,'#3f2a1a')]),6); s.rect(270,180,260,20,'#a37a50',4); s.rect(360,130,80,66,'#f1e6d0',6); s.ell(400,125,24,24,'#d9b478'); s.rect(380,210,40,70,'#2a1f16',0,.3)
    s.rect(80,300,130,16,'#a37a50',3); s.rect(590,300,130,16,'#a37a50',3); s.rect(0,330,W,8,'#2a1a10')
    s.glow(400,40,200,'#ffd98a',.4); s.light(400,60,100)
def t_theater(s):
    s.rect(0,0,W,H,s.grad([(0,'#4a0f1f'),(1,'#220610')]))
    for i in range(7): s.poly([(i*130-30,0),(i*130+70,0),(i*130+40,330),(i*130-60,330)],s.grad([(0,'#a82a3a'),(1,'#5a0f1e')]),.9)
    s.rect(120,330,560,36,'#7a5232',4); s.rect(0,366,W,84,s.grad([(0,'#5a3a22'),(1,'#2a1a10')]))
    s.poly([(300,0),(500,0),(700,330),(100,330)],'#ffeab0',.17); s.glow(400,100,260,'#ffd98a',.55)
    for i in range(7): s.ell(70+i*110,420,34,16,'#220610',.9); s.rect(36+i*110,400,68,40,'#4a0f1f',10)
    s.light(400,120,200)
def t_museum(s):
    wall(s,'#f0ede4','#ddd8c8',340,'#d9d3c4','#a9a290',True); 
    for x,w,c in [(70,150,('#7aa8d0','#f0b46a')),(300,200,('#b86a5a','#f2d27a')),(580,130,('#5a9a7a','#f2e6a0'))]: frame(s,x,70,w,w*.7,c[0],c[1])
    for x in (140,400,660):
        s.rect(x-34,300,68,40,'#cfc8b6',3); s.ell(x,290,22,22,'#e9e4d6'); s.rect(x-10,310,20,10,'#d9d3c0'); s.light(x,60,60)
    s.rect(0,340,W,8,'#a9a290'); s.glow(400,0,300,'#fff6d8',.35)
    for x in (230,520): person_sil(s,x,418,120,'#3d3a52')
def t_studio(s):
    s.rect(0,0,W,H,s.grad([(0,'#1b1735'),(1,'#2e2250')])); 
    for i in range(10): s.rect(30+i*78,40,56,170,'#2a2250',4); s.rect(40+i*78,50,36,150,'#3a2f6a',3)
    s.rect(100,260,600,16,'#8a5a3a',4); s.rect(150,276,10,150,'#4a3a2a'); s.rect(640,276,10,150,'#4a3a2a')
    s.rect(300,210,80,50,'#111',4); s.rect(306,216,68,38,'#6fd6f0',3); s.ell(440,212,16,24,'#222'); s.rect(436,236,8,26,'#333'); s.ell(520,206,30,30,'#222'); s.ell(520,206,22,22,'#444'); s.ell(520,206,8,8,'#d9473a')
    s.glow(335,235,110,'#7fe6ff',.5); s.glow(640,80,160,'#ff5aa8',.3); s.light(400,100,260,'#ff5aa8',.5); s.light(180,100,180,'#5aa8ff',.4)
    s.rect(0,420,W,30,'#12102a')
def t_shop(s):
    wall(s,'#f6efe4','#e5d9c4',330,'#c9a77a','#a6824f'); 
    for i in range(3): s.rect(40,70+i*80,300,10,'#9a6a40',2)
    for i in range(3):
        for j in range(6): s.rect(54+j*48,40+i*80,34,32,s.r.choice(['#e0525a','#3b6aa8','#f2c24a','#4aa87a','#a85aa8']),4)
    s.rect(420,200,340,120,s.grad([(0,'#d9b488'),(1,'#a6824f')]),6); s.rect(430,160,100,40,'#222',3); s.rect(438,166,84,28,'#6fe6a0',2)
    for x in (560,610,660): s.rect(x,170,34,30,s.r.choice(['#e0525a','#f2c24a','#3b6aa8']),4)
    s.rect(430,320,320,10,'#8a5a3a'); window(s,470,40,260,90,SK[s.tod],'#fff',view=vw(s)); s.light(250,40,160,'#fff3c2',.4)
def t_restaurant(s):
    wall(s,'#5a2a30','#3a1a22',340,'#4a3020','#2a1a10'); 
    for i in range(5): s.rect(30+i*150,60,110,160,'#3a1a22',6); frame(s,44+i*150,76,82,60,'#d9825a','#f2d27a')
    for x in (140,380,620):
        s.rect(x-70,310,140,10,'#f4efe4',3); s.rect(x-4,320,8,100,'#8a6a4a'); s.ell(x,306,70,14,'#fff',.0)
        s.ell(x-30,302,16,5,'#f4efe4'); s.ell(x+30,302,16,5,'#f4efe4'); s.rect(x-4,276,8,24,'#ffd98a'); s.glow(x,280,70,'#ffb066',.8)
        s.rect(x-80,350,40,70,'#2a1a10',10); s.rect(x+40,350,40,70,'#2a1a10',10)
    hanging_lamp(s,140,0,100); hanging_lamp(s,380,0,100); hanging_lamp(s,620,0,100)
def t_lobby(s):
    wall(s,'#e9ecf2','#cdd5e0',330,'#a8adbc','#6f7586',True); 
    for i in range(3): window(s,60+i*250,50,190,230,SK[s.tod],'#cfd8e6',view=vw(s))
    s.rect(300,310,200,40,'#2f6aa8',8); s.rect(320,330,160,18,'#fff',3,.9); s.ell(400,380,18,6,'#000',.2)
    for x in (110,640): s.ell(x,364,26,10,'#000',.18); s.rect(x-40,330,80,38,'#6b7a94',10); s.rect(x-40,310,80,26,'#8996ae',8)
    plant(s,60,430,1.3); plant(s,740,430,1.3); s.light(400,30,260,'#fff6d8',.5)
THEMES={k[2:]:v for k,v in list(globals().items()) if k.startswith('t_')}
