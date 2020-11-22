import pygame 
from pygame.locals import * 
from data.backgrounds import Backgound as Back

class Initiation:
    def __init__(self, screen, nrImage, menuEsc, nivel):
        self.screen = screen
        self.background = Back(nrImage, menuEsc, nivel)
        self.esc = 0

    # Method to blit the start game font on the screen
    def settingStart(self, pressed_keys):
        self.background.settingBackground(self.screen)
        if(pressed_keys[K_KP_ENTER]):
            pygame.time.delay(100)
            self.esc = 1
        return self.esc