#basicPaintDefs.py
from pygame import * 
from Colours import * 
from random import *
from math import *
def painter(surf, cmx, cmy, ocmx, ocmy,thicknessX,col,randomCol): 
	if randomCol==True:
		deltaX, deltaY=((cmx-ocmx), (cmy-ocmy))
		dist = max(hypot(deltaX, deltaY), 1)
		angle = atan2(deltaY,deltaX)
		drawx, drawy = cos(angle), sin(angle)
		for p in range(round(dist)):
			draw.circle(surf,(randint(0,255),randint(0,255),randint(0,255)),(ocmx+round(p*drawx),ocmy+round(p*drawy)),thicknessX)

	else:
		deltaX, deltaY=((cmx-ocmx), (cmy-ocmy))
		dist = max(hypot(deltaX, deltaY), 1)
		angle = atan2(deltaY,deltaX)
		drawx, drawy = cos(angle), sin(angle)
		for p in range(round(dist)):
			draw.circle(surf,col,((ocmx+round(drawx*p)),ocmy+round(drawy*p)),thicknessX)

def eraser (surf, cmx, cmy, ocmx, ocmy,thicknessX):    
	deltaX, deltaY=((cmx-ocmx), (cmy-ocmy))
	dist = max(hypot(deltaX, deltaY), 1)
	angle = atan2(deltaY,deltaX)
	drawx, drawy = cos(angle), sin(angle)
	for p in range(round(dist)):
		draw.circle(surf,WHITE,((ocmx+round(drawx*p)),ocmy+round(drawy*p)),thicknessX)

def lineDrawTool(surf, mx, my, canvas_copy, sx, sy, col, thicknessX):
	surf.blit(canvas_copy,(0,0))
	deltaX, deltaY=((mx-sx), (my-sy))
	dist = max(hypot(deltaX, deltaY), 1)
	angle = atan2(deltaY,deltaX)
	drawx, drawy = cos(angle), sin(angle)
	for p in range(round(dist)):
		draw.circle(surf,col,((sx+round(drawx*p)),sy+round(drawy*p)),thicknessX)

def circleDrawTool(surf, mx, my, canvas_copy, sx, sy, col, thicknessX):
	surf.blit(canvas_copy,(0,0))
	if my-sy < 0 and mx-sx < 0:
		draw.circle(surf,col,(int((mx+sx)/2),int((my+sy)/2)),max(int(sx-mx),int(sy-my))//2)
	else:    
		draw.circle(surf,col,(int((mx+sx)/2),int((my+sy)/2)),max(int(mx-sx),int(my-sy))//2)