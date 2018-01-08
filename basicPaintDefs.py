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
		draw.circle(surf,(255,255,255,0),((ocmx+round(drawx*p)),ocmy+round(drawy*p)),thicknessX)

def lineDrawTool(surf, mx, my, canvas_copy, sx, sy, col, thicknessX):
	surf.blit(canvas_copy,(0,0))
	deltaX, deltaY=((mx-sx), (my-sy))
	dist = max(hypot(deltaX, deltaY), 1)
	angle = atan2(deltaY,deltaX)
	drawx, drawy = cos(angle), sin(angle)
	for p in range(round(dist)):
		draw.circle(surf,col,((sx+round(drawx*p)),sy+round(drawy*p)),thicknessX)

def ellipseDrawTool(surf, cmx, cmy, canvas_copy, sx, sy, col, thicknessX):
	try:
		dx=cmx-sx
		dy=cmy-sy
		ellipseRect= Rect(sx,sy,dx,dy)
		ellipseRect.normalize()
		surf.blit(canvas_copy,(0,0))
		draw.ellipse(surf,col,ellipseRect)
	
		# dx=cmx-sx
		# dy=cmy-sy
		# ellipseRect= Rect(sx,sy,dx,dy)
		# ellipseRect.normalize()
		# surf.blit(canvas_copy,(0,0))
		# draw.ellipse(surf,GREEN,ellipseRect,thicknessX)
	except:
		pass

def filledEllipseDrawTool(surf, cmx, cmy, canvas_copy, sx, sy, col):
	kp=key.get_pressed()
	if kp[K_LSHIFT]:
		m = max(int((cmx-sx)),int((cmy-sy)))
		surf.blit(canvas_copy,(0,0)) 
		if cmx-sx > 0 and cmy-sy > 0:
			draw.circle(surf,col,(int((sx+m/2)),int((sy+m/2))),abs(m)//2)
		elif cmx-sx < 0 and cmy-sy > 0:
			draw.circle(surf,col,(int((sx-m/2)),int((sy+m/2))),abs(m)//2)
		elif cmx-sx < 0 and cmy-sy < 0:
			draw.circle(surf,col,(int((sx-m/2)),int((sy-m/2))),abs(m)//2)
		elif cmx-sx > 0 and cmy-sy < 0:
			draw.circle(surf,col,(int((sx+m/2)),int((sy-m/2))),abs(m)//2)

	else:
		dx=cmx-sx
		dy=cmy-sy
		ellipseRect= Rect(sx,sy,dx,dy)
		ellipseRect.normalize()
		surf.blit(canvas_copy,(0,0))
		draw.ellipse(surf,col,ellipseRect)
def rectDrawTool(surf, cmx, cmy, canvas_copy, sx, sy, col, thicknessX):
	dx=cmx-sx
	dy=cmy-sy
	rectRect= Rect(sx,sy,dx,dy)
	rectRect.normalize()
	surf.blit(canvas_copy,(0,0))
	draw.rect(surf,col,rectRect,thicknessX)

def filledRectDrawTool(surf, cmx, cmy, canvas_copy, sx, sy, col):
	dx=cmx-sx
	dy=cmy-sy
	rectRect= Rect(sx,sy,dx,dy)
	rectRect.normalize()
	surf.blit(canvas_copy,(0,0))
	draw.rect(surf,col,rectRect)
	