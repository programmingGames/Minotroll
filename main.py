from data.start import Initiation as start
from data.menus import Menus
from data.plataforma import Plataform
from data.player import Player
from data.enimy.wizard import WizardSimpleAI
import pygame 
from sys import exit
from pygame.locals import *

screen = pygame.display.set_mode((700, 480), 0, 32)
pygame.display.set_caption("Minotroll")


# Variable to control the screen page of the game
screenState = int(0)
# Variable to control the nivel
nivel = 1
# To control the player rects
player_rect = pygame.Rect(0, 0, 0, 0)

# Variable to control the scroll of the screen
scroll = [0, 0]

pygameEvent = 0

initiation = start(screen, 1, screenState, nivel)
menu = Menus(screen, 2, screenState, nivel)
player = Player(screen)
wizard = WizardSimpleAI(screen)
plataforma = 0




clock = pygame.time.Clock()

while True:
    # pygame.event.wait()
    for event in pygame.event.get():
        pygameEvent = event
        if event.type == QUIT:
            exit()
    pressed_keys = pygame.key.get_pressed()

    if(pressed_keys[K_ESCAPE]):
        screenState = 1

    if(screenState==0):
        screenState = initiation.settingStart()
    elif((screenState>=1)and(screenState<=6)):
        screenState = menu.interMenuMoving(screenState, pygameEvent)
    elif(screenState == 7):
        plataforma = Plataform(screen, 1, screenState, nivel)
        tile_rects, tile_item = plataforma.settingPlataform(scroll)
        # wizard_rect = wizard.activation(pygameEvent, tile_rects, scroll, player_rect)
        # tile_rects.append(wizard_rect)
        scroll, player_rect = player.settingPlayer(pygameEvent, tile_rects,tile_item, scroll)
        tile_rects.append(player_rect)
    pygame.display.update()
    clock.tick(60)