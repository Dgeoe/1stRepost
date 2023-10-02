def setup():
    size(500,500)
    background(0)
    global x
    x= width/2
    global y
    y= height/2
    
def draw():
    background(0)
    noStroke()
    colorMode(HSB)
    
    if mouseX < x and mouseY < y:
        fill(255,255,255)
        rect(0,0,y,x)
    
    elif mouseX < x  and mouseY > y:
        fill(255,255,255)
        rect(0,y,x,height)
    
    elif mouseX > x and mouseY < y:
        fill(255,255,255)
        rect(y,0,x,y)
    
    else: 
        fill(255,255,255)
        rect(x,y,y,x)
        

        

        

    
            
        
    
