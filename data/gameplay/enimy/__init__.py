import pygame
from pygame import rect
from data.gameplay.enimy.cactus import Cactus
from data.gameplay.enimy.wizard import Wizard
from data.gameplay.enimy.golens import Golens
from data.gameplay.collisionControl import Colision

class ControlEnimys(object):
    def __init__(self, screen, nivel):
        self.screen = screen
        self.nivel = nivel
        self.collision = Colision()
        self.allEnimys = []
        self.killAttempt = []
        self.count = 0
        self.addingAllTheAnimys()

    def enimysAdd(self, tile_rects, player_rect,fireCollision, scroll):
        all_rects = []
        self.count = 0
        fireColid = False
        enimyFiredPos = 0
        
        if fireCollision[0]:
            fireColid = True
            enimyFiredPos = fireCollision[1]
            # del all_rects[fireCollision[1]]
        else:
            fireColid = False
        self.calculatingEnimyDelete(fireColid,enimyFiredPos, scroll)

        if(len(self.positions)!=0):
            for (pos, enimy) in zip(self.positions, self.allEnimys):
                if(pos[0] in range(scroll[0]-450, scroll[0]+650)):
                    all_rects.append(enimy.add(tile_rects,player_rect, scroll))
                    self.count += 1
        print(self.killAttempt)
        return all_rects
    def addingAllTheAnimys(self):
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
            # self.killAttempt = [None, None, 2, 2, None, ]
            for enimy in self.allEnimys:
                if(enimy.name == 'stone golem'):
                    self.killAttempt.append(1)
                elif(enimy.name == 'blue wizard'):
                    self.killAttempt.append(2)
                elif(enimy.name == 'cactus'):
                    self.killAttempt.append(None)

        elif (self.nivel == 1):
            self.allEnimys.append(Cactus(self.screen, (1088, 648)))
            self.allEnimys.append(Golens(self.screen, (1260, 184), 100))
            self.allEnimys.append(Golens(self.screen, (1404, 184), 100))
            self.allEnimys.append(Cactus(self.screen, (1578, 424)))
            self.allEnimys.append(Wizard(self.screen, (1716, 616), 100))
            self.allEnimys.append(Golens(self.screen, (1932, 616), 100))
            self.allEnimys.append(Golens(self.screen, (2120, 616), 100))
            self.allEnimys.append(Cactus(self.screen, (2240, 344)))
            self.allEnimys.append(Cactus(self.screen, (2288, 360)))
            self.allEnimys.append(Cactus(self.screen, (2340, 376)))
            self.allEnimys.append(Golens(self.screen, (2758, 616), 100))
            self.allEnimys.append(Cactus(self.screen, (2986, 408)))
            self.allEnimys.append(Golens(self.screen, (3282, 184), 100))
            self.allEnimys.append(Golens(self.screen, (3442, 184), 100))
            self.allEnimys.append(Cactus(self.screen, (3650, 136)))
            self.allEnimys.append(Golens(self.screen, (4178, 184), 100))
            self.allEnimys.append(Golens(self.screen, (4178, 104), 100))
            self.allEnimys.append(Golens(self.screen, (4846, 104), 100))

            self.positions = [(1088, 648), (1260, 184),(1404, 184), (1578, 424),(1716, 616),(1932, 616),(2120, 616),(2240, 344),(4846, 104)
                            ,(2288, 360),(2340, 376),(2758, 616),(2986, 408),(3282, 184),(3442, 184),(3650, 136),(4178, 184),(4178, 104)]

            for enimy in self.allEnimys:
                if(enimy.name == 'stone golem'):
                    self.killAttempt.append(1)
                elif(enimy.name == 'blue wizard'):
                    self.killAttempt.append(2)
                elif(enimy.name == 'cactus'):
                    self.killAttempt.append(None)

        elif (self.nivel == 2):
            self.allEnimys.append(Golens(self.screen, (876, 530), 100))
            self.allEnimys.append(Golens(self.screen, (1048, 530), 100))
            self.allEnimys.append(Golens(self.screen, (1156, 530), 100))
            self.allEnimys.append(Golens(self.screen, (1256, 530), 100))
            self.allEnimys.append(Golens(self.screen, (1856, 350), 100))
            self.allEnimys.append(Golens(self.screen, (3148, 50), 100))
            self.allEnimys.append(Golens(self.screen, (3604, 110), 100))
            self.allEnimys.append(Golens(self.screen, (3704, 110), 100))
            self.allEnimys.append(Golens(self.screen, (3848, 110), 100))
            self.allEnimys.append(Golens(self.screen, (5168, 560), 100))
            self.allEnimys.append(Golens(self.screen, (5240, 560), 100))

            self.positions = [(876, 530),(1048, 530),(1156, 530),(1256, 530),(1856, 350),(3148, 50), (3604, 110),(3704, 110),(3848, 110),(5168, 560),(5240, 560)]
            for enimy in self.allEnimys:
                if(enimy.name == 'stone golem'):
                    self.killAttempt.append(1)
                elif(enimy.name == 'blue wizard'):
                    self.killAttempt.append(2)
                elif(enimy.name == 'cactus'):
                    self.killAttempt.append(None)

        elif (self.nivel == 3):

            self.allEnimys.append(Cactus(self.screen, (716, 232)))
            self.allEnimys.append(Cactus(self.screen, (756, 232)))
            self.allEnimys.append(Cactus(self.screen, (788, 232)))
            self.allEnimys.append(Cactus(self.screen, (828, 232)))
            self.allEnimys.append(Cactus(self.screen, (942, 232)))
            self.allEnimys.append(Cactus(self.screen, (982, 232)))
            self.allEnimys.append(Cactus(self.screen, (1010, 232)))
            self.allEnimys.append(Cactus(self.screen, (1046, 232)))
            self.allEnimys.append(Cactus(self.screen, (1170, 232)))
            self.allEnimys.append(Cactus(self.screen, (1194, 232)))
            self.allEnimys.append(Cactus(self.screen, (1218, 232)))
            self.allEnimys.append(Cactus(self.screen, (1238, 232)))
            self.allEnimys.append(Cactus(self.screen, (1266, 232)))
            self.allEnimys.append(Cactus(self.screen, (1394, 232)))
            self.allEnimys.append(Cactus(self.screen, (1414, 232)))
            self.allEnimys.append(Cactus(self.screen, (1438, 232)))
            self.allEnimys.append(Cactus(self.screen, (1466, 232)))
            self.allEnimys.append(Cactus(self.screen, (1494, 232)))
            self.allEnimys.append(Cactus(self.screen, (1882, 232)))
            self.allEnimys.append(Cactus(self.screen, (1906, 232)))
            self.allEnimys.append(Cactus(self.screen, (1934, 232)))
            self.allEnimys.append(Wizard(self.screen, (1960, 536), 100))
            self.allEnimys.append(Wizard(self.screen, (2724, 280), 100))

            self.positions = [(716, 232),(756, 232),(788, 232),(828, 232),(942, 232),(982, 232),(1010, 232),(1046, 232),(1170, 232),
                        (1194, 232),(1218, 232),(1238, 232),(1266, 232),(1394, 232),(1414, 232),(1438, 232),(1466, 232),(1494, 232),
                        (1882, 232),(1906, 232),(1934, 232),(1960, 536),(2724, 280)]

            for enimy in self.allEnimys:
                if(enimy.name == 'stone golem'):
                    self.killAttempt.append(1)
                elif(enimy.name == 'blue wizard'):
                    self.killAttempt.append(2)
                elif(enimy.name == 'cactus'):
                    self.killAttempt.append(None)
            # self.positions = [(1448, 168),(1595, 168),(2718, 408),(2750, 296),(4014, 296),(4710, 584), (4870, 584)] 

    def calculatingEnimyDelete(self,fireColid, pos, scroll):
        onlyOne = False
        i = 0
        if(len(self.positions)!=0):
            for (position, enimy, attemp) in zip(self.positions, self.allEnimys, self.killAttempt):
                print(type(attemp))
                if(position[0] in range(scroll[0]-450, scroll[0]+650)):
                    if fireColid and not onlyOne:
                        if(self.allEnimys[pos].name != 'cactus'):
                            if(attemp == 0):
                                del self.allEnimys[pos]
                                del self.positions[pos]
                                del self.killAttempt[pos]
                            else:
                                attemp -= 1
                                self.killAttempt[i] = attemp
                        onlyOne = True           
                elif(position[0] < scroll[0]):
                    del self.allEnimys[0]
                    del self.positions[0]
            i += 1  