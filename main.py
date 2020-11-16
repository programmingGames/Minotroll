# from data.start import Name as nm
from data.backgrounds import Backgound as Back
from data.mainMenu import MainMenu as mainMenu
import pygame 
from sys import exit
from pygame.locals import *


screen = pygame.display.set_mode((700, 480), 0, 32)
MainmenuControl = 150
a = "Minotroll"
menu = mainMenu(screen, 2)
pygame.display.set_caption(a)

while True:
    # pygame.event.wait()
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    menu.startingMenu(screen)
    pressed_keys = pygame.key.get_pressed()
    MainmenuControl = menu.movingInMainMenu(screen, pressed_keys, MainmenuControl)
    pygame.display.update()
