from data.menus import Menus
import pygame

menu = Menus()
clock = pygame.time.Clock()

while True:
    menu.interMenuMoving()
    pygame.display.update()
    clock.tick(60)