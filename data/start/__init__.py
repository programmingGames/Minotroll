import pygame 
from pygame.locals import * 

class Initiation:
    def __init__(self, screen, nrImage):
        self.screen = screen
        self.background = pygame.Surface(screen.get_size())
        self.background = self.background.convert()
    def settingStart(self, pressed_keys):
        self.background.fill((0, 0, 0))
        self.screen.blit(self.background, (0, 0))
        if(pressed_keys[K_KP_ENTER]):
            return 1