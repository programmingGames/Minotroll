import pygame
import random
from data.menus import Menus

menu = Menus()
clock = pygame.time.Clock()

while True:
    menu.interMenuMoving()
    pygame.display.update()
    clock.tick(30)


    