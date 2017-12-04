#basicPaint.py
##                                   Variable Names/Importing functions                                 ##
import os
from pygame import * # This will import all functions and actions of pygame
from random import *
from basicPaintDefs import *# this imports functions saved in another file to make code more efficient
from Colours import *#imports some variables to make code cleaner 
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
screen = display.set_mode(size, FULLSCREEN)
##                      Variable Naming Ends                           ##

##                    Loading Initial Startup Music                 ##
mixer.music.load('MUSIC/SOUND TRACK/Pokemon_-_Gotta_Catch_Em_All_Lyrics.ogg')
mixer.music.play(-1)# will load and play initial music forever 
##                    Ending Loading Initial Startup Music                 ##

##                      Importing Pictures / Animations / Editing Pictures                        ##

bc1=image.load("PICS/IMAGES/water_Background_1.jpg").convert()
bc1=transform.scale(bc1, size)# loads initial background and scales it to size

wheelPic=image.load("PICS/IMAGES/colour_picker.png").convert_alpha()
wheelPic=transform.scale(wheelPic, (155,155))# loads the colour wheel and scales it to size

for i in range(30):# Imports all pictures that make up the animation of the sprite in the selection and scales it
	chikorita=image.load('PICS/GRAPHICS/Chikorita/Chikorita Stamp/frame_%02d_delay-0.08s.png' % i).convert_alpha()
	ChikoritaAnimation.append(transform.scale(chikorita, (141//2,210//2)))

for i in range(52):
	bayleef=image.load('PICS/GRAPHICS/Chikorita/Bayleef Stamp/frame_%02d_delay-0.03s.png' % i).convert_alpha()
	BayleefAnimation.append(transform.scale(bayleef, (49,84)))

for i in range(59):
	meganium=image.load('PICS/GRAPHICS/Chikorita/Meganium Stamp/frame_%02d_delay-0.04s.png' % i).convert_alpha()
	MeganiumAnimation.append(transform.scale(meganium, (64,93)))

for i in range(119):
	MegaGengar=image.load("PICS/GRAPHICS/Gengar/Mega Gengar Stamp/frame_%003d_delay-0.03s.png" % i).convert_alpha()
	MegaGengarAnimation.append(transform.scale(MegaGengar, (112,92)))

for i in range(39):
	Gengar=image.load("PICS/GRAPHICS/Gengar/Gengar Stamp/frame_%02d_delay-0.04s.gif" % i).convert_alpha()
	GengarAnimation.append(transform.scale(Gengar, (84,78)))

for i in range(59):
	Haunter=image.load('PICS/GRAPHICS/Gengar/Haunter Stamp/frame_%02d_delay-0.03s.gif' % i).convert_alpha()
	HaunterAnimation.append(transform.scale(Haunter, (85,73)))

for i in range(64):
	Gastly=image.load('PICS/GRAPHICS/Gengar/Gastly Stamp/frame_%02d_delay-0.03s.png' % i).convert_alpha()
	GastlyAnimation.append(transform.scale(Gastly, (52,61)))

for i in range(39):
	Infernape=image.load('PICS/GRAPHICS/Infernape/Infernape Stamp/frame_%02d_delay-0.04s.png' % i).convert_alpha()
	InfernapeAnimation.append(transform.scale(Infernape, (98,119)))

for i in range(29):
	Monferno=image.load('PICS/GRAPHICS/Infernape/Monferno Stamp/frame_%02d_delay-0.04s.png' % i).convert_alpha()
	MonfernoAnimation.append(transform.scale(Monferno, (57,91)))

for i in range(27):
	Chimchar=image.load('PICS/GRAPHICS/Infernape/Chimchar Stamp/frame_%02d_delay-0.04s.png' % i).convert_alpha()
	ChimcharAnimation.append(transform.scale(Chimchar, (54,70)))	
	
for i in range(75):
	MegaBlastoise=image.load('PICS/GRAPHICS/Blastoise/Mega Blastoise Stamp/frame_%02d_delay-0.03s.png' % i).convert_alpha()
	MegaBlastoiseAnimation.append(transform.scale(MegaBlastoise, (110,114)))

paintOption=image.load("PICS/IMAGES/Tool Selection Sprite/paint_tool.png").convert_alpha()
paintOption=transform.scale(paintOption, (40,40))# imports and scales the paint tool option picture

eraserOption=image.load("PICS/IMAGES/Tool Selection Sprite/eraser_tool.png").convert_alpha()
eraserOption=transform.scale(eraserOption, (40,40))# imports and scales the eraser tool option picture
##                      End Of Importing Pictures / Animations / Editing Pictures                 ##

##                      Creating Rect Objects                        ##
MegaBlastoiseRect=Rect(300,605,40,40)

infernapeRect=Rect(250,605,40,40)
monfernoRect=Rect(250,645,40,40)
chimcharRect=Rect(250,685,40,40)

chikoritaRect=Rect(150,685,40,40)
bayleefRect=Rect(150,645,40,40)
meganiumRect=Rect(150,605,40,40)

MegaGengarRect=Rect(200,605,40,40)
gengarRect=Rect(200,645,40,40)
haunterRect=Rect(200,685,40,40)
gastlyRect=Rect(200,725,40,40)

canvasRect=Rect(150,100,800,500)
paintRect=Rect(20,80,40,40)
eraserRect=Rect(70,80,40,40)
randomRect=Rect(70,130,40,40)

wheelRect=wheelPic.get_rect()
wheelRect.topleft = 770, 600

currentColRect = Rect(700,600,50,50)
##                      Creating Rect Objects Ending                        ##

##                      Event Loop Start                        ##
while running:
	for evt in event.get(): 
		if evt.type == QUIT:
			running = False 
		if evt.type == KEYDOWN:
			if evt.key == K_ESCAPE:#if ESC pressed the program will end
					running = False
			if evt.key == K_y:
				if len(control_Y) > 1:
					control_Z.append(control_Y.pop(-1))
					canvas.blit(control_Y[-1], (0,0))

			if evt.key == K_z:
				if len(control_Z) > 1:
					control_Y.append(control_Z.pop(-1))
					canvas.blit(control_Z[-1], (0,0))

			if evt.key == K_o:
				mixer.music.stop()

			if evt.key == K_p:
				mixer.music.load('MUSIC/SOUND TRACK/Pokemon_-_Gotta_Catch_Em_All_Lyrics.ogg')
				mixer.music.play(-1)

		if evt.type == MOUSEBUTTONUP:
			if evt.button == 1:
				if canvasRect.collidepoint((mx, my)):
					control_Z.append(canvas.copy())

					
		if evt.type == MOUSEBUTTONDOWN:
			
			if evt.button == 1:
				canvas_copy = canvas.copy()
				if randomRect.collidepoint(mx,my):
					randomCol=1-randomCol
			
			if evt.button == 4:
				if thickness<=100:
					thickness += 1
			
			if evt.button == 5:
				if thickness>3:
					thickness -= 1

	mb = mouse.get_pressed()
	mx, my = mouse.get_pos()
## Selection Animation Start ##	
	chikorita_counter += 1
	if chikorita_counter > len(ChikoritaAnimation)-1:
		chikorita_counter = 0

	bayleef_counter += 1
	if bayleef_counter > len(BayleefAnimation)-1:
		bayleef_counter = 0	

	meganium_counter += 1
	if meganium_counter > len(MeganiumAnimation)-1:
		meganium_counter = 0

	MegaGengar_counter += 1
	if MegaGengar_counter > len(MegaGengarAnimation)-1:
		MegaGengar_counter = 0

	gengar_counter += 1
	if gengar_counter > len(GengarAnimation)-1:
		gengar_counter = 0

	haunter_counter += 1
	if haunter_counter > len(HaunterAnimation)-1:
		haunter_counter = 0	

	gastly_counter += 1
	if gastly_counter > len(GastlyAnimation)-1:
		gastly_counter = 0		 

	infernape_counter += 1
	if infernape_counter > len(InfernapeAnimation)-1:
		infernape_counter = 0

	monferno_counter += 1
	if monferno_counter > len(MonfernoAnimation)-1:
		monferno_counter = 0	

	chimchar_counter += 1
	if chimchar_counter > len(ChimcharAnimation)-1:
		chimchar_counter = 0

	MegaBlastoise_counter += 1
	if MegaBlastoise_counter > len(MegaBlastoiseAnimation)-1:
		MegaBlastoise_counter = 0	
## Selection Animation End ##	

##                      CollidePoint Start                        ##
	if mb[0]:
		if wheelRect.collidepoint(mx,my):
			col=screen.get_at((mx,my))
		if paintRect.collidepoint(mx,my):
			tool="paint"
		elif eraserRect.collidepoint(mx,my):    
			tool='eraser'
		elif chikoritaRect.collidepoint(mx,my):    
			tool='chikoritaStamp'
		elif bayleefRect.collidepoint(mx,my):
			tool='bayleefStamp'
		elif meganiumRect.collidepoint(mx,my):
			tool='meganiumStamp'
		elif MegaGengarRect.collidepoint(mx,my):
			tool='MegaGengarStamp'
		elif gengarRect.collidepoint(mx,my):
			tool='gengarStamp'
		elif haunterRect.collidepoint(mx,my):
			tool='haunterStamp'
		elif gastlyRect.collidepoint(mx,my):
			tool='gastlyStamp'
		elif infernapeRect.collidepoint(mx,my):
			tool='infernapeStamp'
		elif monfernoRect.collidepoint(mx,my):
			tool='monfernoStamp'
		elif chimcharRect.collidepoint(mx,my):
			tool='chimcharStamp'
		elif MegaBlastoiseRect.collidepoint(mx,my):
			tool='MegaBlastoiseStamp'										
##                      CollidePoint End                       ##

##                   Surface / Canvas / Blit / Start               ##
	screen.blit(bc1, (0,0))
	# screen.fill(GREEN)
	## Tool Selection Check Red ##
	if tool=='paint':
		draw.rect(screen,RED,paintRect)
	else:
		draw.rect(screen,WHITE,paintRect)

	if tool=="eraser":	
		draw.rect(screen,RED,eraserRect)
	else:
		draw.rect(screen,WHITE,eraserRect)

	if tool=="chikoritaStamp":
		draw.rect(screen,RED,chikoritaRect)
	else:
		draw.rect(screen,WHITE,chikoritaRect)

	if tool=='bayleefStamp':
		draw.rect(screen,RED,bayleefRect)
	else:
		draw.rect(screen,WHITE,bayleefRect)

	if tool=='meganiumStamp':
		draw.rect(screen,RED,meganiumRect)
	else:
		draw.rect(screen,WHITE,meganiumRect)	

	if tool=='MegaGengarStamp':
		draw.rect(screen,RED,MegaGengarRect)
	else:
		draw.rect(screen,WHITE,MegaGengarRect)

	if tool=='gengarStamp':
		draw.rect(screen,RED,gengarRect)
	else:
		draw.rect(screen,WHITE,gengarRect)

	if tool=='haunterStamp':
		draw.rect(screen,RED,haunterRect)
	else:
		draw.rect(screen,WHITE,haunterRect)

	if tool=='gastlyStamp':
		draw.rect(screen,RED,gastlyRect)
	else:
		draw.rect(screen,WHITE,gastlyRect)

	if tool=='infernapeStamp':
		draw.rect(screen,RED,infernapeRect)
	else:
		draw.rect(screen,WHITE,infernapeRect)

	if tool=='monfernoStamp':
		draw.rect(screen,RED,monfernoRect)
	else:
		draw.rect(screen,WHITE,monfernoRect)

	if tool=='chimcharStamp':
		draw.rect(screen,RED,chimcharRect)
	else:
		draw.rect(screen,WHITE,chimcharRect)

	if tool=='MegaBlastoiseStamp':
		draw.rect(screen,RED,MegaBlastoiseRect)
	else:
		draw.rect(screen,WHITE,MegaBlastoiseRect)								
	## Tool Selection Check Red End ##
	
	## Tool Sprites Start ##
	screen.blit(eraserOption, eraserRect)

	screen.blit(paintOption, paintRect)
	## Tool Sprites End ##
	screen.blit(wheelPic,wheelRect)
	
	draw.rect(screen, col, currentColRect)
		
	draw.rect(screen,WHITE,randomRect)
	
	screen.blit(transform.scale(ChikoritaAnimation[chikorita_counter], (40,40)), chikoritaRect)
	
	screen.blit(transform.scale(BayleefAnimation[bayleef_counter], (40,40)), bayleefRect)
	screen.blit(transform.scale(MeganiumAnimation[meganium_counter], (40,40)), meganiumRect)
	screen.blit(transform.scale(MegaGengarAnimation[MegaGengar_counter], (40,40)),MegaGengarRect)
	screen.blit(transform.scale(GengarAnimation[gengar_counter], (40,40)), gengarRect)
	screen.blit(transform.scale(HaunterAnimation[haunter_counter], (40,40)),haunterRect)
	screen.blit(transform.scale(GastlyAnimation[gastly_counter],(40,40)),gastlyRect)
	screen.blit(transform.scale(InfernapeAnimation[infernape_counter],(40,40)),infernapeRect)
	screen.blit(transform.scale(MonfernoAnimation[monferno_counter],(40,40)),monfernoRect)
	screen.blit(transform.scale(ChimcharAnimation[chimchar_counter],(40,40)),chimcharRect)
	screen.blit(transform.scale(MegaBlastoiseAnimation[MegaBlastoise_counter],(40,40)),MegaBlastoiseRect)
	draw.rect(screen, BLACK, canvasRect)
	screen.blit(canvas, (150,100))
	
	screen.set_clip(canvasRect)
	
	draw.circle(screen, (100,100,100), (mx, my), thickness, 2)
	
	draw.circle(screen, (100,100,100), (mx, my), 3)
	
	screen.set_clip(None)
##                   Surface / Canvas Blit End               ##

##                   Draw Options Start               ##
	cmx, cmy = mx-150, my-100
	if mb[0] and tool=='eraser':
		eraser(canvas, cmx, cmy, ocmx, ocmy,thickness)

	elif mb[0] and tool=='paint':
		painter(canvas, cmx, cmy, ocmx, ocmy, thickness, col,randomCol)

	elif mb[0] and tool=='chikoritaStamp':
		chikorita = ChikoritaAnimation[0]#when the chikorita is put on the canvas it will print the stationary version of the animated version
		canvas.blit(canvas_copy, (0,0))#makes it so that chikorita can be dragged and can't draw it on screen before mouse button press was let go
		canvas.blit(chikorita, (cmx-chikorita.get_rect().width/2, cmy-chikorita.get_rect().height/2))#This will spawn Chikorita from the centre of that stamp
	
	elif mb[0] and tool=='bayleefStamp':
		canvas.blit(canvas_copy, (0,0))
		bayleef=BayleefAnimation[0]
		canvas.blit(bayleef, (cmx-bayleef.get_rect().width/2, cmy-bayleef.get_rect().height/2))

	elif mb[0] and tool=='meganiumStamp':
		canvas.blit(canvas_copy, (0,0))
		meganium=MeganiumAnimation[0]
		canvas.blit(meganium, (cmx-meganium.get_rect().width/2, cmy-meganium.get_rect().height/2))		

	elif mb[0] and tool=='MegaGengarStamp':
		canvas.blit(canvas_copy, (0,0))
		MegaGengar=MegaGengarAnimation[0]
		canvas.blit(MegaGengar, (cmx-MegaGengar.get_rect().width/2, cmy-MegaGengar.get_rect().height/2))
	
	elif mb[0] and tool=='gengarStamp':
		canvas.blit(canvas_copy, (0,0))
		gengar=GengarAnimation[0]
		canvas.blit(gengar, (cmx-gengar.get_rect().width/2, cmy-gengar.get_rect().height/2))

	elif mb[0] and tool=='haunterStamp':
		canvas.blit(canvas_copy, (0,0))
		haunter=HaunterAnimation[0]
		canvas.blit(haunter, (cmx-haunter.get_rect().width/2, cmy-haunter.get_rect().height/2))	
	
	elif mb[0] and tool=='gastlyStamp':
		canvas.blit(canvas_copy, (0,0))
		gastly=GastlyAnimation[0]
		canvas.blit(gastly, (cmx-gastly.get_rect().width/2, cmy-gastly.get_rect().height/2))	

	elif mb[0] and tool=='infernapeStamp':
		canvas.blit(canvas_copy, (0,0))
		infernape=InfernapeAnimation[0]
		canvas.blit(infernape, (cmx-infernape.get_rect().width/2, cmy-infernape.get_rect().height/2))

	elif mb[0] and tool=='monfernoStamp':
		canvas.blit(canvas_copy, (0,0))
		monferno=MonfernoAnimation[0]
		canvas.blit(monferno, (cmx-monferno.get_rect().width/2, cmy-monferno.get_rect().height/2))	
	
	elif mb[0] and tool=='chimcharStamp':
		canvas.blit(canvas_copy,(0,0))
		Chimchar=ChimcharAnimation[0]
		canvas.blit(Chimchar, (cmx-Chimchar.get_rect().width/2, cmy-Chimchar.get_rect().height/2))

	elif mb[0] and tool=='MegaBlastoiseStamp':
		canvas.blit(canvas_copy,(0,0))
		MegaBlastoise=MegaBlastoiseAnimation[0]
		canvas.blit(MegaBlastoise, (cmx-MegaBlastoise.get_rect().width/2, cmy-MegaBlastoise.get_rect().height/2))			
	myClock.tick(60)
	display.flip()
	ocmx, ocmy = cmx, cmy
##                   Draw Options End                   ##
quit() # closes out pygame window
