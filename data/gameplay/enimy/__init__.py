from data.gameplay.enimy import golens
from data.gameplay.enimy.golens import Golens
import pygame
from data.gameplay.enimy.wizard import Wizard
from data.gameplay.enimy.golens import Golens

class ControlEnimys(object):
    def __init__(self, screen):
        self.screen = screen
        self.allWizards = []
        self.allEnimys = []
        self.allGolens = []

        # test
        #self.allWizards.append(Wizard(self.screen, 100, 600))
        self.allGolens.append(Golens(self.screen,100,600))
        # self.allWizards.append(Wizard(self.screen, 200, 1500))
        # self.allWizards.append(Wizard(self.screen,100, 1200))
        # self.allWizards.append(Wizard(self.screen,100, 1100))
        # self.allWizards.append(Wizard(self.screen,100, 1300))
        # self.allWizards.append(Wizard(self.screen,300, 1350))
        # self.allWizards.append(Wizard(self.screen,100, 1450))
        # self.allWizards.append(Wizard(self.screen,200, 1450))

    def enimysAdd(self, tile_rects, player_rect, scroll):
        # Just for test
        [self.allEnimys.append(golens.addingGolens(tile_rects,player_rect,scroll))for golens in self.allGolens]
        #[self.allEnimys.append(wizard.addingWizard(tile_rects, player_rect, scroll)) for wizard in self.allWizards]

        return self.allEnimys