from pygame import * 
from tkinter import *
from tkinter import filedialog
font.init()
size=(1000,1000)
screen = display.set_mode(size) 

init()
root = Tk()
root.withdraw()

OK = False
text = ""

timesNewRomanFont=font.SysFont("Times New Roman", 18)
myText=timesNewRomanFont.render("Massey",True,(255,255,255))#render creates a picture


infoBar=Surface((500,20),SRCALPHA)#info bar is our "sticky note"
infoRect=Rect(0,0,500,20)
openRect=Rect(770,280,40,40)
saveRect=Rect(820,280,40,40)
entRect=Rect(0,0,1000,1000)
draw.rect(infoBar, (255,255,255,10),infoRect)

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
			pass		
	mx,my=mouse.get_pos()
	mb=mouse.get_pressed()
	
	draw.rect(screen,(255,0,0),saveRect)							
	
	draw.rect(screen,(0,255,0),openRect)							
	if mb[0]:
		def ok(e, root):
			user = e.get()
			# print(user)
			root.withdraw()
			root.destroy()
			root.quit()
			# tool='paint'
			text = user
			print(text)
			OK=True
			if OK==False:
				root = Tk()
				e = Entry(root)
				e.pack()
				b=Button(root, text='OK', command=lambda:ok(e,root))
				b.pack()
				root.mainloop()
		userText=timesNewRomanFont.render(text,True,(255,255,255))
		screen.blit(userText, (0,0))
		
		
	
	display.flip() 
quit() 
