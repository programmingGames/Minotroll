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
        all_rects = []
        if(len(self.positions)!=0):
            for (pos, enimy) in zip(self.positions, self.allEnimys):
                if(pos[0] in range(scroll[0]-450, scroll[0]+650)):
                    all_rects.append(enimy.add(tile_rects,player_rect, scroll))

        return all_rects
    def addingAllTheAnimys(self):
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
        elif (self.nivel == 1):
            self.positions = []
        elif (self.nivel == 2):
            self.positions = []
        elif (self.nivel == 3):
            self.positions = []
            # self.positions = [(1448, 168),(1595, 168),(2718, 408),(2750, 296),(4014, 296),(4710, 584), (4870, 584)] 
        
