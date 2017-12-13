from pygame import * 
from tkinter import *

font.init()
size=(1000,1000)
screen = display.set_mode(size) 

init()
root = Tk()
root.withdraw()

timesNewRomanFont=font.SysFont("Times New Roman", 18)
myText=timesNewRomanFont.render("Massey",True,(255,255,255))#render creates a picture
infoBar=Surface((500,20),SRCALPHA)#info bar is our "sticky note"
infoRect=Rect(0,0,500,20)
openRect=Rect(770,280,40,40)
saveRect=Rect(820,280,40,40)
entRect=Rect(0,0,1000,1000)
draw.rect(infoBar, (150,150,150,10),infoRect)

entRect=surface

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
		if evt.type == MOUSEBUTTONDOWN:
			try:
				fname=filedialog.asksaveasfilename(defaultextension=".png")
				image.save(screen.subsurface(entRect), fname)#canvas.subsurface(canvasRect)
			except:
				print("saving error")			
	mx,my=mouse.get_pos()
	mb=mouse.get_pressed()
	
	draw.rect(screen,(255,0,0),saveRect)							
	
	draw.rect(screen,(0,255,0),openRect)							
	# if mb[0]:
		# screen.blit(myTextPIC1,(300,200))
		# screen.blit(rotText,(300,300))
	
	display.flip() 
quit() 
