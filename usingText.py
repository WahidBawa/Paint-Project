from pygame import * 
init()
font.init()
size=(800,600)
screen = display.set_mode(size) 

timesNewRomanFont=font.SysFont("Times New Roman", 40)
comicFont=font.SysFont("Comic Sans MS", 40)
words=['q','w','e','r','t','y']
myTextPIC1=timesNewRomanFont.render("Massey is a good school",True,(0,255,0))#render creates a picture
rotText=transform.rotate(myTextPIC1, 45)
screen.blit(myTextPIC1,(300,200))
screen.blit(rotText,(300,300))
running = True
while running:
	for evt in event.get():  
		if evt.type == QUIT: 
			running = False
		if evt.type == KEYUP:
			if evt.key == K_ESCAPE:
				running=False    

	mx,my=mouse.get_pos()
	mb=mouse.get_pressed()
							
	if mb[0]:
		screen.blit(myTextPIC1,(300,200))
		screen.blit(rotText,(300,300))

	display.flip() 
quit() 
