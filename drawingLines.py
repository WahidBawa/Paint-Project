#drawingLines.py

#you can use this example to draw rectangle, ellipse....

from pygame import *
from math import *
size=(800,600)
screen = display.set_mode(size) 
thickness=5                               
running = True
display.set_caption("Line Tool")
while running:
    for evt in event.get():  
        if evt.type == QUIT: 
            running = False
        if evt.type == KEYDOWN:
            if evt.key == K_ESCAPE:
                running=False    
        if evt.type==MOUSEBUTTONDOWN:
            sx,sy=mouse.get_pos()#starting position
            backPic=screen.copy()#screen capture (screenshot)
            if evt.button==4:
                #print("scrolling up")
                thickness+=1
                
            if evt.button==5:
                #print("scrolling down")
                thickness-=1

    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()


    if mb[0]==1:
        screen.blit(backPic,(0,0))
                                #start  current
        deltaX, deltaY=((mx-sx), (my-sy))
        dist = max(hypot(deltaX, deltaY), 1)
        angle = atan2(deltaY,deltaX)
        drawx, drawy = cos(angle), sin(angle)
        for p in range(round(dist)):
            draw.circle(screen,(0,255,0),((sx+round(drawx*p)),sy+round(drawy*p)),thickness)
    
    display.flip() 
quit() 
