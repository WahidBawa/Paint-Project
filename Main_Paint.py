#Main_Paint.py 
##                                   Variable Names/Importing functions                                 ##
# from pygame import * # This will import all functions and actions of pygame
from Defs import *# this imports functions saved in another file to make code more efficient
from Variables import *#imports some variables to make code cleaner 

root = Tk() # sets up Tkinter
root.withdraw() # sets up Tkinter
os.environ['SDL_VIDEO_WINDOW_POS'] = '10,10' # Will open the screen at the specified coordinate
screen = display.set_mode(size) # will create a screen at a certain size
display.set_caption("PokePaint") # Sets the title of the screen
##                      Variable Naming Ends                           ##
##                    Loading Initial Startup Music                 ##
mixer.music.load('MUSIC/SOUND TRACK/Pokemon_-_Gotta_Catch_Em_All_Lyrics.ogg') #loads music
mixer.music.play(-1)# will load and play initial music forever 
##                    Ending Loading Initial Startup Music                 ##
##                      Importing Pictures / Animations / Editing Pictures                        ##
selectedPokemon=image.load("PICS/IMAGES/Templates/pokemon_selected.png")
pokeMenu1=image.load("PICS/IMAGES/Templates/pokemon_selection_menu_cropped.png")
pokeMenu2=image.load("PICS/IMAGES/Templates/pokemon_selection_menu_cropped.png")
pokeMenu3=image.load("PICS/IMAGES/Templates/pokemon_selection_menu_cropped.png")
pokeMenu4=image.load("PICS/IMAGES/Templates/pokemon_selection_menu_cropped.png")

bc1=image.load("PICS/IMAGES/pikachu_background.jpg").convert_alpha() # convert_alpha converts the pixel format of the screen
bc1=transform.scale(bc1, size)# loads initial background and scales it to size

descriptionBox=image.load("PICS/IMAGES/Templates/Dialog_Box_Edited.jpg").convert_alpha()
descriptionBox=transform.scale(descriptionBox, (500,160))

logo=image.load("PICS/IMAGES/Title/PokePaintLogoOfficial.png").convert_alpha()

syed=image.load("PICS/IMAGES/SYED/WIN_20171207_12_15_15_Pro (2).jpg").convert_alpha()
shahoon=image.load("PICS/IMAGES/SYED/Shahoon.jpg").convert_alpha()
usman=image.load("PICS/IMAGES/SYED/USMAN.jpg").convert_alpha()

wheelPic=image.load("PICS/IMAGES/colour_picker.png").convert_alpha()
wheelPic=transform.scale(wheelPic, (155,155))# loads the colour wheel and scales it to size

selected = transform.scale(image.load("PICS/IMAGES/Templates/selected_adjusted.png").convert_alpha(), (40,40)) # loads and transforms the images
hover = transform.scale(image.load("PICS/IMAGES/Templates/hover_adjusted.png").convert_alpha() , (40,40))
stationary = transform.scale(image.load("PICS/IMAGES/Templates/Stationary_adjusted.png").convert_alpha(), (40,40))
for i in range(30):# Imports all pictures that make up the animation of the sprite in the selection and scales them is needed
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

# will import tool selection sprites and scale them to the desired size	
paintOption=image.load("PICS/IMAGES/Tool Selection Sprite/paint_tool.png").convert_alpha()
paintOption=transform.scale(paintOption, (40,40))
pencilOption=transform.scale(image.load("PICS/IMAGES/Tool Selection Sprite/pencil_tool.png"), (40,40)).convert_alpha()
textOption=transform.scale(image.load("PICS/IMAGES/Tool Selection Sprite/text_tool.png"), (40,40)).convert_alpha()
eraserOption=image.load("PICS/IMAGES/Tool Selection Sprite/eraser_tool.png").convert_alpha()
eraserOption=transform.scale(eraserOption, (40,40))
ellipseOption=image.load("PICS/IMAGES/Tool Selection Sprite/ellipse_tool.png").convert_alpha()
ellipseOption=transform.scale(ellipseOption, (40,40))
filledEllipseOption=image.load("PICS/IMAGES/Tool Selection Sprite/filledEllipse_tool.png").convert_alpha()
filledEllipseOption=transform.scale(filledEllipseOption, (40,40))
lineOption=image.load("PICS/IMAGES/Tool Selection Sprite/line_tool.jpg").convert_alpha()
lineOption=transform.scale(lineOption, (40,40))
rectOption=image.load("PICS/IMAGES/Tool Selection Sprite/rect_tool.png").convert_alpha()
rectOption=transform.scale(rectOption, (40,40))
filledRectOption=image.load("PICS/IMAGES/Tool Selection Sprite/filledRect_tool.png").convert_alpha()
filledRectOption=transform.scale(filledRectOption, (40,40))
colOption=image.load("PICS/IMAGES/Tool Selection Sprite/colpicker_tool.png").convert_alpha()
colOption=transform.scale(colOption, (40,40))
colourPickerOption=transform.scale(image.load("PICS/IMAGES/Tool Selection Sprite/colour_picker_tool.png"), (40,40)).convert_alpha()
clearOption=transform.scale(image.load("PICS/IMAGES/Tool Selection Sprite/clear_screen.png"), (40,40)).convert_alpha()
saveOption=transform.scale(image.load("PICS/IMAGES/Tool Selection Sprite/save_tool.png"), (40,40)).convert_alpha()
loadOption=transform.scale(image.load("PICS/IMAGES/Tool Selection Sprite/load_tool.png"), (40,40)).convert_alpha()
##                      End Of Importing Pictures / Animations / Editing Pictures                 ##

##                      Creating Rect Objects                        ##
MegaBlastoiseRect=Rect(1035,175,115,115) # creation of the rect objects in the Pokemon selection tool
infernapeRect=Rect(1165,175,115,115)
MegaGengarRect=Rect(1035,296,115,115)
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
DarkraiRect=Rect(1035,296,115,115)
GiratinaRect=Rect(1165,300,115,115)
PalkiaRect=Rect(1035,425,115,115)
MewtwoRect=Rect(1165,425,115,115)

syedRect=Rect(1035,175,115,115)
shahoonRect=Rect(1165,175,115,115)
usmanRect=Rect(1035,296,115,115)

canvasRect=Rect(150,100,800,500)#setting rect objects for tool selection
saveRect=Rect(20,30,40,40)
loadRect=Rect(70,30,40,40)
paintRect=Rect(20,80,40,40)
eraserRect=Rect(70,80,40,40)
pencilRect=Rect(20,130,40,40)
colourPickerRect=Rect(20,180,40,40)
lineDrawRect=Rect(70,180,40,40)
ellipseDrawRect=Rect(20,230,40,40)
rectDrawRect=Rect(70,230,40,40)
filledEllipseDrawRect=Rect(20,280,40,40)
filledRectDrawRect=Rect(70,280,40,40)
textBoxRect=Rect(20,330,40,40)
clearRect=Rect(70,330,40,40)
wheelRect=wheelPic.get_rect()
wheelRect.topleft = 770, 600
radiusRect=Rect(950,650,135,25)
colourRect=Rect(70,130,40,40)

secretRect=Rect(1326,0,40,40)
currentColRect = Rect(700,600,50,50) # setting rect for the current colour
##                      Creating Rect Objects Ending                        ##

##                      Event Loop Start                        ##
key.set_repeat(500,100)# if a key is held it will repeat it
while running:
	kp=key.get_pressed()# checks for key presses
	for evt in event.get(): 
		if evt.type == QUIT:
			running = False 
		if evt.type == KEYDOWN:
			if evt.key == K_ESCAPE:#if ESC pressed the program will end
					running = False
			if kp[K_LCTRL] and evt.key == K_y:
				if len(control_Y) > 0:
					control_Z.append(control_Y.pop())# if CTRL Y is pressed then it will add the last thing in the control_Y list to the control_Z list 
			if kp[K_LCTRL] and evt.key == K_z:
				if len(control_Z) > 1:
					control_Y.append(control_Z.pop())# if CTRL Z is pressed and the length of control_Z is more than 1 it will add the last thing in control_Z to control_Y
			if evt.key == K_r and tool == "paint":
				randomCol = 1 - randomCol# creates a toggle switch to check if the random colour option is enabled		
			if evt.key == K_o:
				mixer.music.stop()# if the O key is pressed the music will stop
			if evt.key == K_p:
				mixer.music.load('MUSIC/SOUND TRACK/Pokemon_-_Gotta_Catch_Em_All_Lyrics.ogg')
				mixer.music.play(-1)# if P is pressed the music will play again from the start and loop
			if evt.key == K_RIGHT:# this will change the pokemon selection screen
				if pokeSelect == 3 and secret == True:
					pokeSelect = 4	
				if pokeSelect == 2:
					pokeSelect = 3    
				if pokeSelect == 1:
					pokeSelect = 2
			if evt.key == K_LEFT:# this will change the pokemon selection screen
				if pokeSelect==2:
					pokeSelect=1
				if pokeSelect==3:
					pokeSelect=2    
				if pokeSelect == 4 and secret == True:
					pokeSelect = 3	

		if evt.type == MOUSEBUTTONUP:
			if evt.button == 1:
				if canvasRect.collidepoint((mx, my)):
					control_Z.append(canvas.copy())# every time the mouse button lifts up it takes a picture of the screen and adds it to the control_Z list
				elif colourPickerRect.collidepoint(mx,my):# if the colour picker button has been pressed then the following will run
					c = askcolor(title='Pick a Colour') # this will open the colour screen and will assign a colour to the list c
					if c[0] != None:
						col = c[0]  # will make col become the selected colour
					tool = "paint"

		if evt.type == MOUSEBUTTONDOWN:
			if evt.button == 1 or evt.button == 2:
				sx, sy = cmx, cmy ## will assign cmx and cmy to sx and sy which are used for drawing shapes
				ocmx, ocmy = cmx, cmy # ocmx and ocmy will become cmx and cmy which is used for certain toolss
				canvas_copy = canvas.copy() # this captures a picture of the screen
			if evt.button == 4: # if you scroll down the size will increase and will be limited at 4000
				if thickness <= 4000: 
					thickness += int(thickness*0.2)

				if thickness > 4000:
					thickness = 4000
			if evt.button == 5: # is scrolling up size will go down and will be limited to a minimum of 5
				if thickness > 5:
					thickness -= int(thickness*0.2)
	mb = mouse.get_pressed() # will check what on the mouse is being pressed
	mx, my = mouse.get_pos() # will get the position of the mouse and assign it to the variable of mx and my
	if not mb[0] and not mb[2]: # will blit the last thing in the control_Z list to the canvas 
		canvas.blit(control_Z[-1], (0,0))
## Selection Animation Counter Start ## 

	chikorita_counter += 1# will increase counter by 1
	if chikorita_counter > len(ChikoritaAnimation)-1: # if the counter is larger then the animation list the counter will reset
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
## Selection Animation Counter End ##   

##                      CollidePoint Start                        ##
	if mb[0]: # will check if the button has been pressed
		if wheelRect.collidepoint(mx,my): # if you click on the colour wheel it will get the colour on that pixel
			col=screen.get_at((mx,my))
		elif paintRect.collidepoint((mx,my)): # will check if the tool button has been clicked in and will assign the tool name to the variable tool
			tool="paint"
		elif colourPickerRect.collidepoint(mx,my):
			tool = 'colourPicker'	
		elif eraserRect.collidepoint(mx,my):    
			tool = 'eraser'
		elif lineDrawRect.collidepoint(mx,my):
			tool = 'lineTool'
		elif ellipseDrawRect.collidepoint(mx,my):
			tool = 'ellipseTool'
		elif filledEllipseDrawRect.collidepoint(mx,my):
			tool = "filledEllipseTool"	
		elif rectDrawRect.collidepoint(mx,my):
			tool = "rectTool"	
		elif filledRectDrawRect.collidepoint(mx,my):
			tool = "filledRectTool"	
		elif textBoxRect.collidepoint(mx,my):
			tool = "textTool"	
		elif saveRect.collidepoint(mx,my):
			tool = "saveTool"
		elif loadRect.collidepoint(mx,my):
			tool = "loadTool"
		elif pencilRect.collidepoint(mx,my):
			tool = "pencil"
		elif radiusRect.collidepoint(mx,my):
			tool = "radiusChange"
		elif colourRect.collidepoint(mx,my):
			tool = "colour"	
		elif clearRect.collidepoint(mx,my):
			tool = "clear"
		elif secretRect.collidepoint(mx,my):
			secret_c += 1
			if secret_c >= 1:		
				secret = True
				tool = "secret"
		if pokeSelect == 1: # this will check which page in the pokemon selection page is showing and will only check for the pokemon that are showing
			if MegaBlastoiseRect.collidepoint(mx,my):# Will check if you are clicking on the specified area and will assign the tool to the variable tool
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
		if pokeSelect == 2:
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
		if pokeSelect == 3:
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
		if pokeSelect == 4:
			if syedRect.collidepoint(mx,my):
				tool='SyedStamp'
			elif shahoonRect.collidepoint(mx,my):
				tool="shahoonStamp"
			elif usmanRect.collidepoint(mx,my):
				tool="usmanStamp"		
##                      CollidePoint End                       ##
##                   Surface / Canvas / Blit / Start               ##
	screen.blit(bc1, (0,0))# blits the background picture to the screen
	screen.blit(descriptionBox, (150,600))# blits the description box tp the screen
	
	## Tool Selection Check Red ##

	screen.blit(paintOption, paintRect)# blits the tool option picture to the screen
	if tool == 'paint': # will perform the tasks if the certain tool is selected
		screen.blit(selected, paintRect)# will blit the selected picture to the tool rect
		paintDescription=pokeGB_Font.render("This is the famous brush ",True,BLACK).convert_alpha()# this is the description itself
		screen.blit(paintDescription, (175,625)) # this blits the description to the screen
		paintDescription=pokeGB_Font.render("tool, you can draw whate-",True,BLACK).convert_alpha()
		screen.blit(paintDescription, (175,643))
		paintDescription=pokeGB_Font.render("ver you want! Press the R",True,BLACK).convert_alpha()
		screen.blit(paintDescription, (175,661))
		paintDescription=pokeGB_Font.render("button to toggle random ",True,BLACK).convert_alpha()
		screen.blit(paintDescription, (175,679))
		paintDescription=pokeGB_Font.render("colours!!",True,BLACK).convert_alpha()
		screen.blit(paintDescription, (175,697))
	elif paintRect.collidepoint(mx,my):
		screen.blit(hover, paintRect) # if the mouse is just hovering over the tool then it will blit this image to the tool rect
	else: # if the tool is not hovering or clicking on the tool then it will blit this image to the tool rect
		screen.blit(stationary, paintRect)

	if tool == 'secret':
		secretDescription=pokeGB_Font.render("Secret Stickers Unlocked",True,BLACK).convert_alpha()
		screen.blit(secretDescription, (175,625))

	screen.blit(eraserOption, eraserRect)
	if tool=="eraser":  
		screen.blit(selected, eraserRect)
		eraserDescription=pokeGB_Font.render("This is the eraser tool, ",True,BLACK).convert_alpha()
		screen.blit(eraserDescription, (175,625))
		eraserDescription=pokeGB_Font.render("this tool will help you ",True,BLACK).convert_alpha()
		screen.blit(eraserDescription, (175,643))
		eraserDescription=pokeGB_Font.render("erase all your mistakes!",True,BLACK).convert_alpha()
		screen.blit(eraserDescription, (175,661))
	elif eraserRect.collidepoint(mx,my):
		screen.blit(hover, eraserRect)	
	else:
		screen.blit(stationary, eraserRect)	
	
	screen.blit(lineOption, lineDrawRect)
	if tool=="lineTool":
		screen.blit(selected, lineDrawRect)
		lineDescription=pokeGB_Font.render("This is the straightest, ",True,BLACK).convert_alpha()
		screen.blit(lineDescription, (175,625))
		lineDescription=pokeGB_Font.render("most brilliant line of a-",True,BLACK).convert_alpha()
		screen.blit(lineDescription, (175,643))
		lineDescription=pokeGB_Font.render("ll the lands. Use it to ",True,BLACK).convert_alpha()
		screen.blit(lineDescription, (175,661))
		lineDescription=pokeGB_Font.render("line up all you desires!!",True,BLACK).convert_alpha()
		screen.blit(lineDescription, (175,679))
	elif lineDrawRect.collidepoint(mx,my):
		screen.blit(hover, lineDrawRect)	
	else:
		screen.blit(stationary, lineDrawRect)	

	screen.blit(ellipseOption, ellipseDrawRect)
	if tool=="ellipseTool":
		screen.blit(selected, ellipseDrawRect)
		ellipseDescription=pokeGB_Font.render("The ellipse tool draws a ",True,BLACK).convert_alpha()
		screen.blit(ellipseDescription, (175,625))
		ellipseDescription=pokeGB_Font.render("oval looking shape, hold",True,BLACK).convert_alpha()
		screen.blit(ellipseDescription, (175,643))
		ellipseDescription=pokeGB_Font.render("SHIFT and it will draw a ",True,BLACK).convert_alpha()
		screen.blit(ellipseDescription, (175,661))
		ellipseDescription=pokeGB_Font.render("circle. Circle it!!!",True,BLACK).convert_alpha()
		screen.blit(ellipseDescription, (175,679))
	elif ellipseDrawRect.collidepoint(mx,my):
		screen.blit(hover, ellipseDrawRect)	
	else:
		screen.blit(stationary, ellipseDrawRect)

	screen.blit(filledEllipseOption, filledEllipseDrawRect)
	if tool=="filledEllipseTool":
		screen.blit(selected, filledEllipseDrawRect)
		filledEllipseDescription=pokeGB_Font.render("This is the ellipse tool",True,BLACK).convert_alpha()
		screen.blit(filledEllipseDescription, (175,625))
		filledEllipseDescription=pokeGB_Font.render("but filled. Hold SHIFT ",True,BLACK).convert_alpha()
		screen.blit(filledEllipseDescription, (175,643))
		filledEllipseDescription=pokeGB_Font.render("and you will be able to ",True,BLACK).convert_alpha()
		screen.blit(filledEllipseDescription, (175,661))
		filledEllipseDescription=pokeGB_Font.render("draw a circle!!!",True,BLACK).convert_alpha()
		screen.blit(filledEllipseDescription, (175,679))
	elif filledEllipseDrawRect.collidepoint(mx,my):
		screen.blit(hover, filledEllipseDrawRect)	
	else:
		screen.blit(stationary, filledEllipseDrawRect)
	
	screen.blit(rectOption, rectDrawRect)		
	if tool=="rectTool":
		screen.blit(selected, rectDrawRect)
		rectDescription=pokeGB_Font.render("This is the infamous rect",True,BLACK).convert_alpha()
		screen.blit(rectDescription, (175,625))
		rectDescription=pokeGB_Font.render("tool. Use this tool to d-",True,BLACK).convert_alpha()
		screen.blit(rectDescription, (175,643))
		rectDescription=pokeGB_Font.render("raw rectangles in all si- ",True,BLACK).convert_alpha()
		screen.blit(rectDescription, (175,661))
		rectDescription=pokeGB_Font.render("zes!! ",True,BLACK).convert_alpha()
		screen.blit(rectDescription, (175,679))
	elif rectDrawRect.collidepoint(mx,my):
		screen.blit(hover, rectDrawRect)	
	else:
		screen.blit(stationary, rectDrawRect)	
	screen.blit(filledRectOption, filledRectDrawRect)
	if tool=="filledRectTool":
		screen.blit(selected, filledRectDrawRect)
		filledRectDescription=pokeGB_Font.render("This tool creates filled ",True,BLACK).convert_alpha()
		screen.blit(filledRectDescription, (175,625))
		filledRectDescription=pokeGB_Font.render("rectangles. You can block",True,BLACK).convert_alpha()
		screen.blit(filledRectDescription, (175,643))
		filledRectDescription=pokeGB_Font.render("out all your haters with",True,BLACK).convert_alpha()
		screen.blit(filledRectDescription, (175,661))
		filledRectDescription=pokeGB_Font.render("no problems at all!!",True,BLACK).convert_alpha()
		screen.blit(filledRectDescription, (175,679))
	elif filledRectDrawRect.collidepoint(mx,my):
		screen.blit(hover, filledRectDrawRect)	
	else:
		screen.blit(stationary, filledRectDrawRect)

	screen.blit(saveOption, saveRect)
	if tool=="saveTool":
		screen.blit(selected, saveRect)
		saveDescription=pokeGB_Font.render("This is the save tool, it",True,BLACK).convert_alpha()
		screen.blit(saveDescription, (175,625))
		saveDescription=pokeGB_Font.render("is used so that you can ",True,BLACK).convert_alpha()
		screen.blit(saveDescription, (175,643))
		saveDescription=pokeGB_Font.render("save your pieces of art ",True,BLACK).convert_alpha()
		screen.blit(saveDescription, (175,661))
		saveDescription=pokeGB_Font.render("to admire them at a later",True,BLACK).convert_alpha()
		screen.blit(saveDescription, (175,679))
		saveDescription=pokeGB_Font.render("time.",True,BLACK).convert_alpha()
		screen.blit(saveDescription, (175,697))
	elif saveRect.collidepoint(mx,my):
		screen.blit(hover, saveRect)	
	else:
		screen.blit(stationary, saveRect)

	screen.blit(loadOption, loadRect)
	if tool=="loadTool":
		screen.blit(selected, loadRect)
		loadDescription=pokeGB_Font.render("This is the load tool, it",True,BLACK).convert_alpha()
		screen.blit(loadDescription, (175,625))
		loadDescription=pokeGB_Font.render("is used so that you can ",True,BLACK).convert_alpha()
		screen.blit(loadDescription, (175,643))
		loadDescription=pokeGB_Font.render("load your art if you want ",True,BLACK).convert_alpha()
		screen.blit(loadDescription, (175,661))
		loadDescription=pokeGB_Font.render("to add more to it, have a",True,BLACK).convert_alpha()
		screen.blit(loadDescription, (175,679))
		loadDescription=pokeGB_Font.render("good time improving your ",True,BLACK).convert_alpha()
		screen.blit(loadDescription, (175,697))
		loadDescription=pokeGB_Font.render("art works.",True,BLACK).convert_alpha()
		screen.blit(loadDescription, (175,715))
	elif loadRect.collidepoint(mx,my):
		screen.blit(hover, loadRect)	
	else:
		screen.blit(stationary, loadRect)
	screen.blit(textOption, textBoxRect)
	if tool == "textTool":
		screen.blit(selected, textBoxRect)
		textDescription=pokeGB_Font.render("This is the text tool, it",True,BLACK).convert_alpha()
		screen.blit(textDescription, (175,625))
		textDescription=pokeGB_Font.render("is used so that you can ",True,BLACK).convert_alpha()
		screen.blit(textDescription, (175,643))
		textDescription=pokeGB_Font.render("place pieces of text onto",True,BLACK).convert_alpha()
		screen.blit(textDescription, (175,661))
		textDescription=pokeGB_Font.render("the canvas. To start cli-",True,BLACK).convert_alpha()
		screen.blit(textDescription, (175,679))
		textDescription=pokeGB_Font.render("ck on the canvas. TYPE!!",True,BLACK).convert_alpha()
		screen.blit(textDescription, (175,697))
	elif textBoxRect.collidepoint(mx,my):
		screen.blit(hover, textBoxRect)	
	else:		           
		screen.blit(stationary, textBoxRect)

	screen.blit(colOption, colourPickerRect)
	if tool == 'colourPicker':
		screen.blit(selected, colourPickerRect)		
		colourPickerDescription=pokeGB_Font.render("This tool allows you to ",True,BLACK).convert_alpha()
		screen.blit(colourPickerDescription, (175,625))
		colourPickerDescription=pokeGB_Font.render("choose any colour you can",True,BLACK).convert_alpha()
		screen.blit(colourPickerDescription, (175,643))
		colourPickerDescription=pokeGB_Font.render("think of and use them to ",True,BLACK).convert_alpha()
		screen.blit(colourPickerDescription, (175,661))
		colourPickerDescription=pokeGB_Font.render("draw beautiful paintings!",True,BLACK).convert_alpha()
		screen.blit(colourPickerDescription, (175,679))
	elif colourPickerRect.collidepoint(mx,my):
		screen.blit(hover, colourPickerRect)	
	else:	
		screen.blit(stationary, colourPickerRect)	

	screen.blit(pencilOption, pencilRect)
	if tool == "pencil":
		screen.blit(selected, pencilRect)
		pencilDescription=pokeGB_Font.render("This is a pencil. Just a ",True,BLACK).convert_alpha()
		screen.blit(pencilDescription, (175,625))
		pencilDescription=pokeGB_Font.render("normal pencil. What else ",True,BLACK).convert_alpha()
		screen.blit(pencilDescription, (175,643))
		pencilDescription=pokeGB_Font.render("do you want me to say!",True,BLACK).convert_alpha()
		screen.blit(pencilDescription, (175,661))
	elif pencilRect.collidepoint(mx,my):
		screen.blit(hover, pencilRect)
	else:
		screen.blit(stationary, pencilRect)		

	if tool == "radiusChange":
		radiusInfo=hollowPokeFont.render("Click on the radius information",True,BLACK).convert_alpha()
		screen.blit(radiusInfo, (950,680))
		radiusInfo=hollowPokeFont.render("to type in a radius !",True,BLACK).convert_alpha()
		screen.blit(radiusInfo, (950,710))
	else:	
		radiusInfo=hollowPokeFont.render("Click on the radius information",True,BLACK).convert_alpha()
		screen.blit(radiusInfo, (950,680))
		radiusInfo=hollowPokeFont.render("to type in a radius !",True,BLACK).convert_alpha()
		screen.blit(radiusInfo, (950,710))

	screen.blit(colourPickerOption, colourRect)
	if tool == "colour":
		screen.blit(selected, colourRect)
		colourDescription=pokeGB_Font.render("See a colour you like on ",True,BLACK).convert_alpha()
		screen.blit(colourDescription, (175,625))
		colourDescription=pokeGB_Font.render("the canvas? Well you're ",True,BLACK).convert_alpha()
		screen.blit(colourDescription, (175,643))
		colourDescription=pokeGB_Font.render("in luck! Capture those ",True,BLACK).convert_alpha()
		screen.blit(colourDescription, (175,661))
		colourDescription=pokeGB_Font.render("eye catching colours and ",True,BLACK).convert_alpha()
		screen.blit(colourDescription, (175,679))
		colourDescription=pokeGB_Font.render("use them everywhere!!",True,BLACK).convert_alpha()
		screen.blit(colourDescription, (175,697))
	elif colourRect.collidepoint(mx,my):
		screen.blit(hover, colourRect)
	else:
		screen.blit(stationary, colourRect)			

	screen.blit(clearOption, clearRect)
	if tool == "clear":
		screen.blit(selected, clearRect)
		clearDescription=pokeGB_Font.render("Did you make another bad",True,BLACK).convert_alpha()# this is the description itself
		screen.blit(clearDescription, (175,625)) # this blits the description to the screen
		clearDescription=pokeGB_Font.render("painting and want to scr-",True,BLACK).convert_alpha()
		screen.blit(clearDescription, (175,643))
		clearDescription=pokeGB_Font.render("ap the painting? Just pr- ",True,BLACK).convert_alpha()
		screen.blit(clearDescription, (175,661))
		clearDescription=pokeGB_Font.render("ess this button and your",True,BLACK).convert_alpha()
		screen.blit(clearDescription, (175,679))
		clearDescription=pokeGB_Font.render("painting will disappear!",True,BLACK).convert_alpha()
		screen.blit(clearDescription, (175,697))
	elif clearRect.collidepoint(mx,my):
		screen.blit(hover, clearRect)
	else:
		screen.blit(stationary, clearRect)			
	## Tool Selection Check Red End ##
	## Tool Sprites Start ##
	
	if pokeSelect == 1:# if pokeSelect equals a certain number the same picture is blitted to the screen
		screen.blit(pokeMenu1, (1025, 170))
	if pokeSelect == 2:
		screen.blit(pokeMenu2, (1025, 170))
	if pokeSelect == 3:
		screen.blit(pokeMenu3, (1025, 170))
	if pokeSelect == 4:
		screen.blit(pokeMenu4, (1025, 170))
			
	## Tool Sprites End ##
	screen.blit(logo, (350,0)) # will blit the logo to the screen
	screen.blit(wheelPic, wheelRect)# will blit the colour wheel to the screen
	##          Mouse Position Start       ##
	mousePos=pokeFont.render("Mouse Position: " + str(mx) + ", " + str(my),True,BLACK).convert_alpha()
	screen.blit(mousePos, (955,600))# this will blit the mouse position to the screen

	radius=pokeFont.render("Radius: "+str(thickness),True,BLACK).convert_alpha()
	screen.blit(radius, (955,650))# this will blit the thickness to the screen

	O=pokeFont.render("O - Stop Music",True,BLACK).convert_alpha()
	screen.blit(O, (150,30))# this will blit the instruction to the screen to the screen

	P=pokeFont.render("P - Play Music",True,BLACK).convert_alpha()
	screen.blit(P, (770,30))# this will blit the instruction to the screen to the screen

	##          Mouse Position Ended       ##

	screen.blit(selectedPokemon, (1025,50))# the selected Pokemon will be blitted to thw screen
	draw.rect(screen, col, currentColRect)# This shows the current colour to this box

	if pokeSelect == 1:# will show the pokemon animations corresponding to the pokeSelect number
		screen.blit(transform.scale(MeganiumAnimation[meganium_counter], (115,115)), meganiumRect)
		screen.blit(transform.scale(MegaBlastoiseAnimation[MegaBlastoise_counter],(115,115)),MegaBlastoiseRect)
		screen.blit(transform.scale(InfernapeAnimation[infernape_counter],(115,115)),infernapeRect)
		screen.blit(transform.scale(GengarAnimation[gengar_counter], (115,115)), gengarRect)
		screen.blit(transform.scale(MegaGengarAnimation[MegaGengar_counter], (115,115)),MegaGengarRect)
		screen.blit(transform.scale(BlastoiseAnimation[Blastoise_counter],(115,115)),BlastoiseRect)
	if pokeSelect == 2:
		screen.blit(transform.scale(HaunterAnimation[haunter_counter], (115,115)),haunterRect)
		screen.blit(transform.scale(MonfernoAnimation[monferno_counter],(115,115)),monfernoRect)
		screen.blit(transform.scale(WartortleAnimation[Wartortle_counter],(115,115)),WartortleRect)
		screen.blit(transform.scale(BayleefAnimation[bayleef_counter], (115,115)), bayleefRect)
		screen.blit(transform.scale(GastlyAnimation[gastly_counter],(115,115)),gastlyRect)
		screen.blit(transform.scale(ChimcharAnimation[chimchar_counter],(115,115)),chimcharRect)
	if pokeSelect == 3:
		screen.blit(transform.scale(ChikoritaAnimation[chikorita_counter], (115,115)), chikoritaRect)
		screen.blit(transform.scale(SquirtleAnimation[Squirtle_counter],(115,115)),SquirtleRect)
		screen.blit(transform.scale(DarkraiAnimation[Darkrai_counter],(115,115)),DarkraiRect)
		screen.blit(transform.scale(GiratinaAnimation[Giratina_counter],(115,115)),GiratinaRect)
		screen.blit(transform.scale(PalkiaAnimation[Palkia_counter],(115,115)),PalkiaRect)
		screen.blit(transform.scale(MewtwoAnimation[Mewtwo_counter],(115,115)),MewtwoRect)
	if pokeSelect == 4:
		screen.blit(transform.scale(syed, (115,115)), syedRect)
		screen.blit(transform.scale(shahoon, (115,115)), shahoonRect)
		screen.blit(transform.scale(usman, (115,115)), usmanRect)

	if tool == "MegaBlastoiseStamp":# if the tool is the specified tool, then it will blit the pokemon into the selected box and blit a description
		screen.blit(transform.scale(MegaBlastoiseAnimation[MegaBlastoise_counter],(115,115)),(1035,55))
		MegaBlastoiseDescription=pokeGB_Font.render("The jets of water it spo-",True,BLACK).convert_alpha()
		screen.blit(MegaBlastoiseDescription, (175,625))
		MegaBlastoiseDescription=pokeGB_Font.render("uts from the rocket cann-",True,BLACK).convert_alpha()
		screen.blit(MegaBlastoiseDescription, (175,643))
		MegaBlastoiseDescription=pokeGB_Font.render("ons on its shell can pu-",True,BLACK).convert_alpha()
		screen.blit(MegaBlastoiseDescription, (175,661))
		MegaBlastoiseDescription=pokeGB_Font.render("nch through thick steel.",True,BLACK).convert_alpha()
		screen.blit(MegaBlastoiseDescription, (175,679))

	elif tool == "MegaGengarStamp":
		screen.blit(transform.scale(MegaGengarAnimation[MegaGengar_counter],(115,115)),(1035,55))
		MegaGengarDescription=pokeGB_Font.render("The leer that floats in ",True,BLACK).convert_alpha()
		screen.blit(MegaGengarDescription, (175,625))
		MegaGengarDescription=pokeGB_Font.render("darkness belongs to Mega",True,BLACK).convert_alpha()
		screen.blit(MegaGengarDescription, (175,643))
		MegaGengarDescription=pokeGB_Font.render("Gengar delighting in cas-",True,BLACK).convert_alpha()
		screen.blit(MegaGengarDescription, (175,661))
		MegaGengarDescription=pokeGB_Font.render("ting curses on people.",True,BLACK).convert_alpha()
		screen.blit(MegaGengarDescription, (175,679))

	elif tool == "gengarStamp":
		screen.blit(transform.scale(GengarAnimation[gengar_counter],(115,115)),(1035,55))   
		GengarDescription=pokeGB_Font.render("The leer that floats in ",True,BLACK).convert_alpha()
		screen.blit(GengarDescription, (175,625))
		GengarDescription=pokeGB_Font.render("darkness belongs to a ",True,BLACK).convert_alpha()
		screen.blit(GengarDescription, (175,643))
		GengarDescription=pokeGB_Font.render("Gengar delighting in cas-",True,BLACK).convert_alpha()
		screen.blit(GengarDescription, (175,661))
		GengarDescription=pokeGB_Font.render("ting curses on people.",True,BLACK).convert_alpha()
		screen.blit(GengarDescription, (175,679))
	elif tool == "infernapeStamp":
		screen.blit(transform.scale(InfernapeAnimation[infernape_counter],(115,115)),(1035,55))
		infernapeDescription=pokeGB_Font.render("It tosses its enemies aro-",True,BLACK).convert_alpha()
		screen.blit(infernapeDescription, (175,625))
		infernapeDescription=pokeGB_Font.render("und with agility. It uses",True,BLACK).convert_alpha()
		screen.blit(infernapeDescription, (175,643))
		infernapeDescription=pokeGB_Font.render("all its limbs to fight in",True,BLACK).convert_alpha()
		screen.blit(infernapeDescription, (175,661))
		infernapeDescription=pokeGB_Font.render("its own unique style.",True,BLACK).convert_alpha()
		screen.blit(infernapeDescription, (175,679))
	elif tool == "meganiumStamp":
		screen.blit(transform.scale(MeganiumAnimation[meganium_counter],(115,115)),(1035,55))
		meganiumDescription=pokeGB_Font.render("Meganium's breath has the ",True,BLACK).convert_alpha()
		screen.blit(meganiumDescription, (175,625))
		meganiumDescription=pokeGB_Font.render("power to revive dead gra-",True,BLACK).convert_alpha()
		screen.blit(meganiumDescription, (175,643))
		meganiumDescription=pokeGB_Font.render("ss and plants. It can ma-",True,BLACK).convert_alpha()
		screen.blit(meganiumDescription, (175,661))
		meganiumDescription=pokeGB_Font.render("ke them healthy again.",True,BLACK).convert_alpha()
		screen.blit(meganiumDescription, (175,679))
	elif tool == "BlastoiseStamp":
		screen.blit(transform.scale(BlastoiseAnimation[Blastoise_counter],(115,115)),(1035,55))
		BlastoiseDescription=pokeGB_Font.render("The jets of water it spo-",True,BLACK).convert_alpha()
		screen.blit(BlastoiseDescription, (175,625))
		BlastoiseDescription=pokeGB_Font.render("uts from the rocket cann-",True,BLACK).convert_alpha()
		screen.blit(BlastoiseDescription, (175,643))
		BlastoiseDescription=pokeGB_Font.render("ons on its shell can pu-",True,BLACK).convert_alpha()
		screen.blit(BlastoiseDescription, (175,661))
		BlastoiseDescription=pokeGB_Font.render("nch through thick steel.",True,BLACK).convert_alpha()
		screen.blit(BlastoiseDescription, (175,679))
	elif tool == "haunterStamp":
		screen.blit(transform.scale(HaunterAnimation[haunter_counter],(115,115)),(1035,60))
		haunterDescription=pokeGB_Font.render("On moonless nights, Haun-",True,BLACK).convert_alpha()
		screen.blit(haunterDescription, (175,625))
		haunterDescription=pokeGB_Font.render("ter searches for someone ",True,BLACK).convert_alpha()
		screen.blit(haunterDescription, (175,643))
		haunterDescription=pokeGB_Font.render("to curse, so it's best ",True,BLACK).convert_alpha()
		screen.blit(haunterDescription, (175,661))
		haunterDescription=pokeGB_Font.render("not to go out walking ar-",True,BLACK).convert_alpha()
		screen.blit(haunterDescription, (175,679))
		haunterDescription=pokeGB_Font.render("ound.",True,BLACK).convert_alpha()
		screen.blit(haunterDescription, (175,697))
	elif tool == "monfernoStamp":
		screen.blit(transform.scale(MonfernoAnimation[monferno_counter],(115,115)),(1035,55))
		monfernoDescription=pokeGB_Font.render("It uses ceilings and wal-",True,BLACK).convert_alpha()
		screen.blit(monfernoDescription, (175,625))
		monfernoDescription=pokeGB_Font.render("ls to launch aerial atta-",True,BLACK).convert_alpha()
		screen.blit(monfernoDescription, (175,643))
		monfernoDescription=pokeGB_Font.render("cks. Its fiery tail is b-",True,BLACK).convert_alpha()
		screen.blit(monfernoDescription, (175,661))
		monfernoDescription=pokeGB_Font.render("ut one weapon.",True,BLACK).convert_alpha()
		screen.blit(monfernoDescription, (175,679))
	elif tool == "gastlyStamp":
		screen.blit(transform.scale(GastlyAnimation[gastly_counter],(115,115)),(1035,55))
		gastlyDescription=pokeGB_Font.render("Born from gases, anyone ",True,BLACK).convert_alpha()
		screen.blit(gastlyDescription, (175,625))
		gastlyDescription=pokeGB_Font.render("would faint if engulfed ",True,BLACK).convert_alpha()
		screen.blit(gastlyDescription, (175,643))
		gastlyDescription=pokeGB_Font.render("by its gaseous body, whi-",True,BLACK).convert_alpha()
		screen.blit(gastlyDescription, (175,661))
		gastlyDescription=pokeGB_Font.render("ch contains poison.",True,BLACK).convert_alpha()
		screen.blit(gastlyDescription, (175,679))
	elif tool == "bayleefStamp":
		screen.blit(transform.scale(BayleefAnimation[bayleef_counter],(110,110)),(1035,60))
		bayleefDescription=pokeGB_Font.render("The buds that ring its ",True,BLACK).convert_alpha()
		screen.blit(bayleefDescription, (175,625))
		bayleefDescription=pokeGB_Font.render("neck give off a spicy ar-",True,BLACK).convert_alpha()
		screen.blit(bayleefDescription, (175,643))
		bayleefDescription=pokeGB_Font.render("oma that perks people up.",True,BLACK).convert_alpha()
		screen.blit(bayleefDescription, (175,661))
	elif tool == "chimcharStamp":
		screen.blit(transform.scale(ChimcharAnimation[chimchar_counter],(115,115)),(1035,55))
		chimcharDescription=pokeGB_Font.render("Its fiery rear end is fu-",True,BLACK).convert_alpha()
		screen.blit(chimcharDescription, (175,625))
		chimcharDescription=pokeGB_Font.render("eled by gas made in its ",True,BLACK).convert_alpha()
		screen.blit(chimcharDescription, (175,643))
		chimcharDescription=pokeGB_Font.render("belly. Even rain can't e-",True,BLACK).convert_alpha()
		screen.blit(chimcharDescription, (175,661))
		chimcharDescription=pokeGB_Font.render("xtinguish the fire.",True,BLACK).convert_alpha()
		screen.blit(chimcharDescription, (175,679))
	elif tool == "WartortleStamp":
		screen.blit(transform.scale(WartortleAnimation[Wartortle_counter],(110,110)),(1035,60))
		wartortleDescription=pokeGB_Font.render("It is said to live 10,000",True,BLACK).convert_alpha()
		screen.blit(wartortleDescription, (175,625))
		wartortleDescription=pokeGB_Font.render("years. Its furry tail is ",True,BLACK).convert_alpha()
		screen.blit(wartortleDescription, (175,643))
		wartortleDescription=pokeGB_Font.render("popular as a symbol of ",True,BLACK).convert_alpha()
		screen.blit(wartortleDescription, (175,661))
		wartortleDescription=pokeGB_Font.render("longevity.",True,BLACK).convert_alpha()
		screen.blit(wartortleDescription, (175,679))
	elif tool == "SquirtleStamp":
		screen.blit(transform.scale(SquirtleAnimation[Squirtle_counter],(110,110)),(1035,60))
		squirtleDescription=pokeGB_Font.render("Shoots water at prey whi-",True,BLACK).convert_alpha()
		screen.blit(squirtleDescription, (175,625))
		squirtleDescription=pokeGB_Font.render("le in the water.Withdraws",True,BLACK).convert_alpha()
		screen.blit(squirtleDescription, (175,643))
		squirtleDescription=pokeGB_Font.render("into its shell when in ",True,BLACK).convert_alpha()
		screen.blit(squirtleDescription, (175,661))
		squirtleDescription=pokeGB_Font.render("danger.",True,BLACK).convert_alpha()
		screen.blit(squirtleDescription, (175,679))
	elif tool == "chikoritaStamp":
		screen.blit(transform.scale(ChikoritaAnimation[chikorita_counter],(110,110)),(1035,60))
		chikoritaDescription=pokeGB_Font.render("Its pleasantly aromatic ",True,BLACK).convert_alpha()
		screen.blit(chikoritaDescription, (175,625))
		chikoritaDescription=pokeGB_Font.render("leaf has the ability to ",True,BLACK).convert_alpha()
		screen.blit(chikoritaDescription, (175,643))
		chikoritaDescription=pokeGB_Font.render("check humidity and tempe-",True,BLACK).convert_alpha()
		screen.blit(chikoritaDescription, (175,661))
		chikoritaDescription=pokeGB_Font.render("rature.",True,BLACK).convert_alpha()
		screen.blit(chikoritaDescription, (175,679))
	elif tool == "DarkraiStamp":
		screen.blit(transform.scale(DarkraiAnimation[Darkrai_counter],(115,115)),(1035,50))
		darkraiDescription=pokeGB_Font.render("It can lull people to sl-",True,BLACK).convert_alpha()
		screen.blit(darkraiDescription, (175,625))
		darkraiDescription=pokeGB_Font.render("eep and make them dream. ",True,BLACK).convert_alpha()
		screen.blit(darkraiDescription, (175,643))
		darkraiDescription=pokeGB_Font.render("It is active during nigh-",True,BLACK).convert_alpha()
		screen.blit(darkraiDescription, (175,661))
		darkraiDescription=pokeGB_Font.render("ts of the new moon.",True,BLACK).convert_alpha()
		screen.blit(darkraiDescription, (175,679))
	elif tool == "GiratinaStamp":
		screen.blit(transform.scale(GiratinaAnimation[Giratina_counter],(110,110)),(1035,60))
		giratinaDescription=pokeGB_Font.render("It was banished for its ",True,BLACK).convert_alpha()
		screen.blit(giratinaDescription, (175,625))
		giratinaDescription=pokeGB_Font.render("violence. It silently ga-",True,BLACK).convert_alpha()
		screen.blit(giratinaDescription, (175,643))
		giratinaDescription=pokeGB_Font.render("zed upon the old world f-",True,BLACK).convert_alpha()
		screen.blit(giratinaDescription, (175,661))
		giratinaDescription=pokeGB_Font.render("rom the Distortion World.",True,BLACK).convert_alpha()
		screen.blit(giratinaDescription, (175,679))
	elif tool == "PalkiaStamp":
		screen.blit(transform.scale(PalkiaAnimation[Palkia_counter],(110,110)),(1035,60))
		palkiaDescription=pokeGB_Font.render("It has the ability to di-",True,BLACK).convert_alpha()
		screen.blit(palkiaDescription, (175,625))
		palkiaDescription=pokeGB_Font.render("stort space. It is descr-",True,BLACK).convert_alpha()
		screen.blit(palkiaDescription, (175,643))
		palkiaDescription=pokeGB_Font.render("ibed as a deity in Sinnoh",True,BLACK).convert_alpha()
		screen.blit(palkiaDescription, (175,661))
		palkiaDescription=pokeGB_Font.render("region mythology.",True,BLACK).convert_alpha()
		screen.blit(palkiaDescription, (175,679))
	elif tool == "MewtwoStamp":
		screen.blit(transform.scale(MewtwoAnimation[Mewtwo_counter],(110,110)),(1035,60))           
		mewtwoDescription=pokeGB_Font.render("Said to rest quietly in ",True,BLACK).convert_alpha()
		screen.blit(mewtwoDescription, (175,625))
		mewtwoDescription=pokeGB_Font.render("an undiscovered cave, th-",True,BLACK).convert_alpha()
		screen.blit(mewtwoDescription, (175,643))
		mewtwoDescription=pokeGB_Font.render("is Pokémon was created so-",True,BLACK).convert_alpha()
		screen.blit(mewtwoDescription, (175,661))
		mewtwoDescription=pokeGB_Font.render("lely for battling.",True,BLACK).convert_alpha()
		screen.blit(mewtwoDescription, (175,679))

	elif tool=="SyedStamp":
		screen.blit(transform.scale(syed ,(115,115)), (1035,55))
		syedDescription=pokeGB_Font.render("This is the master of all.",True,BLACK).convert_alpha()
		screen.blit(syedDescription, (175,625))
		syedDescription=pokeGB_Font.render("The legend is that he can",True,BLACK).convert_alpha()
		screen.blit(syedDescription, (175,643))
		syedDescription=pokeGB_Font.render("make your program 90 per-",True,BLACK).convert_alpha()
		screen.blit(syedDescription, (175,661))
		syedDescription=pokeGB_Font.render("cent better!",True,BLACK).convert_alpha()
		screen.blit(syedDescription, (175,679))
	elif tool=='shahoonStamp':
		screen.blit(transform.scale(shahoon ,(115,115)), (1035,55))
		shahoonDescription=pokeGB_Font.render("This is the most powerful",True,BLACK).convert_alpha()
		screen.blit(shahoonDescription, (175,625))
		shahoonDescription=pokeGB_Font.render("alchemist in all the land.",True,BLACK).convert_alpha()
		screen.blit(shahoonDescription, (175,643))
		shahoonDescription=pokeGB_Font.render("He can make your crap pa-",True,BLACK).convert_alpha()
		screen.blit(shahoonDescription, (175,661))
		shahoonDescription=pokeGB_Font.render("intings into gold!!!",True,BLACK).convert_alpha()
		screen.blit(shahoonDescription, (175,679))
	elif tool=="usmanStamp":
		screen.blit(transform.scale(usman ,(115,115)), (1035,55))
		usmanDescription=pokeGB_Font.render("This is the ancient beast",True,BLACK).convert_alpha()
		screen.blit(usmanDescription, (175,625))
		usmanDescription=pokeGB_Font.render("only known as the Usman!!",True,BLACK).convert_alpha()
		screen.blit(usmanDescription, (175,643))
		usmanDescription=pokeGB_Font.render("Make your painting terri-",True,BLACK).convert_alpha()
		screen.blit(usmanDescription, (175,661))
		usmanDescription=pokeGB_Font.render("fying and spoopy with the",True,BLACK).convert_alpha()
		screen.blit(usmanDescription, (175,679))
		usmanDescription=pokeGB_Font.render("beast!!",True,BLACK).convert_alpha()
		screen.blit(usmanDescription, (175,697))	

	elif tool == "textBlit":
		textBlitDescription=pokeGB_Font.render("Now that you have typed a",True,BLACK).convert_alpha()
		screen.blit(textBlitDescription, (175,625))
		textBlitDescription=pokeGB_Font.render("word in, use the mouse ",True,BLACK).convert_alpha()
		screen.blit(textBlitDescription, (175,643))
		textBlitDescription=pokeGB_Font.render("and click anywhere on the",True,BLACK).convert_alpha()
		screen.blit(textBlitDescription, (175,661))
		textBlitDescription=pokeGB_Font.render("screen to place what you ",True,BLACK).convert_alpha()
		screen.blit(textBlitDescription, (175,679))
		textBlitDescription=pokeGB_Font.render("typed in! Happy Typing!!!",True,BLACK).convert_alpha()
		screen.blit(textBlitDescription, (175,697))
		
	elif tool == '':
		Description=pokeGB_Font.render("There is no tool selected.",True,BLACK).convert_alpha()
		screen.blit(Description, (175,625))
		Description=pokeGB_Font.render("Please select a tool to ",True,BLACK).convert_alpha()
		screen.blit(Description, (175,643))
		Description=pokeGB_Font.render("start creating art!!",True,BLACK).convert_alpha()
		screen.blit(Description, (175,661))

	screen.blit(canvas, (150,100))# this will blit the canvas at the specified coordinates
	screen.set_clip(canvasRect)# Anything outside of the canvas will be cut off so that it remains within the canvas
	
	if tool != "saveTool" and tool != 'pencil' and tool != "filledRectTool" and tool != "filledEllipseTool" and tool != 'colour':
		draw.circle(screen, (100,100,100), (mx, my), thickness, 2)# the size circle will only show when the tools stated above are not selected
	draw.circle(screen, (100,100,100), (mx, my), 3)# this is the point of clicking
	
	screen.set_clip(None)

##                   Surface / Canvas Blit End               ##

##                   Draw Options Start               ##
	cmx, cmy = mx-150, my-100# this sets the canvas mouse position in accordance to where the canvas was drawn
	if mb[0] and tool=='eraser' and canvasRect.collidepoint((mx, my)): #Will only do the function in the if statement if the mouse is clicking on the canvas
		eraser(canvas, cmx, cmy, ocmx, ocmy,thickness)# This calls a function created in another file

	elif mb[0] and tool=='paint' and canvasRect.collidepoint((mx, my)):
		painter(canvas, cmx, cmy, ocmx, ocmy, thickness, col, randomCol)

	elif mb[0] and tool == "pencil" and canvasRect.collidepoint(mx,my):
 		pencil(canvas, col , ocmx, ocmy, cmx, cmy)		

	elif mb[0] and tool=="saveTool" and canvasRect.collidepoint(mx,my):
		try:
			types = [('Portable Network Graphics', 'png'),('JPEG', 'jpg')]# defines file types in a list
			fname = filedialog.asksaveasfilename(defaultextension='png', filetypes=types)# sets default extension and the different file types
			if fname != '':# this will save the canvas
				image.save(canvas, fname)
			tool="paint"# tool will be set to the paint tool
		except:
			print("saving error")# if there is an error ot will print this line and the tool will be set to the paint tool
			tool="paint"
			
	elif mb[0] and tool=="loadTool" and canvasRect.collidepoint(mx,my):
		try:
			types = [('Portable Network Graphics', 'png'), ("JPEG", "jpg")]# defines file types in a list
			fname = filedialog.askopenfilename(defaultextension='png',filetypes=types)# sets default extension and the different file types 
			if fname != "":# if the user picks something to load:
				img = image.load(fname)# the image will load
				canvas = transform.scale(img, (canvasRect.width, canvasRect.height))# the picture will be loaded to the size of the canvas
				control_Z.append(canvas.copy())# picture of canvas will be added to the control_Z list
				tool = 'paint'# tool set to paint
		except:
			print("Error")
			tool = 'paint'
	elif mb[0] and tool=='lineTool' and canvasRect.collidepoint((mx, my)):
		lineDrawTool(canvas, cmx, cmy, canvas_copy, sx, sy, col, thickness)# it calls a function from another file to perform a certain task
	elif mb[0] and tool=="ellipseTool" and canvasRect.collidepoint((mx, my)):
		ellipseDrawTool(canvas, cmx, cmy, mx, my, ocmx, ocmy, canvas_copy, sx, sy, col, thickness)

	elif mb[0] and tool=="filledEllipseTool" and canvasRect.collidepoint((mx, my)):
		filledEllipseDrawTool(canvas, cmx, cmy, canvas_copy, sx, sy, col)

	elif mb[0] and tool=="rectTool" and canvasRect.collidepoint((mx, my)):
		rectDrawTool(canvas, cmx, cmy, ocmx, ocmy, canvas_copy, sx, sy, col, thickness)	

	elif mb[0] and tool=="filledRectTool" and canvasRect.collidepoint((mx, my)):
		filledRectDrawTool(canvas, cmx, cmy, canvas_copy, sx, sy, col)

	elif mb[0] and tool=='chikoritaStamp' and canvasRect.collidepoint((mx, my)):
		chikorita = ChikoritaAnimation[0]#when the chikorita is put on the canvas it will print the stationary version of the animated version
		canvas.blit(canvas_copy, (0,0))#makes it so that chikorita can be dragged and can't draw it on screen before mouse button press was let go
		canvas.blit(transform.scale(chikorita, (thickness,thickness)), (cmx-thickness/2, cmy-thickness/2))#This will spawn Chikorita from the centre of that stamp
	
	elif mb[0] and tool=='bayleefStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy, (0,0))
		bayleef=BayleefAnimation[0]
		canvas.blit(transform.scale(bayleef, (thickness,thickness)), (cmx-thickness/2, cmy-thickness/2))

	elif mb[0] and tool=='meganiumStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy, (0,0))
		meganium=MeganiumAnimation[0]
		canvas.blit(transform.scale(meganium, (thickness,thickness)), (cmx-thickness/2, cmy-thickness/2))       

	elif mb[0] and tool=='MegaGengarStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy, (0,0))
		MegaGengar=MegaGengarAnimation[0]
		canvas.blit(transform.scale(MegaGengar, (thickness,thickness)), (cmx-thickness/2, cmy-thickness/2))
	
	elif mb[0] and tool=='gengarStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy, (0,0))
		gengar=GengarAnimation[0]
		canvas.blit(transform.scale(gengar, (thickness,thickness)), (cmx-thickness/2, cmy-thickness/2))

	elif mb[0] and tool=='haunterStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy, (0,0))
		haunter=HaunterAnimation[0]
		canvas.blit(transform.scale(haunter, (thickness,thickness)), (cmx-thickness/2, cmy-thickness/2))    
	
	elif mb[0] and tool=='gastlyStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy, (0,0))
		gastly=GastlyAnimation[0]
		canvas.blit(transform.scale(gastly, (thickness,thickness)), (cmx-thickness/2, cmy-thickness/2)) 

	elif mb[0] and tool=='infernapeStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy, (0,0))
		infernape=InfernapeAnimation[0]
		canvas.blit(transform.scale(infernape, (thickness,thickness)), (cmx-thickness/2, cmy-thickness/2))

	elif mb[0] and tool=='monfernoStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy, (0,0))
		monferno=MonfernoAnimation[0]
		canvas.blit(transform.scale(monferno, (thickness,thickness)), (cmx-thickness/2, cmy-thickness/2))   
	
	elif mb[0] and tool=='chimcharStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy,(0,0))
		Chimchar=ChimcharAnimation[0]
		canvas.blit(transform.scale(Chimchar, (thickness,thickness)), (cmx-thickness/2, cmy-thickness/2))

	elif mb[0] and tool=='MegaBlastoiseStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy,(0,0))
		MegaBlastoise=MegaBlastoiseAnimation[0]
		canvas.blit(transform.scale(MegaBlastoise, (thickness,thickness)), (cmx-thickness/2, cmy-thickness/2))

	elif mb[0] and tool=='BlastoiseStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy,(0,0))
		Blastoise=BlastoiseAnimation[0]
		canvas.blit(transform.scale(Blastoise, (thickness,thickness)), (cmx-thickness/2, cmy-thickness/2))

	elif mb[0] and tool=="WartortleStamp" and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy,(0,0))
		Wartortle=WartortleAnimation[0]
		canvas.blit(transform.scale(Wartortle, (thickness,thickness)), (cmx-thickness/2, cmy-thickness/2))

	elif mb[0] and tool=='SquirtleStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy,(0,0))
		Squirtle=SquirtleAnimation[0]
		canvas.blit(transform.scale(Squirtle ,(thickness, thickness)), (cmx-thickness/2, cmy-thickness/2))

	elif mb[0] and tool=='DarkraiStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy,(0,0))
		Darkrai=DarkraiAnimation[0]
		canvas.blit(transform.scale(Darkrai,(thickness, thickness)), (cmx-thickness/2.5, cmy-thickness/2))
	elif mb[0] and tool=='GiratinaStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy,(0,0))
		Giratina=GiratinaAnimation[0]
		canvas.blit(transform.scale(Giratina ,(thickness, thickness)), (cmx-thickness/2, cmy-thickness/2))

	elif mb[0] and tool=='PalkiaStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy,(0,0))
		Palkia=PalkiaAnimation[0]
		canvas.blit(transform.scale(Palkia ,(thickness, thickness)), (cmx-thickness/2, cmy-thickness/2))

	elif mb[0] and tool=='MewtwoStamp' and canvasRect.collidepoint((mx, my)):
		canvas.blit(canvas_copy,(0,0))
		Mewtwo=MewtwoAnimation[0]
		canvas.blit(transform.scale(Mewtwo ,(thickness, thickness)), (cmx-thickness/3, cmy-thickness/3))    

	elif mb[0] and tool=='SyedStamp':
		canvas.blit(canvas_copy, (0,0))
		canvas.blit(transform.scale(syed, (thickness,thickness)), (cmx-thickness/2, cmy-thickness/2))

	elif mb[0] and tool=='shahoonStamp':
		canvas.blit(canvas_copy, (0,0))
		canvas.blit(transform.scale(shahoon, (thickness,thickness)), (cmx-thickness/2, cmy-thickness/2))
	
	elif mb[0] and tool=='usmanStamp':
		canvas.blit(canvas_copy, (0,0))
		canvas.blit(transform.scale(usman, (thickness,thickness)), (cmx-thickness/2, cmy-thickness/2))			

	elif mb[0] and tool == 'textBlit':
		canvas.blit(canvas_copy, (0,0))# will make it so the user can drag the text around without blitting it multiple times
		if col != pcol: # if the colour selected before is not the same, the text colour will change to the new selected colour
			myText=timesNewRomanFont.render(text,True,col).convert_alpha()
			pcol = col
		canvas.blit(transform.scale(myText, (thickness,thickness)), (cmx-thickness/2, cmy-thickness/2))# this will blit the text on the screen

	elif mb[0] and tool == 'clear' and canvasRect.collidepoint(mx,my):
		canvas.fill(WHITE)# fills and clears the canvas

	elif mb[0] and tool == "colour":
		try:
			col = canvas.get_at((cmx,cmy))# captures any colour on the canvas
		except:
			pass	

	elif mb[0] and tool == "radiusChange":
		try:
			def ok(e, root):# defines what will happen when the ok function is called
				global radius # creates a global variable
				global thickness # creates a global variable
				user = e.get()# captures what the user typed in
				root.withdraw()
				root.destroy()# destroys root
				root.quit()# quits the root
				try:
					radius = user# radius = user input
					if int(radius) > 4000: # if the input is an integer and is more than 4000, thickness will remain the same as before the user made an input
						radius = int(thickness)
					elif int(radius) < 5:# if it is less than 5 then the thickness will also remain the same
						radius = int(thickness)	
					thickness = int(radius)# if the if and elif system has passed then the new thickness will be assigned
					tool = ''# tool will equal nothing
				except:
					pass	
			if OK ==False:
				root = Tk()
				e = Entry(root)# created an area 
				e.pack(padx=10,pady=10) # packs the area with the certain dimensions
				b=Button(root, text='OK', command=lambda:ok(e,root))# creates the ok button which calls upon the ok function
				b.pack(padx=10,pady=10)
				root.mainloop() # runs the root loop
			tool = ''# tool== nothing
		except:
			print("error")

	elif mb[0] and tool == "textTool" and canvasRect.collidepoint(mx,my):	
		try:
			def ok(e, root):
				global text# global variable
				user = e.get()
				root.withdraw()
				root.destroy()
				root.quit()
				text = user# text will equal user
				OK = True# will make it so that it won't run the code that has run already after the function
				tool="textBlit"# tool = textBlit which allows the user to blit the text on to the canvas
			if OK ==False:
				root = Tk()
				e = Entry(root)
				e.pack(padx=10,pady=10)
				b=Button(root, text='OK', command=lambda:ok(e,root))
				b.pack(padx=10,pady=10)
				root.mainloop()
			timesNewRomanFont=font.SysFont("Times New Roman", 1000)# creates and defines the font with a certain font size
			pcol = col # a previous colour variable will equal the colour when the text was rendered in the first place
			myText=timesNewRomanFont.render(text,True,col).convert_alpha()# renders the text
			tool="textBlit"# tool = textBlit
			# Sometimes the tool will not change so I had to add it twice to make sure that innonw of those steps it changes
		except:
			print("error")	# if an error is made then the program will print error
	myClock.tick(60)# sets the framerate to 60fps
	display.flip()# blits everything on to the screen
	ocmx, ocmy = cmx, cmy #old canvas mouse position will equal the current canvas mouse position
##                   Draw Options End                   ##
quit() # closes out pygame window