# Escape - A python Adventure
# by Sean McManus / www.sean.co.uk
# This version by me

import time, random, math

###############
## VARIABLES ##
###############

WIDTH = 800
HEIGHT = 800

STARTING_ROOM = 32

#PLAYER variables
PLAYER_NAME = "Cloud"
FRIEND1_NAME = "Tifa"
FRIEND2_NAME = "Erith"
current_room = STARTING_ROOM

top_left_x = 100
top_left_y = 150

DEMO_OBJECTS = [images.floor, images.pillar, images.soil]

#############
##   MAP   ##
#############

MAP_WIDTH  = 5
MAP_HEIGHT = 10
MAP_SIZE = MAP_WIDTH * MAP_HEIGHT

GAME_MAP = [["Room 0 - where unused objects are kept", 0, 0, False, True]]

outdoor_rooms = range(1, 26)
for planetsectors in range(1, 26): #Rooms 1 to 25 are generated here
    GAME_MAP.append(["The dusty planet surface", 13, 13, True, True])

GAME_MAP += [
    #["Room Name", height, width, Top exit?, Bottom exit?]
]