# from data.start import Name as nm
from data.backgrounds import Backgound as Back
from data.mainMenu import MainMenu as mainMenu
import pygame 
from sys import exit
from pygame.locals import *


screen = pygame.display.set_mode((740, 500), 0, 32)

a = "Minotroll"
menu = mainMenu(screen, 2)
pygame.display.set_caption(a)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    menu.startingMenu()
    pygame.display.update()
