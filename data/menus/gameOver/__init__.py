import pygame
from pygame.locals import *


class GameOver(object):
    def __init__(self, screen):
        self.screen = screen
        self.back = pygame.image.load("resources/image/menu/gamOver/back.png").convert_alpha()


    def showGameOverPainel(self):
        self.screen.blit(self.back, (0, 0))