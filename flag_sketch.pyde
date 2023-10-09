#trig problem 3 digital sketch
def setup():
    size(500,500)
    background(0)
    global mouseX
    global mouseY
    
def draw():
    background(255)
    fill(0,0,0)
    textAlign(LEFT)
    text("53", 200, 220)
    noFill()
    triangle(200,200,200,250,250,250)
    fill(0,0,0)
    text("12", 215, 265)
    fill(0,0,0)
    textAlign(LEFT)
    text("Soh Cah Toa", 195, 150)
    rect(170,200,2,50)
    colorMode(HSB)
    fill(0,255,255)
    triangle(150, 215, 170, 200, 170, 225)
    textAlign(CENTER)
    text("x", 190, 230)
    fill(255,255,255)
