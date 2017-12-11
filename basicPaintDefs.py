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

def lineDrawTool(surf, mx, my, cmx, cmy, thicknessY, col, canvas_copy):
	cmx, cmy= mx-150, my-100
	ocmx, ocmy= mx-150, my-100
	canvas.blit(canvas_copy, (0,0))
	draw.line(canvas,col,(cmx,cmy),(ocmx,ocmy),thicknessY)