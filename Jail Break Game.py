
#Kryptix Incorporation
#Roy, Nick, Kennen, Mia

#Jail Break
#Jail Break is about a famed escapist, named Jack Wellington, who is caught in Essex and has to escape to regain his lost freedom.
#He does this by passing through 3 levels, each filled with different bosses.
#@coypright 2019 krytpix incoorpertions


from gamelib_1 import*



#objects
game=Game(800,600,"Jail Break")
pony=Sound("Pony.WAV",1)
elevator=Sound("elevator.WAV",2)
ace=Sound("ace.WAV",3)
herof=Animation("prisoner.gif",8,game,864/8,140,3)
herof.resizeBy(-25)

herof.moveTo(190,540)


bk=Image("PrisonBackground.jpg",game)

bk.resizeTo(game.width, game.height)
game.setBackground(bk)


logo=Image("logo.png",game)
logo.y=100
logo.resizeBy(30)


story=Image("story.png", game)
story.y=263
story.resizeBy(30)


hop=Image("HOP.png",game)
hop.y=342
hop.resizeBy(30)

play=Image("play.png",game)
play.y=420
play.resizeBy(30)
si=Image("storyImage.png",game)
si.resizeTo(game.width,game.height)
si.draw()
si.visible=False
game.setMusic("frosty.WAV")
jumping = False #used to see if you are jumping
landed = False #used to see if you gaved landed on the ground
factor = 1 #used for a slow effect of the jumping
game.distance=1000
plat=[]
boss1=[]
boss2=[]
boss3=[]
boss4=[]
bomb=[]
boom=[]
distance=5000

for index in range(5):
    
    plat.append(Image("Plat.png",game))

for index in range(5):
    x=randint(100,1200)
    y=randint(100,500)
    plat[index].moveTo(950,y)
    plat[index].resizeBy(-85)
    plat[index].setSpeed(3,90)


for index in range(5):
    
    boom.append(Image("explosion.png",game))

for index in range(5):
    x=randint(100,400)
    y=randint(100,500)
    boom[index].moveTo(950,y)
    boom[index].setSpeed(9,90)

for index in range(50):
    
    boss1.append(Image("Boss1.png",game))

for index in range(50):
    x=randint(1000,15000)
    y=randint(100,600)
    boss1[index].moveTo(x,y)
    boss1[index].resizeBy(-85)
    boss1[index].setSpeed(4,90)


for index in range(50):
    
    boss2.append(Image("boss2.png",game))

for index in range(5):
    x=randint(100,400)
    y=randint(100,600)
    boss2[index].moveTo(x,y)
    boss2[index].resizeBy(-50)
    boss2[index].setSpeed(3,90)


for index in range(50):
    
    boss3.append(Image("boss3.png",game))

for index in range(5):
    x=randint(950,1500)
    y=randint(100,700)
    boss3[index].moveTo(x,y)
    boss3[index].resizeBy(-80)
    boss3[index].setSpeed(9,90)

for index in range(50):
    
    boss4.append(Image("boss4.png",game))

for index in range(5):
    x=randint(950,1500)
    y=randint(100,600)
    boss4[index].moveTo(x,y)
    boss4[index].resizeBy(-70)
    boss4[index].setSpeed(9,90)

for index in range(5):
    
    bomb.append(Image("Bomb.png",game))

for index in range(5):
    x=randint(100,400)
    y=randint(100,500)
    bomb[index].moveTo(-950,y)
    bomb[index].resizeBy(-85)
    bomb[index].setSpeed(9,270)








while not game.over: #title screen
    ace.play()
    game.processInput()
    bk.draw()
    logo.draw()
    story.draw()
    hop.draw()
    play.draw()

 
    if play.collidedWith(mouse) and mouse.LeftButton:
        game.over=True
    
    
    if si.collidedWith(mouse) and mouse.LeftButton:
        si.visible=True
        bk.visible=False
        logo.visible=False
        story.visible=False
        hop.visible=False
        play.visible=False

    
 
    game.update(30)   
game.over=False




#Level 1
while not game.over: #essential game loop
    pony.play()
    game.processInput()
    bk.draw()
    game.scrollBackground("left",0)
    herof.draw()
    herof.stop()
    if distance<0:
        game.over=True
    if distance<1000:
        ace.play()
    

    for index in range(len(boss1)):
        if boss1[index].collidedWith(herof):
            herof.health-=1
            boss1[index].visible=False

    for index in range(len(boss2)):
        if boss2[index].collidedWith(herof):
            herof.health-=3
            boss2[index].visible=False

    for index in range(len(boss3)):
        if boss3[index].collidedWith(herof):
            herof.health-=2
            boss3[index].visible=False
            
                       
                       
    


        
    for index in range(5):
        plat[index].move()

        if plat[index].isOffScreen("left"):
            y=randint(100,500)
            plat[index].moveTo(950,y)
            

    for index in range(50):
        boss1[index].move()

        if boss1[index].isOffScreen("left"):
            
            y=randint(100,500)
            x=randint(1000,12000)
            boss1[index].moveTo(x,y)

    for index in range(50):
        boss3[index].move()

        if boss3[index].isOffScreen("left"):
            
            y=randint(100,700)
            x=randint(1000,1200)
            boss3[index].moveTo(x,y)

    for index in range(50):
        boss2[index].move()

        if boss2[index].isOffScreen("left"):
            y=randint(100,600)
            x=randint(1000,1200)
            boss2[index].moveTo(x,y)

    for index in range(5):
        boss4[index].move()

        if boss4[index].isOffScreen("left"):
            y=randint(100,600)
            x=randint(1000,1200)
            boss4[index].moveTo(x,y)

    #for index in range(5):
            #boom[index].move()

            #if boom[index].isOffScreen("left"):
             #   y=randint(100,700)
              #  x=randint(-100,-1200)
              #  boom[index].moveTo(x,y)

    for index in range(5):
            bomb[index].move()

            if bomb[index].isOffScreen("left"):
                bomb[index].setSpeed(9,90)
                y=randint(100,700)
                x=randint(100,1950)
                bomb[index].moveTo(x,y)

        
            
            
            

    if herof.y<540:
        landed=False

    else:
        landed=True

    if keys.Pressed[K_SPACE] and landed and not jumping:
        jumping=True
    if jumping:

        herof.y-=27*factor
        factor*=.95
        landed=False
        if factor<.18:
            jumping=False
            factor=1
    if not landed:
        herof.y+=6


    
     
        
    if keys.Pressed[K_RIGHT]:
        distance-=3
        game.scrollBackground("left",10)
        herof.draw()
        herof.nextFrame()
        for index in range(5):
            plat[index].move()

            if plat[index].isOffScreen("left"):
                y=randint(100,700)
                x=randint(100,1500)
                plat[index].moveTo(x,y)

        for index in range(50):
            boss1[index].move()

            if boss1[index].isOffScreen("left"):
                y=randint(100,700)
                x=randint(5000,15000)
                boss1[index].moveTo(x,y)

        for index in range(5):
            boss3[index].move()

            if boss3[index].isOffScreen("left"):
                y=randint(100,700)
                x=randint(1000,1500)
                boss3[index].moveTo(x,y)

        for index in range(50):
            boss2[index].move()

            if boss2[index].isOffScreen("left"):
                boss2[index].visible=True
                y=randint(100,700)
                x=randint(5000,7000)
                boss2[index].moveTo(x,y)

        for index in range(5):
            boss4[index].move()

            if boss4[index].isOffScreen("left"):
                y=randint(100,700)
                x=randint(1000,3500)
                boss4[index].moveTo(x,y)

        for index in range(5):
            bomb[index].move()

            if bomb[index].isOffScreen("left"):
                y=randint(100,700)
                x=randint(950,1500)
                bomb[index].moveTo(x,y)



    if boss1[index].collidedWith(herof):
        herof.health-=10
        boss1[index].visible=False
    if boss2[index].collidedWith(herof):
            herof.health-=1
            boss2[index].visible=False

    if boss3[index].collidedWith(herof):
        herof.health-=1
        boss3[index].visible=False

    if boss4[index].collidedWith(herof):
        boss4[index].visible=False
        
    if bomb[index].collidedWith(herof):
        boss1[index].visible=False
        boss2[index].visible=False
        boss3[index].visible=False
        boom[index].moveTo(herof.x,herof.y)

    if boom[index].collidedWith(boss1[index]):
        boss1[index].visible=False
    if boom[index].collidedWith(boss2[index]):
        boss2[index].visible=False
    if boom[index].collidedWith(boss3[index]):
        boss3[index].visible=False 
        

       
            

        
        
        
    if keys.Pressed[K_LEFT]:
        distance-=3
        game.scrollBackground("right",10)
        herof.draw()
        herof.nextFrame()
        for index in range(5):
            plat[index].move()

            if plat[index].isOffScreen("left"):
                y=randint(100,700)
                x=randint(1000,1500)
                plat[index].moveTo(x,y)


        for index in range(50):
            boss1[index].move()

            if boss1[index].isOffScreen("left"):
                y=randint(100,700)
                x=randint(1000,1200)
                boss1[index].moveTo(x,y)

        for index in range(5):
            boss3[index].move()

            if boss3[index].isOffScreen("left"):
                y=randint(100,700)
                x=randint(1000,1500)
                boss3[index].moveTo(x,y)

        for index in range(5):
            boss2[index].move()

            if boss2[index].isOffScreen("left"):
                y=randint(100,700)
                x=randint(1000,1500)
                boss2[index].moveTo(x,y)

        for index in range(5):
            boss4[index].move()

            if boss4[index].isOffScreen("left"):
                y=randint(100,700)
                x=randint(1000,1500)
                boss4[index].moveTo(x,y)

        for index in range(5):
            bomb[index].move()

            if bomb[index].isOffScreen("left"):
                y=randint(100,700)
                x=randint(1000,1500)


                bomb[index].moveTo(x,y)
        if boss1[index].collidedWith(herof):
            herof.health-=1
            boss1[index].visible=False
        if boss2[index].collidedWith(herof):
            herof.health-=1
            boss2[index].visible=False
        if boss3[index].collidedWith(herof):
            herof.health-=1
            boss3[index].visible=False

        
        if bomb[index].collidedWith(boss1[index]):
            boss1[index].visible=False
            boss2[index].visible=False
            boss3[index].visible=False
            boom[index].moveTo(bomb.x,bomb.y)

        if bomb[index].collidedWith(boss2[index]):
            boss1[index].visible=False
            boss2[index].visible=False
            boss3[index].visible=False
            boom[index].moveTo(bomb.x,bomb.y)

        if bomb[index].collidedWith(boss3[index]):
            boss1[index].visible=False
            boss2[index].visible=False
            boss3[index].visible=False
            boom[index].moveTo(bomb.x,bomb.y)


        
        

    
    game.drawText("Level 2", 740, 5)
    game.drawText("hero's health:"+str(herof.health),550,20)
    game.drawText("distance away from exit"+str(distance),550,40)
    game.drawText("Objective:SURIVIE",550,60)
    
    if herof.collidedWith(boss1[index]):
        herof.health=100000
        herof.health-=1

    if herof.collidedWith(boss2[index]):
        herof.health-=3

    if herof.collidedWith(bomb[index]):
        boom[index].moveTo(herof.x,herof.y)

    if herof.health<1:
        game.over=True

    
    game.update(30)

game.over=False
game.quit()

#Level 2

while not game.over:
    game.processInput()



    game.update(30)

game.over=False


#End Screen
while not game.over:
    game.processInput()



    game.update(30)


game.over=False
  
    
