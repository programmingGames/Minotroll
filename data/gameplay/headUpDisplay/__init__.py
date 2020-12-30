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
        self.skillOfThePlayer()
        self.inUse = 0
        self.show = False
        self.count = 0
        self.allcards = []
        self.allpos = []
        self.y_Disable = 460
        self.y_Active = 445
        self.timeToHidde = 0

    # method to draw the HUD um the game screen
    def headUpDisplayScreenDraw(self, lastPassPoint):
        self.lastPassPoint = lastPassPoint
        self.screen.blit(self.player, (10, 10))
        self.life.draw()
        self.progress.draw(lastPassPoint)
        self.displaySkillsCars()
        self.showHiddenSkilssOnGameEnvirement()
        # self.screen.blit(self.lifeBox, (50, 50))

    def showSkillsOnGameEnvirement(self):
        self.allcards = []
        self.allpos = []
        x1 = 700/2 - ((50+(40*self.nivel))/2)
        x2 = (550/2 + ((50+(40*self.nivel))/2))
        count = 0
        control = 0
        midle = int(len(self.cardsActive)/2)
        for (cardActive, cardDisable) in zip(self.hiddenCardsActive, self.hiddenCardsDisable):
            if(count == self.inUse):
                midlecard = cardActive
            elif(count != self.inUse):
                if (control < midle):
                    self.allcards.append(cardDisable)
                    self.allpos.append((x1, self.y_Disable))
                    x1 += 30
                elif(control >= midle):
                    self.allcards.append(cardDisable)
                    self.allpos.append((x2, self.y_Disable))
                    x2 -= 30
                control += 1
            count += 1
            
        self.allcards.append(midlecard)
        self.allpos.append(((700/2 - 100/2), self.y_Active))

    def hiddeSkillsOnGameEnvirement(self):
        self.allcards = []
        self.allpos = []
        x1 = 700/2 - ((50+(40*self.nivel))/2)
        x2 = (550/2 + ((50+(40*self.nivel))/2))
        count = 0
        control = 0
        midle = int(len(self.cardsActive)/2)
        for (cardActive, cardDisable) in zip(self.hiddenCardsActive, self.hiddenCardsDisable):
            if(count == self.inUse):
                midlecard = cardActive
            elif(count != self.inUse):
                if (control < midle):
                    self.allcards.append(cardDisable)
                    self.allpos.append((x1, self.y_Disable))
                    x1 += 30
                elif(control >= midle):
                    self.allcards.append(cardDisable)
                    self.allpos.append((x2, self.y_Disable))
                    x2 -= 30
                control += 1
            count += 1
        self.allcards.append(midlecard)
        self.allpos.append(((700/2 - 100/2), self.y_Active))

    def showHiddenSkilssOnGameEnvirement(self):
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
        self.changeSkillsToUse()
        

    def skillOfThePlayer(self):
        if (self.nivel == 1):
            self.maxskills = self.nivel + 1
            self.nivel = 2
        else:
            self.maxskills = self.nivel
        self.cardsActive = [pygame.image.load("resources/image/headUpDisplay/cardIcon/"+str(i)+"-True.png")for i in range(self.nivel+1)]
        self.cardsDisable = [pygame.image.load("resources/image/headUpDisplay/cardIcon/"+str(i)+"-False.png")for i in range(self.nivel+1)]
        self.hiddenCardsActive = [pygame.image.load("resources/image/headUpDisplay/card/"+str(i)+"-True.png")for i in range(self.nivel+1)]
        self.hiddenCardsDisable = [pygame.image.load("resources/image/headUpDisplay/card/"+str(i)+"-False.png")for i in range(self.nivel+1)]
    
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

        # controls to hidde in show the skills cards
        if(key_press[K_TAB] and (self.count >= 10)):
            self.show = not self.show
            self.count = 0
        self.count += 1

        # verification if the skills is available and reselect
        if(self.inUse > self.maxskills):
            self.inUse = self.maxskills
    def damagingPlayerLife(self,enimyType):
        if(enimyType == 'blue wizard'):
            self.life.damageLife(1)
        # if(key_press[K_x]):
            
        # if(key_press[K_c]):
        #     self.life.incrementLife(1)
        
        