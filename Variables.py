# Variables.py
# import antigravity
# import this
# import pickle
from pygame import * # This will import all functions and actions of pygame
from random import *
from math import *
import os
from random import *
from tkinter.colorchooser import *
from tkinter import *
from tkinter import filedialog
font.init()# intializes font function
running = True # the program is running
size = (1366,768)# sets the size of the screen
RED = (255,0,0)# sets colour values
GREEN = (0,255,0)# sets colour values
BLUE = (0,0,255)# sets colour values
WHITE = (255,255,255)# sets colour values
BLACK = (0,0,0)# sets colour values
randomCol = 0# creates a toggle to check if the user has toggled the random colour switch
col=BLACK # initial colour is black and col is every colour that the user selects
text = '' # this is the text where the user text input is stored
myText = "" #This will store the text rendering
OK = False # checks if the OK button for text input has been clicked
secret = False # if the secret has been found then the variable will equal true
secret_c = 0 # a counter
pokeFont=font.Font("Fonts/Pokemon Solid.ttf", 25) # creates a font with a certain size
pokeGB_Font=font.Font("Fonts/Pokemon GB.ttf", 18) # creates a font with a certain size
hollowPokeFont=font.Font("Fonts/Pokemon Hollow.ttf", 25) # creates a font with a certain size

canvas = Surface((800,500))# creates a surface
canvas.fill(WHITE)# fills the canvas with white

myClock = time.Clock()# counts the time

mixer.pre_init(44100, -16, 1, 512)# initializes the music mixer before it is actually initialized
mixer.init()# initializes the music mixer

thickness = 10# the thickness/radius that is changeable
pokeSelect = 1 # Pokemon stamp selection page counter
tool = 'paint' # stores which tool is selected
subtool = 'randomCol' # this is the only thing that subTool will be

control_Z=[canvas.copy()]# for the undo array
control_Y=[] #for the redo array

ChikoritaAnimation = []# creates a list for pokemon animations
chikorita_counter = 0 # counts the frames for the animations
BayleefAnimation = []
bayleef_counter = 0
MeganiumAnimation = []
meganium_counter = 0
MegaGengarAnimation = []
MegaGengar_counter = 0
GengarAnimation = []
gengar_counter = 0
HaunterAnimation = []
haunter_counter = 0
GastlyAnimation = []
gastly_counter = 0
InfernapeAnimation = []
infernape_counter = 0
MonfernoAnimation = []
monferno_counter = 0
ChimcharAnimation = []
chimchar_counter = 0
MegaBlastoiseAnimation = []
MegaBlastoise_counter = 0
BlastoiseAnimation = []
Blastoise_counter = 0
WartortleAnimation = []
Wartortle_counter = 0
SquirtleAnimation = []
Squirtle_counter = 0
DarkraiAnimation = []
Darkrai_counter = 0
GiratinaAnimation = []
Giratina_counter = 0
PalkiaAnimation = []
Palkia_counter = 0
MewtwoAnimation = []
Mewtwo_counter = 0