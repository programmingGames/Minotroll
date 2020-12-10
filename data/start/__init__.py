import pygame 
from pygame.locals import * 
from data.backgrounds import Backgound as Back

class Initiation:
    def __init__(self, screen):
        self.screen = screen
        self.background = Back(screen)
        self.frame = 1

    # Method to blit the start game font on the screen
    def settingStart(self):
        self.background.settingBackgroundMenu(1)
        if(self.frame == 50):
            return 1
        else:
            self.frame += 1
        return 0