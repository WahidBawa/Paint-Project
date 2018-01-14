#basicPaintDefs.py
# from pygame import * 
from Colours import * 
# from random import *
# from math import *
def painter(surf, cmx, cmy, ocmx, ocmy,thickness,col,randomCol): 
	if randomCol==True:
		deltaX, deltaY=((cmx-ocmx), (cmy-ocmy))
		dist = max(hypot(deltaX, deltaY), 1)
		angle = atan2(deltaY,deltaX)
		drawx, drawy = cos(angle), sin(angle)
		for p in range(round(dist)):
			draw.circle(surf,(randint(0,255),randint(0,255),randint(0,255)),(ocmx+round(p*drawx),ocmy+round(p*drawy)),thickness)

	else:
		deltaX, deltaY=((cmx-ocmx), (cmy-ocmy))
		dist = max(hypot(deltaX, deltaY), 1)
		angle = atan2(deltaY,deltaX)
		drawx, drawy = cos(angle), sin(angle)
		for p in range(round(dist)):
			draw.circle(surf,col,((ocmx+round(drawx*p)),ocmy+round(drawy*p)),thickness)

def eraser (surf, cmx, cmy, ocmx, ocmy,thickness):    
	deltaX, deltaY=((cmx-ocmx), (cmy-ocmy))
	dist = max(hypot(deltaX, deltaY), 1)
	angle = atan2(deltaY,deltaX)
	drawx, drawy = cos(angle), sin(angle)
	for p in range(round(dist)):
		draw.circle(surf,(255,255,255,0),((ocmx+round(drawx*p)),ocmy+round(drawy*p)),thickness)

def lineDrawTool(surf, mx, my, canvas_copy, sx, sy, col, thickness):
	surf.blit(canvas_copy,(0,0))
	deltaX, deltaY=((mx-sx), (my-sy))
	dist = max(hypot(deltaX, deltaY), 1)
	angle = atan2(deltaY,deltaX)
	drawx, drawy = cos(angle), sin(angle)
	for p in range(round(dist)):
		draw.circle(surf,col,((sx+round(drawx*p)),sy+round(drawy*p)),thickness)

def ellipseDrawTool(surf, cmx, cmy, mx, my, ocmx, ocmy, canvas_copy, sx, sy, col, thickness):

	canvas.blit(canvas_copy, (0, 0))

	ellipseSurface = Surface((max(abs(cmx - sx), 1), max(abs(cmy - sy), 1)), SRCALPHA)
	ellipseSurface.fill((0, 0, 0, 0))

	ellipseRect = Rect(sx, sy, cmx - sx, cmy - sy)

	if thickness > abs(ellipseRect.width) or thickness > abs(ellipseRect.height):
		draw.ellipse(ellipseSurface, col, (0, 0, abs(ellipseRect.width), abs(ellipseRect.height)))
	else:
		draw.ellipse(ellipseSurface, col, (0, 0, abs(ellipseRect.width), abs(ellipseRect.height)))
		draw.ellipse(ellipseSurface, (255, 255, 255, 0), (thickness // 2, thickness // 2, abs(ellipseRect.width) - thickness, abs(ellipseRect.height) - thickness))

	if ellipseRect.width < 0:
		if ellipseRect.height > 0:
			canvas.blit(ellipseSurface, (cmx, sy))
		else:
			canvas.blit(ellipseSurface, (cmx, cmy))
	else:
		if ellipseRect.height > 0:
			canvas.blit(ellipseSurface, (sx, sy))
		else:
			canvas.blit(ellipseSurface, (sx, cmy))

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
		dx = cmx - sx
		dy = cmy - sy
		ellipseRect = Rect(sx, sy, dx, dy)
		ellipseRect.normalize()
		surf.blit(canvas_copy, (0,0))
		draw.ellipse(surf, col, ellipseRect)
def rectDrawTool(surf, cmx, cmy, ocmx, ocmy, canvas_copy, sx, sy, col, thickness):
	surf.blit(canvas_copy, (0,0))
	draw.rect(surf, col, (sx,sy,cmx-sx,cmy-sy), thickness*2)
	draw.circle(surf, col, (sx,sy), thickness - 1)
	draw.circle(surf, col, (cmx,cmy), thickness - 1)
	draw.circle(surf, col, (cmx,sy), thickness - 1)
	draw.circle(surf, col, (sx,cmy), thickness - 1)

def filledRectDrawTool(surf, cmx, cmy, canvas_copy, sx, sy, col):
	surf.blit(canvas_copy,(0,0))
	draw.rect(surf, col, (sx,sy,cmx-sx,cmy-sy))

def pencil(surf, col , ocmx, ocmy, cmx, cmy):
	draw.line(surf,col,(ocmx,ocmy),(cmx,cmy),3)	