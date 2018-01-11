from pygame import * 
size=(800,600)
screen = display.set_mode(size) 
                                 
running = True
while running:
    for evt in event.get():  
        if evt.type == QUIT: 
            running = False
        if evt.type == KEYDOWN:
        	if evt.key == K_ESCAPE:
        		running = False
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    
    draw.ellipse(screen,(0,255,0),Rect(100,100,90,70),1)                     
    
    display.flip() 
quit() 