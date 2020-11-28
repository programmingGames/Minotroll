from data.start import Initiation as start
from data.mainMenu import MainMenu as mainMenu
from data.createUser import CreateUser as createUser
from data.intro import Intro
from data.plataforma import Plataform
from data.player import Player
from data.enimy.wizard import Wizard
import pygame 
from sys import exit
from pygame.locals import *

screen = pygame.display.set_mode((700, 480), 0, 32)
pygame.display.set_caption("Minotroll")

# Variable to control the player rect
player_rect = 0
# variable to control the main menu
MainmenuControl = 150
# Variable to store all the pygameEvent
pygameEvent = 0
# Variable to control the screen page of the game
menuEsc = 4
# Variable to control the nivel
nivel = 1

# Variable to control the scroll of the screen
scroll = [0, 0]

initiation = start(screen, 1, menuEsc, nivel)
menu = mainMenu(screen, 2, menuEsc, nivel)
user = createUser(screen, 2, menuEsc, nivel)
player = Player(screen)
wizard = Wizard(screen)
intro = Intro(screen, 2, menuEsc, nivel)
plataforma = 0

## teste 
wizard = Wizard(screen)


clock = pygame.time.Clock()

while True:

    # pygame.event.wait()
    for event in pygame.event.get():
        pygameEvent = event
        if event.type == QUIT:
            exit()

    pressed_keys = pygame.key.get_pressed()

    if(pressed_keys[K_ESCAPE]):
        menuEsc = 1

    if(menuEsc==0):
        menuEsc = initiation.settingStart(pressed_keys)
    elif(menuEsc==1):
        menu.startingMenu(screen)
        MainmenuControl, menuEsc = menu.movingInMainMenu(screen, pressed_keys, MainmenuControl, menuEsc)
    elif(menuEsc==2):
        menuEsc = user.settingUserMenu(pygameEvent, pressed_keys, menuEsc)
    elif(menuEsc==3):
        menuEsc = intro.introDisplay()
    elif(menuEsc == 4):
        plataforma = Plataform(screen, 1, menuEsc, nivel)
        tile_rects = plataforma.settingPlataform(scroll)
        #scroll, player_rect = player.settingPlayer(pygameEvent, tile_rects, scroll)
        wizard.move(pygameEvent, tile_rects)
    pressed_keys = pygame.key.get_pressed()
    pygame.display.update()