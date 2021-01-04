import pygame
from data.gameplay.enimy.cactus import Cactus
from data.gameplay.enimy.wizard import Wizard
from data.gameplay.enimy.golens import Golens

class ControlEnimys(object):
    def __init__(self, screen):
        self.screen = screen
        self.allWizards = []
        self.allEnimys = []
        self.allCactus = []
        self.addingAllTheAnimys()
        # test
        
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
        # [self.allEnimys.append(wizard.addingWizard(tile_rects, player_rect, scroll)) for wizard in self.allWizards]
        # [self.allEnimys.append(cactus.addCactus(tile_rects, scroll)) for cactus in self.allCactus]

        return self.allEnimys
    def addingAllTheAnimys(self):
        pass
        # self.allWizards.append(Wizard(self.screen, 160, 1520))
        # self.allWizards.append(Wizard(self.screen, 100, 1490))
        # self.allCactus.append(Cactus(self.screen, 916))
        # self.allCactus.append(Cactus(self.screen, 948))
        # self.allCactus.append(Cactus(self.screen, 976))
        # self.allCactus.append(Cactus(self.screen, 1986))
        # self.allCactus.append(Cactus(self.screen, 2278))
        # self.allCactus.append(Cactus(self.screen, 2310))
        # self.allCactus.append(Cactus(self.screen, 2338))
        # self.allCactus.append(Cactus(self.screen, 2362))
        # self.allCactus.append(Cactus(self.screen, 2386))
        # self.allCactus.append(Cactus(self.screen, 2402))
        # self.allCactus.append(Cactus(self.screen, 3696))
        # self.allCactus.append(Cactus(self.screen, 3724))
        # self.allCactus.append(Cactus(self.screen, 3748))
        # self.allCactus.append(Cactus(self.screen, 3764))
        # self.allCactus.append(Cactus(self.screen, 3788))
        # self.allCactus.append(Cactus(self.screen, 4514))
        # self.allCactus.append(Cactus(self.screen, 4494))
        # self.allCactus.append(Cactus(self.screen, 4474))
        # self.allCactus.append(Cactus(self.screen, 4454))
        # self.allCactus.append(Cactus(self.screen, 5010))
        # self.allCactus.append(Cactus(self.screen, 5048))
        # self.allCactus.append(Cactus(self.screen, 5078))
        # self.allCactus.append(Cactus(self.screen, 5102))
        # self.allCactus.append(Cactus(self.screen, 5130))
        # self.allCactus.append(Cactus(self.screen, 5158))
        # self.allCactus.append(Cactus(self.screen, 5178))
        # self.allCactus.append(Cactus(self.screen, 5200))
