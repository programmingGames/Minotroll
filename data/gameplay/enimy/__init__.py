import pygame
from data.gameplay.enimy.cactus import Cactus
from data.gameplay.enimy.wizard import Wizard
from data.gameplay.enimy.golens import Golens

class ControlEnimys(object):
    def __init__(self, screen, nivel):
        self.screen = screen
        self.nivel = nivel
        self.allEnimys = []
        self.addingAllTheAnimys()


    def enimysAdd(self, tile_rects, player_rect, scroll):

        # Just for test

        #[self.allEnimys.append(golens.addingGolens(tile_rects,player_rect,scroll))for golens in self.allGolens]
        #[self.allEnimys.append(wizard.addingWizard(tile_rects, player_rect, scroll)) for wizard in self.allWizards]
        #[self.allEnimys.append(cactus.addCactus(tile_rects, scroll)) for cactus in self.allCactus]

 #       [self.allEnimys.append(golens.addingGolens(tile_rects,player_rect,scroll))for golens in self.allGolens]
        # [self.allEnimys.append(wizard.addingWizard(tile_rects, player_rect, scroll)) for wizard in self.allWizards]
#        [self.allEnimys.append(cactus.addCactus(tile_rects, scroll)) for cactus in self.allCactus]


        all_rects = []
        if(len(self.positions)!=0):
            for (pos, enimy) in zip(self.positions, self.allEnimys):
                if(pos[0] in range(scroll[0]-450, scroll[0]+650)):
                    all_rects.append(enimy.add(tile_rects,player_rect, scroll))


        return all_rects
    def addingAllTheAnimys(self):

        pass
        #self.allWizards.append(Wizard(self.screen, 160, 1520))
        #self.allWizards.append(Wizard(self.screen, 100, 1490))
       # self.allCactus.append(Cactus(self.screen, 916))
        #self.allCactus.append(Cactus(self.screen, 948))
        #self.allCactus.append(Cactus(self.screen, 976))
        #self.allCactus.append(Cactus(self.screen, 1986))
        #self.allCactus.append(Cactus(self.screen, 2278))
        #self.allCactus.append(Cactus(self.screen, 2310))
        #self.allCactus.append(Cactus(self.screen, 2338))
        #self.allCactus.append(Cactus(self.screen, 2362))
        #self.allCactus.append(Cactus(self.screen, 2386))
        #self.allCactus.append(Cactus(self.screen, 2402))
        #self.allCactus.append(Cactus(self.screen, 3696))
        #self.allCactus.append(Cactus(self.screen, 3724))
        #self.allCactus.append(Cactus(self.screen, 3748))
        #self.allCactus.append(Cactus(self.screen, 3764))
        #self.allCactus.append(Cactus(self.screen, 3788))
        #self.allCactus.append(Cactus(self.screen, 4514))
        #self.allCactus.append(Cactus(self.screen, 4494))
        #self.allCactus.append(Cactus(self.screen, 4474))
        #self.allCactus.append(Cactus(self.screen, 4454))
        #self.allCactus.append(Cactus(self.screen, 5010))
        #self.allCactus.append(Cactus(self.screen, 5048))
        #self.allCactus.append(Cactus(self.screen, 5078))
        #self.allCactus.append(Cactus(self.screen, 5102))
        #self.allCactus.append(Cactus(self.screen, 5130))
        #self.allCactus.append(Cactus(self.screen, 5158))
        #self.allCactus.append(Cactus(self.screen, 5178))
        #self.allCactus.append(Cactus(self.screen, 5200))


        # wizards = []
        # golems = []
        # cactus = []
        if(self.nivel == 0):
            self.allEnimys.append(Cactus(self.screen, (928, 184)))
            self.allEnimys.append(Cactus(self.screen, (964, 184)))
            self.allEnimys.append(Wizard(self.screen,(1448, 168), 100)) 
            self.allEnimys.append(Wizard(self.screen,(1595, 168), 100))
            self.allEnimys.append(Cactus(self.screen, (2370, 504)))
            self.allEnimys.append(Cactus(self.screen, (2410, 504)))
            self.allEnimys.append(Cactus(self.screen, (2450, 504)))
            self.allEnimys.append(Cactus(self.screen, (2478, 504)))
            self.allEnimys.append(Golens(self.screen, (2718, 408), 100))
            self.allEnimys.append(Wizard(self.screen,(2750, 296), 100))
            self.allEnimys.append(Cactus(self.screen, (3778, 472)))
            self.allEnimys.append(Cactus(self.screen, (3746, 472)))
            self.allEnimys.append(Cactus(self.screen, (3706, 472)))
            self.allEnimys.append(Golens(self.screen, (4014, 296), 100))
            self.allEnimys.append(Cactus(self.screen, (4458, 408)))
            self.allEnimys.append(Cactus(self.screen, (4490, 408)))
            self.allEnimys.append(Cactus(self.screen, (4514, 408)))
            self.allEnimys.append(Golens(self.screen, (4710, 584), 100))
            self.allEnimys.append(Golens(self.screen, (4870, 584), 100))
            self.allEnimys.append(Cactus(self.screen, (5030, 520)))
            self.allEnimys.append(Cactus(self.screen, (5070, 520)))
            self.allEnimys.append(Cactus(self.screen, (5106, 520)))
            self.allEnimys.append(Cactus(self.screen, (5138, 520)))
            self.allEnimys.append(Cactus(self.screen, (5162, 520)))
            self.allEnimys.append(Cactus(self.screen, (5194, 520)))

            
            self.positions = [(928, 184),(964, 184),(1448, 168),(1595, 168),(2370, 504),(2410, 504),(2450, 504),(2478, 504),(2718, 408)
            ,(2750, 296),(3778, 472),(3746, 472),(3706, 472),(4014, 296),(4458, 408),(4490, 408),(4514, 408),(4710, 584),(4870, 584)
            ,(5030, 520),(5070, 520),(5106, 520),(5138, 520),(5162, 520),(5194, 520)]

            # self.positions = [(1448, 168),(1595, 168),(2718, 408),(2750, 296),(4014, 296),(4710, 584), (4870, 584)] 
        

