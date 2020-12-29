import pygame
from pygame.locals import *
from data.gameplay.headUpDisplay.life import Life
from data.gameplay.headUpDisplay.progress import LevelProgress

class HeadUpDisplay(object):
    def __init__(self, screen, nivel, lastPassPoint, qtlife):
        self.screen = screen
        self.life = Life(self.screen, qtlife)
        self.lastPassPoint = lastPassPoint
        # self.qtlife = qtlife
        self.progress = LevelProgress(self.screen, self.lastPassPoint)
        self.player = pygame.image.load("resources/image/headUpDisplay/conteiner/faceIcon.png")
        self.nivel = nivel
        # self.lifeBox = pygame.image.load("resources/image/headUpDisplay/lifebox1.png")
        self.skillOfThePlayer()
        self.inUse = 0

    # method to draw the HUD um the game screen
    def headUpDisplayScreenDraw(self, lastPassPoint):
        self.lastPassPoint = lastPassPoint
        self.screen.blit(self.player, (10, 10))
        self.life.draw()
        self.progress.draw(lastPassPoint)
        
        self.displaySkillsCars()
        # self.screen.blit(self.lifeBox, (50, 50))

    def displaySkillsCars(self):
        x, y = 10, 98
        count = 0
        for (cardActive, cardDisable) in zip(self.cardsActive, self.cardsDisable):
            if(count == self.inUse):
                self.screen.blit(cardActive, (x, y))
            else:
                self.screen.blit(cardDisable, (x, y))
            count += 1
            x += 29
        self.changeSkillsToUse()
        

    def skillOfThePlayer(self):
        if (self.nivel == 1):
            self.maxskills = self.nivel + 1
            self.nivel = 2
        else:
            self.maxskills = self.nivel
        self.cardsActive = [pygame.image.load("resources/image/headUpDisplay/cardIcon/"+str(i)+"-True.png")for i in range(self.nivel+1)]
        self.cardsDisable = [pygame.image.load("resources/image/headUpDisplay/cardIcon/"+str(i)+"-False.png")for i in range(self.nivel+1)]
    
    def changeSkillsToUse(self):

        key_press = pygame.key.get_pressed()
        if(key_press[K_1]):
            self.inUse = 0
        elif(key_press[K_2]):
            self.inUse = 1
        elif(key_press[K_3]):
            self.inUse = 2
        elif(key_press[K_4]):
            self.inUse = 3
        elif(key_press[K_5]):
            self.inUse = 4
        elif(key_press[K_6]):
            self.inUse = 5
        elif(key_press[K_7]):
            self.inUse = 6

        # test
        if(key_press[K_x]):
            self.life.damageLife(1)

        # verification if the skills is available and reselect
        if(self.inUse > self.maxskills):
            self.inUse = self.maxskills
