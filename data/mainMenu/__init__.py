import pygame
from data.backgrounds import Backgound as Back

class MainMenu(object):
    def __init__(self, screen, backgroundImage):
        self.screen = screen
        self.background = Back(backgroundImage)
    def startingMenu(self):
        self.background.settingBackground(self.screen)

    pass