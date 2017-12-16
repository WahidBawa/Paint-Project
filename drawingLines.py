#drawingLines.py

#you can use this example to draw rectangle, ellipse....

from pygame import * 
size=(800,600)
screen = display.set_mode(size) 
thickness=5                               
running = True
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
            if evt.button == 3:
                screen.fill(0)
            if evt.button==4:
                #print("scrolling up")
                thickness+=1
                
            if evt.button==5:
                #print("scrolling down")
                thickness-=1

    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()


    if mb[0]:
        screen.blit(backPic,(0,0))
        if my-sy < 0 and mx-sx < 0:
            draw.ellipse(screen,(0,255,0),(int((mx+sx)/2),int((my+sy)/2)),max(int(sx-mx),int(sy-my))//2)
        else:    
            draw.ellipse(screen,(0,255,0),(int((mx+sx)/2),int((my+sy)/2)),max(int(mx-sx),int(my-sy))//2)

    display.flip() 
quit() 
