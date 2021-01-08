import pygame
from pygame.display import update
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
        self.skillOfThePlayer()
        self.inUse = 0
        self.show = False
        self.count = 0
        self.allcards = []
        self.allpos = []
        self.y_Disable = 460
        self.y_Active = 455
        self.timeToHidde = 0

    # method to draw the HUD um the game screen
    def headUpDisplayScreenDraw(self, lastPassPoint):
        self.changeSkillsToUse()
        self.lastPassPoint = lastPassPoint
        self.screen.blit(self.player, (10, 10))
        self.life.draw()
        self.progress.draw(lastPassPoint)
        self.displaySkillsCars()
        self.showHiddenSkilssOnGameEnvirement()

        if(self.life.qtlife <= 0):
            return 11
        else:
            return 7
        # self.screen.blit(self.lifeBox, (50, 50))

    def showSkillsOnGameEnvirement(self):
        
        x1 = 700/2 - ((60*self.skills)/2)
        count = 0
        for (cardActive, cardDisable) in zip(self.hiddenCardsActive, self.hiddenCardsDisable):
            if(count == self.inUse):
                self.allcards.append(cardActive)
                self.allpos.append(((x1), self.y_Active))
            else:
                self.allcards.append(cardDisable)
                self.allpos.append(((x1), self.y_Disable))
            x1 += 60
            count +=1

    def hiddeSkillsOnGameEnvirement(self):

        x1 = 700/2 - ((60*self.skills)/2)
        count = 0
        for (cardActive, cardDisable) in zip(self.hiddenCardsActive, self.hiddenCardsDisable):
            if(count == self.inUse):
                self.allcards.append(cardActive)
                self.allpos.append(((x1), self.y_Active))
            else:
                self.allcards.append(cardDisable)
                self.allpos.append(((x1), self.y_Disable))
            x1 += 60
            count += 1

    def showHiddenSkilssOnGameEnvirement(self):
        self.allcards = []
        self.allpos = []
        if(self.show):
            self.showSkillsOnGameEnvirement()
            
            [self.screen.blit(card, pos) for (card, pos) in zip(self.allcards, self.allpos)]
            if((self.y_Active >= 360)and(self.y_Disable >= 387)):
                self.y_Active -= 2
                self.y_Disable -= 2
            self.timeToHidde += 1
        else:
            self.hiddeSkillsOnGameEnvirement()
            [self.screen.blit(card, pos) for (card, pos) in zip(self.allcards, self.allpos)]
            if((self.y_Active <= 470)and(self.y_Disable <= 455)):
                self.y_Active += 2
                self.y_Disable += 2
        if(self.timeToHidde > 90):
            self.show = not self.show
            self.timeToHidde = 0
            

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
        

    def skillOfThePlayer(self):
        if (self.nivel == 0):
            self.skills = 2

        elif(self.nivel == 1):
            self.skills = 4

        elif(self.nivel >= 2):
            self.skills = 5

        self.cardsActive = [pygame.image.load("resources/image/headUpDisplay/cardIcon/"+str(i)+"-True.png")for i in range(self.skills)]
        self.cardsDisable = [pygame.image.load("resources/image/headUpDisplay/cardIcon/"+str(i)+"-False.png")for i in range(self.skills)]
        self.hiddenCardsActive = [pygame.image.load("resources/image/headUpDisplay/card/"+str(i)+"-True.png")for i in range(self.skills)]
        self.hiddenCardsDisable = [pygame.image.load("resources/image/headUpDisplay/card/"+str(i)+"-False.png")for i in range(self.skills)]
    
    def changeSkillsToUse(self):
        key_press = pygame.key.get_pressed()
        

        # controls to hidde in show the skills cards
        if(key_press[K_TAB] and (self.count >= 10)):
            self.show = not self.show
            self.count = 0
        self.count += 1
        
        if(self.show):
            if(key_press[K_1]and (self.count >= 10)):
                self.inUse = 0
                self.count = 0
            elif(key_press[K_2]and (self.count >= 10)):
                self.inUse = 1
                self.count = 0
            elif(key_press[K_3]and (self.count >= 10)):
                self.inUse = 2
                self.count = 0
            elif(key_press[K_4]and (self.count >= 10)):
                self.inUse = 3
                self.count = 0
            elif(key_press[K_5]and (self.count >= 10)):
                self.inUse = 4
                self.count = 0

        # verification if the skills is available and reselect
        if(self.inUse > self.skills - 1):
            self.inUse = 0
    def updatingPlayerLife(self,itemType):
        # print(enimyType)
        if(itemType == 'blue wizard'):
            self.life.updateLife(-1)
        elif(itemType == 'stone golem'):
            self.life.updateLife(-1)
        elif(itemType == "cactus"):
            self.life.updateLife(-10)
        elif(itemType == 'brown minotaur'):
            self.life.updateLife(-1)
        elif(itemType == "life plant"):
            self.life.updateLife(20)