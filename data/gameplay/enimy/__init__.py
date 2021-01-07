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
        # if(len(self.positions)!=0):
        #     for (pos, enimy) in zip(self.positions, self.allEnimys):
        #         if(pos[0] in range(scroll[0]-250, scroll[0]+750)):
        #             all_rects.append(enimy.add(tile_rects,player_rect, scroll))

        return all_rects
    def addingAllTheAnimys(self):
        # wizards = []
        # golems = []
        # cactus = []
        if(self.nivel == 0):
            self.allEnimys.append(Wizard(self.screen,(1448, 168), 100)) 
            self.allEnimys.append(Wizard(self.screen,(1595, 168), 100))
            self.allEnimys.append(Golens(self.screen, (2718, 408), 100))
            self.allEnimys.append(Wizard(self.screen,(2750, 296), 100))
            self.allEnimys.append(Golens(self.screen, (4014, 296), 100))
            self.allEnimys.append(Golens(self.screen, (4710, 584), 100))
            self.allEnimys.append(Golens(self.screen, (4870, 584), 100))
            self.positions = [(1448, 168),(1595, 168),(2718, 408),(2750, 296),(4014, 296),(4710, 584), (4870, 584)] 
        
