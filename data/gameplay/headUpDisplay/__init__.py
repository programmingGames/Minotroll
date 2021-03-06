import pygame
from pygame.locals import *
from data.gameplay.headUpDisplay.life import Life

# Class that ilustrate the H.U.D
class HeadUpDisplay(object):
    def __init__(self, screen, nivel, lastPassPoint, qtlife):
        self.screen = screen
        self.life = Life(self.screen, qtlife)
        self.lastPassPoint = lastPassPoint[0]
        self.qtlife = qtlife
        self.player = pygame.image.load("resources/image/headUpDisplay/conteiner/faceIcon.png")
        self.enimysBox = pygame.image.load("resources/image/headUpDisplay/attackinfo/enimys.png")
        self.greenFireBox = pygame.image.load("resources/image/headUpDisplay/attackinfo/greenFire.png")
        self.blueFireBox = pygame.image.load("resources/image/headUpDisplay/attackinfo/blueFire.png")
        self.avalableSkills = ["kicking", "slashing","battleax", "greenfire", "bluefire"]
        self.font = pygame.font.Font("resources/font/montserrat-font/MontserratMedium-nRxlJ.ttf", 18)
        self.font.set_bold(True)
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

    # Method to draw the HUD um the game screen
    def headUpDisplayScreenDraw(self, lastPassPoint, greenFire, blueFire, enimysKilled):
        self.greenFire, self.blueFire, self.enimysKilled = greenFire, blueFire, enimysKilled
        self.changeSkillsToUse()
        self.lastPassPoint = lastPassPoint
        self.screen.blit(self.player, (10, 10))
        self.qtlife = self.life.draw()
        self.displaySkillsCars()
        self.showHiddenSkilssOnGameEnvirement()
        self.showFireAndEnimysInfo()
        if(self.life.qtlife <= 0):
            return 11, self.qtlife, self.avalableSkills[self.inUse]
        else:
            return 7, self.qtlife, self.avalableSkills[self.inUse]
    
    # Method to show the player items info
    def showFireAndEnimysInfo(self):
        # enimys info
        if(len(str(self.enimysKilled))==2):
            eX = 12
        else:
            eX=15
        self.screen.blit(self.enimysBox, (5, 405))
        if self.enimysKilled < 10:
            line = self.font.render(str(self.enimysKilled), True, (255, 0,0))
        else:
            line = self.font.render(str(self.enimysKilled), True, (255, 255,255))
        self.screen.blit(line, (eX, 447))

        # draw green and blue fire info 
        if(len(str(self.greenFire))==2):
            gX = 11
        else:
            gX=14

        if(len(str(self.blueFire))==2):
            fX = 86
        else:
            fX=91
        if((self.skills == 4) or(self.skills == 5)):
            self.screen.blit(self.greenFireBox, (5, 329))
            line = self.font.render(str(self.greenFire), True, (0, 255, 14))
            self.screen.blit(line, (gX, 372))
            if(self.skills == 5):
                self.screen.blit(self.blueFireBox, (79, 405))
                line = self.font.render(str(self.blueFire), True, (0, 0, 255))
                self.screen.blit(line, (fX, 448))
    
    # Method to show the skills of the player on the screen
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

    # Method to hidde the skills on the screen
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

    # Method to control the show and hidde effect of the skills on the screen
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
            
    # Method to display to skills cards and show the one that is active
    def displaySkillsCars(self):
        x, y = 10, 85
        count = 0
        for (cardActive, cardDisable) in zip(self.cardsActive, self.cardsDisable):
            if(count == self.inUse):
                self.screen.blit(cardActive, (x, y))
            else:
                self.screen.blit(cardDisable, (x, y))
            count += 1
            x += 29
        
    # Method that control the skills that are going to be display acording to the level
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
    
    # Method to control the interetions in the H.U.D
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
        
        ## Verify the available green fires
        if((self.inUse == 3)and(self.greenFire<=0)or((self.inUse == 4)and (self.blueFire == 0))):
            self.inUse = 0

    # Method that update the player life
    def updatingPlayerLife(self,itemType):
        # print(enimyType)
        if(itemType == 'blue wizard'):
            self.life.updateLife(-3)
        elif(itemType == 'stone golem'):
            self.life.updateLife(-2)
        elif(itemType == 'fire golem'):
            self.life.updateLife(-2)
        elif(itemType == 'ice golem'):
            self.life.updateLife(-3)
        elif(itemType == "cactus"):
            self.life.updateLife(-6)
        elif(itemType == "life plant"):
            self.life.updateLife(80)
        elif(itemType == 'graveller'):
            self.life.updateLife(-5)
        elif(itemType == 'minotauro'):
            self.life.updateLife(-3)