from data.start import Initiation as start
from data.mainMenu import MainMenu as mainMenu
from data.createUser import CreateUser as createUser
from data.intro import Intro
from data.plataforma import Plataform
import pygame 
from sys import exit
from pygame.locals import *

screen = pygame.display.set_mode((700, 480), 0, 32)
pygame.display.set_caption("Minotroll")

# variable to control the main menu
MainmenuControl = 150
# variable to control the create User menu
createUserMenuControl = 250
# Variable to store all the pygameEvent
pygameEvent = 0
# Variable to control the screen page of the game
menuEsc = 0

initition = start(screen, 1)
menu = mainMenu(screen, 2)
user = createUser(screen, 2)
intro = Intro(screen, 2)
plataforma = Plataform(screen)


clock = pygame.time.Clock()

while True:

    # pygame.event.wait()
    clock.tick(30)
    for event in pygame.event.get():
        pygameEvent = event
        if event.type == QUIT:
            pygame.quit()
            exit()

    pressed_keys = pygame.key.get_pressed()

    if(pressed_keys[K_ESCAPE]):
        exit()

    if(menuEsc==0):
        menuEsc = initition.settingStart(pressed_keys)
    elif(menuEsc==1):
        menu.startingMenu(screen)
        MainmenuControl, menuEsc = menu.movingInMainMenu(screen, pressed_keys, MainmenuControl, menuEsc)
    elif(menuEsc==2):
        createUserMenuControl, menuEsc = user.settingUserMenu(pygameEvent, pressed_keys, menuEsc, createUserMenuControl)
    elif(menuEsc==3):
        menuEsc = intro.introDisplay()
    elif(menuEsc == 4):
        plataforma.settingPlataform()

    pygame.display.update()