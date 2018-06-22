#Defs.py
from Variables import * 
from random import *
from math import *
def painter(surf, cmx, cmy, ocmx, ocmy,thickness,col,randomCol): 
	if randomCol==True:
		deltaX, deltaY=((cmx-ocmx), (cmy-ocmy))# the space between the current mouse position and the old mouse position is calculated
		dist = max(hypot(deltaX, deltaY), 1)# dist is the distance between the x and y coordinates
		angle = atan2(deltaY,deltaX)# finds the angle of the space between the current mouse position and the old mouse position that was calculated
		drawx, drawy = cos(angle), sin(angle)# finds the cos and sin of the angle
		for p in range(round(dist)):# will draw the amount of circles to cover the distance
			draw.circle(surf,(randint(0,255),randint(0,255),randint(0,255)),(ocmx+round(p*drawx),ocmy+round(p*drawy)),thickness)
				#draws circles that make a multiple coloured line which will not skip between the circles 
	else:
		deltaX, deltaY=((cmx-ocmx), (cmy-ocmy))
		dist = max(hypot(deltaX, deltaY), 1)
		angle = atan2(deltaY,deltaX)
		drawx, drawy = cos(angle), sin(angle)
		for p in range(round(dist)):
			draw.circle(surf,col,((ocmx+round(drawx*p)),ocmy+round(drawy*p)),thickness)
				#draws circles that make a solid coloured line which will not skip between the circles 
				#same code as before except that it is one solid colour

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
	kp = key.get_pressed()
	canvas.blit(canvas_copy, (0, 0))

	if kp[K_LSHIFT]:
		# See the ellipse comments, these two are coded with the same technique
		circleSurface = Surface((max(abs(cmx-sx),abs(cmy-sy),1),max(abs(cmx-sx),abs(cmy-sy),1)), SRCALPHA)
		circleSurface.fill((0,0,0,0))
		circleRect = Rect(sx,sy,max(abs(cmx-sx),abs(cmy-sy),1),max(abs(cmx-sx),abs(cmy-sy),1))
		if thickness > abs(circleRect.width)//2:
			draw.circle(circleSurface,col,(abs(circleRect.width//2),abs(circleRect.height//2)), abs(circleRect.width)//2)
		else:
			draw.circle(circleSurface,col,(abs(circleRect.width//2),abs(circleRect.height//2)),abs(circleRect.width)//2)
			draw.circle(circleSurface,(255,255,255,0),(abs(circleRect.width//2),abs(circleRect.height//2)),abs(circleRect.width)//2 - thickness)

		if cmx-sx < 0:
			if cmy-sy > 0:
				canvas.blit(circleSurface, (sx-abs(circleRect.width),sy))
			else:
				canvas.blit(circleSurface, (sx-abs(circleRect.width),sy-abs(circleRect.height)))
		else:
			if cmy-sy > 0:
				canvas.blit(circleSurface, (sx,sy))
			else:
				canvas.blit(circleSurface, (sx,sy-abs(circleRect.height)))
	else:
		ellipseSurface = Surface((max(abs(cmx - sx), 1), max(abs(cmy - sy), 1)), SRCALPHA)# creates a surface which has an alpha value
		ellipseSurface.fill((0, 0, 0, 0)) #fills the surface

		ellipseRect = Rect(sx, sy, cmx - sx, cmy - sy) # creates an ellipse rect

		if thickness > abs(ellipseRect.width) or thickness > abs(ellipseRect.height):# if the thickness is larger than the width and the height of the ellipse then you just draw a normal ellipse
			draw.ellipse(ellipseSurface, col, (0, 0, abs(ellipseRect.width), abs(ellipseRect.height)))#draws a normal ellipse
		else:
			draw.ellipse(ellipseSurface, col, (0, 0, abs(ellipseRect.width), abs(ellipseRect.height)))# draws a normal filled ellipse
			draw.ellipse(ellipseSurface, (255, 255, 255, 0), (thickness // 2, thickness // 2, abs(ellipseRect.width) - thickness, abs(ellipseRect.height) - thickness))
			# this draws an ellipse that is invisible and is in the middle and is smaller than the normal ellipse
			#it creates the illusion that is is a hollow ellipse that is being drawn when it is 2 full ellipses 

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
		# the above will draw the surface on to the canvas otherwise the ellipse will not stay on the canvas
			#it will just disappear
def filledEllipseDrawTool(surf, cmx, cmy, canvas_copy, sx, sy, col):
	kp=key.get_pressed()# captures which keys have been pressed
	if kp[K_LSHIFT]:# is shift has been pressed
		m = abs(max(int((cmx-sx)),int((cmy-sy))))
		surf.blit(canvas_copy,(0,0)) 
		if cmx-sx > 0 and cmy-sy > 0:
			draw.circle(surf,col,(int((sx+m/2)),int((sy+m/2))),abs(m)//2)
		elif cmx-sx < 0 and cmy-sy > 0:
			draw.circle(surf,col,(int((sx-m/2)),int((sy+m/2))),abs(m)//2)
		elif cmx-sx < 0 and cmy-sy < 0:
			print("-, -")
			draw.circle(surf,col,(int(sx-m/2),int(sy-m/2)),abs(m)//2)
		elif cmx-sx > 0 and cmy-sy < 0:
			draw.circle(surf,col,(int((sx+m/2)),int((sy-m/2))),abs(m)//2)
		# Think of the cartesian plane, when in the first quadrant, you will add from the start point for x and y
		# in the second you subtract from the start point for x but still add to the start point for y


	else:
		ellipseRect = Rect(sx, sy, cmx - sx, cmy - sy)# sets ellipse rect
		ellipseRect.normalize()# normalizes the rect
		surf.blit(canvas_copy, (0,0))
		draw.ellipse(surf, col, ellipseRect)#draws a normal filled ellipse
def rectDrawTool(surf, cmx, cmy, ocmx, ocmy, canvas_copy, sx, sy, col, thickness):
	surf.blit(canvas_copy, (0,0))
	draw.rect(surf, col, (sx,sy,cmx-sx,cmy-sy), thickness*2)# draws a rectangle using the mouse
	draw.circle(surf, col, (sx,sy), thickness - 1)# draws a circle at the corners
	draw.circle(surf, col, (cmx,cmy), thickness - 1)# draws a circle at the corners
	draw.circle(surf, col, (cmx,sy), thickness - 1)# draws a circle at the corners
	draw.circle(surf, col, (sx,cmy), thickness - 1)# draws a circle at the corners

def filledRectDrawTool(surf, cmx, cmy, canvas_copy, sx, sy, col):
	surf.blit(canvas_copy,(0,0))
	draw.rect(surf, col, (sx,sy,cmx-sx,cmy-sy))# will draw a rectangle using the mouse

def pencil(surf, col , ocmx, ocmy, cmx, cmy):
	draw.line(surf,col,(ocmx,ocmy),(cmx,cmy),3)	# draws a line from where the started clicking and draw a line wherever the mouse is
def load():
	types = [('Portable Network Graphics', 'png'), ("JPEG", "jpg")]# defines file types in a list
	fname = filedialog.askopenfilename(defaultextension='png',filetypes=types)# sets default extension and the different file types 	
	return fname