# Colours.py
# import antigravity
#import this
#import pickle
from pygame import * # This will import all functions and actions of pygame
from random import *
from math import *

rainbowCol=0
rainbowNum=1000

running = True

size=(1366,768)

RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
BLACK=(0,0,0)

randomCol=0
col=BLACK

thickness=10
thicknessY = 10

mixer.pre_init(44100, -16, 1, 512)
mixer.init()

tool='paint'

canvas = Surface((800,500))
canvas.fill(WHITE)

myClock = time.Clock()
thickness=10

control_Z=[canvas.copy()]
control_Y=[]

ChikoritaAnimation = []
chikorita_counter = 0

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
Squirtle_Counter = 0