def setup():
    size(1000,1000)
    global cx
    global cy
    global r
    global c
    global x
    global y
    global px
    global py
    global theata
    cx= width/2
    cy= height/2
    background(0)
    
    px= cx
    py= cy

    colorMode(HSB)
    background(0)

# below is a circle spiral
#~cx= 0
#~cy= 0
#~r= 100
#~theata= 0

##def draw():
    #~global cx
    #~global cy
    #~global r
    #~global theata
    #~x= cx + sin(theata) * r
    #~y= cy + cos(theata) * r
    
    #~fill(255)
    #~circle(x,y,10)
    
    #~r= r + 1
    #~theata= theata + 0.2

#and now, code to spawn a line spiral
#~def draw(): 
  #~noFill() 
  #~stroke(255, 255, 255) 
  # loop to create 16 arcs 
  #~for i in range(16): 
    # if i is even 
    #~if i % 2 == 0: 
        #~arc(500, 525, 50+i*50, 50+i*50, HALF_PI, HALF_PI+PI) 
    ############################################################################
    # function to create an arc with center (500,525) 
    # and width and height as 50px and 50px respectively 
    # In each alternate iteration, the height and width of the arcs increases 
    # ^by 100px. 
    # The arc starts at 90 degrees, that is half times PI and end at 270 degrees 
    # ^^(90 + 180) <-- that is PI + half times PI 
    #############################################################################
    # if i is odd 
    #~else:
        #~arc(500, 500, 50+i*50, 50+i*50, HALF_PI+PI, HALF_PI + 2*PI) 
    #############################################################################
    # The arc starts at 270 degrees that is PI + half times PI and end at 450 
    # ^^degrees (90 + 360) that is 2 times PI + half times PI 
    #############################################################################
    
#what about code for a line sprial that shifts over time?
cx = 0 
cy= 0
r= 1
theata= 0

px= 0
py= 0
c= 0
x= 0
y= 0

def draw():
    global cx
    global cy
    global px
    global py
    global r
    global c
    global x
    global y
    global theata
    #x= cx + sin(theata) * r
    y= c + cos(theata) * r
    
    stroke(c,c,255,c)
    strokeWeight(20)
    line(px,py,x,y)
    r= r+1
    c= (c + 0.1) % 256
    theata = theata + 2
    px= x
    py = y
    x= x + 1
