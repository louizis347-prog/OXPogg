from scenes import *
V={}  # (tema, variante) -> função
def reg(k,v):
    def d(f): V[(k,v)]=f; return f
    return d
# ---------- CAFÉ ----------
@reg('cafe',1)
def _(s):
    wall(s,'#2f3b3a','#222b2a',320,'#6a4a30','#3f2a1a'); s.rect(0,0,W,12,'#1a2120')
    s.rect(0,150,W,12,'#1d2625'); 
    for i in range(6): s.rect(40+i*128,60,92,70,'#2a3534',4); s.rect(46+i*128,66,80,58,'#f0e6d0' if i%2 else '#e2d3b6',2); s.rect(54+i*128,78,50,5,'#444',1,.8); s.rect(54+i*128,92,64,4,'#666',1,.7); s.rect(54+i*128,104,40,4,'#666',1,.7)
    s.rect(0,230,W,100,'#3a2a20'); s.rect(0,230,W,8,'#a9733f'); s.rect(0,320,W,10,'#6a4a30')
    for i,c in enumerate(['#c8d0d4','#b9c2c8']): s.rect(120+i*300,176,170,56,c,8); s.rect(130+i*300,160,60,20,'#2a2f38',4); s.ell(260+i*300,172,14,14,'#e9eef0'); s.rect(300+i*300,184,50,10,'#8a929a')
    for x in (130,270,410,550,690): s.rect(x-4,330,8,70,'#3a3a44'); s.ell(x,330,26,8,'#8a2f2f'); s.rect(x-3,330,6,10,'#222')
    s.rect(0,230,W,5,'#fff',0,.18)
    for x in (180,420,660): hanging_lamp(s,x,0,126,'#ffbf6a')
    s.light(400,300,220,'#ffb066',.5)
@reg('cafe',2)
def _(s):
    wall(s,'#e7d9c6','#d3c0a2',330,'#8f6a45','#5a3b22'); window(s,40,50,420,220,SK[s.tod],'#f6ecd8',3,vw(s),curt=('#c9a57a','#a6805a'))
    for x in (90,260,380): s.shadow(x+50,345,76,9,.3); s.rect(x,300,100,34,'#9a6a46',12); s.rect(x,260,100,48,'#b97b53',12); s.rect(x+8,266,84,10,'#fff',5,.15)
    table(s,540,330,150); cup(s,590,326); cup(s,640,326,'#f0d890'); plant(s,740,420,1.4); plant(s,40,430,1.1)
    frame(s,540,70,110,80,'#8cbf9a','#f2d27a'); frame(s,670,90,70,90,'#d9825a','#f2d27a')
    s.rect(500,0,2,70,'#222'); hanging_lamp(s,501,0,90,'#ffd08a')
# ---------- BIBLIOTECA ----------
@reg('library',1)
def _(s):
    wall(s,'#3b2a20','#2a1d15',340,'#5a3a24','#2f1d10'); 
    for i in range(3): books(s,30+i*262,30,235,270,6)
    s.rect(0,300,W,40,'#2a1b12'); s.rect(60,280,10,60,'#8a6a3a'); 
    s.path('M70 280 L120 330',"none",1,'stroke="#8a6a3a" stroke-width="5"'); s.path('M95 280 L140 330',"none",1,'stroke="#8a6a3a" stroke-width="5"')
    for x in (150,420,620): table(s,x,350,150,12,'#7a4a28'); lamp_green(s,x+75,350)
    for x in (150,420,620): chair(s,x-10,392); chair(s,x+130,392)
    for x in (90,400,700): hanging_lamp(s,x,0,70,'#ffd08a')
def lamp_green(s,x,y):
    s.rect(x-2,y-28,4,28,'#c9a24a'); s.ell(x,y-30,20,9,'#2f7a4a'); s.rect(x-20,y-30,40,4,'#2f7a4a'); s.light(x,y-24,40,'#ffe0a0',.8)
@reg('library',2)
def _(s):
    wall(s,'#d9cdb6','#bfae90',340,'#8a6038','#563820'); 
    s.path('M120 340 L120 150 Q400 -30 680 150 L680 340Z',s.grad(SK[s.tod if s.tod!='day' else 'gold']))
    for x in (400,): s.rect(x-2,40,4,300,'#6a4a30')
    s.path('M120 340 L120 150 Q400 -30 680 150 L680 340Z',"none",1,'stroke="#6a4a30" stroke-width="12"')
    for x in (160,640): books(s,x-60,170,120,170,4)
    for i in range(5): table(s,100+i*130,372,100,10,'#9a6a40'); s.rect(120+i*130,360,60,14,s.r.choice(['#c8452f','#3b6aa8','#e0a030']),2)
    plant(s,60,430,1.5); plant(s,745,430,1.5)
# ---------- COZINHA ----------
@reg('kitchen',1)
def _(s):
    wall(s,'#e8eef0','#cfd9dc',330,'#b5a58a','#8a7a60',False)
    s.rect(0,0,W,330,s.grad([(0,'#eef2f3'),(1,'#d9e2e4')])); 
    for i in range(10): s.rect(i*82,30,80,2,'#000',0,.06)
    s.rect(280,40,240,120,'#cfd6dc',6); s.rect(300,60,200,70,'#2a2f38',4,.0); s.poly([(300,160),(500,160),(470,60),(330,60)],'#9aa3ac')
    for i in range(5): s.rect(330+i*36,170,3,40,'#555'); s.ell(331+i*36,214,12,12,'#8a929a'); 
    s.rect(60,260,680,70,s.grad([(0,'#3a4a5a'),(1,'#222d3a')]),6); s.rect(40,250,720,16,'#e9eef0',4); s.rect(280,236,160,16,'#222'); 
    for x in (300,360,420): s.ell(x,244,14,5,'#444')
    s.rect(520,200,40,50,'#b9c2c8',4); s.ell(540,190,22,10,'#c0453a'); 
    for x in (120,640): s.rect(x,300,100,60,'#e6ecef',4)
    for x in (140,260,380,500,620): s.rect(x,342,90,50,'#b9a98a',4)
    for x in (180,420,660): hanging_lamp(s,x,0,100,'#ffe0a0')
@reg('kitchen',2)
def _(s):
    wall(s,'#f3e7d3','#e0cfb0',330,'#9a6a40','#6a4326'); window(s,500,60,220,160,SK[s.tod],'#fff',3,vw(s),curt=('#e6b45a','#c8933a'))
    for i in range(6): s.rect(30+i*70,80,64,100,'#7a5233',3); s.rect(60+i*70,120,5,18,'#e6d6b0')
    s.rect(0,240,W,12,'#d9c9a8'); s.rect(60,262,380,18,'#c8a373',5); s.rect(60,280,380,60,'#8a5a3a',4)
    s.rect(120,200,100,60,'#cfd6dc',6); s.rect(130,210,80,30,'#2a2f38',3); s.rect(260,226,90,34,'#e9eef0',5); s.ell(305,222,26,10,'#9aa3ac')
    table(s,540,330,200,12); chair(s,560,396); chair(s,690,396); cup(s,620,326); plant(s,60,430,1.1)
# ---------- SALA ----------
@reg('living',1)
def _(s):
    wall(s,'#d9e0e6','#bfc9d3',320,'#a8845a','#6f5333')
    s.rect(120,60,560,200,'#2a2f3a',8); s.rect(130,70,540,180,s.grad([(0,'#3b5a8a'),(1,'#1f2f50')]),4); s.rect(380,260,40,30,'#444'); s.rect(250,288,300,18,'#6a4a30',4)
    s.rect(60,80,40,230,'#7a5233'); s.rect(700,80,40,230,'#7a5233'); 
    for i in range(3): s.rect(66,100+i*70,28,60,'#3b2a1d')
    rug(s,400,396,230,32,'#455a7a','#d9c8a8'); sofa(s,250,392,300,('#7a5a8a','#9a7aaa')); lamp(s,640,420,140); plant(s,60,430,1.3)
    s.rect(330,400,140,12,'#6a4a30',4); cup(s,380,398)
@reg('living',2)
def _(s):
    wall(s,'#efe6d8','#dccfb8',330,'#c0a06a','#8f7040'); window(s,60,50,300,230,SK[s.tod],'#fff',3,vw(s),curt=('#d9c8a8','#b9a888'))
    s.rect(470,60,260,150,'#6a4a30',4); s.rect(480,70,240,130,'#f4eddc',2); s.poly([(500,190),(560,100),(620,190)],'#c8a373'); s.rect(580,120,100,70,'#d9825a',2); 
    s.rect(440,214,320,10,'#8a5a3a',3); s.rect(480,226,60,70,'#a9835a'); s.rect(660,226,60,70,'#a9835a')
    sofa(s,400,410,300,('#c8794a','#e09a66')); rug(s,330,400,170,26,'#4a6a5a','#e8dfc4'); plant(s,740,430,1.2); lamp(s,780,420,150)
# ---------- ESCRITÓRIO ----------
@reg('office',1)
def _(s):
    wall(s,'#dfe5ec','#c3ccd8',320,'#7c8696','#4f5868',True)
    s.rect(0,60,W,170,s.grad(SK[s.tod]),0,.0); window(s,40,50,720,190,SK[s.tod],'#f4f7fa',3,vw(s),sill=False)
    for x in (80,260,440,620):
        s.rect(x,330,150,12,'#c9a878',4); s.rect(x+10,342,6,50,'#4f5868'); s.rect(x+134,342,6,50,'#4f5868'); s.rect(x+40,290,70,40,'#2a3040',4); s.rect(x+44,294,62,30,'#6fb6f0',2); s.rect(x+70,330,10,4,'#2a3040')
        s.rect(x+45,380,60,40,'#3a4a6a',14); s.ell(x+75,430,28,6,'#000',.2)
    plant(s,40,430,1.3); plant(s,760,430,1.3)
@reg('office',2)
def _(s):
    wall(s,'#cdb89a','#b39a76',320,'#4a3a2a','#2a1f16'); 
    s.rect(60,60,300,200,'#e7eef4',4); window(s,60,60,300,200,SK[s.tod],'#3a2a1c',3,vw(s))
    s.rect(430,70,300,150,'#3a2a1c',4); s.rect(438,78,284,134,'#f4efe2',2); 
    for i,c in enumerate(['#c0453a','#3b6aa8','#4a9b6a','#d9b44a']): s.rect(456+i*66,96,52,26,c,2); s.rect(456+i*66,134,52,3,'#999'); s.rect(456+i*66,146,40,3,'#999')
    s.rect(200,330,400,18,s.grad([(0,'#5a3a24'),(1,'#3a2414')]),5); s.rect(220,348,10,60,'#2a1a10'); s.rect(570,348,10,60,'#2a1a10')
    s.rect(300,270,90,60,'#222',4); s.rect(306,276,78,48,'#7ac2f0',3); s.rect(450,310,70,20,'#f1f3f7',3); s.ell(400,420,46,14,'#000',.2); s.rect(350,372,100,50,'#2a1f16',16)
    lamp(s,680,420,130); plant(s,740,430,1.1)
# ---------- SALA DE AULA ----------
@reg('classroom',1)
def _(s):
    wall(s,'#f0f2e6','#dfe3cf',330,'#c9a373','#8f6a40'); s.rect(60,60,200,150,'#2f6a52',4); s.rect(54,54,212,10,'#a9733f'); s.rect(54,210,212,10,'#a9733f')
    s.add('<text x="80" y="118" font-family="Georgia,serif" font-size="26" fill="#f4f1e0" opacity=".9">H2O  CO2</text>'); s.path('M80 150 h150',"none",.7,'stroke="#f4f1e0" stroke-width="3"')
    for i,c in enumerate(['#c0453a','#3b6aa8','#4a9b6a']): s.rect(320+i*130,80,100,130,c,4,.85); s.rect(326+i*130,86,88,60,'#fff',2,.9); s.ell(370+i*130,170,18,18,'#fff',.8)
    for i in range(3):
        x=80+i*250; s.rect(x,320,200,14,'#e9eef2',4); s.rect(x+10,334,8,56,'#8f98a6'); s.rect(x+172,334,8,56,'#8f98a6'); s.rect(x+40,290,30,30,'#6fb6f0',8); s.rect(x+120,300,40,20,'#c0453a',3)
    s.rect(0,330,W,6,'#000',0,.15)
@reg('classroom',2)
def _(s):
    wall(s,'#e6ecf3','#cdd8e4',330,'#9aa6b5','#6a7688',True); window(s,540,60,220,170,SK[s.tod],'#fff',3,vw(s))
    for i in range(4):
        x=40+i*170; s.rect(x,300,140,12,'#d9dde3',4); s.rect(x+10,312,6,60,'#6a7688'); s.rect(x+124,312,6,60,'#6a7688'); s.rect(x+30,250,80,50,'#1f2a3a',4); s.rect(x+34,254,72,40,'#6fb6f0',3); s.rect(x+60,300,20,5,'#1f2a3a')
    s.rect(40,60,420,100,'#fff',4); s.add('<text x="70" y="118" font-family="Arial" font-size="30" fill="#2f6aa8">Hello, class!</text>')
# ---------- RUA ----------
@reg('street',1)
def _(s):
    heaven(s,(260,140)); city_blocks(s,310,9,[('#c9a58a','#a5826a'),('#b9c4cc','#97a4ae'),('#d4c09a','#b59f78')],(120,210),(80,130),11)
    s.rect(0,310,W,40,'#c9c2b4'); road(s,350,'#454a54','#262a32')
    for x in (100,330,600):
        s.rect(x,300,70,36,'#c0453a'); s.poly([(x-4,300),(x+35,276),(x+74,300)],'#8a2f2a'); 
        for k in range(7): s.rect(x+k*10,300,5,8,'#f4f1e8')
    for x in (70,360,700): tree(s,x,350,120,('#4f8a3a','#86bd50','#d0e88a'))
    for x in (230,540): lamp(s,x,350,120)
    s.rect(180,300,120,40,'#2f6aa8',3); s.add('<text x="196" y="328" font-family="Arial" font-size="20" fill="#fff">CAFÉ</text>'); 
@reg('street',2)
def _(s):
    s.rect(0,0,W,H,s.grad([(0,'#2a3350'),(1,'#6a5a7a')]) if s.tod!='day' else s.grad(SK['day'])); 
    city_blocks(s,330,8,[('#6a7a9a','#4a5a7a'),('#7a6a8a','#5a4a6a')],(140,260),(90,150),21)
    s.rect(0,330,W,H-330,s.grad([(0,'#3a3f4a'),(1,'#1c1f28')]))
    for i in range(10): s.rect(0,345+i*12,W,2,'#6fb6f0',0,.12+i*.01)
    for x in range(40,W,120): s.rect(x,380,70,5,'#e9e4d0',0,.5)
    for x,c in ((120,'#c0453a'),(420,'#f2c24a')): s.rect(x,350,150,36,c,10); s.rect(x+30,326,80,30,c,8); s.rect(x+36,331,32,20,'#bfe6ff',3); s.rect(x+74,331,28,20,'#bfe6ff',3); s.ell(x+34,388,14,14,'#111'); s.ell(x+116,388,14,14,'#111'); s.light(x+142,368,40,'#fff3c2',.9)
    for x in (60,300,560,740): lamp(s,x,340,140)
# ---------- PARQUE / FLORESTA / LAGO ----------
@reg('park',1)
def _(s):
    heaven(s,(220,120)); hills(s,[(250,40,'#8fc27a','#6ea85c',2)]); s.rect(0,290,W,H-290,s.grad([(0,'#6fb85a'),(1,'#3a7a36')]))
    s.rect(0,300,W,80,s.grad([(0,'#4aa6d0'),(1,'#2a6a9a')]),0,.0); s.ell(560,350,230,50,s.grad([(0,'#6fb6e0'),(1,'#2a6a9a')])); s.ell(560,348,220,44,'#fff',.0)
    for i in range(12): s.rect(380+s.r.uniform(0,300),335+s.r.uniform(0,30),s.r.uniform(20,60),2,'#fff',1,.4)
    for x,h in [(60,190),(170,150),(740,200)]: tree(s,x,320,h,('#3f8a3a','#7ab84a','#cfe68a'))
    s.rect(120,380,110,8,'#8a5a3a',2); s.rect(120,370,110,6,'#a6713f',2); s.rect(128,388,6,22,'#4a3a2a'); s.rect(216,388,6,22,'#4a3a2a')
    s.path(f'M0 {H} Q200 400 300 360 T500 330',"none",1,'stroke="#e2cf9e" stroke-width="40"')
@reg('park',2)
def _(s):
    heaven(s,(600,150)); hills(s,[(280,30,'#a9d27a','#7aa85a',3)]); s.rect(0,300,W,H-300,s.grad([(0,'#7fc15a'),(1,'#3f8a3a')]))
    for i in range(9): s.rect(40+i*90,300,6,50,'#c9b48a'); 
    s.rect(0,320,W,4,'#c9b48a'); s.rect(0,344,W,4,'#c9b48a')
    for x,y_ in [(200,360),(430,380),(640,350)]:
        s.poly([(x,y_),(x+30,y_-20),(x+60,y_)],'#c0453a'); s.rect(x+4,y_,52,26,'#f4efe2'); s.rect(x+22,y_+8,14,18,'#6a4a30')
    for x in (80,700): tree(s,x,330,170)
    s.ell(320,420,12,8,'#e9a05a'); s.ell(500,430,8,6,'#e9a05a'); s.rect(560,410,60,40,'#c0453a',3); s.rect(540,420,100,6,'#fff',0,.0)
@reg('forest',1)
def _(s):
    s.rect(0,0,W,H,s.grad([(0,'#2d3f6a'),(.5,'#6a5a8a'),(1,'#d99a70')])) if s.tod!='day' else s.rect(0,0,W,H,s.grad([(0,'#3d7a52'),(1,'#d7e89a')]))
    for x,h in [(60,420),(200,380),(360,430),(520,400),(680,420),(780,370)]: s.rect(x-h*.04,0,h*.08,H,'#2a1f16',0,.9); s.rect(x+h*.012,0,h*.02,H,'#fff',0,.06)
    mist(s,230,100,.28,'#fff0d0'); s.beam([(330,0),(420,0),(520,420),(260,420)],'#fff0b0',.32)
    s.rect(0,380,W,H-380,s.grad([(0,'#2f5a3a'),(1,'#16301f')]))
    for x in (110,300,470,640): s.rect(x,396,5,16,'#efe6cf'); s.ell(x+2,396,14,9,'#c0453a'); 
    for x,y_ in [(60,410),(250,430),(560,420),(740,440)]:
        for a in range(-4,5): s.path(f'M{x} {y_} Q{x+a*14} {y_-34} {x+a*24} {y_-24+abs(a)*4}',"none",1,'stroke="#3f8a4f" stroke-width="4" stroke-linecap="round"')
@reg('lake',1)
def _(s):
    heaven(s,(400,150),2); s.poly([(0,300),(160,120),(320,260),(520,90),(700,250),(800,170),(800,320),(0,320)],s.grad([(0,'#6f86b0'),(1,'#a8bcd6')])); s.poly([(500,120),(520,90),(548,128)],'#fff',.85)
    hills(s,[(320,40,'#3f7a58','#2a5a42',3)]); s.rect(0,320,W,H-320,s.grad([(0,'#86bfd9'),(1,'#2f5f88')]))
    s.poly([(150,290),(250,290),(330,330),(70,330)],'#fff',.1)
    for x,h in [(50,170),(130,140),(690,180),(760,150)]: pine(s,x,340,h)
    s.rect(280,350,260,12,'#8a5a3a',3); 
    for x in range(290,540,40): s.rect(x,362,6,30,'#6a4429')
    s.poly([(600,400),(680,400),(700,380),(580,380)],'#c0453a'); 
# ---------- SAGUÃO / LOJA / QUARTO ----------
@reg('lobby',1)
def _(s):
    wall(s,'#2b2f3b','#1c1f29',340,'#3a3d48','#1e2029',True); 
    for x in (120,300,500,680): s.rect(x,40,6,300,'#c9a24a',0,.8)
    s.rect(280,210,240,120,'#5a3a24',4); s.rect(270,196,260,18,'#c9a24a',3); s.rect(380,150,40,50,'#222'); s.rect(386,156,28,38,'#6fb6f0',2)
    s.rect(560,60,200,100,'#c9a24a',4); s.add('<text x="590" y="122" font-family="Georgia" font-size="34" fill="#2b2f3b">HOTEL</text>')
    for x in (100,660): s.ell(x,396,34,12,'#000',.25); s.rect(x-38,340,76,44,'#7a2f3a',12); s.rect(x-38,320,76,26,'#8f3f4a',10)
    for x in (150,400,650): hanging_lamp(s,x,0,90,'#ffcf80')
@reg('lobby',2)
def _(s):
    wall(s,'#eef1f6','#d3dae4',340,'#c9ced9','#8a909f',True)
    s.rect(0,40,W,300,s.grad(SK[s.tod]),0,.0); window(s,40,40,720,260,SK[s.tod],'#cfd8e6',4,vw(s),sill=False)
    for x in (200,400,600): s.rect(x-2,40,4,260,'#cfd8e6')
    s.rect(240,320,320,46,'#2f6aa8',8); s.rect(240,320,320,6,'#fff',3,.5)
    for x in (80,700): s.ell(x,398,36,10,'#000',.2); s.rect(x-36,340,72,40,'#4a5a7a',14); s.rect(x-36,324,72,22,'#5a6a8a',10)
    plant(s,40,430,1.5); plant(s,760,430,1.5)
@reg('shop',1)
def _(s):
    wall(s,'#f4e6e6','#e3cfcf',330,'#d9c8b4','#a9937a',True)
    for i in range(4): s.rect(40+i*180,60,150,100,'#fff',4); s.rect(48+i*180,68,134,84,s.r.choice(['#e0525a','#3b6aa8','#f2c24a','#4aa87a']),3,.8); s.rect(100+i*180,160,6,90,'#8a8f9e'); 
    for i in range(5):
        x=60+i*150; s.rect(x,230,6,100,'#8a8f9e'); s.rect(x-30,244,66,4,'#8a8f9e')
        for k in range(4): s.rect(x-28+k*16,250,10,30,s.r.choice(['#c0453a','#3b6aa8','#4a9b6a','#e0a030','#8c5aa8']),2)
    s.rect(560,310,200,50,'#c9a373',5)
@reg('bedroom',1)
def _(s):
    wall(s,'#e9dfe9','#d3c3d3',330,'#b5936a','#7f5f3a'); window(s,540,60,200,170,SK[s.tod],'#fff',3,vw(s),curt=('#c8a3c8','#a883a8'))
    s.rect(60,250,380,90,'#fff',14); s.rect(60,200,380,60,'#8a6aa0',12); s.rect(80,266,130,50,'#fff',12); s.rect(220,266,130,50,'#fff',12); s.rect(60,320,380,24,'#6a4a80',8)
    s.shadow(250,348,200,10,.35); table(s,470,330,60,10); lamp(s,500,340,70); rug(s,300,396,230,30,'#7a6a9a','#e8dfec'); frame(s,150,70,180,100,'#9ac2d6','#f2d9a0'); plant(s,740,430,1.3)
# ---------- NOVOS TEMAS ----------
N={}
def new(k):
    def d(f): N[k]=f; return f
    return d
@new('gym')
def _(s):
    wall(s,'#2a2f3b','#1b1f29',330,'#3a3f4a','#1e2128',True); s.rect(0,60,W,170,'#0f131c',0,.5)
    for i in range(8): s.rect(30+i*95,70,70,150,'#9ad1ff',2,.08)
    for x in (120,300,480,660):
        s.rect(x,300,8,60,'#555'); s.rect(x-40,296,90,8,'#888'); s.ell(x-40,300,22,22,'#222'); s.ell(x+50,300,22,22,'#222'); s.ell(x-40,300,8,8,'#555'); s.ell(x+50,300,8,8,'#555')
    s.rect(80,330,120,16,'#222',5); s.rect(100,346,12,40,'#444'); s.rect(170,346,12,40,'#444'); s.rect(300,170,120,90,'#333',6); s.rect(304,174,112,82,'#7fe6ff',4,.35)
    for x in (140,400,660): hanging_lamp(s,x,0,70,'#c9e6ff')
@new('bakery')
def _(s):
    wall(s,'#f0ddc0','#dcc29c',330,'#8a5a3a','#5f3a22'); s.rect(0,0,W,50,'#c0453a',0,.9); 
    for i in range(20): s.rect(i*42,0,21,50,'#fff',0,.85)
    s.rect(60,200,680,130,s.grad([(0,'#d9b488'),(1,'#a6824f')]),6); s.rect(70,210,660,90,'#bfe6ff',4,.35)
    for i,c in enumerate(['#d9a05a','#c0803a','#e8c27a','#a9652a','#e6b86a','#c0803a']): s.ell(110+i*105,276,36,16,c); s.ell(104+i*105,270,10,5,'#fff',.35)
    s.rect(100,70,130,90,'#3a2a20',4); s.add('<text x="112" y="128" font-family="Georgia" font-size="28" fill="#f4e6c8">Bread</text>')
    for x in (400,600): hanging_lamp(s,x,50,80,'#ffd08a')
    s.rect(560,90,170,90,'#fff',4,.9); s.rect(572,102,60,66,'#e0a05a',4); s.rect(640,102,76,66,'#c0453a',4)
@new('cinema')
def _(s):
    s.rect(0,0,W,H,s.grad([(0,'#1a1020'),(1,'#0c0610')])); s.rect(120,60,560,220,'#f4f1e8',4); s.rect(130,70,540,200,s.grad([(0,'#6fb6f0'),(1,'#f0b46a')]),2)
    s.poly([(130,270),(300,150),(420,230),(540,120),(670,270)],'#2f6a58',.85); s.ell(560,120,24,24,'#fff3c0')
    s.poly([(0,0),(120,60),(120,280),(0,H)],'#5a0f1e'); s.poly([(W,0),(680,60),(680,280),(W,H)],'#5a0f1e')
    for i in range(8):
        for j in range(3): s.rect(60+i*86,330+j*34,64,30,'#7a1a2a',9); s.rect(66+i*86,320+j*34,52,14,'#8a2a3a',6)
    s.beam([(380,0),(420,0),(560,300),(260,300)],'#cfe6ff',.16)
@new('subway')
def _(s):
    s.rect(0,0,W,H,s.grad([(0,'#cfd6dc'),(1,'#9aa3ac')])); s.rect(0,0,W,60,'#e7ecef'); 
    for i in range(14): s.rect(i*60,60,58,200,'#f0f3f5',2); s.rect(i*60,60,2,200,'#000',0,.06)
    s.rect(0,260,W,20,'#2f6aa8'); s.rect(0,280,W,H-280,s.grad([(0,'#8a8f98'),(1,'#454a54')])); s.rect(0,330,W,8,'#f2c24a')
    s.rect(420,110,300,150,'#2a3a52',8); s.rect(436,126,120,110,'#bfe6ff',4,.7); s.rect(572,126,130,110,'#bfe6ff',4,.7); s.rect(420,240,300,14,'#d9473a')
    s.rect(60,100,160,70,'#2f6aa8',6); s.add('<text x="78" y="146" font-family="Arial" font-size="28" fill="#fff">Line 4</text>')
    for x in (150,300): hanging_lamp(s,x,0,40,'#e6f2ff')
@new('bridge')
def _(s):
    heaven(s,(560,160)); s.rect(0,300,W,H-300,s.grad([(0,'#5aa6d0'),(1,'#1f4f7a')]))
    city_blocks(s,300,7,[('#8d97ad','#6c7690')],(80,170),(60,110),13)
    s.rect(0,250,W,16,'#c9ced9'); s.rect(0,266,W,6,'#000',0,.25)
    for x in (140,660): s.rect(x-10,60,20,210,'#b9c0ce'); s.rect(x-24,80,48,8,'#b9c0ce')
    for i in range(0,W,40): s.add(f'<line x1="140" y1="70" x2="{i}" y2="250" stroke="#b9c0ce" stroke-width="1.4" opacity=".8"/>'); s.add(f'<line x1="660" y1="70" x2="{i}" y2="250" stroke="#b9c0ce" stroke-width="1.4" opacity=".8"/>')
    for i in range(30): s.rect(s.r.uniform(0,W),310+s.r.uniform(0,130),s.r.uniform(30,100),2,'#fff',1,.3)
@new('temple')
def _(s):
    heaven(s,(240,130)); hills(s,[(300,40,'#8fb98a','#5f8f6a',2)]); s.rect(0,330,W,H-330,s.grad([(0,'#d9c9a4'),(1,'#a58f68')]))
    x,w=400,260
    s.rect(x-w/2,250,w,90,'#c0453a'); s.poly([(x-w/2-30,250),(x,170),(x+w/2+30,250)],'#2a2f38'); s.poly([(x-w*.35,170),(x,110),(x+w*.35,170)],'#2a2f38'); s.rect(x-24,260,48,80,'#3a2a20')
    for dx in (-90,90): s.rect(x+dx-18,262,36,48,'#f2c24a',3)
    for xx in (80,720): tree(s,xx,340,150,('#e88aa8','#f4b6c8','#fde0e8'))
    for i in range(30): s.ell(s.r.uniform(0,W),s.r.uniform(200,H),3,2,'#f7c6d4',.8)
@new('cabin')
def _(s):
    wall(s,'#7a5238','#5a3a26',330,'#5a3a24','#2f1d10'); 
    for i in range(10): s.rect(0,i*33,W,2,'#000',0,.25)
    s.rect(280,130,240,210,'#8a8f98',4); s.rect(310,190,180,150,'#14100c',4); s.poly([(330,330),(400,250),(470,330)],'#f0a040'); s.poly([(360,330),(400,280),(440,330)],'#ffd860'); s.light(400,300,120,'#ff9a40',.9)
    s.rect(270,120,260,20,'#6a4a30',3); s.rect(60,80,160,110,'#2a3a52',4); window(s,70,90,140,90,SK['night'],'#5a3a24',3)
    s.ell(160,396,70,18,'#a86a4a'); s.rect(580,300,100,40,'#7a3a3a',10); s.rect(580,270,100,40,'#8a4a4a',10)
@new('rain')
def _(s):
    s.rect(0,0,W,H,s.grad([(0,'#27303f'),(1,'#5a6578')])); city_blocks(s,330,8,[('#4a5668','#3a4558'),('#5a5668','#464258')],(150,290),(80,140),31)
    s.rect(0,330,W,H-330,s.grad([(0,'#2f3644'),(1,'#161a22')]))
    for x in (120,360,600): lamp(s,x,340,130)
    for i in range(140): x=s.r.uniform(0,W); y=s.r.uniform(0,H); s.add(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x-6:.0f}" y2="{y+22:.0f}" stroke="#cfe0ff" stroke-opacity=".3" stroke-width="1.2"/>')
    for i in range(8): s.ell(s.r.uniform(40,760),s.r.uniform(360,440),s.r.uniform(30,70),4,'#cfe0ff',.12)
