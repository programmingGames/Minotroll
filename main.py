from data.start import Initiation as start
from data.mainMenu import MainMenu as mainMenu
from data.createUser import CreateUser as createUser
import pygame 
from sys import exit
from pygame.locals import *

screen = pygame.display.set_mode((700, 480), 0, 32)
pygame.display.set_caption("Minotroll")

# variable to control the main menu
MainmenuControl = 150
pygameEvent = 0
menuEsc = 0
menu = mainMenu(screen, 2)
user = createUser(screen, 2)

# initition = start(screen, 1)

clock = pygame.time.Clock()

while True:
    # pygame.event.wait()
    
    for event in pygame.event.get():
        pygameEvent = event
        if event.type == QUIT:
            pygame.quit()
            exit()

    pressed_keys = pygame.key.get_pressed()

    # if(menuEsc==0):
    #     menuEsc = initition.settingStart(pressed_keys)
    if(menuEsc==1):
        user.settingUserName(pygameEvent)
    else:
        menu.startingMenu(screen)
        MainmenuControl, menuEsc = menu.movingInMainMenu(screen, pressed_keys, MainmenuControl)
        
    pygame.display.update()
    clock.tick(30)