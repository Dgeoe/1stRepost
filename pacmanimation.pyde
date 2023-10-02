def setup():
    size(500,500)
    background(0)
    global x
    x= width/2
    global y
    y= height/2
    
x=250
y=250
a=250
b=250
c= 50
d= 30
e= 50
f= 75
g= 20
h= 75
i=80
j=75
k=35
l=20
m=65
n=20
o=50
p=45

def draw():
    background(0)
    colorMode(HSB)
    noStroke()
    global x
    global y
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global j
    global k
    global l
    global m
    global n
    global o
    global p
    fill(45,255,255)
    circle(x,y,100)
    fill(255,255,0)
    rect(a,b,100,100)
    fill(180,255,255)
    circle(c,d,80)
    fill(180,255,255)
    ellipse(e,f,20,40)
    fill(180,255,255)
    ellipse(g,h,20,40)
    fill(180,255,255)
    ellipse(i,j,20,40)
    fill(0,0,255)
    ellipse(k,l,10,20)
    fill(0,0,255)
    ellipse(m,n,10,20)
    fill(0,0,255)
    ellipse(o,p,20,10)
    x= x+1
    y= y+1
    a= a+1
    b= b+1
    c= c+1
    d= d+1
    e= e+1
    f= f+1
    g= g+1
    h= h+1
    i= i+1
    j= j+1
    k= k+1
    l= l+1
    m= m+1
    n= n+1
    o= o+1
    p= p+1
    
    if x == 600 and y == 600:
        noStroke()
        fill(180,255,255)
        circle(x,y,100)
        fill(255,255,0)
        rect(a,b,100,100)
        x= x-600
        y= y-600
        a= a-600
        b= b-600
        
    if c == 600:
        noStroke()
        fill(180,255,255)
        circle(c,d,80)
        fill(180,255,255)
        ellipse(e,f,20,40)
        fill(180,255,255)
        ellipse(g,h,20,40)
        fill(180,255,255)
        ellipse(i,j,20,40)
        fill(0,0,255)
        ellipse(k,l,10,20)
        fill(0,0,255)
        ellipse(m,n,10,20)
        fill(0,0,255)
        ellipse(o,p,20,10)
        c= c-600
        d= d-600
        e= e-600
        f= f-600
        g= g-600
        h= h-600
        i= i-600
        j= j-600
        k= k-600
        l= l-600
        m= m-600
        n= n-600
        o= o-600
        p= p-600
        
        
        
   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
