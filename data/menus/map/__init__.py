import pygame
from pygame.locals import *
from data.backgrounds import Backgound as Back

class Map(object):
    def __init__(self, screeen, nivel):
        self.screen = screeen
        self.nivel = nivel
        self.background = Back(screeen)
        self.map = pygame.image.load("resources/image/map/map.png")
        self.painel = pygame.image.load("resources/image/map/painel.png")
        self.golem = pygame.image.load("resources/image/map/Head.png")
        self.allPlayerLevelMapPosition = [(235, 123),(228, 220), (296, 225), (356, 192), (416, 159), (430, 220), (455, 263)]
        self.state = [False, False, False, False, False, False, False]
        self.limiteOfThePlayerViewInMap()
        self.font = pygame.font.SysFont("Arial", 14)
        self.font1 = pygame.font.SysFont("Arial", 24)
        self.font1.set_bold(True)
        self.maxPositionMap = self.nivel
        self.levelDescription = pygame.image.load("resources/image/map/Level/"+str(self.nivel)+"-"+str(self.state[self.nivel])+".png")
        self.effect = 0
        self.count = 0
        

    # Method to display the map in the screen
    def drawMapInTheScreen(self):
        self.background.settingBackgroundMenu(2)
        self.screen.blit(self.painel,(15, 17))
        self.screen.blit(self.map,(155, 60))
        self.screen.blit(self.levelDescription, (160, 315))
        title = self.font1.render("Map", True, (0, 0,0))
        self.screen.blit(title, (330,30))
        self.font.set_bold(True)
        if(self.effect == 15):
            self.effect = 0
        else:
            line = self.font.render("Press ESC to exit map", True, (0, 0,0))
            self.screen.blit(line, (275, 440))
            self.effect += 1
        self.screen.blit(self.golem, (self.allPlayerLevelMapPosition[self.nivel]))
        
        self.movementInMap()
        

    # Method to control the movemente in the map
    def movementInMap(self):
        key_press = pygame.key.get_pressed()
        
        if((key_press[K_RIGHT])and(self.nivel<6)and(self.count > 10)):
            self.nivel += 1
            self.levelDescription = pygame.image.load("resources/image/map/Level/"+str(self.nivel)+"-"+str(self.state[self.nivel])+".png")
            self.count = 0
        elif((key_press[K_LEFT])and(self.nivel>0)and(self.count > 10)):
            self.nivel -= 1
            self.levelDescription = pygame.image.load("resources/image/map/Level/"+str(self.nivel)+"-"+str(self.state[self.nivel])+".png")
            self.count = 0
        self.count += 1

    # Method to determinate the display level description on the map
    def limiteOfThePlayerViewInMap(self):
        count = 0
        for state in self.state:
            if (self.nivel >= count):
                self.state[count] = not state
            count += 1