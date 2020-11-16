import pygame
from pygame.locals import *
from data.backgrounds import Backgound as Back

class CreateUser:
    def __init__(self, screen, nrImage):
        self.screen = screen
        self.background = Back(nrImage)
    def settingUserName(self):
        self.background.settingBackground(self.screen)