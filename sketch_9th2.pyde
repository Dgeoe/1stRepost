import random
import time

def setup():
    frameRate(30)
    size(1920, 1080)    
    colorMode(HSB)
    global colors, current_color_index, shape_color, x, y, a, b, c, d, e, f, g, h, i, j, k, l, m, n, var, var2, var3, var4, var5, var6,var7,var8
    global start_time
    start_time = time.time() 
    # List of predefined colors
    colors = [
        #color(255,0,255),    #White
        #color(255,255,0),    #Black 
        color(180,255,255),  # Blue
        color(200,255,255),  # Purple
        color(225,255,255),  # Pink
        color(0,255,255),    # Red
        color(20,255,255),   # Orange
        color(40,255,255),    # Yellow
    ]
    
    # Initial color for the shape
    current_color_index = random.randint(0,5)
    shape_color = colors[current_color_index]
    
    #set spawn conditions
    x = 960 #random.randint(300, 660)
    y = 340 #random.randint(100, 340)
    
    a = 960 #random.randint(300, 660)
    b = 600 #random.randint(100, 340)
    
    c = random.randint(200, 1720)
    d = random.randint(200, 880)
    
    e = random.randint(200, 1720)
    f = random.randint(200, 880)
    
    g = random.randint(200, 1720)
    h = random.randint(200, 880)
    
    i = random.randint(200, 1720)
    j = random.randint(200, 880)
    
    k = random.randint(200, 1720)
    l = random.randint(200, 880)
    
    m = random.randint(200, 1720)
    n = random.randint(200, 880)
    
    #growth
    var = 1
    var2 = 1
    var3 = 1
    var4 = 1
    var5 = 1
    var6 = 1
    var7 = 1
    var8 = 1
    
    global cx
    global cy
    global r
    global c
    global px
    global py
    global plea
    
    cx = 960
    cy = 540
    background(70, 250, 150)
    px = cx
    py = cy
    plea = 0
    
    #MSX 
    global center, xa, latency,opacC,radius1,radius2, radius3,centerx1,centerx2,centery1,centery2,centeroy1,centeroy2,cx1,cx2,cx3,cx4,cy1,cy2,cy3,cy4,ax
    global ra
    global rb
    global rc
    global rd
    global re
    global rf
    global rg
    global rh
    global ri
    global rj
    global rk
    global rl
    global rm
    global rn
    global ro
    global rp
    global rq
    global rr
    global rs
    global rt
    global ru
    global rv
    global rw
    global rx
    global ry
    global rz
    global rra
    global rrb
    global rrc
    global rrd
    global rre
    global rrf
    global rrg
    global rrh
    global rri
    global rrj
    global rrk
    global rrl
    global rrm
    global rrn
    global rro
    global rrp
    global rrq
    
    ra = 1
    rb = 960
    rc = 5
    rd = 5
    re = 961
    rf = 5
    rg = 5
    rh = 0.1
    ri = 0.1
    rj = 960
    rk = 0.0001
    rl = 0.0001
    rm = 0.0001
    rn = 960
    ro = 960
    rp = 960
    rq = 960
    rr = 960
    rs = 0.1
    rt = 0.1
    ru = 540
    rv = 0.1
    rw = 0.1
    rx = 540
    ry = 0.1
    rz = 0.1
    rra = 960
    rrb = 540
    rrc = 3
    rrd = 0.0001
    rre = 960
    rrf = 540
    rrg = 3
    rrh = 960
    rri = 540
    rrj = 3
    rrk = 960
    rrl = 540
    rrm = 3
    rrn = 540
    rro = 960
    rrp = 540
    rrq = 960
    rrr = 0.1

    
ra = 0
rb = 0
rc = 0
rd = 0
re = 0
rf = 0
rg = 0
rh = 0
ri = 0
rj = 0
rk = 0
rl = 0
rm = 0
rn = 0
ro = 0
rp = 0
rq = 0
rr = 0
rs = 0
rt = 0
ru = 0
rv = 0
rw = 0
rx = 0
ry = 0
rz = 0
rra = 0
rrb = 0
rrc = 0
rrd = 0
rre = 0
rrf = 0
rrg = 0
rrh = 0
rrj = 0
rri = 0
rrk = 0
rrl = 0
rrm = 0
rrn = 0
rro = 0
rrp = 0
rrq = 0
rrr = 0
rrs = 0
rrt = 0
rru = 0

center=960
xa=0
latency=0
opacC=0
radius1=24
radius2=83
radius3=79
centerx1=834
centerx2=828
centery1=460
centeroy1=473
centery2=366
centeroy2=357
# c is for corner
cx1=0
cx2=0
cx3=0
cx4=0
cy1=0
cy2=0
cy3=0
cy4=0
ax=0

#background
cx = 90
cy = 90
c=90
r = 100
theta = 0
px = 0
py = 0

def draw():
    global x, y, a, b, c, d, e, f, g, h, i, j, k, l, m, n
    global shape_color
    global var, var2, var3, var4, var5, var6, var7, var8
    colorMode(HSB)
    global cx
    global cy
    global r
    global c
    global theta
    global px
    global py
    global plea
    global center, xa, latency,opacC,radius1,radius2, radius3, centerx1,centerx2,centery1,centery2,cx1,cx2,cx3,cx4,cy1,cy2,cy3,cy4,ax,centeroy1,centeroy2
    global rb
    global rc
    global rd
    global re
    global rf
    global rg
    global ra
    global rn
    global ro
    global rp
    global rq
    global rra
    global rrb
    global rrc
    global rrd
    global rre
    global rrf
    global rrg
    global rrh
    global rri
    global rrj
    global rrk
    global rrl
    global rrm
    global rh
    global ri
    global rj
    global rk
    global rl
    global rm
    global rr
    global rs
    global rt
    global ru
    global rv
    global rw
    global rx
    global ry
    global rz
    global rrn
    global rro
    global rrp
    global rrq
    global rrr
    
    # Initial color for the shape
    current_color_index = random.randint(0,5)
    shape_color = colors[current_color_index]
    
    frameRate(100)
    draw_backing()
    elapsed= time.time() - start_time
    plea = plea + elapsed
    
    if plea > 10000 and plea < 97000:
        limit = 1
        frameRate(150 + limit)
        draw_ohgod()
        limit + 100
        
    if plea > 65000:
        colorMode(RGB)
        frameRate(60)
        draw_MSX()
    
    if var > 19 and var < 90 : #flower 1
        frameRate(30)
        fill(100,255,255)
        noStroke()
        rect(x-5, y+90, 10, var)
        
        var= var + 10
          
    if var < 20 and plea > 8000:
        frameRate(30)
        fill(shape_color)
        draw_petal(x, y, var)
        
        translate(x+30, y)  #petal 2
        rotate(radians(15))  
        draw_petal(0, 0, var)
        
        translate(-60, 15)  # petal 3
        rotate(radians(-30))  
        draw_petal(0, 0, var)
        
        var = var + 1
    
    if var2 > 19 and var2 < 90: #flower 2
        frameRate(20)
        fill(100,255,255)
        noStroke()
        rect(a-5, b+90, 10, var)
        
        var2= var2 + 10
          
    if var > 89 and var2 < 20:
        frameRate(30)
        global shape_color
        fill(shape_color)
        draw_petal(a, b, var2)
        
        translate(a+30, b)  #petal 2
        rotate(radians(15))  
        draw_petal(0, 0, var2)
        
        translate(-60, 15)  # petal 3
        rotate(radians(-30))  
        draw_petal(0, 0, var2)
        
        var2 = var2 + 1
    
    if var3 > 19 and var3 < 90: #flower 3
        frameRate(20)
        fill(100,255,255)
        noStroke()
        rect(c-5, d+90, 10, var)
        
        var3= var3 + 10
          
    if var2 > 89 and var3 < 20:
        frameRate(30)
        global shape_color
        fill(shape_color)
        draw_petal(c, d, var3)
        
        translate(c+30, d)  #petal 2
        rotate(radians(15))  
        draw_petal(0, 0, var3)
        
        translate(-60, 15)  # petal 3
        rotate(radians(-30))  
        draw_petal(0, 0, var3)
        
        var3 = var3 + 1
    
    if var4 > 19 and var4 < 90: #flower 4
        frameRate(20)
        fill(100,255,255)
        noStroke()
        rect(e-5, f+90, 10, var4)
        
        var4= var4 + 10
          
    if var3 > 89 and var4 < 20:
        frameRate(30)
        global shape_color
        fill(shape_color)
        draw_petal(e, f, var4)
        
        translate(e+30, f)  #petal 2
        rotate(radians(15))  
        draw_petal(0, 0, var4)
        
        translate(-60, 15)  # petal 3
        rotate(radians(-30))  
        draw_petal(0, 0, var4)
        
        var4 = var4 + 1
    
    # Flower 5
    if var5 > 19 and var5 < 90:
        frameRate(20)
        fill(100, 255, 255)
        noStroke()
        rect(g - 5, h + 90, 10, var5)
        var5 = var5 + 10

    if var4 > 89 and var5 < 20:
        frameRate(30)
        fill(shape_color)
        draw_petal(g, h, var5)

        translate(g + 30, h)  # Petal 2
        rotate(radians(15))
        draw_petal(0, 0, var5)

        translate(-60, 15)  # Petal 3
        rotate(radians(-30))
        draw_petal(0, 0, var5)

        var5 = var5 + 1
        
    # Flower 6
    if var6 > 19 and var6 < 90:
        frameRate(20)
        fill(100, 255, 255)
        noStroke()
        rect(i - 5, j + 90, 10, var6)
        var6 = var6 + 10

    if var5 > 89 and var6 < 20:
        frameRate(30)
        fill(shape_color)
        draw_petal(i, j, var6)

        translate(i + 30, j)  # Petal 2
        rotate(radians(15))
        draw_petal(0, 0, var6)

        translate(-60, 15)  # Petal 3
        rotate(radians(-30))
        draw_petal(0, 0, var6)

        var6 = var6 + 1
    
        # Flower 7
    if var7 > 19 and var7 < 90:
        frameRate(20)
        fill(100, 255, 255)
        noStroke()
        rect(k - 5, l + 90, 10, var7)
        var7 = var7 + 10

    if var6 > 89 and var7 < 20:
        frameRate(30)
        fill(shape_color)
        draw_petal(k, l, var7)

        translate(k + 30, l)  # Petal 2
        rotate(radians(15))
        draw_petal(0, 0, var7)

        translate(-60, 15)  # Petal 3
        rotate(radians(-30))
        draw_petal(0, 0, var7)

        var7 = var7 + 1
    
        # Flower 8
    if var8 > 19 and var8 < 90:
        frameRate(20)
        fill(100, 255, 255)
        noStroke()
        rect(m - 5, n + 90, 10, var8)
        var8 = var8 + 10

    if var7 > 89 and var8 < 20:
        frameRate(20)
        fill(shape_color)
        draw_petal(m, n, var8)

        translate(m + 30, n)  # Petal 2
        rotate(radians(15))
        draw_petal(0, 0, var8)

        translate(-60, 15)  # Petal 3
        rotate(radians(-30))
        draw_petal(0, 0, var8)

        var8 = var8 + 1
        
# Draw petal
def draw_petal(x, y, size):
    noStroke()
    for i in range(2, size):
        ellipse(x, y + i * 4, i * 2, i * 2)
    
def draw_backing():
    frameRate(60)
    colorMode(HSB)
    global cx
    global cy
    global r
    global c
    global theta
    global px
    global py
    global plea
    translate(-200,-100)
    x = cx + sin(theta) * r
    y = cy + cos(theta) * r
    
    strokeWeight(20)
    stroke(80,c,255)
    triangle(px, py, x, y, px, py)
    
    fill(c,255,255)
    #circle(960, 540, 50)
    r = r+1
    c = (c+1) % 256
    theta = theta + 900
    
    px = x
    py = y
    
def draw_MSX():
    colorMode(RGB)
    #translate(200,100)
    global center, xa, latency,opacC,radius1,radius2, radius3, centerx1,centerx2,centery1,centery2,cx1,cx2,cx3,cx4,cy1,cy2,cy3,cy4,ax,centeroy1,centeroy2
    latency=latency+1
    noStroke()
    fill(60,56,138)
    rect(200,0,200,1080)
    rect(1520,0,300,1080)
    
    rect(0,0,1920,300)
    rect(0,730,1920,300)
    
    translate(200,100)
    
    noStroke()
    if latency==16:
        background(0,0,0)
        if xa<8:
            originX=192+x*54
            fill(43,42,41)
            rect(240,originX,1016,54)
            xa=xa+1
        else:
            xa=xa+1
        
        if xa>10:
            fill(255,255,255)
            #M
            quad(258,556,354,556,402,394,354,278)
            quad(354,278,450,556,546,556,450,278)
            quad(450,556,546,556,642,278,546,278)
            quad(642,278,546,278,642,556,738,556)
            
            #S
            quad(642,556,834,556,834,484,642,484)
            quad(834,390,834,436,828,436,828,390)
            
            while ax<90:
                cx1=centerx1+sin(ax)*radius1+1
                cx2=centerx1+sin(ax)*radius1
                cx3=centerx1+sin(ax)*radius2
                cx4=centerx1+sin(ax)*radius2
                cy1=centery1+cos(ax)*radius1+1
                cy2=centery1+cos(ax)*radius1
                cy3=centeroy1+cos(ax)*radius2
                cy4=centeroy1+cos(ax)*radius2+1
                
                if sin(ax)>0:
                    quad(cx1,cy1,cx2,cy2,cx3,cy3,cx4,cy4)
                ax=ax+0.005
            ax=0
            
            while ax<90:
                cx1=centerx2+sin(ax)*radius1+1
                cx2=centerx2+sin(ax)*radius1
                cx3=centerx2+sin(ax)*radius3
                cx4=centerx2+sin(ax)*radius3
                cy1=centery2+cos(ax)*radius1+1
                cy2=centery2+cos(ax)*radius1
                cy3=centeroy2+cos(ax)*radius3
                cy4=centeroy2+cos(ax)*radius3+1
                
                if sin(ax)<0:
                    quad(cx1,cy1,cx2,cy2,cx3,cy3,cx4,cy4)
                ax=ax+0.005
            
                
            quad(828,278,1020,278,1020,342,828,342)
            
            #X
            quad(924,278,1020,278,1212,556,1116,556)
            quad(924,556,1020,556,1212,278,1116,278)
            
        latency=0

def draw_ohgod():
    colorMode(HSB)
    global rb
    global rc
    global rd
    fill(90, 255, 255)
    stroke(0, 130, 0)
    ellipse(rb, 540, rc, rd)
    #left leaf
    rb = rb - 0.2
    rc = rc + 0.3
    rd = rd + 0.2
    
    global re
    global rf
    global rg
    ellipse(re, 540, rf, rg)
    #right leaf
    re = re + 0.2
    rf = rf + 0.3
    rg = rg + 0.2
    
    global ra
    fill(90,255,255)
    stroke(0, 190, 0)
    circle(960, 540, ra)
    #stem of the flower
    ra = ra + 0.1
    
    global rn
    global ro
    stroke (0, 120, 0)
    line(rn, 540, ro, 540)
    line(rn + 5, 541, ro ,541)
    line(rn + 5, 539, ro, 539)
    #main vein left leaf
    rn = rn - 0.3
    ro = ro - 0.06
    
    global rp
    global rq
    line(rp, 540, rq, 540)
    line(rp - 5, 541, rq ,541)
    line(rp - 5, 539, rq, 539)
    #main vein right leaf
    rp = rp + 0.3
    rq = rq + 0.06
    
    global rra
    global rrb
    global rrc
    global rrd
    rrd = rrd + 0.0004
    fill(0,255,255)
    stroke(170,0,0)
    circle(rra, rrb, rrc)
    #top left flower petal
    rra = rra - rm
    rrb = rrb - rm
    rrc = rrc + rrd
    
    global rre
    global rrf
    global rrg
    circle(rre, rrf, rrg)
    #bottem left flower petal
    rre = rre - rm
    rrf = rrf + rm
    rrg = rrg + rrd
    
    global rrh
    global rri
    global rrj
    circle(rrh, rri, rrj)
    #top right flower petal
    rrh = rrh + rm
    rri = rri - rm
    rrj = rrj + rrd
    
    global rrk
    global rrl
    global rrm
    circle(rrk, rrl, rrm)
    #bottem right flower petal
    rrk = rrk + rm
    rrl = rrl + rm
    rrm = rrm + rrd
    
    global rh
    global ri
    global rj
    global rk
    global rl
    global rm
    rk = rk + 0.0006
    rl = rl + 0.0004
    rm = rm + 0.0003
    fill(0,255,255)
    stroke(170,0,0)
    ellipse(rj, 540, rh, ri)
    #left petal of flower
    rh = rh - rk
    ri = ri + rl
    rj = rj - rm
    
    global rr
    global rs
    global rt
    ellipse(rr, 540, rs, rt)
    #right petal flower
    rr = rr + rm
    rs = rs + rk
    rt = rt - rl
    
    global ru
    global rv
    global rw
    ellipse(960, ru, rv, rw)
    #top petal flower
    ru = ru - rm
    rv = rv + rl
    rw = rw + rk
    
    global rx
    global ry
    global rz
    ellipse(960, rx, ry, rz)
    #bottem petal flower
    rx = rx + rm
    ry = ry + rl
    rz = rz + rk
    
    global rrn
    global rro
    global rrp
    global rrq
    stroke(150, 0, 0)
    line(960, 540, 960, rrn)
    line(961, 540, 961, rrn + 3)
    line(959, 540, 959, rrn + 3) 
    #main line up
    
    line(960, 540, rro, 540)
    line(960, 541, rro - 3, 541)
    line(960, 539, rro - 3, 539) 
    #main line right
    
    line(960, 540, 960, rrp) 
    line(961, 540, 961, rrp - 3) 
    line(959, 540, 959, rrp - 3)     
    #main line down
    
    line(960, 540, rrq, 540) 
    line(960, 541, rrq + 3, 541)
    line(960, 539, rrq + 3, 539)
    #main line left
    rrn = rrn - rl
    rro = rro + rl
    rrp = rrp + rl
    rrq = rrq - rl
    
    global rrr
    fill(180, 0, 0)
    stroke(180, 0, 0)
    circle(960, 540, rrr)
    rrr = rrr + rm
    #inner flower circle 1
    
    fill(170, 0, 0)
    stroke(170, 0, 0)
    circle(960, 540, rrr - 5)
    #inner flower circle 2
    
    fill(160, 0, 0)
    stroke(160, 0, 0)
    circle(960, 540, rrr - 10)
    #inner flower circle 3
    
    fill(150, 0, 0)
    stroke(150, 0, 0)
    circle(960, 540, rrr - 15)
    #inner flower circle 4
    
    fill(140, 0, 0)
    stroke(140, 0, 0)
    circle(960, 540, rrr - 20)
    #inner flower circle 5
    
    fill(130, 0, 0)
    stroke(120, 0, 0)
    circle(960, 540, rrr - 25)
    #inner flower circle 6
    
    fill(100, 0, 0)
    stroke(100, 0, 0)
    circle(960, 540, rrr - 30)
    #inner flower circle 7
