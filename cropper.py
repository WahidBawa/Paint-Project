from pygame import *
from Defs import *
size=(800,600)
screen = display.set_mode(size) 
def rectDrawTool(surf, sx, sy, mx, my, copy):
	screen.blit(copy, (0,0))
	draw.rect(surf, (255,255,255), (sx,sy,mx-sx,my-sy), 1*2)# draws a rectangle using the mouse
	draw.circle(surf, (255,255,255), (sx,sy), 5)# draws a circle at the corners
	draw.circle(surf, (255,255,255), (mx,my), 5)# draws a circle at the corners
	draw.circle(surf, (255,255,255), (mx,sy), 5)# draws a circle at the corners
	draw.circle(surf, (255,255,255), (sx,my), 5)# draws a circle at the corners

running = True
while running:
	for evt in event.get():  
		if evt.type == QUIT: 
			running = False
		if evt.type == KEYDOWN:
			if evt.key == K_ESCAPE:
				running = False    
		if evt.type == MOUSEBUTTONDOWN:
			if evt.button == 1:
				sx, sy = mx, my
				copy  = screen.copy()
				print(sx, sy)
	mx,my = mouse.get_pos()
	mb = mouse.get_pressed()

	if mb[0]:
		rectDrawTool(screen, sx, sy, mx, my, copy)

	display.flip() 
quit()	