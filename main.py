from data.start import Name as nm
import pygame 
from sys import exit
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)


#fr,ep,


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        
    pygame.display.update()
