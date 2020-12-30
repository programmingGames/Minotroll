import pygame
from data.gameplay.enimy.wizard import Wizard

class ControlEnimys(object):
    def __init__(self, screen):
        self.screen = screen
        self.wizard = Wizard(self.screen)

    def enimysAdd(self, tile_rects, player_rect, scroll):
        enimy_rect, enimy_type = self.wizard.addingWizard(tile_rects, player_rect, scroll)
        
        return (enimy_rect, enimy_type)