#Our class function file
def polygon(t,d,s):
    a = 360/s
    for times in range(s):
        t.forward(d)
        t.right(a)
def polygonFill(t,s,d):
    a = 360 / sides
    t.begin_fill()
    for times in range(s):
            t.forward(d)
            t.right(a)
    t.end_fill()

def moveTo(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def hyperspace(t,x,y):
    for times in range(100):
        t.color(0,0+times*2,150)
        t.forward(20)
        t.right(1)
        t.forward(10)
        moveTo(t,x,y)
        t.right(25)
        t.forward(10)
        t.right(25)
        t.penup()
        t.forward(20)
        t.pendown()
        t.forward(20)
        t.right(40)
        t.forward(30)
        moveTo(t,x,y)


def semicircle(t):

    for times in range(179):
        t.forward(1)
        t.right(1)


        
    
        
      
