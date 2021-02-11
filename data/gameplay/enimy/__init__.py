# from os import POSIX_FADV_DONTNEED
import pygame
from pygame import rect
from data.gameplay.enimy.cactus import Cactus
from data.gameplay.enimy.wizard import Wizard
from data.gameplay.enimy.golens import Golens
from data.gameplay.enimy.minotauro import Minotauro
from data.gameplay.enimy.graveler import Graveller
from data.gameplay.collisionControl import Colision

# Class to control all the enimys collision and their life's
class ControlEnimys(object):
    def __init__(self, screen, nivel, enimysKilled):
        self.screen = screen
        self.nivel = nivel
        self.enimyskilled = enimysKilled
        self.collision = Colision()
        self.allEnimys = []
        self.allEnimysPosition = []
        self.allCactus = []
        self.allCactusPosition = []
        self.enimyKilled = 0
        self.bossKilled = False
        self.count = 0
        self.addingAllTheAnimys()

    # Method that add all enimys on the screen
    def enimysAdd(self, tile_rects, player_rect,fireCollision,playerAttack,scroll):
        self.allEnimys_rects = []
        allCactus_rects = []        

        # drawing the enimys on the screen
        if(len(self.allEnimysPosition)!=0):
            for (pos, enimy) in zip(self.allEnimysPosition, self.allEnimys):
                if(pos[0] in range(scroll[0]-450, scroll[0]+650)):
                    self.allEnimys_rects.append(enimy.add(tile_rects,player_rect,(playerAttack[0], playerAttack[1]), scroll))
                    self.count += 1
        # drawing the cactus on the screen
        if(len(self.allCactusPosition)!=0):
            for (pos, cactus) in zip(self.allCactusPosition, self.allCactus):
                if(pos[0] in range(scroll[0]-450, scroll[0]+650)):
                    allCactus_rects.append(cactus.add(tile_rects, scroll))
                    self.count += 1
        self.calculatingEnimyDelete(fireCollision[0],playerAttack, scroll)
        self.allEnimys_rects += [cactus for cactus in allCactus_rects]
        return self.allEnimys_rects, self.enimyKilled, self.bossKilled
    
    # Method that define the number, and what type of enimys can be found in the leve's
    def addingAllTheAnimys(self):
        if(self.nivel == 0):          
            self.allCactusPosition = [(928, 184),(964, 184),(2370, 504),(2410, 504),(2450, 504),(2478, 504),(3778, 472),(3746, 472),
            (3706, 472),(4458, 408),(4490, 408),(4514, 408),(5030, 520),(5070, 520),(5106, 520),(5138, 520),(5162, 520),(5194, 520)]
            self.allCactus = [(Cactus(self.screen, pos)) for pos in self.allCactusPosition] 
            self.allEnimys.append(Wizard(self.screen,(1388,168), 100, 6))
            self.allEnimys.append(Wizard(self.screen,(1500,168), 100, 6))
            self.allEnimys.append(Wizard(self.screen,(1596,168), 100, 6))
            self.allEnimys.append(Wizard(self.screen,(2086,328), 100, 6))
            self.allEnimys.append(Golens(self.screen,(2630,408), 50,1, 5))
            self.allEnimys.append(Golens(self.screen,(2794,408), 50, 1, 5))
            self.allEnimys.append(Wizard(self.screen,(2674,296), 100, 5))
            self.allEnimys.append(Wizard(self.screen,(2806,296), 100, 6))
            self.allEnimys.append(Golens(self.screen,(3938,296), 50, 1, 5))
            self.allEnimys.append(Golens(self.screen,(4022,296), 50, 1, 5))
            self.allEnimys.append(Golens(self.screen,(4114,296), 50, 1, 5))
            self.allEnimys.append(Wizard(self.screen,(4376,520), 100, 6))
            self.allEnimys.append(Golens(self.screen,(4672,584), 50,1, 5))
            self.allEnimys.append(Golens(self.screen,(4764,584), 50, 1, 6))
            self.allEnimys.append(Golens(self.screen,(4836,584), 50, 1, 6))
            self.allEnimys.append(Golens(self.screen,(4908,584), 50, 1, 5))
            self.allEnimysPosition = [(1388,168),(1500,168),(1596,168),(2086,328),(2630,408),(2794,408),(2674,296),(2806,296)
                    ,(3938,296),(4022,296),(4114,296),(4376,520),(4672,584),(4764,584),(4836,584),(4908,584)]
                                
        elif (self.nivel == 1):
            self.allCactusPosition = [(1578, 424), (1088, 648), (2240, 344), (2288, 360), (2340, 376), (2986, 408), (3650, 136)]
            self.allCactus = [(Cactus(self.screen, pos)) for pos in self.allCactusPosition] 
            self.allEnimys.append(Wizard(self.screen,(1220,184), 100, 6))
            self.allEnimys.append(Wizard(self.screen,(1296,184), 100, 6))
            self.allEnimys.append(Wizard(self.screen,(1408,184), 100, 6))
            self.allEnimys.append(Wizard(self.screen,(1244,360), 100, 6))
            self.allEnimys.append(Golens(self.screen,(1364,360), 50, 2, 8))
            self.allEnimys.append(Wizard(self.screen,(1746,616), 100, 7))
            self.allEnimys.append(Golens(self.screen,(1994,616), 50, 2, 7))
            self.allEnimys.append(Wizard(self.screen,(2106,616), 100, 9))
            self.allEnimys.append(Golens(self.screen,(2669,616), 50, 2, 9))
            self.allEnimys.append(Golens(self.screen,(2757,616), 50, 2, 7))
            self.allEnimys.append(Golens(self.screen,(2869,616), 50, 2, 7))
            self.allEnimys.append(Wizard(self.screen,(3270,184), 100, 6))
            self.allEnimys.append(Wizard(self.screen,(3354,184), 100, 6))
            self.allEnimys.append(Wizard(self.screen,(3422,184), 100, 6))
            self.allEnimys.append(Wizard(self.screen,(3502,184), 100, 6))
            self.allEnimys.append(Wizard(self.screen,(4113,184), 100, 6))
            self.allEnimys.append(Wizard(self.screen,(4229,184), 100, 6))
            self.allEnimys.append(Golens(self.screen,(4701,104), 50, 2, 5))
            self.allEnimys.append(Golens(self.screen,(4801,104), 50, 2, 6))
            self.allEnimys.append(Golens(self.screen,(4861,104), 50, 2, 7))
            self.allEnimys.append(Golens(self.screen,(4893,104), 50, 2, 3))

            self.allEnimysPosition = [(1220,184),(1296,184),(1408,184),(1244,360),(1364,360),(1746,616),(1994,616),(2106,616),(2669,616),
            (2757,616),(2869,616),(3270,184),(3354,184),(3422,184),(3502,184),(4113,184),(4229,184),(4701,104),(4801,104),(4861,104),(4893,104),]

        elif (self.nivel == 2):
            self.allEnimys.append(Golens(self.screen,(852,530), 50, 3,7))
            self.allEnimys.append(Golens(self.screen,(928,530), 50, 3,7))
            self.allEnimys.append(Golens(self.screen,(988,530), 50, 3,7))
            self.allEnimys.append(Golens(self.screen,(1036,530), 50, 3,7))
            self.allEnimys.append(Golens(self.screen,(1096,530), 50, 3,7))
            self.allEnimys.append(Golens(self.screen,(1136,530), 50, 3,7))
            self.allEnimys.append(Golens(self.screen,(1184,530), 50, 3,7))
            self.allEnimys.append(Golens(self.screen,(1264,530), 50, 3,6))
            self.allEnimys.append(Golens(self.screen,(1862,350), 50, 3,4))
            self.allEnimys.append(Golens(self.screen,(3508,110), 50, 3,5))
            self.allEnimys.append(Golens(self.screen,(3596,110), 50, 3,7))
            self.allEnimys.append(Golens(self.screen,(3648,110), 50, 3,7))
            self.allEnimys.append(Golens(self.screen,(3724,110), 50, 3,5))
            self.allEnimys.append(Golens(self.screen,(3824,110), 50, 3,6))
            self.allEnimys.append(Minotauro(self.screen,(3916,110), 50, 8))
            self.allEnimys.append(Minotauro(self.screen,(5108,560), 50, 9))
            self.allEnimys.append(Minotauro(self.screen,(5304,560), 50, 6))
            self.allEnimys.append(Minotauro(self.screen,(5310,560), 50, 6))

            self.allEnimysPosition = [(852,530),(928,530),(988,530),(1036,530),(1096,530),(1136,530),(1184,530),(1264,530),(1862,350),
                        (3508,110),(3596,110),(3648,110),(3724,110),(3824,110),(3916,110),(5108,560),(5304,560),(5360,560)]            

        elif (self.nivel == 3):
            self.allCactusPosition = [(716, 232), (756, 232), (788, 232), (828, 232), (942, 232), (982, 232), (1010, 232), (1046, 232)
                        ,(1170, 232), (1194, 232), (1218, 232), (1238, 232), (1266, 232), (1394, 232), (1414, 232), (1438, 232), (1466, 232)
                        , (1494, 232), (1882, 232), (1906, 232), (1934, 232)]
            self.allCactus = [(Cactus(self.screen, pos)) for pos in self.allCactusPosition]            

            self.allEnimys.append(Wizard(self.screen,(2008,536), 100, 7))
            self.allEnimys.append(Wizard(self.screen,(2720,280), 100, 7))
            self.allEnimys.append(Wizard(self.screen,(2720,280), 100, 8))
            self.allEnimys.append(Wizard(self.screen,(2720,280), 100, 8))
            self.allEnimys.append(Graveller(self.screen, (3603, 120), 250, 20))
            self.allEnimysPosition = [(2008,536), (2720,280), (2720,280), (2720,280), (3603, 120)]
        if len(self.allEnimys) and len(self.allEnimysPosition):
            [self.allEnimys.pop(0) for i in range(self.enimyskilled)]
            [self.allEnimysPosition.pop(0) for i in range(self.enimyskilled)]

    # Method that control what is the enimys that the player is attacking and control the damage cause
    def calculatingEnimyDelete(self,fireColid,playerAttack, scroll):
        i = 0
        for (position, enimy) in zip(self.allEnimysPosition, self.allEnimys):
            if(position[0] in range(scroll[0]-450, scroll[0]+650)):
                # print(playerAttack[3])
                if (fireColid or (playerAttack[0] and playerAttack[1] and playerAttack[3]==i)):
                    if((enimy.life < 0)and(self.count >= 20)):
                        self.allEnimys.pop(i)
                        self.allEnimysPosition.pop(i)
                        self.enimyKilled += 1
                        # self.allEnimys_rects.pop(i)
                        self.count = 0
                    else:
                        if(playerAttack[2] == "greenfire"):
                            enimy.sufferingDamage(1)    
                        elif(playerAttack[2] == "bluefire"):
                            enimy.sufferingDamage(1.5)
                        elif(playerAttack[2] == "slashing"):
                            enimy.sufferingDamage(0.9)
                        elif(playerAttack[2] == "kicking"):
                            enimy.sufferingDamage(0.2)
                        elif(playerAttack[2] == "battleax"):
                            enimy.sufferingDamage(0.8)
                
            elif(position[0] < scroll[0]-450):
                self.allEnimys.pop(i)
                self.allEnimysPosition.pop(i)
            if self.nivel == 3 and position[0] < scroll[0]-350:
                self.allEnimys.pop(i)
                self.allEnimysPosition.pop(i)
            i += 1
        self.count += 1
        if((self.nivel == 3)and(len(self.allEnimysPosition)==0)):
            self.bossKilled = True
