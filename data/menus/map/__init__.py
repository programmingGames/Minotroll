import pygame
from pygame.locals import *

class Map(object):
    def __init__(self, screeen, nivel):
        self.screen = screeen
        self.nivel = nivel
        self.map = pygame.image.load("resources/image/map/map.png").convert_alpha()
        self.golem = pygame.image.load("resources/image/map/Head.png")
        self.levelDescription = pygame.image.load("resources/image/map/Level/1.png")
        self.progressPositions = []
        self.initialProgresplayer()
        self.nrPoints = len(self.progressPositions)
        self.indexPosition = 0
        # self.font = pygame.font.SysFont("Arial", 14)
        # self.font1 = pygame.font.SysFont("Arial", 24)
        # self.font1.set_bold(True)
        # self.maxPositionMap = self.nivel
        self.x, self.y = 0, 0
        self.effect = 0
        # self.count = 0

    # Method to display the map in the screen
    def drawMapInTheScreen(self):
        self.screen.blit(self.map,(700/2-473/2, 60))
        self.screen.blit(self.levelDescription, (700/2-150/2, 340))
        # title = self.font1.render("Map", True, (0, 0,0))
        # self.screen.blit(title, (330,30))
        # self.font.set_bold(True)
        if(self.indexPosition <= self.nrPoints):
            self.screen.blit(self.golem, (self.progressPositions[self.indexPosition-1]))
            # print(self.progressPositions[self.indexPosition-1])
        else:
            self.screen.blit(self.golem, (self.progressPositions[self.nrPoints-1]))
        # player_x=0
        # self.updateProgressInMap(500)

    # Method to update the map progress
    def updateProgressInMap(self, player_x):
        self.indexPosition = int((self.nrPoints * player_x)/self.pixelNr)
    
    # Method to determinate the display level description on the map
    def initialProgresplayer(self):
        if(self.nivel == 0):
            self.progressPositions = [(196, 148),(184, 176),(180, 192),(184, 204),(192, 224),(200, 232),(200,240),(202, 256)]
            self.pixelNr = 4960
        elif(self.nivel == 1):
            self.progressPositions = [(204, 256), (208, 272),(220, 292),(240, 292),(256, 280),(276, 276),(292, 268),(304, 260),(324, 252)]
            self.pixelNr = 4960
        elif(self.nivel == 2):
            self.pixelNr = 6260
            self.progressPositions = [(324, 252),(348, 232),(364, 220),(380, 208),(396, 200),(416, 200),(432, 200)]
        elif(self.nivel == 3):
            self.pixelNr = 3000
            self.progressPositions = [(432, 200),(444, 212),(444, 224),(440, 236),(436, 248),(436, 260),(452, 280)]