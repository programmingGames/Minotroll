from data.start import Name as nm
import pygame 
from sys import exit
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((740, 500), 0, 32)

a = "Minotroll"
pygame.display.set_caption(a)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        
    pygame.display.update()
