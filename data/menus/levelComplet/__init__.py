import pygame
from pygame.locals import *


class LevelComplet(object):
    def __init__(self, screen):
        self.screen = screen
        self.back = pygame.image.load("resources/image/menu/levelComplet/back.png").convert_alpha()



    def drawingLevelCompletPainel(self):
        self.screen.blit(self.back, (0, 0))
        return 13, True