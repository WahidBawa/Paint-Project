from pygame import * 
init()
font.init()
size=(800,600)
screen = display.set_mode(size) 

timesNewRomanFont=font.SysFont("Times New Roman", 18)
myText=timesNewRomanFont.render("Massey",True,(255,255,255))#render creates a picture
infoBar=Surface((500,20),SRCALPHA)#info bar is our "sticky note"
infoRect=Rect(0,0,500,20)
draw.rect(infoBar, (150,150,150,10),infoRect)


infoBar.blit(myText, (200,0))#writing massey on the info bar surface
screen.blit(infoBar,(200,20))
# rotText=transform.rotate(myTextPIC1, 45)
# screen.blit(myTextPIC1,(300,200))
# screen.blit(rotText,(300,300))
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
							
	# if mb[0]:
		# screen.blit(myTextPIC1,(300,200))
		# screen.blit(rotText,(300,300))

	display.flip() 
quit() 
