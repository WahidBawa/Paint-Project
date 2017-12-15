#Main_Paint.py 
##                                   Variable Names/Importing functions                                 ##
import os
from pygame import * # This will import all functions and actions of pygame
from random import *
from basicPaintDefs import *# this imports functions saved in another file to make code more efficient
from Colours import *#imports some variables to make code cleaner 
from tkinter.colorchooser import *
from tkinter import *
root = Tk()
root.withdraw()
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
screen = display.set_mode(size, FULLSCREEN)
display.set_caption("PokePaint")
##                      Variable Naming Ends                           ##

##                    Loading Initial Startup Music                 ##
mixer.music.load('MUSIC/SOUND TRACK/Pokemon_-_Gotta_Catch_Em_All_Lyrics.ogg')
mixer.music.play(-1)# will load and play initial music forever 
##                    Ending Loading Initial Startup Music                 ##

##                      Importing Pictures / Animations / Editing Pictures                        ##
selectedPokemon=image.load("PICS/IMAGES/Templates/pokemon_selected.png")
pokeMenu1=image.load("PICS/IMAGES/Templates/pokemon_selection_menu_cropped.png")
pokeMenu2=image.load("PICS/IMAGES/Templates/pokemon_selection_menu_cropped.png")
pokeMenu3=image.load("PICS/IMAGES/Templates/pokemon_selection_menu_cropped.png")

bc1=image.load("PICS/IMAGES/water_Background_1.jpg").convert()
bc1=transform.scale(bc1, size)# loads initial background and scales it to size

logo=image.load("PICS/IMAGES/Title/PokePaintLogoOfficial.png")

idiot=image.load("PICS/IMAGES/SYED/WIN_20171207_12_15_15_Pro (2).jpg")

wheelPic=image.load("PICS/IMAGES/colour_picker.png").convert_alpha()
wheelPic=transform.scale(wheelPic, (155,155))# loads the colour wheel and scales it to size


for i in range(30):# Imports all pictures that make up the animation of the sprite in the selection and scales it
	chikorita=image.load('PICS/GRAPHICS/Chikorita/Chikorita Stamp/frame_%02d_delay-0.08s.png' % i).convert_alpha()
	ChikoritaAnimation.append(transform.scale(chikorita, (141//2,210//2)))
for i in range(52):
	bayleef=image.load('PICS/GRAPHICS/Chikorita/Bayleef Stamp/frame_%02d_delay-0.03s.png' % i).convert_alpha()
	BayleefAnimation.append(bayleef)
for i in range(59):
	meganium=image.load('PICS/GRAPHICS/Chikorita/Meganium Stamp/frame_%02d_delay-0.04s.png' % i).convert_alpha()
	MeganiumAnimation.append(meganium)
for i in range(119):
	MegaGengar=image.load("PICS/GRAPHICS/Gengar/Mega Gengar Stamp/frame_%003d_delay-0.03s.png" % i).convert_alpha()
	MegaGengarAnimation.append(MegaGengar)
for i in range(39):
	Gengar=image.load("PICS/GRAPHICS/Gengar/Gengar Stamp/frame_%02d_delay-0.04s.gif" % i).convert_alpha()
	GengarAnimation.append(Gengar)
for i in range(59):
	Haunter=image.load('PICS/GRAPHICS/Gengar/Haunter Stamp/frame_%02d_delay-0.03s.gif' % i).convert_alpha()
	HaunterAnimation.append(Haunter)
for i in range(64):
	Gastly=image.load('PICS/GRAPHICS/Gengar/Gastly Stamp/frame_%02d_delay-0.03s.png' % i).convert_alpha()
	GastlyAnimation.append(Gastly)
for i in range(39):
	Infernape=image.load('PICS/GRAPHICS/Infernape/Infernape Stamp/frame_%02d_delay-0.04s.png' % i).convert_alpha()
	InfernapeAnimation.append(Infernape)
for i in range(29):
	Monferno=image.load('PICS/GRAPHICS/Infernape/Monferno Stamp/frame_%02d_delay-0.04s.png' % i).convert_alpha()
	MonfernoAnimation.append(Monferno)
for i in range(27):
	Chimchar=image.load('PICS/GRAPHICS/Infernape/Chimchar Stamp/frame_%02d_delay-0.04s.png' % i).convert_alpha()
	ChimcharAnimation.append(Chimchar)  
for i in range(75):
	MegaBlastoise=image.load('PICS/GRAPHICS/Blastoise/Mega Blastoise Stamp/frame_%02d_delay-0.03s.png' % i).convert_alpha()
	MegaBlastoiseAnimation.append(MegaBlastoise)
for i in range(75):
	Blastoise=image.load('PICS/GRAPHICS/Blastoise/Blastoise Stamp/frame_%02d_delay-0.03s.png' % i).convert_alpha()
	BlastoiseAnimation.append(Blastoise)
for i in range(31):
	Wartortle=image.load('PICS/GRAPHICS/Blastoise/Wartortle Stamp/frame_%02d_delay-0.04s.png' % i)
	WartortleAnimation.append(Wartortle)
for i in range(66):
	Squirtle=image.load('PICS/GRAPHICS/Blastoise/Squirtle Stamp/frame_%02d_delay-0.03s.png' % i).convert_alpha()
	SquirtleAnimation.append(Squirtle)
for i in range(59):
	Darkrai=image.load("PICS/GRAPHICS/Legendary/Darkrai/frame_%02d_delay-0.04s.png" % i).convert_alpha()
	DarkraiAnimation.append(Darkrai)
for i in range(79):
	Giratina=image.load("PICS/GRAPHICS/Legendary/Giratina/frame_%02d_delay-0.03s.png" % i).convert_alpha()
	GiratinaAnimation.append(Giratina)
for i in range(79):
	Palkia=image.load("PICS/GRAPHICS/Legendary/Palkia/frame_%02d_delay-0.03s.png" % i).convert_alpha()
	PalkiaAnimation.append(Palkia)
for i in range(90):
	Mewtwo=image.load("PICS/GRAPHICS/Legendary/Mewtwo/frame_%02d_delay-0.03s.png" % i).convert_alpha()
	MewtwoAnimation.append(Mewtwo)				
paintOption=image.load("PICS/IMAGES/Tool Selection Sprite/paint_tool.png").convert_alpha()
paintOption=transform.scale(paintOption, (40,40))# imports and scales the paint tool option picture
eraserOption=image.load("PICS/IMAGES/Tool Selection Sprite/eraser_tool.png").convert_alpha()
eraserOption=transform.scale(eraserOption, (40,40))# imports and scales the eraser tool option picture
syedOption=image.load("PICS/IMAGES/SYED/WIN_20171207_12_15_15_Pro (2).jpg")
syedOption=transform.scale(syedOption, (34,34))
##                      End Of Importing Pictures / Animations / Editing Pictures                 ##

##                      Creating Rect Objects                        ##
MegaBlastoiseRect=Rect(1035,175,115,115)
infernapeRect=Rect(1165,175,115,115)
MegaGengarRect=Rect(1035,300,115,115)
meganiumRect=Rect(1165,300,115,115)
gengarRect=Rect(1035,425,115,115)
BlastoiseRect=Rect(1165,425,115,115)

haunterRect=Rect(1035,175,115,115)
monfernoRect=Rect(1165,175,115,115)
gastlyRect=Rect(1035,300,115,115)
bayleefRect=Rect(1165,300,115,115)
chimcharRect=Rect(1035,425,115,115)
WartortleRect=Rect(1165,425,115,115)

SquirtleRect=Rect(1035,175,115,115)
chikoritaRect=Rect(1165,175,115,115)
DarkraiRect=Rect(1035,300,115,115)
GiratinaRect=Rect(1165,300,115,115)
PalkiaRect=Rect(1035,425,115,115)
MewtwoRect=Rect(1165,425,115,115)

canvasRect=Rect(150,100,800,500)
paintRect=Rect(20,80,40,40)
eraserRect=Rect(70,80,40,40)
randomRect=Rect(70,130,40,40)
syedRect=Rect(20,130,40,40)
colourPickerRect=Rect(20,180,40,40)
lineDrawRect=Rect(70,180,40,40)
circleDrawRect=Rect(20,230,40,40)
saveRect=Rect(0,0,40,40)

wheelRect=wheelPic.get_rect()
wheelRect.topleft = 770, 600

currentColRect = Rect(700,600,50,50)
##                      Creating Rect Objects Ending                        ##

##                      Event Loop Start                        ##
key.set_repeat(500,100)
while running:
	for evt in event.get(): 
		if evt.type == QUIT:
			running = False 
		if evt.type == KEYDOWN:
			if evt.key == K_ESCAPE:#if ESC pressed the program will end
					running = False
			if evt.key == K_y:
				if len(control_Y) > 0:
					transfer = control_Y.pop()
					control_Z.append(transfer)
			if evt.key == K_z:
				if len(control_Z) > 1:
					transfer = control_Z.pop()
					control_Y.append(transfer)
			if evt.key == K_o:
				mixer.music.stop()
			if evt.key == K_p:
				mixer.music.load('MUSIC/SOUND TRACK/Pokemon_-_Gotta_Catch_Em_All_Lyrics.ogg')
				mixer.music.play(-1)
			if evt.key == K_RIGHT:
				if pokeSelect==2:
					pokeSelect=3    
				if pokeSelect==1:
					pokeSelect=2
			if evt.key == K_LEFT:
				if pokeSelect==2:
					pokeSelect=1
				if pokeSelect==3:
					pokeSelect=2    
		if evt.type == MOUSEBUTTONUP:
			if evt.button == 1:
				if canvasRect.collidepoint((mx, my)):
					control_Z.append(canvas.copy())
				elif colourPickerRect.collidepoint(mx,my):
					c = askcolor(title='Pick Colour')
					if c[0] != None:
						col = c[0]  

		if evt.type == MOUSEBUTTONDOWN:
			if evt.button == 1 or evt.button == 2:
				sx,sy = cmx,cmy
				canvas_copy = canvas.copy()
				if randomRect.collidepoint(mx,my):
					randomCol = 1 - randomCol
			if evt.button == 3:
				fill=True      
			if evt.button == 4:
				if thicknessX <= 4000:
					thicknessX+=int(thicknessX*0.1)
				if thicknessY <= 4000:
					thicknessY += int(thicknessY*0.1)
			if evt.button == 5:
				if thicknessX > 5:
					thicknessX -= int(thicknessX*0.1)
				if thicknessY > 5:
					thicknessY -= int(thicknessY*0.1)
	mb = mouse.get_pressed()
	mx, my = mouse.get_pos()
	if not mb[0] and not mb[2]:
		canvas.blit(control_Z[-1], (0,0))
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
	Blastoise_counter += 1
	if Blastoise_counter > len(BlastoiseAnimation)-1:
		Blastoise_counter = 0
	Wartortle_counter += 1
	if Wartortle_counter > len(WartortleAnimation)-1:
		Wartortle_counter = 0
	Squirtle_counter += 1
	if Squirtle_counter > len(SquirtleAnimation)-1:
		Squirtle_counter = 0
	Darkrai_counter += 1
	if Darkrai_counter > len(DarkraiAnimation)-1:
		Darkrai_counter = 0	
	Giratina_counter += 1
	if Giratina_counter > len(GiratinaAnimation)-1:
		Giratina_counter = 0	
	Palkia_counter += 1
	if Palkia_counter > len(PalkiaAnimation)-1:
		Palkia_counter = 0
	Mewtwo_counter += 1
	if Mewtwo_counter > len(MewtwoAnimation)-1:
		Mewtwo_counter = 0		
## Selection Animation End ##   

##                      CollidePoint Start                        ##
	
	if mb[0]:
		if wheelRect.collidepoint(mx,my):
			col=screen.get_at((mx,my))

		if paintRect.collidepoint(mx,my):
			tool="paint"
		elif eraserRect.collidepoint(mx,my):    
			tool='eraser'
		elif lineDrawRect.collidepoint(mx,my):
			tool='lineTool'
		elif circleDrawRect.collidepoint(mx,my):
			tool='circleTool'	
		elif saveRect.collidepoint(mx,my):
			tool="saveTool"
		if pokeSelect==1:
			if MegaBlastoiseRect.collidepoint(mx,my):
				tool='MegaBlastoiseStamp'
			elif infernapeRect.collidepoint(mx,my):
				tool='infernapeStamp'
			elif MegaGengarRect.collidepoint(mx,my):
				tool='MegaGengarStamp'
			elif meganiumRect.collidepoint(mx,my):
				tool='meganiumStamp'
			elif gengarRect.collidepoint(mx,my):
				tool='gengarStamp'
			elif BlastoiseRect.collidepoint(mx,my):
				tool='BlastoiseStamp'
		if pokeSelect==2:
			if haunterRect.collidepoint(mx,my):
				tool='haunterStamp'
			elif monfernoRect.collidepoint(mx,my):
				tool='monfernoStamp'
			elif gastlyRect.collidepoint(mx,my):
				tool='gastlyStamp'
			elif bayleefRect.collidepoint(mx,my):
				tool='bayleefStamp'
			elif chimcharRect.collidepoint(mx,my):
				tool='chimcharStamp'
			elif WartortleRect.collidepoint(mx,my):
				tool='WartortleStamp'
		if pokeSelect==3:
			if chikoritaRect.collidepoint(mx,my):    
				tool='chikoritaStamp'
			elif SquirtleRect.collidepoint(mx,my):
				tool='SquirtleStamp'
			elif DarkraiRect.collidepoint(mx,my):
				tool="DarkraiStamp"
			elif GiratinaRect.collidepoint(mx,my):
				tool="GiratinaStamp"
			elif PalkiaRect.collidepoint(mx,my):
				tool="PalkiaStamp"
			elif MewtwoRect.collidepoint(mx,my):
				tool="MewtwoStamp"			
		elif syedRect.collidepoint(mx,my):
			tool='SyedStamp'
##                      CollidePoint End                       ##
##                   Surface / Canvas / Blit / Start               ##
	screen.blit(bc1, (0,0))
	# screen.fill(GREEN)
	## Tool Selection Check Red ##
	if tool=="SyedStamp":
		draw.rect(screen,RED,syedRect)
	else:
		draw.rect(screen,WHITE,syedRect) 
	if tool=='paint':
		draw.rect(screen,RED,paintRect)
	else:
		draw.rect(screen,WHITE,paintRect)
	if tool=="eraser":  
		draw.rect(screen,RED,eraserRect)
	else:
		draw.rect(screen,WHITE,eraserRect)
	if tool=="lineTool":
		draw.rect(screen,RED,lineDrawRect)
	else:
		draw.rect(screen,WHITE,lineDrawRect)                                            
	if tool=="circleTool":
		draw.rect(screen,RED,circleDrawRect)
	else:
		draw.rect(screen,WHITE,circleDrawRect)
	if tool=="saveTool":
		draw.rect(screen,RED,saveRect)	
	else:
		draw.rect(screen,WHITE,saveRect)	
						
	## Tool Selection Check Red End ##
	## Tool Sprites Start ##
	
	if pokeSelect==1:
		screen.blit(pokeMenu1, (1025, 170))
	if pokeSelect==2:
		screen.blit(pokeMenu2, (1025, 170))
	if pokeSelect==3:
		screen.blit(pokeMenu3, (1025, 170))
			
	## Tool Sprites End ##
	screen.blit(logo, (350,0))

	screen.blit(wheelPic,wheelRect)
	screen.blit(eraserOption, eraserRect)
	screen.blit(paintOption, paintRect)
	screen.blit(syedOption, Rect(25,133,40,40))
	screen.blit(selectedPokemon, (1025,50))
	
	draw.rect(screen, col, currentColRect)
	draw.rect(screen,WHITE,randomRect)
	draw.rect(screen,WHITE,colourPickerRect)
	
	if pokeSelect==1:
		screen.blit(transform.scale(MeganiumAnimation[meganium_counter], (115,115)), meganiumRect)
		screen.blit(transform.scale(MegaBlastoiseAnimation[MegaBlastoise_counter],(115,115)),MegaBlastoiseRect)
		screen.blit(transform.scale(InfernapeAnimation[infernape_counter],(115,115)),infernapeRect)
		screen.blit(transform.scale(GengarAnimation[gengar_counter], (115,115)), gengarRect)
		screen.blit(transform.scale(MegaGengarAnimation[MegaGengar_counter], (115,115)),MegaGengarRect)
		screen.blit(transform.scale(BlastoiseAnimation[Blastoise_counter],(115,115)),BlastoiseRect)
	if pokeSelect==2:
		screen.blit(transform.scale(HaunterAnimation[haunter_counter], (115,115)),haunterRect)
		screen.blit(transform.scale(MonfernoAnimation[monferno_counter],(115,115)),monfernoRect)
		screen.blit(transform.scale(WartortleAnimation[Wartortle_counter],(115,115)),WartortleRect)
		screen.blit(transform.scale(BayleefAnimation[bayleef_counter], (115,115)), bayleefRect)
		screen.blit(transform.scale(GastlyAnimation[gastly_counter],(115,115)),gastlyRect)
		screen.blit(transform.scale(ChimcharAnimation[chimchar_counter],(115,115)),chimcharRect)
	if pokeSelect==3:
		screen.blit(transform.scale(ChikoritaAnimation[chikorita_counter], (115,115)), chikoritaRect)
		screen.blit(transform.scale(SquirtleAnimation[Squirtle_counter],(115,115)),SquirtleRect)
		screen.blit(transform.scale(DarkraiAnimation[Darkrai_counter],(115,115)),DarkraiRect)
		screen.blit(transform.scale(GiratinaAnimation[Giratina_counter],(115,115)),GiratinaRect)
		screen.blit(transform.scale(PalkiaAnimation[Palkia_counter],(115,115)),PalkiaRect)
		screen.blit(transform.scale(MewtwoAnimation[Mewtwo_counter],(115,115)),MewtwoRect)

	if tool=="MegaBlastoiseStamp":
		screen.blit(transform.scale(MegaBlastoiseAnimation[MegaBlastoise_counter],(115,115)),(1035,55))
	if tool=="MegaGengarStamp":
		screen.blit(transform.scale(MegaGengarAnimation[MegaGengar_counter],(115,115)),(1035,55))
	if tool=="gengarStamp":
		screen.blit(transform.scale(GengarAnimation[gengar_counter],(115,115)),(1035,55))   
	if tool=="infernapeStamp":
		screen.blit(transform.scale(InfernapeAnimation[infernape_counter],(115,115)),(1035,55))
	if tool=="meganiumStamp":
		screen.blit(transform.scale(MeganiumAnimation[meganium_counter],(115,115)),(1035,55))
	if tool=="BlastoiseStamp":
		screen.blit(transform.scale(BlastoiseAnimation[Blastoise_counter],(115,115)),(1035,55))
	if tool=="haunterStamp":
		screen.blit(transform.scale(HaunterAnimation[haunter_counter],(115,115)),(1035,60))
	if tool=="monfernoStamp":
		screen.blit(transform.scale(MonfernoAnimation[monferno_counter],(115,115)),(1035,55))
	if tool=="gastlyStamp":
		screen.blit(transform.scale(GastlyAnimation[gastly_counter],(115,115)),(1035,55))
	if tool=="bayleefStamp":
		screen.blit(transform.scale(BayleefAnimation[bayleef_counter],(110,110)),(1035,60))
	if tool=="chimcharStamp":
		screen.blit(transform.scale(ChimcharAnimation[chimchar_counter],(115,115)),(1035,55))
	if tool=="WartortleStamp":
		screen.blit(transform.scale(WartortleAnimation[Wartortle_counter],(110,110)),(1035,60))
	if tool=="SquirtleStamp":
		screen.blit(transform.scale(SquirtleAnimation[Squirtle_counter],(110,110)),(1035,60))
	if tool=="chikoritaStamp":
		screen.blit(transform.scale(ChikoritaAnimation[chikorita_counter],(110,110)),(1035,60))
	if tool=="DarkraiStamp":
		screen.blit(transform.scale(DarkraiAnimation[Darkrai_counter],(115,115)),(1035,50))
	if tool=="GiratinaStamp":
		screen.blit(transform.scale(GiratinaAnimation[Giratina_counter],(110,110)),(1035,60))
	if tool=="PalkiaStamp":
		screen.blit(transform.scale(PalkiaAnimation[Palkia_counter],(110,110)),(1035,60))
	if tool=="MewtwoStamp":
		screen.blit(transform.scale(MewtwoAnimation[Mewtwo_counter],(110,110)),(1035,60))			
	draw.rect(screen, BLACK, canvasRect)
	screen.blit(canvas, (150,100))
	
	screen.set_clip(canvasRect)
	
	draw.circle(screen, (100,100,100), (mx, my), thicknessX, 2)
	
	draw.circle(screen, (100,100,100), (mx, my), 3)
	
	screen.set_clip(None)

	if fill==True:
		canvas.fill(WHITE)
##                   Surface / Canvas Blit End               ##

##                   Draw Options Start               ##
	cmx, cmy = mx-150, my-100
	if mb[0] and tool=='eraser' and canvasRect.collidepoint((mx, my)):
		eraser(canvas, cmx, cmy, ocmx, ocmy,thicknessX)

	elif mb[0] and tool=='paint' and canvasRect.collidepoint((mx, my)):
		painter(canvas, cmx, cmy, ocmx, ocmy, thicknessX, col, randomCol)

	elif mb[0] and tool=="saveTool":#left mouse click (button down)
		try:
			fname=filedialog.asksaveasfilename(defaultextension=".png")
			image.save(screen.subsurface(canvasRect), fname)#canvas.subsurface(canvasRect)
			tool="paintTool"
		except:
			print("saving error")
	elif mb[0] and tool=='lineTool' and canvasRect.collidepoint((mx, my)):
		lineDrawTool(canvas, cmx, cmy, canvas_copy, sx, sy, col, thicknessX)

	elif mb[0] and tool=="circleTool" and canvasRect.collidepoint((mx, my)):
		circleDrawTool(canvas, mx, my, canvas_copy, sx, sy, col, thicknessX)


	elif mb[0] and tool=='chikoritaStamp' and canvasRect.collidepoint((mx, my)):
		chikorita = ChikoritaAnimation[0]#when the chikorita is put on the canvas it will print the stationary version of the animated version
		canvas.blit(canvas_copy, (0,0))#makes it so that chikorita can be dragged and can't draw it on screen before mouse button press was let go
		canvas.blit(transform.scale(chikorita, (thicknessX,thicknessY)), (cmx-thicknessX/2, cmy-thicknessY/2))#This will spawn Chikorita from the centre of that stamp
	
	elif mb[0] and tool=='bayleefStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy, (0,0))
		bayleef=BayleefAnimation[0]
		canvas.blit(transform.scale(bayleef, (thicknessX,thicknessY)), (cmx-thicknessX/2, cmy-thicknessY/2))

	elif mb[0] and tool=='meganiumStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy, (0,0))
		meganium=MeganiumAnimation[0]
		canvas.blit(transform.scale(meganium, (thicknessX,thicknessY)), (cmx-thicknessX/2, cmy-thicknessY/2))       

	elif mb[0] and tool=='MegaGengarStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy, (0,0))
		MegaGengar=MegaGengarAnimation[0]
		canvas.blit(transform.scale(MegaGengar, (thicknessX,thicknessY)), (cmx-thicknessX/2, cmy-thicknessY/2))
	
	elif mb[0] and tool=='gengarStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy, (0,0))
		gengar=GengarAnimation[0]
		canvas.blit(transform.scale(gengar, (thicknessX,thicknessY)), (cmx-thicknessX/2, cmy-thicknessY/2))

	elif mb[0] and tool=='haunterStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy, (0,0))
		haunter=HaunterAnimation[0]
		canvas.blit(transform.scale(haunter, (thicknessX,thicknessY)), (cmx-thicknessX/2, cmy-thicknessY/2))    
	
	elif mb[0] and tool=='gastlyStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy, (0,0))
		gastly=GastlyAnimation[0]
		canvas.blit(transform.scale(gastly, (thicknessX,thicknessY)), (cmx-thicknessX/2, cmy-thicknessY/2)) 

	elif mb[0] and tool=='infernapeStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy, (0,0))
		infernape=InfernapeAnimation[0]
		canvas.blit(transform.scale(infernape, (thicknessX,thicknessY)), (cmx-thicknessX/2, cmy-thicknessY/2))

	elif mb[0] and tool=='monfernoStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy, (0,0))
		monferno=MonfernoAnimation[0]
		canvas.blit(transform.scale(monferno, (thicknessX,thicknessY)), (cmx-thicknessX/2, cmy-thicknessY/2))   
	
	elif mb[0] and tool=='chimcharStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy,(0,0))
		Chimchar=ChimcharAnimation[0]
		canvas.blit(transform.scale(Chimchar, (thicknessX,thicknessY)), (cmx-thicknessX/2, cmy-thicknessY/2))

	elif mb[0] and tool=='MegaBlastoiseStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy,(0,0))
		MegaBlastoise=MegaBlastoiseAnimation[0]
		canvas.blit(transform.scale(MegaBlastoise, (thicknessX,thicknessY)), (cmx-thicknessX/2, cmy-thicknessY/2))

	elif mb[0] and tool=='BlastoiseStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy,(0,0))
		Blastoise=BlastoiseAnimation[0]
		canvas.blit(transform.scale(Blastoise, (thicknessX,thicknessY)), (cmx-thicknessX/2, cmy-thicknessY/2))

	elif mb[0] and tool=="WartortleStamp" and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy,(0,0))
		Wartortle=WartortleAnimation[0]
		canvas.blit(transform.scale(Wartortle, (thicknessX,thicknessY)), (cmx-thicknessX/2, cmy-thicknessY/2))

	elif mb[0] and tool=='SquirtleStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy,(0,0))
		Squirtle=SquirtleAnimation[0]
		canvas.blit(transform.scale(Squirtle ,(thicknessX, thicknessY)), (cmx-thicknessX/2, cmy-thicknessY/2))

	elif mb[0] and tool=='DarkraiStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy,(0,0))
		Darkrai=DarkraiAnimation[0]
		canvas.blit(transform.scale(Darkrai ,(thicknessX, thicknessY)), (cmx-thicknessX/2, cmy-thicknessY/2))

	elif mb[0] and tool=='GiratinaStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy,(0,0))
		Giratina=GiratinaAnimation[0]
		canvas.blit(transform.scale(Giratina ,(thicknessX, thicknessY)), (cmx-thicknessX/2, cmy-thicknessY/2))

	elif mb[0] and tool=='PalkiaStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy,(0,0))
		Palkia=PalkiaAnimation[0]
		canvas.blit(transform.scale(Palkia ,(thicknessX, thicknessY)), (cmx-thicknessX/2, cmy-thicknessY/2))

	elif mb[0] and tool=='MewtwoStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy,(0,0))
		Mewtwo=MewtwoAnimation[0]
		canvas.blit(transform.scale(Mewtwo ,(thicknessX, thicknessY)), (cmx-thicknessX/3, cmy-thicknessY/3))	
	elif mb[0] and tool=='SyedStamp':
		canvas.blit(canvas_copy, (0,0))
		canvas.blit(transform.scale(idiot, (thicknessX,thicknessY)), (cmx-thicknessX/2, cmy-thicknessY/2))
	myClock.tick(60)
	display.flip()
	ocmx, ocmy = cmx, cmy
##                   Draw Options End                   ##
quit() # closes out pygame window
