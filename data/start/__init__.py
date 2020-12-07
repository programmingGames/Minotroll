import pygame 
from pygame.locals import * 
from data.backgrounds import Backgound as Back

class Initiation:
    def __init__(self, screen, nrImage,screenState, nivel):
        self.screen = screen
        self.screenState = screenState
        self.background = Back(nrImage, screenState, nivel)
        self.frame = 1

    # Method to blit the start game font on the screen
    def settingStart(self):
        pressed_keys = pygame.key.get_pressed()
        self.background.settingBackground(self.screen)
        if(self.frame == 50):
            return 1
        else:
            self.frame += 1
        return self.screenState