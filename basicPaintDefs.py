#basicPaintDefs.py
# from pygame import * 
from Colours import * 
# from random import *
# from math import *
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

def ellipseDrawTool(surf, mx, my, canvas_copy, sx, sy, col, thicknessX):
	mx>=sx and my>=sy
	dx=hypot(mx,sx)
	dy=hypot(my,sy)
	ellipseRect= Rect(sx,sy,dx,dy)
	ellipseRect.normalize()
	surf.blit(canvas_copy,(0,0))
	draw.ellipse(surf,col,(sx,sy,dx,dy),thicknessX)

def filledEllipseDrawTool(surf, mx, my, canvas_copy, sx, sy, col):
	mx>=sx and my>=sy
	dx=hypot(mx,sx)
	dy=hypot(my,sy)
	ellipseRect= Rect(sx,sy,dx,dy)
	ellipseRect.normalize()
	surf.blit(canvas_copy,(0,0))
	draw.ellipse(surf,col,(sx,sy,dx,dy))

def rectDrawTool(surf, mx, my, canvas_copy, sx, sy, col, thicknessX):
	mx>=sx and my>=sy
	dx=hypot(mx,sx)
	dy=hypot(my,sy)
	rectRect= Rect(sx,sy,dx,dy)
	rectRect.normalize()
	surf.blit(canvas_copy,(0,0))
	draw.rect(surf,col,(sx,sy,dx,dy),thicknessX)

def filledRectDrawTool(surf, mx, my, canvas_copy, sx, sy, col):
	mx>=sx and my>=sy
	dx=hypot(mx,sx)
	dy=hypot(my,sy)
	rectRect= Rect(sx,sy,dx,dy)
	rectRect.normalize()
	surf.blit(canvas_copy,(0,0))
	draw.rect(surf,col,(sx,sy,dx,dy))
	