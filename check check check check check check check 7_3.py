import turtle

bob=turtle.Turtle()


from myFunctions5  import*
turtle.colormode(255)
bob.speed(11)



moveTo(bob,0,0)

for times in range(100):
    bob.color(0,2*2,255)
    bob.forward(1)
    bob.right(times*5)
    bob.forward(100)
    bob.begin_fill()
    bob.circle(23)
    bob.end_fill()
    moveTo(bob,0,0)



for times in range(250):
    bob.color(0+times,0,0)
    bob.forward(150)
    bob.right(2)
    bob.forward(100)
    bob.circle(23)
    moveTo(bob,0,0)



for times in range(360):
    bob.penup()
    bob.color(160,160,160)
    bob.forward(250)
    bob.pendown()
    bob.right(2)
    bob.forward(50)
    bob.forward(300)

    bob.begin_fill()
    bob.circle(23)
    bob.end_fill()
    moveTo(bob,0,0)

for times in range(400):
    bob.color(255,255,255)
    bob.forward(100)
    bob.right(1)
    bob.forward(300)
    moveTo(bob,0,0)







    
    
    


