import pygame
from data.gameplay.enimy.wizard import Wizard
from data.gameplay.enimy.cactus import Cactus

class ControlEnimys(object):
    def __init__(self, screen):
        self.screen = screen
        self.allWizards = []
        self.allCactus = []
        self.allEnimys = []

        # test
        self.allWizards.append(Wizard(self.screen, 160, 1520))
        self.allWizards.append(Wizard(self.screen, 100, 1490))
        self.allCactus.append(Cactus(self.screen, 600))
        # self.allWizards.append(Wizard(self.screen, 200, 1500))
        # self.allWizards.append(Wizard(self.screen,100, 1200))
        # self.allWizards.append(Wizard(self.screen,100, 1100))
        # self.allWizards.append(Wizard(self.screen,100, 1300))
        # self.allWizards.append(Wizard(self.screen,300, 1350))
        # self.allWizards.append(Wizard(self.screen,100, 1450))
        # self.allWizards.append(Wizard(self.screen,200, 1450))

    def enimysAdd(self, tile_rects, player_rect, scroll):
        # Just for test
        [self.allEnimys.append(wizard.addingWizard(tile_rects, player_rect, scroll)) for wizard in self.allWizards]
        [self.allEnimys.append(cactus.addCactus(tile_rects, scroll)) for cactus in self.allCactus]

        return self.allEnimys