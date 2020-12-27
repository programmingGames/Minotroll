import pygame
from pygame.locals import *
from data.gameplay.headUpDisplay.life import Life

class HeadUpDisplay(object):
    def __init__(self, screen):
        self.screen = screen
        self.life = Life(self.screen)
        # self.lifeBox = pygame.image.load("resources/image/headUpDisplay/lifebox1.png")

    # method to draw the HUD um the game screen
    def headUpDisplayScreenDraw(self):
        self.life.draw()
        # self.screen.blit(self.lifeBox, (50, 50))
        pass